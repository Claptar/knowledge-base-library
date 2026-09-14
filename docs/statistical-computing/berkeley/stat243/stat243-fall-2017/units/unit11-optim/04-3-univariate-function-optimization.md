---
title: 3 Univariate function optimization
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Univariate function optimization

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We’ll start with some strategies for univariate functions. These can be useful later on in dealing with multivariate functions.

3

### **3.1 Golden section search**

This strategy requires only that the function be unimodal.

Assume we have a single minimum, in [ _a, b_ ]. We choose two points in the interval and evaluate them, _f_ ( _x_ 1) and _f_ ( _x_ 2). If _f_ ( _x_ 1) _< f_ ( _x_ 2) then the minimum must be in [ _a, x_ 2], and if the converse in [ _x_ 1 _, b_ ]. We proceed by choosing a new point in the new, smaller interval and iterate. At each step we reduce the length of the interval in which the minimum must lie. The primary question involves what is an efficient rule to use to choose the new point at each iteration.

Suppose we start with _x_ 1 and _x_ 2 s.t. they divide [ _a, b_ ] into three equal segments. Then we use _f_ ( _x_ 1) and _f_ ( _x_ 2) to rule out either the leftmost or rightmost segment based on whether _f_ ( _x_ 1) _< f_ ( _x_ 2). If we have divided equally, we cannot place the next point very efficiently because either _x_ 1 or _x_ 2 equally divides the remaining space, so we are forced to divide the remaining space into relative lengths of 0.25, 0.25, and 0.5. The next time around, we may only rule out the shorter segment, which leads to inefficiency.

The efficient strategy is to maintain the _golden ratio_ between the distances between the points using _φ_ = ( _√_ 5 _−_ 1) _/_ 2 _≈ ._ 618, the golden ratio. We start with _x_ 1 = _a_ + (1 _− φ_ )( _b − a_ ) and _x_ 2 = _a_ + _φ_ ( _b − a_ ). Then suppose _f_ ( _x_ 1) _< f_ ( _x_ 2). We now choose to place _x_ 3 s.t. it uses the golden ratio in the interval [ _a, x_ 1]: _x_ 3 = _a_ + (1 _− φ_ )( _x_ 2 _− a_ ). Because of the way we’ve set it up, we once again have the third subinterval, [ _x_ 1 _, x_ 2], of equal length as the first subinterval, [ _a, x_ 3]. The careful choice allows us to narrow the search interval by an equal proportion,1 _− φ_ , in each iteration. Eventually we have narrowed the minimum to between _xt−_ 1 and _xt_ , where the difference _|xt − xt−_ 1 _|_ is sufficiently small (within some tolerance - see Section 4 for details), and we report ( _xt_ + _xt−_ 1) _/_ 2. We’ll see an example of this on the board in class.

### **3.2 Bisection method**

The bisection method requires the existence of the first derivative but has the advantage over the golden section search of halving the interval at each step. We again assume unimodality.

We start with an initial interval ( _a_ 0 _, b_ 0) and proceed to shrink the interval. Let’s choose _a_ 0 and _b_ 0, and set _x_ 0 to be the mean of these endpoints. Now we update according to the following algorithm, assuming our current interval is [ _at, bt_ ]:


and set _xt_ +1 to the mean of _at_ +1 and _bt_ +1. The basic idea is that if the derivative at both _at_ and _xt_ is negative, then the minimum must be between _xt_ and _bt_ , based on the intermediate value theorem.

4

If the derivatives at _at_ and _xt_ are of different signs, then the minimum must be between _at_ and _xt_ .

Since the bisection method reduces the size of the search space by one-half at each iteration, one can work out that each decimal place of precision requires 3-4 iterations. Obviously bisection is more efficient than the golden section search because we reduce by 0 _._ 5 _>_ 0 _._ 382 = 1 _− φ_ , so we’ve gained information by using the derivative. It requires an evaluation of the derivative however, while golden section just requires an evaluation of the original function.

Bisection is an example of a _bracketing_ method, in which we trap the minimum within a nested sequence of intervals of decreasing length. These tend to be slow, but if the first derivative is continuous, they are robust and don’t require that a second derivative exist.

### **3.3 Newton-Raphson (Newton’s method)**

#### **3.3.1 Overview**

We’ll talk about Newton-Raphson (N-R) as an optimization method rather than a root-finding method, but they’re just different perspectives on the same algorithm.

For N-R, we need two continuous derivatives that we can evaluate. The benefit is speed, relative to bracketing methods. We again assume the function is unimodal. The minimum must occur at _x_<sup>_∗_</sup> s.t. _f_<sup>_′_</sup> ( _x_<sup>_∗_</sup> ) = 0, provided the second derivative is non-negative at _x_<sup>_∗_</sup> . So we aim to find a zero (a root) of the first derivative function. Assuming that we have an initial value _x_ 0 that is close to _x_<sup>_∗_</sup> , we have the Taylor series approximation


Now set _f_<sup>_′_</sup> ( _x_ ) = 0, since that is the condition we desire (the condition that holds when we are at _x_<sup>_∗_</sup> ), and solve for _x_ to get


and iterate, giving us updates of the form _xt_ +1 = _xt −_<sup>_<u>f</u>′_</sup><sup><u>(</u></sup><sup>_xt_</sup><sup><u>)</u></sup> _f_<sup>_′′_</sup> ( _xt_ )<sup>.Whatarewedoingintuitively?</sup> Basically we are taking the tangent to _f_ ( _x_ ) at _x_ 0 and extrapolating along that line to where it crosses the x-axis to find _x_ 1. We then reevaluate _f_ ( _x_ 1) and continue to travel along the tangents.

One can prove that if _f_<sup>_′_</sup> ( _x_ ) is twice continuously differentiable, is convex, and has a root, then N-R converges from any starting point.

Note that we can also interpret the N-R update as finding the analytic minimum of the quadratic Taylor series approximation to _f_ ( _x_ ).

Newton’s method converges very quickly (as we’ll discuss in Section 4), but if you start too far from the minimum, you can run into serious problems.

5

#### **3.3.2 Secant method variation on N-R**

Suppose we don’t want to calculate the second derivative required in the divisor of N-R. We might replace the analytic derivative with a discrete difference approximation based on the secant line joining ( _xt, f_<sup>_′_</sup> ( _xt_ )) and ( _xt−_ 1 _, f_<sup>_′_</sup> ( _xt−_ 1)), giving an approximate second derivative:


For this variant on N-R, we need two starting points, _x_ 0 and _x_ 1.

An alternative to the secant-based approximation is to use a standard discrete approximation of the derivative such as


#### **3.3.3 How can Newton’s method go wrong?**

Let’s think about what can go wrong - namely when we could have _f_ ( _xt_ +1) _> f_ ( _xt_ )? Basically, if _f_<sup>_′_</sup> ( _xt_ ) is relatively flat, we can get that _|xt_ +1 _− x_<sup>_∗_</sup> _| > |xt − x_<sup>_∗_</sup> _|_ . We’ll see an example on the board and the demo code (see below). Newton’s method can also go uphill when the second derivative is negative, with the method searching for a maximum.

First let’s see an example of divergence.

**par** (mfrow = **c** (1,2)) fp <- **function** (x, theta = 1){ **exp** (x*theta)/(1+ **exp** (x*theta)) - .5 } fpp <- **function** (x, theta = 1){ **exp** (x*theta)/((1+ **exp** (x*theta))^2) } xs <- **seq** (-15, 15, len = 300) _## good starting point_ x0 <- 2 xvals <- **c** (x0, **rep** (NA,9)) **for** (t **in** 2:10){ xvals[t]=xvals[t-1] - **fp** (xvals[t-1]) / **fpp** (xvals[t-1]) } **print** (xvals)

6

---

[← 2 Overview](03-2-overview.md) · [Up: contents](index.md) · [Unit 11 — optim Part 05 — →](05-unit-11-optim-part-05.md)
