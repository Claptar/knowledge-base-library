---
title: Lecture 2 (8/29/2023)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture02-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture02-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture02-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture02-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 2 (8/29/2023)

### Outline

1) Statistical models

2) Estimation

3) Decision theory

---

## Statistical Models

### Probability vs statistics

```
Distribution P  ---- Probability --->  Data X
                <--- Statistics ----
```

**Probability:** Distribution $P$ fully specified
What can we say about $X \sim P$?
**Deductive**

**Statistics:** Observe data $X$ from unknown dist. $P$
What can we conclude about $P$?
**Inductive**

**Statistical model** Family $\mathcal{P}$ of candidate probability distributions for data $X$ ("the model")

Assume $X \sim P$ for **some** $P \in \mathcal{P}$
$X$ yields evidence about which $P$ (hopefully)

---

## Parametric vs. Nonparametric

### Parametric model
dist.s indexed by parameter $\theta \in \Theta$

$$\mathcal{P} = \{P_\theta : \theta \in \Theta\}$$

Typically $\Theta \subseteq \mathbb{R}^d$, $d$ called **model dimension**

**Example** $X \sim \text{Binom}(n, \theta)$ for $\theta \in [0, 1]$
$n$ "known", $\theta$ "unknown" (by analyst)
$\mathcal{P} = \{\text{Binom}(n, \theta) : \theta \in [0, 1]\}$

### Nonparametric model
no natural way to index $\mathcal{P}$

Still usually makes assumptions, e.g.
- independence
- shape constraints (e.g. unimodal density)

**Example** $X_1, \dots, X_n \overset{\text{iid}}{\sim} P$
$P$ any distr. on $\mathbb{R}$
$\mathcal{P} = \{P^n : P \text{ is a distr. on } \mathbb{R}\}$ (for $X = (X_1, \dots, X_n)$)

We can use "parametric notation" $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ wlog
(could take $\theta = P$, $\Theta = \mathcal{P}$)

---

## Bayesian vs. "Frequentist" Inference

Assume $X \sim P_\theta \qquad \theta$ unknown

### Bayesian assumption:
$\theta$ random with known dist.

$$\text{Inference} = \text{calculating dist.}(\theta \mid X) \quad (\text{posterior})$$

Considered a strong assumption
(will consider interp., pros & cons later)

**Alternate perspective:** treat $\theta$ as fixed, unknown
Methods designed without knowledge of $\theta$
Study **frequency properties** as $\theta$ varies

---

## Estimation

### Setup
Model $\mathcal{P} = \{P_\theta : \theta \in \Theta\} \qquad (\text{wlog})$

**Estimand** $g(\theta) \qquad (\text{something we want to know})$

Observe $X$, calculate **estimate** $\delta(X)$

$\delta(\cdot)$ called **estimator**.

We want to **evaluate & compare** estimators

### Example
Flip a biased coin $n$ times
$\theta \in [0, 1]$ probability of heads

$X = \text{# heads} \sim \text{Binom}(n, \theta)$

**Goal:** estimate $\theta$

Natural estimator is $\delta_0(X) = \frac{X}{n}$
How good is it?

---

## Loss and Risk

**Loss function** $L(\theta, d)$

Disutility of guessing $g(\theta) = d$

Typically non-negative, with $L(\theta, d) = 0$ iff $d = g(\theta)$
[Different for every realization]

**Squared error loss:** $L(\theta, d) = (d - g(\theta))^2$

**Risk function:** expected loss of an estimator

$$R(\theta; \delta(\cdot)) = \mathbb{E}_\theta [L(\theta, \delta(X))]$$

($\theta$ tells us which parameter value is in effect, **NOT** "what randomness to integrate over")

**Risk for sq. error loss** is **mean squared error** (MSE)

$$\text{MSE}(\theta; \delta(\cdot)) = \mathbb{E}_\theta \left[(\delta(X) - g(\theta))^2\right]$$

---

## Binomial example

What is $\text{MSE}(\theta; \delta_0)$? $\qquad \left(\delta_0(X) = \frac{X}{n}\right)$

$$\mathbb{E}_\theta \left[\frac{X}{n}\right] = \theta \qquad (\text{unbiased})$$

$$\implies \text{MSE}(\theta; \delta_0) = \mathbb{E}_\theta \left[\left(\frac{X}{n} - \theta\right)^2\right]$$

$$= \text{Var}_\theta \left(\frac{X}{n}\right)$$

$$= \frac{1}{n} \theta (1 - \theta)$$

**Other possibilities** (based on adding "pseudo-flips")

$$\delta_1(X) = \frac{X+1}{n+2} \qquad \delta_2(X) = \frac{X+2}{n+4} \qquad \delta_3(X) = \frac{X+1}{n}$$

**Mean squared error for binomial estimators (n=16)**

[Graph showing $\text{MSE}(\theta)$ vs $\theta$ for $\theta \in [0.0, 1.0]$ and $\text{MSE}(\theta) \in [0.000, 0.020]$ with curves: $\delta_0$ (black, parabolic peaking at 0.5), $\delta_1$ (red, flatter parabolic peaking at 0.5), $\delta_2$ (blue, flat horizontal line at $\approx 0.010$), and $\delta_3$ (green, higher parabolic peaking at 0.5).]

---

## Comparing estimators

We want to choose $\delta$ to minimize $R$
...but this is generally not possible

An estimator $\delta$ is **inadmissible** if $\exists \delta^*$ with

a) $R(\theta; \delta^*) \le R(\theta, \delta) \quad$ for all $\theta$

b) $R(\theta, \delta^*) < R(\theta, \delta) \quad$ for some $\theta$

We say $\delta^*$ **strictly dominates** $\delta$

$\delta_3$ is inadmissible because $\delta_0$ dominates it

Is there any **uniformly** best estimator for the binomial example? (all $\theta$)

---

## Resolving ambiguity

**Main strategies to resolve ambiguity:**

1) **Summarize risk function by a scalar:**

   a) **Average-case risk**

   $$\text{Minimize} \quad \int_\Theta R(\theta; \delta) \, d\pi(\theta)$$

   for some measure $\pi$, called **prior**

   If $\pi$ is probability measure, same as

   $$\mathbb{E}_{\theta \sim \pi} \left[ R(\theta; \delta) \right]$$

   $\rightsquigarrow$ **Bayes estimator**

   **Binomial:** $\delta_1$ is Bayes wrt $\pi = \lambda$ on $[0, 1]$
   $\delta_2$ also Bayes wrt $\pi = \text{Beta}(2, 2)$

   b) **Worst-case risk**

   $$\text{Minimize} \quad \sup_\theta R(\theta; \delta)$$

   $\rightsquigarrow$ **Minimax estimator**

   Closely related to Bayes

   **Binomial:** $\delta_2$ is minimax (for $n=16$)

---

2) **Restrict choices of estimators**

   a) **Restrict to unbiased estimators:**

   $$\mathbb{E}_\theta [\delta(X)] = g(\theta) \quad \text{for all } \theta$$

   **Binomial:** $\delta_0$ is best unbiased estimator

---

[Up: contents](../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 7 of the original](lecture02-F24/figures/p007-2.png)

