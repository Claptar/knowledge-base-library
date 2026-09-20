---
title: "28. Statistical models and decisions"
course: "Berkeley Stat 210A Fall 2024"
chapter: 28
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 28. Statistical models and decisions

## What this covers

This chapter sets up the vocabulary of statistical decision theory: what a *statistical model* is,
what it means to *estimate* a quantity from data, and how to compare candidate estimators when no
single one is best in every situation. It assumes familiarity with the binomial and Bernoulli
distributions and with expectation and variance, and works throughout with one running example: a
large real-world coin-flipping experiment. Nothing here settles "which estimator should I use" —
it develops the several ways (dominance, Bayes risk, minimax risk, restricting to unbiased
estimators) that the rest of the course uses to make that choice.

## Probability and statistics as inverse problems

Probability and statistics ask opposite questions about the same relationship between a
distribution $P$ and data $X$.

**Probability** starts from a fully specified distribution $P$ and asks: what can we say about
$X \sim P$? This is a *deductive* question — given the model, deduce properties of the data.

**Statistics** starts from observed data $X$ drawn from an unknown distribution $P$ and asks: what
can we conclude about $P$? This is an *inductive* question — reasoning from a particular
observation back to the mechanism that produced it, which is intrinsically less certain than
deduction.

A **statistical model** is a family $\mathcal{P}$ of candidate distributions for the data $X$. The
working assumption is that $X \sim P$ for *some* $P \in \mathcal{P}$, though we don't know which
one; the data $X$ is then evidence — hopefully — about which member of $\mathcal{P}$ generated it.

## Building a model: coin flipping

Recall a real experiment: 48 people tossed coins a total of $n = 350{,}757$ times, and
$X = 178{,}079$ of those flips landed with the same side facing up as it started. The choice of
model for this data is not forced by the data itself — it is a modeling decision, and different
assumptions about what varies across flips and flippers give genuinely different models.

**Model 1.** All flips are independent with the same probability $\theta \in (0,1)$ of landing
same-side-up. Then
$$X \sim P_\theta = \mathrm{Binom}(n,\theta), \qquad p_\theta(x) = \binom{n}{x}\theta^x(1-\theta)^{n-x}, \quad x = 0,1,\dots,n,$$
so $\mathcal{P} = \{P_\theta : \theta \in (0,1)\}$. Here $\theta$ indexes the family, $n$ is known,
and $\theta$ is the single unknown.

**Model 2.** Flippers have different biases. With $X_i$ the number of same-side flips by flipper
$i$ out of $n_i$ total flips,
$$X_i \overset{\text{ind.}}{\sim} \mathrm{Binom}(n_i,\theta_i), \qquad i = 1,\dots,48,$$
so the parameter is now a vector $(\theta_1,\dots,\theta_{48}) \in (0,1)^{48}$.

**Model 3.** A flipper's own bias can also change over the course of their flips, and — as a
further assumption — only decreases. Writing $X_{i,t}$ for flipper $i$'s $t$-th flip,
$$X_{i,t} \overset{\text{ind.}}{\sim} \mathrm{Bernoulli}(\theta_{i,t}), \qquad i=1,\dots,48,\ t=1,\dots,n_i,$$
subject to $\theta_{i,1} \ge \theta_{i,2} \ge \cdots \ge \theta_{i,n_i}$: now there are as many
parameters as flips recorded.

An open question raised at this point, and left unanswered in the notes: why does the sample space
itself keep changing shape as we move from Model 1 through Model 3?

## Parametric and nonparametric models

A model is **parametric** if its distributions are indexed by a parameter $\theta$ ranging over a
set $\Theta$,
$$\mathcal{P} = \{P_\theta : \theta \in \Theta\},$$
typically with $\Theta \subseteq \mathbb{R}^d$; $d$ is called the model's **dimension**. Once a
model is written this way, $P_\theta(\cdot)$ and $\mathbb{E}_\theta(\cdot)$ denote probabilities and
expectations computed under the specific distribution $P_\theta$.

A model is **nonparametric** if there is no natural way to index $\mathcal{P}$ by such a parameter.
It still usually carries assumptions — independence, or a shape constraint such as "$P$ has a
decreasing density on $\mathbb{R}_+$" — just not ones that reduce the family to a handful of
numbers. The standard example: $X_1,\dots,X_n \overset{\text{iid}}{\sim} P$ for $P$ an *arbitrary*
distribution on $\mathbb{R}$, giving
$$\mathcal{P} = \{P^n : P \text{ a distribution on } \mathbb{R}\}, \qquad X = (X_1,\dots,X_n) \sim P^n.$$

The boundary between the two is genuinely blurry — which of the three coin-flipping models above is
parametric and which is nonparametric is not a clean question, since Model 3's parameter count
grows with the amount of data. And formally the distinction can be erased entirely: any model can
be written in "parametric notation" $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ by simply
taking $\theta = P$ and $\Theta = \mathcal{P}$ — the parameter is then just a name for the
distribution itself, so the notation carries no real content until $\Theta$ is genuinely
low-dimensional.

## Three answers to "what is $\theta$?"

Take Model 1: $X \sim \mathrm{Binom}(n,\theta)$, $\theta$ unknown. The question "what is $\theta$?"
has (at least) three answers.

The **skeptic's answer**: it could be anything. Every value $x \in \{0,\dots,n\}$ is possible under
every $\theta \in (0,1)$, so no single observation rules any $\theta$ out.

The **Bayesian answer**: treat $\theta$ itself as random, with a known prior distribution, and
compute the conditional (posterior) distribution of $\theta$ given the data $X$.

The **frequentist answer**: don't try to pin down this particular $\theta$ directly. Instead find a
method $\delta(X)$ — e.g. $\delta_0(X) = X/n$ — for turning data into a guess, and show that the
method behaves well *across* possible values of $\theta$. This is a statement about the procedure's
long-run behavior ("inductive behavior"), and by itself it says nothing about how well this
particular estimate performed for this particular $\theta$.

Formalizing the frequentist route needs some vocabulary. Given a model
$\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ (parametric or not) and an **estimand** $g(\theta)$
— the quantity we actually want to know, written $g(P)$ in the nonparametric case — an
**estimator** is a function $\delta(\cdot)$ that turns observed data $X$ into an **estimate**
$\delta(X)$. The rest of this chapter is about how to *evaluate* and *compare* estimators.

## Loss and risk

A **loss function** $L(\theta,d)$ measures the disutility of reporting $d$ as a guess for
$g(\theta)$ when the truth is $\theta$. It is typically non-negative, with $L(\theta,d)=0$ exactly
when $d = g(\theta)$; a single loss value describes a single realization, not an average behavior.

The most common choice is **squared error loss**: $L(\theta,d) = (d-g(\theta))^2$.

The **risk function** of an estimator is its expected loss:
$$R(\theta;\delta(\cdot)) = \mathbb{E}_\theta\big[L(\theta,\delta(X))\big].$$
The subscript on $\mathbb{E}_\theta$ is doing a specific job: it says *which* value of $\theta$ is
in effect while averaging over $X$'s randomness — it is not instructing us to also average over
$\theta$.

Risk under squared error loss has its own name, the **mean squared error**:
$$\mathrm{MSE}(\theta;\delta(\cdot)) = \mathbb{E}_\theta\big[(\delta(X)-g(\theta))^2\big].$$

## The binomial example, worked

Back in Model 1, take the estimand $g(\theta) = \theta$ and the natural estimator
$\delta_0(X) = X/n$. Since $\mathbb{E}_\theta[X/n] = \theta$, $\delta_0$ is **unbiased**, and its
MSE reduces to its variance:
$$\mathrm{MSE}(\theta;\delta_0) = \mathbb{E}_\theta\!\left[\left(\frac{X}{n}-\theta\right)^2\right] = \mathrm{Var}_\theta\!\left(\frac{X}{n}\right) = \frac{\theta(1-\theta)}{n}.$$

$\delta_0$ is not the only reasonable estimator. Three others, each built by adding some number of
fictitious "pseudo-flips" to the count before dividing:
$$\delta_1(X) = \frac{X+1}{n+2}, \qquad \delta_2(X) = \frac{X+2}{n+4}, \qquad \delta_3(X) = \frac{X+1}{n}.$$

<figure>
<svg viewBox="0 0 480 340" role="img" aria-label="Mean squared error against theta for four candidate estimators of a binomial success probability with n=16">
  <line x1="60" y1="260" x2="440" y2="260" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="260" x2="60" y2="40" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="260" x2="60" y2="265" stroke="currentColor" stroke-width="1"/>
  <line x1="250" y1="260" x2="250" y2="265" stroke="currentColor" stroke-width="1"/>
  <line x1="440" y1="260" x2="440" y2="265" stroke="currentColor" stroke-width="1"/>
  <text x="60" y="278" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="250" y="278" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>
  <text x="440" y="278" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="250" y="296" text-anchor="middle" font-size="12" fill="currentColor">θ</text>
  <line x1="55" y1="260" x2="60" y2="260" stroke="currentColor" stroke-width="1"/>
  <line x1="55" y1="150" x2="60" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="55" y1="40" x2="60" y2="40" stroke="currentColor" stroke-width="1"/>
  <text x="50" y="264" text-anchor="end" font-size="11" fill="currentColor">0</text>
  <text x="50" y="154" text-anchor="end" font-size="11" fill="currentColor">0.01</text>
  <text x="50" y="44" text-anchor="end" font-size="11" fill="currentColor">0.02</text>
  <text x="20" y="150" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 20 150)">MSE(θ)</text>
  <polyline points="60,260 98,198.1 136,150 174,115.6 212,95 250,88.1 288,95 326,115.6 364,150 402,198.1 440,260" fill="none" stroke="currentColor" stroke-width="2"/>
  <polyline points="60,226.1 98,189.4 136,160.9 174,140.5 212,128.3 250,124.2 288,128.3 326,140.5 364,160.9 402,189.4 440,226.1" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="60" y1="150" x2="440" y2="150" stroke="currentColor" stroke-width="1.5" stroke-dasharray="1,4" stroke-linecap="round"/>
  <polyline points="60,217.0 98,155.2 136,107.0 174,72.7 212,52.0 250,45.2 288,52.0 326,72.7 364,107.0 402,155.2 440,217.0" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="8,3,2,3"/>
  <line x1="60" y1="312" x2="90" y2="312" stroke="currentColor" stroke-width="2"/>
  <text x="95" y="316" font-size="12" fill="currentColor">δ₀</text>
  <line x1="150" y1="312" x2="180" y2="312" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="185" y="316" font-size="12" fill="currentColor">δ₁</text>
  <line x1="240" y1="312" x2="270" y2="312" stroke="currentColor" stroke-width="1.5" stroke-dasharray="1,4" stroke-linecap="round"/>
  <text x="275" y="316" font-size="12" fill="currentColor">δ₂</text>
  <line x1="330" y1="312" x2="360" y2="312" stroke="currentColor" stroke-width="1.5" stroke-dasharray="8,3,2,3"/>
  <text x="365" y="316" font-size="12" fill="currentColor">δ₃</text>
</svg>
<figcaption>MSE against θ for four estimators of a Binomial(n=16, θ) success probability:
δ₀=X/n (solid), δ₁=(X+1)/(n+2) (dashed), δ₂=(X+2)/(n+4) (dotted, flat), δ₃=(X+1)/n (dash-dot).
δ₃'s curve lies strictly above δ₀'s everywhere, so δ₀ dominates it; δ₀, δ₁ and δ₂ are not
comparable this way, since their curves cross, but δ₂'s flat risk gives it the smallest
worst-case value, which is what makes it minimax here.</figcaption>
</figure>

For $n=16$, the four MSE curves cross each other: near $\theta = 1/2$, $\delta_2$ has the largest
risk of the four, but near $\theta=0$ or $\theta=1$ it has the smallest. $\delta_3$, though, differs
in kind from the other three: its curve lies *strictly above* $\delta_0$'s at every $\theta$. Both
are parabolas of the same shape — $\delta_3$ has the same variance as $\delta_0$, since it is also
$X/n$ shifted by a constant, $X/n + 1/n$ — but $\delta_3$'s fixed bias of $1/n$ adds a constant
$1/n^2$ to its MSE everywhere, so $\mathrm{MSE}(\theta;\delta_3) = \mathrm{MSE}(\theta;\delta_0) +
1/n^2$ for every $\theta$. That relationship — one risk curve lying below another everywhere, and
strictly below somewhere — is worth naming.

## Comparing estimators: dominance and admissibility

We would like to choose $\delta$ to minimize $R(\theta;\delta)$, but in general this is not
possible: lowering the risk at one $\theta$ trades off against the risk at another. What is always
meaningful is a pairwise comparison. An estimator $\delta$ is **inadmissible** if there exists
$\delta^*$ with

a) $R(\theta;\delta^*) \le R(\theta;\delta)$ for all $\theta$,
b) $R(\theta;\delta^*) < R(\theta;\delta)$ for some $\theta$,

in which case $\delta^*$ is said to **strictly dominate** $\delta$. In the binomial example,
$\delta_3$ is inadmissible because $\delta_0$ dominates it.

This leaves the harder question open: is there any **uniformly best** estimator — one that beats
every other estimator at *every* $\theta$? For the binomial example, no: $\delta_0$, $\delta_1$ and
$\delta_2$ each have risk curves that cross one another, so none of them dominates the others.

## Resolving the ambiguity

Two strategies turn an entire risk *curve* into a single number that can be minimized, and a third
instead restricts which estimators are allowed to compete.

**1. Summarize the risk function by a scalar.**

*(a) Average-case risk.* Fix a measure $\pi$ on $\Theta$, called a **prior**, and minimize
$$\int_\Theta R(\theta;\delta)\,d\pi(\theta),$$
which, when $\pi$ is a probability measure, is the same as
$\mathbb{E}_{\theta\sim\pi}[R(\theta;\delta)]$. The minimizer is the **Bayes estimator** for that
prior. In the binomial example, $\delta_1$ is Bayes for $\pi = \lambda$, Lebesgue (uniform) measure
on $[0,1]$, and $\delta_2$ is Bayes for $\pi = \mathrm{Beta}(2,2)$ — consistent with the
"pseudo-flip" picture: a uniform prior behaves like one fictitious success and one fictitious
failure already folded into the count, and a $\mathrm{Beta}(2,2)$ prior like two of each.

*(b) Worst-case risk.* Minimize
$$\sup_\theta R(\theta;\delta),$$
whose minimizer is the **minimax estimator**; minimax and Bayes turn out to be closely related. In
the binomial example, $\delta_2$ is minimax for $n=16$: its risk curve is flat, so its worst case is
its everywhere-value, $0.01$ — lower than the peak risk of $\delta_0$ or $\delta_1$, even though
both of those beat $\delta_2$ over much of the range.

**2. Restrict the class of competing estimators.** Rather than summarizing risk, only allow
estimators satisfying a side condition, most commonly **unbiasedness**:
$$\mathbb{E}_\theta[\delta(X)] = g(\theta) \quad \text{for all } \theta.$$
Once attention is restricted to unbiased estimators, a uniformly best one can exist even when none
exists among all estimators. In the binomial example, $\delta_0$ is the best unbiased estimator.

## Sources

- Handwritten lecture notes for *berkeley-stat210a*, "Statistical models and decisions" (lecture
  3), reconstructed by a model from the source PDF: `handwritten/lecture03-estimation.md` in each
  of the fall-2024, fall-2025 and fall-2026 course years. The three are the same lecture taught in
  different years and are essentially identical in content; this chapter follows that common
  version. A fourth copy, `units/handwritten/lecture03-estimation.md` in fall-2025, records the
  same lecture but the conversion breaks off mid-sentence partway through the minimax discussion
  ("b)" with nothing after it) and was not used beyond confirming it agrees with the other three up
  to that point.
- The MSE-against-$\theta$ figure reproduces the plot appearing on page 7 of the source PDF in all
  four notes files; the curve values shown were recomputed directly from the stated estimator
  formulas at $n=16$ rather than read off the source image.
- All four source files carry the conversion's own caveat: they were read from a PDF with no
  extractable text layer by a model, and "the prose is a paraphrase in places and every equation is
  unverified" — treat them as a pointer into the original lecture, not as a citable source in their
  own right.
- Two questions posed in the lecture are left open in the notes and are left open here rather than
  answered: why the sample space changes shape across Models 1–3, and whether Model 3 counts as
  parametric or nonparametric.

---

[← 27. Probability as a Measure](27-probability-as-a-measure.md) · [Contents](index.md) · [29. Canonical Form →](29-canonical-form.md)
