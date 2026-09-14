---
title: Buffon’s needle
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Buffon’s needle

**Source:** `lectures/09-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Parallel lines at distance _d_ Needle of length _￿_ (assume _￿< d_ )


- Interpretation:

- **P** ( _x ≤ X ≤ x_ + _δ, y ≤ Y ≤ y_ + _δ_ ) _≈ fX,Y_ ( _x, y_ ) _·δ_<sup>2</sup>

- Expectations:

- **E** [ _g_ ( _X, Y_ )] = ￿ _−∞∞_ ￿ _−∞∞ g_ ( _x, y_ ) _fX,Y_ ( _x, y_ ) _dx dy_

- From the joint to the marginal: _fX_ ( _x_ ) _· δ ≈_ **P** ( _x ≤ X ≤ x_ + _δ_ ) =

- _X_ and _Y_ are called independent if _fX,Y_ ( _x, y_ ) = _fX_<sup>(</sup> _x_<sup>)</sup> _fY_ ( _y_ ) _,_ for all _x, y_

   - Find **P** (needle intersects one of the lines)

-


<!-- Start of picture text -->
q<br>x<br>l<br>d<br><!-- End of picture text -->

- _X ∈_ [0 _, d/_ 2]: distance of needle midpoint to nearest line

- Model: _X_ , Θ uniform, independent

   - _fX,_ Θ( _x, θ_ ) = 0 _≤ x ≤ d/_ 2 _,_ 0 _≤ θ ≤ π/_ 2

- _￿_

- _•_ Intersect if _X ≤_ sin Θ 2


1

---

[← Summary of concepts](03-summary-of-concepts.md) · [Up: contents](index.md) · [Conditioning →](05-conditioning.md)
