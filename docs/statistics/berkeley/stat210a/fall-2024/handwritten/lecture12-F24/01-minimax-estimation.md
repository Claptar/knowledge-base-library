---
title: Minimax Estimation
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture12-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture12-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Minimax Estimation

10/5/2021

### Outline

1) Minimax risk, estimator
2) Least favorable priors

---

## Minimax risk

Last idea for choosing an estimator: worst-case risk

$$\text{minimize }_\delta \quad \sup_\theta R(\theta; \delta)$$

The minimum achievable sup-risk is called the **minimax risk** of the estimation problem

$$r^* = \inf_\delta \sup_\theta R(\theta; \delta)$$

An estimator $\delta^*$ is called **minimax** if it achieves the minimax risk, i.e.

$$\sup_\theta R(\theta; \delta^*) = r^*$$

Game theory interpretation:
1) Analyst chooses estimator $\delta$
2) Nature chooses parameter $\theta$ to max. risk

**NB**: Nature chooses $\theta$ adversarially, not $X$

Compare to Bayes, where Nature chooses prior from a known distribution
$\Rightarrow$ Nature plays a specific mixed strategy
We will look for Nature's Nash-equil. strategy

---

## Least Favorable Priors

Minimax closely related to Bayes

**Key observation**: average-case risk $\le$ worst-case risk

For proper prior $\Lambda$, the Bayes risk is

$$\begin{aligned}
r_\Lambda &= \inf_\delta \int R(\theta; \delta) \, d\Lambda(\theta) \\
&\le \inf_\delta \sup_\theta R(\theta; \delta) = r^*
\end{aligned}$$

If $\delta_\Lambda$ Bayes then $r_\Lambda = \int R(\theta; \delta_\Lambda) \, d\Lambda(\theta)$

$\Rightarrow$ Bayes risk of **any** Bayes estimator lower bounds $r^*$

**Least favorable prior** $\Lambda^*$ gives best lower bound: $r_{\Lambda^*} = \sup_\Lambda r_\Lambda$

Sup-risk of any estimator upper bounds $r^*$

$$\begin{array}{ccccccc}
\sup_\theta R(\theta; \delta) & \ge & r^* & \ge & r_{\Lambda^*} & \ge & r_\Lambda \\
\uparrow & & & & & & \uparrow \\
(\text{any } \delta) & & & & & & (\text{any } \Lambda)
\end{array}$$

Can exhibit minimax est. / LF prior by finding $\delta$ and $\Lambda$ that collapse these ineq. to $=$

---

---

[Up: contents](index.md) · [Theorem →](02-theorem.md)
