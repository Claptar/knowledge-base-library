---
title: Influence Curves
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Influence Curves

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_Definition_ : For _O_ 1 _, ..., On ∼ P_ i.i.d., _φn_ = _φn_ ( _O_ 1 _, ..., On_ ) is said to an _asymptotically linear_ estimator of _φ_ ( _P_ ) _∈R_<sup>_k_</sup> with _influence curve IC_ ( _O|P_ ) _∈R_<sup>_k_</sup> if _EP IC_ ( _O|P_ ) = 0, _EP ∥IC_ ( _O|P_ ) _∥_<sup>2</sup> 2<sup>_< ∞_,and</sup><sup>_φn_=</sup><sup>_φ_(</sup><sup>_P_) +</sup> _n_<sup><u>1</u></sup> � _ni_ =1<sup>_IC_(</sup><sup>_Oi|P_) +</sup><sup>_oP_(</sup><sup>_n−_1</sup><sup>_/_2).</sup>

Note: The influence curve depends on the unknown _P_ , so it is not a statistic.

If _φn_ is asymptotically linear for _φ_ ( _P_ ), the CLT tells us that<sup>_√_</sup> _<u>n</u>_ <u>(</u> _φn−φ_ ( _P_ ) = _⇒ N_ (0 _,_ Σ _P_ )

8

under _P_ , where Σ _P_ = _EP_ [ _IC_ ( _O|P_ ) _IC_ ( _O|P_ )<sup>_T_</sup> ]. If we can consistently estimate Σ _P_ from the data (often with the empirical estimator _n_<sup><u>1</u></sup> � _ni_ =1<sup>_IC_(</sup><sup>_Oi|Pn_)</sup><sup>_IC_(</sup><sup>_Oi|Pn_)</sup><sup>_T_),then</sup> we can form asymptotically valid confidence regions for _φ_ ( _P_ ). This is why asymptotic linearity is considered a stronger and more desirable property that<sup>_√_</sup> _<u>n</u>_ <u>-consistency</u> ( _∥φn − φ_ ( _P_ ) _∥_ = _OP_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> )).

---

[← Basics of convergence in Distribution](12-basics-of-convergence-in-distribution.md) · [Up: contents](index.md) · [Examples →](14-examples.md)
