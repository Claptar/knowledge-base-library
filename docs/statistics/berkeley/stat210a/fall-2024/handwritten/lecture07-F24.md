---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture07-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture07-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture07-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture07-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

9/19/2023

1) Score function
2) Fisher information
3) Cramér-Rao Lower Bound
4) Examples

---

## Motivation: Tangent family

$$p_\theta(x) = e^{\eta(\theta)'T(x) - A(\eta(\theta))} h(x) \qquad \eta: \mathbb{R} \to \mathbb{R}^2$$

$$\Xi = \{\eta(\theta): \theta \in \mathbb{R}\}$$

Curved family: $\eta(\theta)$ nonlinear, $T(x)$ minimal

For $\eta(\theta) = \eta_0 + \theta \delta$, $\delta' T(x)$ is complete sufficient.

Tangent family:
$$\Xi = \{\eta(\theta_0) + \varepsilon \dot{\eta}(\theta_0): \varepsilon \in \mathbb{R}\}$$
where $\dot{\eta}(\theta_0) = \frac{d\eta}{d\theta}(\theta_0)$.

$$q_\varepsilon(x) = e^{(\eta(\theta_0) + \varepsilon \dot{\eta}(\theta_0))'T(x) - A(\dots)} h(x)$$

$$= e^{\varepsilon \underbrace{\dot{\eta}(\theta_0)'(T(x) - \mathbb{E}_{\theta_0} T)}_{S_{\theta_0}(x)} - B(\varepsilon)} k(x)$$

Complete sufficient for tangent family at $\theta_0$.
Called **Score function**.

---

## Score function

Assume $\mathcal{P}$ has densities $p_\theta$ wrt $\mu$, $\Theta \subseteq \mathbb{R}^d$
Common support: $\{x: p_\theta(x) > 0\}$ same $\forall \theta$

Recall $\ell(\theta; x) = \log p_\theta(x)$,
thought of as random function of $\theta$

**Def** The **score** is $\nabla \ell(\theta; x)$; plays a key role in many areas of statistics, esp. asymptotics.

Can think of as "local complete sufficient statistic":
$$p_{\theta_0 + \tau}(x) = e^{\ell(\theta_0 + \tau; x)}$$
$$\approx e^{\tau' \nabla \ell(\theta_0; x)} p_{\theta_0}(x) \quad \text{for } \tau \approx 0$$

**Differential identities:** (assuming enough regularity)

$$1 = \int_{\mathcal{X}} e^{\ell(\theta; x)} d\mu(x)$$

$$\frac{\partial}{\partial \theta_j} \Rightarrow \quad 0 = \int_{\mathcal{X}} \frac{\partial}{\partial \theta_j} \ell(\theta; x) \, e^{\ell(\theta; x)} d\mu(x)$$

$$\Rightarrow \quad \mathbb{E}_\theta [\nabla \ell(\theta; x)] = 0$$
*(only true if these are the same value of $\theta$!)*

---

$$\frac{\partial}{\partial \theta_k} \Rightarrow \quad 0 = \int \left( \frac{\partial^2 \ell}{\partial \theta_j \partial \theta_k} + \frac{\partial \ell}{\partial \theta_j} \cdot \frac{\partial \ell}{\partial \theta_k} \right) e^\ell d\mu$$

$$= \mathbb{E}_\theta \left[ \frac{\partial^2 \ell}{\partial \theta_j \partial \theta_k} \right] + \mathbb{E}_\theta \left[ \frac{\partial \ell}{\partial \theta_j} \frac{\partial \ell}{\partial \theta_k} \right]$$

$$\Rightarrow \quad \underbrace{\operatorname{Var}_\theta [\nabla \ell(\theta; x)]}_{J(\theta)} = \mathbb{E}_\theta [-\nabla^2 \ell(\theta; x)]$$
*(same $\theta$)*

Called "**Fisher Information**"

[It is possible to extend this definition to certain cases where $\ell$ is not even differentiable, e.g. Laplace location family, but for our purposes we can just assume "sufficient regularity."]

Try with another statistic $\delta(X)$, let $g(\theta) = \mathbb{E}_\theta [\delta(X)]$ ("unbiased estimator")

$$g(\theta) = \int \delta \, e^\ell d\mu$$

$$\Rightarrow \quad \nabla g(\theta) = \int \delta \, \nabla \ell \, e^\ell d\mu = \mathbb{E}_\theta [\delta(X) \nabla \ell(\theta; x)]$$

$$= \operatorname{Cov}_\theta(\delta(X), \nabla \ell(\theta; x))$$
*(Since $\mathbb{E} \nabla \ell = 0$)*

---

Combining these results with Cauchy-Schwarz gives us the **Cramér-Rao Lower Bound** or **Information Lower Bound**:

**1-param:**
$$\operatorname{Var}_\theta(\delta) \cdot \operatorname{Var}_\theta(\dot{\ell}(\theta; x)) \ge \operatorname{Cov}_\theta(\delta, \dot{\ell}(\theta; x))^2$$

$$\Rightarrow \quad \operatorname{Var}_\theta(\delta) \ge \dot{g}(\theta)^2 / J(\theta)$$

**Multivariate:** $\theta \in \mathbb{R}^d, \quad g(\theta), \delta(X) \in \mathbb{R}$

$$\operatorname{Var}_\theta(\delta) \ge \nabla g(\theta)' J(\theta)^{-1} \nabla g(\theta)$$

**Proof:**
$$\operatorname{Var}_\theta(\delta) \cdot a' J(\theta) a = \operatorname{Var}_\theta(\delta) \operatorname{Var}(a' \nabla \ell(\theta))$$
$$\ge \operatorname{Cov}_\theta(\delta, a' \nabla \ell(\theta))^2$$
$$= a' \nabla g \, \nabla g' a, \quad \text{for all } a \in \mathbb{R}^d$$

$$\Rightarrow \operatorname{Var}_\theta(\delta) \ge \max_{a \ne 0} \frac{a' \nabla g \, \nabla g' a}{a' J(\theta) a} \overset{\text{Exercise}}{=} \nabla g' J(\theta)^{-1} \nabla g$$

**Interp:** If $g(\theta)$ is estimand, no unbiased estimator can have smaller variance than $\nabla g(\theta)' J(\theta)^{-1} \nabla g(\theta)$

---

## Ex.: (i.i.d. sample)

$$X_1, \dots, X_n \overset{\text{iid}}{\sim} p_\theta^{(1)}(x) \qquad \theta \in \Theta \subseteq \mathbb{R}^d$$

$p_\theta$ "regular": common support, finite derivative wrt $\theta$

$$X \sim p_\theta(x) = \prod_i p_\theta^{(1)}(x_i)$$

Let $\ell_1(\theta; x_i) = \log p_\theta^{(1)}(x_i)$
$$\ell(\theta; x) = \sum_i \ell_1(\theta; x_i)$$

$$J(\theta) = \operatorname{Var}_\theta(\nabla \ell(\theta; x))$$
$$= \operatorname{Var}_\theta\left(\sum_i \nabla \ell_1(\theta; X_i)\right)$$
$$= n J_1(\theta) \qquad \text{where } J_1(\theta) \text{ is Fisher info in single observation}$$

$\Rightarrow$ Lower bound scales like $n^{-1}$ ($\text{SD} \asymp n^{-1/2}$ for "regular" families)

---

## Efficiency

CRLB is not nec. attainable.

We define the **efficiency** of an unbiased estimator as:

$$\operatorname{eff}_\theta(\delta) = \frac{\text{CRLB}}{\operatorname{Var}_\theta(\delta)} \quad \left(= \frac{1/J(\theta)}{\operatorname{Var}_\theta(\delta)} \quad \text{if } g(\theta) = \theta \in \mathbb{R}\right)$$

$$\operatorname{eff}_\theta(\delta) \le 1$$

We say $\delta(X)$ is **efficient** if $\operatorname{eff}_\theta(\delta) = 1 \quad \forall \theta$

Depends on $\operatorname{Corr}_\theta(\delta(X), \nabla \ell(\theta; X))$:

$$\operatorname{eff}_\theta(\delta) = \frac{\operatorname{Cov}_\theta^2(\delta(X), \dot{\ell}(\theta; x))}{\operatorname{Var}_\theta(\delta) \cdot \operatorname{Var}_\theta(\dot{\ell}(\theta))}$$
$$= \operatorname{Corr}_\theta^2(\delta, \dot{\ell}(\theta))$$

$$\le 1$$

$\delta(X)$ is efficient $\iff \operatorname{Corr}_\theta^2(\delta, \dot{\ell}(\theta)) = 1 \quad \forall \theta$

Rarely achieved in finite samples but we can approach it asymptotically as $n \to \infty$

---

## Ex. Exponential Families

$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$$

$$\ell(\eta; x) = \eta' T(x) - A(\eta) + \log h(x)$$

$$\nabla \ell(\eta; x) = T(x) - \nabla A(\eta)$$
$$= T(x) - \mathbb{E}_\eta T(X)$$

$$\operatorname{Var}_\eta(\nabla \ell(\eta)) = \operatorname{Var}_\eta(T(X)) = \nabla^2 A(\eta)$$

$$\nabla^2 \ell(\eta; x) = -\nabla^2 A(\eta)$$

$$\mathbb{E}_\eta [-\nabla^2 \ell(\eta; x)] = \nabla^2 A(\eta) \quad \checkmark$$

So any unbiased est. of $\eta$ has
$$\operatorname{Var}_\eta(\delta) \ge \nabla^2 A(\eta)^{-1}$$

---

## Curved family:

$$p_\theta(x) = e^{\eta(\theta)' T(x) - B(\theta)} h(x), \quad \theta \in \mathbb{R}$$
$$B(\theta) = A(\eta(\theta))$$

$$\ell(\theta; x) = \eta(\theta)' T(x) - B(\theta) + \log h(x)$$

$$\dot{\ell}(\theta; x) = \dot{\eta}(\theta)' T(x) - \dot{\eta}(\theta)' \nabla_\eta A(\eta(\theta))$$
$$= \dot{\eta}(\theta)' (T(x) - \nabla_\eta A(\eta(\theta)))$$
$$= \dot{\eta}(\theta)' (T(x) - \mathbb{E}_\theta T(X))$$

$\Rightarrow \dot{\eta}(\theta)' T(X)$ is "locally complete suff. stat."

For the curve $\eta(\theta)$ in the $(\eta_1, \eta_2)$ plane:
- At a point where $\dot{\eta}(\theta) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\Rightarrow T_1(x)$ important.
- At a point where $\dot{\eta}(\theta) = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, $\Rightarrow T_2(x)$ important.

---

[Up: contents](../index.md)
