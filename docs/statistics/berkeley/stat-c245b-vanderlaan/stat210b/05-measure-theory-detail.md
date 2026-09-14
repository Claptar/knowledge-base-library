---
title: Measure Theory Detail
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Measure Theory Detail

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

When working with real-valued random variables, measurability issues can often be completely ignored, as the construction of subsets of _R_ that are non-Borel measurable usually requires cavilling with the Axiom of Choice. Unfortunately, this is not the case when working with random functions.

If _Gn_ = _⇒ G_ , we need from the definition of weak convergence that _E_ [ _g_ ( _Gn_ )] converges to _E_ [ _g_ ( _G_ )] for bounded continuous _g_ mapping ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥· ∥F_ ) to _R_ . But to even talk about _E_ [ _g_ ( _Gn_ )] according to the usual definition of expectation, we need for _g_ ( _Gn_ ) to be a Borel measurable function. If _O_ 1 _, ..., On_ are defined on a probability space (Ω _, B, P_ ), where _B_ denotes the Borel subsets, it is possible to find _B ∈B_ and bounded continuous _g_ such that _{ω_ : _g_ ( _Gn_ )( _ω_ ) _∈ B} ∈B/_ , so that _g_ ( _Gn_ ) is non- Borel measurable.

We can circumvent this technical difficulty by defining the outer expectation as _E_<sup>_⋆_</sup> _g_ = inf _{Ef_ : _f ≥ g_ is measurable _}_ . So technically, _Xn ∈_ ( _D, ∥·∥_ ) converges in distribution to _X ∈_ ( _D, ∥· ∥_ ) if for all bounded continuous _g_ mapping ( _D, ∥· ∥_ ) to _R_ , _E_<sup>_⋆_</sup> [ _g_ ( _Xn_ )] converges to _E_ [ _g_ ( _X_ )]. However, this and other measurability details will be ignored in subsequent lectures.

---

[← Donsker Classes](04-donsker-classes.md) · [Up: contents](index.md) · [An application of empirical process results to simultaneous confidence bands. →](06-an-application-of-empirical-process-results-to-simultaneous.md)
