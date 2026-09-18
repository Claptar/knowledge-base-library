---
title: Ex. Linear Regression
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture18-linearmodel.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture18-linearmodel.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture18-linearmodel.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture18-linearmodel.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Ex. Linear Regression

$x_i \in \mathbb{R}^d$ fixed

$$Y_i = x_i' \beta + \varepsilon_i, \quad \varepsilon_i \overset{iid}{\sim} N(0, \sigma^2)$$

$$Y \sim N_d(X\beta, \sigma^2 I_n) \qquad X = \begin{pmatrix} - x_1' - \\ \vdots \\ - x_n' - \end{pmatrix} \in \mathbb{R}^{d \times n}$$
$$= \begin{pmatrix} | & & | \\ X_1 & \cdots & X_d \\ | & & | \end{pmatrix} \quad \text{capital letters}$$

(Assume $X$ has full column rank)

$$\theta = X\beta \in \Theta = \text{Span}(X_1, \dots, X_d) \quad (\text{"model space"})$$

$$H_0: \beta_1 = \dots = \beta_{d_1} = 0, \quad (1 \le d_1 \le d)$$

$$\iff \theta \in \Theta_0 = \text{Span}(X_{d_1+1}, \dots, X_d) \quad (\text{"null model space"})$$
$$(\text{or } \{0\} \text{ if } d_1 = d)$$

Rotate into canonical basis:
$Q_0 = \text{orthobasis for } \Theta_0$
$Q_1 = \text{orthobasis for } \Theta \cap \Theta_0^\perp$
$Q_r = \text{orthobasis for } \mathbb{R}^n \cap \Theta_0$

$$F\text{-stat} = \frac{\|Q_1' Y\|^2 / d_1}{\|Q_r' Y\|^2 / (n-d)}, \qquad t\text{-stat} = \frac{q_1' Y}{\sqrt{\|Q_r' Y\|^2 / (n-d)}} \quad (\text{if } d_1 = 1)$$

---

Nice to get more explicit expressions

$$\hat{\beta}_{\text{OLS}} = \underset{\beta}{\text{argmin}} \, \|Y - X\beta\|^2 = (X'X)^{-1} X'Y$$

$$\|Z_r\|^2 = \|Q_r' Y\|^2$$
$$= \|\text{Proj}_\Theta^\perp(Y)\|^2$$
$$= \|Y - \text{Proj}_\Theta(Y)\|^2$$
$$= \sum_i (Y_i - x_i' \hat{\beta}_{\text{OLS}})^2 \qquad \begin{matrix} r_i = Y_i - x_i' \hat{\beta}_{\text{OLS}} \\ \text{called residual} \end{matrix}$$
$$= \text{Residual sum of squares } (RSS)$$

$n-d$ called **residual degrees of freedom**

$$\|Z_1\|^2 + \|Z_r\|^2 = \|[Q_1 Q_r]' Y\|^2$$
$$= \|\text{Proj}_{\Theta_0}^\perp(Y)\|^2$$
$$= RSS_0 \quad (\text{null } RSS)$$

$$F\text{-statistic} \quad \text{is} \quad \frac{\|Z_1\|^2 / (d - d_0)}{\|Z_r\|^2 / (n - d)} = \frac{(RSS_0 - RSS) / (d - d_0)}{RSS / (n - d)}$$

---

$d_1 = 1$: Let $X_0 = \begin{pmatrix} X_2 \cdots X_d \end{pmatrix} \in \mathbb{R}^{d_0 \times n}$

$$q_1 = \frac{X_{1\perp}}{\|X_{1\perp}\|},$$

where $X_{1\perp} = X_1 - \text{Proj}_{\Theta_0}(X_1)$
$$= X_1 - X_0 (X_0' X_0)^{-1} X_0' X_1$$
$$= X_1 - X_0 \gamma$$

Reparametrize:
$$\theta = X\beta \iff \theta = X_{1\perp}\beta_1 + X_0 \overbrace{(\beta_{-1} + \gamma\beta_1)}^\delta$$
$$= \begin{bmatrix} X_{1\perp} & X_0 \end{bmatrix} \begin{pmatrix} \beta_1 \\ \delta \end{pmatrix}$$

OLS solution in new parametrization:
$$\begin{pmatrix} \hat{\beta}_1 \\ \hat{\delta} \end{pmatrix} = \left( [X_{1\perp} \, X_0]' [X_{1\perp} \, X_0] \right)^{-1} [X_{1\perp} \, X_0]' Y$$
$$= \begin{bmatrix} X_{1\perp}' X_{1\perp} & 0 \\ 0 & X_0' X_0 \end{bmatrix}^{-1} \begin{pmatrix} X_{1\perp}' Y \\ X_0' Y \end{pmatrix} = \begin{pmatrix} X_{1\perp}' Y / \|X_{1\perp}\|^2 \\ (X_0' X_0)^{-1} X_0' Y \end{pmatrix}$$

$$\hat{\beta}_1 = X_{1\perp}' Y / \|X_{1\perp}\|^2, \qquad \text{s.e.}(\hat{\beta}_1) \triangleq \sqrt{\text{Var}(\hat{\beta}_1)} = \sigma / \|X_{1\perp}\|$$

$$t\text{-statistic}: \quad \frac{q_1' Y}{\sqrt{RSS / (n-d)}} = \frac{\hat{\beta}_1}{\hat{\sigma} / \|X_{1\perp}\|} = \frac{\hat{\beta}_1}{\widehat{\text{s.e.}}(\hat{\beta}_1)}$$

---

## **Ex**: Two-sample $t$-test (equal variance)

$$Y_1, \dots, Y_m \overset{iid}{\sim} N(\mu, \sigma^2) \qquad Y_{m+1}, \dots, Y_{n+m} \overset{iid}{\sim} N(\nu, \sigma^2)$$

$$\text{Model}: \quad \theta = \mathbb{E} Y = \begin{pmatrix} \mu \mathbf{1}_m \\ \nu \mathbf{1}_n \end{pmatrix} \iff \theta \in \text{Span}\left( \begin{pmatrix} \mathbf{1}_m \\ -\mathbf{1}_n \end{pmatrix}, \mathbf{1}_{n+m} \right)$$

$$H_0: \mu_1 = \mu_2 \iff \theta \in \text{Span}(\mathbf{1}_{n+m})$$

$$d_0 = 1, \quad d = 2, \quad d_r = n + m - 2$$

$$\text{Orthogonalize } \begin{pmatrix} \mathbf{1}_m \\ -\mathbf{1}_n \end{pmatrix} \leadsto \left.\begin{matrix} m\Bigg\{ \\ n\Bigg\{ \end{matrix}\right. \begin{pmatrix} 1/m \\ \vdots \\ 1/m \\ -1/n \\ \vdots \\ -1/n \end{pmatrix}$$

$\Rightarrow$ Reject for large

$$\frac{\frac{1}{m} \sum_{i \le m} Y_i - \frac{1}{n} \sum_{i > m} Y_i}{\sqrt{\frac{1}{m} + \frac{1}{n}} \cdot \sqrt{RSS / (n + m - 2)}} = \frac{\overline{Y}_1 - \overline{Y}_2}{\hat{\sigma} \cdot \sqrt{\frac{1}{m} + \frac{1}{n}}}$$

---

## **Ex**. One-way ANOVA: (fixed effects)

$$Y_{k, i} \overset{ind}{\sim} \mu_k + \varepsilon_{k, i} \qquad \varepsilon_{k, i} \overset{iid}{\sim} N(0, \sigma^2)$$
$$k = 1, \dots, m \qquad i = 1, \dots, n$$

$$H_0: \mu_1 = \dots = \mu_m = \mu$$

$$\overline{Y}_k = \frac{1}{n} \sum_i Y_{k, i} \qquad S_k^2 = \frac{1}{n-1} \sum_i (Y_{k, i} - \overline{Y}_k)^2$$

$$\overline{Y} = \frac{1}{mn} \sum_k \sum_i Y_{k, i} \qquad S_0^2 = \frac{1}{mn-1} \sum_k \sum_i (Y_{k, i} - \overline{Y})^2$$

$$d_0 = 1, \quad d = m, \quad d_r = m(n-1)$$

$$RSS = \sum_{k, i} (Y_{k, i} - \overline{Y}_k)^2 = \|Y\|^2 - n \sum_k \overline{Y}_k^2$$

$$RSS_0 = \sum_{k, i} (Y_{k, i} - \overline{Y})^2 = \|Y\|^2 - mn\,\overline{Y}^2$$

$$RSS_0 - RSS = n \left( \sum_k \overline{Y}_k^2 - m\overline{Y}^2 \right)$$
$$= n \sum_k (\overline{Y}_k - \overline{Y})^2$$

$$F\text{-stat} = \frac{\frac{n}{m-1} \sum_k (\overline{Y}_k - \overline{Y})^2}{\frac{1}{m(n-1)} \sum_k \sum_i (Y_{k, i} - \overline{Y}_k)^2} \quad \begin{matrix} \leftarrow \text{"between" variance} \\ \\ \leftarrow \text{"within" variance} \end{matrix}$$

---

[← Canonical Linear Model](02-canonical-linear-model.md) · [Up: contents](index.md)
