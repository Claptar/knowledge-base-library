---
title: "50. P-Values and Confidence Sets"
course: "Berkeley Stat 210A Fall 2024"
chapter: 50
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 50. P-Values and Confidence Sets

## What this covers

A test tells you whether to reject $H_0$ at a chosen level $\alpha$; it does not tell you how extreme
the data are, or how big the parameter is. This chapter builds the two objects that answer those
questions. The $p$-value is defined precisely enough to make sense even for tests that don't simply
reject on "large $T(X)$" — the interesting case, since most useful two-sided tests don't — and two
facts about it are proved: it collapses to the familiar tail-probability formula when it can, and
under the null it is never below $\alpha$ more than $\alpha$ of the time. The confidence set is then
shown to be the *same* object as a family of tests, just read the other way: "invert" one and you get
the other for free. The chapter closes with the standard warnings against the ways both objects get
misread. It assumes the testing machinery already built in the course: a test function $\phi$, a
significance level $\alpha$, a null parameter space $\Theta_0$ and alternative $\Theta_1$, and the
notions of UMP and UMPU tests.

## The $p$-value, informally

Suppose $\phi(x)$ rejects for large values of a statistic $T(X)$. The $p$-value is meant to capture

$$
p(x) = \text{"the null probability that } T(X) \text{ is at least as extreme as what we observed"} = \sup_{\theta \in \Theta_0} \mathbb{P}_\theta\big(T(X) \ge T(x)\big).
$$

The sup over $\Theta_0$ is there because the null is typically composite; when $\Theta_0$ is a single
point it is just $\mathbb{P}_{\theta_0}(T(X) \ge T(x))$.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A null distribution density with the tail beyond the observed statistic shaded as the p-value">
  <line x1="30" y1="170" x2="310" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <path d="M230,140.1 L235,146.8 L240,152.4 L245,156.9 L250,160.5 L255,163.2 L260,165.2 L265,166.7 L270,167.8 L275,168.6 L280,169.1 L285,169.4 L290,169.6 L295,169.8 L300,169.9 L300,170 L230,170 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M40,169.9 L45,169.8 L50,169.6 L55,169.4 L60,169.1 L65,168.6 L70,167.8 L75,166.7 L80,165.2 L85,163.2 L90,160.5 L95,156.9 L100,152.4 L105,146.8 L110,140.1 L115,132.2 L120,123.1 L125,113.1 L130,102.3 L135,91.2 L140,80.0 L145,69.3 L150,59.6 L155,51.4 L160,45.2 L165,41.3 L170,40.0 L175,41.3 L180,45.2 L185,51.4 L190,59.6 L195,69.3 L200,80.0 L205,91.2 L210,102.3 L215,113.1 L220,123.1 L225,132.2 L230,140.1 L235,146.8 L240,152.4 L245,156.9 L250,160.5 L255,163.2 L260,165.2 L265,166.7 L270,167.8 L275,168.6 L280,169.1 L285,169.4 L290,169.6 L295,169.8 L300,169.9" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="230" y1="170" x2="230" y2="140.1" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="230" y="185" text-anchor="middle" font-size="12" fill="currentColor">T(x) (observed)</text>
  <text x="272" y="120" text-anchor="middle" font-size="12" fill="currentColor">p-value</text>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">distribution of T(X) under the null</text>
</svg>
<figcaption>The shaded tail past the observed value of the test statistic is the p-value: how much of the null
distribution lies at or beyond what was actually seen.</figcaption>
</figure>

**Example (one-sided binomial).** $X \sim \mathrm{Binom}(n,\theta)$, $H_0: \theta \le 0.5$ vs.
$H_1: \theta > 0.5$. The one-sided test rejects for large $X$, and

$$
p(x) = \mathbb{P}_{0.5}(X \ge x) = \sup_{\theta \le 0.5} \mathbb{P}_\theta(X \ge x),
$$

the sup being attained at $\theta = 0.5$ since larger $\theta$ makes $X$ stochastically larger.

**Example (two-sided normal).** $X \sim N(\theta,1)$, $H_0:\theta=0$ vs. $H_1:\theta\ne0$. The
two-sided test rejects for large $T(X)=|X|$, i.e. $\phi(x) = \mathbf{1}\{|X| > z_{\alpha/2}\}$, and

$$
p(x) = \mathbb{P}_0(|X| > |x|) = 2\big(1-\Phi(|x|)\big).
$$

## A definition that survives tests that don't reject on "large $T$"

Not every test rejects on large values of a single statistic — the UMPU two-sided test for many
problems does not, since its rejection region is typically two disjoint pieces with *different*
cutoffs on either side. So the tail-probability formula above needs a definition that doesn't
presuppose "large $T$."

Suppose we have, for every level $\alpha \in (0,1)$, a test $\phi_\alpha$ with
$\sup_{\theta \in \Theta_0} \mathbb{E}_\theta \phi_\alpha(X) \le \alpha$ (non-randomized:
$\phi_\alpha = \mathbf{1}\{x \in R_\alpha\}$), and suppose the family is **monotone in $\alpha$**: if
$\alpha_1 \le \alpha_2$ then $\phi_{\alpha_1}(x) \le \phi_{\alpha_2}(x)$ for every $x$ (non-randomized:
$R_{\alpha_1} \subseteq R_{\alpha_2}$ — a looser level can only reject more). Then define

$$
p(x) = \sup\{\alpha : \phi_\alpha(x) < 1\} = \inf\{\alpha : \phi_\alpha(x) = 1\},
$$

the borderline level at which $x$ tips from "not rejected" to "rejected." (A randomized version of
$p$ can be defined but isn't worth the bookkeeping.)

**Proposition.** If $\phi_\alpha$ rejects on large values of $T(x)$, using the *tightest* possible
cutoffs

$$
c_\alpha = \min\Big\{c : \sup_{\theta \in \Theta_0} \mathbb{P}_\theta(T > c) \le \alpha\Big\},
$$

then this general definition reduces to the naive one: $p(x) = \sup_{\theta \in \Theta_0} \mathbb{P}_\theta(T(X) \ge T(x))$.

*Proof.* Write $p_1(x) = \sup_{\theta \in \Theta_0} \mathbb{P}_\theta(T(X) \ge T(x))$ for the naive
definition and $p_2(x) = \sup\{\alpha : \phi_\alpha(x) < 1\}$ for the general one. Fix $\alpha$. Then

$$
p_1(x) > \alpha \iff \mathbb{P}_\theta(T(X) \ge T(x)) > \alpha \text{ for some } \theta \in \Theta_0.
$$

By the definition of $c_\alpha$ as the tightest cutoff with $\sup_\theta \mathbb{P}_\theta(T > c_\alpha) \le \alpha$,
this happens exactly when $T(x) < c_\alpha$, or $T(x) = c_\alpha$ and the randomization probability
$\gamma_\alpha$ needed at the boundary to hit level $\alpha$ exactly is less than $1$ — and that is
precisely the condition under which $\phi_\alpha$ does not reject $x$ outright, i.e. $\phi_\alpha(x) < 1$.
So $\{\alpha : p_1(x) > \alpha\} = \{\alpha : \phi_\alpha(x) < 1\}$, and taking suprema of both sides
gives $p_2(x) = p_1(x)$. $\blacksquare$

## $p$-values are super-uniform under the null

**Proposition.** For every $\theta \in \Theta_0$, $\mathbb{P}_\theta(p(X) \le \alpha) \le \alpha$.

Equivalently, under the null the $p$-value **stochastically dominates** $\mathrm{Unif}[0,1]$ — it is
never *more* likely to fall below $\alpha$ than a uniform variable would be, which is exactly the
property that makes "reject when $p(X) \le \alpha$" a level-$\alpha$ test.

*Proof.* By monotonicity of $\alpha \mapsto \phi_\alpha(x)$,

$$
p(x) \le \alpha \iff \phi_{\alpha+\varepsilon}(x) = 1 \text{ for every } \varepsilon > 0.
$$

The events $\{\phi_{\alpha+\varepsilon}(X) = 1\}$ shrink as $\varepsilon \downarrow 0$ (monotonicity
again: a larger $\varepsilon$ only rejects more), so by continuity of probability,

$$
\mathbb{P}_\theta\big(p(X) \le \alpha\big) = \mathbb{P}_\theta\Big(\bigcap_{\varepsilon>0} \{\phi_{\alpha+\varepsilon}(X)=1\}\Big) = \lim_{\varepsilon \downarrow 0} \mathbb{P}_\theta\big(\phi_{\alpha+\varepsilon}(X) = 1\big) \le \lim_{\varepsilon \downarrow 0} \mathbb{E}_\theta \phi_{\alpha+\varepsilon}(X) \le \lim_{\varepsilon \downarrow 0} (\alpha + \varepsilon) = \alpha,
$$

where the last inequality uses that $\phi_{\alpha+\varepsilon}$ has level at most $\alpha+\varepsilon$
by assumption. $\blacksquare$

If $\phi_\alpha$ rejects on large $T(X)$, this is exactly the naive definition, so the naive
tail-probability $p$-value is super-uniform too.

## A $p$-value depends on more than the data and the hypotheses

The $p$-value is defined relative to **the model and the null**, **the data**, *and* **the choice of
test** — and different reasonable choices of test genuinely disagree.

**Example.** $X \sim \mathrm{Exp}(\theta)$, $H_0: \theta = 1$ vs. $H_1: \theta \ne 1$. Two natural
two-sided tests are the equal-tailed test and the UMPU test. For $x > 1$:

$$
\text{equal-tailed: } p(x) = 2\,\mathbb{P}_1(X \ge x) = 2e^{-x}, \qquad \text{UMPU: } p(x) = \alpha \text{ for which } c_2(\alpha) = x,
$$

where $c_2(\alpha)$ is the upper cutoff of the UMPU rejection region (built earlier in the course);
the two formulas give different numbers for the same $x$.

**Example.** $X \sim N_d(\theta, I_d)$, $H_0: \theta = 0$ vs. $H_1: \theta \ne 0$. Two natural
statistics are

$$
T_1(X) = \|X\|^2 \quad (\chi^2\text{ test}), \qquad T_2(X) = \|X\|_\infty = \max_i |X_i| \quad (\text{max test}).
$$

For large $d$ these give very different $p$-values and very different power, depending on whether
the true $\theta$ is spread across all $d$ coordinates or concentrated ("sparse") in a few — the
choice of statistic is implicitly a choice about which alternative you expect.

## Confidence sets

An accept/reject decision is only so interesting by itself: usually the real question is *how big*
$\theta$ is, and a tiny $p$-value doesn't imply a big effect (nor does a big $p$-value imply a small
one). A confidence set answers the question a test can't.

Let $\mathcal{P} = \{\mathbb{P}_\theta : \theta \in \Theta\}$. $C(X)$ is a **$1-\alpha$ confidence set**
for $g(\theta)$ if

$$
\mathbb{P}_\theta\big(C(X) \ni g(\theta)\big) \ge 1 - \alpha \qquad \forall\, \theta \in \Theta.
$$

We say $C(X)$ **covers** $g(\theta)$ when $C(X) \ni g(\theta)$; $\mathbb{P}_\theta(C(X) \ni g(\theta))$
is the **coverage probability**, and $\inf_\theta \mathbb{P}_\theta(C(X) \ni g(\theta))$ is the
**confidence level**.

A few things worth being careful about:

- $C(X)$ is the random object here, not $g(\theta)$ — the randomness in the statement is entirely in
  where the interval lands, not in the fixed (if unknown) parameter.
- The guarantee is routinely misread as a Bayesian one. Say **"$C(X)$ has a 95% chance of covering
  $g(\theta)$,"** not "$g(\theta)$ has a 95% chance of being in $C$," and never, for a specific
  realized interval, "there is a 95% chance that $g(\theta) \in [0.5, 1.5]$." Once $X$ is observed
  and $C(X) = [0.5,1.5]$ is a fixed set, $g(\theta)$ either is or isn't in it — the 95% describes the
  procedure, not that particular interval.

## Duality: a test and a confidence set are the same object

Suppose that for every $a \in g(\Theta)$ we have a level-$\alpha$ test $\phi(x;a)$ of
$H_0: g(\theta) = a$ vs. $H_1: g(\theta) \ne a$. Define

$$
C(X) = \{a : \phi(X;a) < 1\} = \text{"all values of } a \text{ not rejected by the data."}
$$

Then for every $\theta$,

$$
\mathbb{P}_\theta\big(C(X) \not\ni g(\theta)\big) = \mathbb{P}_\theta\big(\phi(X; g(\theta)) = 1\big) \le \alpha,
$$

since $\phi(\cdot; g(\theta))$ is a level-$\alpha$ test of the (true) null $g(\theta) = g(\theta)$. So
$C(X)$ is a $1-\alpha$ confidence set for $g(\theta)$.

Conversely, given a $1-\alpha$ confidence set $C(X)$, build a test of $H_0: g(\theta) = a$ vs.
$H_1: g(\theta) \ne a$ by

$$
\phi(X) = \mathbf{1}\{a \notin C(X)\}.
$$

For any $\theta$ with $g(\theta) = a$,

$$
\mathbb{E}_\theta \phi(X) = \mathbb{P}_\theta\big(C(X) \not\ni g(\theta)\big) \le \alpha,
$$

so $\phi$ has level $\alpha$. Going from a family of tests to a confidence set, or back, is called
**inverting** the test (or the confidence set) — they carry exactly the same information.

## Confidence intervals, bounds, and their optimality names

- $C(X) = [C_1(X), C_2(X)]$: a **confidence interval (CI)**.
- $C(X) = [C_1(X), \infty)$: a **lower confidence bound (LCB)**.
- $C(X) = (-\infty, C_2(X)]$: an **upper confidence bound (UCB)**.

An LCB or UCB is usually obtained by inverting a *one-sided* test in the matching direction; it is
called **uniformly most accurate (UMA)** if the underlying test is UMP. A CI is obtained by
inverting a *two-sided* test; it is called **UMAU** if the underlying test is UMPU.

## Worked example: bounding an exponential scale parameter

$X \sim \mathrm{Exp}(\theta)$, density $\frac{1}{\theta}e^{-x/\theta}$ for $x>0,\theta>0$, cdf
$\mathbb{P}_\theta(X \le x) = 1 - e^{-x/\theta}$.

**LCB.** Invert the level-$\alpha$ test of $H_0: \theta \le \theta_0$ (which rejects for large $X$,
since larger $\theta$ makes $X$ stochastically larger). Solve for the cutoff at the worst case
$\theta = \theta_0$:

$$
\alpha = \mathbb{P}_{\theta_0}\big(X > c(\theta_0)\big) = e^{-c(\theta_0)/\theta_0} \implies c(\theta_0) = \theta_0 \log(1/\alpha).
$$

$\theta_0$ is *not* rejected exactly when $X \le c(\theta_0)$, i.e. when
$\theta_0 \ge X/(-\log\alpha)$, giving

$$
C(X) = \left[\frac{X}{-\log \alpha},\ \infty\right).
$$

**UCB.** Inverting the test of $H_0: \theta \ge \theta_0$ (which rejects for small $X$) the same way
gives

$$
C(X) = \left(-\infty,\ \frac{X}{-\log(1-\alpha)}\right].
$$

**Equal-tailed CI.** Invert the equal-tailed test of $H_0: \theta = \theta_0$, built by combining the
two one-sided tests above each at level $\alpha/2$:

$$
\phi_\alpha^{\mathrm{ET}}(X) = \phi_{\alpha/2}^{\ge \theta_0}(X) + \phi_{\alpha/2}^{\le \theta_0}(X).
$$

Intersecting the corresponding LCB and UCB (each built with $\alpha/2$ in place of $\alpha$) gives

$$
C(X) = \left[\frac{X}{-\log(\alpha/2)},\ \infty\right) \cap \left(-\infty,\ \frac{X}{-\log(1-\alpha/2)}\right] = \left[\frac{X}{-\log(\alpha/2)},\ \frac{X}{-\log(1-\alpha/2)}\right].
$$

The same recipe, inverting the UMPU two-sided test instead of the equal-tailed one, gives the UMAU
interval.

## Worked example: a nonparametric confidence interval for the median

Model: $X_1,\dots,X_n \overset{\mathrm{iid}}\sim F$ for *any* cdf $F$, and let
$g(F) = \mathrm{median}(F) = F^{-1}(1/2)$ (assumed well-defined). This is nonparametric — no shape
is assumed for $F$ at all — so a test that works for every $F$ has to be found.

The **two-sided sign test**: $H_0: g(F) = \mu \iff F(\mu) = 1/2$ vs. $H_1: g(F) \ne \mu \iff F(\mu) \ne 1/2$.
Let $S(X;\mu) = \#\{X_i > \mu\}$; then $S(X;\mu) \sim \mathrm{Binom}(n,\, 1-F(\mu))$, which is
$\mathrm{Binom}(n,1/2)$ exactly when $H_0$ holds — and this distribution does not depend on $\mu$ under
the null, so a single cutoff $c_\alpha$ works for every candidate $\mu$ at once. Reject when

$$
T(X;\mu) = |S(X;\mu) - n/2| > c_\alpha
$$

(e.g. $n=100$, $c_\alpha=5$: reject $\mu$ when $S(X) \notin [45,55]$).

Inverting: $\mu \in C(X)$ iff $\mu$ is *not* rejected, i.e.

$$
|S(X;\mu) - n/2| \le c_\alpha \iff \#\{X_i > \mu\} \in [n/2 - c_\alpha,\, n/2 + c_\alpha].
$$

Since $\mu \mapsto \#\{X_i > \mu\}$ is a step function that decreases by one every time $\mu$ passes an
order statistic, this count stays inside $[n/2-c_\alpha, n/2+c_\alpha]$ exactly while $\mu$ runs between
the $(n/2-c_\alpha)$-th and $(n/2+c_\alpha)$-th order statistics:

$$
C(X) = \Big[X_{(n/2 - c_\alpha)},\ X_{(n/2 + c_\alpha)}\Big].
$$

No distributional assumption on $F$ was used anywhere — the interval is built entirely from order
statistics and is valid for every $F$ with a well-defined median.

## Common misreadings of $p$-values and confidence intervals

Hypothesis tests are used everywhere in science, and the same handful of misinterpretations recur:

1. $p<0.05 \implies$ "there is an effect," or worse, "the effect size equals the point estimate." A
   small $p$-value says the data are inconsistent with $H_0$; it says nothing about how large the
   effect is.
2. $p>0.05 \implies$ "there is no effect." Failing to reject is not evidence for $H_0$ — it may just
   reflect low power.
3. $p = 10^{-6} \implies$ "the effect is huge." An extremely small $p$-value can come from a tiny
   effect measured very precisely (e.g. a huge sample), so the *size* of the $p$-value says nothing
   about the *size* of the effect.
4. $p = 10^{-6} \implies$ "the data are significant, and everything about the model is correct." A
   tiny $p$-value under a misspecified model just reflects the misspecification.
5. If the CI for an effect in men is $[0.2, 3.2]$ and for women is $[-0.2, 2.8]$, this does **not**
   license "there is an effect for men and not for women." The two intervals overlap heavily and
   neither addresses the men-vs-women comparison directly; that needs its own test or interval.

A dichotomous test doesn't make uncertainty go away — it just compresses it into one bit. Confidence
intervals are usually less misleading to a novice than a bare accept/reject decision, precisely
because they display the whole range of plausible values rather than a single verdict.

## How much weight can a hypothesis test bear?

Learning about the world from data is not easy or automatic. A hypothesis test lets you ask a
specific question, about a specific data set, under specific modeling assumptions, using a specific
testing method — and every one of those choices bears on how the result should be read. It is a real
problem, not a hypothetical one, that top-tier journals routinely publish $p$-values without stating
what model or test produced them. A test can be a good companion to critical thinking; it is never a
substitute for it. "All models are wrong, some are useful" — but knowing *when* the wrongness of the
assumptions actually matters takes experience and theory, not just the number that comes out of the
test.

Two conceptual objections worth having an answer to:

**Q1. Why test $H_0:\theta=0$ at all? No real $\theta$ is ever exactly zero.**

- Test $H_0: |\theta| \le \delta$ instead, if that is the real concern — if the standard error of
  $\hat\theta$ is much larger than $\delta$, it makes little practical difference which you use.
- Most two-sided tests already support a directional conclusion for free: "declare $\theta>0$ if
  $T > c_\alpha$, declare $\theta<0$ if $T < -c_\alpha$," with $\mathbb{P}(\text{false directional
  claim}) \le \alpha$. So the point-null test is doing real work even though no $\theta$ is exactly
  zero.
- This is harder to make in nonparametric problems — e.g. $H_0: P=Q$ vs. $H_1: P \ne Q$ tested by
  permutation — but the alternative of forcing a fully Bayesian framework imposes its own strong
  assumptions.

**Q2. People only like frequentist $p$-values and CIs because they mistake them for Bayesian
statements** — "95% chance $C(X) \ni \theta$" gets read as a claim about the posterior
$p(\theta \mid X)$.

This is often true. But subjective Bayesian results are misread just as often, reported as "the"
posterior distribution of $\theta$ when what is actually being reported is "*my* posterior opinion
about $\theta$," conditional on a prior nobody else is obliged to share.

## Sources

- Formal definition of $p(x)$, monotone test families, the reduction proposition, and
  super-uniformity: `berkeley-stat210a` fall-2025 and fall-2026, `handwritten/lecture16-pconf.pdf`
  (converted `fall-2025/handwritten/lecture16-pconf.md`, `fall-2026/handwritten/lecture16-pconf.md`)
  — these two years give the same lecture with cleaner statements of the propositions and their
  proofs; the fall-2026 file duplicates fall-2025 verbatim and both conversions cut off mid-proof of
  super-uniformity, completed here from the fall-2024 version of the same argument.
- Informal $p$-value picture, the binomial/normal examples, the exponential and $N_d$ examples of
  test-dependence, confidence sets, duality/inverting, CI/LCB/UCB/UMA/UMAU definitions, the
  exponential worked example, the median sign-test example, and the misinterpretation and
  conceptual-objection sections: `berkeley-stat210a` fall-2024,
  `handwritten/lecture16-pconf/01-formal-definition.md` and
  `handwritten/lecture16-pconf/02-confidence-intervals-bounds.md`.
- All four files are model reconstructions of a handwritten PDF with no text layer (route: llm,
  fidelity: reconstructed); equations are unverified against the original scan.
- Referred to but not contained in any of the four files: the earlier-lecture construction of the
  UMPU test for $\mathrm{Exp}(\theta)$ and its cutoff $c_2(\alpha)$, used in the test-dependence
  example; the general Neyman–Pearson randomized-test construction (boundary randomization
  probability $\gamma_\alpha$), used implicitly in the reduction proposition's proof.

---

[← 49. $p$-Values and Confidence Sets](49-p-values-and-confidence-sets.md) · [Contents](index.md) · [51. Nuisance Parameters and Conditioning →](51-nuisance-parameters-and-conditioning.md)
