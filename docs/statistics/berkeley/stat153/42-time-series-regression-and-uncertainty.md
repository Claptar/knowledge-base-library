---
title: "42. Time Series Regression and Uncertainty"
course: "Berkeley Stat 153 Fall 2024"
chapter: 42
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 42. Time Series Regression and Uncertainty

## What this covers

Once a time series regression $y = X\beta + \epsilon$ has been fit by least squares, two questions
remain: what should go into the columns of $X$, and how much should the fitted coefficients be
trusted? This chapter answers both, working through five datasets: US population, Lake Huron water
levels, a simulated quadratic trend, monthly US accidental deaths, and monthly alcohol retail
sales. It assumes ordinary least squares — the normal equations $\hat\beta = (X^TX)^{-1}X^Ty$,
residual sum of squares, $R^2$ — and an earlier result, used here rather than re-derived, that the
posterior distribution of $\beta$ under a linear Gaussian model is a multivariate $t$.

## Two ways to build a design matrix for a time series

Multiple linear regression works with an $n\times 1$ vector $y$ and an $n\times(m+1)$ matrix $X$
whose first column is all ones. In a time series, $y$ is the observed series itself, and there are
two distinct ways to fill in the rest of $X$:

1. **Functions of time.** Each covariate is some deterministic function of the time index $t$: a
   polynomial trend ($t$, $t^2$, …) or a seasonal component (sines and cosines at a fixed
   frequency).
2. **Autoregression.** The covariates are lagged values of the series itself, $y_{t-1}, y_{t-2},
   \dots$

Both are still ordinary linear regressions in $\beta$ — the difference is entirely in what goes
into $X$, and it changes what forecasting means, as the later sections show.

## Trend regression and the uncertainty in its coefficients

Take monthly US population (FRED series `POPTHM`) and fit a straight-line trend, with $t$ running
from 1 to $n$: $X = [\mathbf{1}, t]$. On the version of the series pulled in September 2025
($n=799$, January 1959 to July 2025), OLS gives an intercept of about $174{,}500$ (thousand) and a
slope of $213.685$ (thousand per month), with $R^2=0.997$ — almost all of the variation in
population over this window is the linear trend. Fit to the same series pulled in January 2025
($n=791$) the slope comes out at $213.235$, close but not identical, because it is a different
sample of the same noisy process.

A slope and an $R^2$ are point summaries. They say nothing about how much the fitted line itself
could plausibly have been different, and that is a separate question from how well it fits.

### The posterior is a multivariate $t$, not a normal

Under the linear Gaussian model, the posterior distribution of the coefficient vector (derived in
an earlier lecture, and used here as a known result) is

$$
\beta_0,\dots,\beta_m \mid \text{data} \;\sim\; t_{\,n-m-1}\!\left(\hat\beta,\ \frac{S(\hat\beta)}{n-m-1}(X^TX)^{-1}\right),
$$

where $\hat\beta$ is the OLS estimate, $S(\hat\beta) = \sum_i \hat\epsilon_i^2$ is the residual sum
of squares, and $n-m-1$ is the residual degrees of freedom. Two things are worth noticing about
this formula. First, the scale matrix $\hat\sigma^2(X^TX)^{-1}$, with $\hat\sigma^2 =
S(\hat\beta)/(n-m-1)$, is exactly the covariance matrix that `statsmodels` already reports as
`linmod.cov_params()` — the classical standard-error calculation and the Bayesian posterior scale
are the same matrix, computed the same way. Second, the distribution is a $t$, not a normal,
because $\sigma^2$ itself had to be estimated from the data rather than being known; the normal
would be the right answer only if $\sigma^2$ were given.

### Two routes to the same posterior samples

To see the uncertainty in the fitted line rather than just its standard errors, draw many samples
of $\beta$ from this posterior, and plot the line $X\beta^{(r)}$ for each draw over the data. The
resulting fan of lines shows which trends are consistent with the data, not just the single
best-fitting one. There are two ways to generate the samples.

The direct way calls a library routine for the multivariate $t$ directly, with location $\hat\beta$,
shape $\hat\sigma^2(X^TX)^{-1}$, and $n-m-1$ degrees of freedom (`scipy.stats.multivariate_t.rvs`).
This is what the population-trend example does with $N=1000$ draws.

The constructive way builds the same distribution from its standard representation as a
normal-variance mixture: if $Z\sim N(0,\Sigma)$ and $W\sim\chi^2_\nu$ are independent, then

$$
\hat\beta + \frac{Z}{\sqrt{W/\nu}} \;\sim\; t_\nu(\hat\beta,\Sigma).
$$

Concretely: draw $\beta$-samples from $N(\hat\beta,\Sigma)$ with $\Sigma=\hat\sigma^2(X^TX)^{-1}$,
subtract off $\hat\beta$ to center them, draw an independent $\chi^2_{n-m-1}$ value for each sample,
and divide the centered normal draw by $\sqrt{W/(n-m-1)}$ before adding $\hat\beta$ back. The
$N(\hat\beta,\Sigma)$ draws alone are what the posterior would look like *if* $\sigma^2$ were known
exactly and fixed at $\hat\sigma^2$; dividing by $\sqrt{W/\nu}$ randomly inflates each draw by a
factor usually near 1 but occasionally much larger, which is exactly the extra spread that comes
from not knowing $\sigma^2$ and having estimated it from the same data. Plotting the two sets of
samples together — normal-posterior draws and $t$-posterior draws, in the (intercept, slope) plane —
shows the same central cluster for both, but the $t$-posterior scattered with heavier tails: more
occasional draws far from the centre.

## What the fan of lines does and does not fix

Run the same procedure on Lake Huron's annual water level (1875–1972, $n=98$): the trend is much
weaker here, slope $-0.0242$ feet per year with $R^2=0.272$, an order of magnitude less explained
variance than the population fit. Sampling from the posterior and plotting the resulting fan of
lines over the data shows a visibly wider band than in the population case — correctly, since the
same amount of noise now represents a much larger fraction of the total variation, so a wider range
of slopes and intercepts is consistent with the data.

But the fan can only be as flexible as the model it comes from. Take a simulated dataset built from
a genuinely quadratic trend, $y_t = 5 + 0.8(t - n/2)^2 + \epsilon_t$ with $n=400$ and noise standard
deviation $1000$ — the quadratic term dominates the noise almost everywhere except near the centre,
so the data trace out a visible parabola. Fitting a straight line $X=[\mathbf 1, t]$ to this and
sampling its posterior gives a fan of straight lines that are all close to each other — but none of
them curve, because a straight line cannot: perturbing the two coefficients moves the line up, down,
or tilts it, and no perturbation bends it. The fan reflects only the uncertainty *within* the
straight-line model; it says nothing about whether a straight line was the right model to begin
with. Adding the quadratic covariate ($X = [\mathbf 1, t, t^2]$) and repeating the same posterior
sampling produces a fan of curves that does track the parabola. The fix was a different model, not
a wider error band on the wrong one.

<figure>
<svg viewBox="0 0 380 240" role="img" aria-label="A parabolic data trend with a fitted straight line and a fan of nearby straight-line posterior draws, none of which follow the curve">
  <line x1="30" y1="220" x2="360" y2="220" stroke="currentColor" stroke-width="1"/>
  <line x1="30" y1="20" x2="30" y2="220" stroke="currentColor" stroke-width="1"/>
  <path d="M 40,50 Q 190,230 340,50" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="40" y1="128" x2="340" y2="100" stroke="currentColor" stroke-width="1" stroke-opacity="0.3"/>
  <line x1="40" y1="118" x2="340" y2="112" stroke="currentColor" stroke-width="1" stroke-opacity="0.3"/>
  <line x1="40" y1="100" x2="340" y2="130" stroke="currentColor" stroke-width="1" stroke-opacity="0.3"/>
  <line x1="40" y1="110" x2="340" y2="118" stroke="currentColor" stroke-width="1" stroke-opacity="0.3"/>
  <line x1="40" y1="122" x2="340" y2="106" stroke="currentColor" stroke-width="1" stroke-opacity="0.3"/>
  <line x1="40" y1="112" x2="340" y2="112" stroke="currentColor" stroke-width="2"/>
  <text x="345" y="55" font-size="12" fill="currentColor">data</text>
  <text x="345" y="116" font-size="12" fill="currentColor">fitted line</text>
</svg>
<figcaption>A straight line fit to data generated from a quadratic trend. The fan of nearby lines
sampled from the coefficients' posterior stays close to the fitted line — it reflects parameter
uncertainty within the straight-line model, and cannot bend to follow the curve no matter how wide
it is. Only adding an $x^2$ covariate and refitting lets the fan track the parabola.</figcaption>
</figure>

## Harmonic regression: fitting seasonality with sines and cosines

Functions of time are not limited to polynomials. Monthly US accidental deaths (1973–1978, $n=72$)
show a clear yearly pattern, so instead of a trend the covariates are sinusoids at the seasonal
frequency and its first two harmonics:

$$
y_t = \beta_0 + \sum_{k=1}^{3}\left[\beta_{k1}\cos\!\left(\frac{2\pi k t}{12}\right) +
\beta_{k2}\sin\!\left(\frac{2\pi k t}{12}\right)\right] + \epsilon_t,
$$

with $k=1$ the fundamental annual cycle (period 12 months), $k=2$ a 6-month period, and $k=3$ a
4-month period. Each term is a known function of $t$, so the whole thing is still linear in the six
$\beta$'s and $\beta_0$, and OLS applies exactly as before. The fit gives $R^2=0.706$: the
fundamental frequency ($k=1$, both cosine and sine) is highly significant, as is the cosine term of
the first harmonic ($k=2$); the remaining three terms are not clearly distinguishable from noise.
Adding a few more harmonics buys the shape of the seasonal pattern the flexibility to depart from a
pure sine wave without giving up linearity in the coefficients.

Because every covariate here is a function of $t$ alone — never of $y$ — forecasting means simply
evaluating the same cosines and sines at future time points and multiplying by the already-fitted
$\hat\beta$. No iteration is needed: $\hat y_{n+j} = x_{n+j}^T\hat\beta$ directly, for every $j$ at
once. The worked example extends the design matrix 60 months (5 years) past the end of the data and
forecasts all of them in a single matrix multiplication.

## Autoregression: the series regressed on its own past

The second way to build $X$ uses the series' own lagged values as covariates:

$$
y_t = \beta_0 + \beta_1 y_{t-1} + \cdots + \beta_m y_{t-m} + \epsilon_t.
$$

Building the regression costs the first $m$ observations: the response and design matrix become

$$
y = \begin{pmatrix} y_{m+1} \\ y_{m+2} \\ \vdots \\ y_n \end{pmatrix}, \qquad
X = \begin{pmatrix}
1 & y_m & y_{m-1} & \cdots & y_1 \\
1 & y_{m+1} & y_m & \cdots & y_2 \\
\vdots & \vdots & \vdots & & \vdots \\
1 & y_{n-1} & y_{n-2} & \cdots & y_{n-m}
\end{pmatrix},
$$

so the regression has $n-m$ effective observations rather than $n$; each row is the same window of
$m$ consecutive values, shifted by one.

Applied to monthly FRED retail sales of beer, wine and liquor ($n=403$) with $m=12$ lags, OLS gives
$R^2=0.988$. One coefficient dominates: the 12-month lag has coefficient $\approx 0.974$ (t-statistic
over 50), meaning this month's sales are explained mainly by the same month a year earlier — the
signature of strong annual seasonality — while several nearby lags are only modestly significant
and a few are not distinguishable from noise. The regression output also flags a large condition
number, a warning that consecutive lags of a smooth series are highly collinear with each other;
that collinearity is part of why only the 12-month lag stands out cleanly while the others do not.

Forecasting an autoregression is qualitatively different from forecasting the harmonic regression
above, because the covariates for $y_{n+1}$ are the last $m$ *observed* values, but the covariates
for $y_{n+2}$ would need $y_{n+1}$, which was never observed. Forecasting therefore has to proceed
sequentially: predict $y_{n+1}$ from the observed data, treat that prediction as if it were data to
predict $y_{n+2}$, and so on, one step at a time, out to whatever horizon is wanted. The choice of
$m$ matters for how good these forecasts look: with $m<12$ the model cannot see across a full year
and the forecasts come out visibly wrong, while any $m\ge 12$ gives forecasts that look sensible.
Autoregression is picked up again in more detail later in the course; this is only the mechanics of
setting one up and fitting it by least squares.

## Sources

- Trend regression and Bayesian uncertainty quantification for US population (direct sampling
  from the multivariate $t$ posterior via `scipy.stats.multivariate_t`): berkeley-stat153,
  fall 2025, lecture 4 code notebook, "Dataset One: US Population"
  (`statistics/berkeley/stat153/fall-2025/CodeLectureFour153248Fall2025/01-dataset-one-us-population.md`).
- The same posterior, built from a normal-plus-chi-square construction, applied to US population,
  Lake Huron water levels, and the simulated quadratic-trend dataset (including the linear-then-
  quadratic model comparison behind the diagram above): berkeley-stat153, spring 2025, lecture 4
  code notebook
  (`statistics/berkeley/stat153/spring-2025/CodeLectureFour153248Spring2025.md`).
- Harmonic (Fourier) regression on monthly US accidental deaths and its direct multi-step-ahead
  forecast: berkeley-stat153, fall 2026, lecture 4 code notebook, part 1, "Example of Regression
  with functions of time: USA Accidents Dataset"
  (`statistics/berkeley/stat153/fall-2026/CodeLectureFour153248Fall2026/01-example-of-regression-with-functions-of-time-usa-accidents-d.md`).
- Autoregression on monthly beer/wine/liquor retail sales and sequential forecasting:
  berkeley-stat153, fall 2026, lecture 4 code notebook, part 2, "Example of Lagged or Auto
  Regression"
  (`statistics/berkeley/stat153/fall-2026/CodeLectureFour153248Fall2026/02-example-of-lagged-or-auto-regression.md`).

All four are code-lecture notebooks (no accompanying slide deck or transcript for this lecture): the
narrative is limited to what the notebooks themselves state, in comment text and headings. The
derivation of the multivariate-$t$ posterior for $\beta$ — stated and used across all of these
notebooks as "we have seen" — comes from an earlier lecture in the course that was not supplied
here and so is not reconstructed in this chapter; it is used here only as a stated result.

---

[← 41. Regression Uncertainty and Profile Estimation](41-regression-uncertainty-and-profile-estimation.md) · [Contents](index.md) · [43. Smoothing Trend, Variance, and Spectrum →](43-smoothing-trend-variance-and-spectrum.md)
