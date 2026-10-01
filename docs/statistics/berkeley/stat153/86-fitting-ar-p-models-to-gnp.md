---
title: "86. Fitting AR(p) Models to GNP"
course: "Berkeley Stat 153"
chapter: 86
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 86. Fitting AR(p) Models to GNP

## What this covers

A lab worked on a single question with three attempts at an answer: given one economic time series
— quarterly US GNP — how do you decide the order $p$ of an autoregressive model, fit it, and use it
to forecast, and does it matter whether the AR model is fit to the raw series, to its logarithm, or
to the differences of the logarithm? It assumes the reader already knows what an AR($p$) process is
and how ordinary least squares estimates its coefficients; the new material is the *practice* of
order selection, multi-step forecasting, and the effect of transforming the series before fitting.

## The data and the train/test split

The series is quarterly US GNP from FRED, from 1947 onward. The last 16 observations — the most
recent four years — are held out as a test set; every model below is fit only to the remaining
data ($n_{\text{train}}$ observations) and then judged on how well it predicts the 16 points it
never saw.

## Two equivalent ways to fit AR($p$)

An AR($p$) model,
$$y_t = \phi_0 + \phi_1 y_{t-1} + \cdots + \phi_p y_{t-p} + \epsilon_t,$$
can be fit two ways, and both were used side by side on an AR(2) model for the GNP training data:

- **`AutoReg`** (from `statsmodels`), which fits the model directly. `trend = 'c'` includes the
  intercept $\phi_0$ (the default); `trend = 'n'` drops it.
- **Manual OLS**: build the response vector $y_p, y_{p+1}, \dots$ and a design matrix whose rows
  are $(1, y_{t-1}, \dots, y_{t-p})$, then run ordinary least squares.

Fitting AR(2) to the GNP training data both ways gives *identical* coefficient estimates —
$\hat\phi_0 = 27.538$, $\hat\phi_1 = 0.7827$, $\hat\phi_2 = 0.2273$ — but slightly different
standard errors: `AutoReg` reports $13.295, 0.057, 0.057$ and labels its test statistics
$z$-scores, while OLS reports $13.363, 0.057, 0.058$ and labels them $t$-scores. The two methods
are solving the same estimation problem; the discrepancy is only in how each computes the reference
distribution for inference, not in the point estimates. Either method is fine to use in practice.

## Choosing the order $p$ by testing the last coefficient

Raising $p$ makes an AR model more flexible and more prone to overfitting, so some rule is needed
to stop. The heuristic used here is sequential:

1. Start at $p = 1$.
2. Fit AR($p$) and look at the 95% confidence interval for $\phi_p$ — the coefficient on the
   *most distant* lag just added. If the interval excludes 0, that lag is doing real work: set
   $p \leftarrow p+1$ and repeat. If the interval contains 0, that lag looks redundant: stop, and
   use order $p - 1$.

Applied to the GNP training data directly (Model One):

| $p$ | coefficient tested | estimate | 95% CI | contains 0? |
|---|---|---|---|---|
| 1 | $\phi_1$ | $1.008$ | $[1.005,\ 1.011]$ | no — go to $p=2$ |
| 2 | $\phi_2$ | $0.227$ | $[0.115,\ 0.340]$ | no — go to $p=3$ |
| 3 | $\phi_3$ | $0.246$ | $[0.104,\ 0.387]$ | no — go to $p=4$ |
| 4 | $\phi_4$ | $-0.070$ | $[-0.406,\ 0.266]$ | **yes — stop** |

So the chosen order is $p = 3$, and it is the AR(3) fit — with $\hat\phi_0 = 35.78$,
$\hat\phi_1 = 0.720$, $\hat\phi_2 = 0.047$, $\hat\phi_3 = 0.246$ — that is carried forward to
forecasting. Note that $\phi_2$ itself is not significant in the final AR(3) fit (its own interval,
$[-0.105, 0.198]$, contains 0); the rule only ever tests the newest, highest-order coefficient at
each step, not every coefficient in the current model.

The same rule, automated as a loop that fits $p = 1, 2, \dots$ and stops the first time the
confidence interval for $\phi_p$ contains 0 (then backs off to $p-1$), is reused for Models Two and
Three below.

## Producing multi-step forecasts

Once a model is fit, forecasting the 16 held-out points can be done two ways, and both were checked
to agree exactly. The built-in route is `get_prediction`, which returns `predicted_mean` for the
requested horizon. The manual route extends the training series with placeholder values and fills
them in recursively:
$$\hat y_{n+i} = \hat\phi_0 + \sum_{j=1}^{p} \hat\phi_j \, z_{n+i-j}, \qquad
z_t = \begin{cases} y_t & t \le n \\ \hat y_t & t > n \end{cases}$$
so that once the forecast horizon runs past the end of the training data, the recursion feeds its
own earlier forecasts back in as if they were data.

<figure>
<svg viewBox="0 0 480 240" role="img" aria-label="Diagram of how each multi-step AR forecast is built from actual data and from the model's own earlier forecasts">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="150" y="16" text-anchor="middle" font-size="12" fill="currentColor">observed</text>
  <text x="330" y="16" text-anchor="middle" font-size="12" fill="currentColor">forecast</text>
  <line x1="196" y1="26" x2="196" y2="220" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>

  <path d="M60,140 Q150,72 240,140" fill="none" stroke="currentColor" marker-end="url(#arrow)" opacity="0.7"/>
  <path d="M150,140 Q195,112 240,140" fill="none" stroke="currentColor" marker-end="url(#arrow)" opacity="0.7"/>
  <path d="M150,140 Q240,72 330,140" fill="none" stroke="currentColor" marker-end="url(#arrow)" opacity="0.7"/>
  <path d="M240,140 Q285,112 330,140" fill="none" stroke="currentColor" marker-end="url(#arrow)" opacity="0.7"/>
  <path d="M240,140 Q330,72 420,140" fill="none" stroke="currentColor" marker-end="url(#arrow)" opacity="0.7"/>
  <path d="M330,140 Q375,112 420,140" fill="none" stroke="currentColor" marker-end="url(#arrow)" opacity="0.7"/>

  <rect x="30" y="140" width="60" height="36" rx="4" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="60" y="163" text-anchor="middle" font-size="12" fill="currentColor">y(n-1)</text>
  <rect x="120" y="140" width="60" height="36" rx="4" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="150" y="163" text-anchor="middle" font-size="12" fill="currentColor">y(n)</text>
  <rect x="210" y="140" width="60" height="36" rx="4" fill="none" stroke="currentColor" stroke-dasharray="3 2"/>
  <text x="240" y="163" text-anchor="middle" font-size="12" fill="currentColor">ŷ(n+1)</text>
  <rect x="300" y="140" width="60" height="36" rx="4" fill="none" stroke="currentColor" stroke-dasharray="3 2"/>
  <text x="330" y="163" text-anchor="middle" font-size="12" fill="currentColor">ŷ(n+2)</text>
  <rect x="390" y="140" width="60" height="36" rx="4" fill="none" stroke="currentColor" stroke-dasharray="3 2"/>
  <text x="420" y="163" text-anchor="middle" font-size="12" fill="currentColor">ŷ(n+3)</text>
</svg>
<figcaption>An AR(2) forecast beyond the training set feeds its own earlier forecasts back into the
recursion once the true lagged values run out. The same idea reappears in Model Three, undoing a
difference by cumulatively adding each forecast increment onto the previous forecast level.</figcaption>
</figure>

For the GNP data, this AR(3)-on-levels forecast (Model One) is, in the lab's own words, "decent but
not very accurate" against the 16 actual held-out values.

## Model Two: fit to $\log(\text{GNP})$ instead of the level

Rather than fit AR($p$) to the raw series, the same procedure can be applied to $\log(\text{GNP})$;
predictions then come out on the log scale and must be exponentiated to compare against the actual
GNP values. Running the automated order-selection loop on $\log(\text{GNP})$ stops at $p=4$ (the
interval for $\phi_4$ contains 0), so the chosen order is $p = 3$. The fitted AR(3) is
$$\log\text{GNP}_t = 0.0201 + 1.1730\,\log\text{GNP}_{t-1} + 0.0029\,\log\text{GNP}_{t-2}
- 0.1772\,\log\text{GNP}_{t-3} + \epsilon_t,$$
with the middle coefficient statistically indistinguishable from 0 ($z = 0.032$) even though it
survived the sequential test that chose $p$ (the test only ever screens the *newest* coefficient
added, as noted above). Forecasting 16 steps ahead and exponentiating back to the GNP scale gives
predictions that are, compared with Model One, "closer... to the actual values but the accuracy is
still not very good."

## Model Three: fit to the differenced log series

Instead of the level of $\log(\text{GNP})$, work with its first difference:
$$y_t = \log\text{GNP}_t - \log\text{GNP}_{t-1} = \log\frac{\text{GNP}_t}{\text{GNP}_{t-1}}.$$
Because $\log x \approx x - 1$ for $x$ near 1, $100 y_t$ is approximately the percentage change in
GNP from one quarter to the next. Plotted, this differenced series looks qualitatively different
from either the level or the log level: the trend is gone, because differencing is exactly what
removed it.

Running the same order-selection loop on the differenced series stops at $p = 3$ (the interval for
$\phi_3$ contains 0), so the chosen order is $p = 2$:
$$y_t = 0.0092 + 0.1948\,y_{t-1} + 0.2051\,y_{t-2} + \epsilon_t,$$
with both lag coefficients clearly nonzero ($z = 3.39$ and $3.40$).

This model forecasts *differences*, not levels, so its 16-step forecast has to be integrated back
before it means anything on the GNP scale. Writing $\widehat{\Delta}_{n+i}$ for the forecast of
$y_{n+i} = \log\text{GNP}_{n+i} - \log\text{GNP}_{n+i-1}$, the recursion is
$$\hat y_{n+1} = \log\text{GNP}_n + \widehat{\Delta}_{n+1}, \qquad
\hat y_{n+i} = \hat y_{n+i-1} + \widehat{\Delta}_{n+i} \ \ (i \ge 2),$$
and then $\widehat{\text{GNP}}_{n+i} = \exp(\hat y_{n+i})$. This is the same recursive-forecast idea
as the figure above, just applied to increments instead of levels. The resulting predictions are
"much more accurate compared to the predictions obtained by the previous two models" — the central
empirical finding of the lab: an AR($p$) model fits the differenced log data far better than it
fits either the level or the plain log data.

## Why differencing helped: the restricted AR(3) hiding inside the AR(2)

The AR(2) fitted to differences can be translated back into a statement about $\log\text{GNP}_t$
itself. Substituting $y_t = \log\text{GNP}_t - \log\text{GNP}_{t-1}$ into
$y_t = \hat\phi_0 + \hat\phi_1 y_{t-1} + \hat\phi_2 y_{t-2} + \epsilon_t$ and collecting terms gives
$$\log\text{GNP}_t = \hat\phi_0 + (\hat\phi_1+1)\log\text{GNP}_{t-1}
+ (\hat\phi_2-\hat\phi_1)\log\text{GNP}_{t-2} - \hat\phi_2\log\text{GNP}_{t-3} + \epsilon_t.$$
So the differenced model *is* an AR(3) model for $\log\text{GNP}_t$ — but a constrained one: whatever
$\hat\phi_1$ and $\hat\phi_2$ turn out to be, the three level-coefficients satisfy
$$(\hat\phi_1+1) + (\hat\phi_2-\hat\phi_1) + (-\hat\phi_2) = 1$$
exactly. That constraint is the algebraic signature of having been built from a difference, and it
is exactly what differencing is for: forcing the characteristic polynomial to have a root at 1, so
that the trend that made the level series so persistent is no longer part of what the AR model has
to explain.

Plugging in the fitted numbers, the implied level-coefficients are $(0.0092, 1.1948, 0.0104,
-0.2051)$, compared with $(0.0201, 1.1730, 0.0029, -0.1772)$ for the AR(3) fit directly to
$\log\text{GNP}_t$ (Model Two) — "somewhat similar but not exactly the same." Running the ordinary
forecast recursion with the derived, constrained coefficients reproduces exactly the same 16
predictions as integrating the differenced forecasts one step at a time above; the two routes to
the same forecast agree to the last digit.

The lab's conclusion: predictions from an AR(3) fit directly to $\log\text{GNP}_t$ (Model Two) are
different from predictions of the constrained AR(3) implied by an AR(2) fit to the differences
(Model Three) — they are not the same model, even though both are technically third-order — and
"it is quite common, while using AR models, to work with differenced data."

## Sources

- Berkeley STAT 153, Spring 2025, Lab 10 — "AR models (estimation, inference and prediction)",
  converted from `Lab10.ipynb`
  (https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab10.ipynb),
  split into three sections used in full here:
  - Section 1, "Model One: AR(p) directly on the training data" — train/test split, `AutoReg` vs.
    manual OLS, the sequential order-selection heuristic worked through $p=1$–$4$, and both
    forecasting routes.
  - Section 2, "Model Two: AR(p) model on the log(data)" — the automated order-selection loop and
    the AR(3) fit to $\log(\text{GNP})$.
  - Section 3, "Model Three: Working with Differenced Data" — the AR(2) fit to differenced
    $\log(\text{GNP})$, undoing the difference to forecast levels, and the algebraic equivalence to
    a constrained AR(3) on $\log(\text{GNP})$.
- No slide deck or lecture transcript was supplied for this lab; no problem-set exercises were
  supplied either.

---

[← 85. Course Overview: Time Series Analysis](85-course-overview-time-series-analysis.md) · [Contents](index.md) · [87. ACF and PACF in Practice →](87-acf-and-pacf-in-practice.md)
