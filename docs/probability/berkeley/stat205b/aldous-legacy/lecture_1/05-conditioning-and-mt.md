---
title: Conditioning and MT
source: https://www.stat.berkeley.edu/~aldous/205B/lecture_1.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/lecture_1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Conditioning and MT

**Source:** [`lecture_1.pdf`](https://www.stat.berkeley.edu/~aldous/205B/lecture_1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Formal definition of conditional expectation.** Let (Ω _, F,_ P) be a probability space. Suppose _X ∈F_ and E _|X | < ∞_ . Suppose _G_ is a _σ_ -field contained in _F_ . We say that a random variable _Y_ is a version of E( _X |G_ ) if

- (I) _Y ∈G_

(II) E[ _Y_ 1 _A_ ] = E[ _X_ 1 _A_ ] _∀ A ∈G_ . This _Y_ exists, is integrable, and is unique (almost surely).

Then there is a “calculus of conditional expectations” which is very useful, in particular in the context of martingales, so you need to learn that. For example: if E _X_<sup>2</sup> _< ∞_ then

var _X_ = E var( _X |G_ ) + var E( _X |G_ ) _._

[board example of use]


Much of this theory is intuitive as gambling on a fair game. If you pay a fixed stake _x_ to get a random return _X_ , your gain is _X − x_ , this is “fair” if E(gain) = 0, that is if _x_ = E _X_ . A sub- _σ_ -field _G_ represents “information”. What is the fair stake _Y_ if you know _G_ ? Consider _A ∈G_ and the strategy: _if A occurs, stake Y , if not, don’t bet._

Your gain is ( _X − Y_ )1 _A_ , and to be fair we need E(gain) = 0, that is E[ _Y_ 1 _A_ ] = E[ _X_ 1 _A_ ]. **That’s where the formal definition comes from.** Optional sampling [stopping] theorems (OST) formalize the **conservation of fairness** principle: under technical assumptions, the overall result of any strategy involving a sequence of bets on fair games is just like a single bet on a fair game: E(overall gain) = 0.


Gambling is like stock market. Imagine mutual fund; can buy/sell at end of day price.


_Xn_ price of 1 share at end of day _n Fn_ information at end of day _n Hn_ number of shares held during day _n Sn_ = accrued profit at end of day _n_ .

Related by

_Sn − Sn−_ 1 = _Hn_ ( _Xn − Xn−_ 1) _._

From the story


_Hn ∈Fn−_ 1 (( _Hn_ ) is **predictable** )

If also ( _Xn_ ) is a martingale and each _Hn_ is bounded then


( _Sn_ ) is a martingale.

This is the discrete analog of **stochastic calculus** . One can get many results (e.g. the **upcrossing inequality** ) about ( _Xn_ ) by choice of ( _Hn_ ) use of OST for ( _Sn_ ).

---

[← Understanding the Radon-Nikodym theorem.](04-understanding-the-radon-nikodym-theorem.md) · [Up: contents](index.md)
