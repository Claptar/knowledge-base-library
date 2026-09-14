---
title: 'Example: Yule process'
source: https://www.stat.berkeley.edu/~aldous/150/lecture_21_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_21_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Example: Yule process

**Source:** [`lecture_21_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_21_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

parameter _β >_ 0 states 1 _,_ 2 _,_ 3 _, . . ._ transition rates _qi,i_ +1 = _βi X_ (0) = 1.

The differential equations are

_dtd_<sup>_πj_(</sup><sup>_t_) =</sup><sup>_β_[(</sup><sup>_j−_1)</sup><sup>_πj−_1(</sup><sup>_t_)</sup><sup>_−jπj_(</sup><sup>_t_)]</sup><sup>_._</sup> One can solve these equations – see [PK] section 6.1.3 _πj_ ( _t_ ) = P( _X_ ( _t_ ) = _j_ ) = _e_<sup>_−βt_</sup> (1 _− e_<sup>_−βt_</sup> )<sup>_j−_1</sup> _, j_ = 1 _,_ 2 _, . . ._

In other words _X_ ( _t_ ) has Geometric _e_<sup>_−βt_</sup> distribution, so E _X_ ( _t_ ) = _e_<sup>_βt_</sup> .

David Aldous Lecture 21


The Yule process is a basic example of a continuous-time branching process [picture on board]

The Yule process is also an example of a “pure birth” process, meaning the only transitions are _i → i_ + 1. For such processes the distribution of _X_ ( _t_ ) can be related to the sum of independent Exponentials RVs – see [PK] section 6.1.2.

David Aldous Lecture 21


**Example: Linear pure death process** [PK] section 6.2.1. parameter _µ >_ 0 states 0 _,_ 1 _,_ 2 _,_ 3 _, . . . , N_ transition rates _qi,i−_ 1 = _µi X_ (0) = _N_ .

The differential equations are

_dtd_<sup>_πj_(</sup><sup>_t_) =</sup><sup>_µ_[(</sup><sup>_j_+ 1)</sup><sup>_πj_+1(</sup><sup>_t_)</sup><sup>_−jπj_(</sup><sup>_t_)]</sup><sup>_._</sup>

But one can find the time- _t_ distribution easily via an alternative description of the process.


_N_ individuals; initially alive, each dies at rate _µ_ . _X_ ( _t_ ) = number alive at time _t_ ,

Clearly _X_ ( _t_ ) has Binomial( _N, e_<sup>_−µt_</sup> ) distribution.


Note the **general** pure death process (only transitions are _i → i −_ 1) is mathematically the same as the general pure birth <u>process.</u>

David Aldous Lecture 21


**Some theory – similar to discrete-time setting.**

If the chain is irreducible, and either finite-state or infinite state and positive-recurrent, then a unique stationary distribution _π_ exists, and is the solution of _π_ **Q** = 0, that is


**If** you can find weights _wi >_ 0 such that


then the stationary distribution is


provided (in the infinite-state case) _w < ∞_ .

David Aldous Lecture 21

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Birth-and-death chains. →](03-birth-and-death-chains.md)
