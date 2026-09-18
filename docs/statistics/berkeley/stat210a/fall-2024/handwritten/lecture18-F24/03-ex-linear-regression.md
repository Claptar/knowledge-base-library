---
title: Ex. Linear Regression
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture18-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture18-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture18-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture18-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Ex. Linear Regression

$$x_i \in \mathbb{R}^d \text{ fixed}$$
$$Y_i = x_i' \beta + \varepsilon_i, \quad \varepsilon_i \overset{\text{iid}}{\sim} N(0, \sigma^2)$$

$$Y \sim N_d(X\beta, \sigma^2 I_n) \qquad X = \begin{pmatrix} - x_1' - \\ \vdots \\ - x_n' - \end{pmatrix} \in \mathbb{R}^{d \times n}$$
$$= \begin{pmatrix} | & & | \\ X_1 & \cdots & X_d \\ | & & | \end{pmatrix} \quad \substack{\text{capital} \\ \text{letters}}$$

(Assume $X$ has full column rank)

$$\theta = X\beta \in \Theta = \text{Span}(X_1, \dots, X_d)$$

$$H_0: \beta_1 = \cdots = \beta_{d_1} = 0, \quad (1 \le d_1 \le d)$$
$$\Leftrightarrow \theta \in \text{Span}(X_{d_1+1}, \dots, X_d)$$
$$(\text{or } \{0\} \text{ if } d_1 = d)$$

$$\|Z_r\|^2 = \|Y - \text{Proj}_\Theta(Y)\|^2$$
$$= \|Y - X \hat{\beta}_{\text{OLS}}\|^2 \qquad \hat{\beta}_{\text{OLS}} = \arg\min \|Y - X\beta\|^2 = (X'X)^{-1} X' Y$$
$$= \sum (Y_i - x_i' \hat{\beta})^2$$
$$= \text{Residual sum of squares (RSS)}$$

$$\|Z_1\|^2 + \|Z_r\|^2 = \|Y - \text{Proj}_{\Theta_0}(Y)\|^2 = \text{RSS}_0 \quad \text{(null RSS)}$$

---

$$F\text{-statistic} \quad \text{is} \quad \frac{\|Z_1\|^2 / (d - d_0)}{\|Z_r\|^2 / (n - d)} = \frac{(\text{RSS}_0 - \text{RSS}) / (d - d_0)}{\text{RSS} / (n - d)}$$

$n - d$ called **residual degrees of freedom**

$d_1 = 1$: Let $X_0 = (X_2 \cdots X_d) \in \mathbb{R}^{d_0 \times n}$

Let $X_{1\perp} = X_1 - \text{Proj}_{\Theta_0}(X_1)$
$$= X_1 - X_0 (X_0' X_0)^{-1} X_0' X_1$$
$$= X_1 - X_0 \gamma$$

Reparametrize:
$$\theta = X\beta \Leftrightarrow \theta = X_{1\perp} \beta_1 + X_0 (\overbrace{\beta_{-1} + \gamma}^\delta)$$

$$\begin{pmatrix} \hat{\beta}_1 \\ \hat{\delta} \end{pmatrix} = \begin{bmatrix} X_{1\perp}' X_{1\perp} & 0 \\ 0 & X_0' X_0 \end{bmatrix}^{-1} \begin{pmatrix} X_{1\perp}' Y \\ X_0' Y \end{pmatrix} = \begin{pmatrix} X_{1\perp}' Y / \|X_{1\perp}\|^2 \\ (X_0' X_0)^{-1} X_0' Y \end{pmatrix}$$

$$\hat{\beta}_1 = X_{1\perp}' Y / \|X_{1\perp}\|^2, \quad \text{s.e.}(\hat{\beta}_1) = \sigma / \|X_{1\perp}\|$$

$$q_1 = X_{1\perp} / \|X_{1\perp}\|, \quad Q_1 = \begin{pmatrix} q_1' \end{pmatrix}, \quad Q_0 = X_0 (X_0' X_0)^{-1} X_0'$$

$$t\text{-statistic}: \quad \frac{q_1' Y}{\sqrt{\text{RSS} / (n - d)}} = \frac{\hat{\beta}_1}{\hat{\sigma} / \|X_{1\perp}\|} = \frac{\hat{\beta}_1}{\widehat{\text{s.e.}}(\hat{\beta}_1)}$$

---

## Ex: Two-sample $t$-test (equal variance)

$$Y_1, \dots, Y_m \overset{\text{iid}}{\sim} N(\mu, \sigma^2) \qquad Y_{m+1}, \dots, Y_{n+m} \overset{\text{iid}}{\sim} N(\nu, \sigma^2)$$

$$\text{Model}: \quad \theta = \mathbb{E} Y = \begin{pmatrix} \mu \mathbf{1}_m \\ \nu \mathbf{1}_n \end{pmatrix} \Leftrightarrow \theta \in \text{Span}\left(\begin{pmatrix} \mathbf{1}_m \\ -\mathbf{1}_n \end{pmatrix}, \mathbf{1}_{n+m}\right)$$

$$H_0: \mu_1 = \mu_2 \Leftrightarrow \theta \in \text{Span}(\mathbf{1}_{n+m})$$

$$d_0 = 1, \quad d = 2, \quad d_r = n + m - 2$$

$$\text{Orthogonalize } \begin{pmatrix} \mathbf{1}_m \\ -\mathbf{1}_n \end{pmatrix} \rightsquigarrow \begin{matrix} m \\ n \end{matrix} \left\{ \begin{pmatrix} 1/m \\ \vdots \\ 1/m \\ -1/n \\ \vdots \\ -1/n \end{pmatrix} \right.$$

$$\Rightarrow \text{Reject for large}$$

$$\frac{\frac{1}{m} \sum_{i \le m} Y_i - \frac{1}{n} \sum_{i > m} Y_i}{\sqrt{\frac{1}{m} + \frac{1}{n}} \cdot \sqrt{\text{RSS} / (n + m - 2)}} = \frac{\bar{Y}_1 - \bar{Y}_2}{\hat{\sigma} \cdot \sqrt{\frac{1}{m} + \frac{1}{n}}}$$

---

## Ex. One-way ANOVA: (fixed effects)

$$Y_{k, i} \overset{\text{ind.}}{\sim} \mu_k + \varepsilon_{k, i} \qquad \varepsilon_{k, i} \overset{\text{iid}}{\sim} N(0, \sigma^2)$$

$$k = 1, \dots, m \qquad i = 1, \dots, n$$

$$H_0: \mu_1 = \cdots = \mu_m = \mu$$

$$\bar{Y}_k = \frac{1}{n} \sum_i Y_{k, i} \qquad S_k^2 = \frac{1}{n-1} \sum_i (Y_{k, i} - \bar{Y}_k)^2$$

$$\bar{Y} = \frac{1}{mn} \sum_k \sum_i Y_{k, i} \qquad S_0^2 = \frac{1}{mn-1} \sum_k \sum_i (Y_{k, i} - \bar{Y})^2$$

$$d_0 = 1, \quad d = m, \quad d_r = m(n-1)$$

$$\text{RSS} = \sum_{k, i} (Y_{k, i} - \bar{Y}_k)^2 = \|Y\|^2 - n \sum_k \bar{Y}_k^2$$

$$\text{RSS}_0 = \sum_{k, i} (Y_{k, i} - \bar{Y})^2 = \|Y\|^2 - mn \bar{Y}^2$$

$$\text{RSS}_0 - \text{RSS} = n \left(\sum_k \bar{Y}_k^2 - m \bar{Y}^2\right)$$
$$= n \sum_k (\bar{Y}_k - \bar{Y})^2$$

$$F\text{-stat} = \frac{\frac{n}{m-1} \sum_k (\bar{Y}_k - \bar{Y})^2}{\frac{1}{m(n-1)} \sum_k \sum_i (Y_{k, i} - \bar{Y}_k)^2} \begin{matrix} \leftarrow \text{"between" variance} \\ \\ \leftarrow \text{"within" variance} \end{matrix}$$

---

[← Canonical Linear Model](02-canonical-linear-model.md) · [Up: contents](index.md)
