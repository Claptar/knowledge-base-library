---
title: Unit 09 — linalg Part 11 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit9-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit9-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — linalg Part 11 —

**Source:** [`units/unit9-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit9-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can do a fast matrix multiply, _Ab_ , as follows in pseudo-code:

f o r ( i in 1: nrows (A) ) { x [ i ] = 0 # should a l s o check t h a t row i s not empty . . . f o r ( j in ( rowptr [ i ] : ( rowptr [ i +1] _−_ 1)) { x [ i ] = x [ i ] + value [ j ] * b [ c o l i n d i c e s [ j ] ] } }

How many computations have we done? Only _k_ multiplies and _O_ ( _k_ ) additions where _k_ is the number of non-zero elements of _A_ . Compare this to the usual _O_ ( _n_<sup>2</sup> ) for dense multiplication.

Note that for the Cholesky of a sparse matrix, if the sparsity pattern is fixed, but the entries change, one can precompute an optimal re-ordering that retains as much sparsity in _U_ as possible. Then multiple Cholesky decompositions can be done more quickly as the entries change.

**Banded matrices** Suppose we have a banded matrix _A_ where the lower bandwidth is _p_ , namely _Aij_ = 0 for _i > j_ + _p_ and the upper bandwidth is _q_ ( _Aij_ = 0 for _j > i_ + _q_ ). An alternative

30

to reducing to _Ux_ = _b_<sup>_∗_</sup> is to compute _A_ = _LU_ and then do two solutions, _U_<sup>_−_1</sup> ( _L_<sup>_−_1</sup> _b_ ). One can show that the computational complexity of the LU factorization is _O_ ( _npq_ ) for banded matrices, while solving the two triangular systems is _O_ ( _np_ + _nq_ ), so for small _p_ and _q_ , the speedup can be dramatic.

Banded matrices come up in time series analysis. E.g., MA models produce banded covariance structures because the covariance is zero after a certain number of lags.

### **5.3 Low rank updates**

A transformation of the form _A − uv_<sup>_⊤_</sup> is a rank-one update because _uv_<sup>_⊤_</sup> is of rank one. More generally a low rank update of _A_ is _A_<sup>˜</sup> = _A − UV_<sup>_⊤_</sup> where _U_ and _V_ are _n × m_ with _n ≥ m_ . The Sherman-Morrison-Woodbury formula tells us that


so if we know _x_ 0 = _A_<sup>_−_1</sup> _b_ , then the solution to _Ax_<sup>˜</sup> = _b_ is _x_ + _A_<sup>_−_1</sup> _U_ ( _Im − V_<sup>_⊤_</sup> _A_<sup>_−_1</sup> _U_ )<sup>_−_1</sup> _V_<sup>_⊤_</sup> _x_ . Provided _m_ is not too large, and particularly if we already have a factorization of _A_ , then _A_<sup>_−_1</sup> _U_ is not too bad computationally, and _Im − V_<sup>_⊤_</sup> _A_<sup>_−_1</sup> _U_ is _m × m_ . As a result _A_<sup>_−_1</sup> ( _U_ ( _· · ·_ )<sup>_−_1</sup> _V_<sup>_⊤_</sup> _x_ ) isn’t too bad.

This also comes up in working with precision matrices in Bayesian problems where we may have _A_<sup>_−_1</sup> but not _A_ (we often add precision matrices to find conditional normal distributions). An alternative expression for the formula is _A_<sup>˜</sup> = _A_ + _UCV_<sup>_⊤_</sup> , and the identity tells us


Basically Sherman-Morrison-Woodbury gives us matrix identities that we can use in combination with our knowledge of smart ways of solving systems of equations.

---

[← Unit 09 — linalg Part 10 —](10-unit-09-linalg-part-10.md) · [Up: contents](index.md) · [6 Iterative solutions of linear systems →](12-6-iterative-solutions-of-linear-systems.md)
