---
title: Lecture 25 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_25_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_25_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 25 — post

**Source:** [`lecture_25_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_25_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 25 David Aldous


26 October 2015

David Aldous

Lecture 25


- The collection of all events determined by a family ( _W , X , Y , Z_ ) is called _σ_ ( _W , X , Y , Z_ )


- A RV _T_ whose value is determined by the values of ( _W , X , Y , Z_ ) is called _σ_ ( _W , X , Y , Z_ )-measurable.


- A _σ_ -field _F_ of events is regarded as “information”.


- _F ⊆G_ means: if _A ∈F_ then _A ∈G_ . So _G_ contains more information than _F_ .


- A sequence _F_ 0 _⊆F_ 1 _⊆F_ 2 _⊆ . . ._ is called a **filtration** . _Ft_ is the _σ_ -field of known events at time _t_ , and saying a RV _Y_ is _Ft_ -measurable means we know the value of _Y_ at time _t_ .

David Aldous

Lecture 25


[BZ] exercise 3.1 - [board]

A sequence of coin tosses. _Ft_ tells us the results of the first _t_ tosses. Which is the smallest _t_ such that _Ft_ contains the following event.

_C_ = _{_ the first 100 tosses produce the same outcome _}_ . _A_ = _{_ the first occurrence of heads is preceded by at most 10 tails _}_ . _B_ = _{_ there is at least one head in the infinite sequence _} D_ = _{_ no more than 2 heads and 2 tails in the first 5 tosses _}_ . Note this is just “logic” – no probability.

David Aldous Lecture 25


For a real-valued RV _X_ and a _σ_ -field _F_ , we can define the conditional expectation E( _X |F_ ).


The **gambling interpretation** of E( _X |F_ ) is as the fair stake _Z_ to pay today in order to receive _X_ tomorrow, when _F_ is the known information,


The **abstract math definition** of E( _X |F_ ) is as the _F_ -measurable RV _Z_ such that


In the case _F_ = _σ_ ( _Y_ ) we have E( _X |F_ ) = E( _X |Y_ ) as defined before. Analogous to rules in algebra/calculus, there are many rules for manipulating conditional expectations; will develop as we go.

David Aldous Lecture 25


Most material in this lecture is in [BZ] chapter 3, different notation. A martingale is a process ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) such that E( _Xt_ +1 _|Ft_ ) = _Xt_ for each _t ≥_ 0.

If no filtration is specified then we take the natural filtration _Ft_ = _σ_ ( _X_ 0 _, . . . , Xt_ ).

**Examples of martingales** - check on board **(A).** If _X_ 1 _, X_ 2 _, . . ._ are independent, E _Xi_ = 0 and _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_then</sup> (0 = _S_ 0 _, S_ 1 _, S_ 2 _, . . ._ ) is a martingale.


**(B).** If _Y_ 1 _, Y_ 2 _, . . ._ are independent, E _Yi_ = 1 and _Mn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Yi_then</sup>


David Aldous Lecture 25


**(C).** In the Galton-Watson branching process with offspring distribution _ξ_ , let _Zn_ be the population in generation _n_ . Write _µ_ = E _ξ_ . Then


**(D).** Given a filtration ( _Ft_ ), for **any** RV _X_ with E _|X | < ∞_ we can consider _Mt_ = E( _X |Ft_ ) and then


Recalling P( _A_ ) = E1 _A_ , we can define conditional probability given a _σ_ -field by P( _A|F_ ) = E(1 _A|F_ ), and then for **any** event _A_


Later we’ll see how this works with real-world future events, Also relevant to mathematical study of models. Recall (Lecture 6) “first step analysis” of a Markov chain ( _Xt_ ) with **P** = ( _pij_ ).

David Aldous Lecture 25


Consider disjoint subsets _A, B_ of States – maybe _A_ = _{a}_ and _B_ = _{b}_ . Let’s study _g_ ( _i_ ) = P _i_ ( _TA < TB_ )

the probability starting at _i_ of hitting _A_ before hitting _B_ . We have


and by conditioning on the first step


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

In Lecture 6 we discussed solving these equations. Here we observe (explain _TA∪B_ later) **(E).** ( _g_ ( _Xt_ ) _,_ 0 _≤ t ≤ TA∪B_ ) is a martingale.

Conceptual point: “solving these equations” is the same as “find a function _g_ : States _→_ R such that _g_ ( _Xt_ ) is a martingale”.

David Aldous Lecture 25


**Rules for manipulating conditional expectation** All RVs assumed integrable. **1.** E( _X ± Y |F_ ) = E( _X |F_ ) _±_ E( _Y |F_ )

**2.** If _X_ is _F_ -measurable then E( _X |F_ ) = _X_ .

**3.** If _X_ is independent of _F_ then E( _X |F_ ) = E _X_ .

**4.** If _W_ is _F_ -measurable then E( _WX |F_ ) = _W_ E( _X |F_ ).

**5.** If _F ⊆G_ then E[E( _X |G_ ) _|F_ ] = E( _X |F_ ). In particular E[E( _X |G_ )] = E _X_ .

David Aldous Lecture 25

---

[Up: contents](index.md)
