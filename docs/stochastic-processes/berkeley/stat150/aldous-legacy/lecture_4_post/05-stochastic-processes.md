---
title: Stochastic Processes
source: https://www.stat.berkeley.edu/~aldous/150/lecture_4_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_4_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stochastic Processes

**Source:** [`lecture_4_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_4_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For our purposes a **stochastic process** is just a sequence ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) of random variables. The range space of the _X_ ’s might be the integers Z or the reals R or some more general space _S_ . We envisage observing some physical process changing with time in some random way: _Xt_ is the observed value of the process at time _t_ = 0 _,_ 1 _,_ 2 _, . . ._ . So _X_ 0 is the “initial” value.

Perhaps the simplest example is **simple symmetric random walk**


where ( _ξi_ ) are i.i.d. with P( _ξi_ = 1) = P( _ξi_ = _−_ 1) =<sup><u>1</u></sup> 2<sup>.Here</sup><sup>_X_0= 0.</sup>

There are many ways to study this process, but I want to illustrate the technique “conditioning on the first step” which will be a fundamental technique for studying Markov chains.

David Aldous Lecture 4


Interpret this process as“gambling at fair odds” – bet 1 unit on an event with probability 1 _/_ 2, either win or lose the 1 unit. So _Xt_ is your “fortune” after _t_ bets. Suppose


start with fortune _x_

continue until your fortune reach some target amount _K_ or 0. There is some probability _p_ ( _x_ ) that you succeed in reaching _K_ ; this probability depends on _x_ and on _K_ , but let us take _K_ as fixed. So we know

_p_ ( _K_ ) = 1; _p_ (0) = 0 _._

What can we say about _p_ ( _x_ ) for 1 _≤ x ≤ K −_ 1?

David Aldous

Lecture 4


From the “law of total probability” P( _A_ ) = P( _B_ )P( _A|B_ ) + P( _B_<sup>_c_</sup> )P( _A|B_<sup>_c_</sup> )

we have

= _p_ ( _x_ ) P( win first bet) _×_ P( reach _K |_ win first bet) + P( lose first bet) _×_ P( reach _K |_ lose first bet)

That is,


This is the simplest case of a **linear difference equation** and the general solution is _p_ ( _x_ ) = _a_ + _bx_ . Because we know the “boundary conditions” _p_ (0) = 0 _, p_ ( _K_ ) = 1 we can solve to find _a, b_ and find


David Aldous Lecture 4


We can use the same “conditioning on the first step” method to study _s_ ( _x_ ) = E(number of steps until reach _K_ or 0)

starting from _x_ . Here the equation is


The general form of solution (see textbook for details) is _s_ ( _x_ ) = _cx_ ( _K − x_ ); plugging into the equation gives _c_ = 1, so


David Aldous Lecture 4


**Conceptual point.** The notion of **independence** is used in two conceptually different ways.


We often use independence as an **assumption** in a model – throwing dice, for instance.


Given a well-defined math model, events or random variables _X , Y_ either are independent, or are not independent, as a mathematical **conclusion** . For instance, for a uniform random pick of a playing card from a standard deck, the events “card is a King” and “card is a Spade” are independent.

- The same point will arise with the Markov property.

David Aldous Lecture 4

---

[← and this says](04-and-this-says.md) · [Up: contents](index.md)
