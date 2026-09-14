---
title: Completeness
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/completeness.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Completeness

**Source:** [`reader/completeness.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

As we have seen, for a given statistical problem we may have many different sufficient statistics, some of which reduce the data more than others. We usually want to look for one that is *minimal sufficient*, meaning that it strips away as much irrelevant information as possible and only retains the information that is relevant to estimating the parameter.

In some cases the minimal sufficient statistic has an additional property called *completeness*. The definition of completeness is initially counterintuitive, but it has a number of useful implications we will explore throughout the semester.

### Definition of completeness

A statistic $T(X)$ is complete for a family of distributions $\cP = \{P_\theta: \theta \in \Theta\}$ if no nontrivial function of $T$ can have expectation zero for every distribution in the family:

$$\EE_\theta \,f(T(X)) = 0 \quad \forall \theta \in \Theta \implies f(T) \eqPas 0$$
::: callout-note
The name for complete statistics comes from a prior notion that $\cP^T = \{P_\theta^T:\; \theta \in \Theta\}$ is ``complete'' as a model if its linear span includes all possible distributions on $T(X)$; see Homework 3.
:::

If $X$ itself is complete, then the definition immediately implies that there can be at most one unbiased estimator for any estimand: if $\EE_\theta \delta_1(X) = \EE_\theta \delta_2(X) = g(\theta)$ for all $\theta \in \Theta$, then $f(X) = \delta_1(X) - \delta_2(X) = 0$ almost surely. More generally, if $T(X)$ is a complete statistic then there can be at most one unbiased estimator that runs through $T$. We will return to this fact when we discuss unbiased estimation.

We will be especially interested in statistics that are both complete and sufficient. If $T(X)$ is complete and sufficient we call it a *complete sufficient statistic*.

::: callout-warning
A complete statistic need not be sufficient: the constant "statistic" $T(X) \equiv 0$ is complete in any model. In general, to show that $T(X)$ is complete sufficient we must establish both properties.
:::


### Examples

**Example 1 (Laplace location family)**: Let $X_1,\ldots,X_n \simiid \text{Lap}(\theta)$ for $\theta \in \RR$, and recall that the vector of order statistics $S(X) = (X_{(1)},\ldots,X_{(n)})$ is a minimal sufficient statistic. Is $S(X)$ complete?

!!! important "Important"

---

[← Under construction](01-under-construction.md) · [Up: contents](index.md) · [Expand to see answer →](03-expand-to-see-answer.md)
