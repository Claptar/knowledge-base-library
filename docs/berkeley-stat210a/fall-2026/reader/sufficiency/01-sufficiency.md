---
title: Sufficiency
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/sufficiency.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/sufficiency.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Sufficiency

**Source:** [`reader/sufficiency.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/sufficiency.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Sufficiency is a central concept in statistics that allows us to focus on the essential aspects of the data set while ignoring details that are irrelevant to the inference problem. As we will see, in many problems we can find a more stripped-down representation of the data that carries all of the relevant information for a statistical problem.

Let $X\sim P_\theta$ represent a data set drawn from a model $\cP = \{P_\theta:\; \theta \in \Theta\}$. A *statistic* $T(X)$ is any random variable that is a function of the data $X$ (and which does not depend on the unknown parameter $\theta$). We say the statistic $T(X)$ is *sufficient* for the model $\cP$ if $P_\theta(X \mid T)$ does not depend on $\theta$. This lecture will be devoted to interpreting this definition and giving examples.

**Example (Independent Bernoulli sequence):** We can introduce a binomial model by telling a story about an investigator who flips a biased coin $n$ times and records the total number of heads, which has a binomial distribution if we assume the flips are independent and share a common probability $\theta$ of landing heads. All of the estimators we considered in the last lecture were functions only of the count.

But if the investigator had actually performed this experiment, they would have observed not only the total number of heads, but the entire sequence of $n$ heads and tails. If we let $X_i$ denote a binary indicator of whether the $i$th throw is heads, for $i=1,\ldots,n$, then we have assumed that these indicators are i.i.d. Bernoulli random variables:

$$
X_1,\ldots,X_n \simiid \text{Bern}(\theta).
$$

Let $T(X) = \sum_i X_i \sim \text{Binom}(n,\theta)$ denote the summary statistic that we previously used to represent the entire data set. It is undeniable that we have lost some information by only recording $T(X)$ instead of the entire sequence $X = (X_1,\ldots,X_n)$. As a result, we might wonder whether we could have improved the estimator by considering all functions of $X$, not just functions of $T(X)$.

The answer is that, no, we did not really lose anything by summarizing the data by $T(X)$ because $T(X)$ is sufficient. The joint pmf of the data set $X \in \{0,1\}^n$ (i.e., the density wrt the counting measure on $\{0,1\}^n$) is

$$
p_\theta(x) = \prod_{i=1}^n \theta^{x_i}(1-\theta)^{1-x_i} = \theta^{\sum_i x_i}(1-\theta)^{n-\sum_i x_i}.
$$

Note that this pmf depends only on $T(x)$: it assigns probability $\theta^t (1-\theta)^{n-t}$ to every sequence with $T(X)=t$ total heads. As a result, the conditional distribution given $T(X)=t$ should be uniform on all of the $\binom{n}{t}$ sequences with $t$ heads. We can confirm this by calculating the conditional pmf directly:

$$
\begin{aligned}
\PP_\theta(X = x \mid T(X) = t)
&= \frac{\PP_\theta(X=x, \sum_i X_i = t)}{\PP_\theta(T(X) = t)} \\[7pt]
&= \frac{\theta^t (1-\theta)^{n-t}1\{\sum_i x_i = t\}}{\theta^t(1-\theta)^{n-t}\binom{n}{t}}\\[5pt]
&= \binom{n}{t}^{-1}1\{T(x) = t\}.
\end{aligned}
$$

Since the conditional distribution does not depend on $\theta$, $T(X)$ is sufficient for the model $\cP$.

---

[Up: contents](index.md) · [Visualization of sufficiency →](02-visualization-of-sufficiency.md)
