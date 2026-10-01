---
title: "62. The Discrete Fourier Transform"
course: "Berkeley Stat 153"
chapter: 62
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 62. The Discrete Fourier Transform

## What this covers

This chapter continues the search for the frequency $f$ that best fits a periodic regression model
to data $y_1,\dots,y_n$. It recaps how minimizing the residual sum of squares $RSS(f)$ over a grid
of admissible frequencies turns into maximizing a quantity called the periodogram, and it introduces
the discrete Fourier transform (DFT) as the object whose values *are* the periodogram — one that can
be computed at every relevant frequency at once in $O(n\log n)$ time rather than $O(n^2)$. It
assumes the harmonic regression model $y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2\sin(2\pi f t)
+ \epsilon_t$ and the reduction of $RSS(f)$ to a closed-form expression in $f$ from the previous
lecture; that reduction is recapped here rather than rederived.

## Recap: from RSS to the periodogram

The model under study is
$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad \epsilon_t \overset{iid}{\sim} N(0,\sigma^2), \quad t=1,\dots,n,$$
with $\beta_0,\beta_1,\beta_2$ the main parameters, estimated by least squares for a fixed frequency
$f$:
$$RSS(f) = \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \big[y_t - \beta_0 - \beta_1\cos 2\pi f t - \beta_2 \sin 2\pi f t\big]^2.$$
The search can be restricted to $f\in[0,\tfrac12]$. Finding $\hat f$ by brute force means laying a
grid of $f$-values over $[0,\tfrac12]$, computing $RSS(f)$ at each, and minimizing — so what is
needed is a formula for $RSS(f)$ cheap enough to evaluate over the whole grid.

The grid that turns out to matter is the set of **Fourier frequencies**: those $f \in [0,\tfrac12]$
with $nf$ an integer,
$$f \in \begin{cases} \left\{0,\ \dfrac1n,\ \dfrac2n,\ \dots,\ \dfrac{(n-1)/2}{n}\right\} & n \text{ odd} \\[4pt] \left\{0,\ \dfrac1n,\ \dfrac2n,\ \dots,\ \dfrac{n/2}{n}\right\} & n \text{ even.}\end{cases}$$

At a Fourier frequency with $0<f<\tfrac12$, the previous lecture derived
$$RSS(f) = \sum_{t=1}^n (y_t-\bar y)^2 - \frac{2}{n}\Big[(y\cdot\cos)^2 + (y\cdot \sin)^2\Big],$$
where
$$y\cdot\cos = \sum_{t=1}^n y_t\cos 2\pi f t, \qquad y\cdot\sin=\sum_{t=1}^n y_t \sin 2\pi ft$$
are ordinary real dot products of the data with a cosine wave and a sine wave of frequency $f$.
Writing
$$I(f) = \frac1n\Big[(y\cdot\cos)^2+(y\cdot\sin)^2\Big], \qquad 0<f<\tfrac12,\ f \text{ a Fourier frequency},$$
the recap formula collapses to
$$RSS(f) = \sum_{t=1}^n(y_t-\bar y)^2 - 2I(f).$$
The first term does not depend on $f$, so **minimizing $RSS(f)$ over Fourier frequencies is the same
problem as maximizing $I(f)$** over Fourier frequencies. $I(f)$ is the **periodogram**.

## Rewriting the periodogram with complex exponentials

Euler's formula, $e^{i\theta}=\cos\theta + i\sin\theta$, packages the two real dot products inside
$I(f)$ into a single complex number. For complex vectors $a=(a_1,\dots,a_n)$ and $b=(b_1,\dots,b_n)$,
define the complex inner product
$$a\cdot b = \langle a,b\rangle = \sum_{j=1}^n a_j\,\overline{b_j},$$
with a complex conjugate on the second argument — this reuses the symbol $\cdot$ already used above
for a real dot product; which one is meant is clear from whether the vectors involved are real or
complex. Then
$$\sum_{t=1}^n y_t e^{-2\pi i f t} = y \cdot e^{2\pi i f t},$$
and expanding the exponential by Euler's formula shows this complex number has real part $y\cdot\cos$
and imaginary part $-(y\cdot\sin)$. Its squared modulus recovers the periodogram exactly:
$$I(f) = \frac1n\left|y\cdot e^{2\pi i ft}\right|^2 = \frac1n\Big[(y\cdot\cos)^2+(y\cdot\sin)^2\Big].$$

## The discrete Fourier transform

Re-index the data starting from $0$ rather than $1$: $y_0,y_1,\dots,y_{n-1}$. For each
$j=0,1,\dots,n-1$, define
$$b_j = \sum_{t=0}^{n-1} y_t \exp\!\left(-2\pi i \frac{j}{n}t\right) = y\cdot \exp\!\left(2\pi i\frac jn t\right) = \langle y, u^j\rangle,$$
where $u^j = \big(\exp(2\pi i \tfrac jn t)\big)_{t=0,\dots,n-1}$ is the vector of samples of the
complex sinusoid of frequency $j/n$ — data coming from that sinusoid. The sequence
$(b_0,\dots,b_{n-1})$ is the **discrete Fourier transform (DFT)** of $y_0,\dots,y_{n-1}$: it is
exactly the construction $y\cdot e^{2\pi ift}$ above, evaluated only at the Fourier frequencies
$f=j/n$. So the periodogram at a Fourier frequency is a rescaled squared DFT coefficient,
$$I\!\left(\frac jn\right) = \frac{|b_j|^2}{n}, \qquad 0<\frac jn<\frac12,$$
and $RSS(j/n) = \sum_t(y_t-\bar y)^2 - 2I(j/n)$. Although the data $y_0,\dots,y_{n-1}$ are always
real, the transform $b_j$ is in general complex.

## Two indexing conventions

The DFT can equally well be written with the data indexed from $1$:
$$\tilde b_j = \sum_{t=1}^n y_t \exp\!\left(-2\pi i\frac jn t\right).$$
Lining the two sums up term by term — $b_j$ pairs the first data point with $\exp(-2\pi i\tfrac jn
\cdot 0)$, the second with $\exp(-2\pi i \tfrac jn \cdot 1)$, and so on, while $\tilde b_j$ pairs the
same data points with every exponent shifted up by one — shows the two differ only by an overall
phase:
$$b_j = \tilde b_j \exp\!\left(\frac{2\pi i j}{n}\right).$$
Since $\big|\exp(2\pi i j/n)\big| = 1$, this rotation does not change magnitude: $|b_j| = |\tilde
b_j|$. That is why the choice of indexing convention is immaterial to the periodogram, which only
ever uses $|b_j|^2$. From here on, the $0$-indexed convention
$$b_j = \sum_{t=0}^{n-1} y_t \exp\!\left(-2\pi i \frac jn t\right), \qquad j=0,1,\dots,n-1,$$
is the one used.

## Why bother: the FFT

The point of packaging the periodogram this way is computational. The DFT values
$b_0,\dots,b_{n-1}$ — hence $I(j/n)$ at every Fourier frequency at once — can be computed by the
**fast Fourier transform (FFT)** algorithm of Cooley and Tukey in $O(n\log n)$ operations, rather
than the $O(n^2)$ that evaluating every $b_j$ directly as a length-$n$ sum would cost. (The
algorithm's efficiency comes from splitting a transform of size $n$ into transforms of half the
size; the lecture illustrated this by reducing a transform of size $n=4$ to ones of size $n=2$, a
diagram the notes do not preserve in enough detail to reconstruct here.)

## The DFT of real data has a mirror symmetry

A few structural facts about $b_j$, for real data $y_0,\dots,y_{n-1}$:

**The $j=0$ term is real and uninteresting.** $b_0 = \sum_{t=0}^{n-1} y_t$ is just the sum of the
data — it carries no frequency information.

**In general $b_j$ is complex,**
$$b_j = \sum_{t=0}^{n-1} y_t \cos\!\left(2\pi \frac jn t\right) - i\sum_{t=0}^{n-1} y_t \sin\!\left(2\pi \frac jn t\right),$$
though it can happen to be real — e.g. when $n$ is even and $j=n/2$ (the **Nyquist** term).

**Conjugate symmetry.** $b_{n-j} = \overline{b_j}$. This follows from
$$b_{n-j} = \sum_t y_t \exp\!\left(-2\pi i\frac{n-j}{n}t\right) = \sum_t y_t \underbrace{\exp(-2\pi i t)}_{=\,1 \text{ for integer } t}\exp\!\left(2\pi i \frac jn t\right) = \sum_t y_t \exp\!\left(2\pi i\frac jn t\right),$$
and, using $e^{i\theta} = \overline{e^{-i\theta}}$ and that each $y_t$ is real (so it can be moved
inside a conjugate for free),
$$\sum_t y_t \exp\!\left(2\pi i\frac jn t\right) = \sum_t \overline{y_t\exp\!\left(-2\pi i\frac jn t\right)} = \overline{b_j}.$$

So a real data sequence's DFT is determined by roughly its first half: $b_0$ (real), then complex
terms up to the middle, with everything past the middle a conjugate of something already computed.
For $n=11$:
$$y_0,\dots,y_{10} \;\longrightarrow\; \underbrace{b_0}_{\text{real}},\ \underbrace{b_1,b_2,b_3,b_4,b_5}_{\text{complex}},\ \overline{b_5},\overline{b_4},\overline{b_3},\overline{b_2},\overline{b_1},$$
and for $n=10$:
$$y_0,\dots,y_9 \;\longrightarrow\; b_0,\ b_1,b_2,b_3,b_4,\ \underbrace{b_5}_{\text{real (Nyquist)}},\ \overline{b_4},\overline{b_3},\overline{b_2},\overline{b_1}.$$
Since $I(j/n) = |b_j|^2/n$ and $|\overline{b_j}| = |b_j|$, the periodogram inherits the same mirror
symmetry, $I\!\left(\frac{n-j}{n}\right) = I\!\left(\frac jn\right)$ — for $n=11$, for instance,
$I(6/11) = I(5/11)$.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Conjugate pairing of the ten DFT coefficients of real data with n=10">
  <line x1="30" y1="140" x2="311" y2="140" stroke="currentColor" stroke-width="1" opacity="0.4"/>
  <path d="M156,140 Q185,110 214,140" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <path d="M127,140 Q185,85 243,140" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <path d="M98,140 Q185,60 272,140" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <path d="M69,140 Q185,32 301,140" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <g font-size="12" text-anchor="middle" fill="currentColor">
    <circle cx="40" cy="140" r="4"/>
    <text x="40" y="160">b0</text>
    <text x="40" y="176" font-size="10">real</text>
    <circle cx="69" cy="140" r="3"/>
    <text x="69" y="160">b1</text>
    <circle cx="98" cy="140" r="3"/>
    <text x="98" y="160">b2</text>
    <circle cx="127" cy="140" r="3"/>
    <text x="127" y="160">b3</text>
    <circle cx="156" cy="140" r="3"/>
    <text x="156" y="160">b4</text>
    <circle cx="185" cy="140" r="4"/>
    <text x="185" y="160">b5</text>
    <text x="185" y="176" font-size="10">real</text>
    <circle cx="214" cy="140" r="3"/>
    <text x="214" y="160">b6</text>
    <circle cx="243" cy="140" r="3"/>
    <text x="243" y="160">b7</text>
    <circle cx="272" cy="140" r="3"/>
    <text x="272" y="160">b8</text>
    <circle cx="301" cy="140" r="3"/>
    <text x="301" y="160">b9</text>
  </g>
</svg>
<figcaption>For real data with $n=10$: $b_0$ and the Nyquist coefficient $b_5$ are real; every other
coefficient is mirrored across the midpoint by conjugation, $b_{n-j}=\overline{b_j}$.</figcaption>
</figure>

## Recovering the data: the inverse DFT

The DFT is invertible: the original data can be recovered from $b_0,\dots,b_{n-1}$ by
$$y_t = \frac1n\sum_{j=0}^{n-1} b_j \exp\!\left(2\pi i \frac jn t\right), \qquad t=0,\dots,n-1,$$
called the **inverse discrete Fourier transform (IDFT)**. The DFT and its inverse are the two
directions of a single passage between two representations of the same data: $y_t$ in the **time
domain**, and $b_j$ in the **frequency domain**.

## Proof of the inverse DFT

The proof rests on the vectors $u^j = \big(\exp(2\pi i\tfrac jn t)\big)_{t=0,\dots,n-1}$,
$j=0,\dots,n-1$, forming an **orthogonal basis** of the space of length-$n$ (complex) vectors. They
satisfy, as a fact used without further proof here,
$$\langle u^j, u^k\rangle = \begin{cases} 0 & j\neq k \\ n & j=k.\end{cases}$$
Being orthogonal, of constant length, and $n$ of them in an $n$-dimensional space, $u^0,\dots,u^{n-1}$
form a basis: every length-$n$ vector is a linear combination of them. In particular the data vector
$y$ can be written
$$y = a_0 u^0 + a_1 u^1 + \dots + a_{n-1}u^{n-1}$$
for some coefficients $a_0,\dots,a_{n-1}$. Taking the inner product of both sides with $u^j$ and
using orthogonality to kill every term except $k=j$:
$$\langle y, u^j\rangle = a_0\langle u^0,u^j\rangle + \dots + a_{n-1}\langle u^{n-1},u^j\rangle = a_j\langle u^j,u^j\rangle = a_j n,$$
so
$$a_j = \frac1n\langle y,u^j\rangle = \frac{b_j}{n},$$
recalling that $b_j = \langle y,u^j\rangle$ is exactly the definition of the DFT. Substituting back,
$$y = \frac{b_0}{n}u^0 + \frac{b_1}{n}u^1 + \dots + \frac{b_{n-1}}{n}u^{n-1},$$
and reading off the $t$-th coordinate on both sides — $u^j_t = \exp(2\pi i \tfrac jn t)$ — gives the
inverse DFT:
$$y_t = \frac1n\sum_{j=0}^{n-1} b_j \exp\!\left(2\pi i\frac jn t\right).$$

## Sources

- Handwritten lecture notes, `HandwrittenNotesLectureEight153248Fall2025` (Berkeley STAT 153, Fall
  2025, Lecture 8), sections *Recap from last lecture*, *Indexing starting at 0 vs 1*, *More on
  DFT*, and *Proof of IDFT* — all four sections of the lecture, used in full and in their given
  order.
- These notes are a model's reconstruction of a scanned handwritten PDF with no text layer; the
  source itself flags every equation in it as unverified, so the formulas above should be checked
  against the original PDF before being relied on as authoritative.
- The reduction of $RSS(f)$ to the periodogram formula opening the recap section was derived in the
  *previous* lecture (referenced here as "last class"); that derivation is not part of this input
  set and is not reproduced.
- The FFT's divide-and-conquer illustration ("$n=4$", "$n=2$") corresponds to a diagram in the
  original handwritten page that the conversion did not capture beyond those two labels; only its
  existence and rough content are noted here, not reconstructed.

---

[← 61. Regression for Time Series Trends](61-regression-for-time-series-trends.md) · [Contents](index.md) · [63. AR(p) Estimation and Multistep Forecasting →](63-ar-p-estimation-and-multistep-forecasting.md)
