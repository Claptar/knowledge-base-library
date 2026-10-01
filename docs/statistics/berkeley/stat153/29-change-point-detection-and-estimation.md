---
title: "29. Change-Point Detection and Estimation"
course: "Berkeley Stat 153"
chapter: 29
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 29. Change-Point Detection and Estimation

## What this covers

How to locate a sudden shift in the level of a time series — a **change-point** — from data
alone. It sets up the change-point regression model, shows how to estimate the change-point by
profiling the residual sum of squares, gives the (non-derived, as-given) Bayesian posterior over
the change-point and shows how to sample from it, and then extends everything to several
change-points, comparing an exhaustive grid search against a much faster iterative scheme. It
assumes familiarity with ordinary least squares regression (design matrices, RSS, degrees of
freedom) and with the basic vocabulary of Bayesian inference (prior, posterior, sampling from a
posterior).

## The change-point regression model

Suppose a series $y_1, \dots, y_n$ sits at one level for a while and then jumps to another level
partway through. The model for this is

$$
y_t = \beta_0 + \beta_1 I\{t > c\} + \epsilon_t,
$$

where $I\{t > c\}$ is the indicator function, equal to $1$ if $t > c$ and $0$ otherwise. The mean
function $\beta_0 + \beta_1 I\{t > c\}$ equals $\beta_0$ up to time $c$ and $\beta_0 + \beta_1$
after it, so the series has level $\beta_0$ until the change-point $c$, then switches to level
$\beta_0 + \beta_1$.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Step function showing the mean level beta_0 before the change-point c and beta_0 plus beta_1 after it">
  <line x1="40" y1="20" x2="40" y2="160" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1.2"/>
  <text x="300" y="178" text-anchor="end" font-size="12" fill="currentColor">t</text>
  <line x1="40" y1="110" x2="170" y2="110" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="60" x2="300" y2="60" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="60" x2="170" y2="110" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="40" y1="110" x2="300" y2="110" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2,4" opacity="0.5"/>
  <line x1="40" y1="60" x2="170" y2="60" stroke="currentColor" stroke-width="0.6" stroke-dasharray="2,4" opacity="0.5"/>
  <text x="30" y="114" text-anchor="end" font-size="12" fill="currentColor">&#946;&#8320;</text>
  <text x="30" y="64" text-anchor="end" font-size="12" fill="currentColor">&#946;&#8320;+&#946;&#8321;</text>
  <text x="170" y="175" text-anchor="middle" font-size="12" fill="currentColor">c</text>
</svg>
<figcaption>The mean function of the change-point model: level β₀ up to time c, level β₀+β₁ after it. The data are this step plus noise.</figcaption>
</figure>

Given the data $y_1, \dots, y_n$, the parameters to infer are $c$, $\beta_0$, $\beta_1$, and the
noise scale $\sigma$. The change-point $c$ is what makes the model nonlinear: if $c$ were known in
advance, the model would be an ordinary linear regression with design matrix

$$
X_c = \begin{pmatrix} 1 & I\{1 > c\} \\ 1 & I\{2 > c\} \\ \vdots & \vdots \\ 1 & I\{n > c\} \end{pmatrix}.
$$

## Estimating the change-point by profiling the RSS

The trick for a nonlinear parameter that would make everything linear if only it were known is to
**profile it out**: for each candidate value of $c$, fit the linear regression and record its
residual sum of squares,

$$
\mathrm{RSS}(c) := \min_{\beta_0, \beta_1} \sum_{t=1}^n \big(y_t - \beta_0 - \beta_1 I\{t > c\}\big)^2,
$$

and then minimize $\mathrm{RSS}(c)$ over $c$ to get the MLE $\hat c$. Since $c$ only takes integer
values from $1$ to $n-1$, this minimization is a grid search: fit the regression at every
candidate $c$, plot $\mathrm{RSS}(c)$ against $c$, and read off the minimizer. Once $\hat c$ is
fixed, $\hat\beta_0, \hat\beta_1$ are just the OLS estimates from the regression with design matrix
$X_{\hat c}$, and $\sigma$ is estimated from the residuals in the usual two ways — the MLE
$\sqrt{\mathrm{RSS}(\hat c)/n}$ and the (nearly identical, for large $n$) unbiased version
$\sqrt{\mathrm{RSS}(\hat c)/(n-p)}$ with $p = 2$ parameters in $\beta$.

### Worked example

A series of length $n = 10{,}000$ was simulated with true levels $\mu_1 = 0$ before the midpoint
and $\mu_2 = 0.4$ after it, Gaussian noise with $\sigma = 1$, and true change-point $c = 5000$.
Plotting $\mathrm{RSS}(c)$ against $c$ over the whole grid $c = 1, \dots, 9999$ produces a curve
with a single sharp minimum; the minimizer was $\hat c = 5045$, close to the true $5000$. Refitting
the regression at $\hat c = 5045$ gave

$$
\hat\beta_0 = -0.0193, \quad \hat\beta_1 = 0.4219
$$

against true values $\beta_0 = 0$, $\beta_1 = \mu_2 - \mu_1 = 0.4$, and

$$
\hat\sigma_{\mathrm{MLE}} = 1.0060, \quad \hat\sigma_{\mathrm{unbiased}} = 1.0061
$$

against the true $\sigma = 1$. Overlaying the fitted step function on the raw series shows the fit
tracking the two levels with the jump located essentially where the data actually jump.

## Bayesian inference for the change-point

The change-point can also be treated as a discrete parameter with a posterior distribution over
its $n-1$ possible values. The (unnormalized) posterior given in the material is

$$
\pi(c \mid y) \;\propto\; |X_c^\top X_c|^{-1/2} \left(\frac{1}{\mathrm{RSS}(c)}\right)^{(n-p)/2},
$$

where $p = 2$ is the number of regression coefficients and $|X_c^\top X_c|$ is the determinant of
$X_c^\top X_c$. As with other likelihood-type quantities computed over a long grid, it is
numerically safer to work with the **log**-posterior,

$$
\log \pi(c \mid y) = \frac{p-n}{2}\log \mathrm{RSS}(c) - \tfrac{1}{2}\log|X_c^\top X_c| + \text{const},
$$

evaluate it over the grid of candidate $c$ values, and only exponentiate at the end (after
subtracting the maximum, to avoid overflow) to recover values proportional to the posterior. Since
$c$ ranges over a finite set, normalizing is just dividing by the sum over the grid, which turns
the exponentiated log-posterior values into an honest discrete probability distribution over
change-points. In the single change-point example above, this posterior distribution is
concentrated tightly around $c = 5000$, and the log-posterior curve has essentially the same shape
as the $\mathrm{RSS}(c)$ curve (both are driven by the same term).

### Sampling from the posterior

Because the posterior over $c$ is an explicit discrete distribution on a grid, drawing samples of
$c$ from it is a direct categorical draw with those probabilities as weights. To get a full
posterior sample of $(c, \beta_0, \beta_1, \sigma)$, each draw of $c$ is completed by drawing the
other parameters from their conditional posterior given that $c$:

- $\sigma^2$ is drawn from a scaled distribution built from a $\chi^2_{n-p}$ draw: $\sigma =
  \sqrt{\mathrm{RSS}(c)/\chi^2_{n-p}}$;
- $\beta = (\beta_0,\beta_1)$ is then drawn from a multivariate normal centered at the OLS estimate
  $\hat\beta_c$, with covariance $\sigma^2 (X_c^\top X_c)^{-1}$.

Repeating this 2000 times gives 2000 draws from the joint posterior. Plotting the fitted step
function for every sampled $(c, \beta_0, \beta_1)$ on top of the raw series shows a bundle of
red curves all sitting close to the true step, visualizing the uncertainty in the fit; plotting
just the sampled change-points as vertical lines against the true change-point (at $t=5000$, in
black) shows the sampled $c$ values clustering tightly around the truth, consistent with how
sharply peaked the posterior was.

## Multiple change-points

The model generalizes to several change-points $c_1 < c_2 < c_3$:

$$
y_t = \beta_0 + \beta_1 I\{t > c_1\} + \beta_2 I\{t > c_2\} + \beta_3 I\{t > c_3\} + \epsilon_t.
$$

### Worked example: joint grid search

A series of length $n = 400$ was simulated in four segments of 100 points each, with levels
$\mu_1 = 0$, $\mu_2 = 1.5$, $\mu_3 = -1$, $\mu_4 = 0$ and $\sigma = 1$, so the true change-points
are $c_1 = 100$, $c_2 = 200$, $c_3 = 300$. The most direct estimator jointly minimizes
$\mathrm{RSS}(c_1, c_2, c_3)$ over a three-dimensional grid — here, $c_1 \in \{75,\dots,125\}$,
$c_2 \in \{175,\dots,225\}$, $c_3 \in \{275,\dots,325\}$, a grid of $51^3 = 132{,}651$
combinations, each requiring its own OLS fit (about 12 seconds to run). The minimizing combination
was

$$
(\hat c_1, \hat c_2, \hat c_3) = (104, 200, 306), \qquad \mathrm{RSS} = 399.9,
$$

close to the true $(100, 200, 300)$ — a decent recovery, but at real computational cost, since a
joint grid over $p$ change-points scales like $n^p$.

### A faster iterative algorithm

Instead of searching jointly, change-points can be found **one at a time**, each time fixing the
change-points already found and searching only over the new one:

1. Find $\hat c_1$ by single change-point RSS minimization, ignoring the other change-points
   entirely:
   $$
   \hat c_1 = \arg\min_{c_1} \ \min_{\beta_0,\beta_1} \sum_{t=1}^n \big(y_t - \beta_0 - \beta_1 I\{t>c_1\}\big)^2.
   $$
2. Fix the indicator $I\{t > \hat c_1\}$ in the regression and find $\hat c_2$ by minimizing the
   two-change-point RSS over the new change-point only:
   $$
   \hat c_2 = \arg\min_{c_2} \ \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \big(y_t - \beta_0 - \beta_1 I\{t>\hat c_1\} - \beta_2 I\{t>c_2\}\big)^2.
   $$
3. Fix both $I\{t>\hat c_1\}$ and $I\{t>\hat c_2\}$ and find $\hat c_3$ the same way.

Each step is an $O(n)$ grid search rather than an $O(n^p)$ joint one, so the total cost is
$O(pn)$ — a large saving over the joint grid. Run on the same simulated data, the steps produced,
in order, $200$, then $104$, then $306$. Notice that the *order in which the algorithm finds them*
is not the temporal order of the true change-points: it finds $c=200$ first because that is where
the largest single jump in level occurs ($\mu_1=0$ to $\mu_2=1.5$), then finds $104$ once that
jump is accounted for, then $306$. But the final *set* of estimated change-points, $\{104, 200,
306\}$, is exactly the same set the much slower joint grid search found — the iterative scheme
recovers the same answer far faster.

## Sources

- Notebook: `docs/statistics/berkeley/stat153/fall-2025/CodeLabFour153248Fall2025.md` (Berkeley
  STAT 153, Fall 2025, "Code Lab Four"), CC BY 4.0, converted from
  `CodeLabFour153248Fall2025.ipynb`. All definitions, formulas, code outputs, and numerical results
  in this chapter (the single change-point simulation with $n=10{,}000$, the Bayesian posterior
  formula and sampling scheme, and the three-change-point simulation with $n=400$) come from this
  notebook; no accompanying slides, transcript, or exercise set was supplied for this lecture. The
  notebook does not derive the Bayesian posterior formula for $c$ — it is presented there directly
  — so it is likewise presented here without derivation. Figures referenced in the text (the raw
  series, the RSS/log-posterior/posterior curves, and the posterior-sample overlays) are described
  from the notebook's own commentary and code; the images themselves were omitted in the source
  conversion.

---

[← 28. High-Dimensional Regression for Change-Points](28-high-dimensional-regression-for-change-points.md) · [Contents](index.md) · [30. AR(p): Levels, Logs, and Differences →](30-ar-p-levels-logs-and-differences.md)
