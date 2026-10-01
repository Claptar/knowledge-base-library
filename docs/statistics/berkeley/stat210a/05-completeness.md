---
title: "5. Completeness"
course: "Berkeley Stat 210A"
chapter: 5
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Completeness

## What this covers

This chapter answers a question left open by minimal sufficiency: among the minimal sufficient
statistics for a family, when is one of them *complete* — meaning no nontrivial function of it can
be built into an unbiased estimator of zero? It assumes sufficiency, minimal sufficiency, the
factorization theorem, and exponential families in their natural (canonical) parameterization. It
ends by using completeness to prove two statistics independent via Basu's theorem, which along the
way needs the notion of an *ancillary* statistic — one carrying no information about $\theta$ at
all.

## The definition, and why it is worth having

For a given problem there is usually more than one sufficient statistic, and some reduce the data
further than others. The *minimal* sufficient statistic strips away as much as possible while
keeping everything relevant to $\theta$. Some minimal sufficient statistics have a further
property, *completeness*, whose definition looks unmotivated at first but pays off repeatedly
through the rest of the course.

A statistic $T(X)$ is **complete** for a family $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ if
no nontrivial function of $T$ can have expectation zero under every member of the family:
$$
\mathbb{E}_\theta\, f(T(X)) = 0 \quad \text{for all } \theta \in \Theta \implies f(T) \overset{\mathcal{P}\text{-a.s.}}{=} 0.
$$
An equivalent form is sometimes more useful: if $\mathbb{E}_\theta f(T(X)) = c$ for *every* $\theta$
and some fixed constant $c$, then $f(T) \overset{\mathcal{P}\text{-a.s.}}{=} c$ — a function of a
complete statistic whose expectation is constant across the whole family cannot actually vary.

The name comes from an older notion that the induced family $\mathcal{P}^T = \{P_\theta^T\}$ is
"complete" if its linear span already contains every distribution on the range of $T$ (developed
further on a homework problem, not reproduced here).

**Why bother:** completeness pins down unbiased estimators uniquely. If $\delta_1(T)$ and
$\delta_2(T)$ both satisfy $\mathbb{E}_\theta \delta_i(T) = g(\theta)$ for every $\theta$, then
$f(T) = \delta_1(T) - \delta_2(T)$ has expectation zero for every $\theta$, so completeness forces
$f(T) = 0$ almost surely: the two estimators agree. (Taking $T(X) = X$ recovers the same conclusion
for the whole sample.) So if $T$ is complete, there is *at most one* unbiased estimator of any
estimand that can be written as a function of $T$ — the fact this chapter will lean on when we come
to unbiased estimation.

When $T$ is both complete and sufficient it is called a **complete sufficient statistic**. The two
properties are logically independent, and it is worth having a counterexample in mind: the constant
statistic $T(X) \equiv 0$ is complete in *any* model (there is no nontrivial function of a constant
whose expectation could vary in the first place), yet it throws away all the information in the
data. Showing a statistic is complete sufficient always takes two separate arguments — completeness
does not follow from sufficiency, or vice versa.

## Two examples worked by hand

**The order statistics of a Laplace location family need not be complete.** Let $X_1, \dots, X_n
\overset{\text{i.i.d.}}{\sim} \text{Lap}(\theta)$ for $\theta \in \mathbb{R}$ and $n \ge 2$; the
order statistics $S(X) = (X_{(1)}, \dots, X_{(n)})$ are minimal sufficient for this family. $S(X)$
is *not* complete, and there are two ways to see it.

Write $X_i = \theta + Z_i$ with $Z_1, \dots, Z_n \overset{\text{i.i.d.}}{\sim} \text{Lap}(0)$. The
range $X_{(n)} - X_{(1)} = Z_{(n)} - Z_{(1)}$ then has the *same* distribution for every $\theta$ —
it is a function of $S(X)$ whose mean does not move with $\theta$ at all. So
$$
f(S) = \big(X_{(n)} - X_{(1)}\big) - \mathbb{E}\big[Z_{(n)} - Z_{(1)}\big]
$$
has expectation zero for every $\theta$ but is not almost surely zero, which already breaks
completeness for every $n \ge 2$.

A second, more evocative counterexample: because $\text{Lap}(0)$ is symmetric, both the sample mean
$\overline{X}$ and the sample median $\text{Med}(X)$ are unbiased for $\theta$ (since
$\text{Med}(X) = \theta + \text{Med}(Z)$ and $\text{Med}(Z)$ has mean $0$ by symmetry), and both are
functions of $S(X)$ alone. So $f(S) = \text{Med}(X) - \overline{X}$ has expectation zero for every
$\theta$, yet mean and median are almost surely *unequal* once $n > 2$ — a second, independent
failure of completeness. (It genuinely needs $n>2$: with $n=2$ the mean and median of two order
statistics coincide, so that particular $f$ is trivial even though the range argument above still
applies.)

**The maximum in a uniform scale family is complete.** Let $X_1, \dots, X_n
\overset{\text{i.i.d.}}{\sim} U[0,\theta]$ for $\theta > 0$; the maximum $T(X) = X_{(n)}$ is minimal
sufficient, and this time it *is* complete. Its density for $t>0$ is
$$
p_\theta(t) = \frac{n\, t^{n-1}}{\theta^n} \cdot \mathbb{1}\{t \le \theta\}.
$$
Suppose $f$ satisfies $\mathbb{E}_\theta f(T) = 0$ for every $\theta>0$:
$$
0 = \frac{n}{\theta^n} \int_0^\theta f(t)\, t^{n-1}\, dt, \qquad \text{for all } \theta > 0.
$$
Multiply through by $\theta^n/n$ and differentiate both sides with respect to $\theta$ — the
fundamental theorem of calculus removes the integral and leaves
$$
0 = f(\theta)\, \theta^{n-1}, \qquad \text{for all } \theta > 0,
$$
so $f \equiv 0$. The trick generalizes: differentiating an integral with a $\theta$-dependent upper
limit is often the fastest route to completeness when $T$ has a density supported on an interval
that grows or shrinks with $\theta$, precisely because it turns a condition that must hold for
every $\theta$ into a pointwise condition on $f$ itself.

## Full-rank exponential families are complete sufficient for free

The trick above worked because $T(X)$ ranged over an interval whose endpoint moved with $\theta$.
In general $T(X)$ can range over a much larger space, the space of candidate counterexample
functions $f$ becomes infinite-dimensional, and a direct search for one is hopeless. Full-rank
exponential families are the one large class of models where completeness can nonetheless be
checked once and for all.

Let $\mathcal{P} = \{P_\eta : \eta \in \Xi\}$ be an $s$-parameter exponential family with densities
$$
p_\eta(x) = e^{\eta' T(x) - A(\eta)}\, h(x)
$$
with respect to a carrier measure $\mu$, and suppose $T(X)$ satisfies no affine constraint: there is
no $\alpha \in \mathbb{R}$ and nonzero $\beta \in \mathbb{R}^s$ with $\beta' T(x)
\overset{\mathcal{P}\text{-a.s.}}{=} \alpha$. (If $T$ *did* satisfy such a constraint, the family
could be rewritten with $r < s$ parameters, and full-rankness would need to be checked again in
that lower-dimensional parameterization.) Call $\mathcal{P}$ **full-rank** if $\Xi$ contains an open
set, and **curved** otherwise.

**Theorem.** If $\mathcal{P}$ is a full-rank $s$-parameter exponential family, then $T(X)$ is
complete sufficient.

Sufficiency is immediate from the factorization theorem, so the content is completeness, and the
proof is worth having in full because its technique — matching two expectations to conclude that
two densities coincide, via the uniqueness of moment generating functions — recurs throughout the
course.

*Proof.* Reparameterize so that $0$ lies in the interior of $\Xi$, and reduce to canonical form
$T(X) = X$, $p_\eta(x) = e^{\eta'x - A(\eta)}$ (always possible by a sufficiency reduction, taking
$P_0^T$ as the carrier measure — completeness after such a reduction is equivalent to completeness
in the original model). Suppose, toward a contradiction, that $X$ is *not* complete: some
nontrivial $f$ has $\mathbb{E}_\eta f(X) = 0$ for every $\eta \in \Xi$. Split $f = f^+ - f^-$ into
its (nonnegative) positive and negative parts. The hypothesis becomes
$$
\int e^{\eta'x} f^+(x)\, d\mu(x) = \int e^{\eta'x} f^-(x)\, d\mu(x), \qquad \text{for all } \eta \in \Xi. \tag{$\ast$}
$$
Since $\Xi$ contains an open neighborhood of $0$ on which both sides are finite, normalize so that
$\int f^+\, d\mu = \int f^-\, d\mu = 1$ and read $f^+, f^-$ as probability densities of random
variables $Y^+, Y^-$. Then $(\ast)$ says $Y^+$ and $Y^-$ have equal moment generating functions on a
neighborhood of $0$, hence the same distribution, hence $f^+ = f^-$ almost everywhere. But $f^+$ and
$f^-$ can only agree where both are zero, since $f^+ f^- \equiv 0$ pointwise by construction — so
$f \overset{\mu\text{-a.s.}}{=} 0$, contradicting the assumption that $f$ was nontrivial. $\blacksquare$

The proof is really about parameter spaces, not about $T$ itself: the same sufficient statistic can
sit inside many different exponential subfamilies, and whether completeness comes for free depends
on whether the natural parameter space of that particular subfamily contains an open set.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Three subfamilies of a two-parameter exponential family, shown as subsets of the natural parameter plane">
  <rect x="20" y="20" width="300" height="170" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="26" y="36" font-size="12" fill="currentColor">natural parameter space</text>
  <circle cx="85" cy="140" r="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <text x="85" y="144" text-anchor="middle" font-size="13" fill="currentColor">A</text>
  <path d="M 150 175 Q 210 90 275 150" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="282" y="148" font-size="13" fill="currentColor">B</text>
  <line x1="150" y1="65" x2="230" y2="65" stroke="currentColor" stroke-width="2.5"/>
  <text x="236" y="69" font-size="13" fill="currentColor">C</text>
</svg>
<figcaption>Three subfamilies with the same sufficient statistic $T$, as subsets of the natural
parameter space of a generic 2-parameter exponential family. The shaded disk (A) contains an open
set, so it is full-rank and $T$ is automatically complete sufficient there. The curve (B) contains
no open set, so it is curved and completeness is not automatic. The segment (C) is also,
technically, curved by the definition above — but being a line, it can be re-parameterized as a
full-rank 1-parameter family, and checked that way instead.</figcaption>
</figure>

## Complete sufficient statistics are minimal

A second convenient property: completeness upgrades sufficiency all the way to minimality, so
finding a complete sufficient statistic settles the search for a minimal one in a single step.

**Theorem.** If $T(X)$ is complete sufficient for $\mathcal{P}$, then $T(X)$ is minimal sufficient
for $\mathcal{P}$.

The proof is a template for how completeness gets used throughout the course: to show two
quantities are almost surely equal, show they have the same expectation for every $\theta$, then
invoke completeness.

*Proof.* Let $S(X)$ be any minimal sufficient statistic, and define
$$
\overline{T}(S(X)) = \mathbb{E}\big[T(X) \mid S(X)\big].
$$
This conditional expectation does not depend on $\theta$ because $S(X)$ is sufficient, so
$\overline{T}$ is a genuine statistic. If $\overline{T} \overset{\text{a.s.}}{=} T(X)$, then $T(X)$
can be recovered from $S(X)$, and hence $T(X)$ is itself minimal sufficient — which is exactly what
needs to be shown.

Because $S(X)$ is minimal sufficient, it can be written as $S(X) = f(T(X))$ for some function $f$.
Use this $f$ to define
$$
g(t) = t - \overline{T}(f(t)),
$$
so that $g(T(X)) = T(X) - \overline{T}(S(X))$. The expectation of $g(T)$ is zero for every $\theta$:
$$
\mathbb{E}_\theta\, g(T(X)) = \mathbb{E}_\theta\, T(X) - \mathbb{E}_\theta\, \overline{T}(S(X))
= \mathbb{E}_\theta\, T(X) - \mathbb{E}_\theta\Big[\mathbb{E}[T(X) \mid S(X)]\Big] = 0,
$$
the last equality being the tower property. By completeness of $T$, $g(T)
\overset{\text{a.s.}}{=} 0$, i.e. $T \overset{\text{a.s.}}{=} \overline{T}$, as desired.
$\blacksquare$

## Ancillary statistics and the conditionality principle

Sufficient statistics carry *all* the information about $\theta$. The next definition is the
opposite extreme: a statistic that carries *none*.

**Definition.** $V(X)$ is **ancillary** for the model $\mathcal{P} = \{P_\theta : \theta \in
\Theta\}$ if the distribution of $V(X)$ does not depend on $\theta$.

Just as the sufficiency principle says inference should depend only on sufficient statistics, a
companion principle says inference should depend on ancillary statistics as little as possible —
by treating an observed ancillary value as fixed and evaluating everything else conditional on it.

**Conditionality Principle.** If $V(X)$ is ancillary, all inference should be conditional on
$V(X)$.

It is not yet obvious why conditioning on $V(X)$ removes it from the problem; that becomes clearer
once conditional inference is used in earnest, in the unit on hypothesis testing and interval
estimation.

## Basu's theorem

Completeness and ancillarity combine to give a strikingly easy way to prove two statistics are
independent — often easier than any direct computation.

**Theorem (Basu).** If $T(X)$ is complete sufficient and $V(X)$ is ancillary for the model
$\mathcal{P}$, then $V(X) \perp\!\!\!\!\perp T(X)$ under $P_\theta$, for every $\theta \in \Theta$.

The proof follows the same template as the minimality theorem above: reduce independence to an
almost-sure equality, and get that equality from completeness.

*Proof.* Fix a set $A$ and define the marginal and conditional probabilities that $V$ falls in $A$:
$$
p_A = \mathbb{P}(V \in A), \qquad q_A(T(X)) = \mathbb{P}(V \in A \mid T(X)).
$$
$p_A$ does not depend on $\theta$ because $V$ is ancillary; $q_A$ does not depend on $\theta$
because $T$ is sufficient. Their difference has expectation zero for every $\theta$:
$$
\mathbb{E}_\theta\big[q_A(T) - p_A\big] = p_A - p_A = 0, \qquad \text{for all } \theta.
$$
By completeness of $T$, $q_A(T) \overset{\text{a.s.}}{=} p_A$: the conditional probability equals
the marginal probability, for (almost) every value of $T$. Hence, for any set $B$,
$$
\mathbb{P}_\theta(V \in A,\, T \in B) = \int q_A(t)\, \mathbb{1}\{t \in B\}\, dP_\theta^T(t)
= \int p_A\, \mathbb{1}\{t \in B\}\, dP_\theta^T(t)
= \mathbb{P}_\theta(V \in A)\, \mathbb{P}_\theta(T \in B),
$$
which is exactly independence. $\blacksquare$

### Using Basu's theorem: independence of the sample mean and sample variance

The hypotheses of Basu's theorem — sufficiency, completeness, ancillarity — are all statements
about a *family* $\mathcal{P}$, while the conclusion is a statement about an individual
*distribution*. This mismatch is what makes the theorem powerful: to apply it, one gets to choose
which family to view the problem through, and a clever choice can make hypotheses hold that look,
at first, hopeless to establish.

**Example.** Let $X_1, \dots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$ with $\mu \in
\mathbb{R}$ and $\sigma^2 > 0$ both unknown. Define the sample mean and sample variance
$$
\overline{X} = \frac{1}{n}\sum_{i=1}^n X_i, \qquad S^2 = \frac{1}{n-1}\sum_{i=1}^n \big(X_i - \overline{X}\big)^2,
$$
and suppose the goal is to show $\overline{X} \perp\!\!\!\!\perp S^2$.

Applying Basu's theorem directly to the two-parameter family $\{N(\mu,\sigma^2) : \mu \in
\mathbb{R}, \sigma^2 > 0\}$ looks hopeless, because in that family *neither* statistic is ancillary
or sufficient. The fix is to change which family is under consideration, not which statistics are
under consideration.

Fix $\sigma^2 > 0$ at a known value and treat only $\mu \in \mathbb{R}$ as unknown. This restricted
family is a one-parameter full-rank exponential family, so by the theorem above its (complete)
sufficient statistic is $\overline{X}$. Meanwhile, writing $Z_i = X_i - \mu$,
$$
S^2 = \frac{1}{n-1}\sum_{i=1}^n \big(Z_i - \overline{Z}\big)^2,
$$
and since $Z_1, \dots, Z_n \overset{\text{i.i.d.}}{\sim} N(0, \sigma^2)$ has a distribution that
does not involve the only unknown parameter $\mu$ (specifically $S^2/\sigma^2$ is $\chi^2$ with
$n-1$ degrees of freedom), $S^2$ is ancillary in *this* restricted family. Basu's theorem now
applies directly: $\overline{X} \perp\!\!\!\!\perp S^2$ for this fixed $\sigma^2$ and every $\mu \in
\mathbb{R}$. But $\sigma^2$ was an arbitrary fixed value, so the conclusion holds for every $\mu \in
\mathbb{R}$ and every $\sigma^2 > 0$ — which is the independence statement for the original,
two-parameter Gaussian family.

## Sources

- Definition of completeness, its uniqueness-of-unbiased-estimator consequence, and the warning
  that completeness does not imply sufficiency: `fall-2025/reader/completeness/01-1-completeness.md`
  §1–1.1 (equivalently `fall-2024/reader/completeness/01-completeness.md` and
  `fall-2026/reader/completeness/01-completeness.md`, which record the same material with a shorter
  form of the definition and without the constant-$c$ equivalent form). The remark that
  completeness is named for an older linear-span notion of a "complete" model points to Homework 3
  of the course, which was not supplied as input.
- The Laplace order-statistics and uniform-maximum examples:
  `fall-2025/reader/completeness/01-1-completeness.md` §1.2, the more complete of two versions (it
  adds the range-based counterexample $X_{(n)} - X_{(1)}$ and the $n\ge2$ / $n>2$ distinction not
  present in `fall-2024/reader/completeness/01-completeness.md` and
  `fall-2024/reader/completeness/02-expand-to-see-answer.md`, whose median/mean counterexample this
  chapter also uses). The claims that the order statistics are minimal sufficient for the Laplace
  family and that $X_{(n)}$ is minimal sufficient for the uniform scale family are carried over from
  an earlier lecture not included among the inputs for this chapter, and the Laplace sample-median
  construction is attributed to a homework problem, also not supplied.
- Full-rank exponential families, the completeness theorem and its proof, and the accompanying
  figure of full-rank versus curved parameter subsets:
  `fall-2025/reader/completeness/01-1-completeness.md` §1.3, whose proof write-up (normalizing
  $f^+,f^-$ to probability densities directly) is cleaner than the equivalent passage in
  `fall-2024/reader/completeness/02-expand-to-see-answer.md` and
  `fall-2024/reader/completeness/03-expand-for-proof.md`, used here instead. The referenced figure
  itself (`completeness.png`) was not supplied as an input image; the diagram above is redrawn from
  the description in the text.
- Complete sufficient statistics are minimal, with proof: `fall-2025/reader/completeness/01-1-completeness.md`
  §1.4 (also `fall-2024/reader/completeness/03-expand-for-proof.md`).
- Ancillarity and the conditionality principle: `fall-2025/reader/completeness/02-2-ancillarity.md`
  (also `fall-2024/reader/completeness/03-expand-for-proof.md`, under "Ancillarity"). The forward
  reference to conditional inference in the hypothesis-testing and interval-estimation unit points
  to material later in the course, not included here.
- Basu's theorem, its proof, and the Gaussian mean/variance independence example:
  `fall-2025/reader/completeness/03-3-basu-s-theorem.md` (also
  `fall-2024/reader/completeness/04-basu-s-theorem.md`, materially identical).
- All source files are UC Berkeley STAT 210A course reader pages ("Completeness, Ancillarity, and
  Basu's Theorem"), licensed CC BY 4.0, converted from the `fall-2024`, `fall-2025`, and
  `fall-2026` offerings. Where the three versions repeat the same material, this chapter follows
  the clearest of the three rather than layering all of them; editorial "under construction" notes
  present in the fall-2024 and fall-2026 sources (flagging unresolved homework cross-references)
  are omitted as production notes rather than course content.

---

[← 4. Where Does the Prior Come From?](04-where-does-the-prior-come-from.md) · [Contents](index.md) · [6. Convergence and the Delta Method (part 1) →](06-convergence-and-the-delta-method-part-1.md)
