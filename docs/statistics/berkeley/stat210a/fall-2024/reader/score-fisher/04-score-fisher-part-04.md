---
title: Score fisher Part 04 —
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Score fisher Part 04 —

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Assume a family $\cP$ has densities $p_\theta$ with respect to a measure $\mu$, for $\theta \in \Theta \subseteq \RR^d$. Assume additionally that these densities have common support: that $\{x: p_\theta(x) > 0\}$ is the same for all $\theta$.

Recall the log-likelihood is $l(\theta;X) = \log p_\theta(X)$ (thought of as a random function of $\theta$)

**Definition:** The *Score function* is $\nabla l_\theta(X)$.

It plays a key role in many areas of statistics, especially in asymptotics. We can think of it as a "local complete sufficient statistic." For $\eta \approx 0$, and $\theta_0 \in \Theta^\circ$, we have

$$p_{\theta_0+\eta}(x) = e^{\ell(\theta_0 + \eta; x)} \approx e^{\eta'\nabla \ell(\theta_0;x)}p_{\theta_0}(x).$$

---

[← Motivation: Tangent Family](03-motivation-tangent-family.md) · [Up: contents](index.md) · [Differential Identities and the Fisher Information →](05-differential-identities-and-the-fisher-information.md)
