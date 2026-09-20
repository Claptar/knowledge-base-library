---
title: "41. Regression Uncertainty and Profile Estimation"
course: "Berkeley Stat 153 Fall 2024"
chapter: 41
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 41. Regression Uncertainty and Profile Estimation

## What this covers

Berkeley Stat 153 runs a "code lecture" alongside the theory lectures: a notebook that fits the
models on real or simulated data and checks the formulas numerically. This chapter follows the
fifth one, taught with different data in three offerings (fall 2025, fall 2026, spring 2025), and
answers two questions that recur throughout: once ordinary least squares has produced $\hat\beta$,
how much uncertainty is actually attached to it — as a classical standard error and confidence
interval, and as a Bayesian posterior — and what changes when a parameter of interest does not
enter the regression linearly, so that the usual closed-form estimator no longer applies? It
assumes multiple linear regression in matrix form: a design matrix $X$, the estimator
$\hat\beta = (X^TX)^{-1}X^Ty$, and residual sum of squares.

## A warm-up: why a minimum can be sharply determined

Before turning to real data, the fall-2026 notebook opens with a small synthetic example that is
worth keeping in mind for everything that follows. Take five numbers, $y = (1, 0, 2, -2, 5)$, and
the squares function

$$S(\theta) := \sum_{i=1}^n (y_i-\theta)^2.$$

This is minimized at $\hat\theta = \bar y = 1.2$, the sample mean — the single-parameter case of
least squares. Because $\hat\theta$ minimizes $S$, the ratio $S(\hat\theta)/S(\theta)$ is at most
$1$ for every $\theta$, with equality only at $\theta=\hat\theta$. Raising that ratio to a power
$m\ge 1$ leaves the value at $\hat\theta$ fixed at $1$ while shrinking every other value further
toward $0$, so $\big(S(\hat\theta)/S(\theta)\big)^m$ becomes an increasingly narrow spike centered
at $\hat\theta$ as $m$ grows. The point of the exercise is qualitative: a criterion that has a
unique minimum can pin that minimum down arbitrarily sharply once it is weighted or compounded
enough. The same manoeuvre — write down a criterion in the unknown parameter, and see how sharply
it is determined — is exactly the tool used later in this chapter to locate a breakpoint and a
frequency for which no closed-form minimizer exists.

## Reading a fitted trend: interpreting a log-linear slope

The fall-2025 notebook returns to the CPI (Consumer Price Index) data from FRED already fit in an
earlier lecture: $y_i = \log(\text{CPI}_i) = \beta_0+\beta_1 x_i+\epsilon_i$ with $x_i=i$ indexing
943 months from January 1947 to July 2025. Fitting gives $\hat\beta_1 = 0.0031618$. Because $y$ is
a logarithm, $100\hat\beta_1$ is the percentage change in CPI from one month to the next, and
$12\times100\times\hat\beta_1 \approx 3.79\%$ is the corresponding annualized rate — read off here
as an estimate of the historical inflation rate over the full sample.

The same idea, and the same caution, appears with a second dataset: the annual resident population
of California from 1900 to 2024 (FRED, in thousands of persons), fit on the log scale as
$y_t=\beta_0+\beta_1 t+\epsilon_t$. The fitted slope is $\hat\beta_1=0.0269$, i.e. $2.69\%$ growth
per year — but the data visibly do not grow at a constant rate: growth looks faster than $2.69\%$
early in the century and slower than that in recent decades. A single straight line, fit on log
scale or not, cannot express a change in growth rate. That failure is what motivates the nonlinear
model taken up further down.

## Quantifying uncertainty in ordinary least squares

For a general design matrix $X\in\mathbb R^{n\times p}$ (whose columns can include indicators,
polynomial terms, or anything else — the argument does not care), and errors assumed i.i.d.
$N(0,\sigma^2)$, the same computation used in the previous lecture gives the standard error and
confidence interval directly from $X$ and the residuals:

$$\hat\beta=(X^TX)^{-1}X^Ty, \qquad \hat\sigma^2=\frac{1}{n-p}\sum_{i=1}^n\hat\epsilon_i^2,
\qquad \widehat{\operatorname{Var}}(\hat\beta)=\hat\sigma^2(X^TX)^{-1},$$

$$\operatorname{se}(\hat\beta_j)=\sqrt{\big[\widehat{\operatorname{Var}}(\hat\beta)\big]_{jj}},
\qquad \hat\beta_j \pm t_{n-p,\,1-\alpha/2}\,\operatorname{se}(\hat\beta_j)$$

for a $100(1-\alpha)\%$ confidence interval, with $t_{n-p,1-\alpha/2}$ the corresponding quantile
of the $t$-distribution on $n-p$ degrees of freedom.

The notebook checks this formula against a regression package rather than deriving it again. Fit
the simple regression $y_t=\beta_0+\beta_1 t+\epsilon_t$ to the monthly US population series
(FRED, in thousands, January 1959 to July 2026, $n=811$). The regression output reports
$\hat\beta_0=174{,}585.5$, $\hat\beta_1=213.216$, standard errors $189.05$ and $0.403$, and a 95%
interval for the slope of $[212.424,\,214.008]$. Computing $\hat\beta$, $\hat\sigma^2$,
$\operatorname{se}(\hat\beta)$ and the confidence interval directly from the three formulas above
reproduces every one of these numbers to the same decimal places — the regression output is not
doing anything beyond what the formulas say.

## A Bayesian posterior for the same coefficients

Standard errors and confidence intervals answer a frequentist question: how would $\hat\beta$
vary if the experiment (here, the same $n$ time points) were repeated. A previous lecture derived
the Bayesian alternative — the posterior distribution of the coefficients given the data, under a
standard reference prior — and it turns out to have the same two ingredients as the classical
answer, packaged as a multivariate $t$-distribution rather than a normal:

$$\beta_0,\dots,\beta_m \mid \text{data} \;\sim\; t_{m+1}\!\left(\hat\beta,\;
\frac{S(\hat\beta)}{n-m-1}(X^TX)^{-1},\; n-m-1\right),$$

where $m$ is the number of predictors besides the intercept (so $\beta$ has $m+1$ entries),
$S(\hat\beta)=\sum_i\hat\epsilon_i^2$ is the residual sum of squares, and the degrees of freedom
$n-m-1$ is exactly the same $n-p$ that appears in the classical formula. The scale matrix
$\frac{S(\hat\beta)}{n-m-1}(X^TX)^{-1}$ is, term for term, the same matrix
$\widehat{\operatorname{Var}}(\hat\beta)$ computed above for the standard errors — the two
questions, "how spread out is the sampling distribution of $\hat\beta$" and "how much posterior
mass sits away from $\hat\beta$," are answered by the identical covariance matrix, and only differ
in that the posterior is a $t$-distribution because $\sigma$ itself is unknown and has been
integrated out rather than plugged in.

This is easy to turn into a picture. For the US population regression above, draw $N=1000$ samples
$\beta^{(1)},\dots,\beta^{(N)}$ from that multivariate $t$-distribution, and for each one plot the
line $X\beta^{(r)}$ against time. Because the regression fits this series almost exactly
($R^2=0.997$), the thousand sampled lines form a narrow band that is barely distinguishable from
the single fitted line by eye; the visualization is a direct, sampling-based alternative to reading
off a numerical confidence interval for each coefficient separately.

## What that picture misses: a misspecified mean function

Both the classical interval and the Bayesian posterior above are conditional on the mean function
being right — they say how uncertain $\hat\beta$ is *given* that $y_t=\beta_0+\beta_1 t+\epsilon_t$
is the correct model, not whether it is. A simulated example makes the distinction concrete.
Generate $n=400$ points from a genuinely quadratic mean, $y = 5+0.8\,(x-n/2)^2+\epsilon$ with
$\epsilon\sim N(0,1000^2)$, and fit a straight line to it anyway. The fitted line runs through the
middle of the data but tracks neither the early nor the late curvature; sampling from its posterior
and overlaying the thousand resulting straight lines produces a band of *plausible straight lines*,
none of which is anywhere close to the true quadratic shape. The interval is not wrong about what
it claims — it correctly describes the uncertainty in the best-fitting line — but what it claims is
the wrong question, because the assumed mean function is wrong.

Refitting with the quadratic term present, $y=\beta_0+\beta_1 x+\beta_2 x^2+\epsilon$, recovers
$\hat\beta_2=0.7997$ against the true value $0.8$ used to generate the data — a striking recovery
given that the noise standard deviation, $1000$, is not small relative to the fitted curve — because
$n=400$ points is enough evidence to pin the quadratic coefficient down tightly once the functional
form is right. Posterior samples from the quadratic fit now trace the true parabola closely. The
moral the notebook draws is procedural as much as statistical: a plot of the fit against the data,
before trusting any interval, is what catches this kind of error.

## Profiling out a nonlinear parameter: an unknown breakpoint

Return to the California population series and its non-constant growth rate. A natural fix is to
let the growth rate change at some time $c$:

$$y_t = \beta_0+\beta_1 t+\beta_2\,(t-c)_+ + \epsilon_t, \qquad (t-c)_+ := \max(t-c,\,0).$$

Before $c$ the fitted slope is $\beta_1$; from $c$ onward, since the second term now contributes
$\beta_2$ per unit time as well, the slope is $\beta_1+\beta_2$. If $c$ were known this is ordinary
multiple regression on the three columns $1,\,t,\,(t-c)_+$. What makes it a genuinely *nonlinear*
regression is that $c$ is not known and the design matrix itself depends on it — there is no
closed-form estimator for $c$ the way there is for $\beta_0,\beta_1,\beta_2$.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A trend with a steep slope before an unknown breakpoint c and a shallower slope after it">
  <line x1="30" y1="185" x2="320" y2="185" stroke="currentColor" stroke-width="1.2"/>
  <text x="325" y="189" font-size="12" fill="currentColor">t</text>
  <line x1="30" y1="185" x2="30" y2="20" stroke="currentColor" stroke-width="1.2"/>
  <text x="12" y="25" font-size="11" fill="currentColor">y</text>
  <line x1="170" y1="15" x2="170" y2="185" stroke="currentColor" stroke-width="1" stroke-dasharray="4,4" opacity="0.6"/>
  <text x="176" y="15" font-size="12" fill="currentColor">c (unknown)</text>
  <polyline points="30,165 170,60" fill="none" stroke="currentColor" stroke-width="2"/>
  <polyline points="170,60 320,28" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="55" y="100" font-size="12" fill="currentColor">slope β₁</text>
  <text x="200" y="50" font-size="12" fill="currentColor">slope β₁+β₂</text>
  <circle cx="170" cy="60" r="3" fill="currentColor"/>
</svg>
<figcaption>The broken-stick model: a straight line of slope $\beta_1$ up to an unknown time $c$,
continuing from that same point with slope $\beta_1+\beta_2$.</figcaption>
</figure>

The estimation strategy exploits that, for any *fixed* candidate value of $c$, the rest of the
model is linear: define the profile residual sum of squares

$$\operatorname{RSS}(c) := \min_{\beta_0,\beta_1,\beta_2}\sum_{t=1}^n\big(y_t-\beta_0-\beta_1
t-\beta_2(t-c)_+\big)^2,$$

computed, for each candidate integer $c$, by simply running ordinary least squares on the design
matrix built from that $c$ and reading off the residual sum of squares. Since $c$ can only usefully
range over the $n=125$ observed time points, $\hat c$ is taken to be whichever integer minimizes
$\operatorname{RSS}(c)$ over the full grid $c\in\{1,\dots,n\}$ — no calculus is available here, so
the search is exhaustive rather than gradient-based. This gives $\hat c=66$, corresponding to the
year 1965. Plugging $\hat c$ back in and re-running the regression gives
$\hat\beta_1=0.038,\ \hat\beta_2=-0.024$: a growth rate of $3.8\%$ per year before 1965 and
$3.8-2.4=1.4\%$ per year after — against the single, misspecified rate of $2.69\%$ that a plain
linear fit reports for the whole span. Plotted together, the broken-stick fit tracks both the
earlier steep rise and the later slower growth, while the single-line fit runs between the two and
matches neither part particularly well. The residual variance can be estimated as usual once $c$ is
fixed, dividing by $n-3$ (three fitted coefficients) rather than $n$ for the unbiased version.

## Profiling out a nonlinear parameter: an unknown frequency

The spring-2025 offering runs the identical recipe on a different kind of nonlinearity: an unknown
*frequency*, using the annual mean sunspot number (SILSO/SIDC) from 1700 onward. The model is the
sinusoidal regression

$$y_t = \beta_0+\beta_1\cos(2\pi f t)+\beta_2\sin(2\pi f t)+\epsilon_t,$$

which, for a fixed frequency $f$, is again ordinary linear regression on the columns
$1,\,\cos(2\pi ft),\,\sin(2\pi ft)$ — trying a handful of specific values (periods of 10, 11, 4, 15
years) shows visibly different fits, with none of them yet chosen by any principled rule. Define

$$\operatorname{crit}(f) := \min_{\beta_0,\beta_1,\beta_2}\sum_{t=1}^n\big(y_t-\beta_0-\beta_1
\cos(2\pi ft)-\beta_2\sin(2\pi ft)\big)^2,$$

the residual sum of squares from the OLS fit at that $f$; under i.i.d. Gaussian errors, minimizing
$\operatorname{crit}(f)$ over $f$ is the maximum-likelihood estimate of the frequency. A grid search
over $f\in[0,0.5]$ in steps of $10^{-5}$ gives $\hat f_{\text{MLE}}=0.09089$, a period of
$1/\hat f\approx11.0023$ years — close enough to the independently known roughly eleven-year solar
cycle to serve as a check that the procedure found the right minimum. The plot of
$\operatorname{crit}(f)$ over the full grid has one clear global minimum but is otherwise rough,
with a number of smaller local minima; that non-smoothness is exactly why the frequency is located
by scanning a grid of candidates and taking the minimum by brute force, rather than by any
derivative-based search that could get trapped in one of the smaller dips. The lecture notes that
$\operatorname{crit}(f)$ is closely related to the **periodogram**, a standard tool for time series
analysis of periodic data, without developing that connection in this lecture.

## A Bayesian posterior for the frequency

A previous lecture also derived, and this notebook evaluates rather than re-derives, a formula for
the (unnormalized) log-posterior density of $f$ given the data:

$$\log p(f\mid\text{data}) \;=\; \frac{p-n}{2}\log\operatorname{RSS}(f) \;-\;
\tfrac12\log\big|\det(X_f^TX_f)\big| \;+\; \text{const},$$

where $p=3$ is the number of linear coefficients and $X_f$ is the design matrix built from $f$.
Evaluating this over a grid excludes the exact endpoints $f=0$ and $f=0.5$, since
$\det(X_f^TX_f)\to0$ there and the log-determinant term diverges. Because the formula is more
stable computed on the log scale, the values are exponentiated only after subtracting the maximum
log value, and the resulting numbers are then normalized to sum to one over the grid — giving a
discrete approximation to the posterior density of $f$.

The maximizer of this posterior coincides exactly with the maximum-likelihood estimate,
$\hat f=0.09089$. A 95% credible interval is built by expanding a window of $m$ grid points on
either side of that maximizer and accumulating the posterior mass inside it until the total first
reaches $0.95$: with a grid resolution of $10^{-5}$, $m=28$ points either side already gives
$0.9522$, so the credible interval for the frequency is $[0.09061,\,0.09117]$, which inverts to a
credible interval for the period of $[10.969,\,11.036]$ years — tightly consistent with the known
eleven-year cycle, and visibly narrower than the crude "try a few periods" exploration that opened
the section.

## Sources

- Fall-2025 offering, [`CodeLectureFive153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb) (CC BY 4.0): the log-CPI regression and its percent-change interpretation; the manual check of $\hat\beta$, standard errors and confidence intervals against the regression package (CPI data); the California population example, its log-linear misfit, and the full broken-stick / unknown-breakpoint derivation, including the numerical values of $\hat c$, $\hat\beta$ and the two growth rates.
- Fall-2026 offering, same notebook split across three converted files (CC BY 4.0):
  [`01-introduction.md`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb) — the squares-function warm-up and the $\big(S(\hat\theta)/S(\theta)\big)^m$ concentration example;
  [`02-dataset-one-us-population.md`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb) — the US population regression, the manual SE/CI check, and the multivariate-$t$ posterior with sampled-line visualization;
  [`04-dataset-three-a-simulated-dataset.md`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/CodeLectureFive153248Fall2026.ipynb) — the simulated quadratic dataset, the linear-vs-quadratic misspecification comparison, and a second, independent worked check of the SE/CI formulas (US population data), not repeated here since it duplicates the fall-2025 check.
- Spring-2025 offering, [`CodeLectureFive153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFive153248Spring2025.ipynb) (CC BY 4.0): the sunspots dataset, the sinusoidal model, the frequency-profiling recipe and its MLE, and the Bayesian posterior over $f$ with its 95% credible interval.
- Referred to but not contained in any of the supplied notebooks: the periodogram itself (named as the next class's topic); the earlier-lecture derivation of the multivariate-$t$ posterior for regression coefficients and of the log-posterior density formula for $f$, both of which are evaluated numerically here rather than re-derived; the underlying CSV data files (CPI, California and US population, sunspot counts); and the Wikipedia figure for the sunspot cycle length used in the notebook only as an offhand sanity check.
- No slides, transcript, written notes or problem set were supplied for this lecture; the chapter is built entirely from the three notebook conversions listed above, treated as three independent worked treatments of one recurring "code lecture."

---

[← 40. Applying the Spectrum Smoother](40-applying-the-spectrum-smoother.md) · [Contents](index.md) · [42. Time Series Regression and Uncertainty →](42-time-series-regression-and-uncertainty.md)
