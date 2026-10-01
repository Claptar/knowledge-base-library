---
title: "21. The James-Stein Estimator"
course: "Berkeley Stat 210A"
chapter: 21
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 21. The James-Stein Estimator

## What this covers

Why is the obvious estimator — just reporting the data — not the best one, once you are estimating
three or more numbers at once? This chapter answers that question by constructing the James-Stein
estimator and proving that it beats the sample mean everywhere, for every value of the unknown
parameter. It assumes the Gaussian sequence model, the normal-prior Bayes estimator for a Gaussian
mean, and the notion of admissibility, all from earlier in the course.

## The Gaussian sequence model

Take $X \sim N_d(\theta, I_d)$: a vector of $d$ independent, unit-variance Gaussian observations,
one for each coordinate of an unknown mean vector $\theta \in \mathbb{R}^d$. The model looks
narrow but is not: if $X_1, \ldots, X_n \overset{\text{iid}}{\sim} N_d(\theta, \sigma^2 I_d)$ for a
*known* $\sigma^2 > 0$, a sufficiency reduction collapses the sample to

$$Z = \frac{1}{\sigma \sqrt n} \sum_i X_i \sim N_d(\mu, I_d), \qquad \mu = \theta \sqrt n / \sigma,$$

which is exactly the vanilla model again. Everything below is stated for the vanilla version; it
transfers to the general one through this reduction.

Throughout, the loss is squared error summed over coordinates,

$$L(\theta, \delta) = \|\delta(X) - \theta\|^2 = \sum_j (\delta_j(X) - \theta_j)^2,$$

and $\operatorname{MSE}(\theta; \delta) = \mathbb{E}_\theta L(\theta, \delta(X))$ is the risk.

The obvious estimator is $\delta_0(X) = X$ itself. It has several independent justifications: it is
the UMVU estimator for $\theta$, it is the objective Bayes estimator (the flat prior coincides with
the Jeffreys prior for any location model), and it is also the MLE. Every route to "the" answer
points at the same estimator — which is exactly what makes it surprising that $X$ turns out to be
beatable.

## Bayes estimators and linear shrinkage

Put an exchangeable Gaussian prior on the mean, $\theta_i \overset{\text{iid}}{\sim} N(0, \tau^2)$.
The resulting Bayes estimator is $\frac{\tau^2}{1+\tau^2} X$: pull $X$ toward $0$ by a factor
depending on how concentrated the prior is.

This suggests a whole family, the **linear shrinkage estimators**

$$\delta_\zeta(X) = (1 - \zeta) X, \qquad \zeta \in [0, 1],$$

where $\zeta$ is the *shrinkage parameter*. Taking $\zeta = 0$ recovers $X$; taking
$\zeta = 1/(1+\tau^2)$ recovers the Bayes estimator for a known $\tau^2$.

If $\tau^2$ itself is uncertain, hierarchical Bayes estimates it from the data, giving

$$\delta(X) = \bigl(1 - \mathbb{E}[\zeta \mid X]\bigr) X = \delta_{\hat\zeta_{\text{Bayes}}(X)}(X):$$

$\zeta$ is estimated from the whole data set and then plugged back in as a data-adaptive tuning
parameter. But a hierarchical Bayes estimate of $\zeta$ is not the only option — an *empirical
Bayes* approach can plug in any reasonable estimator of $\zeta$, Bayesian or not. For $d \geq 3$,
the UMVU estimator of $\zeta$ turns out to be

$$\hat\zeta_{\text{UMVU}}(X) = \frac{d-2}{\|X\|^2},$$

which can be verified from the identity

$$\mathbb{E}[1/Y] = \frac{1}{d-2} \quad \text{for } Y \sim \chi^2_d = \operatorname{Gamma}(d/2, 2),\ d > 2$$

(proved elsewhere in the course; not reproduced here). Substituting $\hat\zeta_{\text{UMVU}}$ into
the linear shrinkage family gives the **James-Stein estimator**,

$$\delta_{\text{JS}}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right) X.$$

It shrinks hardest when $\|X\|^2$ is small — exactly the case in which a fixed-$\zeta$ Bayes
estimator would want $\zeta$ close to $1$.

## The James-Stein paradox

The James-Stein estimator has a Bayesian motivation, but its real content is that it needs none.
For $d \geq 3$, $X$ is **inadmissible** as an estimator of $\theta$ under squared error loss:

$$\operatorname{MSE}(\theta, \delta_{\text{JS}}) < \operatorname{MSE}(\theta, X) \quad \text{for every } \theta \in \mathbb{R}^d.$$

It is unremarkable for a Bayes estimator to beat the UMVU estimator *on average* under some prior —
that is what a prior is for. What is remarkable is that this inequality holds pointwise, for every
fixed $\theta$, with no averaging at all.

There is nothing special about shrinking toward $0$: shrinking toward any fixed $\theta_0$,

$$\tilde\delta(X) = \theta_0 + \left(1 - \frac{d-2}{\|X - \theta_0\|^2}\right)(X - \theta_0),$$

dominates $\delta_0$ by exactly the same argument, applied after the substitution
$Y = X - \theta_0 \sim N_d(\mu, I_d)$ with $\mu = \theta - \theta_0$. Translation invariance of the
Gaussian location model carries the domination result for $\mu$ straight back to a domination
result for $\theta$.

This result was a genuine shock when it appeared in the 1950s. It was treated for a long time as a
curiosity, and only later understood to carry a real message: shrinkage helps, especially in high
dimensions, even with no Bayesian argument behind it at all.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Risk of the James-Stein estimator stays below the risk of X for every value of the norm of theta">
  <line x1="45" y1="180" x2="310" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="45" y1="20" x2="45" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="310" y="197" text-anchor="end" font-size="12" fill="currentColor">$\|\theta\|^2$</text>
  <text x="20" y="26" text-anchor="start" font-size="12" fill="currentColor">MSE</text>
  <line x1="45" y1="55" x2="310" y2="55" stroke="currentColor" stroke-width="1.2" stroke-dasharray="5 4"/>
  <text x="315" y="59" font-size="12" fill="currentColor">$d$ = MSE($\theta$, $X$)</text>
  <path d="M 45 158 C 110 130, 180 90, 310 58" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="140" y="145" font-size="12" fill="currentColor">MSE($\theta$, $\delta_{JS}$)</text>
  <text x="20" y="162" text-anchor="end" font-size="12" fill="currentColor">2</text>
  <line x1="45" y1="158" x2="40" y2="158" stroke="currentColor" stroke-width="1.2"/>
</svg>
<figcaption>The risk of the James-Stein estimator is always strictly below the risk $d$ of $X$: it
equals $2$ at $\theta = 0$, independently of the dimension $d$, and rises back toward $d$ as
$\|\theta\|^2 \to \infty$, but never reaches it.</figcaption>
</figure>

## Where the right amount of shrinkage comes from

Shrinkage can also be motivated with no prior at all, purely by trading bias for variance. For a
single coordinate of $\delta_\zeta(X) = (1-\zeta)X$,

$$\mathbb{E}_\theta[(\theta_i - \delta_i(X))^2] = (\theta_i - (1-\zeta)\theta_i)^2 + (1-\zeta)^2 = (\zeta \theta_i)^2 + (1-\zeta)^2,$$

the usual bias-variance split. Summing over the $d$ coordinates,

$$\operatorname{MSE}(\theta; \delta) = \zeta^2 \|\theta\|^2 + d(1-\zeta)^2,$$

squared bias plus variance. This is quadratic in $\zeta$ with positive curvature, so it is minimized
where its derivative vanishes:

$$0 = 2\zeta\|\theta\|^2 - 2(1-\zeta)d \quad \Longrightarrow \quad \zeta^*(\theta) = \frac{d}{d + \|\theta\|^2} = \frac{1}{1 + \|\theta\|^2/d},$$

which is strikingly close in form to the Bayes-optimal $\zeta = 1/(1+\tau^2)$ from the Gaussian
prior above — the frequentist and Bayesian answers point at the same quantity, $\|\theta\|^2 / d$
playing the role of $\tau^2$.

Two things follow. First, $\zeta^*(\theta) > 0$ always: some shrinkage always helps, whatever
$\theta$ is. Second, the *right amount* of shrinkage depends on the unknown $\|\theta\|^2$: as
$\|\theta\|^2 \to \infty$ the optimal $\zeta$ goes to $0$, so any single fixed $\zeta$ overshoots
for some $\theta$. What is needed is an estimator that gets the shrinkage right *without knowing*
$\|\theta\|^2$ — which is exactly what the James-Stein estimator does, since it estimates $\zeta$
from the data. Making that claim precise needs a general tool for computing the MSE of an estimator
whose tuning parameter is itself a function of the data: Stein's unbiased risk estimator.

## Stein's lemma

**Theorem (Stein's lemma, univariate).** Let $X \sim N(\theta, \sigma^2)$ and let
$h : \mathbb{R} \to \mathbb{R}$ be differentiable with $\mathbb{E}|\dot h(X)| < \infty$. Then

$$\operatorname{Cov}(X, h(X)) = \mathbb{E}[(X - \theta) h(X)] = \sigma^2 \, \mathbb{E}[\dot h(X)].$$

*Sketch.* Take $\theta = 0$, $\sigma^2 = 1$ first. Since $\dot\phi(x) = -x\phi(x)$ for the standard
normal density $\phi$,

$$\mathbb{E}[Xh(X)] = \int x h(x) \phi(x)\, dx = \int \dot h(x) \phi(x)\, dx = \mathbb{E}[\dot h(X)]$$

by integration by parts (made rigorous by first centering $h$ so that $h(0) = 0$ and splitting the
integral at $0$). For general $\theta, \sigma^2$, write $X = \theta + \sigma Z$ with $Z \sim N(0,1)$
and apply the centered result to $k(z) = h(\theta + \sigma z)$:

$$\mathbb{E}[(X-\theta)h(X)] = \sigma \, \mathbb{E}[Z h(\theta + \sigma Z)] = \sigma^2 \, \mathbb{E}[\dot h(\theta + \sigma Z)] = \sigma^2\, \mathbb{E}[\dot h(X)]. \qquad \blacksquare$$

The multivariate version is what the James-Stein calculation actually needs. For
$h : \mathbb{R}^d \to \mathbb{R}^d$ differentiable, write $Dh(x) \in \mathbb{R}^{d\times d}$ for its
Jacobian, $(Dh(x))_{ij} = \partial h_i / \partial x_j (x)$, and $\|A\|_F = (\sum_{ij} A_{ij}^2)^{1/2}$
for the Frobenius norm of a matrix $A$.

**Theorem (Stein's lemma, multivariate).** Let $X \sim N_d(\theta, \sigma^2 I_d)$ and let
$h : \mathbb{R}^d \to \mathbb{R}^d$ be differentiable with $\mathbb{E}\|Dh(X)\|_F < \infty$. Then

$$\mathbb{E}[(X-\theta)^\top h(X)] = \sigma^2\, \mathbb{E}\operatorname{tr}(Dh(X)) = \sigma^2 \sum_i \mathbb{E}\left[\frac{\partial h_i}{\partial x_i}(X)\right].$$

*Proof.* Conditional on the other coordinates $X_{-i}$, $X_i \sim N(\theta_i, \sigma^2)$, so the
univariate lemma applies coordinatewise:

$$\mathbb{E}\bigl[(X_i - \theta_i) h_i(X) \mid X_{-i}\bigr] = \sigma^2\, \mathbb{E}\left[\frac{\partial h_i}{\partial x_i}(X) \,\middle|\, X_{-i}\right].$$

Taking expectations and summing over $i$ gives the claim. $\blacksquare$

## Stein's unbiased risk estimator (SURE)

Apply the multivariate lemma to $h(x) = x - \delta(x)$, for any differentiable estimator $\delta$
whose $h$ satisfies the regularity condition — which covers essentially every estimator of
interest. Using $\|a-b\|^2 = \|a\|^2 + \|b\|^2 - 2a^\top b$ with $a = X - \theta$ and
$b = h(X) = X - \delta(X)$,

$$
\begin{aligned}
\operatorname{MSE}(\theta; \delta)
&= \mathbb{E}_\theta \|\delta(X) - \theta\|^2 = \mathbb{E}_\theta\|(X-\theta) - h(X)\|^2 \\
&= \mathbb{E}_\theta\|X-\theta\|^2 + \mathbb{E}_\theta\|h(X)\|^2 - 2\,\mathbb{E}_\theta[(X-\theta)^\top h(X)] \\
&= \sigma^2 d + \mathbb{E}_\theta\|h(X)\|^2 - 2\sigma^2\, \mathbb{E}_\theta\operatorname{tr}(Dh(X)).
\end{aligned}
$$

Every term on the right except the risk itself is either a known constant or has $X$-measurable
expectation, so — when $\sigma^2$ is known — **Stein's unbiased risk estimator** is

$$\widehat{\operatorname{MSE}}(X) = \sigma^2 d + \|h(X)\|^2 - 2\sigma^2 \operatorname{tr}(Dh(X)),$$

an unbiased estimate of the risk of $\delta$, computable from the single observation $X$ — with no
need to know $\theta$, and no need for $\delta$ to have come from a Bayesian argument at all.

### Worked example: shrinking toward the grand mean

Consider shrinking each coordinate toward the overall average $\overline X = \frac1d \sum_i X_i$,

$$\delta_i^\gamma(X) = (1-\gamma) X_i + \gamma \overline X,$$

a bet that most of the $\theta_i$ are close to $\bar\theta = \frac1d\sum_i \theta_i$. Here
$h(X) = X - \delta^\gamma(X) = \gamma(X - \overline X \mathbf 1_d)$, so
$Dh(X)_{ii} = \gamma(1 - 1/d)$ and $\operatorname{tr}(Dh(X)) = (d-1)\gamma$. SURE gives

$$\widehat{\operatorname{MSE}}^\gamma(X) = \sigma^2 d + \gamma^2 (d-1) V^2 - 2(d-1)\gamma\sigma^2,
\qquad V^2 = \frac{1}{d-1}\sum_i (X_i - \overline X)^2$$

(the $X_i$ need not be i.i.d. here — their means can genuinely differ). This estimator can be used
two ways.

**Take its expectation.** Writing $X_i = \theta_i + Z_i$ with $Z_i \sim N(0,\sigma^2)$,
$\mathbb{E}_\theta V^2 = \beta^2 + \sigma^2$ where $\beta^2 = \frac{1}{d-1}\sum_i (\theta_i - \bar\theta)^2$
is the dispersion of the true means. Substituting gives the actual risk,

$$\operatorname{MSE}^\gamma(\theta) = \sigma^2 + (d-1)(1-\gamma)^2 \sigma^2 + (d-1)\gamma^2 \beta^2,$$

minimized at $\gamma^*(\beta) = \sigma^2/(\beta^2+\sigma^2)$: shrink all the way to the mean if the
$\theta_i$ are truly equal ($\beta^2=0$), shrink hardly at all if they are very spread out relative
to the noise ($\beta^2 \gg \sigma^2$).

**Or minimize SURE directly over $\gamma$**, without ever computing $\operatorname{MSE}^\gamma(\theta)$:

$$\hat\gamma(X) = \operatorname*{argmin}_\gamma \widehat{\operatorname{MSE}}^\gamma(X) = \sigma^2 / V^2,$$

a data-driven stand-in for $\gamma^*(\theta)$, since $V^2$ is unbiased for $\beta^2 + \sigma^2$.
Plugging $\hat\gamma(X)$ back in produces a new adaptive estimator, distinct from $\delta^\gamma$
for any fixed $\gamma$ — the same idea SURE will now be used to analyze for James-Stein.

## The risk of the James-Stein estimator

Apply the same machinery to $\delta_{\text{JS}}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right)X$, with
$\sigma^2 = 1$. Here $h(X) = \frac{d-2}{\|X\|^2} X$, so $\|h(X)\|^2 = (d-2)^2/\|X\|^2$. The quotient
rule gives

$$\frac{\partial}{\partial X_i}\left(\frac{X_i}{\|X\|^2}\right) = \frac{\|X\|^2 - 2X_i^2}{\|X\|^4},$$

and summing over coordinates,

$$\operatorname{tr}(Dh(X)) = (d-2) \cdot \frac{d\|X\|^2 - 2\|X\|^2}{\|X\|^4} = \frac{(d-2)^2}{\|X\|^2}.$$

Substituting into $\widehat{\operatorname{MSE}}(X) = d + \|h(X)\|^2 - 2\operatorname{tr}(Dh(X))$ gives

$$\widehat{\operatorname{MSE}}(X) = d + \frac{(d-2)^2}{\|X\|^2} - 2\frac{(d-2)^2}{\|X\|^2} = d - \frac{(d-2)^2}{\|X\|^2},$$

and taking expectations,

$$\operatorname{MSE}(\theta; \delta_{\text{JS}}) = d - (d-2)^2\, \mathbb{E}_\theta\left[\frac{1}{\|X\|^2}\right],$$

which is strictly less than $d$ — the risk of $\delta_0$ — for every $\theta$, since $\|X\|^2 > 0$
almost surely. This is the James-Stein paradox proved directly, by computing both risks rather than
appealing to a Bayesian argument.

Two special cases show the shape of the improvement. At $\theta = 0$, $\|X\|^2 \sim \chi^2_d$, and
the identity from earlier gives

$$\operatorname{MSE}(0; \delta_{\text{JS}}) = d - (d-2)^2 \cdot \frac{1}{d-2} = 2:$$

even though $d$ parameters are being estimated, the total MSE at the origin does not grow with $d$
at all — because the estimator shrinks harder and harder toward $0$ as $d$ grows. At the other
extreme, as $\|\theta\|^2 \to \infty$, $\mathbb{E}_\theta\|X\|^2 \to \infty$ too, and the improvement
term $(d-2)^2/\mathbb{E}_\theta\|X\|^2$ is driven to $0$: far from the origin, James-Stein is no
better than $X$, but it is never worse. This is exactly the risk curve drawn above.

For general known $\sigma^2$, the James-Stein estimator is $\left(1 - \frac{(d-2)\sigma^2}{\|X\|^2}\right)X$,
and the same computation gives $\widehat{\operatorname{MSE}}(X) = \sigma^2 d - \sigma^4(d-2)^2/\|X\|^2$
and $\operatorname{MSE}(0; \delta_{\text{JS}}) = 2\sigma^2$.

## Final remarks

The James-Stein estimator itself is inadmissible: $\zeta = (d-2)/\|X\|^2$ can exceed $1$, at which
point $\delta_{\text{JS}}$ overshoots past $0$ and flips the sign of a coordinate — never a good
idea, since shrinking to exactly $0$ instead can only help. The **positive-part** estimator

$$\delta_+(X) = \left(1 - \frac{d-2}{\|X\|^2}\right)_+ X$$

is strictly better. A version more useful in practice shrinks toward the grand mean rather than the
origin,

$$\delta_{\text{JS}+,i}(X) = \overline X + \left(1 - \frac{d-3}{V^2}\right)_+ (X_i - \overline X),$$

which dominates $\delta_0 = X$ for $d \geq 4$.

Taken to its logical extreme, the paradox has a genuinely strange consequence: should every
scientist at a university, working on completely unrelated problems, pool their estimates into one
big James-Stein shrinkage, purely because each of them happens to be estimating a Gaussian location
parameter? The *overall* MSE, summed across everyone's estimates, really would improve. The escape
is that overall improvement can come at the cost of individual coordinates: if $\theta_1 = 10$ while
$\theta_2 = \cdots = \theta_{1000} = 0$, the pooled estimator will over-shrink $\theta_1$ toward $0$
in order to do well on the other 999 coordinates. Anyone confident their own parameter is unusually
large has no reason to want to join such a scheme, even though the group as a whole benefits from
it.

## Sources

- All material is from the course reader chapter "The James-Stein Estimator" (author Will Fithian),
  split across three consecutive pages: *Gaussian sequence model*, *Stein's Unbiased Risk
  Estimator*, and *Risk of the James-Stein estimator*. The fall-2024 markdown conversion was used as
  the primary text (`reader/jamesstein.qmd`, lossless route); the fall-2025 and fall-2026
  conversions of the same reader chapter were checked and contain the same content, differing only
  in formatting.
- Two results are cited by the reader but not proved in it, and are not reproduced here either: the
  identity $\mathbb{E}[1/Y] = 1/(d-2)$ for $Y \sim \chi^2_d$, and a more careful version of the
  Stein's-lemma integration-by-parts argument — both attributed to accompanying "handwritten notes"
  not included in the supplied material. One of the later reader versions instead attributes the
  $\chi^2_d$ identity to "Lecture 10" of the course, which was likewise not supplied.

---

[← 20. Statistics as Inductive Reasoning](20-statistics-as-inductive-reasoning.md) · [Contents](index.md) · [22. Reader Notation Conventions →](22-reader-notation-conventions.md)
