---
title: 3 Utility of the Periodogram
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEight153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEight153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Utility of the Periodogram

**Source:** [`LectureEight153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEight153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The periodogram is a very commonly used tool for time series data analysis. It has the following two main uses:

1. If we want to fit the single sinusoidal model


to the data, then the periodogram allows efficient computation of _RSS_ ( _f_ ) for Fourier frequencies _f ∈_ (0 _,_ 0 _._ 5) via the following formula:


For data sets with large _n_ , directly computing _RSS_ ( _f_ ) over a fine grid might be computationally infeasible. In such cases, one can restrict to Fourier frequencies and compute _RSS_ ( _f_ ) using the above formula (note that, due to the FFT algorithm, _I_ ( _f_ ) for Fourier frequencies _f_ can be computed very efficiently).

Remember also that _RSS_ ( _f_ ) is key to doing inference for _f_ in the model (7). The MLE of _f_ is obtained by minimizing _RSS_ ( _f_ ). The Bayesian posterior is given by:


When _f_ is a Fourier frequency lying in (0 _,_ 1 _/_ 2), we saw in Lecture 6 that


so that _|Xf_<sup>_TXf|_=</sup><sup>_n_3</sup><sup>_/_8.Importantly,thistermdoesnotdependon</sup><sup>_f_.Thusifwe</sup> restrict to Fourier frequencies, then the Bayesian posterior simplifies to


2. The periodogram can suggest alternative models for the data. For example, if the periodogram has two prominent peaks, then this suggests the model:

_yt_ = _β_ 0 + _β_ 1 cos(2 _πf_ 1 _t_ ) + _β_ 2 sin(2 _πf_ 1 _t_ ) + _β_ 3 cos(2 _πf_ 2 _t_ ) + _β_ 4 sin(2 _πf_ 2 _t_ ) + _ϵt._ (8)

Formal inference for this model proceeds very similarly to (7). The main difference is that the definition of _RSS_ should now be changed to:

_RSS_ ( _f_ 1 _, f_ 2)


The analysis now proceeds as before with this modified definition of _RSS_ . The MLE of _f_ 1 and _f_ 2 is obtained by minimizing _RSS_ ( _f_ 1 _, f_ 2) over _f_ 1 _, f_ 2, and the Bayesian posterior is given by


3

where _Xf_ is now given by


In practice, evaluation and minimization of _RSS_ ( _f_ 1 _, f_ 2) can be done either on a joint grid for _f_ 1 and _f_ 2, or some sequential algorithm. It may be helpful to note here that if _f_ 1 and _f_ 2 are both Fourier frequencies and both lie strictly between 0 and 0 _._ 5, then


Thus if one restricts to Fourier frequencies, then inference under the model (8) can be easily via the periodogram. If we work with arbitrary frequencies, grid-based minimization of _RSS_ and evaluation of the Bayesian posterior would be computationally expensive.

---

[← 2 The Periodogram](02-2-the-periodogram.md) · [Up: contents](index.md) · [4 Other Nonlinear Regression Models →](04-4-other-nonlinear-regression-models.md)
