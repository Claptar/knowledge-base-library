---
title: Lecture 30 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_30_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_30_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 30 — post

**Source:** [`lecture_30_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_30_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 30


David Aldous

9 November 2015

David Aldous

Lecture 30


It turns out there is a mathematical object ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) called “standard Brownian motion” (BM) with properties

**1.** _B_ ( _t_ ) has Normal(0,t) distribution.

**2.** _B_ ( _t_ ) _− B_ ( _s_ ) has Normal(0,t-s) distribution ( _s < t_ ).

**3.** For _s_ 1 _< t_ 1 _≤ s_ 2 _< t_ 2 _≤ . . . ≤ sk < tk_ the increments _B_ ( _t_ 1) _− B_ ( _s_ 1) _, . . . , B_ ( _tk_ ) _− B_ ( _sk_ ) are independent.

**4.** The sample paths _t → B_ ( _t_ ) are (random) continuous functions of _t_ .

Keep in mind this is a **model** – looking at some time-varying real-world quantity, it may or may not behave like this BM model. BM is important because

> 1 one can do many explicit calculations.

> 2 it is a “building block” for defining other random processes.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

David Aldous Lecture 30


We will study the first hitting time to position _b >_ 0


and the maximum up to time _t_


Note – an idea we have seen before –

the event _{M_ ( _t_ ) _≥ b}_ is the event _{Tb ≤ t}._

So the distribution of either _Tb_ or _M_ ( _t_ ) determines the other:


We can calculate these distributions – and more – using the **reflection principle** . I will give a more general formulation than [PK] sec. 8.2.1.

David Aldous Lecture 30


Theorem (from general reflection principle) P( _Tb ≤ t, B_ ( _t_ ) _≥ b_ + _a_ ) = P( _Tb ≤ t, B_ ( _t_ ) _≤ b − a_ ); _a, b >_ 0 _._ [picture on board] We can deduce quite a lot of information from this identity. Set _a_ = 0; we can then argue [board]


which can be rewritten as


So from last class


David Aldous Lecture 30


We will find an explicit probability density for _Tb_ below. First note an interesting “paradox”. From the Markov property


But from scaling


So for integer _k ≥_ 2 we have


How can this happen?

David Aldous Lecture 30


Use (*) to see

P( _Tb ≤ t_ ) = P( _M_ ( _t_ ) _≥ b_ ) = 2P( _B_ ( _t_ ) _≥ b_ ) = 2Φ(<sup>¯</sup> _b/t_<sup>1</sup><sup>_/_2</sup> ) _._

Differentiate w.r.t. _t_ to get


[sketch on board] and note E _Tb_ = _∞_ .

Another calculation will give us the joint density of ( _M_ ( _t_ ) _, B_ ( _t_ )). The reflection principle tells us (changing notation)

P( _B_ ( _t_ ) _≥ a_ + _c_ ) = P( _M_ ( _t_ ) _≥ a, B_ ( _t_ ) _≤ a − c_ ); _a, c >_ 0 _._

Set _b_ = _a − c_ :


Write the right side in terms of Φ<sup>¯</sup> and differentiate twice

David Aldous Lecture 30


This is complicated, but there are two interesting consequences.


[board]

David Aldous Lecture 30

---

[Up: contents](index.md)
