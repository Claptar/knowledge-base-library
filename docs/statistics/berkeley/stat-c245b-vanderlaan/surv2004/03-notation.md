---
title: Notation
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Notation

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- T = _Survival time._ T is a nonnegative random variable.

- F(t) = P(T _≤_ t). F is the _cumulative distribution function_ (cdf). F(t)=0 for t _≤_ 0, F(t) _→_ 1 as t _→∞_ , F is nondecreasing, and F is right continuous.

- S(t) = 1-F(t) = _Survival function_ .

- dF(t) = P(t-dt _≤_ T _≤_ t), for dt infintesimal. dF(t) = f(t)dt if F continuous with Lebesgue density f, and dF(t) = F(t) - F( _t−_ ) if F is a discrete cdf.

- If _T_ 1 _, ..., Tn_ are iid observations of T, then _Fn_ ( _t_ ) = _n_<sup><u>1</u>Σ</sup> _i_<sup>_n_</sup> =1<sup>_I_(</sup><sup>_Ti≤t_) and</sup><sup>_Sn_(</sup><sup>_t_) = 1</sup><sup>_−Fn_(</sup><sup>_t_) are the</sup> _empirical cdf_ and the _empirical survival function_ . If all observations are unique and _T_ (1) _, ..., T_ ( _n_ ) denote the sorted observations in increasing order, then _Fn_ ( _t_ ) = 0 for _t <_ = _T_ (1) _, Fn_ ( _t_ ) = _n_<sup>_<u>i</u>_for</sup> _T_ ( _i_ ) _≤ t < T_ ( _i_ +1) _,_ and _Fn_ ( _t_ ) = 1 for _t ≥ T_ ( _n_ ). When the observations are unique, we also have that _dFn_ ( _t_ ) = 1 _/n_ if _t ∈{T_ 1 _, ..., Tn}_ and _dFn_ ( _t_ ) = 0 zero otherwise.

1

- _λ_ ( _t_ ) = _Hazard function_ .

If T is continuous, the Lebesgue hazard is _λ_ ( _t_ ) = _S_<sup>_<u>f</u>_</sup><sup><u>(</u></sup> (<sup>_t_</sup> _t_<sup><u>)</u></sup> )<sup>= lim</sup><sup>_δ→_0</sup> _P_ <u>(</u> _TP ∈_ (( _Tt, ≥t_ <u>+</u> _tδ_ )]) _<u>/δ</u>_ <u>(</u> _F_ <u>(</u> _t_ <u>)</u> _−F_ <u>(</u> _t−δ_ <u>))</u> _<u>/δ</u>_ = _limδ→_ 0 _S_ ( _t_ ) = _limδ→_ 0 _P_ ( _T ∈_ ( _t, t_ + _δ_ ] _|T ≥ t_ ) _/δ_ If F is discrete, the discrete hazard is _λ_ ( _t_ ) = _P_ ( _T_ = _t|T ≥ t_ ). When T represents the time until a failure, _λ_ ( _t_ ) represents the probability of instantaneous failure given that no failure has occured in [0, t).

_•_ Λ( _t_ ) = _Cumulative hazard function_ . Λ( _t_ ) = �0 _t S_ ( _s_ <u>1</u> _−_ )<sup>_dF_(</sup><sup>_s_),and</sup><sup>_d_Λ(</sup><sup>_s_) =</sup> _S_ ( _s_ <u>1</u> _−_ )<sup>_dF_(</sup><sup>_s_) =</sup><sup>_P_(</sup><sup>_T∈_[</sup><sup>_s −ds, s_])</sup><sup>_/P_(</sup><sup>_T≥s_).</sup>

---

[← Survival Analysis](02-survival-analysis.md) · [Up: contents](index.md) · [Relationship between the hazard and survival functions →](04-relationship-between-the-hazard-and-survival-functions.md)
