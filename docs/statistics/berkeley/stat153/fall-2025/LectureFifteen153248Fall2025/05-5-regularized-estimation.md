---
title: 5 Regularized Estimation
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Regularized Estimation

**Source:** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Parameter estimation is done by maximizing likelihood with a regularization penalty which ensures smoothness of the estimates (without the regularization penalty, we would overfit in the sense that the estimate of _f_ ( _j/n_ ) would coincide with the periodogram _I_ ( _j/n_ )).

To obtain the likelihood, we can use any of the three definitions of the spectrum model. If we use Definition 1 (i.e., (3)), the likelihood will be given by:


We can rewrite the above likelihood in terms of the periodogram (because _I_ ( _j/n_ ) = _|bj|_<sup>2</sup> _/n_ ) as follows:


We can also use the definition (1) and write the likelihood directly using the exponential distribution. Note that the density of _ηj_ is exp( _−x_ ) _I{x >_ 0 _}_ and the density of _f_ ( _j/n_ ) _ηj_ is _f_ ( _j/n_ <u>1</u> )<sup>exp(</sup><sup>_−_</sup> _f_ ( _j/nx_ )<sup>)</sup><sup>_I{x >_0</sup><sup>_}_.Thusthelikelihood(jointdensityof</sup><sup>_I_(</sup><sup>_j/n_)</sup><sup>_,_1</sup><sup>_≤j≤m_)is:</sup>


The above is equivalent to (8) (up to proportionality) because _f_ ( _j/n_ ) = 2 _γj_<sup>2</sup><sup>_/n_.</sup>

The negative log-likelihood corresponding to (8) is


For optimization purposes we work with the logarithms of _γj_ . Let _αj_ = log _γj_ . The negative log-likelihood in terms of _αj_ is


5

If we directly minimize the above with respect to _αj_ (without any additional regularization), we get


This basically means that the _γj_<sup>2parametersfullyinterpolatetheperiodogramleadingto</sup> full overfitting. For more meaningful estimation, we need to add regularization. If we assume smoothness of _αj_ , we can add the penalty<sup>�</sup><sup>_m_</sup> _j_ =2<sup>_−_1((</sup><sup>_αj_+1</sup><sup>_−αj_)</sup><sup>_−_(</sup><sup>_αj−αj−_1))2or</sup> � _mj_ =2 _−_ 1<sup>_|_(</sup><sup>_αj_+1</sup><sup>_−αj_)</sup><sup>_−_(</sup><sup>_αj −αj−_1)</sup><sup>_|_to the negative log-likelihood.This leads to the estimators</sup> _α_ ˆ _t_<sup>ridge</sup> ( _λ_ ) and _α_ ˆ _t_<sup>lasso</sup> ( _λ_ ) which are defined as the minimizers of

and


respectively. The penalties encourage smoothness in _{αj}_ , leading to more stable and interpretable estimates for _{γj_<sup>2</sup><sup>_}_.</sup>

Once we obtain estimates _α_ ˆ _j_ of _αj_ , we can convert them to estimates of _γj_ via ˆ _γj_ = exp(ˆ _αj_ ) and then to estimates of _f_ ( _j/n_ ) via _f_<sup>ˆ</sup> ( _j/n_ ) = 2ˆ _γj_<sup>2</sup><sup>_/n_.</sup>

---

[← 4 Rewriting the Model in terms of yt](04-4-rewriting-the-model-in-terms-of-yt.md) · [Up: contents](index.md) · [6 The case of even n →](06-6-the-case-of-even-n.md)
