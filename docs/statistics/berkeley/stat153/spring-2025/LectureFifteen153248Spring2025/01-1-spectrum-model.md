---
title: 1 Spectrum Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFifteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFifteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Spectrum Model

**Source:** [`LectureFifteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFifteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we looked at the spectral model for a given time series dataset _y_ 0 _, . . . , yn−_ 1. In terms of the DFT _b_ 0 _, . . . , bn−_ 1, the model is given by:


for _j_ = 1 _, . . . , m_ where _m_ = ( _n −_ 1) _/_ 2 (we are assuming that _n_ is odd). The unknown parameters in this model are _γ_ 1<sup>2</sup><sup>_, . . . , γ_</sup> _m_<sup>2and</sup><sup>_γj_representsthestrengthofsinusoidsatfrequency</sup> _j/n_ .

The likelihood corresponding to (1) is proportional to:


Therefore the likelihood depends on the squared magnitudes _|bj|_<sup>2</sup> of the DFT coefficients. Recall that the periodogram _I_ ( _j/n_ ) is defined as


We can therefore rewrite the likelihood in terms of the periodogram as follows:


This likelihood depends on the data only through the periodogram ordinates _I_ ( _j/n_ ) for _j_ = 1 _, . . . , m_ . Therefore the periodogram forms the sufficient statistic in this model. Under (7), we have


The model can therefore be written directly in terms of the periodogram as


1

We can write the likelihood for the above model in terms of the periodogram and this would be proportional to (8). Note also that _χ_<sup>2</sup> 2<sup>distributionwithtwodegreesoffreedomactually</sup> coincides with the Exponential distribution with _λ_ parameter equal to 1 _/_ 2.

Model (1) does not care so much about the individual DFT coefficients _bj_ but only their magnitude.

The negative log-likelihood corresponding to (8) is


For optimization purposes we work with the logarithms of _γj_ . Let _αj_ = log _γj_ . The negative log-likelihood in terms of _αj_ is


If we directly minimize the above with respect to _αj_ (without any additional regularization), we get


This basically means that the _γj_<sup>2parametersfullyinterpolatetheperiodogramleadingto</sup> full overfitting. For more meaningful estimation, we need to add regularization. If we assume smoothness of _αj_ , we can add the penalty<sup>�</sup><sup>_m_</sup> _j_ =2<sup>_−_1((</sup><sup>_αj_+1</sup><sup>_−αj_)</sup><sup>_−_(</sup><sup>_αj−αj−_1))2or</sup> � _mj_ =2 _−_ 1<sup>_|_(</sup><sup>_αj_+1</sup><sup>_−αj_)</sup><sup>_−_(</sup><sup>_αj −αj−_1)</sup><sup>_|_to the negative log-likelihood.This leads to the estimators</sup> _α_ ˆ _t_<sup>ridge</sup> ( _λ_ ) and _α_ ˆ _t_<sup>lasso</sup> ( _λ_ ) which are defined as the minimizers of

and


respectively. The penalties encourage smoothness in _{αj}_ , leading to more stable and interpretable estimates for _{γj_<sup>2</sup><sup>_}_.</sup>

---

[Up: contents](index.md) · [2 Power Spectral Density →](02-2-power-spectral-density.md)
