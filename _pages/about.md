---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# Xiucheng Wang (王秀程)

**PhD Student** · School of Telecommunication Engineering, Xidian University. 

Advised by [Prof. Xuemin (Sherman) Shen](https://uwaterloo.ca/scholar/sshen) and [Prof. Nan Cheng](https://scholar.google.com/citations?user=Cxm51twAAAAJ&hl=en&oi=ao)

**Google Scholar Citations:** <span id="total_cit">loading...</span>

[![中国科协青托](https://img.shields.io/badge/中国科协-青托博士生专项-red?style=flat-square)](https://www.cast.org.cn/)
![Presidential Award](https://img.shields.io/badge/🏆-Presidential%20Award%20of%20XDU-gold?style=flat-square)
![Best Paper](https://img.shields.io/badge/🏅-IEEE%20ICC%20Best%20Paper-blue?style=flat-square)


---

## 🔬 Research Interests

`Radio Map` &nbsp; `EM Ray Tracing` &nbsp; `Diffusion Model` &nbsp; `Graph Neural Network` &nbsp; `Learn to Optimize`

---

## 📰 News

- 🎉 **2025** &nbsp; 西安电子科技大学承楠教授团队突破电磁空间孪生认知大模型技术 → [**新华社·强国科技**](https://h.xinhuaxmt.com/vh512/share/12678291?docid=12678291&newstype=1001&d=13500b7)
- 📡 **2025** &nbsp; 面向6G环境感知通信！西电开源3D×3D无线电地图数据集与生成式基准框架 → [**新智元**](https://mp.weixin.qq.com/s/EW9u_72wduBkxnJEDuUB7w)
- 📻 **2025** &nbsp; "首次理论分析，「无线电地图构建」竟是生成问题？西电全新模型，性能全面领先" → [**新智元**](https://mp.weixin.qq.com/s/3Yc911BY6vbbWIQckhOvrA?scene=25)

---

## 🖊️ Tutorial Paper

**`Xiucheng Wang`**, Yuhao Pan, Nan Cheng.
**A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awareness**.
[arXiv 2026](https://arxiv.org/abs/2603.17499)

---

## 📝 Publications

### English

<details open markdown="1">
<summary><b>📡 Radio Map Construction</b></summary>


| Paper | Venue | Links | Notes |
|:------|:------|:------|:------|
| **`Xiucheng Wang`** et al. **RadioDiff-k<sup>2</sup>: Helmholtz Equation Informed Generative Diffusion Model for Multi-Path Aware Radio Map Construction** | ![JSAC](https://img.shields.io/badge/IEEE-JSAC%202025-005BAC?style=flat-square) | [📄 Paper](https://ieeexplore.ieee.org/document/11278649) · [💻 Code](https://github.com/UNIC-Lab/RadioDiff-k) | ⭐ 中科院一区 · 🏆 CCF-A |
| **`Xiucheng Wang`** et al. **RadioDiff: An Effective Generative Diffusion Model for Sampling-Free Dynamic Radio Map Construction** | ![TCCN](https://img.shields.io/badge/IEEE-TCCN%202025-005BAC?style=flat-square) | [📄 Paper](https://ieeexplore.ieee.org/abstract/document/10764739) · [💻 Code](https://github.com/UNIC-Lab/RadioDiff) | ⭐ 中科院一区 · 🏆 ESI Highly Cited · IEEE Popular Paper |
| **`Xiucheng Wang`** et al. **RadioDiff-3D: A 3D × 3D Radio Map Dataset and Generative Diffusion Based Benchmark for 6G Environment-Aware Communication** | ![TNSE](https://img.shields.io/badge/IEEE-TNSE%202025-005BAC?style=flat-square) | [📄 Paper](https://ieeexplore.ieee.org/document/11083758) · [💻 Code](https://github.com/UNIC-Lab/UrbanRadio3D) | ⭐ 中科院二区 · 🏆 TNSE Feature Paper · IEEE Popular Paper |
| **`Xiucheng Wang`** et al. **RadioDiff-Inverse: Diffusion Enhanced Bayesian Inverse Estimation for ISAC Radio Map Construction** | ![TWC](https://img.shields.io/badge/IEEE-TWC%202026-005BAC?style=flat-square) | [📄 Paper](https://arxiv.org/abs/2504.14298) · [💻 Code](https://github.com/UNIC-Lab/radiodiff-inverse) | ⭐ 中科院一区 · 🏆 CCF-A |
| **`Xiucheng Wang`** et al. **iRadioDiff: Physics-Informed Diffusion Model for Indoor Radio Map Construction and Localization** | ![ICC](https://img.shields.io/badge/IEEE-ICC%202026-005BAC?style=flat-square) | [📄 Paper](https://arxiv.org/abs/2511.20015) · [💻 Code](https://github.com/UNIC-Lab/iRadioDiff) | 🏆 **Best Paper Award** · ⭐ IEEE ComSoc Flagship |
| **`Xiucheng Wang`** et al. **RadioDiff-Flux: Efficient Radio Map Construction via Generative Denoise Diffusion Model Trajectory Midpoint Reuse** | ![TCCN](https://img.shields.io/badge/IEEE-TCCN%202025-005BAC?style=flat-square) | [📄 Paper](https://ieeexplore.ieee.org/document/11282987) | ⭐ 中科院一区 |
| **`Xiucheng Wang`** et al. **RadioDiff-Turbo: Lightweight Generative Large Electromagnetic Model for Wireless Digital Twin Construction** | ![INFOCOM](https://img.shields.io/badge/IEEE-INFOCOM%20Wksp%202025-6C757D?style=flat-square) | [📄 Paper](https://ieeexplore.ieee.org/abstract/document/11152929/) | 🏆 CCF-A |
| **`Xiucheng Wang`** et al. **RadioDiff-FS: Physics-Informed Manifold Alignment in Few-Shot Diffusion Models for High-Fidelity Radio Map Construction** | ![arXiv](https://img.shields.io/badge/arXiv-2026-B31B1B?style=flat-square) | [📄 Paper](https://arxiv.org/abs/2603.18865) · [💻 Code](https://github.com/UNIC-Lab/RadioDiff-FS) | |
| **`Xiucheng Wang`** et al. **Beam-Aware Radio Map Estimation With Physics-Consistent Parametric Modeling for Unknown Multiple Satellites** | ![arXiv](https://img.shields.io/badge/arXiv-2026-B31B1B?style=flat-square) | [📄 Paper](https://arxiv.org/abs/2605.07763) | |
| **`Xiucheng Wang`** et al. **RadioDiff-Loc: Diffusion Model Enhanced Scattering Cognition for NLoS Localization with Sparse Radio Map Estimation** | ![arXiv](https://img.shields.io/badge/arXiv-2025-B31B1B?style=flat-square) | [📄 Paper](https://www.arxiv.org/abs/2509.01875) | |

</details>

<details open markdown="1">
<summary><b>🌐 Network Optimization</b></summary>


| Paper | Venue | Links | Notes |
|:------|:------|:------|:------|
| **`Xiucheng Wang`** et al. **Graph Neural Network-Based Multicast Routing for On-Demand Streaming Services in 6G Networks** | ![TMC](https://img.shields.io/badge/IEEE-TMC%202025-005BAC?style=flat-square) | [📄 Paper](https://ieeexplore.ieee.org/abstract/document/11260947) · [💻 Code](https://github.com/UNIC-Lab/GNN-Routing) | ⭐ 中科院一区 · 🏆 CCF-A |
| **`Xiucheng Wang`** et al. **Joint Flying Relay Location and Routing Optimization for 6G UAV–IoT Networks: A Graph Neural Network-Based Approach** | ![RS](https://img.shields.io/badge/MDPI-Remote%20Sensing%202022-4CAF50?style=flat-square) | [📄 Paper](https://www.mdpi.com/2072-4292/14/17/4377) · [💻 Code](https://github.com/UNIC-Lab/LGNN-RGNN) | ⭐ 中科院二区 |

</details>

### Chinese

| Paper | Venue |
|:------|:------|
| 承楠, **王秀程**, 沈学民. **基于生成式模型的新型机器语义通信方法研究** | [中兴通讯技术, 2025](https://kns.cnki.net/kcms2/article/abstract?v=liLFU49ICVs8P0YCg2w_YZYYW9AEXmUawPZCsln3_jBxJ_F7Z8qybYc9D1dbo2zLGkfttc1sRl_jEQeU7G6MHEMJRjDwSwZugMWwQq-4rfMM1k9JmyIq3lXxzWKR4kN-obNssNzsVsZQhU9hOyIw5-xxync0r3R9vXPT9KoTZmOOk9Dy4dV3sQ==&uniplatform=NZKPT&language=CHS) |

---

## 🎖️ Honors & Awards

| Year | Award |
|:-----|:------|
| 2026 | 🏅 **IEEE ICC Best Paper Award** (IEEE ComSoc Flagship) |
| 2026 | 🏅 **ACM WWW 2026 Workshop Best Student Paper Award** |
| 2025 | 🏅 **IEEE WCSP Best Paper Award** |
| 2025 | 🏅 **IEEE ICCT Best Paper Award** |
| 2025 | 🏆 **National Scholarship** |
| 2025 | 🏆 **Presidential Award**, Xidian University |
| 2025 | 🌟 中国科协"青托"博士生专项 |
| 2023 | 💰 Fundamental Research Funds for Central Universities · Innovation Fund of XDU (YJSJ23012) |
| 2022 | 🏆 **National Scholarship** |

---

## 🎓 Academic Services

**Technical Program Committee (TPC) Member**

- IEEE ICC &nbsp; 2024 · 2025 · 2026
- IEEE GlobeCom &nbsp; 2025 · 2026
- IEEE ICCC &nbsp; 2025

---
