---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_2_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`lecture_2_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_2_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 2


David Aldous

28 August 2015

David Aldous

Lecture 2


The specific examples I’m discussing are not so important; the point of these first lectures is to illustrate a few of the 100 ideas from STAT134.

**Ideas used in Lecture 1.**


Bayes rule. E _g_ ( _X_ ) =<sup>�</sup> _x_<sup>_g_(</sup><sup>_x_)P(</sup><sup>_X_=</sup><sup>_x_)</sup><sup>_._</sup> Fair bet means E(gain) = 0. Indicator r.v.’s 11( _A_ ) useful notation. Law of large numbers.

David Aldous Lecture 2


**4. Fair price for option on Normal payoff.**

Consider _Z_ with Normal(0 _,_ 1) distribution. The fair price today to receive _Z_ tomorrow = E _Z_ = 0.

What is fair price for an “option” to receive _Z_ tomorrow for cost _c_ ? That is, a contract that says

_tomorrow, after you see the value of Z, you can buy it for c if you wish._ If you buy the option, then tomorrow

if _Z > c_ then you have payoff _Z − c_ if _Z < c_ then you have payoff 0.

In other words, your payoff is max( _Z − c,_ 0), so fair price is

E max( _Z − c,_ 0) _._

David Aldous Lecture 2


for


David Aldous Lecture 2

---

[Up: contents](index.md) · [5. Decreasing dice rolls. →](02-5-decreasing-dice-rolls.md)
