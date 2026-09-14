---
title: Relationship Between Estimating Functions and Tangent Spaces
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Relationship Between Estimating Functions and Tangent Spaces

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

It has been shown by van der Laan and Robbins that in a very strong sense, the only estimating functions of interest are those that are members of _TNUIS_<sup>_⊥_.</sup> For such estimating functions _D_ ( _X|µ, η_ ), it can be shown that if _Fϵ_ is a submodel whose score is in the nuisance tangent space, then _dϵ_<sup>_<u>d</u>EFX_[</sup><sup>_D_(</sup><sup>_X|µ_(</sup><sup>_Fϵ_)</sup><sup>_, η_(</sup><sup>_Fϵ_))] = 0 at</sup><sup>_ϵ_= 0.This property can be used to show that if ˆ</sup><sup>_η_is consistent</sup> for _η_ , then under regularity conditions the solution _µn_ of _n_<sup><u>1</u></sup> � _ni_ =1<sup>_D_(</sup><sup>_Xi|µ,_ˆ</sup><sup>_η_)=0isasymptotically</sup> linear for _µ_ ( _FX_ ) with influence curve IC = _−_ [ _dϵ_<sup>_<u>d</u>EFX_[</sup><sup>_D_(</sup><sup>_X|µ_(</sup><sup>_FX_)</sup><sup>_, η_(</sup><sup>_FX_)]</sup><sup>_−_1</sup><sup>_D_(</sup><sup>_X|µ_(</sup><sup>_FX_)</sup><sup>_, η_(</sup><sup>_FX_)).</sup>

Another property of the nuisance tangent space _TNUIS_<sup>_⊥_isthatitcontainsthelinearspanofall</sup> components of all gradients. Here a gradient is a random variable l(X) such that if _Fϵ_ has score s(X) then _limϵ→_ 0<sup><u>1</u></sup> _ϵ_<sup>(</sup><sup>_µ_(</sup><sup>_Fϵ_)</sup><sup>_−µ_(</sup><sup>_FX_)) =</sup><sup>_⟨l_(</sup><sup>_X_)</sup><sup>_, s_(</sup><sup>_X_)</sup><sup>_⟩_.In general there can be many different gradients,but</sup> the unique gradient in the tangent space _T_ ( _FX_ ) is called the canonical gradient. If an asymptotically linear estimator has an influence curve equal to the canonical gradient, then the estimator is efficient, meaning that it has better asymptotic performance than any other regular estimator.

---

[← Background on Tangent Spaces](41-background-on-tangent-spaces.md) · [Up: contents](index.md) · [Example: Survival Analysis with no Censoring →](43-example-survival-analysis-with-no-censoring.md)
