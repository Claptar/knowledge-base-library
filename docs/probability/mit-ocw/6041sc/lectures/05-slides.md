---
title: LECTURE 5
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# LECTURE 5

**Source:** `lectures/05-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Readings: Sections 2.1-2.3, start 2.4

# Random variables

- An assignment of a value (number) to every possible outcome

# Lecture outline

- Random variables

- Probability mass function (PMF)

   - Mathematically: A function from the sample space Ωto the real numbers

   - discrete or continuous values

- Expectation

- Variance

- Can have several random variables defined on the same sample space

- Notation:

- random variable _X_

- numerical value _x_

# Probability mass function (PMF)

- (“probability law”, “probability distribution” of _X_ )

How to compute a PMF _pX_ ( _x_ )

   - collect all possible outcomes for which _X_ is equal to _x_

      - add their probabilities

      - repeat for all _x_

- Notation:

_pX_ ( _x_ ) = P( _X_ = _x_ ) = P( _{ω ∈_ Ωs _._ t _. X_ ( _ω_ ) = _x}_ )

- _pX_ ( _x_ ) _≥_ 0 � _x_<sup>_p_</sup> _X_<sup>(</sup><sup>_x_) = 1</sup>

- Example: _X_ =number of coin tosses until first head

- assume independent tosses, P( _H_ ) = _p >_ 0

   - _pX_ ( _k_ ) = P( _X_ = _k_ ) = P( _TT · · · TH_ ) = (1 _− p_ )<sup>_k−_1</sup> _p, k_ = 1 _,_ 2 _, . . ._

- Example: Two independent rools of a fair tetrahedral die

_F_ : outcome of first throw _S_ : outcome of second throw _X_ = min( _F, S_ )


<!-- Start of picture text -->
4<br>3<br>S = Second roll<br>2<br>1<br>1 2 3 4<br>F = First roll<br><!-- End of picture text -->

- geometric PMF

_pX_ (2) =

1

# Binomial PMF

- _X_ : number of heads in _n_ independent coin tosses

- Definition:

# Expectation


- P( _H_ ) = _p_

         - Interpretations:

- Let _n_ = 4

   - _pX_ (2) = P( _HHTT_ ) + P( _HTHT_ ) + P( _HTTH_ ) +P( _THHT_ ) + P( _THTH_ ) + P( _TTHH_ )

      - = 6 _p_<sup>2</sup> (1 _− p_ )<sup>2</sup> 4

      - = �2� _p_ 2(1 _− p_ )<sup>2</sup>

In general:

_k pX_ ( _k_ ) = � _nk_ � _p_ (1 _−p_ )<sup>_n−k_</sup> _, k_ = 0 _,_ 1 _, . . . , n_

# Properties of expectations

- Let _X_ be a r.v. and let _Y_ = _g_ ( _X_ )

– Hard: E[ _Y_ ] = � _ypY_ ( _y_ ) _y_ – Easy: E[ _Y_ ] = � _g_ ( _x_ ) _pX_ ( _x_ ) _x_

- Caution: In general, E[ _g_ ( _X_ )] = _g_ (E[ _X_ ])

Properties: If _α_ , _β_ are constants, then:

- E[ _α_ ] =

- E[ _αX_ ] =

- E[ _αX_ + _β_ ] =

   - Center of gravity of PMF

- Average in large number of repetitions of the experiment (to be substantiated later in this course)

- Example: Uniform on 0 _,_ 1 _, . . . , n_


# Variance


_•_ Second moment: E[ _X_ 2] =<sup>�</sup> _x_<sup>_x_</sup> 2<sup>_p_</sup> _X_ (<sup>_x_)</sup>

- Variance


Properties:

- var( _X_ ) _≥_ 0

- var( _αX_ + _β_ ) = _α_ 2var( _X_ )

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
