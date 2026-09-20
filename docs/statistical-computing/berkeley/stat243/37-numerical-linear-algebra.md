---
title: "37. Numerical Linear Algebra"
course: "Berkeley Stat 243 Fall 2024"
chapter: 37
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 37. Numerical Linear Algebra

## What this covers

This chapter is about the numerical side of linear algebra: not what a matrix decomposition *is*
mathematically, but how it changes what a computer actually does, and why that matters for
statistics. It assumes ordinary matrix algebra (rank, eigenvalues, inverses) and some prior exposure
to the limits of computer arithmetic — floating-point precision, and the fact that a computation
that is exact on paper can lose accuracy on a machine. The question the chapter answers is: given a
linear-algebra calculation that shows up in a statistical method, how should it actually be carried
out, and what goes wrong if it is not?

## Why this is a separate subject

Many statistical and machine-learning methods lean on linear algebra somewhere — at minimum matrix
multiplication, and very often a decomposition to fit a model: linear regression and its many
elaborations, deep networks, principal components analysis and its relatives. The key principle
behind this whole chapter is that **the form of a mathematical expression and how it should be
evaluated on a computer can be very different** — a better computational approach can be both faster
and more numerically accurate. Three examples make the point concrete:

- If $X, Y$ are matrices and $z$ a vector, compute $X(Yz)$, never $(XY)z$: the parenthesization
  changes the operation count enormously.
- The OLS quantity $(X^{\top}X)^{-1}X^{\top}Y$ is never computed by forming $X^{\top}X$ and
  inverting it — in some implementations $X^{\top}X$ is never formed at all.
- To swap two rows of a matrix $A$, you can multiply by a permutation matrix $P$, but on a computer
  you typically don't touch the data in memory at all — you just rework which index points to which
  stored row.

Everything below is really working out the consequences of that principle for the specific
decompositions and algorithms that recur in statistics.

## Notation, norms, and orthogonality

Capital letters denote matrices ($A$), lower case vectors ($x$); $x_i$ is the $i$th entry of $x$,
$A_{ij}$ the $(i,j)$ entry, $A_{\cdot j}$ the $j$th column, $A_{i\cdot}$ the $i$th row. A vector is
treated as a one-column matrix, so $x^{\top}$ is a one-row matrix. Two matrices are *conformable*
for an operation when the dimensions line up — for $A+B$, equal dimensions; for $AB$, the number of
columns of $A$ must equal the number of rows of $B$. Checking conformability is a cheap way to catch
errors: is $\mathrm{Cov}(Ax)=A\,\mathrm{Cov}(x)A^{\top}$ or $A^{\top}\mathrm{Cov}(x)A$? If $A$ is
$m\times n$, only the first is conformable, so it must be that one.

The **inner product** is $\sum_i x_iy_i = x^{\top}y \equiv \langle x,y\rangle$; the **outer product**
$xy^{\top}$ collects all pairwise products.

For vectors, $\|x\|_p = \left(\sum_i |x_i|^p\right)^{1/p}$, and the Euclidean norm
$\|x\|_2=\sqrt{x^{\top}x}$ is written $\|x\|$ unless noted otherwise. For matrices, one common norm
is the Frobenius norm, $\|A\|_F = \left(\sum_{i,j}a_{ij}^2\right)^{1/2}$. More important for this
chapter is the **induced matrix norm**, defined from a vector norm as
$$\|A\| = \sup_{x\neq 0}\frac{\|Ax\|}{\|x\|},$$
so that $\|A\|_2 = \sup_{\|x\|_2=1}\|Ax\|_2$ — the most that $A$ can stretch a unit vector. In the
2-norm this supremum is exactly the largest singular value of $A$. Any legitimate matrix norm
satisfies $\|AB\|\leq\|A\|\|B\|$ and the triangle inequality $\|A+B\|\leq\|A\|+\|B\|$. A vector is
*normalized* if $\|x\|=1$; any vector can be normalized as $\tilde x = x/\|x\|$, and the angle
between two vectors is $\theta = \cos^{-1}\!\left(\langle x,y\rangle/\sqrt{\langle x,x\rangle\langle
y,y\rangle}\right)$.

Two vectors are **orthogonal** if $x^{\top}y=0$. A square matrix is **orthogonal** if its columns
(equivalently its rows) are pairwise orthogonal and normalized; orthogonal matrices have full rank,
satisfy $A^{\top}A=I$ so $A^{-1}=A^{\top}$, and have determinant $\pm 1$. The product of two
orthogonal matrices is orthogonal, since $(AB)^{\top}AB = B^{\top}A^{\top}AB = B^{\top}B=I$. A matrix
that swaps two rows (or columns) when multiplied — a *permutation matrix* — is an orthogonal matrix
with determinant $-1$; premultiplying by $P$ permutes rows, postmultiplying permutes columns.
Crucially, a computer usually never carries out that multiplication: it reworks stored index values
instead, which is the concrete version of the third example above.

A few further facts used repeatedly: $AB\neq BA$ in general, but $A+B=B+A$ and $A(BC)=(AB)C$. The
trace (sum of diagonal entries) satisfies $\mathrm{tr}(A+B)=\mathrm{tr}(A)+\mathrm{tr}(B)$,
$\mathrm{tr}(A)=\mathrm{tr}(A^{\top})$, and — usefully — $\mathrm{tr}(ABC)=\mathrm{tr}(CAB)=\mathrm{tr}(BCA)$:
a matrix can be cycled from the front to the back of a trace, provided the product stays
conformable. This lets you (a) reorder a product of non-square matrices to minimize computation, and
(b) rewrite a scalar quadratic form as a trace, $x^{\top}Ax = \mathrm{tr}(xx^{\top}A)$, which is
occasionally the easier object to manipulate. For square matrices the determinant satisfies
$|AB|=|A||B|$, hence $|A^{-1}|=1/|A|$, and $|A|=|A^{\top}|$ (visible once you have the QR
decomposition of $A$, using that triangular and orthogonal matrices have easily-computed
determinants). For invertible square $A,B$: $(A^{-1})^{\top}=(A^{\top})^{-1}$ — from
$(AB)^{\top}=B^{\top}A^{\top}$ applied to $A^{\top}(A^{-1})^{\top}=(A^{-1}A)^{\top}=I$ — and
$(AB)^{-1}=B^{-1}A^{-1}$, since $B^{-1}A^{-1}AB=I$.

Two other products are worth naming. The **Hadamard (direct) product** $A*B$ multiplies
corresponding entries. The **Kronecker product** multiplies every entry of one matrix by the whole
of the other:
$$A\otimes B=\begin{pmatrix}A_{11}B & \cdots & A_{1m}B\\ \vdots & \ddots & \vdots\\ A_{n1}B & \cdots & A_{nm}B\end{pmatrix},$$
and its inverse is the Kronecker product of the inverses, $(A\otimes B)^{-1}=A^{-1}\otimes B^{-1}$
— useful because solving the Kronecker-structured system this way costs $O(n^3+m^3)$ instead of the
naive $O((nm)^3)$.

Finally, a **matrix decomposition** re-expresses $A$ as a product of two or three simpler matrices —
simpler by having fewer rows/columns, being diagonal, triangular, or sparse, or being orthogonal.
Once you have a decomposition, computation with $A$ is generally much cheaper, because it inherits
the structure of the pieces. The bulk of this chapter is about which decomposition to use when.

## Counting the cost

Computational complexity is assessed by counting multiplies/divides and adds/subtracts (addition is
marginally cheaper, so some algorithms trade multiplications for additions). What matters is usually
the *order* of the count, written $O(f(n))$: the number of operations approaches $c\,f(n)$ as
$n\to\infty$. For matrix multiplication $AB$ with $A$ of size $a\times b$ and $B$ of size $b\times
c$: each of the $ac$ entries of the product is an inner product of length $b$, so there are $abc$
multiplies, $O(abc)$ operations — usually one just counts multiplies, since there is generally one
addition per multiply. Two symmetric $n\times n$ matrices multiply in $O(n^3)$, and most
factorizations (e.g. Cholesky) are also $O(n^3)$ unless the matrix has exploitable structure such as
sparsity. Memory scales too: holding the product above needs $ab+bc+ac$ entries, which for symmetric
$n\times n$ matrices is $3n^2$ — at $n=10{,}000$, that's $3\cdot 10000^2\cdot 8/10^9 = 2.4$ GB of
doubles, for the inputs and output of a single multiply.

$O(n^q)$ is *polynomial time*; $O(b^n)$ (exponential) is much worse, $O(\log n)$ (log time) much
better. NP-complete problems are, roughly, ones with no known polynomial-time algorithm, and all
such problems can be rewritten as instances of one another. But asymptotic order can mislead about
actual running time: an $O(n^2)$ algorithm can beat an $O(n\log n)$ one for realistic $n$, if the
latter's hidden constant is large — e.g. $n^2$ operations can be faster than $1000(n\log n + n)$,
because the constant $1000$ and the lower-order term $1000n$ both matter at finite $n$. *Flops*
(floating point operations, or floating point operations per second) is the usual unit for both
the operation count and the speed of a machine.

## Rank and invertibility, read statistically

A set of vectors $v_1,\ldots,v_n$ is **linearly independent** (LIN) if none is a linear combination
of the others; with vectors of length $n$ you can have at most $n$ of them. The **rank** of a matrix
is the number of LIN rows (equivalently columns), bounded by the smaller dimension. A set of LIN
vectors spans a space of all their linear combinations and is a set of **basis vectors** for it; a
vector $y$ in that space can be written $y=\sum_i c_iv_i$, and if the basis is orthonormal, $c_i =
\langle y,v_i\rangle$.

Read this in a regression context. With $p$ covariates (columns of the design matrix $X$) of which
$q\leq p$ are LIN, the column space of $X$ has dimension $q$, and $X^{\top}X$ has $p-q$ zero
eigenvalues. Think of the $q$ basis vectors as (non-orthogonal) axes: a point in the space is a set
of $q$ coordinates against them, just as in $\mathbb{R}^q$. If $n=p=q$, the $n$ observations sit
exactly on the fitted surface — a unique exact solution, no residual (with $n=p=2$, the two points
determine the line exactly). If $n<p$, the covariates span at most an $n$-dimensional space, and
there are infinitely many exact solutions — the system is *underdetermined*. If $n>p=q$ (the usual
case), there is generally no exact solution, and regression is about finding the point in the column
space of $X$ closest to the observation vector — i.e. projecting $y$ onto that space.

For square matrices, invertibility, rank, and definiteness are tightly linked. A "regular" square
matrix has an eigendecomposition $A=\Gamma\Lambda\Gamma^{-1}$, with eigenvectors as the columns of
$\Gamma$ and eigenvalues $\lambda_i$ on the diagonal of $\Lambda$ (symmetric matrices, and matrices
with distinct eigenvalues, are always regular). The rank of $A$ equals its number of nonzero
eigenvalues, and $A$ is invertible (nonsingular, full rank) exactly when none are zero, in which case
$A^{-1}=\Gamma\Lambda^{-1}\Gamma^{-1}$. For a symmetric $A$, $\Gamma$ is orthogonal and real, giving
$A=\Gamma\Lambda\Gamma^{\top}$ and $A^{-1}=\Gamma\Lambda^{-1}\Gamma^{\top}$; the determinant is the
product of the eigenvalues, zero exactly when rank is deficient.

Restricting to symmetric matrices — the ones that actually arise as covariance-like objects in
statistics — positive definiteness has a direct statistical meaning: if $\mathrm{Cov}(y)=A$, then
$x^{\top}Ax = \mathrm{Var}(x^{\top}y)$, so $A$ positive definite is exactly the statement that every
linear combination of $y$'s entries has positive variance. That is why every genuine covariance
matrix is positive (semi-)definite, and vice versa. Two chains of equivalence summarize it:

$$A\text{ p.d.} \iff A\text{ is a covariance matrix} \iff x^{\top}Ax>0\ \forall x \iff \lambda_i>0\ \forall i \implies |A|>0 \implies A\text{ invertible} \iff A\text{ nonsingular} \iff A\text{ full rank},$$

$$A\text{ p.s.d.} \iff A\text{ is a constrained covariance matrix} \iff x^{\top}Ax\geq 0,\ =0\text{ for some }x \iff \lambda_i\geq 0,\text{ some }=0 \implies |A|=0 \iff A\text{ singular} \iff A\text{ not full rank}.$$

### The eigendecomposition as a generative device

Read $A=\Gamma\Lambda\Gamma^{\top}$ as a recipe for generating a random vector with $\mathrm{Cov}(y)=A$:
set $y=\Gamma\Lambda^{1/2}z$ for $\mathrm{Cov}(z)=I$, where $\Lambda^{1/2}$ has entries
$\sqrt{\lambda_i}$. Then $y$ is a linear combination of the eigenvectors (as basis vectors), with the
weight on eigenvector $\Gamma_{\cdot i}$ having standard deviation $\sqrt{\lambda_i}$ — the $z$'s
supply the (independent, unit-variance) coordinates, and $\Lambda^{1/2}$ rescales them. Going the
other way, projecting $y$ back onto the eigenvector basis recovers those weights:
$w = (\Gamma^{\top}\Gamma)^{-1}\Gamma^{\top}y = \Gamma^{\top}y = \Lambda^{1/2}z$, using
orthogonality of $\Gamma$.

If instead $x^{\top}Ax\geq 0$ (positive *semi*-definite), one or more eigenvalues can be exactly
zero, and it is worth asking what that means for the generative picture: what does a zero eigenvalue
mean for $y=\Gamma\Lambda^{1/2}z$? What if an eigenvalue is merely very small and gets rounded to
zero? And for a **precision matrix** — the inverse of a covariance matrix,
$A^{-1}=\Gamma\Lambda^{-1}\Gamma^{\top}$ — what does a very large or very small diagonal entry of
$\Lambda^{-1}$ mean? (These are worth sitting with before reading on; see the exercises.) One fact
worth recording along the way: for any $n\times p$ matrix $X$, the cross-product $X^{\top}X$ is
always positive definite (or semi-definite, if $p>n$) — it is, after all, a scaled empirical
covariance matrix.

### Generalized inverses

Solving $Ax=b$ when $A$ is invertible just gives $x=A^{-1}b$. When $A$ is not full rank, a
**generalized inverse** $A^{-}$ satisfies $AA^{-}A=A$; the **Moore–Penrose inverse** (the
pseudo-inverse) $A^{+}$ is the unique generalized inverse with the further property that $x=A^{+}b$
is the *shortest* solution to $Ax=b$. It is built from an eigendecomposition (or SVD) as
$\Gamma\Lambda^{+}\Gamma^{\top}$, where $\Lambda^{+}$ inverts every nonzero $\lambda_i$ and leaves
the zero ones as zero. Statistically: a zero eigenvalue of a precision matrix means infinite
variance for the corresponding basis direction — no information about it at all — and the
pseudo-inverse handles this by assigning that direction exactly **zero** variance rather than
infinite, i.e. it constrains that linear combination not to vary.

A worked example makes this concrete. Autoregressive smoothing models are often specified through
conditional means: a first-order model has $E(y_i\mid y_{-i}) = \tfrac12(y_{i-1}+y_{i+1})$, and a
second-order model $E(y_i\mid y_{-i}) = \tfrac16(4y_{i-1}+4y_{i+1}-y_{i-2}-y_{i+2})$ — each value is
a smoothed version of its neighbors. Working through the algebra, the corresponding precision matrix
for the first-order model is tridiagonal, with $2$ on the diagonal and $-1$ on the off-diagonals in
the interior (the boundary rows of a finite chain have $1$ instead of $2$, since they have only one
neighbor):

$$\begin{pmatrix}1 & -1 & & & \\ -1 & 2 & -1 & & \\ & -1 & 2 & -1 & \\ & & -1 & 2 & -1\\ & & & -1 & 1\end{pmatrix}.$$

This matrix has a zero eigenvalue whose eigenvector is the constant vector — the model carries no
information about the *overall level* of $y$, only about how it varies. To simulate from it, you
cannot put infinite variance on the constant direction, so the pseudo-inverse is used instead,
assigning that direction exactly zero variance: this is the same as generating under the constraint
$\sum_i y_i = 0$.

```python
precMat = np.array([[1,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,0],
                     [0,0,-1,2,-1],[0,0,0,-1,1]])
e = np.linalg.eig(precMat)          # 4th eigenvalue is numerically zero;
                                     # its eigenvector is constant

evals = 1 / e[0]                    # variances
evals[3] = 0                        # generalized inverse: zero variance here
rng = np.random.default_rng(seed=1)
y = e[1] @ ((evals ** 0.5) * rng.normal(size=5))
```

A model could then be parameterized as $\mu + y$, adding back an explicit mean (and, in the
second-order case with two non-identifiable directions — level and linear trend — an explicit
linear term too), letting the covariance structure above handle only the smooth deviation from that
mean.

This machinery also explains two facts about regression's central object, $X^{\top}X$: it is always
symmetric and non-negative definite, hence the use of $(X^{\top}X)^{-1}$ in OLS, and it fails to be
positive definite exactly when $X$'s columns are not all linearly independent. The fitted-value
("hat") matrix $H = X(X^{\top}X)^{-1}X^{\top}$ projects $Y$ onto the column space of $X$, and is
**idempotent**, $HH=H$ — a second projection onto a space you're already in does nothing — and
**singular**, except in one special case (see the exercises).

## Ill-conditioning

A problem is **ill-conditioned** if small changes to its inputs produce large changes in its output,
and this is quantified by a **condition number**. The most important case for us is inversion: the
*condition number with respect to inversion*, using the $L_2$ norm, is the ratio of the largest to
the smallest eigenvalue magnitude of a nonsingular square matrix. A vivid example:
$$A=\begin{pmatrix}10&7&8&7\\7&5&6&5\\8&6&10&9\\7&5&9&10\end{pmatrix}.$$
Solving $Ax=b$ for $b=(32,23,33,31)$ gives $x=(1,1,1,1)$ exactly. Perturb $b$ only slightly, to
$(32.1,22.9,33.1,30.9)$, and the solution jumps to roughly $(9.2,-12.6,4.5,-1.1)$ — a tiny change in
the input produces a wildly different answer.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A unit circle mapped by an ill-conditioned matrix to a long thin ellipse, showing the condition number as the ratio of the axes">
  <circle cx="75" cy="100" r="42" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <text x="75" y="155" text-anchor="middle" font-size="12" fill="currentColor">unit vectors, length 1</text>
  <defs>
    <marker id="arrow-lin" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="128" y1="100" x2="170" y2="100" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow-lin)"/>
  <text x="149" y="90" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <g transform="translate(255 100) rotate(-15)">
    <ellipse cx="0" cy="0" rx="60" ry="10" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.3"/>
    <line x1="0" y1="0" x2="60" y2="0" stroke="currentColor" stroke-width="1"/>
    <line x1="0" y1="0" x2="0" y2="10" stroke="currentColor" stroke-width="1"/>
  </g>
  <text x="255" y="45" text-anchor="middle" font-size="12" fill="currentColor">Ax: an ellipse with axes of length sigma-max, sigma-min</text>
  <text x="255" y="175" text-anchor="middle" font-size="12" fill="currentColor">cond(A) = sigma-max / sigma-min</text>
</svg>
<figcaption>The induced 2-norm is how much a matrix can stretch a unit vector; applied to the whole
unit circle, $A$ produces an ellipse whose axis lengths are its singular values. A large ratio
between the longest and shortest axis is exactly what makes a problem ill-conditioned: some
directions are barely felt by $A$ (or by solving $Ax=b$), and error concentrated in a
nearly-invisible direction of $A$ becomes hugely amplified by $A^{-1}$.</figcaption>
</figure>

The bound behind this comes from manipulating the induced-norm inequality: for a perturbation
$\delta b$ of $b$ producing a perturbed solution $x+\delta x$,
$$\frac{\|\delta x\|}{\|x\|} \leq \|A\|\,\|A^{-1}\|\,\frac{\|\delta b\|}{\|b\|},$$
and $\mathrm{cond}(A)\equiv\|A\|\|A^{-1}\|$ is exactly the ratio-of-eigenvalues quantity above,
because $\|A\|_2$ is the largest-magnitude eigenvalue and $\|A^{-1}\|_2$ its reciprocal counterpart
(the eigenvalues of $A^{-1}$ are the reciprocals of those of $A$). The practical use of all this is
in understanding the accuracy of a computed solution, since on a computer the *actual* system solved
is $(A+\delta A)(x+\delta x) = b+\delta b$, with the perturbations coming from the finite precision
of computer numbers: $\|\delta b\|/\|b\| \approx 10^{-p}$ and $\|\delta A\|/\|A\|\approx 10^{-p}$,
with $p=16$ for standard double precision. This gives the approximation
$$\frac{\|\delta x\|}{\|x\|} \approx \mathrm{cond}(A)\cdot 10^{-p},$$
valid as long as the result is still much less than one. So if $\mathrm{cond}(A)\approx 10^t$, you
get accuracy of order $10^{t-p}$ rather than $10^{-p}$: the condition number tells you how many
digits of precision a calculation loses relative to the machine's native precision. A condition
number of $10^{8}$ costs 8 of the usual 16 digits.

**Improving conditioning.** In statistics, ill-conditioning most often comes from collinearity among
regressors, and often the right fix is not numerical but statistical — rethinking the model, since
severe ill-conditioning usually signals a real identifiability problem, not just a computational
inconvenience. Where a purely numerical fix is appropriate, the general principle is to avoid large
disparities in the magnitudes of the numbers involved — centering and scaling columns, in a
regression context. A worked example: fit $y=\beta_0+\beta_1 t+\beta_2 t^2+\epsilon$ with $t$ ranging
over calendar years $1990,\ldots,2010$ and true coefficients $(5,\,0.1,\,0.0001)$. The naive design
matrix (with raw years) is badly conditioned — the fitted coefficients come out quite far from the
truth, especially the intercept and linear term, and this is primarily an artifact of conditioning
rather than of the added noise. Centering the covariate at $t-2000$ improves things sharply: the
*true* coefficients after centering (found by expanding $\beta_0+\beta_1((t-2000)+2000)+
\beta_2((t-2000)+2000)^2$) become $(605,\,0.5,\,0.0001)$, and now the fitted intercept and linear
term land close to that. Interestingly, the quadratic coefficient's estimate does not move at all
between the naive and centered fits — a genuinely surprising piece of behavior that isn't fully
explained here; scaling $t$ down further (e.g. dividing the centered years by 10) improves the
condition number still more. The general lesson: try to work with quantities whose magnitude is
around 1 — a matter of choosing convenient units (income in thousands rather than dollars, say)
rather than heavier machinery.

## Solving linear systems without inverting

Numerically, $x=A^{-1}b$ is essentially never computed by forming $A^{-1}$ and multiplying. Instead
you solve the system via a decomposition. The standard options:

| Name | Representation | Restrictions | Properties | Typical use |
|---|---|---|---|---|
| LU | $A_{nn}=L_{nn}U_{nn}$ | $A$ generally square | $L$ lower triangular, $U$ upper triangular | solving equations, inversion |
| QR | $A_{nm}=Q_{nn}R_{nm}$ (or skinny $Q_{nm}R_{mm}$) | — | $Q$ orthogonal, $R$ upper triangular | regression |
| Cholesky | $A_{nn}=U_{nn}^{\top}U_{nn}$ | $A$ positive (semi-)definite | $U$ upper triangular | multivariate normal, covariance, solving equations |
| Eigendecomposition | $A_{nn}=\Gamma_{nn}\Lambda_{nn}\Gamma_{nn}^{\top}$ | $A$ square, symmetric | $\Gamma$ orthogonal, $\Lambda$ diagonal | PCA and relatives |
| SVD | $A_{nm}=U_{nn}D_{nm}V_{mm}^{\top}$ (or reduced) | — | $U,V$ orthogonal, $D$ non-negative diagonal | machine learning, topic models |

*(adapted from Gentle, Computational Statistics, Table 5.1)*

### Triangular systems: the common final step

Every one of these decompositions ends by solving a **triangular** system, so it is worth fixing
that algorithm first. For upper-triangular $A$, solving $Ax=b$ proceeds bottom-up (a *backsolve*):
$$x_n = b_n/A_{nn}, \qquad x_k = \frac{b_k - \sum_{j=k+1}^n x_jA_{kj}}{A_{kk}} \text{ for } k<n,$$
using already-known entries of $x$ as you move up. Solving a lower-triangular system is symmetric,
with the same operation count. This is why it matters that $U^{-1}b$, when written down
mathematically, means "run this algorithm" on a computer — not "form $U^{-1}$, then multiply." The
difference is not just elegance: forming the explicit inverse and multiplying costs meaningfully
more than solving directly, and the gap only grows with $n$.

### LU (Gaussian elimination)

Gaussian elimination directly solves $Ax=b$ and is equivalent to the **LU decomposition** — mostly
applied to square $A$, though it exists for some singular matrices too. The idea: preserve the
solution while adding multiples of equations (rows) together, to zero out everything below the
diagonal one column at a time. Formally, $L_1Ax=L_1b$ for a lower-triangular $L_1$ that zeroes the
first column of $A$ below its first entry; iterating over columns gives
$$L_{n-1}\cdots L_1 A x \equiv Ux = L_{n-1}\cdots L_1 b \equiv b^{*},$$
with $U$ upper triangular — the *forward reduction* — after which $Ux=b^{*}$ is a backsolve. If the
factorization itself is wanted, $L=(L_{n-1}\cdots L_1)^{-1}$ turns out to have a simple form (unit
lower triangular, entries the negatives of those in the $L_j$), computable on the fly and storable
in the same memory as $A$. The whole procedure is $O(n^3)$.

Dividing by a very small pivot is numerically dangerous — small errors in the divisor get amplified.
**Partial pivoting** avoids this by, at each step, swapping in whichever remaining row has the
largest entry in the current column to use as the divisor (the *pivot*); this can be expressed as
premultiplying by permutation matrices, giving $PA=LU$ for $P=P_{n-1}\cdots P_1$. (*Complete*
pivoting also permutes columns; it is theoretically better but rarely worth the extra cost over
partial pivoting.) One consequence: since $|PA|=|P||A|=|L||U|=|U|$ and $|L|=1$ (unit triangular), the
determinant is $|A|=|U|/|P|$, and $|P|=\pm 1$ depending on the parity of the number of row swaps —
so Gaussian elimination gives a fast, stable route to the determinant for free.

When would you actually want an explicit inverse, rather than a decomposition? Only when the inverse
itself is the desired output — for standard errors, say. If you only need $A^{-1}$ multiplied by
something, solving via a decomposition is always cheaper, regardless of how many columns you're
multiplying by.

### Cholesky

When $A$ is positive definite, it factors as $A=U^{\top}U$ for a unique upper-triangular $U$ with
positive diagonal (the sign convention that makes it unique) — a matrix "square root." One recursive
way to build $U$: $U_{11}=\sqrt{A_{11}}$; then $U_{1j}=A_{1j}/U_{11}$ across the first row; then for
each subsequent $i$, $U_{ii}=\sqrt{A_{ii}-\sum_{k<i}U_{ki}^2}$ and, for $j>i$,
$U_{ij}=(A_{ij}-\sum_{k<i}U_{ki}U_{kj})/U_{ii}$. A system solves as two triangular solves,
$U^{-1}(U^{-\top}b)$.

The Cholesky has two real advantages over the LU: both are $O(n^3)$, but Cholesky needs only about
$n^3/6$ operations against roughly double that for LU, and it has only $(n^2+n)/2$ distinct values
to store rather than $n^2+n$ — it exploits symmetry that the LU throws away. Its main use in
statistics is generating correlated normal draws: if $L=U^{\top}$ is the lower-triangular Cholesky
factor of $A$, then $L z$ for $z\sim N(0,I)$ is distributed $N(0,A)$.

Its numerical failure mode is instructive. If $A$ is severely ill-conditioned, the quantity
$A_{ii}-\sum_kU_{ki}^2$ inside a square root can come out numerically negative even though
mathematically $A$ is positive definite — the Cholesky decomposition exists in theory but not in
floating point. This is common with high-dimensional, highly-correlated covariance matrices, for
example a squared-exponential covariance kernel with a short length scale:

```python
locs = rng.uniform(size=100)
rho = 0.1
dists = np.abs(locs[:, np.newaxis] - locs)
C = np.exp(-dists**2 / rho**2)
np.linalg.cholesky(C)   # fails: not numerically positive definite,
                        # even though it is mathematically
```

Its eigenvalues, in this case, are spread across many orders of magnitude — the matrix is badly
conditioned, and the smallest eigenvalues are effectively swamped by floating-point error long
before the recursion gets to them. Even when the Cholesky *does* succeed, small eigenvalues near
machine precision can still produce unstable results wherever the inverse is used — the numerical
manifestation of near-collinearity among the underlying variables. The general remedy is the same
pseudo-inverse idea from the eigendecomposition section: truncate small eigenvalues (or singular
values) to zero rather than trying to invert them.

### QR

The **QR decomposition**, $X=QR$ with $Q$ orthogonal and $R$ upper triangular, exists for *any*
matrix, not just square ones. For $n\times p$ $X$ with $n>p$, only the leading $p$ rows of $R$ (and
$p$ columns of $Q$) are nonzero — the **skinny QR**, $X=Q_1R_1$, which is what standard software
returns. Fixing the sign convention that $R$'s diagonal is nonnegative makes $R$ literally the
upper-triangular Cholesky factor of $X^{\top}X$, since
$X^{\top}X = R^{\top}Q^{\top}QR = R^{\top}R$. The pseudo-inverse follows too:
$X^{+}=[R_1^{-1}\ 0]Q^{\top}$.

QR is central to regression. Writing the normal equations $X^{\top}X\beta = X^{\top}Y$ in terms of
the skinny QR,
$$R^{\top}Q^{\top}QR\beta = R^{\top}Q^{\top}Y \quad\Longrightarrow\quad R\beta = Q^{\top}Y,$$
so $\beta$ is recovered by a single backsolve, and standard regression quantities (fitted values,
SSE, residuals) all have clean expressions in $Q$ and $R$. Why use QR rather than forming $X^{\top}X$
and using Cholesky? Because the condition number of $X$ is the *square root* of the condition number
of $X^{\top}X$ — so factoring $X$ directly avoids squaring the numerical difficulty. In practice this
mostly matters exactly when OLS itself is already on shaky statistical ground (highly collinear
predictors); the computational-order comparison bears this out:

| Method | Operations | Notes |
|---|---|---|
| Cholesky on $X^{\top}X$ | $np^2 + \tfrac13p^3$ | fast when $n\gg p$ |
| Sweeping | $np^2 + p^3$ | least numerically stable |
| Householder QR | $2np^2 - \tfrac23p^3$ | |
| Modified Gram–Schmidt QR | $2np^2$ | most numerically stable |

so for $n\gg p$, Cholesky/sweeping are faster, but since regression cost is linear in $n$ regardless
of method, the difference rarely matters in practice.

**Computing the QR.** Three standard constructions:

- *Householder reflections.* For orthonormal $u,v$ and $x=c_1u+c_2v$, $\tilde x=-c_1u+c_2v$ reflects
  $x$ across the hyperplane perpendicular to $u$; this reflection is carried out by the matrix
  $Q=I-2uu^{\top}$, which satisfies $Qu=-u$, $Qv=v$ whenever $u^{\top}v=0$, and is both orthogonal
  and symmetric. Choosing $u$ so that $Q_1x = (\|x\|,0,\ldots,0)$ zeroes out everything below the
  first entry of the first column; repeating for later columns with successively smaller reflections
  builds $R=Q_p\cdots Q_1X$ and $Q=(Q_p\cdots Q_1)^{\top}$. (For numerical stability, the sign of
  $\tilde x$ at each step is chosen opposite to $x_1$, to avoid subtracting two near-equal numbers.)
  This costs $2n^3/3$ flops for square $X$ — more than LU or Cholesky.
- *Givens rotations.* A rotation in a two-dimensional subspace can zero a single entry of a vector;
  a sequence of such rotations zeroes the whole lower triangle. $Q$ here is orthogonal but not
  symmetric, and unless done carefully this needs more computation than Householder reflections.
- *(Modified) Gram–Schmidt.* Orthonormalize the columns of $X$ one at a time: normalize $x_1$, then
  remove the $\tilde x_1$-component from the remaining columns and normalize the next one, and so
  on. The resulting orthonormal vectors are the columns of $Q$; the diagonal entries of $R$ are the
  normalizing constants, and the off-diagonal entries are the inner products removed along the way
  — equivalently, $R=Q^{\top}X$ is "regressing the columns of $X$ on $Q$." The *modified* version
  (removing components against each already-computed column immediately, rather than against the
  raw original columns) is more stable when the columns of $X$ are nearly collinear.

**Large, thin $X$.** When $n$ is enormous and $n\gg p$, the **tall-skinny QR** finds the
decomposition by first QR-decomposing blocks of rows in parallel, then recursively QR-decomposing
pairs of the resulting $R$ factors, until a single $R$ remains.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A reduction tree that computes the QR decomposition of a tall matrix by recursively combining QR factors of row blocks">
  <defs>
    <marker id="arrow-qr" markerWidth="7" markerHeight="7" refX="5" refY="2.5" orient="auto">
      <polygon points="0 0, 6 2.5, 0 5" fill="currentColor"/>
    </marker>
  </defs>
  <g font-size="12" fill="currentColor" text-anchor="middle">
    <rect x="10" y="15" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="35" y="31">X0</text>
    <rect x="95" y="15" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="120" y="31">X1</text>
    <rect x="190" y="15" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="215" y="31">X2</text>
    <rect x="275" y="15" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="300" y="31">X3</text>

    <line x1="35" y1="39" x2="35" y2="60" stroke="currentColor" marker-end="url(#arrow-qr)"/>
    <line x1="120" y1="39" x2="120" y2="60" stroke="currentColor" marker-end="url(#arrow-qr)"/>
    <line x1="215" y1="39" x2="215" y2="60" stroke="currentColor" marker-end="url(#arrow-qr)"/>
    <line x1="300" y1="39" x2="300" y2="60" stroke="currentColor" marker-end="url(#arrow-qr)"/>
    <text x="170" y="55" font-size="11">QR of each row block, in parallel</text>

    <rect x="10" y="65" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="35" y="81">R0</text>
    <rect x="95" y="65" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="120" y="81">R1</text>
    <rect x="190" y="65" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="215" y="81">R2</text>
    <rect x="275" y="65" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="300" y="81">R3</text>

    <line x1="35" y1="89" x2="77" y2="115" stroke="currentColor" marker-end="url(#arrow-qr)"/>
    <line x1="120" y1="89" x2="77" y2="115" stroke="currentColor" marker-end="url(#arrow-qr)"/>
    <line x1="215" y1="89" x2="257" y2="115" stroke="currentColor" marker-end="url(#arrow-qr)"/>
    <line x1="300" y1="89" x2="257" y2="115" stroke="currentColor" marker-end="url(#arrow-qr)"/>

    <rect x="52" y="120" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="77" y="136">R01</text>
    <rect x="232" y="120" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="257" y="136">R23</text>
    <text x="167" y="115" font-size="11" text-anchor="middle">QR of pairs of Rs (reduction)</text>

    <line x1="77" y1="144" x2="167" y2="170" stroke="currentColor" marker-end="url(#arrow-qr)"/>
    <line x1="257" y1="144" x2="167" y2="170" stroke="currentColor" marker-end="url(#arrow-qr)"/>

    <rect x="142" y="175" width="50" height="24" fill="none" stroke="currentColor"/>
    <text x="167" y="191">R</text>
  </g>
</svg>
<figcaption>The tall-skinny QR: rows of a very large, thin $X$ are QR-factored in parallel blocks,
and the resulting $R$ factors are combined pairwise (each combination itself a small QR) until a
single overall $R$ remains. The full $Q$ is never formed explicitly for a problem this size — it
stays represented by its constituent pieces.</figcaption>
</figure>

A serial variant handles the case where $X$ doesn't fit in memory at all: QR-factor $X_0$ to get
$R_0$; stack $R_0$ on top of $X_1$ and QR-factor that to get $R_{01}$; stack that on top of $X_2$,
and so on.

### Determinants, in general

The determinant of a square matrix, up to sign, is always the product of the diagonal of whatever
triangular (or diagonal) factor a decomposition produces, since orthogonal factors contribute only
$\pm 1$: $|A|=|QR|=|Q||R|=\pm|R|$, or, via the SVD $A=UDV^{\top}$, the product of the singular
values. For positive (semi-)definite matrices the sign ambiguity disappears — the determinant is
non-negative — and the Cholesky diagonal gives it directly; equivalently, it is the product of the
eigenvalues, $|A|=|\Gamma\Lambda\Gamma^{-1}|=|\Lambda|$. Whichever route is used, computing a
determinant as a raw product of diagonal entries risks overflow or underflow, so it is **always**
computed on the log scale, as a sum of logs (tracking the sign, or the count of negative factors,
separately if needed). Since a factorization is often already available from elsewhere in the
computation, the determinant frequently comes for free.

## Eigendecomposition and SVD: computing them

The **spectral radius** $\rho(A)$, the largest eigenvalue magnitude, satisfies $\rho(A)\leq\|A\|$
for any induced norm, with equality to the induced 2-norm when $A$ is symmetric; it governs the
convergence rate of several iterative algorithms encountered elsewhere in this chapter.

**Computing a full eigendecomposition** is usually done by the *QR algorithm*: first reduce $A$ to
upper Hessenberg form (triangular except for one nonzero sub-diagonal; tridiagonal, if $A$ is
symmetric) using Householder or Givens transformations, then repeatedly apply the QR decomposition
to a shifted version of the matrix. The iterates converge to a diagonal matrix of eigenvalues; the
eigenvectors come out as the accumulated product of the Householder matrices from the initial
reduction and the $Q$ matrices from each QR step.

When only the largest eigenvalue (and its eigenvector) is needed — as in finding the steady state of
a Markov chain, $x_t = A^tx_0$ — the much cheaper **power method** suffices: iterate
$v^{(k)}=Az^{(k-1)}$, $z^{(k)}=v^{(k)}/\|v^{(k)}\|$, and $z^{(k)}$ converges to the dominant
eigenvector. To get the next-largest eigenvalue, *deflate*: form $B = A - \lambda_1 z_1z_1^{\top}$
(removing the dominant component) and apply the power method again to $B$.

**The SVD.** For an $n\times m$ matrix $A$ with $n\geq m$ (transpose first if not — think rows as
observations, columns as features: $n$ documents and $m$ words, or $n$ samples and $m$ measured
conditions), the singular value decomposition writes
$$A = UDV^{\top} = \sum_{j=1}^{k} D_{jj}\,u_jv_j^{\top},$$
with $U,V$ having orthonormal columns, $D$ diagonal and non-negative, and $k$ the rank of $A$ — a
sum of $k$ rank-one pieces. If $A$ is positive semi-definite, its eigendecomposition *is* an SVD;
more generally $A^{\top}A=VD^2V^{\top}$ and $AA^{\top}=UD^2U^{\top}$, so singular values of $A$ are
square roots of eigenvalues of $A^{\top}A$ (and of $AA^{\top}$).

The SVD is the standard route to a matrix's rank and to its pseudo-inverse,
$A^{+}=VD^{+}U^{\top}$. It is also the standard route to **low-rank approximation**: truncating the
sum after $p<k$ terms, $\tilde A = \sum_{j\leq p} D_{jj}u_jv_j^{\top}$, gives the best possible
rank-$p$ approximation to $A$ in Frobenius norm (the Eckart–Young theorem) — the basis for image
compression by keeping only the largest singular components, and for the SVD-based methods behind,
among other things, the winning entries in the Netflix Prize. A useful way to think about what
applying the SVD to a vector actually does: $V^{\top}x$ re-expresses $x$ as weights on the columns of
$V$; multiplying by $D$ rescales those weights; multiplying by $U$ turns the rescaled weights back
into a vector, now expressed in the column space of $U$. The SVD is, in this sense, a change of
basis, a stretch, and a second change of basis.

**Computing the SVD** (the Golub–Reinsch algorithm) mirrors the QR algorithm for eigenvalues:
Householder transformations on both sides reduce $A$ to upper bidiagonal form, and a sequence of
Givens-transformation sweeps then drives it to diagonal, with $U$ and $V$ accumulated as the products
of the transformations applied on each side; a final adjustment fixes signs and sorts the singular
values in decreasing order. For a tall, thin $X$ (large $n$, modest $p$), it is far cheaper to first
compute $X=QR$ and then take the SVD of the small $p\times p$ matrix $R=UDV^{\top}$, giving
$X = QU\,D\,V^{\top}$.

## Making it fast: libraries and structure

Matrix operations in Python and R mostly drop straight into compiled C or Fortran, via two core
libraries: **BLAS** (Basic Linear Algebra Subroutines: vector operations at level 1, matrix-vector
at level 2, dense matrix-matrix at level 3) and **LAPACK**, which builds on BLAS to implement
eigendecompositions, linear-system solves, and the various factorizations above. Which *implementation*
of BLAS you're linked against — OpenBLAS, Intel's MKL, AMD's ACML, Apple's vecLib (which on Apple
Silicon uses the AMX co-processor) — can make a large difference to speed, since these are tuned,
often multi-threaded, implementations of the same routines. (Conda-installed numpy is typically
linked against MKL or OpenBLAS; pip-installed numpy typically against OpenBLAS.) Packages such as
JAX and PyTorch offer an alternative linear-algebra layer that can additionally target a GPU
automatically when one is available, and (for JAX) offer just-in-time compilation on top.

**Exploiting known structure.** A symmetric matrix can be stored as only its upper or lower triangle;
banded and block-diagonal matrices are other common special cases. A **banded** matrix with lower
bandwidth $p$ and upper bandwidth $q$ ($A_{ij}=0$ once $i>j+p$ or $j>i+q$) admits an LU factorization
in $O(npq)$ and triangular solves in $O(np+nq)$ — dramatically cheaper than the dense $O(n^3)$ and
$O(n^2)$ when $p,q$ are small. Banded covariance structures arise naturally from moving-average time
series models, where correlation vanishes beyond a fixed lag.

For genuinely **sparse** matrices, a standard storage scheme is compressed sparse row (CSR): store
the non-zero entries in row-major order in one array, `data`; a second array, `indptr`, gives the
position in `data` where each row starts; a third, `indices`, gives the column of each entry:

```python
mat = sparse.csr_array(mat)   # from a dense array
mat.data      # non-zero entries
mat.indices   # column indices
mat.indptr    # row pointers
```

A sparse matrix-vector product $x=Ab$ then costs only $O(k)$ multiplies and additions, where $k$ is
the number of non-zero entries — compare the dense $O(n^2)$. If a matrix's sparsity *pattern* is
fixed but its entries change repeatedly (as in an iterative fitting procedure), the optimal
fill-reducing reordering for a sparse Cholesky can be computed once and reused across factorizations.
R's `Matrix`, `spam`, and `bdsmatrix` packages provide analogous structured representations
(`spam` in particular for general sparse matrices with a fast sparse Cholesky, `bdsmatrix` for
block-diagonal matrices arising from clustered/independent-across-cluster data).

**Low-rank updates.** A rank-one update of $A$ is $A - uv^{\top}$; more generally, for $U,V$ of size
$n\times m$ ($m\leq n$), the **Sherman–Morrison–Woodbury** identity gives the inverse of the updated
matrix $\tilde A = A - UV^{\top}$ directly from the inverse of $A$:
$$\tilde A^{-1} = A^{-1} + A^{-1}U\left(I_m - V^{\top}A^{-1}U\right)^{-1}V^{\top}A^{-1}.$$
If $x_0=A^{-1}b$ is already known, the solution to $\tilde Ax=b$ follows from one $m\times m$ inverse
rather than a fresh $n\times n$ solve — cheap provided $m$ is modest. An equivalent form, for
$\tilde A = A+UCV^{\top}$,
$$\tilde A^{-1} = A^{-1} - A^{-1}U\left(C^{-1}+V^{\top}A^{-1}U\right)^{-1}V^{\top}A^{-1},$$
is useful in Bayesian settings where a *precision* matrix $A^{-1}$ is available directly (e.g. from
combining independent sources of precision) but $A$ itself is not.

## Iterative methods (optional)

Direct methods (LU, Cholesky, QR) find an exact answer in a fixed number of steps. **Iterative**
methods instead generate a sequence of approximations, and can save computation when they are
stopped well before converging exactly — useful for very large or very sparse systems where a full
factorization is too expensive.

**Gauss–Seidel** updates one coordinate of $x$ at a time: starting from $x^{(0)}$, hold everything
but $x_1$ fixed and solve for it exactly, $x_1^{(1)} = \frac{1}{a_{11}}\left(b_1 - \sum_{j\geq
2}a_{1j}x_j^{(0)}\right)$; repeat across the remaining coordinates to get $x^{(1)}$, then iterate to
$x^{(2)},x^{(3)},\ldots$ until, say, $\|x^{(k)}-x^{(k-1)}\|\leq\epsilon$. Each full update is
$O(n^2)$: $O(n)$ per coordinate. Writing $A=L+D+U$ (strictly lower, diagonal, strictly upper), one
sweep of Gauss–Seidel is equivalent to solving the lower-triangular system
$(L+D)x^{(k+1)} = b - Ux^{(k)}$, itself $O(n^2)$; its rate of convergence is governed by the spectral
radius of $(L+D)^{-1}U$. Because it moves one axis-aligned coordinate at a time, it can converge
slowly.

**Conjugate gradient (CG)**, for positive definite $A$, instead reframes solving $Ax=b$ as minimizing
the quadratic $f(x) = \tfrac12x^{\top}Ax - x^{\top}b$, whose gradient is $Ax-b$ — zero exactly at the
solution. Rather than following the gradient directly at each step (steepest descent, which can
converge slowly by zig-zagging), CG moves along a sequence of directions $d_k$ that are mutually
*conjugate* with respect to $A$ ($d_i^{\top}Ad_j=0$ for $i\neq j$), chosen to equal the successive
residuals $r_{(k)}=b-Ax_{(k)}$ after removing components not $A$-orthogonal to earlier directions.
Concretely, starting from $x_{(0)}$ with $r_{(0)}=d_0=b-Ax_{(0)}$, each step computes
$$\alpha_k = \frac{r_{(k)}^{\top}r_{(k)}}{d_k^{\top}Ad_k}, \qquad x_{(k+1)}=x_{(k)}+\alpha_kd_k,
\qquad r_{(k+1)}=r_{(k)}-\alpha_kAd_k,$$
$$d_{k+1} = r_{(k+1)} + \frac{r_{(k+1)}^{\top}r_{(k+1)}}{r_{(k)}^{\top}r_{(k)}}\,d_k,$$
stopping once $\|r^{(k+1)}\|$ is small enough. In principle CG reaches the exact solution in $n$
steps for $n\times n$ $A$, but in practice accuracy is lost along the way, so it is used as a
genuinely iterative method, stopped well short of $n$ steps — the convergence rate improves as the
condition number of $A$ shrinks (eigenvalues less spread out). CG is the standard tool for large,
sparse, positive-definite systems.

**Updating a solution.** If you have already solved $Ax=b$ via a factorization and later need to
solve $Ax=c$ for the *same* $A$, reuse the factorization: the new solve costs only $O(n^2)$ rather
than a fresh $O(n^3)$. If instead $c=b+\delta b$ for a small perturbation $\delta b$, an iterative
method warm-started from the old solution $x$ (as $x^{(0)}$) can converge very quickly.

## Exercises

These are the questions and challenges posed alongside the material above; none are answered here.

1. Solving an upper-triangular system by backsolve takes how many multiplies and how many adds, as
   a function of $n$? (Solving a lower-triangular system is essentially the same count — check why.)
2. In the matrix-multiply pseudocode that accumulates $b=Ax$ either by rows or by columns, both use
   the same number of arithmetic operations but access memory differently. Time both approaches in
   Python, writing the outer loop explicitly and the inner loop as a vectorized operation. Does the
   faster approach depend on how large the matrices are?
3. For the autoregressive precision-matrix example, work out: what does it mean, statistically, for
   one of its eigenvalues to be exactly zero? What changes if a very small (but nonzero) eigenvalue
   is rounded to zero before inverting? And for a precision matrix generally, what does it mean for
   one of the entries of $\Lambda^{-1}$ to be very large, or very small?
4. Show that the hat matrix $H=X(X^{\top}X)^{-1}X^{\top}$ is singular in general. Under what special
   circumstance is it *not* singular?
5. Find $\mathrm{tr}(AB)$ without ever explicitly forming the matrix product $AB$.
6. Generating $y\sim N(0,A)$ via $y = Lz$ (with $L$ the Cholesky factor of $A$ and $z$ standard
   normal) is a two-step calculation. Where does most of the computational cost fall — computing
   $L$, or computing $Lz$? What does that imply about generating many draws from the same $A$?
7. Write efficient code to compute the GLS estimator $\hat\beta = (X^{\top}\Sigma^{-1}X)^{-1}X^{\top}\Sigma^{-1}Y$
   using a Cholesky factorization of $\Sigma$, rather than forming $\Sigma^{-1}$ explicitly.

## Sources

All material is from the Numerical Linear Algebra unit (Unit 10) of UC Berkeley's STAT 243
(Introduction to Statistical Computing), as taught by Christopher Paciorek. The fall-2024 and
fall-2025 offerings are essentially identical in content; fall-2025 was used as the primary source,
split by the course into seven parts:

- **Notation, norms, orthogonality, and the key computational principle** —
  `statistical-computing/berkeley/stat243/fall-2025/units/unit10-linalg/01-1-preliminaries.md`
  ("1. Preliminaries").
- **Rank, invertibility, generalized inverses, and the regression connection** —
  `.../02-2-statistical-interpretations-of-matrix-invertibility-rank-e.md`
  ("2. Statistical interpretations of matrix invertibility, rank, etc.").
- **Ill-conditioning** — `.../03-3-computational-issues.md` ("3. Computational issues").
- **LU, Cholesky, QR, and determinants** — `.../04-4-matrix-factorizations-decompositions-and-solving-systems-o.md`
  ("4. Matrix factorizations..."). Note: the converted markdown for this section is missing its
  entire LU/Gaussian-elimination and Cholesky subsections (roughly lines 46–166 of the converted
  file), apparently lost during `.qmd`-to-markdown conversion; that material was recovered directly
  from the raw source, `sources/berkeley-stat243/fall-2025/units/unit10-linalg.qmd` (lines
  941–1167), and is reproduced faithfully above.
- **Eigendecomposition and SVD** — `.../05-5-eigendecomposition-and-svd.md`.
- **BLAS/LAPACK, GPUs, sparse and banded structure, low-rank updates** — `.../06-6-computation.md`.
- **Gauss–Seidel, conjugate gradient, and updating a solution** —
  `.../07-7-iterative-solutions-of-linear-systems-optional.md` ("7. Iterative solutions of linear
  systems (optional)").

The stat243-fall-2021 offering of the same unit
(`statistical-computing/berkeley/stat243/stat243-fall-2021/units/unit10-linalg/`) covers the same
early material at lower fidelity (an unverified model reconstruction of a PDF with no text layer,
and truncated after section 2) and was checked for continuity only; it contributed no content not
already in the fall-2025 version.

Referred to but not supplied, and so not reproduced here: the course's cited textbooks (Gentle,
*Numerical Linear Algebra for Applications in Statistics*; Gentle, *Computational Statistics*;
Lange, *Numerical Analysis for Statisticians*; Monahan, *Numerical Methods of Statistics*), a set of
2020 lecture videos referenced as optional viewing in the bCourses media gallery, Golub and Van
Loan (1996) for an algorithm to estimate the condition number, an SCF documentation page on linear
algebra and parallelized BLAS, an SCF parallelization tutorial with worked PyTorch/JAX examples, and
Shewchuk's "An Introduction to the Conjugate Gradient Method Without the Agonizing Pain."

---

[← 36. Unix, Version Control, and Editors](36-unix-version-control-and-editors.md) · [Contents](index.md) · [38. Numerical Optimization for Statistics →](38-numerical-optimization-for-statistics.md)
