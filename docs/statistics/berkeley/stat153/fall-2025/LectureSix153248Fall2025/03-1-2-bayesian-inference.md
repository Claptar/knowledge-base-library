---
title: 1.2 Bayesian Inference
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSix153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSix153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.2 Bayesian Inference

**Source:** [`LectureSix153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSix153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For uncertainty quantification, let us consider Bayesian inference for this model. We need to first write down the likelihood and prior, and then use them to derive the posterior. For the likelihoood, we shall assume (just as in usual linear regression) that the normal distribution for the errors _{ϵt}_ in (1): _ϵt_ i.i.d _∼ N_ (0 _, σ_<sup>2</sup> ). This leads to the likelihood:


where again _S_ ( _β, c_ ) is the sum of squares (3).

For the prior, recall that, for linear regression, we used:


Here unif( _−∞, ∞_ ) can be thought of as short form for unif( _−C, C_ ) for a very large constant _C_ . We will use the same prior here also. However we also need to supply a prior for the parameter _c_ . Here note that _c_ needs to be in the range (1 _, n_ ) (open interval from 1 to _n_ ). Because if _c ≥ n_ , then ReLU( _t − c_ ) = 0 for all _t_ = 1 _, . . . , n_ so the term ReLU( _t − c_ ) is not needed in the model (1). If _c ≤_ 1, then ReLU( _t − c_ ) = _t − c_ for all _t_ = 1 _, . . . , n_ so that the ReLU term in (1) becomes linear so the model again becomes a linear function of _t_ .

2

Because _c ∈_ (1 _, n_ ), a natural prior is to take:


In practice, we would not be interested in values of _c_ that are near the boundaries 1 and _n_ . This is because if _c_ is very close to 1 or _n_ , then the model is essentially linear for most of dataset. To reflect this, we can take the prior for _c_ to be uniform in smaller range than (1 _, n_ ) ignoring points near each end; for example, uniform on (5 _, n −_ 5). Let us work with the prior (7), and we shall mention the changes that need to be made to the posterior if we are instead working with the uniform prior on a smaller range such as (5 _, n −_ 5).

The posterior joint density of all the parameters _β, c, σ_ (here _β_ denotes the vector consisting of _β_ 0 _, β_ 1 _β_ 2) is given by


The likelihood is given in (6) and the prior is


_σ_

We shall drop the indicator terms involving _C_ because _C_ is very large (think _∞_ ). This will lead to


The posterior is then given by


To get the posterior density of _c_ alone ( _c_ is the most important parameter in the model (1)), we need to integrate the joint posterior density above with respect to _β_ and _σ_ :


Let us first calculate the inner integral. _S_ ( _β, c_ ) is a quadratic function in _β_ so that � exp( _−S_ ( _β, c_ ) _/_ (2 _σ_<sup>2</sup> )) _dβ_ should be related to the normalizing constants in the multivariate normal density. To figure the integral precisely, we first use the Pythagorean identity (discussed previously):


where _β_<sup>ˆ</sup> _c_ is given in (4). The value _S_ ( _β_<sup>ˆ</sup> _c, c_ ) is equal to _RSS_ ( _c_ ) as noted in (5). Thus


3

where _|Xc_<sup>_TXc|_=det(</sup><sup>_X_</sup> _c_<sup>_TXc_).Here</sup><sup>_p_=3becausetherearethreecomponentsinside</sup><sup>_β_.</sup> Therefore


The change of variable _σ_ = _s_ ~~�~~ _RSS_ ( _c_ ), gives


This posterior will be evaluated numerically over a grid of values of _c_ in the range (1 _, n_ ). The term _|Xc_<sup>_TXc|−_1</sup><sup>_/_2will become infinite when</sup><sup>_|X_</sup> _c_<sup>_TXc|_= 0 i.e.,when</sup><sup>_Xc_does not have full</sup> column rank. This is the case when _c_ is outside of the range (1 _, n_ ). When _c_ is in the range (1 _, n_ ), the determinant of _Xc_<sup>_TXc_willbenon-zerobutitwillstillbegoodtonotconsider</sup><sup>_c_</sup> too close to 1 or _n_ to prevent numerical instability due to near-singularity.

If the prior is taken to be uniform on a different range (say (5 _, n −_ 5)), then we simply need to change the indicator _I{_ 1 _< c < n}_ in (8) by the indicator over the prior range.

The main term in the posterior (8) is (1 _/RSS_ ( _c_ ))<sup>(</sup><sup>_n−p_)</sup><sup>_/_2</sup> (the other term _|Xc_<sup>_TXc|−_1</sup><sup>_/_2</sup> generally does not vary significantly with _c_ ). This term takes its largest value when _c_ equals the least squares estimator _c_ ˆ (note _c_ ˆ minimizes _RSS_ ( _c_ )). The size of the power _n − p_ determines the amount of concentration of the posterior around _c_ ˆ. When _n − p_ is large, the posterior is very tightly concentrated around _c_ ˆ.

4

---

[← 1.1 Parameter Estimation](02-1-1-parameter-estimation.md) · [Up: contents](index.md)
