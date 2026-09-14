---
title: The distribution of X + Y
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The distribution of X + Y

**Source:** `lectures/11-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- _W_ = _X_ + _Y_ ; _X, Y_ independent


- _pW_ ( _w_ ) = P( _X_ + _Y_ = _w_ ) = � P( _X_ = _x_ )P( _Y_ = _w − x_ ) _x_

- = � _pX_ ( _x_ ) _pY_ ( _w − x_ ) _x_

- Mechanics:

- Put the pmf’s on top of each other

- Flip the pmf of _Y_

- Let _Y_ = _g_ ( _X_ ) _g_ strictly monotonic.


<!-- Start of picture text -->
d g<br>y slope  dx (x)<br>g(x)<br>[y, y+?]<br>x<br>[x, x+d]<br><!-- End of picture text -->

- Event _x ≤ X ≤ x_ + _δ_ is the same as _g_ ( _x_ ) _≤ Y ≤ g_ ( _x_ + _δ_ ) or (approximately) _g_ ( _x_ ) _≤ Y ≤ g_ ( _x_ ) + _δ|_ ( _dg/dx_ )( _x_ ) _|_

- Hence,

   - _dg_

   - _δfX_ ( _x_ ) = _δfY_ ( _y_ ) ��� ( _x_ )��� � _dx_ �

   - where _y_ = _g_ ( _x_ )

---

[← Example](01-example.md) · [Up: contents](index.md) · [The continuous case →](03-the-continuous-case.md)
