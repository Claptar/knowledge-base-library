---
title: Unit 14 — integ Part 02 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit14-integ.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit14-integ.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 14 — integ Part 02 —

**Source:** [`units/unit14-integ.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit14-integ.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **2 Integration**

We’ve actually already discussed numerical integration extensively in the simulation unit, where we considered Monte Carlo approximation of high-dimensional integrals. In the case where we have an integral in just one or two dimensions, MC is fine, but we can get highly-accurate, very fast approximations by numerical integration methods known as quadrature. Unfortunately such approximations scale very badly as the dimension grows, while MC methods scale well, so MC is recommended in higher dimensions. Here’s an empirical example in R, where the MC estimator is


for _f_ = _U_ (0 _, π_ ):

f <- **function** (x) **sin** (x) _# mathematically, the integral from 0 to pi is 2 # quadrature through integrate()_ **integrate** (f, 0, pi)

## 2 with absolute error < 2.2e-14 **system.time** ( **integrate** (f, 0, pi))

## user system elapsed ## 0.000 0.000 0.001 _# MC estimate_

ninteg <- **function** (n) **mean** ( **sin** ( **runif** (n, 0, pi))*pi) n <- 1000 **ninteg** (n)

7

## [1] 2.01159876 **system.time** ( **ninteg** (n)) ## user system elapsed ## 0 0 0 n <- 10000 **ninteg** (n) ## [1] 1.99442722 **system.time** ( **ninteg** (n)) ## user system elapsed ## 0.000 0.000 0.001 n <- 1000000 **ninteg** (n) ## [1] 1.99911318 **system.time** ( **ninteg** (n)) ## user system elapsed ## 0.064 0.000 0.065 _# that was fairly slow, # especially if you need to do a lot of individual integrals_

More on this issue below.

### **2.1 Numerical integration methods**

The basic idea is to break the domain into pieces and approximate the integral within each piece:


where we then approximate � _xxii_ +1 _f_ ( _x_ ) _dx ≈_<sup>�</sup><sup>_m_</sup> _j_ =0<sup>_Aijf_(</sup><sup>_x∗_</sup> _ij_<sup>) where</sup><sup>_x∗_</sup> _ij_<sup>are the</sup><sup>_nodes_.</sup>

8

#### **2.1.1 Newton-Cotes quadrature**

Newton-Cotes quadrature has equal length intervals of length _h_ = ( _b−a_ ) _/n_ , with the same number of nodes in each interval. _f_ ( _x_ ) is replaced with a polynomial approximation in each interval and _Aij_ are chosen so that the sum equals the integral of the polynomial approximation on the interval.

A basic example is the _Riemann rule_ , which takes a single node, _x_<sup>_∗_</sup> _i_<sup>=</sup><sup>_xi_and the “polynomial”</sup> is a constant, _f_ ( _x_<sup>_∗_</sup> _i_<sup>), so we have</sup>


Of course using a piecewise constant to approximate _f_ ( _x_ ) is not likely to give us high accuracy. The _trapezoidal rule_ takes _x_<sup>_∗_</sup> _i_ 0<sup>=</sup><sup>_xi_,</sup><sup>_x_</sup> _i_<sup>_∗_</sup> 1<sup>=</sup><sup>_xi_+1and uses a linear interpolation between</sup><sup>_f_(</sup><sup>_x∗_</sup> _i_ 0<sup>)</sup> and _f_ ( _x_<sup>_∗_</sup> _i_ 1<sup>) to give</sup>


_Simpson’s rule_ uses a quadratic interpolation at the points _x_<sup>_∗_</sup> _i_ 0<sup>=</sup><sup>_xi_,</sup><sup>_x_</sup> _i_<sup>_∗_</sup> 1<sup>=(</sup><sup>_xi_+</sup><sup>_xi_+1)</sup><sup>_/_2,</sup> _x_<sup>_∗_</sup> _i_ 2<sup>=</sup><sup>_xi_+1to give</sup>


The error of various rules is often quantified as a power of _h_ = _xi_ +1 _− xi_ . The trapezoid rule gives _O_ ( _h_<sup>2</sup> ) while Simpson’s rule gives _O_ ( _h_<sup>4</sup> ).

**Romberg quadrature** There is an extension of Newton-Cotes quadrature that takes combinations of estimates based on different numbers of intervals. This is called Richardson extrapolation and when used with the trapezoidal rule is called _Romberg quadrature_ . The result is greatly increased accuracy. A simple example of this is as follows. Let _T_<sup>ˆ</sup> ( _h_ ) be the trapezoidal rule approximation of the integral when the length of each interval is _h_ . Then<sup>4 ˆ</sup><sup>_T_</sup><sup><u>(</u></sup><sup>_h/_2</sup> 3<sup><u>)</u></sup><sup>_−T_ˆ(</sup><sup>_h_</sup><sup><u>)</u></sup> results in an approximation with error of _O_ ( _h_<sup>4</sup> ) because the differencing is cleverly chosen to kill off the error term that is _O_ ( _h_<sup>2</sup> ) _._ In fact this approximation is Simpson’s rule with intervals of length _h/_ 2, with the advantage that we don’t have to do as many function evaluations (2 _n_ vs. 4 _n_ ). Even better, one can iterate this approach for more accuracy as described in detail in Givens and Hoeting.

Note that at some point, simply making intervals smaller in quadrature will not improve accuracy because of errors introduced by the imprecision of computer numbers.

9

#### **2.1.2 Gaussian quadrature**

Here the idea is to relax the constraints of equally-spaced intervals and nodes within intervals. We want to put more nodes where the function is larger in magnitude.

Gaussian quadrature approximates integrals that are in the form of an expected value as


where _µ_ ( _x_ ) is a probability density, with the requirement that � _xkµ_ ( _x_ ) _dx_ = _EµX k < ∞_ for _k ≥_ 0. Note that it can also deal with indefinite integrals where _a_ = _−∞_ and/or _b_ = _∞_ . Typically _µ_ is non-uniform, so the nodes (the quadrature points) cluster in areas of high density.The choice of node locations depends on understanding orthogonal polynomials, which we won’t go into here.

It turns out this approach can exactly integrate polynomials of degree 2 _m_ + 1 (or lower). The advantage is that for smooth functions that can be approximated well by a single polynomial, we get highly accurate results. The downside is that if the function is not well approximated by such a polynomial, the result may not be so good. The Romberg approach is more robust.

Note that if the problem is not in the form � _ab_<sup>_f_(</sup><sup>_x_)</sup><sup>_µ_(</sup><sup>_x_)</sup><sup>_dx_, but rather</sup> � _ab_<sup>_f_(</sup><sup>_x_)</sup><sup>_dx_, we can reex-</sup> press as � _ab µf_ <u>((</u> _xx_ <u>))</u><sup>_µ_(</sup><sup>_x_)</sup><sup>_dx_.</sup>

Note that the trapezoidal rule amounts to _µ_ being the uniform distribution with the points equally spaced.

#### **2.1.3 Adaptive quadrature**

Adaptive quadrature chooses interval lengths based on the behavior of the integrand. The goal is to have shorter intervals where the function varies more and longer intervals where it varies less. The reason for avoiding short intervals everywhere involves the extra computation and greater opportunity for rounding error.

#### **2.1.4 Higher dimensions**

For rectangular regions, one can use the techniques described above over squares instead of intervals, but things become more difficult with more complicated regions of integration.

The basic result for Monte Carlo integration (i.e., Unit 10 on simulation) is that the error of the MC estimator scales as _O_ ( _m_<sup>_−_1</sup><sup>_/_2</sup> ), where _m_ is the number of MC samples, regardless of dimensionality. Let’s consider how the error of quadrature scales. We’ve seen that the error is often quantified as _O_ ( _h_<sup>_q_</sup> ). In _d_ dimensions, the error is the same as a function of _h_ , but if in one dimension we need _n_ function evaluations to get intervals of length _h_ , in _d_ dimensions, we need _n_<sup>_d_</sup> function evaluations to get hypercubes with sides of length _h_ . Let’s re-express the error in terms

10

of _n_ rather than _h_ based on _h_ = _c/n_ for a constant _c_ (such as _c_ = _b − a_ ), which gives us error of _O_ ( _n_<sup>_−q_</sup> ) for one-dimensional integration. In _d_ dimensions we have _n_<sup>1</sup><sup>_/d_</sup> function evaluations per dimension, so the error for fixed _n_ is _O_ (( _n_<sup>1</sup><sup>_/d_</sup> )<sup>_−q_</sup> ) = _O_ ( _n_<sup>_−q/d_</sup> ) which scales as _n_<sup>_−_1</sup><sup>_/d_</sup> . As an example, suppose _d_ = 10 and we have _n_ = 1000 function evaluations. This gives us an accuracy comparable to one-dimensional integration with _n_ = 1000<sup>1</sup><sup>_/_10</sup> _≈_ 2, which is awful. Even with only _d_ = 4, we get _n_ = 1000<sup>1</sup><sup>_/_4</sup> _≈_ 6, which is pretty bad. This is one version of the curse of dimensionality.

### **2.2 Numerical integration in R**

R implements an adaptive version of Gaussian quadrature in _integrate()_ . The ’...’ argument allows you to pass additional arguments to the function that is being integrated. The function must be vectorized (i.e., accept a vector of inputs and evaluate and return the function value for each input as a vector of outputs).

Note that the domain of integration can be unbounded and if either the upper or lower limit is unbounded, you should enter **Inf** or **-Inf** respectively.

**integrate** (dnorm, -Inf, Inf, 0, .1) ## 1 with absolute error < 6.1e-07 **integrate** (dnorm, -Inf, Inf, 0, .001)

## 1 with absolute error < 2.1e-06

**integrate** (dnorm, -Inf, Inf, 0, .0001) _# THIS FAILS!_ ## 0 with absolute error < 0

### **2.3 Singularities and infinite ranges**

A singularity occurs when the function is unbounded, which can cause difficulties with numerical integration. For example, �01 _~~√~~_ <u>1</u> _<u>x</u>_<sup>=2,but</sup><sup>_f_(0)=</sup><sup>_∞_.One strategy is a change of variables.For</sup> example, to find �01 ex _~~√~~_ <u>p(</u> _<u>xx</u>_ <u>)</u><sup>_dx_, let</sup><sup>_u_=</sup><sup>_√_</sup> _<u>x</u>_ <u>, which gives the integral, 2</u> �01<sup>exp(</sup><sup>_u_2)</sup><sup>_du_.</sup> Another strategy is to subtract off the singularity. E.g., in the example above, reexpress as


11

where we do the second integral analytically. It turns out that the first integral is well-behaved at 0.

exp( _x_ <u>)</u> It turns out that R’s _integrate()_ function can handle �01 _~~√~~_ _<u>x</u>_<sup>_dx_directlywithoutuschanging</sup> the problem statement analytically. Perhaps this has something to do with the use of adaptive quadrature, but I’m not sure. _# doing it directly with integrate()_ f <- **function** (x) **exp** (x)/ **sqrt** (x) **integrate** (f, 0, 1) ## 2.92530349 with absolute error < 9.4e-06 _# subtracting off the singularity_ f <- **function** (x) ( **exp** (x) - 1)/ **sqrt** (x) x <- **seq** (0,1, len = 200) **integrate** (f, 0, 1) ## 0.925303567 with absolute error < 7.6e-05 _# analytic change of variables, followed by numeric integration_ f <- **function** (u) 2* **exp** (u^2) **integrate** (f, 0, 1) ## 2.92530349 with absolute error < 3.2e-14

**Infinite ranges** Gaussian quadrature deals with the case that _a_ = _−∞_ and/or _b_ = _∞_ . Another possibility is change of variables using transformations such as 1 _/x_ , exp( _x_ ) _/_ (1 + exp( _x_ )), exp( _−x_ ), and _x/_ (1 + _x_ ).

### **2.4 Symbolic integration**

Mathematica and Maple are able to do symbolic integration for many problems that are very hard to do by hand (and with the same concerns as when doing differentiation by hand). So this may be worth a try.

---

[← Unit 14: Numerical Integration and Differentiation](01-unit-14-numerical-integration-and-differentiation.md) · [Up: contents](index.md) · [one-dimensional integration Integrate[Sin[x]^2, x] →](03-one-dimensional-integration-integrate-sin-x-2-x.md)
