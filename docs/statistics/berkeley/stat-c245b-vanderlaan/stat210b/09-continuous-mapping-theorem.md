---
title: Continuous Mapping Theorem
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Continuous Mapping Theorem

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Theorem 0.2.** _Suppose that Xn converges to X in distribution in a normed space_ ( _D, ∥· ∥_ ) _, where X is Borel measurable and separable with probability one, and H is a continuous mapping from_ ( _D, ∥· ∥_ ) _to another normed space_ ( _E, ∥· ∥_ ) _. Then H_ ( _Xn_ ) _converges in distribution to H_ ( _X_ ) _._

**proof** : Let _g_ be a bounded continuous mapping from ( _E, ∥· ∥_ ) to _R_ . By the a.s. representation theorem, there exists _Yn_ = _d Xn_ , _Y_ = _d X_ such that _Yn → Y_ a.s. Hence, _H_ ( _Yn_ ) _→ H_ ( _Y_ ) almost surely because _H_ is continuous. Hence, _g_ ( _H_ ( _Yn_ )) _→ g_ ( _H_ ( _Y_ )) almost surely because _g_ is continuous. As _g_ is bounded, the bounded convergence theorem tells us that _E_ [ _g_ ( _H_ ( _Xn_ ))] = _E_ [ _g_ ( _H_ ( _Yn_ ))] _→ E_ [ _g_ ( _H_ ( _Y_ ))] = _E_ [ _g_ ( _H_ ( _X_ ))], and the result follows from the definition of convergence in distribution. □

Note that the method used in this proof shows that almost sure convergence always implies convergence in distribution. See the class notes for a more powerful version of this theorem, called the extended continuous mapping theorem.

The continuous mapping theorem has many important applications. In particular, it can be invoked to show convergence in distribution for real-valued continuous functionals of the empirical process _Gn_ . Usually we only care such functionals, rather than the behavior of the entire random function _Gn_ in _l_<sup>_∞_</sup> ( _F_ ), and empirical process theory provides an elegant tool for answering questions of statistical interest.

For example, consider the class of indicator functions _F_ = _{_ 1(( _−∞, t_ ]) : _t ∈R}_ , and define _H_ : _l_<sup>_∞_</sup> ( _F_ ) _→R_ by _H_ ( _X_ ) = _∥X∥F_ . Clearly _H_ is continuous on ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥· ∥F_ ), so the continuous mapping theorem tells us that _H_ ( _Gn_ ) converges in distribution to _H_ ( _G_ ), for _G_ the _P_ -Brownian Bridge. Kolmogorov found the distribution of _H_ ( _G_ ) analytically, and the quantiles of this distribution can be used to form asymptotically valid confidence bands for the cumulative distribution function of _P_ .

5

---

[← Almost Sure Representation Theorem](08-almost-sure-representation-theorem.md) · [Up: contents](index.md) · [The Ordinary Delta Method →](10-the-ordinary-delta-method.md)
