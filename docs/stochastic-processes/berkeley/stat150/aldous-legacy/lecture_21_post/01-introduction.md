---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/150/lecture_21_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_21_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`lecture_21_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_21_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 21


David Aldous

16 October 2015

David Aldous

Lecture 21


In continuous time 0 _≤ t < ∞_ we specify transition **rates**


or informally

P( _X_ ( _t_ + _dt_ ) = _j|X_ ( _t_ ) = _i_ ) = _qij dt_

but note these are defined only for _j̸_ = _i_ . The time- _t_ distribution _π_ ( _t_ ) evolves as


where **Q** is the matrix with off-diagonal entries ( _qij_ ) and with diagonal entries defined by


David Aldous Lecture 21


There is an alternative “jump and hold” description of a continuous-time Markov chain.


After jumping into a state _i_ , the process remains in state _i_ for a random time with Exponential( _qi_ ) distribution.


Then it jumps to some other state, to state _j̸_ = _i_ with probability � _pij_ = _qij /qi_ .

So the matrix


is the transition matrix for the discrete-time **jump chain** _X_<sup>ˆ</sup> (0) _, X_<sup>ˆ</sup> (1) _, . . ._ that shows the successive states visited.

David Aldous Lecture 21

---

[Up: contents](index.md) · [Example: Yule process →](02-example-yule-process.md)
