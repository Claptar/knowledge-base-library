---
title: "46. Sinusoidal Regression and the DFT"
course: "Berkeley Stat 153 Fall 2024"
chapter: 46
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 46. Sinusoidal Regression and the DFT

## What this covers

This chapter fits a sinusoidal regression model to data that oscillates with an unknown period,
and works through what it takes to (a) estimate that unknown frequency, (b) quantify how confident
that estimate is, and (c) do both without a brute-force search once the dataset is large. It
assumes ordinary least squares (design matrices, residual sum of squares, $R^2$) and is comfortable
with complex exponentials $e^{i\theta} = \cos\theta + i\sin\theta$. Two datasets carry the
argument throughout: the annual sunspot count, and 14 seconds of a recorded piano note.

## The sinusoidal regression model

A series $y_1,\dots,y_n$ that oscillates with an unknown period is modelled as

$$
y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad \epsilon_t \overset{iid}{\sim} N(0,\sigma^2).
$$

If $f$ were known this is an ordinary linear regression on the two columns $\cos(2\pi f t)$ and
$\sin(2\pi f t)$ plus an intercept: it is the *frequency* $f$ that makes this a nonlinear problem,
not the amplitude or phase. Once $f$ is fixed, $\beta_0$ sets the mean level and $\beta_1,\beta_2$
together fix the amplitude $\sqrt{\beta_1^2+\beta_2^2}$ and phase of the cycle, and OLS estimates
them as usual.

The running example is the SILSO annual sunspot count (325 years of one row per year: year, mean
sunspot number, plus quality columns that are not used). Plotted against time it looks roughly
periodic but not cleanly sinusoidal. Fitting a guessed frequency $f=1/10$ — regressing on
$\cos(2\pi t/10)$ and $\sin(2\pi t/10)$ — gives a mediocre fit, $R^2 = 0.132$, with the sine
coefficient significant ($t=6.93$) but the cosine coefficient not ($t=-0.99$). That the fit depends
so much on the guessed frequency is exactly why $f$ should be estimated rather than guessed.

## Estimating the frequency: $RSS(f)$

For a fixed frequency $f$, define

$$
RSS(f) \;:=\; \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \Big(y_t - \beta_0 - \beta_1\cos(2\pi f t) - \beta_2 \sin(2\pi f t)\Big)^2,
$$

the residual sum of squares of the best-fitting sinusoid *at that frequency*. $RSS(f)$ is small
exactly where a sinusoid at frequency $f$ explains the data well, so scanning $f$ over a grid in
$(0,1/2)$ — the Nyquist range, since for data sampled once per unit time no frequency above $1/2$
is distinguishable from one below it — and taking the minimizer gives an estimate $\hat f$.

On the sunspot data, a handful of candidate frequencies already point somewhere: $RSS(1/15)\approx
1{,}235{,}555$, $RSS(1/4)\approx 1{,}243{,}980$, $RSS(1/10)\approx 1{,}079{,}859$, and
$RSS(1/11)\approx 866{,}129$ — clearly the best of the four. Scanning $10{,}000$ equally spaced
values of $f$ across $[0,0.5]$ and minimizing gives $\hat f = 0.0\overline{90} = 1/11$ exactly, an
estimated periodicity of $11$ years — the well-known sunspot cycle. Refitting the regression at
$f=\hat f$ improves the fit substantially over the guessed $f=1/10$: $R^2 = 0.304$, both
coefficients now strongly significant, and $\hat\sigma = \sqrt{RSS(\hat f)/(n-3)} \approx 51.9$.

## Quantifying uncertainty in $\hat f$

Point estimation only tells half the story; the lecture also builds a Bayesian posterior over $f$:

$$
\text{posterior}(f) \;\propto\; \mathbb{1}\{0 < f < 1/2\}\, \big|X_f^\top X_f\big|^{-1/2} \left(\frac{1}{RSS(f)}\right)^{(n-p)/2},
$$

where $X_f$ is the $n\times p$ design matrix built at frequency $f$ (here $p=3$: intercept,
cosine, sine). Two factors drive this posterior: $\left(1/RSS(f)\right)^{(n-p)/2}$, which grows
fast wherever $RSS(f)$ is small, and $|X_f^\top X_f|^{-1/2}$, which does not depend on the data at
all, only on how the geometry of the design matrix changes with $f$.

Plotting the log-posterior with and without the determinant term shows the two curves nearly
parallel except very close to the boundary $f \approx 0$ or $f\approx 1/2$ — their difference is
essentially flat away from the endpoints. So in practice the $RSS(f)$ term alone drives the shape
of the posterior, and, consistent with that, the posterior's mode coincides exactly with the
least-squares estimate found above: both give $f = 0.0909\ldots = 1/11$.

Once the posterior is normalized to sum to $1$ over the grid, a $95\%$ credible interval is built
by starting at the mode and expanding symmetrically — $m$ grid points on either side — until the
accumulated mass reaches $0.95$. On the sunspot grid ($10{,}000$ points over $[0,0.5]$, with the
endpoints trimmed): the mass at the mode alone is $0.141$; one point either side gives $0.407$; six
points either side gives $0.978$, the first value past $0.95$. That gives $\hat f \in [0.0906,
0.0912]$, or, inverting to periods, a period in $[10.96, 11.04]$ years — a strikingly narrow band
around $11$.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="RSS(f) as a function of frequency, showing a sharp minimum near f = 1/11 with the narrow credible band shaded around it">
  <line x1="40" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="187" text-anchor="end" font-size="12" fill="currentColor">f</text>
  <text x="46" y="30" text-anchor="start" font-size="12" fill="currentColor">RSS(f)</text>
  <rect x="160" y="20" width="20" height="150" fill="currentColor" fill-opacity="0.15"/>
  <path d="M40,150 L90,130 L140,112 L155,95 L165,60 L170,30 L175,60 L185,95 L200,112 L250,130 L300,150" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <line x1="170" y1="170" x2="170" y2="30" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="170" y="187" text-anchor="middle" font-size="12" fill="currentColor">1/11</text>
</svg>
<figcaption>RSS(f) drops sharply as f nears the sunspot cycle's true frequency 1/11 and rises just as sharply on either side (shaded band). Because the posterior is essentially RSS(f) raised to a large negative power, this narrow dip is what makes the 95% credible interval for f so tight.</figcaption>
</figure>

The reason for the tight interval is visible directly in $RSS$: moving $f$ only slightly away from
$1/11$ costs a lot. $RSS(1/11)\approx 866{,}129$, while $RSS(1/11.05)\approx 887{,}294$ and
$RSS(1/10.95)\approx 891{,}223$ — a jump of roughly $20{,}000$–$25{,}000$ for a change of only
$\pm 0.05$ years in the assumed period. Because the posterior is essentially $RSS(f)^{-(n-p)/2}$,
a sharp minimum in $RSS$ translates directly into a sharply peaked posterior and hence a narrow
credible interval.

## Why grid search does not scale

The same recipe — grid over $f$, refit OLS, record $RSS(f)$ — is tried on a second dataset: a
recording of a piano's Middle C, loaded as a waveform sampled at $22{,}050$ Hz over about $13.66$
seconds, giving $n = 301{,}272$ points. A short segment of the waveform shows visible cyclical
structure, so the same sinusoidal-model idea should apply. But evaluating $RSS(f)$ at each of
$10{,}000$ grid points, each requiring a fresh OLS fit on $n\approx 3\times 10^5$ observations, is
far too slow to run in practice. Finding the dominant frequency in a long recording needs a way of
computing $RSS(f)$ that does not refit a regression from scratch at every candidate $f$.

## Fourier frequencies

A frequency $f$ is a **Fourier frequency** relative to sample size $n$ if $nf$ is an integer —
equivalently, the sinusoid $\cos(2\pi f t)$ (or $\sin$) completes a whole number of cycles over the
observation window $t=1,\dots,n$, closing exactly rather than cutting off partway through a cycle.
Comparing a sinusoid built at a Fourier frequency (e.g. $f=5/79$ for $n=79$) against one at a
nearby non-Fourier frequency (e.g. $f=5.5/79$) shows the difference directly in a plot: only the
Fourier-frequency sinusoid returns to where it started by the time $t$ reaches $n$.

At Fourier frequencies, the cosine and sine columns of the design matrix satisfy orthogonality
identities that a generic $f$ does not give. For $f\in(0,1/2)$ a Fourier frequency:

1. Zero mean: $\sum_{t=1}^n \cos(2\pi f t) = \sum_{t=1}^n \sin(2\pi f t) = 0$.
2. Constant energy: $\sum_{t=1}^n \cos^2(2\pi f t) = \sum_{t=1}^n \sin^2(2\pi f t) = n/2$.
3. Cosine and sine at the same frequency are orthogonal: $\sum_{t=1}^n \cos(2\pi f t)\sin(2\pi f t) = 0$.
4. Cosine/sine at two distinct Fourier frequencies $f_1 \ne f_2$ are pairwise orthogonal: all four
   sums $\sum \cos f_1 t\cos f_2 t$, $\sum \sin f_1 t \sin f_2 t$, $\sum \cos f_1 t \sin f_2 t$,
   $\sum \sin f_1 t \cos f_2 t$ vanish (writing $\cos f_j t$ for $\cos(2\pi f_j t)$, etc.).

These check out numerically for $n=79$: at $f=5/79$, $\sum_t \cos(2\pi f t) \approx 8.9\times
10^{-15}$ and $\sum_t \sin(2\pi f t)\approx 6.6\times10^{-16}$ (both zero up to floating-point
error), while $\sum_t \cos^2 \approx 39.5 = 79/2$ and likewise for $\sin^2$. Cross-checking two
distinct Fourier frequencies $f_1=4/79$, $f_2=5/79$: $\sum_t \sin(2\pi f_1 t)\cos(2\pi f_2 t)
\approx -1.3\times10^{-15} \approx 0$, and a scatterplot of $\sin(2\pi f_1 t)$ against
$\cos(2\pi f_2 t)$ across $t$ shows no linear trend — exactly what zero correlation between two
design columns looks like.

The reason this matters for speed: because the cosine and sine regressors at *different* Fourier
frequencies are mutually orthogonal, and orthogonal to the intercept, they don't compete with one
another the way an arbitrary pair of regressors would. That is what makes it possible to read
$RSS(f)$ off from a single calculation on the data at each Fourier frequency, instead of running a
fresh least-squares fit per $f$.

## The periodogram

At a Fourier frequency $f\in(0,1/2)$, $RSS(f)$ has a closed form that avoids refitting the
regression entirely:

$$
RSS(f) = \sum_{t=1}^n (y_t - \bar y)^2 - 2I(f), \qquad I(f) := \frac{1}{n}\left|\sum_{t=1}^n y_t e^{-2\pi i f t}\right|^2.
$$

$I(f)$ is the **periodogram**: it is built from a single sum, $\sum_t y_t e^{-2\pi i f t}$,
computed once per Fourier frequency, rather than from a separate least-squares fit per $f$. That
sum, evaluated as $f$ ranges over the Fourier frequencies in $(0,1/2)$, is the discrete Fourier
transform of $y_1,\dots,y_n$.

## The discrete Fourier transform

For a dataset $y_0,\dots,y_{n-1}$, its **discrete Fourier transform (DFT)** is $b_0,\dots,b_{n-1}$
where

$$
b_j = \sum_{t=0}^{n-1} y_t \exp\!\left(-\frac{2\pi i j t}{n}\right), \qquad j=0,1,\dots,n-1,
$$

a complex number whose real part is $\sum_t y_t \cos(2\pi (j/n) t)$ and whose imaginary part is
$-\sum_t y_t \sin(2\pi (j/n) t)$.

On the toy series $y=(2,-5,3,0)$ (so $n=4$), computing all four $b_j$ gives
$(0,\; -1+5i,\; 10+0i,\; -1-5i)$. Two checks confirm the formula: $b_0 = \sum_t y_t = 0$ (the
zero-frequency term of a DFT is always the sum of the data), and building $b_2$ by hand from
$\sum_t y_t \cos(2\pi \cdot 2t/4)$ and $-\sum_t y_t \sin(2\pi \cdot 2t/4)$ reproduces $10 + 0i$
exactly, matching the direct computation.

Computed this way, each $b_j$ costs $O(n)$ work and there are $n$ of them, so the whole transform
costs $O(n^2)$ — no faster than the grid search it is meant to replace. The lecture flags, without
developing it, that an efficient algorithm — the Fast Fourier Transform (FFT) — computes the entire
DFT in $O(n\log n)$, and that this, together with the periodogram identity above, is what makes
finding periodicities in a series as long as the piano recording ($n\approx 3\times10^5$ samples)
practical. That algorithm is left for the next lecture.

## Sources

- Berkeley STAT 153, *Code Lecture Seven*, Fall 2025 notebook —
  [`CodeLectureSeven153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSeven153248Fall2025.ipynb)
  (converted at `docs/statistics/berkeley/stat153/fall-2025/CodeLectureSeven153248Fall2025.md`):
  the sinusoidal regression model, the SILSO sunspot dataset, the $RSS(f)$ grid search and the
  fitted model at $\hat f = 1/11$, the Bayesian posterior for $f$ and its 95% credible interval, the
  piano-note audio example motivating faster computation, and the periodogram identity for
  $RSS(f)$ at Fourier frequencies.
- Berkeley STAT 153, *Code Lecture Seven*, Spring 2025 notebook —
  [`CodeLectureSeven153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSeven153248Spring2025.ipynb)
  (converted at `docs/statistics/berkeley/stat153/spring-2025/CodeLectureSeven153248Spring2025.md`):
  the definition of a Fourier frequency, the orthogonality properties of sinusoids at Fourier
  frequencies (verified numerically for $n=79$), and the discrete Fourier transform, worked on
  $y=(2,-5,3,0)$.
- No slides or lecture transcript were supplied for this chapter — both inputs are Jupyter
  notebooks (route: notebook) converted losslessly from the course repositories. The sunspot data
  itself is external, from SILSO (https://www.sidc.be/SILSO/datafiles).
- The Fast Fourier Transform algorithm for computing the DFT in $O(n\log n)$ is named by the Fall
  2025 notebook as material for "the next lecture" but is not developed in either notebook
  supplied here.

---

[← 45. Prediction Uncertainty in AR Models](45-prediction-uncertainty-in-ar-models.md) · [Contents](index.md) · [47. AR(p) Estimation and Forecasting (part 1) →](47-ar-p-estimation-and-forecasting-part-1.md)
