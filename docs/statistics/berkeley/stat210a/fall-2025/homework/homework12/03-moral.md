---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework12.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework12.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework12.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework12.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Likelihood-based methods give us good options for estimation in models where exact inference could be difficult.

**Problem 3** (Estimation in misspecified models).

Assume we observe a sample $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}p(x)$, and we perform maximum likelihood estimation for a real parameter $\theta$ using a dominated family $\mathcal{P}= \{p_{\theta}(x):\; \theta\in\Theta \subseteq \mathbb{R}\}$, where $p\notin\mathcal{P}$. Let $\hat\theta_n$ denote the maximum likelihood estimator, and let $\theta^*$ denote the parameter value that minimizes KL divergence: $$\theta^* = \mathop{\mathrm{argmin}}_{\theta\in\Theta} \;D_{\text{KL}}(p \;\|\; p_{\theta})
= \mathop{\mathrm{argmax}}_{\theta\in\Theta}\; \mathbb{E}_p\left[\ell_n(\theta; X)\right].$$ Since there is no true value of $\theta$, we might still hope to “fail gracefully” by estimating $\theta^*$, which (in some sense) best approximates the true distribution $p$.

Assume $\theta^*$ is unique, that the parameter space $\Theta$ is compact, that $\theta^*$ is in its interior, and that the supremum log-likelihood ratio between any pair of parameter values is bounded in expectation: $$\mathbb{E}_p\left[\sup_{\theta_1,\theta_2\in\Theta}|\ell_1(\theta_1; X) - \ell_1(\theta_2; X)|\right] < B.$$ In addition, assume that the log-likelihood is twice continuosly differentiable, and that for all $\theta\in\Theta$, $$\text{Var}_p(\dot{\ell}_1(\theta;X)) \in (0,\infty), \quad \mathbb{E}_p\left[\ddot{\ell}_1(\theta;X)\right] \in (-\infty,0).$$ Note that by dominated convergence we can bring derivatives inside the integral; you do not need to justify this. Finally, assume $\mathbb{E}_p\left[\sup_{\theta\in\Theta} |\ddot{\ell}_1(\theta;X)|\right]<\infty$.

1.  Show that the maximum likelihood estimator converges in probability to $\theta^*$.

2.  Give a counterexample to show why, even for smooth models, we should not expect under misspecification to have $$-\mathbb{E}_p [\ddot{\ell}_n(\theta^*;X)] = \text{Var}_p(\dot{\ell}_n(\theta^*;X)).$$

3.  Find the limiting distribution of $\hat\theta_n$ as $n \to \infty$. We can think of a confidence interval for $\theta$ more generally as a confidence interval for the best-fitting parameter value $\theta^*$. Can we expect the Wald confidence interval for the misspecified model to asymptotically achieve the correct coverage of $\theta^*$?

---

[← Moral](02-moral.md) · [Up: contents](index.md) · [Moral →](04-moral.md)
