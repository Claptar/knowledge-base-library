---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSix153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSix153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`LectureSix153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSix153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **STAT 153 & 248 - Time Series Lecture Six**

**Fall 2025, UC Berkeley**

Aditya Guntuboyina

September 16, 2025

## **1 Nonlinear Regression**

We started discussing nonlinear regression models near the end of last lecture. In these models, certain parameters appear in a nonlinear fashion. One simple example of such a model is:


i.i.d with _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Here ReLU( _t − c_ ) = ( _t − c_ )+ equals 0 if _t ≤ c_ and equals _t − c_ if _t ≥ c_ . We can also write


( _·_ )+ is also called the positive part function, or, the ramp function.

The model (1) says that for times _t ≤ c_ , the slope of the regression line is _β_ 1, while for _t > c_ , the slope changes to ( _β_ 1 + _β_ 2). We shall refer to (1) as the ’Change of Slope’ model. An alternative name for this model is “Broken-stick regression”. This is because the function


resembles a broken stick.

The unknown parameters for this model are _c, β_ 0 _, β_ 1 _, β_ 2 as well as _σ_ . The unknown parameter _c_ makes (1) a nonlinear regression model. If _c_ were known, then (1) would be a linear regression model:


with


1

---

[Up: contents](index.md) · [1.1 Parameter Estimation →](02-1-1-parameter-estimation.md)
