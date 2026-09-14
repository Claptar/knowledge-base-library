---
title: Theorem
source: https://www.stat.berkeley.edu/~aldous/150/lecture_28_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_28_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Theorem

**Source:** [`lecture_28_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_28_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_Whatever strategy you use,_ P( _next card is red_ ) = 1 _/_ 2 _._


- _At_ event “ _t_ ’th card is red. _Ft_ = information from first _t_ cards.


given _Ft_ the remaining cards are in random order, so P( _At_ +1 _|Ft_ ) = P( _A_ 52 _|Ft_ ).

- **key idea:** betting on next card is like betting on bottom card. _Mt_ = P( _A_ 52 _|Ft_ ) is a martingale.


- the time _τ_ when we make the bet (on card _τ_ + 1) is a stopping time. P(win bet _|Ft, τ_ = _t_ ) = P( _At_ +1 _|Ft, τ_ = _t_ ) = P( _A_ 52 _|Ft, τ_ = _t_ ). P(win bet _|Fτ_ ) = _Mτ_


- P(win bet) = EP(win bet _|Fτ_ ) = E _Mτ_


- but optional sampling theorem says E _Mτ_ = E _M_ 0 = E _M_ 52 = P( _A_ 52) = 1 _/_ 2.

David Aldous Lecture 28


In more advanced probability, we use the optional sampling theorem to prove a variety of **general inequalities** and **general convergence theorems** . I will give one example of each.

The basic property of a martingale was


Replacing the equality by an inequality gives two new definitions:


Letting _t_ 0 _→∞_ we can conclude


David Aldous Lecture 28


The event _{_ max _t≤t_ 0 _Xt ≥ b}_ is the event _{τ ≤ t_ 0 _}_ for the stopping time _τ_ = min _{t_ : _Xt ≥ b}._

The optional sampling theorem for supermartingales says


for stopping times _τ_<sup>_∗_</sup> . Apply to _τ_<sup>_∗_</sup> = min( _τ, t_ 0 + 1).

[continue on board]

David Aldous

Lecture 28

---

[← Other examples of martingales.](01-other-examples-of-martingales.md) · [Up: contents](index.md) · [Convergence theorems →](03-convergence-theorems.md)
