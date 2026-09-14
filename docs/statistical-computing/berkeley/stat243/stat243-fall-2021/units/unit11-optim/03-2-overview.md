---
title: 2 Overview
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit11-optim.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Overview

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The basic goal here is to optimize a function numerically when we cannot find the maximum (or minimum) analytically. Some examples:

1. Finding the MLE for a GLM

2. Finding least squares estimates for a nonlinear regression model,


where _g_ ( _·_ ) is nonlinear and we seek to find the value of _θ_ = ( _β, σ_<sup>2</sup> ) that best fits the data.

3. Maximizing a likelihood under constraints

4. Fitting a machine learning prediction method

Maximum likelihood estimation and variants thereof is a standard situation in which optimization comes up.

We’ll focus on **minimization** , since any maximization of _f_ can be treated as minimization of _−f_ . The basic setup is to find the _argument_ , _x_ , that minimizes _f_ ( _x_ ):


where _D_ is the domain. Sometimes _D_ = _ℜ_<sup>_p_</sup> but other times it imposes constraints on _x_ . When there are no constraints, this is unconstrained optimization, where any _x_ for which _f_ ( _x_ ) is defined is a possible solution. We’ll assume that _f_ is continuous as there’s little that can be done systematically if we’re dealing with a discontinuous function.

In one dimension, minimization is the same as root-finding with the derivative function, since the minimum of a differentiable function can only occur at a point at which the derivative is zero. So with differentiable functions we’ll seek to find _x_<sup>_∗_</sup> s.t. _f_<sup>_′_</sup> ( _x_<sup>_∗_</sup> ) = _∇f_ ( _x_<sup>_∗_</sup> ) = 0. To ensure a minimum, we want that for all _y_ in a neighborhood of _x_<sup>_∗_</sup> , _f_ ( _y_ ) _≥ f_ ( _x_<sup>_∗_</sup> ), or (for twice differentiable functions) _f_<sup>_′′_</sup> ( _x_<sup>_∗_</sup> ) _≥_ 0.

2

In more than one dimension, we want that the Hessian evaluated at _x_<sup>_∗_</sup> is positive semi-definite, which tells us that moving in any direction away from _x_<sup>_∗_</sup> would not go downhill.

Different strategies are used depending on whether _D_ is discrete and countable, or continuous, dense and uncountable. We’ll concentrate on the continuous case but the discrete case can arise in statistics, such as in doing variable selection.

In general we rely on the fact that we can evaluate _f_ . Often we make use of analytic or numerical derivatives of _f_ as well.

To some degree, optimization is a solved problem, with good software implementations, so it raises the question of how much to discuss in this class. The basic motivation for going into some of the basic classes of optimization strategies is that the function being optimized changes with each problem and can be tricky to optimize, and I want you to know something about how to choose a good approach when you find yourself with a problem requiring optimization. Finding global, as opposed to local, minima can also be an issue.

Note that I’m not going to cover MCMC (Markov chain Monte Carlo) methods, which are used for approximating integrals and sampling from posterior distributions in a Bayesian context and in a variety of ways for optimization. If you take a Bayesian course you’ll cover this in detail, and if you don’t do Bayesian work, you probably won’t have much need for MCMC, though it comes up in MCEM (Monte Carlo EM) and simulated annealing, among other places.

**Goals for the unit** Optimization is a big topic. Here’s what I would like you to get out of this:

1. an understanding of line searches (one-dimensional optimization),

2. an understanding of multivariate derivative-based optimization and how line searches are useful within this,

3. an understanding of derivative-free methods,

4. an understanding of the methods used in R’s optimization routines, their strengths and weaknesses, and various tricks for doing better optimization in R, and

5. a basic idea of what convex optimization is and when you might want to go learn more about it.

---

[← 1 Notation](02-1-notation.md) · [Up: contents](index.md) · [3 Univariate function optimization →](04-3-univariate-function-optimization.md)
