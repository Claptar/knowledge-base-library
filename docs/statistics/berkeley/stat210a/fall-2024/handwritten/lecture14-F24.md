---
title: Outline 10/10/2023
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture14-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture14-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture14-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture14-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline 10/10/2023

1) Hypothesis testing
2) Neyman-Pearson Lemma

---

## Hypothesis Testing

In hypothesis testing, we use data $X$ to infer which of two submodels generated $X$.

Model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$

Null hypothesis $H_0 : \theta \in \Theta_0$
Alternative hyp. $H_1 : \theta \in \Theta_1$

(Whenever $H_1$ unspecified, assume $\Theta_1 = \Theta \setminus \Theta_0$)

$H_0$ is "default choice" : we either
1. accept $H_0$ (fail to reject, no definite concl.)
2. reject $H_0$ (conclude $\Theta_0$ false, $\Theta_1$ true)

**Ex** $X \sim N(\theta, 1) \quad H_0 : \theta \le 0 \quad \text{vs} \quad H_1 : \theta > 0$
or $H_0 : \theta = 0 \quad \text{vs} \quad H_1 : \theta \neq 0$

**Ex** $X_1, \dots, X_n \sim P \quad Y_1, \dots, Y_m \sim Q \quad H_0 : P = Q \quad \text{vs} \quad H_1 : P \neq Q$

[ Common conceptual objection: we "know" $\theta \neq 0$ or $P \neq Q$ already, why bother?
We will return to this. ]

---

## Power Function

Can describe a test formally by its critical function (a.k.a. test function)

$$
\phi(x) = \begin{cases}
0 & \text{accept } H_0 \\
\pi \in (0, 1) & \text{reject w.p. } \pi \\
1 & \text{reject } H_0
\end{cases}
$$

In practice, randomization rarely used ($\phi(x) \in \{0, 1\}$)
(In theory, simplifies discussions.)

A non-randomized test partitions $\mathcal{X}$ into
$$
\begin{aligned}
R &= \{x : \phi(x) = 1\} \quad \text{rejection region} \\
A &= \{x : \phi(x) = 0\} \quad \text{acceptance region}
\end{aligned}
$$

**Power function** :
$$
\begin{aligned}
\beta_\phi(\theta) &= \mathbb{E}_\theta[\phi(X)] \quad \text{rejection prob.} \\
&= \mathbb{P}_\theta[\text{Reject } H_0]
\end{aligned}
$$
fully summarizes test's behavior

$\phi$ is a **level-$\alpha$ test** ($\alpha \in [0, 1]$) if $\sup_{\theta \in \Theta_0} \beta_\phi(\theta) \le \alpha$

Ubiquitous choice is $\alpha = 0.05$
["Most influential offhand remark in history of science"]

**Goal**: Maximize $\beta_\phi(\theta)$ on $\Theta_1$, subject to level-$\alpha$ constraint

---

## Examples

**Ex** \$X \sim N(\theta, 1) \qquad

---

[Up: contents](../index.md)
