---
title: 1 Recap from last lecture
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSix153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSix153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Recap from last lecture

**Source:** [`LectureSix153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSix153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we discussed fitting the sinusoidal model:


to the observed time series _y_ 1 _, . . . , yn_ . We looked at both the MLE and Bayesian inference for estimating the unknown parameters _f, β_ 0 _, β_ 1 _, β_ 2 _, σ_ . The main parameter is _f_ which we reasoned can be taken to lie in the interval [0 _,_ 1 _/_ 2] (this is because the observed times are 1 _, . . . , n_ ).

In both the MLE and Bayesian approaches, a key role for inferring _f_ is played by the following criterion function:


where


_RSS_ ( _f_ ) is simply the residual sum of squares in the linear regression model obtained by fixing the frequency parameter _f_ . The MLE for _f_ is obtained by minimizing _RSS_ ( _f_ ) over _f ∈_ [0 _,_ 1 _/_ 2] while the Bayesian posterior is given by:


We discussed how the MLE can be calculated (approximately) and how the Bayesian posterior can be evaluated (approximately) by taking a fine grid of values of _f_ inside the domain [0 _,_ 1 _/_ 2] (for the Bayesian posterior, it is important to not go too close to the boundary values 0 and 0 _._ 5 because the term _Xf_<sup>_TXf_willbeclosetosingularforsuch</sup><sup>_f_).</sup>

1

---

[Up: contents](index.md) · [2 Fourier Frequencies and Computation of RSS ( f ) →](02-2-fourier-frequencies-and-computation-of-rss-f.md)
