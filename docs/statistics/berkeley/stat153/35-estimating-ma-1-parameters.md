---
title: "35. Estimating MA(1) Parameters"
course: "Berkeley Stat 153"
chapter: 35
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 35. Estimating MA(1) Parameters

## What this covers

Fitting an AR model is ordinary least squares, but an MA(1) model has no such shortcut, because
the lagged quantity in the equation — the previous innovation — is never observed. This chapter
works out how to fit the MA(1) model $y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$ by maximum
likelihood despite that, how to attach standard errors to the resulting estimates, and then checks
both against `statsmodels`' `ARIMA` routine, first on simulated data with known parameters and then
on the glacial varve series used earlier in the course. It assumes the MA(1) model itself, the
AR(1) conditional-likelihood trick of conditioning on $y_1$, ordinary maximum likelihood, and a
Bayesian posterior built from a flat prior (as used for AR(1) standard errors earlier in the
course).

## Why MA(1) needs more than regression

Recall the MA(1) model,
$$y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2).$$
An AR model can be fit by ordinary regression because every term on the right-hand side is either
observed or a parameter. Here $\epsilon_{t-1}$ is neither: it is unobserved noise, so there is no
design matrix to regress $y_t$ on. Parameter estimation for MA (and, more generally, ARIMA and
SARIMA) models is genuinely harder than for AR models, and this lab works out just enough of it —
for the simplest case, MA(1) — to see how the estimation actually works, rather than treating
`ARIMA` as a black box.

## The exact likelihood is expensive

Because $y_1,\dots,y_n$ is a linear combination of jointly normal $\epsilon$'s, it is itself
multivariate normal, with mean vector $m = (\mu,\dots,\mu)^T$ and $n\times n$ covariance matrix
$\Sigma$ whose $(i,j)$ entry is
$$\Sigma_{ij} = \begin{cases} \sigma^2(1+\theta^2) & i = j \\ \sigma^2 \theta & |i-j| = 1 \\ 0 & \text{otherwise.} \end{cases}$$
The likelihood is therefore
$$\left(\frac{1}{\sqrt{2\pi}}\right)^n (\det \Sigma)^{-1/2} \exp\left(-\frac12 (y-m)'\Sigma^{-1}(y-m)\right),$$
a function of $\mu,\theta,\sigma$ that could in principle be maximized numerically. The obstacle is
$\Sigma^{-1}$: without an exact or approximate formula for it, maximizing this likelihood means
inverting an $n\times n$ matrix at every evaluation, which is too expensive to do inside an
optimizer's inner loop.

## The conditional likelihood: pretend $\epsilon_0 = 0$

The fix mirrors the one used for AR(1): there, conditioning on $y_1$ turned an awkward likelihood
into a simple product. Here the trick is to condition on $\epsilon_0 = 0$ — not an observed value,
but a *pretend* starting innovation — which lets the joint density factor by the chain rule:
$$f_{y_1,\dots,y_n \mid \epsilon_0 = 0}(y_1,\dots,y_n) = f_{y_1\mid\epsilon_0=0}(y_1)\, f_{y_2\mid y_1,\epsilon_0=0}(y_2) \cdots f_{y_n \mid y_1,\dots,y_{n-1},\epsilon_0=0}(y_n).$$
Define residuals recursively by running the model equation backwards: $\hat\epsilon_1 = y_1 - \mu$,
and for $t = 2,\dots,n$,
$$\hat\epsilon_t = y_t - \mu - \theta \hat\epsilon_{t-1}.$$
Knowing $y_1,\dots,y_{t-1}$ together with $\epsilon_0 = 0$ is exactly equivalent to knowing
$\epsilon_1 = \hat\epsilon_1,\dots,\epsilon_{t-1}=\hat\epsilon_{t-1}$, so each factor above is just
the $N(0,\sigma^2)$ density of $\epsilon_t$ evaluated at $y_t - \mu - \theta\hat\epsilon_{t-1}$.
Multiplying the factors out, the conditional likelihood collapses to
$$\left(\frac{1}{\sigma\sqrt{2\pi}}\right)^n \exp\left(-\frac{1}{2\sigma^2}\sum_{t=1}^n \hat\epsilon_t^2\right),$$
with no matrix to invert — just one forward pass through the data computing $\hat\epsilon_t$
recursively.

## From likelihood to least squares

Collect the sum of squared residuals into
$$S(\mu,\theta) := \sum_{t=1}^n \hat\epsilon_t^2,$$
so the log-likelihood is
$$\log(\text{likelihood}) = -\frac{n}{2}\log(\sigma^2) - \frac{S(\mu,\theta)}{2\sigma^2}.$$
Since $\sigma$ enters only through this simple form, maximizing over $\mu,\theta$ is the same as
*minimizing* $S(\mu,\theta)$ — a nonlinear least-squares problem, nonlinear because $\hat\epsilon_t$
depends on $\theta$ through the recursion rather than linearly. Once $\hat\mu,\hat\theta$ minimize
$S$, the MLE of $\sigma$ falls out as
$$\hat\sigma = \sqrt{\frac{S(\hat\mu,\hat\theta)}{n}},$$
exactly the residual-based variance estimate familiar from ordinary regression.

Computing $S(\mu,\theta)$ is one loop:

```python
def S_func(params, y):
    mu, theta = params
    n = len(y)
    eps = np.zeros(n)
    eps[0] = y[0] - mu
    for t in range(1, n):
        eps[t] = y[t] - mu - theta * eps[t-1]
    return np.sum(eps**2)
```

and `scipy.optimize.minimize` finds the minimizer numerically, started from $\mu_0 = \bar y$,
$\theta_0 = 0$.

## Worked example: recovering known parameters

Simulate 400 points from an MA(1) with $\theta = -0.7$, then add a mean of 5. `ARIMA(0,0,1)` fit by
the full (exact) likelihood reports
$$\hat\mu = 5.0092,\quad \hat\theta = -0.6566,\quad \hat\sigma^2 = 0.9603.$$
Minimizing $S(\mu,\theta)$ from scratch gives
$$\hat\mu = 5.0091,\quad \hat\theta = -0.6582,$$
matching to three decimal places, and
$$\hat\sigma = \sqrt{S(\hat\mu,\hat\theta)/n} = 0.9800$$
against ARIMA's $\sqrt{0.9603} = 0.9799$. The two procedures are not optimizing exactly the same
objective — conditional versus exact likelihood — so a small gap between them, visible here in the
third or fourth decimal place, is expected rather than a bug.

## Standard errors: a Bayesian route to a $t$-posterior

A point estimate alone says nothing about how much $\hat\mu,\hat\theta$ would move under
resampling. As with the AR(1) standard errors earlier in the course, put a flat (improper) prior on
$\mu,\theta$ and on $\log\sigma$:
$$\mu,\theta,\log\sigma \overset{\text{i.i.d.}}{\sim} \text{Unif}(-C,C), \qquad C \text{ large}.$$
The change of variables to $\log\sigma$ contributes a Jacobian factor $1/\sigma$, so the joint
posterior (up to a constant) is
$$f_{\mu,\theta,\sigma\mid\text{data}}(\mu,\theta,\sigma) \propto \sigma^{-n-1}\exp\left(-\frac{S(\mu,\theta)}{2\sigma^2}\right) I\{-C < \mu,\theta,\log\sigma < C\}.$$
Integrating this over $\sigma$ from $0$ to $\infty$ — the same integral used to build the AR(1)
posterior — leaves the marginal posterior of $(\mu,\theta)$ alone:
$$f_{\mu,\theta\mid\text{data}}(\mu,\theta) \propto S(\mu,\theta)^{-n/2} I\{-C<\mu,\theta<C\} \propto \left(\frac{S(\hat\mu,\hat\theta)}{S(\mu,\theta)}\right)^{n/2} I\{-C<\mu,\theta<C\}.$$

If $S(\mu,\theta)$ were an exact quadratic function of $(\mu,\theta)$, this would already be (up to
the indicator) a bivariate $t$-density. It is not — $\hat\epsilon_t$ depends on $\theta$ through a
recursion, so $S$ involves higher powers of $\theta$ — but the posterior is fairly concentrated
around the MLE, so approximate $S$ near $\hat\alpha := (\hat\mu,\hat\theta)$ by its second-order
Taylor expansion. Writing $\alpha = (\mu,\theta)$,
$$S(\alpha) = S(\hat\alpha) + \langle \nabla S(\hat\alpha), \alpha - \hat\alpha\rangle + (\alpha-\hat\alpha)^T\left(\tfrac12 HS(\hat\alpha)\right)(\alpha-\hat\alpha) = S(\hat\alpha) + (\alpha - \hat\alpha)^T\left(\tfrac12 HS(\hat\alpha)\right)(\alpha-\hat\alpha),$$
the gradient term dropping out because $\hat\alpha$ minimizes $S$. Substituting this quadratic
approximation into the posterior and simplifying algebraically puts it in the form
$$\left(1 + \frac{1}{n-2}(\alpha-\hat\alpha)^T\left(\frac{n-2}{2S(\hat\alpha)}HS(\hat\alpha)\right)(\alpha-\hat\alpha)\right)^{-\frac{n-2+2}{2}} I\{-C<\mu,\theta<C\},$$
which matches the general $p$-variate $t_{k,p}(m,\Sigma)$ density
$$\left(1 + \frac1k (x-m)^T\Sigma^{-1}(x-m)\right)^{-(k+p)/2}$$
term for term (ignoring the indicator, valid for $C$ large). Reading off $k = n-2$, $p=2$, $m =
\hat\alpha$ identifies
$$\alpha \mid \text{data} \;\sim\; t_{n-2,\,2}\left(\hat\alpha,\ \frac{S(\hat\alpha)}{n-2}\left(\tfrac12 HS(\hat\alpha)\right)^{-1}\right).$$
So the posterior of $(\mu,\theta)$ is approximately a bivariate $t$ centered at the MLE, and the
standard errors of $\hat\mu$ and $\hat\theta$ are the square roots of the diagonal entries of its
scale matrix
$$\frac{S(\hat\alpha)}{n-2}\left(\tfrac12 HS(\hat\alpha)\right)^{-1}.$$
The one missing ingredient is the Hessian of $S$ at $\hat\alpha$. Rather than differentiate the
recursion symbolically, the lab gets it numerically, via the `numdifftools` package:

```python
H = nd.Hessian(lambda alpha: S_func(alpha, dt), step=1e-6)(alphaest)
sighat = np.sqrt(S_func(alphaest, dt) / (n - 2))
covmat = (sighat ** 2) * np.linalg.inv(0.5 * H)
stderrs = np.sqrt(np.diag(covmat))
```

## Worked example: checking the standard errors

On the same simulated data, this recipe gives standard errors $(0.01685, 0.03655)$ for
$(\hat\mu,\hat\theta)$, against ARIMA's reported $(0.01689, 0.03683)$ — close agreement, obtained
without ever writing down $\Sigma^{-1}$.

## Application: the varve dataset from Lecture 21

The glacial varve thickness series was fit with an MA(1) model earlier in the course, on the
differenced logarithm of the raw thickness: take logs, then first-difference. The sample ACF and
PACF of the differenced log series (60 lags) show a pattern consistent with MA(1).

Fitting `ARIMA(0,0,1)` to the 633 differenced values by full likelihood gives
$$\hat\mu = -0.0013,\quad \hat\theta = -0.7710,\quad \hat\sigma^2 = 0.2353.$$
Minimizing $S(\mu,\theta)$ from scratch gives
$$\hat\mu = -0.00114,\quad \hat\theta = -0.7728,\quad \hat\sigma = \sqrt{S(\hat\mu,\hat\theta)/n} = 0.4852,$$
close to ARIMA's $\sqrt{0.2353} = 0.4851$ throughout.

The standard errors are where the two approaches part company more visibly: the from-scratch
calculation gives $(0.0044, 0.0342)$ for $(\hat\mu,\hat\theta)$, against ARIMA's $(0.0169, 0.0368)$.
The $\theta$ standard errors agree closely; the $\mu$ standard error does not. The reason offered is
that `ARIMA` optimizes the *full* (exact) likelihood, while everything derived in this chapter uses
the *conditional* likelihood (conditioning on $\epsilon_0 = 0$) — the two objectives are close but
not identical, and the full likelihood is the more complicated of the two to write down, which is
exactly why the conditional version was the one worked out here. No standard error for $\sigma$ is
computed in this lab; doing so would mean working out the posterior of $\sigma$ alone, which can be
written in terms of the chi-squared distribution.

## Sources

- Berkeley STAT 153, Fall 2025, Code Lab 12 (`CodeLabTwelve153248Fall2025.ipynb`), converted to
  three linked pages:
  - "Introduction" — MA(1) model, exact likelihood, conditional likelihood derivation, $S(\mu,\theta)$,
    and the simulated-data worked example.
  - "Standard Errors corresponding to the parameter estimates" — the Bayesian/Taylor-expansion
    derivation of the $t$-posterior and the standard-error worked example.
  - "Varve Dataset from Lecture 21" — the differenced-log-varve MA(1) fit and its comparison to
    `ARIMA`.
- No slide deck or lecture transcript was supplied for this chapter; the notebook text is the only
  source.
- The lab refers to two earlier lectures it does not itself contain: "Lecture 4" (the Bayesian
  construction with a flat prior on $\mu,\theta,\log\sigma$ used earlier for AR(1) standard errors,
  whose $\sigma$-integration step is reused here without repeating it) and "Lecture 21" (where the
  varve dataset was first introduced and its ACF/PACF used to select the MA(1) model). Neither is
  part of the supplied material.
- Three figures referenced in the notebook (raw varve thickness, its logarithm, and the differenced
  logarithm, plus the ACF/PACF plot) were omitted from the converted source and so are not
  reproduced here.

---

[← 34. Inference in Sinusoid Models](34-inference-in-sinusoid-models.md) · [Contents](index.md) · [36. Anatomy of a Regression Fit (part 1) →](36-anatomy-of-a-regression-fit-part-1.md)
