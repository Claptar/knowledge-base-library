---
title: 12 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12 slides

**Source:** `lectures/12-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# LECTURE 12

- Readings: Section 4.3; parts of Section 4.5 (mean and variance only; no transforms)

# Conditional expectations

- Given the value _y_ of a r.v. _Y_ :


(integral in continuous case)

# Lecture outline

- Conditional expectation

- Law of iterated expectations

   - Stick example: stick of length _ℓ_ break at uniformly chosen point _Y_ break again at uniformly chosen point _X_

   - _<u>y</u>_

   - _•_ E[ _X | Y_ = _y_ ] = (number) 2

- Law of total variance

- Sum of a random number of independent r.v.’s


- mean, variance

- Law of iterated expectations:


- In stick example: E[ _X_ ] = E[E[ _X | Y_ ]] = E[ _Y/_ 2] = _ℓ/_ 4

var( _X | Y_ ) and its expectation

- var( _X | Y_ = _y_ ) = E �( _X −_ E[ _X | Y_ = _y_ ])2 _| Y_ = _y_ �

- var( _X | Y_ ): a r.v. with value var( _X | Y_ = _y_ ) when _Y_ = _y_

# Section means and variances

Two sections: _y_ = 1 (10 students); _y_ = 2 (20 students)


- Law of total variance:

   - var( _X_ ) = E[var( _X | Y_ )] + var(E[ _X | Y_ ])

# Proof:


Sum of right-hand sides of (c), (d): E[ _X_ 2] _−_ (E[ _X_ ])<sup>2</sup> = var( _X_ )


1

Section means and variances (ctd.)


var( _X | Y_ = 1) = 10 var( _X | Y_ = 2) = 20


var( _X_ ) = E[var( _X | Y_ )] + var(E[ _X | Y_ ]) 50 = + 200 3

= (average variability within sections) + (variability between sections)

Sum of a random number of independent r.v.’s

- _N_ : number of stores visited

# Example


<!-- Start of picture text -->
var( X ) = E[var( X | Y  )] + var(E[ X | Y ])<br>f X(x)<br>2/3<br>1/3<br>Y=1 1 Y=2 2 x<br>E[ X | Y = 1] = E[ X | Y = 2] =<br>var( X | Y = 1) = var( X | Y = 2) =<br>E[ X ] =<br><!-- End of picture text -->

var(E[ _X | Y_ ]) =

# Variance of sum of a random number of independent r.v.’s

      - var( _Y_ ) = E[var( _Y | N_ )] + var(E[ _Y | N_ ])

   - ( _N_ is a nonnegative integer r.v.)

- _Xi_ : money spent in store _i_

   - E[ _Y | N_ ] = _N_ E[ _X_ ] var(E[ _Y | N_ ]) = (E[ _X_ ])<sup>2</sup> var( _N_ )

- _Xi_ assumed i.i.d.

- independent of _N_

- Let _Y_ = _X_ 1 + _· · ·_ + _XN_

      - var( _Y | N_ = _n_ ) = _n_ var( _X_ ) var( _Y | N_ ) = _N_ var( _X_ ) E[var( _Y | N_ )] = E[ _N_ ] var( _X_ )

- E[ _Y | N_ = _n_ ] = E[ _X_ 1 + _X_ 2 + _· · ·_ + _Xn | N_ = _n_ ]

   - = E[ _X_ 1 + _X_ 2 + _· · ·_ + _Xn_ ]

   - = E[ _X_ 1] + E[ _X_ 2] + _· · ·_ + E[ _Xn_ ] = _n_ E[ _X_ ]

         - var( _Y_ ) = E[var( _Y | N_ )] + var(E[ _Y | N_ ]) = E[ _N_ ] var( _X_ ) + (E[ _X_ ])2 var( _N_ )

- E[ _Y | N_ ] = _N_ E[ _X_ ]

   - E[ _Y_ ] = E[E[ _Y | N_ ]] = E[ _N_ E[ _X_ ]]

      - = E[ _N_ ] E[ _X_ ]

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
