---
title: Lecture Six
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSix153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureSix153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureSix153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSix153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture Six

$$y_t = \beta_0 + \beta_1 t + \beta_2 (t-c)_+ + \varepsilon_t$$

## Parameter Estimation

(1) Calculate $RSS(c)$ for a bunch of values of $c$.
$$c \in [1, n]$$
$$c \in \{1, 2, \dots, n\}$$

(2) $\hat{c}$ : value which minimizes $RSS(c)$

(3) Fix $c = \hat{c}$ & run linear regression of $y$ on $[1, t, (t-\hat{c})_+] = X$ to estimate $\beta_0, \beta_1, \beta_2$ (also $\sigma$)

**Least Squares:**

$$\sum_{t=1}^n [y_t - \beta_0 - \beta_1 t - \beta_2(t-c)_+]^2$$

$$RSS(c) = \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n [y_t - \beta_0 - \beta_1 t - \beta_2(t-c)_+]^2$$

## Uncertainty Quantification

**Likelihood:** $\varepsilon_t \overset{\text{iid}}{\sim} N(0, \sigma^2)$

$$\prod_{t=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{1}{2\sigma^2} (y_t - \beta_0 - \beta_1 t - \beta_2(t-c)_+)^2 \right)$$

$$\propto \sigma^{-n} \exp\left[ -\frac{\sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2(t-c)_+)^2}{2\sigma^2} \right]$$

---

$$S(\boldsymbol{\beta}, c) = \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2(t-c)_+)^2$$

$$\left. \sigma^{-n} \exp\left[ -\frac{S(\boldsymbol{\beta}, c)}{2\sigma^2} \right] \right\} \text{SAME AS FOR LINEAR REGRESSION}$$

**Remark:** $\text{MLE of } \boldsymbol{\beta} \ & \ c = \text{Least squares of } \boldsymbol{\beta} \ & \ c$

**prior:** $\beta_0, \beta_1, \beta_2, \sigma, c$

$\beta_0, \beta_1, \beta_2, \log \sigma \overset{\text{iid}}{\sim} \text{Unif}[-C, C]$ as $C \to \infty$
*(previous prior that we used in linear regression)*

$$c \in \{$$

$$y_t = \beta_0 + \beta_1 t + \beta_2 (t-c)_+ + \varepsilon_t$$

$c = 0 : \quad \beta_0 + \beta_1 t + \beta_2 t = \beta_0 + (\beta_1 + \beta_2)t$

$c = 1 : \quad \beta_0 + \beta_1 t + \beta_2 (t-1) = \beta_0 - \beta_2 + (\beta_1 + \beta_2)t$

$c = n : \quad (t-c)_+ = 0 \to \beta_0 + \beta_1 t$

Natural to restrict $c \in (1, n) \to \text{wide region}$
$c \in (10, n-10) \to \text{reasonable}$
*(reasonable: our interest mainly lies in $c$ away from the edges)*

$$c \sim \text{Unif}(1, n)$$
$$c \sim \text{Unif}\{2, 3, \dots, n-1\}$$

---

**Prior:** $\beta_0, \beta_1, \beta_2, \log \sigma, c \text{ independent}$

$$\beta_0, \beta_1, \beta_2, \log \sigma \overset{\text{iid}}{\sim} \text{Unif}(-\infty, \infty), \quad c \sim \text{Unif}(1, n)$$

$$f_{\beta_0, \beta_1, \beta_2, \sigma, c}(\beta_0, \beta_1, \beta_2, \sigma, c) \propto \frac{1}{\sigma} I\{1 < c < n\} I\{\sigma > 0\}$$

$$\text{posterior} \propto \text{likelihood} \times \text{prior}$$

$$\propto \sigma^{-n} \exp\left[ -\frac{S(\boldsymbol{\beta}, c)}{2\sigma^2} \right] \frac{1}{\sigma} I\{1 < c < n\} I\{\sigma > 0\}$$

$$= \sigma^{-n-1} \exp\left[ -\frac{S(\boldsymbol{\beta}, c)}{2\sigma^2} \right] I\{1 < c < n\} I\{\sigma > 0\}$$

To get posterior for $c$ alone, need to integrate $\boldsymbol{\beta}$ ($\beta_0, \beta_1, \beta_2$) as well as $\sigma$.

$$S(\boldsymbol{\beta}, c) = \sum_{t=1}^n [y_t - \beta_0 - \beta_1 t - \beta_2(t-c)_+]^2$$

$$= \|y - X_c \boldsymbol{\beta}\|^2$$

$$y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}, \quad X_c = \begin{bmatrix} 1 & 1 & (1-c)_+ \\ 1 & 2 & (2-c)_+ \\ \vdots & \vdots & \vdots \\ 1 & n & (n-c)_+ \end{bmatrix}$$
$$\quad \downarrow$$
$$t, t=1, \dots, n$$

**Pythagorean Identity:**

---

$$\|y - X_c \boldsymbol{\beta}\|^2 = \|y - X_c \hat{\boldsymbol{\beta}}_c\|^2 + (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}_c)^T X_c^T X_c (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}_c)$$
$$S(\boldsymbol{\beta}, c) = S(\hat{\boldsymbol{\beta}}_c, c) + (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}_c)^T X_c^T X_c (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}_c)$$

$$S(\boldsymbol{\beta}, c) = RSS(c) + (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}_c)^T X_c^T X_c (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}_c)$$

$$\underset{\text{for all parameters}}{\text{posterior}} \propto \sigma^{-n-1} \exp\left[ -\frac{S(\boldsymbol{\beta}, c)}{2\sigma^2} \right] \begin{aligned} & I(\sigma > 0) \\ & I(c \in (1, n)) \end{aligned}$$

$$= \sigma^{-n-1} \exp\left[ -\frac{RSS(c)}{2\sigma^2} \right] \exp\left[ -\frac{(\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}_c)^T X_c^T X_c (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}_c)}{2\sigma^2} \right] I(\sigma > 0) I(1 < c < n)$$

**Formula:**
$$\int_{\mathbb{R}^p} \exp\left[ -\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu) \right] dx = (2\pi)^{p/2} \sqrt{\det \Sigma}$$
$$\Sigma = \sigma^2 (X_c^T X_c)^{-1}$$

$$\underset{\text{for } \sigma, c}{\text{posterior}} \propto \sigma^{-n-1} \exp\left[ -\frac{RSS(c)}{2\sigma^2} \right] (2\pi)^{p/2} \sqrt{\det(\sigma^2 (X_c^T X_c)^{-1})} I(\sigma > 0) I(1 < c < n)$$

$$\propto \sigma^{-n+p-1} |X_c^T X_c|^{-1/2} \exp\left[ -\frac{RSS(c)}{2\sigma^2} \right] I(\sigma > 0) I(1 < c < n)$$

$$\det(a \underset{p \times p}{A}) = a^p \det(A)$$

**posterior for $c$:** Integrate over $\sigma$:

---

$$\propto \int_0^\infty \sigma^{-n+p-1} |X_c^T X_c|^{-1/2} \exp\left( -\frac{RSS(c)}{2\sigma^2} \right) d\sigma \, I(1 < c < n)$$

$$\propto |X_c^T X_c|^{-1/2} I(1 < c < n) \int_0^\infty \sigma^{-n+p-1} \exp\left( -\frac{RSS(c)}{2\sigma^2} \right) d\sigma$$

$$\propto |X_c^T X_c|^{-1/2} \left( \frac{1}{RSS(c)} \right)^{\frac{n-p}{2}} I(1 < c < n)$$

$$\int_0^\infty \sigma^{-n-1} \exp\left( -\frac{S(\beta)}{2\sigma^2} \right) d\sigma \propto \left( \frac{1}{S(\beta)} \right)^{\frac{n}{2}}$$
$$\text{change of variable } \frac{\sigma}{\sqrt{S(\beta)}} = t$$

$p$ : # columns in $X_c$
(In our case, $p=3$)

$$\text{posterior of } c \propto \underbrace{|X_c^T X_c|^{-1/2}}_{} \left( \frac{1}{RSS(c)} \right)^{\frac{n-p}{2}} I(1 < c < n)$$

$$X_c = \begin{bmatrix} 1 & 1 & (1-c)_+ \\ 1 & 2 & \vdots \\ \vdots & \vdots & \vdots \\ 1 & n & (n-c)_+ \end{bmatrix}$$

$$\text{If } c=0 : \quad \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ \vdots & \vdots & \vdots \\ 1 & n & n \end{bmatrix}$$

$$I(2 \le c \le n-1)$$
$$c \in [2, n-1]$$

---

(1) Take a grid of values of $c$ in $[2, n-1]$

(2) For each $c$ in the grid, calculate
$$|X_c^T X_c|^{-1/2} \left( \frac{1}{RSS(c)} \right)^{\frac{n-p}{2}}$$
This gives the unnormalized posterior

```
        4.5|  5|  |8.5
           |   |  |
      -----+---+--+-----
          64  65  66
```

(3) Normalize these values.
$$\mathbb{P}(c = 65 \mid \text{data}) \quad \mathbb{P}(c = 65.05 \mid \text{data})$$

---

$$y_t = \beta_0 + \beta_1 t + \beta_2 (t-c_1)_+ + \beta_3 (t-c_2)_+ + \varepsilon_t$$

$$RSS(c_1, c_2) = \min_{\boldsymbol{\beta}} \|y - X_{c_1, c_2} \boldsymbol{\beta}\|^2$$

$$\underset{(c_1, c_2)}{\text{posterior}} \propto |X_{c_1, c_2}^T X_{c_1, c_2}|^{-1/2} \left( \frac{1}{RSS(c_1, c_2)} \right)^{\frac{n-p}{2}}$$

$$p = 4$$

---

[Up: contents](index.md)
