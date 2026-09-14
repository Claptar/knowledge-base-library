---
title: 8 Convexity
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Convexity

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Many optimization problems involve (or can be transformed into) convex functions. Convex optimization (also called convex programming) is a big topic and one that we’ll only brush the surface of in Sections 8 and 9. The goal here is to give you enough of a sense of the topic that you know when you’re working on a problem that might involve convex optimization, in which case you’ll need to go learn more.

Optimization for convex functions is simpler than for ordinary functions because we don’t have to worry about local optima - any stationary point (point where the gradient is zero) is a global minimum. A set _S_ in _ℜ_<sup>_p_</sup> is convex if any line segment between two points in _S_ lies entirely within

34

_S_ . More generally, _S_ is convex if any convex combination is itself in _S_ , i.e.,<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_αixi∈S_for</sup> non-negative weights, _αi_ , that sum to 1. Convex functions are defined on convex sets - _f_ is convex if for points in a convex set, _xi ∈ S_ , we have _f_ (<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_αixi_)</sup><sup>_≤_�</sup><sup>_m_</sup> _i_ =1<sup>_αif_(</sup><sup>_xi_).Strict convexity is</sup> when the inequality is strict (no equality).

The first-order convexity condition relates a convex function to its first derivative: _f_ is convex if and only if _f_ ( _x_ ) _≥ f_ ( _y_ ) + _∇f_ ( _y_ )<sup>_⊤_</sup> ( _x − y_ ) for _y_ and _x_ in the domain of _f_ . We can interpret this as saying that the first order Taylor approximation to _f_ is tangent to and below (or touching) the function at all points.

The second-order convexity condition is that a function is convex if (provided its first derivative exists), the derivative is non-decreasing, in which case we have _f_<sup>_′′_</sup> ( _x_ ) _≥_ 0 _∀x_ (for univariate functions). If we have _f_<sup>_′′_</sup> ( _x_ ) _≤_ 0 _∀x_ (a concave, or convex down function) we can always consider _−f_ ( _x_ ), which is convex. Convexity in multiple dimensions means that the gradient is nondecreasing in all dimensions. If _f_ is twice differentiable, then if the Hessian is positive semi-definite, _f_ is convex.

There are a variety of results that allow us to recognize and construct convex functions based on knowing what operations create and preserve convexity. The Boyd book is a good source for material on such operations. Note that norms are convex functions (based on the triangle inequality), _∥_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_αixi∥≤_�</sup><sup>_n_</sup> _i_ =1<sup>_αi∥xi∥_.</sup>

We’ll talk about a general algorithm that works for convex functions (the MM algorithm) and about the EM algorithm that is well-known in statistics, and is a special case of MM.

### **8.1 MM algorithm**

The MM algorithm is really more of a principle for constructing problem specific algorithms. MM stands for majorize-minorize. We’ll use the majorize part of it to minimize functions - the minorize part is the counterpart for maximizing functions.

Suppose we want to minimize a convex function, _f_ ( _x_ ). The idea is to construct a majorizing function, at _xt_ , which we’ll call _g_ . _g_ majorizes _f_ at _xt_ if _f_ ( _xt_ ) = _g_ ( _xt_ ) and _f_ ( _x_ ) _≤ g_ ( _x_ ) _∀x_ .

The iterative algorithm is as follows. Given _xt_ , construct a majorizing function _g_ ( _xt_ ) _._ Then minimize _g_ w.r.t. _x_ (or at least move downhill, such as with a modified Newton step) to find _xt_ +1. Then we iterate, finding the next majorizing function. The algorithm is obviously guaranteed to go downhill, and ideally we use a function _g_ that is easy to work with (i.e., to minimize or go downhill with respect to). Note that we haven’t done any matrix inversions or computed any derivatives of _f_ . Furthermore, the algorithm is numerically stable - it does not over- or undershoot the optimum. The downside is that convergence can be quite slow.

The tricky part is finding a good majorizing function. Basically one needs to gain some skill in

35

working with inequalities. The Lange book has some discussion of this.

An example is for estimating regression coefficients for median regression (aka least absolute deviation regression), which minimizes _f_ ( _θ_ ) =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_|yi−z_</sup> _i_<sup>_⊤θ|_=�</sup><sup>_n_</sup> _i_ =1<sup>_|ri_(</sup><sup>_θ_)</sup><sup>_|_.Note that</sup><sup>_f_(</sup><sup>_θ_)</sup> is convex because affine functions (in this case _yi − zi_<sup>_⊤θ_)areconvex,convexfunctionsofaffine</sup> functions are convex, and the summation preserves the convexity. We’ll work through this example in class. We’ll make use the following (commonly-used) inequality, which holds for any concave function, _f_ :


For an example of MM being used in practice for a real problem, see Jung et al. (2014): Biomarker Detection in Association Studies: Modeling SNPs Simultaneously via Logistic ANOVA, Journal of the American Statistical Association 109:1355.

### **8.2 Expectation-Maximization (EM)**

It turns out the EM algorithm that many of you have heard about is a special case of MM. For our purpose here, we’ll consider maximization.

The EM algorithm is most readily motivated from a missing data perspective. Suppose you want to maximize _L_ ( _θ|X_ = _x_ ) = _f_ ( _x|θ_ ) based on available data in a missing data context. Denote the complete data as _Y_ = ( _X, Z_ ) with _Z_ is missing. As we’ll see, in many cases, _Z_ is actually a set of latent variables that we introduce into the problem to formulate it so we can use EM. The canonical example is when _Z_ are membership indicators in a mixture modeling context.

In general, _L_ ( _θ|x_ ) may be hard to optimize because it involves an integral over the missing data, _Z_ :


but the EM algorithm provides a recipe that makes the optimization straightforward for many problems.

The algorithm is as follows. Let _θt_ be the current value of _θ_ . Then define


The algorithm is

1. E step: Compute _Q_ ( _θ|θt_ ), ideally calculating the expectation over the missing data in closed form. Note that log _L_ ( _θ|Y_ ) is a function of _θ_ so _Q_ ( _θ|θt_ ) will involve both _θ_ and _θt_ .

2. M step: Maximize _Q_ ( _θ|θt_ ) with respect to _θ_ , finding _θt_ +1.

36

#### 3. Continue until convergence.

Ideally both the E and M steps can be done analytically. When the M step cannot be done analytically, one can employ some of the numerical optimization tools we’ve already seen. When the E step cannot be done analytically, one standard approach is to estimate the expectation by Monte Carlo, which produces Monte Carlo EM (MCEM). The strategy is to draw from _zj_ from _f_ ( _z|x, θt_ ) and approximate _Q_ as a Monte Carlo average of log _f_ ( _x, zj|θ_ ), and then optimize over this approximation to the expectation. If one can’t draw in closed form from the conditional density, one strategy is to do a short MCMC to draw a (correlated) sample.

EM can be show to increase the value of the function at each step using Jensen’s inequality (equivalent to the information inequality that holds with regard to the Kullback-Leibler divergence between two distributions) (Givens and Hoeting, p. 95, go through the details). Furthermore, one can show that it amounts, at each step, to maximizing a minorizing function for log _L_ ( _θ_ ) - the minorizing function (effectively _Q_ ) is tangent to log _L_ ( _θ_ ) at _θt_ and lies below log _L_ ( _θ_ ).

A standard example is a mixture model. Suppose we have


where we have _K_ mixture components and _πk_ are the (marginal) probabilities of being in each component. The complete parameter vector is _θ_ = _{{πk}, {φk}}_ . Note that the likelihood is a complicated product (over observations) over the sum (over components), so maximization may be difficult. Furthermore, such likelihoods are well-known to be multimodal because of label switching.

To use EM, we take the group membership indicators for each observation as the missing data. For the _i_ th observation, we have _zi ∈{_ 1 _,_ 2 _, . . . , K}_ . Introducing these indicators “breaks the mixture”. If we know the memberships for all the observations, it’s often easy to estimate the parameters for each group based on the observations from that group. For example if the _{fk}_ ’s were normal densities, then we can estimate the mean and variance of each normal density using the sample mean and sample variance of the _xi_ ’s that belong to each mixture component. EM will give us a variation on this that uses “soft” (i.e., probabilistic) weighting.

The complete log likelihood given _z_ and _x_ is


37

which can be expressed as


with _Q_ equal to


where _E_ ( _I_ ( _zi_ = _k_ ) _|xi, θt_ ) is equal to the probability that the _i_ th observation is in the _k_ th group given _xi_ and _θt_ , which is calculated from Bayes theorem as


We can now separately maximize _Q_ ( _θ|θt_ ) with respect to _πk_ and _φk_ to find _πk,t_ +1 and _φk,t_ +1, since the expression is the sum of a term involving the parameters of the distributions and a term involving the mixture probabilities. In the latter case, if the _fk_ are normal distributions, you end up with a weighted sum of normal distributions, for which the estimators of the mean and variance parameters are the weighted mean of the observations and the weighted variance.

---

[← 7 Combinatorial optimization over discrete spaces](15-7-combinatorial-optimization-over-discrete-spaces.md) · [Up: contents](index.md) · [9 Optimization under constraints →](17-9-optimization-under-constraints.md)
