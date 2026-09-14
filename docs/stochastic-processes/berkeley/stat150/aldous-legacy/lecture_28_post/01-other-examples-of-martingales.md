---
title: Other examples of martingales.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_28_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_28_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Other examples of martingales.

**Source:** [`lecture_28_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_28_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**1.** Consider the rate- _λ_ Poisson counting process ( _N_ ( _t_ ) _,_ 0 _≤ t < ∞_ ). Here


is a (continuous-time) martingale. [board]

**2. The Polya urn process.** Consider a box, initially with _r_ 0 _≥_ 1 red balls and _b_ 0 _≥_ 1 black balls. At each step, pull out a uniform random ball, and the return it into the box along with another new ball of the same color. Consider

_Mt_ = proportion of balls that are red at time _t._

Then ( _Mt_ ) is a martingale. [board]

David Aldous

Lecture 28


**3. Fisher-Wright genetic model.** (2-type, no mutation or selection) (from Lecture 5)


2 _N_ genes in each generation, of types **a** or **A** .


“children choose parents”: each gene is a copy (same type) of a uniform random gene from previous generation.

Then


is a Markov chain, with states _{_ 0 _,_ 1 _,_ 2 _, . . . ,_ 2 _N}_ and transition probabilities


- - - - - - - - - - - - - - - - - - - - - - - - - -

( _Xt_ ) is a martingale.

David Aldous

Lecture 28


Here is a counter-intuitive problem.


regular deck of cards – 26 red and 26 black. I deal, face-up.


At some time you have to bet that the next card will be red. If you bet on the first card then P(next card is red) = 1 _/_ 2. Is there a better strategy (for instance by counting the number of red/black cards dealt)?

Theorem


_Whatever strategy you use,_ P( _next card is red_ ) = 1 _/_ 2 _._


David Aldous Lecture 28

---

[Up: contents](index.md) · [Theorem →](02-theorem.md)
