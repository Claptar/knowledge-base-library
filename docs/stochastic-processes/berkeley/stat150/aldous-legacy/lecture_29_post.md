---
title: Lecture 29 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_29_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_29_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 29 — post

**Source:** [`lecture_29_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_29_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 29


David Aldous

6 November 2015

David Aldous

Lecture 29


We have seen two kinds of “purely random” process:


coin-tossing, dice-throwing, etc – IID sequences. Poisson process of random points in _d_ dimensions.

A third kind one might imagine is


a “purely random” continuous function.

It is not obvious what this means. To start, consider simple symmetric random walk


For large _n_ , how can we draw the graph of ( _S_ 0 = 0 _, S_ 1 _, . . . , Sn_ ) on “unit size” paper?

[board]

Know E _Sn_ = 0 and s.d.( _Sn_ ) =<sup>_√_</sup> _<u>n</u>_ .

David Aldous Lecture 29


The picture suggests that the “scaling limit” [jargon!] of the random walk is a process ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) with the property **1.** _B_ ( _t_ ) has Normal(0,t) distribution.

It turns out there is a mathematical object called “standard Brownian motion” (BM) with properties (1) and

**2.** _B_ ( _t_ ) _− B_ ( _s_ ) has Normal(0,t-s) distribution ( _s < t_ ).

**3.** For _s_ 1 _< t_ 1 _≤ s_ 2 _< t_ 2 _≤ . . . ≤ sk < tk_ the increments _B_ ( _t_ 1) _− B_ ( _s_ 1) _, . . . , B_ ( _tk_ ) _− B_ ( _sk_ ) are independent.

**4.** The sample paths _t → B_ ( _t_ ) are (random) continuous functions of _t_ .

Keep in mind this is a **model** – looking at some time-varying real-world quantity, it may or may not behave like this BM model.

One example which does fit the model quite well is short-term stock prices [show].

As the stock price graphs suggest, although continuous the sample paths are irregular – not differentiable.

David Aldous Lecture 29


BM is important because

> 1 one can do many explicit calculations.

> 2 it is a “building block” for defining other random processes. This part of the course is more “mathematical” in the sense of emphasizing calculations rather than toy models. Here is a very simple instance of (1).

David Aldous Lecture 29


Given parameters _−∞ < µ < ∞_ and 0 _< σ < ∞_ we can define


called _Brownian motion with drift rate µ and variance rate σ_<sup>2</sup> . In particular _X_ (1) has Normal( _µ, σ_<sup>2</sup> ) distribution. The appearance of the Normal distribution is not arbitrary (cf. the Poisson distribution in the Poisson process), as shown by the next theorem.

Theorem


_If a process X_ ( _t_ ) _,_ 0 _≤ t < ∞ has X_ (0) = 0 _, continuous sample paths, and (for each a >_ 0 _) the increments X_ ( _a_ ) _, X_ (2 _a_ ) _− X_ ( _a_ ) _, X_ (3 _a_ ) _− X_ (2 _a_ ) _, . . . are IID, then the process must be BM with some drift and variance rates._


This is a consequence of the CLT.

David Aldous Lecture 29


Explicit formulas for BM will ultimately be based on the Normal density formula, but first let us see some “structural properties” of BM. Write = _d_ for “equal in distribution”.

**1: Symmetry.** ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) = _d_ ( _−B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ). **2: Markov.** Given _t_ 0 and the “past” ( _B_ ( _t_ ) _,_ 0 _≤ t ≤ t_ 0), the “future” process _B_<sup>�</sup> ( _u_ ) = ( _B_ ( _t_ 0 + _u_ ) _− B_ ( _t_ 0) _,_ 0 _≤ u < ∞_ ) has the distribution of BM and is independent of the past process.

**3: Scaling.** For _c >_ 0 the “scaled” process _B_ �( _u_ ) = ( _c_<sup>_−_1</sup><sup>_/_2</sup> _B_ ( _cu_ ) _,_ 0 _≤ u < ∞_ ) has the distribution of BM. [show Wikipedia demo]

**4: Martingale.** ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) is a martingale.

David Aldous Lecture 29


# **Recall facts about the Normal density.**


is the density of a “standard Normal(0 _,_ 1)” RV _Z_ . Write the distribution function as


We have


A few lines of calculus show [board]


Calculations with _B_ ( _t_ ) easily done by scaling: _B_ ( _t_ ) = _d t_<sup>1</sup><sup>_/_2</sup> _Z_ and so (for instance) E _|B_ ( _t_ ) _|_ = �2 _t/π_ . The general relation


gives the density of _B_ ( _t_ )

_fB_ ( _t_ )( _x_ ) = _t_<sup>_−_1</sup><sup>_/_2</sup> _φ_ ( _t_<sup>_−_1</sup><sup>_/_2</sup> _x_ ) = (2 _πt_ )<sup>_−_1</sup><sup>_/_2</sup> exp( _−x_<sup>2</sup> _/_ (2 _t_ )) _, −∞ < x < ∞._

David Aldous Lecture 29

---

[Up: contents](index.md)
