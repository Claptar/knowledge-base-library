---
title: "100. Discrete Fourier Transform and Periodogram"
course: "Berkeley Stat 153"
chapter: 100
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 100. Discrete Fourier Transform and Periodogram

## What this covers

Continuing from the sinusoidal regression model of the previous lecture, this chapter asks how to
compute $RSS(f)$ — and hence fit and do inference for the frequency $f$ — efficiently across many
candidate frequencies at once. The answer is the Discrete Fourier Transform (DFT): a single linear
transform of the data whose squared magnitudes *are* the periodogram values needed for $RSS(f)$,
and which can itself be computed in $O(n\log n)$ time by the FFT algorithm. It assumes the
sinusoidal model $y_t = \beta_0+\beta_1\cos(2\pi ft)+\beta_2\sin(2\pi ft)+\epsilon_t$ and the
definitions of $RSS(f)$ and the periodogram $I(f)$ from the previous lecture, recapped below.

## Recap: RSS, Fourier frequencies, and the periodogram

The previous lecture fit the sinusoidal model
$$y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2),$$
to an observed series $y_1,\dots,y_n$. Inference about the frequency $f$ turns on
$$RSS(f) := \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \bigl(y_t - \beta_0 - \beta_1\cos(2\pi ft) - \beta_2 \sin(2\pi ft)\bigr)^2 = \|y - X_f\hat\beta_f\|^2,$$
the residual sum of squares of the linear regression obtained by fixing $f$, where $X_f$ is the design
matrix with columns $1,\ \cos(2\pi ft),\ \sin(2\pi ft)$ and $\hat\beta_f = (X_f^\top X_f)^{-1}X_f^\top y$.
Evaluating $RSS(f)$ separately at every point of a fine grid of $f$ is expensive when $n$ is large, so
the previous lecture proved a shortcut: whenever $f\in(0,0.5)$ is a **Fourier frequency** — meaning
$nf$ is an integer —
$$RSS(f) = \sum_t (y_t-\bar y)^2 - 2I(f), \qquad I(f) := \frac1n\Bigl(\sum_{t=1}^n y_t\cos(2\pi ft)\Bigr)^2 + \frac1n\Bigl(\sum_{t=1}^n y_t \sin(2\pi ft)\Bigr)^2.$$
$I(f)$ is the **periodogram** of the data. This chapter studies the Discrete Fourier Transform of
$y_1,\dots,y_n$ and shows it is essentially the periodogram in disguise — which is what makes $I(f)$,
and hence $RSS(f)$, cheap to compute at every Fourier frequency simultaneously.

## From the periodogram to the DFT

The periodogram can be rewritten using the modulus of a complex number:
$$I(f) = \frac1n\Bigl|\sum_{t=1}^n y_t \exp(-2\pi i f t)\Bigr|^2.$$
The quantity inside the modulus is almost the Discrete Fourier Transform (DFT) of the data. The one
difference is indexing convention: when discussing the DFT it is standard to write the data as
$y_0,y_1,\dots,y_{n-1}$ rather than $y_1,\dots,y_n$ — indexing from $0$, as in Python, rather than from
$1$. With that indexing, the DFT of $y_0,\dots,y_{n-1}$ is the collection of (possibly complex) numbers
$$b_j := \sum_{t=0}^{n-1} y_t \exp\Bigl(-\frac{2\pi i jt}{n}\Bigr), \qquad j = 0,1,\dots,n-1.$$
In words, $b_j$ is the dot product of the data with the complex sinusoid of frequency $f=j/n$, namely
$\exp(2\pi i f t)$ evaluated at $t=0,\dots,n-1$. Even though the $y_t$ are real, the $b_j$ can be
complex.

**Why the indexing does not matter for the periodogram.** In the definition above, $y_0$ is multiplied
by $\exp(0)=1$, $y_1$ by $\exp(-2\pi ij/n)$, and so on. If instead one indexes from $1$ and defines
$\tilde b_j := \sum_{t=1}^n y_t\exp(-2\pi ijt/n)$, then $y_t$ is multiplied by $\exp(-2\pi ijt/n)$ one
step further along, and the two transforms are related by $b_j = \tilde b_j\exp(2\pi ij/n)$. Since
$|\exp(2\pi ij/n)|=1$, this gives $|b_j| = |\tilde b_j|$ — the two indexing conventions produce DFTs
with the same moduli, and since the periodogram only uses moduli, it makes no difference which one is
used. The DFT itself is conventionally indexed from $0$.

The connection to the periodogram and to $RSS$ is now:
$$I(j/n) = \frac{|b_j|^2}{n}, \qquad RSS(j/n) = \sum_t(y_t-\bar y)^2 - 2I(j/n), \qquad 0<\frac jn<\frac12.$$

This matters because the DFT can be computed very efficiently. Computing each $b_j$ directly from its
defining sum costs $O(n)$ operations, and there are $n$ values of $j$, so a naive computation of the
whole DFT costs $O(n^2)$. The **Fast Fourier Transform (FFT)** algorithm exploits symmetry and
redundancy among the complex exponentials to compute the entire DFT in $O(n\log n)$ time instead — in
numpy, `np.fft.fft(y)`. (The lecture did not go over the details of the FFT algorithm itself.)

## Basic properties of the DFT

Three facts about $b_0,\dots,b_{n-1}$ are worth recording.

1. **$b_0$ is the sum of the data.** Setting $j=0$ in the defining sum gives $b_0 = y_0+\dots+y_{n-1}$.

2. **Real and imaginary parts.** In general $b_j$ is complex, with
$$\operatorname{Re}(b_j) = \sum_{t=0}^{n-1} y_t\cos\Bigl(\frac{2\pi jt}{n}\Bigr), \qquad \operatorname{Im}(b_j) = -\sum_{t=0}^{n-1} y_t\sin\Bigl(\frac{2\pi jt}{n}\Bigr).$$
Occasionally the imaginary part vanishes (for instance when $n$ is even and $j=n/2$), but $b_j$ is
generally complex-valued.

3. **Conjugate symmetry.** For $j=1,\dots,n-1$,
$$b_{n-j} = \bar b_j,$$
because
$$b_{n-j} = \sum_t y_t\exp\Bigl(-\frac{2\pi i(n-j)t}{n}\Bigr) = \sum_t y_t \exp\Bigl(\frac{2\pi ijt}{n}\Bigr)\exp(-2\pi it) = \bar b_j,$$
using $\exp(-2\pi it)=1$ for integer $t$, and that $\exp(2\pi ijt/n)$ is the conjugate of
$\exp(-2\pi ijt/n)$. This argument uses that the data are real; if some $y_t$ were complex, the
relation would fail.

Conjugate symmetry means the DFT terms at the higher indices are determined by the ones at the lower
indices — for example, when $n=11$ the DFT is
$$b_0,\,b_1,\,b_2,\,b_3,\,b_4,\,b_5,\,\bar b_5,\,\bar b_4,\,\bar b_3,\,\bar b_2,\,\bar b_1,$$
and when $n=12$ it is
$$b_0,\,b_1,\,b_2,\,b_3,\,b_4,\,b_5,\,b_6=\bar b_6,\,\bar b_5,\,\bar b_4,\,\bar b_3,\,\bar b_2,\,\bar b_1$$
(here $b_6=\bar b_6$ forces $b_6$ to be real). So for $n=11$, eleven real data values correspond to one
real number ($b_0$) and five complex-conjugate pairs; for $n=12$, twelve real data values correspond to
two real numbers ($b_0,b_6$) and five conjugate pairs. Either way the data and its DFT carry the same
amount of information — $n$ real numbers' worth.

The data can in fact be recovered exactly from the DFT, by an **inverse DFT formula**. Getting there
requires understanding the orthogonality of complex sinusoids at Fourier frequencies.

## Complex sinusoids and the orthogonal basis $u^0,\dots,u^{n-1}$

Sinusoids are linear combinations of $\cos(2\pi ft)$ and $\sin(2\pi ft)$, and algebra with them is
easier in complex-exponential form:
$$\cos(2\pi ft) = \tfrac12 e^{2\pi ift} + \tfrac12 e^{-2\pi ift}, \qquad \sin(2\pi ft) = \tfrac1{2i}e^{2\pi ift} - \tfrac1{2i}e^{-2\pi ift}.$$
When working with real sinusoids at integer time points, $f$ could be restricted to $[0,1/2]$. Once
complex exponentials are in play, the $e^{-2\pi ift}$ term equals $e^{2\pi i(-f)t}$, so negative
frequencies $-f\in(-1/2,0)$ appear too, and the natural range becomes $f\in[-0.5,0.5)$ — this is what
`np.fft.fftfreq(n)` returns ($f=-0.5$ and $f=0.5$ give the same exponential, so one of them is
dropped).

Alternatively, negative frequencies can be avoided altogether, using
$$e^{-2\pi ift} = \cos(2\pi ft) - i\sin(2\pi ft) = \cos(2\pi(1-f)t) + i\sin(2\pi(1-f)t) = e^{2\pi i(1-f)t}$$
(valid because $t$ is an integer, so $\cos(2\pi t - 2\pi ft)=\cos(2\pi ft)$ and
$\sin(2\pi t-2\pi ft) = -\sin(2\pi ft)$). This lets $e^{2\pi ift}$ be restricted to $f\in[0,1)$ instead
— the convention used from here on.

For $j=0,1,\dots,n-1$, define the vector
$$u^j = \bigl(1,\ e^{2\pi ij/n},\ e^{2\pi i\cdot2j/n},\ \dots,\ e^{2\pi i(n-1)j/n}\bigr)^\top,$$
the complex sinusoid of Fourier frequency $f=j/n$ sampled at $t=0,\dots,n-1$. Immediately,
$u^0=(1,\dots,1)^\top$, and for $1\le j\le n-1$, $u^j = \bar u^{\,n-j}$.

The key property is **orthogonality**: for $0\le j\ne k\le n-1$,
$$\langle u^j,u^k\rangle = 0,$$
using the complex inner product $\langle a,b\rangle = \sum_t a_t\bar b_t$ (note the conjugate on the
second argument). To see this, fix $j\ne k$ and write
$$\langle u^j,u^k\rangle = \sum_{t=0}^{n-1} e^{2\pi i\frac jn t}\,\overline{e^{2\pi i\frac kn t}} = \sum_{t=0}^{n-1}\Bigl[e^{2\pi i\frac{j-k}n}\Bigr]^t = \frac{1-e^{2\pi i(j-k)}}{1-e^{2\pi i(j-k)/n}} = \frac{1-\cos(2\pi(j-k))-i\sin(2\pi(j-k))}{1-e^{2\pi i(j-k)/n}} = 0,$$
since $j-k$ is a nonzero integer, so the numerator is $1-1-i\cdot0 = 0$ while the denominator is
nonzero (as $j\ne k$ and $0\le j,k\le n-1$). Taking $j=k$ in the same geometric-series computation,
before the final cancellation, gives instead
$$\langle u^j,u^j\rangle = \|u^j\|^2 = n.$$
So $u^0,\dots,u^{n-1}$ are $n$ mutually orthogonal vectors in $\mathbb C^n$, all of squared length $n$
— hence a basis for $\mathbb C^n$. Every length-$n$ complex vector is a linear combination of them.

## Recovering the data: the inverse DFT

Because $u^0,\dots,u^{n-1}$ form a basis, the data vector $y=(y_0,\dots,y_{n-1})^\top$ can be written
$$y = a_0u^0 + a_1u^1 + \dots + a_{n-1}u^{n-1}$$
for some complex coefficients $a_j$. Taking the inner product of both sides with a fixed $u^j$ and using
orthogonality — $\langle u^j,u^k\rangle=0$ for $k\ne j$ and $\langle u^j,u^j\rangle = n$ — isolates
$$a_j = \frac1n\langle y,u^j\rangle = \frac1n\sum_{t=0}^{n-1} y_t\exp\Bigl(-\frac{2\pi ijt}{n}\Bigr) = \frac{b_j}{n}.$$
So $a_j$ is exactly $b_j/n$, and the expansion becomes $y = \frac1n(b_0u^0+\dots+b_{n-1}u^{n-1})$, or
entrywise,
$$y_t = \frac1n\sum_{j=0}^{n-1} b_j\exp\Bigl(\frac{2\pi ijt}{n}\Bigr), \qquad t=0,1,\dots,n-1.$$
This is the **inverse DFT formula**. It looks like the forward DFT with two changes: the sign in the
exponent flips, and there is a factor of $\frac1n$. The data and the DFT are two representations of the
same information, related by an orthogonal (up to scaling) change of basis.

## Back to inference: why the DFT earns its keep

### Efficient RSS, and the Bayesian posterior

Restricting attention to Fourier frequencies $f\in(0,0.5)$ turns the periodogram, and hence
$RSS(f) = \sum_t(y_t-\bar y)^2 - 2I(f)$, into something the FFT computes for every such $f$ at once, in
$O(n\log n)$ time — rather than solving a separate least-squares problem, at $O(n)$ cost each, on every
point of a grid. The MLE of $f$ is the minimiser of $RSS(f)$, so this is already a large saving; the
Bayesian posterior benefits the same way. Recall the posterior for $f$ takes the form
$$\propto \Bigl(\frac1{RSS(f)}\Bigr)^{(n-3)/2}\,|X_f^\top X_f|^{-1/2}\,\mathbb 1\{0<f<1/2\}.$$
For a Fourier frequency $f\in(0,1/2)$, $X_f^\top X_f = \operatorname{diag}(n,\,n/2,\,n/2)$ (established
in an earlier lecture), so $|X_f^\top X_f| = n^3/8$ regardless of $f$. The determinant term therefore
drops out of the posterior when restricted to Fourier frequencies, leaving simply
$$\propto \Bigl(\frac1{RSS(f)}\Bigr)^{(n-3)/2}\mathbb 1\{0<f<1/2\},$$
which the periodogram again makes cheap to evaluate over the whole grid of Fourier frequencies.

### More than one frequency

The periodogram is also a diagnostic: a plot of $I(j/n)$ against $j/n$ showing two prominent peaks
suggests the two-sinusoid model
$$y_t = \beta_0+\beta_1\cos(2\pi f_1t)+\beta_2\sin(2\pi f_1t)+\beta_3\cos(2\pi f_2t)+\beta_4\sin(2\pi f_2t)+\epsilon_t.$$

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A periodogram with two prominent peaks, one at each of two frequencies">
  <line x1="40" y1="160" x2="310" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="160" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="40,155 60,153 80,150 100,140 115,90 125,45 135,90 150,140 170,152 190,155 205,150 215,120 225,70 235,45 245,70 255,120 270,150 290,154 310,155" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="125" y1="160" x2="125" y2="45" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="235" y1="160" x2="235" y2="45" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="125" y="176" text-anchor="middle" font-size="12" fill="currentColor">f₁</text>
  <text x="235" y="176" text-anchor="middle" font-size="12" fill="currentColor">f₂</text>
  <text x="305" y="176" text-anchor="middle" font-size="12" fill="currentColor">f</text>
  <text x="55" y="30" text-anchor="middle" font-size="12" fill="currentColor">I(f)</text>
</svg>
<figcaption>A periodogram with two prominent peaks at $f_1$ and $f_2$ suggests fitting a two-sinusoid
model rather than a single one.</figcaption>
</figure>

Inference proceeds exactly as before, with $RSS(f_1,f_2)$ now the minimum over five coefficients
$\beta_0,\dots,\beta_4$ against the corresponding five-column design matrix $X_{f_1,f_2}$, and the MLE
and Bayesian posterior for $(f_1,f_2)$ defined analogously to the one-frequency case. When $f_1,f_2$ are
both Fourier frequencies strictly between $0$ and $0.5$,
$$RSS(f_1,f_2) = \sum_t(y_t-\bar y)^2 - 2I(f_1) - 2I(f_2)$$
— the two-frequency RSS decomposes additively into periodogram values, so restricting to Fourier
frequencies keeps the joint search over $(f_1,f_2)$ cheap. Without that restriction, minimising
$RSS(f_1,f_2)$ over a grid, or evaluating the posterior on one, is computationally expensive.

### Other nonlinear regression models

The same RSS-minimisation approach extends beyond pure sinusoids. Two examples: a sinusoid
superimposed on a linear trend,
$$y_t = \beta_0+\beta_1t+\beta_2\cos(2\pi ft)+\beta_3\sin(2\pi ft)+\epsilon_t, \qquad RSS(f) = \min_{\beta_0,\dots,\beta_3}\sum_t\bigl(y_t-\beta_0-\beta_1t-\beta_2\cos(2\pi ft)-\beta_3\sin(2\pi ft)\bigr)^2,$$
and the **broken-stick** (piecewise-linear) regression model,
$$y_t = \beta_0+\beta_1t+\beta_2(t-s)_++\epsilon_t, \qquad RSS(s) = \min_{\beta_0,\beta_1,\beta_2}\sum_t\bigl(y_t-\beta_0-\beta_1t-\beta_2(t-s)_+\bigr)^2,$$
named for the shape of $t\mapsto\beta_0+\beta_1t+\beta_2(t-s)_+$, which bends at the knot $s$. Both are
fit by minimising their $RSS$ over the free nonlinear parameter ($f$ or $s$) exactly as in the
single-sinusoid model — though, unlike the sinusoidal case, there is no periodogram shortcut here, since
neither reduces to a sum over Fourier frequencies. Homework Two takes up further examples of this kind.

## Sources

- Fall 2025, *Lecture Eight* (Aditya Guntuboyina, 23 September 2025): the recap of $RSS(f)$ and the
  periodogram, the DFT definition and its connection to the periodogram, the indexing convention, the
  basic properties of the DFT, complex sinusoids, the orthogonal basis $u^0,\dots,u^{n-1}$, and the
  inverse-DFT derivation — `docs/statistics/berkeley/stat153/fall-2025/LectureEight153248Fall2025/`,
  files `01-1-recap-from-last-lecture.md` through `04-4-complex-sinuoids-and-orthogonality.md`.
- Spring 2025, *Lecture Eight* (Aditya Guntuboyina, 13 February 2025): the periodogram definition, and
  its use for efficient $RSS$ computation, the Bayesian posterior for $f$ (referring back to a result on
  $X_f^\top X_f$ from "Lecture 6", not itself supplied), the two-frequency model, and the trend+sinusoid
  and broken-stick regression models —
  `docs/statistics/berkeley/stat153/spring-2025/LectureEight153248Spring2025/01-1-dft.md` and
  `02-3-utility-of-the-periodogram.md`.
- Both sets of notes are model reconstructions of PDF slide decks with no usable text layer and no
  accompanying transcript (see the fidelity banner on each file); every equation in the source is
  marked unverified there. No lecture transcript, slide deck, or problem set was supplied for this
  chapter. The single-sinusoid model derivation from the lecture immediately before this one, "Lecture
  6"'s derivation of $X_f^\top X_f$, and "Homework Two" are all referred to in the notes but were not
  themselves supplied.

---

[← 99. Sinusoid, Yule, and AR(2) Models](99-sinusoid-yule-and-ar-2-models.md) · [Contents](index.md) · [101. AR(p) Estimation and Forecasting (part 2) →](101-ar-p-estimation-and-forecasting-part-2.md)
