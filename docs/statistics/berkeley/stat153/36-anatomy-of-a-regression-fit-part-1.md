---
title: "36. Anatomy of a Regression Fit (part 1)"
course: "Berkeley Stat 153 Fall 2024"
chapter: 36
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 36. Anatomy of a Regression Fit (part 1)

## What this covers

This chapter unpacks the numbers that appear in a standard linear-regression printout — an
`OLS` summary table like the one `statsmodels` produces — by rebuilding each one from its
defining formula. The running example is a cubic trend fitted to quarterly US GDP data, so every
formula below is checked immediately against actual output. It assumes the reader can already
write down the least-squares model $y = X\beta + \epsilon$ and has seen a regression summary
table before, but treats "where do these numbers come from" as still open.

## The model: a cubic trend for GDP

The dataset is quarterly US Gross Domestic Product (billions of dollars) from FRED. Plotted
against time it has an obvious upward, curving trend, so the model fit is a cubic in time:

$$
y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \beta_3 t^3 + \epsilon_t, \qquad t = 1, \dots, n,
$$

where $n$ is the number of observations. In matrix form this is $y = X\beta + \epsilon$ with

$$
y = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix} \quad
X = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 2^2 & 2^3 \\ 1 & 3 & 3^2 & 3^3 \\
\vdots & \vdots & \vdots & \vdots \\ 1 & n & n^2 & n^3 \end{pmatrix} \quad
\beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ \beta_3 \end{pmatrix} \quad
\epsilon = \begin{pmatrix} \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n \end{pmatrix}.
$$

Here $y$ is $n \times 1$, $X$ is $n \times 4$, $\beta$ is $4 \times 1$, and $\epsilon$ is
$n \times 1$. The errors are assumed i.i.d. $\epsilon_i \sim N(0, \sigma^2)$, so the model has
five unknown parameters — $\beta_0, \beta_1, \beta_2, \beta_3, \sigma$ — to be estimated from the
data. For the GDP series, $n = 311$ and fitting this model (`sm.OLS(y, X).fit()`) gives
$R^2 = 0.995$: the cubic trend alone accounts for essentially all of the variation in the level
of GDP. Everything that follows is about what is happening inside that one call.

## Least squares estimates

The reported estimates are $\hat\beta_0 = 292.184$, $\hat\beta_1 = -2.581$,
$\hat\beta_2 = 0.0759$, $\hat\beta_3 = 0.000665$. These are the **least squares estimates**
(which for this model coincide with the maximum likelihood estimates), computed by

$$
\hat\beta = (X^TX)^{-1}X^Ty.
$$

Forming $X^TX$, inverting it, and multiplying by $X^Ty$ by hand reproduces `md.params` exactly
(to numerical precision). In practice a regression routine does not literally invert $X^TX$ —
that formula is correct but numerically wasteful — it instead solves the linear system
$X^TX\beta = X^Ty$ with a more stable algorithm. The formula is the right way to *understand*
the estimate; it is not how software *computes* it.

### Fitted values

The fitted values $\hat y = X\hat\beta$ are the model's prediction at each observed time point.
Plotting $y$ and $\hat y$ together against time shows the cubic trend tracking the broad shape of
GDP growth closely — which is exactly what an $R^2$ of $0.995$ says it should do.

## Residuals

The residuals are the leftover discrepancies between data and fit,

$$
e = y - \hat y,
$$

and $e_i$ is the $i$-th entry. A plot of $e$ against time is a basic diagnostic. For the GDP fit
it shows two things worth separating:

1. **Some very large residuals.** These flag time points where the model's prediction is far
   from the data — either outliers, or systematic structure the model is missing.
2. **A smooth-looking residual series.** Consecutive residuals do not look independent; they
   drift together over stretches of several quarters, which suggests correlation between nearby
   residuals rather than noise.

The second point is worth pinning down with a contrast. Suppose instead the *true* process were
exactly this cubic model with genuinely i.i.d. noise: generate $z = X\gamma + \eta$ for a fixed
$\gamma = (300, -3, 0.1, 0.001)$ and $\eta_t \sim N(0,1)$ i.i.d., then fit the same model to $z$.
The fitted coefficients recover $\gamma$ almost exactly
($\hat\gamma \approx (299.767, -2.996, 0.09998, 0.0010000)$), and — this is the point — the
residual plot from that fit looks like plain noise, with no visible run structure. The real GDP
residual plot does not look like that. That difference is the evidence that the cubic trend is
missing something systematic, and the tool for making "smooth-looking residuals" precise is the
autocorrelation function.

## The ACF plot: autocorrelation of the residuals

Given a series $z_1, \dots, z_n$ and a lag $h = 0, 1, 2, \dots$, define the **sample
autocorrelation**

$$
r_h := \frac{\sum_{t=1}^{n-h} (z_t - \bar z)(z_{t+h} - \bar z)}{\sum_{t=1}^n (z_t - \bar z)^2},
$$

where $\bar z$ is the mean of the whole series. The **ACF plot** (or correlogram) graphs $h$
against $r_h$; by construction $r_0 = 1$ always, so the content of the plot is in $r_h$ for
$h \geq 1$.

$r_h$ is an approximation to an ordinary sample correlation. If you form the bivariate dataset
of pairs $h$ apart, $(z_1, z_{h+1}), (z_2, z_{h+2}), \dots, (z_{n-h}, z_n)$, its sample
correlation is

$$
\frac{\sum_{t=1}^{n-h} (z_t - \bar z^{(1)})(z_{t+h} - \bar z^{(2)})}
{\sqrt{\sum_{t=1}^{n-h}(z_t-\bar z^{(1)})^2}\sqrt{\sum_{t=1}^{n-h}(z_{t+h}-\bar z^{(2)})^2}},
\qquad
\bar z^{(1)} = \frac{\sum_{t=1}^{n-h} z_t}{n-h}, \quad
\bar z^{(2)} = \frac{\sum_{t=1}^{n-h} z_{t+h}}{n-h}.
$$

Replacing the two separate means $\bar z^{(1)}, \bar z^{(2)}$ by the overall mean $\bar z$, and
extending the sums in the denominator to run over all $t = 1, \dots, n$ rather than just
$t = 1, \dots, n-h$, turns this into the formula for $r_h$. Both replacements are harmless when
$n$ is large and $h$ is small relative to $n$ — which is the usual regime an ACF plot is read in.

Plotting the ACF of the GDP regression's residuals out to lag 50 shows large autocorrelations,
especially at small lags. The plot also carries a shaded band automatically: this is a reference
for what autocorrelations look like under pure noise. Even if the data really were i.i.d.
$N(0,\sigma^2)$ — so that every true autocorrelation is zero — the *sample* autocorrelations
would still be nonzero purely from sampling variability; the shaded band shows the typical size of
that noise (computed by fitting the same plot to a batch of simulated i.i.d. $N(0,1)$ values).
The rule of thumb is to treat $r_h$ as meaningfully nonzero only once it sticks out past the band.

<figure>
<svg viewBox="0 0 360 210" role="img" aria-label="Sample autocorrelation function of the GDP regression residuals, with lags 1 through 3 sticking out above the null confidence band">
  <rect x="30" y="155.6" width="315" height="28.9" fill="currentColor" fill-opacity="0.15"/>
  <line x1="30" y1="170" x2="345" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="50" y1="170" x2="50" y2="40" stroke="currentColor" stroke-width="10"/>
  <line x1="85" y1="170" x2="85" y2="63.4" stroke="#d97706" stroke-width="10"/>
  <line x1="120" y1="170" x2="120" y2="92" stroke="#d97706" stroke-width="10"/>
  <line x1="155" y1="170" x2="155" y2="120.6" stroke="#d97706" stroke-width="10"/>
  <line x1="190" y1="170" x2="190" y2="158.3" stroke="currentColor" stroke-width="10"/>
  <line x1="225" y1="170" x2="225" y2="172.6" stroke="currentColor" stroke-width="10"/>
  <line x1="260" y1="170" x2="260" y2="164.8" stroke="currentColor" stroke-width="10"/>
  <line x1="295" y1="170" x2="295" y2="171.3" stroke="currentColor" stroke-width="10"/>
  <line x1="330" y1="170" x2="330" y2="166.1" stroke="currentColor" stroke-width="10"/>
  <text x="50" y="188" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="85" y="188" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="120" y="188" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="155" y="188" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="190" y="188" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <text x="225" y="188" text-anchor="middle" font-size="11" fill="currentColor">5</text>
  <text x="260" y="188" text-anchor="middle" font-size="11" fill="currentColor">6</text>
  <text x="295" y="188" text-anchor="middle" font-size="11" fill="currentColor">7</text>
  <text x="330" y="188" text-anchor="middle" font-size="11" fill="currentColor">8</text>
  <text x="187" y="204" text-anchor="middle" font-size="12" fill="currentColor">lag h</text>
</svg>
<figcaption>Sample autocorrelation $r_h$ of the residuals against lag $h$, with the shaded null
band roughly $\pm 1.96/\sqrt n$: lags 1–3 stick out well past it, later lags mostly do not.</figcaption>
</figure>

The significant autocorrelations at small lags (especially $h = 1, 2, 3$) have a direct
forecasting consequence. Suppose you want to predict GDP for the quarter right after the last
observation. The naive forecast is just the model's fitted value there. But the actual last
residual is about $2548$ — far from zero — and because of the strong positive autocorrelation at
lag 1, the *next* residual is likely to be strongly positive as well. So a better forecast nudges
the model's prediction upward by roughly that amount. This matches what the plot of data versus
fitted values already suggests visually, and it is the kind of correction the course develops
into proper forecasting procedures later.

## Residual sum of squares, residual degrees of freedom, and $\hat\sigma$

The **residual sum of squares** is

$$
\text{RSS} = \sum_{i=1}^n e_i^2 = \sum_{t=1}^n \left(y_t - \hat\beta_0 - \hat\beta_1 t -
\hat\beta_2 t^2 - \hat\beta_3 t^3\right)^2,
$$

which is exactly the minimum value achieved by the least-squares criterion
$S(\beta_0,\beta_1,\beta_2,\beta_3) = \sum_t (y_t - \beta_0 - \beta_1 t - \beta_2 t^2 -
\beta_3 t^3)^2$ that $\hat\beta$ was chosen to minimize.

The residual vector satisfies an important identity, $X^Te = 0$:

$$
X^Te = X^T(y-\hat y) = X^T(y - X\hat\beta) = X^T\Big(y - X(X^TX)^{-1}X^Ty\Big)
     = X^Ty - X^TX(X^TX)^{-1}X^Ty = X^Ty - X^Ty = 0.
$$

Since $X^Te = 0$ says the dot product of $e$ with every column of $X$ is zero, for this model it
is four scalar constraints:

$$
\sum_t e_t = 0, \qquad \sum_t t\,e_t = 0, \qquad \sum_t t^2 e_t = 0, \qquad \sum_t t^3 e_t = 0.
$$

So although there are $n$ residuals, they are forced to satisfy four linear constraints, leaving
only $n - 4$ of them "free." That is the **residual degrees of freedom**. More generally, residual
df is the number of observations minus the number of columns of $X$ — here $311 - 4 = 307$.

The estimate of $\sigma$, the **residual standard error**, is

$$
\hat\sigma = \sqrt{\frac{\text{RSS}}{n-4}} = \sqrt{\frac{S(\hat\beta_0,\hat\beta_1,\hat\beta_2,\hat\beta_3)}{n-4}}.
$$

For the GDP fit, $\hat\sigma \approx 550.99$. It gives a scale for judging the residuals: a
residual much larger in magnitude than about twice $\hat\sigma$ — here, above roughly $1100$ —
marks a point where the model fits particularly poorly, and the residual-vs-time plot shows
several residuals in that range.

### Standard errors of the coefficients

The standard errors reported alongside $\hat\beta_0, \dots, \hat\beta_3$ (`md.bse`) are the
square roots of the diagonal entries of

$$
\hat\sigma^2 (X^TX)^{-1}.
$$

Recomputing this from $\hat\sigma$ and the already-inverted $(X^TX)^{-1}$ reproduces `md.bse`
exactly.

## t-statistics and confidence intervals

The **$t$-statistic** for each coefficient is just the estimate divided by its standard error.
The confidence interval for $\beta_j$ is

$$
\left[\hat\beta_j - t_{\alpha/2,\,n-4}\;\mathrm{se}(\hat\beta_j),\;\;
       \hat\beta_j + t_{\alpha/2,\,n-4}\;\mathrm{se}(\hat\beta_j)\right],
$$

where $t_{\alpha/2,\,n-4}$ is the point beyond which the $t$-distribution with $n-4$ degrees of
freedom has probability mass $\alpha/2$. This comes directly from the distributional result

$$
\frac{\beta_j - \hat\beta_j}{\mathrm{se}(\hat\beta_j)} \;\Big|\; \text{data} \;\sim\; t_{n-4}.
$$

That statement can be read two ways: conditionally on the data with $\beta_j$ random (a Bayesian
reading), or — dropping the conditioning and letting the data be the random quantity with
$\beta_j$ fixed — as the ordinary frequentist sampling distribution used to justify the interval.
Both readings give the same interval formula.

For $\alpha = 0.05$ and $n - 4 = 307$, $t_{0.025,\,307} \approx 1.9677$. Plugging in gives:

| Term | $\hat\beta$ | std. err. | $t$ | $P(>\lvert t\rvert)$ | 95% CI |
|---|---|---|---|---|---|
| intercept | $292.184$ | $126.498$ | $2.310$ | $0.022$ | $[43.271,\ 541.097]$ |
| $t$ | $-2.581$ | $3.506$ | $-0.736$ | $0.462$ | $[-9.479,\ 4.317]$ |
| $t^2$ | $0.0759$ | $0.0261$ | $2.910$ | $0.004$ | $[0.025,\ 0.127]$ |
| $t^3$ | $0.000665$ | $0.0000550$ | $12.093$ | $0.000$ | $[0.001,\ 0.001]$ |

Notice the coefficient on the linear term $t$ is not significant at all — its interval comfortably
contains zero — while $t^2$ and especially $t^3$ are. The regression summary also flags a large
condition number ($\approx 4.63\times 10^7$), a warning about strong multicollinearity: the
columns $t, t^2, t^3$ over a range of $1$ to $311$ are highly correlated with each other, which is
exactly the kind of thing that inflates individual coefficient standard errors and can make an
individually "insignificant" coefficient still matter to the fit as a whole.

## Visualizing the uncertainty in $\hat\beta$

A confidence interval per coefficient does not by itself say how uncertain the *fitted curve* is,
especially when the coefficients are correlated the way multicollinearity implies. A more direct
picture comes from the posterior distribution of $\beta$, derived elsewhere in the course
(not reproduced here) as

$$
\beta \mid \text{data} \;\sim\; t_4\Big(\hat\beta,\ \hat\sigma^2(X^TX)^{-1},\ n-4\Big),
$$

a multivariate $t$-distribution in the 4 coefficients, with location $\hat\beta$, scale matrix
$\hat\sigma^2(X^TX)^{-1}$, and $n-4$ degrees of freedom. Such a distribution can be represented as
a normal variable divided by an independent chi-squared variable:

$$
\hat\beta + \frac{Z}{\sqrt{V/(n-4)}}, \qquad Z \sim N\!\big(0,\ \hat\sigma^2(X^TX)^{-1}\big),
\quad V \sim \chi^2_{n-4}, \quad Z \perp V.
$$

That representation is what makes the posterior easy to sample from: draw $V$ from $\chi^2_{n-4}$
and $Z$ from the multivariate normal, combine them, and repeat. Drawing $N = 200$ such $\beta$
vectors and plotting the resulting regression curve $X\beta$ for each one, overlaid on the data,
turns coefficient uncertainty into a picture of curve uncertainty.

The result for the GDP fit is that the $200$ curves stay tightly bunched together, even though
individual coefficients (the linear term especially) have wide, sign-ambiguous intervals. That is
consistent with the multicollinearity flagged above: errors in the individual coefficients are
correlated with each other and largely cancel when recombined into $X\hat\beta$, so the fitted
*curve* is much more tightly pinned down than any single coefficient looks on its own.

## Other transformations of the data

Two variants of the outcome variable are common in this kind of analysis. Taking $y = \log(\text{GDP})$
tends to stabilize the exponential-looking growth. Taking the difference of logs,
$y_t = \log(\text{GDP}_t) - \log(\text{GDP}_{t-1})$, is interpreted as the GDP growth rate. The
second is particularly convenient for prediction: a forecast of the future difference-of-logs can
be converted back into a forecast of the original GDP level.

## Sources

All material in this chapter comes from the Stat 153 (Berkeley) "Linear Regression Details" code
lab, converted to markdown from the course notebook `CodeLabTwo153248Fall2025.ipynb`
(`docs/statistics/berkeley/stat153/fall-2025/CodeLabTwo153248Fall2025/`, sections
`01-introduction.md` through `07-visualizing-uncertainty.md`, CC BY 4.0). The GDP data, cubic
trend model, least-squares formula, residual and fitted-value checks, the residual-vs-simulated-noise
comparison, the ACF definition and its reading, the RSS/residual-df identity and proof, the
residual standard error, coefficient standard errors, $t$-statistics and confidence intervals, the
posterior-sampling visualization, and the closing remark on logs and log-differences are all drawn
directly from that notebook's worked GDP example and its surrounding text.

The parallel fall-2026 version of the same notebook
(`docs/statistics/berkeley/stat153/fall-2026/CodeLabTwo153248Fall2026/`) is the same lab with the
same numbers; it differs only cosmetically (import order, run dates/times, a minor rewording of
the posterior-distribution notation) and omits the simulated-noise residual comparison that
fall-2025 includes, which is why fall-2025 is the version followed here.

The notebook itself states that the posterior distribution of $\beta$ used in "Visualizing the
uncertainty" was derived "in Lecture 4" of the course — that derivation is not part of the
supplied material and is not reproduced here; the result is used as given, as the notebook does.

---

[← 35. Estimating MA(1) Parameters](35-estimating-ma-1-parameters.md) · [Contents](index.md) · [37. The Periodogram and Sinusoidal Models →](37-the-periodogram-and-sinusoidal-models.md)
