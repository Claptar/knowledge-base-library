---
title: "63. AR(p) Estimation and Multistep Forecasting"
course: "Berkeley Stat 153"
chapter: 63
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 63. AR(p) Estimation and Multistep Forecasting

## What this covers

The previous lecture set up conditional maximum likelihood for the $AR(1)$ model. This chapter
extends that recipe to $AR(p)$, compares two ways of fitting it in software, introduces the *full*
(unconditional) likelihood as an alternative to the conditional one, and then asks how a fitted
$AR(p)$ model is used to forecast future values — and how uncertain those forecasts are. Answering
the second question needs the algebra of covariance matrices for random vectors, which the lecture
builds from scratch along the way. Assumes: the $AR(p)$ model and its conditional least-squares/MLE
fit, and the ordinary (scalar) properties of variance and covariance.

## Recap: conditional likelihood, from AR(1) to AR(p)

Estimation for the $AR(1)$ model,
$$y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t, \qquad \varepsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2), \qquad t = 2,\dots,n,$$
was set up by writing the likelihood of $y_2,\dots,y_n$ *conditional on* $y_1$:
$$f^\theta_{y_2,\dots,y_n\mid y_1} = \prod_{t=2}^n \frac{1}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{(y_t-\phi_0-\phi_1y_{t-1})^2}{2\sigma^2}\right).$$
Because the errors are iid Gaussian, maximizing this over $(\phi_0,\phi_1,\sigma)$ is the same
problem as ordinary least squares: maximizing the likelihood is equivalent to minimizing
$\sum_t (y_t-\phi_0-\phi_1y_{t-1})^2$. This is the *conditional* MLE — conditional because it treats
$y_1$ as given rather than modeling where it came from.

The same idea extends directly to $AR(p)$:
$$y_t = \phi_0+\phi_1y_{t-1}+\dots+\phi_py_{t-p}+\varepsilon_t, \qquad t=p+1,\dots,n,$$
with conditional likelihood
$$\prod_{t=p+1}^n \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(y_t-\phi_0-\dots-\phi_py_{t-p})^2}{2\sigma^2}\right),$$
now conditioning on the first $p$ values $y_1,\dots,y_p$.

## Two ways to fit it, and why they disagree on $\hat\sigma$

Two recipes fit the same conditional likelihood:

(a) Build the response vector $y$ (size $(n-p)\times 1$) and the design matrix $X$ (size
$(n-p)\times(p+1)$, one column of $1$'s for $\phi_0$ and one column per lag), and run ordinary
least squares: `sm.OLS(y, X).fit()`.

(b) Call `AutoReg(y, p=1, 2, \dots)`, the `statsmodels` routine written specifically for
autoregressions.

They return **identical estimates of $\phi_0,\phi_1,\dots,\phi_p$** — both are solving the same
least-squares problem — but they do not agree on $\hat\sigma$. Method (a), being generic OLS,
divides the residual sum of squares by the usual residual degrees of freedom, observations minus
parameters:
$$\hat\sigma = \sqrt{\frac{\mathrm{RSS}}{(n-p)-(p+1)}}.$$
Method (b) divides by $n-p$, the number of terms in the conditional likelihood, with no correction
for the $p+1$ parameters estimated:
$$\hat\sigma = \sqrt{\frac{\mathrm{RSS}}{n-p}}.$$
The two denominators differ by $p+1$, and this is the reason the two routines' standard errors —
and the reference distribution used to build confidence intervals and tests, $t$ for one and $z$
(normal) for the other — do not match exactly.

## The full (unconditional) likelihood for AR(1)

The conditional likelihood above treats $y_1$ as given and says nothing about its distribution. If
instead $|\phi_1| < 1$ — the stationarity condition — the $AR(1)$ recursion can be run backward
indefinitely, $t = 1, 0, -1, \dots$, and solved forward as an infinite moving average:
$$y_1 = \frac{\phi_0}{1-\phi_1} + \sum_{j=0}^\infty \phi_1^j\,\varepsilon_{1-j}.$$
This is a sum of independent Gaussians, hence Gaussian itself, with mean $\phi_0/(1-\phi_1)$ and
variance $\sigma^2\sum_j \phi_1^{2j} = \sigma^2/(1-\phi_1^2)$:
$$y_1 \sim N\!\left(\frac{\phi_0}{1-\phi_1},\ \frac{\sigma^2}{1-\phi_1^2}\right).$$
This is the stationary marginal distribution of the $AR(1)$ process. Multiplying this marginal
density of $y_1$ by the same conditional factors as before gives the **full, or unconditional,
likelihood**:
$$L(\theta) = \underbrace{\frac{\sqrt{1-\phi_1^2}}{\sqrt{2\pi}\sigma}\exp\left[-\frac{\left(y_1-\frac{\phi_0}{1-\phi_1}\right)^2(1-\phi_1^2)}{2\sigma^2}\right]}_{\text{marginal density of } y_1} \times \prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(y_t-\phi_0-\phi_1y_{t-1})^2}{2\sigma^2}\right),$$
valid only under $|\phi_1| < 1$, which is exactly what makes the series variance
$\sigma^2/(1-\phi_1^2)$ finite and the marginal distribution well defined. `AutoReg` has no option
to maximize this more complicated likelihood; `statsmodels`'s `arima` routine does.

## Forecasting: the recursive point forecast

Given a fitted $AR(p)$ model and data $y_1,\dots,y_n$, the natural point forecast of a future value
is its conditional expectation. One step ahead,
$$\hat y_{n+1}(\theta) = \mathbb E(y_{n+1}\mid y_1,\dots,y_n,\theta) = \phi_0+\phi_1y_n+\dots+\phi_py_{n+1-p},$$
is immediate, because every term on the right is already observed. Two steps ahead is not, since
$y_{n+1}$ is itself unknown at time $n$:
$$\hat y_{n+2}(\theta) = \mathbb E(y_{n+2}\mid y_1,\dots,y_n,\theta) = \mathbb E\left[\phi_0+\phi_1y_{n+1}+\phi_2y_n+\dots+\phi_py_{n+2-p}\mid y_1,\dots,y_n,\theta\right].$$
Since $\phi_0, \phi_2 y_n, \dots$ are already known and, by definition,
$\mathbb E(y_{n+1}\mid y_1,\dots,y_n,\theta) = \hat y_{n+1}(\theta)$,
$$\hat y_{n+2}(\theta) = \phi_0+\phi_1\hat y_{n+1}(\theta)+\phi_2y_n+\dots+\phi_py_{n+2-p}.$$
The same substitution repeats at every horizon, giving the general recursion
$$\hat y_{n+k}(\theta) = \phi_0+\phi_1\hat y_{n+k-1}(\theta)+\phi_2\hat y_{n+k-2}(\theta)+\dots+\phi_p\hat y_{n+k-p}(\theta), \qquad k=1,2,\dots,$$
with the convention $\hat y_j(\theta) = y_j$ for $j \le n$: plug in the observed value once the
recursion reaches data already in hand, and the forecast otherwise. Forecasting $k$ steps ahead is
just running the $AR(p)$ recursion forward $k$ times, feeding each new forecast back in as if it
were data.

## Forecast uncertainty: why the variance is not just $\sigma^2$

The forecast $\hat y_{n+k}(\theta)$ is a conditional expectation, so the natural measure of its
uncertainty is the conditional variance $\mathrm{Var}(y_{n+k}\mid y_1,\dots,y_n,\theta)$. At $k=1$,
$$y_{n+1} = \phi_0+\phi_1y_n+\dots+\phi_py_{n+1-p}+\varepsilon_{n+1},$$
and everything but $\varepsilon_{n+1}$ is fixed by the conditioning, so
$$\mathrm{Var}(y_{n+1}\mid y_1,\dots,y_n,\theta) = \mathrm{Var}(\varepsilon_{n+1}\mid \dots) = \sigma^2.$$
At $k=2$, though,
$$y_{n+2} = \phi_0+\phi_1y_{n+1}+\phi_2y_n+\dots+\varepsilon_{n+2},$$
and now $y_{n+1}$ is *not* fixed by the conditioning — it is itself the random quantity forecast one
step earlier. Since $\varepsilon_{n+2}$ is independent of everything before it,
$$\mathrm{Var}(y_{n+2}\mid y_1,\dots,y_n,\theta) = \mathrm{Var}(\phi_1y_{n+1}+\varepsilon_{n+2}\mid\dots) = \phi_1^2\sigma^2+\sigma^2.$$
The forecast variance grows with the horizon: each step reuses previous forecasts as if they were
inputs, and their own uncertainty feeds forward. For $AR(p)$ with $p \ge 2$ this bookkeeping needs
more than one marginal variance at a time, because the recursion for $y_{n+k}$ is a linear
combination of *several* previous forecasts $y_{n+k-1},\dots,y_{n+k-p}$, and their pairwise
covariances matter too. That is what forces the machinery below.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A point forecast continuing past the last observation, with a band of uncertainty that widens the further ahead it is projected">
  <line x1="30" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="1"/>
  <line x1="150" y1="170" x2="150" y2="20" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3"/>
  <text x="150" y="188" text-anchor="middle" font-size="12" fill="currentColor">n</text>
  <text x="320" y="188" text-anchor="middle" font-size="12" fill="currentColor">n + k</text>
  <path d="M 150 108 L 320 38 L 320 122 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <polyline points="30,122 90,116 150,108" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="150,108 230,90 320,78" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="55" y="140" font-size="12" fill="currentColor">observed</text>
  <text x="215" y="70" font-size="12" fill="currentColor">forecast</text>
</svg>
<figcaption>The point forecast continues the recursion forward, but the band around it — governed by
the diagonal of $\Gamma_k(\theta)$ — widens with the horizon $k$, because each new forecast reuses
the uncertainty of the ones before it.</figcaption>
</figure>

## A toolkit: covariance matrices of random vectors

For a $p\times 1$ random vector $Y = (Y_1,\dots,Y_p)^T$, define $\mathbb E Y$ componentwise, and let
$\mathrm{Cov}(Y)$ be the $p\times p$ matrix whose $(i,j)$ entry is $\mathrm{Cov}(Y_i,Y_j)$ — the
diagonal holds the variances of the individual coordinates. For a second random vector $W$, size
$q\times 1$, the *cross-covariance* $\mathrm{Cov}(Y,W)$ is the $p\times q$ matrix with $(i,j)$ entry
$\mathrm{Cov}(Y_i,W_j)$.

Three rules extend the familiar scalar identities to this setting. For constant matrices $A,B$ and
constant vectors $b,d$:
$$\mathbb E(AY+b) = A\,\mathbb EY + b,$$
$$\mathrm{Cov}(AY+b) = A\,\mathrm{Cov}(Y)\,A^T,$$
$$\mathrm{Cov}(AY+b,\ BW+d) = A\,\mathrm{Cov}(Y,W)\,B^T.$$
These are exactly $\mathbb E(aX+b) = a\mathbb EX+b$, $\mathrm{Var}(aX+b) = a^2\mathrm{Var}(X)$, and
$\mathrm{Cov}(aX+b,cW+d) = ac\,\mathrm{Cov}(X,W)$, with scalars promoted to matrices. Taking
$A = a^T$ (a row vector) in the second and third rules gives two special cases used below:
$$\mathrm{Var}(a^TY) = a^T\mathrm{Cov}(Y)a, \qquad \mathrm{Cov}(Y,\,a^TY) = \mathrm{Cov}(Y)\,a.$$

## Building the forecast covariance matrix $\Gamma_k(\theta)$

Collect the next $k$ future values into a random vector and take its covariance conditional on the
data:
$$\Gamma_k(\theta) = \mathrm{Cov}\!\left(\begin{pmatrix}y_{n+1}\\ \vdots \\ y_{n+k}\end{pmatrix} \,\middle|\, y_1,\dots,y_n,\theta\right), \qquad (i,j)\text{ entry} = \mathrm{Cov}(y_{n+i},y_{n+j}\mid y_1,\dots,y_n,\theta).$$
The diagonal of $\Gamma_k(\theta)$ is exactly the forecast variances at horizons $1,\dots,k$, and
$\Gamma_1(\theta) = \mathrm{Var}(y_{n+1}\mid\dots) = \sigma^2$.

Split off the last coordinate. Writing $\tilde y = (y_{n+1},\dots,y_{n+k-1})^T$ for the first $k-1$
future values,
$$\Gamma_k(\theta) = \begin{bmatrix} \Gamma_{k-1}(\theta) & \gamma_k(\theta) \\ \gamma_k(\theta)^T & \mathrm{Var}(y_{n+k}\mid\dots)\end{bmatrix}, \qquad \gamma_k(\theta) = \mathrm{Cov}(\tilde y,\, y_{n+k}\mid y_1,\dots,y_n,\theta).$$
The top-left block is the covariance matrix one horizon shorter, $\Gamma_{k-1}(\theta)$, so the
whole matrix can be built up recursively once $\gamma_k(\theta)$ and the new corner entry are known.

For $k$ large enough that the $p$ lags feeding $y_{n+k}$ all fall among $y_{n+1},\dots,y_{n+k-1}$,
the $AR(p)$ equation for $y_{n+k}$ reads
$$y_{n+k} = \phi_0 + \underbrace{\phi_1y_{n+k-1}+\phi_2y_{n+k-2}+\dots+\phi_py_{n+k-p}}_{=\ a^T\tilde y} + \varepsilon_{n+k},$$
for a coefficient vector $a$ (depending on $k$, $p$, and $\phi_1,\dots,\phi_p$) that places
$\phi_1,\dots,\phi_p$ in the positions of $y_{n+k-1},\dots,y_{n+k-p}$ and zero elsewhere. Because
$\varepsilon_{n+k}$ is independent of the past and of $\tilde y$ (built only from
$\varepsilon_{n+1},\dots,\varepsilon_{n+k-1}$ and the conditioning data), and covariance with the
constant $\phi_0$ is zero, the two rules above give
$$\gamma_k(\theta) = \mathrm{Cov}(\tilde y,\ a^T\tilde y + \varepsilon_{n+k}\mid\dots) = \mathrm{Cov}(\tilde y)\,a = \Gamma_{k-1}(\theta)\,a,$$
$$\mathrm{Var}(y_{n+k}\mid\dots) = \mathrm{Var}(a^T\tilde y+\varepsilon_{n+k}\mid\dots) = a^T\Gamma_{k-1}(\theta)a+\sigma^2.$$
Substituting both back gives the recursion the lecture was building toward:
$$\Gamma_k(\theta) = \begin{bmatrix}\Gamma_{k-1}(\theta) & \Gamma_{k-1}(\theta)a \\ a^T\Gamma_{k-1}(\theta) & a^T\Gamma_{k-1}(\theta)a + \sigma^2\end{bmatrix}.$$
This reproduces the scalar case worked directly above: at $k=2$ for $AR(1)$ ($p=1$, $a = \phi_1$),
$\Gamma_1(\theta) = \sigma^2$ and the corner entry is $\phi_1^2\sigma^2 + \sigma^2$, exactly as
computed before by hand.

The algorithm this suggests: start from $\Gamma_1(\theta) = \sigma^2$; then for $k = 2, 3, \dots$,
work out the coefficient vector $a$ for that $k$ from $\phi_1,\dots,\phi_p$, and grow
$\Gamma_{k-1}(\theta)$ into $\Gamma_k(\theta)$ by the block formula above. Plugging in $\hat\theta$
for $\theta$ turns the diagonal of $\Gamma_k(\hat\theta)$ into the standard errors reported
alongside a multistep forecast.

## Sources

- Handwritten lecture notes, Berkeley Stat 153, Fall 2025, Lecture Eighteen, page 1
  (`01-lecture-eighteen.md`): the conditional-likelihood recap for $AR(1)$ and $AR(p)$, the two
  fitting methods (`sm.OLS` vs. `AutoReg`) and their differing $\hat\sigma$, the full/unconditional
  $AR(1)$ likelihood and the role of `arima`, and the point-forecast recursion
  $\hat y_{n+k}(\theta)$.
- Handwritten lecture notes, same lecture, page 2 (`02-covariance-matrices.md`): the covariance
  matrix toolkit for random vectors and the derivation of the forecast-covariance recursion
  $\Gamma_k(\theta)$.
- Both source files carry a conversion note that they were reconstructed by a model from a
  handwritten PDF with no text layer, and that every equation is unverified; the material above is
  a faithful reorganisation of that reconstruction, not independently checked mathematics.
- The lecture refers to, but the notes do not themselves contain, the previous lecture's setup of
  $AR(1)$ conditional MLE, and the `statsmodels` routines `sm.OLS`, `AutoReg`, and `arima` used for
  fitting. No slides, transcript, or exercises were supplied for this lecture.

---

[← 62. The Discrete Fourier Transform](62-the-discrete-fourier-transform.md) · [Contents](index.md) · [64. Ridge and Lasso Trend Filtering →](64-ridge-and-lasso-trend-filtering.md)
