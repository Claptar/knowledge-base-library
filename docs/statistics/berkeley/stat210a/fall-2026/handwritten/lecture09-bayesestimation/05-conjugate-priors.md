---
title: Conjugate Priors
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture09-bayesestimation.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture09-bayesestimation.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture09-bayesestimation.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture09-bayesestimation.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Conjugate Priors

Suppose
$$
X_i \mid \eta \stackrel{iid}{\sim} p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x) \quad \eta \in \Xi \subseteq \mathbb{R}^s, \; i = 1, \dots, n
$$

For carrier $\lambda_0(\eta)$, define $s+1$-dim family:
$$
\lambda_{\mu, k}(\eta) = e^{k\mu'\eta - kA(\eta) - B(k\mu, k)} \lambda_0(\eta)
$$

$$
\text{Suff. stat } \begin{pmatrix} \eta \\ -A(\eta) \end{pmatrix} \in \mathbb{R}^{s+1} \quad \text{Nat. param. } \begin{pmatrix} k\mu \\ k \end{pmatrix}
$$

$$
\begin{aligned}
\Rightarrow \lambda(\eta \mid x_1, \dots, x_n) &\propto_\eta \left(\prod_{i=1}^n e^{\eta' T(x_i) - A(\eta)} h(x_i)\right) \cdot e^{k\mu'\eta - kA(\eta) - B(k\mu, k)} \lambda_0(\eta) \\
&\propto_\eta e^{(k\mu + \sum T(x_i))'\eta - (k+n)A(\eta)} \lambda_0(\eta) \\
&= \lambda_{\mu_{\text{post}}, \, k+n}(\eta)
\end{aligned}
$$

where
$$
\mu_{\text{post}} = \frac{k\mu + n\bar{T}}{k+n}, \quad \bar{T}(x) = \frac{1}{n}\sum_{i=1}^n T(x_i)
$$
*(often Bayes est. for $\mathbb{E}_\eta T$)*

then
$$
\mu_{\text{post}} = \underset{\substack{\uparrow \\ \text{UMVUE from} \\ \text{data}}}{\bar{T}} \cdot \frac{n}{k+n} + \underset{\substack{\uparrow \\ \text{"UMVUE" from} \\ \text{"pseudo data"}}}{\mu} \cdot \frac{k}{k+n}
$$

---

## Conjugate Prior Examples

| Likelihood | Prior |
| :--- | :--- |
| $X_i \mid \theta \sim \operatorname{Binom}(1, \theta)$
$\quad = \theta^x (1-\theta)^{n-x} \binom{n}{x}$ | $\theta \sim \operatorname{Beta}(\alpha, \beta)$
$\quad = \theta^{\alpha - 1} (1-\theta)^{\beta - 1} \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ |
| $X_i \mid \theta \sim N(\theta, \sigma^2) \quad (\sigma^2 \text{ known})$
$\quad = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-(\theta-x)^2 / 2\sigma^2}$ | $\theta \sim N(\mu, \tau^2)$
$\quad = \frac{1}{\sqrt{2\pi\tau^2}} e^{-(\theta-\mu)^2 / 2\tau^2}$ |
| $X_i \mid \theta \sim \operatorname{Pois}(\theta) \quad x = 0, 1, \dots$
$\quad = \frac{\theta^x e^{-\theta}}{x!}$ | $\theta \sim \operatorname{Gamma}(\nu, s) \quad \theta > 0$
$\quad = \frac{1}{\Gamma(\nu) s^\nu} \theta^{\nu - 1} e^{-\theta/s}$ |

### **Gamma / Poisson**:

$$
\begin{aligned}
\lambda(\theta \mid x) &\propto_\theta \theta^{\nu - 1 + \sum x_i} e^{-(s^{-1} + n)\theta} \\
&= \operatorname{Gamma}\left(\nu + \sum x_i, \; (s^{-1} + n)^{-1}\right)
\end{aligned}
$$

$\Rightarrow k = s^{-1}, \quad \mu = \nu s$

$\lambda_0(\theta) = \theta^{-1}$ (not normalizable)

---

## Flexibility of Bayes

Any $\Lambda, \mathcal{P}, L, g(\theta)$: $\delta_\Lambda$ defined straightforwardly

$$
\delta_\Lambda(x) = \arg\min_d \int L(\theta, d) \lambda(\theta \mid x) \, d\theta
$$

Problem reduced to (possibly hard) computation

Posterior is "one stop shop" for all answers

No need for:
* special family structure (exp. fam. / complete s.s.)
* special estimator (U-estimable)
* convex or nice $L$

$\Rightarrow$ Highly expressive modeling & estimation

**Caveat**: Limited by ability to do computations

---

[← Example: Normal mean](04-example-normal-mean.md) · [Up: contents](index.md)
