---
title: "30. AR(p): Levels, Logs, and Differences"
course: "Berkeley Stat 153"
chapter: 30
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 30. AR(p): Levels, Logs, and Differences

## What this covers

This chapter works one forecasting example three different ways, to see how the *scale* on which
an AR(p) model is fit — the raw series, its logarithm, or the differenced logarithm — changes both
the fitted model and the quality of the resulting forecasts. The running example is quarterly US
GNP. The chapter assumes you already know what an AR(p) model is, how to estimate one by least
squares, and roughly why a trending series is often log-transformed and differenced before it is
modelled; what it adds is a worked, numerical comparison of doing all three to the same dataset.

## The data and the train/test split

The dataset is quarterly US GNP from FRED, starting 1947. Because the interest is in forecasting,
part of the series is held back to check the forecasts against: the last 16 observations (the most
recent four years, since the data are quarterly) are set aside as a test set, and every model below
is fit only to the remaining training data, $y_1, \dots, y_n$.

## Fitting an AR(p): two routes to the same estimate

An AR(p) model with intercept is

$$y_t = \phi_0 + \phi_1 y_{t-1} + \cdots + \phi_p y_{t-p} + \epsilon_t.$$

(Dropping $\phi_0$ — `trend = 'n'` in the code below rather than the default `trend = 'c'` — fits
the no-intercept version instead.) There are two equivalent ways to fit it. One is to call a
dedicated routine (`AutoReg` in `statsmodels`), which fits by conditional maximum likelihood. The
other is to build the regression by hand: stack the lagged values of $y$ into a design matrix,

$$X = \begin{pmatrix} 1 & y_{p} & y_{p-1} & \cdots & y_1 \\ 1 & y_{p+1} & y_{p} & \cdots & y_2 \\
\vdots \end{pmatrix}, \qquad \text{response} = \begin{pmatrix} y_{p+1} \\ y_{p+2} \\ \vdots
\end{pmatrix},$$

and run ordinary least squares. Fitting AR(2) to the GNP training data both ways gives exactly the
same coefficients:

| parameter | AutoReg | OLS |
|---|---|---|
| $\phi_0$ | 27.5376 | 27.5376 |
| $\phi_1$ (lag 1) | 0.7827 | 0.7827 |
| $\phi_2$ (lag 2) | 0.2273 | 0.2273 |

The standard errors are close but not identical — 13.295 / 0.057 / 0.057 from `AutoReg` against
13.363 / 0.057 / 0.058 from OLS — because `AutoReg` reports $z$-scores (using the asymptotic normal
approximation behind maximum likelihood) while OLS reports $t$-scores (the finite-sample
correction). With almost 300 observations here the two barely differ, but the distinction is worth
knowing: the two routes give identical point estimates and *almost* identical inference.

## Choosing the order $p$: a sequential test

Increasing $p$ can only improve the in-sample fit — a bigger model has more free parameters — so
fit quality alone cannot be used to choose $p$; the risk is overfitting a model that will not
generalize to the test set. The heuristic used here is a forward, test-and-stop procedure:

1. Start at $p = 1$.
2. Fit AR(p). Look at the 95% confidence interval for the *last* coefficient, $\phi_p$.
   - If the interval excludes 0, the newest lag is doing real work: set $p \leftarrow p+1$ and
     repeat.
   - If the interval contains 0, that lag is not distinguishable from having no effect: stop, and
     use $p - 1$ as the final order.

Applied to the GNP training data directly (Model One, below), this runs as follows.

| $p$ fit | 95% CI for $\phi_p$ | contains 0? |
|---|---|---|
| 1 | $[1.005,\ 1.011]$ | no — continue |
| 2 | $[0.115,\ 0.340]$ | no — continue |
| 3 | $[0.104,\ 0.387]$ | no — continue |
| 4 | $[-0.406,\ 0.266]$ | **yes — stop** |

So $p = 3$ is used. The same idea, automated as a loop that fits $p = 1, 2, \dots$ and checks the
confidence interval each time, is used again below for the log-scale and differenced-scale fits;
the only wrinkle worth flagging is that the object holding the confidence interval is indexed
differently depending on whether `statsmodels` hands it back as a plain array or as a labelled
pandas object (`conf_ints[-1, :]` versus `conf_ints.iloc[-1]`) — a minor API inconsistency rather
than anything conceptual.

## Forecasting from a fitted AR(p)

Once $p$ and the coefficients $\hat\phi_0, \dots, \hat\phi_p$ are fixed, a forecast $k$ steps beyond
the training data is generated recursively: extend the series with placeholder values and, working
forward one step at a time, apply the fitted equation, feeding in *forecast* values wherever a lag
reaches past the end of the training data:

$$\hat y_{n+i} = \hat\phi_0 + \sum_{j=1}^{p} \hat\phi_j\, z_{n+i-j}, \qquad
z_t = \begin{cases} y_t & t \le n \\ \hat y_t & t > n. \end{cases}$$

This manual recursion and the library's built-in `get_prediction` give identical numbers — a good
sanity check that the recursion is understood correctly and not just being called as a black box.

## Model One: AR(3) directly on the GNP level data

Fitting the chosen AR(3) to the raw training series and forecasting the next 16 quarters gives
point predictions that climb steadily, roughly in step with the training data's own trend:

| quarter ahead | 1 | 2 | 3 | 4 | ... | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|
| forecast | 22015.8 | 22297.4 | 22577.5 | 22733.3 | ... | 24608.0 | 24824.2 | 25042.1 | 25261.8 |

Plotted against the actual held-out values, the verdict given is that these predictions are
"decent but not very accurate" — the model captures the broad upward drift but not the finer
movement of the series.

## Model Two: AR(p) on $\log(\text{GNP})$

The next attempt fits the AR(p) machinery to $\log y_t$ rather than $y_t$ itself, and exponentiates
the resulting forecasts at the end to bring them back to the original scale. (The motivation for
working in logs at all — that a difference of logs approximates a percentage change, since $\log x
\approx x - 1$ near $x=1$ — is the same one that motivates Model Three below, where it is used
directly.)

Running the automated order-selection loop on $\log(\text{GNP})$ stops at $p = 4$ (the confidence
interval for $\phi_4$ contains 0), so the order actually used is $p = 3$, the same order as Model
One. The fitted AR(3):

| parameter | estimate | 95% CI |
|---|---|---|
| $\phi_0$ | 0.0201 | $[0.011,\ 0.030]$ |
| $\phi_1$ | 1.1730 | $[1.060,\ 1.286]$ |
| $\phi_2$ | 0.0029 | $[-0.179,\ 0.184]$ |
| $\phi_3$ | $-0.1772$ | $[-0.297,\ -0.058]$ |

One of the characteristic roots of this fitted model has modulus $1.0020$ — essentially on the unit
circle, just as the level-data AR(3) in Model One had a root of modulus $0.9922$. A root that close
to 1 is the signature of a highly persistent, close-to-non-stationary fit: it is what makes a model
fit directly to a trending series extrapolate the recent trend forward almost undamped, which is
exactly the behaviour Model One's forecast showed.

Forecasting and exponentiating back to the GNP scale gives predictions described as "closer
(compared to Model One) to the actual values... but the accuracy is still not very good."

## Model Three: differencing the log data first

Rather than fit the trend directly, Model Three removes it first by differencing the log series:

$$y_t = \log \text{GNP}_t - \log \text{GNP}_{t-1} = \log \frac{\text{GNP}_t}{\text{GNP}_{t-1}}.$$

Because $\log x \approx x - 1$ for $x$ near 1, $100 y_t$ is approximately the percentage change in
GNP from one quarter to the next. Plotted, this differenced series visibly has no trend — the trend
has been removed by the differencing itself, leaving something that looks like it could plausibly
be modelled by a low-order stationary AR(p).

Running the same order-selection loop on the differenced series stops at $p = 3$ (the interval for
$\phi_3$ contains 0), so $p = 2$ is used:

| parameter | estimate | 95% CI |
|---|---|---|
| $\phi_0$ | 0.0092 | $[0.007,\ 0.012]$ |
| $\phi_1$ (lag 1) | 0.1948 | $[0.082,\ 0.307]$ |
| $\phi_2$ (lag 2) | 0.2051 | $[0.087,\ 0.324]$ |

The characteristic roots now have moduli $1.7837$ and $2.7332$ — well clear of the unit circle,
unlike the near-unit roots of Models One and Two. This is the sign that differencing has done its
job: what is left behaves like a genuinely stationary AR(2), not a barely-damped trend.

Forecasting requires one extra step, because the AR(2) fitted here predicts *differences*
$y_{n+i} = \log \text{GNP}_{n+i} - \log \text{GNP}_{n+i-1}$, not log-GNP itself. To recover
forecasts of $\log \text{GNP}$, accumulate the predicted differences back onto the last observed
log value:

$$\hat y^{\log}_{n+1} = \log \text{GNP}_n + \widehat{(y_{n+1})}, \qquad
\hat y^{\log}_{n+i} = \hat y^{\log}_{n+i-1} + \widehat{(y_{n+i})} \ \ (i \ge 2),$$

then exponentiate the accumulated sequence to get forecasts of GNP itself. The result is described
as "much more accurate compared to the predictions obtained by the previous two models" — the
strongest verdict of the three, and it is offered as evidence that "AR(p) models are better for the
differenced log-data than for the log-data without differencing (and also for the original data)."

## The differenced AR(2) is a constrained AR(3) on $\log\text{GNP}$

The AR(2) fitted to $y_t = \log\text{GNP}_t - \log\text{GNP}_{t-1}$ can be rewritten, purely
algebraically, back in terms of $\log\text{GNP}_t$ itself. Substituting $y_t = \log\text{GNP}_t -
\log\text{GNP}_{t-1}$ into $y_t = \hat\phi_0 + \hat\phi_1 y_{t-1} + \hat\phi_2 y_{t-2} + \epsilon_t$
and collecting terms gives

$$\log\text{GNP}_t = \hat\phi_0 + (\hat\phi_1 + 1)\log\text{GNP}_{t-1} +
(\hat\phi_2 - \hat\phi_1)\log\text{GNP}_{t-2} - \hat\phi_2 \log\text{GNP}_{t-3} + \epsilon_t,$$

which is an AR(3) in $\log\text{GNP}_t$ — but a special one. Its three lag coefficients,
$(\hat\phi_1+1)$, $(\hat\phi_2-\hat\phi_1)$, and $-\hat\phi_2$, necessarily sum to exactly 1, as
they do here: $1.194775 + 0.010350 - 0.205125 = 1.000000$. That is precisely the unit-root
condition — the characteristic polynomial $1 - c_1 - c_2 - c_3$ evaluates to 0 at the AR
coefficients $c_1, c_2, c_3$ — and differencing *builds it in* by construction: any AR(2) fitted to
first differences, rewritten this way, will have coefficients summing to 1. An AR(3) fit directly
and freely to $\log\text{GNP}_t$ is not constrained that way, and indeed comes out close but not
identical:

| coefficient | derived from AR(2)-on-differences | fit directly as AR(3) |
|---|---|---|
| $\log\text{GNP}_{t-1}$ | 1.194775 | 1.173032 |
| $\log\text{GNP}_{t-2}$ | 0.010350 | 0.002946 |
| $\log\text{GNP}_{t-3}$ | $-0.205125$ | $-0.177248$ |

Forecasting with this derived, constrained AR(3) — using the same recursive formula as before —
reproduces exactly the same forecasts as the telescoping-sum method above (once exponentiated):
the two routes to a Model Three forecast agree. But the freely-fit AR(3) on $\log\text{GNP}_t$
(Model Two) is a genuinely different model from the constrained one implied by differencing, and
gives different forecasts, which is the point of keeping the three models distinct rather than
treating "AR(3) on logs" and "AR(2) on differenced logs" as the same idea in different clothes.

## What the comparison shows

| model | fit to | order chosen | forecast verdict |
|---|---|---|---|
| One | GNP level | 3 | decent, not very accurate |
| Two | $\log$ GNP | 3 | closer than One, still not very good |
| Three | differenced $\log$ GNP | 2 | much more accurate than One or Two |

The pattern across Models One and Two — a fitted AR(p) whose dominant characteristic root sits
almost exactly on the unit circle — is what makes their forecasts little more than an extrapolation
of the recent trend. Differencing first, in Model Three, removes that near-unit root before the
AR(p) machinery ever sees the data, leaving a shorter, genuinely stationary-looking model whose
forecasts tracked the held-out data much better. The stated conclusion is that it is "quite common,
while using AR models, to work with differenced data" for series of this kind.

## Sources

All three sections are drawn from one converted lecture notebook, `CodeLabNine153248Fall2025.ipynb`
(berkeley-stat153, fall 2025, CC BY 4.0), split across three files:

- Model One (GNP-level fit, the two fitting routes, the order-selection heuristic worked by hand,
  and the manual/automatic forecasting comparison):
  `docs/statistics/berkeley/stat153/fall-2025/CodeLabNine153248Fall2025/01-model-one-ar-p-directly-on-the-training-data.md`
- Model Two (log-scale fit, automated order-selection loop, root/unit-root observation):
  `docs/statistics/berkeley/stat153/fall-2025/CodeLabNine153248Fall2025/02-model-two-ar-p-model-on-the-log-data.md`
- Model Three (differencing, telescoping forecast recursion, the AR(3)-from-AR(2) algebra):
  `docs/statistics/berkeley/stat153/fall-2025/CodeLabNine153248Fall2025/03-model-three-working-with-differenced-data.md`

Two things the notebook points to but does not itself contain: the phrase "as seen in class" for
the two ways of fitting an AR(p), and "as we remarked previously" for the $\log x \approx x - 1$
approximation — both referring to earlier lecture material not included among the supplied files.
The plotted comparisons between forecast and actual test data are described in the notebook's own
words ("decent but not very accurate", "closer... but still not very good", "much more accurate")
but the figures themselves are not reproduced here, since the notebook conversion omitted the
images and only their numeric outputs survive.

---

[← 29. Change-Point Detection and Estimation](29-change-point-detection-and-estimation.md) · [Contents](index.md) · [31. Fitting Trends to Time Series →](31-fitting-trends-to-time-series.md)
