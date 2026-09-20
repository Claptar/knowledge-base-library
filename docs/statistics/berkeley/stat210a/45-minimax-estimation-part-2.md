---
title: "45. Minimax Estimation (part 2)"
course: "Berkeley Stat 210A Fall 2024"
chapter: 45
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 45. Minimax Estimation (part 2)

## What this covers

This chapter introduces the **minimax criterion** for choosing an estimator — minimize the worst
case over the parameter, rather than average performance against a prior — and the one technique
the lecture develops for actually pinning down a minimax estimator: pair it with a **least
favorable prior** whose Bayes risk matches the worst-case risk exactly. Two examples are worked in
full (the sign of a truncated normal mean, and a binomial proportion), and the idea is then
extended to **least favorable sequences** of priors, for problems where no single prior is quite
enough. It assumes the language of decision theory from earlier in the course: a loss function, the
risk $R(\theta;\delta) = \mathbb{E}_\theta L(\theta,\delta(X))$, Bayes estimators, and Bayes risk.

## The minimax criterion

Every estimator built so far — MLE, Bayes, UMVU — was chosen by some other principle and then
evaluated by its risk function $R(\theta;\delta)$. Minimax turns this around: choose $\delta$ to
directly control the worst case,

$$
\underset{\delta}{\text{minimize}} \quad \sup_\theta R(\theta; \delta).
$$

The smallest achievable worst-case risk is the **minimax risk** of the problem,

$$
r^* = \inf_\delta \sup_\theta R(\theta; \delta),
$$

and an estimator $\delta^*$ is **minimax** if it attains it, $\sup_\theta R(\theta;\delta^*) = r^*$.

It helps to read this as a two-player zero-sum game. In the **minimax game**, the analyst moves
first and commits to an estimator $\delta$; then nature, playing adversarially, picks whichever
$\theta$ makes that $\delta$ look as bad as possible. Note carefully what nature does *not* control:
$X$ is still random, drawn from $P_\theta$ once $\theta$ is fixed — nature only chooses which $P_\theta$
generates it.

Compare this with the Bayes setup, which is the same game with the moves reversed — a **maximin
game**: nature moves first, but now with a *mixed strategy*, a prior $\Lambda$ over $\theta$, and the
analyst responds with whichever $\delta$ minimizes the resulting average risk (the Bayes estimator
for $\Lambda$). The goal of this chapter is to find nature's optimal mixed strategy in this game —
its Nash equilibrium — because that turns out to be exactly the tool for finding $\delta^*$.

## Least favorable priors

The link between the two games rests on one observation: **average-case risk is never worse than
worst-case risk.** For any proper prior $\Lambda$ and any fixed $\delta$,

$$
\int R(\theta;\delta)\, d\Lambda(\theta) \le \sup_\theta R(\theta;\delta),
$$

since averaging a function against a probability measure cannot exceed its supremum. Taking the
infimum over $\delta$ on both sides preserves the inequality, so the **Bayes risk** of $\Lambda$,

$$
r_\Lambda = \inf_\delta \int R(\theta;\delta)\, d\Lambda(\theta),
$$

satisfies $r_\Lambda \le \inf_\delta \sup_\theta R(\theta;\delta) = r^*$. If $\delta_\Lambda$ is a Bayes
estimator for $\Lambda$ (it attains the infimum), then $r_\Lambda = \int R(\theta;\delta_\Lambda)\,
d\Lambda(\theta)$ — so **the Bayes risk of any Bayes estimator, for any prior, is a lower bound on
$r^*$.** The best such bound comes from the **least favorable prior** $\Lambda^*$, the one that
maximizes this lower bound:

$$
r_{\Lambda^*} = \sup_\Lambda r_\Lambda.
$$

On the other side, $r^* = \inf_\delta \sup_\theta R(\theta;\delta) \le \sup_\theta R(\theta;\delta)$ for
*any particular* $\delta$ — the worst-case risk of any single estimator is an upper bound on $r^*$.
Putting the two together, for any prior $\Lambda$ and any estimator $\delta$,

$$
r_\Lambda \;\le\; r_{\Lambda^*} \;\le\; r^* \;\le\; \sup_\theta R(\theta;\delta).
$$

Everything in this chapter is the same idea applied to specific problems: **find a $\delta$ and a
$\Lambda$ that make the two outer bounds meet.** If they do, both inequalities in the sandwich
collapse and $r^*$ is pinned down exactly.

## The Bayes–minimax theorem

**Theorem.** Let $\Lambda$ be a prior with Bayes estimator $\delta_\Lambda$. If

$$
r_\Lambda = \sup_\theta R(\theta;\delta_\Lambda),
$$

then $\delta_\Lambda$ is minimax, $\Lambda$ is least favorable, and $r^* = r_\Lambda$. If $\delta_\Lambda$
is the unique Bayes estimator (up to almost-sure equality), $\delta_\Lambda$ is also the unique
minimax estimator.

*Proof.* Let $\delta$ be any other estimator. Chaining the average-vs-worst-case bound, the
optimality of $\delta_\Lambda$ among all estimators on average, and the hypothesis:

$$
\sup_\theta R(\theta;\delta) \;\ge\; \int R(\theta;\delta)\, d\Lambda(\theta)
\;\ge\; \int R(\theta;\delta_\Lambda)\, d\Lambda(\theta) \;=\; r_\Lambda \;=\; \sup_\theta R(\theta;\delta_\Lambda),
$$

where the middle inequality is strict whenever $\delta_\Lambda$ is the unique Bayes estimator and
$\delta$ differs from it on a set of positive $\Lambda$-measure. So every competitor has worst-case
risk at least that of $\delta_\Lambda$: it is minimax. Combined with the sandwich above, $r_\Lambda \le
r^* \le \sup_\theta R(\theta;\delta_\Lambda) = r_\Lambda$, forcing equality throughout, which also
makes $\Lambda$ least favorable. $\blacksquare$

This gives two checkable ways to certify a guess:

1. **Constant risk.** If $\delta_\Lambda$ has risk not depending on $\theta$, the hypothesis holds
   automatically — averaging a constant against any prior returns that same constant — so
   $\delta_\Lambda$ is minimax.
2. **A weaker, more useful version.** The risk need not be constant everywhere at all: it is enough
   that $R(\theta;\delta_\Lambda)$ attains its overall maximum at every point of $\mathrm{supp}(\Lambda)$.
   Averaging that maximum value against a prior sitting entirely on the argmax set still returns the
   maximum, which is exactly what the hypothesis needs.

One trap the lecture flags explicitly: showing that $\mathbb{E}_\Lambda\, R(\theta;\delta)$ is some
constant is **not** evidence of anything — $\theta$ has already been integrated out, so of course
the result doesn't depend on it. The constancy (or the argmax condition) has to hold in $\theta$,
*before* averaging.

## Example: the sign of a truncated normal mean

$X \sim N(\theta,1)$, but $\theta$ is known to satisfy $|\theta| \ge 1$, i.e. $\Theta = (-\infty,-1]
\cup [1,\infty)$. Estimate $g(\theta) = \operatorname{sgn}(\theta) \in \{-1,+1\}$ under squared error.

Try the two-point prior $\Lambda = \mathrm{Unif}(\{-1,+1\})$. By Bayes' rule with equal prior weights
and Gaussian likelihoods centred at $\pm 1$,

$$
\mathbb{P}_\Lambda(\theta = 1 \mid X = x) = \frac{\phi(x-1)}{\phi(x-1) + \phi(x+1)},
$$

and the Bayes estimator under squared error is the posterior mean of $g(\theta)$, which simplifies
(the common factor $e^{-(x^2+1)/2}$ cancels between numerator and denominator) to

$$
\delta_\Lambda(x) = \mathbb{E}_\Lambda(g(\theta)\mid X=x) = \frac{\phi(x-1)-\phi(x+1)}{\phi(x-1)+\phi(x+1)}
= \frac{e^x - e^{-x}}{e^x+e^{-x}} = \tanh(x).
$$

This risk is **not** constant in $\theta$ over the true parameter space — but it doesn't need to be.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Risk of the sign estimator tanh(X), peaking exactly at the two points where the least favorable prior sits">
  <rect x="140" y="20" width="80" height="160" fill="currentColor" fill-opacity="0.1"/>
  <line x1="40" y1="180" x2="320" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <path d="M60,150 C90,112 115,65 140,50" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M220,50 C245,65 270,112 300,150" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="140" cy="50" r="4" fill="currentColor"/>
  <circle cx="220" cy="50" r="4" fill="currentColor"/>
  <line x1="140" y1="180" x2="140" y2="186" stroke="currentColor" stroke-width="1.5"/>
  <line x1="220" y1="180" x2="220" y2="186" stroke="currentColor" stroke-width="1.5"/>
  <line x1="180" y1="180" x2="180" y2="186" stroke="currentColor" stroke-width="1"/>
  <text x="140" y="200" text-anchor="middle" font-size="12" fill="currentColor">-1</text>
  <text x="220" y="200" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="180" y="200" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="332" y="184" text-anchor="middle" font-size="12" fill="currentColor">&#952;</text>
  <text x="30" y="24" text-anchor="end" font-size="11" fill="currentColor">R(&#952;;&#948;)</text>
  <text x="180" y="35" text-anchor="middle" font-size="11" fill="currentColor">|&#952;| &#60; 1 excluded from &#920;</text>
  <text x="180" y="100" text-anchor="middle" font-size="11" fill="currentColor">supp(&#923;*) = {-1, 1}</text>
</svg>
<figcaption>The mean-squared error of &#948;<sub>&#923;</sub>(X) = tanh(X) as a function of &#952;. It is not
constant, but it peaks exactly at &#952; = &#8722;1, +1, the two points carrying all the mass of &#923; &#8212;
the edge of the parameter space, where the sign is hardest to read off from X. That is checkable
condition (2), not condition (1): the maximum of the risk is attained everywhere on the support of the
prior, which is enough.</figcaption>
</figure>

Away from the boundary the sign becomes easier to read off as $|\theta|$ grows, so the risk decays;
right at $|\theta|=1$ it is hardest, and that is precisely where $\Lambda$ puts its mass. So condition
(2) of the theorem holds, and $\tanh(X)$ is minimax for estimating the sign, with $\Lambda$ least
favorable.

## Example: a binomial proportion

$X \sim \mathrm{Binom}(n,\theta)$, estimate $\theta$ under squared error. Try a $\mathrm{Beta}(\alpha,\beta)$
prior, hoping to land on one whose Bayes estimator has constant risk. By symmetry take $\alpha=\beta$;
the Bayes (posterior-mean) estimator is

$$
\delta_\alpha(X) = \frac{X+\alpha}{n+2\alpha},
$$

which reads as the raw count $X$ padded with $\alpha$ pseudo-successes and $\alpha$ pseudo-failures
before normalizing. Its bias and variance are

$$
\mathbb{E}_\theta \delta_\alpha(X) = \frac{n\theta+\alpha}{n+2\alpha}
\;\Rightarrow\; \mathrm{Bias}(\theta;\delta_\alpha) = \frac{\alpha(1-2\theta)}{n+2\alpha},
\qquad
\mathrm{Var}_\theta \delta_\alpha(X) = \frac{n\theta(1-\theta)}{(n+2\alpha)^2},
$$

so

$$
\mathrm{MSE}(\theta;\delta_\alpha) = (2\alpha+n)^{-2}\Big[\alpha^2(1-2\theta)^2 + n\theta(1-\theta)\Big]
= (2\alpha+n)^{-2}\Big[\alpha^2 + (n-4\alpha^2)\,\theta(1-\theta)\Big].
$$

The whole $\theta$-dependence sits in the coefficient of $\theta(1-\theta)$, so it vanishes exactly
when $n - 4\alpha^2 = 0$, i.e. at $\alpha^* = \sqrt n / 2$. At that choice the risk is constant in
$\theta$,

$$
\mathrm{MSE}(\theta;\delta_{\alpha^*}) \equiv \frac{n/4}{(n+\sqrt n)^2} = r^*,
\qquad
\delta_{\alpha^*}(X) = \frac{\sqrt n/2 + X}{\sqrt n + n},
$$

and constant risk is checkable condition (1): $\delta_{\alpha^*}$ is minimax, with least favorable
prior $\Lambda^* = \mathrm{Beta}(\sqrt n/2,\sqrt n/2)$, a symmetric density peaked at $\theta = 1/2$.

The lecture poses, without resolving in the notes, the question of *why* $\Lambda^*$ concentrates at
$\theta=1/2$. One thing the algebra above already says: the only $\theta$-dependence in the MSE of any
symmetric $\delta_\alpha$ runs through $\theta(1-\theta)$, the variance of $X$ itself, which is largest
at $\theta=1/2$ — so $1/2$ is where a symmetric conjugate prior has the least room to help, and as
$\alpha^*=\sqrt n/2 \to \infty$ with $n$, the least favorable prior concentrates ever more tightly
there.

## Least favorable sequences

Sometimes no single proper prior attains the supremum $\sup_\Lambda r_\Lambda$ exactly — only a
sequence of priors approaches it. A sequence $\Lambda_1,\Lambda_2,\dots$ is **least favorable** if

$$
r_{\Lambda_n} \to \sup_\Lambda r_\Lambda.
$$

**Theorem.** If $\delta$ satisfies $\sup_\theta R(\theta;\delta) = \lim_n r_{\Lambda_n}$ for such a
sequence, then $\delta$ is minimax and $(\Lambda_n)$ is least favorable.

*Proof.* For any competitor $\tilde\delta$ and every $n$,

$$
\sup_\theta R(\theta;\tilde\delta) \ge \int R(\theta;\tilde\delta)\, d\Lambda_n(\theta) \ge r_{\Lambda_n},
$$

so $\sup_\theta R(\theta;\tilde\delta) \ge \sup_n r_{\Lambda_n} \ge \lim_n r_{\Lambda_n} = \sup_\theta
R(\theta;\delta)$. Hence $\lim_n r_{\Lambda_n} \le r^* \le \sup_\theta R(\theta;\delta) = \lim_n
r_{\Lambda_n}$, forcing equality throughout. $\blacksquare$

**Example.** $X \sim N_d(\theta,I_d)$, estimate $\theta$ under squared error. The identity estimator
$\delta_0(X) = X$ is unbiased with risk $R(\theta;\delta_0) = d$ for every $\theta$ — constant risk,
which is suggestive, but there is no *proper* prior whose Bayes estimator is exactly $X$: the Bayes
estimator under any proper Gaussian prior $N_d(0,\tau^2 I_d)$ shrinks $X$ toward $0$, never leaving it
unchanged for finite $\tau^2$. So reach for a sequence of increasingly diffuse priors, $\Lambda_n =
N_d(0, nI_d)$, whose posterior mean is the shrinkage estimator

$$
\delta_{\zeta_n}(X) = (1-\zeta_n)X, \qquad \zeta_n = \frac{1}{n+1} \to 0.
$$

Its risk decomposes into squared bias plus variance,
$\mathrm{MSE}(\theta;\delta_{\zeta_n}) = \zeta_n^2\|\theta\|^2 + (1-\zeta_n)^2 d$, and averaging over
$\theta \sim N_d(0,nI_d)$ (so $\mathbb{E}\|\theta\|^2 = nd$) gives the Bayes risk

$$
r_{\Lambda_n} = \zeta_n^2\, nd + (1-\zeta_n)^2 d = d\left(\frac{n}{(1+n)^2} + \frac{n^2}{(1+n)^2}\right) \to d.
$$

This limit matches the constant risk of $\delta_0$, so by the theorem $(\Lambda_n)$ is a least
favorable sequence, $\delta_0(X) = X$ is minimax, and $r^* = d$. The notes add a parenthetical
question here — "*(but inadmissible?)*" — flagging, without developing it, that being minimax says
nothing about being admissible; that is a separate question the lecture leaves open.

## Using minimax bounds without a minimax estimator

The theorem above is really a recipe for bounding $r^*$, and the two directions don't have to be
matched to be useful on their own:

- **Upper bound.** Any estimator $\delta$ gives $r^* \le \sup_\theta R(\theta;\delta)$ (with equality
  iff $\delta$ is minimax).
- **Lower bound.** Any prior $\Lambda$ gives $r^* \ge \int R(\theta;\delta_\Lambda)\, d\Lambda(\theta)$
  (with equality iff $\Lambda$ is least favorable).

Exact minimax estimators are hard to find, but these one-sided bounds are a routine tool for
characterizing how hard a problem is — especially the lower bound. A typical use: propose a
practical estimator $\delta$, then exhibit a prior $\Lambda$ for which $r_\Lambda$ is close to
$\sup_\theta R(\theta;\delta)$ — exactly, at the same rate, or asymptotically — and conclude that
$\delta$ cannot be improved by much. Another: quantify the intrinsic difficulty of a whole problem by
its minimax rate as some asymptotic parameter (sample size, dimension) grows.

**Caveat.** A problem can be easy over most of the parameter space and only pathologically hard in
some corner nobody encounters in practice — the minimax criterion, being a pure worst case, cannot
tell the difference.

## Sources

- Berkeley STAT 210A, fall 2025, Lecture 13 ("Minimax Estimation"), handwritten notes: [`01-minimax-estimation.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture13-minimax.pdf) (minimax risk, the minimax/Bayes game, least favorable priors, the Bayes–minimax theorem, the truncated-normal sign example) and [`02-example-binomial.md`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture13-minimax.pdf) (the binomial example, least favorable sequences, the multivariate normal example, and the practical bounding strategy).
- The same lecture (fall 2026, Lecture 13) appears in the library with identical content; only one copy was used, per the rule to take the clearest single treatment rather than repeat it.
- No slide deck, transcript, or problem set was supplied for this lecture. The source is a model's reconstruction of a handwritten PDF with no text layer — the frontmatter on both files flags every equation as unverified, so treat the displayed algebra as a pointer into the original scan, worth checking against it before citing.
- Two questions are posed in the notes and left open there rather than answered: why $\Lambda^*$ concentrates at $\theta=1/2$ in the binomial example (addressed above with a direct reading of the derived MSE, not asserted as the lecture's own answer), and whether $X$ is *admissible* as an estimator of a multivariate normal mean despite being minimax — admissibility itself is a topic this lecture gestures at but does not develop.

---

[← 44. Empirical Bayes, James-Stein](44-empirical-bayes-james-stein.md) · [Contents](index.md) · [46. Hypothesis Testing and Power Functions →](46-hypothesis-testing-and-power-functions.md)
