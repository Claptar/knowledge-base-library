---
title: Canonical Linear Model
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture18-linearmodel.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture18-linearmodel.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture18-linearmodel.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture18-linearmodel.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Canonical Linear Model

Assume $Z = \begin{pmatrix} Z_0 \\ Z_1 \\ Z_r \end{pmatrix} \begin{matrix} d_0 \\ d_1 = d - d_0 \\ d_r = n - d \end{matrix} \sim N_n \left( \begin{pmatrix} \mu_0 \\ \mu_1 \\ 0 \end{pmatrix}, \sigma^2 I_n \right)$

$\mu_0 \in \mathbb{R}^{d_0}$, $\mu_1 \in \mathbb{R}^{d_1}$, $\sigma^2 > 0$

Test $H_0: \mu_1 = 0$ vs. $H_1: \mu_1 \neq 0$
(or possibly one-sided, if $d_1 = 1$).

Exp. Fam.:
$$p(z) = e^{\frac{\mu_1}{\sigma^2}' Z_1 + \frac{\mu_0}{\sigma^2}' Z_0 - \frac{1}{2\sigma^2} \|Z\|^2}$$

**$\sigma^2$ known, $d_1 = 1$**:

"Cond. on $Z_0$", reject for large(/small/extreme) $Z_1$

$Z_0 \perp \!\!\! \perp Z_1$, test stat is $Z_1 \sim N(\mu_1, \sigma^2)$

$\frac{Z_1}{\sigma} \overset{H_0}{\sim} N(0, 1)$ ($z$-test) $\overset{\text{unless we have}}{\underset{\text{anisotropic prior on }\mu_1}{\downarrow}}$

**$\sigma^2$ known, $d_1 \ge 1$**: reject for large $\|Z_1\|$
$$\|Z_1\|^2 / \sigma^2 \sim \chi^2_{d_1} \quad (\chi^2\text{-test})$$

---

**$\sigma^2$ unknown, $d_1 = 1$**:

Cond. on $Z_0$, $\|Z\|^2 = \|Z_1\|^2 + \|Z_0\|^2 + \|Z_r\|^2$

Reject for large(/small/extreme) $Z_1$

$\iff$ Reject for large $Z_1 / \|Z\|$

$\iff$ Reject for large $\frac{Z_1}{\sqrt{\|Z_r\|^2 / (n-d)}} \overset{H_0}{\sim} t_{d_r}$

($t$-test)

**$\sigma^2$, $d_1 \ge 1$**: Reject for (conditionally) large $\|Z_1\|^2$

$\iff$ Reject for large $\frac{\|Z_1\|^2 / d_1}{\|Z_r\|^2 / (n-d)} \overset{H_0}{\sim} F_{d_1, n-d}$

($F$-test)

Here $\|Z_r\|^2 / d_r \sim \frac{\sigma^2}{d_r} \chi^2_{n-d}$
functioning as estimator of $\sigma^2$
$$\mathbb{E}\,\hat{\sigma}^2 = \sigma^2, \quad \text{Var}(\hat{\sigma}^2) = 2\sigma^4 / (n-d)$$

Compare:
$$z: \frac{Z_1}{\sigma} \qquad t: \frac{Z_1}{\hat{\sigma}}$$
$$\chi^2: \frac{\|Z_1\|^2}{\sigma^2} \qquad F: \frac{\|Z_1\|^2 / d_1}{\hat{\sigma}^2}$$

---

## Intervals for Canonical Model

How to test $H_0: \mu_1 = \mu_1^\circ \in \mathbb{R}^d$?

**Problem**: $\mu_1$ is not a natural parameter.

Translate problem:

$$\begin{pmatrix} Z_0 \\ Z_1 - \mu_1^\circ \\ Z_r \end{pmatrix} \sim N_d \left( \begin{pmatrix} \mu_0 \\ \mu_1 - \mu_1^\circ \\ 0 \end{pmatrix}, \sigma^2 I_n \right)$$

Can do same tests with $Z_1 - \mu_1^\circ$ replacing $Z_1$

**Invert**:
$$d_1 = 1, \sigma^2 \text{ kn}: \quad \frac{Z_1 - \mu_1}{\sigma} \sim N(0, 1) \leadsto \text{CI } Z_1 \pm \sigma z_{\alpha/2} = [Z_1 - \sigma z_{\alpha/2}, Z_1 + \sigma z_{\alpha/2}]$$

$$d_1 = 1, \hat{\sigma} \text{ unkn}: \quad \frac{Z_1 - \mu_1}{\hat{\sigma}} \sim t_{n-d} \leadsto Z_1 \pm \hat{\sigma} t_{n-d}^{(\alpha/2)}$$

$$d \ge 1, \sigma^2 \text{ kn}: \quad \frac{\|Z_1 - \mu_1\|}{\sigma} \sim \chi^2_{d_1} \leadsto Z_1 + \sigma \sqrt{c_{\chi^2}(\alpha)} B_1(0)^{\{x: \|x\| \le 1\}}$$

$$d_1 \ge 1, \sigma^2 \text{ unkn}: \quad \frac{\|Z_1 - \mu_1\|}{\hat{\sigma}} \sim F_{d_1, n-d} \leadsto Z_1 + \hat{\sigma} \sqrt{c_F(\alpha)} B_1(0)$$
*(where $c(\alpha)$ is the upper-$\alpha$ quantile)*

---

## General Linear Model

Many problems can be put into canonical linear model after change of basis.

**Basic setup**:
$$\text{Observe } Y \sim N_n(\theta, \sigma^2 I_n), \quad \sigma^2 > 0 \quad (\text{known or unknown})$$

Test $\theta \in \Theta_0$ vs. $\theta \in \Theta \setminus \Theta_0$
where $\Theta_0 \subseteq \Theta$ are subspaces of $\mathbb{R}^n$
$$\dim(\Theta_0) = d_0, \quad \dim(\Theta) = d = d_0 + d_1$$

**Idea**: rotate into canonical form

$$Q = \begin{bmatrix} \overset{d_0}{Q_0} & \overset{d_1}{Q_1} & \overset{n-d}{Q_r} \end{bmatrix}$$
$$\text{orthonormal basis for } \Theta_0 \quad\quad \text{o.b. for } \Theta \cap \Theta_0^\perp \quad\quad \text{o.b. for } \mathbb{R}^n \cap \Theta^\perp$$

$$Z = Q'Y \sim N_n\left( \begin{pmatrix} Q_0' \theta \\ Q_1' \theta \\ 0 \end{pmatrix}, \sigma^2 I_n \right)$$

$$H_0: Q_1' \theta = 0$$

Do $z$, $\chi^2$, $t$, or $F$-test as appropriate

---

---

[← Outline](01-outline.md) · [Up: contents](index.md) · [Ex. Linear Regression →](03-ex-linear-regression.md)
