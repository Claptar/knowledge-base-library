---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture19-asymptotics.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture19-asymptotics.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture19-asymptotics.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture19-asymptotics.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) **Convergence in Probability and Distribution**

2) **Continuous Mapping, Slutsky's Theorem**

3) **Delta method**

---

## Example

### Logistic Regression (fixed design)

$(x_i, y_i)$ pairs $\quad i = 1, \dots, n$

* $x_i \in \mathbb{R}^d$ Continuous feature vector, fixed ($x_{i,1} = 1$ for intercept)
* $Y_i \stackrel{\text{ind.}}{\sim} \text{Bern.}(\pi_\beta(x_i))$
* $\text{logit}(\pi_\beta(x_i)) = \log \frac{\pi_\beta}{1 - \pi_\beta} = \beta' x_i$

\$\$
\begin{aligned}
p_\beta(y \mid x) &= \prod_{i=1}^n \pi_\beta(x_i)^{y_i} (1 - \pi_\beta(x_i))^{1 - y_i} \\
&= \prod_{i=1}^n e^{(\beta' x_i) y_i + \log(

---

[Up: contents](../index.md)
