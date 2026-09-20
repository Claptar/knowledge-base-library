---
title: "38. AR(p) Forecasting and Prediction Uncertainty"
course: "Berkeley Stat 153 Fall 2024"
chapter: 38
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 38. AR(p) Forecasting and Prediction Uncertainty

## What this covers

This chapter turns a fitted AR($p$) model into the three things a forecaster actually wants from
it: point forecasts beyond the end of the data, standard errors and intervals around those
forecasts, and — the part usually left as a black box — a worked account of *where* those standard
errors come from. Two datasets carry the argument. Quarterly U.S. Personal Consumption Expenditures
(PCE) from FRED are fit with AR(1), split into training and test data, and forecast twice — once on
the raw series and once on its logarithm — to see what the log transform buys. The annual
sunspot-count series is fit with AR(2), and its complex characteristic roots show up directly in the
shape of its forecasts. The chapter assumes the AR($p$) equation and its causal-stationarity
condition (every root of the characteristic polynomial has modulus greater than $1$), and that
AR($p$) can be fit either by hand-built OLS or by `statsmodels`' `AutoReg`, from earlier lectures.
What is new here is what happens *after* fitting: forecasting, and quantifying the uncertainty in
that forecast.

## Two routes to $\hat\sigma$, and why $z$-scores and $t$-scores disagree

Recall that fitting $y_t = \phi_0 + \phi_1 y_{t-1} + \cdots + \phi_p y_{t-p} + \epsilon_t$ by hand
means stacking lagged values into a design matrix $X$ and regressing the response
$y_{p+1},\dots,y_n$ on it by OLS, and that `AutoReg` fits the same model by conditional maximum
likelihood. The two routes return exactly the same coefficient estimates $\hat\phi_0,\dots,\hat\phi_p$
— OLS *is* the conditional MLE, since the conditional likelihood is Gaussian in the residuals. What
differs is the estimate of the innovation variance $\sigma^2$ feeding into the standard errors,
because the two routines use different denominators for the same sum of squared residuals:

$$
\hat\sigma_{\text{ols}}^2 = \frac{\|Y-X\hat\beta\|^2}{n-2p-1}, \qquad
\hat\sigma_{\text{mle}}^2 = \frac{\|Y-X\hat\beta\|^2}{n-p},
$$

where $n$ is the number of observations fit and the response vector has length $n-p$ once the first
$p$ values are used up as lags. The OLS denominator is the usual regression degrees of freedom:
$n-p$ effective observations minus $p+1$ estimated parameters (the intercept and $p$ slopes) leaves
$n-2p-1$. The MLE denominator makes no such correction — it just divides by the number of
observations used, which is why it is a biased (though asymptotically negligible) estimate of
$\sigma^2$. Standard errors are $\sqrt{\operatorname{diag}\big(\hat\sigma^2(X^\top X)^{-1}\big)}$
with whichever $\hat\sigma^2$, which is why the OLS summary reports $t$-scores and `AutoReg` reports
$z$-scores.

The sunspot AR(2) fit ($n=325$, $p=2$) prints both estimates directly and shows the pattern cleanly:
$\hat\sigma_{\text{mle}}=25.588$ against $\hat\sigma_{\text{ols}}=25.708$, and standard errors
$(2.3725, 0.04002, 0.03997)$ against $(2.3835, 0.04020, 0.04016)$ for $\hat\phi_0,\hat\phi_1,
\hat\phi_2$ respectively — each `AutoReg` value matching `armod_sm.bse`, each OLS value matching
`armod.bse`, exactly. The two $\hat\sigma$'s must always be in the exact ratio
$\hat\sigma_{\text{ols}}/\hat\sigma_{\text{mle}} = \sqrt{(n-p)/(n-2p-1)}$, and the same identity
carries over to the standard errors (both come from the same $(X^\top X)^{-1}$, scaled by
$\hat\sigma$). The raw-level PCE AR(1) fit ($n=295$, $p=1$) confirms it independently: `AutoReg`
reports $\hat\sigma_{\text{mle}}=115.583$ ("S.D. of innovations"), and while the OLS $\hat\sigma$ is
not printed there, the ratio is: $9.377/9.345 = 1.00342$ for the intercept's standard error, and
$\sqrt{294/292}=1.00342$ from the formula — matching to five figures.

## Point forecasts are a recursion, not a formula

Once $\hat\phi_0,\dots,\hat\phi_p$ are fixed, a forecast $k$ steps past the end of the training data
is built one step at a time:

$$
\hat y_{n+i} = \hat\phi_0 + \sum_{j=1}^{p} \hat\phi_j\, \tilde y_{n+i-j}, \qquad
\tilde y_m = \begin{cases} y_m & m \le n \ \text{(actual data)} \\ \hat y_m & m > n \ \text{(a
previous forecast)} \end{cases}.
$$

Plug in real data where it exists, and your own earlier forecasts once it runs out. Coding this loop
by hand and comparing it against `AutoReg`'s `.predict()` / `.get_prediction()` reproduces the exact
same numbers in both datasets — the built-in method is doing nothing more than this recursion.

On the raw-level PCE series (AR(1), $\hat\phi_0=16.733$, $\hat\phi_1=1.0077$), the forecast climbs
smoothly from $14{,}606.9$ at one quarter ahead to $17{,}080.5$ at nineteen quarters ahead, and the
lecture's own verdict is that "the predicted values are somewhat below the actual test values." The
`AutoReg` summary reports the root of the AR(1) characteristic polynomial as $0.9924$ — *inside* the
unit circle, since $\hat\phi_1>1$ — which fails the causal-stationarity condition (root modulus
$>1$) from the causal AR(2) chapter. That is exactly what you'd expect of a steadily trending series
like consumption spending: fit in levels, it looks mildly explosive, not stationary.

On the sunspot series (AR(2), $\hat\phi_1=1.388$, $\hat\phi_2=-0.6965$), the picture is different in
kind. The characteristic roots are a complex-conjugate pair, $0.9965 \mp 0.6655i$, of modulus
$1.1983$ (comfortably stationary) and frequency $\pm0.0937$ — a cycle roughly every $1/0.0937\approx
10.7$ steps. That periodicity is visible directly in the forecast table: starting at $151.8$, the
point forecasts fall to a trough of $50.1$ around six steps out, climb back to a local peak of $90.6$
around eleven steps out, and then the oscillation damps quickly, settling to $79.29$ — the process's
estimated long-run mean, approached in a spiral rather than a straight line, exactly as complex roots
of a linear recursion predict.

## Working on the log scale

"Instead of applying AR models directly to the raw data, it is common practice to apply them to the
logarithms." The reasoning fits what the roots above already suggest: a series like PCE grows
roughly multiplicatively (a fairly constant *percentage* increase per quarter), and a linear AR
recursion is a poor match for multiplicative growth but a good match for the roughly additive growth
of its logarithm. Refitting AR(1) to $\log(\text{PCE})$ gives $\hat\phi_1 = 0.9984$, whose
characteristic root has modulus $1.0016$ — just barely on the stationary side of $1$, consistent
with a series that behaves almost like a random walk with a small positive drift once you're working
in logs. Repeating the forecast-versus-test-data comparison on this scale (exponentiating the
forecasts back to the original units before plotting), the lecture's verdict flips: "now the
predictions are slightly closer to the actual observations."

## From a point forecast to an interval

A point forecast alone hides how much confidence to place in it. The standard construction is the
usual normal-approximation interval,

$$
\hat y_{n+i} \pm z_{\alpha/2}\, \operatorname{se}(\hat y_{n+i}), \qquad
z_{\alpha/2} = \Phi^{-1}\!\left(1-\tfrac{\alpha}{2}\right),
$$

with $\alpha=0.05$ giving $z_{0.025}\approx1.96$. Built by hand from `fcast.se_mean`, this matches
`fcast.conf_int()` column for column — again, the built-in interval is exactly this formula, not
something more elaborate. Applied to the raw-level PCE forecast, the interval starts narrow (about
$\pm227$ around $14{,}606.9$ at one quarter out) and widens steadily as the horizon grows, reaching
roughly $\pm1060$ around $17{,}080.5$ at nineteen quarters out:

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="PCE point forecast with a widening 95 percent prediction interval over a 19-quarter horizon">
  <polygon points="40.0,169.5 54.4,159.4 68.9,150.2 83.3,141.4 97.8,133.0 112.2,124.6 126.7,116.4 141.1,108.3 155.6,100.2 170.0,92.2 184.4,84.2 198.9,76.2 213.3,68.2 227.8,60.2 242.2,52.2 256.7,44.2 271.1,36.2 285.6,28.1 300.0,20.0 300.0,115.8 285.6,121.0 271.1,126.1 256.7,131.1 242.2,136.0 227.8,140.8 213.3,145.6 198.9,150.3 184.4,154.8 170.0,159.3 155.6,163.6 141.1,167.8 126.7,171.9 112.2,175.8 97.8,179.5 83.3,182.9 68.9,186.0 54.4,188.5 40.0,190.0" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <polyline points="40.0,179.8 54.4,173.9 68.9,168.1 83.3,162.2 97.8,156.2 112.2,150.2 126.7,144.2 141.1,138.1 155.6,131.9 170.0,125.8 184.4,119.5 198.9,113.2 213.3,106.9 227.8,100.5 242.2,94.1 256.7,87.6 271.1,81.1 285.6,74.5 300.0,67.9" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="200" x2="300" y2="200" stroke="currentColor" stroke-width="1"/>
  <text x="40" y="212" font-size="11" fill="currentColor">1 quarter ahead</text>
  <text x="230" y="212" font-size="11" fill="currentColor">19 quarters ahead</text>
  <text x="10" y="24" font-size="11" fill="currentColor">$18{,}140bn</text>
  <text x="10" y="196" font-size="11" fill="currentColor">$14{,}380bn</text>
</svg>
<figcaption>The AR(1) point forecast for PCE (solid line) and its 95% prediction interval (shaded
band), plotted against forecast horizon. The band widens because the prediction standard error grows
with horizon, as the next section derives.</figcaption>
</figure>

## How the standard errors are actually built

The interval needs $\operatorname{se}(\hat y_{n+i})$, and the lecture computes it directly rather
than quoting it, by tracking the forecast *error* $e_i = y_{n+i}-\hat y_{n+i}$ rather than the
forecast itself. Treating the fitted $\hat\phi_j$ as fixed — this is the key simplification: the
recursion propagates only the uncertainty from *future, not-yet-observed* shocks, not the uncertainty
in $\hat\phi_j$ itself — the true and forecast values agree everywhere they both use actual past
data, so those terms cancel and

$$
e_i = \sum_{j=1}^{\min(p,\,i-1)} \hat\phi_j\, e_{i-j} + \epsilon_{n+i}, \qquad e_m = 0 \text{ for }
m\le 0.
$$

The first error is pure noise, $e_1=\epsilon_{n+1}$, so $\operatorname{Var}(e_1)=\sigma^2$ — exactly
the $1\times1$ starting matrix `Gamhat = [[sigest**2]]` in the code. Each new error is a *fixed*
linear combination of all previous errors plus one new independent shock, so writing
$\boldsymbol\Gamma_i=\operatorname{Cov}(e_1,\dots,e_i)$ and $v_i$ for the vector of coefficients on
$(e_1,\dots,e_i)$ in the recursion above (zeros for lags older than $p$, then $\hat\phi_p,\dots,
\hat\phi_1$ for the most recent $p$),

$$
\operatorname{Cov}(e_{1:i},\,e_{i+1}) = \boldsymbol\Gamma_i\, v_i, \qquad
\operatorname{Var}(e_{i+1}) = \sigma^2 + v_i^\top \boldsymbol\Gamma_i v_i,
$$

which is exactly `covterm` and `varterm` in the code, and the covariance matrix grows by one row and
column at a time,

$$
\boldsymbol\Gamma_{i+1} = \begin{pmatrix} \boldsymbol\Gamma_i & \boldsymbol\Gamma_i v_i \\
v_i^\top \boldsymbol\Gamma_i & \sigma^2 + v_i^\top \boldsymbol\Gamma_i v_i \end{pmatrix},
$$

matching the `np.block` assembly line for line. The prediction standard errors are then
$\sqrt{\operatorname{diag}(\boldsymbol\Gamma_k)}$, and the notebook checks this by comparing the
hand-built recursion against `fcast.se_mean` for every forecast step and finds them identical —
confirming that `AutoReg`'s reported prediction error really is just this shock-propagation
calculation, with the coefficients plugged in as if they were known exactly rather than estimated.

The worked numeric example in the notebook is an AR(1) case: the recursion is run out to 100 steps,
starting from $\hat\sigma=0.023188$ and growing to $0.198$ with no sign yet of leveling off. Because
$v_i$ then holds only a single coefficient $\hat\phi_1$ against the most recent error,
$\operatorname{Var}(e_{i+1}) = \sigma^2+\hat\phi_1^2\operatorname{Var}(e_i)$ collapses to the familiar
geometric sum $\operatorname{Var}(e_i)=\sigma^2\sum_{j=0}^{i-1}\hat\phi_1^{2j}$, and solving that
recursion backwards out of the printed sequence gives $\hat\phi_1\approx0.9967$, consistently to five
significant figures across the first twenty steps — strong evidence that this really is a single-lag
recursion, and that $\hat\phi_1$ here sits, once again, just inside the stationary region: the
implied ceiling $\sigma/\sqrt{1-\hat\phi_1^2}\approx0.284$ is still a long way above the $0.198$
reached after 100 steps, exactly the slow, not-yet-settled growth you'd expect that close to a unit
root. This $\hat\phi_1\approx0.9967$ does *not* match the log-PCE fit from earlier in the notebook
($\hat\phi_1=0.9984$, $\hat\sigma=0.012$): the two `S.D. of innovations` values disagree by roughly a
factor of two, which is the tell that this recursion is being demonstrated on a different AR(1) fit
— see the note on this in Sources below. The method itself, and the algebra behind it, does not
depend on which fit it is run on; the general form (the `if i < p` branch in the code, appending
zeros once the horizon outruns the AR order) is written to handle any $p$, even though the concrete
example here happens to be $p=1$.

## Sources

- `01-dataset-one-personal-consumption-expenditures-from-fred.md` — PCE dataset: train/test split,
  the AR(1) fit both ways (raw levels), the $\hat\sigma$ formulas and their ratio check, the manual
  forecast recursion checked against `AutoReg`, the log-scale refit and its root, and the two
  quoted verdicts on forecast accuracy — `berkeley-stat153/fall-2025`,
  `CodeLectureEighteen153248Fall2025.ipynb`, CC BY 4.0.
- `03-how-are-the-prediction-uncertainties-actually-calculated.md` — the `Gamhat`/`vkp` recursion
  for the prediction standard errors, checked against `fcast.se_mean` — same notebook and licence.
  **This file continues from a "Dataset Two: House Price Data from FRED" section of the same
  notebook that was not included in the supplied material.** Its printed $\hat\sigma=0.023188$ does
  not match the log-PCE fit's `S.D. of innovations = 0.012` from Part 01, and the $\hat\phi_1$
  implied by its own printed numbers ($\approx0.9967$) does not match Part 01's log-PCE $\hat\phi_1
  = 0.9984$ either — so the specific AR(1) fit underlying this recursion's worked numbers is most
  likely the missing house-price example, not the PCE example carried through the rest of this
  chapter. The recursion itself, and the fact that it exactly reproduces `fcast.se_mean`, is
  independent of that gap.
- `01-fitting-ar-2-to-the-sunspots-dataset.md` — sunspot dataset: the AR(2) fit both ways, the
  explicit $\hat\sigma_{\text{mle}}$/$\hat\sigma_{\text{ols}}$ and standard-error comparison, and
  the point-forecast recursion checked against `AutoReg.predict`, including the complex
  characteristic roots and the damped oscillatory forecast — `berkeley-stat153/spring-2025`,
  `CodeLectureEighteen153248Spring2025.ipynb`, CC BY 4.0.
- The causal-stationarity criterion (root modulus $>1$) and the mechanics of fitting an AR($p$) by
  OLS or `AutoReg` are established in earlier chapters of this course; none of the three supplied
  files re-derives them, and neither does this one.

---

[← 37. The Periodogram and Sinusoidal Models](37-the-periodogram-and-sinusoidal-models.md) · [Contents](index.md) · [39. Ridge and LASSO Trend Estimation →](39-ridge-and-lasso-trend-estimation.md)
