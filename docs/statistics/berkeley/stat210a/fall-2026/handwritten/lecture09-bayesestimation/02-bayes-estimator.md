---
title: Bayes Estimator
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture09-bayesestimation.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture09-bayesestimation.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture09-bayesestimation.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture09-bayesestimation.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Bayes Estimator

Model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$, (proper) prior $\Lambda$

Assume
* $L(\theta, d) \ge 0$
* $r_\Lambda(\delta_0) < \infty$ for some $\delta_0(x)$

Then $\delta_\Lambda(x)$ is Bayes, with $r_\Lambda(\delta_\Lambda) < \infty$

$$
\text{iff } \delta_\Lambda(x) \in \arg\min_d \mathbb{E}[L(\theta, d) \mid X = x] \quad \text{a.e. } x
$$
($\mathbb{P}(\delta_\Lambda(x) \notin \arg\min) = 0$ wrt marginal)

**Proof**

$(\Leftarrow)$ $\delta$ any other estimator

$$
\mathbb{E}[L(\theta, \delta(x)) \mid X] \stackrel{\text{a.s.}}{\ge} \mathbb{E}[L(\theta, \delta_\Lambda(x)) \mid X]
$$

Marginalize $\rightsquigarrow r_\Lambda(\delta) \ge r_\Lambda(\delta_\Lambda) < \infty$ (take $\delta = \delta_0$)

$(\Rightarrow)$ Assume $r_\Lambda(\delta_\Lambda) < \infty$ (o.w. $\delta_0$ better)

Define $E_x(d) = \mathbb{E}[L(\theta, d) \mid X]$

$$
A_\varepsilon = \left\{ x : E_x(\delta_\Lambda(x)) > \varepsilon + \inf_d E_x(d) \right\}
$$

For some $\varepsilon > 0$, $\mathbb{P}(X \in A_\varepsilon) > 0$

On $A_\varepsilon$ choose $\delta^*(x)$ so $E_x(\delta^*(x)) \le E_x(\delta_\Lambda(x)) - \varepsilon$
$\delta^* = \delta_\Lambda$ on $A_\varepsilon^c \Rightarrow E_x(\delta_\Lambda(x)) - E_x(\delta^*(x)) \ge \varepsilon \mathbf{1}\{x \in A_\varepsilon\}$

Take expectations $\rightsquigarrow r_\Lambda(\delta_\Lambda) - r_\Lambda(\delta^*) \ge \varepsilon \mathbb{P}(X \in A_\varepsilon)$  $\boxtimes$

---

## Posterior Mean

If $L(\theta, d) = (g(\theta) - d)^2$ then the Bayes estimator is the **posterior mean**:

$$
\begin{aligned}
\mathbb{E}\left[ (g(\theta) - d)^2 \mid X \right] &= \mathbb{E}\left[ \left( g(\theta) - \mathbb{E}[g(\theta) \mid X] + \mathbb{E}[g(\theta) \mid X] - d \right)^2 \mid X \right] \\
&= \operatorname{Var}(g(\theta) \mid X) + \left( \mathbb{E}[g(\theta) \mid X] - d \right)^2
\end{aligned}
$$
*(why is the cross-term 0?)*

$$
\Rightarrow \delta_\Lambda(x) = \mathbb{E}[g(\theta) \mid X = x]
$$

**Weighted sq. error**:

$L(\theta, d) = w(\theta)(g(\theta) - d)^2$
e.g. $\left(\frac{\theta - d}{\theta}\right)^2$ sq. rel. error

$$
\begin{aligned}
\mathbb{E}[(d - g(\theta))^2 w(\theta) \mid X] &= d^2 \mathbb{E}[w(\theta) \mid X] - 2d \mathbb{E}[w(\theta) g(\theta) \mid X] \\
&\quad + \mathbb{E}[w(\theta) g(\theta)^2 \mid X]_{\text{no dep. on } d}
\end{aligned}
$$

min at
$$
d = \frac{\mathbb{E}[w(\theta) g(\theta) \mid X]}{\mathbb{E}[w(\theta) \mid X]} \quad (= \delta_\Lambda(x))
$$

---

---

[← Frequentist Motivation](01-frequentist-motivation.md) · [Up: contents](index.md) · [Example: Beta-Binomial →](03-example-beta-binomial.md)
