---
title: "35. Rao\u2013Blackwell and UMVU Estimators"
course: "Berkeley Stat 210A Fall 2024"
chapter: 35
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 35. Rao–Blackwell and UMVU Estimators

## What this covers

This chapter answers a natural follow-up to sufficiency and completeness: among all estimators
that are *unbiased* for a target $g(\theta)$, is there always a single best one, and how do you
find it? It assumes the reader already knows what a sufficient statistic and a complete statistic
are, and is comfortable with risk functions, bias and variance. The chapter ends by asking whether
requiring zero bias was ever the right thing to want.

## Where this fits: three ways to choose an estimator

Recall the general problem: many estimators exist for the same target, and the risk
$R(\theta;\delta) = \mathbb{E}_\theta L(\theta,\delta(X))$ is a function of $\theta$, not a single
number, so "smallest risk" is not automatically well defined. Two strategies for making the
comparison meaningful were:

1. collapse the risk function to a single scalar (its average or its supremum over $\theta$), or
2. restrict attention to a smaller class of estimators, small enough that one of them dominates
   the rest for every $\theta$.

This lecture develops the second route in a specific and very productive form: restrict to
**unbiased** estimators, i.e. those with $\mathbb{E}_\theta \delta(X) = g(\theta)$ for every
$\theta \in \Theta$. The reward, when a complete sufficient statistic $T(X)$ is available, is
strong: there is at most one unbiased estimator that is a function of $T$, and if it exists it is
uniformly best — for *every* $\theta$ at once — among *all* unbiased estimators, for any convex
loss function.

## Convex loss and Jensen's inequality

A function $f$ is **convex** if for all $x_1, x_2$ and all $\gamma \in [0,1]$,
$$f(\gamma x_1 + (1-\gamma) x_2) \le \gamma f(x_1) + (1-\gamma) f(x_2),$$
and **strictly convex** if the inequality is strict whenever $x_1 \ne x_2$ and $\gamma \in (0,1)$.
Geometrically, the graph of $f$ lies below every chord joining two of its points.

**Jensen's inequality.** If $f$ is convex, then for any random variable $X$,
$$f(\mathbb{E}X) \le \mathbb{E}f(X),$$
with strict inequality (when $f$ is strictly convex) unless $X$ is almost surely constant.

Why this holds: convexity guarantees that at any point $x_0$ there is a line
$\ell(x) = a + bx$ that touches $f$ at $x_0$ and lies below it everywhere — $\ell(x_0) = f(x_0)$
and $\ell(x) \le f(x)$ for all $x$. Take $x_0 = \mathbb{E}X$. Then
$$f(\mathbb{E}X) = \ell(\mathbb{E}X) = \mathbb{E}[\ell(X)] \le \mathbb{E}[f(X)],$$
using linearity of expectation in the middle step. Strictness can fail only if $\ell(X) = f(X)$
almost surely, which for strictly convex $f$ forces $X$ to equal $x_0$ almost surely.

A **loss function** $L(\theta,d)$ is convex if it is convex in $d$ for each fixed $\theta$. The
running example is squared-error loss, $L(\theta,d) = (g(\theta)-d)^2$, whose risk is the mean
squared error,
$$\mathrm{MSE}(\theta;\delta) = \mathbb{E}_\theta\big[(g(\theta)-\delta(X))^2\big]
= \mathrm{Bias}_\theta(\delta)^2 + \mathrm{Var}_\theta(\delta(X)),$$
which collapses to $\mathrm{Var}_\theta(\delta(X))$ exactly when $\delta$ is unbiased. This is the
sense in which convex losses "penalize noise": once bias is pinned at zero, all that is left to
control is variance.

## The Rao–Blackwell theorem

Suppose $T(X)$ is sufficient and $\delta(X)$ is some estimator that ignores this — it is not
already a function of $T$. There is a mechanical way to improve it. Define the
**Rao–Blackwellization** of $\delta$,
$$\bar\delta(T(X)) = \mathbb{E}[\delta(X) \mid T(X)].$$
This is a genuine statistic — no $\theta$ appears in it — precisely because $T$ is sufficient: the
conditional distribution of $X$ given $T$ does not depend on $\theta$, so neither does this
conditional expectation.

**Theorem (Rao–Blackwell).** If $L(\theta,\cdot)$ is convex, then $R(\theta;\bar\delta) \le
R(\theta;\delta)$ for every $\theta$. If $L(\theta,\cdot)$ is strictly convex, the inequality is
strict unless $\delta(X) = \bar\delta(T(X))$ almost surely.

*Proof.* By Jensen's inequality applied to the conditional distribution of $\delta(X)$ given $T$,
$$R(\theta;\bar\delta) = \mathbb{E}_\theta\big[L(\theta, \mathbb{E}[\delta \mid T])\big]
\le \mathbb{E}_\theta\big[\mathbb{E}[L(\theta,\delta)\mid T]\big] = R(\theta;\delta),$$
the last step by the tower property, with strict inequality (for strictly convex $L$) unless
$\delta = \bar\delta$ almost surely. $\blacksquare$

So Rao–Blackwellizing never hurts and, generically, strictly helps: conditioning on a sufficient
statistic removes exactly the randomness in $\delta$ that carries no information about $\theta$,
and a convex loss always charges for carrying that extra noise.

## UMVU estimators

Not every quantity has an unbiased estimator at all.

**Definition.** $g(\theta)$ is **U-estimable** if there exists $\delta(X)$ with
$\mathbb{E}_\theta\delta(X) = g(\theta)$ for all $\theta \in \Theta$.

**Definition.** An unbiased estimator $\delta(X)$ of $g(\theta)$ is **uniformly minimum variance
unbiased (UMVU)** if $\mathrm{Var}_\theta(\delta(X)) \le \mathrm{Var}_\theta(\tilde\delta(X))$ for
every $\theta \in \Theta$ and every other unbiased $\tilde\delta$.

**Theorem.** Let $T(X)$ be complete and sufficient, and let $g(\theta)$ be U-estimable. Then there
is a unique estimator $\delta^*(T(X))$ that is unbiased for $g(\theta)$, and it

1. is UMVU, and moreover
2. uniformly minimizes risk, among all unbiased estimators, for *any* convex loss function.

*Proof.*

- **Existence.** Take any unbiased $\delta_0(X)$ (one exists, since $g$ is U-estimable) and set
  $\delta^*(T) = \mathbb{E}[\delta_0 \mid T]$. This is unbiased:
  $\mathbb{E}_\theta \delta^* = \mathbb{E}_\theta \mathbb{E}[\delta_0 \mid T]
  = \mathbb{E}_\theta \delta_0 = g(\theta)$.
- **Uniqueness.** If $\delta(T)$ is another unbiased function of $T$, then
  $\mathbb{E}_\theta[\delta^*(T) - \delta(T)] = 0$ for all $\theta$, and completeness of $T$ forces
  $\delta^*(T) = \delta(T)$ almost surely.
- **Optimality for any convex loss.** Let $\delta(X)$ be *any* unbiased estimator (not necessarily
  a function of $T$), and Rao–Blackwellize it: $\bar\delta(T) = \mathbb{E}[\delta \mid T]$. By the
  uniqueness step, $\bar\delta(T) = \delta^*(T)$ almost surely. By Rao–Blackwell,
  $R(\theta;\delta^*) = R(\theta;\bar\delta) \le R(\theta;\delta)$ for every $\theta$. Taking $L$ to
  be squared error gives $\mathrm{Var}_\theta(\delta^*) \le \mathrm{Var}_\theta(\delta)$, so
  $\delta^*$ is UMVU. $\blacksquare$

The proof's slogan: *every* Rao–Blackwellization of *every* unbiased estimator collapses onto the
same $\delta^*$ — completeness is what forces all roads to lead to the same place.

This gives two practical recipes for finding a UMVUE, both used below:

1. Search directly among functions of $T$ for one that is unbiased.
2. Find *any* unbiased estimator (a function of $T$ or not) and Rao–Blackwellize it.

## Example: estimating $\theta^2$ for a Poisson mean

Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} \mathrm{Poisson}(\theta)$, with
$p_\theta(x) = \theta^x e^{-\theta}/x!$, and take $g(\theta) = \theta^2$. The statistic
$T = \sum_i X_i \sim \mathrm{Poisson}(n\theta)$ is complete and sufficient, with mass function
$p_\theta^T(t) = (n\theta)^t e^{-n\theta}/t!$.

**Method 1: solve directly.** A function $\delta(T)$ is unbiased for $\theta^2$ iff
$$\sum_{t=0}^\infty \delta(t) \frac{(n\theta)^t e^{-n\theta}}{t!} = \theta^2 \quad \text{for all } \theta,$$
i.e.
$$\sum_{t=0}^\infty \delta(t)\frac{n^t}{t!}\theta^t = e^{n\theta}\theta^2
= \sum_{k=0}^\infty \frac{n^k}{k!}\theta^{k+2}.$$
Both sides are power series in $\theta$; matching coefficients of $\theta^t$ forces
$\delta(0)=\delta(1)=0$ and, for $t \ge 2$ (writing $t = k+2$),
$$\delta(t)\frac{n^t}{t!} = \frac{n^{t-2}}{(t-2)!} \quad\Longrightarrow\quad \delta(t) = \frac{t(t-1)}{n^2}.$$
So the UMVUE is $\delta^*(T) = T(T-1)/n^2$ — close to the naive plug-in $(T/n)^2$ for large $t$, but
corrected downward.

**Method 2: Rao-Blackwellize.** $\delta_0(X) = X_1 X_2$ is unbiased for $\theta^2$, since
independence gives $\mathbb{E}_\theta[X_1X_2] = (\mathbb{E}_\theta X_1)(\mathbb{E}_\theta X_2)
= \theta^2$. To find $\mathbb{E}[X_1X_2\mid T]$, use the standard fact that, conditional on
$T=t$, the vector $(X_1,\dots,X_n)$ is $\mathrm{Multinomial}(t, (1/n,\dots,1/n))$: the $t$
Poisson "arrivals" are equally likely to have come from any of the $n$ coordinates. Then
$X_1 \mid T \sim \mathrm{Binomial}(T,1/n)$, so
$$\mathbb{E}[X_1\mid T] = T/n, \qquad \mathrm{Var}(X_1\mid T) = \frac{T(n-1)}{n^2},$$
and, given $T$ and $X_1$, the remaining $T-X_1$ arrivals are spread equally over the other $n-1$
coordinates, so $\mathbb{E}[X_2 \mid T, X_1] = (T-X_1)/(n-1)$. By the tower rule,
$$\mathbb{E}[X_1X_2\mid T] = \mathbb{E}\Big[X_1\cdot\frac{T-X_1}{n-1}\,\Big|\,T\Big]
= \frac{1}{n-1}\Big(T\,\mathbb{E}[X_1\mid T] - \mathbb{E}[X_1^2 \mid T]\Big).$$
Using $\mathbb{E}[X_1^2\mid T] = \mathrm{Var}(X_1\mid T) + \mathbb{E}[X_1\mid T]^2
= \frac{T(n-1)}{n^2} + \frac{T^2}{n^2}$, this simplifies to
$$\mathbb{E}[X_1X_2\mid T] = \frac{T(T-1)}{n^2},$$
the same answer as Method 1, exactly as the uniqueness half of the theorem guarantees.

## Example: estimating the range of a uniform distribution

Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} \mathrm{Uniform}[0,\theta]$. The maximum
$T = X_{(n)}$ is complete and sufficient, with density $p_\theta^T(t) = \frac{n}{\theta^n}t^{n-1}$
on $[0,\theta]$. Its mean is
$$\mathbb{E}_\theta T = \int_0^\theta t\cdot\frac{n}{\theta^n}t^{n-1}\,dt = \frac{n}{n+1}\theta,$$
so $\frac{n+1}{n}T$ is unbiased for $\theta$, hence UMVU.

**Alternative route.** $2X_1$ is unbiased for $\theta$ (since $\mathbb{E}X_1 = \theta/2$).
Conditional on $T$, $X_1$ is the maximum itself with probability $1/n$ (it is equally likely to be
any of the $n$ order statistics), and otherwise — with probability $(n-1)/n$ — it is uniform on
$[0,T]$:
$$X_1 \mid T \sim \begin{cases} T & \text{w.p. } 1/n \\ \mathrm{Uniform}[0,T] & \text{w.p. } (n-1)/n.\end{cases}$$
So $\mathbb{E}[2X_1 \mid T] = 2T\cdot\frac1n + T\cdot\frac{n-1}{n} = \frac{n+1}{n}T$ — again the
same estimator, as it must be.

Here the lecture adds a warning worth keeping: $\frac{n+1}{n}T$, although UMVU, is *itself
inadmissible* — there is an estimator of the form $cT$ with strictly smaller MSE for every
$\theta$ (the lecture cites Keener's result that $c = \frac{n+2}{n+1}$ is best among constant
multiples of $T$). Being the best *unbiased* estimator says nothing about whether some biased
estimator beats it outright. That observation is the hinge the rest of the lecture turns on:
**why insist on zero bias in the first place?**

## Should unbiasedness be trusted?

Two examples make the case that the UMVU theorem, though airtight, can hand back an estimator
with no epistemic virtue at all.

**A discontinuous UMVUE.** Let $X \sim \mathrm{Binomial}(1000,\theta)$ and suppose the target is
$g(\theta) = \mathbb{P}_\theta(X \ge 500)$. Since $X$ is itself complete and sufficient, and
$\mathbb{1}\{X\ge 500\}$ is trivially unbiased for $g(\theta)$ (its expectation *is* $g(\theta)$
by definition), it is the UMVUE. But then observing $X = 500$ forces the conclusion
"$g(\theta) = 100\%$", while $X=499$ forces "$g(\theta)=0\%$" — a single trial's worth of data
flipping the estimate between the two extremes. This is not a reasonable summary of the evidence;
an MLE- or Bayes-based estimate of $g(\theta)$ would move continuously with $X$ instead.

The general point: the UMVU theorem says the estimator is *best among unbiased estimators of
$g(\theta)$*, which is a much weaker claim than "sensible." Indeed, any function $h(T)$ of the
complete sufficient statistic is automatically the UMVUE of its own expectation
$\mathbb{E}_\theta h(T)$ — unbiasedness for *some* target is cheap, and the theorem never checks
whether that target, or the constraint of zero bias, was the right thing to want.

**A UMVUE that can be dominated outright.** Let $X_i \overset{\text{iid}}{\sim} N(\mu_i,1)$ for
$i=1,\dots,d$, written $X \sim N_d(\mu, I_d)$, and take $g(\mu) = \|\mu\|^2$. The full data $X$ is
complete and sufficient. Writing $X = \mu + Z$ with $Z \sim N_d(0,I_d)$,
$$\mathbb{E}_\mu\|X\|^2 = \mathbb{E}\|\mu+Z\|^2 = \|\mu\|^2 + \mathbb{E}\|Z\|^2 + 2\mu^\top\mathbb{E}[Z]
= \|\mu\|^2 + d,$$
since $\mathbb{E}\|Z\|^2 = d$ and $\mathbb{E}[Z]=0$. So $\delta(X) = \|X\|^2 - d$ is unbiased for
$\|\mu\|^2$, and by completeness it is the UMVUE.

But $\|\mu\|^2 \ge 0$ always, while $\delta(X)$ is not: at $\mu=0$, $\|X\|^2$ is
$\chi^2_d$-distributed, whose median sits slightly below its mean $d$, so $\delta(X) < 0$ close to
half the time. The truncated estimator
$$\big(\|X\|^2-d\big)_+ = \max\big(0,\ \|X\|^2-d\big)$$
strictly dominates the UMVUE — smaller MSE for every $\mu$ — despite being biased. Clipping an
unbiased estimator at a boundary the parameter is known to respect can only help, and here it
strictly does.

Both examples land the same lesson: completeness plus sufficiency hands you *the* unbiased
estimator, uniquely and mechanically, but the mechanism has no way to notice that unbiasedness
itself, or the target $g(\theta)$, might not have been the thing worth optimizing.

## Sources

- Handwritten lecture notes (a course PDF with no usable text layer, converted by a model — every
  equation in the conversion is flagged unverified by the conversion itself):
  - `statistics/berkeley/stat210a/fall-2024/handwritten/lecture06-F24/01-outline.md` —
    orientation (unbiased estimation as a third strategy for choosing among estimators), convex
    loss functions and Jensen's inequality, the Rao–Blackwell theorem and proof, the UMVU
    definitions, and the existence/uniqueness/optimality theorem and proof.
  - `statistics/berkeley/stat210a/fall-2024/handwritten/lecture06-F24/02-finding-the-umvue.md` —
    the two recipes for finding a UMVUE, the Poisson ($\theta^2$) and uniform ($X_{(n)}$)
    examples worked both ways, Keener's admissibility remark (cited but not derived in the
    notes), the binomial tail-probability example, and the Gaussian sequence model example.
- The lecture is dated 9/14 in the notes themselves; the equations above follow the reconstructed
  transcription and have not been checked against the original handwriting.
- No slides or spoken transcript were supplied for this lecture — the handwritten notes are the
  only source. No exercises were supplied.

---

[← 34. Completeness and Basu's Theorem](34-completeness-and-basu-s-theorem.md) · [Contents](index.md) · [36. Score, Fisher Information, and CRLB (part 1) →](36-score-fisher-information-and-crlb-part-1.md)
