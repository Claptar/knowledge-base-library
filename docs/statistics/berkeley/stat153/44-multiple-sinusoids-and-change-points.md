---
title: "44. Multiple Sinusoids and Change-Points"
course: "Berkeley Stat 153 Fall 2024"
chapter: 44
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 44. Multiple Sinusoids and Change-Points

## What this covers

Two Berkeley STAT 153 code lectures push the same idea past the single-parameter case: a
regression model has one linear part, fit instantly by least squares, and one non-linear "knob"
that has to be located by search. Here the knob is let multiply — several sinusoid frequencies at
once in a model for the yearly sunspot number, and several change-of-slope points at once in a
model for the logarithm of California's population — and the chapter asks what changes when it
does: how the search gets more expensive, how much the fit actually improves, and how the same
Bayesian machinery that gave a credible interval for one parameter extends to several. It assumes
ordinary least squares (design matrices, RSS, degrees of freedom), the discrete Fourier transform
and periodogram as a fast route to the RSS of a single sinusoid, and the mechanics of Bayesian
linear regression — sampling $\sigma$ from a $\chi^2$ draw and $\beta$ from a multivariate normal
draw, under a reference prior that is used here without re-derivation.

## The shared recipe

Both examples have the same shape. The model is linear in a coefficient vector $\beta$ once one or
more non-linear parameters $\theta$ (a frequency, a change-point) are fixed:
$$
y_t = X_\theta \beta + \epsilon_t, \qquad \epsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2).
$$
For any fixed $\theta$, $X_\theta$ is a known matrix and $\beta$ is estimated by ordinary least
squares, so define the **profile residual sum of squares**
$$
\mathrm{RSS}(\theta) = \min_\beta \sum_t \big(y_t - (X_\theta\beta)_t\big)^2,
$$
computed in practice by literally fitting the regression at each candidate $\theta$ and summing
the squared residuals. The point estimate $\hat\theta$ minimizes $\mathrm{RSS}(\theta)$. Because
$\theta$ enters non-convexly — inside a cosine, or at the kink of a ReLU — this minimization is a
grid search, not a gradient method.

For uncertainty, both lectures treat $\theta$ as having an (unnormalized, and here presented
directly rather than derived) posterior
$$
\pi(\theta \mid y) \ \propto\ \big|X_\theta^\top X_\theta\big|^{-1/2}
\left(\frac{1}{\mathrm{RSS}(\theta)}\right)^{(n-p)/2},
$$
with $p$ the number of columns of $X_\theta$. Both work on the log scale to avoid overflow when
the exponent $(n-p)/2$ is in the hundreds,
$$
\log \pi(\theta\mid y) = \frac{p-n}{2}\log \mathrm{RSS}(\theta) - \tfrac12 \log\big|X_\theta^\top
X_\theta\big| + \text{const},
$$
exponentiate after subtracting the maximum (to avoid overflow the other way), and normalize by the
sum over the grid to get an honest discrete probability distribution over the candidate values of
$\theta$. From that distribution: a credible interval is the narrowest window of grid points whose
cumulative probability clears some target (95% below), and — because $\theta$ now has an actual
normalized probability on a finite grid — literal posterior samples of $\theta$ by a weighted
categorical draw.

One thing decides how much of this machinery is actually needed: if every candidate $\theta$ on the
grid gives the *same* $X_\theta^\top X_\theta$ (same determinant), that factor is a constant across
$\theta$ and can be dropped from the comparison — the credible interval then comes straight off
$\mathrm{RSS}$, or equivalently off a periodogram. That happens for a sinusoid restricted to Fourier
frequencies. It does not happen on a finer frequency grid, and it does not happen for a
change-point, so the determinant has to be tracked explicitly in both of those cases.

## One sinusoid: the sunspot series

The data are $n=325$ yearly values of the sunspot number, read from `SN_y_tot_V2.0.csv`. The model
is
$$
y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t,
$$
with $f$ — cycles per year, whose reciprocal is a period in years — the one non-linear parameter.

Evaluating $\mathrm{RSS}(f)$ by literally re-fitting the regression at every candidate $f$ does not
scale to a dense grid. Restricted to the **Fourier frequencies** $f=j/n$, though, it collapses to a
single FFT, because at those frequencies
$$
\mathrm{RSS}(j/n) = \sum_t (y_t-\bar y)^2 \; - \; 2\,I(j/n), \qquad I(j/n) = \frac{|b_j|^2}{n},
$$
where $b_j$ is the $j$-th discrete Fourier transform (DFT) coefficient (defined precisely below)
and $I$ is the **periodogram**. Minimizing $\mathrm{RSS}$ over Fourier frequencies is exactly
maximizing the periodogram:

```python
def periodogram(y):
    fft_y = np.fft.fft(y)          # O(n log n)
    n = len(y)
    fourier_freqs = np.arange(1/n, 1/2, 1/n)
    pgram_y = (np.abs(fft_y[1:len(fourier_freqs)+1]) ** 2) / n
    return fourier_freqs, pgram_y
```

The periodogram of the sunspot series peaks at $j=30$: $\hat f = 30/325 \approx 0.0923$, an
estimated period of $1/\hat f \approx 10.83$ years — close to, but not exactly, the traditional
11-year sunspot cycle.

### Uncertainty on the Fourier grid

Applying the shared recipe with $p=3$ and (as noted above) no determinant term, since it is
constant across Fourier frequencies, gives a posterior over $j=1,\dots$ concentrated around
$j=30$. The narrowest window with at least 95% posterior mass is $j\in\{29,30,31\}$, i.e.
$$
f \in [0.0892,\ 0.0954], \qquad \text{period} \in [10.48,\ 11.21]\ \text{years}.
$$
Converted to a symmetric-looking summary around the point estimate, in days:
$$
[\,10.83\text{ years} - 127\text{ days},\ \ 10.83\text{ years} + 136\text{ days}\,].
$$
The interval is symmetric in $f$ but not in the period $1/f$ — inversion is non-linear, so a
symmetric range of frequencies maps to an asymmetric range of periods.

### A finer grid narrows it

Fourier resolution is capped at $1/n \approx 0.00308$ regardless of how informative the data
actually are. Repeating the calculation on a much denser grid, $f \in [0.01, 0.5)$ in steps of
$0.0001$, now needs the determinant term explicitly (via `np.linalg.slogdet`, since $X_f^\top X_f$
genuinely varies with $f$ off the Fourier grid), and finds $\hat f \approx 0.0909$, a period of
about $11.00$ years, with 95% credible interval
$$
[\,11\text{ years} - 13\text{ days},\ \ 11\text{ years} + 13\text{ days}\,],
$$
roughly ten times narrower in days than the Fourier-grid interval. Restricting to Fourier
frequencies is computationally convenient — an FFT rather than a numerical search, no determinant
to track — but it costs real precision.

## More than one sinusoid

The model with $k$ sinusoids is
$$
y_t = \beta_0 + \sum_{j=1}^{k}\Big(\beta_{2j-1}\cos(2\pi f_j t) + \beta_{2j}\sin(2\pi f_j t)\Big) +
\epsilon_t,
$$
with $\mathrm{RSS}(f_1,\dots,f_k)$ computed the same way, generalized to several frequency columns
in the design matrix. Searching over $(f_1,f_2)$ jointly on a grid has one wrinkle: swapping the
labels $f_1 \leftrightarrow f_2$ (with the coefficients swapped correspondingly) gives exactly the
same fit, so half of any full grid is wasted work. The lecture's fix is to keep only the
non-decreasing combinations:

```python
mask = (X <= Y)              # kill (f1, f2) / (f2, f1) duplicates
xf, yf = X[mask], Y[mask]
```

Searching $(f_1,f_2)$ over $[0,0.15]^2$ (frequencies above 0.15 were judged implausible for this
series) finds $(\hat f_1,\hat f_2) = (0.0907, 0.0998)$, periods $(11.03, 10.02)$ years,
$\mathrm{RSS}=702{,}139$ — down from $866{,}098$ for one frequency — and $R^2=0.436$, up from
$0.304$. A three-frequency search (on a coarser $200$-point-per-axis grid, since even with the
ordering mask a three-dimensional grid is expensive) finds
$(\hat f_1,\hat f_2,\hat f_3) = (0.0912, 0.0935, 0.1003)$, periods $(10.96, 10.70, 9.97)$ years,
$\mathrm{RSS} = 580{,}238$, $R^2 = 0.534$. One of the six coefficients in that fit — the sine term
at the third frequency — is not significant at the 5% level ($p=0.605$), a hint that the third
frequency is doing comparatively little work. Across one, two and three frequencies the RSS falls
monotonically, $866{,}098 \to 702{,}139 \to 580{,}238$, as it must once each new sinusoid is a free
addition to a nested model.

### Fourier frequencies versus a free search

Ranking the Fourier frequencies by periodogram height gives, in order, $j = 30, 31, 29, 32, 3,
27,\dots$. Using just the top three of these, $(30/n, 31/n, 29/n)$, gives $\mathrm{RSS} =
765{,}576$ — worse than the freely-searched three-frequency fit ($580{,}238$) but better than the
freely-searched single frequency ($866{,}098$). Restricting the search to a handful of Fourier
frequencies is a reasonable shortcut, not the best attainable fit. Fitting the top five Fourier
frequencies ($j=30,31,29,32,3$) raises $R^2$ to $0.560$, but three of the ten coefficients — the
cosine terms at $j=31$ and $j=32$, and the sine term at $j=3$ — are not significant at the 5%
level, so the in-sample gain is partly cosmetic.

### Does a better in-sample fit forecast better?

Training on the first 275 observations and testing on the last 50, a model built from four Fourier
frequencies ($30/n, 31/n, 29/n, 32/n$) gives a test MSE of about $2254$. The notebook notes, without
displaying the comparison run, that using the freely-optimized three-frequency set instead gives
the best prediction accuracy among the options tried — a caution that the frequency set minimizing
in-sample RSS is not automatically the one that generalizes best.

## The discrete Fourier transform

For a series $y_0,\dots,y_{n-1}$, the DFT is $b_0,\dots,b_{n-1}$ with
$$
b_j = \sum_{t=0}^{n-1} y_t \exp\!\left(-\frac{2\pi i\, jt}{n}\right),
$$
a complex number whose real part is $\sum_t y_t\cos(2\pi (j/n) t)$ and whose imaginary part is
$-\sum_t y_t \sin(2\pi (j/n) t)$. Its squared magnitude divided by $n$ is exactly the periodogram
value $I(j/n)$ used above. On the small check series $y=(1,-5,3,10,-5,1,6)$, the $j=0$ coefficient
is real by construction — $\sin(0)=0$ for every term — and equals the sum of the series,
$b_0 = \sum_t y_t = 11$; computing $b_3$ two ways, once via `np.fft.fft` and once by summing
$y_t\cos(2\pi\cdot\frac37 t)$ and $y_t\sin(2\pi\cdot\frac37 t)$ directly, is the notebook's way of
checking the formula against the fast implementation before trusting the periodogram calculations
above.

## A different knob: where does the growth rate change?

The second dataset is the resident population of California, 1900–2024 ($n=125$), taken in logs so
that a constant proportional growth rate shows up as a straight line: with
$y_t=\beta_0+\beta_1 t$, consecutive years satisfy $\mathrm{pop}_{t+1}/\mathrm{pop}_t=e^{\beta_1}
\approx 1+\beta_1$ for small $\beta_1$, so $\beta_1$ is (to first order) the annual growth rate. A
plain linear regression on $\log(\text{population})$ gives slope $0.0269$ — a claimed uniform
$2.69\%$ per year, $R^2=0.950$ — but the plotted series bends: growth was visibly faster than that
in the early decades and slower in recent ones, which a single straight line cannot represent.

### The change-of-slope model

The fix is a **broken-stick** (change-of-slope) model with one kink at an unknown time $c$:
$$
y_t = \beta_0 + \beta_1 t + \beta_2 (t-c)_+ + \epsilon_t, \qquad (t-c)_+ = \max(t-c,\,0).
$$
Before $c$ the slope is $\beta_1$; after it, the slope is $\beta_1+\beta_2$.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A kinked broken-stick trend bowing above the single straight-line fit between the same endpoints, with the slope change marked at c">
  <line x1="30" y1="195" x2="320" y2="195" stroke="currentColor" stroke-width="1.2"/>
  <text x="322" y="199" font-size="12" fill="currentColor">t</text>
  <line x1="45" y1="170" x2="300" y2="60" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5,4" opacity="0.6"/>
  <path d="M 45 170 L 170 100 L 300 60" fill="none" stroke="currentColor" stroke-width="2.2"/>
  <line x1="170" y1="100" x2="170" y2="195" stroke="currentColor" stroke-width="1" stroke-dasharray="2,3" opacity="0.6"/>
  <text x="170" y="209" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="70" y="128" font-size="12" fill="currentColor">slope &#946;&#8321;</text>
  <text x="210" y="72" font-size="12" fill="currentColor">slope &#946;&#8321;+&#946;&#8322;</text>
  <text x="222" y="150" font-size="11" fill="currentColor" opacity="0.75">single-line fit</text>
</svg>
<figcaption>The broken-stick mean function: a straight segment of slope β₁ up to the change-point
c, continuing with slope β₁+β₂ after it. Because the early slope is steeper than the single-line
average, the true kinked path bows above a straight line drawn between the same two endpoints.</figcaption>
</figure>

Applying the shared recipe with $\theta=c$ ranging over the integer grid $1,\dots,n$ and $p=3$
finds $\hat c = 66$, i.e. **1965**. Refitting at $\hat c$ gives $\hat\beta_1 = 0.038$ (a $3.8\%$
annual growth rate before 1965) and $\hat\beta_1+\hat\beta_2 = 0.038-0.024=0.014$ (a $1.4\%$ rate
after) — growth slowed to well under half of its earlier pace. The residual scale is
$\hat\sigma_{\mathrm{MLE}}=0.0529$, $\hat\sigma_{\mathrm{unbiased}}=0.0535$.

### How sure are we about 1965?

Here $X_c^\top X_c$ genuinely changes with $c$, so the determinant term in the shared recipe is
tracked explicitly. The resulting 95% credible interval for the change-point is
$$
c \in [63, 69], \qquad \text{i.e. the years } [1962,\ 1968].
$$

### Sampling the whole posterior

Because $c$ has an honest normalized probability on a finite grid, $4000$ draws of $c$ were taken
by weighted categorical sampling. Each drawn $c$ was then completed to a full parameter draw by
sampling from the conditional Bayesian-linear-model posterior given that $c$ — presented directly
in the lecture rather than derived:

```python
chirv = rng.chisquare(df = n - p)
sig_sample = np.sqrt(np.sum(md_c.resid ** 2) / chirv)         # posterior draw of sigma
covmat = (sig_sample ** 2) * np.linalg.inv(X.T @ X)
beta_sample = rng.multivariate_normal(mean = md_c.params, cov = covmat)   # posterior draw of beta
```

The $4000$ joint draws of $(c,\beta_0,\beta_1,\beta_2,\sigma)$ give, by simply looking at their
empirical distribution, posterior summaries for anything derived from them:

| quantity | posterior mean (or estimate) | 95% credible interval |
|---|---|---|
| change-point (year) | 1965.3 | $[1964, 1967]$ |
| growth rate before $c$ | $3.80\%$ | $[3.73\%,\ 3.87\%]$ |
| growth rate after $c$ | $1.39\%$ | $[1.30\%,\ 1.48\%]$ |
| $\sigma$ | $0.0540$ | $[0.0478,\ 0.0612]$ |

The two growth-rate intervals are pinned down tightly even though the change-point's exact year is
uncertain by a few years either way — plotting the fitted broken-stick line for all $4000$ draws on
top of the data gives a bundle of nearly-overlapping lines, the visual form of "the location of the
kink is a little uncertain, but the two regimes it separates are not."

## More than one change of slope

The model with two kinks is
$$
y_t = \beta_0 + \beta_1 t + \beta_2(t-c_1)_+ + \beta_3(t-c_2)_+ + \epsilon_t.
$$
A joint grid search over $(c_1,c_2)$ finds the minimum at time-indices $(62, 101)$, i.e. the years
**1961** and **2000**, with $\mathrm{RSS}=0.199$. That is a real improvement over the single
change-point fit: since $\mathrm{RSS} = n\,\hat\sigma_{\mathrm{MLE}}^2$, the one-change-point RSS
works out to $125 \times 0.0529^2 \approx 0.350$, so the second kink cuts the residual sum of
squares by roughly $43\%$.

A third change-point was fit by an exhaustive three-dimensional grid search — "this took 14
minutes to run," per the lecture notes, because the cost of a joint grid over $p$ change-points
scales like $n^{p}$. The minimizing triple was $(c_1,c_2,c_3) = (1924,\ 1964,\ 2000)$, with
$\mathrm{RSS} \approx 0.101$, roughly halving the two-change-point RSS again — but the resulting
fitted curve is, in the lecture's own words, "quite close" to the two-change-point fit. Each extra
kink can only reduce the RSS further, but the improvement shrinks while the cost of finding it by
brute-force grid search keeps growing — exactly the trade-off already seen when moving from one
sinusoid to three.

## Sources

- Berkeley STAT 153, Fall 2025, "Code Lecture Nine" — the sunspot-frequency material, from
  `docs/statistics/berkeley/stat153/fall-2025/CodeLectureNine153248Fall2025/01-sunspots-dataset.md`
  (single-sinusoid model, periodogram, Fourier-grid and fine-grid Bayesian intervals) and
  `.../02-fitting-more-sinusoids-to-the-sunspots-data.md` (two- and three-frequency grid search,
  Fourier-frequency comparison, train/test check, and the DFT definition), CC BY 4.0, converted
  from `CodeLectureNine153248Fall2025.ipynb`.
- Berkeley STAT 153, Spring 2025, "Code Lecture Nine" — the California-population material, from
  `docs/statistics/berkeley/stat153/spring-2025/CodeLectureNine153248Spring2025.md` (broken-stick
  change-of-slope model, single- and multiple-change-point grid search, and the full posterior
  sampling scheme), CC BY 4.0, converted from `CodeLectureNine153248Spring2025.ipynb`.
- No slides, transcript, or problem set were supplied for either lecture; every definition,
  formula, code fragment and numerical result above comes from these three notebook files.
- Presented directly rather than derived, in both notebooks alike: the Bayesian posterior formula
  for the non-linear parameter, and the reference-prior recipe for sampling $\sigma$ (via a
  $\chi^2$ draw) and $\beta$ (via a multivariate normal draw) conditional on it.
- The notebooks' own plots (the raw series, the periodogram, the RSS and log-posterior curves, the
  fitted-line overlays, and the posterior-sample bundles) were omitted in the source conversion and
  are described here only from the surrounding text and code, not from the images themselves.
- The source notebook's printed "RSS with five Fourier frequencies" figure is a copy of the
  three-frequency RSS (the code re-used the wrong model's residuals) and is not reported here;
  only that model's $R^2$, computed independently, is used.
- The small DFT check in the second notebook (`b_cos`, `b_sin`, and the raw `np.fft.fft` output for
  the seven-point example series) has no printed output in the supplied conversion; only $b_0$,
  which follows directly from the stated data, is reported here.

---

[← 43. Smoothing Trend, Variance, and Spectrum](43-smoothing-trend-variance-and-spectrum.md) · [Contents](index.md) · [45. Prediction Uncertainty in AR Models →](45-prediction-uncertainty-in-ar-models.md)
