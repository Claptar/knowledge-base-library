---
title: "1. White Noise and Random Walks"
course: "Berkeley Stat 153"
chapter: 1
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. White Noise and Random Walks

## What this covers

This chapter answers a basic question: why can't a time series be treated as an ordinary sample of
independent, identically distributed observations, and what is the minimal vocabulary — white
noise, moving averages, autoregression, and the random walk — for describing a sequence that
depends on its own past? It assumes only elementary probability: expectation, variance, and what it
means for a sequence of random variables to be iid.

## Dependence is the whole subject

Most time series are not iid. Instead, the value $x_t$ typically depends on its own recent past,
$x_{t-1}, \dots, x_{t-p}$ — a dependence often called *autocorrelation* — and many series also drift
over time rather than fluctuating around a fixed level. The purpose of time series analysis is to
build mathematical models that give plausible explanations for data with this kind of structure. If
every series behaved like an iid sample, classical statistics would already be enough; it is the
dependence that forces a separate toolkit.

Formally, a time series is thought of as one realization of a **stochastic process** — a system that
evolves randomly over time — even though real series usually mix genuinely random components with
deterministic, predictable ones (a trend, a known periodicity). Stochastic processes in general are
the subject of Stat 150; here they are treated only as much as is needed to describe time series.

## White noise

Many real series are usefully thought of as an underlying signal $s_t$ plus noise $w_t$. In the
nicest case, that noise is **white noise**: a sequence $w_t$, $t = 1, 2, 3, \dots$, that actually is
iid, with mean $0$ and variance $\sigma_w^2$. White noise is a special case of an uncorrelated
sequence, and it is the one case where the observations at different times carry no information
about each other at all. The most common special case is *Gaussian white noise*,

$$w_t \sim \text{iid } \mathcal{N}(0, \sigma_w^2).$$

White noise is the baseline against which everything else in this chapter is a departure: each of
moving averages, autoregression, and the random walk builds a dependent series out of an
independent one.

## Smoothing: the moving average

One way to smooth a series — including a white-noise series — is to replace the value at $t$ by an
average of it with its neighbors. A simple three-point version is

$$v_t = \frac{1}{3}(w_{t-1} + w_t + w_{t+1}),$$

and more generally, for an odd window of length $n$,

$$v_t = \frac{1}{n} \sum_{k=-\frac{n-1}{2}}^{\frac{n-1}{2}} w_{t+k}.$$

Averaging over a window is inherently a **low-pass filter**: it lets slow variation through and
suppresses fast variation. Concretely, it preserves trends that change more slowly than about $n$
samples, and suppresses oscillations with period shorter than about $n$ samples. This is useful for
revealing a trend buried in noisy data, for removing fluctuations treated as noise, or for simple
online smoothing — particularly if the window is restricted to past values only, so that it can be
computed as data arrive. It is, however, the crudest form of smoothing, and in practice it is often
replaced by more elaborate methods such as exponential moving averages, Kalman filters, or median
filters.

## Autoregression

A different kind of dependence comes from an **autoregressive** process: the value at $t$ is a
(noisy) regression on the series' own past values — hence "auto." A concrete example is

$$x_t = 1.5\,x_{t-1} - 0.75\,x_{t-2} + w_t.$$

Because $x_t$ depends on the two preceding values $x_{t-1}$ and $x_{t-2}$, this is called an AR(2)
process. Generating data this way — as will be seen directly in Lab 1 — can produce oscillatory
behavior, even though the driving noise $w_t$ is white.

## The random walk

The **simple random walk** is the basic example of a series built by accumulating white noise:

$$x_t = x_{t-1} + w_t, \qquad x_0 = 0,$$

equivalently $x_t = \sum_{j=1}^t w_j$.

Its mean is constant: $\mathbb{E}[x_t] = \mathbb{E}[x_0] = 0$ for every $t$. Its variance, however,
is **additive** and grows linearly in time, because it is a sum of $t$ independent terms each of
variance $\sigma^2$:

$$\operatorname{Var}(x_t) = \operatorname{Var}\!\left(\sum_{j=1}^t w_j\right) = t\sigma^2.$$

A random walk is emphatically not iid: successive values are dependent (each is built directly from
the one before), and they are not identically distributed either, since the variance itself changes
with $t$. Real examples include short-timescale stock prices (days, not months or years), Brownian
motion — the continuous-time analogue, describing diffusion of molecules — and null models used in
decision-making research, representing the case where no evidence is being accumulated.

### Random walk with drift

More often the series of interest is a random walk with **drift** $\delta$:

$$x_t = \delta + x_{t-1} + w_t, \qquad x_0 = 0,$$

equivalently $x_t = \delta t + \sum_{j=1}^t w_j$.

The drift shows up directly in the mean: $\mathbb{E}[x_t] = \delta t + x_0$. Conditioning on an
earlier observation $x_s$ gives $\mathbb{E}[x_t \mid x_s] = x_s + \delta(t - s)$ — the process is
expected to keep moving at rate $\delta$ from wherever it currently is. The variance is unchanged
from the driftless case, $t\sigma^2$, since the drift term is deterministic and does not add
randomness; noise still accumulates step by step regardless of drift. Real examples include
longer-timescale stock prices, decision-making (see below), and atmospheric $\text{CO}_2$
concentration, where the drift represents the human contribution and the noise reflects natural
variability.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A random walk with drift tracks a rising trend line with growing spread, while a driftless random walk meanders around zero with the same growing spread.">
<defs>
<marker id="rw-arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
<polygon points="0,0 8,4 0,8" fill="currentColor"/>
</marker>
</defs>
<line x1="40" y1="195" x2="315" y2="195" stroke="currentColor" stroke-width="1.5" marker-end="url(#rw-arrow)"/>
<line x1="40" y1="195" x2="40" y2="15" stroke="currentColor" stroke-width="1.5" marker-end="url(#rw-arrow)"/>
<text x="320" y="199" font-size="12" fill="currentColor">t</text>
<text x="14" y="14" font-size="12" fill="currentColor">x(t)</text>
<polygon points="40,195 102,148 165,110 227,74 290,38 290,102 227,129 165,155 102,180 40,195" fill="currentColor" fill-opacity="0.15"/>
<line x1="40" y1="195" x2="290" y2="70" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
<polyline points="40,195 70,185 102,160 130,140 165,125 200,100 227,90 260,60 290,55" fill="none" stroke="currentColor" stroke-width="2"/>
<polyline points="40,195 70,190 102,205 130,185 165,210 200,180 227,215 260,175 290,205" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 2"/>
<text x="292" y="50" font-size="12" fill="currentColor">drift</text>
<text x="292" y="212" font-size="12" fill="currentColor">no drift</text>
</svg>
<figcaption>One realized path with drift $\delta$ (solid, tracking the dashed trend line $\delta t$)
and one without drift (dashed, meandering around zero). The shaded envelope is the same for both:
because $\operatorname{Var}(x_t) = t\sigma^2$, the band of plausible values widens like
$\sqrt{t}$.</figcaption>
</figure>

### Drift diffusion models

The random walk with drift is also a cognitive model of decision-making, called a **drift diffusion
model**. Here $x_t$ is a decision variable, and the drift $\delta$ is the mean evidence gained per
unit time. Two boundaries are set for a binary choice, conventionally $-1$ (incorrect) and $+1$
(correct); the reaction time for the decision is the first time $x_t$ hits either boundary, at which
point the walk stops. With no drift ($\delta = 0$), the model predicts a long reaction time and a
50/50 chance of either outcome. A high $\delta$ represents high confidence or high-quality
information: it might be lower for a visual discrimination task done under heavy noise, and could be
raised by motivation or by more certain information. An example of neurons that behave as if they
were accumulating evidence in something like this way is given by
[Gold & Shadlen (2007)](https://pubmed.ncbi.nlm.nih.gov/17600525/), recorded during a task in which a
monkey watches movies of moving dots, a task made easy or hard by varying the percentage of dots
moving coherently in the same direction.

## Signal buried in noise

More generally, a periodic signal can be contaminated by white noise:

$$x_t = A\cos(2\pi\omega t + \phi) + w_t,$$

where $A$ is the amplitude, $\omega$ the frequency of oscillation, and $\phi$ a phase shift. The
ratio of the signal amplitude to the standard deviation of the noise is the **signal-to-noise ratio
(SNR)**: the larger it is, the easier it is to recover the underlying signal from the noisy data.
Recovering signals of this kind — and the AR and random-walk structures above — is exactly what the
regression methods developed later in the course are for.

## Sources

This chapter covers a single lecture (Liberty Hamilton, STAT 153, Spring 2026, Thursday 22 January
2026), supplied here as two independent conversions of the same material:

- Primary source: the lecturer's own markdown notes, `02_characteristics_notes.md`, split into
  "Review / basic concepts" and "Random Walk" (a lossless conversion, CC BY 4.0, from
  [berkeley-stat153/spring-2026](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md)).
  This supplied the text and equations for every section above.
- Cross-check source: a model's reconstruction of a PDF handout of the same lecture, `Lec02_Notes.pdf`
  (also [berkeley-stat153/spring-2026](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec02_Notes.pdf)),
  split the same way; its own header marks every equation as unverified, since the PDF has no text
  layer. It matches the primary source closely and was used only to confirm wording and to identify
  the drift figure as Shumway & Stoffer's Fig. 1.11 ($\sigma_w = 1$, $\delta = .2$ vs. $\delta = 0$)
  — the diagram above is a schematic of that relationship, not a reproduction of the original figure.
- No transcript, written notes, or problem set were supplied for this lecture, so there is no
  Exercises section.

Named but not contained in the supplied material: Shumway & Stoffer, *Time Series Analysis and Its
Applications*, §1.2 (this lecture's assigned reading) and §§1.3–1.7 (assigned for the following
week); Gold & Shadlen (2007) on decision-related neural activity during a random-dot motion task;
Stat 150, referred to as covering stochastic processes in more depth; and Lab 1, referred to as
where the AR(2) example is generated and examined directly. The white-noise, random-walk, and
dot-motion figures shown in the slides are hosted images that were not reproduced here.

---

[Contents](index.md) · [2. Mean, Autocovariance, and Correlation →](02-mean-autocovariance-and-correlation.md)
