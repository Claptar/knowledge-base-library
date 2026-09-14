---
title: 'Topic Seven: Neural Networks'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureOneSlides153248Fall2026PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Topic Seven: Neural Networks

**Source:** [`LectureOneSlides153248Fall2026PDF.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureOneSlides153248Fall2026PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- <sup>AR models are simply linear regression of  on</sup> _yt_

- lagged covariates _xt_ := (1, _yt_ −1, …, _yt_ − _p_ )

- •<sup>It is natural to use nonlinear regression of  on</sup> _yt_

- for improved predictive power

- _xt_

- We perform this nonlinear regression using single hidden-layer neural networks

• These is Nonlinear AutoRegression which fits functions _yt_ = _f_ ( _xt_ ) = _f_ ( _yt_ −1, …, _yt_ − _p_ )

---

[← Topic Six: Vector Time Series](10-topic-six-vector-time-series.md) · [Up: contents](index.md) · [Topic Seven: Neural Networks →](12-topic-seven-neural-networks.md)
