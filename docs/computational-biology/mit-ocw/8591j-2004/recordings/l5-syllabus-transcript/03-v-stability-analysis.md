---
title: V Stability analysis
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l5-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# V Stability analysis

**Source:** `recordings/l5-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider the following two coupled differential equations:

& _x_ = _f_ ( _x_ , _y_ ) & **[V.1]** = _y g x y_ ( , )

The nullclines are defined as:

& _x_ & = 0 → _f_ ( _x o_ , _y o_ ) = 0 **[V.2]** _y_ = 0 → _g x y_ ( _o_ , _o_ ) = 0 in order to solve [V.2] we linearize around the fixed point (xo,yo): o,yo): ,yo): o): ): ~ _x_ ≡ _x_ − _x o_ ~ **[V.3]** _y_ ≡ _y_ − _y o_

in order to solve [V.2] we linearize around the fixed point (xo,yo): o,yo): ,yo): o): ):

If f(x,y) and g(x,y) are approximated by a first order Taylor expansion, [V.2] can be written as:


or in matrix notation:


The matrix A is characterized by its trace and the determinant:

τ = _trace_ ( _A_ ) = _a_ + _d_ = ∆ det( _A_ ) = _ad_ − _bc_

**[V.6]**

Let’s try to find a solution of the convenient form:

_v_ v& = λ _v_ v = _A v_ v

**[V.7]**

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

24

This vector is called the eigenvector, λ is the corresponding eigenvalue. [V.7] can be solved by:


leading to:


or


For a stable fixed point both λ1 and λ2 should be negative. Therefore a stable fixed point is characterized by:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

25

---

[← Reference](02-reference.md) · [Up: contents](index.md)
