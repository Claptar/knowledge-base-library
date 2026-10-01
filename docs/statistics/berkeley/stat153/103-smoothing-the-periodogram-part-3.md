---
title: "103. Smoothing the Periodogram (part 3)"
course: "Berkeley Stat 153"
chapter: 103
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 103. Smoothing the Periodogram (part 3)

## What this covers

The periodogram tells us which frequencies drive a time series, but as a statistic it is wildly
noisy — even computed from otherwise well-behaved data, its ordinates jump around from one
frequency to the next. This chapter builds a genuine probability model for that noise (the
*spectrum model*), gives the model in three equivalent forms, and uses it to explain why fitting it
by unregularized maximum likelihood is pointless — the fit just reproduces the raw periodogram. It
ends with the practical fix: a smoothness penalty on the log-spectrum. It assumes the discrete
Fourier transform (DFT) $b_j$, the periodogram $I(j/n)$, and the inverse DFT formula, all covered in
earlier lectures.

## Why the periodogram needs smoothing

Given a time series $y_0, \dots, y_{n-1}$, the periodogram is
$$I(j/n) := \frac{|b_j|^2}{n}, \qquad 0 < \frac j n < \frac12,$$
where $b_j$ is the DFT,
$$b_j := \sum_{t=0}^{n-1} y_t \exp\left(-\frac{2\pi i jt}{n}\right).$$
Take $n$ odd and $m = (n-1)/2$; the periodogram is then defined for $j = 1, \dots, m$. It shows
which frequencies contribute most strongly to the series, and is the usual tool for spotting
dominant cyclical behaviour.

The trouble is that for most real datasets the periodogram — especially on the log scale — looks
rough and noisy rather than showing a clean trend. We want a principled way to smooth it, and the
natural route is to build a model for the noise rather than smooth it by eye.

## A model for the noise in the periodogram

For a smooth trend $\mu_t$ underlying data $y_t$, the natural model is additive Gaussian noise,
$y_t = \mu_t + \epsilon_t$ with $\epsilon_t$ i.i.d. $N(0,\sigma^2)$. The same idea does not transfer
to the periodogram: $I(j/n)$ is always positive, so Gaussian noise is the wrong shape, and the noise
is more nearly additive on the *log* periodogram than on the periodogram itself. Both facts point to
a *multiplicative* noise model,
$$I(j/n) = f(j/n)\,\eta_j, \qquad j = 1, \dots, m,$$
where $f(j/n)$ is the smooth trend we actually want, and the $\eta_j$ are i.i.d. noise with
$$\eta_j \sim \tfrac12 \chi^2_2.$$
This choice of noise distribution is not arbitrary. The $\chi^2_2$ density is
$f_{\chi^2_2}(x) = \tfrac12 e^{-x/2}\mathbb 1\{x>0\}$, so the density of $\chi^2_2/2$ is
$$f_{\chi^2_2/2}(x) = 2f_{\chi^2_2}(2x) = e^{-x}\mathbb 1\{x>0\},$$
which is exactly the standard exponential density. So $\chi^2_2/2 = \mathrm{Exp}(1)$, and the model
can equally be written
$$I(j/n) = f(j/n)\,\eta_j, \qquad \eta_j \overset{\text{i.i.d.}}{\sim} \mathrm{Exp}(1). \qquad \text{(the spectrum model)}$$
Taking logs turns this into an additive model,
$$\log I(j/n) = \log f(j/n) + \log \eta_j, \qquad \eta_j \overset{\text{i.i.d.}}{\sim} \mathrm{Exp}(1),$$
but with a catch: the noise term $\log \eta_j$ does not have mean zero — for $\eta \sim \mathrm{Exp}(1)$,
$\mathbb E[\log \eta] = -\gamma \approx -0.5772$ (the Euler–Mascheroni constant). So $\log f(j/n)$ is
*not* the mean of $\log I(j/n)$; it sits strictly above it. What $f(j/n)$ *does* equal is the mean of
$I(j/n)$ itself, since $\mathbb E[\eta_j] = 1$.

## Power spectral density

Because $f(j/n)$ is the mean of $I(j/n)$, it is called the **power of frequency $j/n$**. Plotting
the points $(j/n, f(j/n))$ for $j=1,\dots,m$ and joining them gives the **power spectral density**, a
function on $[0, 0.5]$. It is not a probability density — it need not integrate to one. (This is an
informal definition; a rigorous one is in Chapter 4 of Shumway and Stoffer, or in Percival and
Walden's *Spectral Analysis for Univariate Time Series* — neither is reproduced here.)

## The same model, from the DFT

The spectrum model can also be stated directly on the DFT coefficients.

**Definition 1.** $\mathrm{Re}(b_j), \mathrm{Im}(b_j)$ are independent across $j = 1,\dots,m$ and
within $j$, with
$$\mathrm{Re}(b_j), \mathrm{Im}(b_j) \overset{\text{i.i.d.}}{\sim} N(0, \gamma_j^2).$$
Here $\gamma_j$ measures the strength of the sinusoid at frequency $j/n$. From the definition of the
periodogram,
$$I(j/n) = \frac{|b_j|^2}{n} = \frac{1}{n}\Big((\mathrm{Re}\,b_j)^2 + (\mathrm{Im}\,b_j)^2\Big)
= \frac{2\gamma_j^2}{n}\cdot\frac12\left(\left(\frac{\mathrm{Re}\,b_j}{\gamma_j}\right)^2 + \left(\frac{\mathrm{Im}\,b_j}{\gamma_j}\right)^2\right).$$
Under Definition 1 the term in parentheses is a sum of two squared standard normals, so it is
$\chi^2_2$-distributed, and
$$I(j/n) = \frac{2\gamma_j^2}{n}\,\eta_j, \qquad \eta_j \overset{\text{i.i.d.}}{\sim} \tfrac12\chi^2_2 = \mathrm{Exp}(1).$$
This is exactly the spectrum model with $f(j/n) = 2\gamma_j^2/n$. Definition 1 is therefore just
another formulation of the same model, and the periodogram is a **sufficient statistic** for it: the
likelihood
$$\prod_{j=1}^m \frac{1}{\gamma_j^2}\exp\left(-\frac{|b_j|^2}{2\gamma_j^2}\right)
= \prod_{j=1}^m \frac{1}{\gamma_j^2}\exp\left(-\frac{nI(j/n)}{2\gamma_j^2}\right)$$
depends on the data only through $I(1/n), \dots, I(m/n)$.

## Back to the data: a sinusoid formulation

Because $y_t$ can itself be recovered from the DFT via the inverse DFT formula
$$y_t = \frac1n \sum_{j=0}^{n-1} b_j \exp\left(\frac{2\pi i jt}{n}\right), \qquad t=0,\dots,n-1,$$
the model can be pushed all the way back to a statement about $y_t$ directly. Expanding
$b_j = \mathrm{Re}(b_j) + i\,\mathrm{Im}(b_j)$ and
$\exp(2\pi i jt/n) = \cos(2\pi jt/n) + i \sin(2\pi jt/n)$, then discarding the imaginary part (since
$y_t$ is real), leaves
$$y_t = \frac{b_0}{n} + \frac1n\sum_{j=1}^{n-1}\Big(\mathrm{Re}(b_j)\cos\tfrac{2\pi jt}{n} - \mathrm{Im}(b_j)\sin\tfrac{2\pi jt}{n}\Big).$$
Splitting the sum at $j=m$ and using the conjugate symmetry $b_{n-j} = \overline{b_j}$ (equivalently
$\mathrm{Re}(b_{n-j}) = \mathrm{Re}(b_j)$, $\mathrm{Im}(b_{n-j}) = -\mathrm{Im}(b_j)$) folds the
second half of the sum onto the first, giving
$$y_t = \beta_0 + \sum_{j=1}^m \left(\beta_{1j}\cos\frac{2\pi jt}{n} + \beta_{2j}\sin\frac{2\pi jt}{n}\right),$$
with
$$\beta_0 = \frac{b_0}{n}, \qquad \beta_{1j} = \frac{2\,\mathrm{Re}(b_j)}{n}, \qquad \beta_{2j} = -\frac{2\,\mathrm{Im}(b_j)}{n}.$$
This identity holds for *every* dataset — it is just a rewriting of the inverse DFT. Combined with
Definition 1, it gives a third form of the same model:

**Definition 2.** $y_t = \beta_0 + \sum_{j=1}^m (\beta_{1j}\cos\frac{2\pi jt}{n} + \beta_{2j}\sin\frac{2\pi jt}{n})$,
with all the $\beta_{1j}, \beta_{2j}$ independent and
$\beta_{1j}, \beta_{2j} \overset{\text{i.i.d.}}{\sim} N(0, \tau_j^2)$.

**Definition 3.** $I(j/n) = f(j/n)\eta_j$ with $\eta_j \overset{\text{i.i.d.}}{\sim} \mathrm{Exp}(1)$.

The three parameterizations — $\gamma_j^2$ (Definition 1), $\tau_j^2$ (Definition 2), and $f(j/n)$
(Definition 3) — describe the same model and convert into one another by
$$\tau_j^2 = \frac{4\gamma_j^2}{n^2}, \qquad f(j/n) = \frac{2\gamma_j^2}{n} = \frac{n\tau_j^2}{2}.$$

## What the spectral density says about $y_t$

Definition 2 makes the payoff of the model concrete: it fixes both the variance of $y_t$ and its
autocovariance in terms of the shape of $f$. Since the $\beta_{1j}, \beta_{2j}$ are independent
mean-zero terms,
$$\mathrm{var}(y_t) = \sum_{j=1}^m \tau_j^2 = \frac2n \sum_{j=1}^m f(j/n) \approx 2\int_0^{1/2} f(\omega)\, d\omega,$$
so the variance of the series is, approximately, twice the area under the power spectral density.
And for the covariance between observations $h$ steps apart,
$$\mathrm{cov}(y_t, y_{t+h}) = \sum_{j=1}^m \tau_j^2 \cos\left(\frac{2\pi jh}{n}\right)
= \frac2n\sum_{j=1}^m f(j/n)\cos\left(\frac{2\pi jh}{n}\right) \approx 2\int_0^{1/2} f(\omega)\cos(2\pi \omega h)\, d\omega.$$
This covariance need not be zero, so the spectrum model — despite being built out of *independent*
Fourier coefficients — perfectly accommodates a $y_t$ that is correlated across time: the dependence
structure is entirely encoded in the shape of $f$, not in any explicit correlation parameter.

## Fitting the model by maximum likelihood overfits

Take the likelihood in the DFT form (Definition 1):
$$\prod_{j=1}^m \frac{1}{\gamma_j^2}\exp\left(-\frac{nI(j/n)}{2\gamma_j^2}\right).$$
(Working instead from Definition 3 and the exponential density of $\eta_j$ gives
$\prod_{j=1}^m \frac{1}{f(j/n)}\exp(-I(j/n)/f(j/n))$, the same likelihood up to the identification
$f(j/n) = 2\gamma_j^2/n$.) The negative log-likelihood is
$$\sum_{j=1}^m \left(2\log\gamma_j + \frac{nI(j/n)}{2\gamma_j^2}\right).$$
Reparametrizing by $\alpha_j = \log \gamma_j$ (so $\gamma_j$ stays positive automatically) turns this
into
$$\sum_{j=1}^m \left(2\alpha_j + \frac{nI(j/n)}{2}e^{-2\alpha_j}\right).$$
Minimizing this over each $\alpha_j$ separately, with no further constraint, gives
$$\hat\alpha_j = \log\sqrt{\frac{nI(j/n)}{2}}, \qquad \hat\gamma_j^2 = \frac{nI(j/n)}{2}, \qquad \hat f(j/n) = \frac{2\hat\gamma_j^2}{n} = I(j/n).$$
The unregularized estimate of the spectrum is exactly the periodogram — the fit interpolates the
noise instead of smoothing it. This is the formal version of the complaint that opened the chapter:
without some constraint forcing $f$ to be smooth, "fitting the model" does nothing at all.

## Regularized estimation

The fix is to penalize roughness in $\{\alpha_j\}$ directly. A natural roughness measure is the sum
of squared (or absolute) discrete second differences,
$$\sum_{j=2}^{m-1}\big((\alpha_{j+1}-\alpha_j) - (\alpha_j - \alpha_{j-1})\big)^2 \quad \text{or} \quad \sum_{j=2}^{m-1}\big|(\alpha_{j+1}-\alpha_j) - (\alpha_j - \alpha_{j-1})\big|,$$
each penalizing curvature in the sequence $\alpha_j$ — large when consecutive slopes change sharply,
zero when $\alpha_j$ is exactly linear in $j$. Adding either to the negative log-likelihood gives a
ridge and a lasso estimator,
$$\hat\alpha^{\text{ridge}}(\lambda) = \arg\min_\alpha \sum_{j=1}^m \left(2\alpha_j + \frac{nI(j/n)}{2}e^{-2\alpha_j}\right) + \lambda \sum_{j=2}^{m-1}\big((\alpha_{j+1}-\alpha_j)-(\alpha_j-\alpha_{j-1})\big)^2,$$
$$\hat\alpha^{\text{lasso}}(\lambda) = \arg\min_\alpha \sum_{j=1}^m \left(2\alpha_j + \frac{nI(j/n)}{2}e^{-2\alpha_j}\right) + \lambda \sum_{j=2}^{m-1}\big|(\alpha_{j+1}-\alpha_j)-(\alpha_j-\alpha_{j-1})\big|.$$
The tuning parameter $\lambda$ trades off fit to the periodogram against smoothness of $\alpha_j$;
$\lambda = 0$ recovers the interpolating (overfit) estimate above, and larger $\lambda$ pulls the
estimate toward a smooth curve. Once $\hat\alpha_j$ is found, convert back via
$\hat\gamma_j = \exp(\hat\alpha_j)$ and $\hat f(j/n) = 2\hat\gamma_j^2 / n$.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Schematic periodogram scattered around a smooth spectral trend, next to the smooth curve a smoothness penalty recovers">
  <line x1="40" y1="180" x2="310" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="40" y="196" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="300" y="196" text-anchor="middle" font-size="12" fill="currentColor">1/2</text>
  <text x="175" y="212" text-anchor="middle" font-size="12" fill="currentColor">frequency</text>
  <path d="M40,170 Q53,155 66,139 Q79,125 92,111 Q105,100 118,89 Q131,82 144,75 Q157,71 170,70 Q183,71 196,75 Q209,82 222,89 Q235,100 248,111 Q261,125 274,139 Q287,155 300,170" fill="none" stroke="#d97706" stroke-width="2.5"/>
  <polyline points="40,165 66,100 92,150 118,60 144,95 170,45 196,110 222,70 248,140 274,115 300,175" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <g fill="currentColor">
    <circle cx="40" cy="165" r="2.5"/><circle cx="66" cy="100" r="2.5"/><circle cx="92" cy="150" r="2.5"/>
    <circle cx="118" cy="60" r="2.5"/><circle cx="144" cy="95" r="2.5"/><circle cx="170" cy="45" r="2.5"/>
    <circle cx="196" cy="110" r="2.5"/><circle cx="222" cy="70" r="2.5"/><circle cx="248" cy="140" r="2.5"/>
    <circle cx="274" cy="115" r="2.5"/><circle cx="300" cy="175" r="2.5"/>
  </g>
  <text x="90" y="22" text-anchor="middle" font-size="12" fill="currentColor">periodogram</text>
  <text x="250" y="22" text-anchor="middle" font-size="12" fill="#d97706">smoothed estimate</text>
</svg>
<figcaption>Schematic only, not real data: the periodogram (dots, jagged line) is also the
unregularized maximum-likelihood estimate of $f$ — it reproduces every fluctuation. The smoothness
penalty on $\alpha_j = \log\gamma_j$ pulls the estimate toward the orange curve instead.</figcaption>
</figure>

## The case of even $n$

Everything above assumed $n$ odd, $m=(n-1)/2$. If $n$ is even, $1/2$ itself becomes a Fourier
frequency and $b_{n/2}$ is real (since $\sin(\pi t) = 0$ for all $t$). The simplest fix is to set
$m = (n-2)/2$ and work only with
$$\mathrm{Re}(b_j), \mathrm{Im}(b_j) \overset{\text{i.i.d.}}{\sim} N(0,\gamma_j^2), \qquad j=1,\dots,m,$$
leaving everything else unchanged — this amounts to setting $\gamma_{n/2} = 0$, i.e. dropping
frequency $1/2$ entirely. It is possible instead to estimate $\gamma_{n/2}$ from
$b_{n/2} \sim N(0, \gamma_{n/2}^2)$, but this is more involved (it is what was done in Lab 7, which is
not part of these notes).

## Sources

- Fall 2025, Lecture Fifteen (Aditya Guntuboyina, October 16, 2025): motivation for smoothing the
  periodogram, the multiplicative noise model and its $\chi^2_2/2 = \mathrm{Exp}(1)$ derivation, and
  the power spectral density —
  `docs/statistics/berkeley/stat153/fall-2025/LectureFifteen153248Fall2025/01-1-smoothing-the-periodogram.md`;
  the DFT formulation and sufficiency —
  `.../02-3-spectrum-model-from-dft.md`; the sinusoid rewrite and the three equivalent definitions —
  `.../03-4-rewriting-the-model-in-terms-of.md`; the likelihood, overfitting, ridge/lasso
  regularization, and the even-$n$ case — `.../04-5-regularized-estimation.md`.
- Spring 2025, Lecture Fifteen (Aditya Guntuboyina, March 11, 2025), the same lecture slot in an
  earlier offering of the course: used here for the sufficiency remark and for the "what the
  spectral density says about $y_t$" section (variance and autocovariance as integrals of $f$),
  which the fall recording does not include —
  `docs/statistics/berkeley/stat153/spring-2025/LectureFifteen153248Spring2025/01-1-spectrum-model.md`
  and `.../02-3-rewriting-the-model-in-terms-of.md`.
- Both source sets are reconstructed by a model from PDFs with no text layer and carry the note
  "every equation is unverified"; this chapter follows their equations as given, correcting only
  evident transcription slips (a stray $t$ and $n$ in the lasso objective, where every other line in
  the same source indexes by $j$ and $m$).
- Referred to but not contained here: Chapter 4 of Shumway and Stoffer, and Percival and Walden's
  *Spectral Analysis for Univariate Time Series*, for a rigorous definition of the power spectral
  density; Lecture 8 (the inverse DFT formula) and Lecture 13 (the harmonic-regression form of
  $y_t$), as prior material this lecture builds on; Lab 7, for estimating $\gamma_{n/2}$ directly
  rather than setting it to zero.

---

[← 102. Ridge and LASSO Trend Filtering](102-ridge-and-lasso-trend-filtering.md) · [Contents](index.md) · [104. The Posterior t-Distribution in Regression →](104-the-posterior-t-distribution-in-regression.md)
