---
title: 1 Lagrange duality
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_03_Empirical_Risk_Kernel.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_03_Empirical_Risk_Kernel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Lagrange duality

**Source:** [`notes/Lecture_03_Empirical_Risk_Kernel.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_03_Empirical_Risk_Kernel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To solve the problem in Figure 1, we need to work with kernel SVM which is motivated by the dual problem of the optimization problem. Moreover, the dual problem will also allow us to derive an efficient algorithm to solve SVM better than generic QP software.

**Review of Lagrange with equality constraints** Instead of considering an inequality constraints in the optimization problem for SVM, consider a problem of a simpler form with equality constraint:


We define the **Lagrangian** _L_ : R<sup>_d_</sup> _×_ R<sup>_p_</sup> _→_ R associated with the problem (1) as


We refer to _λi_ as the Lagrange multiplier associated with the _i_ th equality constraint _hi_ (w) = 0. The vector _λ_ = ( _λ_ 1 _, . . . , λn_ )<sup>_′_</sup> is called the **dual variable** or the **Lagrange multiplier vector** associated with the problem (1). We would then find and set _L_ (w _, λ_ )’s partial derivatives to zero:


and solve for w and _λ_ .

**Lagrange with inequality and equality constraints–primal and dual problems** Now we generalize this to constrained optimization problems in which we may have inequality as well as equality constraints:


1

We refer to the above problem as the **primal problem** , and the Lagrangian associated with the primal problem is


Here, _νi ≥_ 0 and _λi_ are the Lagrange multipliers. We can show that the solution of the primal problem (2) is also the solution to the following problem (see footnote for proof)<sup>1</sup> :


We also define the optimal value of the objective function to be _p_<sup>_∗_</sup> = minw _L_ `primal` (w).

Next, we define the **Lagrange dual function** (or just dual function) as


When the Lagrange is unbounded below in w, the dual function takes on the value _−∞_ . The **dual problem** is then defined as


This is exactly the same as our primal problem shown above, except that the order of the “max” and the “min” are now exchanged. We again define the optimal value of the dual problem’s objective to be _d_<sup>_∗_</sup> = max _L_ `dual` (w). w

How are the primal and dual problems related? It is easy to see that


Under certain conditions<sup>2</sup> , we can show that the dual problem and the primal problem have no gap (no

1

_Proof._ To see this, consider the quantity


Then, for a given w: (a) If w violates any of the primal constraints, then we can verify that


Conversely, if the constraints are indeed satisfied for a particular value of w, then _L_ `primal` (w) = _f_ (w). Hence, we conclude


Thus, _L_ `primal` (w) takes the same value as the objective function in the problem (2) for all w that satisfies the primal constraints, and is positive infinity if the constraints are violated. We conclude


Therefore, the solution to the primal problem is also the solution to the unconstrained problem minw _ν_ max _⪰_ 0 _,λ_<sup>_L_(w</sup><sup>_, λ, ν_).</sup>

> 2One set of sufficient conditions: Suppose _f_ and _gi_ ’s are convex function, and _hi_ ’s are affine. Further suppose that the

2

duality gap): _d_<sup>_∗_</sup> = _p_<sup>_∗_</sup> . This suggests there must exists (w<sup>_∗_</sup> _, ν_<sup>_∗_</sup> _, λ_<sup>_∗_</sup> ) satisfies the _Karush-Kuhn-Tucker (KKT)_ conditions, which are defined as

---

[Up: contents](index.md) · [2 SVM-continued →](02-2-svm-continued.md)
