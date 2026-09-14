---
title: An application of empirical process results to simultaneous confidence bands.
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# An application of empirical process results to simultaneous confidence bands.

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Result 0.1.** _Let Gn,P ∈ ℓ_<sup>_∞_</sup> ( _F_ ) _be an empirical process indexed by a class of funcD tions F. Suppose that F is a Donsker class: that is, Gn,P_ = _⇒GP in ℓ_<sup>_∞_</sup> ( _F_ ) _, where GP is the Gaussian process defined by its finite dimensional distributions being multivariate normal with covariance implied by pairwise covariances COV_ ( _GP_ ( _f_ 1) _, GP_ ( _f_ 2)) = _COVP_ ( _f_ 1( _O_ ) _, f_ 2( _O_ )) _. Let q_ 0 _._ 95 _,P be the 0.95-quantile of ∥GP ∥F ≡_ sup _f ∈F | G_ ( _f_ ) _|. Then_


To obtain the nicest type simultaneous confidence band (that is, a band which is wide were the estimator _Pnf_ is highly variable, and small at _f_ where the estimator _Pnf_ is precise) one would choose _F_ so that VAR _P_ ( _f_ ( _O_ )) = _σ_<sup>2</sup> does not depend on the choice _f ∈F_ . For example, given a class _F_ 0, one would define


where _σ_<sup>2</sup> ( _f_ ) _≡_ VAR _P f_ ( _O_ ). An interesting question for empirical process theory is if the fact that _F_ 0 is Donsker, implies that _F_ is Donsker. Clearly, if inf _f ∈F_ 0 _σ_<sup>2</sup> ( _f_ ) _>_ 0,

3

then the answer is yes, but, if _σ_ ( _f_ ) can approximate zero arbitrarily close so that functions _f/σ_ ( _f_ ) can become unbounded (but finite variance), then we will probably need some condition,.

**Proof:** Consider the function _g_ : _ℓ_<sup>_∞_</sup> ( _F_ ) _→_ IR defined by _g_ ( _G_ ) _≡∥G∥F_ = sup _f ∈F | D G_ ( _f_ ) _|_ . This function is continuous. Since _Gn,P_ = _⇒GP_ in _ℓ_<sup>_∞_</sup> ( _F_ ), the continuous _D_ mapping theorem teaches us that _g_ ( _Gn,P_ )= _⇒g_ ( _GP_ ). Since _q_ 0 _._ 95 _,P_ is a continuity point of the limit distribution _g_ ( _GP_ ), weak convergence implies that


Since the left-hand side equals (1), this completes the proof.

**Result 0.2.** _Let Gn,Pn ∈ ℓ_<sup>_∞_</sup> ( _F_ ) _be the empirical process indexed by a class of functions F corresponding with sampling from the empirical distribution Pn. Suppose that F is a D Donsker class so that Gn,Pn_ = _⇒GP , conditional on almost every data realization_ ( _Pn_ : _n ≥_ 1) _(van der Vaart, Wellner, 1996). Let qn,_ 0 _._ 95 _be the 0.95-quantile of ∥Gn,Pn∥F . Then qn,_ 0 _._ 95 _→ q_ 0 _._ 95 _,P , and thus (by the previous result)_


_D_ By the continuous mapping theorem, we have _∥Gn,Pn∥F_ = _⇒∥GP ∥F_ a.e. Since pointwise convergence of cumulative distribution functions to a continuous cumulative distribution function implies uniform convergence, this implies that the cumulative distribution function of _∥Gn,Pn∥F_ converges uniformly to the cumulative distribution function of _∥GP ∥F_ . Thus,


for _n →∞_ . Combining this with (3) yields


Finally, taking the inverse of the cdf of _∥GP ∥F_ on both sides yields the wished convergence of _qn,_ 0 _._ 95 to _q_ 0 _._ 95 _,P_ a.e. This completes the proof.

---

[← Measure Theory Detail](05-measure-theory-detail.md) · [Up: contents](index.md) · [References →](07-references.md)
