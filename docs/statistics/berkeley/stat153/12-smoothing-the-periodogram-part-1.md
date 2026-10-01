---
title: "12. Smoothing the Periodogram (part 1)"
course: "Berkeley Stat 153"
chapter: 12
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Smoothing the Periodogram (part 1)

## What this covers

The periodogram is the natural way to estimate a process's spectral density from data, but it
turns out to be a bad estimator in a specific, fixable way: it never gets less noisy, no matter how
much data you feed it. This chapter works through why that happens and three ways to fix it —
averaging over independent copies of the series (the idea, though rarely available), averaging over
neighbouring frequencies (the Daniell smoother), and averaging over overlapping chunks of a single
series (Welch's method) — and how each trades frequency resolution for a calmer estimate. It assumes
the reader already has the discrete Fourier transform, the periodogram, and the spectral
density/autocovariance pair from earlier lectures.

## Recap: the spectral density of a causal moving average

As a warm-up, recall the spectral density of a causal moving-average process (only past noise terms
enter):

$$x_t = w_t + \theta w_{t-1}.$$

Its autocovariance function is

$$
\gamma(h) = \begin{cases}
(1+\theta^2)\sigma^2 & h=0\\
\theta\sigma^2 & |h|=1\\
0 & |h| > 1.
\end{cases}
$$

Plugging this into the definition of the spectral density and using Euler's formula
$e^{i\theta} = \cos\theta + i\sin\theta$, so that $\cos\theta = (e^{i\theta}+e^{-i\theta})/2$, gives

$$
\begin{aligned}
f(\omega) &= (1+\theta^2)\sigma^2 + \theta\sigma^2\left(e^{-2\pi i\omega} + e^{2\pi i\omega}\right)\\
&= \sigma^2\left(1+\theta^2+2\theta\cos(2\pi\omega)\right).
\end{aligned}
$$

This spectral density decays away from $\omega = 0$: larger $\theta$ gives a steeper decay from
$\omega = 0$ to $\omega = 1/2$. This is the kind of smooth curve the rest of the chapter is trying
to recover from noisy data.

## From the DFT to the periodogram: a worked example

The DFT and the periodogram carry different information. The DFT at frequency $j/n$,

$$d(j/n) = \frac{1}{\sqrt{n}}\sum_{t=1}^n x_t e^{-i2\pi tj/n},$$

is a complex number: it encodes both the amplitude and the *phase* of whatever oscillation sits at
that frequency. The periodogram,

$$P(j/n) = \frac{4}{n}\,|d(j/n)|^2,$$

keeps only the real-valued power, discarding phase. Because $P(j/n) = P(1-j/n)$, only frequencies
$j/n \le 1/2$ need to be computed.

A tiny example makes the mechanics concrete. Take $n=4$ points, $x_1=2,\ x_2=3,\ x_3=1,\ x_4=4$. The
Fourier frequencies are $j/4$ for $j=0,1,2,3$, and by the symmetry above only $j=0,1,2$ need
computing.

For $j=0$:

$$d(0) = \frac{1}{2}(2+3+1+4) = 5.$$

For $j=1$, using $e^{-i\pi t/2}$ at $t=1,2,3,4$ (values $-i,-1,i,1$):

$$d(1/4) = \frac{1}{2}\big(2(-i)+3(-1)+1(i)+4(1)\big) = \frac{1}{2}(1-i) = 0.5-0.5i.$$

For $j=2$, $e^{-i\pi t} = (-1)^t$:

$$d(2/4) = \frac{1}{2}\big(2(-1)+3(1)+1(-1)+4(1)\big) = \frac{1}{2}(4) = 2.$$

Squaring and rescaling turns these into the periodogram:

$$
\begin{aligned}
P(0/4) &= |5|^2 = 25,\\
P(1/4) &= |0.5-0.5i|^2 = 0.5,\\
P(2/4) &= |2|^2 = 4,\\
P(3/4) &= P(1/4) = 0.5.
\end{aligned}
$$

The phase information in $d(j/n)$ (whether the oscillation looks like a sine, a cosine, or a mix)
has disappeared; only the squared magnitude — the power at that frequency — survives.

## The periodogram does not get better with more data

The periodogram looks like the obvious estimator of the spectral density $f(\omega)$, and it is
(asymptotically) unbiased: $E[P(\omega)] \approx f(\omega)$. The trouble is its *variance*.

Simulating white noise, whose true spectral density is flat, $f(\omega)=\sigma^2$ (the theoretical
periodogram level under the density scaling used here is $2\sigma^2$, from folding the two-sided
spectrum onto $[0,1/2]$), and overlaying many independent periodograms at sample sizes $n=64$,
$256$, and $1024$ shows the problem directly: as $n$ grows, the periodogram is evaluated at *more*
Fourier frequencies (it gets denser), but the scatter of each individual ordinate around the true
flat line $2\sigma^2$ does not shrink at all. Every additional data point buys another noisy
estimate at a new frequency, not a less noisy estimate at the frequencies already there. The
periodogram is not a consistent estimator of the spectral density, and more data alone cannot fix
that.

## The fix in principle: average away the noise

Suppose, unrealistically, that many independent realizations of the same process were available.
Since each periodogram ordinate is (approximately) unbiased, averaging $K$ of them,

$$\bar P_K(\omega) = \frac{1}{K}\sum_{k=1}^K P_k(\omega),$$

converges to $f(\omega)$ as $K \to \infty$ by the law of large numbers — with $K=1$ the estimate is
very noisy, and by $K=100$ it is nearly flat at the true level. This is the right idea, but in
practice there is usually only **one** time series, so $K$ independent copies do not exist. The two
practical methods below both manufacture a substitute for that averaging from a single series — one
by borrowing from neighbouring frequencies, the other by borrowing from overlapping stretches of
time.

## Averaging over neighbouring frequencies: the Daniell smoother

If the true spectral density is smooth, periodogram ordinates at nearby frequencies are
approximately independent of one another and have approximately the same expectation. That means
averaging $2L+1$ neighbours behaves like averaging $2L+1$ independent estimates:

$$\hat f(\omega) = \frac{1}{2L+1}\sum_{k=-L}^{L} P\!\left(\omega+\frac{k}{n}\right).$$

This reduces variance by roughly a factor of $1/(2L+1)$, at the cost of some bias: the estimate at
$\omega$ is now really an estimate of the density averaged over a small band around $\omega$, so any
genuine feature narrower than that band gets blurred. For white noise there is no such cost, since
the true spectrum is already flat — smoothing it changes nothing in expectation. For a spectrum with
a peak, though, smoothing flattens the peak, which is a real bias introduced by the estimator.

## Averaging over overlapping segments: Welch's method

The other route averages over *time* instead of over frequency. Welch's method chops one long
series into overlapping segments, computes a periodogram for each, and averages them — manufacturing
pseudo-independent "realizations" out of a single dataset. It is conceptually the same idea as
averaging over true replicates, except the segments are not really independent (they overlap and
come from the same series); in practice it still works well.

Before each segment's periodogram is computed, the segment is multiplied by a tapering window — by
default a Hann window,

$$w(m) = 0.5 - 0.5\cos\!\left(\frac{2\pi m}{M-1}\right), \qquad 0 \le m \le M-1,$$

which is zero at both ends of the segment and rises smoothly to one in the middle. Tapering avoids
the abrupt jump that truncating a segment would otherwise create at its edges, which gives a
better-behaved Fourier transform. The full procedure is:

1. chop the series into overlapping segments of length `nperseg`;
2. multiply each segment by the Hann window;
3. compute the periodogram of each windowed segment;
4. average the periodograms across segments.

<figure>
<svg viewBox="0 0 400 190" role="img" aria-label="A time series divided into overlapping, tapered segments for Welch's method">
  <line x1="20" y1="165" x2="380" y2="165" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="380,165 370,161 370,169" fill="currentColor"/>
  <text x="378" y="182" text-anchor="end" font-size="12" fill="currentColor">time</text>

  <rect x="20" y="40" width="160" height="115" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M 20,150 Q 100,55 180,150" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="100" y="50" text-anchor="middle" font-size="12" fill="currentColor">segment 1</text>

  <rect x="100" y="40" width="160" height="115" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M 100,150 Q 180,55 260,150" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="70" text-anchor="middle" font-size="12" fill="currentColor">segment 2</text>

  <rect x="180" y="40" width="160" height="115" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M 180,150 Q 260,55 340,150" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="260" y="90" text-anchor="middle" font-size="12" fill="currentColor">segment 3</text>
</svg>
<figcaption>Each rectangle is one overlapping segment of the series; the curve inside it is the
Hann window applied before that segment's periodogram is computed. The periodograms of all
segments are then averaged.</figcaption>
</figure>

## Choosing how much to smooth: resolution against noise

Both methods face the same trade-off: more averaging means less variance but coarser frequency
resolution, since averaging necessarily blends together frequencies that were originally distinct.
A worked example with three sinusoidal components makes this concrete. The clean signal is

$$x(t) = 12\cos(2\pi \cdot 6t) + 13\sin(2\pi \cdot 6t) + 4\cos(2\pi \cdot 10.5t) + 5\sin(2\pi\cdot 10.5t) + 6\cos(2\pi\cdot 39.2t) + 7\sin(2\pi\cdot 39.2t),$$

sampled at $f_s = 1000$ Hz for one second, with the theoretical power of each component equal to
$a^2+b^2$ (so $12^2+13^2=313$, $4^2+5^2=41$, $6^2+7^2=85$). A noisy version adds Gaussian noise with
standard deviation $20$.

The raw periodogram of this signal already shows **spectral leakage**: because the sinusoid
frequencies do not fall exactly on the Fourier frequencies $j/n$, their power spreads into
neighbouring bins — the $10.5$ Hz component, for instance, shows up split across the $10$ Hz and
$11$ Hz bins rather than as one clean spike.

Smoothing the noisy periodogram with the Daniell smoother or Welch's method recovers the three peaks
at low smoothing but starts to merge the $6$ Hz and $10.5$ Hz peaks (only $4.5$ Hz apart) as the
smoothing gets heavier. Each method has an explicit rule for how much smoothing is safe:

**Welch.** Two peaks $\Delta f$ apart can only be resolved if the segment length is at least

$$N_{\text{seg}} \ge \frac{f_s}{\Delta f}.$$

For the $6$ and $10.5$ Hz peaks, $\Delta f = 4.5$ Hz and $f_s=1000$, so $N_{\text{seg}} \ge
1000/4.5 \approx 222$. That is the absolute floor; in practice segments $2$–$3$ times longer
(around $400$–$600$ samples) work better.

**Daniell.** To keep the smoothed bandwidth narrower than a target separation $\Delta f$, the
window half-width must satisfy

$$L < \frac{N\,\Delta f}{2f_s} - \frac12.$$

For the same $6$ and $10.5$ Hz peaks, with $N=f_s=1000$,

$$L < \frac{1000(4.5)}{2(1000)} - \frac12 = 2.25 - 0.5 = 1.75,$$

so $L=1$ leaves both peaks resolved, while $L=2$ is already borderline.

The lecture closed by asking the reader to think about signals for which the periodogram — a single
frequency-domain summary of the *whole* series — throws away information that matters, pointing
toward the idea of tracking how frequency content changes over time (an interactive spectrogram
tool was linked as a way to explore this), but the worked material supplied here stops at the
periodogram and its smoothing.

## Exercises

1. The lecture posed this as an open question rather than a computation: think of a signal for
   which knowing only its periodogram — a single, whole-series summary of power at each frequency —
   would obscure information you might care about. What kind of time structure would the
   periodogram be blind to?

## Sources

- `14_spectral_analysis_time_frequency_notes.md` (Lecture 14 notes, Berkeley STAT 153, spring 2026)
  — moving-average spectral density recap, and the DFT/periodogram overview with the $n=4$ worked
  example.
- `Lecture14/01-the-periodogram-stays-noisy-no-matter-how-much-data-you-have.md` — the simulation
  showing periodogram variance does not shrink with $n$.
- `Lecture14/02-averaging-the-periodogram.md` — averaging over independent realizations and the law
  of large numbers argument.
- `Lecture14/03-averaging-across-neighboring-frequencies-daniell-smoother.md` — the Daniell smoother,
  its formula, and its variance/bias trade-off.
- `Lecture14/05-welch-s-method-a-third-way-to-average.md` — Welch's method, the Hann window, and the
  segmenting/tapering/averaging procedure.
- `Lecture14/06-comparing-methods-on-data-with-frequency-peaks.md` — the three-sinusoid worked
  example, spectral leakage, and the resolution formulas for Welch's method and the Daniell
  smoother, plus the closing question about the limits of the periodogram.
- Reading named alongside the lecture but not itself supplied: Shumway and Stoffer, Chapter 4
  (Chapter 4.4 specifically, on periodogram smoothing). The "Interactive Spectrogram" tool linked
  from the lecture (musiclab.chromeexperiments.com) was likewise referred to but not contained in
  the supplied material.
- No transcript, additional notes, or problem set were supplied for this lecture; the exercise above
  is the one discussion question the lecture itself posed.

---

[← 11. Fourier Transform and Spectral Density](11-fourier-transform-and-spectral-density.md) · [Contents](index.md) · [13. Time-Frequency Analysis of Music →](13-time-frequency-analysis-of-music.md)
