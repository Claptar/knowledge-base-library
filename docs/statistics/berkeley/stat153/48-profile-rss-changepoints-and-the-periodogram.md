---
title: "48. Profile RSS: Changepoints and the Periodogram"
course: "Berkeley Stat 153 Fall 2024"
chapter: 48
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 48. Profile RSS: Changepoints and the Periodogram

## What this covers

Two linked worked examples on **nonlinear regression**: fitting a model that is linear in most of
its parameters but nonlinear in one of them. Both follow the same recipe — hold the nonlinear
parameter fixed, fit the rest by ordinary least squares, and search over the nonlinear parameter for
the value that fits best — and the second example turns that search into something genuinely fast.
The chapter assumes ordinary least-squares regression, $R^2$, and the residual sum of squares (RSS)
as already-familiar tools, and it introduces changepoint regression, a Bayesian treatment of the
changepoint, the periodogram, and the Fast Fourier Transform (FFT).

## From straight-line growth to a broken stick

The motivating dataset is the annual resident population of California, 1900–2024 (in thousands of
persons, from FRED). Working with $y_t = \log(\text{population})$ makes growth rates additive and
gives a model with a cleaner interpretation. Fitting a simple linear regression $y_t = \beta_0 +
\beta_1 t + \epsilon_t$ to the $n = 125$ log-population values gives a fitted slope
$\hat\beta_1 = 0.0269$: the model says the population grows at a constant $2.69\%$ per year. The fit
is not good — $\mathrm{RSS} = 6.189$ — because the growth rate visibly was not constant: faster in
the early decades, slower in recent ones. A single straight line cannot capture that.

The fix is a model that lets the slope change once, at some unknown time $c$:

$$
y_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \epsilon_t, \qquad (t-c)_+ := \max(0, t-c).
$$

Before $c$ the slope is $\beta_1$; after $c$ it is $\beta_1 + \beta_2$, because the extra term
$(t-c)_+$ is zero until $t$ passes $c$ and then grows linearly alongside it.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A broken-stick function with a single change of slope at t = c">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="160" x2="170" y2="80" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="80" x2="290" y2="45" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="190" x2="170" y2="80" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="300" y="205" text-anchor="middle" font-size="12" fill="currentColor">t</text>
  <text x="25" y="25" text-anchor="middle" font-size="12" fill="currentColor">y</text>
  <text x="90" y="110" text-anchor="middle" font-size="11" fill="currentColor">slope &#946;&#8321;</text>
  <text x="235" y="55" text-anchor="middle" font-size="11" fill="currentColor">slope &#946;&#8321;+&#946;&#8322;</text>
</svg>
<figcaption>The broken-stick (changepoint) model: slope β₁ before c, slope β₁+β₂ after it. Fitting c
means finding the kink location that minimizes the residual sum of squares.</figcaption>
</figure>

If $c$ were known, fitting this model is nothing new: it is ordinary multiple linear regression on
the design matrix with columns $1$, $t$, and $(t-c)_+$. Two arbitrary choices illustrate that the
choice of $c$ matters a great deal: fixing $c = 25$ (i.e., year 1924) gives $\mathrm{RSS} = 2.970$
and $R^2 = 0.976$, already a large improvement on the single-slope model; fixing $c = 75$ (year
1974) gives $\mathrm{RSS} = 0.543$, a further improvement. Since different guesses at $c$ give very
different fits, the natural next step is to stop guessing and estimate $c$ from the data.

## Estimating the changepoint by profiling

For each candidate value of $c$, fitting the model by least squares and recording the resulting
residual sum of squares defines a function $\mathrm{RSS}(c)$ — this is the *profile* RSS, the linear
parameters $\beta_0, \beta_1, \beta_2$ having been optimized out for that fixed $c$. The estimate of
$c$ is then

$$
\hat c = \operatorname*{arg\,min}_{c} \mathrm{RSS}(c).
$$

Evaluating $\mathrm{RSS}(c)$ on a grid of 1000 values of $c$ between $1$ and $n$ and taking the
minimizer gives $\hat c = 66.289$, corresponding to the year $\widehat{1900 + \hat c - 1} =
1965.29$: the population growth pattern changed around 1965. The resulting RSS, $0.349$, is smaller
than either of the arbitrary guesses tried above, confirming that neither $c=25$ nor $c=75$ was the
best choice. Refitting at $\hat c$ gives $\hat\beta_0 = 7.369$, $\hat\beta_1 = 0.038$,
$\hat\beta_2 = -0.024$: the growth rate before 1965 was about $3.8\%$ per year, and after 1965 about
$3.8 - 2.4 = 1.4\%$ per year.

## Quantifying uncertainty about the changepoint: a Bayesian posterior

The ordinary least-squares standard errors that come out of the regression fit *at* $\hat c$ do not
account for the fact that $\hat c$ was itself estimated from the same data — they describe
uncertainty in $\beta_0,\beta_1,\beta_2$ conditional on $c=\hat c$ being correct, not uncertainty
about $c$ itself. To get an interval for $c$, the lecture instead builds a Bayesian posterior for it:

$$
\text{posterior}(c) \;\propto\; \mathbb{1}\{1 < c < n\}\; \left|X_c^\top X_c\right|^{-1/2}
\left(\frac{1}{\mathrm{RSS}(c)}\right)^{(n-p)/2},
$$

where $X_c$ is the design matrix built with that value of $c$ and $p$ is the number of regression
parameters. Reading the factors: the indicator restricts $c$ to the interior of the data range; the
$\mathrm{RSS}(c)^{-(n-p)/2}$ term favors values of $c$ that fit the data well, with more data ($n$
large) sharpening that preference; the determinant term $|X_c^\top X_c|^{-1/2}$ is a correction that
comes out of integrating the linear parameters out of the model analytically, and it means the
posterior mode need not exactly coincide with the least-squares estimate $\hat c$, though the two
are typically close. (The posterior is only known up to a normalizing constant here, which is why it
is written with $\propto$; and the log of it is computed rather than the raw value, for numerical
stability, dropping candidate $c$ values too close to the two ends of the range to avoid near-
singularity of $X_c^\top X_c$.)

On this dataset the posterior mode and the least-squares estimate land on the identical grid point,
$66.289$. Normalizing the posterior over the grid and taking a $95\%$ credible region — the smallest
window of adjacent grid points around the mode whose posterior probability totals at least
$0.95$ — gives

$$
\hat c = 66.289 \ (\text{year } 1965.29), \qquad 95\% \text{ credible interval: } [64.303,\, 68.275]
\ (\text{years } [1963.30,\, 1967.28]).
$$

Drawing samples of $c$ from the (discretized) posterior and overlaying them on the data as a band of
candidate changepoints — most clustered tightly around 1965, with a visible but narrow spread —
gives the same message pictorially: the changepoint is reasonably well pinned down, to within a few
years.

## A second nonlinear regression problem: fitting a sinusoid

The same idea reappears in an unrelated-looking problem: fitting a periodic component to a time
series. The model is

$$
y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad
\epsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2).
$$

If the frequency $f$ is known, this is again ordinary linear regression on the columns $1$,
$\cos(2\pi f t)$, $\sin(2\pi f t)$. If $f$ is unknown, it plays exactly the role that the changepoint
$c$ played above: profile it out by minimizing over $\beta_0,\beta_1,\beta_2$ for each fixed $f$,
then search over $f$, and the same Bayesian machinery used for $c$ carries over unchanged for
uncertainty about $f$.

## The periodogram identity: an exact shortcut for RSS(f)

Define, as before, the profile sum of squares

$$
\mathrm{RSS}(f) := \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \bigl(y_t - \beta_0 - \beta_1\cos(2\pi
ft) - \beta_2 \sin(2\pi f t)\bigr)^2.
$$

For the sinusoid problem, unlike the changepoint problem, there is an exact closed-form shortcut for
$\mathrm{RSS}(f)$ whenever $f$ is a **Fourier frequency** — that is, $f \in (0, 1/2)$ with $nf$ an
integer:

$$
\mathrm{RSS}(f) = \sum_{t=1}^n (y_t - \bar y)^2 - 2 I(f), \qquad
I(f) := \frac{1}{n}\left|\sum_{t=1}^n y_t\, e^{-2\pi i f t}\right|^2.
$$

$I(f)$ is called the **periodogram**. The quantity inside the absolute value, $\sum_t y_t
e^{-2\pi i f t}$, evaluated across all the Fourier frequencies, is the **Discrete Fourier Transform**
(DFT) of the data — so the periodogram is (up to the factor $1/n$) just the squared magnitude of the
DFT. This means $\mathrm{RSS}(f)$ at every Fourier frequency can be read off directly from the DFT of
the series, without fitting a separate regression for each candidate $f$.

## Fourier frequencies and the Fast Fourier Transform

The identity above only holds exactly at Fourier frequencies, so those — rather than an arbitrary
fine grid — are the natural frequencies to search over. For $n$ odd, the Fourier frequencies in
$(0,\tfrac12)$ are $\tfrac1n, \tfrac2n, \dots, \tfrac{n-1}{2n}$: there are $(n-1)/2$ of them. On a
yearly sunspot-count dataset (1700–2024, $n = 325$), computing $\mathrm{RSS}(f)$ directly at each of
the $162$ Fourier frequencies — by fitting the three-column regression from scratch at every one —
gives exactly the same values as computing it via the periodogram identity fed by an FFT of the
whole series, confirming the identity numerically.

The point of the identity is speed. Computing $\mathrm{RSS}(f)$ directly needs a separate regression
fit for every candidate frequency. Computing it via the periodogram needs a single FFT of the entire
series, which produces the DFT — and hence $I(f)$, and hence $\mathrm{RSS}(f)$ — at *every* Fourier
frequency at once, using the efficient FFT algorithm rather than $n$ or more separate fits. The gap
between the two only becomes dramatic when $n$ is large, as the next example shows.

## Worked example: finding a piano note's frequency

The final example applies this to an audio recording of the middle-C note on a piano, about $13.66$
seconds long. Loaded at a sampling rate of $sr = 22050$ samples per second, it has
$n = 301{,}272$ data points — far larger than the sunspot series. Running the direct, per-frequency
regression approach over even a modest grid of $10{,}000$ candidate frequencies took too long to be
practical and was abandoned. Computing the periodogram from a single FFT of the series, by contrast,
stayed fast and gave $\mathrm{RSS}(f)$ (equivalently $I(f)$) at every one of the roughly $n/2$
Fourier frequencies.

The frequency at which the periodogram peaks is $\hat f = 0.0118$ (in cycles per sample). To convert
this to a physical frequency in Hertz: $\cos(2\pi f t)$ completes $f$ cycles per unit of $t$, and
here one unit of $t$ is one sample, i.e. $1/sr$ seconds — so the sinusoid completes $f \times sr$
cycles per second. Multiplying, $\hat f \times sr = 260.19$ Hz. The standard frequency of the
middle-C note is about $261.63$ Hz, so the periodogram peak — found without ever fitting a
regression by hand at the true frequency — lands very close to the physically correct pitch.

## Sources

- **`CodeLectureSix153248Fall2025.ipynb`** (Berkeley Stat 153, fall 2025, lecture titled "Nonlinear
  Regression"), CC BY 4.0, converted 2026-09-18 —
  <https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureSix153248Fall2025.ipynb>.
  Source for the California population example, the broken-stick model, profile-RSS estimation of
  the changepoint, and the Bayesian posterior, credible interval and posterior sampling for it. Also
  the source of the transition sentence into the sinusoid model at the end of the notebook.
- **`CodeLectureSix153248Spring2025.ipynb`** (Berkeley Stat 153, spring 2025, lecture titled "Sum of
  Squares and Periodogram"), CC BY 4.0, converted 2026-09-18 —
  <https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureSix153248Spring2025.ipynb>.
  Source for the sinusoid regression setup, the periodogram identity for $\mathrm{RSS}(f)$, the
  Fourier-frequency grid, the sunspot verification of the identity, and the piano-note example.

Both notebooks are lecture-6 code walkthroughs from the same course taught in different terms; they
were combined here because they are complementary rather than repeated material — the fall version
supplies the general profile/Bayesian recipe with a fully worked example, and the spring version
supplies the closed-form shortcut and its computational payoff for the case the fall version only
introduces at its end.

Two things the lecture refers to but that are not in either notebook: the in-class algebraic
derivation of the periodogram identity ("In class today, we derived the following alternative
formula…") is stated and used but not shown; and the spring notebook's opening reuse of "the
following function for computing $\mathrm{RSS}(f)$… In the last lecture" refers to a direct grid-
search fit from an earlier class session not included in this material. The DFT and FFT algorithm
themselves are flagged as "next lecture" topics and are used here only as a black box. All figures
in both source notebooks are marked as omitted from the converted text, so the plots described above
(fitted curves, RSS-vs-$c$ and RSS-vs-$f$ curves, the posterior density, the periodogram) are
described from the surrounding narrative and printed numerical output, not reproduced as images.

---

[← 47. AR(p) Estimation and Forecasting (part 1)](47-ar-p-estimation-and-forecasting-part-1.md) · [Contents](index.md) · [49. Autoregressive Models in Practice →](49-autoregressive-models-in-practice.md)
