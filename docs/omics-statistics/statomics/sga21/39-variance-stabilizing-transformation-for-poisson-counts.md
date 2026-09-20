---
title: "39. Variance-Stabilizing Transformation for Poisson Counts"
course: "StatOmics Sga21"
chapter: 39
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 39. Variance-Stabilizing Transformation for Poisson Counts

## What this covers

This chapter answers a narrow but recurring question in the analysis of count data such as
single-cell RNA-seq read counts: if a count $Y$ is modelled as Poisson-distributed, its variance
is tied to its mean, so any statistic built directly from raw counts is noisier wherever the
counts happen to be larger. What transformation of $Y$ removes that dependence, so that the
transformed variable has (approximately) the same variance everywhere? It assumes familiarity
with the Poisson distribution and with a first-order Taylor expansion of a function of a random
variable (the delta method).

## Why raw counts are heteroscedastic

For $Y \sim Poi(\mu)$, $E(Y) = Var(Y) = \mu$: the variance is pinned to the mean by the
distribution itself. That is a problem for any method that treats the noise around every
observation as comparable in size — clustering, PCA, or a variance-based test all implicitly
assume the spread of the noise doesn't itself depend on the signal. With Poisson counts it does: a
gene or cell with a large mean count carries proportionally more variance than one with a small
mean, so the large-mean observations dominate any distance- or variance-based summary of the data
purely because they are large, not because they are more informative.

A **variance stabilizing transformation (VST)** is a function $f$ chosen so that $Var(f(Y))$ is
(approximately) a constant $c$, independent of $\mu$. After applying it, the transformed data can
be treated as roughly homoscedastic.

## Deriving the transform: the delta method

The derivation uses only a first-order Taylor expansion of $f$ around the mean $\mu$:

$$f(Y) \approx f(\mu) + (Y-\mu) f'(\mu).$$

Rearranging and squaring,

$$\{f(Y) - f(\mu)\}^2 = (Y-\mu)^2 f'(\mu)^2,$$

and taking expectations turns the left-hand side into $Var(f(Y))$ and $(Y-\mu)^2$ into $Var(Y)$,
so

$$Var(f(Y)) = Var(Y)\, f'(\mu)^2 = \mu\, f'(\mu)^2,$$

using $Var(Y) = \mu$ for the Poisson. This is the point of the whole calculation: $Var(f(Y))$
depends on $\mu$ both through the $\mu$ that appears explicitly and through $f'(\mu)^2$, and the
transform is stabilizing exactly when those two dependencies cancel.

They cancel when

$$f'(\mu)^2 = \frac{1}{\mu} \quad\Longleftrightarrow\quad f'(\mu) = \mu^{-1/2},$$

because then $Var(f(Y)) = \mu \cdot \mu^{-1} = 1$ for every $\mu$. Integrating,

$$f(\mu) = \int \mu^{-1/2}\, d\mu = 2\mu^{1/2},$$

so $f(Y) = 2\sqrt{Y}$ stabilizes the variance at exactly $1$. Dropping the factor of $2$ — as is
more commonly written in the literature — the plain square-root transform $f(Y) = \sqrt{Y}$
stabilizes the variance at $1/4$ instead. Either version carries the same content: **the square
root of a Poisson count has a variance that no longer depends on the mean.**

## How good is the approximation?

Everything above rests on the first-order Taylor expansion being accurate, and that approximation
is better the larger $\mu$ is: for a Poisson with a small mean, the distribution is concentrated
on a handful of small integers and is far from smooth, so the linear approximation to $f$ around
$\mu$ is comparatively poor. The transform should therefore stabilize the variance more
successfully for counts with a large mean than for counts near zero.

This was checked by simulation: for many different values of $\mu$ drawn uniformly between $1$
and $500$, a sample of $500$ Poisson($\mu$) draws was generated, and both the raw sample variance
and the sample variance of $\sqrt{Y}$ were recorded against the sample mean.

<figure>
<svg viewBox="0 0 460 240" role="img" aria-label="Scatter of variance against mean before and after the square-root transform">
  <text x="115" y="14" text-anchor="middle" font-size="12" fill="currentColor">raw counts Y</text>
  <text x="340" y="14" text-anchor="middle" font-size="12" fill="currentColor">after &#8730;Y</text>

  <line x1="40" y1="200" x2="200" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="200" x2="40" y2="20" stroke="currentColor" stroke-width="1.2"/>
  <text x="120" y="222" text-anchor="middle" font-size="11" fill="currentColor">mean μ</text>
  <text x="18" y="115" text-anchor="middle" font-size="11" fill="currentColor" transform="rotate(-90 18 115)">variance</text>
  <line x1="40" y1="200" x2="190" y2="50" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/>

  <circle cx="70" cy="168" r="2.6" fill="currentColor"/>
  <circle cx="70" cy="173" r="2.6" fill="currentColor"/>
  <circle cx="95" cy="138" r="2.6" fill="currentColor"/>
  <circle cx="95" cy="151" r="2.6" fill="currentColor"/>
  <circle cx="120" cy="110" r="2.6" fill="currentColor"/>
  <circle cx="120" cy="131" r="2.6" fill="currentColor"/>
  <circle cx="145" cy="82" r="2.6" fill="currentColor"/>
  <circle cx="145" cy="108" r="2.6" fill="currentColor"/>
  <circle cx="170" cy="52" r="2.6" fill="currentColor"/>
  <circle cx="170" cy="86" r="2.6" fill="currentColor"/>
  <circle cx="185" cy="34" r="2.6" fill="currentColor"/>
  <circle cx="185" cy="74" r="2.6" fill="currentColor"/>

  <line x1="260" y1="200" x2="420" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <line x1="260" y1="200" x2="260" y2="20" stroke="currentColor" stroke-width="1.2"/>
  <text x="340" y="222" text-anchor="middle" font-size="11" fill="currentColor">mean μ</text>
  <text x="238" y="115" text-anchor="middle" font-size="11" fill="currentColor" transform="rotate(-90 238 115)">variance</text>
  <line x1="260" y1="140" x2="420" y2="140" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/>

  <circle cx="280" cy="146" r="2.6" fill="currentColor"/>
  <circle cx="300" cy="135" r="2.6" fill="currentColor"/>
  <circle cx="320" cy="145" r="2.6" fill="currentColor"/>
  <circle cx="340" cy="133" r="2.6" fill="currentColor"/>
  <circle cx="360" cy="147" r="2.6" fill="currentColor"/>
  <circle cx="380" cy="136" r="2.6" fill="currentColor"/>
  <circle cx="400" cy="144" r="2.6" fill="currentColor"/>
</svg>
<figcaption>Schematic of the simulation's qualitative shape: the variance of the raw counts fans out as the mean grows, while the variance of the square-root-transformed counts stays in a narrow band across the whole range of means.</figcaption>
</figure>

The right-hand pattern is what "variance stabilized" looks like: no visible trend with $\mu$,
just scatter of roughly constant width. The left-hand pattern is the untransformed variance
widening as the mean grows.

## Why does the raw-variance plot fan out?

The fan in the raw plot is *not* simply the Poisson identity $Var(Y) = \mu$ drawn as a scatter —
both axes are themselves estimated from a finite sample of $500$ draws, so both carry sampling
noise. The spread of the sample-mean estimate around its own true value is

$$Var(\hat\mu) = \frac{\mu}{n},$$

and since every simulated dataset used the same $n$, this is $Var(\hat\mu) = c\mu$ for a fixed
constant $c$: **the variance of the mean estimate itself grows with the mean being estimated.**
The same is true, more strongly, of the sample variance. That is why the cloud of points widens as
$\mu$ grows even though the underlying relationship $Var(Y) = \mu$ is a single deterministic line
— the estimates of both the mean and the variance become noisier together as $\mu$ increases.

## Sources

- `docs/omics-statistics/statomics/sga21/singleCell_varStabilization.md` — converted from
  `singleCell_varStabilization.Rmd` (statOmics SGA21 course, CC BY-NC-SA 4.0), the sole input
  supplied for this chapter. It supplied the definition of a variance stabilizing transformation,
  the delta-method derivation of $f(Y) = 2\sqrt{Y}$ (equivalently $\sqrt{Y}$), the simulation
  design (Poisson($\mu$) with $\mu \sim \text{Uniform}(1,500)$, $n = 500$ per draw, $N = 1000$
  replicates comparing raw and square-root-transformed variance), and the closing
  question-and-answer on why the raw-variance plot fans out. No slide deck, transcript, or
  separate exercise set was supplied for this chapter.

---

[← 38. Single-Cell QC and Dimensionality Reduction](38-single-cell-qc-and-dimensionality-reduction.md) · [Contents](index.md) · [40. Proteomics Software Setup →](40-proteomics-software-setup.md)
