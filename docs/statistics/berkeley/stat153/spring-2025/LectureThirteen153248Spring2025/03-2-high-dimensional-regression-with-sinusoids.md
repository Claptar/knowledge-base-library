---
title: 2 High-dimensional Regression with Sinusoids
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThirteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureThirteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 High-dimensional Regression with Sinusoids

**Source:** [`LectureThirteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThirteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One natural attempt to fix issues with the low dimensional models (1), (2) and (3) is to include sinusoid terms for all possible frequencies. There are, in general, infinitely many

1

possible values of frequences (in the range (0 _,_ 0 _._ 5]) but we shall, for simplicity, stick to Fourier frequencies. Recall that, when _n_ is odd, the Fourier frequencies are 1 _/n,_ 2 _/n, . . . , m/n_ where _m_ equals ( _n −_ 1) _/_ 2. When _n_ is even, 1 _/_ 2 is also a Fourier frequency. We shall stick to the case where _n_ is odd for simplicity.

The high-dimensional analogue of (1), (2), (3) is (note again that _n_ is odd and _m_ = ( _n −_ 1) _/_ 2)


i.i.d where again _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). We can write this model in matrix form as

_y_ = _Xβ_ + _ϵ_

where


and _β_ is the _n ×_ 1 vector with components _β_ 0 _, β_ 11 _, β_ 21 _, . . . , β_ 1 _m, β_ 2 _m_ . The number of these coefficient parameters is _n_ so this is a high-dimensional regression model.

If we fit this model via least squares without any regularization by minimizing _∥y − Xβ∥_<sup>2</sup> , we would obtain a perfect fit to the data for the choice of parameters:


These can be derived from the orthogonality properties of sinusoids that we discussed previously in Lectures 6 and 7. One can also write _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _k, β_<sup>ˆ</sup> 2 _k,_ 1 _≤ k ≤ m_ in terms of the DFT _b_ 0 _, . . . , bn−_ 1 of _yt_ .

To prevent overfitting and to obtain something meaningful, we need to add some kind regularization to the high-dimensional model (4). Last week, we look at the ridge and LASSO regularization in high-dimensional linear regression models. In the context of (4), the ridge estimator is given by minimizing


The motivation for this estimator is a desire to obtain estimates of _β_ for which _β_ 1 _j, β_ 2 _j_ are somewhat small. In the case of the change of slope model considered last week, smallness of the _β_ -coefficients leads to smooth fits to the data which can be treated as smooth estimates of the underlying trend in the data. However, in the context of the sinusoidal model (4), it is unclear why one would want to obtain small values for _β_ 1 _j, β_ 2 _j_ . In fact, for the sunspots data, we expect that _β_ 1 _j, β_ 2 _j_ would not be small for some special frequencies (e.g., frequencies _j/n_ which are close to 1 _/_ 11). This suggests that the ridge estimator (5) may not yield any anything useful insights when applied to the sunspots dataset.

2

From our discussion in the last lecture, the ridge estimator (5) can also be understood from the Bayesian perspective under the prior:


Again, this model makes sense in the change-of-slope ReLU model from last week because it implies that the underlying trend function is smooth but the data, because of somewhat random fluctuations, looks noisy. In the present sinusoidal case, (6) is less justifiable.

---

[← 1 Recap: Sunspots Data](02-1-recap-sunspots-data.md) · [Up: contents](index.md) · [3 The Spectrum Model →](04-3-the-spectrum-model.md)
