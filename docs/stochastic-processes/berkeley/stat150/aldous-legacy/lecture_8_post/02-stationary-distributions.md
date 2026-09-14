---
title: Stationary distributions
source: https://www.stat.berkeley.edu/~aldous/150/lecture_8_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_8_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stationary distributions

**Source:** [`lecture_8_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_8_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Recall the distribution _µ_ ( _t_ ) of _Xt_ evolves as _µ_ ( _t_ ) = _µ_ ( _t −_ 1) **P** in vector-matrix notation. So suppose a probability distribution _π_ = ( _πi , i ∈_ **States** ) satisfies


If the chain has initial (time-0) distribution _µ_ (0) = _π_ then _µ_ ( _t_ ) = _π_ for every time _t_ . A distribution _π_ satisfying (1) is called **stationary** . This language is a bit confusing, when we imagine a Markov chain as a particle jumping between states. The particle continues to move even when we have a stationary distribution; **stationary** refers to the fact that the **probabilities** (of where the particle is at time _t_ ) do not change with time _t_ .

We will soon see theory relating long-term behavior of a Markov chain to its stationary distribution. First we look at some examples where we can easily find the stationary distribution.

David Aldous Lecture 8


Two remarks.

- (1) The notion of stationary distribution is also useful when the number of states is infinite, though some of our theorems assume a finite number of states.


and then _normalizing_ by setting


If the number of states is infinite, this only works if _w < ∞_ .

David Aldous Lecture 8

---

[← Ideas used in Lecture 7.](01-ideas-used-in-lecture-7.md) · [Up: contents](index.md) · [Special setting: Doubly stochastic chains →](03-special-setting-doubly-stochastic-chains.md)
