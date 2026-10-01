---
title: "83. Long-Range ARIMA and Cross-Validation"
course: "Berkeley Stat 153"
chapter: 83
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 83. Long-Range ARIMA and Cross-Validation

## What this covers

This chapter works through the ideas behind Homework 4 of Stat 153: the algebra that lets the
factors of a SARIMA model be written in either order, what repeated differencing does to
polynomial trends in $t$ and hence to the long-run forecasts of an ARIMA model, and how the R
package `fable` automates time series cross-validation through a function called
`stretch_tsibble()`. It assumes the backshift/SARIMA notation, the ARMA forecast recursion, and
the manual time-series-CV loop already built in lecture — none of those derivations are repeated
here, only the notation and definitions needed to read the exercises.

## The backshift operator and operator polynomials

Write $B$ for the backshift operator, $Bx_t = x_{t-1}$, and $B^k x_t = x_{t-k}$ for $k \ge 0$
applications of it. An AR or MA factor is a polynomial in $B$, such as
$$
\phi(B) = 1 - \phi_1 B - \cdots - \phi_p B^p, \qquad \theta(B) = 1 + \theta_1 B + \cdots + \theta_q B^q,
$$
and a seasonal factor is the same kind of polynomial written in the seasonal lag $B^s$, e.g.
$\Phi(B^s)$ and $\Theta(B^s)$ for period $s$. The **difference operator** $\nabla = 1 - B$ removes
a linear trend, $\nabla x_t = x_t - x_{t-1}$, and its seasonal counterpart is $\nabla_s = 1 - B^s$.
A general SARIMA model is written by stacking all four kinds of factor around $x_t$:
$$
\phi(B)\,\Phi(B^s)\,\nabla^d \nabla_s^D\, x_t = \theta(B)\,\Theta(B^s)\, w_t .
$$

Because $\phi(B)$, $\Phi(B^s)$, $\nabla^d$ and $\nabla_s^D$ are all just polynomials built out of
powers of the *same* operator $B$, multiplying them together behaves exactly like multiplying
ordinary polynomials in a scalar variable — and that multiplication is commutative. This is why
the SARIMA equation above can equally be written with the seasonal and non-seasonal factors
swapped, or with the differencing operators moved to the front; Q1–Q4 below ask you to make this
precise, first for two arbitrary powers of $B$, then for two arbitrary polynomials in $B$, and
finally as a statement about SARIMA notation itself.

## Differencing and polynomial trends

Ordinary differencing interacts with polynomial trends in a specific way: if $x_t$ is a
(deterministic) polynomial in $t$ of degree $k$, then $\nabla x_t$ is a polynomial of degree
$k-1$, and $\nabla^k x_t$ is constant. Q5–Q8 study the *converse* direction, which is really what
matters for forecasting: starting only from a statement about $\nabla x_t$ or $\nabla^2 x_t$ (that
it equals a constant, or a linear function of $t$), they ask you to prove that $x_t$ itself must be
a polynomial of the corresponding degree. This is the fact that underlies why an ARIMA$(p,d,q)$
model — which models $\nabla^d x_t$ as a stationary ARMA process — can produce forecasts that look
like a polynomial trend of degree related to $d$, even though nothing in the model was written
down as a trend explicitly.

## Long-run forecasts of ARMA and ARIMA models

For a stationary and invertible ARMA model, the $h$-step-ahead forecast $\hat x_{t+h\mid t}$ is
built by iterating the model equation forward from time $t$: at each future step, an unobserved
noise term $w_{t+j}$ ($j>0$) is replaced by its conditional mean of zero, and an unobserved
$x_{t+j}$ is replaced by its own forecast, computed recursively from the same equation. For an
ARMA(1,1) model
$$
(1-\phi B)x_t = (1+\theta B) w_t,
$$
with $|\hat\phi|<1$, unraveling this recursion for a growing horizon $h$ shows what happens to the
forecast as $h \to \infty$ (Q9 below); adding a nonzero intercept $c$ changes the limit but not the
fact that it converges (Q10). Q11 asks you to combine this with the polynomial-trend facts from the
previous section: once the AR/MA part of an ARIMA$(1,d,1)$ model is written in terms of
$\nabla^d x_t$, the same "$\nabla^d x_t \to$ polynomial in $t$" correspondence tells you what shape
the long-run forecast $\hat x_{t+h\mid t}$ approaches, depending on whether $c=0$ and on whether
$d=1$ or $d=2$. (The forecast-iteration procedure itself was worked out in lecture; it is used
here, not re-derived.)

## Time series cross-validation with `fable`

Lecture built time series cross-validation "by hand": loop over time, refit a model at each step,
forecast one step ahead, and score it. The R package `fable`, working on data stored as a
`tsibble` (a data frame with a declared time index), automates the bookkeeping with a function
called `stretch_tsibble()`. Given an initial window length `.init`, it takes an $n$-row tsibble and
produces an expanding sequence of windows, each tagged with its own `.id`: `.id = 1` is the first
`.init` rows, `.id = 2` appends one more row, `.id = 3` appends another, and so on, up to the full
series.

<figure>
<svg viewBox="0 0 380 190" role="img" aria-label="Expanding windows produced by stretch_tsibble, each followed by a one-step forecast">
  <defs>
    <marker id="arrow83" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <text x="10" y="30" font-size="12" fill="currentColor">.id = 1</text>
  <circle cx="60" cy="26" r="4" fill="currentColor"/>
  <circle cx="88" cy="26" r="4" fill="currentColor"/>
  <circle cx="116" cy="26" r="4" fill="currentColor"/>
  <line x1="120" y1="26" x2="140" y2="26" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arrow83)"/>
  <circle cx="144" cy="26" r="4" fill="none" stroke="currentColor" stroke-width="1.2"/>

  <text x="10" y="80" font-size="12" fill="currentColor">.id = 2</text>
  <circle cx="60" cy="76" r="4" fill="currentColor"/>
  <circle cx="88" cy="76" r="4" fill="currentColor"/>
  <circle cx="116" cy="76" r="4" fill="currentColor"/>
  <circle cx="144" cy="76" r="4" fill="currentColor"/>
  <line x1="148" y1="76" x2="168" y2="76" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arrow83)"/>
  <circle cx="172" cy="76" r="4" fill="none" stroke="currentColor" stroke-width="1.2"/>

  <text x="10" y="130" font-size="12" fill="currentColor">.id = 3</text>
  <circle cx="60" cy="126" r="4" fill="currentColor"/>
  <circle cx="88" cy="126" r="4" fill="currentColor"/>
  <circle cx="116" cy="126" r="4" fill="currentColor"/>
  <circle cx="144" cy="126" r="4" fill="currentColor"/>
  <circle cx="172" cy="126" r="4" fill="currentColor"/>
  <line x1="176" y1="126" x2="196" y2="126" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arrow83)"/>
  <circle cx="200" cy="126" r="4" fill="none" stroke="currentColor" stroke-width="1.2"/>

  <text x="60" y="160" font-size="12" fill="currentColor">...</text>
  <line x1="50" y1="175" x2="330" y2="175" stroke="currentColor" stroke-width="1"/>
  <text x="190" y="188" font-size="12" text-anchor="middle" fill="currentColor">time</text>
</svg>
<figcaption>Each stretch adds one more observation to the training window (filled points) and
leaves the next observation (open circle) to be forecast; fitting a model to every `.id` and
forecasting at horizon `h = 1` reproduces one-step-ahead time series CV.</figcaption>
</figure>

Fitting a model with `model()` on the stretched tsibble fits a separate model to each `.id`
automatically, and `forecast(h = 1)` produces the one-step-ahead forecast for each window — which
are exactly the forecasts a manual time-series-CV loop would produce. The `.mean` column of the
result holds the point forecasts, and the `accuracy()` function joins these back to the true
values and computes error metrics such as MAE directly, without the analyst writing the alignment
code by hand.

Q12–Q13 below ask you to check this workflow against the manual version: how many rows the
stretched tsibble has as a function of $n$ and the burn-in $t_0$, and that the MAE it reports for a
simple random-walk-with-drift forecaster matches a manual time-series-CV loop on the same data.
Q14–Q16 then use the same machinery — extended to horizons $h = 1,\dots,12$ rather than just
$h=1$ — to compare four ARIMA/SARIMA specifications on the `leisure` employment series from the
*Forecasting: Principles and Practice* book, by their cross-validated MAE.

## Exercises

Points shown are out of the homework's total of 34; the problems marked *(Bonus)* can offset lost
points elsewhere but do not raise the total above full credit.

**Backshift commuting**

1. *(1 pt)* Let $B$ denote the backshift operator. Given any integers $k,\ell \ge 0$, explain why
   $B^k B^\ell = B^\ell B^k$.
2. *(2 pts)* Using Q1, if $\phi_1,\dots,\phi_k$ and $\varphi_1,\dots,\varphi_\ell$ are any
   coefficients, show that
   $$
   (1 + \phi_1 B + \cdots + \phi_k B^k)(1 + \varphi_1 B + \cdots + \varphi_\ell B^\ell) =
   (1 + \varphi_1 B + \cdots + \varphi_\ell B^\ell)(1 + \phi_1 B + \cdots + \phi_k B^k).
   $$
3. *(2 pts)* Verify the result in Q2 with a small code example.
4. *(3 pts)* Using Q2, show that a SARIMA model can equivalently be written as
   $$
   \phi(B)\,\Phi(B^s)\,\nabla^d \nabla_s^D\, x_t = \theta(B)\,\Theta(B^s)\, w_t
   $$
   and as
   $$
   \Phi(B^s)\,\phi(B)\,\nabla_s^D \nabla^d\, x_t = \Theta(B^s)\,\theta(B)\, w_t.
   $$

**Long-range ARIMA**

5. *(1 pt)* Let $\nabla = 1-B$. Suppose $\nabla x_t = 0$ for all $t$. Prove that $x_t$ must be a
   constant sequence.
6. *(2 pts)* Suppose $\nabla x_t = u$ for all $t$, for an arbitrary constant $u$. Prove that $x_t$
   must be a linear function of $t$, of the form $x_t = a + bt$.
7. *(3 pts)* Suppose $\nabla x_t = u + vt$ for all $t$, for arbitrary constants $u,v$. Prove that
   $x_t$ must be a quadratic function of $t$, of the form $x_t = a + bt + ct^2$.
8. *(1 pt)* Using Q6 and Q7, prove that if $\nabla^2 x_t = u$ for a constant $u$, then $x_t$ must
   be a quadratic function of $t$.
9. *(4 pts)* Consider an ARMA(1,1) model $(1-\phi B) x_t = (1+\theta B) w_t$, and suppose the
   fitted coefficients pass the unit-root test, $|\hat\phi|,|\hat\theta| < 1$ (assume this
   throughout). Unravel the forecast iteration from lecture to show that $\hat x_{t+h\mid t} \to 0$
   as $h \to \infty$.
10. *(2 pts)* Consider the same model with an intercept, $(1-\phi B)x_t = c + (1+\theta B)w_t$.
    Unravel the forecast iteration to show that $\hat x_{t+h\mid t}$ approaches a nonzero constant
    as $h \to \infty$.
11. *(Bonus)* Now consider the extension to ARIMA$(1,d,1)$,
    $$
    (1-\phi B)\nabla^d x_t = c + (1+\theta B) w_t.
    $$
    Use Q5–Q10 to argue that:
    - if $c=0$ and $d=1$, then $\hat x_{t+h\mid t}$ approaches a constant as $h \to \infty$;
    - if $c=0$ and $d=2$, then $\hat x_{t+h\mid t}$ approaches a linear trend as $h \to \infty$;
    - if $c \neq 0$ and $d=1$, then $\hat x_{t+h\mid t}$ approaches a linear trend as $h \to \infty$;
    - if $c \neq 0$ and $d=2$, then $\hat x_{t+h\mid t}$ approaches a quadratic trend as $h \to \infty$.

**Time series CV**

12. *(3 pts)* A clear advantage of the `stretch_tsibble()` workflow is convenience, at the cost of
    memory: for a series with $n$ observations and burn-in $t_0$ stored as a tsibble `x`, running
    `stretch_tsibble(x, .init = t0)` produces how many rows in total? Derive an explicit formula in
    $n$ and $t_0$, then check it against a couple of code examples.
13. *(4 pts)* Show that the MAE reported by `accuracy()` for the random-walk-with-drift forecaster
    on the example series `dat` matches the MAE from a manual time-series-CV implementation of the
    same forecaster (you may build on code from the regression lecture or earlier homeworks).
14. *(6 pts)* Using the `leisure` employment series (prepared from `us_employment` as in the ARIMA
    lecture), run time series CV via `stretch_tsibble()`, `model()` and `forecast()`, with burn-in
    `.init = 50`, over forecast horizons $h = 1,\dots,12$, for the four models
    - ARIMA$(2,1,0)$,
    - ARIMA$(0,1,2)$,
    - ARIMA$(2,1,0)(1,1,0)_{12}$,
    - ARIMA$(0,1,2)(0,1,1)_{12}$.

    For each model, average the MAE over all twelve horizons, report the results, and rank the
    models.
15. *(Bonus)* Break the MAE from Q14 down by forecast horizon: for each $h=1,\dots,12$, compute the
    MAE of the $h$-step-ahead forecasts made by each model, and plot MAE against $h$. Compare in
    particular the two seasonal models, ARIMA$(2,1,0)(1,1,0)_{12}$ and ARIMA$(0,1,2)(0,1,1)_{12}$ —
    does anything interesting happen to their relative MAE as $h$ varies?
16. *(Bonus²)* Run the same time-series-CV pipeline with auto-ARIMA in place of a fixed
    specification (auto-ARIMA is refit at every CV iteration, so this may take a long time to run).
    If it finishes, how does its MAE compare to the four models in Q14?

## Sources

All material is from the converted homework file `homeworks/homework4/homework4.Rmd`
(berkeley-stat153, fall 2024, CC BY 4.0), split into three parts in the library:

- backshift/SARIMA notation and Q1–4: `01-introduction.md`;
- differencing and the ARMA/ARIMA forecast questions Q5–11: `02-long-range-arima.md`;
- the `tsibble`/`fable`/`stretch_tsibble()` exposition and Q12–16: `03-time-series-cv.md`.

No slide deck or lecture transcript was supplied for this item — only the homework text. The
homework explicitly refers to, but does not itself contain: the forecast-iteration recursion for
ARMA models (used in Q9–Q11, described in the source as "the forecast iteration described in
lecture"); the manual time-series-CV loop built "in lecture (weeks 3–4, Linear regression and
prediction)" and reused in earlier homeworks (Q13); and the exploratory analysis of the `leisure`
data set done in "the ARIMA lecture" that motivates the four model choices in Q14. Those
derivations are assumed background here, not reconstructed.

---

[← 82. Homework 3](82-homework-3.md) · [Contents](index.md) · [84. Evaluating Covid-19 Death Forecasts →](84-evaluating-covid-19-death-forecasts.md)
