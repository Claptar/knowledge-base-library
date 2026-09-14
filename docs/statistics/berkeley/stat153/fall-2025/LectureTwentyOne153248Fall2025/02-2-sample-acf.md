---
title: 2 Sample ACF
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyOne153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Sample ACF

**Source:** [`LectureTwentyOne153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyOne153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For a fixed value of _h_ , the correlation coefficient between ( _at, bt_ ) _, t_ = 1 _, . . . , n − h_ where _at_ = _yt_ and _bt_ = _yt_ + _h_ is given by:

where


This correlation can be simplified slightly by making the following approximations:


which are reasonable when _h_ is very small compared to _n_ . Making these approximations lead to the following definition of the sample ACF:


Note that _r_ 0 is always equal to 1.

The sample ACF _rh, h ≥_ 0 can be computed for any time series dataset, although it is only useful for data for which stationary models are appropriate.

The sample ACF is particularly useful for determining the order _q_ for fitting an MA( _q_ ) model. For an MA( _q_ ) model, we have seen in the previous section that the theoretical ACF _ρ_ ( _h_ ) becomes exactly zero when _h > q_ . This suggests that if the sample ACF _rh_ for a particular dataset becomes small (not exactly zero because of randomness) when _h_ exceeds a particular _q_ , then MA( _q_ ) is probably a good model for that dataset. This diagnostic is very commonly used when working with MA models.

---

[← 1 MA( q ) models](01-1-ma-q-models.md) · [Up: contents](index.md) · [3 On Parameter Estimation in MA( q ) →](03-3-on-parameter-estimation-in-ma-q.md)
