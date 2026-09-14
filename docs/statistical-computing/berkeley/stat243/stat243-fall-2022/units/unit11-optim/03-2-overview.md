---
title: 2. Overview
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit11-optim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Overview

**Source:** [`units/unit11-optim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

The basic goal here is to optimize a function numerically when we cannot
find the maximum (or minimum) analytically. Some examples:

1.  Finding the MLE for a GLM

2.  Finding least squares estimates for a nonlinear regression model,
    $$Y_{i}\sim\mathcal{N}(g(z_{i};\beta),\sigma^{2})$$ where $g(\cdot)$
    is nonlinear and we seek to find the value of
    $\theta=(\beta,\sigma^{2})$ that best fits the data.

3.  Maximizing a likelihood under constraints

4.  Fitting a machine learning prediction method

Maximum likelihood estimation and variants thereof is a standard
situation in which optimization comes up.

We'll focus on **minimization**, since any maximization of $f$ can be
treated as minimization of $-f$. The basic setup is to find the
*argument*, $x$, that minimizes $f(x)$: $$x^{*}=\arg\min_{x\in D}f(x)$$
where $D$ is the domain. Sometimes $D=\Re^{p}$ but other times it
imposes constraints on $x$. When there are no constraints, this is
unconstrained optimization, where any $x$ for which $f(x)$ is defined is
a possible solution. We'll assume that $f$ is continuous as there's
little that can be done systematically if we're dealing with a
discontinuous function.

In one dimension, minimization is the same as root-finding with the
derivative function, since the minimum of a differentiable function can
only occur at a point at which the derivative is zero. So with
differentiable functions we'll seek to find $x^{*}$ s.t.
$f^{\prime}(x^{*})=\nabla f(x^{*})=0$. To ensure a minimum, we want that
for all $y$ in a neighborhood of $x^{*}$, $f(y)\geq f(x^{*})$, or (for
twice differentiable functions) $f^{\prime\prime}(x^{*})\geq0$.

In more than one dimension, we want that the Hessian evaluated at
$x^{*}$ is positive semi-definite, which tells us that moving in any
direction away from $x^{*}$ would not go downhill.

Different strategies are used depending on whether $D$ is discrete and
countable, or continuous, dense and uncountable. We'll concentrate on
the continuous case but the discrete case can arise in statistics, such
as in doing variable selection.

In general we rely on the fact that we can evaluate $f$. Often we make
use of analytic or numerical derivatives of $f$ as well.

To some degree, optimization is a solved problem, with good software
implementations, so it raises the question of how much to discuss in
this class. The basic motivation for going into some of the basic
classes of optimization strategies is that the function being optimized
changes with each problem and can be tricky to optimize, and I want you
to know something about how to choose a good approach when you find
yourself with a problem requiring optimization. Finding global, as
opposed to local, minima can also be an issue.

Note that I'm not going to cover MCMC (Markov chain Monte Carlo)
methods, which are used for approximating integrals and sampling from
posterior distributions in a Bayesian context and in a variety of ways
for optimization. If you take a Bayesian course you'll cover this in
detail, and if you don't do Bayesian work, you probably won't have much
need for MCMC, though it comes up in MCEM (Monte Carlo EM) and simulated
annealing, among other places.

#### Goals for the unit

Optimization is a big topic. Here's what I would like you to get out of
this:

1.  an understanding of line searches (one-dimensional optimization),
2.  an understanding of multivariate derivative-based optimization and
    how line searches are useful within this,
3.  an understanding of derivative-free methods,
4.  an understanding of the methods used in R's optimization routines,
    their strengths and weaknesses, and various tricks for doing better
    optimization in R, and
5.  a basic idea of what convex optimization is and when you might want
    to go learn more about it.

---

[← 1. Notation](02-1-notation.md) · [Up: contents](index.md) · [3. Univariate function optimization →](04-3-univariate-function-optimization.md)
