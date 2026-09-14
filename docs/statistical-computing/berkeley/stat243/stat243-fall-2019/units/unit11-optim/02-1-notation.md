---
title: 1 Notation
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Notation

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We’ll make use of the first derivative (the gradient) and second derivative (the Hessian) of functions. We’ll generally denote univariate and multivariate functions (without distinguishing between them) as _f_ ( _x_ ) with _x_ = ( _x_ 1 _, . . . , xp_ ). The (column) vector of first partial derivatives (the gradient) is _f_<sup>_′_</sup> ( _x_ ) = _∇f_ ( _x_ ) = ( _∂x_<sup>_∂f_</sup> 1<sup>_, . . . ,_</sup> _∂x_<sup>_∂f_</sup> _p_<sup>)</sup><sup>_⊤_and the matrix of second partial derivatives (the Hessian) is</sup>


In considering iterative algorithms, I’ll use _x_ 0 _, x_ 1 _, . . . , xt, xt_ +1 to indicate the sequence of values as we search for the optimum, denoted _x_<sup>_∗_</sup> . _x_ 0 is the starting point, which we must choose (often

1

carefully). If it’s unclear at any point whether I mean a value of _x_ in the sequence or a sub-element of the _x_ vector, let me know, but hopefully it will be clear from context most of the time.

I’ll try to use _x_ (or if we’re talking explicitly about a likelihood, _θ_ ) to indicate the argument with respect to which we’re optimizing and _Y_ to indicate data involved in a likelihood. I’ll try to use _z_ to indicate covariates/regressors so there’s no confusion with _x_ .

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Overview →](03-2-overview.md)
