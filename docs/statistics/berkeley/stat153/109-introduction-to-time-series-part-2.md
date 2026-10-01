---
title: "109. Introduction to Time Series (part 2)"
course: "Berkeley Stat 153"
chapter: 109
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 109. Introduction to Time Series (part 2)

## What this covers

This is the syllabus lecture for a time series course (STAT 153/STAT 248), delivered entirely as
slides with no accompanying transcript. It does not develop any one method in depth. Instead it
asks what a time series is and what "prediction" means for one, poses the question through a
sequence of "guess the next number" puzzles, and then walks through the seven topics the course
builds toward, each anchored to a real dataset. It assumes only that the reader is comfortable with
ordinary linear regression, since every topic in the roadmap below is introduced as a regression of
$y_t$ on something — time, lagged values of $y_t$ itself, or a nonlinear function learned by a
network.

## What is a time series?

A time series is a set of observations, each one recorded at a specific time. US monthly
population, daily stock prices, annual sunspot counts and quarterly GNP are all examples; sites
such as FRED (fred.stlouisfed.org) and Google Trends archive many more.

Running example: monthly US population from FRED, `POPTHM`, starting January 1959 (values recorded
in thousands, so a reading of 300,000 means 300 million people). Given a series like this, the
questions time series analysis is built to answer are:

- **Prediction**: what is a reasonable estimate of the population at a future date, e.g. January
  2040?
- What is the population's rate of growth?
- Has that growth rate been roughly constant over time?
- Over what period did the population grow fastest? Slowest?

Time series analysis answers such questions by fitting statistical models to the observed data.

## The prediction problem

Prediction — estimating future values of a series from the values already observed — is one of the
central problems the course is organized around. Before touching real data, the lecture warms up
with a set of "what's the next number" puzzles (posed but not solved in the source; see
[Exercises](#exercises)), and then works one all the way through:

> Find the next number: $5, 8, 13, 20, 29, 40, \#$.

The answer is $53$, and the way to arrive at it is to notice that the observed value $y_t$ is a
function of the time index $t$:
$$y_t = t^2 + 4.$$
Checking $t = 1, 2, 3, \dots$ against $5, 8, 13, 20, \dots$ confirms the fit, and plugging in the
next index gives $53$. What was actually done here is a **quadratic regression of $y_t$ on $t$** —
and that reframing is the seed of the entire course: instead of guessing patterns by eye, fit a
regression of the series against time (or against its own past) and let the fitted model do the
extrapolating.

## Topic 1: multiple linear regression

The first technique the course develops is regression of the series on the time variable itself.

- **Simple linear regression** of $y_t$ on $1, t$ fits a single straight line to the whole series.
- **Multiple linear regression** of $y_t$ on $1, t$ together with other functions of $t$ — powers of
  $t$, or sinusoids such as $\cos(\pi t/6)$ and $\sin(\pi t/6)$ — fits richer, still-linear-in-the-
  parameters functions. Adding higher harmonics, $\cos(\pi t/3), \sin(\pi t/3), \cos(\pi t/2),
  \sin(\pi t/2)$, and combining the sinusoids with a quadratic trend, lets the fitted curve track
  both a slow trend and a periodic wiggle at once.

These models already give workable, sometimes reasonable, solutions to the prediction problem. This
is the first topic of the course, covering both the usual frequentist inference for linear
regression and, in more detail than is typical, Bayesian inference for it.

## Topic 2: nonlinear regression

Fitting one global line, or even a global polynomial, to a series like US population is unrealistic:
a single line ignores changes in the growth rate, and a higher-order polynomial, while it can bend
to fit the data, is not interpretable in terms of growth rates and behaves badly away from the data
it was fit to. A more realistic model allows the slope itself to change at a few breakpoints in
time:
$$y_t = \beta_0 + \beta_1 t + \alpha_1 (t - c_1)_+ + \alpha_2 (t - c_2)_+ + \text{error},$$
where $(x)_+ = \max(x, 0)$. Before $c_1$ the series grows at rate $\beta_1$; between $c_1$ and $c_2$
it grows at rate $\beta_1 + \alpha_1$; after $c_2$, at rate $\beta_1 + \alpha_1 + \alpha_2$. This
gives three different growth rates over the series, with each rate directly readable off the
fitted parameters. Because the breakpoints $c_1, c_2$ are themselves parameters to be estimated
(not chosen by eye), fitting $\beta_0, \beta_1, \alpha_1, c_1, \alpha_2, c_2$ is a genuinely
nonlinear regression problem, unlike Topic 1's models.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A piecewise-linear trend with two breakpoints, showing three different slopes">
  <line x1="30" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <text x="320" y="188" text-anchor="end" font-size="12" fill="currentColor">t</text>
  <line x1="150" y1="20" x2="150" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="230" y1="20" x2="230" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="150" y="185" text-anchor="middle" font-size="11" fill="currentColor">c1</text>
  <text x="230" y="185" text-anchor="middle" font-size="11" fill="currentColor">c2</text>
  <polyline points="30,150 150,120 230,55 320,25" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="80" y="128" font-size="11" fill="currentColor">slope β1</text>
  <text x="165" y="80" font-size="11" fill="currentColor">slope β1+α1</text>
  <text x="245" y="35" font-size="11" fill="currentColor">slope β1+α1+α2</text>
</svg>
<figcaption>The changepoint model for population growth: a straight line whose slope resets at each
breakpoint c1, c2, giving three interpretable growth rates instead of one line or one polynomial.</figcaption>
</figure>

A second running example makes the same point differently: the number of sunspots is known to vary
on an approximately 11-year cycle. But why exactly 11, and not 10.5 or 11.5 — and how much
uncertainty is there around that number? To answer this from the data, fit
$$y_t = \beta_0 + \beta_1 \cos(\omega t) + \beta_2 \sin(\omega t) + \text{error},$$
where the frequency $\omega$ is itself an unknown parameter (the period is $2\pi/\omega$). Because
$\omega$ sits inside the cosine and sine, this is again a nonlinear regression model, in contrast to
Topic 1, where the frequencies in the sinusoidal regressors had to be fixed in advance. The lecture
also showed further real series that raise the same trend-fitting question — lynx trapping counts
and the US unemployment rate from FRED — without additional worked detail.

## Topic 3: high-dimensional regression

The changepoint idea from Topic 2 scales awkwardly: fitting
$$y_t = \beta_0 + \beta_1 t + \sum_{j=1}^{k} \alpha_j (t - c_j)_+ + \epsilon$$
with a small number of breakpoints $k$ is usually not flexible enough to capture the underlying
trend, but with $k$ large there is a real risk of overfitting to noise. The resolution is to stop
choosing $k$ by hand: fit the "full" model with one hinge function at every time point,
$$y_t = \beta_0 + \beta_1 t + \beta_2 (t-2)_+ + \beta_3 (t-3)_+ + \cdots + \beta_{n-1}(t-n+1)_+ +
\epsilon,$$
and control overfitting not by limiting the number of breakpoints but by **regularizing** the
coefficients — Ridge and LASSO regularization are the two the course studies. Applied to the
temperature-anomalies dataset, this high-dimensional model with Ridge regularization recovers a
smooth underlying trend with the noise artifacts removed, and comparing two datasets' trends this
way makes their differences much easier to see than looking at the raw series side by side.

## Topic 4: variance modeling and spectral analysis

Every model so far has modeled the *mean* of $y_t$ — a regression model. Topic 4 turns to modeling
the *variance* instead. The running example is daily closing prices $P_t$ of the S&P 500
(2000–2024). Financial analysts work not with the prices directly but with returns,
$$r_t = 100 \times (\log P_t - \log P_{t-1}) \approx 100 \times \frac{P_t - P_{t-1}}{P_{t-1}},$$
i.e. the (approximate) percentage change from one day to the next. To study volatility, the common
model is $r_t \sim N(0, \sigma_t^2)$, with $\sigma_t$ — a proxy for volatility — modeled as a
function of $t$. This is a **variance model**, as distinct from the mean models seen up to this
point.

**Spectral analysis** is the special case of variance modeling where the variance model is applied
not to the data itself but to its Discrete Fourier Transform (DFT) — one of the most important
tools in engineering signal processing, and closely related to the sinusoidal regression from
Topic 2 (the sunspot model above is itself a Fourier-type fit). The course develops Fourier
frequencies, the DFT and the periodogram to make this precise. As an example, comparing EEG spectra
recorded with eyes open versus eyes closed shows a clear difference concentrated around 10 Hz (after
rescaling the frequency axis by a factor of 160) — a pattern the lecture notes is a known result in
cognitive neuroscience.

## Topic 5: lagged regression (ARIMA)

A different puzzle exposes a different kind of structure:

> Find the next number: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \#$.

This is the Fibonacci sequence, $y_t = y_{t-1} + y_{t-2}$, and the next term is $144$. Regressing
$y_t$ on the time index $t$ is useless here — there is no simple function of $t$ alone that
produces this sequence. What works instead is regressing $y_t$ on its own **lagged values**,
$y_{t-1}$ and $y_{t-2}$: **lagged regression**, or **autoregression**.

Autoregression is the core idea behind the ARIMA family — AutoRegressive Integrated Moving Average
models — which are used extensively for real-world time series prediction. The basic move is a
linear regression of $y_t$ on $x_t = (1, y_{t-1}, \dots, y_{t-p})$ for some fixed lag $p \ge 1$.
Two real examples: an AR model fit to FRED's seasonally-adjusted quarterly GNP data, whose forecasts
for the last four years (16 quarters) track the series well; and two different ARIMA models
compared against monthly retail sales for beer, wine and liquor stores.

## Topic 6: vector time series

So far $y_t$ has been a single number at each time. If instead $\mathbf{y}_t$ is a **vector** —
say, unemployment, inflation, GDP growth and the interest rate all recorded together — new
questions become available that a univariate series cannot ask:

- Can inflation be forecast better using its own past *together with* past unemployment, GDP
  growth and interest rates, rather than its own past alone?
- Does a slowdown in economic activity tend to precede a rise in unemployment?
- After interest rates rise, what happens to the other variables?

This is the setting for **vector autoregression (VAR)** models.

## Topic 7: neural networks

Autoregressive models are, at bottom, linear regression of $y_t$ on lagged covariates
$x_t = (1, y_{t-1}, \dots, y_{t-p})$. Two drawbacks come with that: the lag $p$ has to be chosen,
and however well it is chosen, the model's dependence on the past cuts off abruptly at $p$ — nothing
before $y_{t-p}$ can influence the prediction of $y_t$, no matter how relevant it might be. Two
fixes the course studies:

- Nonlinear regression of $y_t$ on the same lagged covariates $x_t$, fit with a single-hidden-layer
  neural network — **nonlinear autoregression**, $y_t = f(x_t) = f(y_{t-1}, \dots, y_{t-p})$.
- Recurrent neural networks (RNNs), which use *all* past values rather than a fixed window:
  $y_t = f_t(x_t, x_{t-1}, \dots, x_1)$. The course covers vanilla RNNs and more elaborate variants —
  LSTMs, GRUs, and possibly transformers.

The value of not having to fix $p$ by hand is illustrated with simulated data generated as
$y_t = y_{t-p} + \epsilon_t$ for $p = 344$ — a very long-range dependence. An AR model given the
correct lag $p$ forecasts it well, unsurprisingly. An LSTM, given no information about the true
value of $p$, produces comparably good forecasts anyway, discovering the long-range dependence
directly from the data.

## The course's seven topics, and how models are fit

Collecting the roadmap:

1. Multiple linear regression
2. Nonlinear regression
3. High-dimensional regression
4. Variance models and spectral analysis
5. ARIMA modeling
6. Vector time series (VAR models)
7. Neural networks

Across all seven, models are fit to a variety of real datasets mostly by likelihood maximization
(sometimes with an added regularization term, as in Topic 3), with Bayesian techniques studied
alongside the frequentist ones, particularly for linear regression in Topic 1.

## Exercises

The lecture opened with the following "guess the next number" puzzles, posed to motivate the idea
that prediction means finding the rule that generated the series so far. None is solved in the
source material.

1. $5, 8, 11, 14, 17, \_$
2. $42, 32, 23, 15, 8, \_$
3. $3, 6, 12, 24, 48, \_$
4. $-3, 7, -6, 11, -9, 15, \_, \_$
5. $4, 16, 36, 64, 100, \_$

## Sources

All material is from a single slide deck, *Lecture One*, STAT 153/STAT 248 (Aditya Guntuboyina,
Fall 2026), UC Berkeley — the first lecture of the course, given as a syllabus/roadmap talk with no
accompanying transcript, problem set, or written notes. The deck was converted from a PDF with no
text layer, so per its own conversion banner the prose is a model's paraphrase and every equation
is unverified against the original slide images; it is split here across three converted files:

- `01-lecture-one.md` — definition of a time series, the US population example and its guiding
  questions, the "next number" puzzles and the worked quadratic example, and Topics 1 and 2
  (multiple linear and nonlinear regression) including the changepoint model.
- `02-annual-sunspots-data.md` — the sunspot periodicity question and its cosine/sine model, Topics
  3–6 (high-dimensional regression, variance modeling and spectral analysis, ARIMA/lagged
  regression via the Fibonacci example, and vector time series), and the opening of Topic 7.
- `03-topic-seven-neural-networks.md` — the rest of Topic 7 (neural networks and RNNs), the
  simulated long-lag example, the consolidated topic list, and the closing remark on how models are
  fit.

Several slides in the deck carry only a title or a plot with no transcribed caption — the Lynx
Trappings and Unemployment Rate slides, the successive sinusoidal-regression plots in Topic 1, the
ARIMA and EEG-spectrum example plots, and the temperature-anomalies and two-dataset trend
comparisons in Topic 3 — and are referenced above only as far as the surrounding text describes
them; the plots themselves are not reproduced here since this chapter was built from text alone.

---

[← 108. Introduction to Time Series (part 1)](108-introduction-to-time-series-part-1.md) · [Contents](index.md) · [110. Introduction to Time Series Analysis →](110-introduction-to-time-series-analysis.md)
