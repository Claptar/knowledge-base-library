---
title: "49. $p$-Values and Confidence Sets"
course: "Berkeley Stat 210A Fall 2024"
chapter: 49
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 49. $p$-Values and Confidence Sets

## What this covers

This chapter answers two connected questions that come up once a hypothesis test has been built:
what single number should summarize the evidence against a null hypothesis, and how do we turn a
family of tests into a set of plausible parameter values rather than a bare accept/reject verdict?
It assumes the machinery of the preceding lectures — a test function $\phi(X)$, a significance
level $\alpha$, and the notions of a uniformly most powerful (UMP) and uniformly most powerful
unbiased (UMPU) test — and uses them to build $p$-values, confidence sets, and the duality between
testing and confidence sets. It closes with the course's own warnings about how these objects are
routinely misread.

## The $p$-value, informally

Suppose a test rejects for large values of a statistic $T(X)$. The **$p$-value** is the null
probability of seeing a value of $T$ at least as extreme as the one actually observed:

$$p(x) = \mathbb{P}_{H_0}\big(T(X) \ge T(x)\big).$$

When the null is composite — $\theta$ ranges over a set $\Theta_0$ rather than a single point —
this is read as the worst case over the null:

$$p(x) = \sup_{\theta \in \Theta_0} \mathbb{P}_\theta\big(T(X) \ge T(x)\big).$$

Geometrically, $p(x)$ is the area under the null density of $T$ to the right of the observed value.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A null density of the test statistic T, with the tail beyond the observed value T(x) shaded as the p-value">
  <line x1="30" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 30 160 C 60 60, 90 30, 130 30 C 170 30, 195 65, 210 100 C 230 122, 260 145, 300 159" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 210 100 C 230 122, 260 145, 300 159 L 300 160 L 210 160 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="210" y1="160" x2="210" y2="100" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="210" y="176" text-anchor="middle" font-size="12" fill="currentColor">T(x)</text>
  <text x="262" y="142" text-anchor="middle" font-size="12" fill="currentColor">p-value</text>
  <text x="304" y="164" text-anchor="middle" font-size="12" fill="currentColor">T</text>
</svg>
<figcaption>The null distribution of the test statistic; the p-value is the null probability mass at or beyond the observed value T(x).</figcaption>
</figure>

**Example (one-sided binomial).** $X \sim \text{Binom}(n,\theta)$, $H_0:\theta\le 0.5$ vs.
$H_1:\theta>0.5$. The natural one-sided test rejects for large $X$, and

$$p(x) = \mathbb{P}_{0.5}(X\ge x) = \sup_{\theta\le 0.5}\mathbb{P}_\theta(X\ge x).$$

The two expressions agree because $\mathbb{P}_\theta(X\ge x)$ is non-decreasing in $\theta$ for the
binomial family, so the supremum over $\theta \le 0.5$ is attained at the boundary $\theta = 0.5$ —
the "worst case" null value is the one closest to the alternative.

**Example (two-sided normal).** $X\sim N(\theta,1)$, $H_0:\theta=0$ vs. $H_1:\theta\ne 0$. The
two-sided test rejects for large $T(X)=|X|$, i.e. $\phi(x) = \mathbf{1}\{|X|>z_{\alpha/2}\}$ where
$z_{\alpha/2}$ is the upper-$\alpha/2$ quantile of the standard normal. Its $p$-value is

$$p(x) = \mathbb{P}_0(|X|>|x|) = 2\big(1-\Phi(|x|)\big).$$

## A formal definition, and why $p$-values behave like a uniform variable

The informal definition is a special case of something more general. Suppose that for every
significance level $\alpha$ we have a valid test $\phi_\alpha$,

$$\sup_{\theta\in\Theta_0}\mathbb{E}_\theta\,\phi_\alpha(X) \le \alpha,$$

(non-randomized: $\phi_\alpha(x) = \mathbf{1}\{x\in R_\alpha\}$ for a rejection region $R_\alpha$),
and that the tests are **nested** in $\alpha$: if $\alpha_1\le\alpha_2$ then $\phi_{\alpha_1}\le
\phi_{\alpha_2}$ pointwise (non-randomized: $R_{\alpha_1}\subseteq R_{\alpha_2}$ — asking for less
evidence only ever grows the rejection region). Then define

$$p(x) = \sup\{\alpha : \phi_\alpha(x) < 1\} = \sup\{\alpha : x \notin R_\alpha\},$$

the smallest level at which the data would just start to be rejected. (One can extend this to a
randomized $p$-value to handle boundary ties, but it isn't worth the bookkeeping.)

This object has the property that makes it useful. For $\theta\in\Theta_0$,

$$\mathbb{P}_\theta\big(p(X)\le\alpha\big) = \mathbb{P}_\theta\Big(\sup\{\tilde\alpha:\phi_{\tilde\alpha}(X)<1\}\le\alpha\Big).$$

If that supremum is $\le\alpha$, then in particular $\phi_{\tilde\alpha}(X)=1$ for every fixed
$\tilde\alpha>\alpha$ (the data are already rejected at every level above $\alpha$), so the event on
the right is contained in $\{\phi_{\tilde\alpha}(X)=1\}$ for each such $\tilde\alpha$. Taking the
tightest such bound,

$$\mathbb{P}_\theta\big(p(X)\le\alpha\big) \le \inf_{\tilde\alpha>\alpha}\mathbb{P}_\theta\big(\phi_{\tilde\alpha}(X)=1\big) \le \inf_{\tilde\alpha>\alpha}\tilde\alpha = \alpha.$$

So $p(X)$ **stochastically dominates** $U[0,1]$ under every null $\theta$: it is no more likely to
fall below any threshold $\alpha$ than a uniform variable would be. This is exactly what makes
thresholding the $p$-value a valid test — "reject when $p(X)\le\alpha$" has type-I error at most
$\alpha$ by the display above — which is the point of packaging a whole nested family of tests into
one number. When $\phi_\alpha$ rejects for large $T(X)$ at an $\alpha$-dependent cutoff, this
construction reduces to the informal tail-probability definition above.

## The $p$-value depends on more than the data

A $p$-value is defined relative to three choices: the model and the null hypothesis, the observed
data, **and** the choice of test. Two valid tests of the same null, applied to the same data, can
give different $p$-values.

**Example (exponential mean).** $X\sim\text{Exp}(\theta)$ with $H_0:\theta=1$ vs. $H_1:\theta\ne1$.
Two natural two-sided tests are the *equal-tailed* test and the *UMPU* test. For an observation
$x>1$:

- Equal-tailed: $p(x) = 2\,\mathbb{P}_1(X\ge x) = 2e^{-x}$.
- UMPU: the UMPU test's rejection region at level $\alpha$ has an upper cutoff $c_2(\alpha)$ (built
  from the unbiasedness condition of the previous lecture); the UMPU $p$-value is the level $\alpha$
  at which $x$ sits exactly at that cutoff, i.e. $p(x)=\alpha$ solving $c_2(\alpha) = x$.

Because the UMPU cutoffs are not equal-tailed for an asymmetric family like the exponential, these
two numbers generally differ, even though both are legitimate $p$-values for the same null and the
same data.

**Example (sparse vs. dense signal).** $X\sim N_d(\theta, I_d)$, $H_0:\theta=0$ vs. $H_1:\theta\ne0$.
Two natural statistics are

$$T_1(X) = \|X\|^2 \quad(\chi^2\text{ test}), \qquad T_2(X) = \|X\|_\infty = \max_i|X_i| \quad(\text{max test}).$$

$T_2$ looks only at the single largest coordinate, so it is well suited to a $\theta$ concentrated
in a few large entries — a *sparse* alternative. $T_1$ sums the squared size of every coordinate, so
it is well suited to a $\theta$ spread thinly and evenly across many entries — a *dense*
alternative. For $d$ large the two tests can have very different $p$-values and very different
power on the same data, and choosing between them is a modeling choice — a belief about whether
$\theta$ is sparse — not a purely statistical one.

## From testing to confidence sets

A pure accept/reject verdict is only so informative: usually what we want to know is *how big*
$\theta$ is, and a tiny $p$-value does not imply a big effect (nor does a big $p$-value imply a
small one — that asymmetry is exactly misinterpretation 1 and 3 below). This motivates building a
whole set of plausible values instead of a single decision.

**Definition.** Given a model $\mathcal{P} = \{\mathbb{P}_\theta : \theta\in\Theta\}$ and a
functional $g(\theta)$ of interest, $C(X)$ is a $1-\alpha$ **confidence set** for $g(\theta)$ if

$$\mathbb{P}_\theta\big(C(X)\ni g(\theta)\big) \ge 1-\alpha \qquad \text{for all } \theta\in\Theta.$$

We say $C(X)$ **covers** $g(\theta)$ when $g(\theta)\in C(X)$; $\mathbb{P}_\theta(C(X)\ni g(\theta))$
is the **coverage probability** at $\theta$, and $\inf_\theta \mathbb{P}_\theta(C(X)\ni g(\theta))$
is the **confidence level**.

Two points are worth holding onto:

- $C(X)$ is the random object here, not $g(\theta)$. The parameter is a fixed, if unknown, number;
  the set varies with the data.
- The guarantee is routinely misread as a Bayesian statement. The correct phrasing is "$C(X)$ has a
  95% chance of covering $g(\theta)$" — **not** "$g(\theta)$ has a 95% chance of being in $C(X)$",
  and never, once a specific interval like $[0.5, 1.5]$ has been computed, "there is a 95% chance
  that $g(\theta)$ is in $[0.5, 1.5]$." The 95% is a property of the procedure across repeated
  samples, not of the one realized interval.

## Duality of testing and confidence sets

Every $1-\alpha$ confidence set corresponds to a family of level-$\alpha$ tests, and vice versa;
building one from the other is called **inverting the test**.

**Test $\Rightarrow$ confidence set.** Suppose that for every $a\in g(\Theta)$ we have a level-
$\alpha$ test $\phi(\cdot\,;a)$ of $H_0: g(\theta)=a$ vs. $H_1: g(\theta)\ne a$. Collect the values
that are *not* rejected:

$$C(x) = \{a : \phi(x;a) < 1\} \quad\text{— "all non-rejected values of } \theta\text{."}$$

Then for every $\theta$,

$$\mathbb{P}_\theta\big(C(X)\not\ni g(\theta)\big) = \mathbb{P}_\theta\big(\phi(X;g(\theta))=1\big) \le \alpha,$$

because $\phi(\cdot\,;g(\theta))$ is a level-$\alpha$ test of the true null $g(\theta)=g(\theta)$. So
$C(X)$ is a $1-\alpha$ confidence set for $g(\theta)$.

**Confidence set $\Rightarrow$ test.** Conversely, given a $1-\alpha$ confidence set $C(X)$, define
a test of $H_0: g(\theta)=a$ vs. $H_1: g(\theta)\ne a$ by

$$\phi(x) = \mathbf{1}\{a\notin C(x)\}.$$

If $\theta$ is such that $g(\theta)=a$ (so $H_0$ is true), then $\mathbb{E}_\theta\phi(X) =
\mathbb{P}_\theta\big(C(X)\not\ni g(\theta)\big) \le \alpha$ by the confidence guarantee, so $\phi$
is a level-$\alpha$ test.

**Example (confidence interval for the median).** Nonparametric model: $X_1,\dots,X_n\overset{iid}\sim
F$ for an arbitrary cdf $F$, and $g(F) = \text{median}(F) = F^{-1}(1/2)$ (assumed well-defined).
Test $H_0: g(F)=\mu$ ($\iff F(\mu)=1/2$) vs. $H_1: g(F)\ne\mu$ with the **two-sided sign test**:

$$S(X;\mu) = \#\{i: X_i>\mu\} \sim \text{Binom}\big(n,\, 1-F(\mu)\big),$$

which is $\text{Binom}(n,1/2)$ exactly when $H_0$ holds — and only through $F(\mu)$, so the null
distribution of $S$ doesn't depend on what $F$ actually is. Reject for $T(X;\mu) = |S(X;\mu)-n/2| >
c_\alpha$, where $c_\alpha$ comes from the $\text{Binom}(n,1/2)$ tails and does not depend on $\mu$
(e.g. $n=100$, $c_\alpha = 5$: reject if $S(x) > 55$). Inverting,

$$\mu\in C(X) \iff |S(X;\mu)-n/2|\le c_\alpha \iff \#\{X_i>\mu\}\in[n/2-c_\alpha,\, n/2+c_\alpha].$$

Since $\#\{X_i>\mu\}$ decreases in steps as $\mu$ increases, this range of counts corresponds to an
interval of $\mu$ between two order statistics:

$$\mu \in \big[X_{(n/2-c_\alpha)},\, X_{(n/2+c_\alpha)}\big] = C(X).$$

No assumption on the shape of $F$ was used — the resulting interval is distribution-free.

## Confidence intervals and bounds

If $C(X) = [c_1(x), c_2(x)]$, call $C(X)$ a **confidence interval (CI)**. If $C(X) = [c_1(x),
\infty)$, call it a **lower confidence bound (LCB)**; if $C(X) = (-\infty, c_2(x)]$, an **upper
confidence bound (UCB)**. An LCB or UCB is usually obtained by inverting a *one-sided* test in the
matching direction, and a CI by inverting a *two-sided* test.

- If the one-sided test is UMP, the resulting bound is **uniformly most accurate (UMA)**: among all
  valid $1-\alpha$ bounds, it is the one built from the test that is best able to reject false
  values — accuracy of a bound is exactly the dual of a test's power.
- If the two-sided test is UMPU, the resulting CI is **UMAU**.

**Worked example (exponential scale).** $X\sim\text{Exp}(\theta)$, density $\frac1\theta
e^{-x/\theta}$ for $x>0$, cdf $\mathbb{P}_\theta(X\le x) = 1-e^{-x/\theta}$.

*LCB.* Invert the test of $H_0:\theta\le\theta_0$ vs. $H_1:\theta>\theta_0$, which rejects for large
$X$. Solve for the critical value:

$$\alpha = \mathbb{P}_{\theta_0}\big(X > c(\theta_0)\big) = e^{-c(\theta_0)/\theta_0} \implies c(\theta_0) = \theta_0\log(1/\alpha).$$

Not rejecting means $X\le c(\theta_0)$, i.e. $\theta_0 \ge X/(-\log\alpha)$, so

$$C(X) = \left[\frac{X}{-\log\alpha},\ \infty\right).$$

*UCB.* By the mirror-image argument, inverting $H_0:\theta\ge\theta_0$ (which rejects for small
$X$) gives

$$C(X) = \left(-\infty,\ \frac{X}{-\log(1-\alpha)}\right].$$

*Equal-tailed CI.* Invert the equal-tailed test of $H_0:\theta=\theta_0$, built by combining an
$\alpha/2$-level test of each one-sided null:

$$\phi_\alpha^{\text{ET}}(X) = \phi_{\alpha/2}^{\ge\theta_0}(X) + \phi_{\alpha/2}^{\le\theta_0}(X).$$

Inverting gives the intersection of the two bounds, each built at level $\alpha/2$:

$$C(X) = \left[\frac{X}{-\log(\alpha/2)},\ \infty\right) \cap \left(-\infty,\ \frac{X}{-\log(1-\alpha/2)}\right] = \left[\frac{X}{-\log(\alpha/2)},\ \frac{X}{-\log(1-\alpha/2)}\right].$$

Inverting a UMPU two-sided test instead gives the UMAU interval for this problem by the same
mechanism, with different (non-equal-tailed) endpoints.

## Misinterpreting hypothesis tests

Hypothesis tests are ubiquitous in the sciences, and so are these errors:

1. "$p<0.05$, therefore there is an effect" — or, worse, "therefore the effect size equals the
   point estimate."
2. "$p>0.05$, therefore there is no effect."
3. "$p=10^{-6}$, therefore the effect is huge." (A tiny $p$-value reflects how confidently the null
   value is excluded, which depends on sample size as much as on effect size — recall that a tiny
   $p$-value does not imply a big $\theta$.)
4. "$p=10^{-6}$, therefore the data — and every assumption behind the model — must be correct,"
   in the most naive reading.
5. "The effect's CI for men is $[0.2, 3.2]$ and for women is $[-0.2, 2.8]$, therefore there is an
   effect for men and not for women" — even though the two intervals overlap substantially and
   no test of the difference between the groups was actually performed.

A dichotomous reject/don't-reject decision does not eliminate the underlying uncertainty; confidence
intervals are usually less misleading to a novice reader than a bare test result.

## How much a test can tell you

Learning about the world from data is not easy or automatic. A hypothesis test lets you ask a
*specific* question, about a *specific* data set, under *specific* modeling assumptions, using a
*specific* testing method — and every one of those choices bears on how the result should be read.
It is, by the course's own account, "pretty bad when you think about it" that top-tier medical
journals routinely let authors publish claims and report $p$-values without stating what model was
used or what test was employed.

A hypothesis test can be a good companion to critical thinking; it is never a substitute for it.
"All models are wrong, some are useful" — but knowing which kind of wrong is harmless takes
experience and theory, not just a $p$-value.

## Conceptual objections

**Q1. Why test $H_0:\theta=0$ at all? No $\theta$ is ever exactly zero.**

- (a) Test $H_0:|\theta|\le\delta$ instead, if that is the real concern. If the standard error of
  $\hat\theta$ is much larger than $\delta$, it won't make much practical difference which you use.
- (b) Most two-sided tests support a directional conclusion for free: "declare $\theta>0$ if
  $T>c_\alpha$, declare $\theta<0$ if $T<c_\alpha$" has probability of a false directional claim at
  most $\alpha$, even though the formal null tested was the point $\theta=0$.
- (c) This is harder to make precise in nonparametric problems — e.g. $H_0: P=Q$ vs. $H_1:P\ne Q$
  for a permutation test — but the alternative of simply going Bayesian is not free either: it
  forces a strong assumption (a full prior) onto a question the permutation test can answer with
  much less structure.

**Q2. People only like frequentist results ($p$-values, CIs) because they mistake them for
Bayesian ones** — reading "95% chance $C(X)\ni\theta$" as a statement about the posterior
$p(\theta\mid X)$.

**A2.** True as far as it goes, but subjective Bayesian results are misread just as often, as "the
posterior distribution of $\theta$" — a fact about the world — when what a subjectivist means is
"my posterior opinion about $\theta$," a personal rather than universal statement. The interpretive
sloppiness is not specific to frequentist tools.

## Sources

- [`01--values.md`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture16-F24.pdf) —
  Berkeley STAT 210A, Fall 2024, handwritten lecture 16, part 1: the $p$-value (informal and formal
  definitions, the stochastic-dominance argument, the exponential and multivariate-normal examples),
  confidence sets, the testing/confidence-set duality, and the median confidence interval.
- [`02-confidence-intervals-bounds.md`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture16-F24.pdf) —
  same lecture, part 2: CI/LCB/UCB definitions, UMA/UMAU, the exponential worked example, and the
  discussion of (mis-)interpreting hypothesis tests, including the conceptual objections.
- Both files are marked in their front matter as reconstructed by a model from a handwritten PDF
  with no text layer (CC BY 4.0, converted 2026-09-18); every equation in them is flagged
  unverified against the original, and this chapter inherits that caveat.
- No slide deck, transcript, or problem set was supplied for this lecture. The notes assume, without
  restating, earlier lectures on test functions, significance levels, and UMP/UMPU testing — in
  particular the UMPU cutoffs used in the exponential $p$-value example and the tests inverted to
  build the UMA/UMAU bounds — which are not included here.

---

[← 48. Testing with one real parameter](48-testing-with-one-real-parameter.md) · [Contents](index.md) · [50. P-Values and Confidence Sets →](50-p-values-and-confidence-sets.md)
