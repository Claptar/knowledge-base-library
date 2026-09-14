---
title: 2 Multivariate t -density
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFour153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Multivariate t -density

**Source:** [`LectureFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFour153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The multivariate _t_ -density is obtained by changing the scale of a **multivariate** normal density. Let _X_ have the _p_ -variate normal distribution _Np_ ( _µ,_ Σ). This means that _X_ is a

3

_p ×_ 1 random vector, _µ_ is a _p ×_ 1 vector, Σ is a _p × p_ (positive-definite) matrix and the density of _X_ is equal to


Let _V_ be a chi-squared random variable with _v_ degrees of freedom and assume that _V_ and _X_ are independent. Define


Note that _X_ and _T_ are both _p ×_ 1 random vectors while _V_ is a scalar. In other words, _T_ is given by


Note specifically that the scale change on each component is given by the same random variable _V_ .

The distribution of this random vector _T_ will be denoted by _tv,p_ ( _µ,_ Σ). Its density can be derived in the following way:


Observe that


so that

where we used det( _x_<sup>_<u>v</u>_Σ) = (</sup><sup>_v/x_)</sup><sup>_p_det(Σ).Asaresult</sup>

The change of variable

leads to

4

Therefore the density corresponding to _tv,p_ ( _µ,_ Σ) distribution is proportional to


Note that, in the notation _tv,p_ ( _µ,_ Σ), _v_ denotes degrees of freedom, _p_ denotes dimension, _µ_ and Σ denote the mean vector and covariance matrix of the corresponding normal random vector _X_ .

When _v_ is large, _tv,p_ ( _µ,_ Σ) is very close to _Np_ ( _µ,_ Σ). The following fact will be useful in the sequel.

**Fact 2.1.** _If T ∼ tv,p_ ( _µ,_ Σ) _has components T_ 1 _, . . . , Tp, then, for each j_ = 1 _, . . . , p,_


_where µj is the j_<sup>_th_</sup> _component of µ and_ Σ( _j, j_ ) _is the_ ( _j, j_ )<sup>_th_</sup> _entry of_ Σ _._

This fact follows directly from (10) (and the univariate definition of the _t_ -density _tv,_ 1) because


and _Xj ∼ N_ ( _µj,_ Σ( _j, j_ )).

---

[← 1 Bayesian Inference for Regression](01-1-bayesian-inference-for-regression.md) · [Up: contents](index.md) · [3 Back to the Bayesian Posterior in Linear Regression →](03-3-back-to-the-bayesian-posterior-in-linear-regression.md)
