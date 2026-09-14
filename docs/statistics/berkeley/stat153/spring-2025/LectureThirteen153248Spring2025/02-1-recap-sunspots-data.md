---
title: '1 Recap: Sunspots Data'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThirteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureThirteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Recap: Sunspots Data

**Source:** [`LectureThirteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThirteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In order to motivate the model that we shall study today, consider the annual sunspots dataset _yt_ that we previously looked at multiple times in this class.

Previously (e.g., Lecture 8), we used the following models for the sunspots data:


_yt_ = _β_ 0+ _β_ 1 cos(2 _πf_ 1 _t_ )+ _β_ 2 sin(2 _πf_ 1 _t_ )+ _β_ 3 cos(2 _πf_ 2 _t_ )+ _β_ 4 sin(2 _πf_ 2 _t_ )+ _β_ 5 cos(2 _πf_ 3 _t_ )+ _β_ 6 sin(2 _πf_ 3 _t_ )+ _ϵt_

(3)

In all these models, _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). _f, f_ 1 _, f_ 2 _, f_ 3 represent unknown frequency parameters. These models are helpful for understanding certain aspects of the sunspots data. For example, model (1), when fitted to the data, gave _f ≈_ 1 _/_ 11 which corresponds to the solar cycle. Models (2) and (3) can give reasonable forecasts of the number of sunspots in future years.

In spite of these utilties, these models do not capture many important characteristics of the sunspots dataset. For example, if we generate simulated data _y_ 1<sup>simulated</sup> _, . . . , yn_<sup>simulated</sup> from any of these models (with the parameters _β_ ’s, _f_ ’s and _σ_ fixed at the estimates obtained from the sunspots data), these simulated datasets visually look quite different from the actual sunspots data. The sunspots dataset will have well-defined peaks and the gaps between the peaks varies (roughly around 11) from one cycle to another. The simulated datasets will not have such clear peaks.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 High-dimensional Regression with Sinusoids →](03-2-high-dimensional-regression-with-sinusoids.md)
