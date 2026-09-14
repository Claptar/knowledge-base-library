---
title: Sample Median
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Sample Median

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This example is slightly harder, because although the sample median is an asymptotically linear estimator of the median under regularity conditions, there is a remainder.

**Theorem 0.6.** _Suppose real-valued O_ 1 _, ...On ∼ P i.i.d. has cumulative distribution function F , and Fn denotes the empirical c.d.f. Suppose that F has a density f that is positive and continuous in a neighborhood of the unique median θ, where F_ ( _θ_ ) = 1 _/_ 2 _. If θn is the sample median F_<sup>_−_1</sup> (1 _/_ 2) = inf _{x_ : _Fn_ ( _x_ ) _≥_ 1 _/_ 2 _}, then θn is an asymptotically linear estimator of θ with influence curve IC_ ( _Oi|P_ ) = _− f_ (1 _θ_ )<sup>(1(</sup><sup>_O≤θ_)</sup><sup>_−_1</sup><sup>_/_2)</sup><sup>_._</sup> **proof** : We first establish the consistency of _θn_ . As the median is given to be unique, _F_ ( _θ_ + _ϵ_ ) _>_ 1 _/_ 2 and _F_ ( _θ − ϵ_ ) _<_ 1 _/_ 2 for any _ϵ >_ 0. Hence, _P_ ( _| θn − θ| > ϵ_ ) = _P_ ( _Fn_ ( _θ − ϵ_ ) _≥_ 1 _/_ 2) + _P_ ( _Fn_ ( _θ_ + _ϵ_ ) _<_ 1 _/_ 2) _→P_ 0 because _Fn_ ( _t_ ) _→P F_ ( _t_ ) for any _t_ by the law of large numbers. Thus _θn →P θ_ .

Let _Gn_ denote the empirical process<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Fn − F_ ) (technically this is<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pn − P_ ) _∈_ ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥·∥F_ ) where _F_ = _{_ 1(( _−∞, t_ ]) : _t ∈R}_ ). It can be shown via empirical process theory that _Gn_ = _⇒ G_ , for _G_ the _P_ -Brownian Bridge. So as ( _Gn, θn_ ) = _⇒_ ( _G, θ_ ) and _G_ is continuous, the continuous mapping theorem yields _Gn_ ( _θ_ ) _− Gn_ ( _θn_ ) = _oP_ (1).

As _f_ is continuous in a neighborhood of _θ_ , Taylor expanding _F_ ( _θn_ ) about _θ_ gives _F_ <u>(</u> _θn_ ) = 1 _/_ 2 + ( _θn − θ_ )( _f_ <u>(</u> _θ_ ) + _oP_ (1)). Clearly _Fn_ ( _θn_ ) = 1 _/_ 2 + _oP_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> ), so _Gn_ <u>(</u> _θn_ ) = _√n_ <u>(</u> _Fn_ ( _θn_ ) _− F_ ( _θn_ )) =<sup>_√_</sup> _<u>n</u>_ <u>(1</u> _/_ 2+ _oP_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> ) _−_ 1 _/_ 2 _−_ ( _θn − θ_ )( _f_ ( _θ_ )+ _oP_ (1)) = _−_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θn − θ_ )( _f_ ( _θ_ ) + _oP_ (1)).

Rearranging terms gives<sup>_√_</sup> _<u>n</u>_ <u>(</u> _θn−θ_ ) = _−_<sup>_G_</sup> _f_<sup>_n_</sup> (<sup><u>(</u></sup> _θ_<sup>_θ_</sup> )<sup>_n_</sup><sup><u>)</u>+</sup><sup>_oP_(1) =</sup><sup>_−G_</sup> _f_<sup>_n_</sup> ( _θ_<sup><u>(</u></sup><sup>_θ_</sup> )<sup><u>)</u>+</sup><sup>_Gn_</sup><sup><u>(</u></sup><sup>_θ_</sup><sup><u>)</u></sup> _f_<sup>_−_</sup> ( _θ_<sup>_G_</sup> )<sup>_n_</sup><sup><u>(</u></sup><sup>_θn_</sup><sup><u>)</u></sup> + _oP_ (1) = _−_<sup>_G_</sup> _f_<sup>_n_</sup> ( _θ_<sup><u>(</u></sup><sup>_θ_</sup> )<sup><u>)</u>+</sup><sup>_oP_(1)fromourcommentsabove.Fromthedefinitionof</sup><sup>_Gn_,dividingboth</sup> sides by<sup>_√_</sup> _<u>n</u>_ gives that _θn_ = _θ − n_<sup><u>1</u></sup> � _ni_ =1 _f_ <u>1(</u> _θ_<sup>(1(</sup><sup>_Oi≤θ_)</sup><sup>_−_1</sup><sup>_/_2) +</sup><sup>_oP_(</sup><sup>_n−_1</sup><sup>_/_2),provingthe</sup>

9

#### desired result. □

---

[← Examples](14-examples.md) · [Up: contents](index.md) · [Bootstrapping →](16-bootstrapping.md)
