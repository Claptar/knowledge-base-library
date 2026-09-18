---
title: 3 Spectrum Model from DFT
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Spectrum Model from DFT

In (1) or (2), we formulated the spectrum model in terms of the periodogram or log-periodogram. We can also describe it in terms of the DFT. Specifically, in terms of the DFT $b_0, \dots, b_{n-1}$ of the data $y_0, \dots, y_{n-1}$, the model is given by:
$$\text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2) \tag{3}$$
for $j = 1, \dots, m$ where $m = (n-1)/2$ (we are assuming that $n$ is odd). The unknown parameters in this model are $\gamma_1^2, \dots, \gamma_m^2$ and $\gamma_j$ represents the strength of sinusoids at frequency $j/n$.

By definition of the periodogram, we get
$$I(j/n) := \frac{|b_j|^2}{n} = \frac{1}{n} \left((\text{Re}(b_j))^2 + (\text{Im}(b_j))^2\right) = \frac{2\gamma_j^2}{n} \frac{1}{2} \left( \left(\frac{\text{Re}(b_j)}{\gamma_j}\right)^2 + \left(\frac{\text{Im}(b_j)}{\gamma_j}\right)^2 \right).$$
By the assumption (3), we get
$$\eta_j := \left( \left(\frac{\text{Re}(b_j)}{\gamma_j}\right)^2 + \left(\frac{\text{Im}(b_j)}{\gamma_j}\right)^2 \right) \overset{\text{i.i.d}}{\sim} \chi_2^2.$$
Therefore the model (3) implies that
$$I(j/n) = \frac{2\gamma_j^2}{n} \eta_j \quad \text{with } \eta_j \overset{\text{i.i.d}}{\sim} \frac{\chi_2^2}{2} = \text{Exp}(1).$$
The is exactly the same as (1) with the identification:
$$f(j/n) = \frac{2\gamma_j^2}{n}.$$
Because of this equivalence, we shall treat (3) as another formulation of the spectrum model.

---

[← 1 Smoothing the Periodogram](01-1-smoothing-the-periodogram.md) · [Up: contents](index.md) · [4 Rewriting the Model in terms of $yt$ →](03-4-rewriting-the-model-in-terms-of.md)
