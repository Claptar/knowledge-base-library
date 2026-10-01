---
title: "26. Statistical Models and Decision Theory"
course: "Berkeley Stat 210A"
chapter: 26
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 26. Statistical Models and Decision Theory

## What this covers

This chapter sets up the basic vocabulary of mathematical statistics: what a *statistical model*
is, how an *estimator* turns data into a guess, and how to compare estimators once no single one is
best for every value of the unknown parameter. It works through one running example — estimating
the bias of a coin from $n$ flips — to make each definition concrete, and ends with the three
standard ways of resolving that ambiguity: Bayes estimators, minimax estimators, and unbiased
estimators. It assumes only basic probability: random variables, expectation, variance, and the
binomial distribution.

## Statistical models

### Probability versus statistics

<figure>
<svg viewBox="0 0 340 150" role="img" aria-label="Two opposite arrows: probability reasons from a distribution to data, statistics reasons from data back to the distribution">
  <defs>
    <marker id="pv-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="55" y="80" text-anchor="middle" font-size="13" fill="currentColor">Distribution P</text>
  <text x="285" y="80" text-anchor="middle" font-size="13" fill="currentColor">Data X</text>
  <line x1="105" y1="55" x2="235" y2="55" stroke="currentColor" stroke-width="1.5" marker-end="url(#pv-arrow)"/>
  <text x="170" y="45" text-anchor="middle" font-size="12" fill="currentColor">probability (deductive)</text>
  <line x1="235" y1="105" x2="105" y2="105" stroke="currentColor" stroke-width="1.5" marker-end="url(#pv-arrow)"/>
  <text x="170" y="122" text-anchor="middle" font-size="12" fill="currentColor">statistics (inductive)</text>
</svg>
<figcaption>Probability reasons forward, from a fully specified distribution to what the data should
look like; statistics reasons backward, from observed data to which distribution produced it.</figcaption>
</figure>

Probability starts from a fully specified distribution $P$ and asks a deductive question: given
$X \sim P$, what can we say about $X$? Statistics runs the arrow backwards: we observe data $X$
drawn from some *unknown* distribution $P$, and ask an inductive question — what can we conclude
about $P$?

A **statistical model** is a family $\mathcal{P}$ of candidate distributions for the data $X$ ("the
model"). We assume $X \sim P$ for *some* $P \in \mathcal{P}$, and the data $X$ is supposed to give
us evidence about which member of $\mathcal{P}$ that is.

### Parametric and nonparametric models

In a **parametric model** the distributions in $\mathcal{P}$ are indexed by a parameter
$\theta \in \Theta$:

$$\mathcal{P} = \{P_\theta : \theta \in \Theta\}.$$

Typically $\Theta \subseteq \mathbb{R}^d$, and $d$ is called the model's **dimension**.

*Example.* $X \sim \text{Binom}(n, \theta)$ for $\theta \in [0, 1]$, with $n$ "known" and $\theta$
"unknown" to the analyst: $\mathcal{P} = \{\text{Binom}(n, \theta) : \theta \in [0, 1]\}$.

In a **nonparametric model** there is no natural way to index $\mathcal{P}$ by a finite-dimensional
parameter. Such a model still usually carries assumptions — independence, or a shape constraint
such as unimodality — just not a parametrization.

*Example.* $X_1, \dots, X_n \overset{\text{iid}}{\sim} P$ for $P$ *any* distribution on
$\mathbb{R}$: $\mathcal{P} = \{P^{\otimes n} : P \text{ a distribution on } \mathbb{R}\}$, for
$X = (X_1, \dots, X_n)$.

Even here we can use "parametric" notation $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ without
loss of generality, simply by taking $\theta = P$ and $\Theta = \mathcal{P}$ — the index and the
object it indexes coincide.

## Bayesian and frequentist inference

Fix the setup $X \sim P_\theta$ with $\theta$ unknown, and consider two stances on what "unknown"
means.

The **Bayesian** assumption treats $\theta$ as random, with a *known* distribution (the **prior**).
Inference is then just calculating the conditional distribution of $\theta$ given $X$ — the
**posterior**:

$$\text{inference} = \text{dist.}(\theta \mid X).$$

This is considered a strong assumption — it commits to a distribution for something a frequentist
would treat as simply a fixed unknown quantity — and its interpretation, along with the trade-offs
it brings, is left for later in the course.

The **frequentist** alternative treats $\theta$ as fixed and unknown, and designs methods without
assuming any particular value of $\theta$. It studies the **frequency properties** of a method —
things like the risk function defined below — as $\theta$ ranges over $\Theta$.

## Estimation as a decision problem

Fix a model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ (any model can be written this way, per
the remark above). The **estimand** is a quantity $g(\theta)$ that we want to know. We observe $X$
and compute an **estimate** $\delta(X)$; the function $\delta(\cdot)$ itself is called the
**estimator**. The rest of this chapter is about evaluating and comparing estimators.

*Running example.* Flip a biased coin $n$ times; $\theta \in [0, 1]$ is the probability of heads,
and $X = \#\text{heads} \sim \text{Binom}(n, \theta)$. The goal is to estimate $\theta$. The obvious
estimator is $\delta_0(X) = X/n$ — but how good is it, and is anything better?

## Loss and risk

To compare estimators we need to say how bad a wrong guess is. A **loss function** $L(\theta, d)$
is the disutility of guessing $g(\theta) = d$ when the truth is $\theta$; it is typically
non-negative, with $L(\theta, d) = 0$ iff $d = g(\theta)$, and it is different for every realization
of the data. The default choice is **squared error loss**,

$$L(\theta, d) = (d - g(\theta))^2.$$

An estimator's loss is itself random, since it depends on $X$. To get a single number attached to
an estimator at a given $\theta$, take its expectation — the **risk function**:

$$R(\theta; \delta(\cdot)) = \mathbb{E}_\theta\big[L(\theta, \delta(X))\big].$$

Here the subscript $\theta$ on $\mathbb{E}$ says which distribution $X$ is drawn from: $\theta$
tells us *which parameter value is in effect*, not something to be integrated over. The risk under
squared error loss is the familiar **mean squared error**,

$$\text{MSE}(\theta; \delta(\cdot)) = \mathbb{E}_\theta\big[(\delta(X) - g(\theta))^2\big].$$

Expanding the square and using $\mathbb{E}_\theta[\delta(X) - \mathbb{E}_\theta \delta(X)] = 0$
splits the MSE into a variance term and a **bias** term,
$\text{Bias}(\theta; \delta) = \mathbb{E}_\theta[\delta(X)] - g(\theta)$:

$$\text{MSE}(\theta; \delta) = \text{Var}_\theta(\delta(X)) + \text{Bias}(\theta; \delta)^2.$$

This decomposition is what makes the binomial example below tractable.

## Worked example: the binomial

For $\delta_0(X) = X/n$,

$$\mathbb{E}_\theta\left[\frac{X}{n}\right] = \theta,$$

so $\delta_0$ is **unbiased**, and its MSE is pure variance:

$$\text{MSE}(\theta; \delta_0) = \text{Var}_\theta\left(\frac{X}{n}\right) = \frac{\theta(1-\theta)}{n}.$$

Other estimators suggest themselves by adding "pseudo-flips" — imaginary extra trials — before
dividing:

$$\delta_1(X) = \frac{X+1}{n+2}, \qquad \delta_2(X) = \frac{X+2}{n+4}, \qquad \delta_3(X) = \frac{X+1}{n}.$$

All three, together with $\delta_0$, are of the form $\delta_{a,b}(X) = (X+a)/(n+b)$: $b$
pseudo-flips are added in total, $a$ of them pseudo-heads ($\delta_0$ is $\delta_{0,0}$). $\delta_3$
adds a pseudo-head to the numerator without adding any pseudo-flip to the denominator — an
asymmetric adjustment that should already look suspect.

Using $\mathbb{E}_\theta[X] = n\theta$ and $\text{Var}_\theta(X) = n\theta(1-\theta)$, the same
bias–variance decomposition applies to the whole family at once:

$$\text{Bias}(\theta; \delta_{a,b}) = \frac{a - b\theta}{n+b}, \qquad
\text{Var}_\theta(\delta_{a,b}) = \frac{n\theta(1-\theta)}{(n+b)^2},$$

$$\text{MSE}(\theta; \delta_{a,b}) = \frac{n\theta(1-\theta) + (a - b\theta)^2}{(n+b)^2}.$$

Plugging in $n = 16$:

$$\text{MSE}(\theta; \delta_1) = \frac{16\theta(1-\theta) + (1-2\theta)^2}{324}, \qquad
\text{MSE}(\theta; \delta_2) = \frac{16\theta(1-\theta) + (2-4\theta)^2}{400}, \qquad
\text{MSE}(\theta; \delta_3) = \frac{16\theta(1-\theta) + 1}{256}.$$

Two things fall out of this algebra that are not obvious from the formulas alone. First, expanding
the numerator of $\text{MSE}(\theta; \delta_2)$ gives $16\theta(1-\theta) + (2-4\theta)^2 = 4$
identically, so

$$\text{MSE}(\theta; \delta_2) = \frac{4}{400} = \frac{1}{100} \quad \text{for every } \theta:$$

its risk is *exactly* constant, not just small on average. Second,

$$\text{MSE}(\theta; \delta_3) = \frac{\theta(1-\theta)}{16} + \frac{1}{256} = \text{MSE}(\theta; \delta_0) + \frac{1}{256}$$

for every $\theta$: the unmatched pseudo-head costs $\delta_3$ exactly $1/256$ of risk everywhere,
for no benefit anywhere.

<figure>
<svg viewBox="0 0 350 240" role="img" aria-label="Mean squared error against theta for four binomial estimators with n=16: three curves are U-shaped and one is exactly flat">
  <line x1="45" y1="210" x2="300" y2="210" stroke="currentColor" stroke-width="1"/>
  <line x1="45" y1="210" x2="45" y2="20" stroke="currentColor" stroke-width="1"/>
  <text x="45" y="225" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="172.5" y="225" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>
  <text x="300" y="225" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="172.5" y="238" text-anchor="middle" font-size="12" fill="currentColor">theta</text>
  <text x="40" y="213" text-anchor="end" font-size="11" fill="currentColor">0.000</text>
  <text x="40" y="118" text-anchor="end" font-size="11" fill="currentColor">0.010</text>
  <text x="40" y="24" text-anchor="end" font-size="11" fill="currentColor">0.020</text>
  <text x="6" y="14" font-size="11" fill="currentColor">MSE</text>
  <polyline points="45.0,210.0 57.8,181.8 70.5,156.6 83.2,134.3 96.0,115.0 108.8,98.7 121.5,85.3 134.2,74.9 147.0,67.5 159.8,63.0 172.5,61.6 185.2,63.0 198.0,67.5 210.8,74.9 223.5,85.3 236.2,98.7 249.0,115.0 261.8,134.3 274.5,156.6 287.2,181.8 300.0,210.0" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="45.0,180.7 57.8,164.0 70.5,149.0 83.2,135.8 96.0,124.4 108.8,114.7 121.5,106.8 134.2,100.6 147.0,96.2 159.8,93.6 172.5,92.7 185.2,93.6 198.0,96.2 210.8,100.6 223.5,106.8 236.2,114.7 249.0,124.4 261.8,135.8 274.5,149.0 287.2,164.0 300.0,180.7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6 3"/>
  <polyline points="45.0,172.9 57.8,144.7 70.5,119.5 83.2,97.2 96.0,77.9 108.8,61.6 121.5,48.2 134.2,37.8 147.0,30.4 159.8,25.9 172.5,24.5 185.2,25.9 198.0,30.4 210.8,37.8 223.5,48.2 236.2,61.6 249.0,77.9 261.8,97.2 274.5,119.5 287.2,144.7 300.0,172.9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="1.5 3"/>
  <polyline points="45.0,115.0 300.0,115.0" fill="none" stroke="#d9822b" stroke-width="2"/>
  <line x1="310" y1="34" x2="328" y2="34" stroke="currentColor" stroke-width="1.5"/>
  <text x="332" y="38" font-size="12" fill="currentColor">&#948;&#8320;</text>
  <line x1="310" y1="54" x2="328" y2="54" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6 3"/>
  <text x="332" y="58" font-size="12" fill="currentColor">&#948;&#8321;</text>
  <line x1="310" y1="74" x2="328" y2="74" stroke="#d9822b" stroke-width="2"/>
  <text x="332" y="78" font-size="12" fill="#d9822b">&#948;&#8322;</text>
  <line x1="310" y1="94" x2="328" y2="94" stroke="currentColor" stroke-width="1.5" stroke-dasharray="1.5 3"/>
  <text x="332" y="98" font-size="12" fill="currentColor">&#948;&#8323;</text>
</svg>
<figcaption>MSE as a function of $\theta$ for the four estimators, with $n = 16$. $\delta_2$
(highlighted) is the only curve that is exactly flat: its risk equals its own worst case, which is
what makes it the minimax estimator. Every other estimator beats $\delta_2$ for some $\theta$ and
loses to it for others.</figcaption>
</figure>

## Comparing estimators

We would like to choose $\delta$ to minimize $R(\theta; \delta)$ — but this is generally not
possible, because the estimator that minimizes risk at one $\theta$ need not minimize it at
another. The figure already shows this: $\delta_0$ has the smallest risk near $\theta = 0$ and
$\theta = 1$, while $\delta_1$ has smaller risk than $\delta_0$ for $\theta$ near $1/2$. Neither
dominates the other, so there is no single estimator among $\delta_0, \delta_1, \delta_2$ that is
best for *every* $\theta$ — which is exactly the question the lecture poses at this point.

There is, at least, a clear notion of one estimator being worse than another *everywhere*. Call
$\delta$ **inadmissible** if there exists $\delta^*$ with

a) $R(\theta; \delta^*) \le R(\theta; \delta)$ for all $\theta$, and

b) $R(\theta; \delta^*) < R(\theta; \delta)$ for some $\theta$;

in that case $\delta^*$ **strictly dominates** $\delta$. The identity
$\text{MSE}(\theta; \delta_3) = \text{MSE}(\theta; \delta_0) + 1/256$ derived above shows that
$\delta_0$ dominates $\delta_3$ at *every* $\theta$, not merely some — so $\delta_3$ is
inadmissible.

## Resolving the ambiguity

If risk cannot be minimized pointwise, two families of strategy remain: summarize the whole risk
function by a single number and minimize that, or restrict attention to a smaller class of
estimators within which a uniformly best one might exist.

### Summarizing risk by a scalar

**Average-case risk.** Fix a measure $\pi$ on $\Theta$, called the **prior**, and minimize

$$\int_\Theta R(\theta; \delta) \, d\pi(\theta).$$

When $\pi$ is a probability measure this is the same as minimizing
$\mathbb{E}_{\theta \sim \pi}[R(\theta; \delta)]$. A minimizer is a **Bayes estimator** (for that
prior). In the binomial example, $\delta_1$ is Bayes for the uniform prior $\pi = \lambda$ on
$[0, 1]$, and $\delta_2$ is Bayes for the $\text{Beta}(2, 2)$ prior — the calculation that
identifies which estimator is Bayes for a given prior is left for a later lecture.

**Worst-case risk.** Minimize $\sup_\theta R(\theta; \delta)$ instead. A minimizer is a **minimax
estimator**, and the two ideas turn out to be closely related. In the binomial example, $\delta_2$
is minimax for $n = 16$ — consistent with the algebra above: its risk is not just small in the
worst case, it is *constant*, so its worst case is no worse than its typical case. Why a
constant-risk Bayes estimator should be minimax in general is, again, a question for later in the
course.

### Restricting the class: unbiased estimators

Alternatively, restrict attention to estimators satisfying

$$\mathbb{E}_\theta[\delta(X)] = g(\theta) \quad \text{for all } \theta,$$

and ask for the one with smallest risk *within that class*. In the binomial example, $\delta_0$ is
the best unbiased estimator.

## Sources

Everything above comes from a single supplied source: the handwritten lecture notes for Statistics
210A (UC Berkeley), *Lecture 2 (8/29/2023)*, at
`docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture02-F24.md` in the library repository
— a model-reconstructed transcription of a PDF with no text layer, licensed CC BY 4.0. No slides,
transcript, or exercises were supplied for this lecture.

The source note itself flags that "every equation is unverified," so the general-$(a,b)$
bias–variance algebra in the "Worked example" and "Comparing estimators" sections above was
reconstructed here (not present in that form in the note) and checked against the note's stated
formulas, its claims about which estimator is Bayes/minimax/best-unbiased, and its own MSE plot.
The MSE figure reproduces the plot on page 7 of the source PDF ("Mean squared error for binomial
estimators (n=16)"), redrawn here from the exact curve formulas rather than traced from the scanned
image.

Two things the lecture points at but does not itself contain: the interpretation of, and the
trade-offs around, the Bayesian assumption that $\theta$ is random ("will consider interp., pros
& cons later"); and the general relationship between Bayes estimators and minimax estimators,
including why a Bayes estimator with constant risk turns out to be minimax.

---

[← 25. Induction and the Coin-Flip Example](25-induction-and-the-coin-flip-example.md) · [Contents](index.md) · [27. Probability as a Measure →](27-probability-as-a-measure.md)
