---
title: Note on Integration Theory
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Note on Integration Theory

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Definition: Let _D_ [0 _, b_ ] denote the space of cadlag functions on [0 _, b_ ]. _BVM ⊂ D_ [0 _, b_ ] is the set of cadlag functions on [0 _, b_ ] of _bounded variation_ , indexed by some _M >_ 0. _A ∈ BVM_ if<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_|A_(</sup><sup>_ti_)</sup><sup>_−A_(</sup><sup>_ti−_1)</sup><sup>_| ≤M_forall0</sup><sup>_≤t_1</sup><sup>_≤... ≤tn≤b_.</sup>

Suppose _a_ is a Borel measurable function on [0 _, b_ ]. If _A_ is a monotone cadlag function on [0 _, b_ ] such that _−∞ < A_ (0) _≤ A_ ( _b_ ) _< ∞_ , recall that �0 _b_<sup>_adA_isdefinedas</sup> �0 _b_<sup>_adµ_.</sup> Here _µ_ is the measure on [0 _, b_ ] (with respect to the Borel sigma-field) uniquely defined (by Caratheodory’s Extension Theorem) by _µ_ ((0 _, b_ ]) = _A_ ( _b_ ) _− A_ (0). It can be shown that if _A ∈ BVM ⊂ D_ [0 _, b_ ] then _A_ can be uniquely written as _A_ 1 _− A_ 2 where _A_ 1 _, A_ 2 are monotone cadlag functions such that _−∞ < Aj_ (0) _≤ Aj_ ( _b_ ) _< ∞_ . In this case �0 _b_<sup>_adA_</sup> can be defined as �0 _b_<sup>_adA_1</sup><sup>_−_</sup> �0 _b_<sup>_adA_2.If</sup><sup>_A_isnotnecessarilyofboundedvariation,</sup> but _a_ is of bounded variation, then �0 _b_<sup>_adA_canbedefinedby</sup><sup>_integrationbyparts_as</sup> _a_ ( _A_ ( _b_ )) _− a_ ( _A_ (0)) _−_ �0 _b_<sup>_A_(</sup><sup>_t−_)</sup><sup>_da_(</sup><sup>_t_).</sup>

---

[← Terminology for Normed Spaces](18-terminology-for-normed-spaces.md) · [Up: contents](index.md) · [Product Integrals →](20-product-integrals.md)
