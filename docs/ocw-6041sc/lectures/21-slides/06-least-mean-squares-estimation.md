---
title: Least Mean Squares Estimation
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/21-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Least Mean Squares Estimation

**Source:** `lectures/21-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Estimation in the absence of information

– pmf _p_ Θ _|X_ ( _· | x_ ) or pdf _f_ Θ _<u>|X</u>_ (<sup>_· |_</sup> _x_ )

- If interested in a single answer:


<!-- Start of picture text -->
f Θ( θ )<br>1/6<br>4 10 θ<br><!-- End of picture text -->

- ~~Maximum a poste~~ riori probability (MAP):

      - find estimate _c_ , to:

- _p_ Θ _X|_ ( _θ_<sup>_∗_</sup> _| x_ ) = max _θ p_ Θ _|X_ ( _θ | x_ ) minimizes probability of error; often used in hypothesis testing

- _f_ Θ _|X_<sup>(</sup><sup>_θ∗| x_) = max</sup> _θ_<sup>_f_</sup> Θ _|X_<sup>(</sup><sup>_θ_</sup> _| x_ )

- Conditional expectation:

   - E[Θ _| X_ = _y_ ] = � _θf_ Θ _|X_ ( _θ | x_ ) _dθ_

      - minimize E �(Θ _− c_ )2�

   - Optimal estimate: _c_ = E[Θ]

   - Optimal mean squared error: E �(Θ _−_ E[Θ])<sup>2</sup> � = Var(Θ)

- Single answers can be misleading!

LMS Estimation of Θ based on _X_

- Two r.v.’s Θ, _X_

- we observe that _X_ = _x_

LMS Estimation w. several measurements

   - Unknown r.v. Θ

   - Observe values of r.v.’s _X_ 1 _, . . . , Xn_

- new universe: condition on _X_ = _x_

   - Best estimator: E[Θ _| X_ 1 _, . . . , Xn_ ]

- E �(Θ _− c_ )2 _| X_ = _x_ � is minimized by _c_ =

- Can be hard to compute/implement

- involves multi-dimensional integrals, etc.


- E �(Θ _−_ E[Θ _| X_ ])<sup>2�</sup> _≤_ E �(Θ _− g_ ( _X_ ))2�


2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Output of Bayesian Inference](05-output-of-bayesian-inference.md) · [Up: contents](index.md)
