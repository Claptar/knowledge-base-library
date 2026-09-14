---
title: 4 Sample PACF
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwenty153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Sample PACF

**Source:** [`LectureTwenty153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As discussed above, the sample ACF is a useful diagnostic for determining the order of _q_ for an MA( _q_ ) model given data. There exists a similar diagnostic called sample PACF (PACF stands for Partial AutoCorrelation Function) which is useful for determining the order of _p_ for an AR( _p_ ) model.

The sample PACF is defined as follows: for _h ≥_ 1,

sample PACF( _h_ ) = estimate _ϕ_<sup>ˆ</sup> _h_ of _ϕh_ when AR( _h_ ) is fit to the data

If the sample PACF( _h_ ) becomes negligibly small after a particular _p_ , this suggests that AR( _p_ ) is a good model for the data. This method is similar to the heuristic technique that we used in last lecture and Lab 10 for selecting the order _p_ to fit AR( _p_ ). There we were looking at the uncertainty interval for _ϕp_ to see if it contains zero when AR( _p_ ) is fit to the data. This is the same as checking whether the sample PACF(h) is small at _h_ = _p_ .

It can happen (we will see examples of this later) that the sample PACF(h) for _h_ = 1 _,_ 2 _, . . . ,_ 11 are all negligible but at _h_ = 12, it is nonnegligible. In that case, we would be using AR(12). More specifically, we will use that value of _p_ for which sample PACF( _h_ ) is negligible for all _h > p_ . The same is true for sample ACF and MA( _q_ ).

---

[← 3 Sample ACF](03-3-sample-acf.md) · [Up: contents](index.md) · [5 Why is this called “Partial” Autocorrelation? →](05-5-why-is-this-called-partial-autocorrelation.md)
