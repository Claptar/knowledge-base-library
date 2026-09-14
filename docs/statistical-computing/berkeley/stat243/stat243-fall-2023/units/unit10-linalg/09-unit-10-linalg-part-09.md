---
title: Unit 10 — linalg Part 09 —
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit10-linalg.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unit 10 — linalg Part 09 —

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit10-linalg.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

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

#### Uses

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

#### Computation

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

#### Computation for large tall-skinny matrices

The SVD can also be generated from a QR decomposition. Take $X=QR$ and
then do an SVD on the $R$ matrix to get $X=QUDV^{\top}=U^{*}DV^{\top}$.
This is particularly helpful for the case when $X$ is tall and skinny
(suppose $X$ is $n\times p$ with $n\gg p$), because we can do the
tall-skinny QR, and the resulting SVD on $R$ is easy computationally if
$p$ is manageable.

---

[← 5. Eigendecomposition and SVD](08-5-eigendecomposition-and-svd.md) · [Up: contents](index.md) · [6. Computation →](10-6-computation.md)
