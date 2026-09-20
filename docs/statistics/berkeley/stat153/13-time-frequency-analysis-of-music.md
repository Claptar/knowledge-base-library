---
title: "13. Time-Frequency Analysis of Music"
course: "Berkeley Stat 153 Fall 2024"
chapter: 13
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. Time-Frequency Analysis of Music

## What this covers

Earlier lectures built the periodogram and Welch's method on simulated series and on a single
long, roughly-behaved record (sunspot counts). This chapter asks what those same tools show when
turned on something the listener already has strong intuitions about — pieces of music — and uses
that to expose a limit that the periodogram alone could not: a single spectrum cannot say *both*
which frequencies are present *and* when they occurred. It assumes the periodogram (including its
formula in terms of the DFT and its frequency resolution $\Delta f = f_s/N$), Welch's method as a
variance-reduction device, the notion of a weakly stationary process, and the autocovariance
function, all from earlier in the course.

The lecture runs as a sequence of demos on four short audio clips, each chosen to typify a
category from a warm-up poll ("guess the category: mostly one instrument, a cappella, strong
beat/danceable, very repetitive, very slow"):

| Demo | Track type | Concept |
|---|---|---|
| 1 | Solo instrument / a cappella | Waveform vs. periodogram vs. spectrogram |
| 2 | Repetitive song | Time–frequency tradeoff (window length) |
| 3 | Danceable / strong beat | Welch vs. raw periodogram (bias–variance) |
| 4 | Slow + danceable | Low-pass and high-pass filtering |
| 5 | All four | Autocovariance, PSD, and stationarity |

## Three views of the same signal

Playing a sound gives three different pictures of it, and each throws away something the others
keep.

**The waveform** is amplitude against time. It shows *when* the signal is loud or quiet, but
nothing about which frequencies (which notes, which pitches) make it up.

**The periodogram** is power against frequency, computed once over the whole clip:

$$P_{xx}(f) = \frac{1}{f_s N}\left|\widehat y(f)\right|^2, \qquad \widehat y = \mathrm{rfft}(y),$$

with $y$ the $N$-sample waveform and $f_s$ the sampling rate. It shows which frequencies are
present across the entire recording, but the time axis is gone — the lecture's own test of this is
to ask, looking only at the periodogram of an a cappella track, "could you sing the song from this
or identify the melody?" You cannot: the plot tells you the pitches used somewhere in the clip, not
in what order.

**The spectrogram** is power against frequency *and* time, and is the new object of this lecture.
It is obtained by recomputing the periodogram on a short sliding window rather than once on the
whole signal:

1. chop the signal into short, typically overlapping chunks, each of length `nperseg`;
2. compute the periodogram of each chunk;
3. stack the resulting spectra side by side, one column per chunk, to form a frequency-by-time
   matrix.

So the spectrogram is not a new mathematical object — it is the periodogram, applied repeatedly to
a moving window, and it is the tool that recovers what the plain periodogram threw away.

## The time–frequency tradeoff

Recovering time information is not free. Recall that a periodogram computed from $N$ samples has
frequency resolution $\Delta f = f_s/N$ — the more samples you feed it, the finer the grid of
frequencies it can distinguish. In a spectrogram, each window supplies only `nperseg` samples to
its periodogram, so that window's frequency resolution is

$$\Delta f = \frac{f_s}{\texttt{nperseg}}.$$

At the same time, each window covers a duration

$$\Delta t = \frac{\texttt{nperseg}}{f_s},$$

which is the finest interval over which the spectrogram can localize an event in time. Multiplying
the two:

$$\Delta t \cdot \Delta f = 1$$

for every choice of window length. Shrinking `nperseg` buys sharper time localization at the direct
cost of frequency resolution; lengthening it buys the reverse. Numerically, on a track sampled at
$f_s = 22050$ Hz:

| `nperseg` | $\Delta t$ (s) | $\Delta f$ (Hz) | $\Delta t \times \Delta f$ |
|---|---|---|---|
| 128 | 0.006 | 172.3 | 1.00 |
| 2048 | 0.093 | 10.8 | 1.00 |
| 8192 | 0.372 | 2.7 | 1.00 |

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Two window lengths drawn as boxes in the time-frequency plane, of equal area but different shape">
  <text x="90" y="16" text-anchor="middle" font-size="12" fill="currentColor">short window</text>
  <text x="270" y="16" text-anchor="middle" font-size="12" fill="currentColor">long window</text>

  <line x1="30" y1="190" x2="170" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="190" x2="30" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">time</text>
  <text x="15" y="35" text-anchor="middle" font-size="12" fill="currentColor">freq</text>
  <rect x="80" y="40" width="20" height="150" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>

  <line x1="210" y1="190" x2="350" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="210" y1="190" x2="210" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <text x="350" y="205" text-anchor="middle" font-size="12" fill="currentColor">time</text>
  <text x="195" y="35" text-anchor="middle" font-size="12" fill="currentColor">freq</text>
  <rect x="210" y="165" width="120" height="25" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
</svg>
<figcaption>Each window is a box in the time-frequency plane: a short window is narrow in time but
tall in frequency (poor $\Delta f$), a long window is wide in time but short in frequency (poor
$\Delta t$). The two boxes have equal area, since $\Delta t \times \Delta f = 1$ regardless of
window length — no choice gives fine resolution in both dimensions at once.</figcaption>
</figure>

This is the same tradeoff seen earlier when using Welch's method to average shorter segments of a
periodogram: smaller segments give more segments to average and so lower variance, but coarser
frequency resolution; larger segments give better frequency resolution but a noisier (higher
variance) estimate. The spectrogram case adds a second axis to worry about — the window length now
trades off *time* resolution against *frequency* resolution, not just variance against resolution.

It also reframes something from an earlier lecture on sunspot counts. A periodogram computed over
the *entire* sunspot record has resolution $\Delta f = 2/N$ cycles per year — fine enough to locate
the roughly 11-year cycle precisely in frequency — but that periodogram carries no information
about *when* the cycle was strong or weak, because $N$ was the whole record and so $\Delta t$ was
the whole record's duration. The periodogram is exactly the limiting case of the spectrogram in
which the window equals the entire signal: the best possible $\Delta f$, purchased at the worst
possible $\Delta t$.

## Welch versus the raw periodogram, revisited

The bias–variance behavior of the periodogram, previously seen on simulated data, shows up
directly when the raw periodogram of a danceable track is plotted: it is visibly jagged, one FFT of
the whole clip. Welch's method — averaging periodograms of overlapping segments — smooths this out,
and the smoothing gets stronger as `nperseg` shrinks (more segments to average) at the cost of
frequency resolution.

The demo that makes the *reason* Welch works vivid is this: chop the same track into thirty
one-second chunks and overlay the thirty raw periodograms, one per chunk. Even though the
underlying music is approximately stationary over these timescales, the individual periodograms
look noticeably different from one another — each is a noisy estimate of the same underlying
spectrum. Welch's average of exactly these segments is the earlier variance-reduction argument
made visible: instead of trusting any one chunk's noisy spectrum, average many of them.

## Filtering: low-pass, high-pass, and multiplication in frequency

A **Butterworth filter** is designed to be as flat as possible in the frequencies it is meant to
keep (the passband). `scipy.signal.butter` designs the filter as a set of second-order sections
(`sos`); `sosfiltfilt` applies it by filtering the signal forward and then backward, which is
*zero-phase* — it introduces no time shift, unlike a single forward pass; `sosfreqz` computes the
filter's frequency response $H(f)$.

The filter acts on the spectrum by multiplication:

$$S_{\text{filtered}}(f) = |H(f)|^2 \cdot S_{\text{original}}(f).$$

In the time domain the same operation is convolution with the filter's impulse response —
multiplication in frequency corresponds to convolution in time. Applying a low-pass filter (cutoff
500 Hz) and a high-pass filter (cutoff 3000 Hz) to the same danceable track, and comparing the
spectrograms and Welch PSDs before and after, shows the filters doing exactly what their frequency
responses predict: the low-pass output keeps only the energy below the cutoff, the high-pass output
only what is above it. In the waveform itself, the low-pass version looks smoother and the
high-pass version spikier, though how strong that visual difference is depends on where the
original track's energy actually sits in frequency — a track with little energy near a cutoff will
barely change when filtered there.

## Autocovariance, the PSD, and stationarity

Two more connections tie the spectral tools back to the autocovariance function:

**The autocovariance function and the PSD are a Fourier transform pair.** Both `periodogram` and
`welch` implicitly assume the signal is (weakly) stationary — that its autocovariance depends only
on lag, not on absolute time — and the lecture poses, without resolving, the natural question: when
is that approximately true for a piece of music?

**Demo:** the sample ACF (`statsmodels.tsa.stattools.acf`) is computed out to one second of lag for
each of the four representative tracks (solo/a cappella, repetitive, danceable, slow), and the four
plots are compared side by side with the question "what patterns repeat, and do they differ if you
try other tracks in the same categories?"

**The periodogram is the FFT of the sample autocovariance.** This is checked directly rather than
just asserted: for each track, the PSD is computed two ways — once via `welch`, once by taking
`np.fft.rfft` of the sample ACF computed out to the full length of the signal — and the two
(rescaled to a common height) are overlaid. They agree, confirming the Fourier-pair relationship
using the estimators already in hand.

**Stationarity check.** Split a track into several (here, six) contiguous segments, compute a
Welch PSD on each segment separately, and overlay them. If the PSDs from different segments have
the same shape, the signal is behaving as approximately stationary over those stretches and the
spectral estimates are trustworthy; where the PSDs disagree across segments, the stationarity
assumption is breaking down. This is the same logic that justifies Welch's method itself, which
already assumes each of its segments is a sample from the same stationary process.

## Bonus: a spectrogram from scratch

To confirm that nothing beyond the periodogram machinery is involved, the spectrogram can be
rebuilt directly from `np.fft.rfft` rather than calling `scipy.signal.spectrogram`. For each
window: multiply the segment by a Hanning window, take its `rfft`, square the magnitude, and
normalize by $f_s \sum(\text{window}^2)$ — the same periodogram formula as before, with a window
correction — then stack the columns exactly as before. Run side by side against
`scipy.signal.spectrogram` on the same track, the two outputs match visually: the spectrogram is
nothing more than the periodogram computed on a sliding window, with no additional machinery
hidden inside the library call.

## Sources

- Both source files are the two markdown parts of the same converted Jupyter notebook,
  `berkeley-stat153/spring-2026`, `public/lectures/Lecture15.ipynb`, CC BY 4.0:
  - `01-lecture-15-time-frequency-analysis-with-music.md` — title, demo table, setup/imports.
  - `02-quick-poll---guess-the-category.md` — the warm-up poll and all five numbered demos
    (waveform/periodogram/spectrogram; window-length tradeoff; Welch vs. raw periodogram;
    filtering; autocovariance/PSD/stationarity), plus the bonus from-scratch spectrogram.
- No transcript, written notes, or problem set were supplied for this lecture; nothing here is
  drawn from a lecture recording.
- The notebook's actual figures (waveforms, periodograms, spectrograms, filter responses, ACF
  plots) and audio clips are not present in the converted source — only their code and captions
  are — so this chapter describes what each figure was constructed to show rather than reproducing
  the images themselves.
- The lecture explicitly refers back to two pieces of material it does not itself contain: the
  earlier derivation of the periodogram's frequency resolution $\Delta f = f_s/N$ and of Welch's
  method as a variance-reduction device (both said to be "from class"), and an earlier lecture's
  periodogram of sunspot counts (`periodogram(sunspots, fs=2.0)`), used here only for its stated
  resolution $\Delta f = 2/N$ cycles/year — neither the sunspots lecture nor the general periodogram
  derivation was among the inputs to this chapter.

---

[← 12. Smoothing the Periodogram (part 1)](12-smoothing-the-periodogram-part-1.md) · [Contents](index.md) · [14. Intro to Autoregressive Models →](14-intro-to-autoregressive-models.md)
