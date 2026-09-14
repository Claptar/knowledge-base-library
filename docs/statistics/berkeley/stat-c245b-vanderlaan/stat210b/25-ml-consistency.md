---
title: ML Consistency
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ML Consistency

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

� log _f_<sup>_<u>f</u>_</sup> _θ_<sup>_<u>θ</u>_</sup> 0<sup>_fθ_0</sup><sup>_dx≤_log</sup> � _ffθθ_ 0<sup>_fθ_0</sup><sup>_dx_=log(1)=0withequalityiff</sup><sup>_fθ_=</sup><sup>_fθ_0byJensen’s</sup> inequality, as log( _·_ ) is strictly concave on (0 _, ∞_ ). By identifiability, this implies _KL_ ( _·_ ) is uniquely maximized at _θ_ 0. As _θn_ is the mle, _Pn_ log _fθn ≥ Pn_ log _fθ_ 0. We can rewrite this as _P_ log _fθn_ + _~~√~~_ <u>1</u> _<u>n</u>_<sup>_Gn_log</sup><sup>_fθn≥P_log</sup><sup>_fθ_0+</sup><sup>_Gn_log</sup><sup>_fθ_0,for</sup><sup>_Gn_=</sup> _√n_ <u>(</u> _Pn − P_ ). _KL_ ( _θ_ 0) = _P_ log _fθ_ 0 _≤ P_ log _fθn ≤ P_ log _fθ_ 0 _−_ _~~√~~_ <u>2</u> _<u>n</u>_<sup>sup</sup><sup>_θ∈_Θ</sup><sup>_|Gn_log</sup><sup>_fθ|→P_log</sup><sup>_fθ_0=</sup> _KL_ ( _θ_ 0) in probability, by the given Glivenko-Cantelli condition, implying that _KL_ ( _θn_ ) converges to _KL_ ( _θ_ 0) in probability.

As _{θ ∈_ Θ : _|θ − θ_ 0 _| ≥ ϵ}_ is compact (check it is closed and bounded if Θ is), _KL_ takes on its maximum on the set, which is less than _KL_ ( _θ_ 0) by identifiability, so there is a _δ_ ( _ϵ_ ) _>_ 0 such that _P_ ( _|θn − θ_ 0 _| ≥ ϵ_ ) _≤ P_ ( _KL_ ( _θ_ 0) _− KL_ ( _θn_ ) _> δ_ ( _ϵ_ )) _→_ 0.

19

---

[← The Exponential with Censoring](24-the-exponential-with-censoring.md) · [Up: contents](index.md) · [Bracketing and Covering Numbers →](26-bracketing-and-covering-numbers.md)
