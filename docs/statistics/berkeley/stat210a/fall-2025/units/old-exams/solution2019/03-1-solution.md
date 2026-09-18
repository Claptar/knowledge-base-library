---
title: 1. Solution.
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2019.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2019.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1. Solution.

(a) By inspection the Poisson density $e^{X \log \theta - \theta}/x!$ is an exponential family, so the MLE solves $\mathbb{E}_\theta X = X$; the MLE is therefore $\hat{\theta} = X$. Its risk is
$$
R(\theta) = \frac{1}{\theta} \mathbb{E}_\theta \left[ (X - \theta)^2 \right] = 1.
$$

(b) The posterior density is
$$
\begin{aligned}
p(\theta \mid X) &\propto_\theta p(\theta) \cdot p(x \mid \theta) \\
&\propto_\theta \theta^{k-1} e^{-\theta \beta} \cdot \theta^x e^{-\theta} \\
&\propto_\theta \theta^{x+k-1} e^{-\theta(\beta+1)} \\
&\propto \text{Gamma}(x + k, \beta + 1).
\end{aligned}
$$
Hence $\theta \mid X \sim \text{Gamma}(X + k, \beta + 1)$. This is true for any setting of the prior parameters so the prior is conjugate.

(c) The Bayes estimator solves
$$
\begin{aligned}
\delta(X) &= \min_d \mathbb{E} \left[ \frac{(d - \theta)^2}{\theta} \;\middle|\; X \right] \\
&= \min_d d^2 \mathbb{E}[\theta^{-1} \mid X] - 2d + \mathbb{E}[\theta \mid X] \\
&= 1/\mathbb{E}[\theta^{-1} \mid X] \\
&= \frac{X + k - 1}{\beta + 1}.
\end{aligned}
$$

(d) For the minimization problem in the last part, the minimized value is
$$
-\delta(X) + \mathbb{E}[\theta \mid X] = -\frac{X + k - 1}{\beta + 1} + \frac{X + k}{\beta + 1} = \frac{1}{\beta + 1}.
$$
The Bayes risk, then, is $\mathbb{E} \mathbb{E} \left[ \frac{(\delta(X) - \theta)^2}{\theta} \;\middle|\; X \right] = \frac{1}{\beta + 1}$.

(e) Taking arbitrary $k > 1$, the sequence $\Gamma(k, \beta_n)$ has limiting risk equal to 1, which is also the sup-risk of the MLE. Hence it is a least-favorable sequence and the MLE is minimax.

---

(f) For the usual squared error loss, the Bayes estimator is the posterior mean and the conditional expectation of the loss (given $X$) is therefore the posterior variance, which is $(X + k + 1)/(1 + \beta)^2$. The Bayes risk is then
$$
\mathbb{E} \frac{X + k + 1}{(1 + \beta)^2} = \frac{k/\beta + k + 1}{(1 + \beta)^2},
$$
where we use $\mathbb{E} X = \mathbb{E} \theta = k/\beta$. If we fix $k > 1$ and send $\beta \to 0$, the Bayes risk tends to $\infty$. The minimax risk is larger than any Bayes risk, so it is also infinite.

---

---

[← 1. Poisson minimax estimation (24 points, 4 points / part).](02-1-poisson-minimax-estimation-24-points-4-points-part.md) · [Up: contents](index.md) · [2. ANOVA with random effects (25 points, 5 points / part). →](04-2-anova-with-random-effects-25-points-5-points-part.md)
