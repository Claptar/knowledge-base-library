---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/150/lecture_5_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_5_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`lecture_5_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_5_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 5


David Aldous

4 September 2015

David Aldous

Lecture 5


The specific examples I’m discussing are not so important; the point of these first lectures is to illustrate a few of the 100 ideas from STAT134.

**Ideas used in Lecture 4.**


Conditional expectation as a random variable. Uses of E[E( _X |Y_ )] = E _X_ . Uniform random point in a region.


If _X_ has continuous distribution function _F_ then _F_ ( _X_ ) has uniform distribution on (0 _,_ 1). Conditioning on first step, for simple symmetric random walk.

David Aldous Lecture 5


A Markov chain ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) = ( _Xt, t ≥_ 0) is a process such that (i) each _Xt_ takes values in the same state space **States** (ii) There are numbers ( _pij , i, j ∈_ **States** ) such that

P( _Xt_ +1 = _j|Xt_ = _i, Xt−_ 1 = _it−_ 1 _, . . . X_ 0 = _i_ 0) = _pij_

for all _t, i, j_ and all ( _i_ 0 _, . . . , it−_ 1).

In words, (ii) says that at each time _t_ , probabilities for the future depend on the current state _Xt_ but not on past states.

We can consider the matrix **P** with entries ( _pij_ ). For the definition to make sense, **P** must have the properties (iii) _pij ≥_ 0 _,_ for all _i, j._

(iv)<sup>�</sup> _j_<sup>_pij_= 1</sup><sup>_,_</sup> for all _i_ .

A matrix with these properties is called a **stochastic matrix** . It is intuitively clear that, given any stochastic matrix **P** indexed by **States** , there exists the Markov chain specified by (i,ii).

David Aldous

Lecture 5


So for a Markov chain ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ )

- (ii) There are numbers ( _pij , i, j ∈_ **States** ) such that

P( _Xt_ +1 = _j|Xt_ = _i, Xt−_ 1 = _it−_ 1 _, . . . X_ 0 = _i_ 0) = _pij_

for all _t, i, j_ and all ( _i_ 0 _, . . . , it−_ 1). In this context we call **P** = ( _pij_ ) the **transition matrix** and call the _pij_ the **transition probabilities** for the chain.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

If we want to calculate a probability or expectation for a Markov chain, the answer will depend not only on **P** but also on the “initial distribution” of _X_ 0. Often we think of the initial state as non-random: _X_ 0 = _i_ 0.

David Aldous Lecture 5


We can visualize **P** as a weighted directed graph; draw edge _i → j_ if _pij >_ 0 and assign “weight” _pij_ to that edge. Then visualize the chain as a jumping particle; from present state _i_ the particle will, at the next step, jump to state _j_ with probability _pij_ .

Textbook [PK] sections 3.1-3.2 gives numerical examples of matrices with 3 or 4 states. You should read this. I do not emphasize numerics, but will do one example on the board.

I will give 5 examples – meaning an explicit set **States** and an explicit transition matrix **P** . Some of these are “toy models”, meaning we are imagining some real-world process but making a hugely over-simplified and unrealistic model. Most of the examples are in [PK] section 3.3.

David Aldous Lecture 5


**Example.** Recall **simple symmetric random walk**


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Here ( _Xt_ ) is the Markov chain with **States** = Z and


In the “gambler’s ruin” variant, where you stop on reaching _K_ or 0, we take the states as _{_ 0 _,_ 1 _,_ 2 _, . . . , K }_ and modify (*) by setting


Note the implicit convention: if _pij_ is not specified then _pij_ = 0.

David Aldous Lecture 5

---

[Up: contents](index.md) · [Example: Ehrenfest urn model. →](02-example-ehrenfest-urn-model.md)
