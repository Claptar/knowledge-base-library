---
title: "80. p-Values"
course: "Berkeley Stat 210A Fall 2024"
chapter: 80
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 80. p-Values

## What this covers

A level-$\alpha$ test gives a single accept/reject verdict. This chapter asks what more can be
extracted from the same testing machinery: the $p$-value, which reports the verdict for *every*
significance level at once, and the confidence region, which reports the verdict for *every* null
hypothesis at once. It then works through how both objects get misread, and why some statisticians
distrust hypothesis testing even when it is used correctly. It assumes the reader already has the
Neyman–Pearson vocabulary of a test $\phi_\alpha$, its size, and the notions of a uniformly most
powerful (UMP) and uniformly most powerful unbiased (UMPU) test.

## From accept/reject to a fuller picture

A hypothesis test, as defined so far, is a dichotomous decision: fix a null $H_0$, a test statistic,
a critical threshold, and a significance level $\alpha$, and either reject or don't. Sometimes a
dichotomous decision really is what is needed — the FDA has to decide whether to approve a drug or
not — but this is the rare case. If a test statistic is large enough to reject $H_0:\theta=0$ at
$\alpha=0.05$, the natural next questions are usually:

- Would we still have rejected at a stricter level, like $\alpha=0.01$ or $\alpha=0.005$?
- Have we established that $\theta$ is *far* from zero, or only that it isn't exactly zero?

The $p$-value answers the first question by summarizing the outcome of the test at every $\alpha$
we could have chosen. The confidence region answers the second by summarizing the outcome of the
test at every null value we could have tested. Both are built from exactly the machinery already in
hand for hypothesis tests — nothing new is assumed about the model.

## $p$-values

### Informal definition

If we reject for large values of a test statistic $T(X)$, the $p$-value asks how extreme the
observed value of $T$ is relative to its distribution under the null.

**Definition (informal).** For a fixed value $x$, the $p$-value is
$$
p(x) = \sup_{\theta \in \Theta_0} \mathbb{P}_\theta(T(X) \geq T(x)),
$$
the probability, computed under the (possibly composite) null, that $T(X)$ would be at least as
large as its realized value. The random variable $p(X)$ is *the* $p$-value.

**Example (binomial).** If $X \sim \mathrm{Binom}(n,\theta)$ and we test $H_0: \theta \leq 0.5$ vs
$H_1: \theta > 0.5$, the UMP test rejects for large $X$. Since $X$ is stochastically increasing in
$\theta$, the supremum over the null is attained at the boundary $\theta = 0.5$:
$$
p(x) = \sup_{\theta \leq 0.5} \mathbb{P}_\theta(X \geq x) = \mathbb{P}_{0.5}(X \geq x).
$$

**Example ($Z$-test).** If $X \sim N(\theta,1)$ and we test $H_0:\theta=0$ vs $H_1:\theta\neq 0$,
the two-sided test rejects for large $|X|$, so
$$
p(x) = \mathbb{P}_0(|X| \geq |x|) = 2(1-\Phi(|x|)) = 2\min\{\Phi(x), 1-\Phi(x)\}.
$$

<figure>
<svg viewBox="0 0 360 210" role="img" aria-label="Null density of a test statistic with both tails beyond the observed value shaded to represent the two-sided p-value">
  <line x1="20" y1="155" x2="340" y2="155" stroke="currentColor" stroke-width="1.5"/>
  <path d="M20,155 C90,155 130,40 180,40 C230,40 270,155 340,155" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="250,125 265,133 280,145 300,153 340,155 340,155 250,155" fill="currentColor" fill-opacity="0.15"/>
  <polygon points="110,125 95,133 80,145 60,153 20,155 20,155 110,155" fill="currentColor" fill-opacity="0.15"/>
  <line x1="110" y1="155" x2="110" y2="122" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="250" y1="155" x2="250" y2="122" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="180" y="172" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="110" y="172" text-anchor="middle" font-size="12" fill="currentColor">-|x|</text>
  <text x="250" y="172" text-anchor="middle" font-size="12" fill="currentColor">|x|</text>
  <text x="180" y="195" text-anchor="middle" font-size="12" fill="currentColor">shaded area = p(x)</text>
</svg>
<figcaption>The two-sided p-value is the total probability mass of the null distribution of T(X) at
least as extreme as the observed value — the shaded tail area beyond ±|x|.</figcaption>
</figure>

### Formal definition

Not every test is "reject for large $T(X)$": a two-sided UMPU test, for instance, rejects when
$T(X)$ is either large or small, with an asymmetric threshold on each side. A definition that covers
every case starts from a whole family of tests rather than one statistic.

Suppose we are testing $H_0:\theta\in\Theta_0$ vs $H_1:\theta\in\Theta_1$, and that for every
$\alpha\in[0,1]$ we have a level-$\alpha$ test $\phi_\alpha$,
$$
\sup_{\theta\in\Theta_0} \mathbb{E}_\theta \phi_\alpha(X) \leq \alpha,
$$
with the family **monotone in $\alpha$**: a test that rejects at a stricter level also rejects at
any more lenient level, i.e. $\phi_{\alpha_1}(X) \leq \phi_{\alpha_2}(X)$ whenever
$\alpha_1 \leq \alpha_2$ (equivalently, in the non-randomized case, $R_{\alpha_1}\subseteq
R_{\alpha_2}$).

**Definition (formal).** The $p$-value for this family is the value of $\alpha$ at which the test
barely rejects:
$$
p(x) = \sup\{\alpha : \phi_\alpha(x) < 1\} = \inf\{\alpha : \phi_\alpha(x) = 1\}
= \inf\{\alpha : x \in R_\alpha\}.
$$
Equivalently, $p(x) \le \alpha$ exactly when $x$ would have been rejected at level $\alpha$ (up to
the boundary case). It is possible to define a randomized version of the $p$-value, by augmenting
the sample space with an independent uniform variable, but the added complexity rarely earns its
keep.

**Example (exponential).** Suppose $X \sim \mathrm{Exp}(\theta)$ with $\mathbb{P}_\theta(X\le x) =
1 - e^{-x/\theta}$, and we test $H_0:\theta=1$ vs $H_1:\theta\neq 1$ using either the equal-tailed
test or the UMPU test. For $x>1$, which lies in the acceptance region for small $\alpha$ and in the
right lobe of the rejection region for large $\alpha$, the acceptance region's right boundary
shrinks continuously as $\alpha$ grows, so $p(x)$ is the unique $\alpha$ at which $x$ sits exactly
on the boundary. For the equal-tailed test, that boundary condition is
$$
\alpha/2 = \mathbb{P}_1(X>x) = e^{-x} \implies p(x) = 2e^{-x}.
$$
For the UMPU test, $p(x)$ is defined implicitly by $c_2(\alpha) = x$ for the (asymmetric) right
cutoff $c_2(\alpha)$, and is generally solved numerically rather than in closed form.

### The two definitions agree

**Proposition.** Suppose that for each $\alpha$ we reject for large $T(X)$, with threshold
$$
c_\alpha = \min\{c : \mathbb{P}_\theta(T(X) > c) \leq \alpha \text{ for all } \theta \in \Theta_0\}
$$
taken as small as Type I error control allows (well-defined since complementary CDFs are
right-continuous), and with randomization at the boundary chosen as generously as level $\alpha$
permits. Then the formal $p$-value coincides with the informal one.

*Why.* Let $p_1(x) = \sup_{\theta\in\Theta_0}\mathbb{P}_\theta(T(X)\ge T(x))$ be the informal value
and $p_2(x)=\sup\{\alpha:\phi_\alpha(x)<1\}$ the formal one. The key equivalence is
$$
p_1(x) > \alpha \iff \mathbb{P}_\theta(T(X)\ge T(x))>\alpha \text{ for some } \theta\in\Theta_0
\iff c_\alpha > T(x), \text{ or } c_\alpha = T(x) \text{ with sub-maximal randomization}
\iff \phi_\alpha(x) < 1.
$$
Taking the supremum of both sides over $\alpha$ for which $p_1(x)>\alpha$ recovers $p_2(x) = p_1(x)$.
So the general definition is not a different object from the tail-probability one — it is the same
quantity, phrased so that it still makes sense when "reject for large $T(X)$" doesn't quite
describe the test.

### $p$-values are super-uniform

**Claim.** Under any $\theta$ in the null, $\mathbb{P}_\theta(p(X)\le\alpha)\le\alpha$ — the
$p$-value is stochastically at least as large as a $\mathrm{Uniform}(0,1)$ variable.

This follows almost immediately from the definition: $p(x)\le\alpha$ if and only if
$\phi_{\alpha+\varepsilon}(x)=1$ for every $\varepsilon>0$, so for $\theta\in\Theta_0$,
$$
\mathbb{P}_\theta(p(X)\le\alpha) = \lim_{\varepsilon\downarrow 0}
\mathbb{P}_\theta(\phi_{\alpha+\varepsilon}(X)=1) \leq \lim_{\varepsilon\downarrow 0}
\mathbb{E}_\theta[\phi_{\alpha+\varepsilon}(X)] \leq \alpha,
$$
using only that each $\phi_{\alpha+\varepsilon}$ has size at most $\alpha+\varepsilon$. This is the
formal content behind "reject when $p(X)\le\alpha$": doing so is a level-$\alpha$ test, by
construction, for every $\alpha$ at once.

### What the $p$-value depends on, and what it doesn't tell you

The $p$-value is not a property of the data alone: it depends on the model, the null hypothesis,
the data, *and* the choice of test statistic. When the null or alternative is composite, several
different tests can be equally defensible, and there is no reason to treat the $p$-value from any
one of them as *the* canonical summary of the evidence against the null.

**Example (multivariate Gaussian, sparse vs. dense alternatives).** Suppose $X\sim N_d(\mu, I_d)$
and we test $H_0:\mu=0$ vs $H_1:\mu\neq 0$. For $d=1$ the alternative is bi-directional and everyone
agrees on the two-sided test. For $d\ge 2$ the alternative is *multidirectional*, and the higher the
dimension, the more this choice matters. If we want the test to be invariant to the direction
$\mu/\|\mu\|$, we reject for large $\|X\|_2$ — the **$\chi^2$ test**, since $\|X\|_2^2$ has a
$\chi^2_d$ distribution under the null. If instead we expect $\mu$, when nonzero, to be *sparse*,
the **max test** $\|X\|_\infty = \max_i |X_i|$ can do far better. Each test dominates the other in
different sparsity regimes: for $\mu$ a $k$-sparse vector of fixed norm, the max test outperforms
the $\chi^2$ test when $\mu$ is sufficiently sparse relative to $d$, and the reverse holds when
$\mu$ is dense, with the gap between them widening as $d$ grows. On the same data set, these two
choices can produce very different $p$-values — the choice of statistic already encodes a belief
about whether the effect, if real, is concentrated in a few coordinates or spread across all of
them.

A further caution, independent of which test is used: accept/reject decisions on their own are not
very interesting, because what we usually care about is *how big* $\theta$ is. A tiny $p$-value
does not imply that $\theta$ is large, and a large $p$-value does not imply that $\theta$ is small
— a huge sample can produce an astronomically small $p$-value for an effect that is negligible in
size, and a small or noisy sample can produce an unremarkable $p$-value while telling us almost
nothing about where $\theta$ actually lies. The next section develops the tool that fills this gap.

## Confidence regions

### Definition and the coverage statement

Suppose we are testing $H_0:\theta=0$ vs $H_1:\theta\neq 0$ and get a very small $p$-value. That
tells us the observed data are inconsistent with $\theta=0$, but it does *not* tell us that $\theta$
is far from zero: with a large enough sample we might be able to say, with great confidence, that
$\theta \in [0.0011, 0.0012]$ — which could well amount to *confirming* that $\theta$ is too small
to matter, even though the formal null is soundly rejected. Symmetrically, a large $p$-value does
not mean $\theta$ is close to zero: it could mean the data pin $\theta$ down to a narrow band around
zero, or it could mean the data are simply too weak to say much about $\theta$ at all. A confidence
region, rather than a single null, tells us what our test would have decided for *every* candidate
null value at once, and is the more reliable guide to which values of $\theta$ are plausible.

**Definition.** $C(X)$ is a $1-\alpha$ **confidence region** for $g(\theta)$ if
$$
\mathbb{P}_\theta(C(X) \ni g(\theta)) \geq 1-\alpha, \quad \text{for all } \theta \in \Theta.
$$
We say $C(x)$ **covers** $g(\theta)$ if $C(x)\ni g(\theta)$; the **coverage probability** at $\theta$
is $\mathbb{P}_\theta(C(X)\ni g(\theta))$; and the **confidence level** of $C$ is
$\inf_{\theta\in\Theta}\mathbb{P}_\theta(C(X)\ni g(\theta))$.

The "$\ni$" is deliberate: $C(X)$ is the random subject of the sentence, and $g(\theta)$ is the fixed
object. This guarantee is routinely misread as a Bayesian one, in which $C(X)$ is realized first and
$g(\theta)$ then has some probability of landing inside it. That reading is wrong: a confidence
region is a frequentist object whose guarantee is meant to hold for each fixed $\theta$. Once $X$ is
observed, $C(X)$ either contains $g(\theta)$ or it doesn't — there is no remaining randomness. So,
although the following are mathematically equivalent statements about the *procedure*, only the
first is safe to say about a *realized* interval:

- **Recommended:** "$C(X)$ has a 95% chance of covering $g(\theta)$."
- **Not recommended:** "$g(\theta)$ has a 95% chance of falling in $C(X)$."

Once we have actually computed, say, $C(x) = [0.8, 1.1]$, it is never correct to say "there is a 95%
chance $g(\theta) \in [0.8, 1.1]$." Under the frequentist model this is a category error, since
$g(\theta)$ isn't random; and even under a Bayesian model with a genuine posterior probability, that
number depends on the prior and need not be 95%.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Six repeated confidence intervals for a fixed unknown parameter, one of which fails to cover it">
  <line x1="170" y1="15" x2="170" y2="205" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="170" y="12" text-anchor="middle" font-size="12" fill="currentColor">&#952;</text>
  <line x1="130" y1="40" x2="210" y2="40" stroke="currentColor" stroke-width="2"/>
  <line x1="130" y1="35" x2="130" y2="45" stroke="currentColor" stroke-width="2"/>
  <line x1="210" y1="35" x2="210" y2="45" stroke="currentColor" stroke-width="2"/>
  <line x1="145" y1="70" x2="225" y2="70" stroke="currentColor" stroke-width="2"/>
  <line x1="145" y1="65" x2="145" y2="75" stroke="currentColor" stroke-width="2"/>
  <line x1="225" y1="65" x2="225" y2="75" stroke="currentColor" stroke-width="2"/>
  <line x1="100" y1="100" x2="165" y2="100" stroke="#c0392b" stroke-width="2"/>
  <line x1="100" y1="95" x2="100" y2="105" stroke="#c0392b" stroke-width="2"/>
  <line x1="165" y1="95" x2="165" y2="105" stroke="#c0392b" stroke-width="2"/>
  <line x1="150" y1="130" x2="200" y2="130" stroke="currentColor" stroke-width="2"/>
  <line x1="150" y1="125" x2="150" y2="135" stroke="currentColor" stroke-width="2"/>
  <line x1="200" y1="125" x2="200" y2="135" stroke="currentColor" stroke-width="2"/>
  <line x1="120" y1="160" x2="190" y2="160" stroke="currentColor" stroke-width="2"/>
  <line x1="120" y1="155" x2="120" y2="165" stroke="currentColor" stroke-width="2"/>
  <line x1="190" y1="155" x2="190" y2="165" stroke="currentColor" stroke-width="2"/>
  <line x1="140" y1="190" x2="210" y2="190" stroke="currentColor" stroke-width="2"/>
  <line x1="140" y1="185" x2="140" y2="195" stroke="currentColor" stroke-width="2"/>
  <line x1="210" y1="185" x2="210" y2="195" stroke="currentColor" stroke-width="2"/>
</svg>
<figcaption>Six confidence intervals from repeated samples, for one fixed but unknown θ (dashed
line). About 95% of such intervals cover θ; here one (highlighted) does not. Coverage is a
probability statement about the random interval, never about θ.</figcaption>
</figure>

### Duality of tests and confidence regions

Confidence regions and hypothesis tests are two views of the same construction.

Given a level-$\alpha$ test $\phi(X;a)$ of $H_0: g(\theta)=a$ vs $H_1: g(\theta)\neq a$, for every
candidate value $a$, define
$$
C(X) = \{a : \phi(X;a) < 1\},
$$
the set of non-rejected values. This is a valid $1-\alpha$ confidence region, because
$$
\mathbb{P}_\theta(C(X)\ni g(\theta)) = \mathbb{P}_\theta(\phi(X;g(\theta))<1) \geq 1-\alpha.
$$
Building a confidence region this way is called **inverting** the family of tests.

Conversely, given a $1-\alpha$ confidence region $C(X)$ for $g(\theta)$, define
$$
\phi(x;a) = 1\{a \notin C(x)\}.
$$
This is a valid level-$\alpha$ test of $H_0:g(\theta)=a$ vs $H_1:g(\theta)\neq a$, since
$$
\mathbb{E}_\theta \phi(X;g(\theta)) = \mathbb{P}_\theta(g(\theta)\notin C(X)) \leq \alpha.
$$

A confidence region is **unbiased** if it is at least as likely to contain the true value as any
other value: $\mathbb{P}_\theta(C(X)\ni a) \leq 1-\alpha$ for every $a\neq g(\theta)$. A region is
unbiased exactly when the test obtained by inverting it is unbiased, and inverting an unbiased
non-randomized test yields an unbiased region.

**Example (Gaussian confidence ellipse).** Suppose $X\sim N_d(\mu,\Sigma)$ with $\Sigma$ known, so
that $Z = \Sigma^{-1/2}(X-\mu)\sim N_d(0,I_d)$. A natural test of $H_0:\mu=\mu_0$ rejects for large
values of $\|\Sigma^{-1/2}(X-\mu_0)\|^2$, which is $\chi^2_d$ under the null. Writing $c_\alpha$ for
the upper-$\alpha$ quantile of $\chi^2_d$, inverting this test gives the confidence ellipse
$$
C(X) = \{\mu_0 : \|\Sigma^{-1/2}(X-\mu_0)\|^2 \leq c_\alpha\}.
$$
Sampling repeatedly from this model produces a scatter of such ellipses, roughly $1-\alpha$ of which
contain the fixed true $\mu$ — the same phenomenon as the one-dimensional picture above, just drawn
in the plane.

### Confidence intervals and bounds

When $C(X) = [C_L(X), C_U(X)] \subseteq \mathbb{R}$, we call it a **confidence interval (CI)**; when
it's a half-line $[C_L(X),\infty)$ or $(-\infty, C_U(X)]$, we call $C_L(X)$ a **lower confidence
bound (LCB)** and $C_U(X)$ an **upper confidence bound (UCB)**. Bounds are typically obtained by
inverting a one-sided test in the matching direction, and intervals by inverting a two-sided test of
a point null. A bound is **uniformly most accurate (UMA)** if it inverts a (non-randomized) UMP
test, and an interval is **uniformly most accurate unbiased (UMAU)** if it inverts a (non-randomized)
UMPU test.

**Example (exponential).** Let $X\sim\mathrm{Exp}(\theta)$ with $\mathbb{P}_\theta(X\le x) =
1-e^{-x/\theta}$, $x>0$.

For an LCB, invert the UMP test of $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$, which rejects
for large $X$. The cutoff solves
$$
\alpha = \mathbb{P}_{\theta_0}(X>c_\alpha) = e^{-c_\alpha/\theta_0} \iff c_\alpha = -\theta_0\log\alpha,
$$
so the test rejects iff $X > -\theta_0\log\alpha$, giving
$$
C(X) = \{\theta_0 : X \leq -\theta_0\log\alpha\} = \left[\frac{X}{-\log\alpha}, \infty\right),
\qquad C_L(X) = \frac{X}{-\log\alpha}.
$$

By the same reasoning, inverting the UMP test of $H_0:\theta\ge\theta_0$ vs $H_1:\theta<\theta_0$
(which rejects for small $X$, when $X < -\theta_0\log(1-\alpha)$) gives the UCB
$$
C_U(X) = \frac{X}{-\log(1-\alpha)}.
$$

Intersecting the two one-sided regions, each computed at level $1-\alpha/2$, gives the equal-tailed
$1-\alpha$ confidence interval
$$
C(X) = \left[\frac{X}{-\log(\alpha/2)},\ \frac{X}{-\log(1-\alpha/2)}\right].
$$

To invert the UMPU test instead, use that the exponential family is a scale family: if $c_1, c_2$
are the left and right cutoffs of the UMPU test of $H_0:\theta=1$ vs $H_1:\theta\neq 1$, the cutoffs
for testing $H_0:\theta=\theta_0$ are $\theta_0 c_1$ and $\theta_0 c_2$, so
$$
C(X) = \{\theta_0 : \theta_0 c_1 \leq X \leq \theta_0 c_2\} = \left[\frac{X}{c_2}, \frac{X}{c_1}\right].
$$

## Misinterpreting hypothesis tests

Hypothesis tests, and their manifestations as $p$-values and confidence intervals, are ubiquitous in
science precisely because drawing reliable conclusions from data is a ubiquitous goal — but they
lend themselves readily to misreading. The following errors show up distressingly often in
published work:

1. $p<0.05$, therefore there is an effect (equal in size to the point estimate).
2. $p>0.05$, therefore there is no effect.
3. $p<10^{-6}$, therefore the effect is huge.
4. $p<10^{-6}$, therefore "the data are highly significant" and every point estimate in the model
   can be taken at face value.
5. The CI for the effect in men is $[0.2, 3.2]$ and for women is $[-0.2, 2.8]$, therefore there is
   an effect for men but not for women.

As a broad generalization, confidence intervals mislead novices less often than $p$-values or bare
accept/reject decisions do: "the effect size was $1.4$ ($p=0.03$)" sounds more precise than "the
effect size was $1.4$ (CI $[0.14, 2.7]$)," even though the second is the more honest summary of what
was actually established. A dichotomous test does not eliminate uncertainty; it just hides where it
is.

More subtly, statistical models are abstractions that never capture every detail of a real
scientific setting, and this matters most exactly when we want to draw a conclusive inference from
the data. Many of these errors come from a desire — often born of shaky confidence in statistics
itself — to compartmentalize the statistical analysis from the scientific reasoning it is meant to
support. It is a genuine problem that top-tier journals, including in medicine, routinely publish
claims backed by a $p$-value without stating what model was assumed or what test was used to compute
it; an argument built on a $p$-value with the model and test left unstated is incomplete on its own
terms.

Interpreting a hypothesis test can never be made easy or automatic, for the same reason that science
itself can't be. A test lets us ask a specific question, in a specific way, under specific modeling
assumptions, and every choice made along the way needs to be defended as part of the eventual
scientific argument. Hypothesis tests are a good companion to critical thinking, never a substitute
for it: all models are wrong, some are useful, and telling which is which for a given purpose takes
experience and theory, not a threshold.

## Conceptual objections to hypothesis testing

That tests are often used carelessly is uncontroversial. More controversially, some statisticians
doubt that hypothesis testing is ever a conceptually sound tool, even used correctly. Two objections
recur.

**Objection 1: point nulls are unrealistic.** Why test $\theta=0$ at all, when no real effect is
ever exactly zero? There are several responses, at least in parametric problems:

- Test a different null instead, such as $H_0: |\theta| \leq \delta$ for some $\delta > 0$ that
  represents "small enough not to matter." If the standard error of $\hat\theta$ is much smaller than
  $\delta$, this makes little practical difference from testing the point null.
- Read a two-sided test of $H_0:\theta=0$ as two one-sided tests, $H_0^1:\theta\ge 0$ and
  $H_0^2:\theta\le 0$, at levels $\alpha_1,\alpha_2$ with $\alpha_1+\alpha_2=\alpha$: reject
  $H_0^2$ and conclude $\theta>0$ if $T>c_2$, reject $H_0^1$ and conclude $\theta<0$ if $T<c_1$.
  The chance of a false claim about the *sign* of $\theta$ is then below $\alpha$ — under this
  reading, rejecting the point null always comes with learning the sign of $\theta$.
- Invert a test of the point null to get a confidence interval for $\theta$, as above.

This objection is harder to answer in nonparametric problems — e.g. a permutation test of
$H_0: P=Q$ against $H_1: P\neq Q$, where "$P=Q$" is no more unrealistic a priori than "$\theta=0$" is
in the parametric case, but the alternatives to testing it (such as Bayesian nonparametrics) force
much stronger assumptions on the analyst.

**Objection 2: frequentist methods answer the wrong question.** A $p$-value reports
$\mathbb{P}(\text{data this extreme} \mid H_0)$, but what a scientist actually wants is something
like $\mathbb{P}(H_0 \mid \text{data})$ — the objection is that frequentist inference is at best a
clever evasion of the real question, and at worst a bait-and-switch that then blames practitioners
for conflating the two. In the same vein, what people really want from a confidence interval is to
say the estimand is *probably* inside it; but a probability statement about a CI is only available
*before* the data are seen (or, after the fact, about a fresh replication) — never about the
particular realized interval.

These are real drawbacks, not just misunderstandings to be corrected with better teaching. But the
Bayesian alternative has its own cost: it requires the analyst to supply personal opinions about
every part of the problem, including the prior probability that the null is true — the very
quantity in question — and a full distribution over alternative values, which a frequentist
analysis very often sidesteps by using a UMP or other canonical test. The versatility of hypothesis
tests, and their comparatively frugal assumptions, are a large part of why they remain the dominant
tool for scientific data analysis despite these objections.

## Sources

- Berkeley STAT210A course reader, "p-values, confidence regions, and (mis-)interpreting tests," in
  its fall-2025 and fall-2026 forms — the fullest treatment, used for the formal definition, the
  equivalence proposition, the super-uniformity result and proof, the multivariate Gaussian
  sparsity example, the confidence-region definition and duality, the Gaussian confidence-ellipse
  example, the exponential confidence-interval derivation, and the misinterpretation/objection
  discussion:
  [fall-2025 `01-p-values-confidence-regions-and-mis--interpreting-tests.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html),
  [`02-p-values.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html),
  [`03-confidence-regions.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html),
  [`04-mis--interpreting-hypothesis-tests.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html),
  [`05-conceptual-objections-to-hypothesis-testing.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html);
  the fall-2026 copy of the same reader chapter is identical in substance
  ([`01`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd)–[`04`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd)).
- Berkeley STAT210A fall-2024 lecture notes and fall-2025 lecture "units" on the same chapter — the
  terser, in-class version of the same material, used for the "accept/reject decisions are not
  interesting" remark, the note that the $p$-value depends on model/null/data/test choice, and the
  aside about journals publishing $p$-values without stating the model or test:
  [fall-2024 `01-p-values.md`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-interpretation.qmd),
  [`02-confidence-regions.md`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-interpretation.qmd),
  [`03-misinterpreting-hypothesis-tests.md`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-interpretation.qmd);
  fall-2025 units
  [`01-1-p-values.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html),
  [`02-2-confidence-regions.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html),
  [`03-3-misinterpreting-hypothesis-tests.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html).
- Not included: the interactive lecture demos (power-curve comparison of the $\chi^2$ and max tests
  as functions of sparsity and dimension; a resampling widget for the Gaussian confidence ellipse)
  were JavaScript widgets embedded in the fall-2025/fall-2026 reader source, described here in prose
  rather than reproduced. A "randomized $p$-value" construction was sketched in the fall-2026 source
  but left commented out (not part of the delivered material) beyond the one-line remark that it
  exists and usually isn't worth the complexity.

---

[← 79. Stat 210A: Course Information](79-stat-210a-course-information.md) · [Contents](index.md) · [81. t, F, and Linear Models →](81-t-f-and-linear-models.md)
