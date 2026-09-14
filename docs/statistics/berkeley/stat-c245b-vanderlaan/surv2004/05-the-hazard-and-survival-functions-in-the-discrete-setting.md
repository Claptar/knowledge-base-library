---
title: The hazard and survival functions in the discrete setting
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The hazard and survival functions in the discrete setting

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We claimed in the last lecture that S(t) =<sup>�</sup> _{j_ : _tj ≤t}_<sup>(1</sup><sup>_−d_Λ(</sup><sup>_t_))ifTisdiscretewithsupporton</sup> _t_ 1 _< t_ 2 _< ... < tm < ∞_ . Below we prove this assertion.

Recall that _d_ Λ( _s_ ) = _SdF_ ( _s_ <u>(</u> _−s_ <u>))</u><sup>.</sup> In the discrete setting _S_ ( _tj−_ ) = _S_ ( _tj−_ 1), _F_ ( _tj−_ ) = _F_ ( _tj−_ 1), and = _dF_ ( _tj_ ) = _F_ ( _tj_ ) _− F_ ( _tj−_ ) = _F_ ( _tj_ ) _− F_ ( _tj−_ 1). This gives that (1 _− d_ Λ( _t_ )) = 1 _−_<sup>_F_</sup><sup><u>(</u></sup><sup>_tj_</sup> _S_<sup><u>)</u></sup> (<sup>_−_</sup> _tj_<sup>_F_</sup> _−_<sup><u>(</u></sup> 1<sup>_t_</sup> )<sup>_<u>j−</u>_1)</sup> _S_ <u>(</u> _tj−_ 1) _−F_ <u>(</u> _tj_ <u>)+</u> _F_ <u>(</u> _tj−_ 1) =<sup>1</sup><sup>_−F_</sup><sup><u>(</u></sup><sup>_tj−_1)</sup><sup>_−F_</sup><sup><u>(</u></sup><sup>_tj_</sup><sup><u>)+</u></sup><sup>_F_</sup><sup><u>(</u></sup><sup>_tj−_1)</sup> =<sup>1</sup><sup>_−F_</sup><sup><u>(</u></sup><sup>_tj_</sup><sup><u>)</u></sup> _S_ <u>(</u> _tj_ <u>)</u> _S_ ( _tj−_ 1) _S_ ( _tj−_ 1) _S_ ( _tj−_ 1)<sup>=</sup> _S_ ( _tj−_ 1)<sup>.Nowlet</sup><sup>_ti_bethelargestofthe</sup> _t_ 1 _, ..., tm_ that does not exceed t, and note that _S_ ( _ti_ ) = _S_ ( _t_ ) because T is discrete. Also let _t_ 0 = 0 and observe that _S_ ( _t_ 0) = 1. Finally, we see that<sup>�</sup> _{j_ : _tj ≤t}_<sup>(1</sup><sup>_−d_Λ(</sup><sup>_t_))=�</sup> _{j_ :1 _≤j≤i}_<sup>(1</sup><sup>_−d_Λ(</sup><sup>_t_))=</sup> � _{j_ :1 _≤j≤i} SS_ ( _t_ <u>(</u> _jt−j_ <u>)1)</u><sup>=</sup> _S_<sup>_S_</sup> (<sup><u>(</u></sup> _t_<sup>_t_</sup> 0<sup>_i_</sup><sup><u>)</u></sup> )<sup>=</sup><sup>_S_(</sup><sup>_ti_) =</sup><sup>_S_(</sup><sup>_t_).</sup>

---

[← Relationship between the hazard and survival functions](04-relationship-between-the-hazard-and-survival-functions.md) · [Up: contents](index.md) · [The hazard and survival functions in the continuous setting →](06-the-hazard-and-survival-functions-in-the-continuous-setting.md)
