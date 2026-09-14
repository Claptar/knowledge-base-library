---
title: Example
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Example

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Population of HIV infected patients _T_ = _TDeath − TAIDS C_<sup>_∗_</sup> = 1988 _− TAIDS_ where _C_<sup>_∗_</sup> = 0 if _TAIDS >_ 1988 Sample is from (T, _C_<sup>_∗_</sup> ) _| T > C_<sup>_∗_</sup>

Define _P_ ( _s_ ) = _Pr_ ( _T_<sup>_′_</sup> _≥ s_ ) Define _P_<sup>¯</sup> ( _s_ ) = _Pr_ ( _T_<sup>_′_</sup> _≥ s, C_<sup>_∗′_</sup> _< s_ )


Essientially, we have proved Identifiability.

Trouble arises if _P_<sup>¯</sup> ( _s_ ) = _Pr_ ( _T_<sup>_′_</sup> _≥ s, C_<sup>_∗′_</sup> _< s_ ) = 0 This occurs if _C_<sup>_∗_</sup> _< s_ is never true.

47

Assuming that _Pr_ ( _C_<sup>_∗_</sup> _< s_ ) _>_ 0 for _s ∈_ (0 _, t_ ), Identifiability is shown.

We now focus on the task of constructing estimators. Define _Pn_ ( _s_ ) = _n_<sup><u>1</u></sup> � _ni_ =1<sup>_I_(</sup><sup>_T ′_</sup> _i_<sup>_≤s_)</sup> Define _P_<sup>¯</sup> _n_ ( _s_ ) = _n_<sup><u>1</u></sup> <u>�</u> _ni_ =1<sup>_I_(</sup><sup>_T ′_</sup> _i_<sup>_≥s, C_</sup> _i_<sup>_∗′< s_)</sup>

We have shown that _S_ ( _t_ ) = _ϕ_ ( _P, P_<sup>¯</sup> ) Therefore, _Sn_ ( _t_ ) = _ϕ_ ( _Pn, P_<sup>¯</sup> _n_ ) This is the Product Limit Estimator for truncated data.

We will now turn our attention to obtaining the Influence Curve. Using the Functional Delta Method:

---

[← Situation](33-situation.md) · [Up: contents](index.md) · [Truncation with Right Censoring →](35-truncation-with-right-censoring.md)
