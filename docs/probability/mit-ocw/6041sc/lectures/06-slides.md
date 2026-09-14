---
title: 06 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/06-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 06 slides

**Source:** `lectures/06-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# LECTURE 6

- Readings: Sections 2.4-2.6

# Lecture outline

- Review: PMF, expectation, variance

- Conditional PMF

- Geometric PMF

- Total expectation theorem

- Joint PMF of two random variables

# Review

- Random variable _X_ : function from sample space to the real numbers

- PMF (for discrete random variables): _pX_ ( _x_ ) = P( _X_ = _x_ )

- Expectation:


# Random speed

- Traverse a 200 mile distance at constant but random speed _V_


<!-- Start of picture text -->
p (v )V 1/2 1/2<br>1 200 v<br><!-- End of picture text -->

- _d_ = 200, _T_ = _t_ ( _V_ ) = 200 _/V_

- E[ _V_ ] =

# Average speed vs. average time

- Traverse a 200 mile distance at constant but random speed _V_


<!-- Start of picture text -->
p (v )V 1/2 1/2<br>1 200 v<br><!-- End of picture text -->

   - time in hours = _T_ = _t_ ( _V_ ) =

   - E[ _T_ ] = E[ _t_ ( _V_ )] =<sup>�</sup> _v_<sup>_t_(</sup><sup>_v_)</sup><sup>_p_</sup> _V_<sup>(</sup><sup>_v_) =</sup>

   - E[ _TV_ ] = 200 = E[ _T_ ] _·_ E[ _V_ ]

- var( _V_ ) =

   - E[200 _/V_ ] = E[ _T_ ] = 200 _/_ E[ _V_ ].

- _σV_ =

1

# Conditional PMF and expectation

- _pX|A_ ( _x_ ) = P( _X_ = _x | A_ )


<!-- Start of picture text -->
• E[ X | A ] = � xpX|A ( x )<br>x<br>p (x )X<br>1/4<br>1 2 3 4 x<br><!-- End of picture text -->

- Let _A_ = _{X ≥_ 2 _}_

_pX|A_ ( _x_ ) =

E[ _X | A_ ] =

# Total Expectation theorem

- Partition of sample space into disjoint events _A_ 1 _, A_ 2 _, . . . , An_


<!-- Start of picture text -->
A1<br>B<br>A2 A3<br><!-- End of picture text -->

P( _B_ ) = P( _A_ 1)P( _B | A_ 1)+ _· · ·_ +P( _An_ )P( _B | An_ ) _pX_ ( _x_ ) = P( _A_ 1) _pX|A_ 1( _x_ )+ _· · ·_ +P( _An_ ) _pX|An_ ( _x_ ) E[ _X_ ] = P( _A_ 1)E[ _X | A_ 1]+ _· · ·_ +P( _An_ )E[ _X | An_ ]

- Geometric example: _A_ 1 : _{X_ = 1 _}_ , _A_ 2 : _{X >_ 1 _}_ =

- E[ _X_ ] P( _X_ = 1)E[ _X | X_ = 1] +P( _X >_ 1)E[ _X | X >_ 1]

# Geometric PMF

- _X_ : number of independent coin tosses until first head


- Memoryless property: Given that _X >_ 2, the r.v. _X −_ 2 has same geometric PMF


<!-- Start of picture text -->
p<br>pX (k) pX |X>2(k)<br>p(1-p)2<br>p<br>... ...<br>1 k 3 k<br>pX- 2|X>2(k)<br>p<br>...<br>1 k<br><!-- End of picture text -->

# Joint PMFs

- _pX,Y_ ( _x, y_ ) = P( _X_ = _x_ and _Y_ = _y_ )


<!-- Start of picture text -->
y<br>4 1/20 2/20 2/20<br>3 2/20 4/20 1/20 2/20<br>2 1/20 3/20 1/20<br>1 1/20<br>1 2 3 4 x<br><!-- End of picture text -->

   - � � _pX,Y_ ( _x, y_ ) = _x y_

   - _pX_ ( _x_ ) = � _pX,Y_ ( _x, y_ ) _y_

   - _pX|Y_ ( _x | y_ ) = P( _X_ = _x | Y_ = _y_ ) = _pXp,YY_ ( ( _x, yy_ ) )

   - � _pX|Y_ ( _x | y_ ) = _x_

- Solve to get E[ _X_ ] = 1 _/p_

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
