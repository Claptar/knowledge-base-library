---
title: 5. Eigendecomposition and SVD
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit10-linalg.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd) — berkeley-stat243 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 5. Eigendecomposition and SVD

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

### Computation

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
#| include: false
#| eval: false
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

# following Gentle-NLA, p. 125, we can get the next largest eigenvalue, which is the largest eigenvalue of the matrix B
B = A - val1 * outer(c(z1), c(z1))

z2 = c(1, 0, 0)
for(i in 1:200){
  z2 = B %*% z2
  z2 = z2/norm2(z2)
  print(z2)
}

val2 = B%*%z2/z2 + val1
```

## Singular value decomposition

Let's consider an $n\times m$ matrix, $A$, with $n\geq m$ (if $m>n$, we
can always work with $A^{\top})$. This often is a matrix representing
$m$ features of $n$ observations. We could have $n$ documents and $m$
words, or $n$ gene expression levels and $m$ experimental conditions,
etc. $A$ can always be decomposed as $$A=UDV^{\top}$$ where $U$ and $V$
are matrices with orthonormal columns (left and right eigenvectors) and
$D$ is diagonal with non-negative values (which correspond to
eigenvalues in the case of square $A$ and to squared eigenvalues of
$A^{\top}A$).

The SVD can be represented in more than one way. One representation is
$$A_{n\times m}=U_{n\times k}D_{k\times k}V_{k\times m}^{\top}=\sum_{j=1}^{k}D_{jj}u_{j}v_{j}^{\top}$$
where $u_{j}$ and $v_{j}$ are the columns of $U$ and $V$ and where $k$
is the rank of $A$ (which is at most the minimum of $n$ and $m$ of
course). The diagonal elements of $D$ are the singular values.

That representation is as the sum of rank-one matrices (since
each term is the scaled outer product of two vectors).

If $A$ is positive semi-definite, the eigendecomposition is an SVD.
Furthermore, $A^{\top}A=VD^{2}V^{\top}$ and $AA^{\top}=UD^{2}U^{\top}$,
so we can find the eigendecomposition of such matrices using the SVD of
$A$ (for $AA^{\top}$ we need to fill out $U$ to have $n$ columns). Note
that the squares of the singular values of $A$ are the eigenvalues of
$A^{\top}A$ and $AA^{\top}$.

We can also fill out the matrices to get
$$A=U_{n\times n}D_{n\times m}V_{m\times m}^{\top}$$ where the added
rows and columns of $D$ are zero with the upper left block the
$D_{k\times k}$ from above.

### Uses

The SVD is an excellent way to determine a matrix rank and to construct
a pseudo-inverse ($A^{+}=VD^{+}U^{\top})$.

We can use the SVD to approximate $A$ by taking
$A\approx\tilde{A}=\sum_{j=1}^{p}D_{jj}u_{j}v_{j}^{\top}$ for $p<m$.
The Eckart-Minsky-Young theorem shows that the truncated SVD
minimizes the Frobenius norm of $A-\tilde{A}$ over all possible rank-$p$ approximations.
As an example if we have a large image of dimension
$n\times m$, we could hold a compressed version by a rank-$p$
approximation using the SVD. The SVD is used a lot in clustering
problems. For example, the Netflix prize was won based on a variant of
SVD (in fact all of the top methods used variants on SVD, I believe).

Here's another way to think about the SVD in terms of transformations and bases.
Applying the SVD to a vector, $ UDV^{\top}x$, carries out the following steps:

 - $V^{\top}x$ expresses $x$ in terms of weights for the columns of $V$.
 - Multiplying the result by $D$ scales/stretches the weights.
 - Multiplying by $U$ produces the result, which is a weighted combination of columns of $U$, spanning the column-space of $U$.

So applying the SVD transforms $x$ from the column space of $V$ to the column space of $U$.

### Computation

The basic algorithm (Golub-Reinsch) is similar to the QR method for the
eigendecomposition. We use a series of Householder transformations on
the left and right to reduce $A$ to an upper bidiagonal matrix,
$A^{(0)}$. The post-multiplications (the transformations on the right)
generate the zeros in the upper triangle. (An upper bidiagonal matrix is
one with non-zeroes only on the diagonal and first subdiagonal above the
diagonal). Then the algorithm produces a series of upper bidiagonal
matrices, $A^{(0)}$, $A^{(1)},$ etc. that converge to a diagonal matrix,
$D$ . Each step is carried out by a sequence of Givens transformations:

$$
\begin{aligned}
A^{(j+1)} & = & R_{m-2}^{\top} R_{m-3}^{\top} \cdots R_{0}^{\top} A^{(j)} T_{0} T_{1} \cdots T_{m-2} \\
 & = & RA^{(j)} T
\end{aligned}.
$$

This eventually gives $A^{(...)}=D$ and
by construction, $U$ (the product of the pre-multiplied Householder
matrices and the $R$ matrices) and $V$ (the product of the
post-multiplied Householder matrices and the $T$ matrices) are
orthogonal. The result is then transformed by a diagonal matrix to make
the elements of $D$ non-negative and by permutation matrices to order
the elements of $D$ in nonincreasing order.

### Computation for large tall-skinny matrices

The SVD can also be generated from a QR decomposition. Take $X=QR$ and
then do an SVD on the $R$ matrix to get $X=QUDV^{\top}=U^{*}DV^{\top}$.
This is particularly helpful for the case when $X$ is tall and skinny
(suppose $X$ is $n\times p$ with $n\gg p$), because we can do the
tall-skinny QR, and the resulting SVD on $R$ is easy computationally if
$p$ is manageable.

---

[← 4. Matrix factorizations (decompositions) and solving systems of linear equations](04-4-matrix-factorizations-decompositions-and-solving-systems-o.md) · [Up: contents](index.md) · [6. Computation →](06-6-computation.md)
