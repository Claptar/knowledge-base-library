---
title: "26. From Sinusoid to AR(2)"
course: "Berkeley Stat 153 Fall 2024"
chapter: 26
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 26. From Sinusoid to AR(2)

## What this covers

A single sunspot-count series is split into a training stretch and a held-out test stretch, and
three forecasting models are fit to the training data and compared by how well they predict the
test data. The three are not unrelated guesses: each is a deliberate loosening of the one before
it, starting from a single rigid sinusoid and ending at a general second-order autoregression. This
chapter assumes the harmonic (sinusoid) regression model and the idea of searching over frequency
by profile least squares, both from earlier in the course, and the basic idea of an autoregressive
model. It does not re-derive either of those; it uses them.

## Setting

The training values are called $y_1, \dots, y_n$ and the withheld future values $y_{n+1}, \dots$
are compared against each model's forecast. Every model below is fit only to the training portion,
then used to produce forecasts over the test horizon, and every model is scored the same way: the
root-mean-square error between its forecasts and the actual (withheld) test values. That common
scorecard is what makes the three comparable at all, since they are fit by different criteria.

## Model One: the sinusoid, fit by profile least squares

The first model is the sinusoid-plus-noise model from earlier in the course:

$$
y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad
\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0, \sigma^2).
$$

For a *fixed* frequency $f$, this is an ordinary linear regression in $(\beta_0, \beta_1, \beta_2)$,
so it can be fit by OLS. What is not linear is $f$ itself, so it is handled by a grid search: for
each candidate $f$ on a fine grid, run the OLS regression and record its residual sum of squares
$\mathrm{RSS}(f)$; then take $\hat f$ to be the grid point that minimizes $\mathrm{RSS}(f)$. This is
the same profile-least-squares idea used for frequency estimation earlier in the course, only
applied here with a much finer grid (spacing $0.0001$) over $f \in (0, 0.5)$ — the search never
looks past $0.5$ because, for data spaced one unit apart, no frequency beyond that is
distinguishable from one below it.

Carrying this out on the sunspot training data gives $\hat f \approx 0.0899$, i.e. an estimated
period of about $1/\hat f \approx 11.12$. Forecasts for the test times are then the deterministic
continuation of the fitted sinusoid — plug the fitted $(\hat\beta_0, \hat\beta_1, \hat\beta_2, \hat
f)$ into the formula at the future times, with no noise term, since $E[\epsilon_t] = 0$. This gives
a root-mean-square prediction error of about **79.84**.

## Model Two: the Yule model

The second model starts from a fact about the *noiseless* sinusoid, stated here without its proof
(that proof was given earlier in the course and is not part of this material): the deterministic
sinusoid

$$
s_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi f t), \qquad t = 1, 2, \dots
$$

satisfies, exactly and with no error term, the second-order linear recursion

$$
s_t = \alpha_0 + \alpha_1 s_{t-1} - s_{t-2}, \qquad
\alpha_0 = 2\beta_0(1 - \cos\omega), \quad \alpha_1 = 2\cos\omega, \quad \omega = 2\pi f.
$$

That is, a pure sinusoid *is* a particular linear autoregression of order two — one whose
second-lag coefficient is pinned at exactly $-1$. This suggests a different way to add noise to a
sinusoid-shaped model: instead of adding $\epsilon_t$ to the sinusoid formula (Model One), add it to
the recursion itself:

$$
y_t = \alpha_0 + \alpha_1 y_{t-1} - y_{t-2} + \epsilon_t.
$$

Because the coefficient on $y_{t-2}$ is fixed at $-1$ rather than estimated, this is still an
ordinary two-parameter linear regression, provided the $-y_{t-2}$ term is moved to the left-hand
side first:

$$
\sum_{t=3}^n \big(y_t + y_{t-2} - \alpha_0 - \alpha_1 y_{t-1}\big)^2.
$$

The trick is to treat $y_t + y_{t-2}$ as a new response variable and regress it, by OLS, on $y_{t-1}$
and a constant, summing from $t = 3$ to $n$ (the recursion needs two lags of history, so the first
two training points cannot be used as responses). Fitting this to the sunspot training data gives
$\hat\alpha_0 \approx 27.31$ and $\hat\alpha_1 \approx 1.635$.

Since $\alpha_1 = 2\cos\omega = 2\cos(2\pi f)$, the fitted $\hat\alpha_1$ carries a frequency
estimate of its own: $\hat f = \arccos(\hat\alpha_1/2)/(2\pi)$, giving an estimated period of about
**10.23** — noticeably shorter than Model One's 11.12. The two estimates need not agree: one comes
from minimizing residual variance in the sinusoid formula directly, the other from minimizing
residual variance in the recursion, and the sunspot cycle is not an exact sinusoid, so the two
criteria pick up slightly different frequencies.

Forecasting now has to be done recursively, because each forecast depends on the previous two
values: starting from the end of the training data, each future value is generated in turn from
the fitted recursion using the two preceding values (actual where available, previously forecast
once the horizon runs past the training data), and the process is iterated across the whole test
span. This gives a root-mean-square prediction error of about **79.53** — "basically the same" as
Model One, marginally smaller here, though a different train/test split could easily reverse that.

## Model Three: AR(2)

The Yule model is a second-order autoregression with one restriction built in: the coefficient on
$y_{t-2}$ is forced to be exactly $-1$. The natural next step is to stop forcing it, and let the
data choose it:

$$
y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \epsilon_t.
$$

With $\phi_2$ now free, there is no need for the algebraic trick above — this is fit directly as an
ordinary three-parameter linear regression of $y_t$ on $(1, y_{t-1}, y_{t-2})$ for $t = 3, \dots, n$.
On the sunspot training data this gives

$$
\hat\phi_0 \approx 23.09, \qquad \hat\phi_1 \approx 1.378, \qquad \hat\phi_2 \approx -0.684,
$$

with an estimated innovation standard deviation $\hat\sigma \approx 24.70$. The fitted $\hat\phi_2$
is much closer to zero than the $-1$ that the Yule model imposes — the data does not actually
support the fully persistent oscillation that Model Two builds in by assumption.

Forecasts are again generated recursively, exactly as for Model Two but with the free $\hat\phi_2$
in place of $-1$. The root-mean-square prediction error is about **70.32** — clearly the best of the
three, even though (as the next section explains) its forecasts look the least like the data.

## Why the AR(2) forecasts look flatter, and still win

Forecast paths from the two lag-2 recursions behave very differently far from the training data.
The Yule model's recursion has characteristic roots $e^{\pm i\omega}$ exactly on the unit circle —
that is what makes it reproduce a sinusoid with no decay at all — so its forecasts keep oscillating
indefinitely, at fixed amplitude, however far ahead they are pushed. The AR(2) recursion, with
$\hat\phi_2 \approx -0.684$ rather than $-1$, has its characteristic roots strictly inside the unit
circle, so the dependence on where the forecast started decays geometrically: pushed far enough
ahead, the AR(2) forecast settles down to a constant (the process's unconditional mean) instead of
continuing to oscillate.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Schematic contrast between a forecast that keeps oscillating and one that damps to a constant">
  <polyline points="30,140 35,107.7 40,87.7 45,87.7 50,107.7 55,140 60,172.3 65,192.3 70,192.3 75,172.3 80,140 85,107.7 90,87.7 95,87.7 100,107.7 105,140 110,172.3 115,192.3 120,192.3 125,172.3 130,140 135,107.7 140,87.7 145,87.7 150,107.7 155,140 160,172.3 165,192.3 170,192.3 175,172.3 180,140 185,107.7 190,87.7 195,87.7 200,107.7 205,140 210,172.3 215,192.3 220,192.3" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="220" y1="20" x2="220" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="222" y="16" font-size="11" fill="currentColor">forecast start</text>
  <polyline points="220,192.3 225,172.3 230,140 235,107.7 240,87.7 245,87.7 250,107.7 255,140 260,172.3 265,192.3 270,192.3 275,172.3 280,140 285,107.7 290,87.7 295,87.7 300,107.7 305,140 310,172.3 315,192.3 320,192.3 325,172.3 330,140" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="332" y="145" font-size="11" fill="currentColor">Yule / Model One</text>
  <polyline points="220,192.3 225,168.9 230,140 235,116.8 240,106.5 245,110 250,123.4 255,140 260,153.3 265,159.2 270,157.2 275,149.5 280,140 285,132.4 290,129 295,130.1 300,134.5 305,140 310,144.4 315,146.3 320,145.7 325,143.1 330,140" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="1,3"/>
  <text x="290" y="205" font-size="11" fill="currentColor">AR(2)</text>
  <text x="32" y="205" font-size="11" fill="currentColor">training data</text>
</svg>
<figcaption>Schematic only, not the sunspot data itself: a recursion with roots on the unit circle
(Model One / the Yule model) forecasts an oscillation that never decays; a recursion with roots
strictly inside it (AR(2), once its second-lag coefficient is freed from $-1$) forecasts an
oscillation that dies out to a constant.</figcaption>
</figure>

The lecture's reading of why the flatter forecast nonetheless wins on this test span: the sunspot
cycle is only *nearly* periodic — its length varies from cycle to cycle — so a model committed to
one exact frequency risks drifting out of phase with the actual data over a long forecast horizon,
and being out of phase can be worse than predicting nothing at all. A model whose forecast settles
to a constant cannot be wrong by more than roughly one cycle's amplitude, and here that turns out to
beat both sinusoid-shaped models. The caveat given alongside the result is worth keeping: this
ranking is a property of this particular training/test split, and is expected to change under a
different split.

## Comparing the three models

| Model | Recursion / formula | What is estimated | Test RMSE |
| --- | --- | --- | --- |
| One: sinusoid | $y_t = \beta_0+\beta_1\cos(2\pi ft)+\beta_2\sin(2\pi ft)+\epsilon_t$ | $\beta_0,\beta_1,\beta_2$ by OLS, $f$ by grid search | 79.84 |
| Two: Yule | $y_t=\alpha_0+\alpha_1y_{t-1}-y_{t-2}+\epsilon_t$ | $\alpha_0,\alpha_1$ by OLS (lag-2 coefficient fixed at $-1$) | 79.53 |
| Three: AR(2) | $y_t=\phi_0+\phi_1y_{t-1}+\phi_2y_{t-2}+\epsilon_t$ | $\phi_0,\phi_1,\phi_2$ all by OLS | 70.32 |

Moving down the table relaxes one restriction at a time — first freeing the frequency estimate from
a single nonlinear search into a linear one (One to Two), then freeing the pinned $-1$ coefficient
itself (Two to Three) — and, on this split, prediction accuracy improves each time, even as the
forecasts stop looking like a sinusoid at all.

## Sources

- All content is from three sections of the same course notebook, *berkeley-stat153*, fall 2025
  (`CodeLabEight153248Fall2025.ipynb`, CC BY 4.0): "Model One: Sinusoid Model", "Model Two: The Yule
  Model", and "Model Three: AR(2)".
- The notebook's own introductory section — where the sunspot series, the train/test split, and the
  variables used throughout (training values, test times, held-out test values) are set up — is not
  part of the supplied material for this chapter and is not reproduced here.
- The sinusoid regression model and the profile-least-squares frequency search (Model One) are
  described in the notes as covered "way back in Lectures 5-8"; that treatment is not part of this
  material.
- The equivalence between a sinusoid and the second-order linear recursion used in Model Two is
  stated in the notes as "discussed with proof in Lecture 16"; the proof itself is not part of this
  material and is not reproduced here.
- Each of the three sections referenced one plot (training data, test data, and forecasts plotted
  together) that was omitted from the supplied notes ("1 figure omitted — see the original
  notebook"); the diagram above is a schematic illustration of the roots-on/inside-the-unit-circle
  argument stated in the text, not a reproduction of those plots.

---

[← 24. Gated RNNs: LSTMs and GRUs](24-gated-rnns-lstms-and-grus.md) · [Contents](index.md) · [27. AR Fitting: AutoReg vs ARIMA →](27-ar-fitting-autoreg-vs-arima.md)
