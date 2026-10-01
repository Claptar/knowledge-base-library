---
title: "110. Introduction to Time Series Analysis"
course: "Berkeley Stat 153"
chapter: 110
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 110. Introduction to Time Series Analysis

## What this covers

This is the opening lecture of the course. It asks what a time series is, poses the questions
about the US population series that motivate everything that follows, and previews the six topics
the course builds toward across the term. It assumes only ordinary linear regression — nothing
about time series is assumed yet.

## What is a time series?

A time series is a set of observations, each recorded at a specific time. The running example is
the monthly US population series from FRED (units of thousands, so a reading of 300,000 means 300
million people), plotted as population against calendar time. Four questions about it set the
agenda for the course:

- **Prediction**: what is a reasonable estimate of the population at a future date, e.g. January 2040?
- **Rate of growth**: how fast is the population growing?
- **Stability**: has that growth rate stayed roughly constant over time?
- **Extremes**: over what period did the population grow fastest? Slowest?

Time series analysis answers such questions by fitting statistical models to observed data.

## The basic idea: regressing $Y_t$ on $t$

A toy version of the prediction problem makes the idea concrete. Find the next number in

$$1, \; 4, \; 9, \; 16, \; 25, \; ?$$

The answer is 36, but the reasoning behind it is the point: you notice that the observed value
$Y_t$ at time $t$ is a function of $t$ itself ($Y_t = t^2$), and you use that function to
extrapolate. In regression language this is a **quadratic regression of $Y_t$ on the time variable
$t$**.

This is the first and simplest time series technique: **regression over time**. Simple linear
regression of $Y_t$ on $t$ fits a straight line to the data. Multiple linear regression of $Y_t$ on
$t$ together with other, fixed functions of $t$ — powers of $t$, sinusoids of $t$, and so on — fits
more elaborate curves while still being *linear* regression, because the fitted function is a
linear combination of known basis functions with unknown coefficients.

## Worked example: monthly accidental deaths

The second dataset is monthly totals of accidental deaths in the US, 1973–1978, which shows a
clear yearly pattern. The lecture builds up a model for it one term at a time, each an instance of
regression over time with a fixed, chosen set of basis functions:

1. $Y_t \sim 1, \cos(\pi t/6), \sin(\pi t/6)$. Since $\cos(\omega t)$ has period $2\pi/\omega$,
   here $\omega = \pi/6$ gives a period of $12$ months — one cycle per year. This is the crudest
   possible sinusoidal fit: a single annual wave.
2. Adding $\cos(\pi t/3), \sin(\pi t/3)$ — a second harmonic, period $6$ months — lets the annual
   shape depart from a pure sine wave.
3. Adding a third harmonic, $\cos(\pi t/2), \sin(\pi t/2)$ (period $4$ months), sharpens the fit
   further.
4. Finally, adding a quadratic term in $t$ on top of the sinusoids lets the model capture a slow
   trend across the six years in addition to the within-year seasonal shape.

In every one of these models the frequencies ($\pi/6, \pi/3, \pi/2$) are chosen in advance, fixed
at multiples that divide evenly into a 12-month year. Because of that, each model is still an
ordinary multiple linear regression: linear in all of $\beta_0, \beta_1, \dots$ once the basis
functions are fixed. This case is exactly what the course calls **Topic One: Multiple Linear
Regression** — both the usual frequentist inference and, in more detail, Bayesian inference for
linear regression.

## Nonlinear regression: an unknown breakpoint

Multiple linear regression already gives reasonable-looking fits, but it is not always the right
tool. Return to the US population data: a single straight line across the whole series is clearly
unrealistic, and a quadratic polynomial is not much better — polynomials are also hard to interpret
in terms of growth rates. A more useful model allows the growth rate itself to change at a small
number of unknown times:

$$Y_t = \beta_0 + \beta_1 t + \alpha_1 (t - c_1)_+ + \alpha_2 (t - c_2)_+ + \text{error}$$

where $(x)_+ = \max(x, 0)$ is the positive-part function. Below $c_1$ the slope is $\beta_1$;
between $c_1$ and $c_2$ it is $\beta_1 + \alpha_1$; above $c_2$ it is $\beta_1 + \alpha_1 +
\alpha_2$ — three different growth rates, exactly the kind of thing the "fastest / slowest" question
above is asking about.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="A piecewise-linear curve with two breakpoints, showing three different growth rates">
  <line x1="40" y1="190" x2="350" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="40,170 150,140 260,50 340,35" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="150" y1="190" x2="150" y2="140" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="260" y1="190" x2="260" y2="50" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="150" y="205" text-anchor="middle" font-size="12" fill="currentColor">c1</text>
  <text x="260" y="205" text-anchor="middle" font-size="12" fill="currentColor">c2</text>
  <text x="352" y="196" text-anchor="start" font-size="12" fill="currentColor">t</text>
  <text x="34" y="20" text-anchor="end" font-size="12" fill="currentColor">Y_t</text>
  <text x="90" y="148" text-anchor="middle" font-size="11" fill="currentColor">slope β1</text>
  <text x="205" y="85" text-anchor="middle" font-size="11" fill="currentColor">slope β1+α1 (fastest)</text>
  <text x="300" y="20" text-anchor="middle" font-size="11" fill="currentColor">slope β1+α1+α2 (slowest)</text>
</svg>
<figcaption>The piecewise-linear population model: the growth rate is constant on each of three
segments and changes only at the breakpoints c1 and c2.</figcaption>
</figure>

The parameters are $\beta_0, \beta_1, \alpha_1, c_1, \alpha_2, c_2$. For *fixed* $c_1, c_2$ the
model is linear in the $\beta$'s and $\alpha$'s — but $c_1$ and $c_2$ are themselves unknown
parameters to be estimated, and they enter the fitted curve nonlinearly (they determine *where* the
line bends, not just the size of a coefficient). That is what makes this a **nonlinear regression
model**, despite every individual segment being a straight line. This is **Topic Two: Nonlinear
Regression**.

## Nonlinear regression again: an unknown frequency

The sunspot dataset gives a second instance of the same pattern. Sunspots are temporary dark
patches on the Sun's surface, tied to concentrations of magnetic flux, and their number is known to
rise and fall on an approximately 11-year cycle. That raises a genuinely statistical question: why
11, exactly? Why not $10.5$ or $11.5$? What is the uncertainty around that number, and can the
period be recovered from the data itself rather than taken on authority? One way to answer this is
to fit

$$Y_t = \beta_0 + \beta_1 \cos(\omega t) + \beta_2 \sin(\omega t) + \text{error}$$

This looks like the sinusoidal terms used for the accidental-deaths data, but there is a crucial
difference: there, the frequencies were fixed in advance (multiples of $\pi/6$, chosen to match a
known 12-month year); here $\omega$ itself is an unknown parameter to be estimated from the data,
because the whole point is to find the period rather than assume it. As with the breakpoints
$c_1, c_2$ above, fixing $\omega$ makes the model linear in $\beta_1, \beta_2$, but $\omega$ enters
the fit nonlinearly — so this, too, is a nonlinear regression model, with parameters $\beta_0,
\beta_1, \beta_2, \omega$.

## Topic Three: high-dimensional regression

It is tempting to skip the question of *where* the breakpoints go by simply putting one at every
time point:

$$Y_t = \beta_0 + \beta_1 t + \beta_2 (t-2)_+ + \beta_3(t-3)_+ + \dots + \beta_n(t-n)_+ + \epsilon$$

This is the same construction as the population model above, taken to its extreme: instead of
choosing two breakpoints $c_1, c_2$ and estimating their locations nonlinearly, it allows a
different growth rate between *every* consecutive pair of time points, with the breakpoint
locations fixed at $2, 3, \dots, n$. The trade-off is that the model is now linear again — but with
roughly as many coefficients as observations. Fitting it sensibly requires **regularization**;
Ridge and LASSO regularization are the two the course studies. As an illustration, the lecture
fits this model with Ridge regularization to Google Trends search-interest data for the term
"yahoo".

## Topic Four: variance modeling

Everything so far models the *mean* of $Y_t$ as a function of time or of other basis functions.
Some questions are instead about the *variance*. The example is daily Apple (AAPL) stock prices
and their returns: financial analysts care about the volatility of returns, not just their average
level. A common model is $Y_t \sim N(0, \sigma_t^2)$, treating $\sigma_t$ — modeled as a function
of $t$ — as a proxy for volatility. These are variance models, as opposed to the mean (regression)
models seen so far. **Spectral analysis** is a related idea: it converts the observed series to the
Fourier basis and then applies a variance model to the resulting coefficients.

## Topic Five: lagged regression (ARIMA)

A second toy prediction problem shows the limits of regression over time. Find the next number in

$$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \; ?$$

This is the Fibonacci sequence, $Y_t = Y_{t-1} + Y_{t-2}$, and the next term is $144$. Regression
over the time index $t$ is no help here — the value of $Y_t$ is not a smooth or periodic function
of $t$ at all. Instead, $Y_t$ must be regressed on its own recent past, $Y_{t-1}$ and $Y_{t-2}$.
This is **lagged regression**, or **autoregression**, and it is the central idea behind the ARIMA
class of models — AutoRegressive Integrated Moving Average — which are widely used for prediction
and are the subject of Topic Five.

## Topic Six: recurrent neural networks

Recurrent Neural Networks (RNNs) are formulated as regression on pairs $(x_t, y_t)$, $t = 1,
\dots, n$: at each time point there is both a response $y_t$ and a covariate vector $x_t$. Ordinary
regression models $y_t = f(x_t)$ — the response depends only on the current covariate. RNNs instead
allow $y_t = f_t(x_t, x_{t-1}, \dots, x_1)$, so the response can depend on the entire history of
covariates. The course covers these models, including LSTMs, and some of their applications.

## The six topics, and the shape of the term

| Topic | Idea |
| --- | --- |
| One: Multiple linear regression | fixed basis functions of $t$; frequentist and Bayesian inference |
| Two: Nonlinear regression | basis functions with unknown parameters that enter nonlinearly (breakpoints, frequencies) |
| Three: High-dimensional regression | as many parameters as data points; Ridge and LASSO |
| Four: Variance modeling and spectral analysis | modeling $\sigma_t$, not the mean |
| Five: ARIMA | regression on the series' own lagged values |
| Six: Recurrent neural networks | response depends on the whole covariate history |

The lecture also showed, without further comment, plots of two more series to illustrate the range
the course draws examples from: annual lynx trappings in Canada (1821–1934) and the US unemployment
rate (from FRED).

## Different kinds of time series data

The course will mostly work with the first of these four, but it is worth distinguishing them from
the start:

- **Univariate time series**: $y_1, \dots, y_T$, each $y_t$ a real number. The simplest case, and
  the main object of study in this course.
- **Vector time series**: $y_1, \dots, y_T$, each $y_t$ vector-valued — for example $y_t =
  (y_{t1}, y_{t2})^T$ where $y_{t1}$ is the unemployment rate and $y_{t2}$ is GDP growth for
  quarter $t$, giving a bivariate series. When the dimension is large these are called
  high-dimensional time series. The course will not spend much time here.
- **Time series regression**: pairs $(x_1, y_1), \dots, (x_T, y_T)$, each $x_t$ a vector of
  covariates and $y_t$ a real response, with the goal of predicting $y_{T+1}$ from $x_{T+1}$ and
  the data so far. This setting is more general than both regression over time ($x_t = t$) and
  lagged regression ($x_t = (y_{t-1}, \dots, y_{t-p})$), and it is the setting in which RNNs are
  studied.
- **Sequential data**: in the machine-learning sense, pairs $(x_i, y_i)$, $i = 1, \dots, n$, where
  each $x_i$ and/or $y_i$ is itself a time series, typically with no dependence across different
  $i$. Example: classifying a review as positive or not, where $x_i$ is the $i$-th review (a
  sequence of words, viewable as a time series) and $y_i$ is binary. RNNs are heavily used here
  too.

## Sources

Both files are Berkeley STAT 153/248, Spring 2025 ("Time Series"), Lecture One, taught by Aditya
Guntuboyina (21 January 2025), reconstructed by a model from a slide PDF with no text layer
(`LectureOneSlides153248Spring2025PDF.pdf`, CC BY 4.0). No transcript, problem set, or separate
lecture notes were supplied for this lecture, and none of the plots embedded in the original slides
survived conversion — they are noted here only as descriptions.

- `01-lecture-one.md` — what a time series is, the US population questions, the toy quadratic
  and Fibonacci prediction problems, the accidental-deaths sinusoidal build-up, and the
  piecewise-linear population model.
- `02-sunspot.md` — background on sunspots (attributed there to Wikipedia), the periodicity
  question and its nonlinear-frequency model, the six-topic overview (high-dimensional
  regression, variance modeling, ARIMA, RNNs), and the taxonomy of univariate / vector / time
  series regression / sequential data.

Because the source PDF had no extractable text, both files carry a fidelity warning that the prose
is a paraphrase in places and that every equation is unverified; the equations reproduced above
should be checked against the original slides before being relied on for anything beyond the
narrative of this lecture.

---

[← 109. Introduction to Time Series (part 2)](109-introduction-to-time-series-part-2.md) · [Contents](index.md) · [111. The Sinusoidal Model →](111-the-sinusoidal-model.md)
