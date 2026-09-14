---
title: 3 Sample ACF
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwenty153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Sample ACF

**Source:** [`LectureTwenty153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We have so far defined the ACF _ρ_ ( _h_ ) for a stationary time series model as the correlation between _yt_ and _yt_ + _h_ . Given a time series dataset _y_ 1 _, . . . , yn_ , we can define a sample autocorrelation function that can be seen as an estimate of the ACF of a time series model that is assumed for the data.

For a fixed value of _h_ , the sample acf at lag _h_ is essentially defined as the correlation coefficient between ( _at, bt_ ) _, t_ = 1 _, . . . , n − h_ where _at_ = _yt_ and _bt_ = _yt_ + _h_ . This correlation coefficient is given by:


where


This correlation can be simplified slightly by making the following approximations:


which are reasonable when _h_ is very small compared to _n_ . Making these approximations lead to the following definition of the sample ACF:


Note that _r_ 0 is always equal to 1.

The sample ACF _rh, h ≥_ 0 can be computed for any time series dataset, although it is only useful for data for which stationary models are appropriate.

The sample ACF is particularly useful for determining the order _q_ for fitting an MA( _q_ ) model. For an MA( _q_ ) model, we have seen in the previous section that the theoretical ACF _ρ_ ( _h_ ) becomes exactly zero when _h > q_ . This suggests that if the sample ACF _rh_ for a particular dataset becomes small (not exactly zero because of randomness) when _h_ exceeds a particular _q_ , then MA( _q_ ) is probably a good model for that dataset. This diagnostic is very commonly used when working with MA models.

4

---

[← 2 Moving Average (MA) Models](02-2-moving-average-ma-models.md) · [Up: contents](index.md) · [4 Sample PACF →](04-4-sample-pacf.md)
