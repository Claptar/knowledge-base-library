---
title: Conditioning
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Conditioning

**Source:** `lectures/09-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Recall

      - **P** ( _x ≤ X ≤ x_ + _δ_ ) _≈ fX_ ( _x_ ) _· δ_

- By analogy, would like:

   - **P** ( _x ≤ X ≤ x_ + _δ | Y ≈ y_ ) _≈ fX|Y_ (<sup>_x | y_)</sup><sup>_· δ_</sup>

- This leads us to the definition:

   - _fX,Y_ ( _x, y_ )

   - _fX|Y_ ( _x | y_ ) = _fY_ ( _y_ ) if _fY_ ( _y_ ) _>_ 0

- For given _y_ , conditional PDF is a (normalized) “section” of the joint PDF

- If independent, _fX,Y_ = _fXfY_ , we obtain _fX|Y_ ( _x|y_ ) = _fX_ ( _x_ )

- Stick-breaking example

- _•_ Break a stick of length _￿_ twice: break at _X_ : uniform in [0 _,_ 1]; break again at _Y_ , uniform in [0 _, X_ ]


<!-- Start of picture text -->
f X(x)   f Y |X (y | x)<br>L x  y<br>fX,Y  ( x, y ) =  fX ( x ) fY |X ( y | x ) =<br>on the set:<br> y<br>L<br>L x<br>E [ Y | X =  x ] = ￿ yfY |X ( y | X =  x )  dy =<br><!-- End of picture text -->


<!-- Start of picture text -->
Joint, Marginal and Conditional Densities<br>Area of slice = Height of marginal<br>density at  x<br>Renormalizing slices for<br>fixed x gives conditional<br>Slice through densities for Y given X =  x<br>density surface<br>for fixed  x<br><!-- End of picture text -->

Image by MIT OpenCourseWare, adapted from _Probability_ , by J. Pittman, 1999.


<!-- Start of picture text -->
1<br>fX,Y  ( x, y ) = , 0  ≤ y ≤ x ≤ ￿<br>￿x<br> y<br>L<br>L x<br><!-- End of picture text -->


<!-- Start of picture text -->
=<br>fY  ( y ) ￿ fX,Y  ( x, y )  dx<br>￿ 1<br>= dx<br>￿ y ￿x<br>1 ￿<br>= log , 0  ≤ y ≤ ￿<br>￿ y<br>￿ ￿ 1 ￿ ￿<br>E [ Y  ] = yfY  ( y )  dy = y log dy =<br>￿0 ￿0 ￿ y 4<br><!-- End of picture text -->

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Buffon’s needle](04-buffon-s-needle.md) · [Up: contents](index.md)
