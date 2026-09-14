---
title: 6. Computation
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit10-linalg.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Computation

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit10-linalg.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Linear algebra in Python

Note that for many matrix decompositions, you can change whether all of
the aspects of the decomposition are returned, or just some, which may
speed calculations.

Given the importance of linear algebra to many (most) statistical and
machine learning algorithms, to improve efficiency of the algorithms,
for large problems, it's important to see whether the linear algebra is being
done using a fast linear algebra package in parallel, potentially on
the GPU. How the linear algebra is done on the back end can make a huge
difference in speed.

### BLAS and LAPACK

In general, matrix operations in Python and R go to compiled C or Fortran code
without much intermediate Python or R  code, so they can actually be pretty
efficient and are based on the best algorithms developed by numerical
experts. The core libraries that are used are LAPACK and BLAS (the
Linear Algebra PACKage and the Basic Linear Algebra Subroutines). As
we've discussed in the parallelization unit, one way to speed up code
that relies heavily on linear algebra is to make sure you have a BLAS
library tuned to your machine. These include OpenBLAS (open source), Intel's MKL, AMD's ACML, and Apple's vecLib.
On newer Macs (Apple Silicon-based, namely using the M1, M2, M3, M4 chips), vecLib uses the Mac's AMX co-processor.


If you use Conda, numpy will generally be linked against MKL or OpenBLAS (this will
depend on the locations online of the packages being installed, i.e., the *channel(s)* used). With pip,
numpy will generally be linked against OpenBLAS.
it's possible to install numpy so that it uses OpenBLAS.
R can be linked to the shared object library file
(*.so* file or *.dylib* on a Mac) for a fast BLAS. These BLAS
libraries are also available in threaded versions that farm out the
calculations across multiple cores or processors that share memory.
More details are available in [this SCF documentation](https://statistics.berkeley.edu/computing/faqs/linear-algebra-and-parallelized-linear-algebra-using-blas).

BLAS routines do vector operations (level 1), matrix-vector operations
(level 2), and dense matrix-matrix operations (level 3). Often the name
of the routine has as its first letter "d", "s", "c" to indicate the
routine is double precision, single precision, or complex. LAPACK builds
on BLAS to implement standard linear algebra routines such as
eigendecomposition, solutions of linear systems, a variety of
factorizations, etc.

### JAX and PyTorch (and GPUs)

Python packages such as JAX and PyTorch provide alternative linear algebra implementations that can exploit parallelization on CPUs and GPUs, automatically using the GPU if it is available. As discussed in Unit 5, JAX can also do just-in-time compilation.

The SCF parallelization tutorial has [this example](https://computing.stat.berkeley.edu/tutorial-parallelization/parallel-python#61-linear-algebra) of doing matrix multiplication using PyTorch either on the CPU or a GPU.

The same tutorial also has an example of doing matrix multiplication using JAX, either [on the CPU](https://computing.stat.berkeley.edu/tutorial-parallelization/parallel-python#72-linear-algebra) or [on the GPU](https://computing.stat.berkeley.edu/tutorial-parallelization/parallel-python#73-using-the-gpu-with-jax). Use of the CPU doesn't give much speed up compared to numpy since as noted above numpy linked to a parallel BLAS will use multiple threads.

## Exploiting known structure in matrices

Speedups and storage savings can be obtained by working with matrices
stored in special formats when the matrices have special structure.
E.g., we might store a symmetric matrix as a full matrix but only use
the upper or lower triangle. Banded matrices and block diagonal matrices
are other common formats. Banded matrices are all zero except for
$A_{i,i+c_{k}}$ for some small number of integers, $c_{k}$. Viewed as an
image, these have bands. The bands are known as co-diagonals.

Scipy provides functionality for working with matrices in various ways,
including the [`scipy.sparse` module](https://docs.scipy.org/doc/scipy/reference/sparse.html),
which provides support for
structured sparse matrices such as triangular and diagonal matrices
as well as unstructured sparse matrices using various standard representations.

Some useful packages in R for matrices are *Matrix*, *spam*, and
*bdsmatrix*. *Matrix* can represent a variety of rectangular matrices,
including triangular, orthogonal, diagonal, etc. and provides methods
for various matrix calculations that are specific to the matrix type.
*spam* handles general sparse matrices with fast matrix calculations, in
particular a fast Cholesky decomposition. *bdsmatrix* focuses on
block-diagonal matrices, which arise frequently in contexts where there
is clustering that induces within-cluster correlation and cross-cluster
independence.

### Sparse matrix formats

As an example of exploiting sparsity, we can use a standard format (CSR = compressed sparse row)
in the Scipy `sparse` module:

Consider the matrix to be row-major and store
the non-zero elements in order in an array called `data`. Then create a
array called *indptr* that stores the position of the first element of
each row. Finally, have a array, *indices* that tells the column
identity of each element.

```python
import scipy.sparse as sparse
mat = np.array([[0,0,1,0,10],[0,0,0,100,0],[0,0,0,0,0],[1000,0,0,0,0]])
mat = sparse.csr_array(mat)
mat.data
mat.indices  # column indices
mat.indptr   # row pointers

## Ideally don't first construct the dense matrix if it is large.
mat2 = sparse.csr_array((mat.data, mat.indices, mat.indptr))
mat2.toarray()
```

That's also how things are done in the `spam` package in R.

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

### Banded matrices

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

[← Unit 10 — linalg Part 09 —](09-unit-10-linalg-part-09.md) · [Up: contents](index.md) · [7. Iterative solutions of linear systems (optional) →](11-7-iterative-solutions-of-linear-systems-optional.md)
