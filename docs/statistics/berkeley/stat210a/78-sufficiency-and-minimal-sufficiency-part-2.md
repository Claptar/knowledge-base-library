---
title: "78. Sufficiency and Minimal Sufficiency (part 2)"
course: "Berkeley Stat 210A Fall 2024"
chapter: 78
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 78. Sufficiency and Minimal Sufficiency (part 2)

## What this covers

This chapter answers a single question: what does it mean for a summary of data to lose no
information about a parameter, and how do we find the *most compressed* such summary? It defines a
**sufficient statistic**, gives the factorization theorem as the standard tool for recognizing one,
works through the examples that motivate it (Bernoulli/binomial, normal, Poisson, uniform location),
and then asks which sufficient statistic is smallest — **minimal sufficiency** — building a
criterion for recognizing it from the likelihood ratio alone. It assumes familiarity with joint
densities and pmfs with respect to a dominating measure, conditional distributions, and the
coin-flip binomial model used to introduce point estimation.

## What is a sufficient statistic?

Let $X\sim P_\theta$ be the entire data set, drawn from a model $\mathcal{P} = \{P_\theta:\theta\in\Theta\}$.
A *statistic* $T(X)$ is any function of the data alone — it must not depend on the unknown $\theta$.
We call $T(X)$ **sufficient** for $\mathcal{P}$ if the conditional distribution $P_\theta(X\mid T)$
does not depend on $\theta$.

The intuition: once you know $T(X)$, whatever randomness remains in $X$ carries no further
information about $\theta$, because its distribution is the same for every candidate value of
$\theta$. So working with $T(X)$ instead of the full data set throws away nothing that could help
estimate $\theta$.

**Example (independent Bernoulli sequence).** Picture an investigator flipping a biased coin $n$
times and recording only the number of heads — the binomial count used to introduce estimation.
Had the investigator kept the entire sequence of flips $X_1,\ldots,X_n$, i.i.d. $\text{Bern}(\theta)$,
would anything have been lost by reducing it to $T(X)=\sum_i X_i$?

The joint pmf on $\{0,1\}^n$ is
$$
p_\theta(x) = \prod_{i=1}^n \theta^{x_i}(1-\theta)^{1-x_i} = \theta^{\sum_i x_i}(1-\theta)^{n-\sum_i x_i},
$$
which depends on $x$ only through $t=\sum_i x_i$: every sequence with $t$ heads gets the same
probability $\theta^t(1-\theta)^{n-t}$. So conditional on $T(X)=t$, all $\binom{n}{t}$ such sequences
should be equally likely, and a direct calculation confirms it:
$$
\mathbb{P}_\theta(X=x\mid T(X)=t) = \frac{\mathbb{P}_\theta(X=x,\sum_i X_i=t)}{\mathbb{P}_\theta(T(X)=t)}
= \frac{\theta^t(1-\theta)^{n-t}\mathbb{1}\{\sum_i x_i=t\}}{\theta^t(1-\theta)^{n-t}\binom{n}{t}}
= \binom{n}{t}^{-1}\mathbb{1}\{T(x)=t\}.
$$
The $\theta$-dependence cancels exactly, leaving a distribution — uniform over the sequences with
$t$ heads — that does not depend on $\theta$. So $T(X)$ is sufficient: nothing about $\theta$ was
lost by recording only the count.

## A picture: when does conditioning erase $\theta$?

To see what sufficiency does and does not buy you, compare two models for a pair
$X_1,X_2$, i.i.d. from a pmf $p_\theta(x)$ on $\{0,\ldots,n\}$, and in both cases set $T(X)=X_1+X_2$.

**Binomial.** Here $p_\theta(x)=\binom{n}{x}\theta^x(1-\theta)^{n-x}$, and
$$
\mathbb{P}_\theta(X=x) = \binom{n}{x_1}\theta^{x_1}(1-\theta)^{n-x_1}\binom{n}{x_2}\theta^{x_2}(1-\theta)^{n-x_2}
= \theta^{T(x)}(1-\theta)^{2n-T(x)}\binom{n}{x_1}\binom{n}{x_2}.
$$
Conditioning on $T(X)=t$ by Bayes' rule, the $\theta$-dependent factor cancels as before:
$$
\mathbb{P}_\theta(X=x\mid T(X)=t) = \frac{\binom{n}{x_1}\binom{n}{x_2}\mathbb{1}\{x_1+x_2=t\}}{\sum_{k=0}^t \binom{n}{k}\binom{n}{t-k}},
$$
and the identity $\sum_{k=0}^t\binom{n}{k}\binom{n}{t-k}=\binom{2n}{t}$ turns this into a
hypergeometric distribution,
$$
\mathbb{P}_\theta(X_1=x_1\mid T(X)=t) = \frac{\binom{n}{x_1}\binom{n}{t-x_1}}{\binom{2n}{t}} = \text{Hypergeom}(2n,n,t),
$$
with no $\theta$ left in it: $T$ is sufficient.

**Discrete Laplace.** Now let $p_\theta(x)\propto e^{-|x-n\theta|}$ on $\{0,\ldots,n\}$ instead — a
pmf that concentrates near $n\theta$ and decays exponentially away from it. $T(X)=X_1+X_2$ is *not*
sufficient here. Take $\theta=0.3$: the pair $(1,2)$ is much more probable than $(0,3)$, because
both coordinates sit closer to the mode $n\theta$. But as $\theta$ moves toward $0$ or $1$, every
remaining sequence with the same sum becomes roughly equally likely, since all of them sit equally
far out in the tail. So $\mathbb{P}_\theta(X=x\mid T(X)=t)$ genuinely changes shape as $\theta$
varies — conditioning on the sum has not thrown away all the $\theta$-information.

<figure>
<svg viewBox="0 0 320 260" role="img" aria-label="Grid of possible values of two independent counts, with the diagonal where their sum equals a fixed t highlighted">
  <line x1="40" y1="230" x2="280" y2="230" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="230" x2="40" y2="40" stroke="currentColor" stroke-width="1"/>
  <text x="282" y="245" font-size="12" fill="currentColor">X1</text>
  <text x="12" y="38" font-size="12" fill="currentColor">X2</text>
  <g fill="currentColor" fill-opacity="0.2">
    <circle cx="40" cy="220" r="3"/><circle cx="40" cy="180" r="3"/><circle cx="40" cy="140" r="3"/><circle cx="40" cy="100" r="3"/>
    <circle cx="90" cy="220" r="3"/><circle cx="90" cy="180" r="3"/><circle cx="90" cy="140" r="3"/><circle cx="90" cy="60" r="3"/>
    <circle cx="140" cy="220" r="3"/><circle cx="140" cy="180" r="3"/><circle cx="140" cy="100" r="3"/><circle cx="140" cy="60" r="3"/>
    <circle cx="190" cy="220" r="3"/><circle cx="190" cy="140" r="3"/><circle cx="190" cy="100" r="3"/><circle cx="190" cy="60" r="3"/>
    <circle cx="240" cy="180" r="3"/><circle cx="240" cy="140" r="3"/><circle cx="240" cy="100" r="3"/><circle cx="240" cy="60" r="3"/>
  </g>
  <line x1="40" y1="60" x2="240" y2="220" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.5"/>
  <g fill="currentColor">
    <circle cx="40" cy="60" r="4"/>
    <circle cx="90" cy="100" r="9"/>
    <circle cx="140" cy="140" r="12"/>
    <circle cx="190" cy="180" r="9"/>
    <circle cx="240" cy="220" r="4"/>
  </g>
  <text x="150" y="132" font-size="12" fill="currentColor" text-anchor="middle">T = X1 + X2 = t</text>
</svg>
<figcaption>The support of $(X_1,X_2)$ conditional on $T=X_1+X_2=t$ is exactly the antidiagonal
$x_1+x_2=t$ (dashed line). In the binomial case, the relative weights along that diagonal (circle
sizes, here the hypergeometric shape for $n=4,\,t=4$) do not depend on $\theta$ — only $\theta$
decides which diagonal the joint distribution mostly sits near before conditioning. In the discrete
Laplace case the weights along the diagonal still shift with $\theta$, which is exactly the failure
of sufficiency.</figcaption>
</figure>

## The factorization theorem

Both calculations above worked the same way: the joint density split into a $\theta$-and-$T(x)$
part and a $\theta$-free part, and that alone was enough to make the conditional distribution
collapse to something $\theta$-free. This is worth stating as a theorem, since checking a
factorization is much easier than computing a conditional distribution directly.

**Factorization theorem.** Let $\mathcal{P}$ have densities $p_\theta(x)$ with respect to a common
dominating measure $\mu$. Then $T(X)$ is sufficient for $\mathcal{P}$ if and only if there exist
non-negative functions $g_\theta$ and $h$ with
$$
p_\theta(x) = g_\theta(T(x))\,h(x)
$$
for $\mu$-almost every $x$. ("Almost every" rules out redefining the densities on a $\mu$-null set
to destroy the factorization without changing any of the actual distributions.)

*Proof (discrete $\mathcal{X}$).* Take $\mu$ to be the counting measure without loss of generality
(otherwise carry along its density $m(x)$ throughout). If the factorization holds,
$$
\mathbb{P}_\theta(X=x\mid T(X)=t) = \frac{\mathbb{P}_\theta(X=x,T(X)=t)}{\mathbb{P}_\theta(T(X)=t)}
= \frac{g_\theta(t)h(x)\mathbb{1}\{T(x)=t\}}{g_\theta(t)\sum_{z:T(z)=t}h(z)}
= \frac{h(x)\mathbb{1}\{T(x)=t\}}{\sum_{z:T(z)=t}h(z)},
$$
with the $g_\theta(t)$ cancelling, so $T$ is sufficient.

Conversely, if $T(X)$ is sufficient, set $g_\theta(t)=\mathbb{P}_\theta(T(X)=t)$ and
$h(x)=\mathbb{P}(X=x\mid T(X)=T(x))$ — well defined without reference to $\theta$ precisely because
$T$ is sufficient. Then
$$
\mathbb{P}_\theta(X=x) = \mathbb{P}_\theta(T(X)=T(x))\cdot \mathbb{P}_\theta(X=x\mid T(X)=T(x)) = g_\theta(T(x))h(x),
$$
which is the required factorization. $\blacksquare$

## Reading off sufficiency from the density

Three worked examples, each reducing to inspection of the joint density.

**Normal location family.** $X_1,\ldots,X_n$, i.i.d. $N(\theta,1)$, so each observation has density
$\frac{1}{\sqrt{2\pi}}e^{-(x-\theta)^2/2} = \frac{1}{\sqrt{2\pi}}e^{-x^2/2+\theta x-\theta^2/2}$, and
the joint density over $X=(X_1,\ldots,X_n)$ is
$$
p_\theta(x) = \underbrace{e^{\theta\sum_i x_i - n\theta^2/2}}_{g_\theta(\sum_i x_i)}\cdot\underbrace{(2\pi)^{-n/2}\prod_i e^{-x_i^2/2}}_{h(x)},
$$
so $\sum_i X_i$ is sufficient.

**Poisson family.** $X_1,\ldots,X_n$, i.i.d. $\text{Pois}(\theta)$, $p_\theta(x)=\theta^xe^{-\theta}/x!$, and
$$
p_\theta(x) = \prod_i \frac{\theta^{x_i}e^{-\theta}}{x_i!} = \underbrace{e^{(\log\theta)\sum_i x_i - n\theta}}_{g_\theta(\sum_i x_i)}\cdot\underbrace{\Big(\prod_i x_i!\Big)^{-1}}_{h(x)},
$$
again making $\sum_i X_i$ sufficient. The two calculations look alike because both models are
instances of an *exponential family*, a structure taken up in the next lecture.

**Uniform location family.** $X_1,\ldots,X_n$, i.i.d. $U[\theta,\theta+1]$, $p_\theta(x)=\mathbb{1}\{\theta\le x\le\theta+1\}$.
Here
$$
p_\theta(x) = \prod_i \mathbb{1}\{\theta\le x_i\le\theta+1\} = \mathbb{1}\{\theta\le \min_i x_i\}\cdot\mathbb{1}\{\max_i x_i\le \theta+1\},
$$
so $T(X)=(\min_i X_i,\max_i X_i)$ is sufficient — a pair of order statistics rather than a sum,
showing the factorization theorem is not tied to smooth exponential-family densities.

## Minimal sufficiency

Sufficiency alone is a weak requirement: the full data set $X$ is always sufficient (condition on
$T(X)=X$ and there is nothing left to be random). So is $\overline X = \frac1n\sum_i X_i$ whenever
$\sum_i X_i$ is, and so is the vector of order statistics $S(X)=(X_{(1)},\ldots,X_{(n)})$ for the
normal location family, since $\sum_i X_i$ is a function of $S(X)$. These are not equally useful:
$\overline X$ and $\sum_i X_i$ carry the same information and both can be recovered from $S(X)$,
and $S(X)$ from $X$, but not the reverse — $S(X)$ cannot be recovered from $\overline X$ alone, and
$X$ cannot be recovered from $S(X)$ (the original order of the sample is lost). So among these four
sufficient statistics there is a strict order of compression, from most ($\overline X$ or
$\sum_i X_i$) to least ($X$ itself), with $S(X)$ in between.

Any statistic from which a sufficient one is recoverable is automatically sufficient too:

**Proposition.** If $T(X)$ is sufficient and $T(X)=f(S(X))$ for some $f$, then $S(X)$ is sufficient.

*Proof.* Factor $p_\theta(x)=g_\theta(T(x))h(x) = (g_\theta\circ f)(S(x))\,h(x)$, which is a valid
factorization through $S$. $\blacksquare$

This gives a natural notion of the *most compressed* sufficient statistic. Say $T(X)$ is
**minimal sufficient** if

1. $T(X)$ is sufficient, and
2. for every other sufficient statistic $S(X)$, $T(X)=f(S(X))$ for some $f$ (almost surely in $\mathcal{P}$).

To recognize one, define an equivalence relation on the sample space: $x\equiv_{\mathcal{P}} y$ if
the likelihood ratio $p_\theta(x)/p_\theta(y)$ does not depend on $\theta$. Two data points are
equivalent exactly when no possible value of $\theta$ can be favored by one over the other through
the likelihood ratio — the data give no way to tell them apart.

**Any sufficient statistic can only merge equivalent points.** If $T(x)=T(y)=t$ then
$$
\frac{p_\theta(x)}{p_\theta(y)} = \frac{\mathbb{P}_\theta(X=x,T(X)=t)}{\mathbb{P}_\theta(X=y,T(X)=t)}
= \frac{\mathbb{P}(X=x\mid T(X)=t)}{\mathbb{P}(X=y\mid T(X)=t)},
$$
which is $\theta$-free by sufficiency of $T$. So $T(x)=T(y)\implies x\equiv_{\mathcal{P}} y$ for
*any* sufficient $T$: sufficiency never collapses two inequivalent points together. A minimal
sufficient statistic is the one that collapses as much as it possibly can — its level sets are
exactly the equivalence classes, no finer:

**Proposition.** If $x\equiv_{\mathcal{P}} y \iff T(x)=T(y)$, then $T(X)$ is minimal sufficient.

*Proof (discrete $\mathcal{X}$).* $T$ is sufficient: for $T(x)=t$,
$$
\mathbb{P}_\theta(X=x\mid T(X)=t) = \frac{p_\theta(x)}{\sum_{z:T(z)=t}p_\theta(z)} = \frac{1}{\sum_{z:T(z)=t}p_\theta(z)/p_\theta(x)},
$$
and every $z$ in that sum has $T(z)=t=T(x)$, hence $z\equiv_{\mathcal{P}} x$ by hypothesis, so each
ratio $p_\theta(z)/p_\theta(x)$ — and the whole sum — is $\theta$-free.

$T$ is minimal: let $S(X)$ be any other sufficient statistic, and suppose $S(x)=S(y)=s$. By the
argument above (applied to $S$), $x\equiv_{\mathcal{P}} y$, so by hypothesis $T(x)=T(y)$; define
$f(s)$ to be this common value. This $f$ is well defined because every $z$ with $S(z)=s$ is
likewise equivalent to $x$, forcing $T(z)=T(x)=f(S(z))$. So $T=f\circ S$ for every sufficient $S$.
$\blacksquare$

**What minimality looks like.** Sufficiency requires a statistic's level sets to lie inside the
equivalence classes $\equiv_{\mathcal{P}}$ — it is never allowed to lump together two points the
likelihood can still tell apart. Minimality asks for equality: the level sets *are* the equivalence
classes. Every other sufficient statistic sits somewhere between the minimal one and the raw data
$X$, partitioning the sample space no coarser than the equivalence classes, but possibly much finer.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Sample space partitioned into equivalence classes, with a finer partition inside one class from a non-minimal sufficient statistic">
  <rect x="20" y="30" width="280" height="140" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="160" y="20" font-size="12" text-anchor="middle" fill="currentColor">sample space</text>
  <line x1="120" y1="30" x2="120" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="210" y1="30" x2="210" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="20" y1="100" x2="120" y2="100" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="70" y="118" font-size="10" text-anchor="middle" fill="currentColor">finer, from a non-minimal S</text>
  <text x="165" y="102" font-size="11" text-anchor="middle" fill="currentColor">one class</text>
  <text x="255" y="102" font-size="11" text-anchor="middle" fill="currentColor">another</text>
</svg>
<figcaption>The solid lines are the equivalence classes under $\equiv_{\mathcal{P}}$ — the level
sets of the minimal sufficient statistic $T$. A sufficient statistic $S$ that is not minimal
(dashed line) is only allowed to subdivide within a class, never to cross one, since crossing would
merge inequivalent points.</figcaption>
</figure>

**Illustration: the Laplace location family.** The reader's applet for this section plots
$\ell(\theta) = -n\log 2 - \sum_i |x_i-\theta|$, the log-likelihood for $X_1,\ldots,X_n$, i.i.d.
$\text{Laplace}(\theta,1)$, for a sample the user can regenerate at will. The curve is piecewise
linear in $\theta$, with a kink exactly at each observed value $x_i$ (the plotted "knots"). Since
the whole likelihood-ratio function $\ell(\theta)-\ell(\theta')$ is determined by, and determines,
the locations of these kinks, two samples are equivalent under $\equiv_{\mathcal{P}}$ exactly when
they place their kinks at the same points — that is, when they share the same order statistics.
That matches the criterion just proved: the natural candidate for the minimal sufficient statistic
in this family is the full vector of order statistics, not any smaller summary such as the sum.

## Sources

- Berkeley STAT210A course reader, "Sufficiency" (author: Will Fithian), converted copies from
  fall-2024, fall-2025 and fall-2026 (`reader/sufficiency.qmd` / `.html`, licensed CC BY 4.0; also
  duplicated as `units/reader/sufficiency` in fall-2025). The three years are near-identical; this
  chapter follows the fall-2025/fall-2026 wording, which adds the discrete-Laplace counterexample
  and the hypergeometric derivation that the fall-2024 wording only asserted for the two-binomial
  case.
  - Definition of statistic and sufficiency, Bernoulli/binomial example: `01-sufficiency.md` (all
    three years).
  - Binomial-vs-discrete-Laplace visualization and hypergeometric conditional distribution:
    `02-visualization-of-sufficiency*.md` (fall-2025, fall-2026; the fall-2024 version covers only
    the binomial half, without the discrete-Laplace comparison).
  - Factorization theorem and discrete-case proof: `03-factorization-theorem.md` (all three years).
  - Normal, Poisson and uniform-location examples: `04-examples.md` (all three years).
  - Minimal sufficiency — recoverability proposition, definition, equivalence relation, and the
    characterization proposition with proof: `05-minimal-sufficiency.md` (fall-2024) /
    `06-minimal-sufficiency.md` (fall-2025, fall-2026). The Laplace log-likelihood applet used for
    the closing illustration appears only in the fall-2025 and fall-2026 versions.
- Three section headings in the reader — "Statement for general $\mathcal{X}$" (end of the
  factorization-theorem page), and "Interpretations of sufficiency" and "Sufficient statistics
  under i.i.d. sampling" (end of the examples page) — are present in all three years but carry no
  body text in any of them. The lecture evidently moved on to these topics but the material was not
  captured in what was supplied here.
- No slides, transcript, or exercise set were supplied for this lecture.

---

[← 77. Sufficiency, Testing, and Bayes: A Final Exam](77-sufficiency-testing-and-bayes-a-final-exam.md) · [Contents](index.md) · [79. Stat 210A: Course Information →](79-stat-210a-course-information.md)
