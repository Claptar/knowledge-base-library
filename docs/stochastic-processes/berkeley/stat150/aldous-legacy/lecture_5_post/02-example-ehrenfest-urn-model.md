---
title: 'Example: Ehrenfest urn model.'
source: https://www.stat.berkeley.edu/~aldous/150/lecture_5_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_5_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Example: Ehrenfest urn model.

**Source:** [`lecture_5_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_5_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- 2 boxes, 2 _a_ balls, each ball in one of the boxes. Each step, pick uniform random ball and move to other box.

Consider _Yt_ = number of balls in left box after _t_ steps, **States** = _{_ 0 _,_ 1 _,_ 2 _, . . . ,_ 2 _a}_ .


David Aldous Lecture 5


**Example: Fisher-Wright genetic model.** (2-type, no mutation or selection).


2 _N_ genes in each generation, of types **a** or **A** . “children choose parents”: each gene is a copy (same type) of a uniform random gene from previous generation.

Then

_Xt_ = number of type- **a** in generation _t_

is a Markov chain, with states _{_ 0 _,_ 1 _,_ 2 _, . . . ,_ 2 _N}_ and transition probabilities


David Aldous Lecture 5


Queue models are more naturally set up in continuous time, but here is a **Discrete time queue model.**


Service takes unit time for each customer.


If no customer, server takes a break for unit time. _ξt_ new customers arrive during time [ _t −_ 1 _, t_ ]. Model ( _ξ_ 1 _, ξ_ 2 _, . . ._ ) as i.i.d.

Consider

_Xt_ = number of customers at time _t_ .

Clearly _Xt_ = ( _Xt−_ 1 _−_ 1)<sup>+</sup> + _ξt._

Here ( _Xt_ ) is a Markov chain on states _{_ 0 _,_ 1 _,_ 2 _, . . .}_ = Z<sup>+</sup> with transition probabilities

_p_ 0 _j_ = P( _ξ_ = _j_ ) _, j ≥_ 0 _pij_ = P( _ξ_ = _j − i_ + 1) _, i ≥_ 1 _, j ≥ i −_ 1 _._

David Aldous Lecture 5

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Example: Umbrellas. →](03-example-umbrellas.md)
