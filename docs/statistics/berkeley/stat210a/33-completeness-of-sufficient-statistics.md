---
title: "33. Completeness of Sufficient Statistics"
course: "Berkeley Stat 210A Fall 2024"
chapter: 33
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 33. Completeness of Sufficient Statistics

## What this covers

This chapter answers: given a sufficient statistic, how do you tell whether it has been reduced
as far as it can go, and how do you certify that in practice rather than by the ad-hoc
"can I find two things with the same expectation" argument used to *disprove* minimality? The
tool is **completeness**. It assumes the reader already has sufficiency and minimal sufficiency
(the order-statistic and likelihood-ratio arguments from the previous lecture) and knows what a
natural exponential family looks like. The lecture's own outline promised a third topic, Basu's
theorem, as a consequence of completeness; the supplied notes stop before reaching it, mid-way
through the proof that completeness implies minimality, so that proof is given here only as far
as the source goes and Basu's theorem is not covered.

## Completeness: the definition

A statistic $T(X)$ is **complete** for a family $\mathcal P = \{P_\theta : \theta \in \Theta\}$ if,
for every (measurable) function $f$,

$$\mathbb{E}_\theta f(T(X)) = 0 \quad \text{for all } \theta \implies f(T(X)) \overset{\text{a.s.}}{=} 0 \quad \text{for all } \theta.$$

In words: the only unbiased estimator of zero that can be built out of $T$ is the zero function
itself, almost surely. Equivalently, there is no room to construct two *different* functions of
$T$ whose expectations happen to agree for every $\theta$ — because if $g_1(T)$ and $g_2(T)$ had
the same expectation under every $\theta$, then $f = g_1 - g_2$ would be a nonzero unbiased
estimator of zero, violating completeness.

The name comes from an older idea: the family of induced distributions
$\mathcal P^T = \{P_\theta^T : \theta \in \Theta\}$ is a "complete basis" with respect to the
inner product $\langle f, P_\theta^T\rangle = \int f(t)\, dP_\theta^T(t)$ — completeness says
this basis is rich enough that nothing orthogonal to every $P_\theta^T$ survives. (See Homework 3
for more on this.)

## Where minimal sufficiency is not enough: the Laplace location family

Recall the Laplace (double-exponential) location family, whose minimal sufficient statistic is
the full vector of order statistics $S = (X_{(i)})_{i=1}^n$. Is $S$ complete?

No. Let $M(S) = \operatorname{median}(X)$ and $\bar X(S) = \frac1n\sum_i X_i$ — both are functions
of $S$. The Laplace density is symmetric about $\theta$, so both the mean and the median are
unbiased for $\theta$:

$$\mathbb{E}_\theta \bar X = \mathbb{E}_\theta M = \theta \quad \text{for every } \theta,$$

hence

$$\mathbb{E}_\theta\big[\bar X(S) - M(S)\big] = 0 \quad \text{for all } \theta,$$

while $\bar X(S) - M(S)$ is certainly not almost surely zero — the sample mean and the sample
median of a finite sample essentially never coincide. So $f = \bar X - M$ is a nonzero function of
$S$ that is an unbiased estimator of zero for every $\theta$: $S$ fails completeness. Minimal
sufficiency only guarantees that $S$ cannot be *shrunk* without losing information; it says
nothing about whether $S$ still carries "extra fluff" — internal structure, like the gap between
mean and median, that never touches $\theta$ but keeps two different functions of $S$ from being
forced to agree.

## Where it works: the uniform upper endpoint

Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} \mathcal U[0,\theta]$, $\theta \in (0,\infty)$, with
minimal sufficient statistic $T(X) = X_{(n)}$. Is $T$ complete?

First find the density of $T$:

$$\mathbb{P}_\theta(T \le t) = \left(\frac{t}{\theta}\wedge 1\right)^n = \left(\frac{t}{\theta}\right)^n \wedge 1
\quad\implies\quad
p_\theta(t) = \frac{d}{dt}\mathbb{P}_\theta(T\le t) = n\,\frac{t^{n-1}}{\theta^n}\,\mathbf 1\{t \le \theta\}.$$

Now suppose $\mathbb{E}_\theta f(T) = 0$ for every $\theta > 0$:

$$0 = \frac{n}{\theta^n}\int_0^\theta f(t)\, t^{n-1}\, dt \quad \text{for all } \theta > 0
\quad\implies\quad
\int_0^\theta f(t)\, t^{n-1}\, dt = 0 \quad \text{for all } \theta > 0.$$

Differentiating both sides in $\theta$ (fundamental theorem of calculus) gives
$f(\theta)\,\theta^{n-1} = 0$ for almost every $\theta > 0$. Since $\theta^{n-1} \ne 0$ on
$(0,\infty)$, this forces $f(\theta) = 0$ almost everywhere. So $T = X_{(n)}$ is complete.

The contrast with the Laplace example is the point: here the family of densities $\{p_\theta\}$
sweeps out shapes rich enough, as $\theta$ ranges over $(0,\infty)$, that an integral vanishing
against $t^{n-1}$ for *every* upper limit $\theta$ pins $f$ down to zero everywhere. In the
Laplace case the order statistics carry more than the family needs, leaving room for two
different functions to cancel.

## Full-rank exponential families are automatically complete

This suggests looking for a general sufficient condition on a family that guarantees completeness
of its natural sufficient statistic, rather than checking case by case.

Suppose $\mathcal P = \{P_\eta : \eta \in \Xi\}$ has densities in natural exponential family form,

$$p_\eta(x) = e^{\eta' T(x) - A(\eta)}\, h(x).$$

**Definition.** $\mathcal P$ is **full rank** if $T(X)$ satisfies no linear constraint — there is
no $\beta \ne 0$ and $\alpha$ with $\beta' T(X) \overset{\text{a.s.}}{=} \alpha$ — and $\Xi$
contains an open set. If $\mathcal P$ is not full rank, it is **curved**.

(If $T(x)$ does satisfy a linear constraint, $\mathcal P$ can still be full rank once described
by a lower-dimensional sufficient statistic — curvature is a property of the pairing of $T$ with
$\Xi$, not something that survives re-parametrizing away the redundant coordinate.)

**Theorem.** If $\mathcal P$ is full rank, then $T(X)$ is complete sufficient. (Proof in Lehmann
& Romano, Theorem 4.3.1.)

**Proof idea.** Without loss of generality take $T(X) = X$ itself, $p_\eta(x) = e^{\eta'x - A(\eta)}$,
with $0$ in the interior of $\Xi$. Suppose $\mathbb{E}_\eta f(X) = 0$ for every $\eta$, and split
$f = f^+ - f^-$ into its positive and negative parts. Writing $d\tilde\nu^{\pm}(x) = f^{\pm}(x)\,d\mu(x)$,
the hypothesis says

$$\int e^{\eta' x}\, d\tilde\nu^+(x) = \int e^{\eta' x}\, d\tilde\nu^-(x) \quad \text{for all } \eta$$

— that is, $\tilde\nu^+$ and $\tilde\nu^-$ have the *same moment generating function* on a
neighbourhood of $0$ (which exists because $\Xi$ contains an open set). Uniqueness of moment
generating functions then forces $\tilde\nu^+ = \tilde\nu^-$, i.e. $f^+ = f^-$, i.e. $f = 0$
almost everywhere. That is exactly completeness.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Parameter space showing a full-rank region containing an open disk, a curved one-dimensional family that does not, and a one-dimensional full-rank interval">
  <line x1="40" y1="20" x2="40" y2="190" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="190" x2="180" y2="190" stroke="currentColor" stroke-width="1"/>
  <text x="185" y="194" font-size="12" fill="currentColor">&#951;&#8321;</text>
  <text x="26" y="24" font-size="12" fill="currentColor">&#951;&#8322;</text>
  <circle cx="115" cy="110" r="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="115" y="113" text-anchor="middle" font-size="11" fill="currentColor">full rank</text>
  <path d="M 55 165 Q 95 70 160 130" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="150" y="150" font-size="11" fill="currentColor">curved</text>
  <line x1="240" y1="110" x2="340" y2="110" stroke="currentColor" stroke-width="1"/>
  <rect x="265" y="106" width="55" height="8" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <text x="290" y="140" text-anchor="middle" font-size="11" fill="currentColor">full rank, s = 1</text>
  <text x="290" y="95" text-anchor="middle" font-size="11" fill="currentColor">&#926; &#8834; &#8477;</text>
</svg>
<figcaption>Left: a two-dimensional parameter space $\Xi \subset \mathbb{R}^2$. A subset that
contains an open disk is full rank; a one-dimensional curve threading through the same space,
however long, contains no open set and is curved. Right: full rank does not require $s > 1$ — an
open interval inside a one-dimensional $\Xi \subset \mathbb{R}$ is already an open set, so the
family is full rank with $s = 1$.</figcaption>
</figure>

## Complete sufficiency implies minimal sufficiency

The exponential-family theorem manufactures complete statistics; the next result says why
completeness was worth having in the first place — it automatically buys minimality, so there is
no need to separately run the likelihood-ratio argument.

**Theorem.** If $T(X)$ is complete and sufficient for $\mathcal P$, then $T(X)$ is minimal
sufficient.

The Laplace example above shows the converse fails: $S = (X_{(i)})$ is minimal sufficient but not
complete. So completeness is the strictly stronger property, and this theorem is the one-directional
payoff for having it.

The general strategy for proving completeness statements, stated in the lecture as a standing
remark: **to show two statistics are almost-surely equal, show they have the same expectation
under every $\theta$, then invoke completeness.** This is the pattern behind the proof that
follows.

**Proof (as recorded).** Let $S(X)$ be a minimal sufficient statistic. Define

$$\bar T(S(X)) = \mathbb{E}[T(X) \mid S(X)]$$

— this is a genuine statistic, with no residual $\theta$-dependence, precisely because $S$ is
sufficient. The claim to be shown is

$$\bar T(S(X)) \overset{\text{a.s.}}{=} T(X).$$

Since $S$ is minimal sufficient, it is a function of every other sufficient statistic; in
particular $S(X) \overset{\text{a.s.}}{=} f(T(X))$ for some function $f$. Let

$$g(t) = t - \bar T(f(t)),$$

so that $g(T(X)) = T(X) - \bar T(S(X))$ is exactly the discrepancy the claim wants to rule out.
Its expectation is

$$\mathbb{E}_\theta[g(T(X))] = \mathbb{E}_\theta T(X) - \mathbb{E}_\theta[\bar T(S(X))].$$

The lecture's notes break off here, mid-computation, before finishing the argument. The standing
"game plan" stated just above tells us where this is headed — $g(T(X))$ is to be shown to have
expectation zero under every $\theta$ (which the tower property applied to $\bar T(S(X)) =
\mathbb{E}[T(X)\mid S(X)]$ would give), and completeness of $T$ then forces
$g(T(X)) \overset{\text{a.s.}}{=} 0$, i.e. $T(X) \overset{\text{a.s.}}{=} \bar T(S(X))$ for every
$\theta$, which is exactly $T$ expressed as a function of $S$ and hence minimal. But the source
stops before writing this out, so the completed algebra is not reproduced here.

## Sources

- Handwritten lecture notes: `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture05-F24.md`
  (Berkeley STAT 210A, Lecture 5, dated 9/12/2023 in the source; reconstructed by a model from a
  PDF with no text layer, so every equation there is flagged unverified). Covers, in order:
  the definition of completeness and its "complete basis" naming remark; the continued Laplace
  location-family example showing the minimal sufficient order statistics are not complete; the
  uniform-upper-endpoint example showing $X_{(n)}$ is complete; the definition of full-rank versus
  curved exponential families and the theorem (with proof idea, citing Lehmann & Romano, Theorem
  4.3.1) that full rank implies complete sufficiency, including the hand-drawn parameter-space
  picture reproduced above; and the theorem that complete sufficiency implies minimal
  sufficiency, whose proof is transcribed only as far as the source goes — the notes end
  mid-derivation.
- The lecture's own outline lists a third topic, **Basu's theorem**, as following from
  completeness. It is not present in the supplied notes and is not covered here.
- The Laplace location family's minimal sufficiency (order statistics reduce no further) is
  referred to as previously established ("Ex. (Cont'd)") but was covered in an earlier lecture,
  not in this file.
- Lehmann & Romano is cited by the lecture as the source of the full proof of the full-rank
  completeness theorem; that proof itself is not reproduced in the notes beyond the sketch given
  here.

---

[← 32. Exponential Families](32-exponential-families.md) · [Contents](index.md) · [34. Completeness and Basu's Theorem →](34-completeness-and-basu-s-theorem.md)
