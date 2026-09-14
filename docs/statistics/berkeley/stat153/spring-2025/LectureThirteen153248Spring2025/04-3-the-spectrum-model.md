---
title: 3 The Spectrum Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThirteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureThirteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 The Spectrum Model

**Source:** [`LectureThirteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThirteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The spectrum model (described below) is obtained by making two changes to (4) and (6). First the additive error _ϵt_ term is dropped from (4). Presence of this term imparts additional random fluctuations to the sinusoidal term, making the model not appropriate for datasets such as the sunspots which appear to not have random fluctuations. This leads to the model:


Secondly, the prior assumption (6) is changed to the following: _β_ 11 _, β_ 21 _, β_ 12 _, β_ 22 _, . . . , β_ 1 _m, β_ 2 _m_ are all independent with


In other words, _β_ 1 _j, β_ 2 _j_ i.i.d _∼ N_ (0 _, τj_<sup>2)for</sup><sup>_j_=1</sup><sup>_, . . . , m_.Insteadofusingasingle</sup><sup>_τ_2,wenow</sup> use _τ_ 1<sup>2</sup><sup>_, . . . , τ_</sup> _m_<sup>2soonevarianceparametereachforthesinusoidateachfrequency</sup><sup>_j/n_.</sup>

Taken together the parameters _τ_ 1<sup>2</sup><sup>_, . . . , τ_</sup> _m_<sup>2areknownasthespectrumofthemodel.The</sup> spectrum represents the variances of the random variables that determine the amplitudes of the sinusoidal terms at the Fourier frequencies (see for example page 8 of the book “Spectral analysis for univariate time series” by Percival and Walden).

Under these modeling assumptions, the variance of _yt_ is given by:


_τj_<sup>2representshowmuchcontributionthecorrespondingfrequency</sup><sup>_j/n_hasintheoverall</sup> variance structure of _yt_ . If _τj_<sup>2islargeforaspecific</sup><sup>_j_,thecorrespondingfrequency</sup><sup>_j/n_has</sup> a strong contribution to the variance of the data. If _τj_<sup>2issmall,thecontributionofthat</sup> frequency is small.

The sequence _{τj_<sup>2</sup><sup>_}_providesa</sup><sup>_spectralrepresentation_ofthetimeseriesinthesensethat</sup> it describes the distribution of variance across frequencies.

We shall refer to (7) as the spectrum model. In the next lecture, we shall look at an alternative way of thinking about this model in terms of the DFT of the data.

3

The spectrum model consists of the unknown parameters _β_ 0 and the spectrum given by the variances _τ_ 1<sup>2</sup><sup>_, . . . , τ_</sup> _m_<sup>2.Ofthese</sup><sup>_β_0isnotreallyaparameterasitsimplyequals</sup><sup>_y_¯.Tosee</sup> this, just average both sides of (7) with respect to _t_ and note that


which gives _β_ 0 = _y_ ¯. In other words, (7) is equivalent to


_τ_ 1<sup>2</sup><sup>_, . . . , τ_</sup> _m_<sup>2denotetheunknownparametersinthismodelwhichwillbeestimatedfromthe</sup> data (we shall see how to do this in the next lecture). Data generated from this model will look differently depending on the exact values of _τ_ 1<sup>2</sup><sup>_, . . . , τ_</sup> _m_<sup>2.Herearesomeexamples.</sup>

1. Suppose _τj_<sup>2equalsaconstantwhen</sup><sup>_j/n_liesinafixedinterval[1</sup><sup>_/_9</sup><sup>_,_1</sup><sup>_/_13]and0other-</sup> wise:


Then data generated from this model look periodic with clear peaks. The gaps between the peaks will change from cycle to cycle (some gaps will be 10, some 11, some 9 etc.).

2. Suppose _τj_<sup>2increaseswith</sup><sup>_j_.Thenthehigherfrequencysinusoidswilldominate,and</sup> the data will look quite wiggly.

3. Suppose _τj_<sup>2decreaseswith</sup><sup>_j_.</sup> Then the lower frequency sinusoids with dominated, giving the data a smoother appearance.

4

---

[← 2 High-dimensional Regression with Sinusoids](03-2-high-dimensional-regression-with-sinusoids.md) · [Up: contents](index.md)
