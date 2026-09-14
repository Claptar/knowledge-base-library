---
title: 6 Iterative solutions of linear systems
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit9-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit9-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Iterative solutions of linear systems

**Source:** [`units/unit9-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit9-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Gauss-Seidel** Suppose we want to iteratively solve _Ax_ = _b_ . Here’s the algorithm, which sequentially updates each element of _x_ in turn.

- Start with an initial approximation, _x_<sup>(0)</sup> .

- <u>1</u>

- • Hold all but _x_<sup>(0)</sup> 1 constant and solve to find _x_<sup>(1)</sup> 1 = _a_ 11<sup>(</sup><sup>_b_1</sup><sup>_−_�</sup> _j_<sup>_n_</sup> =2<sup>_a_1</sup><sup>_jx_</sup> _j_<sup>(0)).</sup>

- Repeat for the other rows of _A_ (i.e., the other elements of _x_ ), finding _x_<sup>(1)</sup> .

- Now iterate to get _x_<sup>(2)</sup> , _x_<sup>(3)</sup> , etc. until a convergence criterion is achieved, such as _∥x_<sup>(</sup><sup>_k_)</sup> _− x_<sup>(</sup><sup>_k−_1)</sup> _∥≤ ϵ_ or _∥r_<sup>(</sup><sup>_k_)</sup> _− r_<sup>(</sup><sup>_k−_1)</sup> _∥≤ ϵ_ for _r_<sup>(</sup><sup>_k_)</sup> = _b − Ax_<sup>(</sup><sup>_k_)</sup> .

Let’s consider how many operations are involved in a single update: _O_ ( _n_ ) for each element, so _O_ ( _n_<sup>2</sup> ) for each update. Thus if we can stop well before _n_ iterations, we’ve saved computation relative to exact methods.

If we decompose _A_ = _L_ + _D_ + _U_ where _L_ is strictly lower triangular, _U_ is strictly upper triangular, then Gauss-Seidel is equivalent to solving


30

and we know that solving the lower triangular system is _O_ ( _n_<sup>2</sup> ).

It turns out that the rate of convergence depends on the spectral radius of ( _L_ + _D_ )<sup>_−_1</sup> _U_ . Gauss-Seidel amounts to optimizing by moving in axis-oriented directions, so it can be slow in some cases.

**Conjugate gradient** For positive definite _A_ , conjugate gradient (CG) reexpresses the solution to _Ax_ = _b_ as an optimization problem, minimizing


since the derivative of _f_ ( _x_ ) is _Ax − b_ and at the minimum this gives _Ax − b_ = 0.

Instead of finding the minimum by following the gradient at each step (so-called steepest descent, which can give slow convergence - we’ll see a demonstration of this in the optimization unit), CG chooses directions that are mutually conjugate w.r.t. _A_ , _d_<sup>_⊤_</sup> _i_<sup>_Adj_=0for</sup><sup>_i̸_=</sup><sup>_j_.The</sup> method successively chooses vectors giving the direction, _dk_ , in which to move down towards the minimum and a scaling of how much to move, _αk_ . If we start at _x_ (0), the _k_ th point we move to is _x_ ( _k_ ) = _x_ ( _k−_ 1) + _αkdk_ so we have


and we use a convergence criterion such as given above for Gauss-Seidel. The directions are chosen to be the residuals, _b − Ax_ ( _k_ ). Here’s the basic algorithm:

- Choose _x_ (0) and define the residual, _r_ (0) = _b − Ax_ (0) (the error on the scale of _b_ ) and the direction, _d_ 0 = _r_ (0) and set _k_ = 0.

- Then iterate

   - _r_<sup>_⊤_</sup> <u>(</u> _k_ <u>)</u><sup>_r_(</sup><sup>_k_)</sup>

   - **–** _αk_ = _d_<sup>_⊤_</sup> _k_<sup>_Adk_(choosestepsizesonexterrorwillbeorthogonaltocurrentdirection-</sup> which we can express in terms of the residual, which is easily computable)

   - _x_ ( _k_ +1) = _x_ ( _k_ ) + _αkdk_ (update current value)

   - _r_ ( _k_ +1) = _r_ ( _k_ ) _− αkAdk_ (update current residual)

   - _r_<sup>_⊤_</sup> <u>(</u> _k_ <u>+1)</u><sup>_r_(</sup><sup>_k_+1)</sup>

   - **–** _dk_ +1 = _r_ ( _k_ +1) + _r_<sup>_⊤_</sup> _dk_ (choose next direction by conjugate Gram-Schmidt, start( _k_ )<sup>_r_(</sup><sup>_k_)</sup>

   - ing with _r_ ( _k_ +1) and removing components that are not _A_ -orthogonal to previous directions, but it turns out that _r_ ( _k_ +1) is already _A_ -orthogonal to all but _dk_ ).

- Stop when _∥r_<sup>(</sup><sup>_k_+1)</sup> _∥_ is sufficiently small.

31

The convergence of the algorithm depends in a complicated way on the eigenvalues, but in general convergence is faster when the condition number is smaller (the eigenvalues are not too spread out). CG will in principle give the exact answer in _n_ steps (where _A_ is _n×n_ ). However, computationally we lose accuracy and interest in the algorithm is really as an iterative approximation where we stop before _n_ steps. The approach basically amounts to moving in axis-oriented directions in a space stretched by _A_ .

In general, CG is used for large sparse systems.

See the extensive description from Shewchuk for more details and for the figures shown in class, as well as the use of CG when _A_ is not positive definite.

**Updating a solution** Sometimes we have solved a system, _Ax_ = _b_ and then need to solve _Ax_ = _c_ . If we have solved the initial system using a factorization, we can reuse that factorization and solve the new system in _O_ ( _n_<sup>2</sup> ). Iterative approaches can do a nice job if _c_ = _b_ + _δb_ . Start with the solution _x_ for _Ax_ = _b_ as _x_<sup>(0)</sup> and use one of the methods above.

32

---

[← 5 Computation](10-5-computation.md) · [Up: contents](index.md)
