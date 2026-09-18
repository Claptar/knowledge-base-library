---
title: Lecture 08 — fisherinfo Part 01 —
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture08-fisherinfo.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture08-fisherinfo.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture08-fisherinfo.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture08-fisherinfo.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 08 — fisherinfo Part 01 —

1) Score function
2) Fisher information
3) Cramér-Rao Lower Bound
4) Examples

---

## Motivation: Tangent family

$$p_\theta(x) = e^{\eta(\theta)'T(x) - A(\eta(\theta))} h(x) \qquad \eta: \mathbb{R} \to \mathbb{R}^2$$
$$\Xi = \{\eta(\theta): \theta \in \mathbb{R}\}$$

*Curved Family*
$\eta(\theta)$ nonlinear
$T(x)$ minimal

$\eta(\theta) = \eta_0 + \theta \delta$
$\delta'T(x)$ complete suff.

$$\dot{\eta}(\theta_0) = \frac{d\eta}{d\theta}(\theta_0)$$

*Tangent family*
$$\Xi = \{\eta(\theta_0) + \varepsilon \dot{\eta}(\theta_0): \varepsilon \in \mathbb{R}\}$$

$$q_\varepsilon(x) = e^{(\eta(\theta_0) + \varepsilon \dot{\eta}(\theta_0))'T(x) - A(\cdots)} h(x)$$
$$= e^{\varepsilon \dot{\eta}(\theta_0)'(T(x) - \mathbb{E}_{\theta_0} T) - B(\varepsilon)} k(x)$$

where $\dot{\eta}(\theta_0)'(T(x) - \mathbb{E}_{\theta_0} T) = S_{\theta_0}(x)$ is the complete sufficient for tangent family at $\theta_0$, called **Score function**.

---

## Score function

Assume $\mathcal{P}$ has densities $p_\theta$ wrt $\mu$, $\Theta \subseteq \mathbb{R}^d$
Common support: $\{x: p_\theta(x) > 0\}$ same $\forall \theta$

Recall $\ell(\theta; x) = \log p_\theta(x)$,
thought of as random function of $\theta$

**Def** The **score** is $\nabla \ell(\theta; x)$; plays a key role in many areas of statistics, esp. asymptotics.

Can think of as "local complete sufficient statistic":
$$p_{\theta_0 + \eta}(x) = e^{\ell(\theta_0 + \eta; x)}$$
$$\approx e^{\eta' \nabla \ell(\theta_0; x)} p_{\theta_0}(x) \quad \text{for } \eta \approx 0$$

**Differential identities**: (assuming enough regularity)
$$1 = \int_{\mathcal{X}} e^{\ell(\theta; x)} d\mu(x)$$

$$\frac{\partial}{\partial \theta_j} \implies 0 = \int \frac{\partial}{\partial \theta_j} \ell(\theta; x) e^{\ell(\theta; x)} d\mu(x)$$

$$\implies \mathbb{E}_\theta [\nabla \ell(\theta; x)] = 0$$
*(only true if these are the same value of $\theta$!)*

---

$$\frac{\partial}{\partial \theta_k} \implies 0 = \int \left( \frac{\partial^2 \ell}{\partial \theta_j \partial \theta_k} + \frac{\partial \ell}{\partial \theta_j} \cdot \frac{\partial \ell}{\partial \theta_k} \right) e^\ell d\mu$$
$$= \mathbb{E}_\theta \left[ \frac{\partial^2 \ell}{\partial \theta_j \partial \theta_k} \right] + \mathbb{E}_\theta \left[ \frac{\partial \ell}{\partial \theta_j} \frac{\partial \ell}{\partial \theta_k} \right]$$

$$\implies \mathrm{Var}_\theta [\nabla \ell(\theta; x)] = \mathbb{E}_\theta [-\nabla^2 \ell(\theta; x)]$$
$$(=\mathcal{J}(\theta))$$
*(same $\theta$)*

Called "**Fisher Information**"

[It is possible to extend this definition to certain cases where $\ell$ is not even differentiable, e.g. Laplace location family, but for our purposes we can just assume "sufficient regularity."]

Try with another statistic $\delta(X)$, let
$$g(\theta) = \mathbb{E}_\theta [\delta(X)] \quad (\text{"unbiased estimator"})$$
$$g(\theta) = \int \delta e^\ell d\mu$$
$$\implies \nabla g(\theta) = \int \delta \nabla \ell e^\ell d\mu = \mathbb{E}_\theta [\delta(X) \nabla \ell(\theta; x)]$$
$$= \mathrm{Cov}_\theta(\delta(X), \nabla \ell(\theta; x))$$
$$\text{Since } \mathbb{E} \nabla \ell = 0$$

---

Combining these results with Cauchy-Schwarz gives us the **Cramér-Rao Lower Bound** or **Information Lower Bound**:

**1-param:**
$$\mathrm{Var}_\theta(\delta) \cdot \mathrm{Var}_\theta(\dot{\ell}(\theta; x)) \ge \mathrm{Cov}_\theta(\delta, \dot{\ell}(\theta; x))^2$$
$$\implies \mathrm{Var}_\theta(\delta) \ge \dot{g}(\theta)^2 / \mathcal{J}(\theta)$$

**Multivariate:** $\theta \in \mathbb{R}^d$, $g(\theta), \delta(X) \in \mathbb{R}$
$$\mathrm{Var}_\theta(\delta) \ge \nabla g(\theta)' \mathcal{J}(\theta)^{-1} \nabla g(\theta)$$

**Proof**:
$$\mathrm{Var}_\theta(\delta) \cdot a' \mathcal{J}(\theta) a = \mathrm{Var}_\theta(\delta) \mathrm{Var}(a' \nabla \ell(\theta))$$
$$\ge \mathrm{Cov}_\theta(\delta, a' \nabla \ell(\theta))^2$$
$$= a' \nabla g \, \nabla g' a, \quad \text{for all } a \in \mathbb{R}^d$$

$$\implies \mathrm{Var}_\theta(\delta) \ge \max_{a \ne 0} \frac{a' \nabla g \, \nabla g' a}{a' \mathcal{J}(\theta) a} \overset{\text{Exercise}}{=} \nabla g' \mathcal{J}(\theta)^{-1} \nabla g$$

$$\left[ u = \mathcal{J}(\theta)^{1/2} a \implies \max_u \frac{u' \mathcal{J}^{-1/2} \nabla g \nabla g' \mathcal{J}^{-1/2} u}{u' u} \implies u = \mathcal{J}^{-1/2} \nabla g \implies a = \mathcal{J}^{-1} \nabla g \right]$$

**Interp**: If $g(\theta)$ is estimand, no unbiased estimator can have smaller variance than $\nabla g(\theta)' \mathcal{J}(\theta)^{-1} \nabla g(\theta)$

---

## Ex.: (i.i.d. sample)

$$X_1, \ldots, X_n \overset{\text{iid}}{\sim} p_\theta^{(1)}(x) \qquad \theta \in \Theta \subseteq \mathbb{R}^d$$

$p_\theta$ "regular": common support, finite derivative wrt $\theta$

$$X \sim p_\theta(x) = \prod_i p_\theta^{(1)}(x_i)$$
$$\text{Let } \ell_1(\theta; x_i) = \log p_\theta^{(1)}(x_i)$$
$$\ell(\theta; x) = \sum_i \ell_1(\theta; x_i)$$

$$\mathcal{J}(\theta) = \mathrm{Var}_\theta(\nabla \ell(\theta; x))$$
$$= \mathrm{Var}_\theta\left(\sum_i \nabla \ell_1(\theta; X_i)\right)$$
$$= n \mathcal{J}_1(\theta) \qquad \text{where } \mathcal{J}_1(\theta) \text{ is Fisher info in single observation}$$

$\implies$ Lower bound scales like $n^{-1}$ ($SD \asymp n^{-1/2}$ for "regular" families)

---

## Efficiency

CRLB is not nec. attainable.

We define the **efficiency** of an unbiased estimator as:
$$\mathrm{eff}_\theta(\delta) = \frac{\text{CRLB}}{\mathrm{Var}_\theta(\delta)} \left(= \frac{1/\mathcal{J}(\theta)}{\mathrm{Var}_\theta(\delta)} \quad \text{if } g(\theta) = \theta \in \mathbb{R}\right)$$
$$\mathrm{eff}_\theta(\delta) \le 1$$

We say $\delta(X)$ is **efficient** if $\mathrm{eff}_\theta(\delta) = 1$ $\forall \theta$

Depends on $\mathrm{Corr}_\theta(\delta(X), \nabla \ell(\theta; x))$:
$$\mathrm{eff}_\theta(\delta) = \frac{\mathrm{Cov}_\theta^2(\delta(X), \dot{\ell}(\theta; x))}{\mathrm{Var}_\theta(\delta) \cdot \mathrm{Var}_\theta(\dot{\ell}(\theta))}$$
$$= \mathrm{Corr}_\theta^2(\delta, \dot{\ell}(\theta))$$
$$\le 1$$

$\delta(X)$ is efficient $\iff \mathrm{Corr}_\theta^2(\delta, \dot{\ell}(\theta)) = 1$ $\forall \theta$

Rarely achieved in finite samples but we can approach it asymptotically as $n \to \infty$

---

---

[Up: contents](index.md) · [Ex. Exponential Families →](02-ex-exponential-families.md)
