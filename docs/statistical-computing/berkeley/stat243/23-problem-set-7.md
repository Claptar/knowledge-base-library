---
title: "23. Problem Set 7"
course: "Berkeley Stat 243 Fall 2024"
chapter: 23
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 23. Problem Set 7

## What this covers

This chapter collects Problem Set 7 of Stat 243 (Statistical Computing for Statistics and Data
Science), as assigned in the Fall 2024 and Fall 2025 offerings of the course. Both versions are
built on Unit 10's central lesson about solving linear systems — factor the matrix, then solve by
back- and forward-substitution, rather than form an explicit matrix inverse — and both ask for an
operation count and a timing experiment that verify it, then a real statistical computation that
depends on doing it right. The two offerings ask genuinely different questions rather than variants
of the same one, so they are given as two separate problem sets below. This chapter assumes the
reader already has Unit 10's lecture material: the LU decomposition (Gaussian elimination) and its
$n^3/3$ operation count for solving $Ax=b$, back- and forward-substitution for triangular systems,
the Cholesky decomposition for symmetric positive definite matrices, matrix condition numbers and
the induced $2$-norm, and the storage and manipulation of sparse matrices — none of which is
reproduced here.

## How the assignment is shaped

Both offerings pair an operation-counting exercise with a timing experiment and a real application
that hinges on the same principle: don't invert. Fall 2024 counts the cost of explicit matrix
inversion against the direct LU solve, then applies the lesson twice — to the generalized least
squares estimator, and to a two-stage least squares calculation so large that even multiplying two
sparse matrices together is not an option. Fall 2025 instead counts the exact operation cost of the
Cholesky decomposition, times inversion against `solve` against Cholesky (including how each scales
with the number of cores under a parallel BLAS), and applies the same principle to a constrained
least-squares (quadratic programming) estimator whose closed form is riddled with inverses that
should never actually be computed as such.

## Exercises

### Fall 2024

1. **Counting the cost of explicit inversion.** Gaussian elimination (the LU decomposition) solves
   $Ax=b$ in $n^3/3$ operations, ignoring lower-order terms. Suppose instead you invert $A$
   explicitly and then multiply, i.e. compute $x=A^{-1}b$ by matrix-vector multiplication. This is
   essentially what `numpy.linalg.inv` does: it solves $AZ=I$ for $Z=A^{-1}$ using LAPACK's `DGESV`
   routine, itself built on the LU decomposition. Count the number of computations for

   a. transforming $AZ=I$ into $UZ=I^{*}$, where $I^{*}$ is no longer diagonal;
   b. solving for $Z$ given $UZ=I^{*}$; and
   c. computing $x=Zb$.

   Then compare the total to the $n^3/3$ cost of solving $Ax=b$ directly. You should be able to
   reuse the operation counts already derived in class for Gaussian elimination and for a
   backsolve, without any new detailed derivation. Since `dgesv` does not exploit the special
   (diagonal) structure of $I$ on the right-hand side, you may count as though $I$ were filled with
   arbitrary values — accounting for that structure properly would in fact save a further $n^3/3$
   operations.

2. **Generalized least squares, efficiently.** The generalized least squares (GLS) estimator is
   $$\hat\beta=(X^{\top}\Sigma^{-1}X)^{-1}X^{\top}\Sigma^{-1}Y,$$
   where $X$ is $n\times p$, $\Sigma$ is a positive definite $n\times n$ matrix, $n>p$, $n$ is of
   order several thousand, and $p$ is of order hundreds.

   a. Write pseudocode for computing $\hat\beta$ efficiently — the specific linear algebra steps
      and their order — then implement it as a Python function `gls()`. You may rely on high-level
      decomposition and linear-solve routines, but not on any existing implementation of
      generalized least squares. (Note that numpy's and scipy's Cholesky routines do not return the
      factor in the same form.)
   b. Compare the timing of this approach against computing $\hat\beta$ directly with the inverse
      (computing the inverse only once, and otherwise using an efficient order of operations). Is
      the comparison consistent with Question 1 and with the efficiency results from Unit 10? For
      simplicity, construct a positive definite test matrix as $\Sigma=W^{\top}W$ for a randomly
      generated $n\times n$ matrix $W$ (in a real problem $\Sigma$ would come from the context), and
      generate $X$ and $Y$ randomly too.
   c. Do the two approaches agree numerically for $\hat\beta$, up to machine precision? Comment on
      how many digits of $\hat\beta$ agree between them, and relate this to the condition number of
      the calculation.

3. **Two-stage least squares on a huge sparse problem.** Two-stage least squares (2SLS) implements
   the instrumental-variables method used in economics via
   $$\hat X = Z(Z^{\top}Z)^{-1}Z^{\top}X, \qquad \hat\beta=(\hat X^{\top}\hat X)^{-1}\hat X^{\top}Y,$$
   which can be read as regressing $Y$ on $X$ after filtering $X$ down to the variation correlated
   with the instrumental variable $Z$. Suppose $Z$ is $60$ million by $630$, $X$ is $60$ million by
   $600$, and $Y$ is $60$ million by $1$, and both $Z$ and $X$ are sparse.

   a. Explain briefly why $\hat\beta$ cannot be computed in the two literal steps given above, even
      applying the OLS techniques discussed in class to each stage.
   b. Rewrite the calculation so that $\hat\beta$ can actually be computed on a computer without
      using a huge amount of memory, assuming that sparse matrix multiplications can be carried out
      (e.g. via `scipy.sparse`). Describe the specific steps, in pseudocode if useful.

   The product of two sparse matrices is not, in general, sparse — and would not be here — so the
   rewriting has to route around ever forming such a product.

4. **(Extra credit) The induced $2$-norm of a symmetric matrix.** The condition number of $Ax=b$ is
   the ratio of the largest to the smallest eigenvalue magnitude of $A$. Show that for symmetric
   $A$, the matrix norm induced by the usual $L_2$ vector norm,
   $$\|A\|_{2}=\sup_{z:\|z\|_{2}=1}\sqrt{(Az)^{\top}Az},$$
   is the largest eigenvalue magnitude of $A$. (Read "sup" as "max" if the supremum is unfamiliar —
   it is the natural extension of "maximum" to a case such as the open interval $(0,1)$, which has
   no maximum but has supremum $1$.) Hint: once you reach an expression involving $\Gamma^{\top}z$
   for an orthogonal matrix $\Gamma$, set $y=\Gamma^{\top}z$ and show that $\|z\|_{2}=1$ forces
   $\|y\|_{2}=1$. Then, given an expression $y^{\top}Dy$ for diagonal $D$, work out how it can be
   rewritten and how to maximize it subject to $\|y\|_{2}=1$.

### Fall 2025

1. **Counting the cost of the Cholesky decomposition.** Work out the exact operation count for the
   Cholesky decomposition of a symmetric positive definite matrix — total multiplications plus
   divisions, including the constant, for every term of order $n^3$ or $n^2$ (e.g. $5n^{3}/2+8n^{2}$,
   not $O(n^{3})$). Ignore square roots, additions and subtractions, and ignore pivoting. Don't
   count any step that multiplies by $0$ or $1$. Compare your count to the one given in the lecture
   notes.

2. **Timing inversion, `solve`, and Cholesky against each other.** Compare the speed of computing
   $x=A^{-1}b$ three ways: (i) `np.linalg.inv(A) @ b`; (ii) `np.linalg.solve(A, b)`; and (iii) a
   Cholesky decomposition followed by solving the resulting triangular systems. Construct a
   positive definite test matrix as $A=W^{\top}W$ for a randomly generated $n\times n$ matrix $W$
   (positive definiteness is needed for the Cholesky approach and is a stricter, and here more
   convenient, condition than mere invertibility for the other two).

   a. Using a single thread and $n=5000$, how do the timings and their relative ordering compare to
      the operation counts discussed in class and in the notes? (For reference, inverting via the
      LU decomposition costs $4n^{3}/3$.)
   b. How does the timing of each of the three approaches scale with the number of cores (threads),
      using a parallelized BLAS? This may require using the SCF cluster to guarantee a parallel
      BLAS is actually in use.
   c. Do methods (ii) and (iii) agree numerically for the solution $x$, up to machine precision?
      Comment on how many digits agree, and relate this to the condition number of the calculation —
      a value of $n$ well below $5000$ is enough for estimating the condition number itself.

3. **A constrained least squares problem.** Minimizing $(Y-X\beta)^{\top}(Y-X\beta)$ over $\beta$
   subject to $m$ linear equality constraints $A\beta=b$ (an $m\times p$ matrix $A$, each row a
   constraint that a linear combination of $\beta$ must equal the corresponding element of $b$) is
   an instance of quadratic programming. A Lagrange-multiplier derivation (covered later, in
   Unit 11) gives
   $$\hat\beta=C^{-1}d+C^{-1}A^{\top}(AC^{-1}A^{\top})^{-1}(-AC^{-1}d+b),$$
   where $C=X^{\top}X$, $d=X^{\top}Y$, and $X$ is $n\times p$.

   a. Sketch, in pseudocode, how you would implement this computation, applying the principles
      about matrix inverses and factorizations discussed in class.
   b. Write a Python function that computes $\hat\beta$ efficiently, using numpy's or scipy's
      matrix factorization and solving routines. (In practice this efficiency mainly matters when
      $p$, the number of regression coefficients, is large.)

## Sources

- `docs/statistical-computing/berkeley/stat243/fall-2024/ps/ps7.md` — converted losslessly from
  [`ps/ps7.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/ps/ps7.qmd)
  in the berkeley-stat243 fall-2024 repository, CC BY 4.0. Problems 1–4 (problem 4 extra credit).
- `docs/statistical-computing/berkeley/stat243/fall-2025/ps/ps7.md` — converted losslessly from
  [`ps/ps7.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/ps/ps7.qmd)
  in the berkeley-stat243 fall-2025 repository, CC BY 4.0. Problems 1–3.
- Referred to but not contained in either file: the course's Unit 10 lecture notes on Gaussian
  elimination/LU decomposition operation counts, the Cholesky decomposition, condition numbers and
  matrix norms, and sparse matrix storage and manipulation (`scipy.sparse`), which both problem sets
  assume throughout; Unit 11's Lagrange-multiplier treatment, referenced as the source of the
  constrained-least-squares formula in the Fall 2025 problem 3; Unit 6, Section 5, on the SCF
  cluster and parallel BLAS, referenced in the Fall 2025 problem 2b; and Problem Set 1, for the
  formatting and attribution requirements both offerings point back to.

---

[← 22. Floating-Point Precision and Importance Sampling](22-floating-point-precision-and-importance-sampling.md) · [Contents](index.md) · [24. Problem Set 8 →](24-problem-set-8.md)
