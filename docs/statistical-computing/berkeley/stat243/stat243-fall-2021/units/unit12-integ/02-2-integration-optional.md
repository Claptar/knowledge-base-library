---
title: 2 Integration (optional)
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit12-integ.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit12-integ.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit12-integ.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit12-integ.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Integration (optional)

We've actually already discussed numerical integration extensively in the simulation unit, where we considered Monte Carlo approximation of high-dimensional integrals. In the case where we have an integral in just one or two dimensions, MC is fine, but we can get highly-accurate, very fast approximations by numerical integration methods known as quadrature. Unfortunately such approximations scale very badly as the dimension grows, while MC methods scale well, so MC is recommended in higher dimensions. Here's an empirical example in R, where the MC estimator is

$$\int_0^\pi \sin(x)dx = \int_0^\pi \pi \sin(x) \left( \frac{1}{\pi} \cdot 1 \right) dx = E_f(\pi \sin(x))$$

for $f = \mathcal{U}(0, \pi)$:

```R
f <- function(x) sin(x)
## mathematically, the integral from 0 to pi is 2
## quadrature through integrate()
integrate(f, 0, pi)
## 2 with absolute error < 2.2e-14
system.time(integrate(f, 0, pi))
## user system elapsed
## 0.001 0.000 0.001
## MC estimate
ninteg <- function(n) mean(sin(runif(n, 0, pi))*pi)
n <- 1000
ninteg(n)
```

```R
## [1] 2.02086145
system.time(ninteg(n))
## user system elapsed
## 0.002 0.000 0.003
n <- 10000
ninteg(n)
## [1] 2.00115929
system.time(ninteg(n))
## user system elapsed
## 0.001 0.000 0.000
n <- 1000000
ninteg(n)
## [1] 1.99795757
system.time(ninteg(n))
## user system elapsed
## 0.052 0.000 0.052
## that was fairly slow,
## especially if you need to do a lot of individual integrals
```

More on this issue below.

## 2.1 Numerical integration methods

The basic idea is to break the domain into pieces and approximate the integral within each piece:

$$\int_a^b f(x)dx = \sum_{i=0}^{n-1} \int_{x_i}^{x_{i+1}} f(x)dx,$$

where we then approximate $\int_{x_i}^{x_{i+1}} f(x)dx \approx \sum_{j=0}^m A_{ij} f(x_{ij}^*)$ where $x_{ij}^*$ are the nodes.

### 2.1.1 Newton-Cotes quadrature

Newton-Cotes quadrature has equal length intervals of length $h = (b-a)/n$, with the same number of nodes in each interval. $f(x)$ is replaced with a polynomial approximation in each interval and $A_{ij}$ are chosen so that the sum equals the integral of the polynomial approximation on the interval.

A basic example is the Riemann rule, which takes a single node, $x_i^* = x_i$ and the "polynomial" is a constant, $f(x_i^*)$, so we have

$$\int_{x_i}^{x_{i+1}} f(x)dx \approx (x_{i+1} - x_i)f(x_i).$$

Of course using a piecewise constant to approximate $f(x)$ is not likely to give us high accuracy. The trapezoidal rule takes $x_{i0}^* = x_i$, $x_{i1}^* = x_{i+1}$ and uses a linear interpolation between $f(x_{i0}^*)$ and $f(x_{i1}^*)$ to give

$$\int_{x_i}^{x_{i+1}} f(x)dx \approx \left( \frac{x_{i+1} - x_i}{2} \right) (f(x_i) + f(x_{i+1})).$$

Simpson's rule uses a quadratic interpolation at the points $x_{i0}^* = x_i$, $x_{i1}^* = (x_i + x_{i+1})/2$, $x_{i2}^* = x_{i+1}$ to give

$$\int_{x_i}^{x_{i+1}} f(x)dx \approx \left( \frac{x_{i+1} - x_i}{6} \right) \left( f(x_i) + 4f\left( \frac{x_i + x_{i+1}}{2} \right) + f(x_{i+1}) \right).$$

The error of various rules is often quantified as a power of $h = x_{i+1} - x_i$. The trapezoid rule gives $O(h^2)$ while Simpson's rule gives $O(h^4)$.

**Romberg quadrature** There is an extension of Newton-Cotes quadrature that takes combinations of estimates based on different numbers of intervals. This is called Richardson extrapolation and when used with the trapezoidal rule is called Romberg quadrature. The result is greatly increased accuracy. A simple example of this is as follows. Let $\hat{T}(h)$ be the trapezoidal rule approximation of the integral when the length of each interval is $h$. Then $\frac{4\hat{T}(h/2) - \hat{T}(h)}{3}$ results in an approximation with error of $O(h^4)$ because the differencing is cleverly chosen to kill off the error term that is $O(h^2)$. In fact this approximation is Simpson's rule with intervals of length $h/2$, with the advantage that we don't have to do as many function evaluations ($2n$ vs. $4n$). Even better, one can iterate this approach for more accuracy as described in detail in Givens and Hoeting.

Note that at some point, simply making intervals smaller in quadrature will not improve accuracy because of errors introduced by the imprecision of computer numbers.

### 2.1.2 Gaussian quadrature

Here the idea is to relax the constraints of equally-spaced intervals and nodes within intervals. We want to put more nodes where the function is larger in magnitude.

Gaussian quadrature approximates integrals that are in the form of an expected value as

$$\int_a^b f(x)\mu(x)dx \approx \sum_{i=0}^m w_i f(x_i)$$

where $\mu(x)$ is a probability density, with the requirement that $\int x^k \mu(x)dx = E_\mu X^k < \infty$ for $k \ge 0$. Note that it can also deal with indefinite integrals where $a = -\infty$ and/or $b = \infty$. Typically $\mu$ is non-uniform, so the nodes (the quadrature points) cluster in areas of high density. The choice of node locations depends on understanding orthogonal polynomials, which we won't go into here.

It turns out this approach can exactly integrate polynomials of degree $2m + 1$ (or lower). The advantage is that for smooth functions that can be approximated well by a single polynomial, we get highly accurate results. The downside is that if the function is not well approximated by such a polynomial, the result may not be so good. The Romberg approach is more robust.

Note that if the problem is not in the form $\int_a^b f(x)\mu(x)dx$, but rather $\int_a^b f(x)dx$, we can reexpress as $\int_a^b \frac{f(x)}{\mu(x)}\mu(x)dx$.

Note that the trapezoidal rule amounts to $\mu$ being the uniform distribution with the points equally spaced.

### 2.1.3 Adaptive quadrature

Adaptive quadrature chooses interval lengths based on the behavior of the integrand. The goal is to have shorter intervals where the function varies more and longer intervals where it varies less. The reason for avoiding short intervals everywhere involves the extra computation and greater opportunity for rounding error.

### 2.1.4 Higher dimensions

For rectangular regions, one can use the techniques described above over squares instead of intervals, but things become more difficult with more complicated regions of integration.

The basic result for Monte Carlo integration (i.e., Unit 10 on simulation) is that the error of the MC estimator scales as $O(m^{-1/2})$, where $m$ is the number of MC samples, regardless of dimensionality. Let's consider how the error of quadrature scales. We've seen that the error is often quantified as $O(h^q)$. In $d$ dimensions, the error is the same as a function of $h$, but if in one dimension we need $n$ function evaluations to get intervals of length $h$, in $d$ dimensions, we need $n^d$ function evaluations to get hypercubes with sides of length $h$. Let's re-express the error in terms of $n$ rather than $h$ based on $h = c/n$ for a constant $c$ (such as $c = b - a$), which gives us error of $O(n^{-q})$ for one-dimensional integration. In $d$ dimensions we have $n^{1/d}$ function evaluations per dimension, so the error for fixed $n$ is $O((n^{1/d})^{-q}) = O(n^{-q/d})$ which scales as $n^{-1/d}$. As an example, suppose $d = 10$ and we have $n = 1000$ function evaluations. This gives us an accuracy comparable to one-dimensional integration with $n = 1000^{1/10} \approx 2$, which is awful. Even with only $d = 4$, we get $n = 1000^{1/4} \approx 6$, which is pretty bad. This is one version of the curse of dimensionality.

## 2.2 Numerical integration in R

R implements an adaptive version of Gaussian quadrature in `integrate()`. The '...' argument allows you to pass additional arguments to the function that is being integrated. The function must be vectorized (i.e., accept a vector of inputs and evaluate and return the function value for each input as a vector of outputs).

Note that the domain of integration can be unbounded and if either the upper or lower limit is unbounded, you should enter `Inf` or `-Inf` respectively.

```R
integrate(dnorm, -Inf, Inf, 0, .1)
## 1 with absolute error < 6.1e-07
integrate(dnorm, -Inf, Inf, 0, .001)
## 1 with absolute error < 2.1e-06
integrate(dnorm, -Inf, Inf, 0, .0001) # THIS FAILS!
## 0 with absolute error < 0
```

## 2.3 Singularities and infinite ranges

A singularity occurs when the function is unbounded, which can cause difficulties with numerical integration. For example, $\int_0^1 \frac{1}{\sqrt{x}} = 2$, but $f(0) = \infty$. One strategy is a change of variables. For example, to find $\int_0^1 \frac{\exp(x)}{\sqrt{x}} dx$, let $u = \sqrt{x}$, which gives the integral, $2 \int_0^1 \exp(u^2)du$.

Another strategy is to subtract off the singularity. E.g., in the example above, reexpress as

$$\int_0^1 \frac{\exp(x) - 1}{\sqrt{x}} dx + \int_0^1 \frac{1}{\sqrt{x}} dx = \int_0^1 \frac{\exp(x) - 1}{\sqrt{x}} dx + 2$$

where we do the second integral analytically. It turns out that the first integral is well-behaved at 0.

It turns out that R's `integrate()` function can handle $\int_0^1 \frac{\exp(x)}{\sqrt{x}} dx$ directly without us changing the problem statement analytically. Perhaps this has something to do with the use of adaptive quadrature, but I'm not sure.

```R
## doing it directly with integrate()
f <- function(x)
exp(x)/sqrt(x)
integrate(f, 0, 1)
## 2.92530349 with absolute error < 9.4e-06
## subtracting off the singularity
f <- function(x) (exp(x) - 1)/sqrt(x)
x <- seq(0,1, len = 200)
integrate(f, 0, 1)
## 0.925303567 with absolute error < 7.6e-05
## analytic change of variables, followed by numeric integration
f <- function(u)
2*exp(u^2)
integrate(f, 0, 1)
## 2.92530349 with absolute error < 3.2e-14
### 2.4 Symbolic integration
### in Mathematica
### one-dimensional integration
# Integrate[Sin[x]^2, x]
### two-dimensional integration
# Integrate[Sin[x] Exp[-y^2], x, y]
```

**Infinite ranges** Gaussian quadrature deals with the case that $a = -\infty$ and/or $b = \infty$. Another possibility is change of variables using transformations such as $1/x$, $\exp(x)/(1 + \exp(x))$, $\exp(-x)$, and $x/(1 + x)$.

## 2.4 Symbolic integration

Mathematica and Maple are able to do symbolic integration for many problems that are very hard to do by hand (and with the same concerns as when doing differentiation by hand). So this may be worth a try.

```mathematica
# one-dimensional integration
Integrate[Sin[x]^2, x]
# two-dimensional integration
Integrate[Sin[x] Exp[-y^2], x, y]
```

---

[← 1 Differentiation](01-1-differentiation.md) · [Up: contents](index.md)
