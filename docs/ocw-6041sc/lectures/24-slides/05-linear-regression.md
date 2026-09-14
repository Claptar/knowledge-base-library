---
title: Linear regression
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/24-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Linear regression

**Source:** `lectures/24-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- **Solution** (set derivatives to zero):


- **Interpretation** of the form of the solution

- **–** Assume a model _Y_ = _θ_ 0 + _θ_ 1 _X_ + _W W_ independent of _X_ , with zero mean

- Check that

   - _θ_ 1 = cov( _X, Y_ <u>)=</u> **E** <u>￿(</u> _X −_ **E** [ _X_ ])( _Y −_ **E** [ _Y_ ])￿ var( _X_ ) **E** ~~￿~~ ( _X −_ **E** [ _X_ ])2 ~~￿~~

- Solution formula for _θ_<sup>ˆ</sup> 1 uses natural estimates of the variance and covariance

1

**The world of linear regression**

- **Multiple linear regression:**

- **data:** ( _xi, x_<sup>_￿_</sup> _i, xi_<sup>_￿￿_</sup> _, yi_ ), _i_ = 1 _, . . . , n_

- **model:** _y ≈ θ_ 0 + _θx_ + _θ_<sup>_￿_</sup> _x_<sup>_￿_</sup> + _θ_<sup>_￿￿_</sup> _x_<sup>_￿￿_</sup>

- **formulation:**

_n_ min ￿ ( _yi − θ_ 0 _− θxi − θ_<sup>_￿_</sup> _x￿i − θ_<sup>_￿￿_</sup> _x_<sup>_￿￿_</sup> _i_<sup>)</sup> 2 _θ,θ_<sup>_￿_</sup> _,θ_<sup>_￿￿_</sup> _i_ =1

- **Choosing the right variables**

- model _y ≈ θ_ 0 + _θ_ 1 _h_ ( _x_ ) 2

- e.g., _y ≈ θ_ 0 + _θ_ 1 _x_

- work with data points ( _yi, h_ ( _x_ ))

- formulation:

**The world of regression** (ctd.)

- **In practice,** one also reports

- Confidence intervals for the _θi_

- “Standard error” (estimate of _σ_ )

   - 2

- 2

- _R_ , a measure of “explanatory power”

- **Some common concerns**

- Heteroskedasticity

- Multicollinearity

- Sometimes misused to conclude causal relations

- etc.

_n_ min ￿ ( _yi − θ_ 0 _− θ_ 1 _h_ 1( _xi_ ))2 _θ i_ =1

---

[← Regression](04-regression.md) · [Up: contents](index.md) · [Binary hypothesis testing →](06-binary-hypothesis-testing.md)
