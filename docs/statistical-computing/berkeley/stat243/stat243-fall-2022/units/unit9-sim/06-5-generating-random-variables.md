---
title: 5. Generating random variables
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit9-sim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Generating random variables

**Source:** [`units/unit9-sim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

There are a variety of methods for generating from common distributions
(normal, gamma, beta, Poisson, t, etc.). Since these tend to be built
into R and presumably use good algorithms, we won't go into them. A
variety of statistical computing and Monte Carlo books describe the
various methods. Many are built on the relationships between different
distributions - e.g., a beta random variable (RV) can be generated from
two gamma RVs.

Also note that you can call the C functions that implement the R
distribution functions as a library (*Rmath*), so if you're coding in C
or another language, you should be able to make use of the standard
functions: *{r,p,q,d}{norm,t,gamma,binom,pois,etc.}* (as well as a
variety of other R math functions, which can be seen in *Rmath.h*). Information on
this can be found in the *Writing R Extensions* manual on CRAN (section
6.16).

## Multivariate distributions

The *mvtnorm* package supplies code for working with the density and CDF
of multivariate normal and t distributions.

To generate a multivariate normal, in Unit 10, we'll see the standard
method based on the Cholesky decomposition:

```r
U <- chol(covMat)
crossprod(U, rnorm(nrow(covMat)))
```


Side note: for a singular covariance matrix we can use the Cholesky with
pivoting, setting as many rows to zero as the rank deficiency. Then when
we generate the multivariate normals, they respect the constraints
implicit in the rank deficiency. However, you'll need to reorder the
resulting vector because of the reordering involved in the pivoted
Cholesky.

## Inverse CDF

Most of you know the inverse CDF method. To generate $X\sim F$ where $F$
is a CDF and is an invertible function, first generate
$Z\sim\mathcal{U}(0,1)$, then $x=F^{-1}(z)$. For discrete CDFs, one can
work with a discretized version. For multivariate distributions, one can
work with a univariate marginal and then a sequence of univariate
conditionals:
$f(x_{1})f(x_{2}|x_{1})\cdots f(x_{k}|x_{k-1},\ldots,x_{1})$, when the
distribution allows this analytic decomposition.

## Rejection sampling

The basic idea of rejection sampling (RS) relies on the introduction of
an auxiliary variable, $u$. Suppose $X\sim F$. Then we can write
$f(x)=\int_{0}^{f(x)}du$. Thus $f$ is the marginal density of $X$ in the
joint density, $(X,U)\sim\mathcal{U}\{(x,u):0<u<f(x)\}$. Now we'd like
to use this in a way that relies only on evaluating $f(x)$ without
having to draw from $f$.

To implement this we draw from a larger set and then only keep draws for
which $u<f(x)$. We choose a density, $g$, that is easy to draw from and
that can *majorize* $f$, which means there exists a constant $c$ s.t. ,
$cg(x)\geq f(x)$ $\forall x$. In other words we have that $cg(x)$ is an
upper envelope for $f(x)$. The algorithm is

1.  generate $x\sim g$
2.  generate $u\sim\mathcal{U}(0,1)$
3.  if $u\leq f(x)/cg(x)$ then use $x$; otherwise go back to step 1

The intuition here is graphical: we generate from under a curve that is
always above $f(x)$ and accept only when $u$ puts us under $f(x)$
relative to the majorizing density. A key here is that the majorizing
density have fatter tails than the density of interest, so that the
constant $c$ can exist. So we could use a $t$ to generate from a normal
but not the reverse. We'd like $c$ to be small to reduce the number of
rejections because it turns out that
$\frac{1}{c}=\frac{\int f(x)dx}{\int cg(x)dx}$ is the acceptance
probability. This approach works in principle for multivariate densities
but as the dimension increases, the proportion of rejections grows,
because more of the volume under $cg(x)$ is above $f(x)$.

If $f$ is costly to evaluate, we can sometimes reduce calculation using
a lower bound on $f$. In this case we accept if
$u\leq f_{\mbox{low}}(y)/cg_{Y}(y)$. If it is not, then we need to
evaluate the ratio in the usual rejection sampling algorithm. This is
called squeezing.

One example of RS is to sample from a truncated normal. Of course we can
just sample from the normal and then reject, but this can be
inefficient, particularly if the truncation is far in the tail (a case
in which inverse CDF suffers from numerical difficulties). Suppose the
truncation point is greater than zero. Working with the standardized
version of the normal, you can use an translated exponential with lower
end point equal to the truncation point as the majorizing density
(Robert 1995; Statistics and Computing, and see calculations in the demo
code). For truncation less than zero, just make the values negative.

## Adaptive rejection sampling (optional)

The difficulty of RS is finding a good enveloping function. Adaptive
rejection sampling refines the envelope as the draws occur, in the case
of a continuous, differentiable, log-concave density. The basic idea
considers the log of the density and involves using tangents or secants
to define an upper envelope and secants to define a lower envelope for a
set of points in the support of the distribution. The result is that we
have piecewise exponentials (since we are exponentiating from straight
lines on the log scale) as the bounds. We can sample from the upper
envelope based on sampling from a discrete distribution and then the
appropriate exponential. The lower envelope is used for squeezing. We
add points to the set that defines the envelopes whenever we accept a
point that requires us to evaluate $f(x)$ (the points that are accepted
based on squeezing are not added to the set).

## Importance sampling

Importance sampling (IS) allows us to estimate expected values, with
some commonalities with rejection sampling.

$$\phi=E_{f}(h(X))=\int h(x)\frac{f(x)}{g(x)}g(x)dx$$ so
$\hat{\phi}=\frac{1}{m}\sum_{i}h(x_{i})\frac{f(x_{i})}{g(x_{i})}$ for
$x_{i}$ drawn from $g(x)$, where $w_{i}=f(x_{i})/g(x_{i})$ act as
weights. (Often in Bayesian contexts, we know $f(x)$ only up to a
normalizing constant. In this case we need to use
$w_{i}^{*}=w_{i}/\sum_{j}w_{j}$.

Here we don't require the majorizing property, just that the densities
have common support, but things can be badly behaved if we sample from a
density with lighter tails than the density of interest. So in general
we want $g$ to have heavier tails. More specifically for a low variance
estimator of $\phi$, we would want that $f(x_{i})/g(x_{i})$ is large
only when $h(x_{i})$ is very small, to avoid having overly influential
points.

This suggests we can reduce variance in an IS context by oversampling
$x$ for which $h(x)$ is large and undersampling when it is small, since
$\mbox{Var}(\hat{\phi})=\frac{1}{m}\mbox{Var}(h(X)\frac{f(X)}{g(X)})$.
An example is that if $h$ is an indicator function that is 1 only for
rare events, we should oversample rare events and then the IS estimator
corrects for the oversampling.

What if we actually want a sample from $f$ as opposed to estimating the
expected value above? We can draw $x$ from the unweighted sample,
$\{x_{i}\}$, with weights $\{w_{i}\}$. This is called sampling
importance resampling (SIR).

## Ratio of uniforms (optional)

If $U$ and $V$ are uniform in $C=\{(u,v):\,0\leq u\leq\sqrt{f(v/u)}$
then $X=V/U$ has density proportion to $f$. The basic algorithm is to
choose a rectangle that encloses $C$ and sample until we find
$u\leq f(v/u)$. Then we use $x=v/u$ as our RV. The larger region
enclosing $C$ is the majorizing region and a simple approach (if
$f(x)$and $x^{2}f(x)$ are bounded in $C$) is to choose the rectangle,
$0\leq u\leq\sup_{x}\sqrt{f(x)}$,
$\inf_{x}x\sqrt{f(x)}\leq v\leq\sup_{x}x\sqrt{f(x)}$.

One can also consider truncating the rectangular region, depending on
the features of $f$.

Monahan recommends the ratio of uniforms, particularly a version for
discrete distributions (p. 323 of the 2nd edition).

---

[← 4. Random number generation (RNG)](05-4-random-number-generation-rng.md) · [Up: contents](index.md)
