---
title: 5. Conclusions
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf
source_file: sources/berkeley-stat243/fall-2024/project/gilks.etal.1992.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`project/gilks.etal.1992.pdf`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5. Conclusions

We have shown that adaptive rejection sampling can be used as a black box routine for efficiently sampling from complex densities, in particular those arising in applications of Gibbs sampling to the analysis of hierarchical Bayesian models involving non-conjugacy. In the context of Gibbs sampling, we suggest the use of centiles from the sampling density $s(x)$ from one iteration to provide starting abscissae for the next iteration, as described in Section 4.

Although adaptive rejection sampling is conceptually simple, care must be taken in its implementation to avoid numerical problems when sampling from densities which are extremely concentrated or skewed. We have written a Fortran program (available on request) to perform adaptive rejection sampling, which behaves well under

TABLE 3
*Posterior summaries based on iterations 11–1000 of the Gibbs sampler for model (7)–(13)*

| Parameter | Mean | Standard deviation | 5th centile | 95th centile |
| :--- | :--- | :--- | :--- | :--- |
| $\tau_1$ | 0.13 | 0.05 | 0.06 | 0.21 |
| $\tau_2$ | 1.59 | 0.55 | 0.80 | 2.65 |
| $\tau_y$ | 0.87 | 0.04 | 0.81 | 0.93 |
| $\sigma_1 = 1/\sqrt{\tau_1}$ | 2.95 | 0.56 | 2.19 | 4.02 |
| $\sigma_2 = 1/\sqrt{\tau_2}$ | 0.83 | 0.16 | 0.61 | 1.11 |
| $\sigma_y = 1/\sqrt{\tau_y}$ | 1.07 | 0.02 | 1.04 | 1.11 |
| $\beta_{2,1}$ | 0.23 | 0.37 | $-0.39$ | 0.85 |
| $\beta_{2,2}$ | 0.03 | 0.39 | $-0.62$ | 0.63 |
| $\beta_{2,3}$ | 0.42 | 0.38 | $-0.21$ | 1.06 |
| $\beta_{2,4}$ | 0.06 | 0.36 | $-0.52$ | 0.60 |
| $\beta_{2,5}$ | $-0.15$ | 0.37 | $-0.75$ | 0.44 |
| $\beta_{2,6}$ | $-0.26$ | 0.36 | $-0.83$ | 0.34 |
| $\beta_{2,7}$ | $-0.04$ | 0.36 | $-0.64$ | 0.53 |
| $\beta_{2,8}$ | 0.06 | 0.37 | $-0.54$ | 0.72 |
| $\beta_{2,9}$ | $-0.26$ | 0.37 | $-0.37$ | 0.88 |
| $\beta_{2,10}$ | $-0.13$ | 0.36 | $-0.69$ | 0.46 |
| $\beta_{2,11}$ | 0.21 | 0.36 | $-0.39$ | 0.78 |
| $\beta_{2,12}$ | $-0.66$ | 0.36 | $-1.27$ | $-0.09$ |
| $\beta_{2,13}$ | 0.10 | 0.37 | $-0.50$ | 0.74 |

extreme conditions. In particular, this algorithm can be used straightforwardly to sample from truncated distributions.

## Acknowledgements

We are grateful to Professor Peter Beverley for permitting us the use of data from the Second International Workshop on Small-cell Lung Cancer Antigens, and to referees for drawing our attention to the work of Devroye (1986).

---

[← 4. Application to Monoclonal Antibody Reactivity](05-4-application-to-monoclonal-antibody-reactivity.md) · [Up: contents](index.md) · [References →](07-references.md)
