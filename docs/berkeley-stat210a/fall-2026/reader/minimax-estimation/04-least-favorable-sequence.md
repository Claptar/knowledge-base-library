---
title: Least Favorable Sequence
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Least Favorable Sequence

**Source:** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Sometimes there is no least favorable prior, because $\sup_\Lambda r_\Lambda$ is not attainable, but a sequence $\Lambda_1,\Lambda_2,\ldots$ is least favorable in the sense defined above, that $\lim_n r_{\Lambda_n} = \sup_\Lambda r_\Lambda$.

**Theorem:** Suppose $\delta$ is an estimator and $\Lambda_1,\Lambda_2,\ldots$ is a sequence of priors such that
$$
\sup_\theta R(\theta;\delta) = \lim_{n\to\infty} r_{\Lambda_n}.
$$
Then $\delta$ is minimax, the sequence is least favorable, and $r^* = \lim_n r_{\Lambda_n}$.

*Proof:* Our proof follows the same structure as our previous theorem. For another estimator $\tilde\delta$, and any $n$,
$$
\begin{aligned}
\sup_\theta R(\theta;\tilde\delta)
&\geq \int R(\theta; \tilde\delta)\,d\Lambda_n(\theta)\\
&\geq r_{\Lambda_n}
\end{aligned}
$$
As a result, we have
$$
\sup_\theta R(\theta;\tilde\delta) \geq \lim_{n\to\infty} r_{\Lambda_n} = \sup_\theta R(\theta;\delta),
$$
and $\delta$ is minimax. Moreover,
$$
\lim_{n\to\infty} r_{\Lambda_n} \leq r^* \leq \sup_\theta R(\theta;\delta) = \lim_{n\to\infty} r_{\Lambda_n},
$$
so the sequence is least favorable and $\lim_{n\to\infty} r_{\Lambda_n}=r^*$. $\blacksquare$

---

[← Least Favorable Priors](03-least-favorable-priors.md) · [Up: contents](index.md) · [Bounding the minimax risk →](05-bounding-the-minimax-risk.md)
