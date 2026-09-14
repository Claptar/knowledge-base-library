---
title: 4 Matrix factorizations (decompositions) and solving systems of linear equations
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit10-linalg.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Matrix factorizations (decompositions) and solving systems of linear equations

**Source:** [`units/unit10-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose we want to solve the following linear system:

_Ax_ = _b_

15

_x_ = _A_<sup>_−_1</sup> _b_

Numerically, this is never done by finding the inverse and multiplying. Rather we solve the system using a matrix decomposition (or equivalent set of steps). One approach uses Gaussian elimination (equivalent to the LU decomposition), while another uses the Cholesky decomposition. There are also iterative methods that generate a sequence of approximations to the solution but reduce computation (provided they are stopped before the exact solution is found).

Gentle-CS has a nice table overviewing the various factorizations (Table 5.1, page 219). I’ve reproduced a variation on it here (sorry about the weird lines – L<sup>A</sup> TEX is being a pain for some reason).

_Table 1. Useful matrix factorizations for statistics._

|Name|Representation|Restrictions|Properties|Uses|
|---|---|---|---|---|
|LU|_Ann_ =_LnnUnn_|_A_generally<br>square|_L_lower triangular;_U_<br>upper triangular|solving equations;<br>inversion|
|QR|_Anm_ =_QnnRnm_or<br>_Anm_ =<br>_QnmRmm_(skinny)||_Q_orthogonal;_R_upper<br>triangular|regression|
|Cholesky|_Ann_ =_U _<sup>_⊤_</sup><br>_nn_<sup>_Unn_</sup>|_A_positive<br>(semi-) definite|_U_ upper triangular|multivariate normal;<br>covariance; solving<br>equations; inversion|
|Eigen de-<br>composition|_Ann_ = Γ_nn_Λ_nn_Γ<sup>_⊤_</sup><br>_nn_|_A_square,<br>symmetric*|Γorthogonal;Λ<br>(non-negative**) diagonal|principal components<br>analysis and related|
|SVD|_Anm_ =_UnnDnmV _<sup>_⊤_</sup><br>_mm_<sup>or</sup><br>_Anm_ =_UnkDkkV _<sup>_⊤_</sup><br>_mk_||_U, V_ orthogonal;_D_<br>(non-negative) diagonal|machine learning, topic<br>models|


*For the eigen decomposition, I assume _A_ is symmetric, though there is a decomposition for non-symmetric _A_ . ** For positive definite or positive semi-definite _A_ .

### **4.1 Triangular systems**

As a preface, let’s figure out how to solve _Ax_ = _b_ if _A_ is upper triangular. The basic algorithm proceeds from the bottom up (and therefore is called a ’backsolve’. We solve for _xn_ trivially, and then move upwards plugging in the known values of _x_ and solving for the remaining unknown in each row (each equation).


3. Repeat for all rows.

16

How many multiplies and adds are done? Solving lower triangular systems is very similar and involves the same number of calculations.

In R, _backsolve()_ solves upper triangular systems and _forwardsolve()_ solves lower triangular systems:

n <- 20 X <- **crossprod** ( **matrix** ( **rnorm** (n^2), n)) b <- **rnorm** (n) U <- **chol** ( **crossprod** (X)) _# U is upper-triangular_ L <- **t** (U) _# L is lower-triangular_ out1 <- **backsolve** (U, b) out2 <- **forwardsolve** (L, b) **all.equal** (out1, **c** ( **solve** (U) %*% b)) ## [1] TRUE **all.equal** (out2, **c** ( **solve** (L) %*% b)) ## [1] TRUE

We can also solve ( _U_<sup>_⊤_</sup> )<sup>_−_1</sup> _b_ and ( _L_<sup>_⊤_</sup> )<sup>_−_1</sup> _b_ as

**backsolve** (U, b, transpose = TRUE) **forwardsolve** (L, b, transpose = TRUE)

**To reiterate the distinction between matrix inversion and solving a system of equations, when we write** _U_<sup>_−_1</sup> _b_ **, what we mean on a computer is to carry out the above algorithm, not to find the inverse and then multiply.**

Here’s a good reason why.

n <- 5000 X <- **crossprod** ( **matrix** ( **rnorm** (n^2), n)) b <- **rnorm** (n) U <- **chol** ( **crossprod** (X)) _# U is upper-triangular_ **system.time** ( out1 <- **backsolve** (U, b) )

17

---

[← Unit 10 — linalg Part 07 —](07-unit-10-linalg-part-07.md) · [Up: contents](index.md) · [Unit 10 — linalg Part 09 — →](09-unit-10-linalg-part-09.md)
