---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/205B/lecture_1.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/lecture_1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`lecture_1.pdf`](https://www.stat.berkeley.edu/~aldous/205B/lecture_1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Admin and Lecture 1: Recap of Measure Theory


David Aldous

January 16, 2018


I don’t use bCourses:


Read web page (search `Aldous 205B` )

Web page rather unorganized – some topics done by Nike in 205A – will post homeworks soon.

I am **not** following Durrett text section-by-section.

After today – math on blackboard. Start today with conceptual review of measure theory [MT] – emphasizing stuff books don’t tell you.


**On measure theory [MT] and probability theory [PT]**

**1.**

_At a purely formal level, one could call probability theory the study of measure spaces with total measure one, but that would be like calling number theory the study of strings of digits which terminate._ [Terry Tao]

My own analogy is

_MT is like an operating system for PT_

and like any good OS it should be _transparent_ . There’s another Terry Tao quote about “3 stages of learning math” . . . . . .

You _shouldn’t_ start a research paper with (Ω _, F,_ P); it’s just there in the background.

_Historical digression:_ In retrospect, what was Kolmogorov’s insight?


While Probability certainly involves some conceptually extra idea (relative to the rest of Mathematics), the issue (100 years ago) was whether Probability required some new technical ingredient to be added to the rest of Mathematics. Kolmogorov’s achievement was the realization that it didn’t. Measure theory had been recently developed to resolve the technical conflict between the intuitive idea ”every region in the plane has some area” and the axioms of set theory dealing with every subset of an uncountable set. This conflict has no conceptual connection with Probability, but Kolmogorov realized that the technical machinery (involved in its resolution) of measures, measurable sets, measurable functions could be reused as an axiomatic setting for Probability. In retrospect, because one special model within Probability is ”pick a uniform random point from the unit square”, it is clear that any general theory of Probability has to include measure theory, but (to reiterate) Kolmogorov’s achievement was the realization that at the technical level it didn’t require anything more.


**2.** Regarding MT:


Not much is needed for most PT. Mostly it’s clever definitions; only hard theorem is existence of Lebesgue measure.


It’s rather magical that integration theory works so very generally (no topology needed) . . . . . . . . . . . . I will explain the secret reason why.

[show picture of measurable f: forwards/backwards]


**3.** Two illustrative contexts where MT helps: (a) For R-valued _X_


- (b) lim sup _n Xn_ is a random variable !

- (b) illustrates point that MT closed under (many) countable limits


**4.** You need to understand, both formally and intuitively, the relations between random variables (RV) and distributions (PM).

- Any RV (general space _S_ ) has a distribution.

- In MT one typically deals with given arbitrary PMs.

- In PT we usually think of a PM as arising as the distribution of a RV.

- **Think in terms of RVs rather than PMs whenever you can.** Here are some aspects of this relationship.

- **(a).** For a PM _µ_ on R, take _U_ uniform(0 _,_ 1) and then

_Fµ_<sup>_−_1(</sup><sup>_U_)</sup><sup>_∼µ._</sup>

**Definition:** A measurable space ( _S, S_ ) is _nice_ if it is isomorphic to a Borel subset _B_ of R.

[explain on board]

**Background fact:** Every space you ever encounter will be a _nice_ space.

**Corollary:** For any PM _µ_ on any nice space _S_ , there is a measurable function _Gµ_ : [0 _,_ 1] _→ S_ such that _Gµ_ ( _U_ ) _∼ µ_ . (But aside from R no canonical choice).


**(b).** For two PMs _µ, ν_ on R the property _ν_ ( _−∞, x_ ] _≥ µ_ ( _−∞, x_ ] _∀x_

is equivalent to


and a canonical choice is


This is _stochastic order ν ⪯ µ_ .


**(c).** For two PMs _µ, ν_ on R with finite means the property


is equivalent to


This is _convex order ν ⪯ µ_ . This result not so easy; and there is no canonical choice.


with relation


the _inf_ over joint distributions with _Xµ ∼ µ, Xν ∼ ν_ . The _inf_ is attained by joint distributions with P( _Xν_ = _Xµ_ = _i_ ) = min( _µi , νi_ ).


Recall an application. By calculation


which easily implies **Le Cam’s theorem** : _For independent Bernouilli(pi ) RVs ξi ,_


These are all examples of _coupling_ , which means (in the wide sense) getting information about a relation between distributions by constructing (dependent) RVs with those distributions.


**5.** Alternative (better!) approach to some 205A theory.


Here **b** takes Lebesgue measure on [0 _,_ 1] to fair-coin-tossing measure (product Bernoulli (1/2)) on _{_ 0 _,_ 1 _}_<sup>_∞_</sup> ), and **s** takes it back. In RV terms, for uniform _U_ and product Bernoulli **B** = ( _Bi_ )


[Imagine idealized RNGs].


Now we do a trick. Take disjoint infinite subsets _S_ 1 _, S_ 2 _, . . ._ of _{_ 1 _,_ 2 _,_ 3 _, . . .}_ and write _Si_ = _{si_ 1 _, si_ 2 _, . . .}_ and define _Ui_ = **s** ( _Bsij , j ≥_ 1) _, i_ = 1 _,_ 2 _, . . ._

This gives an infinite sequence of IID uniform(0 _,_ 1) RVs.

Recall **Corollary:** For any PM _µ_ on any nice space _S_ , there is a measurable function _Gµ_ : [0 _,_ 1] _→ S_ such that _Gµ_ ( _U_ ) _∼ µ_ . Now we can conclude **infinite product measure** _µ_ 1 _× µ_ 2 _× . . ._ exists because it is the distribution of ( _Gµ_ 1 ( _U_ 1) _, Gµ_ 2 ( _U_ 2) _, . . ._ ). This is much simpler than usual MT proofs for _µ_ 1 _× µ_ 2 (though only for _nice_ spaces). Note an interpretation of the Corollary: if it were false there would be PMs one could not simulate even in infinite time from an idealized RNG.

---

[Up: contents](index.md) · [Recall →](02-recall.md)
