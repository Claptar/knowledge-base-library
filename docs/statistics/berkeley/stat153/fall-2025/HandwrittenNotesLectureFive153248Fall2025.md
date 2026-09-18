---
title: LECTURE FIVE
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureFive153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFive153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# LECTURE FIVE

## Multiple Linear Regression

**Data:** $y_i \quad x_{i1} \quad x_{i2} \quad \cdots \quad x_{im}, \quad i = 1, \dots, n$

**Model:** $y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_m x_{im} + \varepsilon_i$
$$\varepsilon_i \overset{\text{iid}}{\sim} N(0, \sigma^2)$$

**Inference:** **Prior:** $\beta_0, \dots, \beta_m, \log \sigma \overset{\text{iid}}{\sim} \text{Unif}(-C, C)$

**Posterior:**
$$f(\beta_0, \dots, \beta_m \mid \text{data}) \propto \left[ \frac{S(\hat{\beta}_0, \dots, \hat{\beta}_m)}{S(\beta_0, \dots, \beta_m)} \right]^{\frac{n}{2}} \quad \text{peaked at the least squares estimator}$$

\$\$S(\beta_0, \dots, \beta_m) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1}

---

[Up: contents](index.md)
