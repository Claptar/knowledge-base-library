---
title: 'Unit 12: Numerical Integration and Differentiation'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit12-integ.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit12-integ.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 12: Numerical Integration and Differentiation

**Source:** [`units/unit12-integ.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit12-integ.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

November 25, 2020

References:

- Gentle: Computational Statistics

- Monahan: Numerical Methods of Statistics

- Givens and Hoeting: Computational Statistics

Our goal here is to understand the basics of numerical (and symbolic) approaches to approximating derivatives and integrals on a computer. Derivatives are useful primarily for optimization. Integrals arise in approximating expected values and in various places where we need to integrate over an unknown random variable (e.g., Bayesian contexts, random effects models, missing data contexts). For example, consider a Poisson regression model with random effects, _Yi ∼_ Poi( _Xi_<sup>_⊤β_+</sup><sup>_bi_).We’d like to estimate</sup><sup>_β_by maximizing the marginal likelihood for the vector</sup> of observations, _Y_ , integrating over the vector of random effects, _b_ : � _f_ ( _y, b_ ; _β_ ) _f_ ( _b_ ) _db_ .

## **1 Differentiation**

### **1.1 Numerical differentiation**

There’s not much to this topic. The basic idea is to approximate the derivative of interest using finite differences.

A standard discrete approximation of the derivative is the forward difference


A more accurate approach is the central difference


1

Provided we already have computed _f_ ( _x_ ), the forward difference takes half as much computing as the central difference. However, the central difference has an error of _O_ ( _h_<sup>2</sup> ) while the forward difference has error of _O_ ( _h_ ).

For second derivatives, if we apply the above approximations to _f_<sup>_′_</sup> ( _x_ ) and _f_<sup>_′_</sup> ( _x_ + _h_ ), we get an approximation of the second derivative based on second differences:


The corresponding central difference approximation is


For multivariate _x_ , we need to compute directional derivatives. In general these will be in axis-oriented directions (e.g., for the Hessian), but they can be in other directions. The basic idea is to find _f_ ( _x_ + _he_ ) in expressions such as those above where _e_ is a unit length vector giving the direction. For axis oriented directions, we have _ei_ being a vector with a one in the _i_ th position and zeroes in the other positions,


Note that for mixed partial derivatives, we need to use _ei_ and _ej_ , so the second difference approximation gets a bit more complicated,


We would have analogous quantities for central difference approximations.

**Numerical issues** Ideally we would take _h_ very small and get a highly accurate estimate of the derivative. However, the limits of machine precision mean that the difference estimator can behave badly for very small _h_ , since we lose accuracy in computing differences such as between _f_ ( _x_ + _h_ ) and _f_ ( _x − h_ ). Therefore we accept a bias in the estimate by not using _h_ so small, often by taking _h_ to be square root of machine epsilon (i.e., about 1 _×_ 10<sup>_−_8</sup> on most systems). Actually, we need to account for the order of magnitude of _x_ , so what we really want is _h_ =<sup>_√_</sup> _<u>ϵ|x|</u>_ - i.e., we want it to be in terms relative to the magnitude of _x_ . As an example, recall that if _x_ = 1 _×_ 10<sup>9</sup> and we did _x_ + _h_ = 1 _×_ 10<sup>9</sup> + 1 _×_ 10<sup>_−_8</sup> , we would get _x_ + _h_ = 1 _×_ 10<sup>9</sup> = _x_ because we can only represent 7 decimal places with precision.

Givens and Hoeting and Monahan point out that some sources recommend the cube root of machine epsilon (about 5 _×_ 10<sup>_−_6</sup> on most systems), in particular when approximating second

2

derivatives.

Let’s assess these recommendations empirically in R. We’ll use a test function, log Γ( _x_ ), for which we can obtain the derivatives with high accuracy using built-in R functions. This is a modification of Monahan’s example from his _numdif.r_ code.

_## compute first and second derivatives of log(gamma(x)) at x=1/2_ **options** (digits = 9, width = 120) h <- 10^(-(1:15)) x <- 1/2 fx <- **lgamma** (x) _## targets: actual derivatives can be computed very accurately ## using built-in R functions:_ **digamma** (x) _# accurate first derivative_ ## [1] -1.96351003 **trigamma** (x) _# accurate second derivative_ ## [1] 4.9348022 _## calculate discrete differences_ fxph <- **lgamma** (x+h) fxmh <- **lgamma** (x-h) fxp2h <- **lgamma** (x+2*h) fxm2h <- **lgamma** (x-2*h) _## now find numerical derivatives_ fp_fwd <- (fxph - fx)/h _# forward difference_ fp_cent <- (fxph - fxmh)/(2*h) _# central difference ## second derivatives_ fpp_fwd <- (fxp2h - 2*fxph + fx)/(h*h) _# forward difference_ fpp_cent <- (fxph - 2*fx + fxmh)/(h*h) _# central difference ## table of results_ **cbind** (h,fp_fwd,fp_cent,fpp_fwd,fpp_cent) ## h fp_fwd fp_cent fpp_fwd fpp_cent ## [1,] 1e-01 -1.74131085 -1.99221980 3.67644733e+00 5.01817899e+00 ## [2,] 1e-02 -1.93911250 -1.96379057 4.77200996e+00 4.93561416e+00 ## [3,] 1e-03 -1.96104543 -1.96351283 4.91803003e+00 4.93481032e+00

3

## [4,] 1e-04 -1.96326331 -1.96351005 4.93311987e+00 4.93480230e+00 ## [5,] 1e-05 -1.96348535 -1.96351003 4.93463270e+00 4.93480257e+00 ## [6,] 1e-06 -1.96350756 -1.96351003 4.93505237e+00 4.93483032e+00 ## [7,] 1e-07 -1.96350978 -1.96351003 4.91828800e+00 4.95159469e+00 ## [8,] 1e-08 -1.96351001 -1.96351003 7.77156117e+00 3.33066907e+00 ## [9,] 1e-09 -1.96351002 -1.96351002 -1.11022302e+02 0.00000000e+00 ## [10,] 1e-10 -1.96351047 -1.96351047 2.22044605e+04 0.00000000e+00 ## [11,] 1e-11 -1.96349603 -1.96350158 -3.33066907e+06 1.11022302e+06 ## [12,] 1e-12 -1.96342942 -1.96348493 -1.11022302e+08 1.11022302e+08 ## [13,] 1e-13 -1.96398453 -1.96398453 2.22044605e+10 0.00000000e+00 ## [14,] 1e-14 -1.96509475 -1.97064587 1.11022302e+12 1.11022302e+12 ## [15,] 1e-15 -1.99840144 -1.94289029 0.00000000e+00 -1.11022302e+14

What do we conclude about the advice about using _h_ proportional to either the square root or cube root of machine epsilon?

### **1.2 Numerical differentiation in R**

There are multiple numerical derivative functions in R. _numericDeriv()_ will do the first derivative. It requires an expression rather than a function as the form in which the function is input, which in some cases might be inconvenient. The functions in the _numDeriv_ package will compute the gradient and Hessian, either in the standard way (using the argument method = ’simple’) or with a more accurate approximation (using the argument method = ’Richardson’). For optimization, one might use the simple option, assuming that is faster, while the more accurate approximation might be good for computing the Hessian to approximate the information matrix for getting an asymptotic covariance. (Although in this case, the statistical uncertainty generally will ovewhelm any numerical uncertainty.)

x <- 1/2 **numericDeriv** ( **quote** ( **lgamma** (x)), "x") ## [1] 0.572364943 ## attr(,"gradient") ## [,1] ## [1,] -1.96351001

Note that by default, if you rely on numerical derivatives in _optim()_ , it uses _h_ = 0 _._ 001 (the _ndeps_ sub-argument to _control_ ), which might not be appropriate if the parameters vary on a small

4

scale. This relatively large value of _h_ is probably chosen based on _optim()_ assuming that you’ve scaled the parameters as described in the text describing the _parscale_ argument.

### **1.3 Symbolic differentiation (optional)**

We’ve seen that we often need the first and second derivatives for optimization. Numerical differentiation is fine, but if we can readily compute the derivatives in closed form, that can improve our optimization. (Venables and Ripley comment that this is particularly the case for the first derivative, but not as much for the second.)

In general, using a computer program to do the analytic differentiation is recommended as it’s easy to make errors in doing differentiation by hand. Monahan points out that one of the main causes of error in optimization is human error in coding analytic derivatives, so it’s good practice to avoid this. R has a simple differentiation ability in the _deriv()_ function (which handles the gradient and the Hessian). However it can only handle a limited number of functions. Here’s an example of using _deriv()_ and then embedding the resulting R code in a user-defined function. This can be quite handy, though the format of the result in terms of attributes is not the most handy, so you might want to monkey around with the code more in practice.

**deriv** ( **quote** ( **atan** (x)), "x") _# derivative of simple expression_ ## expression({ ## .value <- atan(x) ## .grad <- array(0, c(length(.value), 1L), list(NULL, c("x"))) ## .grad[, "x"] <- 1/(1 + x^2) ## attr(.value, "gradient") <- .grad ## .value ## }) _## derivative of a function; note we need to pass in an expression, ## not the entire function_ f <- **function** (x,y) **sin** (x * y)+x^3+ **exp** (y) newBody <- **deriv** ( **body** (f), **c** ("x", "y"), hessian = TRUE) _## now create a new version of f that provides gradient ## and hessian as attributes of the output, ## in addition to the function value as the return value_ f <- **function** (x, y) {} _# function template_ **body** (f) <- newBody

5

_## try out the new function_ **f** (3,1) ## [1] 29.8594018 ## attr(,"gradient") ## x y ## [1,] 26.0100075 -0.251695661 ## attr(,"hessian") ## , , x ## ## x y ## [1,] 17.85888 -1.41335252 ## ## , , y ## ## x y ## [1,] -1.41335252 1.44820176 **attr** ( **f** (3,1), "gradient") ## x y ## [1,] 26.0100075 -0.251695661 **attr** ( **f** (3,1), "hessian") ## , , x ## ## x y ## [1,] 17.85888 -1.41335252 ## ## , , y ## ## x y ## [1,] -1.41335252 1.44820176

For more complicated functions, both Maple and Mathematica do symbolic differentiation. Here are some examples in Mathematica, which is available on the SCF machines and through campus: http://ist.berkeley.edu/software-central:

6

---

[Up: contents](index.md) · [Unit 12 — integ Part 02 — →](02-unit-12-integ-part-02.md)
