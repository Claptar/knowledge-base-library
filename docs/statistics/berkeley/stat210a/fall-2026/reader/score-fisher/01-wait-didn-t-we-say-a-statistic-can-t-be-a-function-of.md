---
title: Wait! Didn't we say a statistic can't be a function of $\theta$?
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Wait! Didn't we say a statistic can't be a function of $\theta$?

In this section we introduce the score function and Fisher information, two concepts that are central in asymptotic statistics. We

Assume a family $\cP$ has densities $p_\theta$ with respect to a measure $\mu$, for $\theta \in \Theta \subseteq \RR^d$. Assume additionally that these densities have common support: that $\{x: p_\theta(x) > 0\}$ is the same for all $\theta$ (since we can truncate the sample space to this common support, we could just as well assume $p_\theta(x) > 0$ for all $x$ and $\theta$).

**Definition:** The *Score function* is defined as $S_{\theta}(X) = \nabla \ell(\theta;X)$, a random vector of dimension $d$.

We can think of the score function $S_{\theta_0}(X)$ at a given value $\theta_0$ as a kind of "local" sufficient statistic that we could use to distinguish between $\theta$ values in a small neighorhood of $\theta_0$.

To see why, recall that the log-likelihood $\ell(\theta;X) = \log p_\theta(X)$, thought of as a random function with argument $\theta$, is a minimal sufficient statistic for $X$, up to a vertical shift.

!!! important "Important"

Yes, but what we meant by this is, more precisely, is that a statistic can be calculated from the data, by an analyst who doesn't know what is the *true* value of $\theta$ that governed the sampling distribution of the data $X$.

The trouble is that there is a bit of notational ambiguity when we write $\ell(\theta;X)$. If we want to be a bit more precise, what we mean here is $\ell(\cdot; X)$, which is realized in the space of functions from $\theta$ to $\mathbb{R}$. If the analyst observes $X$ they can plot a graph of this whole likelihood function; that graph is the statistic.

On the other hand, suppose that instead we interpret $\ell(\theta;X)$ as the function *evaluated at* the true value $\theta$, i.e. in more pedantic notation $\left.\ell(\cdot; X)\right|_{\text{true } \theta}$. Then, this would *not* be a statistic because the analyst can't calculate it without knowing which is the true value.

A third possibility is that we could be evaluating $\ell()

:::

For any fixed reference point $\theta_0 \in \Theta$, we can subtract $\ell(\theta_0; X)$ to obtain the minimal sufficient statistic $\ell(\theta; X) - \ell(\theta_0; X)$. Then, for a nearby value $\theta = \theta_0 + \eta$, with $\eta\$ small, we have
$$
\ell(\theta_0 + \eta; X) - \ell(\theta_0; X) \approx \eta'S_{\theta_0}(X),
$$
so the statistic $S_{\theta_0}(X)$ would approximately capture all of the information in a "local" model $\{P_{\theta_0+\eta}: \eta \text{ small}\} \subseteq \cP$.

!!! important "Important"

---

[Up: contents](index.md) · [Is the score a statistic? →](02-is-the-score-a-statistic.md)
