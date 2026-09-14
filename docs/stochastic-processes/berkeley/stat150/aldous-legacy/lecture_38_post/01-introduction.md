---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/150/lecture_38_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_38_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`lecture_38_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_38_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 38


David Aldous

4 December 2015

David Aldous

Lecture 38


Standard Brownian motion ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) has the properties Sample paths _t → B_ ( _t_ ) are continuous _B_ ( _t_ ) is a martingale _B_<sup>2</sup> ( _t_ ) _− t_ is a martingale.

**Levy’s theorem** states that Brownian motion is the **only** process with these properties. In other words, to check that a given process is Brownian motion, we don’t need to check the “Normal distributions and independent increments” properties in the definition; instead we can just check the properties above, for a filtration ( _F_ ( _t_ ) _,_ 0 _≤ t < ∞_ ). We will work more intuitively in terms of “infinitesimal increments”. For a process _X_ ( _t_ ) write the increment _X_ ( _t_ + _dt_ ) _− X_ ( _t_ ) as _dX_ ( _t_ ). The two martingale properties above can be rewritten as


- E( _dB_ ( _t_ ) _|F_ ( _t_ )) = 0 E(( _dB_ ( _t_ ))<sup>2</sup> _|F_ ( _t_ )) = _dt_ .

Suppose we are given two functions _µ_ : R _→_ R and _σ_ : R _→_ (0 _, ∞_ ). It can be shown that (under minor assumptions on these functions) there exists a **unique** process ( _X_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) with the properties


- Sample paths _t → X_ ( _t_ ) are continuous E( _dX_ ( _t_ ) _|F_ ( _t_ )) = _µ_ ( _Xt_ ) _dt_ E(( _dX_ ( _t_ ))<sup>2</sup> _|F_ ( _t_ )) = _σ_<sup>2</sup> ( _Xt_ ) _dt_

David Aldous Lecture 38


In other words the process ( _X_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) is the continuous-time Markov process specified by Sample paths _t → X_ ( _t_ ) are continuous E( _dX_ ( _t_ ) _|X_ ( _t_ ) = _x_ ) = _µ_ ( _x_ ) _dt_ var ( _dX_ ( _t_ ) _|X_ ( _t_ ) = _x_ ) = _σ_<sup>2</sup> ( _x_ ) _dt_

This is analogous to specifying a Markov chain by specifying its transition matrix. Such processes are called **diffusions** .

Standard Brownian motion _B_ ( _t_ ) is the case _µ_ ( _x_ ) _≡_ 0 _, σ_ ( _x_ ) _≡_ 1. Recall that for constants _µ, σ_ we can define _X_ ( _t_ ) = _µt_ + _σB_ ( _t_ ); this is the case _µ_ ( _x_ ) _≡ µ, σ_ ( _x_ ) _≡ σ_ . In this case _X_ ( _t_ ) has a Normal distribution but in general it does not.

David Aldous Lecture 38


Textbooks develop the theory of such processes – there are formulas for hitting probabilities and mean hitting times, for instance. In this lecture I will just show how diffusions can arise as scaling limits of discrete Markov processes, analogous to the way we introduced Brownian motion as the scaling limit of simple random walk.

David Aldous

Lecture 38

---

[Up: contents](index.md) · [Example: Wright-Fisher model with mutation →](02-example-wright-fisher-model-with-mutation.md)
