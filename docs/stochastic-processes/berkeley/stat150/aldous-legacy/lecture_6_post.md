---
title: Lecture 06 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_6_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_6_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 06 — post

**Source:** [`lecture_6_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_6_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 6


David Aldous

9 September 2015

David Aldous

Lecture 6


# **Ideas used in Lecture 5.**


Transition matrix **P** = ( _pij_ ) on a state space **States** = _{i, j, k, . . .}_ . Definition of Markov chain ( _Xt, t_ = 0 _,_ 1 _,_ 2 _, . . ._ ). Simple examples of Markov chains.

We now start to develop the math theory of Markov chains. This material is in Chapter 3 of textbook [PK].

David Aldous Lecture 6


Write _µi_ ( _t_ ) = P( _Xt_ = _i_ ) and regard _µ_ ( _t_ ) = ( _µi_ ( _t_ ) _, i ∈_ **States** ) as a row-vector. The relationship between _µ_ ( _t_ ) and _µ_ ( _t −_ 1) is


In vector-matrix notation this is


This implies that the individual entries _pij_<sup>(</sup><sup>_t_)</sup> of **P**<sup>(</sup><sup>_t_)</sup> have the meaning


David Aldous Lecture 6


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**Question:** So what is the interpretation of column-vectors? What does


mean for a column vector _h_ = ( _hj , j ∈_ **States** )?

**Answer:** Think of _h_ as a function _h_ : **States** _→_ R and then consider


Then the vector _h_ ( _t_ ) = ( _hi_ ( _t_ ) _, i ∈_ **States** ) is given by (*).

David Aldous

Lecture 6


Calculating **P**<sup>(</sup><sup>_t_)</sup> with pencil-and-paper is only possible in very simple or special cases. Consider a 2-state chain


with 0 _< a, b <_ 1. Here we can calculate [on board]


David Aldous Lecture 6


For **theory** , we are given a Markov chain ( _X_ 0 _, X_ 1 _, . . ._ ) on **States** with a given transition matrix **P** .

**Theory: Conditioning on first step.**

The method we used for simple symmetric random walk works for a Markov chain. For a subset _A ⊂_ **States** consider the **hitting time** _TA_ = min _{t ≥_ 0 : _Xt ∈ A}_

Maybe never hit, in which case we define _TA_ = _∞_ ; for now assume we know _TA < ∞_ . We study


introducing notation E _i_ ( _·_ ) and P _i_ ( _·_ ) for initial state _i_ . By conditioning on the first step,


David Aldous Lecture 6


Consider disjoint subsets _A, B_ of **States** – maybe _A_ = _{a}_ and _B_ = _{b}_ . Let’s study


the probability starting at _i_ of hitting _A_ before hitting _B_ . We have


and by conditioning on the first step


Do these equations have a unique solution? Logically, the chain either hits _A_ before _B_ , or hits _B_ before _A_ , or never hits either. So consider


for which the corresponding equations are


If _g_ solves equations (2,3) then so does _g_ + _g_<sup>_∗_</sup> and so the solution is not unique, unless _g_<sup>_∗_</sup> _≡_ 0, that is unless the chain **always** <u>hits</u> _A_ ~~<u>o</u>~~ r _B_ ~~<u>.</u>~~

David Aldous Lecture 6


**Conceptual point:** often we answer problems by writing down equations and then solving them, but to be more precise we should check the solution is unique.

In the particular case of previous slide, one can prove that, provided

P _i_ ( never hit _A_ or _B_ ) = 0

there is indeed a unique solution.

I will do one numerical example – Exercise 3.4.3 of [PK] – on the board.

David Aldous Lecture 6


Here is another simple example.

**Throw a fair die until getting two 6’s in succession. This requires some random number** _T_ **of throws. Calculate** E _T_ **.** This can be done by defining a Markov chain as follows. _Xt_ = 0 if the _t_ ’th throw is not 6. _Xt_ = 1 if the _t_ ’th throw is 6 but the previous throw was not 6. _Xt_ = 2 if the _t_ ’th throw is 6 and the ( _t −_ 1) throw was 6. This chain has states _{_ 0 _,_ 1 _,_ 2 _}_ and


We can set up and solve [on board] the equations for


We find _h_ (1) = 36 and _h_ (0) = 42, and the answer is the 42.

David Aldous Lecture 6

---

[Up: contents](index.md)
