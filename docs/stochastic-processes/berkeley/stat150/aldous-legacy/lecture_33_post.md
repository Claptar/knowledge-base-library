---
title: Lecture 33 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_33_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_33_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 33 — post

**Source:** [`lecture_33_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_33_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 33


David Aldous

18 November 2015

David Aldous

Lecture 33


**Martingales associated with Brownian motion** For standard Brownian motion ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) the following processes are continuous-time martingales.


_B_ ( _t_ ) _B_<sup>2</sup> ( _t_ ) _− t B_<sup>3</sup> ( _t_ ) _−_ 3 _tB_ ( _t_ ) _B_<sup>4</sup> ( _t_ ) _−_ 6 _tB_<sup>2</sup> ( _t_ ) + 3 _t_<sup>2</sup> . . . . . .


exp( _θB_ ( _t_ ) _− θ_<sup>2</sup> _t/_ 2) _,_ for fixed _−∞ < θ < ∞_

By using the optional sampling theorem – for a martingale _M_ ( _t_ ) and a stopping time _T_ , under mild extra conditions


we can derive formulas for BM.

David Aldous Lecture 33


We can repeat results for simple symmetric random walk. Take _−a <_ 0 _< b_ and consider


Note the first result can be rewritten as


and this is true for any continuous-path martingale with _M_ (0) = 0.

David Aldous Lecture 33


Fix _µ, σ >_ 0 and consider BM with drift rate _−µ_ and variance rate _σ_<sup>2</sup> :


Because _X_ ( _t_ ) _→−∞_ as _t →∞_ there is some maximum value


We can find the distribution of _S_ by considering the value of _θ_ for which


is a martingale. This works out [board] as


A hitting time


for _X_ ( _t_ ) is the same as the hitting time


for _M_ ( _t_ ). Apply (1) to _M_ ( _t_ ) _−_ 1: [board]

David Aldous Lecture 33


Fix _µ, σ >_ 0 and consider BM with drift rate _−µ_ and variance rate _σ_<sup>2</sup> :


Set _θ_ = 2 _µ/σ_<sup>2</sup> ,

- - - - - - - - - - - - - - - - - - - - - - - - - - -

For _−a <_ 0 _< b_ ,


Letting _a →∞_ we have, for


that


David Aldous Lecture 33

---

[Up: contents](index.md)
