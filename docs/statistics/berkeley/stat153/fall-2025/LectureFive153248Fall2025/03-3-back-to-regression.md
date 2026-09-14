---
title: 3 Back to Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Back to Regression

**Source:** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us get back to


The quantity _S_ ( _β_<sup>ˆ</sup> ) _/_ ( _n − m −_ 1) is the **frequentist unbiased** estimator for _σ_<sup>2</sup> , so we denote it by _σ_ ˆ<sup>2</sup> :


_σ_ ˆ can also be justified as a Bayesian estimator of _σ_ (See Question 5 (e) of Homework One). The terminology **Residual Standard Error** is sometimes used for _σ_ ˆ.

With the notation for _σ_ ˆ, the posterior (6) becomes:


By one of the facts mentioned about the _t_ -distribution, the posterior of each individual _βj_ is also _t_ :


3

where ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> is the ( _j_ + 1)<sup>_th_</sup> diagonal entry of ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> (note that we are using the ( _j_ + 1)th diagonal entry of _X_<sup>_T_</sup> _X_ because _βj_ is the ( _j_ + 1)th component of _β_ ). Writing this density out, we have


which implies that


This can be used to obtain uncertainty intervals for _βj_ . If _tn−m−_ 1 _,α/_ 2 is the point beyond which the _t_ -distribution (with _n − m −_ 1 degrees of freedom) assigns probability _α/_ 2, then


which is same as:


is called the 100(1 _− α_ )% Bayesian Credible interval for _βj_ . It **exactly coincides** with the frequentist 100(1 _− α_ )% confidence interval for _βj_ .

When _n−m−_ 1 is large, the _t_ -density (6) is approximately equal to the _Nm_ +1( _β,_<sup>ˆ</sup> ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ). Further, when _n − m −_ 1 is large, the distribution (7) will be close to the normal distribution _N_ ( _β_<sup>ˆ</sup> _j,_ ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> ). The quantity _σ_ ˆ ~~�~~ ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> is known as the standard error corresponding to _βj_ .

---

[← 2 t -density](02-2-t--density.md) · [Up: contents](index.md) · [4 Proof of (4) →](04-4-proof-of-4.md)
