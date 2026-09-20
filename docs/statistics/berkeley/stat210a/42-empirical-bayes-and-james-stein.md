---
title: "42. Empirical Bayes and James-Stein"
course: "Berkeley Stat 210A Fall 2024"
chapter: 42
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 42. Empirical Bayes and James-Stein

## What this covers

This chapter answers two linked questions about estimating a high-dimensional mean: how do you
turn a hierarchical Bayes model into a usable estimator when you don't want to commit to a prior
(empirical Bayes), and why does the ordinary, unbiased, minimax sample mean turn out to be a *bad*
estimator once the dimension is at least three (the James–Stein paradox)? Along the way it develops
Stein's Lemma, a Gaussian integration-by-parts identity, and uses it to build Stein's Unbiased Risk
Estimate (SURE), a tool that computes the exact risk of an estimator without knowing the truth. It
assumes the normal-normal Bayes model, the notions of risk, admissibility, UMVU and minimaxity from
decision theory, maximum likelihood, and the $\chi^2$ distribution.

## The hierarchical model and the empirical Bayes idea

A common hierarchical Bayes setup for estimating many related parameters at once is

$$
\zeta \sim \lambda(\zeta), \qquad \theta_i \mid \zeta \stackrel{\text{iid}}{\sim} \pi_\zeta(\theta)
\ (i = 1,\dots,d), \qquad X_i \mid \theta, \zeta \stackrel{\text{ind.}}{\sim} P_{\theta_i}(x).
$$

Putting a prior $\lambda$ on the hyperparameter $\zeta$ itself is awkward: there is only *one* draw
of $\zeta$, which makes a prior on it hard to justify, but also hard to matter much if there is
enough other information in the data. The $\theta_i$ are a different story: each one is only
informed by its own $X_i$, so a prior genuinely helps there — and because there are *many* $\theta_i$
drawn from the same $\pi_\zeta$, the fit of that common prior can actually be checked against data,
unlike a one-off prior on $\zeta$.

The **empirical Bayes** compromise: treat $\zeta$ as a fixed, unknown constant rather than a random
variable.

1. Estimate $\zeta$ from the observed data (typically from the marginal distribution of $X$, having
   integrated out the $\theta_i$).
2. Plug $\hat\zeta$ into the Bayes rule for known $\zeta$, as though it were the true value.

## A worked example: shrinkage toward zero

Take $\theta_i \sim \mathcal N(0, \tau^2)$ with $\tau^2$ fixed but unknown, and $X_i \mid \theta \sim
\mathcal N(\theta_i, 1)$ for $i = 1,\dots,d$. If $\tau^2$ (equivalently $\zeta := 1/(1+\tau^2)$) were
known, the Bayes estimator of $\theta_i$ is the familiar shrinkage rule

$$
\delta_i(X) = (1-\zeta) X_i, \qquad \zeta = \frac{1}{1+\tau^2}.
$$

To estimate $\zeta$ without knowing $\tau^2$, integrate the $\theta_i$ out: marginally,
$X \sim \mathcal N_d(0, \zeta^{-1} I_d)$, with density

$$
\left(\frac{\zeta}{2\pi}\right)^{d/2} e^{-\zeta \|X\|^2/2},
$$

so $\|X\|^2$ is sufficient for $\zeta$. Maximizing the log-density in $\zeta$,

$$
\frac{d}{2}\log\zeta - \frac{d}{2}\log(2\pi) - \frac{\zeta\|X\|^2}{2}
\quad\Longrightarrow\quad
\frac{d}{2\zeta} - \frac{\|X\|^2}{2} = 0 \ \Longrightarrow\ \hat\zeta_{\text{MLE}} = \frac{d}{\|X\|^2},
$$

which agrees with the scaling fact $\|X\|^2 \sim \zeta^{-1}\chi^2_d$ (mean $d/\zeta$). Plugging in
gives the empirical Bayes rule

$$
\delta_i(X) = \left(1 - \frac{d}{\|X\|^2}\right) X_i,
$$

which the notes flag as "near-optimal" once $d$ is large.

## The James–Stein estimator

James and Stein proposed a slightly different correction, for $d \ge 3$:

$$
\delta_{\text{JS}, i}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right) X_i.
$$

The empirical Bayes motivation for using $d-2$ rather than $d$ is that $\dfrac{d-2}{\|X\|^2}$ is the
**UMVUE** of $\zeta$ (not merely the MLE). The key input is a fact about the reciprocal of a
chi-squared variable.

**Proposition.** If $Y \sim \chi^2_d = \mathrm{Gamma}(d/2, 2)$ and $d \ge 3$, then $\mathbb E[1/Y] =
1/(d-2)$.

*Proof.* Write out the expectation against the $\chi^2_d$ density and shift the exponent to expose a
$\chi^2_{d-2}$ density:

$$
\mathbb E\!\left[\frac1Y\right] = \int_0^\infty \frac1y \cdot \frac{1}{2^{d/2}\Gamma(d/2)} y^{d/2 - 1}
e^{-y/2}\,dy
= \frac{2^{(d-2)/2}\Gamma\!\left(\frac{d-2}2\right)}{2^{d/2}\Gamma\!\left(\frac d2\right)}
\underbrace{\int_0^\infty \frac{1}{2^{(d-2)/2}\Gamma\!\left(\frac{d-2}2\right)} y^{(d-2)/2 - 1}
e^{-y/2}\,dy}_{=\,1,\ \chi^2_{d-2}\text{ density integrates to }1}.
$$

(This step needs $d > 2$, i.e. $d \ge 3$, for $(d-2)/2 > 0$.) Using $\Gamma(x) = (x-1)\Gamma(x-1)$
with $x = d/2$ collapses the ratio of gammas:

$$
\frac{\Gamma\!\left(\frac{d-2}2\right)}{\Gamma\!\left(\frac d2\right)}
= \frac{1}{(d-2)/2}, \qquad\text{so}\qquad
\mathbb E\!\left[\frac1Y\right] = \frac12 \cdot \frac{1}{(d-2)/2} = \frac{1}{d-2}. \qquad\blacksquare
$$

Now apply this with $Y = \zeta\|X\|^2 \sim \chi^2_d$ (from $\|X\|^2 \sim \zeta^{-1}\chi^2_d$):

$$
\zeta^{-1}\,\mathbb E_\zeta\!\left[\frac{1}{\|X\|^2}\right] = \frac{1}{d-2}
\quad\Longrightarrow\quad
\mathbb E_\zeta\!\left[\frac{d-2}{\|X\|^2}\right] = \zeta,
$$

so $\hat\zeta = (d-2)/\|X\|^2$ is exactly unbiased for $\zeta$, and since $\|X\|^2$ is a complete
sufficient statistic for the scale family $\mathcal N_d(0,\zeta^{-1}I_d)$, it is the UMVUE.

## The James–Stein paradox

Now drop the Bayes model entirely. Consider the ordinary Gaussian sequence model with $\theta$ a
fixed, unknown vector:

$$
X_i \stackrel{\text{iid}}{\sim} \mathcal N_d(\theta, \sigma^2 I_d), \quad \theta \in \mathbb R^d,\ \
\sigma^2 > 0 \text{ known}, \quad i = 1,\dots,n, \qquad \bar X = \frac1n\sum_i X_i.
$$

James and Stein's 1956 result: for $d \ge 3$, the sample mean $\bar X$ — which is unbiased, UMVU,
minimax, and the objective Bayes estimator — is **inadmissible** for $\theta$ under squared error
loss. Explicitly, with

$$
\delta_{\text{JS}}(X) = \left(1 - \frac{(d-2)\sigma^2/n}{\|\bar X\|^2}\right)\bar X,
$$

$$
\text{MSE}(\theta, \delta_{\text{JS}}) < \text{MSE}(\theta, \bar X) \qquad \text{for every } \theta
\in \mathbb R^d.
$$

By sufficiency, $\bar X$ carries all the information in the sample, so it is enough to study the
reduced problem $n = 1$, $\sigma^2 = 1$: $X \sim \mathcal N_d(\theta, I_d)$, with
$\delta_{\text{JS}}(X) = \bigl(1 - (d-2)/\|X\|^2\bigr)X$.

Two things make this genuinely shocking rather than a Bayes-flavored curiosity:

- **No prior on $\theta$ is assumed.** The domination holds for *every* fixed $\theta$, including
  wild, unrelated coordinates such as $\theta = (500, -10^{10}, 4)$.
- **Nothing is special about the origin.** For any fixed $\theta_0 \in \mathbb R^d$,

$$
\delta(X) = \theta_0 + \left(1 - \frac{d-2}{\|X - \theta_0\|^2}\right)(X - \theta_0)
$$

also dominates $X$. Shrinking toward *any* fixed point beats not shrinking at all.

The deep implication: shrinkage is not merely a Bayesian convenience. It is a purely frequentist
phenomenon that improves squared-error risk with no distributional assumption on $\theta$ at all.

## Linear shrinkage without Bayesian assumptions

This suggests studying shrinkage directly as a frequentist tuning problem. In the model $X \sim
\mathcal N_d(\theta, I_d)$ with fixed $\theta$, consider the family $\delta_\zeta(X) = (1-\zeta)X$,
for a tuning constant $\zeta$ (the same role $\zeta$ played above, now just a knob rather than a
Bayes hyperparameter). Its risk decomposes as bias$^2$ plus variance:

$$
R(\theta;\delta_\zeta) = \|\theta - \mathbb E\delta_\zeta(X)\|^2 + \sum_i \mathrm{Var}\bigl((1-\zeta)X_i\bigr)
= \underbrace{\zeta^2\|\theta\|^2}_{\text{bias}^2} + \underbrace{d(1-\zeta)^2}_{\text{variance}}.
$$

Minimizing over $\zeta$:

$$
\frac{d}{d\zeta}R(\theta;\delta_\zeta) = 2\zeta\|\theta\|^2 - 2(1-\zeta)d = 0
\quad\Longrightarrow\quad
\zeta^*(\theta) = \frac{d}{d + \|\theta\|^2} = \frac{1}{1 + \|\theta\|^2/d}.
$$

The optimal shrinkage $\zeta^*(\theta)$ is always strictly positive — some shrinkage always helps —
but tends to $0$ as $\|\theta\| \to \infty$, so a huge signal should barely be shrunk. Of course
$\zeta^*(\theta)$ is an oracle quantity: it depends on the unknown $\theta$. This leaves the natural
question the lecture poses next: **what if we estimate $\zeta^*(\theta)$ from the data**, and how
does the resulting adaptivity of $\hat\zeta(X)$ affect the MSE? Answering this requires a way to
compute — or at least unbiasedly estimate — the risk of a data-dependent shrinkage rule, which is
exactly what the next tool provides.

## Stein's Lemma

**Theorem (Stein's Lemma, univariate).** Suppose $X \sim \mathcal N(\theta,\sigma^2)$ and $h:\mathbb
R \to \mathbb R$ is differentiable with $\mathbb E|h'(X)| < \infty$. Then

$$
\mathbb E[(X-\theta)h(X)] = \sigma^2\,\mathbb E[h'(X)].
$$

The left side is $\mathrm{Cov}(X, h(X))$, so this is a covariance identity: covariance with a
Gaussian equals the (scaled) expected derivative.

*Proof.* First note the identity is unaffected by replacing $h$ with $h - h(0)$: shifting $h$ by a
constant $c$ changes the left side by $c\,\mathbb E[X-\theta] = 0$ and leaves $h'$ unchanged. So
without loss of generality $h(0) = 0$.

Take $\theta = 0$, $\sigma^2 = 1$ first, and split $\mathbb E[Xh(X)]$ at $0$. For $x > 0$, write
$h(x) = \int_0^x h'(y)\,dy$ (using $h(0)=0$) and swap the order of integration over $\{0 < y < x\}$:

$$
\int_0^\infty x\,h(x)\,\phi(x)\,dx = \int_0^\infty\!\!\int_0^\infty \mathbf 1_{\{y<x\}}\, x\, h'(y)\,
\phi(x)\,dx\,dy = \int_0^\infty h'(y)\left[\int_y^\infty x\phi(x)\,dx\right]dy = \int_0^\infty h'(y)
\phi(y)\,dy,
$$

using $\phi'(x) = -x\phi(x)$, so $\int_y^\infty x\phi(x)\,dx = \phi(y)$. The same argument on
$(-\infty, 0)$ gives $\int_{-\infty}^0 x h(x)\phi(x)\,dx = \int_{-\infty}^0 h'(x)\phi(x)\,dx$. Adding
the two halves gives the result for $\theta=0,\sigma^2=1$.

For general $\theta,\sigma$, write $X = \theta + \sigma Z$ with $Z \sim \mathcal N(0,1)$ and apply the
$\theta=0,\sigma=1$ case to $g(z) = h(\theta + \sigma z)$, whose derivative is $g'(z) = \sigma
h'(\theta+\sigma z)$:

$$
\mathbb E[(X-\theta)h(X)] = \sigma\,\mathbb E[Z\,h(\theta+\sigma Z)] = \sigma\,\mathbb E[g'(Z)]
= \sigma^2\,\mathbb E[h'(\theta+\sigma Z)] = \sigma^2\,\mathbb E[h'(X)]. \qquad\blacksquare
$$

### Multivariate version

For $h:\mathbb R^d \to \mathbb R^d$ differentiable, its Jacobian $Dh(x) \in \mathbb R^{d\times d}$ has
entries $(Dh(x))_{ij} = \partial h_i/\partial x_j(x)$, and the Frobenius norm is $\|A\|_F =
\bigl(\sum_{i,j}A_{ij}^2\bigr)^{1/2}$.

**Theorem (Stein's Lemma, multivariate).** If $X \sim \mathcal N_d(\theta, \sigma^2 I_d)$ and
$h:\mathbb R^d \to \mathbb R^d$ is differentiable with $\mathbb E\|Dh(X)\|_F < \infty$, then

$$
\mathbb E[(X-\theta)^\top h(X)] = \sigma^2\,\mathbb E\,\mathrm{tr}(Dh(X)) = \sigma^2 \sum_i \mathbb
E\frac{\partial h_i}{\partial x_i}(X).
$$

*Proof.* Because the coordinates of $X$ are independent, condition on $X_{-i}$ (all coordinates but
the $i$-th) and apply the univariate lemma to $x_i \mapsto h_i(x_i, X_{-i})$:

$$
\mathbb E[(X_i - \theta_i)h_i(X)] = \mathbb E\Bigl[\mathbb E\bigl[(X_i-\theta_i)h_i(X) \mid X_{-i}
\bigr]\Bigr] = \mathbb E\left[\mathbb E\left[\sigma^2\frac{\partial h_i}{\partial x_i}(X) \,\middle|\,
X_{-i}\right]\right] = \sigma^2\,\mathbb E\frac{\partial h_i}{\partial x_i}(X).
$$

Summing over $i$ gives the claim. $\blacksquare$

## Stein's Unbiased Risk Estimate (SURE)

Stein's Lemma turns into a way of computing (or unbiasedly estimating) the risk of *any* estimator
$\delta(X)$, not just $X$ itself. Write $h(X) = X - \delta(X)$, and take $\sigma^2=1$. Then

$$
R(\theta;\delta) = \mathbb E_\theta\|X-\theta-h(X)\|^2 = \mathbb E_\theta\|X-\theta\|^2 + \mathbb
E_\theta\|h(X)\|^2 - 2\,\mathbb E_\theta[(X-\theta)^\top h(X)],
$$

and applying the multivariate Stein's Lemma to the cross term ($\mathbb E_\theta\|X-\theta\|^2 = d$):

$$
R(\theta;\delta) = d + \mathbb E_\theta\|h(X)\|^2 - 2\,\mathbb E_\theta\,\mathrm{tr}(Dh(X)).
$$

So

$$
\hat R(X) = d + \|h(X)\|^2 - 2\,\mathrm{tr}(Dh(X))
$$

is an **unbiased estimator** of the MSE — it is a genuine statistic, a function of $X$ alone, with
$R(\theta;\delta) = \mathbb E_\theta \hat R(X)$ for every $\theta$.

Two check cases:

- $\delta(X) = X \Rightarrow h(X) = 0, Dh(X) = 0 \Rightarrow \hat R = d = R(\theta;X)$ for all $\theta$
  (exactly, with no estimation error — as it must be, since $\mathrm{Var}(X_i)=1$ for every $i$).
- $\delta_\zeta(X) = (1-\zeta)X$ for a *fixed* $\zeta$: $h(X) = \zeta X$, $Dh = \zeta I_d$, so
  $\mathrm{tr}(Dh) = \zeta d$ and

$$
\hat R = d + \zeta^2\|X\|^2 - 2\zeta d = (1-2\zeta)d + \zeta^2\|X\|^2.
$$

## The risk of the James–Stein estimator

SURE lets us pin down exactly how much the James–Stein estimator improves on $X$. Here $h(X) =
\dfrac{d-2}{\|X\|^2}X$, so $\|h(X)\|^2 = (d-2)^2/\|X\|^2$. Writing $S = \|X\|^2 = \sum_j X_j^2$,

$$
\frac{\partial h_i}{\partial x_i}(X) = \frac{\partial}{\partial x_i}\frac{(d-2)X_i}{S}
= (d-2)\,\frac{S - 2X_i^2}{S^2},
$$

so, summing over $i$ (using $\sum_i(S-2X_i^2) = dS - 2S = (d-2)S$),

$$
\mathrm{tr}(Dh(X)) = \frac{d-2}{S^2}\sum_i (S-2X_i^2) = \frac{(d-2)^2}{S}.
$$

Plugging into SURE,

$$
\hat R(X) = d + \frac{(d-2)^2}{S} - 2\frac{(d-2)^2}{S} = d - \frac{(d-2)^2}{\|X\|^2},
$$

and taking expectations,

$$
R(\theta;\delta_{\text{JS}}) = d - (d-2)^2\,\underbrace{\mathbb E\!\left[\frac1{\|X\|^2}\right]}_{>\,0}
< d = R(\theta; X) \qquad \text{for every } \theta.
$$

This is the paradox made rigorous: the correction term is a positive quantity for every $\theta$
(finiteness of the expectation is exactly the $d \ge 3$ condition from the Proposition above), so
$\delta_{\text{JS}}$ strictly beats $X$ everywhere, not just on average over some prior.

Two limits show how the size of the improvement varies with $\theta$:

- **At $\theta = 0$:** $\|X\|^2 \sim \chi^2_d$, so by the Proposition, $\mathbb E_0[1/\|X\|^2] =
  1/(d-2)$, giving

$$
R(0;\delta_{\text{JS}}) = d - (d-2) = 2,
$$

  which can be enormously smaller than $d$.

- **As $\|\theta\| \to \infty$:** $X$ concentrates near $\theta$, so $\mathbb E_\theta[1/\|X\|^2]
  \approx 1/\|\theta\|^2$, giving

$$
R(\theta;\delta_{\text{JS}}) \approx d - \frac{(d-2)^2}{\|\theta\|^2} \longrightarrow d.
$$

The advantage shrinks toward nothing for a very large signal, but it never vanishes and is never
negative.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Risk of the James-Stein estimator as a function of the norm of theta, against the constant risk of the sample mean">
  <line x1="45" y1="185" x2="335" y2="185" stroke="currentColor" stroke-width="1.5"/>
  <line x1="45" y1="185" x2="45" y2="25" stroke="currentColor" stroke-width="1.5"/>
  <text x="335" y="202" text-anchor="end" font-size="12" fill="currentColor">||&#952;||</text>
  <text x="52" y="35" font-size="12" fill="currentColor">risk</text>
  <line x1="45" y1="60" x2="335" y2="60" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <text x="335" y="55" text-anchor="end" font-size="12" fill="currentColor">sample mean: risk = d</text>
  <path d="M45,178 C130,172 210,100 335,63" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="55" y="168" font-size="12" fill="currentColor">James&#8211;Stein: risk = 2 at &#952;=0</text>
</svg>
<figcaption>The James-Stein risk is bounded below the sample mean's constant risk d for every &#952;,
equal to 2 at &#952;=0, and climbs back toward d (but never reaches it) as ||&#952;|| grows.</figcaption>
</figure>

## Refinements, and a caution about the paradox

James–Stein itself is not the end of the story:

- **$\delta_{\text{JS}}$ is inadmissible too.** When $\|X\|^2 < d-2$, the factor $1 - (d-2)/\|X\|^2$
  is negative, which flips the sign of every coordinate — clearly wasteful. Clipping at zero,

$$
\delta_{\text{JS}+}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right)_+ X,
$$

  is strictly better than $\delta_{\text{JS}}$.

- **Shrinking toward the grand mean is the practically useful version.** Since nothing was special
  about the origin, shrink toward $\bar X \mathbf 1_d$ instead:

$$
\delta_{\text{JS},2}(X) = \bar X\mathbf 1_d + \left(1 - \frac{d-3}{\|X - \bar X\mathbf 1_d\|^2}\right)
(X - \bar X \mathbf 1_d),
$$

  which dominates $\delta(X) = X$ for $d \ge 4$ — one degree of freedom is spent estimating $\bar X$,
  which is why the correction uses $d-3$ and the threshold moves from $3$ to $4$.

- **The pooling paradox, and its limit.** Taken to its logical extreme, the result says that
  unrelated quantities benefit from being estimated jointly — should everyone at Berkeley pool their
  (unrelated) estimates? That sounds absurd, and the caveat that tempers it is real: what improves is
  the *total* squared error $\mathbb E\|\hat\theta - \theta\|^2$. The MSE of an *individual*
  coordinate, $\mathbb E[(X_i-\theta_i)^2]$, can actually get worse under shrinkage. The paradox is a
  statement about aggregate risk, not a guarantee for every component.

## Sources

All of this chapter is drawn from three converted pages of handwritten lecture notes for Berkeley
Stat 210A, dated on the page as 10/3/2023 and filed under the Fall 2024 course repository:

- `01-empirical-bayes.md` — the hierarchical model, the empirical Bayes motivation, the
  normal-normal worked example, the James–Stein estimator and its UMVUE justification, the
  James–Stein paradox statement, and the non-Bayesian linear-shrinkage optimization ending in the
  open question about estimating $\zeta^*(\theta)$.
- `02-stein-s-lemma.md` — the univariate and multivariate Stein's Lemma with proofs, and the
  derivation of SURE.
- `03-risk-of-james-stein.md` — the SURE computation of the James–Stein estimator's exact risk, the
  $\theta=0$ and $\|\theta\|\to\infty$ limits, the positive-part and recentered refinements, and the
  pooling caveat.

No slide deck, transcript, or problem set was supplied for this lecture; the three files above are
the whole of the input. Each carries the note that it was reconstructed by a model from a scanned
PDF with no text layer (`handwritten/lecture11-F24.pdf`, CC BY 4.0), and that every equation in the
source is unverified. The algebra in this chapter (the gamma-function proof, the Stein's Lemma
proofs, and the SURE computation for James–Stein) has been checked step-by-step against the stated
results and is internally consistent; the underlying source scan was not independently reviewed.

---

[← 41. Hierarchical Bayes Models](41-hierarchical-bayes-models.md) · [Contents](index.md) · [43. Minimax Estimation (part 1) →](43-minimax-estimation-part-1.md)
