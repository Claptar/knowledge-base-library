---
title: 'Motivation: Tangent Family'
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Motivation: Tangent Family

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Consider a family of densities:

$$p(x; \theta) = e^{\theta'T(x) - A(\theta)}h(x)$$

where $\theta \in \RR^d$ and $A(\theta) = \log \int e^{\theta'T(x)}h(x)dx$.

For this family:

-   $T(X)$ is complete sufficient
-   $T(X)$ is minimal
-   $\PP_\theta(T(X) = t) = e^{\theta't - A(\theta)}$
-   $\EE_\theta[T(X)] = A'(\theta)$


Let $\theta_0 \in \RR^d$ be fixed. Define the **tangent family**

$$q(x; t) = e^{t'\nabla l_{\theta_0}(x) - k(t)}p_{\theta_0}(x)$$

where $k(t) = \log \int e^{t'\nabla l_{\theta_0}(x)}p_{\theta_0}(x)dx$.

Then $\nabla l_{\theta_0}(X)$ is complete sufficient for the tangent family at $\theta_0$.

This is called the Score function.

---

[← Outline](02-outline.md) · [Up: contents](index.md) · [Score fisher Part 04 — →](04-score-fisher-part-04.md)
