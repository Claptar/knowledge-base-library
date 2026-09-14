---
title: 2. Statistical interpretations of matrix invertibility, rank, etc.
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit10-linalg.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Statistical interpretations of matrix invertibility, rank, etc.

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Linear independence, rank, and basis vectors

A set of vectors, $v_{1},\ldots v_{n}$, is linearly independent (LIN)
when none of the vectors can be represented as a linear combination,
$\sum c_{i}v_{i}$, of the others for scalars, $c_{1},\ldots,c_{n}$. If
we have vectors of length $n$, we can have at most $n$ linearly
independent vectors. The rank of a matrix is the number of linearly
independent rows (or columns - it's the same), and is at most the
minimum of the number of rows and number of columns. We'll generally
think about it in terms of the dimension of the column space - so we can
just think about the number of linearly independent columns.

Any set of linearly independent vectors (say $v_{1},\ldots,v_{n}$) span
a space made up of all linear combinations of those vectors
($\sum_{i=1}^{n}c_{i}v_{i}$). The spanning vectors are known as basis
vectors. We can express a vector $y$ that is in the space with respect
to (as a linear combination of) basis vectors as $y=\sum_{i}c_{i}v_{i}$,
where if the basis vectors are normalized and orthogonal, we can find
the weights as $c_{i}=\langle y,v_{i}\rangle$.

Consider a regression context. We have $p$ covariates ($p$ columns in
the design matrix, $X$), of which $q\leq p$ are linearly independent
covariates. This means that $p-q$ of the vectors can be written as
linear combos of the $q$ vectors. The space spanned by the covariate
vectors is of dimension $q$, rather than $p$, and $X^{\top}X$ has $p-q$
eigenvalues that are zero. The $q$ LIN vectors are basis vectors for the
space - we can represent any point in the space as a linear combination
of the basis vectors. You can think of the basis vectors as being like
the axes of the space, except that the basis vectors are not orthogonal.
So it's like denoting a point in $\Re^{q}$ as a set of $q$ numbers
telling us where on each of the axes we are - this is the same as a
linear combination of axis-oriented vectors.

When fitting a regression, if $n=p=q$, a vector of $n$ observations can
be represented exactly as a linear combination of the $p$ basis vectors,
so there is no residual and we have a single unique (and exact) solution
(e.g., with $n=p=2$, the observations fall exactly on the simple linear
regression line). If $n<p$, then we have at most $n$ linearly
independent covariates (the rank is at most $n$). In this case we have
multiple possible solutions and the system is ill-determined
(under-determined). Similarly, if $q<p$ and $n\geq p$, the rank is again
less than $p$ and we have multiple possible solutions. Of course we
usually have $n>p$, so the system is overdetermined - there is no exact
solution, but regression is all about finding solutions that minimize
some criterion about the differences between the observations and linear
combinations of the columns of the $X$ matrix (such as least squares or
penalized least squares). In standard regression, we project the
observation vector onto the space spanned by the columns of the $X$
matrix, so we find the point in the space closest to the observation
vector.

## Invertibility, singularity, rank, and positive definiteness

For square matrices, let's consider how invertibility, singularity, rank
and positive (or non-negative) definiteness relate.

Square matrices that are "regular" have an eigendecomposition,
$A=\Gamma\Lambda\Gamma^{-1}$ where $\Gamma$ is a matrix with the
eigenvectors as the columns and $\Lambda$ is a diagonal matrix of
eigenvalues, $\Lambda_{ii}=\lambda_{i}$. Symmetric matrices and matrices
with unique eigenvalues are regular, as are some other matrices. The
number of non-zero eigenvalues is the same as the rank of the matrix.
Square matrices that have an inverse are also called nonsingular, and
this is equivalent to having full rank. If the matrix is symmetric, the
eigenvectors and eigenvalues are real and $\Gamma$ is orthogonal, so we
have $A=\Gamma\Lambda\Gamma^{\top}$. The determinant of the matrix is
the product of the eigenvalues (why?), which is zero if it is less than
full rank. Note that if none of the eigenvalues are zero then
$A^{-1}=\Gamma\Lambda^{-1}\Gamma^{\top}$.

Let's focus on symmetric matrices. The symmetric matrices that tend to
arise in statistics are either positive definite (p.d.) or non-negative
definite (n.n.d.). If a matrix is positive definite, then by definition
$x^{\top}Ax>0$ for any $x$. Note that if $\mbox{Cov}(y)=A$ then
$x^{\top}Ax=x^{\top}\mbox{Cov}(y)x=\mbox{Cov}(x^{\top}y)=\mbox{Var}(x^{\top}y)$
if so positive definiteness amounts to having linear combinations of
random variables (with the elements of $x$ here being the weights)
having positive variance. So we must have that positive definite
matrices are equivalent to variance-covariance matrices (I'll just refer
to this as a variance matrix or as a covariance matrix). If $A$ is p.d.
then it has all positive eigenvalues and it must have an inverse, though
as we'll see, from a numerical perspective, we may not be able to
compute it if some of the eigenvalues are very close to zero. In Python,
`numpy.linalg.eig(A)[1]` is $\Gamma$, with each column a vector, and
`numpy.linalg.eig(A)[0]` contains the (unordered) eigenvalues.

To summarize, here are some of the various connections between
mathematical and statistical properties of **positive definite**
matrices:

$A$ positive definite $\Leftrightarrow$ $A$ is a covariance matrix
$\Leftrightarrow$ $x^{\top}Ax>0$ $\Leftrightarrow$ $\lambda_{i}>0$
(positive eigenvalues) $\Rightarrow$$|A|>0$ $\Rightarrow$$A$ is
invertible $\Leftrightarrow$ $A$ is non singular $\Leftrightarrow$ $A$ is
full rank.

And here are connections for positive semi-definite matrices:

$A$ positive semi-definite $\Leftrightarrow$ $A$ is a constrained
covariance matrix $\Leftrightarrow$ $x^{\top}Ax\geq0$ and equal to 0 for
some $x$ $\Leftrightarrow$ $\lambda_{i}\geq 0$ (non-negative eigenvalues),
with at least one zero $\Rightarrow$ $|A|=0$ $\Leftrightarrow$ $A$ is not
invertible $\Leftrightarrow$ $A$ is singular $\Leftrightarrow$ $A$ is not
full rank.

## Interpreting an eigendecomposition

Let's interpret the eigendecomposition in a generative context as a way
of generating random vectors. We can generate $y$ s.t. $\mbox{Cov}(y)=A$
if we generate $y=\Gamma\Lambda^{1/2}z$ where $\mbox{Cov}(z)=I$ and
$\Lambda^{1/2}$ is formed by taking the square roots of the eigenvalues.
So $\sqrt{\lambda_{i}}$ is the standard deviation associated with the
basis vector $\Gamma_{\cdot i}$. That is, the $z$'s provide the weights
on the basis vectors, with scaling based on the eigenvalues. So $y$ is
produced as a linear combination of eigenvectors as basis vectors, with
the variance attributable to the basis vectors determined by the
eigenvalues.

To go the other direction, we can project a vector $y$ onto the space
spanned by the eigenvectors: $w = (\Gamma^{\top}\Gamma)^{-1}\Gamma^{\top}y = \Gamma^{\top}y = \Lambda^{1/2}z$,
where the simplification of course comes from $\Gamma$ being orthogonal.

If $x^{\top}Ax\geq0$ then $A$ is nonnegative definite (also called
positive semi-definite). In this case one or more eigenvalues can be
zero. Let's interpret this a bit more in the context of generating
random vectors based on non-negative definite matrices,
$y=\Gamma\Lambda^{1/2}z$ where $\mbox{Cov}(z)=I$. Questions:

1.  What does it mean when one or more eigenvalue (i.e.,
    $\lambda_{i}=\Lambda_{ii}$) is zero?

2.  Suppose I have an eigenvalue that is very small and I set it to
    zero? What will be the impact upon $y$ and $\mbox{Cov}(y)$?

3.  Now let's consider the inverse of a covariance matrix, known as the
    precision matrix, $A^{-1}=\Gamma\Lambda^{-1}\Gamma^{\top}$. What
    does it mean if a $(\Lambda^{-1})_{ii}$ is very large? What if
    $(\Lambda^{-1})_{ii}$ is very small?

Consider an arbitrary $n\times p$ matrix, $X$. Any crossproduct or sum
of squares matrix, such as $X^{\top}X$ is positive definite
(non-negative definite if $p>n$). This makes sense as it's just a
scaling of an empirical covariance matrix.

## Generalized inverses (optional)

Suppose I want to find $x$ such that $Ax=b$. Mathematically the answer
(provided $A$ is invertible, i.e. of full rank) is $x=A^{-1}b$.

Generalized inverses arise in solving equations when $A$ is not full
rank. A generalized inverse is a matrix, $A^{-}$ s.t. $AA^{-}A=A$. The
Moore-Penrose inverse (the pseudo-inverse), $A^{+}$, is a (unique)
generalized inverse that also satisfies some additional properties.
$x=A^{+}b$ is the solution to the linear system, $Ax=b$, that has the
shortest length for $x$.

We can find the pseudo-inverse based on an eigendecomposition (or an
SVD) as $\Gamma\Lambda^{+}\Gamma^{\top}$. We obtain $\Lambda^{+}$ from
$\Lambda$ as follows. For values $\lambda_{i}>0$, compute
$1/\lambda_{i}$. All other values are set to 0. Let's interpret this
statistically. Suppose we have a precision matrix with one or more zero
eigenvalues and we want to find the covariance matrix. A zero eigenvalue
means we have no precision, or infinite variance, for some linear
combination (i.e., for some basis vector). We take the pseudo-inverse
and assign that linear combination zero variance.

Let's consider a specific example. Autoregressive models are often used
for smoothing (in time, in space, and in covariates). A first order
autoregressive model for $y_{1},y_{2},\ldots,y_{T}$ has
$E(y_{i}|y_{-i})=\frac{1}{2}(y_{i-1}+y_{i+1})$. Another way of writing
the model is in time-order: $y_{i}=y_{i-1}+\epsilon_{i}$. A second order
autoregressive model has
$E(y_{i}|y_{-i})=\frac{1}{6}(4y_{i-1}+4y_{i+1}-y_{i-2}-y_{i+2})$. These
constructions basically state that each value should be a smoothed
version of its neighbors. One can figure out that the **precision**
matrix for $y$ in the first order model is $$\left(\begin{array}{ccccc}
\ddots &  & \vdots\\
-1 & 2 & -1 & 0\\
\cdots & -1 & 2 & -1 & \dots\\
 & 0 & -1 & 2 & -1\\
 &  & \vdots &  & \ddots
\end{array}\right)$$ and in the second order model is

$$\left( \begin{array}{ccccccc} \ddots &  &  & \vdots \\ 1 & -4 & 6 & -4 & 1 \\ \cdots & 1 & -4 & 6 & -4 & 1 & \cdots \\  &  & 1 & -4 & 6 & -4 & 1 \\  &  &  & \vdots \end{array} \right).$$

If we look at the eigendecomposition of such
matrices, we see that in the first order case, the eigenvalue
corresponding to the constant eigenvector is zero.

```python
import numpy as np

precMat = np.array([[1,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,0],[0,0,-1,2,-1],[0,0,0,-1,1]])
e = np.linalg.eig(precMat)
e[0]        # 4th eigenvalue is numerically zero
e[1][:,3]   # constant eigenvector
```

This means we have no information about the overall level of $y$. So how
would we generate sample $y$ vectors? We can't put infinite variance on
the constant basis vector and still generate samples. Instead we use the
pseudo-inverse and assign ZERO variance to the constant basis vector.
This corresponds to generating realizations under the constraint that
$\sum y_{i}$ has no variation, i.e., $\sum y_{i}=\bar{y}=0$ - you can
see this by seeing that $\mbox{Var}(\Gamma_{\cdot i}^{\top}y)=0$ when
$\lambda_{i}=0$.

```python

---

[← Matrix multiplication](03-matrix-multiplication.md) · [Up: contents](index.md) · [Generate a realization. →](05-generate-a-realization.md)
