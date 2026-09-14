---
title: 5 Computation
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit9-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit9-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Computation

**Source:** [`units/unit9-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit9-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Linear algebra in R**

Speedups and storage savings can be obtained by working with matrices stored in special formats when the matrices have special structure. E.g., we might store a symmetric matrix as a full matrix but only use the upper or lower triangle. Banded matrices and block diagonal matrices are other common formats. Banded matrices are all zero except for _Ai,i_ + _ck_ for some small number of integers, _ck_ . Viewed as an image, these have bands. The bands are known as co-diagonals.

Note that for many matrix decompositions, you can change whether all of the aspects of the decomposition are returned, or just some, which may speed calculations.

Some useful packages in R for matrices are _Matrix_ , _spam_ , and _bdsmatrix_ . _Matrix_ can represent a variety of rectangular matrices, including triangular, orthogonal, diagonal, etc. and provides methods for various matrix calculations that are specific to the matrix type. _spam_ handles general sparse matrices with fast matrix calculations, in particular a fast Cholesky decomposition. _bdsmatrix_ focuses on block-diagonal matrices, which arise frequently in contexts where there is clustering that induces within-cluster correlation and cross-cluster independence.

In general, matrix operations in R go to compiled C or Fortran code without much intermediate R code, so they can actually be pretty efficient and are based on the best algorithms developed by numerical experts. The core libraries that are used are LAPACK and BLAS (the Linear Algebra PACKage and the Basic Linear Algebra Subroutines). As we’ve discussed in the parallelization unit, one way to speed up code that relies heavily on linear algebra is to make sure you have a BLAS library tuned to your machine. These include OpenBLAS (free; formerly called GotoBLAS), Intel’s MKL, AMD’s ACML, and Apple’s vecLib. These can be installed and R can be linked to the shared object library file ( _.so_ file or _.dylib_ on a Mac) for the fast BLAS. These BLAS libraries are also available in threaded versions that farm out the calculations across multiple cores or processors that share memory.

BLAS routines do vector operations (level 1), matrix-vector operations (level 2), and dense matrix-matrix operations (level 3). Often the name of the routine has as its first letter “d”, “s”, “c” to indicate the routine is double precision, single precision, or complex. LAPACK builds on BLAS to implement standard linear algebra routines such as eigendecomposition, solutions of linear systems, a variety of factorizations, etc.

29

### **5.2 Sparse matrices**

As an example of exploiting sparsity, here’s how the _spam_ package in R stores a sparse matrix. Consider the matrix to be row-major and store the non-zero elements in order in a vector called _value_ . Then create a vector called _rowptr_ that stores the position of the first element of each row. Finally, have a vector, _colindices_ that tells the column identity of each element. Here’s an example in the spam package in R:

**require** (spam) mat = **matrix** ( **c** (0,0,1,0,10,0,0,0,100,0, **rep** (0,5),1000, **rep** (0,4)), nrow mat = **as.spam** (mat) mat@entries

= 4, byrow

---

[← 4 Eigendecomposition and SVD](08-4-eigendecomposition-and-svd.md) · [Up: contents](index.md) · [Unit 09 — linalg Part 10 — →](10-unit-09-linalg-part-10.md)
