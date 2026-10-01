---
title: "67. Least Favorable Priors"
course: "Berkeley Stat 210A"
chapter: 67
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 67. Least Favorable Priors

## What this covers

Two earlier ideas for choosing among estimators were to require unbiasedness (leading to UMVU estimators) and
to average the risk function over a prior (leading to Bayes estimators). This chapter develops a third: choosing
the estimator with the smallest *worst-case* risk. It defines minimax risk and minimax estimators, gives the
game-theoretic picture behind the name, and shows the main technique for actually finding a minimax estimator:
pairing it with an adversarial "least favorable" prior whose Bayes estimator happens to have constant — or at
least maximal-on-its-support — risk. It assumes the reader already has risk functions $R(\theta;\delta)$, Bayes
estimators and Bayes risk for a prior, and the Beta–Binomial Bayes-estimator calculation from earlier in the
course.

## Minimax risk

Rather than restricting to unbiased estimators, or averaging risk over a prior, a third approach is to look at
an estimator's worst-case risk over the whole parameter space and try to make that as small as possible:

$$
\operatorname*{minimize}_{\delta}\ \sup_{\theta \in \Theta} R(\theta; \delta).
$$

The (possibly unattained) infimum of all estimators' sup-risks is called the **minimax risk** of the estimation
problem,

$$
r^* = \inf_\delta \sup_\theta R(\theta; \delta),
$$

and an estimator $\delta^*$ is **minimax** if it achieves the minimax risk, i.e. $\sup_\theta R(\theta;\delta^*) = r^*$.

Whether or not a minimax estimator exists, or we intend to use it, $r^*$ is a useful single number: it measures
how hard the estimation problem is, and tracking how it scales with sample size, dimension, or other problem
parameters is one of the standard tools for characterizing a problem's difficulty.

## The game between the analyst and Nature

The minimax risk is the value of an adversarial zero-sum game between the analyst, who picks the estimator to
make risk small, and "Nature," who picks the parameter to make risk large. If the analyst commits to an estimator
$\delta$ first, Nature's best response is to choose whichever $\theta$ maximizes $R(\theta;\delta)$; the risk
realized when the analyst also plays optimally is exactly $r^*$, attained (if at all) by $\delta^*$.

What if Nature moved first instead? If Nature had to reveal $\theta$ before the analyst chose $\delta$, the
problem would be trivial — the analyst would just use the truth. It becomes interesting again if we restrict
Nature to a *mixed strategy*: drawing $\theta$ from a fixed prior $\Lambda$. An analyst who can see $\Lambda$ (but
not the realized $\theta$) responds with the Bayes estimator $\delta_\Lambda$ and attains the Bayes risk
$r_\Lambda$.

Intuitively the analyst is better off moving second than first, and indeed the Bayes risk for any prior is a
lower bound on the minimax risk:

$$
r_\Lambda = \inf_\delta \int_\Theta R(\theta;\delta)\,d\Lambda(\theta) \;\le\; \inf_\delta \sup_\theta R(\theta;\delta) = r^*,
$$

because any estimator's average risk under $\Lambda$ is at most its worst-case risk. To get the tightest such
lower bound, we look for Nature's Nash-equilibrium mixed strategy — the prior that makes this bound as large as
possible.

## Least favorable priors

Since $r_\Lambda \le r^*$ for every prior $\Lambda$, we have $\sup_\Lambda r_\Lambda \le r^*$. A prior $\Lambda^*$
attaining this supremum is a **least favorable prior**: Nature's optimal mixed strategy, the one under which even
the analyst's best possible average performance is as bad as it can be made. (When no prior attains the
supremum — typically because $\Theta$ is not compact — a *sequence* of priors doing so in the limit plays the
same role; see below.)

Combined with the trivial fact that any estimator's sup-risk is itself an upper bound on $r^*$, this gives a
sandwich, valid for every estimator $\delta$ and every prior $\Lambda$:

$$
\sup_\theta R(\theta;\delta) \;\ge\; r^* \;\ge\; \sup_\Lambda r_\Lambda.
$$

If we can exhibit a $\delta$ and a $\Lambda$ that collapse both inequalities to equalities, we have simultaneously
found a minimax estimator and a least favorable prior.

**Theorem.** Suppose $\delta_\Lambda$ is the Bayes estimator for a prior $\Lambda$, with Bayes risk $r_\Lambda$,
and suppose

$$
r_\Lambda = \sup_\theta R(\theta;\delta_\Lambda).
$$

Then $\delta_\Lambda$ is minimax, $\Lambda$ is least favorable, and $r_\Lambda = r^*$. If, moreover, $\delta_\Lambda$
is the *unique* Bayes estimator for $\Lambda$ (up to a.e. equality), it is the unique minimax estimator.

*Proof.* For any other estimator $\delta$,

$$
\sup_\theta R(\theta;\delta) \;\ge\; \int R(\theta;\delta)\,d\Lambda(\theta) \;\ge\; r_\Lambda \;=\; \sup_\theta R(\theta;\delta_\Lambda),
$$

the first inequality because sup-risk dominates average risk under any prior, the second because $\delta_\Lambda$
is Bayes for $\Lambda$ (no estimator beats its average risk). So $\delta_\Lambda$ has the smallest sup-risk among
all estimators — it is minimax. If $\delta_\Lambda$ is the unique Bayes estimator, the second inequality is
strict for every $\delta \ne \delta_\Lambda$, so $\delta_\Lambda$ is uniquely minimax.

For "least favorable," note $r_\Lambda \le r^* \le \sup_\theta R(\theta;\delta_\Lambda) = r_\Lambda$, forcing
$r_\Lambda = r^*$: the lower bound $\Lambda$ produces is the tightest possible one. $\blacksquare$

This gives a checkable recipe: guess a prior, work out its Bayes estimator, and ask whether that estimator's
*average* risk under the prior equals its *worst-case* risk. If so, both the estimator and the prior are pinned
down at once.

The simplest way average risk can equal worst-case risk is for the risk function $R(\theta;\delta_\Lambda)$ to be
**constant** in $\theta$ — then trivially its average equals its maximum. But this is sufficient, not necessary:
more generally the theorem applies whenever the prior places *all* its mass on the set of $\theta$ where the risk
is maximized, whether or not the risk is constant anywhere else.

**A common mistake.** It is tempting to pick some prior $\Lambda$, compute the Bayes risk $r_\Lambda$, notice that
this single number doesn't depend on $\theta$, and declare the theorem satisfied. That observation proves
nothing: $r_\Lambda$ never depends on $\theta$, for *any* prior at all, for the trivial reason that $\theta$ has
already been integrated out. What the theorem actually requires is that the *risk function* $R(\theta;\delta_\Lambda)$
— before integrating over $\theta$ — attain its own supremum on the support of $\Lambda$, which is a genuine
condition to check.

## Example: estimating the sign of a normal mean

Let $X \sim N(\theta,1)$ with $\theta$ restricted to $|\theta|\ge 1$, and suppose the estimand is
$g(\theta) = \operatorname{sgn}(\theta)$ under squared-error loss. This example shows the theorem being used in
its more general form, not via a constant risk function.

Take $\Lambda$ to put mass $1/2$ on $\theta=1$ and $1/2$ on $\theta=-1$. The posterior probability of $\theta=1$
given $X=x$ is

$$
\mathbb{P}(\theta=1\mid X=x) = \frac{\phi(x-1)}{\phi(x-1)+\phi(x+1)},
$$

so the Bayes estimator — the posterior mean of $g(\theta) = \pm 1$ — is

$$
\delta_\Lambda(x) = \mathbb{E}_\Lambda[g(\theta)\mid X=x] = \frac{\phi(x-1)-\phi(x+1)}{\phi(x-1)+\phi(x+1)} = \frac{e^x-e^{-x}}{e^x+e^{-x}} = \tanh(x).
$$

The risk function of $\tanh(X)$ is not constant on $|\theta|\ge 1$: it decreases as $|\theta|$ grows, since a
larger $|\theta|$ makes the sign easier to detect. But it attains its overall supremum at *both* $\theta=1$ and
$\theta=-1$ — exactly the two points where $\Lambda$ places its mass. That is all the theorem needs: since
$\Lambda$'s entire mass sits on the argmax of the risk function, $r_\Lambda = \sup_\theta R(\theta;\delta_\Lambda)$,
so $\delta_\Lambda(X)=\tanh(X)$ is minimax and $\Lambda$ is least favorable.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Risk function of the tanh estimator in the sign-estimation example, touching its supremum exactly at the two points where the least favorable prior places its mass">
  <line x1="20" y1="180" x2="126.67" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="126.67" y1="180" x2="233.33" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="233.33" y1="180" x2="340" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="345" y="184" font-size="12" fill="currentColor">θ</text>

  <line x1="20" y1="40" x2="340" y2="40" stroke="currentColor" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="24" y="34" font-size="11" fill="currentColor">sup_θ R(θ; δ_Λ)</text>

  <path d="M126.67,40 Q70,65 20,120" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M233.33,40 Q290,65 340,120" fill="none" stroke="currentColor" stroke-width="2"/>

  <line x1="126.67" y1="40" x2="126.67" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="233.33" y1="40" x2="233.33" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>

  <circle cx="126.67" cy="180" r="4" fill="currentColor"/>
  <circle cx="233.33" cy="180" r="4" fill="currentColor"/>
  <text x="126.67" y="200" text-anchor="middle" font-size="12" fill="currentColor">-1</text>
  <text x="233.33" y="200" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="180" y="200" text-anchor="middle" font-size="11" fill="currentColor">θ excluded here</text>
</svg>
<figcaption>The risk of δ_Λ(x) = tanh(x) falls as |θ| grows past 1, but reaches its overall supremum exactly at
θ = ±1 — precisely where the least favorable prior Λ places its two point masses. That match on the support,
not a constant risk function, is the general condition the theorem needs.</figcaption>
</figure>

## Example: estimating a binomial proportion

Now consider $X \sim \text{Binom}(n,\theta)$, estimating $\theta$ under squared error, and look for a member of
the Beta-prior family with genuinely *constant* risk. Recall the Bayes estimator for a $\text{Beta}(\alpha,\beta)$
prior is $\frac{X+\alpha}{n+\alpha+\beta}$; a constant-risk member of this family should be symmetric, so try
$\alpha=\beta$: $\delta_\alpha(X) = \frac{X+\alpha}{n+2\alpha}$.

Its mean and bias are

$$
\mathbb{E}_\theta\!\left[\frac{X+\alpha}{n+2\alpha}\right] = \frac{n\theta+\alpha}{n+2\alpha}
\quad\Longrightarrow\quad
\text{Bias}(\theta;\delta_\alpha) = \frac{\alpha(1-2\theta)}{n+2\alpha},
$$

and its variance is

$$
\text{Var}_\theta\!\left(\frac{X+\alpha}{n+2\alpha}\right) = \frac{\text{Var}_\theta(X)}{(n+2\alpha)^2} = \frac{n\theta(1-\theta)}{(n+2\alpha)^2}.
$$

So the MSE is

$$
\text{MSE}(\theta;\delta_\alpha) = \frac{\alpha^2(1-2\theta)^2 + n\theta(1-\theta)}{(n+2\alpha)^2} = \frac{\alpha^2 + (n-4\alpha^2)\theta(1-\theta)}{(n+2\alpha)^2}.
$$

The dependence on $\theta$ vanishes exactly when $n - 4\alpha^2 = 0$, i.e. at $\alpha^* = \sqrt n/2$, giving the
constant risk

$$
R(\theta;\delta_{\alpha^*}) = \left(\frac{\alpha^*}{n+2\alpha^*}\right)^2 = \frac{n}{4(n+\sqrt n)^2}.
$$

Since $\delta_{\alpha^*}$ is the unique Bayes estimator for $\Lambda^* = \text{Beta}(\alpha^*,\alpha^*)$, it is the
unique minimax estimator, and $\Lambda^*$ is least favorable, with $r^* = \frac{n}{4(n+\sqrt n)^2}$. For $n=16$,
$\alpha^*=2$ and $\delta_{\alpha^*}(X) = \frac{X+2}{X+4}$.

It is worth asking why $\Lambda^*$ puts so much weight near $\theta=1/2$. $\Lambda^* = \text{Beta}(\sqrt n/2,\sqrt n/2)$
can be seen as a kind of "objective" prior, in that it isn't chosen from anyone's subjective belief — but it is a
very different object from the Jeffreys prior $\text{Beta}(1/2,1/2)$, which puts the *most* weight near the
boundary $\theta \in \{0,1\}$, where Fisher information is largest. $\Lambda^*$ instead concentrates near
$\theta=1/2$, because that is where squared-error estimation of $\theta$ is hardest — the least favorable prior
reflects difficulty of the estimation problem, not information content.

Being minimax, however, is not the same as being good throughout the parameter space. Compare $\delta_{\alpha^*}$
to the UMVU estimator $\delta_0(X) = X/n$, whose MSE is $\theta(1-\theta)/n$:

$$
\frac{\text{MSE}(\theta;\delta_0)}{\text{MSE}(\theta;\delta_{\alpha^*})} = \frac{\theta(1-\theta)/n}{n/4(n+\sqrt n)^2} = 4\theta(1-\theta)\left(1+n^{-1/2}\right)^2.
$$

This ratio is maximized at $\theta=1/2$, where $\delta_0$ is worse by only a factor $\approx 1+2n^{-1/2}$, shrinking
to nothing as $n \to \infty$. But elsewhere the picture reverses sharply: at $\theta=0.01$ the ratio is about
$0.04$, so for large $n$ the UMVU estimator beats the "optimal" minimax estimator by a factor of roughly $25$. The
minimax estimator spends everything on doing well at the single hardest point of the parameter space and pays a
severe price everywhere else.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="MSE of the UMVU estimator against the constant minimax risk for the binomial problem, showing UMVU winning everywhere except a narrow band around theta equals one half">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="208" text-anchor="middle" font-size="12" fill="currentColor">θ</text>
  <text x="18" y="30" font-size="12" fill="currentColor">MSE</text>

  <line x1="40" y1="55" x2="300" y2="55" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="44" y="49" font-size="11" fill="currentColor">minimax risk (constant)</text>

  <path d="M40,190 Q170,-110 300,190" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="198" y="72" font-size="11" fill="currentColor">UMVU risk θ(1-θ)/n</text>

  <line x1="170" y1="40" x2="170" y2="190" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">1/2</text>
</svg>
<figcaption>Away from θ = 1/2 the UMVU estimator X/n has far smaller MSE than the constant-risk minimax estimator;
the minimax estimator wins only in a thin band around the single hardest point, and pays for that everywhere
else in the parameter space.</figcaption>
</figure>

## Least favorable sequences

Some problems have no least favorable prior at all, typically because $\Theta$ is not compact. For
$X \sim N(\theta,1)$ with $\theta \in \mathbb{R}$, a least favorable prior would need to spread its mass over the
whole real line — something no proper prior can do. The supremum $\sup_\Lambda r_\Lambda$ can still be a
meaningful target even though no single prior attains it. Instead we look for a **least favorable sequence**:
priors $\Lambda_1,\Lambda_2,\dots$ with $r_{\Lambda_n} \to \sup_\Lambda r_\Lambda$.

**Theorem.** Suppose $\delta$ is an estimator and $\Lambda_1,\Lambda_2,\dots$ is a sequence of priors such that

$$
\sup_\theta R(\theta;\delta) = \lim_{n\to\infty} r_{\Lambda_n}.
$$

Then $\delta$ is minimax, the sequence $\{\Lambda_n\}$ is least favorable, and $r^* = \lim_n r_{\Lambda_n}$.

*Proof.* The argument mirrors the single-prior case. For any other estimator $\tilde\delta$ and any $n$,

$$
\sup_\theta R(\theta;\tilde\delta) \;\ge\; \int R(\theta;\tilde\delta)\,d\Lambda_n(\theta) \;\ge\; r_{\Lambda_n},
$$

so letting $n\to\infty$,

$$
\sup_\theta R(\theta;\tilde\delta) \;\ge\; \lim_{n\to\infty} r_{\Lambda_n} = \sup_\theta R(\theta;\delta),
$$

and $\delta$ is minimax. Also

$$
\lim_{n\to\infty} r_{\Lambda_n} \;\le\; r^* \;\le\; \sup_\theta R(\theta;\delta) = \lim_{n\to\infty} r_{\Lambda_n},
$$

forcing equality throughout, so the sequence is least favorable with $r^* = \lim_n r_{\Lambda_n}$. $\blacksquare$

Putting the single-prior and sequence versions together gives one picture of how the relevant quantities sit
relative to one another, for a generic estimator $\delta$ and a generic prior $\Lambda$:

$$
\sup_\theta R(\theta;\delta) \;\ge\; \inf_\delta \sup_\theta R(\theta;\delta) = r^* \;\ge\; \sup_\Lambda r_\Lambda \;\ge\; r_\Lambda.
$$

A minimax estimator $\delta^*$ collapses the first inequality to equality; a least favorable prior (or the limit
along a least favorable sequence) collapses the second.

## Why bother, given that minimax estimators are hard to find

Exact minimax estimators exist only in special cases; outside of simple examples, the sandwich above is used more
often to *bound* $r^*$ than to pin it down exactly. Two standard uses:

**Near-optimal estimators.** Given a practical estimator $\delta$ chosen for other reasons — ease of computation,
unbiasedness, a natural functional form, or a good inductive bias for the settings we actually expect — compute
its sup-risk and compare it to the Bayes risk of *any* Bayes estimator, for any prior. If the two are close, say
within $10\%$, then $\delta$ cannot be improved by more than $10\%$ by *any* estimator whatsoever, because $r^*$
is sandwiched between them.

**Problem hardness and minimax rates.** To quantify the difficulty of a *sequence* of problems — indexed, say, by
sample size $n$ — sandwich $r_n^*$ between an upper bound from some estimator $\delta_n$ and a lower bound from
some prior $\Lambda_n$:

$$
r_{\Lambda_n} \;\le\; r_n^* \;\le\; \sup_\theta R_n(\theta;\delta_n).
$$

If both bounds shrink (or grow) at the same rate in $n$, then $r_n^*$ must shrink (or grow) at that same rate,
which is called the problem's **minimax rate**.

A caveat applies to both uses, and the binomial example makes it vivid: the minimax risk is driven entirely by
the single hardest point (or hardest neighborhood) of the parameter space. A problem can be minimax-hard while
being easy almost everywhere that actually arises in practice, so a minimax bound is the right tool for some
questions and the wrong one for others — it might matter more what is happening away from the worst case than at
it.

## Sources

- Primary exposition, theorems, and both worked examples (sign-estimation and binomial): Berkeley STAT210A course
  reader, "Minimax Estimation," fall-2025 edition, §§1.1–1.5 —
  `docs/statistics/berkeley/stat210a/fall-2025/reader/minimax-estimation.md`; the near-identical fall-2026 edition,
  split as `docs/statistics/berkeley/stat210a/fall-2026/reader/minimax-estimation/01-definitions.md` through
  `04-bounding-the-minimax-risk.md`, was used to cross-check the derivations (it additionally carries the R code
  used to generate the lecture's risk-function and prior-density plots, referenced in the text below but not
  reproduced here).
- Terser bullet-note record of the same lecture, used to confirm notation and definitions and as the source of the
  open question about why the binomial least favorable prior concentrates near $\theta \approx 1/2$: fall-2024
  `docs/statistics/berkeley/stat210a/fall-2024/reader/minimax-estimation/01-least-favorable-priors.md` and
  `02-least-favorable-sequence.md`; fall-2025
  `docs/statistics/berkeley/stat210a/fall-2025/units/reader/minimax-estimation/01-introduction.md` through
  `03-3-least-favorable-sequence.md`.
- Referred to but not contained here: "Lecture 3" of the course, on unbiased/UMVU estimators and on the
  Beta–Binomial Bayes-estimator calculation, cited in both the fall-2025 and fall-2026 readers as prior material.
  The actual rendered plots of the sign-estimation risk function, the least-favorable-vs-Jeffreys prior densities,
  and the minimax-vs-UMVU MSE comparison are referenced in the source text (as a hosted image for fall-2025, and
  as embedded R plotting code for fall-2026) but are not themselves part of the supplied material; the two figures
  in this chapter are new schematic diagrams built from the shapes the text describes, not reproductions of the
  originals.

---

[← 66. Measure Theory for Probability](66-measure-theory-for-probability.md) · [Contents](index.md) · [68. Multiple Testing →](68-multiple-testing.md)
