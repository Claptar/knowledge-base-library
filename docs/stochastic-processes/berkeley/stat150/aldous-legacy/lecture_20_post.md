---
title: Lecture 20 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_20_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_20_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 20 — post

**Source:** [`lecture_20_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_20_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 20


David Aldous

14 October 2015

David Aldous

Lecture 20


**Continuous-time Markov chains** [PK] section 6.6 In discrete time _t_ = 0 _,_ 1 _,_ 2 _, . . ._ we specify a Markov chain by specifying the matrix **P** of transition probabilities


In continuous time 0 _≤ t < ∞_ we specify transition **rates**


or informally


but note these are defined only for _j̸_ = _i_ . Then note that


where


David Aldous Lecture 20


In discrete time the time- _t_ distribution _π_ ( _t_ ) = ( _πi_ ( _t_ )) = (P( _X_ ( _t_ ) = _i_ )) evolves as _π_ ( _t_ + 1) = _π_ ( _t_ ) **P** . In continuous time we have [board]


We can re-write this in vector-matrix notation as

where **Q** is the matrix with off-diagonal entries ( _qij_ ) and with diagonal entries defined by


Note this implies that the condition for a probability distribution _π_ to be a stationary distribution is


Note [PK] write **A** instead of **Q** .

David Aldous Lecture 20


Starting at state _i_ , _Si_ = min _{t_ : _X_ ( _t_ ) _̸_ = _i}_

is called the **sojourn time** in _i_ . It is the time spent at _i_ before jumping to another state. The fact

P( _X_ ( _t_ + _dt_ ) _̸_ = _i|X_ ( _t_ ) = _i_ ) = _qi dt_

is the fact P( _Si ∈_ [ _t, t_ + _dt_ ] _|Si > t_ ) = _qi dt_ which shows that _Si_ has Exponential( _qi_ ) distribution. At time _Si_ the process jumps to another state: the probability it jumps to state _j_ is [board]

� _pij_ = _qij /qi ._

David Aldous Lecture 20


This leads to a “jump and hold” description of a continuous-time Markov chain.


After jumping into a state _i_ , the process remains in state _i_ for a random time with Exponential( _qi_ ) distribution.


Then it jumps to some other state, to state _j̸_ = _i_ with probability � _pij_ = _qij /qi_ .

So the matrix


is the transition matrix for the discrete-time **jump chain** _X_<sup>ˆ</sup> (0) _, X_<sup>ˆ</sup> (1) _, . . ._ that shows the successive states visited.

The relationship between the stationary distributions (where they exist) _π_ and _π_ � can be seen using a long-run argument [board] or algebraically from the equations _π_ � **P**<sup>�</sup> = _π,_ � _π_ **Q** = 0:


David Aldous Lecture 20


In very special cases we can solve the differential equations


where **Q** is the matrix with off-diagonal entries ( _qij_ ) and with diagonal entries defined by


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**Example:** For the rate- _λ_ PPP on [0 _, ∞_ ) the counting process _N_ ( _t_ ) is the continuous-time chain with _qi,i_ +1 = _λ_ .

**Example:** 2-state chain: _q_ 01 = _λ, q_ 10 = _µ_ . [board]


David Aldous

Lecture 20


# **Example: Yule process**


parameter _β >_ 0 states 1 _,_ 2 _,_ 3 _, . . ._ transition rates _qi,i_ +1 = _βi X_ (0) = 1.

The differential equations are

_dtd_<sup>_πj_(</sup><sup>_t_) =</sup><sup>_β_[(</sup><sup>_j−_1)</sup><sup>_πj−_1(</sup><sup>_t_)</sup><sup>_−jπj_(</sup><sup>_t_)]</sup><sup>_._</sup> One can solve these equations – see [PK] section 6.1.3 _πj_ ( _t_ ) = P( _X_ ( _t_ ) = _j_ ) = _e_<sup>_−βt_</sup> (1 _− e_<sup>_−βt_</sup> )<sup>_j−_1</sup> _, j_ = 1 _,_ 2 _, . . ._

In other words _X_ ( _t_ ) has Geometric _e_<sup>_−βt_</sup> distribution, so E _X_ ( _t_ ) = _e_<sup>_βt_</sup> .

David Aldous Lecture 20


The Yule process is a basic example of a continuous-time branching process [picture on board]

The Yule process is also an example of a “pure birth” process, meaning the only transitions are _i → i_ + 1. For such processes the distribution of _X_ ( _t_ ) can be related to the sum of independent Exponentials RVs – see [PK] section 6.1.2.

David Aldous Lecture 20

---

[Up: contents](index.md)
