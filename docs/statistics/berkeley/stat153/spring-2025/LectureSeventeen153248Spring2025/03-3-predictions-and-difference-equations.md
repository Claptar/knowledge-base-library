---
title: 3 Predictions and Difference Equations
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeventeen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSeventeen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Predictions and Difference Equations

**Source:** [`LectureSeventeen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeventeen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Given a fitted AR(p) model with parameter estimates _φ_<sup>ˆ</sup> 0 _, . . . , φ_<sup>ˆ</sup> _p_ , predictions _y_ ˆ _n_ + _i_ for _i_ = 1 _,_ 2 _, . . ._ are obtained by the recursion:


where the recursion is initialized with


The behavior of the predictions (9) given by the _AR_ ( _p_ ) model can be understood by looking at difference equations. A difference equation is of the form:


This is initialized by specifying the values of _u_ 0 _, u_ 1 _, . . . , up−_ 1. Clearly the prediction recursion (9) of the _AR_ ( _p_ ) model along with the initial condition (10) is similar to (11) (basically take _uj_ = _Y_<sup>ˆ</sup> _n_ +1 _−p_ + _j_ ). (11) is called a difference equation of order _p_ . In order to understand its solutions, let us start with the case _p_ = 1.

### **3.1 First Order (** _p_ = 1 **)**

Here _p_ = 1 so the difference equation becomes:


along with an initial value specification for _u_ 0. We first convert this equation into a **homogeneous** difference equation (a homogeneous equation is one with no intercept term) by taking


so that


Thus _vk_ satisfies the homogenous equation:


It is now easy to see that the solution is given by


The solution for _uk_ is thus given by


The last expression above also makes sense when _α_ 1 = 1 (note that, when _α_ 1 = 1, some of the previous expressions do not make sense because 1 _− α_ 1 appearing in the denominator). The behavior of _uk_ will then be of three kinds depending on the precise value of _α_ 1:

7

1. _|α_ 1 _| <_ 1: Here _uk_ converges exponentially to _α_ 0 _/_ (1 _− α_ 1).

2. _|α_ 1 _| >_ 1: Here, when _k_ gets large, _uk_ is essentially equal to _α_ 1<sup>_ku_0whichisexplodingto</sup> infinity exponentially in magnitude.

3. _α_ 1 = 1: Here _uk_ = _kα_ 0 + _u_ 0 which is linear

4. _α_ 1 = _−_ 1: Here _uk_ oscillates between the two values _u_ 0 and _α_ 0 _− u_ 0.

We shall see formulae for solutions of the difference equation for _p ≥_ 2 in the next lecture.

### **3.2 Recommended Reading for Today**

1. For more on fitting _AR_ ( _p_ ) models to data, see Section 3.5 of the book by Shumway and Stoffer titled _Time Series Analysis and its applications_ (Fourth Edition).

2. For more on difference equations, see Section 3.2 of the Shumway-Stoffer book.

8

---

[← 2 The AR Model](02-2-the-ar-model.md) · [Up: contents](index.md)
