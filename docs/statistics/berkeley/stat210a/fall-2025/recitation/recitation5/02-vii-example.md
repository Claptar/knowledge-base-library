---
title: VII Example
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation/recitation5.pdf
source_file: sources/berkeley-stat210a/fall-2025/recitation/recitation5.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`recitation/recitation5.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation/recitation5.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# VII Example

$$Y = X\beta + \varepsilon \qquad \varepsilon \sim N(0, \sigma^2 I)$$

$$H_0 : \beta_1 = \cdots = \beta_k = 0$$

$$H_1 : \text{not } H_0$$

$$SSM = \sum_{i=1}^n (\hat{y}_i - \bar{y})^2$$

$$SST = \sum_{i=1}^n (y_i - \bar{y})^2$$

$$SSE = \sum_{i=1}^n (y_i - \hat{y}_i)^2$$

under $H_0$,
$$\ell(\beta, \sigma^2; Y, X) = -\frac{n}{2}\log 2\pi\sigma^2 - \frac{\|y - \beta_0 \mathbb{1}\|_2^2}{2\sigma^2}$$
is maximized when $\hat{\beta}_0 = \bar{y}$, $\hat{\sigma}^2 = \frac{\|y - \bar{y}\mathbb{1}\|_2^2}{n}$
$$\therefore \max_{H_0} \ell(\beta, \sigma^2 \mid Y, X) = -\frac{n}{2}\left(1 + \log 2\pi/n + \log \underbrace{\|y - \bar{y}\mathbb{1}\|_2^2}_{SST}\right)$$

under $H_1$,
$$\ell(\beta, \sigma^2; Y, X) \text{ is maximized when } \hat{\beta} = \hat{\beta}_{OLS} = (X^T X)^{-1} X^T y$$
$$\hat{\sigma}^2 = \frac{\|y - X\hat{\beta}\|_2^2}{n}$$
$$\text{and } \max_{H_1} \ell(\beta, \sigma^2 \mid Y, X) = -\frac{n}{2}\left(1 + \log \frac{2\pi}{n} + \log \underbrace{\|y - X\hat{\beta}\|_2^2}_{SSE}\right)$$

$\therefore$ maximum likelihood ratio test
$$= \text{reject when } \log SST/SSE \text{ is large.}$$

let $\Pi_1 = \mathbb{1}(\mathbb{1}^T\mathbb{1})^{-1}\mathbb{1}^T \quad :\text{rk } 1$
$\Pi_X = X(X^TX)^{-1}X^T \quad :\text{rk } k+1$

$$SST = \|y - \bar{y}\mathbb{1}\|_2^2 = \|(I - \Pi_1)y\|_2^2 = y^T(I - \Pi_1)y$$
$$SSE = \|y - X\hat{\beta}\|_2^2 = \|(I - \Pi_X)y\|_2^2 = y^T(I - \Pi_X)y$$
$$SSM = \|X\hat{\beta} - \bar{y}\mathbb{1}\|_2^2 = \|(\Pi_X - \Pi_1)y\|_2^2 = y^T(\Pi_X - \Pi_1)y$$

$\therefore SST = SSE + SSM$.

$$\therefore \text{m.l.r } \iff \text{reject when } \frac{SSM/k}{SSE/(n-k-1)} \text{ is large}$$

$$(I - \Pi_X)y = (I - \Pi_X)(X\beta + \varepsilon) = (I - \Pi_X)\varepsilon$$
$$\therefore \frac{SSE}{\sigma^2} \sim \mathcal{X}^2(n-k-1)$$

$$(\Pi_X - \Pi_1)y = (X - \Pi_1 X)\beta + (\Pi_X - \Pi_1)\varepsilon$$
$$\therefore \frac{SSM}{\sigma^2} \sim \mathcal{X}^2(k; \nu) \quad \text{for some } \nu \quad (\nu = 0 \text{ when } H_0)$$

also $(I - \Pi_X)(\Pi_X - \Pi_1) = 0 \quad \therefore SSE \perp SSM$

$$\text{thus } \frac{SSM/k}{SSE/(n-k-1)} \sim F(k, n-k-1; \nu)$$

level $\alpha$ - MLR :
$$\text{reject when } \frac{SSM/k}{SSE/(n-k-1)} > F_\alpha(k, n-k-1)$$

---

[← VII Chi-Square Distributions](01-vii-chi-square-distributions.md) · [Up: contents](index.md)
