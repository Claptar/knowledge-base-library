---
title: "34. Completeness and Basu's Theorem"
course: "Berkeley Stat 210A Fall 2024"
chapter: 34
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 34. Completeness and Basu's Theorem

## What this covers

This chapter asks when a sufficient statistic has been squeezed as far as it can go — not merely
down to the smallest sufficient statistic (minimality), but down to one where no nonzero function
of it can have expectation zero under every parameter value. That stronger property, **completeness**,
is what makes an unbiased estimator built from a sufficient statistic unique, and it is the engine
behind **Basu's theorem**, a way to prove two statistics are independent without ever writing down a
joint density. It assumes sufficiency, minimal sufficiency, and the exponential-family framework
(natural parameter, natural sufficient statistic) from the preceding lectures.

## What completeness says

Minimal sufficiency compresses the data as far as possible while still keeping every scrap of
information about $\theta$. It is natural to ask whether that compression also removes all the
"noise" — whether every function of a minimal sufficient statistic that isn't identically zero can
still be detected by its effect on some $\mathbb E_\theta$. It cannot, in general; the definition
below is what rules this out when it holds.

**Definition.** $T(X)$ is **complete** for $\mathcal P = \{P_\theta : \theta \in \Theta\}$ if, for
every function $f$,
$$\mathbb E_\theta f(T(X)) = 0 \quad \forall\, \theta \in \Theta \quad\implies\quad f(T) \stackrel{\text{a.s.}}{=} 0 \quad \forall\, \theta \in \Theta.$$

(The name comes from an older idea that $\mathcal P^T = \{P_\theta^T : \theta \in \Theta\}$ forms a
"complete basis" with respect to the inner product $\langle f, P_\theta^T\rangle = \int f(t)\,dP_\theta^T(t)$
— a connection developed further in a homework assignment not included among these materials.)

### Minimal sufficiency is not enough: the Laplace example

Continuing an example from the previous lecture, the Laplace location family has minimal sufficient
statistic $S(X) = (X_{(i)})_{i=1}^n$, the vector of order statistics. Is $S$ complete?

No. Let $M(S) = \operatorname{median}(X)$ and $\bar X(S) = \frac1n\sum_i X_i$ — both are functions of
$S$. By symmetry of the Laplace density about $\theta$,
$$\mathbb E_\theta \bar X = \mathbb E_\theta M = \theta,$$
so
$$\mathbb E_\theta\big[\bar X(S) - M(S)\big] = 0 \quad \text{for every } \theta.$$
Yet $\bar X(S) - M(S)$ is not almost-surely zero — the sample mean and sample median of a finite
sample are (generically) different numbers. So $S$ carries a nonzero function whose expectation
vanishes identically: $S$ still has, in the lecture's phrase, "a lot of extra fluff." Minimality
alone does not give completeness.

### A complete statistic: uniform samples

$X_1,\dots,X_n \stackrel{\text{iid}}{\sim} U[0,\theta]$, $\theta \in (0,\infty)$. The joint density is
$$p_\theta(x) = \prod_{i=1}^n \frac1\theta\, \mathbf 1\{x_i \le \theta\} = \frac{1}{\theta^n}\,\mathbf 1\{X_{(n)} \le \theta\},$$
and the likelihood ratio
$$\frac{p_\theta(x)}{p_\theta(y)} = \frac{\mathbf 1\{x_{(n)} \le \theta\}}{\mathbf 1\{y_{(n)}\le\theta\}}$$
depends on $\theta$ only through where $\theta$ falls relative to $x_{(n)}$ and $y_{(n)}$ — so, by the
likelihood-ratio criterion for minimal sufficiency, $T(X) = X_{(n)}$ is minimal sufficient.

Is $T$ complete? First find its distribution:
$$\mathbb P_\theta(T \le t) = \left(\frac t\theta \wedge 1\right)^n \implies p_\theta(t) = n\,\frac{t^{n-1}}{\theta^n}\,\mathbf 1\{t \le \theta\}.$$
Suppose $\mathbb E_\theta f(T) = 0$ for every $\theta > 0$:
$$0 = \frac{n}{\theta^n}\int_0^\theta f(t)\,t^{n-1}\,dt \quad \forall\, \theta > 0 \implies \int_0^\theta f(t)\,t^{n-1}\,dt = 0 \quad \forall\, \theta > 0.$$
The left side is an antiderivative of $f(\theta)\theta^{n-1}$ that is identically zero, so by the
fundamental theorem of calculus its derivative in $\theta$ is zero for almost every $\theta$:
$$f(\theta)\,\theta^{n-1} = 0 \quad \text{a.e. } \theta > 0.$$
Since $\theta^{n-1} \ne 0$ for $\theta > 0$, this forces $f(\theta) = 0$ for almost every $\theta > 0$.
So $T(X) = X_{(n)}$ is complete: unlike the Laplace order statistics, it has no room for a nonzero
function with identically zero expectation.

## Exponential families: full rank versus curved

The uniform example was a direct computation. For exponential families there is a structural
criterion that settles completeness without computing anything.

**Definition.** Suppose $\mathcal P = \{P_\eta : \eta \in \Xi\}$ has densities
$$p_\eta(x) = e^{\eta' T(x) - A(\eta)}\, h(x).$$
$\mathcal P$ is **full rank** if (i) $T(X)$ satisfies no linear constraint — there is no $\beta \ne 0$
and $\alpha$ with $\beta' T(X) \stackrel{\text{a.s.}}{=} \alpha$ for every $\theta$ — and (ii) $\Xi$
contains an open set. A family that is not full rank is called **curved**.

(A linear constraint on $T$ does not necessarily kill completeness outright: if $T$ satisfies one,
$\mathcal P$ can still be full rank for a lower-dimensional sufficient statistic — the part of $T$
that the constraint doesn't pin down.)

**Theorem.** If $\mathcal P$ is full rank, then $T(X)$ is complete sufficient. (Full proof: Lehmann &
Romano, Theorem 4.3.1. The idea, via moment generating functions, is below.)

**Proof idea.** It suffices to treat $T(X)$ itself as the observation — relabelling $x := T(X)$ turns
the problem into showing completeness for the canonical family $p_\eta(x) = e^{\eta'x - A(\eta)}$,
$\eta \in \Xi$. Assume without loss of generality that $0$ is an interior point of $\Xi$ and
$A(0) = 0$.

Suppose $\mathbb E_\eta f(X) = 0$ for every $\eta \in \Xi$, and write $f = f^+ - f^-$ for its positive
and negative parts, $f^+, f^- \ge 0$. Then for every $\eta$,
$$\int e^{\eta'x} f^+(x)\,d\mu(x) = \int e^{\eta'x} f^-(x)\,d\mu(x).$$
Setting $\eta = 0$ gives $\int f^+\,d\mu = \int f^-\,d\mu =: c$. If $f$ is not a.e. zero then $c > 0$
(otherwise both integrals, and hence both parts, vanish), so $f^+/c$ and $f^-/c$ are genuine densities
with respect to $\mu$, and the displayed equation says the moment generating functions of the
corresponding random variables $Y^+ \sim f^+/c$ and $Y^- \sim f^-/c$ agree on a neighbourhood of $0$.
By uniqueness of MGFs, agreement near $0$ already forces $Y^+ \stackrel{\mathcal D}{=} Y^-$, hence
$f^+ \stackrel{\text{a.e.}}{=} f^-$ — so $f \stackrel{\text{a.e.}}{=} 0$, contradicting the assumption
that it is not a.e. zero. So no such $f$ exists, and $T$ (equivalently $X$, in canonical form) is
complete. $\blacksquare$

The two clauses of full rank matter separately, and the lecture's diagram is about exactly that: for
a two-dimensional statistic $T$ (so $\Xi \subset \mathbb R^2$), what does it look like for $\Xi$ to
fail each clause?

<figure>
<svg viewBox="0 0 360 260" role="img" aria-label="Three ways a family's natural parameter space can sit inside the plane: an open patch, a curved arc, and a straight segment.">
  <ellipse cx="190" cy="130" rx="145" ry="95" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <text x="290" y="48" font-size="12" fill="currentColor">&#926;</text>
  <line x1="40" y1="230" x2="340" y2="230" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="230" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="343" y="234" font-size="12" fill="currentColor">&#951;&#8321;</text>
  <text x="26" y="18" font-size="12" fill="currentColor">&#951;&#8322;</text>
  <ellipse cx="125" cy="75" rx="45" ry="28" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="125" y="79" font-size="12" text-anchor="middle" fill="currentColor">A</text>
  <path d="M 220 115 Q 270 70 320 95" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="272" y="60" font-size="12" text-anchor="middle" fill="currentColor">B</text>
  <line x1="110" y1="190" x2="190" y2="150" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="122" cy="184" r="3" fill="currentColor"/>
  <text x="128" y="182" font-size="12" fill="currentColor">&#947;</text>
  <text x="150" y="160" font-size="12" fill="currentColor">C</text>
</svg>
<figcaption>The natural parameter space $\Xi \subset \mathbb R^2$ for a two-dimensional sufficient
statistic $T$. (A) an open two-dimensional patch: $T$ is full rank, hence complete. (B) a curved,
non-straight arc: the family is curved (fails clause (ii)) but $T$ is still minimal, since no linear
combination of $T$ is almost-surely constant. (C) a straight segment through a point $\gamma$: one
linear combination of $T$ is redundant along that line (fails clause (i)), so $T$ is not minimal,
though the reduced one-dimensional statistic is full rank.</figcaption>
</figure>

$T$ is definitely complete in case (A). It need not be in (B) or (C) — but the lecture flags that the
converse of the theorem is false: $T$ can still turn out to be complete sufficient in (B) or (C) too,
just without the theorem's guarantee. Full rank is a sufficient condition for completeness, not a
necessary one.

## Completeness forces minimality

**Theorem.** If $T(X)$ is complete sufficient for $\mathcal P$, then $T(X)$ is minimal sufficient.

The lecture states the general strategy this proof uses on its own, because it recurs: *to show two
statistics are almost-surely equal, show their difference has expectation zero under every $\theta$,
then invoke completeness.*

**Proof.** Let $S(X)$ be a minimal sufficient statistic. Since $S$ is sufficient,
$\bar T(S(X)) := \mathbb E[T(X)\mid S(X)]$ is well defined without reference to $\theta$. Since $S$ is
minimal, $S(X) \stackrel{\text{a.s.}}{=} f(T(X))$ for some function $f$. Let $g(t) = t - \bar T(f(t))$.
For every $\theta$,
$$\mathbb E_\theta[g(T(X))] = \mathbb E_\theta T(X) - \mathbb E_\theta\big[\bar T(S(X))\big] = \mathbb E_\theta T(X) - \mathbb E_\theta\big[\mathbb E[T(X)\mid S(X)]\big] = 0,$$
by the tower property. Completeness of $T$ then forces $g(T(X)) \stackrel{\text{a.s.}}{=} 0$ for every
$\theta$, i.e.
$$T(X) \stackrel{\text{a.s.}}{=} \bar T\big(f(T(X))\big) = \bar T(S(X)).$$
So $T$ is (a.s.) a function of $S$ — and $S$ is already (a.s.) a function of $T$, since $S$ is minimal
and $T$ is sufficient. Each is a function of the other, so they carry the same information; since $S$
is a.s. a function of every sufficient statistic, so is $T$. Hence $T$ is minimal. $\blacksquare$

## Why completeness matters

Two consequences make completeness worth checking, beyond minimality:

1. **Uniqueness of unbiased estimators built from $T$.** If $\delta_1(T)$ and $\delta_2(T)$ are both
   unbiased for the same $g(\theta)$ — $\mathbb E_\theta \delta_1(T) = \mathbb E_\theta \delta_2(T) = g(\theta)$
   for every $\theta$ — then $\mathbb E_\theta[\delta_1(T) - \delta_2(T)] = 0$ for every $\theta$, and
   completeness forces $\delta_1(T) \stackrel{\text{a.s.}}{=} \delta_2(T)$. Once $T$ is complete
   sufficient, there is at most one unbiased estimator that is a function of it. (The lecture flags
   this as a topic developed further in the next lecture, which these materials do not cover.)
2. **Basu's theorem**, a shortcut for proving independence, below.

## Ancillarity and the conditionality principle

**Definition.** $V(X)$ is **ancillary** for $\mathcal P = \{P_\theta : \theta \in \Theta\}$ if its
distribution does not depend on $\theta$ — $V$ carries no information about $\theta$ on its own.

*Aside.* If $V(X)$ is ancillary, the notes state, then all inference should be conducted
conditionally on $V(X)$ — the **conditionality principle**, a topic the course returns to in its
testing and confidence-interval unit.

## Basu's theorem

**Theorem (Basu).** If $T(X)$ is complete sufficient and $V(X)$ is ancillary, both for the same
family $\mathcal P$, then
$$V(X) \perp\!\!\!\perp T(X) \quad \text{under every } P_\theta \in \mathcal P.$$

**Proof.** Fix a set $A$ and let $p_A = \mathbb P(V \in A)$ — this does not depend on $\theta$, since
$V$ is ancillary. Since $T$ is sufficient, $q_A(T(X)) := \mathbb P(V \in A \mid T(X))$ is well defined
without reference to $\theta$. Then for every $\theta$,
$$\mathbb E_\theta\big[q_A(T) - p_A\big] = \mathbb E_\theta\big[\mathbb P(V \in A \mid T)\big] - p_A = \mathbb P_\theta(V \in A) - p_A = p_A - p_A = 0,$$
so completeness of $T$ gives $q_A(T) \stackrel{\text{a.s.}}{=} p_A$ for every $\theta$. Now for any set
$B$,
$$\mathbb P_\theta(V \in A,\, T \in B) = \int_B q_A(t)\,dP_\theta^T(t) = p_A \int_B dP_\theta^T(t) = \mathbb P(V \in A)\,\mathbb P_\theta(T \in B).$$
Since $A$ and $B$ were arbitrary, $V$ and $T$ are independent under $P_\theta$, for every $\theta$.
$\blacksquare$

## Using Basu's theorem: switching families

Applying the theorem well means noticing a gap between its hypotheses and its conclusion:
completeness, sufficiency and ancillarity are all properties of a statistic **relative to a family**
$\mathcal P$, but independence is a property of a single **distribution**. That gap is exploitable —
if $T$ and $V$ fail to be complete-sufficient-and-ancillary in the family you actually care about, try
checking the hypotheses in a smaller, more convenient family that the true distribution still belongs
to. The conclusion, once established there, is a fact about that particular distribution, and holds
regardless of which family was used to get it.

**Example.** Let $X_1,\dots,X_n \stackrel{\text{iid}}{\sim} N(\mu,\sigma^2)$ with both $\mu \in \mathbb R$
and $\sigma^2 > 0$ unknown. Let
$$\bar X = \frac1n \sum_{i=1}^n X_i, \qquad S^2 = \frac1{n-1}\sum_{i=1}^n (X_i - \bar X)^2$$
be the sample mean and sample variance. The goal is to show $\bar X \perp\!\!\!\perp S^2$.

Neither statistic is ancillary or sufficient on its own in the full two-parameter family, so Basu's
theorem doesn't apply there directly. Instead, fix $\sigma^2$ at some value and work in the smaller,
one-parameter family
$$\mathcal P = \{N(\mu,\sigma^2)^{\otimes n} : \mu \in \mathbb R\}.$$
This is a full-rank exponential family in $\mu$ (the natural parameter $\mu/\sigma^2$ ranges over all
of $\mathbb R$, an open set, with no linear constraint on the natural statistic), so by the theorem
above its natural sufficient statistic $\bar X$ is complete sufficient in $\mathcal P$. And $S^2$ is
ancillary in $\mathcal P$: writing $Z_i = X_i - \mu \stackrel{\text{iid}}{\sim} N(0,\sigma^2)$,
$$S^2 = \frac1{n-1}\sum_i (Z_i - \bar Z)^2,$$
whose distribution depends only on $\sigma^2$, not on $\mu$ — the $Z_i$ are not themselves statistics,
since they involve the unknown $\mu$, but that doesn't matter, since it is only the distribution of
$S^2$ that needs to be free of $\mu$. By Basu's theorem applied in $\mathcal P$,
$\bar X \perp\!\!\!\perp S^2$.

The actual distribution, whatever $\mu$ and $\sigma^2$ truly are, is a member of $\mathcal P$ for that
value of $\sigma^2$ — so the independence conclusion holds for it too. It has nothing to do with
$\sigma^2$ being "known" or "unknown"; that was only a device for choosing a family in which Basu's
hypotheses could actually be checked.

## Sources

Notes for this lecture exist in three offerings of the course, all covering completeness, ancillarity
and Basu's theorem in the same order. The fall-2025 and fall-2026 transcriptions are essentially
identical to each other and slightly more complete than fall-2024's (they spell out the likelihood-ratio
argument for minimal sufficiency in the uniform example, and the canonical-form/MGF proof of the
full-rank theorem in more detail), so they are the primary source used here:

- Definition of completeness, the Laplace counterexample, the uniform example, the full-rank
  definition and theorem, and the completeness-implies-minimality theorem:
  `statistics/berkeley/stat210a/fall-2025/handwritten/lecture06-completeness.md` and
  `statistics/berkeley/stat210a/fall-2026/handwritten/lecture06-completeness.md` (identical),
  cross-checked against
  `statistics/berkeley/stat210a/fall-2024/handwritten/lecture06-completeness/01-completeness.md`.
- The parameter-space diagram (full rank / curved / not minimal): reconstructed from the ASCII
  rendering in `statistics/berkeley/stat210a/fall-2024/handwritten/lecture06-completeness/02-diagram-again.md`,
  with the additional remark that the theorem's converse fails taken from the fall-2025/fall-2026
  version of the same page.
- Ancillarity, the conditionality-principle aside, Basu's theorem and its proof, and the normal
  $\bar X \perp\!\!\!\perp S^2$ example: all four files agree; fall-2025/fall-2026 preferred for
  wording.

All four source files carry the same caveat: each is a model's reconstruction of a handwritten PDF
page with no text layer, and every equation is marked unverified in the original conversion. The
three independent transcriptions agree on every formula used here, which is the cross-check available.

Referred to but not supplied: the Laplace location family's exact density and parameter range
(introduced in an earlier lecture, not among these inputs); HW 3, cited for the "complete basis"
motivation behind the name "completeness"; Lehmann & Romano, Theorem 4.3.1, cited for the general
proof that full rank implies completeness; the next lecture, flagged as where uniqueness of unbiased
estimators is developed further; and the course's testing/confidence-interval unit, flagged as where
the conditionality principle is revisited. No slides, transcript, or exercises were supplied for this
lecture.

---

[← 33. Completeness of Sufficient Statistics](33-completeness-of-sufficient-statistics.md) · [Contents](index.md) · [35. Rao–Blackwell and UMVU Estimators →](35-rao-blackwell-and-umvu-estimators.md)
