---
title: "2. Mean, Autocovariance, and Correlation"
course: "Berkeley Stat 153 Fall 2024"
chapter: 2
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Mean, Autocovariance, and Correlation

## What this covers

Last time introduced a handful of specific processes — white noise, a moving average, a
random walk (with and without drift), a signal buried in noise — and looked at how their
paths differ. This chapter asks how to describe that difference numerically: at each time
$t$, where is the process centered and how spread out is it, and — the harder question —
how do two different times of the *same* process relate to each other? That second question
is what makes a time series a time series rather than just a collection of unrelated random
variables. It assumes the reader already has the four example processes above in hand, along
with ordinary variance and covariance for random variables.

## The mean and variance functions

For a stochastic process $x_t$, the **mean function** is just the expectation of the process
at each fixed time,

$$\mu_{xt} = \mathbb{E}(x_t),$$

and the **variance function** is the variance at each fixed time,

$$\sigma_t^2 = \operatorname{Var}(x_t) = \mathbb{E}[(x_t-\mu_t)^2].$$

Both are functions of $t$ — one number per time point, describing the drift and the spread
we should expect to see at that point, but nothing about how the process is built up or how
one time point relates to another.

**White noise.** By definition $\mu_{wt} = \mathbb{E}(w_t) = 0$ for every $t$, and
$\operatorname{Var}(w_t) = 1$ for a Gaussian white noise series (more generally this is
written $\sigma_w^2$).

**Moving average.** Applying a 3-point moving average, $v_t = \tfrac13(w_{t-1}+w_t+w_{t+1})$,
induces correlation between neighbouring points but does not move the mean at all:

$$\mu_{vt} = \mathbb{E}(v_t) = \tfrac13\big[\mathbb{E}(w_{t-1})+\mathbb{E}(w_t)+\mathbb{E}(w_{t+1})\big] = 0.$$

**Random walk with drift.** For $x_t = \delta t + \sum_{j=1}^t w_j$, the mean function is
the deterministic line

$$\mu_{xt} = \delta t + \sum_{j=1}^t \mathbb{E}(w_j) = \delta t.$$

**Signal plus noise.** For a sinusoid buried in noise, $x_t = A\cos(2\pi\omega t + \phi) + w_t$,
linearity of expectation and $\mathbb{E}(w_t)=0$ strip the noise term away entirely:

$$
\begin{aligned}
\mu_{xt} = \mathbb{E}(x_t) &= \mathbb{E}\big[A\cos(2\pi\omega t+\phi) + w_t\big] \\
&= \mathbb{E}\big[A\cos(2\pi\omega t+\phi)\big] + \mathbb{E}[w_t] \\
&= \mathbb{E}\big[A\cos(2\pi\omega t+\phi)\big].
\end{aligned}
$$

In each case the mean function only tells us about the deterministic skeleton of the process —
the drift, or the signal — and is silent about how the noise around that skeleton behaves
across time. That is the gap autocovariance fills.

## Autocovariance

Fix two times $s$ and $t$ in the same series, and ask how $x_s$ and $x_t$ co-vary. This is the
**autocovariance function**,

$$\gamma_x(s,t) = \operatorname{cov}(x_s,x_t) = \mathbb{E}\big[(x_s-\mu_s)(x_t-\mu_t)\big].$$

Setting $s=t$ recovers the variance function as a special case:

$$\gamma_x(t,t) = \mathbb{E}\big[(x_t-\mu_t)^2\big] = \operatorname{Var}(x_t).$$

**White noise** should have no dependence at all between distinct times, and indeed, since
$\mathbb{E}(w_t)=0$,

$$
\gamma_w(s,t) = \operatorname{cov}(w_s,w_t) =
\begin{cases}
\sigma_w^2, & s=t,\\
0, & s\neq t.
\end{cases}
$$

### Bilinearity: the tool for everything that follows

Covariance is bilinear in linear combinations of finite-variance random variables. If
$U=\sum_{j=1}^m a_j X_j$ and $V=\sum_{k=1}^r b_k Y_k$, then

$$\operatorname{cov}(U,V) = \sum_{j=1}^m\sum_{k=1}^r a_j b_k\,\operatorname{cov}(X_j,Y_k),$$

and $\operatorname{Var}(U) = \operatorname{cov}(U,U)$. This is the one identity that turns
"the process is built out of independent noise" into an actual number for $\gamma$, and it is
what drives every computation below.

### Autocovariance of the moving average

Apply bilinearity to $v_t = \tfrac13(w_{t-1}+w_t+w_{t+1})$. In general,

$$
\gamma_v(s,t) = \operatorname{cov}(v_s,v_t) = \tfrac19\operatorname{cov}\big(w_{s-1}+w_s+w_{s+1},\; w_{t-1}+w_t+w_{t+1}\big).
$$

Expanding this covariance turns it into a sum of nine covariance terms between individual
noise variables, and since the $w_i$ are independent, only the terms where the two indices
actually coincide survive — the rest are zero. How many terms coincide depends only on how
far apart $s$ and $t$ are, because the two windows $\{s-1,s,s+1\}$ and $\{t-1,t,t+1\}$ overlap
less as $|s-t|$ grows.

At $s=t$, the two windows are identical, so all three "own-variance" terms survive and every
cross term vanishes:

$$
\begin{aligned}
\gamma_v(t,t) &= \tfrac19\Big[\operatorname{cov}(w_{t-1},w_{t-1})+\operatorname{cov}(w_t,w_t)+\operatorname{cov}(w_{t+1},w_{t+1}) \\
&\qquad + 2\operatorname{cov}(w_{t-1},w_t)+2\operatorname{cov}(w_t,w_{t+1})+2\operatorname{cov}(w_{t-1},w_{t+1})\Big]\\
&= \tfrac19\big[\sigma_w^2+\sigma_w^2+\sigma_w^2+0+0+0\big] = \tfrac39\sigma_w^2 = \tfrac13\sigma_w^2.
\end{aligned}
$$

At $s=t+1$, the windows $\{t,t+1,t+2\}$ and $\{t-1,t,t+1\}$ share exactly the two indices $t$
and $t+1$, so only those two terms survive:

$$\gamma_v(t+1,t) = \tfrac19\big[\operatorname{cov}(w_t,w_t)+\operatorname{cov}(w_{t+1},w_{t+1})\big] = \tfrac29\sigma_w^2.$$

Continuing the same count of overlapping indices out to lag 2, and noting the windows no
longer intersect at all once $|s-t|>2$, gives the full autocovariance function:

$$
\gamma_v(s,t) =
\begin{cases}
\tfrac39\sigma_w^2, & |s-t|=0,\\
\tfrac29\sigma_w^2, & |s-t|=1,\\
\tfrac19\sigma_w^2, & |s-t|=2,\\
0, & |s-t|>2.
\end{cases}
$$

<figure>
<svg viewBox="0 0 340 210" role="img" aria-label="Bar chart of the moving-average autocovariance against lag, peaking at lag 0 and vanishing beyond lag 2">
  <line x1="30" y1="160" x2="320" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <rect x="91" y="123.3" width="18" height="36.7" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="131" y="86.7" width="18" height="73.3" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="171" y="50" width="18" height="110" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="211" y="86.7" width="18" height="73.3" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="251" y="123.3" width="18" height="36.7" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="100" y="118" text-anchor="middle" font-size="11" fill="currentColor">1/9</text>
  <text x="140" y="81" text-anchor="middle" font-size="11" fill="currentColor">2/9</text>
  <text x="180" y="45" text-anchor="middle" font-size="11" fill="currentColor">3/9</text>
  <text x="220" y="81" text-anchor="middle" font-size="11" fill="currentColor">2/9</text>
  <text x="260" y="118" text-anchor="middle" font-size="11" fill="currentColor">1/9</text>
  <text x="60" y="175" text-anchor="middle" font-size="12" fill="currentColor">-3</text>
  <text x="100" y="175" text-anchor="middle" font-size="12" fill="currentColor">-2</text>
  <text x="140" y="175" text-anchor="middle" font-size="12" fill="currentColor">-1</text>
  <text x="180" y="175" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="220" y="175" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="260" y="175" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <text x="300" y="175" text-anchor="middle" font-size="12" fill="currentColor">3</text>
  <text x="175" y="198" text-anchor="middle" font-size="12" fill="currentColor">lag h = s - t</text>
</svg>
<figcaption>The moving-average autocovariance, in units of &#963;<tspan>&#178;</tspan><sub>w</sub>, plotted against the lag h = s - t: it depends only on how far apart s and t are, not on their absolute position, and is zero once the two averaging windows stop overlapping.</figcaption>
</figure>

Why is this interesting? $\gamma_v(s,t)$ depends only on the **lag** $h=s-t$ between $s$ and
$t$, never on their absolute position. Compare that with the mean function, which for this
same process was constant in $t$ too — together these are exactly the two conditions that
will define *stationarity*, which is where the course picks this up next.

### Autocovariance of a random walk

Recall the random walk with (or without) drift, $x_t = \delta t + \sum_{i=1}^t w_i$. Applying
bilinearity again, the deterministic drift terms contribute nothing to a covariance, and the
covariance of the two noise sums is $\sigma^2$ times the number of indices the sums $\sum_{i=1}^s w_i$
and $\sum_{i=1}^t w_i$ have in common, which is $\min(s,t)$:

$$
\gamma(s,t) = \operatorname{cov}(x_s,x_t) = \operatorname{cov}\Big(\sum_{i=1}^s w_i,\ \sum_{i=1}^t w_i\Big) = \sigma^2\min(s,t).
$$

Unlike the moving average, this genuinely depends on the particular values of $s$ and $t$, not
just on the lag between them — a random walk is, in this sense, the opposite of stationary.

## The autocorrelation function

The random-walk autocovariance grows without bound as $\min(s,t)$ grows, which makes it hard
to compare across processes or across pairs of times: is a covariance of 40 "strong" or "weak"?
Normalizing by the standard deviations at each time gives a bounded measure, the
**autocorrelation function (ACF)**:

$$\rho(s,t) = \frac{\gamma(s,t)}{\sqrt{\gamma(s,s)\,\gamma(t,t)}}.$$

This measures the linear predictability of $x_t$ from $x_s$ — how well a straight-line
prediction of $x_t$ can be made using $x_s$ alone.

## Cross-covariance and cross-correlation

The same idea extends to comparing *two different* series $x_t$ and $y_t$, rather than a
series against itself. The **cross-covariance** is

$$\gamma_{xy}(s,t) = \operatorname{cov}(x_s,y_t) = \mathbb{E}\big[(x_s-\mu_{xs})(y_t-\mu_{yt})\big],$$

telling us how the values of $y$ relate to the values of $x$ across time, and the normalized
**cross-correlation** is

$$\rho_{xy}(s,t) = \frac{\gamma_{xy}(s,t)}{\sqrt{\gamma_x(s,s)\,\gamma_y(t,t)}}, \qquad -1\le\rho_{xy}(s,t)\le 1.$$

## Exercises

1. Let $y_t = x_{t-2}$ for some process $x_t$. Find the cross-covariance $\gamma_{xy}(k)$ as a
   function of the lag $k$, and determine at which lag $\gamma_{xy}$ is maximized.

## Sources

- Mean function, variance function, and the four worked examples (white noise, moving
  average, random walk with drift, signal plus noise): *berkeley-stat153*, spring 2026,
  Lecture 3, slides
  [`01-mean-and-variance.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/03_dependence_notes.md),
  CC BY 4.0.
- Autocovariance definition, white noise autocovariance, the bilinearity identity, and the
  full moving-average worked example: same lecture, slides
  [`02-autocovariance.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/03_dependence_notes.md),
  CC BY 4.0.
- Autocovariance of the random walk, the autocorrelation function, cross-covariance, and
  cross-correlation: the fuller version of the same lecture,
  [`Lec03_Notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec03_Notes.tex),
  CC BY 4.0 (this file also carries the cross-covariance exercise used above).
- No transcript, additional notes, or separate problem set were supplied for this lecture.
- Named but not supplied: the assigned reading, Shumway and Stoffer, *Time Series Analysis
  and Its Applications*, Chapter 1.3-1.7. The in-class "poll example" mentioned after the
  cross-correlation definition in `Lec03_Notes.md` is referenced but its content is not in
  the notes. The stationarity discussion the chapter twice defers to ("we'll come back to
  this") belongs to the next lecture, not this one.

---

[← 1. White Noise and Random Walks](01-white-noise-and-random-walks.md) · [Contents](index.md) · [3. Autocovariance and Stationarity →](03-autocovariance-and-stationarity.md)
