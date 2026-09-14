---
title: 3 Back to the Bayesian Posterior in Linear Regression
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFour153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Back to the Bayesian Posterior in Linear Regression

**Source:** [`LectureFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFour153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us compare (9) and (11), and choose the parameters of the _t_ -density so that (11) matches (9). First note that the dimension _p_ = _m_ + 1 (as _β_ has _m_ + 1 components). Matching the powers ( _n/_ 2) and ( _p_ + _v_ ) _/_ 2, we get


It is also clear that _µ_ = _β_<sup>ˆ</sup> and


We have thus proved that


As we remarked in the frequentist treatment of the simple linear regression model, the quantity _S_ ( _β_<sup>ˆ</sup> ) _/_ ( _n − m −_ 1) is the frequentist unbiased estimator of _σ_<sup>2</sup> . So we denote


With this notation, we get


5

With the posterior density (12), one can do uncertainty quantification about the parameters _β_ 0 _, β_ 1 _, . . . , βm_ . One can generate multiple samples from _tn−m−_ 1 _,m_ +1( _β,_<sup>ˆ</sup> ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ) and plot the resulting fitted values to visualize the uncertainty in the coefficients. One can also use Fact 2.1 to deduce that


where ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> is the ( _j_ +1)<sup>_th_</sup> diagonal entry of ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> . These univariate _t_ -densities describe the marginal uncertainty in the _j_<sup>_th_</sup> coefficient _βj_ .

When _n_ is large, the _t_ -density (12) is approximately equal to the _Nm_ +1( _β,_<sup>ˆ</sup> ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ). Further, when _n_ is large, the distribution <u>(13)</u> will be close to the normal distribution _N_ ( _β_<sup>ˆ</sup> _j,_ ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> ). The quantity _σ_ ˆ ~~�~~ ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> is known as the standard error corresponding to _βj_ .

6

---

[← 2 Multivariate t -density](02-2-multivariate-t--density.md) · [Up: contents](index.md)
