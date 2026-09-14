---
title: 3 Model Three
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFourteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFourteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Model Three

**Source:** [`LectureFourteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFourteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Model three is essentially Model two but applied to the DFT. In order to describe this, let us first revisit the DFT. Given a time series _y_ 0 _, . . . , yn−_ 1, its DFT is _b_ 0 _, b_ 1 _, . . . , bn−_ 1 where


_bj_ is a complex number with real and imaginary parts given by


When _j_ = 0, the imaginary part is zero and we get _b_ 0 =<sup>�</sup><sup>_n_</sup> _t_ =0<sup>_−_1</sup><sup>_yt_.</sup><sup>_b_0isthereforejustthe</sup> sum of the datapoints and it does not provide any information on cycles etc.

Another fact that we previously verified is _bn−j_ =<sup>¯</sup> _bj_ (here<sup>¯</sup> _bj_ denotes the complex conjugate of _bj_ ). Because of this property, the later half of the DFT terms is redundant (as they can be recovered from the first half).

If _n_ is odd and _m_ = ( _n −_ 1) _/_ 2, then the most important DFT terms are _b_ 1 _, . . . , bm_ . The other terms are _b_ 0 which is simply the sum of the data points and _bm_ +1 _, . . . , bn−_ 1 which are simply the complex conjugates of _bm, bm−_ 1 _, . . . , b_ 1.

If _n_ is even and _m_ = ( _n −_ 2) _/_ 2, then the most important DFT terms are _b_ 1 _, . . . , bm_ and _bm_ +1. The other DFT terms are _b_ 0 which is simply the sum of the data points and _bm_ +2 _, . . . , bn−_ 1 which are the complex conjugates of _bm, . . . , b_ 1. Note in this case that _m_ +1 = _bn/_ 2 will have zero imaginary part (hence _bm_ +1 is real).

Below we focus on the case where _n_ is odd for simplicity, and take _m_ = ( _n −_ 1) _/_ 2. Model three is obtained by using Model two for the DFT terms _b_ 1 _, . . . , bm_ . Because _bj_ can be complex, we use the modeling assumption for both the real and imaginary parts:


We also assume that _bj_ are independent across _j_ . The unknown parameters in this model are _γ_ 1 _, . . . , γm_ . _γj_ represents the strength of the sinusoids at frequency _j/n_ .

The likelihood corresponding to (4) is proportional to:


Therefore the likelihood depends on the squared magnitudes _|bj|_<sup>2</sup> of the DFT coefficients. Recall that the periodogram _I_ ( _j/n_ ) is defined as


We can therefore rewrite the likelihood in terms of the periodogram as follows:


4

This likelihood depends on the data only through the periodogram ordinates _I_ ( _j/n_ ) for _j_ = 1 _, . . . , m_ . Therefore the periodogram forms the sufficient statistic in this model. Under (4), we have


The model can therefore be written directly in terms of the periodogram as


We can write the likelihood for the above model in terms of the periodogram and this would be proportional to (5). Note also that _χ_<sup>2</sup> 2<sup>distributionwithtwodegreesoffreedomactually</sup> coincides with the Exponential distribution with _λ_ parameter equal to 1 _/_ 2.

Intuitively, Model (4) does not care so much about the individual DFT coefficients _bj_ but only their magnitude.

The negative log-likelihood corresponding to (5) is


As in the case of Model two, for optimization purposes we work with the logarithms of _γj_ . Let _αj_ = log _γj_ . The negative log-likelihood in terms of _αj_ is


If we directly minimize the above with respect to _αj_ (without any additional regularization), we get


This basically means that the _γj_<sup>2parametersfullyinterpolatetheperiodogramleadingto</sup> full overfitting. For more meaningful estimation, we need to add regularization. If we assume smoothness of _αj_ , we can add the penalty<sup>�</sup><sup>_m_</sup> _j_ =2<sup>_−_1((</sup><sup>_αj_+1</sup><sup>_−αj_)</sup><sup>_−_(</sup><sup>_αj−αj−_1))2or</sup> � _mj_ =2 _−_ 1<sup>_|_(</sup><sup>_αj_+1</sup><sup>_−αj_)</sup><sup>_−_(</sup><sup>_αj −αj−_1)</sup><sup>_|_to the negative log-likelihood.This leads to the estimators</sup> _α_ ˆ _t_<sup>ridge</sup> ( _λ_ ) and _α_ ˆ _t_<sup>lasso</sup> ( _λ_ ) which are defined as the minimizers of

and


respectively. The penalties encourage smoothness in _{αj}_ , leading to more stable and interpretable estimates for _{γj}_ .

In the next lecture, we shall discuss alternative ways of representing this model, and also look at more applications.

5

---

[← 2 Model Two](03-2-model-two.md) · [Up: contents](index.md)
