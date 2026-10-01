---
title: "97. High-dimensional regression for change-points"
course: "Berkeley Stat 153"
chapter: 97
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 97. High-dimensional regression for change-points

## What this covers

A signal that is flat except for a handful of sudden jumps — a change-point signal — can be
estimated by ordinary linear regression, if the design matrix is built to match the shape of the
signal rather than a generic smooth trend. This chapter works through that idea on a simulated
example: it builds the right design matrix for a piecewise-constant signal, shows that the
unregularized fit is useless (it just reproduces the data), and then uses ridge and lasso penalties
— tuned by cross-validation — to recover the signal. It closes by using the *wrong* design matrix
(the one built for a smoothly changing trend) on the same data, to see concretely what basis
mismatch costs. It assumes the reader already has ordinary least squares, ridge and lasso
regression, and $k$-fold cross-validation.

## The problem: a signal with jumps, not slopes

The running example is a synthetic signal built from a function called `blocks`: it is constant
everywhere except at eleven points, where it jumps up or down by a fixed amount. Sampling it at
$n = 2048$ points and adding independent Gaussian noise ($\sigma = 5$) gives a dataset $y_1,
\dots, y_n$ in which the underlying signal is piecewise constant, and the only unknowns are *where*
the jumps are and how large they are — not a smooth trend.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A piecewise-constant signal with a few jumps, observed with noise">
  <line x1="20" y1="180" x2="320" y2="180" stroke="currentColor" stroke-width="1"/>
  <text x="325" y="184" font-size="12" fill="currentColor">t</text>
  <line x1="20" y1="180" x2="20" y2="20" stroke="currentColor" stroke-width="1"/>
  <text x="10" y="20" font-size="12" fill="currentColor">y</text>

  <line x1="20" y1="150" x2="90" y2="150" stroke="currentColor" stroke-width="2"/>
  <line x1="90" y1="90" x2="170" y2="90" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="130" x2="230" y2="130" stroke="currentColor" stroke-width="2"/>
  <line x1="230" y1="60" x2="310" y2="60" stroke="currentColor" stroke-width="2"/>

  <line x1="90" y1="150" x2="90" y2="90" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="170" y1="90" x2="170" y2="130" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="230" y1="130" x2="230" y2="60" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>

  <circle cx="35" cy="145" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="55" cy="158" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="75" cy="147" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="105" cy="96" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="130" cy="83" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="150" cy="94" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="185" cy="136" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="210" cy="124" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="245" cy="55" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="270" cy="66" r="2" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="295" cy="58" r="2" fill="currentColor" fill-opacity="0.5"/>

  <text x="170" y="198" text-anchor="middle" font-size="12" fill="currentColor">signal is constant between a few unknown jump points</text>
</svg>
<figcaption>The kind of signal the lab works with: flat segments joined by sharp jumps, observed
through noise. The dots sketch the noisy observations scattered around each flat segment.</figcaption>
</figure>

## A design matrix built for jumps

The natural model for such a signal uses indicator functions rather than a slope: let each
coefficient turn a jump on from some time onward,

$$
y_t = \beta_0 + \beta_1 I\{t \geq 2\} + \beta_2 I\{t \geq 3\} + \cdots + \beta_{n-1} I\{t \geq n\}
+ \epsilon_t .
$$

Written as $y = X\beta + \epsilon$, $X$ is the $n \times n$ lower-triangular matrix of ones: row $t$
has a $1$ in every column up to and including column $t-1$ and zeros after. In `numpy` this is just
`X = np.tril(np.ones((n, n)))`. The lab is explicit that this is a deliberate departure from a model
used earlier in the course that used ReLU functions $(t-c)_+$ instead of indicators — the indicator
basis is the one that matches a signal that jumps, rather than one whose *slope* changes (see
below).

### The unregularized fit is just differencing

Because $X$ is $n\times n$ and lower-triangular with ones on the diagonal, it is invertible, and
with $n$ parameters fit to $n$ observations, ordinary least squares does not average anything away —
it solves $X\beta = y$ exactly. Reading the system row by row makes the solution obvious. Row $t$
says
$$
y_t = \beta_0 + \beta_1 + \cdots + \beta_{t-1},
$$
so $y_t$ is a partial sum of the $\beta$'s. Subtracting consecutive rows undoes the sum:
$$
y_t - y_{t-1} = \beta_{t-1} .
$$
Together with the first row, $y_1 = \beta_0$, this gives the closed form
$$
\hat\beta_0 = y_1, \qquad \hat\beta_t = y_{t+1} - y_t \quad (t = 1, \dots, n-1).
$$
The lab verifies this numerically: `sm.OLS(y, X).fit().params` matches `y[0]` followed by
`np.diff(y)` exactly. The unregularized "fit" is therefore worthless as an estimate of the signal —
it has as many parameters as data points, so it reproduces every noise fluctuation as a "jump."
This is the reason the model needs regularization at all: with $n$ coefficients for $n$ points, the
saturated model has zero bias and enormous variance.

## Ridge and lasso on the jump coefficients

Only the jump coefficients $\beta_1, \dots, \beta_{n-1}$ are penalized — $\beta_0$ is the baseline
level and is left alone. The ridge estimator minimizes
$$
\sum_{t=1}^n \Big(y_t - \beta_0 - \beta_1 I\{t\geq2\} - \cdots - \beta_{n-1} I\{t\geq n\}\Big)^2
+ \lambda \sum_{t=1}^{n-1} \beta_t^2 ,
$$
and the lasso estimator minimizes the same squared error plus $\lambda \sum_{t=1}^{n-1}
|\beta_t|$. Both are solved directly as convex programs (`cvxpy`), with `penalty_start = 1` marking
that the sum starts at $\beta_1$, not $\beta_0$.

Since the unregularized $\hat\beta_t$ for $t \geq 1$ is exactly the increment $y_{t+1}-y_t$, the
penalty on $\beta_1,\dots,\beta_{n-1}$ is really a penalty on how much the fitted level is allowed
to move from one step to the next. That is what separates the two penalties in this problem:

- **Ridge** (squared penalty) shrinks every increment a little, but essentially never sets one to
  exactly zero. The fitted curve keeps drifting between the true jumps — it is smoother than the raw
  data, but still wiggly on the segments that should be flat.
- **Lasso** ($\ell_1$ penalty) drives *most* increments to exactly zero and lets only a few survive
  as real jumps. The fit is genuinely piecewise constant.

Because the true signal is piecewise constant, lasso's bias — toward a small number of exact jumps
— matches the truth, while ridge's bias — toward many small changes — does not. The lab's own
conclusion: "the LASSO fit is piecewise constant while the ridge fit is smoother... Since the true
function is also piecewise constant, LASSO gives better estimates in this problem compared to ridge
regression."

## Picking $\lambda$ by cross-validation

Both penalties need a tuning parameter, chosen here by 5-fold cross-validation. The folds are built
by taking every fifth time index together (fold $i$ is $\{i, i+5, i+10, \dots\}$), rather than five
contiguous blocks of the series. For each candidate $\lambda$, the model is fit on four folds and
evaluated by squared error on the held-out fifth, summed over all five splits.

Over the candidate grid $\lambda \in \{0.1, 1, 10, 10^2, 10^3, 10^4, 10^5\}$, both curves are
U-shaped:

| $\lambda$ | Ridge CV error | Lasso CV error |
|---:|---:|---:|
| 0.1 | 35.02 | 36.68 |
| 1 | 30.60 | 35.47 |
| 10 | **28.13** | 29.13 |
| 100 | 29.27 | **27.15** |
| 1,000 | 36.34 | 45.61 |
| 10,000 | 48.46 | 76.96 |
| 100,000 | 66.79 | 76.96 |

Cross-validation picks $\lambda = 10$ for ridge and $\lambda = 100$ for lasso. Even at its own
optimum, the ridge fit is a compromise: small enough to pick up the real jumps, but "the estimate
will be too wiggly in the constant parts," because no single $\lambda$ can be both small enough to
resolve a sharp jump and large enough to flatten a constant run when every increment is penalized
the same smooth way. Lasso's CV-optimal fit does not face that trade-off in the same way, because
it can set a coefficient to exactly zero instead of merely shrinking it.

## What the wrong basis costs

The lab then asks what happens if the model used earlier in the course — built from an intercept, a
linear trend, and ReLU functions $(t-c)_+$ for every candidate breakpoint $c$ — is applied to this
same change-point data:
$$
X_{\text{full}} = \big[\, \mathbf 1,\; (t-1),\; (t-2)_+,\; (t-3)_+,\; \dots \,\big].
$$
That basis is built for a signal whose *slope* changes at unknown points but which stays
continuous — a piecewise-linear trend — which is why, in the earlier model, `penalty_start = 2`:
the intercept and the linear term are left unpenalized as the baseline, and only the kink terms are
penalized. Fit with lasso at $\lambda = 100$, the result is too wiggly on the flat segments; raising
the penalty to $\lambda = 1000$ smooths the wiggle but also blunts the jumps, because a sum of
continuous ReLU functions cannot produce a true discontinuity — it can only approximate one with a
steep short ramp, and a large penalty flattens the ramp along with everything else. Neither setting
recovers the sharp jumps the indicator-basis lasso found: no choice of $\lambda$ fixes a basis that
cannot represent the shape of the signal. The choice of design matrix — indicators for jumps, ReLUs
for a changing slope — has to match the assumed structure of the signal before regularization can
do useful work.

## Sources

- Lab notebook: `docs/statistics/berkeley/stat153/spring-2025/Lab6.md` (converted from
  `Lab6.ipynb`, Berkeley STAT 153, Spring 2025, CC BY 4.0) — the entire chapter, including the
  `blocks` signal and its simulation, the indicator design matrix and the OLS-as-differencing
  derivation, the ridge/lasso objectives and `cvxpy` solvers, the 5-fold cross-validation routine
  and its numerical output, and the closing ReLU-basis comparison.
- No slide deck, transcript, or separate exercise sheet was supplied for this chapter; nothing in
  those forms was available to merge in.
- The lab refers twice to "the model used in class" — the ReLU/trend-filtering regression with
  `penalty_start = 2` and the general ridge/lasso cross-validation procedure it adapts — as material
  from an earlier lecture in the course. That earlier lecture was not part of the input to this
  chapter, so only what the lab itself reconstructs of it (the `Xfull` design matrix) is described
  here.

---

[← 96. Change-point model](96-change-point-model.md) · [Contents](index.md) · [98. Smoothing the Periodogram (part 2) →](98-smoothing-the-periodogram-part-2.md)
