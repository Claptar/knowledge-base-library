---
title: The Influence Curve and the Functional Delta Method
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The Influence Curve and the Functional Delta Method

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Often the easiest way to compute the influence curve of an estimator _φ_ ( _Pn_ ) of a parameter _φ_ ( _P_ ) is to apply the functional delta method. The major difficulty is often showing that _φ_ is a Hadamard differentiable map. We summarize the result in the following theorem.

**Theorem 0.7.** _Suppose that O_ 1 _, ..., On ∼ P i.i.d., and that Gn ∈_ ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥· ∥F_ ) _is the empirical process, so Gn_ ( _f_ ) =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pn_ ( _f_ ) _− P_ ( _f_ )) _for f ∈F. Let G_ 1 _,O ∈_ ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥·∥F_ ) _be defined by G_ 1 _,O_ ( _f_ ) = _f_ ( _O_ ) _− EP_ ( _f_ ( _O_ )) _. Suppose F is a Donsker class (so Gn_ = _⇒ G for G the P -Brownian Bridge). If φ_ : ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥· ∥F_ ) _→R_<sup>_k_</sup> _has Hadamard derivative dφP at P , then φ_ ( _Pn_ ) _is an asymptotically linear estimator for φ_ ( _P_ ) _with influence curve IC_ ( _O|P_ ) = _dφP_ ( _G_ 1 _,O_ ) _._

**proof** : As _dφP_ is a linear map and _Gn_ = _~~√~~_ <u>1</u> _<u>n</u>_ � _ni_ =1<sup>_G_1</sup><sup>_,O_</sup> _i_<sup>_, dφP_(</sup><sup>_Gn_) =</sup> _~~√~~_ <u>1</u> _<u>n</u>_ � _ni_ =1<sup>_dφP_(</sup><sup>_G_1</sup><sup>_,O_</sup> _i_<sup>) =</sup> _~~√~~_ <u>1</u> _<u>n</u>_ � _ni_ =1<sup>_IC_(</sup><sup>_Oi|P_).Butbythefunctionaldeltamethod(thesecondstatementinthe</sup> theorem),<sup>_√_</sup> _<u>n</u>_ <u>(</u> _φ_ ( _Pn_ ) _− φ_ ( _P_ )) = _dφP_ ( _Gn_ ) + _oP_ (1) = _~~√~~_ <u>1</u> _<u>n</u>_ � _ni_ =1<sup>_IC_(</sup><sup>_Oi|P_)+</sup><sup>_oP_(1),so</sup> dividing both sides by<sup>_√_</sup> _<u>n</u>_ gives that _φ_ ( _Pn_ ) = _φ_ ( _P_ ) + _n_<sup><u>1</u></sup> � _ni_ =1<sup>_IC_(</sup><sup>_Oi|P_) +</sup><sup>_oP_(</sup><sup>_n−_1</sup><sup>_/_2),</sup> thus proving the desired result. □

---

[← Bootstrapping](16-bootstrapping.md) · [Up: contents](index.md) · [Terminology for Normed Spaces →](18-terminology-for-normed-spaces.md)
