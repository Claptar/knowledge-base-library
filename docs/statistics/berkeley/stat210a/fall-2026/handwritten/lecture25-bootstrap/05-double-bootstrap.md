---
title: Double Bootstrap
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture25-bootstrap.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture25-bootstrap.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture25-bootstrap.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture25-bootstrap.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Double Bootstrap

We might have theory that tells us, e.g.
$$\sup_{a < b} |G_{n, \hat{P}_n}([a, b]) - G_{n, P}([a, b])| \overset{P}{\to} 0$$
but still be worried about finite-sample coverage.

Let $\gamma_{n, P}(\alpha) = \mathbb{P}_P(C_{n, \alpha} \ni \theta(P))$
$$\to 1 - \alpha \quad \text{if } C_{n, \alpha} \text{ has asy. coverage}$$

But in finite samples, might have
$$\gamma_{n, P}(\alpha) < 1 - \alpha$$
e.g., "90% interval" has 87% coverage
$$\gamma_{n, P}(0.1) = 0.87 < 0.9$$

**Solution?** **Double Bootstrap!**

1. Estimate $\gamma_{n, P}(\cdot)$ via plug-in $\gamma_{n, \hat{P}_n}(\cdot)$
2. Use $C_{n, \hat{\alpha}}(X)$ where $\hat{\gamma}(\hat{\alpha}) = 1 - \alpha$
e.g., estimate "92% interval" has 90% coverage $\implies \hat{\alpha} = .08$

---

**Step 1 algo.**

For $a = 1, \dots, A$:
$$\begin{array}{|l}
X_1^{*a}, \dots, X_n^{*a} \overset{iid}{\sim} \hat{P}_n \\
\hat{P}_n^{*a} = \frac{1}{n} \sum_{i=1}^n \delta_{X_i^{*a}} \\
\text{For } b = 1, \dots, B: \\
\begin{array}{|l}
X_1^{**a, b}, \dots, X_n^{**a, b} \overset{iid}{\sim} \hat{P}_n^{*a} \\
R_n^{**a, b} = \left(\hat{\theta}_n(X^{**a, b}) - \theta(\hat{P}_n^{*a})\right) / \hat{\sigma}(X^{**a, b})
\end{array} \\
\hat{G}_n^{*a} = \text{ecdf}(R_n^{**a, 1}, \dots, R_n^{**a, B}) \\
\text{For } \alpha \in \text{grid}: \\
\begin{array}{|l}
C_{n, \alpha}^{*a} = \left[\hat{\theta}_n^{*a} - \hat{\sigma}^{*a} \cdot r_2(\hat{G}_n^{*a}), \, \hat{\theta}_n^{*a} - \hat{\sigma}^{*a} \cdot r_1(\hat{G}_n^{*a})\right]
\end{array}
\end{array}$$

For $\alpha \in \text{grid}$:
$$\hat{\gamma}(\alpha) = \frac{1}{A} \sum_a \mathbf{1}\{C_{n, \alpha}^{*a} \ni \theta(\hat{P}_n)\}$$

$$\hat{\alpha} = \hat{\gamma}^{-1}(1 - \alpha)$$

---

[← Bootstrap Confidence Interval](04-bootstrap-confidence-interval.md) · [Up: contents](index.md)
