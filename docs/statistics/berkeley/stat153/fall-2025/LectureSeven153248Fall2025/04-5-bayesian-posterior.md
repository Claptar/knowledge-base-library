---
title: 5 Bayesian Posterior
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 Bayesian Posterior

For Bayesian inference, we need to select the prior on $\beta, \sigma$ and $f$. For $\beta$ and $\sigma$, we shall use, as usual:
$$\beta_0, \beta_1, \beta_2, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C).$$
For $f$, we shall use:
$$f \sim \text{unif}[0, 1/2]$$
because, as seen in Section 3, we know we can restrict $f$ to $[0, 1/2]$.

This will let us write the joint posterior of all the parameters $\beta, \sigma, f$, and then we integrate out $\beta$ and $\sigma$ to deduce the posterior of $f$. This calculation is exactly the same as in the last lecture when we studied the change of slope model; the only difference being that $c$ there is now replaced by $f$ (also the indicator $I\{1 < c < n\}$ should be replaced by $I\{0 \le f \le 1/2\}$). The posterior for $f$ will be given by:
$$\text{posterior}(f) \propto I\{0 \le f \le 1/2\} |X_f^T X_f|^{-1/2} \left( \frac{1}{RSS(f)} \right)^{(n-p)/2}.$$
Thus psoterior will be evaluated numerically over a grid of values of $f$ in the range $[0, 0.5]$. The term $|X_f^T X_f|^{-1/2}$ becomes infinite when $|X_f^T X_f| = 0$ i.e., when $X_f$ does not have full column rank. This will be the case when $f = 0$ or $f = 1/2$. We will exclude these edge cases while computing this posterior:
$$\text{posterior}(f) \propto I\{0 < f < 1/2\} |X_f^T X_f|^{-1/2} \left( \frac{1}{RSS(f)} \right)^{(n-p)/2}. \tag{4}$$

---

[← 3 Discrete sampling and restricting $f$ to $[0, 1/2]$](03-3-discrete-sampling-and-restricting-to.md) · [Up: contents](index.md) · 6 Efficient Computation of $RSS(f)$ →
