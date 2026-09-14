---
title: 8. Convexity
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 8. Convexity

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Many optimization problems involve (or can be transformed into) convex
functions. Convex optimization (also called convex programming) is a big
topic and one that we'll only brush the surface of in Sections 8 and 9.
The goal here is to give you enough of a sense of the topic that you
know when you're working on a problem that might involve convex
optimization, in which case you'll need to go learn more.

Optimization for convex functions is simpler than for ordinary functions
because we don't have to worry about local optima - any stationary point
(point where the gradient is zero) is a global minimum. A set $S$ in
$\Re^{p}$ is convex if any line segment between two points in $S$ lies
entirely within $S$. More generally, $S$ is convex if any convex
combination is itself in $S$, i.e., $\sum_{i=1}^{m}\alpha_{i}x_{i}\in S$
for non-negative weights, $\alpha_{i}$, that sum to 1. Convex functions
are defined on convex sets - $f$ is convex if for points in a convex
set, $x_{i}\in S$, we have
$f(\sum_{i=1}^{m}\alpha_{i}x_{i})\leq\sum_{i=1}^{m}\alpha_{i}f(x_{i})$.
Strict convexity is when the inequality is strict (no equality).

The first-order convexity condition relates a convex function to its
first derivative: $f$ is convex if and only if
$f(x)\geq f(y)+\nabla f(y)^{\top}(x-y)$ for $y$ and $x$ in the domain of
$f$. We can interpret this as saying that the first order Taylor
approximation to $f$ is tangent to and below (or touching) the function
at all points.

The second-order convexity condition is that a function is convex if
(provided its first derivative exists), the derivative is
non-decreasing, in which case we have
$f^{\prime\prime}(x)\geq0\,\,\forall x$ (for univariate functions). If
we have $f^{\prime\prime}(x)\leq0\,\,\forall x$ (a concave, or convex
down function) we can always consider $-f(x)$, which is convex.
Convexity in multiple dimensions means that the gradient is
nondecreasing in all dimensions. If $f$ is twice differentiable, then if
the Hessian is positive semi-definite, $f$ is convex.

There are a variety of results that allow us to recognize and construct
convex functions based on knowing what operations create and preserve
convexity. The Boyd book is a good source for material on such
operations. Note that norms are convex functions (based on the triangle
inequality),
$\|\sum_{i=1}^{n}\alpha_{i}x_{i}\|\leq\sum_{i=1}^{n}\alpha_{i}\|x_{i}\|$.

We'll talk about a general algorithm that works for convex functions
(the MM algorithm) and about the EM algorithm that is well-known in
statistics, and is a special case of MM.

## MM algorithm

The MM algorithm is really more of a principle for constructing problem
specific algorithms. MM stands for majorize-minorize. We'll use the
majorize part of it to minimize functions - the minorize part is the
counterpart for maximizing functions.

Suppose we want to minimize a convex function, $f(x)$. The idea is to
construct a majorizing function, at $x_{t}$, which we'll call $g$. $g$
majorizes $f$ at $x_{t}$ if $f(x_{t})=g(x_{t})$ and
$f(x)\leq g(x)\forall x$.

The iterative algorithm is as follows. Given $x_{t}$, construct a
majorizing function $g_{t}(x).$ Then minimize $g_{t}$ w.r.t. $x$ (or at
least move downhill, such as with a modified Newton step) to find
$x_{t+1}$. Then we iterate, finding the next majorizing function,
$g_{t+1}(x)$. The algorithm is obviously guaranteed to go downhill, and
ideally we use a function $g$ that is easy to work with (i.e., to
minimize or go downhill with respect to). Note that we haven't done any
matrix inversions or computed any derivatives of $f$. Furthermore, the
algorithm is numerically stable - it does not over- or undershoot the
optimum. The downside is that convergence can be quite slow.

The tricky part is finding a good majorizing function. Basically one
needs to gain some skill in working with inequalities. The Lange book
has some discussion of this.

An example is for estimating regression coefficients for median
regression (aka least absolute deviation regression), which minimizes
$f(\theta)=\sum_{i=1}^{n}|y_{i}-z_{i}^{\top}\theta|=\sum_{i=1}^{n}|r_{i}(\theta)|$.
Note that $f(\theta)$ is convex because affine functions (in this case
$y_{i}-z_{i}^{\top}\theta$) are convex, convex functions of affine
functions are convex, and the summation preserves the convexity. We want
to minimize $$\begin{aligned}
f(\theta) & = \sum_{i=1}^{n}|r_{i}(\theta)|\\
 & = \sum_{i=1}^{n}\sqrt{r_{i}(\theta)^{2}}\end{aligned}$$

Next, $h(x)=\sqrt{x}$ is concave, so we can use the following
(commonly-used) inequality, $h(x)\leq h(y)+h^{\prime}(y)(x-y)$ which
holds for any concave function, $h$, and note that we have equality when
$y=x$. For $y=\theta_{t}$, the current value in the iterative
optimization, we have: $$\begin{aligned}
f(\theta) & = \sum_{i=1}^{n}\sqrt{r_{i}(\theta)^{2}}\\
 & \leq \sum_{i=1}^{n}\sqrt{r_{i}(\theta_{t})^{2}}+\frac{r_{i}(\theta)^{2}-r_{i}(\theta_{t})^{2}}{2\sqrt{r_{i}(\theta_{t})^{2}}}\\
 & = g_{t}(\theta)\end{aligned}$$ where the term on the right of the
second equation is our majorizing function $g(\theta)$ for the current
$\theta_{t}$. We then have $$\begin{aligned}
g_{t}(\theta) & = \sum_{i=1}^{n}\sqrt{r_{i}(\theta_{t})^{2}}+\frac{1}{2}\sum_{i=1}^{n}\frac{r_{i}(\theta)^{2}-r_{i}(\theta_{t})^{2}}{2\sqrt{r_{i}(\theta_{t})^{2}}}\\
 & = \frac{1}{2}\sum_{i=1}^{n}\sqrt{r_{i}(\theta_{t})^{2}}+\frac{1}{2}\sum_{i=1}^{n}\frac{r_{i}(\theta)^{2}}{\sqrt{r_{i}(\theta_{t})^{2}}}\end{aligned}$$
Our job in this iteration of the algorithm is to minimize $g$ with
respect to $\theta$ (recall that $\theta_{t}$ is a fixed value), so we
can ignore the first sum, which doesn't involve $\theta$. Minimizing the
second sum can be seen as a weighted least squares problem, where the
numerator is the usual sum of squared residuals and the weights are
$w_{i}=\frac{1}{\sqrt{(y_{i}-z_{i}^{\top}\theta_{t})^{2}}}$. Intuitively
this makes sense: the weight is large when the magnitude of the residual
is small this makes up for the fact that we are using least squares when
we want to mimimize absolute deviations. So our update is:
$$\theta_{t+1}=(Z^{\top}W(\theta_{t})Z)^{-1}Z^{\top}W(\theta_{t})Y,$$
where $W(\theta_{t})$ is a diagonal matrix with elements
$w_{1},\ldots,w_{n}.$

As usual, we want to think about what could go wrong numerically. If we
have some very small magnitude residuals, they will get heavily
upweighted in this procedure, which might cause instability in our
optimization.

For an example of MM being used in practice for a real problem, see Jung
et al. (2014): Biomarker Detection in Association Studies: Modeling SNPs
Simultaneously via Logistic ANOVA, Journal of the American Statistical
Association 109:1355.

## Expectation-Maximization (EM)

It turns out the EM algorithm that many of you have heard about is a
special case of MM. For our purpose here, we'll consider maximization.

The EM algorithm is most readily motivated from a missing data
perspective. Suppose you want to maximize $L(\theta|x)=f(x;\theta)$
based on available data in a missing data context. Denote the complete
data as $Y=(X,Z)$ with $Z$ is missing. As we'll see, in many cases, $Z$
is actually a set of latent variables that we introduce into the problem
to formulate it so we can use EM. The canonical example is when $Z$ are
membership indicators in a mixture modeling context. (Note that in the
case where you introduce $Z$, that also means that one could also just
directly maximize $L(\theta|x)$, which in many cases may work better
than using the EM algorithm.)

In general, $\log L(\theta|x)$ may be hard to optimize because it
involves an integral over the missing data, $Z$:
$$L(\theta|x) = f(x;\theta)=\int f(x,z;\theta)dz,$$ but the EM algorithm provides a
recipe that makes the optimization straightforward for many problems.

The algorithm is as follows. Let $\theta^{t}$ be the current value of
$\theta$. Then define
$$Q(\theta;\theta^{t})=E(\log L(\theta|Y)|x;\theta^{t})$$.

That expectation is an expectation with respect to the conditional distribution,
$f(z|x; \theta = \theta^t)$.

 The algorithm is

1.  E step: Compute $Q(\theta;\theta^{t})$, ideally calculating the
    expectation over the missing data in closed form. Note that
    $\log L(\theta|Y)$ is a function of $\theta$ so
    $Q(\theta;\theta^{t})$ will involve both $\theta$ and $\theta^{t}$.

2.  M step: Maximize $Q(\theta;\theta^{t})$ with respect to $\theta$,
    finding $\theta^{t+1}$.

3.  Continue until convergence.

Ideally both the E and M steps can be done analytically. When the M step
cannot be done analytically, one can employ some of the numerical
optimization tools we've already seen. When the E step cannot be done
analytically, one standard approach is to estimate the expectation by
Monte Carlo, which produces Monte Carlo EM (MCEM). The strategy is to
draw from $z_{j}$ from $f(z|x,\theta^{t})$ and approximate $Q$ as a
Monte Carlo average of $\log f(x,z_{j};\theta)$, and then optimize over
this approximation to the expectation. If one can't draw in closed form
from the conditional density, one strategy is to do a short MCMC to draw
a (correlated) sample. However, if the E step cannot be done analytically
EM often will be very slow. (Even when the E step can be done analytically,
EM is often slow.)

EM can be show to increase the value of the function at each step using
Jensen's inequality (equivalent to the information inequality that holds
with regard to the Kullback-Leibler divergence between two
distributions) (Givens and Hoeting, p. 95, go through the details).
Furthermore, one can show that it amounts, at each step, to maximizing a
minorizing function for $\log L(\theta)$ - the minorizing function
(effectively $Q$) is tangent to $\log L(\theta)$ at $\theta^{t}$ and
lies below $\log L(\theta)$.

A standard example is a mixture model. (Here we'll assume a mixture of
normal distributions, but other distributions could be used.) Therefore
we have $$f(x;\theta)=\sum_{k=1}^{K}\pi_{k}f_{k}(x;\mu_{k},\sigma_{k})$$
where we have $K$ mixture components and $\pi_{k}$ are the (marginal)
probabilities of being in each component. The complete parameter vector
is $\theta=\{\{\pi_{k}\},\{\mu_{k}\},\{\sigma_{k}\}\}$. Note that the
likelihood is a complicated product (over observations) over the sum
(over components), so maximization may be difficult. Furthermore, such
likelihoods are well-known to be multimodal because of label switching.

To use EM, we take the group membership indicators for each observation
as the missing data. For the $i$th observation, we have
$z_{i}\in\{1,2,\ldots,K\}$. Introducing these indicators "breaks the
mixture". If we know the memberships for all the observations, it's
often easy to estimate the parameters for each group based on the
observations from that group. For example if the $\{f_{k}\}$'s were
normal densities, then we can estimate the mean and variance of each
normal density using the sample mean and sample variance of the
$x_{i}$'s that belong to each mixture component. EM will give us a
variation on this that uses "soft" (i.e., probabilistic) weighting.

The complete log likelihood given $z$ and $x$ is
$$\log\prod_{i}f(x_{i}|z_{i};\theta)\mbox{Pr}(Z_{i}=z_{i};\theta)$$
which can be expressed as\
\
$$\begin{aligned}
\log L(\theta|x,z) & = & \sum_{i}\log f(x_{i};\mu_{z_{i}},\sigma_{z_{i}})+\log\pi_{z_{i}}\\
 & = & \sum_{i}\sum_{k}I(z_{i}=k)(\log f_{k}(x_{i};\mu_{k},\sigma_{k})+\log\pi_{k})\end{aligned}$$
with $Q$ equal to
$$Q(\theta|\theta^{t})=\sum_{i}\sum_{k}E(I(z_{i}=k)|x_{i};\theta^{t})(\log f_{k}(x_{i};\mu_{k},\sigma_{k})+\log\pi_{k})$$
where $E(I(z_{i}=k)|x_{i};\theta^{t})$ is equal to the probability that
the $i$th observation is in the $k$th group given $x_{i}$ and
$\theta_{t}$, which is calculated from Bayes theorem as
$$p_{ik}^{t}=\frac{\pi_{k}^{t}f_{k}(x_{i};\mu_{k}^{t},\sigma_{k}^{t})}{\sum_{j}\pi_{j}^{t}f_{j}(x_{i};\mu_{k}^{t},\sigma_{k}^{t})}$$
We can now separately maximize $Q(\theta|\theta^{t})$ with respect to
$\pi_{k}$ and $\mu_{k},\sigma_{k}$ to find $\pi_{k}^{t+1}$ and
$\mu_{k}^{t+1},\sigma_{k}^{t+1}$, since the expression is the sum of a
term involving the parameters of the distributions and a term involving
the mixture probabilities. In the latter case, if the $f_{k}$ are normal
distributions, you end up with a weighted sum of normal distributions,
for which the estimators of the mean and variance parameters are the
weighted mean of the observations and the weighted variance.

---

[← 7. Combinatorial optimization over discrete spaces](38-7-combinatorial-optimization-over-discrete-spaces.md) · [Up: contents](index.md) · [9. Optimization under constraints →](40-9-optimization-under-constraints.md)
