---
title: 6 Determination of the order p of AR( p )
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Determination of the order p of AR( p )

**Source:** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

How to determine the correct order _p_ for fitting the AR( _p_ ) model? For this, one commonly uses a quantity called the sample PACF (PACF stands for Partial AutoCorrelation Function).

The sample PACF is defined as follows: for _h ≥_ 1,

sample PACF( _h_ ) = estimate _φ_<sup>ˆ</sup> _h_ of _φh_ when AR( _h_ ) is fit to the data

If the sample PACF( _h_ ) becomes negligibly small after a particular _p_ , this suggests that AR( _p_ ) is a good model for the data. This method is similar to the heuristic technique that we used in Lab 9 for selecting the order _p_ to fit AR( _p_ ). There we were looking at the uncertainty interval for _φp_ to see if it contains zero when AR( _p_ ) is fit to the data. This is the same as checking whether the sample PACF(h) is small at _h_ = _p_ .

8

It can happen (we will see examples of this later) that the sample PACF(h) for _h_ = 1 _,_ 2 _, . . . ,_ 11 are all negligible but at _h_ = 12, it is nonnegligible. In that case, we would be using AR(12). More specifically, we will use that value of _p_ for which sample PACF( _h_ ) is negligible for all _h > p_ .

Why should the quantity _φ_<sup>ˆ</sup> _h_ (obtained by fitting AR( _h_ ) to the data) be called the Sample Partial Autocorrelation? We will understand this in the next lecture.

9

---

[← 5 AR( p ) for p ≥ 1](06-5-ar-p-for-p-1.md) · [Up: contents](index.md)
