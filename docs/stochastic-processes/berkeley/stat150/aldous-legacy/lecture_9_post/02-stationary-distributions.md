---
title: Stationary distributions
source: https://www.stat.berkeley.edu/~aldous/150/lecture_9_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_9_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stationary distributions

**Source:** [`lecture_9_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_9_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Recall the distribution _µ_ ( _t_ ) of _Xt_ evolves as _µ_ ( _t_ ) = _µ_ ( _t −_ 1) **P** in vector-matrix notation. So suppose a probability distribution _π_ = ( _πi , i ∈_ **States** ) satisfies


If the chain has initial (time-0) distribution _µ_ (0) = _π_ then _µ_ ( _t_ ) = _π_ for every time _t_ . A distribution _π_ satisfying (2) is called **stationary** . This language is a bit confusing, when we imagine a Markov chain as a particle jumping between states. The particle continues to move even when we have a stationary distribution; **stationary** refers to the fact that the **probabilities** (of where the particle is at time _t_ ) do not change with time _t_ .

David Aldous Lecture 9


If _µ_ ( _t_ ) and _µ_ ( _∞_ ) are probability distributions on **States** , then convergence _µ_ ( _t_ ) _→ µ_ ( _∞_ ) as _t →∞_ means _µi_ ( _t_ ) _→ µi_ ( _∞_ ) as _t →∞_ for each _i ∈_ **States** .

So if _µ_ ( _t_ ) is the distribution of _X_ ( _t_ ) then _µ_ ( _t_ ) _→ µ_ ( _∞_ ) means

_µi_ ( _t_ ) = P( _X_ ( _t_ ) = _i_ ) _→ µi_ ( _∞_ ) for each _i ∈_ **States** _._ (3)

**Suppose** that for a chain with transition matrix **P** we know (3) holds. Then (3) implies _µ_ ( _t_ + 1) = _µ_ ( _t_ ) **P** _→ µ_ ( _∞_ ) **P**

which implies, because _µ_ ( _t_ + 1) _→ µ_ ( _∞_ ),


That is, the limit distribution of _X_ ( _t_ ), if it exists, must be a stationary distribution, which we will now call _π_ .

David Aldous Lecture 9

---

[← Ideas used in Lecture 8.](01-ideas-used-in-lecture-8.md) · [Up: contents](index.md) · [Mean occupation times. Consider a state i and time t . →](03-mean-occupation-times-consider-a-state-i-and-time-t.md)
