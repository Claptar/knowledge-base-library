---
title: What’s so great about Tnuis⊥(P)?
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# What’s so great about Tnuis⊥(P)?

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There are many methodologies out there for estimating parameters.

- A: _The plug-in principle_ . If _M ⊃{_ all empirical distributions _}_ , take _ψn_ = _ψ_ ( _Pn_ ), for _Pn_ the empirical distribution.

- B: _Minimum distance estimates_ . For Π( _Pn|M_ ) the closest distribution in _M_ (defined with some metric) to _Pn_ , take _ψn_ = _ψ_ (Π( _Pn|M_ ).

- C: _The method of sieves_ . Approximate _M_ with an increasing nested sequence of regular parametric models, and use the efficient estimate of _ψ_ ( _P_ ) in one of those submodels, where we increase the size of this submodel as we get more data.

- D: _Empirical/Modified likelihood_ . Use maximum likelihood to estimate _ψ_ ( _P_ ) when working in the random model _Mn_ = _{Q ∈M_ : _Q_ ( _{O_ 1 _, ..., On_ ) _}_ ) = 1 _}_ .

Some of these methodologies will be revisited when we study estimation of irregular parameters. But for regular parameters, estimators formed in the ways listed above (or in any other way) can be characterized by _Tnuis_<sup>_⊥_(</sup><sup>_P_).A general result is that if</sup><sup>_ψn_is</sup> a regular asymptotically linear estimator of _ψ_ ( _P_ ), then its influence curve is a gradient (so in _Tnuis_<sup>_⊥_(</sup><sup>_P_)).The estimator then corresponds to using an estimating function from</sup> _Tnuis_<sup>_⊥_(</sup><sup>_P_)(thegradientpremultipliedbytheinverseofitscovariancematrix).Thatis,</sup> all regular asymptotically linear estimators are asymptotically equivalent in first-order with estimators obtained from _Tnuis_<sup>_⊥_(</sup><sup>_P_).Itisforthisreasonthatweconsider</sup><sup>_T_</sup> _nuis_<sup>_⊥_(</sup><sup>_P_)</sup> such a fundamental object.

---

[← The general methodology of van der Laan and Robins](29-the-general-methodology-of-van-der-laan-and-robins.md) · [Up: contents](index.md) · [Stat210b Part 31 — →](31-stat210b-part-31.md)
