---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework1.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework1.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework1.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework1.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Our more general definition of densities extends to situations where there is no probability mass function or probability density function.

**Problem 4** (Bias-variance tradeoff).

Consider a generic estimation setting where we observe $X \sim P_\theta$, for a model $\mathcal{P}= \{P_\theta:\; \theta \in \Theta \subseteq \mathbb{R}^d\}$, and we want to estimate $\theta$ using some estimator $\delta(X) \in \mathbb{R}^d$. The *bias* of $\delta$ (under sampling from $P_\theta$) is defined as $$\text{Bias}_\theta(\delta(X)) = \mathbb{E}_\theta[\delta(X)] - \theta.$$ For $d=1$, it is well-known that the mean squared error $\text{MSE}(\theta; \delta)$ can be decomposed as the sum of the squared bias of $\delta$ and its variance: $$\begin{equation}
\label{eq:biasvar}
    \text{MSE}(\theta; \delta) = \text{Bias}_\theta(\delta)^2 + \textnormal{Var}_\theta(\delta).
\end{equation}$$

1.  Derive the correct generalization of <a href="#eq:biasvar" data-reference-type="eqref" data-reference="eq:biasvar">[eq:biasvar]</a> for general $d \geq 1$, where the MSE is defined as $$\text{MSE}(\theta; \delta) = \mathbb{E}_\theta \|\delta(X) - \theta\|_2^2.$$ It might help to start with $d=1$.

2.  Suppose that we are estimating the false positive rate of a new diagnostic test for some disease, using a sample of $n$ specimens taken from a population known not to have the disease we are testing for. If $X$ is the number of false positives and $\theta \in (0,1)$ is the false positive rate, assume $X \sim \text{Binom}(n, \theta)$. The “obvious” estimator is $\delta_0(X) = X/n$.

    However, biological samples are expensive to obtain and the new test is a slightly modified version of an old test whose false positive rate is known to be $\theta_0 \in (0,1)$, so we might want to “shrink” the estimator toward the anchor value $\theta_0$ as follows: $$\delta_{\gamma}(X) = \gamma \theta_0 + (1-\gamma) \frac{X}{n}, \quad \text{ for } \gamma \in [0,1],$$ where taking $\gamma = 0$ reduces to the “obvious” estimator $\delta_0(X) = X/n$.

    Find the MSE of $\delta_\gamma(X)$ as an explicit expression in $\theta_0, \theta, n$, and $\gamma$.

3.  Find the optimal (i.e., risk-minimizing) shrinkage parameter $\gamma^*$, as a function of the sample size $n$, the true parameter $\theta$, and the anchor value $\theta_0$. What happens to the optimal $\gamma^*$ if we send $\theta \to \theta_0$ while holding $\theta_0$ and $n$ fixed? What if we send $n\to\infty$ while holding $\theta$ and $\theta_0$ fixed instead? Explain why these limits make intuitive sense.

4.  In our calculation above, the optimal $\gamma^*$ is never exactly zero; that is, a smidgeon of shrinkage always beats no shrinkage. Does this make $\delta_0$ inadmissible? Prove or disprove whether $\delta_0$ is dominated by any $\delta_\gamma$.

---

[← Moral](03-moral.md) · [Up: contents](index.md) · [Moral →](05-moral.md)
