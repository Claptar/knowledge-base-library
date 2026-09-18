---
title: 6 Determination of the order $p$ of AR($p$)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 6 Determination of the order $p$ of AR($p$)

How to determine the correct order $p$ for fitting the $\text{AR}(p)$ model? For this, one commonly uses a quantity called the sample PACF (PACF stands for Partial AutoCorrelation Function).

The sample PACF is defined as follows: for $h \ge 1$,
$$\text{sample PACF}(h) = \text{estimate } \hat{\phi}_h \text{ of } \phi_h \text{ when } \text{AR}(h) \text{ is fit to the data}$$

If the $\text{sample PACF}(h)$ becomes negligibly small after a particular $p$, this suggests that $\text{AR}(p)$ is a good model for the data. This method is similar to the heuristic technique that we used in Lab 9 for selecting the order $p$ to fit $\text{AR}(p)$. There we were looking at the uncertainty interval for $\phi_p$ to see if it contains zero when $\text{AR}(p)$ is fit to the data. This is the same as checking whether the $\text{sample PACF}(h)$ is small at $h = p$.

It can happen (we will see examples of this later) that the $\text{sample PACF}(h)$ for $h = 1, 2, \dots, 11$ are all negligible but at $h = 12$, it is nonnegligible. In that case, we would be using $\text{AR}(12)$. More specifically, we will use that value of $p$ for which $\text{sample PACF}(h)$ is negligible for all $h > p$.

Why should the quantity $\hat{\phi}_h$ (obtained by fitting $\text{AR}(h)$ to the data) be called the Sample Partial Autocorrelation? We will understand this in the next lecture.

---

[← 5 AR(p) for $p \ge 1$](05-5-ar-p-for.md) · [Up: contents](index.md)
