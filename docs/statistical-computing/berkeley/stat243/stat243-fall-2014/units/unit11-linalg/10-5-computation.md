---
title: 5 Computation
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit11-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit11-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Computation

**Source:** [`units/unit11-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit11-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Linear algebra in R**

Speedups and storage savings can be obtained by working with matrices stored in special formats when the matrices have special structure. E.g., we might store a symmetric matrix as a full matrix but only use the upper or lower triangle. Banded matrices and block diagonal matrices are

27

other common formats. Banded matrices are all zero except for _Ai,i_ + _ck_ for some small number of integers, _ck_ . Viewed as an image, these have bands. The bands are known as co-diagonals.

Note that for many matrix decompositions, you can change whether all of the aspects of the decomposition are returned, or just some, which may speed calculations.

Some useful packages in R for matrices are _Matrix_ , _spam_ , and _bdsmatrix_ . _Matrix_ can represent a variety of rectangular matrices, including triangular, orthogonal, diagonal, etc. and provides methods for various matrix calculations that are specific to the matrix type. _spam_ handles general sparse matrices with fast matrix calculations, in particular a fast Cholesky decomposition. _bdsmatrix_ focuses on block-diagonal matrices, which arise frequently in contexts where there is clustering that induces within-cluster correlation and cross-cluster independence.

In general, matrix operations in R go to compiled C or Fortran code without much intermediate R code, so they can actually be pretty efficient and are based on the best algorithms developed by numerical experts. The core libraries that are used are LAPACK and BLAS (the Linear Algebra PACKage and the Basic Linear Algebra Subroutines). As we’ve discussed in the parallelization unit, one way to speed up code that relies heavily on linear algebra is to make sure you have a BLAS library tuned to your machine. These include OpenBLAS (free; formerly called GotoBLAS), Intel’s MKL, AMD’s ACML, and Apple’s vecLib. These can be installed and R can be linked to the shared object library file ( _.so_ file or _.dylib_ on a Mac) for the fast BLAS. These BLAS libraries are also available in threaded versions that farm out the calculations across multiple cores or processors that share memory.

BLAS routines do vector operations (level 1), matrix-vector operations (level 2), and dense matrix-matrix operations (level 3). Often the name of the routine has as its first letter “d”, “s”, “c” to indicate the routine is double precision, single precision, or complex. LAPACK builds on BLAS to implement standard linear algebra routines such as eigendecomposition, solutions of linear systems, a variety of factorizations, etc.

### **5.2 Sparse matrices**

As an example of exploiting sparsity, here’s how the _spam_ package in R stores a sparse matrix. Consider the matrix to be row-major and store the non-zero elements in order in a vector called _value_ . Then create a vector called _rowptr_ that stores the position of the first element of each row. Finally, have a vector, _colindices_ that tells the column identity of each element. Here’s an example in the spam package in R:

**require** (spam)

mat = **matrix** ( **c** (0,0,1,0,10,0,0,0,100,0, **rep** (0,5),1000, **rep** (0,4)), nrow = 4, byrow mat = **as.spam** (mat)

28

mat@entries ## [1] 1 10 100 1000 mat@rowpointers ## [1] 1 3 4 4 5 mat@colindices ## [1] 3 5 4 1

We can do a fast matrix multiply, _Ab_ , as follows in pseudo-code:

f o r ( i in 1: nrows (A) ) { x [ i ] = 0 # should a l s o check t h a t row i s not empty . . . f o r ( j in ( rowptr [ i ] : ( rowptr [ i +1] _−_ 1)) { x [ i ] = x [ i ] + value [ j ] * b [ c o l i n d i c e s [ j ] ] }

}

How many computations have we done? Only _k_ multiplies and _O_ ( _k_ ) additions where _k_ is the number of non-zero elements of _A_ . Compare this to the usual _O_ ( _n_<sup>2</sup> ) for dense multiplication.

Note that for the Cholesky of a sparse matrix, if the sparsity pattern is fixed, but the entries change, one can precompute an optimal re-ordering that retains as much sparsity in _U_ as possible. Then multiple Cholesky decompositions can be done more quickly as the entries change.

**Banded matrices** Suppose we have a banded matrix _A_ where the lower bandwidth is _p_ , namely _Aij_ = 0 for _i > j_ + _p_ and the upper bandwidth is _q_ ( _Aij_ = 0 for _j > i_ + _q_ ). An alternative to reducing to _Ux_ = _b_<sup>_∗_</sup> is to compute _A_ = _LU_ and then do two solutions, _U_<sup>_−_1</sup> ( _L_<sup>_−_1</sup> _b_ ). One can show that the computational complexity of the LU factorization is _O_ ( _npq_ ) for banded matrices, while solving the two triangular systems is _O_ ( _np_ + _nq_ ), so for small _p_ and _q_ , the speedup can be dramatic.

Banded matrices come up in time series analysis. E.g., MA models produce banded covariance structures because the covariance is zero after a certain number of lags.

### **5.3 Low rank updates**

A transformation of the form _A − uv_<sup>_⊤_</sup> is a rank-one update because _uv_<sup>_⊤_</sup> is of rank one.

29

More generally a low rank update of _A_ is _A_<sup>˜</sup> = _A − UV_<sup>_⊤_</sup> where _U_ and _V_ are _n × m_ with _n ≥ m_ . The Sherman-Morrison-Woodbury formula tells us that


so if we know _x_ 0 = _A_<sup>_−_1</sup> _b_ , then the solution to _Ax_<sup>˜</sup> = _b_ is _x_ + _A_<sup>_−_1</sup> _U_ ( _Im − V_<sup>_⊤_</sup> _A_<sup>_−_1</sup> _U_ )<sup>_−_1</sup> _V_<sup>_⊤_</sup> _x_ . Provided _m_ is not too large, and particularly if we already have a factorization of _A_ , then _A_<sup>_−_1</sup> _U_ is not too bad computationally, and _Im − V_<sup>_⊤_</sup> _A_<sup>_−_1</sup> _U_ is _m × m_ . As a result _A_<sup>_−_1</sup> ( _U_ ( _· · ·_ )<sup>_−_1</sup> _V_<sup>_⊤_</sup> _x_ ) isn’t too bad.

This also comes up in working with precision matrices in Bayesian problems where we may have _A_<sup>_−_1</sup> but not _A_ (we often add precision matrices to find conditional normal distributions). An alternative expression for the formula is _A_<sup>˜</sup> = _A_ + _UCV_<sup>_⊤_</sup> , and the identity tells us


Basically Sherman-Morrison-Woodbury gives us matrix identities that we can use in combination with our knowledge of smart ways of solving systems of equations.

---

[← 4 Eigendecomposition and SVD](09-4-eigendecomposition-and-svd.md) · [Up: contents](index.md) · [6 Iterative solutions of linear systems →](11-6-iterative-solutions-of-linear-systems.md)
