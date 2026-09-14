---
title: 12.2. Stochastic differential Equations
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12.2. Stochastic differential Equations

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In order to consider more general PDEs, we need to introduce the notion of a _stochastic differential equations (SDEs)_ . We say that the semimartingale _X_ solves the SDE


if


Solutions to three equations exist in particular when _σ_ and _b_ are bounded and Lipschitz. The proof is based on Picard’s iteration.

**Claim 1.** _If Xt solves (124), then_


_where_


_and a_ = _σσ_<sup>_T_</sup> _, is a martingale. Proof._


So by Itˆo’s formula,


Now assume that _u ∈ C_<sup>2</sup> ( _D_ ) _∩ C_ ( _D_ ) is a solution of

_−Au_ ( _X_ ) = _f_ ( _X_ ) in _D,_ and _u_ = 0 on _∂D._

67

_J. Pitman and M. Yor/Guide to Brownian motion_

Then _u_ ( _x_ ) = E _x_ ��0 _τD f_ ( _Xs_ ) _ds_ �. By Itˆo,


Now taking expectation and limit as _t →∞_ ,

and so

---

[← 12.1.5. Non-linear problems](110-12-1-5-non-linear-problems.md) · [Up: contents](index.md) · [12.2.1. Dynamic Equations →](112-12-2-1-dynamic-equations.md)
