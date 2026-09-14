---
title: Conditional expectation as a random variable.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_4_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_4_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Conditional expectation as a random variable.

**Source:** [`lecture_4_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_4_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Given r.v.’s ( _W , Y_ ) consider E( _W |Y_ = _y_ ). This is a number depending on _y_ – in other words it’s a **function** of _y_ . Giving this function a name _h_ we have

( _∗_ ) E( _W |Y_ = _y_ ) = _h_ ( _y_ ) for all possible values _y_ of _Y ._

We now make a notational convention, to rewrite the assertion (*) as


The right side is a r.v., so we must regard E( _W |Y_ ) as a r.v.

[PK] page 60 lists properties of (**), but rather hard to understand at first sight. One important property is that the “law of total probability” becomes


I will give three examples to illustrate this notation.

David Aldous Lecture 4


**Example.** First consider

_n Sn_ = � _ξi_ for i.i.d. ( _ξi_ ) with E _ξi_ = _µξ. i_ =1

Then take _N_ a _{_ 1 _,_ 2 _,_ 3 _, . . .}_ -valued r.v. with E _N_ = _µN_ , independent of ( _ξi_ ).

_What is_ E _SN ?_

David Aldous Lecture 4


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


David Aldous Lecture 4

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [A “geometric probability” example. →](03-a-geometric-probability-example.md)
