---
title: "43. Minimax Estimation (part 1)"
course: "Berkeley Stat 210A"
chapter: 43
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 43. Minimax Estimation (part 1)

## What this covers

An estimator can be judged by its risk against one adversarially chosen parameter value rather
than by an average risk under a prior. This chapter defines that criterion — minimax risk — and
develops the main tool for finding or certifying a minimax estimator: a **least favorable prior**,
which turns nature's adversarial choice of $\theta$ into a specific randomized strategy against
which Bayes and minimax analysis coincide. It assumes the decision-theoretic setup of earlier
lectures: a risk function $R(\theta;\delta)$ for an estimator $\delta$, and Bayes risk and Bayes
estimators relative to a prior.

## Minimax risk

The worst-case criterion asks for an estimator that minimizes the risk at the single most
unfavorable parameter value:

$$\text{minimize}_\delta \quad \sup_\theta R(\theta;\delta).$$

The best achievable value of this worst-case risk is the **minimax risk** of the problem,

$$r^* = \inf_\delta \sup_\theta R(\theta;\delta),$$

and an estimator $\delta^*$ achieving it, $\sup_\theta R(\theta;\delta^*) = r^*$, is called
**minimax**.

This has a game-theoretic reading: the analyst picks $\delta$, and then nature picks $\theta$ to
maximize the resulting risk. The important point is *what* nature is choosing — nature picks the
parameter $\theta$ adversarially, not the data $X$; the randomness in $X\mid\theta$ is still
whatever the model says it is. Compare this with the Bayes setup, where nature's move is
constrained in advance to a known distribution: nature is playing a fixed **mixed strategy** (the
prior) rather than an arbitrary one. This suggests looking for the mixed strategy for nature that
is optimal in a game-theoretic sense — a Nash equilibrium strategy — and that strategy is exactly
what a least favorable prior turns out to be.

## Least favorable priors

The link between minimax and Bayes analysis rests on one observation: **average-case risk is at
most worst-case risk**. For any prior $\Lambda$ (proper, for now) and any estimator $\delta$,

$$\int R(\theta;\delta)\,d\Lambda(\theta) \le \sup_\theta R(\theta;\delta).$$

Taking the infimum over $\delta$ on both sides,

$$r_\Lambda = \inf_\delta \int R(\theta;\delta)\,d\Lambda(\theta) \le \inf_\delta \sup_\theta R(\theta;\delta) = r^*.$$

If $\delta_\Lambda$ is a Bayes estimator for $\Lambda$, the infimum on the left is attained, so
$r_\Lambda = \int R(\theta;\delta_\Lambda)\,d\Lambda(\theta)$. Hence **the Bayes risk of any Bayes
estimator, for any prior, is a lower bound on the minimax risk** $r^*$.

Since there is a lower bound for every prior, it is natural to ask which prior gives the best one.
A **least favorable prior** $\Lambda^*$ is one attaining

$$r_{\Lambda^*} = \sup_\Lambda r_\Lambda.$$

Symmetrically, the worst-case risk of *any* estimator is an upper bound on $r^*$. Putting the two
bounds together:

$$\sup_\theta R(\theta;\delta) \;\ge\; r^* \;\ge\; r_{\Lambda^*} \;\ge\; r_\Lambda,$$

for an arbitrary estimator $\delta$ on the left and an arbitrary prior $\Lambda$ on the right. The
strategy for exhibiting a minimax estimator and a least favorable prior simultaneously is to find a
$\delta$ and a $\Lambda$ that collapse this whole chain to equality.

## The theorem: when a Bayes estimator is minimax

**Theorem.** Suppose $\delta_\Lambda$ is Bayes for a prior $\Lambda$ and
$r_\Lambda = \sup_\theta R(\theta;\delta_\Lambda)$ — that is, the *average* risk of $\delta_\Lambda$
under $\Lambda$ equals its *worst-case* risk. Then:

(a) $\delta_\Lambda$ is minimax;

(b) if $\delta_\Lambda$ is the unique Bayes estimator for $\Lambda$ (up to a.s. equality), it is the
unique minimax estimator;

(c) $\Lambda$ is a least favorable prior.

**Proof.**

(a) Let $\tilde\delta$ be any other estimator. Then

$$
\sup_\theta R(\theta;\tilde\delta) \;\ge\; \int R(\theta;\tilde\delta)\,d\Lambda(\theta)
\;\ge\; \int R(\theta;\delta_\Lambda)\,d\Lambda(\theta) \;=\; r_\Lambda \;=\; \sup_\theta R(\theta;\delta_\Lambda),
$$

where the middle inequality holds because $\delta_\Lambda$ is Bayes for $\Lambda$ (it minimizes
Bayes risk), and the last equality is the hypothesis. So every estimator's worst-case risk is at
least $\sup_\theta R(\theta;\delta_\Lambda)$, which means $\delta_\Lambda$ itself achieves the
minimax risk.

(b) If $\delta_\Lambda$ is the unique Bayes estimator, the middle inequality above is strict for any
$\tilde\delta \ne \delta_\Lambda$, so $\sup_\theta R(\theta;\tilde\delta) > \sup_\theta R(\theta;\delta_\Lambda)$
for every competitor: $\delta_\Lambda$ is the unique minimizer of the worst-case risk.

(c) Let $\tilde\Lambda$ be any other prior. Then

$$
r_{\tilde\Lambda} = \inf_\delta \int R(\theta;\delta)\,d\tilde\Lambda(\theta) \le \int R(\theta;\delta_\Lambda)\,d\tilde\Lambda(\theta)
\le \sup_\theta R(\theta;\delta_\Lambda) = r_\Lambda.
$$

No prior gives a larger Bayes-risk lower bound than $\Lambda$ does, so $\Lambda$ is least
favorable. $\blacksquare$

## A checkable condition — and a mistake to avoid

The theorem turns the hunt for a minimax estimator into a checkable condition: does the *average*
risk of a Bayes estimator equal its *worst-case* risk?

One way this is guaranteed is if the risk function is constant:

1. $R(\theta;\delta_\Lambda)$ does not depend on $\theta$ at all (an "equalizer rule"), or, more
   generally,
2. $\Lambda$ places all of its mass on the set where $R(\theta;\delta_\Lambda)$ attains its maximum:
   $\Lambda(\{\theta : R(\theta;\delta_\Lambda) = \max_\zeta R(\zeta;\delta_\Lambda)\}) = 1$.

Condition 2 is strictly weaker than condition 1: the risk function need not be flat everywhere, it
only has to sit at its peak value everywhere the prior actually puts mass. Outside the support of
$\Lambda$ the risk is free to dip, since the average under $\Lambda$ never sees that dip.

<figure>
<svg viewBox="0 0 340 260" role="img" aria-label="A risk function that is flat at its maximum exactly on the support of the least favorable prior">
  <rect x="120" y="20" width="100" height="215" fill="currentColor" fill-opacity="0.08"/>
  <path d="M40,95 C70,95 90,45 120,45 L220,45 C250,45 270,95 300,95" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="40" y1="95" x2="300" y2="95" stroke="currentColor" stroke-width="1"/>
  <line x1="120" y1="20" x2="120" y2="225" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="220" y1="20" x2="220" y2="225" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <path d="M120,225 Q145,165 170,165 Q195,165 220,225" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="225" x2="300" y2="225" stroke="currentColor" stroke-width="1"/>
  <text x="42" y="18" font-size="12" fill="currentColor">R(&#952;; &#948;&#923;)</text>
  <text x="42" y="150" font-size="12" fill="currentColor">&#955;(&#952;)</text>
  <text x="170" y="248" text-anchor="middle" font-size="12" fill="currentColor">supp(&#923;)</text>
  <text x="304" y="229" font-size="12" fill="currentColor">&#952;</text>
</svg>
<figcaption>The risk function R(&#952;; &#948;&#923;) attains its maximum value on a plateau, and the
least favorable prior &#923; puts all of its mass on that plateau — it never has to average in the
lower risk outside it. This is condition 2: the risk need not be flat everywhere, only on
supp(&#923;).</figcaption>
</figure>

The lecture flagged a specific mistake on an exam: writing that "$r_\Lambda$ is constant" proves
nothing. $r_\Lambda$ is already a single number — a constant by definition, since it is an average
over $\theta$ — so the phrase doesn't assert anything. The condition that actually does the work is
that the *risk function* $\theta \mapsto R(\theta;\delta_\Lambda)$ is constant (or constant on
$\operatorname{supp}(\Lambda)$), which is a statement about a function of $\theta$, not about the
single number $r_\Lambda$.

## Worked example: a binomial proportion

Let $X \sim \mathrm{Binom}(n,\theta)$ and estimate $\theta$ under squared error loss. Try a
$\mathrm{Beta}(\alpha,\beta)$ prior, hoping to land on one that makes the risk of the resulting
Bayes estimator constant in $\theta$. The Bayes estimator (posterior mean) is

$$\delta_{\alpha,\beta}(X) = \frac{\alpha+X}{\alpha+\beta+n}.$$

Its risk splits into variance plus squared bias:

$$
\begin{aligned}
R(\theta;\delta_{\alpha,\beta}) &= \mathbb{E}_\theta\!\left[\left(\frac{\alpha+X}{\alpha+\beta+n}-\theta\right)^2\right] \\
&= \operatorname{Var}_\theta\!\left(\frac{X}{\alpha+\beta+n}\right) + \left(\frac{\alpha+\theta n}{\alpha+\beta+n}-\theta\right)^2 \\
&= (\alpha+\beta+n)^{-2}\Big[n\theta(1-\theta) + \big(\alpha - (\alpha+\beta)\theta\big)^2\Big] \\
&\propto_\theta \underbrace{\big[(\alpha+\beta)^2 - n\big]}_{\text{set }=\,0}\theta^2 + \underbrace{\big[n - 2\alpha(\alpha+\beta)\big]}_{\text{set }=\,0}\theta + \alpha^2.
\end{aligned}
$$

Killing the $\theta^2$ and $\theta$ coefficients makes the risk constant in $\theta$, which is
exactly condition 1 above. Setting $(\alpha+\beta)^2 = n$ and $2\alpha(\alpha+\beta) = n$ gives
$\alpha+\beta = \sqrt n$ and then $2\alpha\sqrt n = n$, so

$$\alpha = \beta = \frac{\sqrt n}{2}.$$

So $\mathrm{Beta}\!\left(\tfrac{\sqrt n}{2}, \tfrac{\sqrt n}{2}\right)$ is least favorable, and by
the theorem the corresponding Bayes estimator

$$\delta^* = \frac{X + \sqrt n/2}{n + \sqrt n}$$

is minimax. Two things are worth noting about how this worked. First, two equations
($\theta^2$-coefficient and $\theta$-coefficient both zero) had to be satisfied by two unknowns
$\alpha,\beta$, and they happened to be consistent — that is not guaranteed in general, and this
example is a case of getting lucky rather than a template that always closes. Second, the
resulting least favorable prior puts more and more of its mass near $\theta = 1/2$ as $n$ grows
(a symmetric Beta with both parameters equal to $\sqrt n / 2$ concentrates there): the lecture left
open, as a question rather than a resolved point, *why* the hardest case for estimating a binomial
proportion should concentrate so much weight at $\theta = 1/2$.

## When there is no least favorable prior: sequences

A least favorable prior need not exist. If the parameter space isn't compact, the prior that
"should" make nature's move hardest may need to spread mass everywhere, which is not a proper
distribution. For $X \sim N(\theta,1)$ with $\theta \in \mathbb{R}$, the natural candidate is a flat
prior over the whole real line — not a proper prior at all.

The fix is to work with a **sequence** of priors instead of a single one. A sequence
$\Lambda_1,\Lambda_2,\dots$ is **least favorable** if

$$r_{\Lambda_n} \to \sup_\Lambda r_\Lambda.$$

**Theorem.** Suppose $\Lambda_1,\Lambda_2,\dots$ is a sequence of priors and $\delta$ satisfies

$$\sup_\theta R(\theta;\delta) = \lim_n r_{\Lambda_n}.$$

Then (a) $\delta$ is minimax, and (b) $\Lambda_1,\Lambda_2,\dots$ is a least favorable sequence.

**Proof.**

(a) Let $\tilde\delta$ be any other estimator. For every $n$,

$$\sup_\theta R(\theta;\tilde\delta) \ge \int R(\theta;\tilde\delta)\,d\Lambda_n(\theta) \ge r_{\Lambda_n},$$

so

$$\sup_\theta R(\theta;\tilde\delta) \ge \sup_n r_{\Lambda_n} \ge \lim_n r_{\Lambda_n} = \sup_\theta R(\theta;\delta).$$

Since $\tilde\delta$ was arbitrary, $\delta$ achieves the minimax risk.

(b) For any prior $\Lambda$,

$$r_\Lambda = \int R(\theta;\delta_\Lambda)\,d\Lambda(\theta) \le \int R(\theta;\delta)\,d\Lambda(\theta) \le \sup_\theta R(\theta;\delta) = \lim_n r_{\Lambda_n}.$$

So no prior's Bayes risk exceeds $\lim_n r_{\Lambda_n}$, which is therefore $\sup_\Lambda r_\Lambda$,
and it is approached along the sequence by construction. $\blacksquare$

Putting the proper-prior and sequence versions together gives the general picture: for a generic
estimator $\delta$ and generic prior $\Lambda$,

$$
\sup_\theta R(\theta;\delta) \;\ge\; \inf_\delta \sup_\theta R(\theta;\delta) \;\ge\; \sup_\Lambda r_\Lambda \;\ge\; r_\Lambda,
$$

where the middle term equals $\sup_\theta R(\theta;\delta^*)$ if a minimax estimator $\delta^*$
exists, and the third term equals $r_{\Lambda^*}$ if a least favorable prior $\Lambda^*$ exists —
but neither has to.

## Bounding minimax risk

Actually finding a minimax estimator is hard in most problems. In practice, minimax **bounds** are
the workhorse, used to characterize how hard an estimation problem is, especially from below:

- **Upper bound**: for any estimator $\delta$, $r^* \le \sup_\theta R(\theta;\delta)$ (with equality
  iff $\delta$ is minimax).
- **Lower bound**: for any prior $\Lambda$, $r^* \ge \int R(\theta;\delta_\Lambda)\,d\Lambda(\theta)$
  (with equality iff $\Lambda$ is least favorable).

Two typical uses of this pair of bounds:

- Propose a practical estimator $\delta$, then find a prior $\Lambda$ whose Bayes risk is close to
  $\sup_\theta R(\theta;\delta)$ — exactly, at the same rate, or asymptotically. This lets you
  conclude $\delta$ cannot be improved by much, without ever exhibiting the exact minimax
  estimator.
- Quantify the intrinsic difficulty of an estimation problem via its minimax *rate* in some
  asymptotic regime, again without pinning down the exact minimax risk or estimator.

**Caveat.** A minimax bound is set by the single worst $\theta$. A problem can be easy throughout
most of the parameter space and only pathologically hard in some corner that is never encountered
in practice — so a large minimax risk does not by itself mean the problem is hard everywhere.

## Sources

All from *Berkeley STAT 210A*, handwritten lecture notes for lecture 12 (the notes themselves are
dated 10/5/2021, filed under the `fall-2024` course directory as `lecture12-F24`), converted from a
scanned PDF with no text layer — the conversion is model-reconstructed and flagged
`fidelity: reconstructed`, so equations here should be checked against the original scan before
being cited further:

- `01-minimax-estimation.md` — minimax risk, the game-theoretic reading, the average-vs-worst-case
  observation, and the inequality chain defining a least favorable prior.
- `02-theorem.md` — the theorem that a Bayes estimator with worst-case risk equal to its Bayes risk
  is minimax (and the prior least favorable), its proof, the checkable condition (constant risk /
  prior supported on the risk-maximizing set), and the exam-mistake remark.
- `03-example-binomial.md` — the worked binomial example with $\mathrm{Beta}(\alpha,\beta)$ priors.
- `04-least-favorable-sequence.md` — least favorable sequences for non-compact parameter spaces,
  the corresponding theorem and proof, the general inequality picture, and the discussion of
  minimax bounds and their caveat.

No slides, transcript, or exercise set were supplied for this lecture. The lecture posed but did
not answer the question of why the least favorable binomial prior concentrates near $\theta=1/2$;
that is left open here as it was left open in the source.

---

[← 42. Empirical Bayes and James-Stein](42-empirical-bayes-and-james-stein.md) · [Contents](index.md) · [44. Empirical Bayes, James-Stein →](44-empirical-bayes-james-stein.md)
