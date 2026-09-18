---
title: 1 Differentiation
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit12-integ.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit12-integ.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit12-integ.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit12-integ.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Differentiation

November 30, 2021

References:

* Gentle: Computational Statistics
* Monahan: Numerical Methods of Statistics
* Givens and Hoeting: Computational Statistics

Our goal here is to understand the basics of numerical (and symbolic) approaches to approximating derivatives and integrals on a computer. Derivatives are useful primarily for optimization. Integrals arise in approximating expected values and in various places where we need to integrate over an unknown random variable (e.g., Bayesian contexts, random effects models, missing data contexts). For example, consider a Poisson regression model with random effects, $Y_i \sim \text{Poi}(X_i^T \beta + b_i)$. We'd like to estimate $\beta$ by maximizing the marginal likelihood for the vector of observations, $Y$, integrating over the vector of random effects, $b$: $\int f(y, b; \beta)f(b)db$.

## 1.1 Numerical differentiation

There's not much to this topic. The basic idea is to approximate the derivative of interest using finite differences.

A standard discrete approximation of the derivative is the forward difference

$$f'(x) \approx \frac{f(x + h) - f(x)}{h}$$

A more accurate approach is the central difference

$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$$

Provided we already have computed $f(x)$, the forward difference takes half as much computing as the central difference. However, the central difference has an error of $O(h^2)$ while the forward difference has error of $O(h)$.

For second derivatives, if we apply the above approximations to $f'(x)$ and $f'(x+h)$, we get an approximation of the second derivative based on second differences:

$$f''(x) \approx \frac{f'(x + h) - f'(x)}{h} \approx \frac{f(x + 2h) - 2f(x + h) + f(x)}{h^2}.$$

The corresponding central difference approximation is

$$f''(x) \approx \frac{f(x + h) - 2f(x) + f(x - h)}{h^2}.$$

For multivariate $x$, we need to compute directional derivatives. In general these will be in axis-oriented directions (e.g., for the Hessian), but they can be in other directions. The basic idea is to find $f(x + he)$ in expressions such as those above where $e$ is a unit length vector giving the direction. For axis oriented directions, we have $e_i$ being a vector with a one in the $i$th position and zeroes in the other positions,

$$\frac{\partial f}{\partial x_i} \approx \frac{f(x + he_i) - f(x)}{h}.$$

Note that for mixed partial derivatives, we need to use $e_i$ and $e_j$, so the second difference approximation gets a bit more complicated,

$$\frac{\partial^2 f}{\partial x_i \partial x_j} \approx \frac{f(x + he_j + he_i) - f(x + he_j) - f(x + he_i) + f(x)}{h^2}.$$

We would have analogous quantities for central difference approximations.

**Numerical issues** Ideally we would take $h$ very small and get a highly accurate estimate of the derivative. However, the limits of machine precision mean that the difference estimator can behave badly for very small $h$, since we lose accuracy in computing differences such as between $f(x + h)$ and $f(x - h)$. Therefore we accept a bias in the estimate by not using $h$ so small, often by taking $h$ to be square root of machine epsilon (i.e., about $1 \times 10^{-8}$ on most systems). Actually, we need to account for the order of magnitude of $x$, so what we really want is $h = \sqrt{\epsilon} |x|$ - i.e., we want it to be in terms relative to the magnitude of $x$. As an example, recall that if $x = 1 \times 10^9$ and we did $x + h = 1 \times 10^9 + 1 \times 10^{-8}$, we would get $x + h = 1 \times 10^9 = x$ because we can only represent 7 decimal places with precision.

Givens and Hoeting and Monahan point out that some sources recommend the cube root of machine epsilon (about $5 \times 10^{-6}$ on most systems), in particular when approximating second derivatives.

Let's assess these recommendations empirically in R. We'll use a test function, $\log \Gamma(x)$, for which we can obtain the derivatives with high accuracy using built-in R functions. This is a modification of Monahan's example from his *numdif.r* code.

```R
## compute first and second derivatives of log(gamma(x)) at x=1/2
options(digits = 9, width = 120)
h <- 10^(-(1:15))
x <- 1/2
fx <- lgamma(x)
## targets: actual derivatives can be computed very accurately
## using built-in R functions:
digamma(x) # accurate first derivative
## [1] -1.96351003
trigamma(x) # accurate second derivative
## [1] 4.9348022
## calculate discrete differences
fxph <- lgamma(x+h)
fxmh <- lgamma(x-h)
fxp2h <- lgamma(x+2*h)
fxm2h <- lgamma(x-2*h)
## now find numerical derivatives
fp_fwd <- (fxph - fx)/h # forward difference
fp_cent <- (fxph - fxmh)/(2*h) # central difference
## second derivatives
fpp_fwd <- (fxp2h - 2*fxph + fx)/(h*h) # forward difference
fpp_cent <- (fxph - 2*fx + fxmh)/(h*h) # central difference
## table of results
cbind(h,fp_fwd,fp_cent,fpp_fwd,fpp_cent)
## h fp_fwd fp_cent fpp_fwd fpp_cent
## [1,] 1e-01 -1.74131085 -1.99221980 3.67644733e+00 5.01817899e+00
## [2,] 1e-02 -1.93911250 -1.96379057 4.77200996e+00 4.93561416e+00
## [3,] 1e-03 -1.96104543 -1.96351283 4.91803003e+00 4.93481032e+00
## [4,] 1e-04 -1.96326331 -1.96351005 4.93311987e+00 4.93480230e+00
## [5,] 1e-05 -1.96348535 -1.96351003 4.93463270e+00 4.93480257e+00
## [6,] 1e-06 -1.96350756 -1.96351003 4.93505237e+00 4.93483032e+00
## [7,] 1e-07 -1.96350978 -1.96351003 4.91828800e+00 4.95159469e+00
## [8,] 1e-08 -1.96351001 -1.96351003 7.77156117e+00 3.33066907e+00
## [9,] 1e-09 -1.96351002 -1.96351002 -1.11022302e+02 0.00000000e+00
## [10,] 1e-10 -1.96351047 -1.96351047 2.22044605e+04 0.00000000e+00
## [11,] 1e-11 -1.96349603 -1.96350158 -3.33066907e+06 1.11022302e+06
## [12,] 1e-12 -1.96342942 -1.96348493 -1.11022302e+08 1.11022302e+08
## [13,] 1e-13 -1.96398453 -1.96398453 2.22044605e+10 0.00000000e+00
## [14,] 1e-14 -1.96509475 -1.97064587 1.11022302e+12 1.11022302e+12
## [15,] 1e-15 -1.99840144 -1.94289029 0.00000000e+00 -1.11022302e+14
```

What do we conclude about the advice about using $h$ proportional to either the square root or cube root of machine epsilon?

## 1.2 Numerical differentiation in R

There are multiple numerical derivative functions in R. `numericDeriv()` will do the first derivative. It requires an expression rather than a function as the form in which the function is input, which in some cases might be inconvenient. The functions in the `numDeriv` package will compute the gradient and Hessian, either in the standard way (using the argument `method = 'simple'`) or with a more accurate approximation (using the argument `method = 'Richardson'`). For optimization, one might use the simple option, assuming that is faster, while the more accurate approximation might be good for computing the Hessian to approximate the information matrix for getting an asymptotic covariance. (Although in this case, the statistical uncertainty generally will ovewhelm any numerical uncertainty.)

```R
x <- 1/2
numericDeriv(quote(lgamma(x)), "x")
## [1] 0.572364943
## attr(,"gradient")
## [,1]
## [1,] -1.96351001
```

Note that by default, if you rely on numerical derivatives in `optim()`, it uses $h = 0.001$ (the `ndeps` sub-argument to `control`), which might not be appropriate if the parameters vary on a small scale. This relatively large value of $h$ is probably chosen based on `optim()` assuming that you've scaled the parameters as described in the text describing the `parscale` argument.

## 1.3 Symbolic differentiation (optional)

We've seen that we often need the first and second derivatives for optimization. Numerical differentiation is fine, but if we can readily compute the derivatives in closed form, that can improve our optimization. (Venables and Ripley comment that this is particularly the case for the first derivative, but not as much for the second.)

In general, using a computer program to do the analytic differentiation is recommended as it's easy to make errors in doing differentiation by hand. Monahan points out that one of the main causes of error in optimization is human error in coding analytic derivatives, so it's good practice to avoid this. R has a simple differentiation ability in the `deriv()` function (which handles the gradient and the Hessian). However it can only handle a limited number of functions. Here's an example of using `deriv()` and then embedding the resulting R code in a user-defined function. This can be quite handy, though the format of the result in terms of attributes is not the most handy, so you might want to monkey around with the code more in practice.

```R
deriv(quote(atan(x)), "x") # derivative of simple expression

## expression({
## .value <- atan(x)
## .grad <- array(0, c(length(.value), 1L), list(NULL, c("x")))
## .grad[, "x"] <- 1/(1 + x^2)
## attr(.value, "gradient") <- .grad
## .value
## })
## derivative of a function; note we need to pass in an expression,
## not the entire function
f <- function(x,y) sin(x * y)+x^3+exp(y)
newBody <- deriv(body(f), c("x", "y"), hessian = TRUE)
## now create a new version of f that provides gradient
## and hessian as attributes of the output,
## in addition to the function value as the return value
f <- function(x, y) {} # function template
body(f) <- newBody
```

```R
## try out the new function
f(3,1)
## [1] 29.8594018
## attr(,"gradient")
## x y
## [1,] 26.0100075 -0.251695661
## attr(,"hessian")
## , , x
##
## x y
## [1,] 17.85888 -1.41335252
##
## , , y
##
## x y
## [1,] -1.41335252 1.44820176
attr(f(3,1), "gradient")
## x y
## [1,] 26.0100075 -0.251695661
attr(f(3,1), "hessian")
## , , x
##
## x y
## [1,] 17.85888 -1.41335252
##
## , , y
##
## x y
## [1,] -1.41335252 1.44820176
```

For more complicated functions, both Maple and Mathematica do symbolic differentiation. Here are some examples in Mathematica, which is available on the SCF machines and through campus: http://ist.berkeley.edu/software-central:

```mathematica
# first partial derivative wrt x
D[ Exp[x^n] - Cos[x y], x]
# second partial derivative
D[ Exp[x^n] - Cos[x y], {x, 2}]
# partials
D[ Exp[x^n] - Cos[x y], x, y]
# trig function example
D[ ArcTan[x], x]
```

---

[Up: contents](index.md) · [2 Integration (optional) →](02-2-integration-optional.md)
