---
title: Lecture 26 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_26_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_26_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 26 — post

**Source:** [`lecture_26_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_26_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 26


David Aldous

28 October 2015

David Aldous

Lecture 26


For a real-valued RV _X_ and a _σ_ -field _F_ , we can define the conditional expectation E( _X |F_ ).


The **gambling interpretation** of E( _X |F_ ) is as the fair stake _Z_ to pay today in order to receive _X_ tomorrow, when _F_ is the known information,


The **abstract math definition** of E( _X |F_ ) is as the _F_ -measurable RV _Z_ such that


In the case _F_ = _σ_ ( _Y_ ) we have E( _X |F_ ) = E( _X |Y_ ) as defined before. Analogous to rules in algebra/calculus, there are many rules for manipulating conditional expectations; will develop as we go.

David Aldous Lecture 26


**Rules for manipulating conditional expectation** All RVs assumed integrable. **1.** E( _X ± Y |F_ ) = E( _X |F_ ) _±_ E( _Y |F_ )

**2.** If _X_ is _F_ -measurable then E( _X |F_ ) = _X_ .

**3.** If _X_ is independent of _F_ then E( _X |F_ ) = E _X_ .

**4.** If _W_ is _F_ -measurable then E( _WX |F_ ) = _W_ E( _X |F_ ).

**5.** If _F ⊆G_ then E[E( _X |G_ ) _|F_ ] = E( _X |F_ ). In particular E[E( _X |G_ )] = E _X_ .

David Aldous Lecture 26


Most material in this lecture is in [BZ] chapter 3, different notation. A martingale is a process ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) such that E( _Xt_ +1 _|Ft_ ) = _Xt_ for each _t ≥_ 0.

If no filtration is specified then we take the natural filtration _Ft_ = _σ_ ( _X_ 0 _, . . . , Xt_ ). A martingale represents your successive fortune in a fair game. In particular


In more advanced Probability, one studies limit theorems and inequalities for martingales, which can be used to prove results about other stochastic processes. In this course, our theory will involve **gambling strategies** and **stopping times** and the **optional sampling theorem** . We then see how to use the theory to do calculations.

David Aldous Lecture 26


Take a process ( _Mt_ ), and view it as results of 1 unit bets at each time, or the value of 1 unit of stock at the end of successive days. A **gambling strategy** is a decision, each time, of how many units to bet, or how many units of stock to hold.

Thinking of the “stock” case, suppose you can buy/sell only at end of trading on day _t_ . So the number _αt_ of shares you hold during day _t_ is chosen by you at end of day _t −_ 1 based on information known then. So


Theorem


_If_ ( _Mt_ ) _is a martingale and αt is Ft−_ 1 _-measurable for each t then_ ( _Xt_ ) _is a martingale._


[outline on board]. The conceptual point is that, with a “fair game”, there is no “system” (varying the amounts you bet each time) which makes the game favorable to you.

David Aldous Lecture 26


A **stopping time** _τ_ is a RV taking values in _{_ 0 _,_ 1 _,_ 2 _, . . ._ ; _∞}_ such that _{τ_ = _t} ∈Ft_ for each 0 _≤ t < ∞._

In words: your decision when to stop depends on past and present information only – you cannot see the future.

Most stopping times we use are defined as “the first time” something happens. Note that “the last time” is usually **not** a stopping time.

Given a process ( _Xt,_ 0 _≤ t < ∞_ ) and a stopping time _τ_ , the “stopped process” is defined as


[board: notationally more convenient to stop the process changing than to stop time.] Mathematically, this is just a simple gambling strategy, so

_If_ ( _Xt_ ) _is a martingale then the stopped process_ ( _Xt_<sup>_∗_)</sup><sup>_isamartingale._</sup>

David Aldous Lecture 26


_If_ ( _Xt_ ) _is a martingale then the stopped process_ ( _Xt_<sup>_∗_)</sup><sup>_isamartingale._</sup>

- - - - - - - - - - - - - - - - - - - - - - - - - - -

Now suppose the stopping time _τ_ is such that, for some constant _t_ 0,


Then


This is a special case of a general theorem.

David Aldous Lecture 26


Theorem (Optional Sampling Theorem) _If_ ( _Xt_ ) _is a martingale and τ is a stopping time, then (under extra technical conditions)_


Advanced Probability courses give different versions of the “extra technical conditions” – see [BZ] Theorem 3.1 for one version of these conditions. In the examples I will give, it is not hard to show the conditions hold.

The “double when you lose” strategy shows that some extra condition is necessary. [board]

**Conceptual point:** The Optional Sampling Theorem and the previous “gambling systems” theorem constitute an informal “conservation of fairness” principle: the overall results of any “system” based on fair games is like a single fair bet. Even in models not explicitly involving gambling, one can do calculations by inventing hypothetical gambling strategies and using this principle.

David Aldous Lecture 26


**Example: patterns in coin-tossing or dice-throwing.**

Throw a die until we see a specified sequence, say 5 2 5 of outcomes. This requires _τ_ throws. Calculate E _τ_ .

[board – outline below] Consider “strategy 17”:

- bet 1 that throw 17 will be “5”;

- if win (now have 6 units) bet 6 units that throw 18 will be “2”;

- if win (now have 36 units) be 36 units that throw 19 will be “5”

- if win then the game stops.

Now consider analogous “strategy _n_ ” for each 1 _≤ n ≤ τ_ . The overall gain from all these strategies works out as 216 + 6 _− τ_ . But by the “conservation of fairness” principle the expected gain must be zero. So E _τ_ = 216 + 6 = 222.

David Aldous

Lecture 26

---

[Up: contents](index.md)
