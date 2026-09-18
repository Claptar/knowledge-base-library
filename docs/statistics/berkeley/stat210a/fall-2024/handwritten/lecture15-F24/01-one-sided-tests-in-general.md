---
title: One-sided tests in general
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture15-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture15-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture15-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture15-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# One-sided tests in general

### Outline

1) Uniformly most powerful test
2) Two-tailed tests

* one-tailed test
  * stoch incr.
  * score / sign
* two-tailed test
  * UMPU (OJS?)
  * Equal-tail
* many-tailed test?

---

$\mathcal{P} = \{P_\theta : \theta \in \Theta \subseteq \mathbb{R}\}$, $\quad \theta_0 \in \Theta$

$H_0: \theta \le \theta_0 \quad\text{vs}\quad H_1: \theta > \theta_0 \quad\text{called \textbf{one-sided hypothesis}}$

Often, no UMP test exists

**Ex.** Laplace: $\quad X_1, \dots, X_n \overset{\text{iid}}{\sim} \frac{1}{2} e^{-|x-\theta|}$

LRT for $H_0: \theta = \theta_0 \quad\text{vs}\quad H_1: \theta = \theta_1 (> \theta_0)$

$$\log(p_1(x)/p_0(x)) = \sum_{i=1}^n |x_i - \theta_0| - |x_i - \theta_1|$$

$$= \sum T(x_i)$$

$$T(x) = \begin{cases} \theta_0 - \theta_1 & x \le \theta_0 \\ 2x - \theta_0 - \theta_1 & \theta_0 \le x \le \theta_1 \\ \theta_1 - \theta_0 & x \ge \theta_1 \end{cases}$$

Very dependent on specific values of $\theta_0$ and $\theta_1$

Test $H_0: \theta \le 0 \quad\text{vs}\quad H_1: \theta > 0$: No UMP test

Test $H_0: \theta = 0 \quad\text{vs}\quad H_1: \theta = \varepsilon, \quad \varepsilon \downarrow 0$:

$$\sum T(x_i) = -\varepsilon #\{x_i \le 0\} + \varepsilon #\{x_i \ge \varepsilon\} + \sum_{x_i \in [0, \varepsilon]} 2x_i - \varepsilon$$

$$\frac{1}{\varepsilon} \sum T(x_i) \underset{\varepsilon \to 0}{\longrightarrow} #\{x_i > 0\} - #\{x_i \le 0\} = 2 #\{x_i > 0\} - n$$

$$n + \frac{1}{2\varepsilon} \sum T(x_i) \underset{\varepsilon \to 0}{\longrightarrow} #\{x_i > 0\} \overset{\theta=0}{\sim} \text{Binom}(n, \frac{1}{2}) \quad \textbf{Sign test}$$

---

## Stochastically incr.

**Def** A real-valued statistic $T(X)$ is **stochastically increasing** in $\theta$ if
$$P_\theta(T(X) \le t) \quad\text{is non-incr. in } \theta, \; \forall t$$

If $\phi(x)$ is **right-tailed test** based on $T(X)$:
$$\phi(x) = \mathbf{1}\{T(X) > c\} + \gamma \mathbf{1}\{T(X) = c\}$$

and $T(X)$ is stochastically increasing in $\theta$,
$$\mathbb{E}_\theta \phi(X) = (1-\gamma) P_\theta(T > c) + \gamma P_\theta(T \ge c) \nearrow \text{in } \theta$$

**Ex** $X_i \overset{\text{iid}}{\sim} p(x - \theta) \quad (\text{location family})$
$T(X) =$ sample mean, median, sign statistic

**Ex** $X_i \overset{\text{iid}}{\sim} \frac{1}{\theta} p(x/\theta) \quad (\text{scale family})$
$T(X) = \sum X_i^2 \quad\text{or}\quad \text{median}(|X_1|, \dots, |X_n|)$

---

## Two-sided Alternatives

Setup: $\mathcal{P} = \{P_\theta : \theta \in \Theta \subseteq \mathbb{R}\}$, $\quad \theta_0 \in \Theta^\circ$

Test $H_0: \theta = \theta_0 \quad\text{vs.}\quad H_1: \theta \ne \theta_0$

(Can be generalized naturally to $H_0: \theta \in [\theta_1, \theta_2]$)

**Two-tailed test** rejects when $T(X)$ is "extreme"

$$\phi(x) = \begin{cases} 1 & T(X) > c_2 \quad\text{or}\quad T(X) < c_1 \\ 0 & T(X) \in (c_1, c_2) \\ \gamma_i & T(X) = c_i \end{cases}$$

Two ways to reject. How to balance?

For symmetric distributions like $N(\theta, 1)$, natural choice is to equalize "lobes" of rej. region

$$\phi_2(x) = \mathbf{1}\{|X - \theta_0| > z_{\alpha/2}\} \quad\text{for } H_0: \theta = \theta_0$$

For asymmetric dists, or interval null $H_1: \theta \notin [\theta_1, \theta_2]$, more complicated

---

## Equal-tailed & unbiased tests

### Point null ($H_0: \theta = \theta_0$)

Let $\alpha_1 = P_{\theta_0}(T < c_1) + \gamma_1 P_{\theta_0}(T = c_1)$

$\alpha_2 = P_{\theta_0}(T > c_2) + \gamma_2 P_{\theta_0}(T = c_2)$

Valid if $\alpha_1 + \alpha_2 = \alpha$ ($\alpha_1$ is "free parameter")

### Idea 1: **Equal-tailed test**: $\alpha_1 = \alpha_2 = \frac{\alpha}{2}$

Null density of test stat $T(X)$

**Ex** $X \sim \text{Exp}(\theta)$, test $H_0: \theta = 1$

Solve for cutoffs:
$$\frac{\alpha}{2} = P_1(X \le c_1) = 1 - e^{-c_1} \implies c_1 = -\log(1 - \alpha/2)$$
$$1 - \frac{\alpha}{2} = 1 - e^{-c_2} \implies c_2 = -\log(\alpha/2)$$

$$\phi(x) = \mathbf{1}\{X < -\log(1-\alpha/2)\} + \mathbf{1}\{X > -\log(\alpha/2)\}$$

$$\beta_\phi(\theta) = P_\theta\left\{\frac{X}{\theta} \overset{\text{Exp}(1)}{<} \frac{-\log(1-\alpha/2)}{\theta}\right\} + P_\theta\left\{\frac{X}{\theta} > \frac{-\log(\alpha/2)}{\theta}\right\}$$
$$= 1 - (1-\alpha/2)^{1/\theta} + (\alpha/2)^{1/\theta} = \alpha \quad\text{for } \theta = 1 \text{ or } 1/2$$

Power $< \alpha$ for $\theta \in (1/2, 1)$

---

## Unbiased tests

**Def** $\phi(x)$ is **unbiased** if $\inf_{\theta \in \Theta_1} \mathbb{E}_\theta \phi(x) \ge \alpha$

### Idea 2: **Unbiased test**: ensure $\min \beta_\phi(\theta) = \alpha$

Choose $c_1, \gamma_1$ and $c_2, \gamma_2$ to solve:

$$\beta_\phi(\theta_0) = \alpha$$
$$\frac{d\beta_\phi}{d\theta}(\theta_0) = 0$$

(2 equations, "2" unknowns)

**Ex:** 1-parameter exp. family, $H_0: \eta = \eta_0 \quad\text{vs}\quad H_1: \eta \ne \eta_0$

$$X \sim e^{\eta T(x) - A(\eta)} h(x) \qquad (\text{MLR in } T(X))$$

Assume $T(X)$ continuous, solve

$$\alpha = \beta_\phi(\eta_0) = P_{\eta_0}(T < c_1) + P_{\eta_0}(T > c_2)$$

$$0 = \frac{d\beta_\phi}{d\eta}(\eta_0) = \text{Cov}_{\eta_0}(\phi(T), T)$$
$$= \mathbb{E}_{\eta_0}\left[(\phi(T) - \alpha) T(X)\right]$$

---

---

[Up: contents](index.md) · [Theorem →](02-theorem.md)
