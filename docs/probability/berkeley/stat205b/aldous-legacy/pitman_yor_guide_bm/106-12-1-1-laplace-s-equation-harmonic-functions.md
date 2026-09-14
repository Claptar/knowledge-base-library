---
title: '12.1.1. Laplace’s equation: harmonic functions'
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12.1.1. Laplace’s equation: harmonic functions

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We begin by considering Laplace’s equation:

∆ _u_ = 0 _._

63

_J. Pitman and M. Yor/Guide to Brownian motion_

where ∆ _u_ :=<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_uxi,xi_.A</sup><sup>_harmonicfunction_isa</sup><sup>_C_2function</sup><sup>_u_whichsolves</sup> Laplace’s equation.

Let _D_ ( _x, r_ ) := _{y_ : _|y − x| < r}_ and let _D_ be a _domain_ , that is a connected open subset of R<sup>_n_</sup> . Let _τD_ := inf _{t_ : _Bt ∈ D_<sup>_c_</sup> _}_ . Since each component of a Brownian motion _B_ in R<sup>_n_</sup> is a.s. unbounded, _P_ ( _τD < ∞_ ) = 1 for any bounded domain _D_ . If _u_ is harmonic in _D_ , then


for every _x ∈ D_ and _r >_ 0 such that _D_ ( _x, r_ ) _⊂ D_ , where _S_ is the uniform probability distribution on _∂D_ ( _x, r_ ) which is invariant under orthogonal transformations. To see this, observe that by Itˆo’s formula,


which is a continuous local martingale. But since _u_ ( _Bt∧τD_ ( _x,r_ )) _−u_ ( _x_ ) is uniformly bounded, it is a true martingale with mean 0. Taking expectation and using _P_ ( _τD_ ( _x,r_ ) _< ∞_ ) = 1 gives


where the last equality is by the symmetry of Brownian motion with respect to orthogonal transformations. Conversely, if _u_ : _D →_ R has this mean value property, then _u_ is _C_<sup>_∞_</sup> and harmonic. (Gauss’s theorem).

---

[← 12.1. Partial differential equations](105-12-1-partial-differential-equations.md) · [Up: contents](index.md) · [12.1.2. The Dirichlet problem →](107-12-1-2-the-dirichlet-problem.md)
