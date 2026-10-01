---
title: "37. The Periodogram and Sinusoidal Models"
course: "Berkeley Stat 153"
chapter: 37
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 37. The Periodogram and Sinusoidal Models

## What this covers

The previous lecture set up the single-sinusoid regression model and estimated its frequency
parameter by a brute-force grid search on the residual sum of squares. This chapter answers the
question that leaves open: how do you compute that same estimate fast enough to use on a real,
large dataset, and how much do you actually know about the frequency once you have it? The route
is the Discrete Fourier Transform and the periodogram, applied first to the sunspots series (as a
check that the fast method agrees with the slow one), then to a much larger audio recording (where
only the fast method is usable at all), and finally back to the sunspots data to quantify the
uncertainty in the estimated frequency and to notice that one sinusoid does not explain the whole
series.

## The single-sinusoid model and the cost of grid search

The model under study is
$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad \epsilon_t \sim N(0,\sigma^2) \text{ i.i.d.}$$
Everything except $f$ is a linear regression coefficient, so once $f$ is fixed the model is
ordinary least squares against the two columns $\cos(2\pi f t)$ and $\sin(2\pi f t)$ plus an
intercept. Write $RSS(f)$ for the residual sum of squares of that regression. The natural estimate
of $f$ is $\hat f = \arg\min_f RSS(f)$, found by evaluating $RSS(f)$ on a grid over $[0, 0.5]$
(frequencies above $1/2$ are aliases of ones below it) and taking the minimizer.

For the annual sunspot-number series ($n = 325$), a grid of $10{,}000$ values of $f$ and a full OLS
fit at each one is workable and gives $\hat f \approx 0.0909$, i.e. an estimated period of about
$1/\hat f = 11$ years. But each evaluation of $RSS(f)$ refits a regression, and doing that on a
fine grid does not scale: run the identical procedure on a dataset with $n$ in the hundreds of
thousands and it is too slow to finish. That is the problem this chapter solves.

## Fourier frequencies, the DFT, and the periodogram

Restrict the candidate frequencies to the **Fourier frequencies**: $f = j/n$ for integer $j$, which
for $0 < j/n < 1/2$ means $j = 1, \dots, m$ with $m = \lfloor (n-1)/2 \rfloor$ when $n$ is odd (as
it is for the 325-year sunspot series). These are not an arbitrary subset — they are exactly the
frequencies at which the discrete Fourier transform is defined. For a series $y_0, \dots, y_{n-1}$,
the DFT coefficient at frequency $j/n$ is
$$b_j := \sum_{t=0}^{n-1} y_t \exp\!\left(-\frac{2\pi i\, j t}{n}\right),$$
and the **periodogram** at that frequency is
$$I(j/n) := \frac{|b_j|^2}{n}, \qquad 0 < \frac{j}{n} < \frac{1}{2}.$$

The reason this matters for the regression problem is an identity connecting $RSS$ and the
periodogram. For $f = j/n$ a Fourier frequency strictly between $0$ and $1/2$,
$$RSS(j/n) = \sum_t (y_t - \bar y)^2 - 2\, I(j/n).$$
The lecture's justification for this is the same fact used later for the Bayesian calculation: at
a Fourier frequency the regression's design matrix satisfies $X_f^\top X_f = \mathrm{diag}(n,\, n/2,\, n/2)$
— the intercept, cosine and sine columns are exactly orthogonal — so the reduction in $RSS$ from
adding the two sinusoid terms decouples cleanly into the single quantity $2|b_j|^2/n$, with no
cross-terms between frequencies to worry about. Because $\sum_t (y_t-\bar y)^2$ does not depend on
$f$, minimizing $RSS(f)$ over Fourier frequencies is the same problem as maximizing $I(j/n)$ over
$j$ — the periodogram peak *is* the least-squares frequency estimate.

This identity was checked directly on the sunspots data: computing $RSS(f)$ at every Fourier
frequency by brute-force OLS, and separately via $\mathrm{var}(y) - 2I(j/n)$ using a single call to
`np.fft.fft`, produces two curves that overlie each other exactly. The FFT computes all $n$ DFT
coefficients at once in $O(n \log n)$ time, against $O(n)$ separate OLS fits (each itself
$O(n)$ work) for the direct method — the gap is what makes the next example possible at all.

## Frequency estimation at scale: a recorded piano note

The payoff example is an audio file: about 14 seconds of the piano's middle C note, sampled at
`sr` $= 22050$ points per second, giving $n = 301{,}272$ data points. Plotted whole the waveform is
uninformative; a 500-sample window shows the periodic structure clearly.

Fitting the same single-sinusoid model to this series by direct grid search over $10{,}000$ values
of $f$ is, in practice, too slow to finish. Replacing it with the FFT–periodogram route is not just
faster but immediately usable: `np.fft.fft(y)` once, then $RSS(f)$ (or, since only the location of
the extremum matters, $I(f)$) at every one of the $\approx n/2$ Fourier frequencies. The
periodogram-maximizing frequency is
$$\hat f \approx 0.011800.$$

This $\hat f$ is a frequency in cycles per *sample*, not per second, so it is not directly
comparable to a musical pitch. One unit of time in the series is $1/sr$ seconds, so a sinusoid that
completes $f$ cycles per sample completes $f \times sr$ cycles per second, i.e. $f \times sr$ Hertz.
Here
$$\hat f \times sr \approx 260.19 \text{ Hz},$$
close to the known frequency of middle C, $261.63$ Hz. The match is the check that the whole
machinery — model, DFT, periodogram — is doing the right thing on data where the answer is known
independently.

## Quantifying uncertainty in $\hat f$

A point estimate is not the whole story, and the lecture adds a Bayesian calculation for how
confident to be in $\hat f$. For frequencies $0 \le f \le 1/2$ the (unnormalized) posterior for $f$
takes the form
$$\mathbb{1}\{0 \le f \le 1/2\}\;\bigl|X_f^\top X_f\bigr|^{-1/2}\left(\frac{1}{RSS(f)}\right)^{(n-p)/2}, \qquad p = 3.$$
Restricted to Fourier frequencies strictly between $0$ and $1/2$, $X_f^\top X_f = \mathrm{diag}(n, n/2, n/2)$
does not depend on $f$, so the determinant factor is a constant that can be dropped, leaving the
much simpler
$$\mathbb{1}\{f \text{ a Fourier frequency in } (0, 0.5)\}\left(\frac{1}{RSS(f)}\right)^{(n-p)/2},$$
which — using the RSS–periodogram identity — is again computable from a single FFT: the
log-posterior over the grid of Fourier frequencies, exponentiated (after subtracting its maximum
for numerical stability) and normalized, gives a discrete posterior distribution over $f$. A
credible interval is read off by growing a symmetric window of grid points around the posterior
mode until the enclosed probability first reaches 95%.

For the piano note this gives, in Hertz,
$$\hat f \times sr \approx 260.19, \qquad 95\% \text{ credible interval} \approx [260.12,\ 260.26] \text{ Hz}.$$
The interval is extremely tight — a direct consequence of $n$ being large: with $n \approx 300{,}000$
points, $RSS(f)$ rises very sharply away from its minimum, so the posterior concentrates hard
around $\hat f$.

## Back to the sunspots: what the Fourier grid costs you

Applying the same Fourier-frequency posterior to the sunspots series gives a point estimate
$\hat f \approx 0.0923$ (period $\approx 10.83$ years) but a much wider credible interval — in
period terms, roughly
$$[10.83 \text{ years} - 247 \text{ days},\ \ 10.83 \text{ years} + 282 \text{ days}].$$
This is not only because $n = 325$ is small. It is also a discretization effect: the Fourier
frequencies are spaced $1/n \approx 0.00308$ apart, and the posterior is only ever evaluated at
these points, so the credible interval cannot resolve anything finer than that spacing allows.

Repeating the calculation on a much finer, non-Fourier grid ($f$ stepped by $0.0001$ over
$[0.01, 0.5]$) removes this restriction — but at a price: away from Fourier frequencies
$X_f^\top X_f$ is no longer a fixed diagonal matrix, so the $|X_f^\top X_f|^{-1/2}$ term must be
computed for each candidate $f$ (via a log-determinant), and $RSS(f)$ must be obtained by direct
OLS rather than the periodogram shortcut. The result is a narrower estimate, $\hat f \approx 0.0909$
(period $\approx 11.00$ years), with credible interval
$$[11.00 \text{ years} - 13.2 \text{ days},\ \ 11.00 \text{ years} + 13.3 \text{ days}] ,$$
markedly tighter than the Fourier-grid version. The trade-off is explicit: the FFT-based route is
fast but its resolution is capped at $1/n$; a fine direct grid buys resolution by giving up the
speedup.

## The periodogram as an exploratory tool, and fitting more than one sinusoid

The periodogram has a second use beyond speeding up a fit already decided on: its shape suggests
which model to fit in the first place. For the sunspots series, alongside the expected peak near
$f \approx 1/11$ there is a second, distinct peak at low frequency, near $f \approx 3/n$, standing
above its neighbors.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Schematic periodogram of the sunspots series with two peaks, one near a low frequency and one near the annual cycle">
  <line x1="40" y1="180" x2="380" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="210" y="205" text-anchor="middle" font-size="12" fill="currentColor">frequency f</text>
  <text x="15" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 15 100)">I(f)</text>
  <path d="M 40 175 L 70 172 L 90 174 L 130 170 L 170 176 L 210 173 L 250 175 L 290 172 L 330 176 L 370 174 L 380 175" fill="none" stroke="currentColor" stroke-width="1" stroke-opacity="0.5"/>
  <path d="M 46 178 C 50 178, 52 45, 55 45 C 58 45, 60 178, 64 178" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <path d="M 96 178 C 100 178, 103 25, 106 25 C 109 25, 112 178, 116 178" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <text x="55" y="60" text-anchor="middle" font-size="11" fill="currentColor">f &#8776; 3/n</text>
  <text x="106" y="18" text-anchor="middle" font-size="11" fill="currentColor">f &#8776; 1/11</text>
  <text x="380" y="195" text-anchor="end" font-size="11" fill="currentColor">0.5</text>
  <text x="40" y="195" text-anchor="middle" font-size="11" fill="currentColor">0</text>
</svg>
<figcaption>The two dominant peaks in the sunspots periodogram — a low-frequency peak near $3/n$ and the
annual-cycle peak near $1/11$ — are what motivate fitting a sum of two, and then three, sinusoids
instead of one.</figcaption>
</figure>

This suggests generalizing the model to a sum of $K$ sinusoids,
$$y_t = \beta_0 + \sum_{k=1}^{K}\Bigl(\beta_{2k-1}\cos(2\pi f_k t) + \beta_{2k}\sin(2\pi f_k t)\Bigr) + \epsilon_t,$$
with all of the $f_k$ (and all the $\beta$'s and $\sigma$) unknown. Fitting several frequencies
jointly is not simply a matter of reading off the top few periodogram peaks, because the columns
for different $f_k$ are no longer orthogonal once the frequencies are free to move together, so
$RSS(f_1,\dots,f_K)$ has to be minimized over a joint grid: a 2-dimensional grid search for two
sinusoids, a 3-dimensional one for three, with the grid ranges chosen using the periodogram as a
guide to where the good values are likely to sit.

For two sinusoids, searching $f_1$ over $[0.05, 0.15]$ and $f_2$ over $[1/n,\, 4/n]$ on a
$300 \times 300$ grid gives $\hat f_1 \approx 0.0908$, $\hat f_2 \approx 0.00993$, with
$RSS \approx 758{,}773$ (down from $RSS \approx 772{,}464$ for the single-sinusoid fit at
$f = 1/11$). For three sinusoids, a $50\times 50\times 50$ grid over three frequency ranges finds
$\hat f \approx (0.0907,\ 0.0100,\ 0.0998)$ with $RSS \approx 595{,}012$. Fitting the regression
at this three-frequency optimum gives $R^2 = 0.522$ — three sinusoids together capture only about
half the variance in the series, which is itself informative: the sunspot cycle is not simply a
sum of a small number of pure tones.

## Sources

- Fall 2025, *DFT and Periodogram* (`CodeLectureEight153248Fall2025.md`) — the single-sinusoid
  model and slow grid search on the sunspots data; definitions of Fourier frequencies, the DFT
  coefficient $b_j$, and the periodogram $I(j/n)$; the $RSS$–periodogram identity and its numerical
  verification against direct OLS; the audio dataset (middle C, `librosa`), the failure of the
  direct grid search at that size, the FFT-based fix, and the conversion of the estimated frequency
  to Hertz via the sampling rate. The lecture opens by referring to "the last lecture," where the
  sinusoidal model and the direct RSS grid search were first introduced on the sunspots data — not
  itself supplied.
- Spring 2025, *Audio Data* (`01-audio-data.md`) — the two stated uses of the periodogram (speed,
  and model exploration); the same middle-C example, described as a repeat of "Lecture 6" (not
  supplied); the Bayesian posterior for $f$, its simplification at Fourier frequencies via
  $X_f^\top X_f = \mathrm{diag}(n, n/2, n/2)$, and the credible-interval construction, applied to
  the audio frequency estimate.
- Spring 2025, *Sunspots Dataset* (`02-sunspots-dataset.md`) — the sunspots frequency/period point
  estimate and its Fourier-frequency credible interval; the finer, non-Fourier grid search and its
  narrower credible interval, contrasting the two; the periodogram's second peak motivating a
  two-sinusoid and then three-sinusoid model, the joint grid searches, and the final OLS fit and
  $R^2$.
- Referred to but not contained in the supplied material: the earlier lecture(s) that first fit the
  single-sinusoid model to the sunspots data and introduced the Bayesian posterior for $f$; the raw
  data files `SN_y_tot_V2.0.csv` (sunspot numbers) and `Hear Piano Note - Middle C.mp3`; and all
  plots, which are noted in the converted notebooks as omitted figures.

---

[← 36. Anatomy of a Regression Fit (part 1)](36-anatomy-of-a-regression-fit-part-1.md) · [Contents](index.md) · [38. AR(p) Forecasting and Prediction Uncertainty →](38-ar-p-forecasting-and-prediction-uncertainty.md)
