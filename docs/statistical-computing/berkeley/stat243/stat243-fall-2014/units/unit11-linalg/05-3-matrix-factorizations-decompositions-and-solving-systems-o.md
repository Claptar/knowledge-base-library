---
title: 3 Matrix factorizations (decompositions) and solving systems of linear equations
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit11-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit11-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Matrix factorizations (decompositions) and solving systems of linear equations

**Source:** [`units/unit11-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit11-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose we want to solve the following linear system:


Numerically, this is never done by finding the inverse and multiplying. Rather we solve the system using a matrix decomposition (or equivalent set of steps). One approach uses Gaussian elimination (equivalent to the LU decomposition), while another uses the Cholesky decomposition. There are also iterative methods that generate a sequence of approximations to the solution but reduce computation (provided they are stopped before the exact solution is found).

Gentle-CS has a nice table overviewing the various factorizations (Table 5.1, page 219).

### **3.1 Triangular systems**

As a preface, let’s figure out how to solve _Ax_ = _b_ if _A_ is upper triangular. The basic algorithm proceeds from the bottom up (and therefore is called a ’backsolve’. We solve for _xn_ trivially, and then move upwards plugging in the known values of _x_ and solving for the remaining unknown in each row (each equation).

1. _xn_ = _bn/Ann_


14

#### 3. Repeat for all rows.

How many multiplies and adds are done? Solving lower triangular systems is very similar and involves the same number of calculations.

In R, _backsolve()_ solves upper triangular systems and _forwardsolve()_ solves lower triangular systems:

n <- 20 X <- **crossprod** ( **matrix** ( **rnorm** (n^2), n)) b <- **rnorm** (n) U <- **chol** ( **crossprod** (X)) _# U is upper-triangular_ L <- **t** (U) _# L is lower-triangular_ out1 <- **backsolve** (U, b) out2 <- **forwardsolve** (L, b) **all.equal** (out1, **c** ( **solve** (U) %*% b)) ## [1] TRUE **all.equal** (out2, **c** ( **solve** (L) %*% b)) ## [1] TRUE

We can also solve ( _U_<sup>_⊤_</sup> )<sup>_−_1</sup> _b_ and ( _L_<sup>_⊤_</sup> )<sup>_−_1</sup> _b_ as

**backsolve** (U, b, transpose = TRUE) **forwardsolve** (L, b, transpose = TRUE)

**To reiterate the distinction between matrix inversion and solving a system of equations, when we write** _U_<sup>_−_1</sup> _b_ **, what we mean on a computer is to carry out the above algorithm, not to find the inverse and then multiply.**

### **3.2 Gaussian elimination (LU decomposition)**

Gaussian elimination is a standard way of directly computing a solution for _Ax_ = _b_ . It is equivalent to the LU decomposition. LU is primarily done with square matrices, but not always. Also LU decompositions do exist for some singular matrices.

The idea of Gaussian elimination is to convert the problem to a triangular system. In class, we’ll walk through Gaussian elimination in detail and see how it relates to the LU decomposition. I’ll describe it more briefly here. Following what we learned in algebra when we have multiple

15

equations, we preserve the solution, _x_ , when we add multiples of rows (i.e., add multiples of equations) together. This amounts to doing _L_ 1 _Ax_ = _L_ 1 _b_ for a lower-triangular matrix _L_ 1 that produces all zeroes in the first column of _L_ 1 _A_ except for the first row. We proceed to zero out values below the diagonal for the other columns of _A_ . The result is _Ln−_ 1 _· · · L_ 1 _A ≡ U_ = _Ln−_ 1 _· · · L_ 1 _b ≡ b_<sup>_∗_</sup> where _U_ is upper triangular. This is the forward reduction step of Gaussian elimination. Then the backward elimination step solves _Ux_ = _b_<sup>_∗_</sup> .

If we’re just looking for the solution of the system, we don’t need the lower-triangular factor _L_ = ( _Ln−_ 1 _· · · L_ 1)<sup>_−_1</sup> in _A_ = _LU_ , but it turns out to have a simple form that is computed as we go along, it is unit lower triangular and the values below the diagonal are the negative of the values below the diagonals in _L_ 1 _, . . . , Ln−_ 1 (note that each _Lj_ has non-zeroes below the diagonal only in the _j_ th column). As a side note related to storage, it turns out that as we proceed, we can store the elements of _L_ and _U_ in the original _A_ matrix, except for the implicit 1s on the diagonal of _L_ .

In class, we’ll work out the computational complexity of the LU and see that it is _O_ ( _n_<sup>3</sup> ).

If we look at _solve.default()_ in R, we see that it uses _dgesv_ . A Google search indicates that this is a Lapack routine that does the LU decomposition with partial pivoting and row interchanges (see below on what these are), so R is using the algorithm we’ve just discussed.

One additional complexity is that we want to avoid dividing by very small values to avoid introducing numerical inaccuracy (we would get large values that might overwhelm whatever they are being added to, and small errors in the divisor willl have large effects on the result). This can be done on the fly by interchanging equations to use the equation (row) that produces the largest value to divide by. For example in the first step, we would switch the first equation (first row) for whichever of the remaining equations has the largest value in the first column. This is called partial pivoting. The divisors are called pivots. Complete pivoting also considers interchanging columns, and while theoretically better, partial pivoting is generally sufficient and requires fewer computations. Note that partial pivoting can be expressed as multiplying along the way by permutation matrices, _P_ 1 _, . . . Pn−_ 1 that switch rows. Based on pivoting, we have _PA_ = _LU_ , where _P_ = _Pn−_ 1 _· · · P_ 1. In the demo code, we’ll see a toy example of the impact of pivoting.

Finally _|PA|_ = _|P ||A|_ = _|L||U |_ = _|U |_ (why?) so _|A|_ = _|U |/|P |_ and since the determinant of each permutation matrix, _Pj_ is -1 (except when _Pj_ = _I_ because we don’t need to switch rows), we just need to multiply by minus one if there is an odd number of permutations. Or if we know the matrix is non-negative definite, we just take the absolute value of _|U |_ . So Gaussian elimination provides a fast stable way to find the determinant.

16

### **3.3 Cholesky decomposition**

When _A_ is p.d., we can use the Cholesky decomposition to solve a system of equations. Positive definite matrices can be decomposed as _U_<sup>_⊤_</sup> _U_ = _A_ where _U_ is upper triangular. _U_ is called a square root matrix and is unique (apart from the sign, which we fix by requiring the diagonals to be positive). One algorithm for computing _U_ is:


3. For _i_ = 2 _, . . . , n_ ,


We can then solve a system of equations as: _U_<sup>_−_1</sup> ( _U_<sup>_⊤−_1</sup> _b_ ), which in R can be done in either of the following ways:

**backsolve** (U, **backsolve** (U, b, transpose = TRUE)) **backsolve** (U, **forwardsolve** ( **t** (U), b)) _# equivalent but less efficient_

The Cholesky has some nice advantages over the LU: (1) while both are _O_ ( _n_<sup>3</sup> ), the Cholesky involves only half as many computations, _n_<sup>3</sup> _/_ 6 + _O_ ( _n_<sup>2</sup> ) and (2) the Cholesky factorization has only ( _n_<sup>2</sup> + _n_ ) _/_ 2 unique values compared to _n_<sup>2</sup> + _n_ for the LU. Of course the LU is more broadly applicable. The Cholesky does require computation of square roots, but it turns out this is not too intensive. There is also a method for finding the Cholesky without square roots.

**Uses of the Cholesky** The standard algorithm for generating _y ∼N_ (0 _, A_ ) is:

U <- **chol** (A)

y <- **crossprod** (U, **rnorm** (n)) _# i.e., t(U)%*%rnorm(n), but much faster_

**Question** : where will most of the time in this two-step calculation be spent?

If a regression design matrix, _X_ , is full rank, then _X_<sup>_⊤_</sup> _X_ is positive definite, so we could find _β_ ˆ = ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ using either the Cholesky or Gaussian elimination. **Challenge** : write efficient R code to carry out the OLS solution using either LU or Cholesky factorization.

However, it turns out that the standard approach is to work with _X_ using the QR decomposition rather than working with _X_<sup>_⊤_</sup> _X_ ; working with _X_ is more numerically stable, though in most situations without extreme collinearity, either of the approaches will be fine.

17

**Numerical issues with eigendecompositions and Cholesky decompositions for positive definite matrices** Monahan comments that in general Gaussian elimination and the Cholesky decomposition are very stable. However, in the Cholesky case, if the matrix is very ill-conditioned we can get _Aii −_<sup>�</sup> _k_<sup>_U_</sup> _ki_<sup>2being negative and then the algorithm stops when we try to take the square root. In</sup> this case, the Cholesky decomposition does not exist numerically although it exists mathematically. It’s not all that hard to produce such a matrix, particularly when working with high-dimensional covariance matrices with large correlations.

_# require(fields)_ locs <- **runif** (100) rho <- .1 C <- **exp** (- **rdist** (locs)^2/rho^2) e <- **eigen** (C) e$values[96:100]

---

[← 2 Computational issues](04-2-computational-issues.md) · [Up: contents](index.md) · [[1] -1.905153e-16 -2.071019e-16 -2.445624e-16 -2.502047e-16 -5.247692e-16 U <- chol (C) →](06-1--1-905153e-16--2-071019e-16--2-445624e-16--2-502047e-16--5.md)
