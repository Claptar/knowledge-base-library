---
title: Sufficiency
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-sufficiency.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture04-sufficiency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture04-sufficiency.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-sufficiency.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Sufficiency

## Outline
1) Sufficiency
2) Factorization Theorem
3) Examples
4) Minimal sufficiency

---

## Three models for coin flipping

**Model 3** $\quad X_{i,j} \stackrel{iid}{\sim} \text{Bernoulli}(\theta_{i,t}) \quad \begin{matrix} i = 1, \dots, 48 \\ j = 1, \dots, n_i \end{matrix} \quad \theta_{i,j} \searrow \text{in } j$

**Model 2** $\quad X_{i+} \stackrel{ind}{\sim} \text{Binom}(n_i, \theta_i) \qquad X_{i+} = \sum_{j=1}^{n_i} X_{i,j}$

**Model 1** $\quad X_{++} \stackrel{ind}{\sim} \text{Binom}(n, \theta) \qquad X_{++} = \sum_{i=1}^{48} \sum_{j=1}^{n_i} X_{i,j}$

These models are **nested**: $\mathcal{P}_1 \subseteq \mathcal{P}_2 \subseteq \mathcal{P}_3$
(Model 1: most assumptions; Model 3: fewest assumptions)

Data keeps getting compressed too...
are we losing anything by doing this?

**Answer** No. $X_{++}$ is a **sufficient statistic** for $\mathcal{P}_1$, and $(X_{1+}, \dots, X_{48+})$ is also sufficient for $\mathcal{P}_2$

**Def** A **statistic** $T(X)$ is any function of data $X$

---

**Def** A statistic $T(X)$ is **sufficient** for model $\mathcal{P}$ if the conditional distribution of $X \mid T(X)$ is the same for all $P \in \mathcal{P}$

Check definition for $T(X) = X_{++}$ in $\mathcal{P}_1$:

$$p_\theta(x) = \prod_{i=1}^{48} \prod_{j=1}^{n_i} \theta^{x_{ij}} (1-\theta)^{1 - x_{ij}}$$

$$= \theta^{X_{++}} (1-\theta)^{n - X_{++}} \quad (\text{why no } \binom{n}{x_{++}}?)$$

$$P_\theta(X = x \mid X_{++} = t) = \frac{P_\theta(X = x, \, X_{++} = t)}{P_\theta(X_{++} = t)}$$

$$= \frac{\mathbf{1}\{X_{++} = t\} \cdot \theta^t (1-\theta)^{n-t}}{\binom{n}{t} \theta^t (1-\theta)^{n-t}}$$

$$= \mathbf{1}\{X_{++} = t\} / \binom{n}{t}$$

**Intuition** Suppose we believe Model 1.
Big/small $X_{++}$ more likely with big/small $\theta$.
But once we know $X_{++} = 178,079$, all data sets $X$ with that many same-side flips are equally likely, regardless of $\theta$.

Not true in Models 2 & 3 $\implies X_{++}$ no longer sufficient

---

---

[Up: contents](index.md) · [Factorization Theorem →](02-factorization-theorem.md)
