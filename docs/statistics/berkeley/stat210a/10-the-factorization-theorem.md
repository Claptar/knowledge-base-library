---
title: "10. The Factorization Theorem"
course: "Berkeley Stat 210A Fall 2024"
chapter: 10
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. The Factorization Theorem

## What this covers

This chapter proves the factorization theorem: a statistic $T$ is sufficient for $\theta$ exactly
when the density of the data splits into a piece that depends on $\theta$ only through $T$, and a
piece that does not involve $\theta$ at all. It assumes the definition of sufficiency — that the
conditional distribution of $X$ given $T(X)$ does not depend on $\theta$ — and the basic apparatus
of dominated families: a $\sigma$-finite dominating measure $\mu$ and the Radon–Nikodym derivative
$p_\theta = dP_\theta/d\mu$.

## Setting and statement

Let $(\mathcal{X}, \mathcal{A})$ be a measurable space and $\mathcal{P} = \{P_\theta : \theta \in
\Theta\}$ a family of probability measures on it. Suppose the whole family is dominated by a single
$\sigma$-finite measure $\mu$ — every $P_\theta$ is absolutely continuous with respect to $\mu$ —
and write $p_\theta = dP_\theta/d\mu$ for the resulting densities. Dominance is what makes a single
function $p_\theta(x)$ available to factor in the first place; without a common dominating measure
there is no shared density to split.

**Theorem (Factorization Theorem).** A statistic $T : \mathcal{X} \to \mathcal{Y}$ is sufficient for
$\theta$ if and only if there exist measurable functions
$$
u : \mathcal{Y} \times \Theta \to [0,\infty), \qquad v : \mathcal{X} \to [0,\infty)
$$
such that, for every $x \in \mathcal{X}$ and every $\theta \in \Theta$,
$$
p_\theta(x) = u(T(x), \theta)\, v(x).
$$

Read the two factors separately. $u$ is where all the $\theta$-dependence is allowed to live, and it
may see $x$ only through $T(x)$. $v$ may depend on $x$ in any way at all, but never on $\theta$. So
the theorem trades sufficiency — a statement about conditional distributions — for a purely
algebraic property of the density that is normally far easier to check by inspection: try to peel
$\theta$ out of $p_\theta(x)$ into a factor that sees $x$ only through $T(x)$, leaving a $\theta$-free
remainder.

## Sufficiency implies factorization

Suppose $T$ is sufficient for $\theta$. By definition, the conditional distribution of $X$ given
$T(X) = t$ does not depend on $\theta$: writing $k(x \mid t)$ for this common conditional density,
it is the same function whether computed under $P_\theta$ or under any other member of the family.

Let $f_{T,\theta}(t)$ denote the marginal density of $T(X)$ under $P_\theta$. The joint density of
$X$ decomposes as (marginal density of $T$) times (conditional density of $X$ given $T$), and the
conditional factor does not involve $\theta$:
$$
p_\theta(x) = f_{T,\theta}(t)\, k(x \mid t), \qquad t = T(x).
$$
Set $v(x) = k(x \mid T(x))$ — a function of $x$ alone, since $\theta$ never entered it — and
$u(t,\theta) = f_{T,\theta}(t)$. Then $p_\theta(x) = u(T(x),\theta)\,v(x)$, which is the required
factorization.

(The source's own proof pauses at exactly this point to flag a subtlety: the naive discrete
computation $p_\theta(x) = P_\theta(X = x \mid T(X) = t)\, P_\theta(T(X) = t)$ does not literally
make sense once $x$ ranges over a continuum, since $P_\theta(X = x) = 0$ there. The fix is the
passage to densities carried out above, which the proof states rather than re-derives from first
principles.)

## Factorization implies sufficiency

Now suppose $p_\theta(x) = u(T(x), \theta)\, v(x)$ for measurable $u, v$. Fix a measurable set $B
\in \mathcal{A}$ and a value $t$, and write the conditional probability of $X \in B$ given $T(X) = t$
under $P_\theta$ as a ratio of integrals over the fiber $T^{-1}(t)$:
$$
P_\theta(X \in B \mid T(X) = t) = \frac{\displaystyle\int_{B \cap T^{-1}(t)} p_\theta(x)\, d\mu(x)}
{\displaystyle\int_{T^{-1}(t)} p_\theta(x)\, d\mu(x)}.
$$
Substitute the factorization. On the fiber $T^{-1}(t)$ every point $x$ satisfies $T(x) = t$, so
$u(T(x),\theta) = u(t,\theta)$ is literally constant over the domain of both integrals and can be
pulled outside each:
$$
P_\theta(X \in B \mid T(X) = t) = \frac{u(t,\theta)\displaystyle\int_{B \cap T^{-1}(t)} v(x)\, d\mu(x)}
{u(t,\theta)\displaystyle\int_{T^{-1}(t)} v(x)\, d\mu(x)}
= \frac{\displaystyle\int_{B \cap T^{-1}(t)} v(x)\, d\mu(x)}{\displaystyle\int_{T^{-1}(t)} v(x)\, d\mu(x)}.
$$
The $u(t,\theta)$ factors cancel exactly, top and bottom, leaving an expression built only from $v$
and the sets $B \cap T^{-1}(t)$ and $T^{-1}(t)$ — nothing that depends on $\theta$. So the
conditional distribution of $X$ given $T(X) = t$ is the same for every $\theta$, which is precisely
the definition of $T$ being sufficient for $\theta$. $\blacksquare$

## What the two directions are really doing

The two halves of the proof are mirror images of each other. The forward direction takes the
definition of sufficiency apart into a marginal-times-conditional decomposition and reads $u$ and
$v$ straight off the two pieces. The reverse direction runs that decomposition backwards: given any
factorization, the factor $u(T(x),\theta)$ is forced to be constant on each fiber $T^{-1}(t)$,
because it can only see $x$ through $T(x)$ — so it always cancels out of the conditional-probability
ratio, whatever it actually is, and the only thing left in the ratio is $v$, which was $\theta$-free
from the start. That cancellation is the entire mechanism of the theorem: it is why isolating the
$\theta$-dependence into a single factor depending on $x$ only through $T(x)$ is not merely *a*
sufficient condition for sufficiency, but an *equivalent* one.

## Sources

- Statement and complete proof of the factorization theorem (both directions):
  `factorizationtheorem.md`, UC Berkeley STAT 210A, Fall 2024 course reader, licensed CC BY 4.0,
  converted from `factorizationtheorem.tex`. No slides, transcript, or exercises were supplied for
  this chapter, and no other version of this material (from another year's offering of the course)
  was provided as input.

---

[← 9. Exponential Family Structure](09-exponential-family-structure.md) · [Contents](index.md) · [11. Fall 2018 Final Examination →](11-fall-2018-final-examination.md)
