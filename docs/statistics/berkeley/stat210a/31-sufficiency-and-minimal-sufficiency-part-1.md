---
title: "31. Sufficiency and Minimal Sufficiency (part 1)"
course: "Berkeley Stat 210A"
chapter: 31
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 31. Sufficiency and Minimal Sufficiency (part 1)

## What this covers

This chapter asks what it means for a statistic — some function of the data — to summarize a
sample without throwing away information about an unknown parameter. It defines **sufficiency**
directly from conditional distributions, gives the standard tool for recognizing a sufficient
statistic by inspecting a density (the **factorization theorem**), and then asks how far a
sufficient statistic can be compressed, which leads to **minimal sufficiency** and a general
recognition criterion built from the likelihood function (**Bahadur's theorem**). It assumes
familiarity with densities with respect to a common dominating measure, conditional distributions,
and order statistics.

## A motivating example: three models for coin flipping

Consider data $X_{i,j}$, for $i = 1, \dots, 48$ and $j = 1, \dots, n_i$, recording the outcome of
flip $j$ in group $i$. Three nested models describe increasingly less restrictive versions of the
same data:

- **Model 3.** $X_{i,j} \overset{\text{ind}}{\sim} \text{Bernoulli}(\theta_{i,j})$, with
  $\theta_{i,j}$ decreasing in $j$ within each group — a separate, monotone-in-$j$ success
  probability for every group and every position.
- **Model 2.** $X_{i+} \overset{\text{ind}}{\sim} \text{Binomial}(n_i, \theta_i)$, where
  $X_{i+} = \sum_{j=1}^{n_i} X_{i,j}$ — one probability per group.
- **Model 1.** $X_{++} \sim \text{Binomial}(n, \theta)$, where
  $X_{++} = \sum_{i=1}^{48}\sum_{j=1}^{n_i} X_{i,j}$ and $n = \sum_i n_i$ — a single probability
  for everything.

Model 1 makes the most assumptions (one shared $\theta$) and so is the most restrictive; Model 3
makes the fewest. The families of distributions are nested, $\mathcal{P}_1 \subseteq \mathcal{P}_2
\subseteq \mathcal{P}_3$, because each more restrictive model is a special case of the next.

Notice that as the model gets more restrictive, the data needed to work with it shrinks: fitting
Model 1 only requires the grand total $X_{++}$; fitting Model 2 requires the vector of group
totals $(X_{1+}, \dots, X_{48+})$. **Are we losing anything by throwing away everything except
these totals?**

The answer is no: $X_{++}$ is a **sufficient statistic** for $\mathcal{P}_1$, and
$(X_{1+}, \dots, X_{48+})$ is sufficient for $\mathcal{P}_2$. The rest of this chapter makes that
statement precise and shows how to check it.

## Statistics and sufficiency

**Definition.** A **statistic** $T(X)$ is any function of the data $X$.

**Definition.** A statistic $T(X)$ is **sufficient** for a model $\mathcal{P} = \{P_\theta\}$ if
the conditional distribution of $X \mid T(X)$ is the same for every $P_\theta \in \mathcal{P}$.

The point of the definition: if $X \mid T(X)$ doesn't depend on $\theta$, then once you know
$T(X)$, the rest of $X$ contains no further evidence about $\theta$ — you could simulate the
remaining randomness yourself, without knowing $\theta$, and it would look exactly like the real
data.

### Checking sufficiency directly: $X_{++}$ in Model 1

Under $\mathcal{P}_1$ the joint density of the full data $x = (x_{ij})$ is

$$p_\theta(x) = \prod_{i=1}^{48}\prod_{j=1}^{n_i} \theta^{x_{ij}}(1-\theta)^{1-x_{ij}} = \theta^{X_{++}}(1-\theta)^{n-X_{++}}.$$

There is no binomial coefficient here — $p_\theta(x)$ is the probability of one specific sequence
of $0$s and $1$s, not the probability of a count. The coefficient $\binom{n}{t}$ appears only when
we compute the probability that the *total* equals $t$, since $\binom{n}{t}$ different sequences
give that total:

$$P_\theta(X_{++} = t) = \binom{n}{t}\theta^t(1-\theta)^{n-t}.$$

Now compute the conditional distribution required by the definition:

$$P_\theta(X = x \mid X_{++} = t) = \frac{P_\theta(X=x,\, X_{++}=t)}{P_\theta(X_{++}=t)} = \frac{\mathbf{1}\{X_{++}=t\}\cdot \theta^t(1-\theta)^{n-t}}{\binom{n}{t}\theta^t(1-\theta)^{n-t}} = \frac{\mathbf{1}\{X_{++}=t\}}{\binom{n}{t}}.$$

The $\theta$s cancel completely: given the total $t$, every sequence with that many $1$s is
equally likely, and this does not depend on $\theta$. So $X_{++}$ is sufficient for $\mathcal{P}_1$.

**Intuition.** Suppose you believe Model 1. A large or small total $X_{++}$ is more or less likely
depending on $\theta$ — that is where the information about $\theta$ lives. But once you are told
$X_{++} = 178{,}079$, every specific arrangement of that many heads among $n$ flips is exactly as
likely as any other, *regardless of $\theta$*. There is nothing left in the arrangement that
$\theta$ could have produced.

This calculation used the exchangeability built into Model 1 (a single shared $\theta$) in an
essential way. It is **not** true in Models 2 or 3: there $\theta$ varies across groups (or across
$j$), so which group contributed which $1$s is itself informative, and $X_{++}$ is no longer
sufficient once you drop down to those larger models.

## The factorization theorem

Checking sufficiency from the definition means computing a conditional distribution, which is
awkward. Usually a sufficient statistic can be spotted just by looking at the density.

**Theorem (Factorization theorem).** Let $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ have
densities $p_\theta(x)$ with respect to a common measure $\mu$. Then $T(X)$ is sufficient for
$\mathcal{P}$ if and only if there exist functions $g_\theta(t)$ and $h(x) \ge 0$ such that

$$p_\theta(x) = g_\theta\big(T(x)\big)\, h(x) \qquad \text{for } \mu\text{-almost every } x.$$

**Reading the statement.** The factor $h(x) \geq 0$ can be absorbed into the dominating measure:
define $\nu(A) = \int_A h(x)\, d\mu(x)$, and then $\mathcal{P}$ has densities
$p_\theta(x) = g_\theta(T(x))$ with respect to $\nu$. So, after the right change of base measure,
the density depends on $x$ *only* through $T(x)$. The factor $g_\theta(T(x))$ cannot similarly be
absorbed, because it depends on $\theta$.

**Proof, discrete case.** Take $\mu$ to be counting measure, without loss of generality.

($\Leftarrow$) Assume $p_\theta(x) = g_\theta(T(x))h(x)$. Then

$$P_\theta(X=x \mid T(X)=t) = \frac{P_\theta(X=x,\,T(X)=t)}{P_\theta(T(X)=t)} = \frac{g_\theta(t)\,h(x)\,\mathbf{1}\{T(x)=t\}}{\sum_{z: T(z)=t} g_\theta(t)\,h(z)},$$

and $g_\theta(t)$ cancels top and bottom, leaving something free of $\theta$.

($\Rightarrow$) Assume $T(X)$ is sufficient. Define

$$g_\theta(t) = P_\theta(T(X)=t), \qquad h(x) = P(X=x \mid T(X)=T(x)),$$

where $h$ does not depend on $\theta$ because $T(X)$ is sufficient. Then

$$g_\theta(T(x))\,h(x) = P_\theta\big(T(X)=T(x) \text{ and } X=x\big) = P_\theta(X=x) = p_\theta(x). \qquad \blacksquare$$

The proof for general (non-discrete) sample spaces is similar, with more care needed about what
conditioning on $T(X)=t$ means in continuous spaces.

### Examples

**Normal location family.** Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} N(\theta,1)$. Then

$$p_\theta(x) = (2\pi)^{-n/2}\prod_{i=1}^n e^{-(x_i-\theta)^2/2} = e^{\theta \sum x_i - n\theta^2/2}\cdot \frac{e^{-\sum x_i^2/2}}{(2\pi)^{n/2}}.$$

Collecting every factor that does not involve $\theta$ into $h(x)$ and everything else into
$g_\theta(T(x))$ with $T(x) = \sum x_i$ shows $\sum X_i$ is sufficient.

**Poisson family.** Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} \text{Pois}(\theta)$. Then

$$p_\theta(x) = \prod_{i=1}^n \frac{\theta^{x_i}e^{-\theta}}{x_i!} = \theta^{\sum x_i}e^{-n\theta}\cdot \frac{1}{\prod x_i!},$$

so again $T(x) = \sum x_i$ is sufficient. (These two examples share a structural feature relevant
to the next topic, exponential families — not developed in this chapter.)

**Uniform location family.** Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} U[\theta,\theta+1]$.
Then

$$p_\theta(x) = \prod_{i=1}^n \mathbf{1}\{\theta \le x_i \le \theta+1\} = \mathbf{1}\{\theta \le X_{(1)}\}\cdot \mathbf{1}\{X_{(n)} \le \theta+1\},$$

so the pair $(X_{(1)}, X_{(n)})$ — the smallest and largest observations — is sufficient. Here $T$
does not reduce to a single number, and there is no way to factor $h(x)$ so as to depend on fewer
than both extremes.

## What sufficiency buys you

$X$ carries information about $\theta$ only because its distribution depends on $\theta$. The
factorization theorem suggests thinking of the data as generated in two stages: first $T(X)$ is
drawn, from a distribution that depends on $\theta$; then $X$ is drawn from $P(X \mid T(X))$,
which does not depend on $\theta$ at all.

<figure>
<svg viewBox="0 0 380 200" role="img" aria-label="Two-stage picture of how a sufficient statistic captures all the information about theta">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="30" y="115" font-size="13" fill="currentColor">θ</text>
  <text x="155" y="65" font-size="13" fill="currentColor">T(X)</text>
  <text x="305" y="65" font-size="13" fill="currentColor">X</text>
  <text x="265" y="168" font-size="13" fill="currentColor">surrogate X̃</text>
  <line x1="42" y1="108" x2="148" y2="70" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="190" y1="60" x2="298" y2="60" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="180" y1="74" x2="278" y2="152" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
  <text x="188" y="45" font-size="11" fill="currentColor">law of T(X) depends on θ</text>
  <text x="195" y="92" font-size="11" fill="currentColor">P(X | T), free of θ</text>
  <text x="183" y="122" font-size="11" fill="currentColor">just as good as X</text>
</svg>
<figcaption>Once T(X) is drawn, generating the rest of X — or a fresh surrogate from the same
conditional law — adds no further information about θ.</figcaption>
</figure>

This gives the **sufficiency principle**: if $T(X)$ is sufficient for $\mathcal{P}$, any
statistical procedure should depend on the data only through $T(X)$. In fact, since the second
stage doesn't involve $\theta$, you could throw away $X$ entirely and generate a fresh
$\tilde{X} \sim P(X \mid T(X))$ — this $\tilde X$ has exactly the same marginal distribution
$P_\theta$ as the real data, so it is just as good as $X$ for any purpose that depends on $\theta$.

## Two more sufficient statistics for iid samples

**Order statistics.** For $x_1,\dots,x_n \in \mathbb{R}$, the order statistics are
$X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$, the values sorted from smallest to largest. If
$X_1,\dots,X_n \overset{\text{iid}}{\sim} P_\theta$ for any model $\mathcal{P} = \{P_\theta^n\}$ on
$\mathcal{X}\subseteq\mathbb{R}$, then $P_\theta^n$ is invariant under permutations of $X$, so
every reordering of a given data set is exactly as likely as any other — meaning the order
statistics $S(X) = (X_{(i)})_{i=1}^n$ are sufficient. Passing from $X$ to $S(X)$ forgets only the
original order in which the observations arrived.

**Empirical distribution.** Order statistics rely on a total ordering of $\mathcal{X}$; for a
general sample space, the analogous object is the **empirical distribution**. Writing
$\delta_x(A) = \mathbf{1}\{x \in A\}$ for the Dirac measure at $x$, define

$$\hat P_n(\cdot) = \frac{1}{n}\sum_{i=1}^n \delta_{X_i}(\cdot),$$

a random measure on $\mathcal{X}$ recording which values were observed and how many times. For iid
sampling from any model on any sample space $\mathcal{X}$, $\hat P_n$ is sufficient.

## Minimal sufficiency

A model typically has many sufficient statistics, of very different sizes. For
$X_1,\dots,X_n \overset{\text{iid}}{\sim} N(\theta,1)$, all of the following are sufficient:

$$X = (X_1,\dots,X_n), \qquad S(X) = (X_{(1)},\dots,X_{(n)}), \qquad \textstyle\sum_i X_i, \qquad \bar X = \tfrac1n\sum_i X_i.$$

Some of these can be recovered from others: $X$ determines $S(X)$ (and no less), $S(X)$ determines
$\sum X_i$ (and no less), while $\sum X_i$ and $\bar X$ determine each other exactly.

<figure>
<svg viewBox="0 0 320 230" role="img" aria-label="Hierarchy of sufficient statistics for the normal location family, from the full data down to the sample mean">
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="150" y="25" font-size="13" fill="currentColor">X</text>
  <text x="130" y="110" font-size="13" fill="currentColor">S(X)</text>
  <text x="45" y="200" font-size="13" fill="currentColor">Σ Xᵢ</text>
  <text x="220" y="200" font-size="13" fill="currentColor">X̄</text>
  <line x1="155" y1="35" x2="150" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="135" y1="120" x2="80" y2="180" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <line x1="75" y1="195" x2="205" y2="195" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)" marker-start="url(#arrow2)"/>
  <text x="170" y="65" font-size="11" fill="currentColor">can compress further</text>
  <text x="150" y="150" font-size="11" fill="currentColor">can compress further</text>
  <text x="115" y="215" font-size="11" fill="currentColor">most compressed</text>
</svg>
<figcaption>Each arrow points from a statistic to a coarser one it determines; Σ Xᵢ and X̄
determine each other, and both turn out to be minimal sufficient for the normal location family.</figcaption>
</figure>

The natural question: are $\sum X_i$ and $\bar X$ as compressed as a sufficient statistic can be?

**Proposition.** If $T(X)$ is sufficient and $T(X) = f(S(X))$ for some function $f$, then $S(X)$
is also sufficient.

*Proof.* By the factorization theorem,
$p_\theta(x) = g_\theta(T(x))h(x) = (g_\theta \circ f)\big(S(x)\big)\,h(x)$, which is again a
factorization through $S(x)$. $\blacksquare$

This says compressing further than a sufficient statistic (through some $f$) keeps you sufficient
— sufficiency only gets easier to maintain as you keep less. It motivates:

**Definition.** $T(X)$ is **minimal sufficient** if

1. $T(X)$ is sufficient, and
2. for every other sufficient statistic $S(X)$, there is a function $f$ with $T(X) = f(S(X))$
   almost surely under $\mathcal{P}$.

However many further sufficient statistics you add to the diagram above, all their arrows point
into $\sum X_i$ (equivalently $\bar X$): it sits at the bottom of the hierarchy.

## Recognizing minimal sufficiency: Bahadur's theorem

Checking minimality against *every* sufficient statistic directly from the definition is not
practical. There is a cleaner criterion, built from an equivalence relation on the sample space.

Assume $\mathcal{P}$ has densities $p_\theta$ on sample space $\mathcal{X}$, and define

$$x \equiv_{\mathcal{P}} y \quad \text{if} \quad \frac{p_\theta(x)}{p_\theta(y)} \text{ does not depend on } \theta.$$

**Any sufficient statistic can only merge equivalent points.** If $T(x) = T(y) = t$ for a
sufficient $T$, then

$$\frac{p_\theta(x)}{p_\theta(y)} = \frac{P_\theta(X=x,\,T(X)=t)}{P_\theta(X=y,\,T(X)=t)} = \frac{P(X=x\mid T(X)=t)}{P(X=y\mid T(X)=t)},$$

and the right-hand side does not depend on $\theta$ because $T$ is sufficient. So
$T(x)=T(y) \implies x \equiv_{\mathcal{P}} y$ for any sufficient $T$ — sufficiency can never
separate two values that are $\equiv_{\mathcal{P}}$-equivalent.

**Theorem (Bahadur).** If $T(X)$ satisfies the converse as well —

$$x \equiv_{\mathcal{P}} y \iff T(x) = T(y),$$

— then $T(X)$ is minimal sufficient. In words: a minimal sufficient statistic collapses the sample
space into exactly the $\equiv_{\mathcal{P}}$ equivalence classes, no more and no less.

*Proof sketch.* First, $T(X)$ is sufficient: for $x$ with $T(x)=t$,

$$P_\theta(X=x\mid T(X)=t) = \frac{p_\theta(x)}{\sum_{z:T(z)=t}p_\theta(z)} = \frac{1}{\sum_{z:T(z)=t} p_\theta(z)/p_\theta(x)},$$

and this does not depend on $\theta$, because every $z$ with $T(z)=t=T(x)$ satisfies
$z \equiv_{\mathcal{P}} x$, so each ratio $p_\theta(z)/p_\theta(x)$ is free of $\theta$.

Now let $S(X)$ be any other sufficient statistic. If $S(x)=S(y)=s$, then (by the merging fact
above) $x \equiv_{\mathcal{P}} y$, so $T(x)=T(y)$; define $f(s)$ to be this common value. Any other
$z$ with $S(z)=s$ has $z \equiv_{\mathcal{P}} x$ (again because $S$ is sufficient), hence
$T(z) = T(x) = f(s) = f(S(z))$. So $T(X) = f(S(X))$ for every sufficient $S$, which is exactly
minimality. $\blacksquare$

### The likelihood function

For $\mathcal{P} = \{P_\theta\}$ with densities $p_\theta(x)$, the **likelihood function** is

$$\text{Lik}(\theta; X) = p_\theta(X),$$

viewed as a function of $\theta$ for the observed (random) $X$ — the data pick out which function
of $\theta$ you are looking at. The **log-likelihood** is $\ell(\theta;X) = \log\text{Lik}(\theta;X)$.

Since $\ell(\theta;x) - \ell(\theta;y) = \log\big(p_\theta(x)/p_\theta(y)\big)$, the equivalence
$x \equiv_{\mathcal{P}} y$ says exactly that the **log-likelihood difference between $x$ and $y$
does not depend on $\theta$** — the two likelihood functions differ only by an additive constant.
Bahadur's theorem can be restated: a minimal sufficient statistic is exactly one whose value tells
you the shape of the log-likelihood function up to an additive constant, and nothing more.

### Example: the Laplace location family

Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} p_\theta^{(1)}(x) = \tfrac12 e^{-|x-\theta|}$. Then

$$\ell(\theta;x) = -\sum_{i=1}^n |x_i - \theta| - n\log 2.$$

As a function of $\theta$, this is piecewise linear with kinks exactly at the order statistics
$x_{(i)}$. On the interval $[x_{(k)}, x_{(k+1)}]$ the slope is $n - 2k$: each of the $k$
observations below $\theta$ contributes slope $-1$ (from $-|x_i - \theta|$), each of the $n-k$
above contributes $+1$.

A piecewise-linear function is determined, up to an additive constant, entirely by the slopes on
each piece and where the kinks are — and here the slopes on $[x_{(k)},x_{(k+1)}]$ depend only on
$k$, not on the values themselves. So

$$\ell(\theta;x) = \ell(\theta;y) + \text{const} \iff x \text{ and } y \text{ have the same order statistics},$$

i.e., $x \equiv_{\mathcal{P}} y$ iff $x$ and $y$ have the same order statistics. By Bahadur's
theorem, the order statistics are minimal sufficient for the Laplace location family.

## Sources

- Berkeley STAT210A, lecture 4 ("Sufficiency"), handwritten notes. Three parallel course offerings
  cover the same lecture — fall-2024, fall-2025, fall-2026, each converted from
  `handwritten/lecture04-sufficiency.pdf` (a PDF with no text layer, reconstructed by a model;
  every equation is flagged unverified in the source conversions).
  - The coin-flipping motivating example, the definitions of statistic and sufficiency, the direct
    check of sufficiency for $X_{++}$, the factorization theorem (statement and proof), and the
    normal/Poisson/uniform examples are common to all three years'
    `01-sufficiency.md`/`02-factorization-theorem.md` (and `03-examples.md` for fall-2025/2026).
  - The fall-2025 and fall-2026 `03-examples.md` files repeat the same three examples and then
    break off partway into "Interpretations of Sufficiency."
  - The fall-2024 notes carry the lecture further and are the sole basis for everything past the
    factorization-theorem examples: the two-stage generative picture and sufficiency principle,
    order statistics, the empirical distribution, and the minimal-sufficiency compression
    hierarchy for the normal location family (all in fall-2024's `02-factorization-theorem.md`),
    plus the equivalence-relation criterion, Bahadur's theorem, the likelihood function, and the
    Laplace-family example (fall-2024's `03-recognizing-minimal-sufficiency.md`).
  - The lecture notes flag, but do not develop, a connection between the normal and Poisson
    sufficient-statistic examples "for next lecture" — that connection (exponential families) is
    not part of this chapter.
- No slides, transcript, or exercises were supplied for this lecture.

---

[← 30. Sufficient Statistics and Factorization](30-sufficient-statistics-and-factorization.md) · [Contents](index.md) · [32. Exponential Families →](32-exponential-families.md)
