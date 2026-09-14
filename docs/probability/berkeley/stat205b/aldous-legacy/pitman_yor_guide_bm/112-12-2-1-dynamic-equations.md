---
title: 12.2.1. Dynamic Equations
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12.2.1. Dynamic Equations

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We consider _dynamic equations_ of the form


We show that the _C_<sup>2</sup> solutions of this equation are of the form


If _c, u_ is bounded, then _Ms_ above is a bounded martingale. The martingale convergence theorem implies that as _s ↗ t_ , _Ms → Mt_ . Since _u_ is continuous and _u_ (0 _, x_ ) = _f_ ( _x_ ), we must have


So we have


We have seen that the solution to


68


is


So if _f_ = 1, we have E _x_ ( _τD_ ) is the solution of


For example, if _D_ = _B_ (0 _,_ 1), then the solution is (1 _−|x|_<sup>2</sup> ) _/n_ , _⇒_ E _x_ ( _τD_ ( _x,_ 1)) = (1 _−|x|_<sup>2</sup> ) _/n_ .

---

[← 12.2. Stochastic differential Equations](111-12-2-stochastic-differential-equations.md) · [Up: contents](index.md) · [12.3. Potential theory →](113-12-3-potential-theory.md)
