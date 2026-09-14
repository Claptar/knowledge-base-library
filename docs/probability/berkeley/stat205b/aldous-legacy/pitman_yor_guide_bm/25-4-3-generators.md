---
title: 4.3. Generators
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.3. Generators

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The _generator G_ of a Markovian semigroup ( _Pt_ ) _t≥_ 0 is the operator defined as


for suitable real-valued functions _f_ , meaning that the limit exists in some sense, e.g. the sense of convergence of functions in a suitable Banach space, such as the space _C_ 0( _E_ ) involved in the definition of Feller-Dynkin processes. Then _f_ is said to belong to the _domain of the generator_ . From (28) it follows that for _f_ in the domain of the generator


and hence


in the sense of strong differentiation and Riemann integration in a Banach space. In particular, if ( _Pt_ ) is the semigroup of Brownian motion, then it is easily verified [372, p. 6] that for _f ∈ C_ 0(R) with two bounded continuous derivatives, the generator of the standard Brownian semigroup is given by


In this case, the first equality in (29) reduces to _Kolmogorov’s backward equation_ for the Brownian transition density:


Similarly, the second equality in (29) yields _Kolmogorov’s forward equation_ for the Brownian transition density:


_J. Pitman and M. Yor/Guide to Brownian motion_

16

This partial differential equation is also known as the _heat equation_ , due to its physical interpretation in terms of heat flow [98]. Thus for each fixed _x_ the Brownian transition density function _pt_ ( _x, y_ ) is identified as the fundamental solution of the heat equation with a pole at _x_ as _t ↓_ 0. If we consider instead of standard Brownian motion _B_ a Brownian motion with drift _b_ and diffusion coefficient _σ_ , we find instead of (31) that the generator acts on smooth functions of _x_ as


This suggests that given some space-dependent drift and variance coefficients _b_ ( _x_ ) and _σ_<sup>2</sup> ( _x_ ) subject to suitable regularity conditions, a Markov process which behaves when started near _x_ like a Brownian motion with drift _b_ ( _x_ ) and variance _σ_ ( _x_ ) should have as its generator the second order differential operator


Kolmogorov [224] showed that the semigroups of such Markov processes could be constructed by establishing the existence of suitable solutions of the FokkerPlanck-Kolmogorov equations determined by this generator. More recent approaches to the existence and uniqueness of such diffusion processes involve martingales in an essential way, as we discuss in the next section.

---

[← 4.2. The strong Markov property](24-4-2-the-strong-markov-property.md) · [Up: contents](index.md) · [4.4. Transformations →](26-4-4-transformations.md)
