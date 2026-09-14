---
title: Birth-and-death chains.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_21_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_21_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Birth-and-death chains.

**Source:** [`lecture_21_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_21_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

These have states _{_ 0 _,_ 1 _,_ 2 _, . . . , N}_ or _{_ 0 _,_ 1 _,_ 2 _, . . . . . .}_ and the only transitions are _i → i ±_ 1. Write


For these chains we can solve the detailed balance equations: [board]


So the stationary distribution is


provided (in the infinite-state case) _w < ∞_ .

**Example.** Take _λi_ = _λ, µi_ = _µi_ . Then [board] _π_ is the Poisson( _λ/µ_ ) distribution.

David Aldous Lecture 21


Note that if the stationary distribution _π_ exists for an infinite-state birth-and-death process, then for the same process on states _{_ 0 _,_ 1 _,_ 2 _, . . . , N}_ the stationary distribution is


In other words, taking _π_ as the distribution of a RV _Z_ , _π_<sup>[</sup><sup>_N_]</sup> is the conditional distribution of _Z_ given _{Z ≤ N}_ .

David Aldous Lecture 21


**More theory – similar to discrete-time setting.** [Assume chain is irreducible, and either finite-state or infinite state and positive-recurrent, so a unique stationary distribution _π_ exists.] For any initial distribution, P( _X_ ( _t_ ) = _i_ ) _→ πi_ as _t →∞_ . Writing _Ni_ ( _t_ ) = length of time chain spends in state _i_ during [0 _, t_ ], we have _Ni_ ( _t_ ) _/t → πi_ as _t →∞_ . E _i Ti_<sup>+</sup> = 1 _/_ ( _πi qi_ ), where _Ti_<sup>+</sup> is the first **return time** to _i_ (after leaving _i_ ).

Note we don’t need “aperiodic” in the first result. The third result can be seen by a general “cycle argument” [next slide and board].

David Aldous Lecture 21


David Aldous Lecture 21

---

[← Example: Yule process](02-example-yule-process.md) · [Up: contents](index.md)
