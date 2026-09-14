---
title: Regression
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/24-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Regression

**Source:** `lectures/24-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
y Residualˆ ˆ ×<br>( xi, yi ) x yi − θ 0  − θ 1 xi ×<br>×<br>x y =  θ ˆ 0 +  θ ˆ 1 x<br>× ×<br>×<br>= 0 y x<br><!-- End of picture text -->

- Data: ( _x_ 1 _, y_ 1) _,_ ( _x_ 2 _, y_ 2) _, . . . ,_ ( _xn, yn_ )

- Model: _y ≈ θ_ 0 + _θ_ 1 _x_

_n_ min ￿ ( _yi − θ_ 0 _− θ_ 1 _xi_<sup>)</sup> 2 ( _∗_ ) _θ_ 0 _,θ_ 1 _i_ =1

- One interpretation: _Yi_ = _θ_ 0 + _θ_ 1 _xi_ + _Wi_ , _Wi ∼ N_ (0 _, σ_ 2), i.i.d.

- **–** Likelihood function _fX,Y |θ_ ( _x, y_ ; _θ_ ) is:


- Take logs, same as (*)

- Least sq. _↔_ pretend _Wi_ i.i.d. normal

---

[← Outline](03-outline.md) · [Up: contents](index.md) · [Linear regression →](05-linear-regression.md)
