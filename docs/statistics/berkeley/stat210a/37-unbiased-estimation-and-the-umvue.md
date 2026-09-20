---
title: "37. Unbiased Estimation and the UMVUE"
course: "Berkeley Stat 210A Fall 2024"
chapter: 37
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 37. Unbiased Estimation and the UMVUE

## What this covers

This lecture asks how to construct the best possible *unbiased* estimator of a quantity $g(\theta)$,
and whether "best unbiased" is actually the right thing to want. It assumes the two tools built in
the preceding lectures — sufficiency and completeness of a statistic $T(X)$ — and the notion of the
risk function $R(\theta;\delta) = \mathbb{E}_\theta L(\theta,\delta(X))$ of an estimator under a loss $L$.

## Two ways to narrow down a choice of estimator

Recall the general strategies for choosing among estimators: summarize the whole risk function by a
single scalar (its average or its supremum over $\theta$), or restrict attention to a smaller class
of estimators and ask for the best one *within* that class. Today's restriction is **unbiasedness**:
require
$$\mathbb{E}_\theta \delta(X) = g(\theta), \qquad \forall\, \theta \in \Theta,$$
where $g(\theta)$ is the quantity being estimated (the *estimand*).

The payoff is a clean uniqueness statement. If $T(X)$ is a **complete** sufficient statistic, then:

- there is **at most one** unbiased estimator that is a function of $T$ alone. (If $\mathbb{E}_\theta \delta_1(T) = \mathbb{E}_\theta \delta_2(T) = g(\theta)$ for all $\theta$, completeness forces $\delta_1(T) \stackrel{\text{a.s.}}{=} \delta_2(T)$.)
- if such an estimator exists, it **uniformly minimizes risk** — for *every* convex loss function, at every $\theta$, simultaneously.

The rest of the lecture makes the second claim precise, and then asks whether it is worth wanting.

## Convex loss functions

Recall $f$ is **convex** if for all $x_1,x_2$ and all $\gamma \in [0,1]$,
$$f(\gamma x_1 + (1-\gamma)x_2) \le \gamma f(x_1) + (1-\gamma) f(x_2),$$
and **strictly convex** if the inequality is strict whenever $x_1 \ne x_2$ and $\gamma \in (0,1)$.

**Jensen's inequality.** If $f$ is convex, then for any random variable $X$ with finite mean,
$$f(\mathbb{E} X) \le \mathbb{E} f(X).$$
If $f$ is strictly convex, the inequality is strict unless $X \stackrel{\text{a.s.}}{=} c$ for a constant $c$.

A loss $L(\theta,d)$ is called **convex** if it is convex in $d$, its second argument, for each fixed
$\theta$. The running example is squared error, $L(\theta,d) = (g(\theta)-d)^2$, for which the risk is
the mean squared error:
$$MSE(\theta;\delta) = \mathbb{E}_\theta\big[(g(\theta)-\delta(X))^2\big] = \mathrm{Bias}_\theta^2(\delta) + \mathrm{Var}_\theta(\delta),$$
which reduces to $\mathrm{Var}_\theta(\delta)$ when $\delta$ is unbiased. Convex losses are exactly the
losses that penalize an estimator for being *noisy*, which is why conditioning down onto a sufficient
statistic — a variance-reducing operation — helps against any of them.

## The Rao-Blackwell theorem

This is the recipe for improving any estimator $\delta(X)$ that ignores the sufficiency principle,
i.e. that uses more of $X$ than the sufficient statistic $T(X)$ actually needs.

**Theorem (Rao-Blackwell).** Let $T(X)$ be sufficient and $\delta(X)$ any estimator. Define
$$\bar\delta(T(X)) = \mathbb{E}[\delta(X) \mid T(X)]$$
— sufficiency guarantees this conditional expectation does not depend on $\theta$, so $\bar\delta$ is a
genuine statistic. If $L(\theta,\cdot)$ is convex, then
$$R(\theta;\bar\delta) \le R(\theta;\delta) \quad \text{for every } \theta.$$
If $L(\theta,\cdot)$ is strictly convex, the inequality is strict unless $\delta(X) \stackrel{\text{a.s.}}{=} \bar\delta(T(X))$ for every $\theta$.

*Proof.* Condition on $T$ and apply Jensen's inequality inside the expectation:
$$R(\theta;\bar\delta) = \mathbb{E}_\theta\big[L(\theta, \mathbb{E}[\delta \mid T])\big] \le \mathbb{E}_\theta\,\mathbb{E}\big[L(\theta,\delta)\mid T\big] = R(\theta;\delta). \qquad \blacksquare$$

$\bar\delta(T)$ is called the **Rao-Blackwellization** of $\delta$. Rao-Blackwellizing preserves
unbiasedness: if $\delta$ is unbiased for $g(\theta)$, so is $\bar\delta$, since
$\mathbb{E}_\theta \bar\delta = \mathbb{E}_\theta \mathbb{E}[\delta \mid T] = \mathbb{E}_\theta \delta = g(\theta)$.

## UMVU estimators

Not every estimand has an unbiased estimator at all.

**Definition.** $g(\theta)$ is **U-estimable** if there exists $\delta(X)$ with
$\mathbb{E}_\theta \delta(X) = g(\theta)$ for all $\theta$.

**Definition.** $\delta(X)$ is **uniform minimum variance unbiased (UMVU)** for $g(\theta)$ if it is
unbiased and, for every other unbiased $\tilde\delta$,
$$\mathrm{Var}_\theta(\delta(X)) \le \mathrm{Var}_\theta(\tilde\delta(X)) \qquad \forall\, \theta\in\Theta.$$

**Theorem.** Suppose $T(X)$ is complete sufficient for the model $\mathcal{P} = \{P_\theta : \theta\in\Theta\}$
and $g(\theta)$ is U-estimable. Then there is a unique estimator $\delta^*(T(X))$ that (1) is UMVU, and
(2) uniformly minimizes risk among *all* unbiased estimators, for every convex loss.

*Proof.* "All Rao-Blackwellizations lead to the same $\delta^*$."

- **Existence.** Take any unbiased $\delta_0(X)$ (one exists, since $g$ is U-estimable) and set
  $\delta^*(T) = \mathbb{E}[\delta_0 \mid T]$. Then
  $\mathbb{E}_\theta \delta^* = \mathbb{E}_\theta \mathbb{E}[\delta_0\mid T] = \mathbb{E}_\theta \delta_0 = g(\theta)$,
  so $\delta^*$ is unbiased.
- **Uniqueness.** If $\delta(T)$ is any other unbiased function of $T$, then
  $\mathbb{E}_\theta[\delta^*(T) - \delta(T)] = 0$ for all $\theta$, so completeness forces
  $\delta^*(T) \stackrel{\text{a.s.}}{=} \delta(T)$.
- **Optimality for any convex loss.** Let $\delta(X)$ be any unbiased estimator (not necessarily a
  function of $T$) and let $\bar\delta(T) = \mathbb{E}[\delta \mid T]$. By the uniqueness step,
  $\bar\delta(T) \stackrel{\text{a.s.}}{=} \delta^*(T)$. Rao-Blackwell then gives, for any convex loss,
  $$R(\theta;\delta^*) = R(\theta;\bar\delta) \le R(\theta;\delta).$$
  Specializing to squared error, $MSE(\theta;\delta^*)\le MSE(\theta;\delta)$, and since both are
  unbiased this says $\mathrm{Var}_\theta(\delta^*)\le \mathrm{Var}_\theta(\delta)$. So $\delta^*$ is
  UMVU. $\blacksquare$

## Finding the UMVUE

The proof suggests two routes to the same estimator:

1. Solve directly for the unique unbiased function of $T$.
2. Find *any* unbiased estimator of $g(\theta)$ (not necessarily a function of $T$) and
   Rao-Blackwellize it.

Both are illustrated on the same example.

### Example: squared Poisson mean

Let $X_1,\dots,X_n \stackrel{\text{iid}}{\sim} \mathrm{Pois}(\theta)$ and take $g(\theta)=\theta^2$. The
statistic $T=\sum_i X_i \sim \mathrm{Pois}(n\theta)$ is complete sufficient, with mass function
$p_\theta^T(t) = (n\theta)^t e^{-n\theta}/t!$.

**Method 1 (direct).** $\delta(T)$ is unbiased for $\theta^2$ iff
$$\sum_{t=0}^\infty \delta(t)\,\frac{(n\theta)^t e^{-n\theta}}{t!} = \theta^2 \iff \sum_{t=0}^\infty \delta(t)\frac{n^t}{t!}\theta^t = e^{n\theta}\theta^2 = \sum_{k=0}^\infty \frac{n^k}{k!}\theta^{k+2}$$
for all $\theta$. Matching coefficients of each power of $\theta$: the powers $\theta^0,\theta^1$ on the
right vanish, so $\delta(0)=\delta(1)=0$; for $t\ge 2$, matching $\theta^t$ (i.e. $k=t-2$) gives
$\delta(t) n^t/t! = n^{t-2}/(t-2)!$, i.e.
$$\delta(t) = \frac{n^{t-2}}{(t-2)!}\cdot\frac{t!}{n^t} = \frac{t(t-1)}{n^2}, \qquad \delta(T) = \frac{T(T-1)}{n^2}.$$
(For large $t$ this is close to $(T/n)^2$, the naive plug-in.)

**Method 2 (Rao-Blackwellize).** $\delta_0(X) = X_1 X_2$ is unbiased, since
$\mathbb{E}_\theta[X_1X_2] = (\mathbb{E}_\theta X_1)(\mathbb{E}_\theta X_2) = \theta^2$ by independence.
Its Rao-Blackwellization is $\delta^*(T) = \mathbb{E}[X_1X_2\mid T]$. Given $T=t$, the vector
$(X_1,\dots,X_n)$ has the standard conditional law of independent Poisson counts given their sum:
$X \mid T=t \sim \mathrm{Multinomial}(t, \tfrac1n\mathbf 1_n)$, so marginally
$X_1 \mid T=t \sim \mathrm{Binomial}(t,\tfrac1n)$, giving
$$\mathbb{E}[X_1\mid T] = \frac Tn, \qquad \mathrm{Var}(X_1\mid T) = \frac{T(n-1)}{n^2}, \qquad \mathbb{E}[X_2\mid T,X_1] = \frac{T-X_1}{n-1}$$
(the last by exchangeability of the remaining $n-1$ counts once $T$ and $X_1$ are fixed). Then
$$\mathbb{E}[X_1X_2\mid T] = \mathbb{E}\Big[X_1\,\mathbb{E}[X_2\mid T,X_1]\;\Big|\;T\Big] = \mathbb{E}\left[\frac{T}{n-1}X_1 - \frac{1}{n-1}X_1^2 \,\middle|\, T\right] = \frac{T^2}{n(n-1)} - \frac{1}{n-1}\left(\frac{T^2}{n^2}+\frac{T(n-1)}{n^2}\right) = \frac{T(T-1)}{n^2},$$
the same estimator as Method 1 — as the uniqueness part of the theorem guarantees it must be.

### Example: uniform scale

Let $X_1,\dots,X_n \stackrel{\text{iid}}{\sim} U[0,\theta]$. The maximum $T = X_{(n)}$ is complete
sufficient, with density $p_\theta^T(t) = \frac{n}{\theta^n}t^{n-1}\mathbf 1\{t\le\theta\}$, so
$$\mathbb{E}_\theta T = \int_0^\theta t\cdot\frac{n}{\theta^n}t^{n-1}\,dt = \frac{n}{n+1}\theta \implies \frac{n+1}{n}T \text{ is UMVU for } \theta.$$

Alternatively, start from the unbiased $2X_1$ (since $\mathbb{E}_\theta X_1 = \theta/2$) and
Rao-Blackwellize. Given $T=t$, $X_1$ equals $t$ with probability $1/n$ (it is the maximum) and, given
that it is not the maximum, is uniform on $[0,t]$:
$$X_1 \mid T=t \sim \begin{cases} t & \text{with probability } \tfrac1n \\ U[0,t] & \text{with probability } \tfrac{n-1}{n}\end{cases} \implies \mathbb{E}[2X_1\mid T] = 2T\cdot\frac1n + T\cdot\frac{n-1}{n} = \frac{n+1}{n}T,$$
again the same estimator.

But $\frac{n+1}{n}T$ turns out to be *inadmissible*: Keener shows that among all estimators of the
form $cT$, $\frac{n+2}{n+1}T$ has uniformly smaller MSE. Since $\frac{n+2}{n+1}T$ is biased and still
beats the UMVUE at every $\theta$, this raises the obvious question: **why insist on zero bias at
all?**

## Doubts about unbiasedness

The UMVUE can be inefficient, inadmissible, or simply a bad estimator, in situations where some
other estimator is obviously more sensible.

**Example.** Let $X \sim \mathrm{Binomial}(1000,\theta)$ and suppose the target is
$g(\theta) = \mathbb{P}_\theta(X\ge 500)$. Because $X$ itself is complete sufficient and
$\mathbf 1\{X\ge500\}$ is trivially unbiased for $g(\theta)$ (its expectation *is* $g(\theta)$, by
definition), it is the UMVUE. But then:

- observing $X=500$ forces the conclusion $g(\theta) = 100\%$,
- observing $X=499$ forces the conclusion $g(\theta) = 0\%$,

which is not an epistemically reasonable way to report a probability that changes on the strength of
one Bernoulli trial. An MLE-based estimate or a Bayes estimator does much better here.

The general moral: for *any* function $h(T)$ of the complete sufficient statistic, $h(T)$ is
automatically the UMVUE of its own expectation $g(\theta) = \mathbb{E}_\theta h(T)$. Being the UMVUE
says nothing about whether the estimator is otherwise sensible — the theorem's guarantee is real, but
narrower than it sounds.

## Example: the Gaussian sequence model

Let $X_i \stackrel{\text{iid}}{\sim} N(\mu_i,1)$ for $i=1,\dots,d$, i.e. $X\sim N_d(\mu, I_d)$, and
suppose the target is $g(\mu) = \|\mu\|^2$. Here $X$ itself is complete sufficient. Writing
$X = \mu + Z$ with $Z\sim N_d(0,I_d)$,
$$\mathbb{E}_\mu\|X\|^2 = \mathbb{E}_0\|\mu+Z\|^2 = \|\mu\|^2 + \mathbb{E}_0\|Z\|^2 + 2\mu^\top\mathbb{E}_0[Z] = \|\mu\|^2 + d,$$
so $\delta(X) = \|X\|^2 - d$ is unbiased, hence UMVU for $g(\mu)$.

But if $\mu=0$, $\|X\|^2$ is a $\chi^2_d$ random variable, so $\delta(X) = \chi^2_d - d$ is *negative
about half the time* — an obviously wrong estimate of a squared norm, which can never be negative.
Truncating,
$$(\|X\|^2-d)_+ = \max(0,\ \|X\|^2-d),$$
strictly dominates the UMVU in MSE at every $\mu$: since $g(\mu)\ge0$ always, replacing any negative
estimate with $0$ can only move it closer to the truth. The UMVUE is inadmissible.

## The pattern across the examples

Both the uniform-scale and Gaussian-sequence examples show the same thing: the UMVU estimator can be
strictly dominated by a biased one, sometimes by nothing more than a deterministic fix — rescaling by
a different constant, or truncating at zero. Completeness and sufficiency pin the UMVUE down uniquely
and make it optimal *within the class of unbiased estimators*, but that class need not contain the
best estimator overall. The lecture leaves this as an open question: unbiasedness is a restriction
chosen for its clean uniqueness theory, not one known in advance to be the right restriction.

## Sources

- Notes: `statistics/berkeley/stat210a/fall-2024/handwritten/lecture07-unbiased/01-outline.md` and
  `02-finding-the-umvue.md` — the primary source for this chapter, a model's reconstruction of a
  handwritten PDF (`handwritten/lecture07-unbiased.pdf`, fall 2024, dated 9/14/23 in the notes),
  covering convex loss, the Rao-Blackwell theorem, the UMVU theorem and its proof, the two Poisson
  derivations of the UMVUE of $\theta^2$, the uniform-scale example, the Binomial(1000,$\theta$)
  critique of unbiasedness, and the Gaussian sequence model example.
- The same lecture recurs, with an identical outline and opening sections, in
  `fall-2025/handwritten/lecture07-unbiased.md` and `fall-2026/handwritten/lecture07-unbiased.md`;
  both reconstructions cut off mid-sentence partway through the statement of the Rao-Blackwell
  theorem, adding nothing past the point where they already agree with the fall-2024 notes, and are
  not otherwise cited here.
- All four files carry the standard disclaimer that they are model reconstructions of handwritten
  PDFs with no text layer, so every displayed equation should be treated as unverified against the
  original scan. One inconsistency was resolved by the surrounding algebra: the fall-2024 notes state
  $X_1\mid T=t \sim \mathrm{Binomial}(n,1/n)$, but the subsequent formulas for $\mathbb{E}[X_1\mid T]$
  and $\mathrm{Var}(X_1\mid T)$ only match $\mathrm{Binomial}(T,1/n)$ (equivalently
  $\mathrm{Multinomial}(T,\cdot)$ rather than $\mathrm{Multinomial}(n,\cdot)$ for the full vector);
  this chapter uses the version consistent with the rest of the derivation.
- Referred to but not contained in any supplied file: Keener's result that $\frac{n+2}{n+1}T$
  minimizes MSE among estimators $cT$ of the uniform endpoint, cited by name in the fall-2024 notes
  without a specific reference.

---

[← 36. Score, Fisher Information, and CRLB (part 1)](36-score-fisher-information-and-crlb-part-1.md) · [Contents](index.md) · [38. Fisher Information and Cramér–Rao Bound →](38-fisher-information-and-cram-r-rao-bound.md)
