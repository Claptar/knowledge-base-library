---
title: 3 The EM-Algorithm For Computing The MLE of a Full Data Model Based on Censored
  Data
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 The EM-Algorithm For Computing The MLE of a Full Data Model Based on Censored Data

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _X_ 1 _, X_ 2 _, . . . , Xn_ be _n i.i.d._ observations drawn from a full data distribution _FX_ with density _fθ._ Let the observed data _Y_ 1 = _φ_ ( _C_ 1 _, X_ 1) _, Y_ 2 = _φ_ ( _C_ 2 _, X_ 2) _, . . . , Yn_ = _φ_ ( _C_ 2 _, Xn_ ) be _n i.i.d._ observations _Y_ = _φ_ ( _C, X_ ) _∼ Pfθ,G ≡ Pθ,G_ , where the random variable _C_ represents the censoring on _X_ (note that _C_ and _X_ may not necessarily be univariate R.V.). Let _G ≡ GC|X_ denote the censoring mechanism.

Let _C_ ( _Y_ ) be the _coarsening_ of _X_ implied by _Y_ : _CY ≡ C_ ( _Y_ ) is a subset of domain (X) such that Pr ( _X ∈ C_ ( _Y_ )) = 1 _._ We’ll assume for the rest of this lecture that _CY_ satisfies the so-called _Coarsening At Random_ (CAR) condition: Pr ( _Y_ = _y | X_ = _x_ ) is constant for _x ∈ C_ ( _Y_ ) _._ Alternatively the condition can be expressed as that the coarsening mechanism (i.e. the conditional density _g_ of the conditional distribution _G_<sup>_′_</sup> ( _·|X_ ) of the observed data _Y_ given _X_ ) is CAR if it’s a function of _Y_ only. In other words knowing what the value of the random variable _X_ is, does not in any way provide more info on the observed data _Y_ , including the censoring mechanism _G_ .

Assuming CAR, the likelihood for an individual observation factorizes into a part that depends on the censoring mechanism _G_ and a part that doesn’t: _Pθ,G_ ( _Y_ = _y_ ) = _Pfθ_ ( _X ∈ C_ ( _Y_ )) _PG_ ( _Y_ = _y | X_ = _x_ ) _._ Hence, the log-likelihood of _Y_ 1 _, Y_ 2 _, . . . , Yn_ under CAR simplifies to:


which is maximized by the MLE estimator:


Note that _Fθ_ ( _C_ ( _Yi_ )) is an alternative form for � _C_ ( _Y_ )<sup>_fθ_(</sup><sup>_x_)</sup><sup>_dx_.</sup>

In the most general case, the model for _Fθ_ is non-parametric , and _θn_ is found using the _Expectation-Maximization algorithm_ , or _EM-alg_ for short, which is described below:

1. Initialize _θ_ with some value _θ_<sup>0</sup> ;

50

2. For _k_ = 1 _,_ 2 _, . . ._ repeat until convergence:


The EM algorithm performs repeatedly two steps: first, for _θ_<sup>_k_</sup> - fixed, the conditional expectation of the the observed data log-likelihood is calculated, which simultaneously imputes the missing/censored data as well. This is followed by finding which value of _θ_ maximizes the full-data likelihood using the newly imputed values of _X_ and setting the _θ_<sup>_k_+1</sup> to that value.

The EM-alg always converges to a local maximum. In the case of _X_ being distributed with density from the exponential family of distributions:


the EM-alg reduces to:


where _Kn_ ( _Y_ 1 _, . . . , Yn_ ) _≡_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Eθk_[</sup><sup>_K_(</sup><sup>_Xi_)</sup><sup>_| Yi_]and</sup><sup>_Sn_(</sup><sup>_Y_1</sup><sup>_, . . . , Yn_)</sup><sup>_≡_�</sup> _i_<sup>_n_</sup> =1<sup>_Eθk_[</sup><sup>_S_(</sup><sup>_Xi_)</sup><sup>_| Yi_].</sup> Now, compare the above with the full data MLE based on _X_ 1 _, . . . , Xn_ :


where _Kn_ ( _X_ 1 _, . . . , Xn_ ) _≡_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_K_(</sup><sup>_Xi_)and</sup><sup>_Sn_(</sup><sup>_X_1</sup><sup>_, . . . , Xn_)</sup><sup>_≡_�</sup><sup>_n_</sup> _i_ =1<sup>_S_(</sup><sup>_Xi_).Hence,inthecaseof</sup> distribution from the exponential family, knowing how to find the full data MLE directly translates in knowing how to find the observed data MLE: replace _K_ ( _Xi_ ) with the conditional expectation _Eθk_ [ _K_ ( _Xi_ ) _| Yi_ ] and iterate.

---

[← Quantiles of F](36-quantiles-of-f.md) · [Up: contents](index.md) · [NPMLE based on censored data →](38-npmle-based-on-censored-data.md)
