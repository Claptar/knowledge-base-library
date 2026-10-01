---
title: "40. Applying the Spectrum Smoother"
course: "Berkeley Stat 153"
chapter: 40
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 40. Applying the Spectrum Smoother

## What this covers

The previous lectures built a model for the periodogram — the DFT-based estimate of a stationary
series' spectral density — and a penalized-likelihood method for smoothing it. This chapter is the
"code lecture" that runs that machinery on five real time series: sunspot counts, the Southern
Oscillation Index, earthquake-vibration control data, an industrial-production index, and EEG
brainwaves. It assumes the reader already has the periodogram, the exponential sampling model for
it, and ridge/LASSO regularization; the point here is what the method finds when it is pointed at
data someone actually cared about, and how much the smoothing parameter has to be adjusted dataset
to dataset. Two of the five applications (industrial production, EEG) were run in only one of the
two years this material was taught; the other three (sunspots, SOI, earthquake) were run in both,
and are given here in the fuller of the two treatments.

## Recap: periodogram, spectrum, and the smoothed estimator

For a stationary series $y_1, \dots, y_n$ with DFT coefficients $b_0, \dots, b_{n-1}$, the model
behind the periodogram is
$$\text{Re}(b_j),\ \text{Im}(b_j) \overset{\text{i.i.d.}}{\sim} N(0, \gamma_j^2), \qquad j = 1, \dots, m,$$
with $m = (n-1)/2$ (so $n$ needs to be odd for $m$ to be a whole number). Writing the periodogram as
$I(j/n) = |b_j|^2/n$, this is equivalent to
$$I(j/n) \overset{\text{ind}}{\sim} f(j/n)\,\eta_j, \qquad \eta_j \overset{\text{i.i.d.}}{\sim} \text{Exp}(1),$$
where $f(j/n) = 2\gamma_j^2/n$ is the **power** at frequency $j/n$ — the mean of the periodogram
there. Treating $f$ as a function on $[0, 1/2]$ by joining the values $f(j/n)$ gives the **power
spectral density**.

```python
def periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, 1/2, 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2) / n
    return fourier_freqs, pgram_y
```

The raw periodogram is a very noisy estimate of $f$ — each $I(j/n)$ is an *independent* draw with
mean $f(j/n)$ and no averaging across neighbouring frequencies. To smooth it, write $\alpha_j =
\log \gamma_j$ and minimize the negative log-likelihood of the exponential model plus a roughness
penalty on the sequence $\alpha_1, \dots, \alpha_m$:
$$\sum_{j=1}^m \left(\frac{nI(j/n)}{2} e^{-2\alpha_j} + 2\alpha_j\right) + \lambda \sum_{j=2}^{m-1}\Big((\alpha_{j+1}-\alpha_j)-(\alpha_j-\alpha_{j-1})\Big)^2$$
(ridge), or with the squared term replaced by an absolute value (LASSO). The penalized term is the
discrete second difference of $\alpha$ — its local curvature. Squaring and summing it (ridge) shrinks
toward a spectrum that is smooth everywhere; summing the absolute value (LASSO) instead lets the
fitted log-spectrum be piecewise linear, holding a narrow peak sharply while staying flat elsewhere.
Once $\alpha_j$ is estimated, the fitted power is recovered by $f(j/n) = \frac{2}{n}e^{2\alpha_j}$.

```python
def spectrum_estimator_ridge(y, lambda_val):
    freq, I = periodogram(y)
    m, n = len(freq), len(y)
    alpha = cp.Variable(m)
    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2 * alpha)
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    problem = cp.Problem(cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty))
    problem.solve(solver=cp.MOSEK)
    return alpha.value, freq

# spectrum_estimator_lasso is identical except cp.square(...) becomes cp.abs(...)
```

Both are convex programs (solved here with MOSEK via `cvxpy`), and neither has a default $\lambda$:
each application below tunes it by eye. The values used are wildly different in scale —

| Dataset | series length $n$ | ridge $\lambda$ | LASSO $\lambda$ |
|---|---|---|---|
| Sunspots | — | 100–200 | 10 |
| Southern Oscillation Index | 1,790 | 50,000 | 100 |
| Earthquake vibration (OL/CL) | 10,000 | 100,000 | 1,000 |
| Industrial-production growth rate | 1,261 | 5,000 | 100 |
| EEG (eyes open/closed) | 9,760 | 1,000,000 | 1,000 |

— which is itself the practical lesson: the right amount of smoothing depends on the scale of
$I(j/n)$ and on how peaked the true spectrum is, not on $n$ alone, so it has to be chosen per
dataset rather than fixed once.

## Application 1: sunspot numbers

The first series is a record of annual total sunspot counts. Its raw periodogram is rough and
wiggly, as expected, and so is its log. Fitting the ridge and LASSO spectrum estimators to it and
overlaying the fitted power spectrum on the periodogram shows a single dominant mode — but the mode
is not a narrow spike at one frequency. It is spread across a whole band of neighbouring
frequencies, all contributing to it:

> "There is a whole band of frequencies which contribute towards the mode in the power spectrum."

This is the point of smoothing the periodogram rather than reading peaks off it directly: a single
raw periodogram ordinate at the "true" frequency of an underlying cycle is itself noisy (it is one
$\text{Exp}(1)$ draw scaled by the true power), so a real periodic component shows up as elevated
power over a band around it, not as one exact spike.

## Application 2: the Southern Oscillation Index and El Niño

The Southern Oscillation Index (SOI) is computed from the difference in surface air pressure
between Tahiti and Darwin, and tracks El Niño / La Niña: sustained negative SOI corresponds to an El
Niño event. El Niño and La Niña are known to recur irregularly, roughly every two to seven years
(Trenberth, "The definition of El Niño", 1997). The monthly SOI series used here runs from 1876 to
2025 ($n = 1{,}790$).

Fitting the ridge estimator ($\lambda = 50{,}000$) and LASSO estimator ($\lambda = 100$) to the SOI
periodogram and searching the smoothed log-spectrum for local maxima (`scipy.signal.find_peaks`)
gives a dominant peak at

$$\frac{1}{\text{frequency}} \approx 52.6 \text{ months} \approx 4.5 \text{ years},$$

with smaller peaks at periods of roughly 9.6, 6.9, 5.6, 4.2, 3.2, 2.8, 2.5, 2.3, and 2.1 months.
The dominant period sits squarely inside the known two-to-seven-year recurrence window for El Niño,
so the spectrum recovers, from the data alone, the periodicity the phenomenon is known for.

## Application 3: earthquake vibration and a control system

The next dataset (from a Mathworks tutorial on frequency-domain analysis) is acceleration
measurements taken on the first floor of a three-story test structure under earthquake conditions,
with an *active mass driver* (AMD) — a mass on the top floor that a control system moves to damp
building sway. Two 10,000-point recordings exist: one **open loop** (OL, driver present but control
system off) and one **closed loop** (CL, control system active).

Fitting the ridge and LASSO spectrum estimators to each series ($\lambda_{\text{ridge}} = 100{,}000$,
$\lambda_{\text{LASSO}} = 1{,}000$) and comparing the two smoothed log-power-spectra side by side
shows a clear structural difference that is not obvious from the two raw time series:

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Schematic comparison of the open-loop and closed-loop vibration power spectra, showing the control system removing one harmonic and lowering overall power">
  <line x1="30" y1="190" x2="320" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="320" y="207" text-anchor="end" font-size="12" fill="currentColor">frequency</text>
  <text x="34" y="20" font-size="12" fill="currentColor">log power</text>
  <path d="M30,190 C60,190 60,60 90,60 C120,60 120,190 150,190 C170,190 170,100 190,100 C210,100 210,190 230,190 C250,190 250,150 270,150 C290,150 290,190 310,190"
        fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M30,190 C60,190 60,90 90,90 C120,90 120,190 150,190 C170,190 170,130 190,130 C210,130 210,190 230,190 C250,190 280,190 310,190"
        fill="none" stroke="orangered" stroke-width="2"/>
  <text x="95" y="52" font-size="12" fill="currentColor">OL</text>
  <text x="195" y="122" font-size="12" fill="orangered">CL</text>
  <text x="272" y="142" font-size="11" fill="currentColor">3rd harmonic (OL only)</text>
</svg>
<figcaption>Schematic of the finding, not the fitted curves themselves: the open-loop (OL) spectrum
has three harmonics; the closed-loop (CL) spectrum, with the control system active, has only two
and lower peaks throughout.</figcaption>
</figure>

There are three peaks (harmonics) in the open-loop spectrum and only two in the closed-loop
spectrum. The control system reduces the overall power of the vibration *and* eliminates one
harmonic component entirely — it does not just damp the vibration, it also brings it closer to a
single pure sinusoid. As the lecture puts it:

> "The main point is that the differences between the two time series is much better summarized
> using their power spectra, compared to the raw data."

## Application 4a: industrial production and the business cycle

FRED's "Industrial Production: Total Index" ($I_t$, monthly, not seasonally adjusted) has a strong
increasing trend, so the stationary spectrum model cannot be applied to the raw series directly.
Instead the lecture works with the annual (12-month) log growth rate,
$$y_t = 100\big(\log I_t - \log I_{t-12}\big),$$
which removes the trend and leaves $n = 1{,}261$ observations (conveniently odd, as the model needs
for $m = (n-1)/2$ to be an integer). Fitting the ridge ($\lambda = 5{,}000$) and LASSO ($\lambda =
100$) estimators to this series and searching for peaks in the smoothed log-spectrum gives a
dominant period of about

$$45 \text{ months} \approx 3.75 \text{ years},$$

with further, smaller peaks at roughly 8.9, 5.1, 4.7, 3.5, 2.7, 2.6, and 2.2 months. Economists take
this roughly-4-year periodicity in growth rates as evidence for a **business cycle** (see Hamilton's
time-series textbook, §6.4, for more on this example).

## Application 4b: EEG alpha rhythm, eyes open vs. eyes closed

The other dataset run only in the other year's version of this lecture is EEG data from the
PhysioNet motor-movement/imagery database: 64-channel recordings from volunteers, sampled at 160 Hz.
One channel is picked for a single subject, comparing a recording with eyes open to one with eyes
closed ($n = 9{,}760$ each). A known finding in cognitive neuroscience is that the power of the
occipital **alpha band** (around 10 Hz) rises when the eyes are closed relative to when they are
open (Hohaia et al., 2022).

Fitting the ridge ($\lambda = 1{,}000{,}000$) and LASSO ($\lambda = 1{,}000$) spectrum estimators to
each recording and overlaying the two smoothed log-spectra shows them agreeing away from one region,
and diverging sharply near a single frequency. Locating that peak in the eyes-closed spectrum and
converting from normalized frequency to Hertz by multiplying by the sampling rate,
$$\left(\frac{\text{peak index}}{n}\right) \times 160\ \text{Hz} \approx 10.03\ \text{Hz},$$
recovers the alpha band almost exactly. The two power spectra — not the two raw traces — are what
makes this visible: the raw eyes-open and eyes-closed EEG traces look like generic noisy signals,
and the difference between them only becomes legible once each is expressed in the frequency domain.

## What the five applications share

In every case, the same three-line recipe is applied: compute the periodogram, fit the penalized
(ridge or LASSO) estimator of the log-spectrum, and read the result either as a picture (sunspots,
earthquake, EEG) or as a located peak converted back to a period or frequency (SOI, industrial
production, EEG). The one thing that changes from dataset to dataset, other than the data, is the
penalty $\lambda$ — chosen each time so the fitted curve tracks the real structure in the periodogram
without still being noisy.

## Sources

- Fall 2025 offering, `CodeLectureFifteen153248Fall2025.ipynb` (berkeley-stat153, CC BY 4.0):
  Application One (Sunspots), Application Two (Southern Oscillation Index), Application Three
  (Quake Vibration), and Application Four (FRED industrial-production index) — used for the
  model recap and for the sunspots, SOI, earthquake and industrial-production sections, as the
  fuller of the two years' treatments (it alone carries the "Spectrum Model" recap reproduced
  above).
- Spring 2025 offering, `CodeLectureFifteen153248Spring2025.ipynb` (berkeley-stat153, CC BY 4.0):
  Application Four (EEG Motor Movement Dataset) — used for the EEG section, which the fall
  offering does not contain. The spring offering's own Sunspots, SOI and Quake-Vibration
  applications are the same analyses (same code, same datasets, minor $\lambda$ differences) and
  are not repeated separately.
- No slide deck, transcript, or problem set was supplied for this lecture; both inputs listed
  above are Jupyter-notebook conversions ("code lectures"), and all figures referred to in them
  were omitted from the conversion and are not reproduced here except as the one schematic diagram
  above, which is not a copy of the original plot.
- External sources the lecture points to but does not itself contain: Trenberth, "The definition
  of El Niño" (1997); the Mathworks tutorial "Practical Introduction to Frequency-Domain Analysis";
  Hamilton, *Time Series Analysis*, §6.4; Hohaia et al., "Occipital alpha-band brain waves when the
  eyes are closed are shaped by ongoing visual processes" (2022); the Bureau of Meteorology SOI
  data page; and the PhysioNet EEG Motor Movement/Imagery Dataset.

---

[← 39. Ridge and LASSO Trend Estimation](39-ridge-and-lasso-trend-estimation.md) · [Contents](index.md) · [41. Regression Uncertainty and Profile Estimation →](41-regression-uncertainty-and-profile-estimation.md)
