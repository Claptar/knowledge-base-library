---
title: t and F Distributions
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-linear.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-linear.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# t and F Distributions

**Source:** [`reader/testing-linear.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-linear.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Definitions and Properties

1. $\chi^2_d$: If $X_i \sim N(0,1)$ iid, then $V = \sum_{i=1}^d X_i^2 \sim \chi^2_d$
   - $\mathbb{E}[V] = d$, $\text{Var}(V) = 2d$
   - CLT: $V \approx N(d, 2d)$ for large $d$

2. $t_d$: If $Z \sim N(0,1)$ and $V \sim \chi^2_d$ independent, then $T = \frac{Z}{\sqrt{V/d}} \sim t_d$
   - Informally: $Y \sim N(\mu, 1)$, $\hat{\sigma}^2 \sim \frac{\chi^2_d}{d}$, $\frac{Y - \mu}{\hat{\sigma}} \sim t_d$

3. If $Z \sim N(0,1)$ and $V \sim \chi^2_d$, $Z/\sqrt{V} \sim t_d$ as $d \to \infty$

4. If $V \sim \chi^2_d$ and $V_2 \sim \chi^2_{d_2}$ independent, $V/V_2 \sim F_{d,d_2}$, then:

   $\frac{V/d}{V_2/d_2} \sim F_{d,d_2}$ as $d,d_2 \to \infty$

Note: If $T \sim t_d$, then $T^2 \sim F_{1,d}$

Recall: $Z \sim N_d(\mu, \Sigma)$ iff $A Z + b \sim N_d(A\mu + b, A\Sigma A^T)$

### Geometric Interpretation

Let $X \sim N_n(\mu, I_n)$, $\mu = \alpha e_1$, where $\{e_1, \ldots, e_n\}$ is a complete orthonormal basis (e.g., via Gram-Schmidt)

$X = \sum_{i=1}^n \langle X, e_i \rangle e_i = \alpha e_1 + \sum_{i=1}^n Z_i e_i$, $Z_i \sim N(0,1)$ iid

New basis: $Z = Q'X$, $\|X\|^2 = \|Z\|^2$

$\begin{pmatrix} Z_1 \\ Z_{2:n} \end{pmatrix} = \begin{pmatrix} Q_1' \\ Q_{2:n}' \end{pmatrix} X \sim N\left(\begin{pmatrix} \alpha \\ 0 \end{pmatrix}, I_n\right)$

$Z_1 = Q_1' X \sim N(\alpha, 1)$
$Z_{2:n} = Q_{2:n}' X \sim N(0, I_{n-1})$

$S^2 = \|Z_{2:n}\|^2 = \sum_{i=2}^n Z_i^2$ and $Z_1$ independent (we already knew from Basu)

### Geometric Interpretation (continued)

Independent of total magnitude under $H_0$:

- $n\bar{X}^2 = \alpha^2 \sim \text{Gamma}(\frac{1}{2}, \frac{2}{n})$
- $\sum_{i=1}^n (X_i - \bar{X})^2 \sim \text{Gamma}(\frac{n-1}{2}, 2)$
- $\|X\|^2 = n\bar{X}^2 + \sum_{i=1}^n (X_i - \bar{X})^2 \sim \text{Gamma}(\frac{n}{2}, 2)$

$\frac{n\bar{X}^2}{\sum_{i=1}^n (X_i - \bar{X})^2} \sim \text{Beta}(\frac{1}{2}, \frac{n-1}{2})$ independent of $\|X\|^2$

$F_{1,n-1}$ related to $\text{Beta}(\frac{1}{2}, \frac{n-1}{2})$: If $U \sim \text{Beta}(\frac{a}{2}, \frac{b}{2})$, then $\frac{b}{a} \cdot \frac{U}{1-U} \sim F_{a,b}$

---

[Up: contents](index.md) · [Canonical Linear Model →](02-canonical-linear-model.md)
