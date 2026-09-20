---
title: "53. Bayesian Regularization of Trends"
course: "Berkeley Stat 153 Fall 2024"
chapter: 53
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 53. Bayesian Regularization of Trends

## What this covers

This chapter reworks the ridge-regression trend estimator from the previous lecture into a genuinely
Bayesian procedure. Instead of choosing the amount of smoothing by hand, the coefficients are given a prior,
the data update it, and the fitted trend, its uncertainty band, and the auto-selected amount of smoothing are
all read off the resulting posterior. The worked example throughout is a monthly temperature-anomaly series,
the same one used for the ridge fit. It assumes the truncated-basis ("hinge function") design matrix for
trend estimation and the ridge estimator built from it, both from the previous code lecture, together with
the ordinary conjugate normal-normal update of Bayesian linear regression.

## A saturated basis: a kink at every time point

The regression is set up exactly as before. With $n$ time points $x = 1, \dots, n$, the design matrix has an
intercept, a linear term, and one hinge (truncated-linear) column per interior time point:

```python
n = len(y)
x = np.arange(1, n+1)
X = np.column_stack([np.ones(n), x-1])
for i in range(n-2):
    c = i+2
    xc = ((x > c).astype(float))*(x-c)
    X = np.column_stack([X, xc])
```

Column $c$ is $(x-c)_+$: zero up to time $c$, then rising linearly after it. A weighted sum of these columns
is a piecewise-linear function that can have a kink at every single time point — with $n$ columns for $n$
observations, the basis is saturated, and an ordinary least-squares fit on it interpolates the data exactly.
Regularizing the kink coefficients is what turns this from a lookup table into a genuine *trend*.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A hinge basis column before and after the prior shrinks it">
  <line x1="40" y1="180" x2="320" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="312" y="197" font-size="12" fill="currentColor" text-anchor="end">time</text>
  <line x1="170" y1="180" x2="170" y2="60" stroke="currentColor" stroke-width="1" stroke-dasharray="2,3" opacity="0.5"/>
  <text x="170" y="197" font-size="12" fill="currentColor" text-anchor="middle">c</text>
  <polyline points="40,180 170,180 300,70" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="196" y="92" font-size="12" fill="currentColor">large weight: sharp kink</text>
  <polyline points="40,180 170,180 300,165" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="5,4" opacity="0.65"/>
  <text x="196" y="178" font-size="12" fill="currentColor">shrunk by the prior: no kink</text>
</svg>
<figcaption>One column of the design matrix is a hinge function, zero up to a knot $c$ and linear after it.
A large coefficient there bends the fitted trend; a tight prior variance shrinks most such coefficients
toward zero, leaving a smooth trend instead of an interpolating one.</figcaption>
</figure>

## The Bayesian model, and ridge regression as a special case

Put a Gaussian prior directly on the coefficients, $\beta \sim N(0, Q)$, with likelihood
$y \mid \beta, \sigma \sim N(X\beta, \sigma^2 I)$. This is the ordinary conjugate normal-normal setup, so the
posterior of $\beta$ given the data and $\sigma$ is Gaussian:

$$
\beta \mid \text{data}, \sigma \;\sim\; N\!\left(\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2},\;\;\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\right).
$$

The choice of $Q$ decides which coefficients get regularized. Take $Q$ diagonal with entries
$C, C, \tau^2, \dots, \tau^2$ for a large constant $C$: the intercept and the linear-trend coefficient get an
essentially flat, non-informative prior, while every kink coefficient gets prior variance $\tau^2$. A small
$\tau$ shrinks the kinks hard toward zero and leaves an almost straight line; a large $\tau$ leaves them
essentially unpenalized and the fit interpolates.

This *is* ridge regression. Minimizing $\|y - X\beta\|^2$ plus an $\ell_2$ penalty on the kink coefficients
only — excluding the intercept and slope, `penalty_start=2` in the code below — gives exactly the posterior
mean above, provided the ridge penalty $\lambda$ and the two variances are related by

$$
\lambda = \frac{\sigma^2}{\tau^2}.
$$

```python
def solve_ridge(X, y, lambda_val, penalty_start=2):
    beta = cp.Variable(X.shape[1])
    loss = cp.sum_squares(X @ beta - y)
    reg = lambda_val * cp.sum_squares(beta[penalty_start:])
    cp.Problem(cp.Minimize(loss + reg)).solve()
    return beta.value
```

The lecture checks this numerically: solving the ridge problem directly with `cvxpy`, and computing the
posterior-mean formula by matrix algebra for the same $\lambda = \sigma^2/\tau^2$, give fitted values that
agree to at least six significant figures at every one of the roughly 175 time points. A large ridge penalty
and a tight prior relative to the noise are the same statement, seen from two directions — one an
optimization problem, the other a posterior mean.

## Choosing $\tau$ and $\sigma$ from the data, not by hand

Fixing $\tau$ and $\sigma$ and reading off $\hat\beta$ works, but it leaves exactly the question ridge
regression always leaves open: what value of the penalty — equivalently, of $\tau$ — should be used? The
Bayesian model answers this without cross-validation: put $\tau$ and $\sigma$ into the model as well, and ask
for their posterior.

Because everything is Gaussian, $\beta$ can be integrated out of the joint distribution of $(y, \beta)$ in
closed form, leaving a posterior over $(\tau, \sigma)$ alone:

$$
f_{\tau,\sigma\mid\text{data}}(\tau,\sigma) \;\propto\; \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}}
\sqrt{\det\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}}\;
\exp\!\left(-\frac{y^Ty}{2\sigma^2}\right)
\exp\!\left(\frac{y^TX\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}X^Ty}{2\sigma^4}\right).
$$

(This marginalization step, and the prior on $\tau,\sigma$ it assumes to produce the $\sigma^{-n-1}\tau^{-1}$
factor, were worked out on the board and are not in either notebook — see Sources.) The formula still refers
to $Q$, and hence to the arbitrary large constant $C$, but $C$ is only there to flatten the prior on the
intercept and slope and should not affect the answer. Since

$$
\det Q = C \cdot C \cdot \tau^2 \cdots \tau^2 = C^2\tau^{2(n-2)} \;\propto\; \tau^{2(n-2)}, \qquad
Q^{-1} = \mathrm{diag}(1/C, 1/C, 1/\tau^2, \dots, 1/\tau^2) \;\approx\; \mathrm{diag}(0, 0, 1/\tau^2, \dots, 1/\tau^2),
$$

letting $C \to \infty$ and writing $Q_{\text{approx}}^{-1}$ for that limiting diagonal matrix removes $C$
entirely:

$$
f_{\tau,\sigma\mid\text{data}}(\tau,\sigma) \;\propto\; \sigma^{-n-1}\tau^{-n+1}
\sqrt{\det\left(\frac{X^TX}{\sigma^2}+Q_{\text{approx}}^{-1}\right)^{-1}}\;
\exp\!\left(-\frac{y^Ty}{2\sigma^2}\right)
\exp\!\left(\frac{y^TX\left(\frac{X^TX}{\sigma^2}+Q_{\text{approx}}^{-1}\right)^{-1}X^Ty}{2\sigma^4}\right).
$$

This is a function of only two numbers, $\tau$ and $\sigma$ — the entire $n$-dimensional $\beta$ has been
integrated away — so it can be evaluated on an ordinary two-dimensional grid and searched directly, a
$100 \times 100$ grid of $\tau \in [10^{-4}, 1]$ and $\sigma \in [0.1, 1]$ on a log scale, something that
would be hopeless if $\beta$ still had to be swept over as well:

```python
for i in range(len(g)):
    tau, sig = g.loc[i, 'tau'], g.loc[i, 'sig']
    Qinv_approx = np.diag(np.concatenate([[0, 0], np.repeat(tau**(-2), n-2)]))
    Mat = Qinv_approx + (X.T @ X)/(sig ** 2)
    Matinv = np.linalg.inv(Mat)
    _, logcovdet = np.linalg.slogdet(Matinv)
    g.loc[i, 'logpost'] = ((-n-1)*np.log(sig) + (-n+1)*np.log(tau) + 0.5*logcovdet
                            - (y @ y)/(2*sig**2) + (y @ X @ Matinv @ X.T @ y)/(2*sig**4))
```

The grid maximizer — the posterior mode, or MAP estimate — comes out at $\tau \approx 0.00215$,
$\sigma \approx 0.171$, the same value in both runs of the lecture, since it is the same data and model.
Fixing $\tau, \sigma$ at this MAP and plugging back into the posterior-mean formula for $\beta$ gives a
single "best" fitted trend, with no penalty value chosen by hand anywhere in the process.

## The full posterior: point estimates and uncertainty

The grid gives the full (discretized) posterior over $(\tau, \sigma)$, not just its mode. Exponentiating the
log-posterior — after subtracting its maximum, for numerical stability — and normalizing so the grid weights
sum to one turns `logpost` into an approximate probability mass function over the grid:

```python
g['post'] = np.exp(g['logpost'] - np.max(g['logpost']))
g['post'] = g['post']/np.sum(g['post'])
```

Weighting each grid value by this probability and averaging gives the posterior means
$\mathbb E[\tau \mid \text{data}] \approx 0.00242$ and $\mathbb E[\sigma \mid \text{data}] \approx 0.173$ —
close to, but not identical to, the MAP values above, which is itself informative: it says the posterior over
$(\tau, \sigma)$ is fairly concentrated and close to symmetric on this scale, not wildly skewed.

The same weighted grid can be resampled directly, `g.sample(N, weights=g['post'], replace=True)`, to draw
$N = 1000$ posterior draws $(\tau_i, \sigma_i)$. For each draw, the conditional posterior of $\beta$ given
that $(\tau_i, \sigma_i)$ is again the Gaussian derived above, so a full posterior draw of $\beta$ — and hence
of the fitted trend $X\beta$ — is obtained by sampling from that Gaussian rather than plugging in only its
mean. This is the version of the sampling loop that correctly propagates both sources of uncertainty, the
hyperparameters and the residual spread of $\beta$ around its conditional mean:

```python
for i in range(N):
    tau, sig = tau_samples[i], sig_samples[i]
    Q = np.diag(np.concatenate([[C, C], np.repeat(tau**2, n-2)]))
    TempMat = np.linalg.inv(np.linalg.inv(Q) + (X.T @ X)/(sig ** 2))
    norm_mean = TempMat @ (X.T @ y)/(sig ** 2)
    betahat = np.random.multivariate_normal(norm_mean, TempMat)
    muhats[:, i] = X @ betahat
```

(The other run of the lecture instead plugs in `norm_mean` at each sampled $(\tau_i, \sigma_i)$ without
drawing $\beta$ from its conditional covariance — a valid but narrower summary of the same posterior, since
it captures the hyperparameter uncertainty but not the extra spread of $\beta$ around its conditional mean.)

Averaging the 1000 fitted curves gives the posterior-mean trend; plotting all 1000 together as a fan around
it shows the posterior uncertainty directly, visibly narrower where the data pin the trend down tightly and
wider elsewhere. The histograms of the sampled $\tau$'s and $\sigma$'s show where the posterior mass actually
sits: the sampled $\tau$ values concentrate away from both extremes — not so large that the fit is wiggly and
interpolates, not so small that it collapses to a straight line. That middle ground is exactly the "right"
amount of smoothing that cross-validation is usually used to find by trial and error; here it falls out of
the posterior automatically, because $\tau$ is a parameter of the model rather than a value chosen by the
analyst.

## Sources

- Both notebooks are the entirety of the input material for this chapter, and there is no separate slide
  deck or transcript for this lecture: `CodeLectureTwelve153248Fall2025.ipynb` (Berkeley STAT 153, Fall 2025)
  and `CodeLectureTwelve153248Spring2025.ipynb` (Spring 2025), both titled "Bayesian Regularization." The
  notebooks' markdown cells and code are the only record.
- The design matrix, the Gaussian-prior posterior formula, and the ridge-regression equivalence check are
  common to both notebooks; the code snippets quoted above are drawn from the Fall version, which is
  syntactically identical to the Spring one at this point in the lecture.
- The elimination of $C$ from the marginal posterior of $(\tau, \sigma)$ — the $\det Q \propto \tau^{2(n-2)}$
  step and the $Q_{\text{approx}}^{-1}$ simplification — is stated only in the Fall notebook. The Spring
  notebook instead works with the un-simplified formula and an explicit finite $C = 10^4$ throughout, and
  reaches the same numerical MAP and posterior-mean values.
- The full posterior sampling of $\beta$ via `np.random.multivariate_normal` is from the Fall notebook; the
  Spring notebook's sampling loop instead uses only the conditional posterior mean of $\beta$ at each sampled
  $(\tau, \sigma)$, noted above as the narrower-variance variant.
- The remark that the uncertainty band is narrower at some time points than others is from the Spring
  notebook; the remark about the sampled $\tau$'s avoiding both extremes appears, in near-identical wording,
  in both.
- The derivation of the marginal posterior for $(\tau, \sigma)$ — integrating $\beta$ out of the joint
  Gaussian model, and the specific prior placed on $\tau$ and $\sigma$ that produces the
  $\sigma^{-n-1}\tau^{-1}$ factor — is described in both notebooks only as "derived in class"; neither
  notebook contains that derivation.
- The ridge-regression estimator and the truncated-basis ("hinge function") construction of $X$ are referred
  to in both notebooks as work from "the last lecture" and are not themselves supplied here.
- Numerical values quoted (MAP estimates, posterior means) are read directly from the notebooks' printed
  output cells.

---

[← 52. Trend and Seasonal Regression](52-trend-and-seasonal-regression.md) · [Contents](index.md) · [54. ACF, PACF, and AR(p) Stationarity →](54-acf-pacf-and-ar-p-stationarity.md)
