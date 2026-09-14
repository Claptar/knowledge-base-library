---
title: Unit 09 — linalg Part 02 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit9-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit9-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — linalg Part 02 —

**Source:** [`units/unit9-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit9-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

How many computations have we done? Only _k_ multiplies and _O_ ( _k_ ) additions where _k_ is the number of non-zero elements of _A_ . Compare this to the usual _O_ ( _n_<sup>2</sup> ) for dense multiplication. Note that for the Cholesky of a sparse matrix, if the sparsity pattern is fixed, but the entries change, one can precompute an optimal re-ordering that retains as much sparsity in _U_ as possible. Then multiple Cholesky decompositions can be done more quickly as the entries change.

**Banded matrices** Suppose we have a banded matrix _A_ where the lower bandwidth is _p_ , namely _Aij_ = 0 for _i > j_ + _p_ and the upper bandwidth is _q_ ( _Aij_ = 0 for _j > i_ + _q_ ). An alternative to reducing to _Ux_ = _b_<sup>_∗_</sup> is to compute _A_ = _LU_ and then do two solutions, _U_<sup>_−_1</sup> ( _L_<sup>_−_1</sup> _b_ ). One can show that the computational complexity of the LU factorization is _O_ ( _npq_ ) for banded matrices, while solving the two triangular systems is _O_ ( _np_ + _nq_ ), so for small _p_ and _q_ , the speedup can be dramatic.

Banded matrices come up in time series analysis. E.g., MA models produce banded covariance structures because the covariance is zero after a certain number of lags.

### **6.3 Low rank updates**

A transformation of the form _A − uv_<sup>_⊤_</sup> is a rank-one update because _uv_<sup>_⊤_</sup> is of rank one.

More generally a low rank update of _A_ is _A_<sup>˜</sup> = _A − UV_<sup>_⊤_</sup> where _U_ and _V_ are _n × m_ with _n ≥ m_ . The Sherman-Morrison-Woodbury formula tells us that


so if we know _x_ 0 = _A_<sup>_−_1</sup> _b_ , then the solution to _Ax_<sup>˜</sup> = _b_ is _x_ + _A_<sup>_−_1</sup> _U_ ( _Im − V_<sup>_⊤_</sup> _A_<sup>_−_1</sup> _U_ )<sup>_−_1</sup> _V_<sup>_⊤_</sup> _x_ . Provided _m_ is not too large, and particularly if we already have a factorization of _A_ , then _A_<sup>_−_1</sup> _U_ is not too bad computationally, and _Im − V_<sup>_⊤_</sup> _A_<sup>_−_1</sup> _U_ is _m × m_ . As a result _A_<sup>_−_1</sup> ( _U_ ( _· · ·_ )<sup>_−_1</sup> _V_<sup>_⊤_</sup> _x_ ) isn’t too bad.

This also comes up in working with precision matrices in Bayesian problems where we may

32

have _A_<sup>_−_1</sup> but not _A_ (we often add precision matrices to find conditional normal distributions). An alternative expression for the formula is _A_<sup>˜</sup> = _A_ + _UCV_<sup>_⊤_</sup> , and the identity tells us


Basically Sherman-Morrison-Woodbury gives us matrix identities that we can use in combination with our knowledge of smart ways of solving systems of equations.

## **7 Iterative solutions of linear systems**

**Gauss-Seidel** Suppose we want to iteratively solve _Ax_ = _b_ . Here’s the algorithm, which sequentially updates each element of _x_ in turn.

- Start with an initial approximation, _x_<sup>(0)</sup> .

- <u>1</u>

- • Hold all but _x_<sup>(0)</sup> 1 constant and solve to find _x_<sup>(1)</sup> 1 = _a_ 11<sup>(</sup><sup>_b_1</sup><sup>_−_�</sup> _j_<sup>_n_</sup> =2<sup>_a_1</sup><sup>_jx_</sup> _j_<sup>(0)).</sup>

- Repeat for the other rows of _A_ (i.e., the other elements of _x_ ), finding _x_<sup>(1)</sup> .

- Now iterate to get _x_<sup>(2)</sup> , _x_<sup>(3)</sup> , etc. until a convergence criterion is achieved, such as _∥x_<sup>(</sup><sup>_k_)</sup> _− x_<sup>(</sup><sup>_k−_1)</sup> _∥≤ ϵ_ or _∥r_<sup>(</sup><sup>_k_)</sup> _− r_<sup>(</sup><sup>_k−_1)</sup> _∥≤ ϵ_ for _r_<sup>(</sup><sup>_k_)</sup> = _b − Ax_<sup>(</sup><sup>_k_)</sup> .

Let’s consider how many operations are involved in a single update: _O_ ( _n_ ) for each element, so _O_ ( _n_<sup>2</sup> ) for each update. Thus if we can stop well before _n_ iterations, we’ve saved computation relative to exact methods.

If we decompose _A_ = _L_ + _D_ + _U_ where _L_ is strictly lower triangular, _U_ is strictly upper triangular, then Gauss-Seidel is equivalent to solving


and we know that solving the lower triangular system is _O_ ( _n_<sup>2</sup> ).

It turns out that the rate of convergence depends on the spectral radius of ( _L_ + _D_ )<sup>_−_1</sup> _U_ . Gauss-Seidel amounts to optimizing by moving in axis-oriented directions, so it can be slow in some cases.

**Conjugate gradient** For positive definite _A_ , conjugate gradient (CG) reexpresses the solution to _Ax_ = _b_ as an optimization problem, minimizing


33

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

The convergence of the algorithm depends in a complicated way on the eigenvalues, but in general convergence is faster when the condition number is smaller (the eigenvalues are not too spread out). CG will in principle give the exact answer in _n_ steps (where _A_ is _n×n_ ). However, computationally we lose accuracy and interest in the algorithm is really as an iterative approximation where we stop before _n_ steps. The approach basically amounts to moving in axis-oriented directions in a space stretched by _A_ .

In general, CG is used for large sparse systems.

See the extensive description from Shewchuk for more details and for the figures shown in class, as well as the use of CG when _A_ is not positive definite.

34

**Updating a solution** Sometimes we have solved a system, _Ax_ = _b_ and then need to solve _Ax_ = _c_ . If we have solved the initial system using a factorization, we can reuse that factorization and solve the new system in _O_ ( _n_<sup>2</sup> ). Iterative approaches can do a nice job if _c_ = _b_ + _δb_ . Start with the solution _x_ for _Ax_ = _b_ as _x_<sup>(0)</sup> and use one of the methods above.

35

---

[← Unit 9: Numerical linear algebra](01-unit-9-numerical-linear-algebra.md) · [Up: contents](index.md)
