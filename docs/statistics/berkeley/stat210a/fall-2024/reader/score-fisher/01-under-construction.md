---
title: Under construction
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Under construction

::: callout-caution

Think through "tangent family" part... is it really helping, or can it be combined with curved exponential family example?

Add back in figures from handwritten notes.
:::

## Outline

1.  Score function
2.  Fisher information
3.  Cramér-Rao Lower Bound
4.  Examples

## Motivation: Tangent Family

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

## Score Function

Assume a family $\cP$ has densities $p_\theta$ with respect to a measure $\mu$, for $\theta \in \Theta \subseteq \RR^d$. Assume additionally that these densities have common support: that $\{x: p_\theta(x) > 0\}$ is the same for all $\theta$.

Recall the log-likelihood is $l(\theta;X) = \log p_\theta(X)$ (thought of as a random function of $\theta$)

**Definition:** The *Score function* is $\nabla l_\theta(X)$.

It plays a key role in many areas of statistics, especially in asymptotics. We can think of it as a "local complete sufficient statistic." For $\eta \approx 0$, and $\theta_0 \in \Theta^\circ$, we have

$$p_{\theta_0+\eta}(x) = e^{\ell(\theta_0 + \eta; x)} \approx e^{\eta'\nabla \ell(\theta_0;x)}p_{\theta_0}(x).$$

---

[Up: contents](index.md) · [Differential Identities and the Fisher Information →](02-differential-identities-and-the-fisher-information.md)
