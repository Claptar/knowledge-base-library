---
title: One-sample T-test
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture18-linearmodel.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture18-linearmodel.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture18-linearmodel.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture18-linearmodel.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# One-sample T-test

1) $\chi^2$, $t$ and $F$ distributions
2) Canonical linear model
3) General linear model

---

## "Gaussian-adjacent" distributions

If $Z_1, \dots, Z_d \overset{\text{iid}}{\sim} N(0, 1)$ then

$$V = \sum Z_i^2 \sim \chi_d^2 = \text{Gamma}(\overset{\text{shape}}{d/2}, \overset{\text{scale}}{2})$$

$$\mathbb{E}V = d, \quad \text{Var}(V) = 2d$$

$$\text{CLT}: \frac{V - d}{\sqrt{2d}} \Rightarrow N(0, 1)$$

$$(\text{informal}) \quad \frac{V}{d} \approx N\left(1, \frac{2}{\sqrt{d}}\right) \to 1$$

If $Z \sim N(0, \sigma^2 \cdot 1)$ and $V \sim \sigma^2 \chi_d^2$, $Z \perp\!\!\!\perp V$ then

$$\frac{Z}{\sqrt{V/d}} \sim t_d \Rightarrow N(0, 1) \quad \text{as } d \to \infty$$

If $V_1 \sim \sigma^2 \chi_{d_1}^2$ and $V_2 \sim \sigma^2 \chi_{d_2}^2$, $V_1 \perp\!\!\!\perp V_2$ then

$$\frac{V_1/d_1}{V_2/d_2} \sim F_{d_1, d_2} \Rightarrow \frac{1}{d_1}\chi_{d_1}^2 \quad \text{as } d_2 \to \infty$$

**Note** if $T \sim t_d$ then $T^2 \sim F_{1, d}$

Recall: $Z \sim N_d(\mu, \Sigma)$, $A \in \mathbb{R}^{k \times d}$, $b \in \mathbb{R}^k$
$$\Rightarrow AZ + b \sim N_k(A\mu + b, A\Sigma A')$$

---

$$X_i \overset{\text{iid}}{\sim} N(\mu, \sigma^2) \Leftrightarrow X \sim N_n(\mu \cdot \mathbf{1}_n, \sigma^2 I_n)$$

$$H_0 : \mu = 0 \quad \text{vs} \quad H_1 : \mu \neq 0$$

UMPU test: Reject for extreme $R = \overset{"\text{corr}(X, \mathbf{1}_n)"}{\frac{\sqrt{n}\,\bar{X}}{\|X\|}}$

```
                   X_2 ^
                       |             / X_1 = X_2
                       |            /
                       |    |\     /
                       |    | \   /
                       |    |  \ /
                       |    |   * X
                       |    |  /
                       |    | /
        ---------------+----+----------------> X_1
                       |   /
                       |  /
                       | /
                       |/
```
*(Vector diagram shows vector $X$, projected onto $\mathbf{1}_n$ giving $\sqrt{n}\,\bar{X} = \|\text{Proj}_{\mathbf{1}_n} X\|$, and projected onto $\mathbf{1}_n^\perp$ giving $\sqrt{(n-1)S^2} = \|\text{Proj}_{\mathbf{1}_n}^\perp X\|$, angle $\measuredangle(\mathbf{1}_n, X)$, and length $\|X\|$)*

$$T = \frac{\sqrt{n}\,\bar{X}}{\sqrt{S^2}} = \frac{\|\text{Proj}_{\mathbf{1}_n} X\|}{\|\text{Proj}_{\mathbf{1}_n}^\perp X\|} \cdot \sqrt{n-1}\;\text{sgn}(\bar{X}) = \frac{R}{\sqrt{1 - R^2}}$$

---

## Change of basis (1-sample t-test)

Let $Q = \begin{pmatrix} q_1 & q_2 & \cdots & q_n \end{pmatrix} = {}_n\begin{pmatrix} \overset{1}{q_1} & \overset{n-1}{Q_r} \end{pmatrix}$

where $q_1 = \frac{1}{\sqrt{n}} \cdot \mathbf{1}_n$,

$q_2, \dots, q_n$ complete orthonormal basis (e.g. via Gram-Schmidt)

New basis:
$$Z = Q'X = {}_{n-1}^1\begin{pmatrix} q_1' X \\ Q_r' X \end{pmatrix} = \begin{pmatrix} \sqrt{n}\,\bar{X} \\ Q_r' X \end{pmatrix}$$

$$\|Q_r' X\|^2 = \|Q' X\|^2 - \|q_1' X\|^2$$
$$= \|X\|^2 - n\bar{X}^2 \qquad (Q'Q = I_n)$$
$$= (n-1)S^2$$

$$Q'X \sim N_n\left(\begin{pmatrix} \sqrt{n}\,\mu \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \; \sigma^2 I_n\right)$$

$$Z_1 \sim N(\sqrt{n}\,\mu, \sigma^2)$$

$$Z_r = Q_r' X \sim N(0, \sigma^2 I_{n-1})$$

$$\Rightarrow S^2 = \frac{1}{n-1}\|Z_r\|^2 \sim \frac{\sigma^2}{n-1}\chi_{n-1}^2$$

and $S^2 \perp\!\!\!\perp Z_1$ (we already knew, from Basu)

---

## Geometric interp.

$$T^2 = \frac{n\bar{X}^2}{S^2} = \frac{\|\text{Proj}_{\mathbf{1}_n} X\|^2}{\frac{1}{n-1}\|\text{Proj}_{\mathbf{1}_n}^\perp X\|^2} \sim F_{1, n-1}$$

$$= \frac{(\text{magnitude of } X \text{ in special dir.})^2}{(\text{average magn. of } X \text{ in resid. dir.s})^2}$$

Independent of total magnitude (under $H_0$):

$$n\bar{X}^2 \overset{H_0}{\sim} \sigma^2 \chi_1^2 = \text{Gamma}\left(\frac{1}{2}, \, 2\sigma^2\right)$$

$$(n-1)S^2 \sim \sigma^2 \chi_{n-1}^2 = \text{Gamma}\left(\frac{n-1}{2}, \, 2\sigma^2\right)$$

$$\|X\|^2 = n\bar{X}^2 + (n-1)S^2 \overset{H_0}{\sim} \sigma^2 \chi_n^2 = \text{Gamma}\left(\frac{n}{2}, \, 2\sigma^2\right)$$

$$\Rightarrow \overset{"\frac{n\bar{X}^2}{n\bar{X}^2 + (n-1)S^2}"}{\frac{n\bar{X}^2}{\|X\|^2}} \sim \text{Beta}\left(\frac{1}{2}, \, \frac{n-1}{2}\right), \quad \text{indep. of } \|X\|^2$$

$F_{d_1, d_2}$ related to $\text{Beta}\left(\frac{d_1}{2}, \frac{d_2}{2}\right)$: If $U \sim \text{Beta}\left(\frac{d_1}{2}, \frac{d_2}{2}\right)$
$$\text{Then } \frac{U/d_1}{(1-U)/d_2} \sim F_{d_1, d_2}$$

---

---

[Up: contents](index.md) · [Canonical Linear Model →](02-canonical-linear-model.md)
