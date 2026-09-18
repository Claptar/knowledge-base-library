---
title: Canonical Linear Model
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture18-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture18-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture18-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture18-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Canonical Linear Model

Assume $Z = \begin{pmatrix} Z_0 \\ Z_1 \\ Z_r \end{pmatrix} \begin{matrix} d_0 \\ d_1 = d - d_0 \\ d_r = n - d \end{matrix} \sim N_n\left(\begin{pmatrix} \mu_0 \\ \mu_1 \\ 0 \end{pmatrix}, \sigma^2 I_n\right)$

$$\mu_0 \in \mathbb{R}^{d_0}, \quad \mu_1 \in \mathbb{R}^{d_1}, \quad \sigma^2 > 0$$

Test $H_0: \mu_1 = 0$ vs. $H_1: \mu_1 \neq 0$
(or possibly one-sided, if $d_1 = 1$).

Exp. Fam.:

$$p(z) = e^{\frac{\mu_1}{\sigma^2}' Z_1 + \frac{\mu_0}{\sigma^2}' Z_0 - \frac{1}{2\sigma^2} \|Z\|^2}$$

**$\sigma^2$ known, $d_1 = 1$:**

"Cond. on $Z_0$," reject for large (/small/extreme) $Z_1$

$Z_0 \perp\!\!\!\perp Z_1$, test stat is $Z_1 \sim N(\mu_1, \sigma^2)$

$$\frac{Z_1}{\sigma} \overset{H_0}{\sim} N(0, 1) \qquad \mathbf{(z\text{-}test)}$$

**$\sigma^2$ known, $d_1 \ge 1$:** reject for large $\|Z_1\|$ $\substack{\text{unless we have} \\ \text{anisotropic prior on } \mu_1 \\ \downarrow}$

$$\|Z_1\|^2 / \sigma^2 \sim \chi^2_{d_1} \qquad \mathbf{(\chi^2\text{-}test)}$$

---

**$\sigma^2$ unknown, $d_1 = 1$:**

Cond. on $Z_0$, $\|Z\|^2 = \|Z_1\|^2 + \|Z_0\|^2 + \|Z_r\|^2$

Reject for large (/small/extreme) $Z_1$

$$\Leftrightarrow \text{Reject for large } Z_1 / \|Z\|$$

$$\Leftrightarrow \text{Reject for large } \frac{Z_1}{\sqrt{\|Z_r\|^2 / (n-d)}} \overset{H_0}{\sim} t_{d_r} \qquad \mathbf{(t\text{-}test)}$$

**$\sigma^2$, $d \ge 1$:** Reject for (conditionally) large $\|Z_1\|^2$

$$\Leftrightarrow \text{Reject for large } \frac{\|Z_1\|^2 / d_1}{\|Z_r\|^2 / (n-d)} \overset{H_0}{\sim} F_{d_1, n-d} \qquad \mathbf{(F\text{-}test)}$$

Here $\frac{\|Z_r\|^2}{d_r} \sim \frac{\sigma^2}{d_r} \chi^2_{n-d}$ functioning as estimator of $\sigma^2$

$$\mathbb{E} \hat{\sigma}^2 = \sigma^2, \quad \text{Var}(\hat{\sigma}^2) = 2\sigma^4 / (n-d)$$

Compare:
$$z: Z_1 / \sigma \qquad t: Z_1 / \hat{\sigma}$$
$$\chi^2: \|Z_1\|^2 / \sigma^2 \qquad F: \frac{\|Z_1\|^2 / d_1}{\hat{\sigma}^2}$$

---

## Intervals for Canonical Model

How to test $H_0: \mu_1 = \mu_1^\circ \in \mathbb{R}^d$?

Problem: $\mu_1$ is not a natural parameter.

Translate problem:

$$\begin{pmatrix} Z_0 \\ Z_1 - \mu_1^\circ \\ Z_r \end{pmatrix} \sim N_d\left(\begin{pmatrix} \mu_0 \\ \mu_1 - \mu_1^\circ \\ 0 \end{pmatrix}, \sigma^2 I_n\right)$$

Can do same tests with $Z_1 - \mu_1^\circ$ replacing $Z_1$

Invert:

$d_1 = 1, \sigma^2 \text{ kn}$
$$\frac{Z_1 - \mu_1}{\sigma} \sim N(0, 1) \rightsquigarrow \text{CI} \quad Z_1 \pm \sigma z_{\alpha/2} = [Z_1 - \sigma z_{\alpha/2}, Z_1 + \sigma z_{\alpha/2}]$$

$d_1 = 1, \sigma \text{ unkn}$
$$\frac{Z_1 - \mu_1}{\hat{\sigma}} \sim t_{n-d} \rightsquigarrow Z_1 \pm \hat{\sigma} t_{n-d}(\alpha/2)$$

$d_1 \ge 1, \sigma^2 \text{ kn}$:
$$\frac{\|Z_1 - \mu_1\|}{\sigma} \sim \chi^2_{d_1} \rightsquigarrow Z_1 + \sigma \sqrt{c_{\chi^2}(\alpha)} B_1(0)^{\{x: \|x\| \le 1\}}$$
$$\uparrow$$
$$\text{upper-}\alpha \text{ quantile}$$

$d_1 \ge 1, \sigma^2 \text{ unkn}$:
$$\frac{\|Z_1 - \mu_1\|}{\hat{\sigma}} \sim F_{d_1, n-d} \rightsquigarrow Z_1 + \hat{\sigma} \sqrt{c_F(\alpha)} B_1(0)$$

---

## General Linear Model

Many problems can be put into canonical linear model after change of basis.

Basic setup:

Observe $Y \sim N_n(\theta, \sigma^2 I_n)$, $\sigma^2 > 0$ (known or unknown)

Test $\theta \in \Theta_0$ vs. $\theta \in \Theta \setminus \Theta_0$

where $\Theta_0 \subseteq \Theta$ are subspaces of $\mathbb{R}^n$

$$\dim(\Theta_0) = d_0, \quad \dim(\Theta) = d = d_0 + d_1$$

Idea: rotate into canonical form

$$Q = \begin{bmatrix} Q_0 & Q_1 & Q_r \end{bmatrix} \begin{matrix} d_0 \\ d_1 \\ n-d \end{matrix}$$
$$\substack{\text{orthonormal} \\ \text{basis for } \Theta_0} \qquad \substack{\text{o.b. for} \\ \Theta \cap \Theta_0^\perp} \qquad \substack{\text{o.b. for} \\ \mathbb{R}^n \cap \Theta^\perp}$$

$$Z = Q' Y \sim N_n\left(\begin{pmatrix} Q_0' \theta \\ Q_1' \theta \\ 0 \end{pmatrix}, \sigma^2 I_n\right)$$

$$H_0: Q_1' \theta = 0$$

Do $z$, $\chi^2$, $t$, or $F$-test as appropriate

---

---

[← Outline](01-outline.md) · [Up: contents](index.md) · [Ex. Linear Regression →](03-ex-linear-regression.md)
