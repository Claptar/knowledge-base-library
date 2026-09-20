---
title: "93. Anatomy of a Regression Fit (part 2)"
course: "Berkeley Stat 153 Fall 2024"
chapter: 93
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 93. Anatomy of a Regression Fit (part 2)

## What this covers

A standard `sm.OLS` regression printout is a wall of numbers — coefficients, standard errors,
t-statistics, an F-statistic, a condition number. This chapter takes that printout apart and
rebuilds each entry from the design matrix and the data, using a single worked example: a cubic
trend fitted to sixty years of quarterly US GDP. It assumes the reader already has the linear
model $y = X\beta + \epsilon$ and knows what least squares estimation is aiming to do; the goal
here is to see *why* the reported numbers are what they are, and then to go one step further, from
a fixed confidence interval to a full posterior distribution over the fitted curve.

## The model and the design matrix

The running example is quarterly US GDP (FRED series `GDP`, in billions of dollars), $n = 311$
observations running from 1947Q1 to 2024Q3. A cubic trend is fit to it:

$$
y_t = \beta_0 + \beta_1 t + \beta_2 t^2 + \beta_3 t^3 + \epsilon_t, \qquad t = 1, \dots, n,
$$

with $\epsilon_1, \dots, \epsilon_n$ i.i.d. $N(0, \sigma^2)$. Written in matrix form, $y = X\beta +
\epsilon$, with

$$
y = \begin{pmatrix} y_1\\ y_2 \\ \vdots \\ y_n \end{pmatrix}, \quad
X = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 2^2 & 2^3 \\ 1 & 3 & 3^2 & 3^3 \\ \vdots & \vdots &
\vdots & \vdots \\ 1 & n & n^2 & n^3 \end{pmatrix}, \quad
\beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ \beta_3 \end{pmatrix}, \quad
\epsilon = \begin{pmatrix} \epsilon_1 \\ \epsilon_2 \\ \vdots \\ \epsilon_n \end{pmatrix}.
$$

Here $y$ is $n \times 1$, $X$ is $n \times 4$, $\beta$ is $4 \times 1$, and $\epsilon$ is $n \times
1$. There are five unknown parameters — $\beta_0, \beta_1, \beta_2, \beta_3, \sigma$ — to estimate
from the data, and everything that follows is about how to estimate them and how much to trust the
estimates.

## Least squares estimates

The least squares estimates (which coincide with the maximum likelihood estimates under the normal
error model above) are

$$
\hat\beta = \begin{pmatrix} \hat\beta_0 \\ \hat\beta_1 \\ \hat\beta_2 \\ \hat\beta_3 \end{pmatrix} =
(X^T X)^{-1} X^T y.
$$

For the GDP fit this gives $\hat\beta_0 = 292.18$, $\hat\beta_1 = -2.581$, $\hat\beta_2 = 0.0759$,
$\hat\beta_3 = 0.000665$ — exactly what `sm.OLS(y, X).fit()` reports via `model.params`, and
exactly what computing $(X^TX)^{-1}X^Ty$ by hand produces. In practice `sm.OLS` does not literally
invert $X^TX$ and multiply; it solves the normal equations $X^TX\beta = X^Ty$ with more numerically
stable linear algebra. That distinction matters here: the printed summary flags a large condition
number ($4.63 \times 10^7$) with a warning about possible multicollinearity, because raw powers of
$t = 1, \dots, n$ are highly collinear columns of $X$. The formula $(X^TX)^{-1}X^Ty$ is still
mathematically correct; it is just not how a good solver would compute it.

The fitted values are $\hat y = X\hat\beta$, and plotting $\hat y$ against the raw series shows a
smooth cubic curve running through six decades of quarterly GDP.

## Residuals

The residuals are the gap between the data and the fit:

$$
e = y - \hat y, \qquad e_i = y_i - \hat y_i.
$$

Plotting $e$ against time is a basic diagnostic. For the GDP fit, the plot shows some very large
residuals — points where the cubic trend is far from the observed value — and the residual series
looks *smooth* rather than jagged, which is itself informative: it suggests the residuals near each
other in time are correlated, not independent noise. The single largest-magnitude residual in this
fit occurs at **2020-04-01** — the COVID-19 quarter — which a smooth deterministic trend has no way
to capture. That combination, one dramatic outlier plus a generally smooth residual series, is
exactly what motivates looking at the residuals' own autocorrelation next.

## The autocorrelation of the residuals

Given a time series $z_1, \dots, z_n$ and a lag $h = 0, 1, 2, \dots$, the **sample autocorrelation**
at lag $h$ is

$$
r_h := \frac{\sum_{t=1}^{n-h} (z_t - \bar z)(z_{t+h} - \bar z)}{\sum_{t=1}^n (z_t - \bar z)^2},
$$

where $\bar z$ is the mean of $z_1, \dots, z_n$. The **ACF plot** (also called a correlogram) plots
$r_h$ against $h$; by construction $r_0 = 1$ always, so the plot is really about the size of $r_h$
for $h \geq 1$.

Where does this formula come from? For large $n$ and small $h$, $r_h$ is an approximation to the
ordinary sample correlation of the bivariate dataset $(z_1, z_{h+1}), (z_2, z_{h+2}), \dots,
(z_{n-h}, z_n)$, whose exact formula is

$$
\frac{\sum_{t=1}^{n-h} (z_t - \bar z^{(1)})(z_{t+h} - \bar z^{(2)})}
{\sqrt{\sum_{t=1}^{n-h} (z_t - \bar z^{(1)})^2}\sqrt{\sum_{t=1}^{n-h} (z_{t+h} - \bar z^{(2)})^2}},
\qquad \bar z^{(1)} = \frac{\sum_{t=1}^{n-h} z_t}{n-h}, \quad \bar z^{(2)} = \frac{\sum_{t=1}^{n-h}
z_{t+h}}{n-h}.
$$

Approximating both means by the overall mean $\bar z$, and extending the sums in the denominator to
run over all $t = 1, \dots, n$ rather than stopping at $n - h$, turns this expression into $r_h$.
Both approximations are reasonable exactly when $n$ is large and $h$ is small — which is the usual
regime of interest.

Running this on the GDP residuals shows significant autocorrelation at small lags, especially $h =
1, 2, 3$. To judge "significant," compare against what pure noise would produce: even genuinely
i.i.d. $N(0, \sigma^2)$ data will show nonzero *sample* autocorrelations purely by chance, and the
typical size of these spurious autocorrelations is what a plotting package shades as a band around
zero. A bar that stays inside the band is consistent with noise; one that sticks out is read as
real serial correlation.

<figure>
<svg viewBox="0 0 380 220" role="img" aria-label="Schematic autocorrelation function with a significance band, showing large autocorrelations at small lags decaying into the band at larger lags">
  <rect x="45" y="135" width="290" height="30" fill="currentColor" fill-opacity="0.15"/>
  <line x1="40" y1="15" x2="40" y2="178" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="150" x2="335" y2="150" stroke="currentColor" stroke-width="1.2"/>
  <line x1="60" y1="150" x2="60" y2="20" stroke="currentColor" stroke-width="4"/>
  <line x1="88" y1="150" x2="88" y2="39.5" stroke="currentColor" stroke-width="4"/>
  <line x1="116" y1="150" x2="116" y2="61.6" stroke="currentColor" stroke-width="4"/>
  <line x1="144" y1="150" x2="144" y2="82.4" stroke="currentColor" stroke-width="4"/>
  <line x1="172" y1="150" x2="172" y2="111" stroke="currentColor" stroke-width="4"/>
  <line x1="200" y1="150" x2="200" y2="130.5" stroke="currentColor" stroke-width="4"/>
  <line x1="228" y1="150" x2="228" y2="143.5" stroke="currentColor" stroke-width="4"/>
  <line x1="256" y1="150" x2="256" y2="153.9" stroke="currentColor" stroke-width="4"/>
  <line x1="284" y1="150" x2="284" y2="140.9" stroke="currentColor" stroke-width="4"/>
  <line x1="312" y1="150" x2="312" y2="161.7" stroke="currentColor" stroke-width="4"/>
  <text x="60" y="192" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="116" y="192" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="172" y="192" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <text x="228" y="192" text-anchor="middle" font-size="11" fill="currentColor">6</text>
  <text x="284" y="192" text-anchor="middle" font-size="11" fill="currentColor">8</text>
  <text x="190" y="210" text-anchor="middle" font-size="12" fill="currentColor">lag h</text>
  <text x="18" y="24" font-size="12" fill="currentColor">r_h</text>
</svg>
<figcaption>Schematic ACF plot: bars are the sample autocorrelations at each lag, the shaded band
is the typical size of autocorrelation produced by pure noise. Bars reaching outside the band, as
at small lags here, are read as real serial correlation rather than sampling noise — this is the
pattern the GDP residuals show at $h = 1, 2, 3$.</figcaption>
</figure>

This has a direct forecasting consequence. Suppose the goal is to predict GDP for the quarter
immediately after the last observation. Using the model's point prediction alone ignores the fact
that the *last* residual is not zero — for this fit it is about $2548$ (billions of dollars), a
large positive number. Because the residuals show significant positive autocorrelation at lag 1,
the next residual is also expected to be positive, so a better forecast adjusts the model's raw
prediction upward by roughly that amount. This is visible directly in the plot of data against
fitted values, and it is the sort of correction the course returns to later with proper forecasting
procedures.

## Residual sum of squares and residual degrees of freedom

The **residual sum of squares** is

$$
\text{RSS} = \sum_{i=1}^n e_i^2 = \sum_{t=1}^n \left(y_t - \hat\beta_0 - \hat\beta_1 t -
\hat\beta_2 t^2 - \hat\beta_3 t^3\right)^2,
$$

and it equals the minimum value of the least-squares criterion $S(\beta_0, \beta_1, \beta_2,
\beta_3) = \sum_t (y_t - \beta_0 - \beta_1 t - \beta_2 t^2 - \beta_3 t^3)^2$ — RSS is $S$ evaluated
at the minimizer $\hat\beta$.

The residual vector satisfies a property worth deriving explicitly, $X^T e = 0$:

$$
X^T e = X^T(y - \hat y) = X^T(y - X\hat\beta) = X^T\!\left(y - X(X^TX)^{-1}X^Ty\right)
= X^Ty - X^TX(X^TX)^{-1}X^Ty = X^Ty - X^Ty = 0.
$$

$X^Te = 0$ says the dot product of every column of $X$ with $e$ is zero. For the GDP model this
unpacks into four separate constraints on the residuals:

$$
\sum_t e_t = 0, \qquad \sum_t t\, e_t = 0, \qquad \sum_t t^2 e_t = 0, \qquad \sum_t t^3 e_t = 0.
$$

So although there are $n$ residuals, they cannot vary freely: four linear constraints tie them
together, leaving $n - 4$ "free" residuals. This is the residual degrees of freedom. More
generally, the residual degrees of freedom is $n$ minus the number of columns of $X$ (equivalently,
the number of parameters being estimated in the mean).

### The residual standard error

The natural estimate of $\sigma$ follows immediately:

$$
\hat\sigma = \sqrt{\frac{\text{RSS}}{n - 4}} = \sqrt{\frac{S(\hat\beta_0, \hat\beta_1, \hat\beta_2,
\hat\beta_3)}{n-4}},
$$

sometimes called the **Residual Standard Error**. For the GDP fit $\hat\sigma \approx 550.99$
(billions of dollars). This number is a yardstick for the residual plot: a residual much larger
than about twice the residual standard error — here, above roughly $1{,}100$ — marks a point where
the model fits particularly poorly, and the residual plot for this fit has several such points.

## Standard errors, t-statistics, and confidence intervals

The standard errors attached to $\hat\beta_0, \hat\beta_1, \hat\beta_2, \hat\beta_3$ are the square
roots of the diagonal entries of

$$
\hat\sigma^2 (X^TX)^{-1}.
$$

This is exactly what `model.bse` reports. Dividing each estimate by its standard error gives the
**t-statistic** for that coefficient, and the confidence interval for $\beta_j$ is

$$
\left[\hat\beta_j - t_{\alpha/2,\, n-4}\cdot \text{SE}(\hat\beta_j),\ \ \hat\beta_j +
t_{\alpha/2,\, n-4}\cdot \text{SE}(\hat\beta_j)\right],
$$

where $t_{\alpha/2, n-4}$ is the value beyond which the $t$-distribution with $n - 4$ degrees of
freedom has probability mass $\alpha/2$. This interval is exactly the statement

$$
\frac{\beta_j - \hat\beta_j}{\text{SE}(\hat\beta_j)} \,\Big|\, \text{data} \sim
t\text{-distribution with } n - 4 \text{ d.f.},
$$

inverted to solve for $\beta_j$. That statement can be read two ways: conditionally on the data (a
statement about where the true $\beta_j$ plausibly sits, given what was observed), or in the
frequentist sense, dropping the conditioning on data and instead treating $\beta_j$ as fixed while
the *data* is random. Both readings give the same interval; they differ only in what randomness is
being described.

For the GDP fit ($n - 4 = 307$, $t_{0.025, 307} \approx 1.968$):

| coefficient | estimate | std. error | t | p-value | 95% CI |
|---|---|---|---|---|---|
| $\beta_0$ | $292.18$ | $126.50$ | $2.31$ | $0.022$ | $[43.27,\ 541.10]$ |
| $\beta_1$ | $-2.581$ | $3.506$ | $-0.74$ | $0.462$ | $[-9.48,\ 4.32]$ |
| $\beta_2$ | $0.0759$ | $0.0261$ | $2.91$ | $0.004$ | $[0.0246,\ 0.1273]$ |
| $\beta_3$ | $0.000665$ | $0.0000550$ | $12.09$ | $<0.001$ | $[0.000557,\ 0.000773]$ |

Notice $\beta_1$'s interval comfortably contains zero — on its own, the linear term is not
distinguishable from noise here. That is worth remembering going into the next section, because it
does not mean the *fitted curve* is poorly determined.

## Visualizing the uncertainty in $\hat\beta$

The confidence intervals above summarize uncertainty one coefficient at a time. A fuller picture
comes from the joint distribution of $\beta$ given the data, which (as derived elsewhere in the
course, referred to here as "Lecture 4" but not reproduced in this material) is a multivariate
$t$-distribution:

$$
\beta \mid \text{data} \sim t_{n-4,\,4}\!\left(\hat\beta,\ \hat\sigma^2(X^TX)^{-1}\right).
$$

The same matrix $(X^TX)^{-1}$ that produced the individual standard errors above is the scale
matrix of this joint posterior. A $t_{n-4,4}$ random vector centered at $\hat\beta$ with that scale
matrix can be represented as

$$
\hat\beta + \frac{Z}{\sqrt{V/(n-4)}}, \qquad Z \sim N\!\left(0,\ \hat\sigma^2(X^TX)^{-1}\right),\
V \sim \chi^2_{n-4},\ Z \perp V.
$$

This representation is directly simulatable: draw $Z$ from the multivariate normal and $V$ from the
chi-squared distribution, combine them to get a posterior draw $\beta^{(k)}$, and plot the
resulting regression curve $X\beta^{(k)}$. Doing this $N = 200$ times and overlaying every curve on
the data gives a visual sense of how much the *fitted curve* — not any one coefficient — could
plausibly have looked different.

For the GDP fit, the $200$ sampled curves come out tightly clustered together, despite $\beta_1$
individually having a confidence interval that includes zero. The two facts are compatible: the
columns of $X$ are highly correlated (the same collinearity flagged by the large condition number
earlier), so individual coefficients trade off against each other while the curve $X\beta$ as a
whole stays well pinned down by the data. Uncertainty in a single coefficient and uncertainty in
the fitted trend are not the same question.

## Exercises

The lab closes with two open-ended prompts, restated here.

1. Refit the same cubic-trend design (an intercept plus $t, t^2, t^3$) to $y_t = \log(\text{GDP}_t)$
   instead of the raw GDP series, and report the fitted regression equation.
2. Refit the cubic-trend design to the differenced log series $y_t = \log(\text{GDP}_t) -
   \log(\text{GDP}_{t-1})$ — interpretable as the quarterly GDP growth rate — and report the fitted
   equation. Then explain how a prediction of a future value of this differenced series can be
   turned into a prediction of the original GDP level.

## Sources

All material in this chapter comes from Berkeley STAT 153 (spring 2025), Lab 2, converted from
`Lab2.ipynb` (CC BY 4.0). No slide deck or lecture transcript was supplied for this chapter; the
notebook itself carries the exposition.

- Model setup, design matrix, `sm.OLS` fit and its printed summary —
  `01-introduction.md`.
- Least squares formula, numerical verification, fitted values —
  `02-least-squares-estimates.md`.
- Residuals, residual plot, the 2020-04-01 outlier —
  `03-residuals.md`.
- Sample autocorrelation $r_h$, ACF plot, significance bands, the forecast-adjustment example
  (last residual $\approx 2548$) — `04-acf-plot.md`.
- RSS, the $X^Te = 0$ derivation, residual degrees of freedom, residual standard error —
  `05-residual-sum-of-squares-rss-and-residual-df.md`.
- Standard errors, t-statistics, confidence intervals, the frequentist/conditional-on-data
  reading — `06-t-statistic-and-confidence-intervals-for-the-coefficients.md`.
- Posterior distribution of $\beta$, the normal/chi-squared sampling representation, the posterior
  simulation of fitted curves, and the two closing exercises —
  `07-visualizing-uncertainty.md`.

The derivation of the posterior $\beta \mid \text{data} \sim t_{n-4,4}(\hat\beta,
\hat\sigma^2(X^TX)^{-1})$ is attributed by the notebook to "Lecture 4" of the course; that lecture's
material is referred to but was not part of the supplied input and is not reproduced here.

---

[← 92. Change of Variables and MLE](92-change-of-variables-and-mle.md) · [Contents](index.md) · [94. Frequency Estimation and Aliasing →](94-frequency-estimation-and-aliasing.md)
