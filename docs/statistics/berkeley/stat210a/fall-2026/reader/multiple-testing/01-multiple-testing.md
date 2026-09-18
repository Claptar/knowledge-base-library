---
title: Multiple Testing
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Multiple Testing

In many testing problems, we want to test many hypotheses at a time, e.g.:

- Test $H_0: \beta_j = 0$ for $j = 1,\ldots,d$ in linear regression
- Test whether each of 20K single nucleotide polymorphisms (SNPs) is associated with a given phenotype (e.g., diabetes, schizophrenia)
- Test whether each of 2000 website tweaks affect user engagement

### Setup

$X \sim P_\theta \in \cP$, $H_{0i}: \theta \in \Theta_i$, $i = 1,\ldots,m$

Commonly, $H_{0i}: \theta_i = 0$

Goal: Return accept/reject decision for each $i$

Let $R = \{i: H_{0i} \text{ rejected}\}$, $|R| \leq m$

$H_{0c} = \{i: H_{0i} \text{ true}\}$, $|H_{0c}| = m_0 \leq m$

$R \cap H_{0c}$ = false rejections

## Family-wise Error Rate (FWER)

Problem: Even if all $H_{0i}$ true, might have:

$\mathbb{P}(\text{any } H_{0i} \text{ rejected}) \leq 1 - (1-\alpha)^m \approx m\alpha$

Example: $X_i \sim N(\theta_i, 1)$ iid, $i = 1,\ldots,m$, $H_{0i}: \theta_i = 0$

$\mathbb{P}_0(\text{any } H_{0i} \text{ rejected}) = 1 - (1-\alpha)^m \approx m\alpha$

Is this a problem? Yes, if all attention will be focused on the false rejections and none on the correct non-rejections.

Classical solution is to control the family-wise error rate (FWER):

FWER = $\mathbb{P}_\theta(\text{any false rejections}) = \mathbb{P}_\theta(R \cap H_{0c} \neq \emptyset)$

Want:
$\sup_\theta \text{FWER}(\theta) \leq \alpha$

Typically achieved by correcting marginal p-values: $p_1(X), \ldots, p_m(X)$, $p_i \sim U(0,1)$

e.g., $\phi_i = 1\{\alpha/(2m)|X_i| > \Phi^{-1}(1-\alpha/(2m))\}$ for Gaussian

## Bonferroni Correction

Assume $p_1,\ldots,p_m$ are p-values for $H_{01},\ldots,H_{0m}$ with $p_i \sim U(0,1)$ under $H_{0i}$

For general dependence, can guarantee control by rejecting $H_{0i}$ iff $p_i \leq \alpha/m$:

$\mathbb{P}_\theta(\text{any false rejections}) \leq \mathbb{P}_\theta(\text{any } H_{0i} \text{ rejected}) \leq \sum_{i \in H_{0c}} \mathbb{P}_\theta(H_{0i} \text{ rejected}) \leq m_0\alpha/m \leq \alpha$

If p-values independent, can improve to $1-(1-\alpha)^{1/m}$ (Šidák correction)

Then $\mathbb{P}_\theta(\text{no false rejections}) = \prod_{i \in H_{0c}} \mathbb{P}_\theta(p_i > (1-(1-\alpha)^{1/m})) \geq (1-\alpha)^{m_0/m} \geq 1-\alpha$

For small $\alpha$: $1-(1-\alpha)^{1/m} \approx \alpha/m$

Šidák doesn't improve much on Bonferroni

## Testing with Dependence

Bonferroni isn't much worse than Šidák
e.g., $\alpha = 0.05$, $m = 20$: $0.0025$ vs $0.00256$

But when tests are highly dependent, can often do much better

### Example: Scheffé's S-method

$X \sim N(\theta, I_d)$, $\theta \in \mathbb{R}^d$
$H_0: a_j^T \theta = 0$ for $j = 1,\ldots,m$, $\|a_j\| = 1$

Reject $H_{0j}$ if $|a_j^T X| > \sqrt{d F_{d,\infty,1-\alpha}}$

Controls FWER:

$\mathbb{P}(\|X - \theta\|^2 \leq dF_{d,\infty,1-\alpha}) = 1-\alpha$

Can view as deduction from confidence region:
$C(X) = \{\theta: \|X - \theta\|^2 \leq dF_{d,\infty,1-\alpha}\}$

---

[Up: contents](index.md) · [Deduced Inference →](02-deduced-inference.md)
