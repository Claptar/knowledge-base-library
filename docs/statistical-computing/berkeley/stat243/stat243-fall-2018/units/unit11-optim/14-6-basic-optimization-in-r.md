---
title: 6 Basic optimization in R
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Basic optimization in R

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **6.1 Core optimization functions**

R has several optimization functions.

- _optimize()_ is good for 1-d optimization: “The method used is a combination of golden section search and successive parabolic interpolation, and was designed for use with continuous functions.”

32

- Another option is _uniroot()_ for finding the zero of a function, which you can use to minimize a function if you can compute the derivative.

- For more than one variable, _optim()_ uses a variety of optimization methods including the robust Nelder-Mead method, the BFGS quasi-Newton method and simulated annealing. You can choose which method you prefer and can try multiple methods. You can supply a gradient function to _optim()_ for use with the Newton-related methods but it can also calculate numerical derivatives on the fly. You can have _optim()_ return the Hessian at the optimum (based on a numerical estimate), which then allows straighforward calculation of asymptotic variances based on the information matrix.

- Also for multivariate optimization, _nlm()_ uses a Newton-style method, for which you can supply analytic gradient and Hessian, or it will estimate these numerically. _nlm()_ can also return the Hessian at the optimum.

- The _optimx_ package provides _optimx()_ , which is a wrapper for a variety of optimization methods (including many of those in _optim()_ , as well as _nlm()_ . One nice feature is that it allow you to use multiple methods in the same function call.

In the demo code (not shown here), we’ll work our way through a real example of optimizing a likelihood for some climate data on extreme precipitation.

### **6.2 Various considerations in using the R functions**

As we’ve seen, initial values are important both for avoiding divergence (e.g., in N-R), for increasing speed of convergence, and for helping to avoid local optima. So it is well worth the time to try to figure out a good starting value or multiple starting values for a given problem.

Scaling can be important. One useful step is to make sure the problem is well-scaled, namely that a unit step in any parameter has a comparable change in the objective function, preferably approximately a unit change at the optimum. _optim()_ allows you to supply scaling information through the _parscale_ component of the _control_ argument. Basically if _xj_ is varying at _p_ orders of magnitude smaller than the other _x_ s, we want to reparameterize to _x_<sup>_∗_</sup> _j_<sup>=</sup><sup>_xj·_10</sup><sup>_p_and then convert</sup> back to the original scale after finding the answer. Or we may want to work on the log scale for some variables, reparameterizing as _x_<sup>_∗_</sup> _j_<sup>=log(</sup><sup>_xj_).We could make such changes manually in our</sup> expression for the objective function or make use of arguments such as _parscale_ .

If the function itself gives very large or small values near the solution, you may want to rescale the entire function to avoid calculations with very large or small numbers. This can avoid problems such as having apparent convergence because a gradient is near zero, simply because the scale of the function is small. In _optim()_ this can be controlled with the _fnscale_ component of _control_ .

33

Always consider your answer and make sure it makes sense, in particular that you haven’t ’converged’ to an extreme value on the boundary of the space.

Venables and Ripley suggest that it is often worth supplying analytic first derivatives rather than having a routine calculate numerical derivatives but not worth supplying analytic second derivatives. As we’ll see in Unit 12, R can do symbolic (i.e., analytic) differentiation to find first and second derivatives using _deriv()_ .

In general for software development it’s obviously worth putting more time into figuring out the best optimization approach and supplying derivatives. For a one-off analysis, you can try a few different approaches and assess sensitivity.

The nice thing about likelihood optimization is that the asymptotic theory tells us that with large samples, the likelihood is approximately quadratic (i.e., the asymptotic normality of MLEs), which makes for a nice surface over which to do optimization. When optimizing with respect to variance components and other parameters that are non-negative, one approach to dealing with the constraints is to optimize with respect to the log of the parameter.

---

[← Unit 11 — optim Part 13 —](13-unit-11-optim-part-13.md) · [Up: contents](index.md) · [7 Combinatorial optimization over discrete spaces →](15-7-combinatorial-optimization-over-discrete-spaces.md)
