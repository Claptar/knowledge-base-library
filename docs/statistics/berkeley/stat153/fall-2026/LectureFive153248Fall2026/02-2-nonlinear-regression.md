---
title: 2 Nonlinear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFive153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureFive153248Fall2026.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Nonlinear Regression

**Source:** [`LectureFive153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFive153248Fall2026.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall next start our discussion on models in which certain parameters appear in a nonlinear fashion. A simple example is:


i.i.d with _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Here ReLU( _t − c_ ) = ( _t − c_ )+ equals 0 if _t ≤ c_ and equals _t − c_ if _t ≥ c_ . We can also write


( _·_ )+ is also called the positive part function, or, the ramp function.

The model (12) says that for times _t ≤ c_ , the slope of the regression line is _β_ 1, while for _t > c_ , the slope changes to ( _β_ 1 + _β_ 2). We shall refer to (12) as the ’Change of Slope’ model. An alternative name for this model is “Broken-stick regression”. This is because the function


resembles a broken stick.

The unknown parameters for this model are _c, β_ 0 _, β_ 1 _, β_ 2 as well as _σ_ . The unknown parameter _c_ makes (12) a nonlinear regression model. If _c_ were known, then (12) would be a linear regression model:


with


7

We shall discuss estimation and uncertainty quantification for _c_ in the next lecture.

8

---

[← 1 Bayesian Inference for Linear Regression](01-1-bayesian-inference-for-linear-regression.md) · [Up: contents](index.md)
