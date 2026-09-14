---
title: 1 Change of Slope Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Change of Slope Model

**Source:** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

While our focus, in the last few lectures, has been on sinusoidal models, the methodology can be applied in the same way to some other nonlinear regression models. As an illustrative example, we study the change of slope model today. Other examples can be found in Homework Two. The change of slope model is given by:


i.i.d with _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Here ReLU( _t − c_ ) = ( _t − c_ )+ equals 0 if _t ≤ c_ and equals _t − c_ if _t ≥ c_ . We can also write


( _·_ )+ is also called the positive part function, or, the ramp function.

The model (1) says that for times _t ≤ c_ , the slope of the regression line is _β_ 1, while for _t > c_ , the slope changes to ( _β_ 1 + _β_ 2). An alternative name for this model is “Broken-stick regression”. This is because the function


resembles a broken stick.

The unknown parameters for this model are _c, β_ 0 _, β_ 1 _, β_ 2 as well as _σ_ . The unknown parameter _c_ makes (1) a nonlinear regression model. If _c_ were known, then (1) would be a linear regression model:


with


1

---

[Up: contents](index.md) · [2 Estimation of c, β 0 , β 1 , β 2 , σ →](02-2-estimation-of-c-β-0-β-1-β-2-σ.md)
