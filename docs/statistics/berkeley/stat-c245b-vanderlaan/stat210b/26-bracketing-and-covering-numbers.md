---
title: Bracketing and Covering Numbers
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bracketing and Covering Numbers

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_Definition_ : The _covering number N_ ( _ϵ, F, ∥·∥_ ) of a class of functions _F_ is the minimum number of balls _{g_ : _∥g − f ∥≤ ϵ}_ such that the union of the balls contians _F_ . The _entropy_ is defined as the logarithm of the covering number.

Note that the covering number increases as epsilon decreases, and that it depends on what norm is chosen.

_Definition_ : Given two functions _l, u_ , define [ _l, u_ ] = _{f_ : _u ≤ f ≤ l}_ . The _bracketing number N_ $$\]( _ϵ, F, ∥·∥_ ) is the minimum number of brackets [ _l, u_ ] with _∥u − l∥≤ ϵ_ needed such that the union contains _F_ . The logarithm of the bracketing number is called the _bracketing entropy_ .

**Theorem 0.17.** _If the norm ∥· ∥ is such that |f | ≤|f | implies ∥f ∥≤∥g∥, then N_ ( _ϵ, F, ∥· ∥_ ) _≤ N_ \[$$(2 _ϵ, F, ∥· ∥_ ) _._

**proof** : For such norms, if _f_ is in the 2 _ϵ_ bracket [ _l, u_ ] then it is the _ϵ_ -ball centered at ( _l_ + _u_ ) _/_ 2. □

Unfortunately, the above theorem has no converse allowing us to bound bracketing numbers from given covering numbers. This means that a good bracketing result is much stronger than a good covering number result.

_Definition F_ ( _o_ ) _≡_ sup _f ∈F |f_ ( _o_ ) _|_ is the _envelope_ for _F_ . In general, we will need _PF_<sup>2</sup> _< ∞_ to establish that _F_ is a _P_ -Donsker class. The _Lr_ ( _Q_ ) norm is defined by _∥f ∥Q,r_ = (� _f_<sup>_r_</sup> _dQ_ )<sup>1</sup><sup>_/r_</sup> . the _uniform entropy number_ (relative to _Lr_ ( _·_ )) is given by sup _Q N_ ( _ϵ∥F ∥Q,r, F, ∥· ∥Q,r_ ), where the supremum is taken over all possible probability distributions.

**Theorem 0.18.** _F is P -Glivenko-Cantelli if N_ $$\]( _ϵ, F, L_ 1( _P_ )) _< ∞ for every ϵ >_ 0 _._

**Theorem 0.19.** _F is P-Glivenko-Cantelli if PF < ∞ and_ sup _Q_ : _QF r<∞ N_ ( _ϵ∥F ∥Q,_ 1 _, F, L_ 1( _Q_ )) _< ∞ for every ϵ >_ 0 _._

**Theorem 0.20.** _F is P -Donsker if_ �0 _∞_ �log _N_ \[$$( _ϵ, F, L_ 2( _P_ ) _dϵ < ∞._

**Theorem 0.21.** _If F is such that_ �0 _∞_<sup>sup</sup><sup>_Q_</sup> �log _N_ ( _ϵ∥F ∥Q,_ 2 _, F, L_ 2( _Q_ ) _dϵ < ∞, then F is P -Donsker for every P such that PF_<sup>2</sup> _< ∞. This integral condition holds if supQ_ log _N_ ( _ϵ∥F ∥Q,_ 2 _, F, L_ 2( _Q_ )) _≤ K_ (1 _/ϵ_ )<sup>2</sup><sup>_−δ_</sup> _, for some δ >_ 0 _._

Note that in the last two theorems, we only have to worry about how the integral behaves for small _ϵ_ , because the bracketing and covering numbers increase as _ϵ_ decreases, and for Glivenko-Cantelli and Donsker classes these numbers will be one for sufficiently large _ϵ_ . Also note that the bracketing number conditions are much weaker than the covering number conditions, and this is because it is harder to find a good bracketing number than a good covering number.

20

### **Some Examples of Donsker classes**

The set of functions with uniformly bounded derivatives is a Donsker class. The class of all monotone functions _{f_ : 0 _≤ f ≤ F }_ is _P_ -Donsker provided _P_ -Donsker provided that _PF_<sup>2</sup> _< ∞_ . The set of indicators of compact, convext subsets of a fixed bounded subset of _R_<sup>_d_</sup> is Donsker for _d ≥_ 2.

### **Permance Properties of Donsker classes**

If _F_ is Donsker and _G ⊂F_ , then _G_ is Donsker. If _F_ and _G_ are Donsker, then so are _c_ 1 _F_ + _c_ 2 _G_ (for scalars _c_ 1 _, c_ 2), _F ∪G_ , _F ∩G_ , the closure of _F_ (set of functions that are limit points both pointwise and in _L_ 2( _P_ )), and the set of convex combinations of functions in _F_ . Also, if _F_ is Donsker with _PF < ∞_ and 1 _/f ≥ δ >_ 0 for _f ∈F_ , then 1 _/F_ = _{_ 1 _/f_ : _f ∈F}_ is Donsker. See section 2.10 of van der Vaart and Wellner for more examples.

---

[← ML Consistency](25-ml-consistency.md) · [Up: contents](index.md) · [1 Estimating Functions →](27-1-estimating-functions.md)
