---
title: Notation and Basic Setup
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Notation and Basic Setup

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We will assume that _O_ 1 _, ..., On ∼ P_ i.i.d.

_Pn_ is the _empirical distribution_ .

_Pf_ means _Epf_ ( _O_ ) = � _fdP_ , likewise _Pnf_ = � _fdPn_ .

_F_ will represent a set of real-valued functions _f_ whose domain is the space of _Oi_ .

_l_<sup>_∞_</sup> ( _F_ ) is the normed space of mappings from _F_ to _R_ . If _G ∈ l_<sup>_∞_</sup> ( _F_ ), the norm is defined by _∥G∥F_ = sup _f ∈F | G_ ( _f_ ) _|< ∞_ .

If _P | f |< ∞_ for all _f ∈F_ , then _Gn ≡_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pn − P_ ) is a random member of _l_<sup>_∞_</sup> ( _F_ ), so it is a random mapping from _F_ to _R_ . It is defined by _Gn_ ( _f_ ) =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pnf − Pf_ ). Note that it is the randomness of the empirical distribution _Pn_ that makes _Gn_ a random element of _l_<sup>_∞_</sup> ( _F_ ).

_G_ is said to be a _P_ -Brownian Bridge if it is a random element of _l_<sup>_∞_</sup> ( _F_ ) that is continuous with probability one, such that ( _G_ ( _f_ 1) _, ..., G_ ( _fk_ ) is multivariate Normal with mean zero and _Cov_ ( _G_ ( _fi_ ) _, G_ ( _fj_ )) = _CovP_ ( _fi_ ( _O_ ) _, fj_ ( _O_ )) for any _k_ members of _F_ . Note that continuity is with respect to the norm of _l_<sup>_∞_</sup> defined earlier, so _G_ is continuous at _f_ 0 _∈F_ if for every _ϵ >_ 0 there exists _δ >_ 0 such that if _f ∈F, ∥f − f_ 0 _∥∞ < δ_ , then _∥G_ ( _f_ ) _− G_ ( _f_ 0) _∥ < ϵ_ .

---

[Up: contents](index.md) · [Glivenko-Cantelli Classes →](02-glivenko-cantelli-classes.md)
