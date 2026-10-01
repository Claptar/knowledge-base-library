---
title: "98. Smoothing the Periodogram (part 2)"
course: "Berkeley Stat 153"
chapter: 98
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 98. Smoothing the Periodogram (part 2)

## What this covers

The periodogram is a genuinely noisy estimate of a time series' spectral density — its variance
does not shrink as the sample grows, no matter how much data is collected. This chapter answers
the question of what to do about that: how to turn a noisy periodogram into a usable estimate of
the spectrum by writing down a likelihood for it and penalizing roughness, and what that estimate
reveals when applied to a real economic series. It assumes the reader already has the discrete
Fourier transform, the periodogram, and the basic vocabulary of ridge and lasso penalties (an
$\ell_2$ versus an $\ell_1$ penalty on a residual).

## From an index to a growth rate

The running example is FRED's "Industrial Production: Total Index" (series `IPB50001N`), a
monthly, *not* seasonally adjusted index $I_t$ starting in January 1919. Rather than model the
level of the index, the analysis works with its monthly growth rate,
$$y_t = 100\left(\log I_t - \log I_{t-1}\right).$$
This is the standard log-growth-rate transform: if $I_t = I_{t-1}(1+x)$ for a small fractional
change $x$, then $\log I_t - \log I_{t-1} = \log(1+x) \approx x$, so $y_t$ is approximately $100$
times the percentage change in the index from one month to the next. Differencing the index series
gives $n = 1272$ values of $y_t$.

## An additive regression model in the frequency domain

For an even sample size $n$, write $m = n/2 - 1$ and model the series as a sum over the Fourier
frequencies $j/n$:
$$y_t = \beta_0 + \sum_{j=1}^m \Big(\beta_{1j}\cos(2\pi (j/n) t) + \beta_{2j}\sin(2\pi (j/n) t)\Big) + \beta_{m+1}\cos(\pi t).$$
The last term, at the Nyquist frequency $1/2$, only appears because $n$ is even — there is no
paired sine term there since $\sin(\pi t) = 0$ for integer $t$. This is not an approximation: any
sequence of length $n$ can be written exactly this way, with coefficients
$$\beta_0 = \bar y, \quad \beta_{1j} = \frac2n\sum_{t=1}^n y_t\cos(2\pi (j/n) t), \quad \beta_{2j} = \frac2n\sum_{t=1}^n y_t \sin(2\pi (j/n) t), \quad \beta_{m+1} = \frac1n \sum_{t=1}^n y_t \cos(\pi t).$$
These coefficients are, up to scale, the real and imaginary parts of the discrete Fourier
transform coefficient $b_j = \sum_t y_t e^{-2\pi i (j/n)t}$: $\mathrm{Re}(b_j)$ is the cosine sum
above and $\mathrm{Im}(b_j)$ is the sine sum. So writing $y_t$ as a harmonic regression and taking
its DFT are the same computation viewed two ways.

## Turning the decomposition into a spectrum

To get an actual estimate of "how much of the variance of $y_t$ sits at each frequency," treat the
harmonic coefficients as random rather than fixed:
$$\beta_{1j}, \beta_{2j} \overset{\text{iid}}{\sim} N(0, \tau_j^2), \qquad \beta_{m+1} \sim N(0, \tau_{m+1}^2).$$
The variance $\tau_j^2$ attached to frequency $j/n$ *is* the spectrum in this model. Carrying this
over to the DFT scale,
$$\mathrm{Re}(b_j), \mathrm{Im}(b_j) \overset{\text{iid}}{\sim} N\!\left(0, \frac{n^2\tau_j^2}{4}\right), \qquad b_{m+1} = b_{n/2} \sim N(0, n^2\tau_{m+1}^2),$$
so that
$$|b_j|^2 \sim \frac{n^2\tau_j^2}{4}\chi_2^2 \ \ (j = 1,\dots,m), \qquad b_{m+1}^2 \sim n^2\tau_{m+1}^2 \chi_1^2.$$
Dividing by $n$ gives the periodogram, $I(j/n) = |b_j|^2/n$, and
$$I(j/n) \sim \frac{n\tau_j^2}{4}\chi_2^2 \ \ (j=1,\dots,m), \qquad I(1/2) \sim n\tau_{m+1}^2\chi_1^2.$$
This is the key fact: each periodogram ordinate is a chi-squared random variable whose *scale* is
the unknown spectral value at that frequency. A chi-squared random variable with 1 or 2 degrees of
freedom is noisy regardless of how large $n$ is — more data gives more frequencies, not less noise
per frequency. That is exactly why the raw periodogram is not, by itself, a good spectrum
estimate.

## The likelihood of the periodogram

Treating the ordinates as independent (an approximation — the Whittle likelihood), the joint
density up to a constant is
$$\left(\prod_{j=1}^m \frac1{\tau_j^2}\right)\frac1{\tau_{m+1}}\exp\left(-\frac2n\sum_{j=1}^m \frac{I(j/n)}{\tau_j^2} - \frac{I(1/2)}{2n\tau_{m+1}^2}\right),$$
giving negative log-likelihood
$$\frac2n\sum_{j=1}^m \frac{I(j/n)}{\tau_j^2} + \frac{I(1/2)}{2n\tau_{m+1}^2} + 2\sum_{j=1}^m \log\tau_j + \log\tau_{m+1}.$$
Since each $\tau_j$ must be positive, reparametrize by its log, $\alpha_j = \log\tau_j$, which
removes the positivity constraint and turns the objective into
$$\frac2n\sum_{j=1}^m I(j/n) e^{-2\alpha_j} + \frac1{2n} I(1/2) e^{-2\alpha_{m+1}} + 2\sum_{j=1}^m \alpha_j + \alpha_{m+1}.$$

## Why the unregularized fit is useless

Minimizing this objective with no further restriction, term by term, gives
$$\alpha_j = \log\sqrt{\frac{2I(j/n)}{n}} \ \ (j=1,\dots,m), \qquad \alpha_{m+1} = \log\sqrt{\frac{I(1/2)}{n}}.$$
Unwinding the log, this is just $\tau_j^2 \propto I(j/n)$: the unconstrained maximum-likelihood
estimate reproduces the periodogram itself, exactly. There is one free parameter $\tau_j$ per
frequency, so each frequency fits its own single noisy observation perfectly and nothing is
smoothed at all. Since $I(j/n)$ is genuinely noisy — its distribution never concentrates, however
much data is collected — this "estimate" is really just the data restated. The spectrum only
becomes learnable once nearby frequencies are tied together, which is what forces a penalty.

## Smoothing by penalizing roughness in the log spectrum

The fix is to penalize how rough the sequence $\alpha_1,\dots,\alpha_{m+1}$ is, using its discrete
second difference $(\alpha_{j+1}-\alpha_j) - (\alpha_j - \alpha_{j-1})$ as a measure of roughness
at $j$ — large when $\alpha$ bends sharply, zero when $\alpha$ is locally linear. Two penalties are
used, both leaving the Nyquist term $\alpha_{m+1}$ out of the sum:

Ridge (squared) penalty:
$$\frac2n\sum_{j=1}^m I(j/n)e^{-2\alpha_j} + \frac1{2n}I(1/2)e^{-2\alpha_{m+1}} + 2\sum_{j=1}^m \alpha_j + \alpha_{m+1} + \lambda\sum_{j=2}^{m-1}\big((\alpha_{j+1}-\alpha_j)-(\alpha_j-\alpha_{j-1})\big)^2.$$

Lasso (absolute-value) penalty: the same objective with the square replaced by
$\left|(\alpha_{j+1}-\alpha_j)-(\alpha_j-\alpha_{j-1})\right|$.

Both penalties are convex, and the likelihood term $I e^{-2\alpha} + 2\alpha$ is convex in $\alpha$
as well, so the whole objective is a convex program rather than something with a closed-form
minimizer. The larger $\lambda$ is, the more the fit is forced toward a smooth curve rather than
tracking every periodogram spike.

<figure>
<svg viewBox="0 0 400 240" role="img" aria-label="Raw jagged periodogram overlaid with a smooth penalized spectrum estimate">
  <line x1="40" y1="200" x2="380" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="20" x2="40" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <text x="380" y="216" text-anchor="end" font-size="12" fill="currentColor">frequency 1/2</text>
  <text x="40" y="216" text-anchor="start" font-size="12" fill="currentColor">0</text>
  <text x="14" y="26" font-size="12" fill="currentColor">high</text>
  <text x="14" y="200" font-size="12" fill="currentColor">low</text>
  <polyline points="40,185 48,150 57,60 66,175 75,190 84,120 96,95 105,180 114,150 124,192 
    134,165 144,110 154,140 164,185 176,120 188,175 200,145 210,105 222,178 234,160 
    246,150 258,120 266,150 278,185 290,140 302,175 314,155 326,110 338,180 350,160 362,190 380,182"
    fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1"/>
  <path d="M 40,178 C 50,160 54,60 60,45 C 68,80 82,140 96,112 C 108,90 116,150 130,150
    C 140,150 148,150 154,132 C 166,150 178,155 210,148 C 240,158 250,158 266,158
    C 290,158 305,166 326,166 C 350,170 365,172 380,174"
    fill="none" stroke="#d9720a" stroke-width="2.5"/>
  <text x="60" y="35" text-anchor="middle" font-size="11" fill="currentColor">business cycle</text>
  <text x="200" y="126" text-anchor="middle" font-size="11" fill="currentColor">seasonal harmonics</text>
  <text x="280" y="200" font-size="11" fill="currentColor" fill-opacity="0.7">raw periodogram</text>
  <text x="280" y="185" font-size="11" fill="#d9720a">smoothed estimate</text>
</svg>
<figcaption>The raw periodogram (thin line) is noisy at every frequency, including where there is
no real structure; the penalized fit (heavy line) is what turns it into a spectrum with a
legible low-frequency peak and a decaying series of seasonal harmonics.</figcaption>
</figure>

## Implementing it: the periodogram, then the convex program

The periodogram is computed directly from an FFT. Written to handle both even and odd $n$ (odd $n$
has no Nyquist term, since $1/2$ is then not a Fourier frequency):

```python
def periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)

    if n % 2 == 0:  # even n
        fourier_freqs = np.arange(1/n, (1/2) + (1/n), 1/n)  # includes 1/2
    else:  # odd n
        fourier_freqs = np.arange(1/n, 1/2, 1/n)  # excludes 1/2

    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m + 1]) ** 2) / n
    return fourier_freqs, pgram_y
```

The ridge-penalized fit for even $n$, following the objective above term for term (the last two
frequency slots hold the special $\alpha_{m+1}$ contribution):

```python
def spectrum_n_even_estimator_ridge(y, lambda_val):
    freq, I = periodogram(y)
    n = len(y)
    m = (n // 2) - 1
    alpha = cp.Variable(n // 2)

    I_1_to_m = I[0:(m - 1)]
    I_m_plus_1 = I[m]

    neg_likelihood_term = (
        cp.sum(cp.multiply((2 * I_1_to_m / n), cp.exp(-2 * alpha[0:(m - 1)])) + 2 * alpha[0:(m - 1)])
        + cp.multiply((I_m_plus_1 / (2 * n)), cp.exp(-2 * alpha[m])) + alpha[m]
    )
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))

    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    cp.Problem(objective).solve()
    return alpha.value, freq
```

The lasso version is identical except `cp.square(...)` becomes `cp.abs(...)`. For an odd $n$ there
is no special last term, so the objective collapses to a single sum over all $m$ frequencies,
`cp.sum(cp.multiply((2 * I / n), cp.exp(-2 * alpha)) + 2 * alpha)`, plus the same roughness penalty
on the full vector $\alpha$.

## Reading the fit: business cycle versus seasonal effects

Fitting the ridge model to the month-over-month growth rate ($n = 1272$, even) with $\lambda =
5000$, and the lasso model with $\lambda = 100$ (values chosen by inspection, not by a stated
selection rule), gives a smoothed $\hat\tau$ curve with a clear sequence of peaks. Plotting
$\log(n/2) + 2\hat\alpha$ against the log periodogram shows the fit tracking the low-frequency
trend of the periodogram while ignoring most of its spike-to-spike noise — exactly the smoothing
the penalty is built to do.

The peaks themselves are interpretable. For the ridge fit, the lowest-frequency peak sits at
frequency $\approx 0.0252$, a period of about $39.75$ months, or roughly $3.31$ years — this is
read as a "business cycle frequency." The remaining peaks (periods of roughly 12, 9, 6, 4, 3.5,
3, 2.4, and 2 months) line up with harmonics of the annual cycle, and are read as seasonal and
calendar effects rather than economic structure. The lasso fit gives a matching first peak (period
$\approx 42.4$ months) and a similar sequence of harmonic peaks after it. Looking at the raw
periodogram alone, on either the linear or the log scale, it is not obvious that any of this
structure is there — the seasonal peaks dominate visually, and there is no clear sign of the
business-cycle frequency until the roughness penalty separates it from the noise.

## Removing the seasonal effects: a year-over-year growth rate

To see the business cycle more directly, the growth rate is redefined using a twelve-month lag
instead of a one-month lag:
$$y_t = 100\left(\log I_t - \log I_{t-12}\right).$$
This differencing removes the annual seasonal pattern directly (subtracting the value exactly one
year earlier cancels a purely annual cycle), leaving $n = 1261$ observations — now an odd sample
size, so the model is the odd-$n$ version with no special Nyquist term.

Refitting the ridge and lasso models to this series gives a spectrum with one dominant peak.  For
the ridge fit, the leading peak is at frequency $\approx 0.0214$, a period of about $46.7$ months
— close to four years — and is read directly as the business cycle. All the other peaks found by
the peak-finder are much smaller than this one, in contrast to the month-over-month series where
several seasonal peaks were comparable in size to the business-cycle peak. The lasso fit again
gives a matching leading peak (period $\approx 42.0$ months) with the same pattern of small
remaining peaks. Twelve-month differencing has done the work that the smoothing penalty alone
could not: it removed the seasonal structure at the source, so what is left in the spectrum is
mostly the slower business-cycle fluctuation.

## Sources

- `docs/statistics/berkeley/stat153/spring-2025/Lab7.md` — Berkeley STAT 153, Spring 2025, Lab 7
  ("Spectrum Model applied to a FRED dataset"), converted from `Lab7.ipynb`
  ([source](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab7.ipynb),
  CC BY 4.0). This is the sole input for the chapter; all equations, code, and numerical results
  above are drawn from it directly.
- The lab states that it follows Section 6.4 of James D. Hamilton, *Time Series Analysis*, for
  this analysis, and points the reader there for more on interpreting the spectral estimates —
  that section is referred to but was not supplied as material for this chapter.
- The dataset is FRED's "Industrial Production: Total Index" series (`IPB50001N`), supplied to the
  lab as a CSV (`IPB50001N-06March2025FRED.csv`) not included in the material given here; only the
  printed head of the data and the numerical results in the notebook were available.

---

[← 97. High-dimensional regression for change-points](97-high-dimensional-regression-for-change-points.md) · [Contents](index.md) · [99. Sinusoid, Yule, and AR(2) Models →](99-sinusoid-yule-and-ar-2-models.md)
