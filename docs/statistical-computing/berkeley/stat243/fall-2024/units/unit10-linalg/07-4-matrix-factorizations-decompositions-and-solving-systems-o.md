---
title: 4. Matrix factorizations (decompositions) and solving systems of linear equations
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit10-linalg.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Matrix factorizations (decompositions) and solving systems of linear equations

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit10-linalg.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Suppose we want to solve the following linear system:

$$\begin{aligned} Ax & = & b\\ x & = & A^{-1}b \end{aligned}$$


Numerically, this is never done by
finding the inverse and multiplying. Rather we solve the system using a
matrix decomposition (or equivalent set of steps). One approach uses
Gaussian elimination (equivalent to the LU decomposition), while another
uses the Cholesky decomposition. There are also iterative methods that
generate a sequence of approximations to the solution but reduce
computation (provided they are stopped before the exact solution is
found).

Gentle-CS has a nice table overviewing the various factorizations (Table
5.1, page 219). I've reproduced a variation on it here.


|     Name   |     Representation   |  Restrictions |   Properties   |  Uses       |
|  ----------| ----------------------| ------------| --------------------|-------------|
|   LU           |       $A_{nn}= L_{nn}U_{nn}$     |    $A$ generally square |  $L$ lower triangular; $U$ upper triangular |  solving equations; inversion |
|   QR           |   $A_{nm}= Q_{nn}R_{nm}$ or $A_{nm}=Q_{nm}R_{mm}$(skinny) | | $Q$ orthogonal; $R$ upper triangular | regression |
|      Cholesky    | $A_{nn}=U_{nn}^{\top}U_{nn}$ | $A$ positive (semi-) definite | $U$ upper triangular | multivariate normal; covariance; solving equations; inversion |
|     Eigen decomposition    | $A_{nn}=\Gamma_{nn}\Lambda_{nn}\Gamma_{nn}^{\top}$ | $A$ square, symmetric*| $\Gamma$ orthogonal; $\Lambda$ (non-negative**) diagonal | principal components analysis and related |
|     SVD    |    $A_{nm}=U_{nn}D_{nm}V_{mm}^{\top}$ or $A_{nm}= U_{nk}D_{kk}V_{mk}^{\top}$ | | $U, V$ orthogonal; $D$ (non-negative) diagonal | machine learning, topic models |

Table: Matrix factorizations useful for statistics / data science / machine learning

*For the eigen decomposition, I assume $A$ is symmetric, though there
is a decomposition for non-symmetric $A$.

** For positive definite or positive semi-definite $A$.

## Triangular systems

As a preface, let's figure out how to solve $Ax=b$ if $A$ is upper
triangular. The basic algorithm proceeds from the bottom up (and
therefore is called a 'backsolve'. We solve for $x_{n}$ trivially, and
then move upwards plugging in the known values of $x$ and solving for
the remaining unknown in each row (each equation).

1.  $x_{n}=b_{n}/A_{nn}$
2.  Now for $k<n$, use the already computed
    $\{x_{n},x_{n-1},\ldots,x_{k+1}\}$ to calculate
    $x_{k}=\frac{b_{k}-\sum_{j=k+1}^{n}x_{j}A_{kj}}{A_{kk}}$.
3.  Repeat for all rows.

How many multiplies and adds are done? Solving lower triangular systems
is very similar and involves the same number of calculations.

In Scipy, we can use `linalg.solve_triangular` to solve triangular systems.
The `trans` argument indicates whether to solve $Ax=b$ or $A^{\top}x=b$
(so one wouldn't need to transpose before solving).

```python
import scipy as sp
rng = np.random.default_rng(seed=1)
n = 20
X = rng.normal(size = (n,n))
## R has the `crossprod` function, which would be more efficient
## than having to transpose, but numpy doesn't seem to have an equivalent.
A = X.T @ X  # produce a positive def. matrix

b = rng.normal(size = n)
L = np.linalg.cholesky(A) # L is lower-triangular
U = L.T

out1 = sp.linalg.solve_triangular(L, b, lower=True)
out2 = np.linalg.inv(L) @ b
np.allclose(out1, out2)

out3 =  sp.linalg.solve_triangular(U, b, lower=False)
out4 = np.linalg.inv(U) @ b
np.allclose(out1, out2)
```


**To reiterate the distinction between matrix inversion and solving a
system of equations, when we write $U^{-1}b$, what we mean on a computer
is to carry out the above algorithm, not to find the inverse and then
multiply.**

Here's a good reason why.

```python
import time

rng = np.random.default_rng(seed=1)
n = 5000
X = rng.normal(size = (n,n))

## R has the `crossprod` function, which would be more efficient
## than having to transpose, but numpy doesn't seem to have an equivalent.
A = X.T @ X
b = rng.normal(size = n)
L = np.linalg.cholesky(A) # L is lower-triangular

t0 = time.time()
out1 = sp.linalg.solve_triangular(L, b, lower=True)
time.time() - t0

t0 = time.time()
out2 = np.linalg.inv(L) @ b
time.time() - t0
```

That assumes you have $L$, but we'll see in a bit that even when one
accounts for the creation of $L$, you don't want to invert matrices in
order to solve systems of equations.

## Gaussian elimination (LU decomposition)

Gaussian elimination is a standard way of directly computing a solution
for $Ax=b$. It is equivalent to the LU decomposition. LU is primarily
done with square matrices, but not always. Also LU decompositions do
exist for some singular matrices.

The idea of Gaussian elimination is to convert the problem to a
triangular system. In class, we'll walk through Gaussian elimination in
detail and see how it relates to the LU decomposition. I'll describe it
more briefly here. Following what we learned in algebra when we have
multiple equations, we preserve the solution, $x$, when we add multiples
of rows (i.e., add multiples of equations) together. This amounts to
doing $L_{1}Ax=L_{1}b$ for a lower-triangular matrix $L_{1}$ that
produces all zeroes in the first column of $L_{1}A$ except for the first
row. We proceed to zero out values below the diagonal for the other
columns of $A$. The result is
$L_{n-1}\cdots L_{1}Ax\equiv Ux=L_{n-1}\cdots L_{1}b\equiv b^{*}$ where
$U$ is upper triangular. This is the forward reduction step of Gaussian
elimination. Then the backward elimination step solves $Ux=b^{*}$.

If we're just looking for the solution of the system, we don't need the
lower-triangular factor $L=(L_{n-1}\cdots L_{1})^{-1}$ in $A=LU$, but it
turns out to have a simple form that is computed as we go along, it is
unit lower triangular and the values below the diagonal are the negative
of the values below the diagonals in $L_{1},\ldots,L_{n-1}$ (note that
each $L_{j}$ has non-zeroes below the diagonal only in the $j$th
column). As a side note related to storage, it turns out that as we
proceed, we can store the elements of $L$ and $U$ in the original $A$
matrix, except for the implicit 1s on the diagonal of $L$.

In class, we'll work out the computational complexity of the LU and see
that it is $O(n^{3})$.

If we look at `help(np.linalg.solve)` in Python, we see that it uses *_gesv*. A
Google search indicates that this is a Lapack routine that does the LU
decomposition with partial pivoting and row interchanges (see below on
what these are), so numpy is using the algorithm we've just discussed.

We can also explicitly get the LU decomposition in Python with
`scipy.linalg.lu()`, though for most use cases, what we want to
do is solve a system of equations. (In R, one can't easily get
the explicit LU decomposition, though `solve()` in R does use the LU.

One additional complexity is that we want to avoid dividing by very
small values to avoid introducing numerical inaccuracy (we would get
large values that might overwhelm whatever they are being added to, and
small errors in the divisor will have large effects on the result). This
can be done on the fly by interchanging equations to use the equation
(row) that produces the largest value to divide by. For example in the
first step, we would switch the first equation (first row) for whichever
of the remaining equations has the largest value in the first column.
This is called partial pivoting. The divisors are called pivots.
Complete pivoting also considers interchanging columns, and while
theoretically better, partial pivoting is generally sufficient and
requires fewer computations. Partial pivoting can be expressed as
multiplying along the way by permutation matrices,
$P_{1},\ldots P_{n-1}$ that switch rows. One can show with some work
that based on pivoting, we have $PA=LU$, where $P=P_{n-1}\cdots P_{1}$.
In the demo code, we'll see a toy example of the impact of pivoting.

Finally $|PA|=|P||A|=|L||U|=|U|$ (why?) so $|A|=|U|/|P|$ and since the
determinant of each permutation matrix, $P_{j}$ is -1 (except when
$P_{j}=I$ because we don't need to switch rows), we just need to
multiply by minus one if there is an odd number of permutations. Or if
we know the matrix is non-negative definite, we just take the absolute
value of $|U|$. So Gaussian elimination provides a fast stable way to
find the determinant.

## When would we explicitly invert a matrix?

In some cases (as we discussed in class) you actually need the inverse as
the output (e.g., for estimating standard errors).

But if you are just needing the inverse to multiply it by a vector or another
matrix, you're better off
using a decomposition. Basically, one can work out that the cost of computing
the inverse and doing subsequent multiplication with it is rather more
than computing the decomposition and doing subsequent multiplications with it,
regardless of how many columns there are in the matrix you are multiplying by.

With numpy, that may mean computing the decomposition and then
carrying out the steps to do the multiplication using the decomposition
or using `np.linalg.solve(A, B)` which, as mentioned above, uses the LU behind the scenes.
One would not do  `np.linalg.inv(A) @ B`.

## Cholesky decomposition

When $A$ is p.d., we can use the Cholesky decomposition to solve a
system of equations. Positive definite matrices can be decomposed as
$U^{\top}U=A$ where $U$ is upper triangular. $U$ is called a square root
matrix and is unique (apart from the sign, which we fix by requiring the
diagonals to be positive). One algorithm for computing $U$ is:

1.  $U_{11}=\sqrt{A_{11}}$
2.  For $j=2,\ldots,n$, $U_{1j}=A_{1j}/U_{11}$
3.  For $i=2,\ldots,n$,
    -   $U_{ii}=\sqrt{A_{ii}-\sum_{k=1}^{i-1}U_{ki}^{2}}$
    -   if $i<n$, then for $j=i+1,\ldots,n$:
        $U_{ij}=(A_{ij}-\sum_{k=1}^{i-1}U_{ki}U_{kj})/U_{ii}$

We can then solve a system of equations as: $U^{-1}(U^{\top-1}b)$.

Confusingly, while numpy's `cholesky` gives $L = U^\top$, scipy's
`cholesky` can return either $L$ or $U$ but defaults to $U$.

Here are two ways we can use the Cholesky to solve a system of equations:

```python
#| eval: false
U = sp.linalg.cholesky(A)
sp.linalg.solve_triangular(U,
          sp.linalg.solve_triangular(U, b, lower=False, trans='T'),
          lower=False)

U, lower = sp.linalg.cho_factor(A)
sp.linalg.cho_solve((U, lower), b)
```


The Cholesky has some nice advantages over the LU: (1) while both are
$O(n^{3})$, the Cholesky involves only half as many computations,
$n^{3}/6+O(n^{2})$ and (2) the Cholesky factorization has only
$(n^{2}+n)/2$ unique values compared to $n^{2}+n$ for the LU. Of course
the LU is more broadly applicable. The Cholesky does require computation
of square roots, but it turns out this is not too intensive. There is
also a method for finding the Cholesky without square roots.

#### Uses of the Cholesky

The standard algorithm for generating $y\sim\mathcal{N}(0,A)$ is:

```python
#| eval: false
L = sp.linalg.cholesky(A, lower=True)
y = L @ rng.normal(size = n)
```

!!! tip "Tip"
Where will most of the time in this two-step calculation
be spent?
:::

If a regression design matrix, $X$, is full rank, then $X^{\top}X$ is
positive definite, so we could find
$\hat{\beta}=(X^{\top}X)^{-1}X^{\top}Y$ using either the Cholesky or
Gaussian elimination.

However, for OLS, it turns out that the standard approach is to work with $X$
using the QR decomposition rather than working with $X^{\top}X$; working
with $X$ is more numerically stable, though in most situations without
extreme collinearity, either of the approaches will be fine.

We could also consider the GLS estimator, which accounts for dependence
in the errors: $\hat{\beta}=(X^{\top}\Sigma^{-1}X)^{-1}X^{\top}\Sigma^{-1}Y$

!!! tip "Tip"
Write efficient Python code to carry out
the GLS solution using the Cholesky factorization.

:::


#### Numerical issues with eigendecompositions and Cholesky decompositions for positive definite matrices

Monahan comments that in general Gaussian elimination and the Cholesky
decomposition are very stable. However, in the Cholesky case, if the
matrix is very ill-conditioned we can get $A_{ii}-\sum_{k}U_{ki}^{2}$
being negative and then the algorithm stops when we try to take the
square root. In this case, the Cholesky decomposition does not exist
numerically although it exists mathematically. It's not all that hard to
produce such a matrix, particularly when working with high-dimensional
covariance matrices with large correlations.

```python
rng = np.random.default_rng(seed=1)
locs = rng.uniform(size = 100)
rho = .1
dists = np.abs(locs[:, np.newaxis] - locs)
C = np.exp(-dists**2/rho**2)
e = np.linalg.eig(C)
np.sort(e[0])[::-1][96:100]
try:
    L = np.linalg.cholesky(C)
except Exception as error:
    print(error)

vals = np.abs(e[0])
np.max(vals)/np.min(vals)
```

I don't see a way to use pivoting with the Cholesky in Python, but in R,
one can do `chol(C, pivot = TRUE)`.

We can think about the accuracy here as follows. Suppose we have a
matrix whose diagonal elements (i.e., the variances) are order of
magnitude 1 and that the true value of a $U_{ii}$ is less than
$1\times10^{-16}$. From the given $A_{ii}$ we are subtracting
$\sum_{k}U_{ki}^{2}$ and trying to calculate this very small number but
we know that we can only represent the values $A_{ii}$ and
$\sum_{k}U_{ki}^{2}$ accurately to 16 places, so the difference is
garbage starting in the 17th position and could well be negative. Now
realize that $\sum_{k}U_{ki}^{2}$ is the result of a potentially large
set of arithmetic operations, and is likely represented accurately to
fewer than 16 places. Now if the true value of $U_{ii}$ is smaller than
the accuracy to which $\sum_{k}U_{ki}^{2}$ is represented, we can get a
difference that is negative.

Note that when the Cholesky fails, we can still compute an
eigendecomposition, but we have negative numeric eigenvalues. Even if
all the eigenvalues are numerically positive (or equivalently, we're
able to get the Cholesky), errors in small eigenvalues near machine
precision could have large effects when we work with the inverse of the
matrix. This is what happens when we have columns of the $X$ matrix
nearly collinear. We cannot statistically distinguish the effect of two
(or more) covariates, and this plays out numerically in terms of
unstable results.

A strategy when working with mathematically but not numerically positive
definite $A$ is to set eigenvalues or singular values to zero when they
get very small, which amounts to using a pseudo-inverse and setting to
zero any linear combinations with very small variance. We can also use
pivoting with the Cholesky and accumulate zeroes in the last $n-q$ rows
(for cases where we try to take the square root of a negative number),
corresponding to the columns of $A$ that are numerically linearly
dependent.

## QR decomposition

### Introduction

The QR decomposition is available for any matrix, $X=QR$, with $Q$
orthogonal and $R$ upper triangular. If $X$ is non-square, $n\times p$
with $n>p$ then the leading $p$ rows of $R$ provide an upper triangular
matrix ($R_{1}$) and the remaining rows are 0. (I'm using $p$ because
the QR is generally applied to design matrices in regression). In this
case we really only need the first $p$ columns of $Q$, and we have
$X=Q_{1}R_{1}$, the 'skinny' QR (this is what R's QR provides). For
uniqueness, we can require the diagonals of $R$ to be nonnegative, and
then $R$ will be the same as the upper-triangular Cholesky factor of
$X^{\top}X$:

$$\begin{aligned} X^{\top}X & = & R^{\top}Q^{\top}QR \\ & = & R^{\top}R\end{aligned}.$$


There are three standard approaches for
computing the QR, using (1) reflections (Householder transformations),
(2) rotations (Givens transformations), or (3) Gram-Schmidt
orthogonalization (see below for details).

For $n\times n$ $X$, the QR (for the Householder approach) requires
$2n^{3}/3$ flops, so QR is less efficient than LU or Cholesky.

We can also obtain the pseudo-inverse of $X$ from the QR:
$X^{+}=[R_{1}^{-1}\,0]Q^{\top}$. In the case that $X$ is not full-rank,
there is a version of the QR that will work (involving pivoting) and we
end up with some additional zeroes on the diagonal of $R_{1}$.

### Regression and the QR

Often QR is used to fit linear models, including in R. Consider the
linear model in the form $Y=X\beta+\epsilon$, finding
$\hat{\beta}=(X^{\top}X)^{-1}X^{\top}Y$. Let's consider the skinny QR
and note that $R^{\top}$ is invertible. Therefore, we can express the
normal equations as

$$
\begin{aligned}
X^{\top}X\beta & = & X^{\top} Y \\
R^{\top}Q^{\top}QR\beta & = & R^{\top}Q^{\top} Y \\
R \beta & = & Q^{\top} Y
\end{aligned}
$$


and solving for $\beta$ is just a
backsolve since $R$ is upper-triangular. Furthermore the standard
regression quantities, such as the hat matrix, the SSE, the residuals,
etc. can be easily expressed in terms of $Q$ and $R$.

Why use the QR instead of the Cholesky on $X^{\top}X$? The condition
number of $X$ is the square root of that of $X^{\top}X$, and the $QR$
factorizes $X$. Monahan has a discussion of the condition of the
regression problem, but from a larger perspective, the situations where
numerical accuracy is a concern are generally cases where the OLS
estimators are not particularly helpful anyway (e.g., highly collinear
predictors).

What about computational order of the different approaches to least
squares? The Cholesky is $np^{2}+\frac{1}{3}p^{3}$, an algorithm called
sweeping is $np^{2}+p^{3}$ , the Householder method for QR is
$2np^{2}-\frac{2}{3}p^{3}$, and the modified Gram-Schmidt approach for
QR is $2np^{2}$. So if $n\gg p$ then Cholesky (and sweeping) are faster
than the QR approaches. According to Monahan, modified Gram-Schmidt is
most numerically stable and sweeping least. In general, regression is
pretty quick unless $p$ is large since it is linear in $n$, so it may
not be worth worrying too much about computational differences of the
sort noted here.

### Regression and the QR in Python and R

We can get the Q and R matrices easily in Python.

```python
#| eval: false
Q,R = np.linalg.qr(X)
```

One of the methods used by the [`statsmodel` package in Python
uses the QR to fit a regression](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.fit.html).

Note that by default in Python (and in R), you get the skinny QR, namely only the
first $p$ rows of $R$ and the first $p$ columns of $Q$, where the latter
form an orthonormal basis for the column space of $X$. The remaining
columns form an orthonormal basis for the null space of $X$ (the space
orthogonal to the column space of $X$). The analogy in regression is
that we get the basis vectors for the regression, while adding the
remaining columns gives us the full $n$-dimensional space of the
observations.

Regression in R uses the QR decomposition via `qr()`, which calls a
Fortran function. `qr()` (and the Fortran functions that are called) is
specifically designed to output quantities useful in fitting linear
models.

In R, `qr()` returns the result as a list meant for use by other tools. R
stores the $R$ matrix in the upper triangle of `\$qr`, while the lower
triangle of *\$qr* and *\$aux* store the information for constructing
$Q$ (this relates to the Householder-related vectors $u$ below). One can
multiply by $Q$ using *qr.qy()* and by $Q^{\top}$ using *qr.qty()*. If
you want to extract $R$ and $Q$, the following will work:

```r
#| eval: false
X.qr = qr(X)
Q = qr.Q(X.qr)
R = qr.R(X.qr)
```

As a side note, there are QR-based functions that provide
regression-related quantities, such as *qr.resid()*, *qr.fitted()* and
*qr.coef()*. These functions (and their Fortran counterparts) exist
because one can work through the various regression quantities of
interest and find their expressions in terms of $Q$ and $R$, with nice
properties resulting from $Q$ being orthogonal and $R$ triangular.

### Computing the QR decomposition

Here we'll see some of the details of the different approaches to the
QR, in part because they involve some concepts that may be useful in
other contexts. I won't expect you to see all of how this works, but
please skim through this to get an idea of how things are done.

One approach involves reflections of vectors and a second rotations of
vectors. Reflections and rotations are transformations that are
performed by orthogonal matrices. The determinant of a reflection matrix
is -1 and the determinant of a rotation matrix is 1. We'll see some of
the details in the demo code.

#### QR Method 1: Reflections

If $u$ and $v$ are orthonormal vectors and $x$ is in the space spanned
by $u$ and $v$, $x=c_{1}u+c_{2}v$, then $\tilde{x}=-c_{1}u+c_{2}v$ is a
reflection (a *Householder* reflection) along the $u$ dimension (since
we are using the negative of that basis vector). We can think of this as
reflecting across the plane perpendicular to $u$. This extends simply to
higher dimensions with orthonormal vectors, $u,v_{1},v_{2},\ldots$

Suppose we want to formulate the reflection in terms of a "Householder"
matrix, $Q$. It turns out that $$Qx=\tilde{x}$$ if $Q=I-2uu^{\top}$. $Q$
has the following properties: (1) $Qu=-u$, (2) $Qv=v$ for $u^{\top}v=0$,
(3) $Q$ is orthogonal and symmetric.

One way to create the QR decomposition is by a series of Householder
transformations that create an upper triangular $R$ from $X$:

$$
\begin{aligned}
R & = & Q_{p}\cdots Q_{1} X \\
Q & = & (Q_{p}\cdots Q_{1})^{\top}
\end{aligned}
$$


where we make use of
the symmetry in defining $Q$.

Basically $Q_{1}$ reflects the first column of $X$ with respect to a
carefully chosen $u$, so that the result is all zeroes except for the
first element. We want $Q_{1}x=\tilde{x}=(||x||,0,\ldots,0)$. This can
be achieved with $u=\frac{x-\tilde{x}}{||x-\tilde{x}||}$. Then $Q_{2}$
makes the last $n-2$ rows of the second column equal to zero. We'll work
through this a bit in class.

In the regression context, as we work through the individual
transformations, $Q_{j}=I-2u_{j}u_{j}^{\top}$, we apply them to $X$ and
$Y$ to create $R$ (note this would not involve doing the full matrix
multiplication - think about what calculations are actually needed) and
$QY=Q^{\top}Y$, and then solve $R\beta=Q^{\top}Y$. To find
$\mbox{Cov}(\hat{\beta})\propto(X^{\top}X)^{-1}=(R^{\top}R)^{-1}=R^{-1}R^{-\top}$
we do need to invert $R$, but it's upper-triangular and of dimension
$p\times p$. It turns out that $Q^{\top}Y$ can be partitioned into the
first $p$ and the last $n-p$ elements, $z^{(1)}$ and $z^{(2)}$. The SSR
is $\|z^{(1)}\|^{2}$ and SSE is $\|z^{(2)}\|^{2}$.

Final side note: if $X$ is square (so $n=p)$ you might wonder why we
need $Q_{p}$ since after $p-1$ reflections, we don't need to zero
anything else out (since the last column of $R$ has $n$ non-zero
elements). It turns out that if we go back to thinking about a
Householder reflection in general, there is a lack of uniqueness in
choosing $\tilde{x}$. It could either be $(||x||,0,\ldots,0)$ or
$(-||x||,0,\ldots,0)$. For better numerical stability, one chooses from
the two of those such that $x_{1}$ is of the opposite sign to
$\tilde{x}_{1}$, so that one avoids cancellation of numbers that may be
of the same magnitude when doing $x-\tilde{x}$. The transformation
$Q_{p}$ is the last step of taking that approach of choosing the sign at
each step. $Q_{p}$ doesn't zero anything out; it just basically just
involves potentially setting $R_{pp}$ to be $-R_{pp}$. (To be honest,
I'm not clear on why one would bother to do that last step, but that
seems to be how it is presented in discussions of the Householder
approach.) Of course in the case of $p<n$, we definitely need $Q_{p}$ so
that the last $n-p$ rows of $R$ are zero and we can then discard them
when just using the skinny QR.

#### QR Method 2: Rotations

A *Givens* rotation matrix rotates a vector in a two-dimensional
subspace to be axis oriented with respect to one of the two dimensions
by changing the value of the other dimension. E.g. we can create
$\tilde{x}=(x_{1},\ldots,\tilde{x}_{p},\ldots,0,\ldots x_{n})$ from
$x=(x_{1,}\ldots,x_{p},\ldots,x_{q},\ldots,x_{n})$ using a matrix
multiplication: $\tilde{x}=Qx$. $Q$ is orthogonal but not symmetric.

We can use a series of Givens rotations to do the QR but unless it is
done carefully, more computations are needed than with Householder
reflections. The basic story is that we apply a series of Givens
rotations to $X$ such that we zero out the lower triangular elements.

$$
\begin{aligned}
R & = & Q_{pn}\cdots Q_{23}Q_{1n}\cdots Q_{13}Q_{12} X \\
Q & = & (Q_{pn}\cdots Q_{12})^{\top}\end{aligned}.
$$


Note that we create
the $n-p$ zero rows in $R$ (because the calculations affect the upper
triangle of $R$), but we can then ignore those rows and the
corresponding columns of $Q$.

#### QR Method 3: Gram-Schmidt Orthogonalization

Gram-Schmidt involves finding a set of orthonormal vectors to span the
same space as a set of LIN vectors, $x_{1},\ldots,x_{p}$. If we take the
LIN vectors to be the columns of $X$, so that we are discussing the
column space of $X$, then G-S yields the QR decomposition. Here's the
algorithm:

1.  $\tilde{x}_{1}=\frac{x_{1}}{\|x_{1}\|}$ (normalize the first vector)

2.  Orthogonalize the remaining vectors with respect to $\tilde{x}_{1}$:

    1.  $\tilde{x}_{2}=\frac{x_{2}-\tilde{x}_{1}^{\top}x_{2}\tilde{x}_{1}}{\|x_{2}-\tilde{x}_{1}^{\top}x_{2}\tilde{x}_{1}\|}$,
        which orthogonalizes with respect to $\tilde{x}_{1}$ and
        normalizes. Note that
        $\tilde{x}_{1}^{\top}x_{2}\tilde{x}_{1}=\langle\tilde{x}_{1},x_{2}\rangle\tilde{x}_{1}$.
        So we are finding a scaling, $c\tilde{x}_{1}$, where $c$ is
        based on the inner product, to remove the variation in the
        $x_{1}$ direction from $x_{2}$.

    2.  For $k>2$, find interim vectors, $x_{k}^{(2)}$, by
        orthogonalizing with respect to $\tilde{x}_{1}$

3.  Proceed for $k=3,\ldots$, in turn orthogonalizing and normalizing
    the first of the remaining vectors w.r.t. $\tilde{x}_{k-1}$ and
    orthogonalizing the remaining vectors w.r.t. $\tilde{x}_{k-1}$ to
    get new interim vectors

Mathematically, we could instead orthogonalize $x_{2}$ w.r.t.
$\tilde{x}_{1}$, then orthogonalize $x_{3}$ w.r.t.
$\{\tilde{x}_{1},\tilde{x}_{2}\}$, etc. The algorithm above is the
*modified* G-S, and is known to be more numerically stable if the
columns of $X$ are close to collinear, giving vectors that are closer to
orthogonal. The resulting $\tilde{x}$ vectors are the columns of $Q$.
The elements of $R$ are obtained as we proceed: the diagonal values are
the the normalization values in the denominators, while the
off-diagonals are the inner products with the already-computed columns
of $Q$ that are computed as part of the numerators.

Another way to think about this is that $R=Q^{\top}X$, which is the same
as regressing the columns of $X$ on $Q,$ since
$(Q^{\top}Q)^{-1}Q^{\top}X=Q^{\top}X$. By construction, the first column
of $X$ is a scaling of the first column of $Q$, the second column of $X$
is a linear combination of the first two columns of $Q$, etc., so $R$
being upper triangular makes sense.

### The "tall-skinny" QR

Suppose you have a very large regression problem, with $n$ very large,
and $n\gg p$. There is a variant of the QR, called the tall-skinny QR
(see <http://arxiv.org/pdf/0808.2664v1.pdf> for details) that allows us
to find the decomposition in a parallel fashion. The basic idea is to do
a nested set of QR decompositions on blocks of rows of $X$:

$$
X  =  \left( \begin{array}{c}
X_{0} \\
X_{1} \\
X_{2} \\
X_{3}
\end{array}
\right) =
\left(
\begin{array}{c}
Q_{0} R_{0} \\
Q_{1} R_{1} \\
Q_{2} R_{2} \\
Q_{3} R_{3}
\end{array} \right),
$$

followed by 'reduction' steps (this
can be done in a map-reduce context) that do the $QR$ of pairs of the
$R$ factors:
$$\left(\begin{array}{c}
R_{0}\\
R_{1}\\
R_{2}\\
R_{3}
\end{array}\right)=\left(\begin{array}{c}
\left(\begin{array}{c}
R_{0}\\
R_{1}
\end{array}\right)\\
\left(\begin{array}{c}
R_{2}\\
R_{3}
\end{array}\right)
\end{array}\right)=\left(\begin{array}{c}
Q_{01}R_{01}\\
Q_{23}R_{23}
\end{array}\right)$$ and $$\left(\begin{array}{c}
R_{01}\\
R_{23}
\end{array}\right)=Q_{0123}R_{0123}.$$

The full decomposition is then

$$X=\left( \begin{array}{cccc} Q_{0} & 0 & 0 & 0 \\ 0 & Q_{1} & 0 & 0 \\ 0 & 0 & Q_{2} & 0 \\ 0 & 0 & 0 & Q_{3} \end{array} \right) \left( \begin{array}{cc} Q_{01} & 0 \\ 0 & Q_{23} \end{array} \right) Q_{0123} R_{0123} = QR.$$


The computation can be done in
parallel (in particular it can be done with map-reduce) and the $Q$
matrix for big problems would generally not be computed explicitly but
would be stored in its constituent pieces.

Alternatively, there is a variant on the algorithm that processes the
row-blocks of $X$ serially, allowing you to do QR on a large tall-skinny
matrix that you can't fit in memory (or possibly even on disk). First
you do $QR$ on $X_{0}$ to get $Q_{0}R_{0}$. Then you stack $R_{0}$ on
top of $X_{1}$ and do QR to get $R_{01}$. Then stack $R_{01}$ on top of
$X_{2}$ to get $R_{012}$, etc.

## Determinants

The absolute value of the determinant of a square matrix can be found
from the product of the diagonals of the triangular matrix in any
factorization that gives a triangular (including diagonal) matrix times
an orthogonal matrix (or matrices) since the determinant of an
orthogonal matrix is either one or minus one.

$|A|=|QR|=|Q||R|=\pm|R|$

$|A^{\top}A|=|(QR)^{\top}QR|=|R^{\top}R|=|R_{1}^{\top}R_{1}|=|R_{1}|^{2}$

(Note of course that that is for square $A$, so we have $R$ is $n \times $n$.

In Python, the following will do it (on the log scale).

```python
#| eval: false
Q,R = qr(A)
magn = np.sum(np.log(np.abs(np.diag(R))))
```

An alternative is the product of the diagonal elements of $D$ (the
singular values) in the SVD factorization, $A=UDV^{\top}$.

For non-negative definite matrices, we know the determinant is
non-negative, so the uncertainty about the sign is not an issue. For
positive definite matrices, a good approach is to use the product of the
diagonal elements of the Cholesky decomposition.

One can also use the product of the eigenvalues:
$|A|=|\Gamma\Lambda\Gamma^{-1}|=|\Gamma||\Gamma^{-1}||\Lambda|=|\Lambda|$

#### Computation

Computing from any of these diagonal or triangular matrices as the
product of the diagonals is prone to overflow and underflow, so we
**always** work on the log scale as the sum of the log of the values.
When some of these may be negative, we can always keep track of the
number of negative values and take the log of the absolute values.

Often we will have the factorization as a result of other parts of the
computation, so we get the determinant for free.

We can use `np.linalg.logdet()` or (definitely not recommended)
`np.linalg.det()` to calculate the determinant in Python.
These functions use the LU decomposition.

---

[← 3. Computational issues](06-3-computational-issues.md) · [Up: contents](index.md) · [5. Eigendecomposition and SVD →](08-5-eigendecomposition-and-svd.md)
