---
title: Example (Binomial)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture12-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture12-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Example (Binomial)

$X \sim \text{Binom}(n, \theta)$, estimate $\theta$, sq. err.

Try $\text{Beta}(\alpha, \beta)$, hope to get one with const. risk

$$\delta_{\alpha, \beta}(X) = \frac{\alpha + X}{\alpha + \beta + n}$$

$$\begin{aligned}
R(\theta; \delta_{\alpha, \beta}(X)) &= \mathbb{E}_\theta \left[ \left( \frac{\alpha + X}{\alpha + \beta + n} - \theta \right)^2 \right] \\
&= \text{Var}_\theta \left( \frac{X}{\alpha + \beta + n} \right) + \left( \frac{\alpha + \theta n}{\alpha + \beta + n} - \theta \right)^2 \\
&= (\alpha + \beta + n)^{-2} \cdot \left[ n\theta(1 - \theta) + (\alpha - (\alpha + \beta)\theta)^2 \right] \\
&\propto_\theta \underbrace{\left[ (\alpha + \beta)^2 - n \right]}_{\text{Set } = 0} \theta^2 + \underbrace{\left[ n - 2\alpha(\alpha + \beta) \right]}_{\text{Set } = 0} \theta + \alpha^2
\end{aligned}$$

Set $(\alpha + \beta)^2 = n$, $2\alpha(\alpha + \beta) = n$

$\Rightarrow \alpha + \beta = \sqrt{n} \Rightarrow 2\alpha\sqrt{n} = n$

$\Rightarrow \alpha = \beta = \sqrt{n}/2$

$\Rightarrow \text{Beta}\left(\frac{\sqrt{n}}{2}, \frac{\sqrt{n}}{2}\right)$ is LF

$\frac{X + \sqrt{n}/2}{n + \sqrt{n}}$ is minimax $\checkmark$ We got lucky!

Question: why so much prior wt. on $\theta = 1/2$?

---

---

[← Theorem](02-theorem.md) · [Up: contents](index.md) · [Least Favorable Sequence →](04-least-favorable-sequence.md)
