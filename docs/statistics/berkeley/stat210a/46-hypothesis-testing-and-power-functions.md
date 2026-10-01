---
title: "46. Hypothesis Testing and Power Functions"
course: "Berkeley Stat 210A"
chapter: 46
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 46. Hypothesis Testing and Power Functions

## What this covers

This chapter sets up the vocabulary of hypothesis testing that the rest of the course builds on:
how a choice between two competing submodels is formalized as a **test function**, how a test's
behavior is fully summarized by its **power function**, and what it means for a test to hold a
given **significance level**. It assumes a parametric model $\mathcal{P} = \{P_\theta : \theta \in
\Theta\}$ and comfort with expectations under $P_\theta$, written $\mathbb{E}_\theta$. The lecture
was heading toward the Neyman-Pearson lemma — stated as the second item on its own outline — but
the available material breaks off just before that argument begins, at the start of a worked normal
example; the lemma itself is not covered here.

## Testing as choosing between submodels

In hypothesis testing, data $X$ is used to infer which of two submodels of a model $\mathcal{P} =
\{P_\theta : \theta \in \Theta\}$ actually generated it. The parameter space is split into two
pieces,

$$
H_0 : \theta \in \Theta_0 \qquad \text{(the null hypothesis)}
$$
$$
H_1 : \theta \in \Theta_1 \qquad \text{(the alternative hypothesis)},
$$

and, whenever $H_1$ is left unspecified, the convention is $\Theta_1 = \Theta \setminus \Theta_0$.

The two hypotheses are not treated symmetrically: $H_0$ is the "default" choice, and a test can
only do one of two things with it —

1. **accept** $H_0$ (fail to reject it — this is not a positive conclusion that $\Theta_0$ holds,
   only that the data gave no reason to leave it), or
2. **reject** $H_0$ (conclude that $\Theta_0$ is false and $\Theta_1$ true).

Two running examples fix the setup:

- $X \sim N(\theta, 1)$, with either the one-sided test $H_0 : \theta \le 0$ versus $H_1 : \theta >
  0$, or the two-sided test $H_0 : \theta = 0$ versus $H_1 : \theta \neq 0$.
- A two-sample problem: $X_1, \dots, X_n \sim P$ and $Y_1, \dots, Y_m \sim Q$, with $H_0 : P = Q$
  versus $H_1 : P \neq Q$.

A conceptual objection was raised and deliberately left open rather than answered: in a continuous
model, one already "knows" in advance that $\theta \neq 0$ exactly, or that $P \neq Q$ exactly — two
continuous distributions are essentially never identical — so why formulate the problem as testing
a sharp null at all? The lecture flagged this as a question to return to later; it is not resolved
in this material.

## The critical function and the rejection region

A test is described formally by its **critical function** (also called the test function)
$\phi(x)$, which reports the (possibly randomized) probability of rejecting $H_0$ having observed
$x$:

$$
\phi(x) = \begin{cases}
0 & \text{accept } H_0 \\
\pi \in (0,1) & \text{reject with probability } \pi \\
1 & \text{reject } H_0.
\end{cases}
$$

Randomized tests — where $\phi(x)$ takes a value strictly between $0$ and $1$ — are almost never
used in practice; the value of allowing them is theoretical, not practical, since it simplifies how
results about optimal tests can be stated.

A **non-randomized** test has $\phi(x) \in \{0,1\}$ for every $x$, so it simply partitions the
sample space $\mathcal{X}$ into two pieces:

$$
R = \{x : \phi(x) = 1\} \quad \text{(the rejection region)}, \qquad
A = \{x : \phi(x) = 0\} \quad \text{(the acceptance region)}.
$$

<figure>
<svg viewBox="0 0 320 140" role="img" aria-label="The sample space split into an acceptance region and a rejection region by a test">
  <rect x="30" y="30" width="260" height="70" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="150" y1="30" x2="150" y2="100" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <rect x="150" y="30" width="140" height="70" fill="currentColor" fill-opacity="0.15"/>
  <text x="90" y="70" text-anchor="middle" font-size="13" fill="currentColor">A: accept $H_0$</text>
  <text x="220" y="70" text-anchor="middle" font-size="13" fill="currentColor">R: reject $H_0$</text>
  <text x="160" y="20" text-anchor="middle" font-size="12" fill="currentColor">boundary set by $\phi$</text>
  <text x="160" y="120" text-anchor="middle" font-size="12" fill="currentColor">$\mathcal{X}$</text>
</svg>
<figcaption>A non-randomized test partitions the sample space $\mathcal{X}$ into an acceptance
region $A$ and a rejection region $R$; the boundary between them is exactly what the choice of
test amounts to.</figcaption>
</figure>

## The power function and the significance level

A test's entire behavior — over every value of $\theta$, not just the ones in $\Theta_0$ — is
summarized by its **power function**:

$$
\beta_\phi(\theta) = \mathbb{E}_\theta[\phi(X)] = \mathbb{P}_\theta[\text{reject } H_0].
$$

Restricted to $\theta \in \Theta_0$, $\beta_\phi(\theta)$ is the probability of a false rejection at
that parameter value; restricted to $\theta \in \Theta_1$, it is the probability of correctly
detecting the alternative.

A test $\phi$ is a **level-$\alpha$ test**, for $\alpha \in [0,1]$, if its worst-case rejection
probability under the null is bounded by $\alpha$:

$$
\sup_{\theta \in \Theta_0} \beta_\phi(\theta) \le \alpha.
$$

The overwhelmingly common choice in practice is $\alpha = 0.05$ — flagged in the lecture as
perhaps "the most influential offhand remark in the history of science."

With this language in place, the goal that organizes the rest of the topic can be stated precisely:

> **Goal.** Maximize $\beta_\phi(\theta)$ for $\theta \in \Theta_1$, subject to the constraint that
> $\phi$ is a level-$\alpha$ test.

That is, among all tests that keep the false-rejection probability under the null at or below
$\alpha$, find the one with the largest possible power against the alternative. The lecture had
begun setting up a worked example with $X \sim N(\theta, 1)$ to illustrate this optimization when
the available notes break off — this is exactly the question the Neyman-Pearson lemma answers, but
that argument is not part of this material.

## Sources

- Handwritten lecture notes, `statistics/berkeley/stat210a`, fall-2024,
  `handwritten/lecture14-F24.pdf` (dated on the page as "Outline 10/10/2023"), covering both
  sections above: hypothesis testing as model choice, the critical/test function, the power
  function and level-$\alpha$ tests. No slides, transcript, or exercises were supplied for this
  lecture.
- The notes are a model reconstruction of a handwritten PDF with no text layer (marked
  "fidelity: reconstructed" in the source file); equations should be treated as unverified against
  the original scan.
- The lecture's own outline lists "Neyman-Pearson Lemma" as its second topic, and the goal
  statement at the end of these notes points directly at it, but the supplied material stops at the
  start of a worked normal example, before the lemma is stated or argued. That content is not
  reproduced here because it is not in the source.

---

[← 45. Minimax Estimation (part 2)](45-minimax-estimation-part-2.md) · [Contents](index.md) · [47. One-Sided Tests in General →](47-one-sided-tests-in-general.md)
