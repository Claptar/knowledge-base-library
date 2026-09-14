---
title: Ideas from previous lecture.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_17_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_17_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ideas from previous lecture.

**Source:** [`lecture_17_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_17_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Notation for studying random times (of events) over 0 _≤ t < ∞_ . Cannot have two events at the same time.


_Wk_ = time at which _k_ ’th event occurs ( _W_ 0 = 0). _Sk_ = _Wk − Wk−_ 1 is the time between successive events.


_N_ ( _t_ ) = number of events during time [0 _, t_ ].


_N_ ( _s, t_ ) = _N_ ( _t_ ) _− N_ ( _s_ ) = number of events during ( _s, t_ ].

Note that the event _{Wn ≤ t}_ is the same as the event _{N_ ( _t_ ) _≥ n}_ . So, regardless of the probability model,


David Aldous Lecture 17


David Aldous Lecture 17


**Poisson point process (PPP) of rate** _λ_ **.**

This process is defined by the properties (a) _N_ ( _s, t_ ) has Poisson( _λ_ ( _t − s_ )) distribution. (b) For disjoint intervals ( _s_ 1 _, t_ 1) _,_ ( _s_ 2 _, t_ 2) _, . . . ,_ ( _sk , tk_ ) the random variables _N_ ( _s_ 1 _, t_ 1) _, N_ ( _s_ 2 _, t_ 2) _, . . . , N_ ( _sk , tk_ ) are independent.

A more informal description in terms of infinitesimal intervals is (a’) P( event during [ _t, t_ + _dt_ ]) = _λ dt_ (b’) What happens in disjoint time intervals is independent.

The PPP is used as an over-simplified model for events that occur at “completely random” times

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

David Aldous Lecture 17

---

[Up: contents](index.md) · [Theorem →](02-theorem.md)
