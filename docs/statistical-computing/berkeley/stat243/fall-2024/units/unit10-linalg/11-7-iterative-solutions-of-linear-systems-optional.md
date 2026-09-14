---
title: 7. Iterative solutions of linear systems (optional)
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit10-linalg.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 7. Iterative solutions of linear systems (optional)

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit10-linalg.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

#### Gauss-Seidel

Suppose we want to iteratively solve $Ax=b$. Here's the algorithm, which
sequentially updates each element of $x$ in turn.

-   Start with an initial approximation, $x^{(0)}$.
-   Hold all but $x_{1}^{(0)}$ constant and solve to find
    $x_{1}^{(1)}=\frac{1}{a_{11}}(b_{1}-\sum_{j=2}^{n}a_{1j}x_{j}^{(0)})$.
-   Repeat for the other rows of $A$ (i.e., the other elements of $x$),
    finding $x^{(1)}$.
-   Now iterate to get $x^{(2)}$, $x^{(3)}$, etc. until a convergence
    criterion is achieved, such as $\|x^{(k)}-x^{(k-1)}\|\leq\epsilon$
    or $\|r^{(k)}-r^{(k-1)}\|\leq\epsilon$ for $r^{(k)}=b-Ax^{(k)}$.

Let's consider how many operations are involved in a single update:
$O(n)$ for each element, so $O(n^{2})$ for each update. Thus if we can
stop well before $n$ iterations, we've saved computation relative to
exact methods.

If we decompose $A=L+D+U$ where $L$ is strictly lower triangular, $U$ is
strictly upper triangular, then Gauss-Seidel is equivalent to solving
$$(L+D)x^{(k+1)}=b-Ux^{(k)}$$ and we know that solving the lower
triangular system is $O(n^{2})$.

It turns out that the rate of convergence depends on the spectral radius
of $(L+D)^{-1}U$.

Gauss-Seidel amounts to optimizing by moving in axis-oriented
directions, so it can be slow in some cases.

#### Conjugate gradient

For positive definite $A$, conjugate gradient (CG) reexpresses the
solution to $Ax=b$ as an optimization problem, minimizing
$$f(x)=\frac{1}{2}x^{\top}Ax-x^{\top}b,$$ since the derivative of $f(x)$
is $Ax-b$ and at the minimum this gives $Ax-b=0$.

Instead of finding the minimum by following the gradient at each step
(so-called steepest descent, which can give slow convergence - we'll see
a demonstration of this in the optimization unit), CG chooses directions
that are mutually conjugate w.r.t. $A$, $d_{i}^{\top}Ad_{j}=0$ for
$i\ne j$. The method successively chooses vectors giving the direction,
$d_{k}$, in which to move down towards the minimum and a scaling of how
much to move, $\alpha_{k}$. If we start at $x_{(0)}$, the $k$th point we
move to is $x_{(k)}=x_{(k-1)}+\alpha_{k}d_{k}$ so we have
$$x_{(k)}=x_{(0)}+\sum_{j\leq k}\alpha_{j}d_{j}$$ and we use a
convergence criterion such as given above for Gauss-Seidel. The
directions are chosen to be the residuals, $b-Ax_{(k)}$. Here's the
basic algorithm:

-   Choose $x_{(0)}$ and define the residual, $r_{(0)}=b-Ax_{(0)}$ (the
    error on the scale of $b$) and the direction, $d_{0}=r_{(0)}$ and
    set $k=0$.

-   Then iterate:

    -   $\alpha_{k}=\frac{r_{(k)}^{\top}r_{(k)}}{d_{k}^{\top}Ad_{k}}$
        (choose step size so next error will be orthogonal to current
        direction - which we can express in terms of the residual, which
        is easily computable)

    -   $x_{(k+1)}=x_{(k)}+\alpha_{k}d_{k}$ (update current value)

    -   $r_{(k+1)}=r_{(k)}-\alpha_{k}Ad_{k}$ (update current residual)

    -   $d_{k+1}=r_{(k+1)}+\frac{r_{(k+1)}^{\top}r_{(k+1)}}{r_{(k)}^{\top}r_{(k)}}d_{k}$
        (choose next direction by conjugate Gram-Schmidt, starting with
        $r_{(k+1)}$ and removing components that are not $A$-orthogonal
        to previous directions, but it turns out that $r_{(k+1)}$ is
        already $A$-orthogonal to all but $d_{k}$).

-   Stop when $\|r^{(k+1)}\|$ is sufficiently small.

The convergence of the algorithm depends in a complicated way on the
eigenvalues, but in general convergence is faster when the condition
number is smaller (the eigenvalues are not too spread out). CG will in
principle give the exact answer in $n$ steps (where $A$ is $n\times n$).
However, computationally we lose accuracy and interest in the algorithm
is really as an iterative approximation where we stop before $n$ steps.
The approach basically amounts to moving in axis-oriented directions in
a space stretched by $A$.

In general, CG is used for large sparse systems.

See the [extensive description from
Shewchuk](http://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf)
for more details, as well as the use
of CG when $A$ is not positive definite.

#### Updating a solution

Sometimes we have solved a system, $Ax=b$ and then need to solve $Ax=c$.
If we have solved the initial system using a factorization, we can reuse
that factorization and solve the new system in $O(n^{2})$. Iterative
approaches can do a nice job if $c=b+\delta b$. Start with the solution
$x$ for $Ax=b$ as $x^{(0)}$ and use one of the methods above.

---

[← 6. Computation](10-6-computation.md) · [Up: contents](index.md)
