---
title: "30. Sufficient Statistics and Factorization"
course: "Berkeley Stat 210A"
chapter: 30
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 30. Sufficient Statistics and Factorization

## What this covers

This chapter answers a basic question about statistical models: when is it safe to throw away
part of the data and keep only a summary of it? It develops the formal notion of a **sufficient
statistic**, checks it by hand for $n$ coin flips, and then gives a general tool — the
**factorization theorem** — for spotting sufficiency directly from the density, without ever
computing a conditional distribution. It assumes familiarity with a statistical model
$\mathcal P = \{P_\theta : \theta \in \Theta\}$, conditional probability, and the binomial and
exponential-family densities.

## Motivating example: summarizing coin flips

Let $X_1, \dots, X_n \overset{\text{iid}}{\sim} \text{Bernoulli}(\theta)$, so that

$$X \sim \prod_{i=1}^n \theta^{X_i}(1-\theta)^{1-X_i} \quad \text{on } \{0,1\}^n.$$

Let $T(X) = \sum_i X_i$. Then $T(X) \sim \text{Binomial}(n,\theta)$:

$$P_\theta(T=t) = \binom{n}{t}\theta^t(1-\theta)^{n-t}, \qquad t \in \{0, \dots, n\}.$$

Passing from the full sequence $(X_1,\dots,X_n)$ to the single number $T(X)$ throws away
information — in particular, which flips were heads. The question the rest of the chapter answers
is: why is that discarding harmless? In exponential-family language, $T(X)$ is called the
*sufficient statistic* for $X$, and the goal is to see precisely why that name is earned.

## The definition of sufficiency

**Definition.** Let $\mathcal P = \{P_\theta : \theta \in \Theta\}$ be a statistical model for data
$X$. A statistic $T(X)$ is **sufficient** for $\mathcal P$ if the conditional distribution
$P_\theta(X \mid T)$ does not depend on $\theta$.

The intuition: once you know $T(X)$, whatever is left over in $X$ carries no further information
about $\theta$ — its distribution is the same no matter which $\theta$ generated the data.

### Checking it directly for the coin-flip example

Return to $X_1,\dots,X_n \overset{\text{iid}}{\sim}\text{Bernoulli}(\theta)$ and $T(X) =
\sum_i X_i$. For $x \in \{0,1\}^n$ and $t = \sum_i x_i$,

$$P_\theta(X=x \mid T=t) = \frac{P_\theta(X=x,\,T=t)}{P_\theta(T=t)} = \frac{\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}\mathbf 1\{\sum x_i = t\}}{\binom{n}{t}\theta^t(1-\theta)^{n-t}} = \frac{\mathbf 1\{\sum x_i = t\}}{\binom{n}{t}}.$$

Every $\theta$-dependent factor cancels. So conditional on $T(X) = t$, $X$ is exactly uniform over
the $\binom{n}{t}$ sequences with $t$ ones — no matter what $\theta$ is. That confirms $T$ is
sufficient: the full sequence tells you nothing about $\theta$ beyond what the count already told
you.

## The factorization theorem

Checking sufficiency from the definition means computing a conditional distribution, which is
often awkward. Usually it is much easier to read a candidate sufficient statistic straight off the
density.

**Theorem (factorization theorem).** Let $\mathcal P = \{P_\theta : \theta \in \Theta\}$ have
densities $p_\theta(x)$ with respect to a common measure $\mu$. Then $T(X)$ is sufficient for
$\mathcal P$ if and only if there exist functions $g_\theta(t)$ and $h(x)$ such that

$$p_\theta(x) = g_\theta(T(x))\,h(x)$$

for $\mu$-almost every $x$, i.e. $\mu(\{x : p_\theta(x) \ne g_\theta(T(x))h(x)\}) = 0$ for every
$\theta$.

The "almost every" qualifier rules out cheap counterexamples made by changing $p_{\theta_0}(x_0)$
at a single point $x_0$ for a single $\theta_0$: such a change would break an exact pointwise
identity but should not be allowed to break sufficiency. (A fully rigorous proof, handling general
$\mu$, is in Keener §6.4; what follows is the argument for a discrete sample space.)

### Proof, discrete case

Assume without loss of generality that $\mu$ is counting measure on $\mathcal X$.

**($\Leftarrow$)** Suppose $p_\theta(x) = g_\theta(T(x))h(x)$ for all $x$. Then

$$P_\theta(X=x \mid T=t) = \frac{P_\theta(X=x,\,T(x)=t)}{P_\theta(T(x)=t)} = \frac{g_\theta(t)\,h(x)\,\mathbf 1\{T(x)=t\}}{\sum_{T(z)=t} g_\theta(t)\,h(z)} = \frac{h(x)\,\mathbf 1\{T(x)=t\}}{\sum_{T(z)=t}h(z)},$$

where $g_\theta(t)$ cancels between numerator and denominator, since it does not depend on $z$
inside the sum. The result has no $\theta$ in it, so $T$ is sufficient.

**($\Rightarrow$)** Suppose $T(X)$ is sufficient. Define

$$g_\theta(t) = \sum_{T(x)=t} p_\theta(x) = P_\theta(T(X)=t).$$

Fix any $\theta_0 \in \Theta$ and define

$$h(x) = \frac{p_{\theta_0}(x)}{\sum_{T(z)=T(x)} p_{\theta_0}(z)} = P_{\theta_0}(X=x \mid T(X)=T(x)).$$

Because $T$ is sufficient, $P_\theta(X=x \mid T(X)=T(x))$ does not depend on $\theta$ — so writing it
with $\theta_0$ costs nothing, and $h$ is a genuine function of $x$ alone with no hidden
$\theta$-dependence. Now

$$g_\theta(T(x))\,h(x) = P_\theta(T=T(x))\cdot P(X=x \mid T=T(x)) = P_\theta(X=x),$$

which is exactly the factorization required. $\blacksquare$

## What sufficiency means: a two-stage generative story

The factorization theorem also explains *why* sufficiency is the right notion of "no information
lost." $X$ is informative about $\theta$ only because its distribution depends on $\theta$. Split
the generation of $X$ into two stages:

1. Generate $T$ — its distribution depends on $\theta$.
2. Generate $X \mid T$ — by sufficiency, this step does **not** depend on $\theta$.

<figure>
<svg viewBox="0 0 380 200" role="img" aria-label="Theta drives T, and T drives both the real data X and a resampled copy X-tilde, both with the same distribution.">
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0 0, 8 4, 0 8" fill="currentColor"/>
    </marker>
  </defs>
  <text x="30" y="65" font-size="13" fill="currentColor">&#952;</text>
  <text x="150" y="65" font-size="13" fill="currentColor">T(X)</text>
  <text x="300" y="65" font-size="13" fill="currentColor">X</text>
  <text x="288" y="178" font-size="13" fill="currentColor">X&#771;</text>

  <line x1="45" y1="60" x2="140" y2="60" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="90" y="45" text-anchor="middle" font-size="11" fill="currentColor">Step 1</text>

  <line x1="180" y1="60" x2="290" y2="60" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="235" y="45" text-anchor="middle" font-size="11" fill="currentColor">Step 2</text>

  <line x1="175" y1="70" x2="285" y2="162" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrowhead)"/>
  <text x="260" y="125" text-anchor="middle" font-size="11" fill="currentColor">fake Step 2</text>

  <text x="90" y="90" text-anchor="middle" font-size="11" fill="currentColor">depends on &#952;</text>
  <text x="235" y="90" text-anchor="middle" font-size="11" fill="currentColor">free of &#952;</text>
</svg>
<figcaption>θ determines the distribution of T(X); given T, both the real X and a freshly
resampled X̃ ~ P(X | T) are generated by the same θ-free rule, so X̃ has the same distribution as
X and carries exactly the same information about θ.</figcaption>
</figure>

### The sufficiency principle

If $T(X)$ is sufficient for $\mathcal P$, any statistical procedure should depend on the data only
through $T(X)$. Concretely: instead of using $X$, you could throw it away and draw a fresh
$\widetilde X \sim P(X \mid T)$ — built with no reference to $\theta$ at all — and $\widetilde X$
would be exactly as good as $X$, because $\widetilde X \sim P_\theta$ too. In the diagram, there is
no reason to pay attention to the arrow from $T(X)$ to $X$: the resampled $\widetilde X$ carries
exactly the same distributional information as the real one.

## Examples

**Exponential families.** If

$$p_\theta(x) = \underbrace{e^{\eta(\theta)'T(x) - B(\theta)}}_{g_\theta(T(x))}\;\underbrace{h(x)}_{h(x)},$$

the factorization is already sitting in the exponential-family form: everything involving $\theta$
appears only through $T(x)$, so $T(X)$ is sufficient by the factorization theorem. This matches the
coin-flip computation above: $T(X) = \sum_i X_i$ is exactly the natural sufficient statistic for
the Bernoulli/binomial exponential family.

**Uniform location family.** The lecture opened a second example,
$X_1,\dots,X_n \overset{\text{iid}}{\sim} U(\cdots)$, presumably to show that factorization also
handles families whose *support* depends on $\theta$ — where the indicator enforcing the support
constraint becomes part of $g_\theta(T(x))$. The source notes break off at this point, before the
density is written down, so the example is not reconstructed here.

## Sources

- Notes: `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture04-F24.md` (Berkeley
  STAT210A, Fall 2024, Lecture 4, 9/5/2023) — the coin-flip motivation, the definition of
  sufficiency, the direct computation for the binomial example, the factorization theorem and its
  discrete-case proof, the two-stage/sufficiency-principle discussion, and the exponential-family
  example all come from this file. These are model-reconstructed handwritten notes converted from
  a PDF with no text layer, so treat every displayed equation as unverified against the original.
- The lecture points to a rigorous proof of the factorization theorem "in Keener 6.4" (Robert
  Keener, *Theoretical Statistics*) — not contained in the supplied notes.
- Not covered here: the lecture's opening "Review" outline item (its content is not present in
  this file) and the uniform location family example, which is cut off mid-sentence in the source
  before its density is written down.

---

[← 29. Canonical Form](29-canonical-form.md) · [Contents](index.md) · [31. Sufficiency and Minimal Sufficiency (part 1) →](31-sufficiency-and-minimal-sufficiency-part-1.md)
