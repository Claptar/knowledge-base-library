---
title: 19 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 19 slides

**Source:** `lectures/19-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

LECTURE 19 Limit theorems – I

- Readings: Sections 5.1-5.3; start Section 5.4

_• X_ 1 _, . . . , Xn_ i.i.d. _X_ 1 + _· · ·_ + _Xn Mn_ = _n_ What happens as _n →∞_ ?

- Why bother?

- A tool: Chebyshev’s inequality

- Convergence “in probability”

- Convergence of _Mn_ (weak law of large numbers)

# Deterministic limits

- Sequence _an_ Number _a_

- _an_ converges to _a_

lim _an_ = _a n→∞_

“ _an_ eventually gets and stays (arbitrarily) close to _a_ ”

- For every _ϵ >_ 0, there exists _n_ 0, such that for every _n ≥ n_ 0, we have _|an − a| ≤ ϵ_ .

# Chebyshev’s inequality

- Random variable _X_ (with finite mean _µ_ and variance _σ_ 2)


# Convergence “in probability”

- Sequence of random variables _Yn_

- converges in probability to a number _a_ : “(almost all) of the PMF/PDF of _Yn_ , eventually gets concentrated (arbitrarily) close to _a_ ”

- For every _ϵ >_ 0,

lim P( _|Yn − a| ≥ ϵ_ ) = 0

_n→∞_


<!-- Start of picture text -->
1 - 1 /n<br>pmf of Yn<br>1 /n<br>0 n<br>Does Yn converge?<br><!-- End of picture text -->

1

Convergence of the sample mean (Weak law of large numbers)

_• X_ 1 _, X_ 2 _, . . ._ i.i.d. finite mean _µ_ and variance _σ_ 2 _X_ 1 + _· · ·_ + _Xn Mn_ = _n_

- E[ _Mn_ ] =

# The pollster’s problem

- _f_ : fraction of population that “. . . ”

- _i_ th (randomly selected) person polled:


   - _Mn_ = ( _X_ 1<sup>+</sup><sup>_· · ·_+</sup><sup>_X_</sup> _n_<sup>)</sup><sup>_/n_</sup> fraction of “yes” in our sample

   - Goal: 95% confidence of _≤_ 1% error

- Var( _Mn_ ) =

   - P( _|Mn − f | ≥ ._ 01) _≤ ._ 05

- Use Chebyshev’s inequality:


- _Mn_ converges in probability to _µ_


- If _n_ = 50 _,_ 000, then P( _|Mn − f | ≥ ._ 01) _≤ ._ 05 (conservative)

# Different scalings of _Mn_

- _X_ 1 _, . . . , Xn_ i.i.d. finite variance _σ_ 2

- Look at three variants of their sum:

# The central limit theorem


   - zero mean

- _Sn_ = _X_ 1 + _· · ·_ + _Xn_ variance _nσ_ 2

   - unit variance

- _Mn_ = _Sn_ variance _σ_ 2 _/n n_

- converges “in probability” to E[ _X_ ] (WLLN)

- _Sn_ constant variance _σ_ 2 _~~√~~_ _<u>n</u>_

- Let _Z_ be a standard normal r.v. (zero mean, unit variance)

- Theorem: For every _c_ :


- Asymptotic shape?

- P( _Z ≤ c_ ) is the standard normal CDF, Φ( _c_ ), available from the normal tables

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
