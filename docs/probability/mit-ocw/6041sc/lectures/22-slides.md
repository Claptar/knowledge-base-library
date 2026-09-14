---
title: LECTURE 22
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/22-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# LECTURE 22

**Source:** `lectures/22-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Readings: pp. 225-226; Sections 8.3-8.4

# Topics

- (Bayesian) Least means squares (LMS) estimation


<!-- Start of picture text -->
• (Bayesian) Linear LMS estimation ·<br>Θ X Estimator Θ ˆ =  g ( X )<br>fX| Θ( x | θ ) g ( · )<br>f Θ( θ )<br><!-- End of picture text -->

- MAP estimate: _θ_<sup>ˆ</sup> MAP maximizes _f_ Θ _|X_ ( _θ | x_ )

- LMS estimation:

- Θ<sup>ˆ</sup> = E[Θ _| X_ ] minimizes E￿(Θ _− g_ ( _X_ ))<sup>2</sup> ￿ over all estimators _g_ ( _·_ )

- for any _x_ , _θ_<sup>ˆ</sup> = E[Θ _| X_ = _x_ ] minimizes E￿(Θ _− θ_<sup>ˆ</sup> )<sup>2</sup> _| X_ = _x_ ￿ over all estimates _θ_<sup>ˆ</sup>

# Conditional mean squared error

- E[(Θ _−_ E[Θ _| X_ ])<sup>2</sup> _| X_ = _x_ ]

- same as Var(Θ _| X_ = _x_ ): variance of the conditional distribution of Θ


<!-- Start of picture text -->
θ<br>10 x<br>4<br>x<br>3 5 9 11 y<br>| |<br>10 x Var(Θ | X =  x ):<br>onal distribution of<br>4<br>x<br>3 5 9 11 y<br><!-- End of picture text -->


<!-- Start of picture text -->
f Θ( θ )<br>1/6<br>4 10 θ<br>fX| Θ( x | θ )<br>1 / 2<br>θ − 1 θ  + 1<br>θ<br>10 x<br>4<br>x<br>3 5 9 11<br>y<br><!-- End of picture text -->

# Some properties of LMS estimation

- Estimator: Θ<sup>ˆ</sup> = E[Θ _| X_ ]

- Estimation error: Θ<sup>˜</sup> = Θ<sup>ˆ</sup> _−_ Θ

- E[Θ<sup>˜</sup> ] = 0 E[Θ<sup>˜</sup> _| X_ = _x_ ] = 0

- E[Θ<sup>˜</sup> _h_ ( _X_ )] = 0, for any function _h_

- cov(Θ<sup>˜</sup> _,_ Θ<sup>ˆ</sup> ) = 0

- Since Θ = Θ<sup>ˆ</sup> _−_ Θ<sup>˜</sup> : var(Θ) = var(Θ<sup>ˆ</sup> ) + var(Θ<sup>˜</sup> )

1

# Linear LMS

- Consider estimators of Θ, of the form Θ =ˆ _aX_ + _b_

- Minimize E ￿(Θ _− aX − b_ )<sup>2</sup> ￿

- Best choice of _a_ , _b_ ; best linear estimator: Cov( _X,_ Θ)

- Θ<sup>ˆ</sup> _L_ = E[Θ] + ( _X −_ E[ _X_ ]) var( _X_ )


<!-- Start of picture text -->
θ<br>10 x<br>4<br>x<br>3 5 9 11<br>y<br><!-- End of picture text -->

# The cleanest linear LMS example


- If all normal, Θ<sup>ˆ</sup> _L_ = E[Θ _| X_ 1 _, . . . , Xn_ ]

# Linear LMS properties


# Linear LMS with multiple data

- Consider estimators of the form:


- Find best choices of _a_ 1 _, . . . , an, b_

- Minimize:

E[( _a_ 1 _X_ 1 + _· · ·_ + _anXn_ + _b −_ Θ)<sup>2</sup> ]

- Set derivatives to zero linear system in _b_ and the _ai_

- Only means, variances, covariances matter

# Big picture

- Standard examples:

- _Xi_ uniform on [0 _, θ_ ]; uniform prior on _θ_

- _Xi_ Bernoulli( _p_ ); uniform (or Beta) prior on _p_

- _Xi_ normal with mean _θ_ , known variance _σ_ 2; normal prior on _θ_ ;

   - _Xi_ = Θ + _Wi_

- Estimation methods:

# Choosing _Xi_ in linear LMS

- E[Θ _| X_ ] is the same as E[Θ _| X_ 3]

- Linear LMS is different:

   - MAP

   - MSE

   - Linear MSE

- Θ<sup>ˆ</sup> = _aX_ + _b_ versus Θ<sup>ˆ</sup> = _aX_ 3 + _b_

- _◦_ Also consider Θ<sup>ˆ</sup> = _a_ 1 _X_ + _a_ 2 _X_ 2 + _a_ 3 _X_ 3 + _b_

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
