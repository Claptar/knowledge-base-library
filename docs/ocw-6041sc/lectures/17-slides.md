---
title: 17 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 17 slides

**Source:** `lectures/17-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

LECTURE 17

Markov Processes – II

- Readings: Section 7.3

# Review

- Discrete state, discrete time, time-homogeneous

- Transition probabilities _pij_

- Markov property

# Lecture outline

   - _rij_ ( _n_ ) = P( _Xn_ = _j | X_ 0 = _i_ )

- Review

- Steady-State behavior

   - Key recursion: _rij_ ( _n_ ) = � _rik_ ( _n −_ 1) _pkj k_

- Steady-state convergence theorem

- Balance equations

- Birth-death processes

# Warmup


<!-- Start of picture text -->
9 3 4<br>6 7<br>5 1 2<br>8<br><!-- End of picture text -->

P( _X_ 1 = 2 _, X_ 2 = 6 _, X_ 3 = 7 _| X_ 0 = 1) =

P( _X_ 4 = 7 _| X_ 0 = 2) =

# Recurrent and transient states

- State _i_ is recurrent if: starting from _i_ , and from wherever you can go, there is a way of returning to _i_

- If not recurrent, called transient

- Recurrent class:

collection of recurrent states that “communicate” to each other and to no other state

# Periodic states

- The states in a recurrent class are periodic if they can be grouped into _d >_ 1 groups so that all transitions from one group lead to the next group


<!-- Start of picture text -->
9<br>5<br>4<br>6 8<br>3<br>2 1 7<br><!-- End of picture text -->

1

# Steady-State Probabilities

- Do the _rij_ ( _n_ ) converge to some _πj_ ? (independent of the initial state _i_ )

- Yes, if:

- recurrent states are all in a single class, and

# Visit frequency interpretation


   - (Long run) frequency of being in _j_ : _πj_

- single recurrent class is not periodic

   - Frequency of transitions _k → j_ : _πkpkj_

- Assuming “yes,” start from key recursion


- take the limit as _n →∞_


- Additional equation:


# Example


<!-- Start of picture text -->
0.5 0.8<br>0.5<br>1 2<br>0.2<br><!-- End of picture text -->


<!-- Start of picture text -->
• Frequency of transitions into j : � πkpkj<br>k<br>1 π jpjj<br>π1 p 1 j<br>2<br>π 2 p 2 j  j<br>m π m pmj<br>.  .  .<br>.  .  .<br><!-- End of picture text -->

# ~~Birth~~ -death processes


<!-- Start of picture text -->
1- p 0 1- p 1- q 1 1- q m<br>p0 p1<br>0 1 2 3 ... m<br>q 1 q2 q m<br>pi<br>i i+1 πipi =  πi +1 qi +1<br>qi+1<br><!-- End of picture text -->

- Special case: _pi_ = _p_ and _qi_ = _q_ for all _i ρ_ = _p/q_ =load factor


- Assume _p < q_ and _m ≈∞_


2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
