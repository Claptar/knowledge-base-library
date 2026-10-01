---
title: "84. Unbiased Estimation"
course: "Berkeley Stat 210A"
chapter: 84
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 84. Unbiased Estimation

## What this covers

Given a decision problem, restricting attention to *unbiased* estimators is one way to narrow the
search for a good one — the alternative, from the previous lecture, is to summarize the whole risk
function by a single number (its average or its worst case). This chapter asks when that
restriction actually pins down a single best estimator, and how to find it. It assumes the
risk/loss framework — a loss function $L(\theta,d)$ and risk $R(\theta,\delta) = \mathbb{E}_\theta
L(\theta,\delta(X))$ — together with sufficiency and completeness of a statistic $T(X)$, all
developed earlier in the course. It ends by asking whether insisting on zero bias is even a good
idea.

## Unbiased estimation as a way to narrow the search

Recall the two general strategies for choosing an estimator when no single $\delta$ minimizes the
risk $R(\theta,\delta)$ at every $\theta$: summarize the risk function by a scalar (its average,
giving a Bayes estimator, or its supremum, giving a minimax one), or restrict attention to a
smaller class of estimators within which comparisons become possible. Unbiased estimation is an
instance of the second strategy: given an estimand $g(\theta)$, we require

$$\mathbb{E}_\theta\, \delta(X) = g(\theta) \quad \text{for all } \theta.$$

This restriction is especially productive when the model has a **complete sufficient statistic**
$T(X)$. In that case, two things happen, both justified below:

- there is at most one unbiased estimator of the form $\delta(T(X))$ — if $\delta_1(T)$ and
  $\delta_2(T)$ are both unbiased, they agree almost surely;
- if an unbiased estimator exists at all, that unique one **uniformly minimizes risk** among *all*
  estimators (not only unbiased ones), for every convex loss function.

The rest of the chapter fills in why.

## Convex loss functions

A function $f$ is **convex** if for all $x_1, x_2$ and $\gamma \in [0,1]$,

$$f(\gamma x_1 + (1-\gamma)x_2) \le \gamma f(x_1) + (1-\gamma) f(x_2),$$

and **strictly convex** if the inequality is strict whenever $x_1 \neq x_2$. Geometrically, the
graph of $f$ lies on or below every chord joining two of its points.

**Jensen's inequality** extends this from finite mixtures to any distribution: if $f$ is convex,
then for any random variable $X$,

$$f(\mathbb{E}[X]) \le \mathbb{E}[f(X)],$$

with strict inequality (when $f$ is strictly convex) unless $X$ is constant.

<figure>
<svg viewBox="0 0 320 230" role="img" aria-label="A convex curve lying below the chord joining two of its points, with the gap between f at the mean and the mean of f marked">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="50" y1="210" x2="270" y2="210" stroke="currentColor" stroke-width="1.2"/>
  <line x1="70" y1="40" x2="250" y2="40" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <polyline points="70,40 90,99.3 110,143.7 130,173.3 150,188.2 160,190 170,188.2 190,173.3 210,143.7 230,99.3 250,40"
            fill="none" stroke="currentColor" stroke-width="1.8"/>
  <line x1="145" y1="190" x2="145" y2="45" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="70" y1="210" x2="70" y2="214" stroke="currentColor" stroke-width="1.2"/>
  <line x1="160" y1="210" x2="160" y2="214" stroke="currentColor" stroke-width="1.2"/>
  <line x1="250" y1="210" x2="250" y2="214" stroke="currentColor" stroke-width="1.2"/>
  <circle cx="70" cy="40" r="2.3" fill="currentColor"/>
  <circle cx="250" cy="40" r="2.3" fill="currentColor"/>
  <circle cx="160" cy="190" r="2.3" fill="currentColor"/>
  <text x="70" y="224" text-anchor="middle" font-size="12" fill="currentColor">a</text>
  <text x="160" y="224" text-anchor="middle" font-size="12" fill="currentColor">m = E[X]</text>
  <text x="250" y="224" text-anchor="middle" font-size="12" fill="currentColor">b</text>
  <text x="55" y="52" text-anchor="end" font-size="12" fill="currentColor">f</text>
  <text x="200" y="185" text-anchor="start" font-size="12" fill="currentColor">f(E[X])</text>
  <text x="200" y="35" text-anchor="start" font-size="12" fill="currentColor">E[f(X)]</text>
</svg>
<figcaption>A convex function lies below the chord joining any two of its points, and in
particular below the chord's height at the mean — the gap between the curve and the chord at
$m = \mathbb{E}[X]$ is exactly the Jensen's-inequality gap, $\mathbb{E}[f(X)] - f(\mathbb{E}[X])$,
that Rao-Blackwellization exploits.</figcaption>
</figure>

We call a loss function $L(\theta, d)$ **(strictly) convex** if it is (strictly) convex as a
function of the estimate $d$ — its second argument — for each fixed $\theta$. Convexity in $\theta$
plays no role here; $\theta$ only indexes the model.

**Example.** The best-known convex loss is squared error. The corresponding risk, the MSE,
decomposes as

$$\mathrm{MSE}_\theta(\delta) = \mathbb{E}_\theta\big[(\delta(X) - g(\theta))^2\big]
= \mathrm{Bias}_\theta(\delta)^2 + \mathrm{Var}_\theta(\delta(X)).$$

If $\delta$ is unbiased, its MSE is exactly its variance — so among unbiased estimators, minimizing
risk under squared error is exactly finding the one with least variance.

## The Rao–Blackwell theorem

Convex losses punish noise: replacing $\delta(X)$ by its expectation would always help, since by
Jensen

$$L\big(\theta,\, \mathbb{E}_\theta[\delta(X)]\big) \le \mathbb{E}_\theta\big[L(\theta, \delta(X))\big].$$

The trouble is that $\mathbb{E}_\theta[\delta(X)]$ depends on the unknown $\theta$, so it is not
itself an estimator. But if $T(X)$ is *sufficient*, the conditional expectation of $\delta(X)$
given $T(X)$ does not depend on $\theta$ — it really is an estimator — and it is always at least as
good as $\delta(X)$ whenever the loss is convex.

**Theorem (Rao–Blackwell).** Let $T(X)$ be sufficient for $\mathcal{P} = \{P_\theta : \theta \in
\Theta\}$, and let $\delta(X)$ be any estimator of $g(\theta)$. Define

$$\bar\delta(T(X)) = \mathbb{E}[\delta(X) \mid T(X)].$$

Then for any convex loss $L(\theta,d)$, $R(\theta,\bar\delta) \le R(\theta,\delta)$ for every
$\theta$. If $L$ is strictly convex, $\bar\delta$ strictly dominates $\delta$ unless $\delta(X)$
already equals $\bar\delta(T(X))$ almost surely — equivalently, unless $\delta$ already depends on
$X$ only through $T(X)$.

*Proof.* Condition on $T(X)$ and apply Jensen's inequality to the conditional distribution of
$\delta(X)$ given $T(X)$:

$$L\big(\theta, \bar\delta(T(X))\big) = L\big(\theta, \mathbb{E}[\delta(X)\mid T(X)]\big)
\le \mathbb{E}\big[L(\theta,\delta(X)) \mid T(X)\big].$$

Taking expectations over $T(X)$ (marginalizing) gives $R(\theta,\bar\delta) \le R(\theta,\delta)$.
If $L$ is strictly convex, the Jensen step is strict unless the conditional distribution of
$\delta(X)$ given $T(X)$ is degenerate, i.e. unless $\delta(X) = \delta(T(X))$ almost surely.
$\blacksquare$

$\bar\delta$ is called the **Rao-Blackwellization** of $\delta$. The theorem does more than assert
that an improvement exists — it hands you a recipe for building it: condition on the sufficient
statistic. And it licenses a real simplification: whenever the loss is convex, attention can be
restricted entirely to estimators that are functions of $T(X)$, since any other estimator is
improved (or at worst left unchanged) by Rao-Blackwellizing it.

## UMVU estimators

Two facts now combine. Completeness of $T(X)$ forces *uniqueness*: there is at most one unbiased
$\delta(T(X))$. Rao–Blackwell forces *universality*: for a convex loss, only estimators that are
functions of $T(X)$ need be considered at all. Together, whenever an unbiased estimator exists,
there is a single best unbiased estimator.

Call $g(\theta)$ **U-estimable** if some $\delta(X)$ satisfies $\mathbb{E}_\theta \delta(X) =
g(\theta)$ for all $\theta$.

**Theorem.** Suppose $T(X)$ is complete sufficient for $\mathcal{P} = \{P_\theta : \theta \in
\Theta\}$. Then:

1. for any U-estimable $g(\theta)$, there is a unique (almost sure) unbiased estimator of the form
   $\delta(T(X))$;
2. for any (strictly) convex loss, that estimator (strictly) dominates every other unbiased
   estimator $\tilde\delta(X)$, unless $\tilde\delta(X)$ already equals $\delta(T(X))$ almost
   surely.

*Proof.* (1) Since $g$ is U-estimable, some unbiased $\delta_0(X)$ exists. Its Rao-Blackwellization
$\delta(T) = \mathbb{E}[\delta_0 \mid T]$ is unbiased too, since $\mathbb{E}_\theta\, \delta(T) =
\mathbb{E}_\theta[\mathbb{E}[\delta_0 \mid T]] = \mathbb{E}_\theta\, \delta_0 = g(\theta)$. If
$\tilde\delta(T)$ is another unbiased estimator based on $T$, then $f(t) = \delta(t) -
\tilde\delta(t)$ satisfies $\mathbb{E}_\theta f(T) = 0$ for all $\theta$, so completeness forces
$f(T) = 0$ almost surely: $\delta(T)$ is unique.

(2) By (1), every unbiased estimator has the same Rao-Blackwellization $\delta(T)$. Rao–Blackwell
then says $\delta(T)$ (strictly) dominates every unbiased $\tilde\delta(X)$ for any (strictly)
convex loss, unless $\tilde\delta$ already coincides with $\delta$ almost surely. $\blacksquare$

The estimator produced by this theorem is the **UMVU (Uniformly Minimum Variance Unbiased)
estimator**: $\delta(X)$ is UMVU if it is unbiased and $\mathrm{Var}_\theta\,\delta(X) \le
\mathrm{Var}_\theta\,\tilde\delta(X)$ for every $\theta$ and every unbiased $\tilde\delta$. Since
squared error is strictly convex and, for unbiased estimators, $\mathrm{MSE} = \mathrm{Var}$, the
theorem immediately gives a unique UMVUE for any U-estimable $g(\theta)$ whenever a complete
sufficient statistic exists.

Completeness is doing real work here. Without it — working only with a *minimal* but not complete
sufficient statistic — there can be several unbiased estimators that are not almost-surely equal
and do not share a risk function. The stock example: for the Laplace location parameter, both the
sample mean and the sample median are unbiased, but they are genuinely different estimators with
different risk functions.

## Finding the UMVUE

The theorem suggests two strategies:

1. solve directly for the unbiased function of $T$, by matching $\mathbb{E}_\theta\,\delta(T) =
   g(\theta)$;
2. find *any* unbiased estimator at all, then Rao-Blackwellize it.

### Example: estimating $\theta^2$ from a Poisson sample

Let $X_1, \dots, X_n \sim \mathrm{Pois}(\theta)$ and consider unbiased estimation of $g(\theta) =
\theta^2$. The complete sufficient statistic is $T = \sum_i X_i \sim \mathrm{Pois}(n\theta)$, with
mass function $p_\theta(t) = e^{-n\theta}(n\theta)^t / t!$.

**Strategy 1.** Set the expectation of a candidate $\delta(T)$ equal to $\theta^2$ and match power
series:

$$\theta^2 = \mathbb{E}_\theta\,\delta(T) = \sum_{t=0}^\infty \delta(t)\,\frac{e^{-n\theta}
(n\theta)^t}{t!} \quad\Longrightarrow\quad \sum_{t=0}^\infty \delta(t)\frac{n^t\theta^t}{t!} =
e^{n\theta}\theta^2 = \sum_{t=2}^\infty \frac{n^{t-2}\theta^t}{(t-2)!},$$

after re-indexing the right-hand series by $t = k+2$. Matching coefficients term by term forces
$\delta(0) = \delta(1) = 0$ and, for $t \ge 2$, $\delta(t) = t!/\big(n^2(t-2)!\big) = t(t-1)/n^2$.
So

$$\delta(T) = \frac{T(T-1)}{n^2}.$$

**Strategy 2.** Start from an easy unbiased estimator, $\delta_0(X) = X_1X_2$ — unbiased because
$\mathbb{E}_\theta[X_1X_2] = \mathbb{E}_\theta[X_1]\,\mathbb{E}_\theta[X_2] = \theta^2$ by
independence (this needs $n \ge 2$) — and Rao-Blackwellize it. Conditional on $T=t$,
$(X_1,\dots,X_n)$ is multinomial$(t, \frac1n \mathbf{1}_n)$, so $X_1 \mid T=t \sim
\mathrm{Binom}(t, \frac1n)$; conditional further on $X_1 = x_1$, $(X_2,\dots,X_n) \mid T=t, X_1=x_1$
is multinomial$(t-x_1, \frac{1}{n-1}\mathbf{1}_{n-1})$, so $X_2 \mid T=t, X_1=x_1 \sim
\mathrm{Binom}(t-x_1, \frac{1}{n-1})$ with mean $(t-x_1)/(n-1)$. Nesting these conditional
expectations,

$$\mathbb{E}[X_1X_2 \mid T] = \mathbb{E}\Big[X_1\cdot\frac{T-X_1}{n-1}\;\Big|\;T\Big]
= \frac{1}{n-1}\left(\frac{T^2}{n} - \frac{T(n-1)}{n^2} - \frac{T^2}{n^2}\right)
= \frac{T(T-1)}{n^2},$$

the same estimator, as the theory guarantees it must be.

### Example: the maximum of a uniform sample

Let $X_1,\dots,X_n \sim \mathrm{Unif}[0,\theta]$. The complete sufficient statistic is $T =
X_{(n)}$, with density $p_\theta(t) = n t^{n-1}/\theta^n$ on $(0,\theta)$.

**Strategy 1.** $T/\theta \sim \mathrm{Beta}(n,1)$, with mean $n/(n+1)$, so $\mathbb{E}_\theta[T] =
\frac{n}{n+1}\theta$ and $\frac{n+1}{n}T$ is unbiased, hence UMVU.

**Strategy 2.** Alternatively, $2X_1$ is unbiased ($\mathbb{E}[X_1] = \theta/2$); Rao-Blackwellizing
it means finding $\mathbb{E}[X_1 \mid T=t]$. Write $I^*(X)$ for the index attaining the maximum.
Conditional on $T=t$ and $I^*=1$, $X_1 = t$ deterministically; conditional on $T=t$ and $I^* \ne 1$,
the coordinates other than the maximizer (including $X_1$) are i.i.d. uniform on $[0,t]$, so
$\mathbb{E}[X_1 \mid T=t, I^*\ne 1] = t/2$. Since the data are exchangeable, $I^*$ is independent of
$T$ and uniform on $\{1,\dots,n\}$ (also a consequence of Basu's theorem), so $I^*=1$ with
probability $1/n$, giving

$$\mathbb{E}[X_1 \mid T=t] = \frac1n\cdot t + \frac{n-1}{n}\cdot\frac t2 = \frac{t(n+1)}{2n},
\qquad \mathbb{E}[2X_1 \mid T] = \frac{n+1}{n}T,$$

again the same estimator.

### A better, biased estimator

This UMVUE is nonetheless *inadmissible*. For any estimator $cT$, writing MSE as squared bias plus
variance and using $\mathrm{Var}_\theta(T/\theta) = n/\big((n+1)^2(n+2)\big)$ (the Beta$(n,1)$
variance),

$$\mathrm{MSE}(\theta; cT) = (\mathbb{E}_\theta[cT] - \theta)^2 + \mathrm{Var}_\theta(cT)
= \theta^2\left[\Big(\frac{cn}{n+1} - 1\Big)^2 + \frac{c^2 n}{(n+1)^2(n+2)}\right].$$

This is a quadratic in $c$, minimized at $c^\star = \frac{n+2}{n+1}$. So $\frac{n+2}{n+1}T$ has
strictly lower MSE than the UMVUE $\frac{n+1}{n}T$ *for every* $\theta$ — even though it is biased.
Requiring zero bias, in this problem, rules out every admissible estimator, and leaves us with the
best of the inadmissible ones.

## Doubts about unbiasedness

That last example raises the obvious question: why insist on zero bias at all? There are real
reasons to want it — an estimator that is "correct on average" is a comfortable thing to defend,
especially when the estimand is contested. But the constraint should not be treated as sacred: it
can make the UMVUE inadmissible, or outright absurd.

**Example.** Let $X \sim N_d(\mu, I_d)$ and consider estimating $g(\mu) = \|\mu\|^2$. Writing
$X = \mu + Z$ with $Z \sim N_d(0,I_d)$,

$$\mathbb{E}_\mu\|X\|^2 = \sum_j \mathbb{E}(Z_j+\mu_j)^2 = \|\mu\|^2 + d,$$

since the cross terms vanish and $\mathbb{E}Z_j^2 = 1$. So $\|X\|^2$ has bias $d$, and $\delta(X) =
\|X\|^2 - d$ is unbiased — and, since $X$ is complete sufficient, UMVU. But $\delta$ can be
negative: if $d=10$ and $\|X\|^2=5$, which certainly can happen, it estimates $-5$ for a quantity
that is by definition non-negative. It is also inadmissible for essentially any reasonable loss:
replacing $\delta$ by $\delta_+ = (\|X\|^2 - d)_+$ can only move the estimate closer to the
(non-negative) truth, so $\delta_+$ strictly dominates $\delta$.

**Example.** Let $X \sim \mathrm{Bin}(1000,\theta)$ and consider estimating $g(\theta) =
\mathbb{P}_\theta(X \ge 500)$. Since $X$ is complete sufficient, the only unbiased estimator — the
indicator $\mathbf{1}\{X \ge 500\}$ of whether the event actually happened — is *the* UMVUE. But it
is absurd: seeing $X=499$ would have us declare that repeating the experiment could never produce
$500$ or more successes. A sensible plug-in estimator, $\mathbb{P}_{\hat\theta}(X \ge 500)$ for a
reasonable $\hat\theta$ such as $X/n$, increases gradually with $X$ — but it cannot be unbiased,
because every unbiased estimator is dominated by the (unique) UMVUE.

No statistical paradigm escapes looking foolish on some example. As the course returns to later, in
the Gaussian location problem above, even the maximum likelihood estimator and the Bayes estimator
under the "objective" Jeffreys prior do worse than the UMVUE. Choosing which paradigm fits a given
problem, rather than trusting one universally, is a large part of what applied statistics is.

## Sources

All of the material above is from the Berkeley STAT210A course reader, "Unbiased Estimation"
chapter, converted to markdown in the library. The course reader was taught (with minor revisions)
across several offerings; this chapter follows the fall-2026 text as primary, cross-checked against
fall-2025 where the two differ only in wording:

- Convex loss functions, Jensen's inequality, and the squared-error example —
  `docs/statistics/berkeley/stat210a/fall-2026/reader/unbiased-estimation/01-convex-loss-functions.md`
  (cf. `.../fall-2025/reader/unbiased-estimation/01-introduction.md` and
  `.../fall-2025/reader/unbiased-estimation/02-2-convex-loss-functions.md`, split into two files
  there).
- The Rao–Blackwell theorem and its proof —
  `docs/statistics/berkeley/stat210a/fall-2026/reader/unbiased-estimation/02-the-rao-blackwell-theorem.md`
  (cf. `.../fall-2025/reader/unbiased-estimation/03-3-the-rao-blackwell-theorem.md`).
- UMVU estimators, U-estimability, and the Laplace mean-vs-median remark —
  `docs/statistics/berkeley/stat210a/fall-2026/reader/unbiased-estimation/03-umvu-estimators.md`
  (cf. `.../fall-2025/reader/unbiased-estimation/04-4-umvu-estimators.md`).
- Finding the UMVUE (Poisson $\theta^2$ example, uniform-maximum example, and the biased-but-better
  estimator) —
  `docs/statistics/berkeley/stat210a/fall-2026/reader/unbiased-estimation/04-finding-the-umvue.md`
  (cf. `.../fall-2025/reader/unbiased-estimation/05-5-finding-the-umvue.md`, which has the same
  content and fixes the same typo as fall-2026 relative to fall-2024).
- Doubts about unbiasedness (Gaussian norm-squared and Binomial threshold examples) —
  `docs/statistics/berkeley/stat210a/fall-2026/reader/unbiased-estimation/05-doubts-about-unbiasedness.md`
  and `.../06-expand-for-answer.md` (cf.
  `.../fall-2025/reader/unbiased-estimation/06-6-doubts-about-unbiasedness.md`, where the same two
  parts appear as one continuous section).

The fall-2024 offering of this same reader chapter
(`docs/statistics/berkeley/stat210a/fall-2024/reader/unbiased-estimation/`) is an earlier,
explicitly "under construction" draft: its Rao–Blackwell proof ends in a typo ($R(\theta,\bar\delta)
= \dots = R(\theta,\bar\delta)$ rather than $R(\theta,\delta)$) and its "Finding the UMVUE" section
breaks off mid-derivation before the Poisson Strategy-2 calculation and the "better estimator"
discussion. It was consulted but not used as a source, since fall-2025/fall-2026 give the same
material complete and correct. The duplicate copy under
`docs/statistics/berkeley/stat210a/fall-2025/units/reader/unbiased-estimation/` mirrors
`fall-2025/reader/` section-for-section and was likewise not used separately.

No slides or lecture transcript were supplied for this chapter, and no exercises were supplied. The
reader text refers to "Lecture 2" for the two general strategies of choosing an estimator
(summarizing the risk vs. restricting the estimator class); that lecture itself was not part of the
supplied material.

---

[← 83. Testing With One Real Parameter](83-testing-with-one-real-parameter.md) · [Contents](index.md)
