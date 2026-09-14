---
title: Data Adaptive Estimation of a Density
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data Adaptive Estimation of a Density

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _T_ 1, _· · ·_ , _Tn_ be i.i.d. observations from distribution density _f_ 0. Given a kernel _K_ , such as _K_ ( _x_ ) = _I_ ( _−_ 1 _≤ x ≤_ 1) _/_ 2, we have as candidate density estimators:


Let _Pn_ denote the empirical distribution, i.e. the probability distribution which puts probability _n_<sup><u>1</u>on</sup> each _Ti, i_ = 1 _, · · · , n_ . Estimators can always be viewed as a function of the empirical distribution _Pn_ . In particular, the kernel density estimator can be viewed as the following function of the empirical distribution:


Here, we note that for any function _h_ ( _T_ )


The estimators _Pn →_ Ψ _h_ ( _Pn_ ), indexed by a bandwidth choice _h_ , are candidate density estimators of _f_ 0.

Definition of the cross-validation selector _hn_

Let _Bn ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> be a random _n_ -dimensional vector.


In other words, _{Ti_ : _Bn_ ( _i_ ) = 1 _}_ is validation sample and _{Ti_ : _Bn_ ( _i_ ) = 0 _}_ is training sample. Let


denote the proportion of the _n_ observations which are in the validation sample. Let _Pn,B_<sup>0</sup> _n_<sup>be</sup> the empirical distribution of training sample, and _Pn,B_<sup>1</sup> _n_<sup>betheempiricaldistributionofvalidation</sup> sample. The cross-validation selector of _h_ can now be defined as:


The idea behind this selector is driven by the fact that


4

where _f →−_ � log _f_ ( _T_ ) _dF_ 0( _T_ ) is called a risk function w.r.t. to the loss function _L_ ( _T, f_ ) = _−_ log _f_ ( _T_ ). Given the bandwidth selection _hn_ , we estimate _f_ 0 with the corresponding kernel density estimator Ψ<sup>ˆ</sup> _hn_ ( _Pn_ ), or equivalently,

---

[← Choice of bandwidth in density estimation](08-choice-of-bandwidth-in-density-estimation.md) · [Up: contents](index.md) · [Some Parametric Models for f 0 →](10-some-parametric-models-for-f-0.md)
