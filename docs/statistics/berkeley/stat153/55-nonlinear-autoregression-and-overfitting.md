---
title: "55. Nonlinear Autoregression and Overfitting"
course: "Berkeley Stat 153"
chapter: 55
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 55. Nonlinear Autoregression and Overfitting

## What this covers

Two simulation experiments that put the NAR($p$) model — an AR($p$) model with its linear
autoregressive function replaced by a single-hidden-layer neural network — to a stress test: can it
recover a nonlinear dependence on one specific lag buried inside a wider window of lags, and what
happens to it as that window is stretched out to lag 20? It assumes the NAR($p$) model itself has
already been introduced (autoregression $y_t = g(y_{t-1},\dots,y_{t-p}) + \epsilon_t$ with $g$
approximated by a network rather than assumed linear), together with the ordinary linear AR($p$)
model it is being measured against.

## The shared design of both experiments

Both examples simulate from the same nonlinear rule, but with the dependence pushed back to a
single lag $\ell$:

$$y_t = g(y_{t-\ell}) + \epsilon_t, \qquad g(x) = \frac{2x}{1+0.8x^2}, \qquad \epsilon_t \sim
\mathrm{Uniform}(-1,1),$$

with $n = 1450$ observations, $\ell = 5$ in the first experiment and $\ell = 20$ in the second. The
noise has mean $0$ and variance $\frac{(1-(-1))^2}{12} = \frac13$.

The shape of $g$ matters for what follows. It is odd, has slope $g'(0) = 2$ at the origin, climbs to
a maximum of about $1.12$ near $x \approx 1.12$, and then bends back down toward $0$ as $x$ grows —
nothing a fixed straight line can track once $x$ moves away from zero.

<figure>
<svg viewBox="0 0 340 225" role="img" aria-label="The curve g(x) = 2x/(1+0.8x^2) compared with the straight line that matches it at the origin">
  <line x1="20" y1="110" x2="320" y2="110" stroke="currentColor" stroke-width="1"/>
  <line x1="170" y1="20" x2="170" y2="200" stroke="currentColor" stroke-width="1"/>
  <text x="308" y="123" font-size="12" fill="currentColor">x</text>
  <text x="176" y="30" font-size="12" fill="currentColor">g(x)</text>
  <line x1="141.9" y1="200" x2="198.1" y2="20" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.7"/>
  <text x="202" y="24" font-size="11" fill="currentColor">y = 2x</text>
  <polyline points="20.0,144.8 27.5,146.3 35.0,148.0 42.5,149.8 50.0,151.8 57.5,153.9 65.0,156.2 72.5,158.7 80.0,161.4 87.5,164.2 95.0,167.1 102.5,170.1 110.0,173.0 117.5,175.4 125.0,176.9 132.5,176.7 140.0,173.5 147.5,165.9 155.0,152.6 162.5,133.3 170.0,110.0 177.5,86.7 185.0,67.4 192.5,54.1 200.0,46.5 207.5,43.3 215.0,43.1 222.5,44.6 230.0,47.0 237.5,49.9 245.0,52.9 252.5,55.8 260.0,58.6 267.5,61.3 275.0,63.8 282.5,66.1 290.0,68.2 297.5,70.2 305.0,72.0 312.5,73.7 320.0,75.2" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="222" y="215" font-size="11" fill="currentColor">g(x)</text>
</svg>
<figcaption>The true nonlinearity g (solid) and the tangent line y = 2x that agrees with it only at
x = 0 (dashed). The line has already left the frame by about |x| = 0.7, while g bends back toward
zero. A linear AR(p) model is confined to something like the dashed line no matter how its
coefficients are chosen; only a model with a nonlinear hidden layer can bend to follow the solid
curve.</figcaption>
</figure>

Two models are fitted to each series, both given a window of $p = \ell$ consecutive lags as input —
so the input width matches the true lag exactly, but only the oldest of the $p$ inputs, $y_{t-p}$,
actually carries information; the other $p-1$ are nuisance lags the model has to learn to ignore:

- **NAR($p$)**: a single hidden layer network,
  $$\hat y_t = \beta_0 + \sum_{j=1}^k \beta_j\, \mathrm{ReLU}\!\Big(b_j + \sum_{i=1}^p W_{ji}\,
  y_{t-i}\Big),$$
  with hidden width $k = 6$ kept fixed across both experiments, fitted by minimizing mean squared
  error with Adam (learning rate $0.01$) for $10{,}000$ epochs.
- **AR($p$)**: the ordinary linear autoregression, fitted the standard way, as a benchmark that is
  structurally wrong (it cannot represent the curvature of $g$) but has far fewer parameters.

Forecasts are then built the same way for three candidates — the fitted NAR model, the fitted AR
model, and the true $g$ itself: starting from the last $p$ observed values, the model predicts one
step ahead, that prediction is appended to the window and the oldest value dropped, and the process
repeats for $k_{\text{future}} = 40$ steps. For the true-$g$ forecast the noise term is replaced by
its mean, $0$, at every step — the best any forecast could do under squared error if $g$ and the lag
were known exactly. Because the simulated series stops at $n = 1450$, there is no real continuation
to compare against; a freshly simulated one would carry its own fresh shocks and nothing could match
it exactly. Comparing to this zero-noise oracle path instead isolates how well each model has learned
$g$ and the lag, rather than how lucky it got with future noise. One caveat: since $g$ is nonlinear,
plugging predicted means back in as if they were realized values is not exactly the true multi-step
conditional expectation once the horizon passes $\ell$ ($E[g(Y)] \ne g(E[Y])$ in general) — but the
same recursion is applied identically to all three candidates, so the comparison between them is
still fair. The metric used is the mean squared error between a candidate's 40-step forecast path and
the oracle path, and the ratio $\mathrm{MSE}_{\mathrm{AR}} / \mathrm{MSE}_{\mathrm{NAR}}$ summarizes
which one tracked the truth more closely.

## Example Two: a lag-5 nonlinearity the network finds

With $\ell = p = 5$, training loss falls from about $0.96$ at initialization to about $0.33$ by
roughly epoch $3000$, and stays there for the remaining $7000$ epochs. That floor is suspiciously
close to the irreducible noise variance, $\frac13 \approx 0.333$ — a sign that the network has come
close to recovering $g$ itself, leaving little beyond the noise in the residuals. Plotting the
network's fitted values against $y_{t-5}$ (sorted) and overlaying the true $g$ confirms this
visually: the two curves sit almost on top of each other.

The 40-step forecast comparison against the oracle path gives

$$\mathrm{MSE}_{\mathrm{AR}} \approx 0.496, \qquad \mathrm{MSE}_{\mathrm{NAR}} \approx 0.00278,
\qquad \frac{\mathrm{MSE}_{\mathrm{AR}}}{\mathrm{MSE}_{\mathrm{NAR}}} \approx 178.$$

The NAR forecast is nearly two orders of magnitude closer to the oracle than the linear AR forecast.
This is exactly what the shape argument above predicts: the linear model can only ever fit a fixed
straight line through the data, while the network's hidden layer lets it bend to follow $g$, and once
it has done so its recursive forecast tracks what perfect knowledge of $g$ would have produced —
while the AR forecast, built from a fundamentally wrong functional form, drifts away over the
40-step horizon.

## Example Three: stretching the window to lag 20

The only changes are $\ell = p = 20$ (with $k = 6$ kept the same) — a fifteen-lag jump that leaves
the true signal in exactly one input, $y_{t-20}$, but multiplies the network's parameter count from
$k(p+1) + (k+1) = 43$ at $p = 5$ to $133$ at $p = 20$, while the number of training pairs barely
moves (about $1445$ to $1430$). Training loss now settles around $0.365$ — a little above the
$\frac13$ noise floor, consistent with the network not having pinned down $g$ as cleanly as before —
and the fitted-values-against-$y_{t-p}$ plot no longer tracks the true curve as well as it did at
$p=5$.

The forecast comparison flips:

$$\mathrm{MSE}_{\mathrm{AR}} \approx 0.155, \qquad \mathrm{MSE}_{\mathrm{NAR}} \approx 0.163, \qquad
\frac{\mathrm{MSE}_{\mathrm{AR}}}{\mathrm{MSE}_{\mathrm{NAR}}} \approx 0.95.$$

The linear AR(20) forecast is now, if anything, slightly *closer* to the oracle than the NAR(20)
forecast is — despite AR being unable to represent $g$'s curvature at all. As the source material
puts it, this is a result of overfitting: with nineteen nuisance lags for the network to potentially
chase noise along, and forecasting done recursively so that whatever the network gets wrong at one
step feeds straight into the next 39, small errors in the learned function compound across the
horizon. The linear model, though permanently misspecified, is a much smaller family — $p+1$
coefficients rather than $k(p+1)+(k+1)$ — and that rigidity, which cost it dearly in Example Two, now
works in its favor: it has nothing extra to overfit with.

## Reading the two examples together

Matching the input window to the true lag is not enough on its own; what matters is how much of that
window is actually informative relative to how many parameters the model is given to work with.
Enlarging $p$ from 5 to 20 kept the hidden width fixed but roughly tripled the parameter count while
leaving the effective sample size unchanged, and that was enough to erase the large advantage the
correctly-specified nonlinear model had shown at $p=5$. A structurally wrong but low-parameter model
can end up forecasting better than a structurally right but higher-parameter one, once the extra
capacity has more room to fit noise than signal.

## Sources

- `docs/statistics/berkeley/stat153/spring-2025/CodeLectureTwentyFive153248Spring2025/02-example-two.md`
  — "Example Two" ($\ell = p = 5$): data simulation, the `SingleHiddenLayerNN` class, training loop
  and loss trace, recursive forecasting code for the NAR, AR(5) and true-$g$ paths, the MSE
  comparison, and the fitted-values-vs-$y_{t-5}$ plot.
- `docs/statistics/berkeley/stat153/spring-2025/CodeLectureTwentyFive153248Spring2025/03-example-three.md`
  — "Example Three" ($\ell = p = 20$): the same pipeline repeated at lag 20, including the explicit
  remark that the larger NAR(20) model raises "the issue of overfitting," the loss trace, the reversed
  MSE comparison, and the fitted-values-vs-$y_{t-p}$ plot.
- Both files are converted from `CodeLectureTwentyFive153248Spring2025.ipynb`, berkeley-stat153
  spring-2025, CC BY 4.0.
- Referred to but not contained in the supplied material: the general NAR($p$) model definition and
  its first illustration with the true lag equal to 1 ("Example One"), which this notebook's index
  implies preceded these two sections but was not included in the input files for this chapter; also
  the plotted figures themselves, which the conversion omits and this chapter describes from the
  numbers and code that produced them rather than from the images.

---

[← 54. ACF, PACF, and AR(p) Stationarity](54-acf-pacf-and-ar-p-stationarity.md) · [Contents](index.md) · [56. Model Fitting via PyTorch →](56-model-fitting-via-pytorch.md)
