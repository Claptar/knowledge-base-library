---
title: Matrix multiplication
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit10-linalg.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Matrix multiplication

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

np.matmul(A, B)
A @ B        # alternative
A.dot(B)     # not recommended by the NumPy docs

A * B # Hadamard (direct) product
```

You don't need the spaces, but they're nice for code readability.

## Trace and determinant of square matrices

The trace of a matrix is the sum of the diagonal elements. For square
matrices, $\mbox{tr}(A+B)=\mbox{tr}(A)+\mbox{tr}(B)$,
$\mbox{tr}(A)=\mbox{tr}(A^{\top})$.

We also have $\mbox{tr}(ABC)=\mbox{tr}(CAB)=\mbox{tr}(BCA)$ - basically
you can move a matrix from the beginning to the end or end to beginning,
provided they are conformable for this operation. This is helpful for a
couple reasons:

1.  We can find the ordering that reduces computation the most if the
    individual matrices are not square.
2.  $x^{\top}Ax=\mbox{tr}(x^{\top}Ax)$ since the quadratic form,
    $x^{\top}Ax$, is a scalar, and this is equal to
    $\mbox{tr}(xx^{\top}A)$ where $xx^{\top}A$ is a matrix. It can be
    helpful to be able to go back and forth between a scalar and a trace
    in some statistical calculations.

For square matrices, the determinant exists and we have $|AB|=|A||B|$
and therefore, $|A^{-1}|=1/|A|$ since $|I|=|AA^{-1}|=1$. Also
$|A|=|A^{\top}|$, which can be seen using the QR decomposition for $A$
and understanding properties of determinants of triangular matrices (in
this case $R$) and orthogonal matrices (in this case $Q$).

## Transposes and inverses

For square, invertible matrices, we have that
$(A^{-1})^{\top}=(A^{\top})^{-1}$. Why? Since we have
$(AB)^{\top}=B^{\top}A^{\top}$, we have:
$$A^{\top}(A^{-1})^{\top}=(A^{-1}A)^{\top}=I$$ so
$(A^{\top})^{-1}=(A^{-1})^{\top}$.

For two invertible matrices, we have that
$(AB)^{-1} = B^{-1}A^{-1}$ since
$B^{-1}A^{-1} AB = I$.

#### Other matrix multiplications

The Hadamard or direct product is simply multiplication of the
correspoding elements of two matrices by each other. In R this is
simply` A * B`.\
**Challenge**: How can I find $\mbox{tr}(AB)$ without using `A %*% B` ?

The Kronecker product is the product of each element of one matrix with
the entire other matrix"

$$A\otimes B=\left(\begin{array}{ccc}
A_{11}B & \cdots & A_{1m}B\\
\vdots & \ddots & \vdots\\
A_{n1}B & \cdots & A_{nm}B
\end{array}\right)$$

The inverse of a Kronecker product is the Kronecker product of the
inverses,

$$ B^{-1} \otimes A^{-1} $$

which is obviously quite a bit faster because
the inverse (i.e., solving a system of equations) in this special case
is $O(n^{3}+m^{3})$ rather than the naive approach being $O((nm)^{3})$.

## Matrix decompositions

A matrix decomposition is a re-expression of a matrix, $A$, in terms of
a product of two or three other, simpler matrices, where the
decomposition reveals structure or relationships present in the original
matrix, $A$. The "simpler" matrices may be simpler in various ways,
including

-   having fewer rows or columns;
-   being diagonal, triangular or sparse in some way,
-   being orthogonal matrices.

In addition, once you have a decomposition, computation is generally
easier, because of the special structure of the simpler matrices.

We'll see this in great detail in Section 3.

---

[← 1. Preliminaries](02-1-preliminaries.md) · [Up: contents](index.md) · [2. Statistical interpretations of matrix invertibility, rank, etc. →](04-2-statistical-interpretations-of-matrix-invertibility-rank-e.md)
