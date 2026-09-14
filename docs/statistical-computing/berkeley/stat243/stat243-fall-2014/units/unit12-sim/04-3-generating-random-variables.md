---
title: 3 Generating random variables
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit12-sim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit12-sim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Generating random variables

**Source:** [`units/unit12-sim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit12-sim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There are a variety of methods for generating from common distributions (normal, gamma, beta, Poisson, t, etc.). Since these tend to be built into R and presumably use good algorithms, we won’t go into them. A variety of statistical computing and Monte Carlo books describe the various methods. Many are built on the relationships between different distributions - e.g., a beta random variable (RV) can be generated from two gamma RVs.

Also note that you can call the C functions that implement the R distribution functions as a library ( _Rmath_ ), so if you’re coding in C or another language, you should be able to make use of the standard functions: _{r,p,q,d}{norm,t,gamma,binom,pois,etc.}_ (as well as a variety of other R math functions, which can be seen in _Rmath.h_ ). Phil Spector has a writeup on this (http://www.stat.berkeley.edu/classes/s243/rmath.html) and material can also be found in the _Writing R Extensions_ manual on CRAN (section 6.16).

### **3.1 Multivariate distributions**

The _mvtnorm_ package supplies code for working with the density and CDF of multivariate normal and t distributions.

To generate a multivariate normal, we’ve seen the standard method based on the Cholesky decomposition:

U <- **chol** (covMat) **crossprod** (U, **rnorm** ( **nrow** (covMat)))

For a singular covariance matrix we can use the Cholesky with pivoting, setting as many rows to zero as the rank deficiency. Then when we generate the multivariate normals, they respect the constraints implicit in the rank deficiency. However, you’ll need to reorder the resulting vector because of the reordering involved in the pivoted Cholesky.

### **3.2 Inverse CDF**

Most of you know the inverse CDF method. To generate _X ∼ F_ where _F_ is a CDF and is an invertible function, first generate _Z ∼U_ (0 _,_ 1), then _x_ = _F_<sup>_−_1</sup> ( _z_ ). For discrete CDFs, one can work with a discretized version. For multivariate distributions, one can work with a univariate marginal and then a sequence of univariate conditionals: _f_ ( _x_ 1) _f_ ( _x_ 2 _|x_ 1) _· · · f_ ( _xk|xk−_ 1 _, . . . , x_ 1), when the distribution allows this analytic decomposition.

15

### **3.3 Rejection sampling**

The basic idea of rejection sampling (RS) relies on the introduction of an auxiliary variable, _u_ . Suppose _X ∼ F_ . Then we can write _f_ ( _x_ ) = �0 _f_ ( _x_ ) _du_ . Thus _f_ is the marginal density of _X_ in the joint density, ( _X, U_ ) _∼U{_ ( _x, u_ ) : 0 _< u < f_ ( _x_ ) _}_ . Now we’d like to use this in a way that relies only on evaluating _f_ ( _x_ ) without having to draw from _f_ .

To implement this we draw from a larger set and then only keep draws for which _u < f_ ( _x_ ). We choose a density, _g_ , that is easy to draw from and that can _majorize f_ , which means there exists a constant _c_ s.t. , _cg_ ( _x_ ) _≥ f_ ( _x_ ) _∀x_ . In other words we have that _cg_ ( _x_ ) is an upper envelope for _f_ ( _x_ ). The algorithm is

1. generate _x ∼ g_

2. generate _u ∼U_ (0 _,_ 1)

3. if _u ≤ f_ ( _x_ ) _/cg_ ( _x_ ) then use _x_ ; otherwise go back to step 1

The intuition here is graphical: we generate from under a curve that is always above _f_ ( _x_ ) and accept only when _u_ puts us under _f_ ( _x_ ) relative to the majorizing density. A key here is that the majorizing density have fatter tails than the density of interest, so that the constant _c_ can exist. So we could use a _t_ to generate from a normal but not the reverse. We’d like _c_ to be small to reduce <u>�</u> _f_ ( _x_ ) _dx_ the number of rejections because it turns out that<sup><u>1</u></sup> _c_<sup>=</sup> <u>�</u> _cg_ ( _x_ ) _dx_<sup>istheacceptanceprobability.</sup> This approach works in principle for multivariate densities but as the dimension increases, the proportion of rejections grows, because more of the volume under _cg_ ( _x_ ) is above _f_ ( _x_ ).

If _f_ is costly to evaluate, we can sometimes reduce calculation using a lower bound on _f_ . In this case we accept if _u ≤ f_ low( _y_ ) _/cgY_ ( _y_ ). If it is not, then we need to evaluate the ratio in the usual rejection sampling algorithm. This is called squeezing.

One example of RS is to sample from a truncated normal. Of course we can just sample from the normal and then reject, but this can be inefficient, particularly if the truncation is far in the tail (a case in which inverse CDF suffers from numerical difficulties). Suppose the truncation point is greater than zero. Working with the standardized version of the normal, you can use an translated exponential with lower end point equal to the truncation point as the majorizing density (Robert 1995; Statistics and Computing, and see calculations in the demo code). For truncation less than zero, just make the values negative.

### **3.4 Adaptive rejection sampling**

The difficulty of RS is finding a good enveloping function. Adaptive rejection sampling refines the envelope as the draws occur, in the case of a continuous, differentiable, log-concave density.

16

The basic idea considers the log of the density and involves using tangents or secants to define an upper envelope and secants to define a lower envelope for a set of points in the support of the distribution. The result is that we have piecewise exponentials (since we are exponentiating from straight lines on the log scale) as the bounds. We can sample from the upper envelope based on sampling from a discrete distribution and then the appropriate exponential. The lower envelope is used for squeezing. We add points to the set that defines the envelopes whenever we accept a point that requires us to evaluate _f_ ( _x_ ) (the points that are accepted based on squeezing are not added to the set). We’ll talk this through some in class.

### **3.5 Importance sampling**

Importance sampling (IS) allows us to estimate expected values, with some commonalities with rejection sampling.


so _µ_ ˆ = _m_<sup><u>1</u></sup> � _i_<sup>_h_(</sup><sup>_x_</sup> _i_<sup>)</sup><sup>_<u>f</u>_</sup> _g_ (<sup><u>(</u></sup> _x_<sup>_x_</sup> _i_<sup>_<u>i</u>_</sup> )<sup><u>)</u>for</sup><sup>_xi_drawn from</sup><sup>_g_(</sup><sup>_x_), where</sup><sup>_w_</sup> _i_<sup>_∗_=</sup><sup>_f_(</sup><sup>_xi_)</sup><sup>_/g_(</sup><sup>_xi_) act as weights.Often in</sup> Bayesian contexts, we know _f_ ( _x_ ) only up to a normalizing constant. In this case we need to use _wi_ = _wi_<sup>_∗/_�</sup> _i_<sup>_w_</sup> _i_<sup>_∗_.</sup>

Here we don’t require the majorizing property, just that the densities have common support, but things can be badly behaved if we sample from a density with lighter tails than the density of interest. So in general we want _g_ to have heavier tails. More specifically for a low variance estimator of _µ_ , we would want that _f_ ( _xi_ ) _/g_ ( _xi_ ) is large only when _h_ ( _xi_ ) is very small, to avoid having overly influential points.

This suggests we can reduce variance in an IS context by oversampling _x_ for which _h_ ( _x_ ) is large and undersampling when it is small, since Var(ˆ _µ_ ) = _m_<sup><u>1</u>Var(</sup><sup>_h_(</sup><sup>_X_)</sup><sup>_<u>f</u>_</sup> _g_ (<sup><u>(</u></sup> _X_<sup>_X_</sup> )<sup><u>)</u>).An example is that if</sup> _h_ is an indicator function that is 1 only for rare events, we should oversample rare events and then the IS estimator corrects for the oversampling.

What if we actually want a sample from _f_ as opposed to estimating the expected value above? We can draw _x_ from the unweighted sample, _{xi}_ , with weights _{wi}_ . This is called sampling importance resampling (SIR).

### **3.6 Ratio of uniforms**

If _U_ and _V_ are uniform in _C_ = _{_ ( _u, v_ ) : 0 _≤ u ≤_ � _f_ ( _v/u_ ) then _X_ = _V/U_ has density proportion to _f_ . The basic algorithm is to choose a rectangle that encloses _C_ and sample until we find _u ≤ f_ ( _v/u_ ). Then we use _x_ = _v/u_ as our RV. The larger region enclosing _C_ is the majorizing

17

region and a simple approach (if _f_ ( _x_ )and _x_<sup>2</sup> _f_ ( _x_ ) are bounded in _C_ ) is to choose the rectangle, 0 _≤ u ≤_ sup _x_ � _f_ ( _x_ ), inf _x x_ ~~�~~ _f_ ( _x_ ) _≤ v ≤_ sup _x x_ ~~�~~ _f_ ( _x_ ).

One can also consider truncating the rectangular region, depending on the features of _f_ .

Monahan recommends the ratio of uniforms, particularly a version for discrete distributions (p. 323 of the 2nd edition).

---

[← 2 Random number generation (RNG)](03-2-random-number-generation-rng.md) · [Up: contents](index.md) · [4 Design of simulation studies →](05-4-design-of-simulation-studies.md)
