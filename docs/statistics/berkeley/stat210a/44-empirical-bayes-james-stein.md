---
title: "44. Empirical Bayes, James-Stein"
course: "Berkeley Stat 210A Fall 2024"
chapter: 44
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 44. Empirical Bayes, James-Stein

## What this covers

Why is the sample mean — UMVU, the MLE, minimax, and the Bayes rule under a flat prior — not the
best way to estimate a $d$-dimensional Gaussian mean once $d \ge 3$? This chapter builds the
Gaussian sequence model, motivates linear shrinkage as an empirical-Bayes device, states the
James-Stein result that shocked the field in 1956, and develops the two tools (Stein's lemma and
its unbiased risk estimator, SURE) needed to actually compute the risk of a shrinkage rule and see
why it beats the mean everywhere. It assumes comfort with the multivariate normal, sufficiency,
UMVU estimation, and basic decision-theoretic risk (bias-variance decomposition of MSE).

## The Gaussian sequence model

Take

$$X \sim N_d(\theta, I_d),$$

and the goal is to estimate $\theta \in \mathbb{R}^d$ by some $\delta(X)$, with small

$$\mathrm{MSE}(\theta;\delta) = \mathbb{E}_\theta \|\theta - \delta(X)\|^2.$$

The model is more general than it looks. If $X_1,\dots,X_n \overset{iid}{\sim}(\theta,\sigma^2 I_d)$
then the (scaled) sample mean

$$Z = \frac{1}{\sigma\sqrt n}\sum_{k=1}^n X_k$$

is approximately $N_d(\theta\sqrt n/\sigma, I_d)$, so any $n$-sample, $\sigma^2$-known problem
reduces to this one after rescaling. Sufficiency lets us take $n = 1$ throughout without loss.

The obvious estimator $\delta_0(X) = X$ has a great deal going for it: it is UMVU, it is the MLE,
and it is the objective-Bayes estimator under a flat (or Jeffreys) prior. The question the rest of
the chapter answers is whether anything can do better — and, remarkably, for $d\ge 3$ something
always does.

## Linear shrinkage and empirical Bayes

Consider instead the family of **linear shrinkage estimators**

$$\delta_\zeta(X) = (1-\zeta)X, \qquad \zeta \in [0,1].$$

These arise naturally from a Bayesian hierarchy on $\theta$, and the amount of information
available at each level of the hierarchy is what makes each stage plausible or not:

- **Simple Bayes.** If $\theta_i \overset{iid}{\sim} N(0,\tau^2)$ with $\tau^2$ *known*, the
  posterior mean is $\delta_\zeta(X)$ with $\zeta = 1/(1+\tau^2)$.
- **Hierarchical Bayes.** Put a prior $\tau^2 \sim \lambda_0$ on the unknown variance itself. Now
  the Bayes rule uses $\zeta = \mathbb{E}[1/(1+\tau^2) \mid X] = \hat\zeta_{\mathrm{Bayes}}(X)$ — a
  single number, drawn once, is hard to justify a prior for; but with many independent draws
  $\theta_i$ there is enough replication to check whether $\tau^2$'s prior even matters, and enough
  data on the $\theta_i$'s that the prior over $\zeta$ starts to wash out.
- **Empirical Bayes.** Skip the prior on $\tau^2$ altogether: estimate $\tau^2$ (equivalently
  $\zeta$) directly from the data and plug the estimate in as though it were known. This is the
  hybrid approach used below.

Marginally, $X_i \mid \tau^2 \overset{iid}{\sim} N(0, 1+\tau^2)$, so $\|X\|^2$ is sufficient for
$\tau^2$ and

$$\|X\|^2 \sim (1+\tau^2)\chi_d^2.$$

Two natural estimators of $\zeta = 1/(1+\tau^2)$ follow:

$$\hat\zeta_{\mathrm{MLE}}(X) = \frac{d}{\|X\|^2}, \qquad \hat\zeta_{\mathrm{UMVU}}(X) = \frac{d-2}{\|X\|^2}.$$

The UMVU version needs the following fact about the reciprocal of a chi-squared variable.

**Lemma.** If $Y \sim \chi_d^2$ with $d \ge 3$, then $\mathbb{E}[1/Y] = 1/(d-2)$.

*Proof.* Write out the expectation against the $\chi_d^2$ density and pull two powers of $y$ into
the normalizing constant:

$$\mathbb{E}\left[\frac1Y\right] = \int_0^\infty \frac1y\,\frac{1}{2^{d/2}\Gamma(d/2)}\,y^{d/2-1}e^{-y/2}\,dy
= \frac{2^{(d-2)/2}\Gamma\!\left(\frac{d-2}2\right)}{2^{d/2}\Gamma\!\left(\frac d2\right)}
\int_0^\infty \underbrace{\frac{1}{2^{(d-2)/2}\Gamma\!\left(\frac{d-2}2\right)}\,y^{(d-2)/2-1}e^{-y/2}}_{\chi^2_{d-2}\text{ density}}\,dy.$$

The integral is $1$ because the integrand is exactly the $\chi^2_{d-2}$ density. Using
$\Gamma(x) = (x-1)\Gamma(x-1)$ with $x = d/2$, i.e. $\Gamma(d/2) = \frac{d-2}2\,\Gamma\!\left(\frac{d-2}2\right)$,
the prefactor collapses to

$$\mathbb{E}\left[\frac1Y\right] = \frac12 \cdot \frac{\Gamma((d-2)/2)}{\Gamma(d/2)} = \frac12\cdot\frac1{(d-2)/2} = \frac1{d-2}. \qquad \blacksquare$$

Since $\zeta\|X\|^2 \sim \chi_d^2$, the lemma gives $\zeta^{-1}\,\mathbb{E}_\zeta[1/\|X\|^2] = 1/(d-2)$,
so $\hat\zeta_{\mathrm{UMVU}}(X) = (d-2)/\|X\|^2$ is exactly unbiased for $\zeta$.

## The James-Stein estimator and the paradox

James and Stein proposed plugging the UMVU shrinkage factor into $\delta_\zeta$ (for $d\ge 3$):

$$\delta_{\mathrm{JS}}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right)X.$$

That is a natural empirical-Bayes move if you believe the hierarchical model above. What is
shocking is that the same estimator is *good even if you don't*. Drop the Bayesian scaffolding
entirely and go back to the plain, frequentist Gaussian sequence model:

$$X_i \overset{iid}{\sim} N_d(\theta,\sigma^2 I_d), \qquad \theta \in \mathbb{R}^d \text{ fixed, } \sigma^2 \text{ known}, \quad i=1,\dots,n.$$

James and Stein's 1956 result: for $d\ge 3$, the sample mean $\bar X$ is **inadmissible** as an
estimator of $\theta$ under squared-error loss. Concretely, with

$$\delta_{\mathrm{JS}}(\bar X) = \left(1 - \frac{(d-2)\sigma^2/n}{\|\bar X\|^2}\right)\bar X,$$

$$\mathrm{MSE}(\theta,\delta_{\mathrm{JS}}) < \mathrm{MSE}(\theta,\bar X) \qquad \text{for every } \theta \in \mathbb{R}^d.$$

This is worth sitting with, because $\bar X$ is UMVU, minimax, and the objective-Bayes rule — every
classical criterion points at it — and yet it is strictly beaten *everywhere*. By sufficiency it is
enough to prove the $n=1$ statement, $(1-(d-2)/\|X\|^2)X$, which is the form used from here on.

Two features sharpen how strange this is. First, the inequality holds with **no** assumption that
$\theta$ was itself drawn from any prior: it is true even for an implausible fixed value like
$\theta = (500,-10^{10},4)$. Second, there is nothing special about shrinking toward $0$ — for any
fixed $\theta_0 \in \mathbb{R}^d$,

$$\delta(X) = \theta_0 + \left(1 - \frac{d-2}{\|X-\theta_0\|^2}\right)(X-\theta_0)$$

also dominates $X$. The deep implication is that shrinkage is not merely a Bayesian convenience —
it is a genuine frequentist improvement, for a reason that has nothing to do with believing a prior
on $\theta$.

## Choosing the shrinkage factor without a Bayesian model

To see where the right amount of shrinkage comes from, go back to the family $\delta_\zeta(X) =
(1-\zeta)X$ and compute its risk directly, without invoking any prior on $\theta$:

$$R(\theta;\delta_\zeta) = \|\theta - \mathbb{E}\delta_\zeta(X)\|^2 + \sum_i \mathrm{Var}\big((1-\zeta)X_i\big)
= \underbrace{\zeta^2\|\theta\|^2}_{\text{bias}^2} + \underbrace{d(1-\zeta)^2}_{\text{variance}}.$$

Setting the derivative in $\zeta$ to zero,

$$\frac{d}{d\zeta}R(\theta;\delta_\zeta) = 2\zeta\|\theta\|^2 - 2(1-\zeta)d = 0
\quad\implies\quad \zeta^*(\theta) = \frac{d}{d+\|\theta\|^2} = \frac{1}{1+\|\theta\|^2/d}.$$

The optimal shrinkage factor $\zeta^*(\theta)$ is always strictly positive — shrinking always helps
in principle — but it decays to $0$ as $\|\theta\|\to\infty$: a genuinely large signal should barely
be shrunk. Of course $\zeta^*$ depends on the unknown $\theta$, so the real question is what happens
if we plug in an estimate $\hat\zeta^*(X)$ instead — does the resulting estimator still beat $X$?
Answering that requires a way to compute (or estimate) the risk of an estimator that is a
complicated function of $X$, which is exactly what Stein's lemma supplies.

## Stein's lemma

**Theorem (Stein's lemma, univariate).** Let $X \sim N(\theta,\sigma^2)$ and let $h:\mathbb{R}\to\mathbb{R}$
be differentiable with $\mathbb{E}|h'(X)| < \infty$. Then

$$\mathbb{E}[(X-\theta)h(X)] = \sigma^2\,\mathbb{E}[h'(X)].$$

The left side is $\mathrm{Cov}(X,h(X))$, so the lemma says this covariance is controlled entirely by
the *average slope* of $h$ — no integration by parts against $h$ itself is needed, only against its
derivative.

*Proof.* We may assume $h(0)=0$ without loss of generality (replacing $h$ by $h - h(0)$ changes
neither side of the identity). First take $\theta=0,\sigma^2=1$, and split the expectation at $0$:

$$\mathbb{E}[Xh(X)] = \int_0^\infty xh(x)\phi(x)\,dx + \int_{-\infty}^0 xh(x)\phi(x)\,dx.$$

Write $h(x) = \int_0^x h'(y)\,dy$ on the positive half-line and swap the order of integration:

$$\int_0^\infty xh(x)\phi(x)\,dx = \int_0^\infty x\left[\int_0^x h'(y)\,dy\right]\phi(x)\,dx
= \int_0^\infty h'(y)\left[\int_y^\infty x\phi(x)\,dx\right]dy = \int_0^\infty h'(y)\phi(y)\,dy,$$

using $\phi'(x) = -x\phi(x)$ to evaluate the inner integral: $\int_y^\infty x\phi(x)\,dx = \phi(y)$.
A symmetric argument gives $\int_{-\infty}^0 xh(x)\phi(x)\,dx = \int_{-\infty}^0 h'(x)\phi(x)\,dx$, so
summing the two halves proves the case $\theta=0,\sigma^2=1$.

For general $\theta,\sigma^2$, write $X = \theta+\sigma Z$ with $Z\sim N(0,1)$:

$$\mathbb{E}[(X-\theta)h(X)] = \sigma\,\mathbb{E}[Zh(\theta+\sigma Z)] = \sigma^2\,\mathbb{E}[h'(\theta+\sigma Z)] = \sigma^2\,\mathbb{E}[h'(X)],$$

where the middle equality is the $\theta=0,\sigma^2=1$ case applied to $z\mapsto h(\theta+\sigma z)$. $\blacksquare$

**Multivariate version.** For $h:\mathbb{R}^d\to\mathbb{R}^d$ differentiable, let $Dh(x)$ be the
Jacobian, $(Dh(x))_{ij} = \partial h_i/\partial x_j(x)$, and let $\|A\|_F = (\sum_{i,j}A_{ij}^2)^{1/2}$
be the Frobenius norm.

**Theorem.** If $X \sim N_d(\theta,\sigma^2 I_d)$ and $\mathbb{E}\|Dh(X)\|_F < \infty$, then

$$\mathbb{E}[(X-\theta)^\top h(X)] = \sigma^2\,\mathbb{E}\,\mathrm{tr}\big(Dh(X)\big) = \sigma^2\sum_i \mathbb{E}\frac{\partial h_i}{\partial x_i}(X).$$

*Proof.* Condition on all coordinates but the $i$-th. Because the coordinates of $X$ are
independent, $X_i \mid X_{-i} \sim N(\theta_i,\sigma^2)$, and applying the univariate lemma to the
function $x_i \mapsto h_i(x_i, X_{-i})$ conditionally on $X_{-i}$ gives

$$\mathbb{E}[(X_i-\theta_i)h_i(X)] = \mathbb{E}\Big[\mathbb{E}\big[(X_i-\theta_i)h_i(X)\mid X_{-i}\big]\Big]
= \mathbb{E}\Big[\mathbb{E}\Big[\sigma^2\frac{\partial h_i}{\partial x_i}(X)\ \Big|\ X_{-i}\Big]\Big]
= \sigma^2\,\mathbb{E}\frac{\partial h_i}{\partial x_i}(X).$$

Summing over $i$ gives the claim, since $(X-\theta)^\top h(X) = \sum_i (X_i-\theta_i)h_i(X)$. $\blacksquare$

## Stein's unbiased risk estimator (SURE)

The multivariate lemma turns into a tool for computing — or *estimating* — the MSE of an arbitrary
estimator $\delta(X)$, by writing $\delta(X) = X - h(X)$ for $h(X) := X-\delta(X)$. Take $\sigma^2=1$:

$$R(\theta;\delta) = \mathbb{E}_\theta\|X-\theta-h(X)\|^2
= \mathbb{E}_\theta\|X-\theta\|^2 + \mathbb{E}_\theta\|h(X)\|^2 - 2\,\mathbb{E}_\theta[(X-\theta)^\top h(X)]
= d + \mathbb{E}_\theta\|h(X)\|^2 - 2\,\mathbb{E}_\theta\,\mathrm{tr}\big(Dh(X)\big).$$

Every term on the right except $R(\theta;\delta)$ itself is now something we can compute *from the
data alone* — no unknown $\theta$ appears inside the expectation being taken. That means

$$\hat R(X) = d + \|h(X)\|^2 - 2\,\mathrm{tr}\big(Dh(X)\big)$$

is an **unbiased estimator of the risk**: $\mathbb{E}_\theta[\hat R(X)] = R(\theta;\delta)$ for every
$\theta$. It also gives a route to computing the risk exactly, via $R(\theta;\delta) = \mathbb{E}_\theta[\hat R(X)]$,
which is how the James-Stein risk is derived below.

Two immediate checks:

- $\delta(X) = X \implies h\equiv 0,\ Dh\equiv 0 \implies \hat R = d$, recovering the (correct,
  constant) risk of the sample mean.
- $\delta_\zeta(X) = (1-\zeta)X$ for a *fixed* $\zeta \implies h(X)=\zeta X,\ Dh = \zeta I_d
  \implies \hat R = d + \zeta^2\|X\|^2 - 2\zeta d = (1-2\zeta)d + \zeta^2\|X\|^2$.

## The risk of the James-Stein estimator

Now apply SURE to $\delta_{\mathrm{JS}}(X) = \big(1-\tfrac{d-2}{\|X\|^2}\big)X$, so
$h(X) = \tfrac{d-2}{\|X\|^2}X$. Then:

$$\|h(X)\|^2 = \frac{(d-2)^2}{\|X\|^4}\|X\|^2 = \frac{(d-2)^2}{\|X\|^2}.$$

For the trace term, differentiate $h_i(X) = (d-2)X_i/\|X\|^2$ coordinatewise:

$$\frac{\partial h_i}{\partial x_i}(X) = (d-2)\,\frac{\|X\|^2 - 2X_i^2}{\|X\|^4}
\quad\implies\quad
\mathrm{tr}\big(Dh(X)\big) = \sum_i \frac{\partial h_i}{\partial x_i}(X) = (d-2)\frac{d\|X\|^2 - 2\|X\|^2}{\|X\|^4} = \frac{(d-2)^2}{\|X\|^2}.$$

The two correction terms are equal, so

$$\hat R(X) = d + \frac{(d-2)^2}{\|X\|^2} - 2\frac{(d-2)^2}{\|X\|^2} = d - \frac{(d-2)^2}{\|X\|^2},$$

and taking expectations,

$$R(\theta;\delta_{\mathrm{JS}}) = d - (d-2)^2\,\mathbb{E}_\theta\left[\frac{1}{\|X\|^2}\right] < d = R(\theta;X)$$

for every $\theta$, since $\mathbb{E}_\theta[1/\|X\|^2] > 0$. This is the paradox made explicit: a
single closed-form inequality, valid at every $\theta \in \mathbb{R}^d$, with no averaging over a
prior anywhere in the argument.

The two extremes make the shape of the gain concrete. At $\theta = 0$, $\|X\|^2 \sim \chi_d^2$, so
the earlier lemma gives $\mathbb{E}[1/\|X\|^2] = 1/(d-2)$ and

$$R(0;\delta_{\mathrm{JS}}) = d - (d-2) = 2,$$

which can be far smaller than $d$ once $d$ is large. As $\|\theta\|\to\infty$,
$\mathbb{E}_\theta[1/\|X\|^2] \approx 1/\|\theta\|^2 \to 0$, so

$$R(\theta;\delta_{\mathrm{JS}}) \approx d - \frac{(d-2)^2}{\|\theta\|^2} \to d.$$

The advantage over $X$ shrinks toward nothing for a very large $\theta$ — but never disappears; the
estimator is *always* strictly better, just by a vanishing margin far from the origin.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Risk of the James-Stein estimator versus the sample mean, as a function of the norm of theta">
  <line x1="40" y1="20" x2="40" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="55" x2="300" y2="55" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <text x="18" y="59" font-size="12" fill="currentColor">d</text>
  <text x="215" y="46" font-size="12" fill="currentColor">risk of X</text>
  <path d="M 40 175 C 120 150, 210 90, 300 61" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="40" cy="175" r="2.5" fill="currentColor"/>
  <text x="46" y="172" font-size="12" fill="currentColor">2 (at &#8722;theta = 0)</text>
  <text x="150" y="120" font-size="12" fill="currentColor">risk of JS</text>
  <text x="278" y="208" font-size="12" fill="currentColor">||&#952;||</text>
  <text x="10" y="30" font-size="12" fill="currentColor">risk</text>
</svg>
<figcaption>The risk of the James-Stein estimator as a function of ‖θ‖: about 2 near the origin,
always strictly below the constant risk d of X, and approaching d as ‖θ‖ grows.</figcaption>
</figure>

A few further remarks the lecture drew out:

- $\delta_{\mathrm{JS}}$ is *itself* inadmissible. The positive-part version
  $\delta_{\mathrm{JS}+}(X) = \big(1-\tfrac{d-2}{\|X\|^2}\big)_+X$, which floors the shrinkage
  factor at zero instead of letting it flip the sign of a coordinate when $\|X\|^2 < d-2$, is
  strictly better still.
- A practically more useful version shrinks toward the **grand mean** rather than the origin:
  $$\delta_{\mathrm{JS},\bar x}(X) = \bar X\mathbf 1_d + \left(1-\frac{d-3}{\|X-\bar X\mathbf 1_d\|^2}\right)(X-\bar X\mathbf 1_d),$$
  which dominates $X$ once $d\ge 4$ (one degree of freedom is spent estimating the grand mean, so
  the constant in the numerator drops from $d-2$ to $d-3$).
- Taken to its logical extreme the idea sounds absurd: should every unrelated quantity anyone at
  Berkeley happens to be estimating be pooled into one big vector and shrunk together, purely
  because doing so lowers total squared error? The catch is exactly that qualifier: shrinkage
  provably improves $\mathbb{E}\|\hat\theta-\theta\|^2$, the *sum* of squared errors across
  coordinates, but the risk of an individual coordinate, $\mathbb{E}(X_i-\theta_i)^2$, can get
  *worse*. Pooling unrelated problems is a real mathematical gain in aggregate and not necessarily
  a sensible thing to do coordinate by coordinate.

## Sources

- **Setup, linear shrinkage, empirical Bayes, the $\mathbb{E}[1/Y]$ lemma, the James-Stein paradox,
  and the risk-optimal $\zeta^*(\theta)$ computation**: handwritten lecture notes, `lecture12-jamesstein`,
  Berkeley STAT 210A. Cross-checked across three near-identical deliveries of the same lecture —
  fall-2024 (`01-empirical-bayes-james-stein.md`, `02-empirical-bayes.md`, and the independent
  second scan `lecture12-jamesstein Copy/01-empirical-bayes.md`), fall-2025
  (`01-linear-shrinkage-estimator.md`), and fall-2026 (`01-linear-shrinkage-estimator.md`) — which
  agree line for line; only the fall-2024 "Copy" scan and the earliest fall-2024 file carry the
  proof of the $\mathbb{E}[1/Y]=1/(d-2)$ lemma in full.
- **Stein's lemma (univariate and multivariate) and the SURE derivation**: `02-stein-s-lemma.md`
  in each of the same three deliveries (fall-2024 `lecture12-jamesstein Copy/`, fall-2025, and
  fall-2026); the fall-2025 and fall-2026 copies cut off mid-derivation of SURE, so the completed
  argument is taken from the fall-2024 `lecture12-jamesstein Copy/02-stein-s-lemma.md` version.
- **The full risk computation for the James-Stein estimator, the positive-part and grand-mean
  refinements, and the pooling remark**: `lecture12-jamesstein Copy/03-risk-of-james-stein.md`
  (fall-2024) — this section does not appear in the fall-2025 or fall-2026 files supplied.
- All of the above are model reconstructions of handwritten PDF pages with no extracted text
  layer; the source markdown flags every equation as unverified against the original scan. No
  slide deck or spoken transcript was supplied for this lecture, and no problem set was supplied,
  so there is no exercises section here.

---

[← 43. Minimax Estimation (part 1)](43-minimax-estimation-part-1.md) · [Contents](index.md) · [45. Minimax Estimation (part 2) →](45-minimax-estimation-part-2.md)
