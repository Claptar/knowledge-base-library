---
title: L6 syllabus transcript
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l6-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# L6 syllabus transcript

**Source:** `recordings/l6-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **V Stability analysis**

Consider the following two coupled differential equations:

& _x_ = _f_ ( _x_ , _y_ ) & **[V.1]** _y_ = _g_ ( _x_ , _y_ ) The nullclines are defined as: & _x_ & = 0 → _f_ ( _xo_ , _yo_ ) = 0 **[V.2]** _y_ = 0 → _g_ ( _xo_ , _yo_ ) = 0 in order to solve [V.2] we linearize around the fixed point (xo,yo):o,yo):,yo):o):): ~ _x_ ≡ _x_ − _xo_ ~ **[V.3]** _y_ ≡ _y_ − _yo_

The nullclines are defined as:

in order to solve [V.2] we linearize around the fixed point (xo,yo):o,yo):,yo):o):):

If f(x,y) and g(x,y) are approximated by a first order Taylor expansion, [V.2] can be written as:


or in matrix notation:


The matrix A is characterized by its trace and the determinant:

τ = _trace_ ( _A_ ) = _a_ + _d_ **[V.6]** ∆ = det( _A_ ) = _ad_ − _bc_ Let’s try to find a solution of the convenient form: v& v v _v_ = λ _v_ = _Av_ **[V.7]**

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

24

This vector is called the eigenvector, λ is the corresponding eigenvalue. [V.7] can be solved by:


leading to:


or


For a stable fixed point both λ1 and λ2 should be negative. Therefore a stable fixed point is characterized by:


Now let us use the evaluate the stability of the toggle switch (Chapter IV) as an example:


The fixed points are:


The matrix A is given by:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

25


The trace of this matrix is always negative so the only requirement for stability is that the determinant of this matrix is larger than zero. Let us focus on the conditions for which the determinant equals zero. This would define the boundary in parameter space that separates the bistable from monostable region. Setting the determinant to zero gives:


Using the conditions for the fixed points **[V.13]** gives:


To be able to solve [V.16] we have to make some assumptions. We assume that we are working with strong promoters and therefore α1 and α2 are large and that expression ratio between the ON and OFF state is large. In the case where _u_ >> _v_ , the fixed points are approximated by:


Condition **[V.16]** now becomes:


Consistent with Fig. 2c-d in the toggle switch paper. The other boundary is obtained by realizing that the system is symmetry. By replacing α1 by α2 and γ by β, the other boundary is found:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

26

---

[Up: contents](../index.md)
