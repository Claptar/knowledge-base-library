---
title: Basics of convergence in Distribution
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Basics of convergence in Distribution

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Review of probabilistic big-oh, little-oh notation: Recall that for random variables _An, Bn_ taking values in a normed space, _An_ = _oP_ ( _Bn_ ) means that _∥An∥/∥Bn∥_ converges to zero in probability under _P_ . So _An_ = _oP_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> ) means that<sup>_√_</sup> _<u>n∥An∥</u>_ converges to zero in probability under _P_ . _An_ is said to be _bounded in probability_ (denoted _An_ = _OP_ (1)) if for all _ϵ >_ 0 there exists _M < ∞_ such that _P_ ( _∥An∥ > M_ ) _≤ ϵ_ . _An_ = _OP_ ( _Bn_ ) means that _∥An∥/∥Bn∥_ = _OP_ (1). Some helpful rules to keep in mind are that _OP_ (1) _oP_ (1) = _oP_ (1) and that _OP_ (1) + _op_ (1) = _OP_ (1).

One important result for proving convergence in distribution is _Slutsky’s Theorem_ . Suppose that a scalar sequence _an_ converges in probability to _a_ , a sequence _bn_ in a metric space ( _D, ∥· ∥_ ) converges to a constant value in ( _D, ∥· ∥_ ) and _Xn ∈_ ( _D, ∥· ∥_ ) converges in distribution to separable _X ∈_ ( _D, ∥· ∥_ ). Slutsky’s Theorem states that _anXn_ + _bn_ converges in distribution to _aX_ + _b_ .

---

[← Functional Derivatives](11-functional-derivatives.md) · [Up: contents](index.md) · [Influence Curves →](13-influence-curves.md)
