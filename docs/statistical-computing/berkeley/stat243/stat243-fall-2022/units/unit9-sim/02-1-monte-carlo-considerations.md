---
title: 1. Monte Carlo considerations
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit9-sim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Monte Carlo considerations

**Source:** [`units/unit9-sim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Motivating example

Let's consider linear regression, with observations
$Y=(y_{1},y_{2},\ldots,y_{n})$ and an $n\times p$ matrix of predictors/covariates/features/variables
$X$, where
$\hat{\beta}=(X^{\top}X)^{-1}X^{\top}Y$. If we assume that we have
$EY=X\beta$ and $\mbox{Var}(Y)=\sigma^{2}I$, then we can determine
analytically that we have $$\begin{aligned}
E\hat{\beta} & = & \beta\\
\mbox{Var}(\hat{\beta})=E((\hat{\beta}-E\hat{\beta})^{2}) & = & \sigma^{2}(X^{\top}X)^{-1}\\
\mbox{MSPE}(Y^{*})=E(Y^{*}-\hat{Y})^{2}) & = & \sigma^{2}(1+X^{*\top}(X^{\top}X)^{-1}X^{*}).\end{aligned}$$
where $Y^{*}$is some new observation we'd like to predict given $X^{*}$.

But suppose that we're interested in the properties of regression
estimation when in reality the mean is not linear in $X$ or the
properties of the errors are more complicated than having independent
homoscedastic errors. (This is always the case, but the issue is how far
from the truth the standard assumptions are.) Or suppose we have a modified procedure to produce
$\hat{\beta}$, such as a procedure that is robust to outliers. In those
cases, we cannot compute the expectations above analytically.

Instead we decide to use a Monte Carlo estimate. To keep the notation
more simple, let's just consider one element of the vector $\beta$
(i.e., one of the regression coefficients) and continue to call that
$\beta$. If we randomly generate $m$ different datasets from some
distribution $f$, and $\hat{\beta}_{i}$ is the estimated coefficient
based on the $i$th dataset: $Y_{i}=(y_{i1},y_{i2},\ldots,y_{in})$, then
we can estimate $E\hat{\beta}$ under that distribution $f$ as
$$\widehat{E(\hat{\beta})}=\bar{\hat{\beta}}=\frac{1}{m}\sum_{i=1}^{m}\hat{\beta}_{i}$$
Or to estimate the variance, we have
$$\widehat{\mbox{Var}(\hat{\beta})}=\frac{1}{m}\sum_{i=1}^{m}(\hat{\beta}_{i}-\bar{\hat{\beta}})^{2}.$$
In evaluating the performance of regression under non-standard
conditions or the performance of our robust regression procedure, what
decisions do we have to make to be able to carry out our Monte Carlo
procedure?

Next let's think about Monte Carlo methods in general.

## Monte Carlo (MC) basics

### Monte Carlo overview

The basic idea is that we often want to estimate
$\phi\equiv E_{f}(h(Y))$ for $Y\sim f$. Note that if $h$ is an indicator
function, this includes estimation of probabilities, e.g., for a scalar
$Y$, we have
$p=P(Y\leq y)=F(y)=\int_{-\infty}^{y}f(t)dt=\int I(t\leq y)f(t)dt=E_{f}(I(Y\leq y))$.
We would estimate variances or MSEs by having $h$ involve squared terms.

We get an MC estimate of $\phi$ based on an iid sample of a large number
of values of $Y$ from $f$:
$$\hat{\phi}=\frac{1}{m}\sum_{i=1}^{m}h(Y_{i}),$$ which is justified by
the Law of Large Numbers:
$$\lim_{m\to\infty}\frac{1}{m}\sum_{i=1}^{m}h(Y_{i})=E_{f}h(Y).$$

Note that in most simulation studies, $Y$ is an entire dataset (predictors/covariates), and the "iid
sample" means generating $m$ different datasets from $f$, i.e.,
$Y_{i}\in\{Y_{1},\ldots,Y_{m}\}$ not $m$ different scalar values. If the
dataset has $n$ observations, then $Y_{i}=(Y_{i1},\ldots,Y_{in})$.

#### Back to the regression example

Let's relate that back to our regression example. In that particular
case, if we're interested in whether the regression estimator is biased,
we want to know: $$\phi=E\hat{\beta},$$ where $h(Y) = \hat(\beta)$. We can use the Monte Carlo
estimate of $\phi$:
$$\hat{\phi}=\frac{1}{m}\sum_{i=1}^{m}h(Y_{i})=\frac{1}{m}\sum_{i=1}^{m}\hat{\beta}_{i}=\widehat{E(\hat{\beta})}.$$
For the variance, we have

$$\phi=\mbox{Var}(\hat{\beta})=E_{f}((\hat{\beta}-E\hat{\beta})^{2})$$
and we can use the Monte Carlo estimate of $\phi$:
$$\hat{\phi}=\frac{1}{m}\sum_{i=1}^{m}h(Y_{i})=\frac{1}{m}\sum_{i=1}^{m}(\hat{\beta}_{i}-E\hat{\beta})^{2}=\widehat{\mbox{Var}(\hat{\beta)}}$$
where $$h(Y)=(\hat{\beta}-E\hat{\beta})^{2}.$$

Finally note that we also need to use the Monte Carlo estimate of
$E\hat{\beta}$ in the Monte Carlo estimation of the variance.

We might also be interested in the coverage of a confidence interval. In
that case we have $$h(Y)=1_{\beta\in CI(Y)}$$ and we can estimate the
coverage as
$$\hat{\phi}=\frac{1}{m}\sum_{i=1}^{m}1_{\beta\in CI(y_{i})}.$$
Of course we want that $\hat{\phi}\approx1-\alpha$ for a $100(1-\alpha)$
confidence interval. In the standard case of a 95% interval we want
$\hat{\phi}\approx0.95$.

### Simulation uncertainty

Since $\hat{\phi}$ is simply an average of $m$ identically-distributed
values, $h(Y_{1}),\ldots,h(Y_{m})$, the simulation variance of
$\hat{\phi}$ is $\mbox{Var}(\hat{\phi})=\sigma^{2}/m$, with
$\sigma^{2}=\mbox{Var}(h(Y))$. An estimator of
$\sigma^{2}=E_{f}((h(Y)-\phi)^{2})$ is $$\begin{aligned}
\hat{\sigma}^{2} & = & \frac{1}{m-1}\sum_{i=1}^{m}(h(Y_{i})-\hat{\phi})^{2}\end{aligned}$$
So our MC simulation error is based on
$$\widehat{\mbox{Var}}(\hat{\phi})=\frac{\hat{\sigma}^{2}}{m}=\frac{1}{m(m-1)}\sum_{i=1}^{m}(h(Y_{i})-\hat{\phi})^{2}.$$
Note that this is particularly confusing if we have
$\hat{\phi}=\widehat{\mbox{Var}(\hat{\beta})}$ because then we have
$\widehat{\mbox{Var}}(\hat{\phi})=\widehat{\mbox{Var}}(\widehat{\mbox{Var}(\hat{\beta})})$!

The simulation variance is $O(\frac{1}{m})$ because we have $m^{2}$ in
the denominator and a sum over $m$ terms in the numerator.

Note that in the simulation setting, the randomness in the system is
very well-defined (as it is in survey sampling, but unlike in most other
applications of statistics), because it comes from the RNG that we
perform as part of our attempt to estimate $\phi$. Happily, we are in
control of $m$, so in principle we can reduce the simulation error to as
little as we desire. Unhappily, as usual, the standard error goes down
with the square root of $m$.

#### Back to the regression example

Some examples of simulation variances we might be interested in in the
regression example include:

-   Uncertainty in our estimate of bias:
    $\widehat{\mbox{Var}}(\widehat{E(\hat{\beta})}-\beta)$.

-   Uncertainty in the estimated variance of the estimated coefficient:
    $\widehat{\mbox{Var}}(\widehat{\mbox{Var}(\hat{\beta})})$.

-   Uncertainty in the estimated mean square prediction error:
    $\widehat{\mbox{Var}}(\widehat{\mbox{MSPE}(Y^{*})})$.

In all cases we have to estimate the simulation variance, hence the
$\widehat{\mbox{Var}}()$ notation.

### Final notes

Sometimes the $Y_{i}$ are generated in a dependent fashion (e.g.,
sequential MC or MCMC), in which case this variance estimator,
$\widehat{\mbox{Var}}(\hat{\phi})$ does not hold because the samples are
not IID, but the estimator $\hat{\phi}$ is still a valid, unbiased
estimator of $\phi$.

## Variance reduction (optional)

There are some tools for variance reduction in MC settings. One is
importance sampling (see Section 3). Others are the use of control
variates and antithetic sampling. I haven't personally run across these
latter in practice, so I'm not sure how widely used they are and won't
go into them here.

In some cases we can set up natural strata, for which we know the
probability of being in each stratum. Then we would estimate $\mu$ for
each stratum and combine the estimates based on the probabilities. The
intuition is that we remove the variability in sampling amongst the
strata from our simulation.

Another strategy that comes up in MCMC contexts is
*Rao-Blackwellization*. Suppose we want to know $E(h(X))$ where
$X=\{X_{1},X_{2}\}$. Iterated expectation tells us that
$E(h(X))=E(E(h(X)|X_{2})$. If we can compute
$E(h(X)|X_{2})=\int h(x_{1},x_{2})f(x_{1}|x_{2})dx_{1}$ then we should
avoid introducing stochasticity related to the $X_{1}$ draw (since we
can analytically integrate over that) and only average over
stochasticity from the $X_{2}$ draw by estimating
$E_{X_{2}}(E(h(X)|X_{2})$. The estimator is
$$\hat{\mu}_{RB}=\frac{1}{m}\sum_{i=1}^{m}E(h(X)|X_{2,i})$$ where we
either draw from the marginal distribution of $X_{2}$, or equivalently,
draw $X$, but only use $X_{2}$. Our MC estimator averages over the
simulated values of $X_{2}$. This is called Rao-Blackwellization because
it relates to the idea of conditioning on a sufficient statistic. It has
lower variance because the variance of each term in the sum of the
Rao-Blackwellized estimator is $\mbox{Var}(E(h(X)|X_{2})$, which is less
than the variance in the usual MC estimator, $\mbox{Var}(h(X))$, based
on the usual iterated variance formula:
$V(X)=E(V(X|Y))+V(E(X|Y))\Rightarrow V(E(X|Y))<V(X)$.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Design of simulation studies →](03-2-design-of-simulation-studies.md)
