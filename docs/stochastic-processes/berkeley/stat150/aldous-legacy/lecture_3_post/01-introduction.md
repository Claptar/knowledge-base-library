---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/150/lecture_3_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_3_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`lecture_3_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_3_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 3


David Aldous

31 August 2015

David Aldous

Lecture 3


This “size-bias” effect occurs in other contexts, such as class size.

If a small Department offers two courses, with enrollments 90 and 10, then

average class (faculty viewpoint) = (90 + 10) _/_ 2 = 50 average class (student viewpoint) = (90 _×_ 90 + 10 _×_ 10) _/_ 100 = 82.

David Aldous Lecture 3


The specific examples I’m discussing are not so important; the point of these first lectures is to illustrate a few of the 100 ideas from STAT134.

**Ideas used in Lecture 2.**


E _g_ ( _X_ ) = � _g_ ( _x_ ) _fX_ ( _x_ ) _dx._


exploit symmetry.


if _X , Y_ independent then var ( _aX_ + _bY_ ) = _a_<sup>2</sup> var ( _X_ ) + _b_<sup>2</sup> var ( _Y_ ) inventing extra structure size-biasing

David Aldous Lecture 3


Different authors use slightly different notation:

P( _A_ ) = _P_ ( _A_ ) = Pr( _A_ ) P( _X ≤_ 4) = P _{X ≤_ 4 _}_ E _X_ = E[ _X_ ] = _EX_ 1 _A_ = **1** _A_ = **1** ( _A_ ) = _I_ ( _A_ )

David Aldous Lecture 3


**Chapter 1 of textbook [PK] provides a review of STAT134 level material.**

It’s rather boring, but helpful for you to read. Here is material from section 1.5.2: some properties of the Exponential distribution, which plays a prominent role in Poisson processes later.

The Exponential( _λ_ ) distribution for a r.v. _X >_ 0 is defined to have density function

_f_ ( _x_ ) = _λe_<sup>_−λx_</sup> _,_ 0 _< x < ∞_

and has E _X_ = 1 _/λ_ = s _._ d _._ ( _X_ ). Also P( _X > x_ ) = _e_<sup>_−λx_</sup> . Note the parametrization convention; _λ_ is called the _rate_ .

There are special properties of independent Exponential r.v.’s – say _X_ 1 with rate _λ_ 1 and _X_ 2 with rate _λ_ 2. Consider

_U_ = min( _X_ 1 _, X_ 2) = _XM_ for _M_ = arg min( _X_ 1 _, X_ 2)

_V_ = max( _X_ 1 _, X_ 2) = _XN_ for _N_ = arg max( _X_ 1 _, X_ 2) _._

Let’s calculate P( _M_ = 1 _, U > t_ ), which is the same as P( _t < X_ 1 _< X_ 2).

David Aldous Lecture 3

---

[Up: contents](index.md) · [independent Exponentials: X 1 with rate λ 1 and X 2 with rate λ 2. →](02-independent-exponentials-x-1-with-rate-λ-1-and-x-2-with-rate.md)
