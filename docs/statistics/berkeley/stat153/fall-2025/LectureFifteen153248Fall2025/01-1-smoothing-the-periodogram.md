---
title: 1 Smoothing the Periodogram
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Smoothing the Periodogram

**Source:** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider a time series dataset _y_ 0 _, . . . , yn−_ 1. One of most common tools in time data analysis is the periodogram. It is given by:


where _bj_ is the Discrete Fourier Transform (DFT) defined by


Let us assume that _n_ is odd and _m_ = ( _n −_ 1) _/_ 2. Then the periodogram ordinate is defined for _j_ = 1 _, dots, m_ .

The periodogram shows which frequency components contribute most strongly to the behaviour of the observed time series. It is useful for identifying the dominant cyclical patterns or periodicities within a dataset.

For most real datasets, the periodogram appears rough and noisy, especially when looking at its plot on the log-scale (i.e., when looking at the plot of log-periodogram). In such cases, researchers attempt to smooth the periodogram to get a clean summary of the trend in the periodogram without getting distracted by noise. What is a good way of smoothing the periodogram?

A nice way of smoothing is via the use of an appropriate model. Previously, we saw for estimating a smooth trend function, say _µt_ , from observed time series data _yt_ , a natural model is:


We can try to use a similar model for the periodogram. Modeling _I_ ( _j/n_ ) as a smooth trend function plus Gaussian noise does not make much sense for multiple reasons: (a) the periodogram is a positive quantity so using the normal distribution may not be a good idea, (b) the noise in the periodogram is more pronounced on the log-scale so we should probably use an additive noise model for the log-periodogram as opposed to the periodogram directly. In other words, we should use a multiplicative noise model for the periodogram.

1

The model that we shall use here is:


where _f_ ( _j/n_ ) is a smooth function that represents the trend in the periodogram, and


_χ_<sup>2</sup> 2<sup>isthechi-squareddistributionwith2degreesoffreedom;itsdensityisgivenby:</sup>


The density of _χ_<sup>2</sup> 2<sup>_/_2isthengivenby:</sup>


The above is the density of the Standard Exponential Distribution (the exponential distribution _Exp_ ( _λ_ ) has density _λe_<sup>_−λx_</sup> _I{x >_ 0 _}_ ; the above corresponds to _λ_ = 1). Thus


Our model can therefore also be written as:


This is a multiplicative noise model. We can rewrite it in additive form by taking logarithms:


The noise in this additive representation is captured by the terms log _ηj,_ 1 _≤ j ≤ n_ . These variables do not have mean zero (from the internet E log _ηj ≈−_ 0 _._ 5772). Therefore log _f_ ( _j/n_ ) does the represent the mean of log _I_ ( _j/n_ ) (in fact, it is strictly larger than the mean of log _I_ ( _j/n_ )). Rather, _f_ ( _j/n_ ) represents the mean of _I_ ( _j/n_ ).

We shall refer to (1) or (2) as the Spectrum Model.

---

[Up: contents](index.md) · [2 Power Spectral Density →](02-2-power-spectral-density.md)
