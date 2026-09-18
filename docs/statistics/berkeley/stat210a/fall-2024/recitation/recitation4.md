---
title: Projection Matrix.
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/recitation/recitation4.pdf
source_file: sources/berkeley-stat210a/fall-2024/recitation/recitation4.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`recitation/recitation4.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/recitation/recitation4.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Projection Matrix.

$$X = \begin{pmatrix} X^1, \cdots, X^d \end{pmatrix} : n \times d \text{ matrix}, \quad (d \le n)$$
$$\in \mathbb{R}^n$$

$$\text{Col}(X) = \text{span}\{X^1, \cdots, X^d\} \le \mathbb{R}^n$$
$$= \left\{ \sum_{j=1}^d \beta_j X^j \;\middle|\; \beta_1, \dots, \beta_d \in \mathbb{R} \right\}$$
$$= \{X\beta \mid \beta \in \mathbb{R}^d\}$$

Consider $\Pi_X := X(X^t X)^{-1} X^t$

(assume $X^1 \sim X^d$ are lin. indep. so that $X^t X$ is full rank)

## Observations

(1) $\Pi_X \cdot X = X(X^t X)^{-1} X^t X = X$, $\quad X^t \Pi_X = X^t$

(1)-1 $\Pi_X \cdot X^j = X^j$ for $j = 1, 2, \cdots, d$

(1)-2 $\forall v \in \text{Col}(X), \quad \Pi_X v = v$

(2) $\Pi_X^2 = X(X^t X)^{-1} X^t \cdot X(X^t X)^{-1} X^t = \Pi_X$

(2)-1 $(I - \Pi_X)^2 = I - 2\Pi_X + \Pi_X^2 = I - \Pi_X$

(3) $\forall v \in \mathbb{R}^n, \quad \Pi_X v = X\left( (X^t X)^{-1} X^t v \right) \in \text{Col}(X)$
$$X^t(I - \Pi_X) v = 0 \implies (I - \Pi_X)v \in (\text{Col}(X))^\perp$$

(4) $\text{tr}(\Pi_X) = \text{tr}\left( X(X^t X)^{-1} X^t \right)$
$$= \text{tr}\left( (X^t X)^{-1} X^t X \right) = \text{tr}(I_d) = d$$
$$\implies \text{tr}(I - \Pi_X) = \text{tr}(I_n) - \text{tr}(\Pi_X) = n - d$$

---

$$v = (I - \Pi_X + \Pi_X) v$$
$$= \Pi_X v + (I - \Pi_X) v$$
$$\in \text{Col}(X) \quad \in (\text{Col}(X))^\perp$$

<!-- Diagram showing R^n space, Col(X) plane, vector Y, projection Pi_X Y on Col(X), and (I - Pi_X)Y orthogonal to Col(X) -->

$\therefore \Pi_X :$ projection matrix to column space of $X$

$I - \Pi_X :$ projection matrix to orthogonal complement of column space of $X$

$\checkmark$ if $X = \mathbb{1}_n = \underbrace{(1, \cdots, 1)^t}_{n \text{ times}} \in \mathbb{R}^{n \times 1}$

$$\implies \Pi_X = \mathbb{1} (\underbrace{\mathbb{1}^t \mathbb{1}}_{= n})^{-1} \mathbb{1}^t = \frac{1}{n} \begin{pmatrix} 1 & \cdots & 1 \\ \vdots & \ddots & \vdots \\ 1 & \cdots & 1 \end{pmatrix}$$

$$\implies \Pi_X Y = \begin{pmatrix} \bar{y} \\ \vdots \\ \bar{y} \end{pmatrix} = \mathbb{1}_n \cdot \bar{y} \qquad \left( \bar{y} = \frac{1}{n} \sum_{i=1}^n y_i \right)$$

$$& \; (I - \Pi_X) Y = Y - \Pi_X Y = (y_1 - \bar{y}, \cdots, y_n - \bar{y})^t$$

---

$\checkmark \quad X_1 \in \mathbb{R}^{n \times d_1}, \quad X_2 \in \mathbb{R}^{n \times d_2}$

$$\text{if } \text{Col}(X_1) \le \text{Col}(X_2), \quad \Pi_{X_2} \Pi_{X_1} = \Pi_{X_1} \Pi_{X_2} = \Pi_{X_1}$$

(pf) $\forall v \in \mathbb{R}^n \quad \Pi_{X_1} v \in \text{Col}(X_1) \le \text{Col}(X_2)$

$$\therefore \Pi_{X_2} (\Pi_{X_1} v) = \Pi_{X_1} v$$

$$\therefore \Pi_{X_2} \Pi_{X_1} = \Pi_{X_1},$$

$$\Pi_{X_2} \Pi_{X_1} = \Pi_{X_1} \Pi_{X_2} \text{ because } \Pi_{X_1} \Pi_{X_2} = \Pi_{X_1} \text{ is symmetric}$$

$\checkmark \quad \hat{\beta}_{\text{OLS}} = \text{argmin} \; \|y - X\beta\|_2^2 \qquad (X \text{ is full rank})$

$\cdot$ **vector calculus approach**

$$\|y - X\beta\|_2^2 = \beta^t X^t X \beta - 2 y^t X \beta + y^t y$$

$$\frac{\partial}{\partial \beta} \bigcirc = 2(X^t X)\beta - 2 X^t y$$

$$\frac{\partial^2}{\partial \beta^2} \bigcirc = 2(X^t X) > 0$$

$$\therefore \hat{\beta} \text{ solves } 2(X^t X)\beta - 2 X^t y = 0 \implies \hat{\beta}_{\text{OLS}} = (X^t X)^{-1} X^t y$$

---

$$\text{minimize } \|y - X\beta\|_2$$

$$\implies \text{find } X\beta \in \text{Col}(X) \text{ that has closest distance from } y$$

$$\therefore \text{orthogonal projection}$$

<!-- Diagram showing Col(X), vector Y, and its orthogonal projection Pi_X Y = X \hat{\beta} -->

$$\Pi_X y = X(X^t X)^{-1} X^t y = X\hat{\beta}$$

$\text{Statistical properties} : \text{next time}.$

$\circ$ **Hint for HW6 Pb 4.**

$$\delta^{\text{JS}}(Y) = \left( 1 - \frac{d-2}{\|Y\|_2^2} \right) Y \quad : \text{works well when } \theta = 0$$
$$\implies \theta \in \text{Col}(0)$$

$$\delta^{(1)}(Y) = \bar{Y} \mathbb{1}_d + \left( 1 - \frac{d-3}{\|Y - \bar{Y}\mathbb{1}_d\|_2^2} \right) (Y - \bar{Y})$$

$$: \text{will work well when } \theta_1 = \cdots = \theta_d$$
$$\implies \theta \in \text{Col}(\mathbb{1}_d)$$

$$\delta^{(2)}(Y) = ??, \quad \text{want to work well when } \theta = X\beta \in \text{Col}(X)$$

---

$$\delta^{\text{JS}} : \quad Y = \underset{\in \text{Col}(0)}{0} + \underset{\in (\text{Col}(0))^\perp}{Y}$$

$$\delta^{\text{JS}} = 0 + (1 - \alpha) Y$$

$$\delta^{(1)} : \quad Y = \underset{\in \text{Col}(\mathbb{1})}{\Pi_{\mathbb{1}} Y} + \underset{\in (\text{Col}(\mathbb{1}))^\perp}{(I - \Pi_{\mathbb{1}}) Y}$$

$$\delta^{(1)} = \Pi_{\mathbb{1}} Y + (1 - \alpha)(I - \Pi_{\mathbb{1}}) Y$$

$\implies$ we are leaving orthogonal projection part the same

and shrinking orthogonal complement part

what next??

---

[Up: contents](../index.md)
