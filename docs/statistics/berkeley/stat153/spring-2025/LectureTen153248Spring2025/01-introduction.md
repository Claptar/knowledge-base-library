---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`LectureTen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **STAT 153 & 248 - Time Series Lecture Ten**

### **Spring 2025, UC Berkeley**

Aditya Guntuboyina

February 20, 2025

For a given time series _y_ 1 _, . . . , yn_ , we consider the model:

_yt_ = _β_ 0 + _β_ 1( _t −_ 1) + _β_ 2ReLU( _t −_ 2) + _· · ·_ + _βn−_ 1ReLU( _t −_ ( _n −_ 1)) + _ϵt_ (1)

i.i.d where, as always, _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Here ReLU( _t − c_ ) = ( _t − c_ )+ equals 0 if _t ≤ c_ and equals ( _t − c_ ) if _t > c_ .

The unknown parameters in this model are _β_ 0 _, β_ 1 _, . . . , βn−_ 1 as well as _σ_ . The model (1) should be compared with the following model that we studied in the previous lecture:

_yt_ = _β_ 0 + _β_ 1( _t −_ 1) + _β_ 2ReLU( _t − c_ 1) + _β_ 3ReLU( _t − c_ 2) + _· · ·_ + _βk_ +1ReLU( _t − ck_ ) + _ϵt._ (2)

Here are the main differences between these two models:

1. The model (2) will be used with a small value of _k_ (such as 1 _,_ 2 _,_ 3 _,_ 4). This makes it a low-dimensional model. On the other hand, the number of unknown parameters in (1) equals _n_ + 1 which is quite large. So (1) is an example of a high-dimensional model.

2. (2) is a nonlinear model because of the presence of the parameters _c_ 1 _, . . . , ck_ . On the other hand, there are no such nonlinear parameters in (1) which makes it a linear regression model.

To summarize, (2) is a low-dimensional nonlinear regression model, while (1) is a highdimensional linear regression model.

---

[Up: contents](index.md) · [1 Parameter Interpretation in (1) →](02-1-parameter-interpretation-in-1.md)
