---
title: The continuous case
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The continuous case

**Source:** `lectures/11-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- _W_ = _X_ + _Y_ ; _X, Y_ independent


<!-- Start of picture text -->
y<br>w<br>w x<br>x + y = w<br><!-- End of picture text -->

   - _fW |X_ ( _w | x_ ) = _fY_ ( _w − x_ )

   - _fW,X_ ( _w, x_ ) = _fX_ ( _x_ ) _fW |X_<sup>(</sup><sup>_w| x_)</sup> _−_

   - = _fX_ ( _x_ ) _fY_ ( _w x_ )

   - _fW_ ( _w_ ) = _fX_ ( _x_ ) _fY_ ( _w − x_ ) _dx_ � _−∞∞_

- Shift the flipped pmf by _w_ (to the right if _w >_ 0)

- Cross-multiply and add

1

Two independent normal r.v.s


- Ellipse is a circle when _σx_ = _σy_

The sum of independent normal r.v.’s

- _X ∼ N_ (0 _, σx_ 2), _Y ∼ N_ (0 _, σy_ 2), independent


- Conclusion: _W_ is normal

- 2

- mean=0, variance= _σx_<sup>2</sup> + _σy_

- same argument for nonzero mean case

---

[← The distribution of X + Y](02-the-distribution-of-x-y.md) · [Up: contents](index.md) · [Covariance →](04-covariance.md)
