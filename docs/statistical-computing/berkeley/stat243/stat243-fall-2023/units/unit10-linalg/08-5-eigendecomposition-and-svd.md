---
title: 5. Eigendecomposition and SVD
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit10-linalg.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Eigendecomposition and SVD

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit10-linalg.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

## Eigendecomposition

The eigendecomposition (spectral decomposition) is useful in considering
convergence of algorithms and of course for statistical decompositions
such as PCA. We think of decomposing the components of variation into
orthogonal patterns (the eigenvectors) with variances (eigenvalues)
associated with each pattern.

Square symmetric matrices have real eigenvectors and eigenvalues, with
the factorization into orthogonal $\Gamma$ and diagonal $\Lambda$,
$A=\Gamma\Lambda\Gamma^{\top}$, where the eigenvalues on the diagonal of
$\Lambda$ are ordered in decreasing value. Of course this is equivalent
to the definition of an eigenvalue/eigenvector pair as a pair such that
$Ax=\lambda x$ where $x$ is the eigenvector and $\lambda$ is a scalar,
the eigenvalue. The inverse of the eigendecomposition is simply
$\Gamma\Lambda^{-1}\Gamma^{\top}$. On a similar note, we can create a
square root matrix, $\Gamma\Lambda^{1/2}$, by taking the square roots of
the eigenvalues.

The spectral radius of $A$, denoted $\rho(A)$, is the maximum of the
absolute values of the eigenvalues. As we saw when talking about
ill-conditionedness, for symmetric matrices, this maximum is the induced
norm, so we have $\rho(A)=\|A\|_{2}$. It turns out that
$\rho(A)\leq\|A\|$ for any induced matrix norm. The spectral radius
comes up in determining the rate of convergence of some iterative
algorithms.

#### Computation

There are several methods for eigenvalues; a common one for doing the
full eigendecomposition is the *QR algorithm*. The first step is to
reduce $A$ to upper Hessenburg form, which is an upper triangular matrix
except that the first subdiagonal in the lower triangular part can be
non-zero. For symmetric matrices, the result is actually tridiagonal. We
can do the reduction using Householder reflections or Givens rotations.
At this point the QR decomposition (using Givens rotations) is applied
iteratively (to a version of the matrix in which the diagonals are
shifted), and the result converges to a diagonal matrix, which provides
the eigenvalues. It's more work to get the eigenvectors, but they are
obtained as a product of Householder matrices (required for the initial
reduction) multiplied by the product of the $Q$ matrices from the
successive QR decompositions.

We won't go into the algorithm in detail, but note that it involves
manipulations and ideas we've seen already.

If only the largest (or the first few largest) eigenvalues and their
eigenvectors are needed, which can come up in time series and Markov
chain contexts, the problem is easier and can be solved by the *power
method*. E.g., in a Markov chain context, steady state is reached
through $x_{t}=A^{t}x_{0}$. One can find the largest eigenvector by
multiplying by $A$ many times, normalizing at each step.
$v^{(k)}=Az^{(k-1)}$ and $z^{(k)}=v^{(k)}/\|v^{(k)}\|$. There is an
extension to find the $p$ largest eigenvalues and their vectors. See the
demo code in the qmd source file for an implementation (in R).

```r
A = matrix(c(3, 1.3, .7, 1.3, 2, .5, .7, .5, 1), 3)

e = eigen(A)

z1 = c(1, 0, 0)
for(i in 1:20){
  z1 = A %*% z1
  z1 = z1/norm2(z1)
  print(z1)
}

val1 = (A %*% z1 / z1)
val1 = val1[1,1]

---

[← 4. Matrix factorizations (decompositions) and solving systems of linear equations](07-4-matrix-factorizations-decompositions-and-solving-systems-o.md) · [Up: contents](index.md) · [Unit 10 — linalg Part 09 — →](09-unit-10-linalg-part-09.md)
