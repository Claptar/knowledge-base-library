---
title: Background on Tangent Spaces
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Background on Tangent Spaces

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _ϵ → Fϵ_ be a one-dimensional parametric submodel of M, going through _FX_ at _ϵ_ = 0. Recall that the score vector of this submodel is defined as _s_ ( _X_ ) = _dϵd_<sup>_logfϵ_(</sup><sup>_X_)</sup><sup>_∈L_</sup> 0<sup>2(</sup><sup>_FX_).Here</sup><sup>_L_2</sup> 0<sup>(</sup><sup>_FX_)isthe</sup> Hilbert space of all functions of X with mean zero and finite variance under _FX_ , and the tangent space _T_ ( _FX_ ) is defined as the linear closure of all possible scores in this Hilbert space. A very important space in efficiency theory is _TNUIS ⊂ T_ , called the nuisance tangent space, which is the linear closure in _L_<sup>2</sup> 0<sup>(</sup><sup>_FX_) of all scores of submodels</sup><sup>_Fϵ_such that</sup> _dϵ_<sup>_<u>d</u>µ_(</sup><sup>_Fϵ_) = 0.The interpretation of such submodels</sup> is that local fluctuations from the truth only change _η_ and not _µ_ . Finally, we define the orthogonal complement of the nuisance tangent space as _TNUIS_<sup>_⊥_(</sup><sup>_FX_)=</sup><sup>_{h∈L_</sup> 0<sup>2(</sup><sup>_FX_):</sup><sup>_⟨h_(</sup><sup>_X_)</sup><sup>_, s_(</sup><sup>_X_)</sup><sup>_⟩_=0</sup>

53

_∀s_ ( _X_ ) _∈ TNUIS_ ( _FX_ ) _}_ , where _⟨h_ ( _X_ ) _, s_ ( _X_ ) _⟩_ = _EFX_ [ _h_ ( _X_ )<sup>_T_</sup> _s_ ( _X_ )] is the inner product of h(X) and s(X) in _L_<sup>2</sup> 0<sup>(</sup><sup>_FX_).</sup>

---

[← What is an Estimating Function](40-what-is-an-estimating-function.md) · [Up: contents](index.md) · [Relationship Between Estimating Functions and Tangent Spaces →](42-relationship-between-estimating-functions-and-tangent-spaces.md)
