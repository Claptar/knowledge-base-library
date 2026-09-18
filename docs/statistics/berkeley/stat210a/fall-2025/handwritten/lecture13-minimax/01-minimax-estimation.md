---
title: Minimax Estimation
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture13-minimax.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture13-minimax.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture13-minimax.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture13-minimax.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Minimax Estimation

### Outline

1) Minimax risk, estimator
2) Least favorable priors
3) Examples

---

## Minimax risk

Last idea for choosing an estimator: worst-case risk

$$
\underset{\delta}{\text{minimize}} \quad \sup_\theta R(\theta; \delta)
$$

The minimum achievable sup-risk is called the **minimax risk** of the estimation problem

$$
r^* = \inf_\delta \sup_\theta R(\theta; \delta)
$$

An estimator $\delta^*$ is called **minimax** if it achieves the minimax risk, i.e.

$$
\sup_\theta R(\theta; \delta^*) = r^*
$$

Game theory interpretation: (Minimax game)
1) Analyst chooses estimator $\delta$
2) Nature chooses parameter $\theta$ to max. risk

**NB**: Nature chooses $\theta$ adversarially, not $X$

Compare to Bayes ("Maximin" game)
1) Nature chooses prior $\Lambda$ (mixed strategy)
2) Analyst chooses estimator to min. (avg) risk

We will look for Nature's Nash-equil. strategy in this problem

---

## Least Favorable Priors

**Key observation**: $\text{average-case risk} \le \text{worst-case risk}$

For proper prior $\Lambda$, the Bayes risk is

$$
r_\Lambda = \inf_\delta \int R(\theta; \delta) \, d\Lambda(\theta)
$$

$$
\le \inf_\delta \sup_\theta R(\theta; \delta) = r^*
$$

If $\delta_\Lambda$ Bayes then $r_\Lambda = \int R(\theta; \delta_\Lambda) \, d\Lambda(\theta)$

$\Rightarrow$ Bayes risk of **any** Bayes estimator lower bounds $r^*$

**Least favorable prior $\Lambda^*$** gives best lower bound: $r_{\Lambda^*} = \sup_\Lambda r_\Lambda$

Sup-risk of any estimator upper bounds $r^*$

$$
\underset{(\text{any } \Lambda)}{r_\Lambda} \le r_{\Lambda^*} \le r^* \le \underset{(\text{any } \delta)}{\sup_\theta R(\theta; \delta)}
$$

**Idea**: try to match upper & lower bounds

---

## Theorem

Let $\Lambda$ be a prior with Bayes estimator $\delta_\Lambda$

If $r_\Lambda = \sup_\theta R(\theta; \delta_\Lambda)$, then $\delta_\Lambda$ is minimax and $\Lambda$ is LF, with $r^* = r_\Lambda$.

If $\delta_\Lambda$ unique Bayes (up to $\overset{\text{a.s.}}{=}$), also unique minimax.

### Proof

Any other $\delta$:

$$
\begin{aligned}
\sup_\theta R(\theta; \delta) &\ge \int R(\theta; \delta) \, d\Lambda(\theta) \\
&\underset{\substack{\text{strict if} \\ \text{unique Bayes}}}{\ge} \int R(\theta; \delta_\Lambda) \, d\Lambda(\theta) \\
&= r_\Lambda \\
&= \sup_\theta R(\theta; \delta_\Lambda) \quad \text{by assumption}
\end{aligned}
$$

Hence $r_\Lambda \le r^* \le \sup_\theta R(\theta; \delta_\Lambda) = r_\Lambda$ $\quad \blacksquare$

Gives checkable conditions:
1) Bayes est. with constant $R(\theta; \delta_\Lambda) \Rightarrow \text{minimax}$
2) If $R(\theta; \delta_\Lambda)$ attains max everywhere on $\text{supp}(\Lambda)$

**NB**: Showing $r_\Lambda = \mathbb{E}_\Lambda R(\theta; \delta)$ const is meaningless since we have integrated out $\theta$!

---

## Ex

$X \sim N(\theta, 1) \qquad |\theta| \ge 1 \qquad (\Theta = (-\infty, -1] \cup [1, \infty))$

Estimate $g(\theta) = \text{sgn}(\theta) = \begin{cases} +1 & \theta > 0 \\ -1 & \theta < 0 \end{cases}$

Try $\Lambda = \text{Unif}(\{-1, +1\}) \qquad (\Lambda(\{-1\}) = \Lambda(\{1\}) = \frac{1}{2})$

$$
\mathbb{P}_\Lambda(\theta = 1 \mid X = x) = \frac{\phi(x - 1)}{\phi(x - 1) + \phi(x + 1)}
$$

$$
\begin{aligned}
\mathbb{E}_\Lambda(g(\theta) \mid X = x) &= \frac{\phi(x - 1) - \phi(x + 1)}{\phi(x - 1) + \phi(x + 1)} \\
&= \frac{e^x - e^{-x}}{e^x + e^{-x}} = \tanh(x)
\end{aligned}
$$

```
       MSE(theta; delta_Lambda)
                ^
                |
          *     |     *
         /|     |     |\
        / |     |     | \
       /  |     |     |  \
      /   |     |     |   \
     /    |     |     |    \
    /     |     |     |     \
  --------*-----+-----*--------> theta
         -1     |    +1
          \_____|_____/
                |
           supp(Lambda)
```

---

---

[Up: contents](index.md) · [Example (Binomial) →](02-example-binomial.md)
