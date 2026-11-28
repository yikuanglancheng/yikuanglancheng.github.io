import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit
from urllib.request import urlopen

from bs4 import BeautifulSoup
from scholarly.author_parser import AuthorParser


class ScholarUnavailable(Exception):
    """Scholar temporarily did not serve the public profile."""


class ProfilePages:
    """Supply the pinned scholarly parser with checked, single-attempt pages."""

    def __init__(self, scholar_id):
        self.scholar_id = scholar_id
        self.seen_publications = set()

    def _get_soup(self, path):
        url = "https://scholar.google.com.hk" + path
        try:
            with urlopen(url, timeout=30) as response:
                soup = BeautifulSoup(response.read(), "html.parser")
        except HTTPError as exc:
            if exc.code in (403, 408, 429) or 500 <= exc.code < 600:
                raise ScholarUnavailable(f"Google Scholar returned HTTP {exc.code}") from exc
            raise
        except (TimeoutError, URLError) as exc:
            raise ScholarUnavailable(f"Google Scholar connection failed ({exc})") from exc

        if not soup.select_one("#gsc_prf_in") and not soup.select_one("#gsc_a_b"):
            raise ScholarUnavailable("Google Scholar returned a non-profile page")

        links = soup.select("#gsc_a_b a.gsc_a_at[href]")
        if not links or not soup.select_one("#gsc_bpf_more"):
            raise ValueError("Incomplete Google Scholar publication list")
        for link in links:
            query = parse_qs(urlsplit(link["href"]).query)
            pub_id = query.get("citation_for_view", [""])[0]
            if not pub_id.startswith(self.scholar_id + ":") or pub_id in self.seen_publications:
                raise ValueError(f"Unexpected or repeated Scholar publication ID: {pub_id!r}")
            self.seen_publications.add(pub_id)

        canonical = soup.find("link", rel="canonical")
        if canonical is None:
            # Some profile pages omit this tag. The publication links above
            # independently identify the author; scholarly requires the tag.
            soup.append(soup.new_tag("link", rel="canonical", href=url))
        elif parse_qs(urlsplit(canonical["href"]).query).get("user") != [self.scholar_id]:
            raise ValueError("Google Scholar returned a different author profile")
        return soup


def fetch_author(scholar_id):
    parser = AuthorParser(ProfilePages(scholar_id))
    author = parser.get_author(scholar_id)
    parser.fill(author, sections=["basics", "indices", "counts", "publications"])
    author["publications"] = {pub["author_pub_id"]: pub for pub in author["publications"]}
    author["updated"] = datetime.now(timezone.utc).isoformat(sep=" ")
    return author


def citation_badge(author):
    return {"schemaVersion": 1, "label": "citations", "message": str(author["citedby"])}


def validate_author(author, scholar_id):
    if author["scholar_id"] != scholar_id or not author["name"]:
        raise ValueError("Invalid Scholar author")
    if type(author["citedby"]) is not int or author["citedby"] < 0:
        raise ValueError("Invalid total citation count")
    if not author["publications"]:
        raise ValueError("Missing Scholar publications")
    for pub_id, pub in author["publications"].items():
        if pub_id != pub["author_pub_id"] or not pub_id.startswith(scholar_id + ":"):
            raise ValueError(f"Invalid publication ID: {pub_id!r}")
        if type(pub["num_citations"]) is not int or pub["num_citations"] < 0:
            raise ValueError(f"Invalid citation count for {pub_id}")
    datetime.fromisoformat(author["updated"])


def refresh(scholar_id, output_dir):
    data_path = output_dir / "gs_data.json"
    badge_path = output_dir / "gs_data_shieldsio.json"
    try:
        author = fetch_author(scholar_id)
    except ScholarUnavailable as exc:
        # Only treat an upstream outage as recoverable when both published
        # files are usable. Keep their contents and original timestamp.
        cached = json.loads(data_path.read_text(encoding="utf-8"))
        validate_author(cached, scholar_id)
        if json.loads(badge_path.read_text(encoding="utf-8")) != citation_badge(cached):
            raise ValueError("Published citation badge does not match the saved profile")
        message = f"{exc}. Kept {cached['citedby']} citations from {cached['updated']}."
        print(f"::warning::{message}")
        return message

    validate_author(author, scholar_id)
    output_dir.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(author, ensure_ascii=False), encoding="utf-8")
    badge_path.write_text(json.dumps(citation_badge(author)), encoding="utf-8")
    message = f"Fetched {author['citedby']} citations across {len(author['publications'])} publications."
    print(message)
    return message


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--output-dir", type=Path, default=Path("results"))
    message = refresh(os.environ["GOOGLE_SCHOLAR_ID"], args.parse_args().output_dir)
    if "GITHUB_STEP_SUMMARY" in os.environ:
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
            print(message, file=summary)
