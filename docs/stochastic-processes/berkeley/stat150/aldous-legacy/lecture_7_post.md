---
title: Lecture 07 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_7_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_7_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 07 — post

**Source:** [`lecture_7_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_7_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 7


David Aldous

11 September 2015

David Aldous

Lecture 7


**Ideas used in Lecture 6.** Markov chain ( _Xt, t_ = 0 _,_ 1 _,_ 2 _. . ._ ) with transition matrix **P** . _µ_ ( _t_ ) = _µ_ (0) **P**<sup>(</sup><sup>_t_)</sup> gives distribution _µ_ ( _t_ ) of _Xt_ . _f_ ( _t_ ) = **P**<sup>(</sup><sup>_t_)</sup> _f_ gives _fi_ ( _t_ ) = E _i f_ ( _Xt_ ). _h_ ( _i_ ) = E _i TA_ can be found as solution of first-step equation _h_ ( _i_ ) = 1 +<sup>�</sup> _j_<sup>_pijh_(</sup><sup>_j_).</sup> _g_ ( _i_ ) = P _i_ ( _TA < TB_ ) can be found as solution of first-step equation _g_ ( _i_ ) =<sup>�</sup> _j_<sup>_pijg_(</sup><sup>_j_).</sup>

There are some special chains where one **can** find analytic solutions to these first-step equations. I will do some in this lecture, and others are in the homework.

David Aldous Lecture 7


**Example: Simple asymmetric random walk – “Gambler’s Ruin”** . In words, you start with _i_ dollars and bet 1 dollar each step, with probability _p_ of winning, and continue until reach _K_ or 0. States _{_ 0 _,_ 1 _, . . . , K } pi,i_ +1 = _p, pi,i−_ 1 = 1 _− p,_ 1 _≤ i ≤ K −_ 1

and states 0 and _K_ are absorbing:


In the symmetric case _p_ = 1 _/_ 2 we already know


David Aldous Lecture 7


In the asymmetric case _p̸_ = 1 _/_ 2 we can find the formulas


I will outline the argument on the board “knowing general form of solution to look for”. See [PK] section 3.6 for full proof, in slightly different symbols.

David Aldous Lecture 7


**Numerical example.** Suppose you attempt to double your money by betting $1 on red at roulette, where p(win) = 18/38. The table shows ( _i_ = initial fortune, _K_ = target) probability of success and mean number of plays, comparing p(win) = 18/38 with the “fair” p(win) = 1/2.

Probability double your money E(number of plays) _p_ =<sup>1</sup> _p_ =<sup>18</sup> _p_ =<sup>1</sup> _p_ =<sup>18</sup> 2 38 2 38 i = 10, K = 20 50% 26% 100 92 i = 20, K = 40 50% 11% 400 298 i = 100, K = 200 50% <u>1</u> 10,000 1,900 40 _,_ 000

David Aldous Lecture 7


# **Example: success runs.**

Here the states are _{_ 0 _,_ 1 _,_ 2 _, . . .}_ and the transition probabilities are of the form _pi,i_ +1 = _qi , pi,_ 0 = 1 _− qi_


[work on board: also [PK] section 3.5]

David Aldous Lecture 7


**Example: Death and Immigration process.**

Imagine _Xt_ = population size at time _t_ . Between times _t_ and _t_ + 1, each individual may die independently with probability _p_ , and a random Poisson( _λ_ ) distributed number of immigrants arrive.

So states are _{_ 0 _,_ 1 _,_ 2 _, . . .}_ and by considering the number of survivors _k_


Suppose the initial distribution of _X_ 0 is Poisson( _λ_ 0). From a STAT134 fact, the number of survivors to time 1 has Poisson( _λ_ 0 _q_ ) distribution, for _q_ = 1 _− p_ . So _X_ 1 also has Poisson distribution with mean _λ_ 1 = _λ_ 0 _q_ + _λ_ . Inductively _Xt_ also has Poisson distribution with mean


from which we can calculate


As _t →∞_ we have _λt → λ_<sup><mark>�</mark></sup><sup>_∞_</sup> _s_ =0<sup>_qs_=</sup><sup>_λ/p_.</sup>

David Aldous Lecture 7


So without needing complicated calculations, in this example the distribution of _Xt_ converges as _t →∞_ to a limit distribution, which is the Poisson( _λ/p_ ) distribution.

David Aldous Lecture 7

---

[Up: contents](index.md)
