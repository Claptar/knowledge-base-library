---
title: 07 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 07 slides

**Source:** `lectures/07-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# LECTURE 7

# Review

- Readings: Finish Chapter 2

# Lecture outline

- Multiple random variables

- Joint PMF

_pX_ ( _x_ ) = P( _X_ = _x_ ) _pX,Y_ ( _x, y_ ) = P( _X_ = _x, Y_ = _y_ ) _pX|Y_<sup>(</sup><sup>_x | y_) = P(</sup><sup>_X_=</sup><sup>_x_</sup> _| Y_ = _y_ )

- Conditioning

- Independence

- More on expectations

- Binomial distribution revisited


- A hat problem

# Independent random variables

_pX,Y,Z_ ( _x, y, z_ ) = _pX_ ( _x_ ) _pY |X_ ( _y | x_ ) _pZ|X,Y_ ( _z | x, y_ )

- Random variables _X_ , _Y_ , _Z_ are independent if:

_pX,Y,Z_ ( _x, y, z_ ) = _pX_ ( _x_ ) _· pY_ ( _y_ ) _· pZ_ ( _z_ ) for all _x, y, z_


<!-- Start of picture text -->
y<br>4 1/20 2/20 2/20<br>3 2/20 4/20 1/20 2/20<br>2 1/20 3/20 1/20<br>1 1/20<br>1 2 3 4 x<br><!-- End of picture text -->

# Expectations


   - In general: E[ _g_ ( _X, Y_ )] = _g_ �E[ _X_ ] _,_ E[ _Y_ ]�

   - E[ _αX_ + _β_ ] = _α_ E[ _X_ ] + _β_

   - E[ _X_ + _Y_ + _Z_ ] = E[ _X_ ] + E[ _Y_ ] + E[ _Z_ ]

   - If _X_ , _Y_ are independent:

   - E[ _XY_ ] = E[ _X_ ]E[ _Y_ ]

   - E[ _g_ ( _X_ ) _h_ ( _Y_ )] = E[ _g_ ( _X_ )] _·_ E[ _h_ ( _Y_ )]

- Independent?

- What if we condition on _X ≤_ 2 and _Y ≥_ 3?

1

# Variances

- Var( _aX_ ) = _a_ 2Var( _X_ )

- Var( _X_ + _a_ ) = Var( _X_ )

- Let _Z_ = _X_ + _Y_ . If _X_ , _Y_ are independent:

   - Var( _X_ + _Y_ ) = Var( _X_ ) + Var( _Y_ )

# Binomial mean and variance

- _X_ = # of successes in _n_ independent trials

- probability of success _p_


   - 1 _,_ if success in trial _i,_

   - _• Xi_ = 0 _,_ otherwise

- Examples:

-

   - E[ _Xi_ ] =

- If _X_ = _Y_ , Var( _X_ + _Y_ ) =

- If _X_ = _−Y_ , Var( _X_ + _Y_ ) =

- If _X_ , _Y_ indep., and _Z_ = _X −_ 3 _Y_ , Var( _Z_ ) =

- E[ _X_ ] =

- Var( _Xi_<sup>) =</sup>

- Var( _X_ ) =

# The hat problem

- _n_ people throw their hats in a box and then pick one at random.

- _X_ : number of people who get their own hat

- Find E[ _X_ ]

# Variance in the hat problem

_•_ Var( _X_ ) = E[ _X_ 2] _−_ (E[ _X_ ])2 = E[ _X_ 2] _−_ 1


- E[ _Xi_ 2] =

 _Xi_<sup>=</sup> 10 _,,_ ifotherwise. _i_ selects own hat 

- _X_ = _X_ 1 + _X_ 2 + _· · ·_ + _Xn_

P( _X_ 1 _X_ 2 = 1) = P( _X_ 1 = 1) _·_ P( _X_ 2 = 1 _| X_ 1 = 1) =

- P( _Xi_ = 1) =

- E[ _Xi_ ] =

- Are the _Xi_ independent?

- E[ _X_ ] =

- E[ _X_ 2] =

- Var( _X_ ) =

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
