---
title: 7. Inventing extra structure in a problem.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_2_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7. Inventing extra structure in a problem.

**Source:** [`lecture_2_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This sounds like cheating, but we are not “making extra assumptions”, but instead we are merely defining extra random variables to help analyze the given random variables.

Here’s an example from STAT134.

- **7a: best-out-of-** (2 _k −_ 1) **contest.** [e.g. baseball World Series]

Teams _A_ and _B_ play until one team has won _k_ games. The model is that P( _A_ beats _B_ ) = _p_ , independently for each game. The number of games played, _G_ , is random with possible values _k ≤ G ≤_ 2 _k −_ 1.

**Problem:** _Calculate_ P( _A wins series_ ) _._

David Aldous

Lecture 2


_Solution._ Imagine they play all 2 _k −_ 1 games, so _A_ wins some number of all the games, say _Y_ . The event _{A_ wins series _}_ is the same as the event _{Y ≥ k}_ . So

P( _A_ wins series ) = P( _Y ≥ k_ )

and _Y_ has Binomial(2 _k −_ 1 _, p_ ) distribution.

David Aldous Lecture 2


**7b. Put** _k ≥_ 3 **points at random (independent uniform) on the circumference of a circle. These points are the vertices of a polygon; what is the probability** _p_ ( _k_ ) **of the event**

- _G_ = _{_ the polygon does not contain the center of the circle _}_ ?

There is a simple argument based on a trick that you or I would never think of. Implement “ _k_ random points” in 2 stages.

Stage 1. Create _k_ pairs of diametrically-opposite points. Stage 2. Pick one point from each pair.

David Aldous Lecture 2


Stage 1. Create _k_ pairs of diametrically-opposite points. Stage 2. Pick one point from each pair.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Condition on the result of Stage 1. What is the conditional probability that, after the Stage 2 process, the event _A_ occurs?

By drawing a picture, the event _G_ occurs if and only if, in Stage 2, we pick _k_ adjacent points. There are 2 _k_ possible sets of such points, so


Because this is the same whatever the result of Stage 1, we have


David Aldous Lecture 2

---

[← 6. The 3rd formula for variance.](03-6-the-3rd-formula-for-variance.md) · [Up: contents](index.md) · [8. Size-biasing →](05-8-size-biasing.md)
