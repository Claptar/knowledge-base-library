---
title: "108. Introduction to Time Series (part 1)"
course: "Berkeley Stat 153"
chapter: 108
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 108. Introduction to Time Series (part 1)

## What this covers

This is the opening lecture of Stat 153/248 (time series analysis), and it does not develop any
single technique in depth. Instead it lays out the five topics the course will spend its weeks on,
motivating each with a real dataset — US population, monthly accidental deaths, sunspot counts,
lynx trappings, S&P 500 returns, EEG recordings, quarterly GNP — and a question that a simple
linear-regression-on-time model cannot quite answer. It assumes a first course in linear regression
and nothing about time series specifically; the job of the chapter is to see what regression can
and cannot do once the explanatory variable is *time*, and why that failure, repeated in different
ways, generates the rest of the course.

## What a time series is

A time series is a set of observations, each recorded at a specific time. The lecture's running
example is the monthly US population series (from FRED, in thousands, so that a value of 300,000
means 300 million):

| Date | Population (thousands) |
| --- | --- |
| 1959-01 | 175,818 |
| 1959-06 | 176,954 |
| 1960-01 | 178,925 |
| 1960-06 | 180,728 |

Plotted against time, this series raises the questions time series analysis exists to answer:

- **Prediction** — what is a reasonable estimate of the population at a future date, e.g. January
  2040?
- What is the population's rate of growth?
- Has that growth rate been roughly constant over time?
- Over what period did the population grow fastest? Slowest?

Time series analysis answers such questions by fitting statistical models to observed data.

## Prediction as pattern-matching

Before touching real data, the lecture opened with a classic guessing game: what's the next number?

1. $5, 8, 11, 14, 17, \_$
2. $42, 32, 23, 15, 8, \_$
3. $3, 6, 12, 24, 48, \_$
4. $-3, 7, -6, 11, -9, 15, \_, \_$
5. $4, 16, 36, 64, 100, \_$

Each is solvable because the sequence's underlying rule can be read off from the terms already
shown. The lecture then made this precise with a single worked case: find the next number in
$1, 4, 9, 16, 25, \#$. The answer is $36$, but the reasoning behind it is the point — writing the
sequence as $y_t$ indexed by $t = 1, 2, 3, \dots$, one notices that $y_t = t^2$. In the language the
course will use throughout, this is a **regression of $y_t$ on the time index $t$** — here a
quadratic one, since $y_t$ is a (quadratic) function of $t$. Prediction, in this framing, means
finding a function of $t$ that fits the observed values and extrapolating it.

This is the idea the first block of the course is built on: model a time series as $y_t = f(t) +
\text{error}$ for some function $f$, and use regression to estimate $f$.

## Topic one: multiple linear regression

The simplest choice of $f$ is a straight line: regress $y_t$ on $1, t$. For the US population data
this fits reasonably over short stretches but is clearly wrong as a single description of eight
decades of growth — a straight line cannot bend to track a rate that itself changes.

A richer family of models comes from letting $f$ be a linear combination of *several* functions of
$t$ — this is still a **linear regression** in the statistical sense (linear in the unknown
coefficients), even though the functions of $t$ themselves need not be linear. The lecture's example
is the monthly count of accidental deaths in the US, 1973–1978. A regression on $1, \cos(\pi t/6),
\sin(\pi t/6)$ already captures the shape of the series reasonably well: since $\cos(\omega t)$ has
period $2\pi/\omega$, the pair $\cos(\pi t/6), \sin(\pi t/6)$ has period $2\pi/(\pi/6) = 12$ months
— the natural annual cycle of a monthly series. Adding $\cos(\pi t/3), \sin(\pi t/3)$ (period 6
months, the second harmonic of the annual cycle) sharpens the fit further, and adding $\cos(\pi
t/2), \sin(\pi t/2)$ (period 4 months, the third harmonic) sharpens it again. Combining these
sinusoids with a quadratic trend term gives a still better fit. Each addition is just another column
in a multiple regression — the model stays linear in its coefficients throughout.

This is the course's **first topic**: multiple linear regression, covering the usual frequentist
inference together with Bayesian inference for linear regression in detail.

## Topic two: nonlinear regression

Sinusoids and polynomials are still limited: for the US population series, a single straight line
forces one growth rate on the whole eight decades, and a higher-order polynomial fits somewhat
better but is not *interpretable* — its coefficients do not correspond to a growth rate one could
quote. A more realistic model lets the growth rate itself change at a small number of points:

$$y_t = \beta_0 + \beta_1 t + \alpha_1(t - c_1)_+ + \alpha_2(t - c_2)_+ + \text{error}$$

where $(x)_+ = \max(x, 0)$ is the positive-part (hinge) function. Before $c_1$ the slope is
$\beta_1$; between $c_1$ and $c_2$ it becomes $\beta_1 + \alpha_1$; after $c_2$ it becomes $\beta_1
+ \alpha_1 + \alpha_2$ — three different growth rates, each directly readable off the fitted
coefficients.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="A piecewise-linear trend with two breakpoints, giving three different slopes">
  <line x1="40" y1="190" x2="380" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="380" y="207" text-anchor="end" font-size="12" fill="currentColor">t</text>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="18" y="28" font-size="12" fill="currentColor">y_t</text>
  <polyline points="40,175 140,150 240,95 360,25" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="140" y1="190" x2="140" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="240" y1="190" x2="240" y2="95" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="140" y="205" text-anchor="middle" font-size="12" fill="currentColor">c1</text>
  <text x="240" y="205" text-anchor="middle" font-size="12" fill="currentColor">c2</text>
  <text x="55" y="168" font-size="11" fill="currentColor">slope β1</text>
  <text x="150" y="128" font-size="11" fill="currentColor">slope β1+α1</text>
  <text x="255" y="65" font-size="11" fill="currentColor">slope β1+α1+α2</text>
</svg>
<figcaption>The hinge model breaks the trend at two change points, so each of the three segments
carries its own, directly interpretable growth rate.</figcaption>
</figure>

Because the change points $c_1, c_2$ themselves are parameters to be estimated — not fixed
regressor columns — this model is no longer linear in its parameters $(\beta_0, \beta_1, \alpha_1,
c_1, \alpha_2, c_2)$. It is the course's **second topic**: nonlinear regression over $t$, motivated
by exactly this gap between models that are easy to fit (linear, but rigid or uninterpretable) and
models that describe the data well (nonlinear, but harder to fit).

## Periodicity and the sunspot cycle

A second nonlinear-regression example is the annual sunspot count, 1700–2021. Sunspot numbers are
known to rise and fall on an approximately 11-year cycle. The lecture used this to raise a sharper
question than "what is the cycle length": why exactly 11 years, and not 10.5 or 11.5? What is the
uncertainty around that number? And can the periodicity be recovered from the data itself, rather
than taken from an external claim?

One way to answer this is to fit

$$y_t = \beta_0 + \beta_1\cos(\omega t) + \beta_2 \sin(\omega t) + \text{error}$$

and estimate the frequency $\omega$ along with $\beta_0, \beta_1, \beta_2$. Because $\omega$ sits
inside the cosine and sine rather than multiplying them, this is again a nonlinear regression model
— contrast this with the accidental-deaths example above, where the frequencies ($\pi/6, \pi/3,
\pi/2$) were fixed in advance and only the coefficients in front of the sinusoids were estimated.
The lecture noted two further series with a similar periodic-or-cyclic flavor that the course will
return to: annual lynx trappings in Canada (1821–1934), and the US unemployment rate.

This periodic-regression model is closely related to Fourier analysis, and the course will develop
the relevant machinery — Fourier frequencies, the discrete Fourier transform, and the periodogram —
tools that are used extensively in engineering time series analysis, with practical applications the
lecture promised to return to.

## Topic three: high-dimensional regression and regularization

The hinge-function idea from Topic Two can be pushed to an extreme: instead of two change points,
put one at every time point in the dataset,

$$y_t = \beta_0 + \beta_1 t + \beta_2(t-2)_+ + \beta_3(t-3)_+ + \cdots + \beta_n(t-n)_+ + \epsilon,$$

allowing a different growth rate between every consecutive pair of observations. With as many
parameters as data points, this model cannot be fit sensibly by ordinary least squares — some form
of **regularization** is needed to make the fit well-behaved. This is the course's **third topic**:
Ridge and LASSO regularization. The lecture illustrated the idea on a temperature-anomaly dataset,
where a Ridge-regularized version of this many-breakpoint model produces a smooth curve tracking the
noisy raw anomalies.

## Topic four: variance modeling and spectral analysis

Everything so far models the *mean* of $y_t$ as a function of time. Financial data motivates a
different question. Using daily S&P 500 closing prices $P_t$ (2000–2024), define the return

$$r_t = 100\times(\log P_t - \log P_{t-1}) \approx 100 \times \frac{P_t - P_{t-1}}{P_{t-1}},$$

i.e. (approximately) the percentage change in price from one day to the next. Financial analysts
care less about the mean of $r_t$ (which is close to zero) than about its **volatility**: a common
model is $r_t \sim N(0, \sigma_t^2)$, with $\sigma_t$ — or $\log \sigma_t$ — itself modeled as a
function of $t$. This is a **variance model**, as distinct from the mean (regression) models
discussed above; the lecture showed a ridge- and a lasso-based estimate of $\log \sigma_t$ for the
S&P return series.

**Spectral analysis** is a special case of variance modeling: instead of modeling the variance of
the raw series, it models the variance of the series' discrete Fourier transform. It is one of the
most important tools engineers use for signal processing. The lecture illustrated this with EEG
recordings taken with eyes open ($y_o$) and eyes closed ($y_c$): the two raw signals look
superficially similar, and the question is how to quantify the difference between them. Comparing
their estimated spectra reveals a clear difference around 10 Hz — a known finding from cognitive
neuroscience.

This is the course's **fourth topic**: variance modeling and spectral analysis.

## Topic five: lagged regression and ARIMA

A final puzzle closed the lecture: find the next number in $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
\#$. This is the Fibonacci sequence, $y_t = y_{t-1} + y_{t-2}$, and the next term is $144$. Crucially,
regression over $t$ cannot recover this rule — $y_t$ is not simply a function of the time index $t$,
it is a function of the series' *own recent past*. To predict it, one instead regresses $y_t$ on its
own lagged values, $y_{t-1}$ and $y_{t-2}$ — **lagged regression**, or **autoregression**.

Autoregression is the core idea behind the ARIMA class of models (AutoRegressive Integrated Moving
Average), widely used for time series prediction. The basic construction is a linear regression of
$y_t$ on $x_t = (1, y_{t-1}, \dots, y_{t-p})$ for some fixed lag $p \geq 1$. ARIMA models give decent
predictions on real data and are used extensively; the lecture closed with an example on FRED's
seasonally-adjusted quarterly GNP series, showing the predictions an AR model gives for the last
four quarters.

This is the course's **fifth topic**: lagged regression and ARIMA.

## Sources

All material is from *Lecture One* of Stat 153/248 (Time Series), UC Berkeley, Fall 2025, delivered
by Aditya Guntuboyina on 28 August 2025 — reconstructed by a model from the lecture's slide PDF
(`LectureOneSlides153248Fall2025PDF.pdf`, CC BY 4.0), since the PDF has no extractable text layer.
No transcript, problem set, or separate notes were supplied for this lecture, only the slide
reconstruction, split across three files:

- `01-lecture-one.md` — what a time series is, the US population example, the "what's next number"
  puzzles, and the worked quadratic example.
- `02-regression-over-time.md` — sinusoidal multiple regression on the accidental-deaths data, and
  the hinge-function nonlinear trend model for US population (Topics One and Two).
- `03-annual-sunspots-data.md` — the sunspot periodicity question and periodic regression, the
  lynx-trapping and unemployment datasets, high-dimensional regression with Ridge/LASSO, variance
  modeling and spectral analysis on S&P 500 returns and EEG data, and the Fibonacci/ARIMA closing
  example (Topics Three through Five).

Per the conversion notice on each file, the source PDF had no usable text layer, so a model
transcribed it: the prose is a paraphrase in places and every displayed equation is unverified
against the original slides. Graphs referenced in the slides (e.g. the US population plot, the
accidental-deaths fits, the sunspot series, the S&P 500 price and return series, the EEG spectra)
are described only by their captions in the source and are not reproduced here since no underlying
data or verified image was supplied.

---

[← 107. Multiple Frequencies and Change-of-Slope Models](107-multiple-frequencies-and-change-of-slope-models.md) · [Contents](index.md) · [109. Introduction to Time Series (part 2) →](109-introduction-to-time-series-part-2.md)
