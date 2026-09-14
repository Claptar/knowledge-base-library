---
title: 5 Nonlinear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Nonlinear Regression

**Source:** [`LectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFive153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall next start our discussion on models in which certain parameters appear in a nonlinear fashion. A simple example is:


i.i.d with _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Here ReLU( _t − c_ ) = ( _t − c_ )+ equals 0 if _t ≤ c_ and equals _t − c_ if _t ≥ c_ . We can also write

ReLU( _t − c_ ) = ( _t − c_ )+ = ( _t − c_ ) _I{t > c}_ = max( _t − c,_ 0) _._

( _·_ )+ is also called the positive part function, or, the ramp function.

The model (8) says that for times _t ≤ c_ , the slope of the regression line is _β_ 1, while for _t > c_ , the slope changes to ( _β_ 1 + _β_ 2). We shall refer to (8) as the ’Change of Slope’ model. An alternative name for this model is “Broken-stick regression”. This is because the function


resembles a broken stick.

The unknown parameters for this model are _c, β_ 0 _, β_ 1 _, β_ 2 as well as _σ_ . The unknown parameter _c_ makes (8) a nonlinear regression model. If _c_ were known, then (8) would be a linear regression model:


with


5

### **5.1 Estimation of** _c, β_ 0 _, β_ 1 _, β_ 2 _, σ_

Least squares again is the most basic estimation procedure. The sum of squares is given by:


We need to minimize this over all the four variables _β_ 0 _, β_ 1 _, β_ 2 _, c_ . Using matrix notation, we can write


If we fix _c_ , then it is easy to minimize _S_ ( _β, c_ ) over _β_ . This is the same as linear regression and the minimizing _β_ is given by:


and the smallest value of _S_ ( _β, c_ ) for fixed _c_ is _S_ ( _β_<sup>ˆ</sup> _c, c_ ) which is just the RSS in the multiple linear regression with fixed _c_ . We use the notation:


The least squares estimates of _β_ and _c_ can therefore be found in the following way:

1. Fix a finite set of possible values of _c_ . In this change of slope model, it is reasonable to assume that _c ∈{_ 1 _, . . . , n}_ .

2. For each value of _c_ in the chosen set, calculate _β_<sup>ˆ</sup> _c_ and define _RSS_ ( _c_ ) = _S_ ( _β_<sup>ˆ</sup> _c, c_ ).

3. Take _c_ ˆ to be the value of _c_ which minimizes _RSS_ ( _c_ ).

4. Take _β_ = _β_<sup>ˆ</sup> _c_ ˆ.

We shall revisit this and also look at uncertainty quantification in this model next week .

6

---

[← 4 Proof of (4)](04-4-proof-of-4.md) · [Up: contents](index.md)
