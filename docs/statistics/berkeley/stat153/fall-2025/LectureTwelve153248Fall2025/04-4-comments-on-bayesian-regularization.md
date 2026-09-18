---
title: 4 Comments on Bayesian Regularization
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Comments on Bayesian Regularization

In practice, the posterior $f_{\tau,\sigma \mid \text{data}}(\tau, \sigma)$ tends to prefer $\tau$ values which are neither too small nor too large. Because
$$f_{\tau,\sigma \mid \text{data}}(\tau, \sigma) \propto f_{\text{data} \mid \tau,\sigma}(\tau, \sigma) f_{\tau,\sigma}(\tau, \sigma),$$

and the prior $f_{\tau,\sigma}(\tau, \sigma)$ is quite flat, the likelihood $f_{\text{data} \mid \tau,\sigma}(\tau, \sigma)$ must prefer values of $\tau$ which are neither too small nor too large. Note that there is a big difference between the two likelihoods:
$$f_{\text{data} \mid \beta,\sigma}(\text{data}) \quad \text{and} \quad f_{\text{data} \mid \tau,\sigma}(\text{data}).$$

Maximizing $f_{\text{data} \mid \beta,\sigma}(\text{data})$ leads to the unregularized least squares estimate which leads to overfitting. On the other hand, maximizing $f_{\text{data} \mid \tau,\sigma}(\text{data})$ often leads to a fairly small estimate of $\hat{\tau}$ leading to a smooth trend function. The reason for this discrepancy can be understood by noting that
$$f_{\text{data} \mid \tau,\sigma}(\text{data}) = \int f_{\text{data} \mid \beta,\sigma}(\text{data}) f_{\beta \mid \tau}(\beta) d\beta.$$

When $\tau$ is large, the term $f_{\beta \mid \tau}(\beta)$ will be small simply because the normal density with variance $\tau^2$ will be flat for large $\tau$. On the other hand, when $\tau$ is too small, the weight $f_{\beta \mid \tau}(\beta)$ will be significant only for very smooth $\beta$s but these $\beta$s will have poor values for $f_{\text{data} \mid \beta,\sigma}(\text{data})$.

---

[← 3 Bayesian approach for dealing with unknown $\tau$ and $\sigma$](03-3-bayesian-approach-for-dealing-with-unknown-and.md) · [Up: contents](index.md)
