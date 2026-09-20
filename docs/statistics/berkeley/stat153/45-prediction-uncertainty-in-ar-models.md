---
title: "45. Prediction Uncertainty in AR Models"
course: "Berkeley Stat 153 Fall 2024"
chapter: 45
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 45. Prediction Uncertainty in AR Models

## What this covers

This chapter covers how a fitted autoregressive model is turned into forecasts of future values,
and — the part usually left as a black box — where the standard errors behind a forecast's
uncertainty interval actually come from. It assumes the $AR(p)$ model itself from earlier in the
course: the recursion $y_t = \phi_0 + \phi_1 y_{t-1} + \cdots + \phi_p y_{t-p} + \epsilon_t$ with
$\epsilon_t$ independent, mean-zero, variance-$\sigma^2$ innovations, and its estimation by least
squares. Here the model is a tool for prediction rather than the object being introduced.

## Setting: forecasting consumption expenditure

The running example is U.S. personal consumption expenditure (PCE) — quarterly, seasonally
adjusted, in billions of dollars, from FRED — running from 1947 to the most recent quarter
available. The last 12 quarters (three years) are held out as a test set; an $AR(p)$ model is fit
to everything before that, and its forecasts for the held-out quarters are compared against what
actually happened. (The order $p$ is picked by eye here, $p=1$; heuristics for choosing it properly
are mentioned as material for the following lab, not this lecture.)

Fitting an AR(1) to the raw series gives
$$\hat y_t = 9.37 + 1.0106\, y_{t-1},$$
with the coefficient on $y_{t-1}$ estimated at $1.0106$, just above $1$ (statsmodels reports this as
a characteristic root of modulus $0.9895 \approx 1/1.0106$). A coefficient this close to one means
the fitted process behaves almost like a random walk with drift: forecasts keep climbing roughly in
line with the recent trend, with very little pull back toward any long-run mean. That matters below,
because it is exactly the kind of process for which forecast uncertainty compounds quickly with the
horizon.

## Point forecasts: running the recursion forward

Given $\hat\phi_0,\hat\phi_1,\ldots,\hat\phi_p$ fitted on training data $y_1,\ldots,y_n$, the natural
point forecast for $y_{n+h}$, $h = 1, 2, \ldots$, is obtained by plugging the estimates into the AR
equation and, whenever a lag falls beyond the end of the training data, substituting the forecast
already produced for it instead of an observation:
$$\hat y_{n+h} = \hat\phi_0 + \sum_{j=1}^p \hat\phi_j\, \tilde y_{n+h-j}, \qquad
\tilde y_{n+h-j} = \begin{cases} y_{n+h-j} & h-j \le 0 \ \text{(observed)} \\
\hat y_{n+h-j} & h-j > 0 \ \text{(previously forecast).}\end{cases}$$

For $h \le p$ this mixes real observations and forecasts; for $h > p$ it uses forecasts only. It is
exactly a forward pass through the fitted recursion, one step at a time, and it is what
`AutoReg.get_prediction` computes internally — the lecture's code reimplements it directly, step by
step, and checks the two columns agree to the displayed precision. For the raw-scale AR(1) above,
the first three quarter-ahead point forecasts come out as $17004.2,\ 17194.4,\ 17386.5$, each about
$190$ higher than the last, consistent with a coefficient just over $1$.

## A first look at uncertainty, and why the log scale matters

Around each point forecast, a $100(1-\alpha)\%$ prediction interval is built the usual way, from a
forecast standard error $\widehat{SE}(\hat y_{n+h})$ and a normal quantile:
$$\hat y_{n+h} \pm z_{\alpha/2}\, \widehat{SE}(\hat y_{n+h}), \qquad z_{\alpha/2} = \Phi^{-1}(1-\alpha/2).$$
With $\alpha = 0.05$ this reproduces `statsmodels`'s own `conf_int()` exactly, confirming the two are
the same construction. On the raw scale the intervals visibly widen with the horizon: the
one-quarter-ahead interval is about $[16760, 17248]$ (width $\approx 488$), while the
twelve-quarter-ahead interval is about $[18314, 20107]$ (width $\approx 1793$) — roughly three and a
half times as wide. And in this example the fit is not very good: the point forecasts run below the
actual test values throughout, with only the upper end of the interval coming close to the truth.

<figure>
<svg viewBox="0 0 360 200" role="img" aria-label="A time series forecast with a shaded prediction interval that widens as the horizon grows">
  <line x1="30" y1="175" x2="338" y2="175" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="340,175 330,171 330,179" fill="currentColor"/>
  <text x="335" y="192" text-anchor="end" font-size="11" fill="currentColor">time</text>

  <line x1="180" y1="15" x2="180" y2="175" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="183" y="12" font-size="11" fill="currentColor">forecast origin</text>

  <polygon points="180,94 210,76 240,62 270,49 300,38 330,28 330,76 300,79 270,82 240,86 210,90 180,94"
           fill="currentColor" fill-opacity="0.15" stroke="none"/>

  <polyline points="30,150 60,144 90,133 120,120 150,106 180,94" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="180,94 210,84 240,75 270,66 300,58 330,51" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 3"/>
  <polyline points="180,94 210,80 240,69 270,59 300,50 330,42" fill="none" stroke="currentColor" stroke-width="1.5"/>

  <text x="45" y="167" font-size="11" fill="currentColor">training data</text>
  <text x="296" y="34" font-size="11" fill="currentColor">interval</text>
  <text x="296" y="47" font-size="11" fill="currentColor">actual</text>
  <text x="296" y="66" font-size="11" fill="currentColor">forecast</text>
</svg>
<figcaption>Point forecast (dashed) and observed future values (solid) after the forecast origin,
with the shaded prediction interval widening with the horizon — the visual counterpart of the
growing diagonal entries of $\Gamma_h$ computed below.</figcaption>
</figure>

The usual fix is to fit the AR model to $\log y_t$ instead of $y_t$, then exponentiate the forecast
and its interval back to the original units. Here that gives $\hat\phi_1 = 0.9987$ on the log scale —
again just under $1$ — and after exponentiating, "the predictions are more accurate": the actual test
values sit more evenly inside the interval instead of hugging its upper edge. Fitting in logs amounts
to treating the series as growing by a roughly constant *percentage* each quarter rather than a
constant dollar amount, which is closer to how consumption spending actually behaves.

## How the prediction standard errors are actually computed

`get_prediction().se_mean` looks like it comes out of a library, but it is built from two pieces that
are both computable by hand: an estimate of the innovation variance $\sigma^2$, and a recursion that
propagates that variance forward through the AR structure. Rebuilding both from scratch, and checking
that the result reproduces `se_mean` exactly, is the point of this section.

### Refitting by OLS, and two estimates of $\sigma$

An $AR(p)$ model can be fit as an ordinary least-squares regression: with training data
$y_1,\ldots,y_n$ (here the logged series), build the response $Y = (y_{p+1},\ldots,y_n)^\top$ and
design matrix $X$ whose $t$-th row is $(1,\ y_{t-1},\ \ldots,\ y_{t-p})$. Then
$\hat\phi = (X^\top X)^{-1}X^\top Y$, and the estimated coefficient covariance is
$\widehat{\mathrm{Cov}}(\hat\phi) = \hat\sigma^2 (X^\top X)^{-1}$ — but there are two natural choices
of $\hat\sigma^2$, differing only in the denominator:
$$\hat\sigma^2_{\text{ML}} = \frac{1}{n-p}\sum_{t=p+1}^n \hat\epsilon_t^2, \qquad
\hat\sigma^2_{\text{OLS}} = \frac{1}{n-2p-1}\sum_{t=p+1}^n \hat\epsilon_t^2.$$
The first averages the $n-p$ squared residuals directly — the convention `AutoReg`'s conditional-MLE
fit uses. The second divides by the residual degrees of freedom, the $n-p$ residuals minus the $p+1$
estimated coefficients, which is the usual unbiased regression estimate that plain `OLS` reports. For
the log-scale fit here ($p=1$, $n=300$) the two are close but not equal:
$\hat\sigma_{\text{ML}} = 0.012469$ against $\hat\sigma_{\text{OLS}} = 0.012511$. Plugging each into
$\widehat{\mathrm{Cov}}(\hat\phi)$ gives two slightly different sets of coefficient standard errors,
and this is exactly why `armod_sm.bse` (from `AutoReg`) and `armod.bse` (from a plain OLS refit on the
same design matrix) don't quite agree — $0.003785$ against $0.003797$ for the intercept — even though
both are fitting the same equation to the same data.

### The recursion for the forecast-error variance

Write the forecast error at horizon $h$ as $e_h = y_{n+h} - \hat y_{n+h}$. Subtracting the forecast
recursion from the true AR equation $y_{n+h} = \phi_0 + \sum_j \phi_j y_{n+h-j} + \epsilon_{n+h}$, and
using that $y_{n+h-j} - \tilde y_{n+h-j} = 0$ exactly when $h - j \le 0$ (both sides are the same
observed value there), leaves
$$e_h = \sum_{j=1}^{\min(p,\,h-1)} \phi_j\, e_{h-j} \;+\; \epsilon_{n+h}, \qquad e_h := 0 \text{ for } h \le 0.$$
In words: the forecast errors obey the *same* $AR(p)$ recursion as the data, driven by the same
innovations, but started from rest at the forecast origin. In particular $e_1 = \epsilon_{n+1}$, so
the one-step-ahead forecast variance is just $\sigma^2$ — the smallest possible, and the value the
recursion builds up from.

Because $\epsilon_{n+h}$ is independent of $e_1,\ldots,e_{h-1}$ (those depend only on innovations up
to time $n+h-1$), the covariance matrix $\Gamma_h = \mathrm{Cov}(e_1,\ldots,e_h)$ can be grown one row
and column at a time instead of derived in closed form. Pair each $\phi_j$ with the error $e_{h-j}$ it
multiplies in the recursion above, and pad with zeros once $j$ would need to exceed $p$ or reach past
$e_1$; call the resulting vector $v$. Then $\mathrm{Cov}(e_l, e_h) = \sum_m \mathrm{Cov}(e_l,e_m)v_m$
for every $l < h$, i.e. the new column of covariances is $\Gamma_{h-1}v$, and the new variance is
$\sigma^2 + v^\top \Gamma_{h-1}v$:
$$\Gamma_h = \begin{pmatrix} \Gamma_{h-1} & \Gamma_{h-1}v \\[2pt] v^\top\Gamma_{h-1} & \sigma^2 + v^\top\Gamma_{h-1}v \end{pmatrix},
\qquad \Gamma_1 = (\sigma^2).$$
This is exactly the block update the code performs at each step, with $v$ itself updated as $h$ grows
by shifting in the next $\phi$ — or a zero, once the available lags run out. After $k$ steps,
$\sqrt{\mathrm{diag}(\Gamma_k)}$ is the vector of prediction standard errors for horizons $1$ through
$k$, and — plugging in $\hat\sigma$ and $\hat\phi_1,\ldots,\hat\phi_p$ for the unknown true values —
it reproduces `fcast_se` = `.se_mean` exactly, to the digits printed.

That equality is itself informative. The recursion only ever uses $\hat\sigma$ and the point estimates
$\hat\phi_j$; nowhere does it touch $\widehat{\mathrm{Cov}}(\hat\phi)$, the uncertainty in the
coefficients themselves. So the prediction interval this produces measures only one source of error —
the future innovations $\epsilon_{n+1},\ldots,\epsilon_{n+k}$ that haven't happened yet — and not the
fact that $\hat\phi_0,\ldots,\hat\phi_p$ were themselves estimated from a finite training sample and
would come out slightly different from another 300 quarters of history.

## Sources

- The whole chapter is drawn from one converted notebook: `CodeLectureNineteen153248Spring2025.ipynb`
  ("Prediction Uncertainty Quantification in AR models"), Berkeley STAT 153, Spring 2025, CC BY 4.0 —
  [`docs/statistics/berkeley/stat153/spring-2025/CodeLectureNineteen153248Spring2025.md`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureNineteen153248Spring2025.ipynb).
  All numbers quoted (coefficients, standard errors, interval widths) are read from that notebook's
  own printed output.
- No slide deck, transcript, or problem set was supplied alongside this notebook. The notebook itself
  states that both recursive methods used here — the point-forecast recursion and the forecast-error
  covariance recursion — were "detailed in class"; that classroom explanation is not part of the
  supplied material, and the derivations given in this chapter were reconstructed directly from the
  code and the $AR(p)$ equation, not copied from an unavailable source.
- The notebook also mentions, without giving detail, that "some heuristics" exist for choosing the
  order $p$, to be covered in the following lab — that material is likewise not included here.
- Two figures in the original notebook (the raw-scale forecast-with-interval plot, and its log-scale
  counterpart) were omitted in conversion to markdown; the diagram in this chapter is a schematic
  built from the notebook's printed numbers, not a reproduction of the omitted images.

---

[← 44. Multiple Sinusoids and Change-Points](44-multiple-sinusoids-and-change-points.md) · [Contents](index.md) · [46. Sinusoidal Regression and the DFT →](46-sinusoidal-regression-and-the-dft.md)
