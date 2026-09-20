---
title: "10. Periodic Signals and the Periodogram"
course: "Berkeley Stat 153 Fall 2024"
chapter: 10
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Periodic Signals and the Periodogram

## What this covers

This chapter builds the model for a deterministic wave hidden inside noisy data — a sinusoid with a
given frequency, amplitude and phase — and then asks the natural next question: if a signal is a
mixture of such waves at frequencies you don't know in advance, how do you find them from data
alone? The answer is the periodogram, a device for reading amplitude and dominant frequency
straight off a decomposition of the observed series. It assumes familiarity with (weak)
stationarity, autocovariance, and ordinary least-squares regression.

## Building a periodic signal

A pure periodic ("harmonic") component is
$$y(t) := \beta_0 + R\cos(2\pi f t + \phi),$$
a wave of frequency $f$, amplitude $R$ and phase $\phi$, riding on a constant $\beta_0$. Expanding
the cosine of a sum,
$$R\cos(2\pi f t + \phi) = R\cos\phi\,\cos(2\pi f t) - R\sin\phi\,\sin(2\pi f t),$$
so the same wave can be written as a linear combination of a cosine and a sine at the same
frequency:
$$y(t) = \beta_0 + U_1\cos(2\pi f t) + U_2 \sin(2\pi f t), \qquad U_1 = R\cos\phi,\ \ U_2=-R\sin\phi.$$
This reparameterization is exact — no information is lost — and it trades the pair $(R,\phi)$ for
the pair $(U_1,U_2)$: amplitude and phase are recovered from them as $A=\sqrt{U_1^2+U_2^2}$
(equal to $R$) and $\phi=\arctan(U_2/U_1)$.

## A random-amplitude, random-phase model, and why it is stationary

Now let $U_1$ and $U_2$ be *random* — uncorrelated, mean zero, each with variance $\sigma^2$ — so
that $y_t$ has the same frequency every time but a random amplitude and phase. With
$\mathbb{E}(y_t)=0$ and writing $\lambda = 2\pi f$, the autocovariance is

$$
\begin{aligned}
\gamma_y(t,s) &= \operatorname{cov}(y_t, y_s)\\
&= \operatorname{cov}\big(U_1\cos(\lambda t) + U_2\sin(\lambda t),\ U_1\cos(\lambda s)+U_2\sin(\lambda s)\big)\\
&= \operatorname{cov}(U_1\cos(\lambda t), U_1\cos(\lambda s)) + \operatorname{cov}(U_1\cos(\lambda t), U_2\sin(\lambda s))\\
&\quad + \operatorname{cov}(U_2\sin(\lambda t), U_1\cos(\lambda s)) + \operatorname{cov}(U_2\sin(\lambda t), U_2\sin(\lambda s))\\
&= \sigma^2\cos(\lambda t)\cos(\lambda s) + 0 + 0 + \sigma^2\sin(\lambda t)\sin(\lambda s)\\
&= \sigma^2\big[\cos(\lambda t)\cos(\lambda s) + \sin(\lambda t)\sin(\lambda s)\big]\\
&= \sigma^2\cos(\lambda(t-s)).
\end{aligned}
$$

The two cross terms vanish because $U_1$ and $U_2$ are uncorrelated; the two surviving terms share
the same variance $\sigma^2$ and combine, by the cosine-difference identity, into a function of the
lag $t-s$ alone. Mean constant, autocovariance a function of lag only: $y_t$ is (weakly) stationary,
with $\gamma_y(h) = \sigma^2\cos(\lambda h)$ at lag $h$.

## Mixtures of frequencies

Real signals rarely consist of one frequency, so generalize to a sum of $q$ harmonic components:
$$y_t = \sum_{k=1}^q \big[U_{k1}\cos(2\pi f_k t) + U_{k2}\sin(2\pi f_k t)\big],$$
with $f_1,\dots,f_q$ distinct frequencies and all the $U_{k1},U_{k2}$ ($k=1,\dots,q$) uncorrelated
with mean zero, $U_{k1}$ and $U_{k2}$ sharing variance $\sigma_k^2$. The covariance calculation
above goes through term by term — cross terms between different components $k$ vanish for the same
reason as before — so the mixture is stationary too.

The lecture's notebook illustrates this with three sinusoids at frequencies $f=6,10,39$ (chosen
with no particular relationship to each other) and amplitude pairs $(U_1,U_2)=(2,3),(4,5),(6,7)$.
Two things about summing sinusoids are worth holding onto, because they resurface once the
frequencies are unknown and have to be estimated:

- **The sum's amplitude is bounded by the sum of the amplitudes.** If component $k$ has amplitude
  $A_k=\sqrt{U_{k1}^2+U_{k2}^2}$, the combined series reaches at most $\sum_k A_k$ in absolute
  value.
- **That ceiling is only reached if every component's peak lines up at the same instant**, which
  happens reliably only when the frequencies are harmonically related — integer multiples of a
  common base frequency. Frequencies picked with no such relationship, like $6, 10, 39$, essentially
  never line up, so the combined wave's envelope stays visibly below the sum-of-amplitudes bound
  even though each component individually reaches its own peak somewhere in the window.

The notebook repeats the same construction with three audio-frequency sinusoids added together and
played as sound, to make audible what a sum of several periodic components looks/sounds like before
any attempt is made to recover the frequencies from it.

## From a model to data: the periodogram

Suppose instead you are handed $n$ observations $y_1,\dots,y_n$ and do not know what mixture of
frequencies, if any, produced them. Rather than assuming some particular number of frequencies $q$
up front, write the data exactly as a sum over every frequency the sample can resolve:
$$y_t = a_0 + \sum_{j=1}^{\lfloor n/2\rfloor}\big[a_j\cos(2\pi tj/n) + b_j \sin(2\pi tj/n)\big],
\qquad t=1,\dots,n,$$
where $\lfloor\cdot\rfloor$ rounds down to the nearest integer. If $n$ is even the top term is
special: $a_{n/2}\cos(2\pi t\cdot\tfrac12)=a_{n/2}(-1)^t$ and $b_{n/2}=0$.

This is not a modeling assumption — it is a change of basis, an exact representation of any $n$
numbers as a combination of cosines and sines at the frequencies $j/n$, $j=1,\dots,\lfloor
n/2\rfloor$, called the **Fourier frequencies**. Here $j/n$ is a frequency in cycles per sample,
and as $j$ runs from $1$ to $\lfloor n/2\rfloor$ it sweeps through every frequency distinguishable
at this sampling rate. With $n=100$: $j=1$ completes exactly one full cycle over the whole window,
the slowest oscillation that fits; $j=2$ completes two cycles, $j=3$ three, and so on; $j=50=n/2$
completes fifty cycles, the fastest oscillation resolvable — alternating up and down every single
sample — the **Nyquist frequency**.

The coefficients come from regression: projecting the data onto the cosine and sine at each Fourier
frequency,
$$a_j = \frac{2}{n}\sum_{t=1}^n x_t \cos(2\pi tj/n), \qquad b_j = \frac{2}{n}\sum_{t=1}^n x_t
\sin(2\pi tj/n).$$
$a_j$ and $b_j$ jointly set the amplitude and phase at frequency $j/n$ — the data-driven analogue of
$U_1,U_2$ in the model above — and are estimated independently at each $j$.

This gives the **(scaled) periodogram**:
$$P(j/n) = a_j^2 + b_j^2, \qquad j/n \neq 0, \tfrac12.$$
$P(j/n)$ is the sample variance carried by frequency $j/n$ — an estimate of $\sigma_j^2$, the
variance a sinusoid at that frequency would need in the mixture model to explain what is seen in
the data. A large value of $P(j/n)$ says frequency $j/n$ is doing real work in the series; a small
value looks like noise.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A periodogram: tall spikes at the frequencies present in a mixed signal, near zero everywhere else">
  <line x1="30" y1="160" x2="305" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <text x="305" y="178" font-size="12" fill="currentColor" text-anchor="end">frequency j/n</text>
  <text x="14" y="60" font-size="12" fill="currentColor">P(j/n)</text>
  <line x1="45" y1="160" x2="45" y2="151" stroke="currentColor" stroke-width="1"/>
  <line x1="58" y1="160" x2="58" y2="146" stroke="currentColor" stroke-width="1"/>
  <line x1="90" y1="160" x2="90" y2="153" stroke="currentColor" stroke-width="1"/>
  <line x1="110" y1="160" x2="110" y2="148" stroke="currentColor" stroke-width="1"/>
  <line x1="130" y1="160" x2="130" y2="152" stroke="currentColor" stroke-width="1"/>
  <line x1="170" y1="160" x2="170" y2="145" stroke="currentColor" stroke-width="1"/>
  <line x1="190" y1="160" x2="190" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="240" y1="160" x2="240" y2="147" stroke="currentColor" stroke-width="1"/>
  <line x1="260" y1="160" x2="260" y2="152" stroke="currentColor" stroke-width="1"/>
  <line x1="280" y1="160" x2="280" y2="149" stroke="currentColor" stroke-width="1"/>
  <line x1="75" y1="160" x2="75" y2="40" stroke="currentColor" stroke-width="2.5"/>
  <text x="75" y="32" font-size="12" fill="currentColor" text-anchor="middle">f1</text>
  <line x1="150" y1="160" x2="150" y2="90" stroke="currentColor" stroke-width="2.5"/>
  <text x="150" y="82" font-size="12" fill="currentColor" text-anchor="middle">f2</text>
  <line x1="215" y1="160" x2="215" y2="65" stroke="currentColor" stroke-width="2.5"/>
  <text x="215" y="57" font-size="12" fill="currentColor" text-anchor="middle">f3</text>
</svg>
<figcaption>Three genuine frequency components stand out as tall spikes against a noise floor of
small values elsewhere — the periodogram's job is exactly to make that contrast visible.</figcaption>
</figure>

## Reading the periodogram: examples from the lecture

The lecture's notebook works through several data sets to show what the periodogram does and does
not tell you.

**Recovering known frequencies exactly.** Three sinusoids at $f=6,10,39$ (amplitude pairs
$(U_1,U_2)=(12,13),(4,5),(6,7)$) are summed and sampled at $100$ Hz over one second, so $n=100$.
`scipy.signal.periodogram` computes $P(j/n)$ against frequency in Hz, and the peaks land exactly at
$6$, $10$ and $39$ Hz — because with $n=100$ samples over a $1$-second window, the Fourier
frequencies $j/n$ (cycles per sample) coincide exactly with $j$ Hz, and $6,10,39$ are all integers.

**Frequency resolution is set by duration, not by the sampling rate.** The notes are explicit about
this: "our frequency resolution is $1/T$ where $T$ is the duration of our signal (in seconds! not
samples!)." Sampling faster adds more Fourier frequencies up to a higher Nyquist frequency, but it
does not pack them closer together — recording for longer, not sampling faster, is what lets two
nearby frequencies be told apart.

**The sunspot cycle.** Sunspot counts sampled twice a year from 1749 to 1978 ($f_s=2$
cycles/year) are run through the same periodogram. Plotted against frequency in cycles/year, it
shows a peak near $1/11$ — the roughly 11-year sunspot cycle — and, once the low-frequency end is
stretched out by plotting against *period* ($1/\text{frequency}$) on a log axis rather than against
frequency directly, a second, much slower peak near $1/110$, the Gleissberg cycle. The two would be
hard to compare on a single linear frequency axis, since one sits close to zero and the other much
further along; a log-period axis brings both into view together.

**Detecting a nuisance frequency.** A recorded vowel sound has a synthetic $60$ Hz tone (a cosine
plus a sine at $f=60$, standing in for electrical mains interference) added onto it. The
periodogram of the contaminated recording, zoomed into $0$–$600$ Hz, shows the injected
interference as a spike at exactly $60$ Hz standing out from the speech spectrum around it — the
periodogram used diagnostically, to locate a known unwanted periodic component rather than to
discover a new one.

## Sources

- Slides, [`01-periodic-signals.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/12_spectral_analysis_notes.md) — the periodic signal model, its reparameterization, the stationarity derivation, and the generalization to a sum of $q$ frequencies.
- Slides, [`02-periodogram.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/12_spectral_analysis_notes.md) — the exact Fourier-frequency expansion of an observed series, the regression formulas for $a_j,b_j$, and the definition of the scaled periodogram.
- Notebook, [`Lecture12.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb) — the worked examples: three synthetic sinusoids and the amplitude-bound comment, the musical-tone audio demo, exact recovery of $6,10,39$ Hz via `scipy.signal.periodogram`, the frequency-resolution note, the sunspot-cycle periodogram (via `astsa.load_sunspotz`), and the line-noise detection example. Several figures and one audio widget referenced in the notebook were not reproduced in the conversion (marked "figure omitted" in the source).
- No transcript, written notes, or exercise set was supplied for this lecture.
- The slides assign **Chapter 4 of Shumway and Stoffer** as the reading for this material; that text was referred to but not supplied. The periodogram notes also point forward to relating $P(j/n)$ to the Discrete Fourier Transform, described as material for "next time" and likewise not covered here.

---

[← 9. Cross-Validation and Regularization](09-cross-validation-and-regularization.md) · [Contents](index.md) · [11. Fourier Transform and Spectral Density →](11-fourier-transform-and-spectral-density.md)
