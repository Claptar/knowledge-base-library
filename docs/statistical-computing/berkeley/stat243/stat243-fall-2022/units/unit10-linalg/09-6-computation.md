---
title: 6. Computation
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit10-linalg.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit10-linalg.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Computation

**Source:** [`units/unit10-linalg.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit10-linalg.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Linear algebra in R

Speedups and storage savings can be obtained by working with matrices
stored in special formats when the matrices have special structure.
E.g., we might store a symmetric matrix as a full matrix but only use
the upper or lower triangle. Banded matrices and block diagonal matrices
are other common formats. Banded matrices are all zero except for
$A_{i,i+c_{k}}$ for some small number of integers, $c_{k}$. Viewed as an
image, these have bands. The bands are known as co-diagonals.

Note that for many matrix decompositions, you can change whether all of
the aspects of the decomposition are returned, or just some, which may
speed calculations.

Some useful packages in R for matrices are *Matrix*, *spam*, and
*bdsmatrix*. *Matrix* can represent a variety of rectangular matrices,
including triangular, orthogonal, diagonal, etc. and provides methods
for various matrix calculations that are specific to the matrix type.
*spam* handles general sparse matrices with fast matrix calculations, in
particular a fast Cholesky decomposition. *bdsmatrix* focuses on
block-diagonal matrices, which arise frequently in contexts where there
is clustering that induces within-cluster correlation and cross-cluster
independence.

In general, matrix operations in R go to compiled C or Fortran code
without much intermediate R code, so they can actually be pretty
efficient and are based on the best algorithms developed by numerical
experts. The core libraries that are used are LAPACK and BLAS (the
Linear Algebra PACKage and the Basic Linear Algebra Subroutines). As
we've discussed in the parallelization unit, one way to speed up code
that relies heavily on linear algebra is to make sure you have a BLAS
library tuned to your machine. These include OpenBLAS (free; formerly
called GotoBLAS), Intel's MKL, AMD's ACML, and Apple's vecLib. These can
be installed and R can be linked to the shared object library file
(*.so* file or *.dylib* on a Mac) for the fast BLAS. These BLAS
libraries are also available in threaded versions that farm out the
calculations across multiple cores or processors that share memory.

BLAS routines do vector operations (level 1), matrix-vector operations
(level 2), and dense matrix-matrix operations (level 3). Often the name
of the routine has as its first letter "d", "s", "c" to indicate the
routine is double precision, single precision, or complex. LAPACK builds
on BLAS to implement standard linear algebra routines such as
eigendecomposition, solutions of linear systems, a variety of
factorizations, etc.

## Sparse matrices

As an example of exploiting sparsity, here's how the *spam* package in R
stores a sparse matrix. Consider the matrix to be row-major and store
the non-zero elements in order in a vector called *value*. Then create a
vector called *rowptr* that stores the position of the first element of
each row. Finally, have a vector, *colindices* that tells the column
identity of each element. Here's an example in the spam package in R:

```r
library(spam)
mat = matrix(c(0,0,1,0,10,0,0,0,100,0,rep(0,5),1000,rep(0,4)), nrow = 4, byrow = TRUE)
mat = as.spam(mat)
mat@entries
mat@rowpointers
mat@colindices
```

We can do a fast matrix multiply, $x = Ab$, as follows in pseudo-code:

```
    for(i in 1:nrows(A)){
        x[i] = 0
        # should also check that row is not empty...
        for(j in (rowpointers[i]:(rowpointers[i+1]-1)) {
            x[i] = x[i] + entries[j] * b[colindices[j]]
        }
    }
```

How many computations have we done? Only $k$ multiplies and $O(k)$
additions where $k$ is the number of non-zero elements of $A$. Compare
this to the usual $O(n^{2})$ for dense multiplication.

Note that for the Cholesky of a sparse matrix, if the sparsity pattern
is fixed, but the entries change, one can precompute an optimal
re-ordering that retains as much sparsity in $U$ as possible. Then
multiple Cholesky decompositions can be done more quickly as the entries
change.

#### Banded matrices

Suppose we have a banded matrix $A$ where the lower bandwidth is $p$,
namely $A_{ij}=0$ for $i>j+p$ and the upper bandwidth is $q$ ($A_{ij}=0$
for $j>i+q$). An alternative to reducing to $Ux=b^{*}$ is to compute
$A=LU$ and then do two solutions, $U^{-1}(L^{-1}b)$. One can show that
the computational complexity of the LU factorization is $O(npq)$ for
banded matrices, while solving the two triangular systems is $O(np+nq)$,
so for small $p$ and $q$, the speedup can be dramatic.

Banded matrices come up in time series analysis. E.g., moving average (MA) models produce
banded covariance structures because the covariance is zero after a
certain number of lags.

## Low rank updates (optional)

A transformation of the form $A-uv^{\top}$ is a rank-one update because
$uv^{\top}$ is of rank one.

More generally a low rank update of $A$ is $\tilde{A}=A-UV^{\top}$ where
$U$ and $V$ are $n\times m$ with $n\geq m$. The
Sherman-Morrison-Woodbury formula tells us that
$$\tilde{A}^{-1}=A^{-1}+A^{-1}U(I_{m}-V^{\top}A^{-1}U)^{-1}V^{\top}A^{-1}$$
so if we know $x_{0}=A^{-1}b$, then the solution to $\tilde{A}x=b$ is
$x+A^{-1}U(I_{m}-V^{\top}A^{-1}U)^{-1}V^{\top}x$. Provided $m$ is not
too large, and particularly if we already have a factorization of $A$,
then $A^{-1}U$ is not too bad computationally, and
$I_{m}-V^{\top}A^{-1}U$ is $m\times m$. As a result
$A^{-1}(U(\cdots)^{-1}V^{\top}x)$ isn't too bad.

This also comes up in working with precision matrices in Bayesian
problems where we may have $A^{-1}$ but not $A$ (we often add precision
matrices to find conditional normal distributions). An alternative
expression for the formula is $\tilde{A}=A+UCV^{\top}$, and the identity
tells us
$$\tilde{A}^{-1}=A^{-1}-A^{-1}U(C^{-1}+V^{\top}A^{-1}U)^{-1}V^{\top}A^{-1}$$

Basically Sherman-Morrison-Woodbury gives us matrix identities that we
can use in combination with our knowledge of smart ways of solving
systems of equations.

---

[← Unit 10 — linalg Part 08 —](08-unit-10-linalg-part-08.md) · [Up: contents](index.md) · [7. Iterative solutions of linear systems (optional) →](10-7-iterative-solutions-of-linear-systems-optional.md)
