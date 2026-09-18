---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture17-nuisanceparams.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture17-nuisanceparams.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-nuisanceparams.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture17-nuisanceparams.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Testing with nuisance parameters
2) Conditional tests
3) Multi-parameter exponential families

---

## Nuisance Parameters

**Common setup**: Extra unknown parameters which are not of direct interest

$\mathcal{P} = \{ P_{\theta, \lambda} : (\theta, \lambda) \in \Omega \}$, $H_0: \theta \in \Theta_0$ vs $H_1: \theta \in \Theta_1$

* $\theta$: parameter of interest
* $\lambda$: nuisance parameter

**Issue**: $\lambda$ unknown but might affect type I error or power of a given test

**Ex** $X_1, \dots, X_n \overset{\text{iid}}{\sim} N(\mu, \sigma^2) \qquad Y_1, \dots, Y_m \overset{\text{iid}}{\sim} N(\nu, \sigma^2)$

$\mu, \nu, \sigma^2$ unknown

$H_0: \mu = \nu \quad \text{vs} \quad H_1: \mu \neq \nu$

$\theta = \mu - \nu \qquad \lambda = (\mu + \nu, \sigma^2) \quad \text{or} \quad (\mu, \sigma^2)$

$H_0: \theta = 0 \quad \text{vs} \quad H_1: \theta \neq 0$

**Ex** $X \sim \text{Pois}(\mu) \qquad Y \sim \text{Pois}(\nu) \qquad X \perp\!\!\!\perp Y$

$H_0: \mu \leq \nu \quad \text{vs} \quad H_1: \mu > \nu$

$\theta = \frac{\mu}{\mu + \nu} \qquad \lambda = \mu + \nu$

$H_0: \theta \leq \frac{1}{2} \qquad H_1: \theta > \frac{1}{2}$

---

## Conditional testing

**Ex** Binomial with random sample size

1) sample $N \sim \text{Pois}(10)$ (e.g., number of survey respondents)
2) sample $X \mid N = n \sim \text{Binomial}(n, \theta)$

Observe $N, X$, test $H_0: \theta \leq \frac{1}{2} \quad \text{vs} \quad H_1: \theta > \frac{1}{2}$

**Should we:**

1) Use marginal dist: $X \sim \text{Pois}(10 \cdot \theta)$

$\text{MLR} \Rightarrow$ Reject if $X > c_\alpha^{(1)}$, upper-$\alpha$ quantile of $\text{Pois}(5)$

$\mathbb{E}_\theta \phi_1(X) \leq \alpha$, for $\theta \leq \frac{1}{2}$

2) Use conditional dist: $X \mid N = n \sim \text{Binom}(n, 1/2)$

$\text{MLR} \Rightarrow$ Reject if $X > c_\alpha^{(2)}(n)$, upper-$\alpha$ quant. of $\text{Binom}(n, 1/2)$

$p(x) = \mathbb{P}_{\theta = 1/2}(X \geq x \mid N = n)$

$\mathbb{E}_\theta [\phi_2(X \mid N) \mid N] \overset{\text{a.s.}}{\leq} \alpha \implies \mathbb{E}_\theta \phi_2(X \mid N) \leq \alpha, \quad \theta \leq \frac{1}{2}$

Neither test is UMP ($\frac{p_{\theta_1}(x, n)}{p_{\theta_0}}$ depends on $n, x$)

(But $\phi_2$ is UMP in conditional problem)

---

## Conditionality Principle

Recall **conditionality principle**:

$N$ is ancillary, so we should condition on it.

**Basic logic**: why should we care $N$ is not fixed?

Condition on $N \iff$ treat as **fixed**

**Conditional model**: Candidate cond. dist.s induced by $\mathcal{P}$:

$$\mathcal{Q}_n = \{ q_\theta(x \mid n) : \theta \in \Theta \}$$

$$X \mid N = n \sim \text{Binom}(n, \theta)$$

$\text{MLR in } X \Rightarrow \phi_2(X \mid N)$ is **optimal conditional test**

**Prop**: If $\phi(X)$ is level $\alpha$ (and unbiased) given $U(X)$ then $\phi(X)$ is level $\alpha$ (and unbiased) marginally

**Proof** $\mathbb{E}_\theta \phi(X) = \mathbb{E}_\theta [\mathbb{E}_\theta [\phi(X) \mid U(X)]]$ $\boxtimes$

---

## Conditioning and nuisance param.s

**Ex** (Random sample size, unknown dist.)

$N \sim P^N \qquad P^N \text{ unknown}$

$X \mid N = n \sim \text{Binom}\left(n, \frac{1}{2}\right)$

Infinite-dimensional nuisance parameter $P^N$

**But**: Can still use conditional test!

$$\mathbb{E}_{\theta, P^N} [\phi_2(X)] = \mathbb{E}_{\theta, P^N} \left[ \mathbb{E}_\theta [\phi_2(X) \mid N] \right] \leq \alpha$$

$N$ is **sufficient stat for nuisance param.** $P^N$ (i.e., $N$ sufficient for model with $\theta$ known)

$\iff$ Conditioning on $N$ removes $P^N$ from problem

**In general**: If $U(X)$ **suff for $\lambda$** (suff. when $\theta$ known) then $\theta$ is the only parameter of

$$\mathcal{Q}_u = \{ Q_\theta(X \mid U(X) = u) : \theta \in \Theta \}$$

---

## Ex (Comparing Poissons)

$$X \sim \text{Pois}(\mu) \qquad Y \sim \text{Pois}(\nu), \qquad X \perp\!\!\!\perp Y$$

Test $H_0: \mu \leq \nu \quad$ vs $\quad H_1: \mu > \nu$

Let $N = X + Y \sim \text{Pois}(\mu + \nu)$

$$X \mid N = n \sim \text{Binom}(n, \theta) \qquad \theta = \frac{\mu}{\mu + \nu} \qquad (Y = N - X)$$

$$H_0: \mu \leq \nu \iff \theta \leq \frac{1}{2} \qquad H_1: \mu > \nu \iff \theta > \frac{1}{2}$$

---

---

[Up: contents](index.md) · [Multiparameter Exp. Families →](02-multiparameter-exp-families.md)
