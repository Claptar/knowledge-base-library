---
title: Time Series Regression
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureOneSlides153248Spring2025PDF.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Time Series Regression

**Source:** [`LectureOneSlides153248Spring2025PDF.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureOneSlides153248Spring2025PDF.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• where each  is vector( _x_ 1, _y_ 1), …, ( _xT_ , _yT_ ) _xt_ valued and  is real-valued _yt_

• For each time point , we observe a covariate _t_ vector  as well as a response value _xt yt_ •<sup>The goal is to predict</sup> given and the _yT_ +1 _xT_ +1 current data set (and then given etc.) _yT_ +2 _xT_ +2 • This is a more general setting compared to both regression over time ( _xt_ = _t_ ) and lagged regression ( ) _xt_ = ( _yt_ −1, _yt_ −2, …, _yt_ − _p_ )

• We shall study RNNs in this setting

---

[← Vector Time Series](09-vector-time-series.md) · [Up: contents](index.md) · [Sequential Data →](11-sequential-data.md)
