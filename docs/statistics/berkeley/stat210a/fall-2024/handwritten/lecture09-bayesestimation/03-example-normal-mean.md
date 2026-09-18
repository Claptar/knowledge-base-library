---
title: 'Example: Normal mean'
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture09-bayesestimation.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture09-bayesestimation.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture09-bayesestimation.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture09-bayesestimation.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Example: Normal mean

$$
X \mid \theta &\sim N(\theta, \sigma^2) \propto_\theta e^{-(x-\theta)^2 / 2\sigma^2} \\
\theta &\sim N(\mu, \tau^2) \propto_\theta e^{-(\theta-\mu)^2 / 2\tau^2}
$$

$$
\lambda(\theta \mid x) &\propto_\theta \exp\left\{ -\frac{(x-\theta)^2}{2\sigma^2} - \frac{(\theta-\mu)^2}{2\tau^2} \right\} \\
&\propto_\theta \exp\left\{ \frac{x\theta}{\sigma^2} - \frac{\theta^2}{2\sigma^2} - \frac{\theta^2}{2\tau^2} + \frac{\theta\mu}{\tau^2} \right\} \\
&= \exp\left\{ \theta \underbrace{\left(\frac{x}{\sigma^2} + \frac{\mu}{\tau^2}\right)}_b - \theta^2 \underbrace{\left(\frac{\sigma^{-2} + \tau^{-2}}{2}\right)}_{a^2} \right\}
$$

Complete square:

$$
a^2 \theta^2 - b\theta &= \left(\theta a - \frac{b}{2a}\right)^2 - c(a, b) \\
&= \left(\theta - \frac{b}{2a^2}\right)^2 a^2 - c
$$

$$
&\propto_\theta \exp\left\{ -\left(\theta - \frac{x\sigma^{-2} + \mu\tau^{-2}}{\sigma^{-2} + \tau^{-2}}\right)^2 \Big/ 2(\sigma^{-2} + \tau^{-2})^{-1} \right\} \\
&\propto_\theta N\left(\frac{x\sigma^{-2} + \mu\tau^{-2}}{\sigma^{-2} + \tau^{-2}}, \, \frac{1}{\sigma^{-2} + \tau^{-2}}\right)
$$

where the mean is a precision-weighted average of $x, \mu$, and variance is the harmonic mean of $\sigma^2, \tau^2$.

$$
\mathbb{E}[\theta \mid X] = X \cdot \frac{\sigma^{-2}}{\sigma^{-2} + \tau^{-2}} + \mu \cdot \frac{\tau^{-2}}{\sigma^{-2} + \tau^{-2}}
$$

---

## Gaussian iid sample

$\theta \sim N(\mu, \tau^2), \quad X_i \mid \theta \overset{\text{iid}}{\sim} N(\theta, \sigma^2), \quad i=1, \dots, n$

$\bar{X} \mid \theta \sim N\left(\theta, \frac{\sigma^2}{n}\right)$

$$
\Rightarrow \mathbb{E}[\theta \mid X] &= \bar{X} \cdot \frac{n\sigma^{-2}}{n\sigma^{-2} + \tau^{-2}} + \mu \cdot \frac{\tau^{-2}}{n\sigma^{-2} + \tau^{-2}} \\
&= \bar{X} \cdot \frac{n}{n + \sigma^2/\tau^2} + \mu \cdot \frac{\sigma^2/\tau^2}{n + \sigma^2/\tau^2}
$$

Interp: $k = \sigma^2/\tau^2$ pseudo-observations, mean $\mu$
If $n \gg k$, "data swamps prior"
If $n \ll k$, "prior swamps data"

[Note in both examples:
* Prior & Likelihood have similar fcn. form
* Posterior comes from same exp. fam. as prior]

If the posterior is from the same family as the prior, we say the prior is **conjugate** to the likelihood.

Most common in exp. families

---

## Conjugate Priors

Suppose $X_i \mid \eta \overset{\text{iid}}{\sim} p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x) \quad \eta \in \Xi \subseteq \mathbb{R}^s, \; i=1,\dots,n$

For carrier $\lambda_0(\eta)$, define $s+1$-dim family:

$$
\lambda_{\mu, k}(\eta) = e^{k\mu'\eta - k A(\eta) - B(k\mu, k)} \lambda_0(\eta)
$$

Suff. stat $\begin{pmatrix} \eta \\ -A(\eta) \end{pmatrix} \in \mathbb{R}^{s+1} \qquad \text{Nat. param. } \begin{pmatrix} k\mu \\ k \end{pmatrix}$

$$
\Rightarrow \lambda(\eta \mid x_1, \dots, x_n) &\propto_\eta \left(\prod_{i=1}^n e^{\eta' T(x_i) - A(\eta)} h(x_i)\right) \cdot e^{k\mu'\eta - kA(\eta) - B(k\mu, k)} \lambda_0(\eta) \\
&\propto_\eta e^{(k\mu + \sum T(x_i))'\eta - (k+n)A(\eta)} \lambda_0(\eta) \\
&= \lambda_{\mu_{\text{post}}, \, k+n}(\eta)
$$

where $\mu_{\text{post}} = \frac{k\mu + n\bar{T}}{k+n}, \quad \bar{T}(x) = \frac{1}{n} \sum_{i=1}^n T(x_i)$

often Bayes est. for $\mathbb{E}_\eta T$

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
$\quad = \theta^{\alpha-1} (1-\theta)^{\beta-1} \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ |
| $X_i \mid \theta \sim N(\theta, \sigma^2) \quad (\sigma^2 \text{ known})$
$\quad = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-(\theta-x)^2 / 2\sigma^2}$ | $\theta \sim N(\mu, \tau^2)$
$\quad = \frac{1}{\sqrt{2\pi\tau^2}} e^{-(\theta-\mu)^2 / 2\tau^2}$ |
| $X_i \mid \theta \sim \operatorname{Pois}(\theta) \quad x=0, 1, \dots$
$\quad = \frac{\theta^x e^{-\theta}}{x!}$ | $\theta \sim \operatorname{Gamma}(\nu, s) \quad \theta > 0$
$\quad = \frac{1}{\Gamma(\nu) s^\nu} \theta^{\nu-1} e^{-\theta/s}$ |

**Gamma / Poisson**:

$$
\lambda(\theta \mid x) &\propto_\theta \theta^{\nu-1 + \sum x_i} e^{-(s^{-1} + n)\theta} \\
&= \operatorname{Gamma}\left(\nu + \sum x_i, \; (s^{-1} + n)^{-1}\right)
$$

$\Rightarrow k = s^{-1}, \quad \mu = \nu s$
$\lambda_0(\theta) = \theta^{-1} \quad (\text{not normalizable})$

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
* special estimator (u-estimable)
* convex or nice $L$

$\Rightarrow$ Highly expressive modeling & estimation

**Caveat**: Limited by ability to do computations

---

## Source #2: "Objective" or "vague" prior

Using default prior removes subjectivity
(But then what does the posterior mean?)

**Flat prior** $\lambda(\theta) \propto_\theta 1 \quad \text{on } \Theta$
"Indifference" (in $\theta$ parameterization)
Often improper ($\Lambda(\Theta) = \infty$) but usually ok

**Ex**: $\theta \sim \text{flat prior on } \mathbb{R}$
$X \mid \theta \sim N(\theta, \sigma^2)$
$\lambda(\theta \mid x) \propto_\theta p_\theta(x)$
$\quad = \frac{1}{\sqrt{2\pi}} e^{-(x-\theta)^2 / 2\sigma^2}$
$\quad \propto_\theta N(x, \sigma^2)$

**Jeffreys prior** $\lambda(\theta) \propto_\theta |J(\theta)|^{1/2}$
Higher density where $P_\theta$ "changing faster"
Invariant to parameterization

**Ex**. $X \mid \theta \sim \operatorname{Binom}(n, \theta)$
$\lambda(\theta) \propto_\theta J(\theta)^{1/2} = \left(\frac{n}{\theta(1-\theta)}\right)^{1/2} \propto_\theta \operatorname{Beta}\left(\frac{1}{2}, \frac{1}{2}\right)$

$\lambda(\theta) \to \infty$ as $\theta \to 0$ or $1$:
$D_{\text{KL}}(0.001 \parallel 0.01) \underset{(35\times)}{\gg} D_{\text{KL}}(0.49 \parallel 0.5)$
$7n \cdot 10^{-3} \qquad\qquad 2n \cdot 10^{-4}$

---

[← Example: Beta-Binomial](02-example-beta-binomial.md) · [Up: contents](index.md)
