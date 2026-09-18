---
title: 2 One-sided testing
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-one-parameter.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/testing-one-parameter.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 One-sided testing

Last time, we showed that if the family $\cP$ has MLR in the statistic $T(X)$, then the one-sided test that rejects for large $T(X)$ is UMP for testing $H_0:\;\theta\leq \theta_0$ vs $H_1:\;\theta > \theta_0$, because:

1.  it is simultaneously the likelihood ratio test for $H_0:\;\theta = \theta_0$ vs $H_1:\;\theta = \theta_1$, for every $\theta_1 > \theta_0$, and

2.  it controls the Type I error for all $\theta < \theta_0$.

Recall that a test *rejects for large $T(X)$* if it is of the form

$$
\phi(X) = \begin{cases} 1 &\quad \text{ if } T(X) > c \\ 0 &\quad \text{ if } T(X) < c\\ \gamma &\quad \text{ if } T(X) = c\end{cases},
$$

 where the critical threshold $c$ is the *upper-$\alpha$ quantile at the boundary*

$$
c_\alpha = \min \{c \in \RR:\; \PP_{\theta_0}(T(X) > c) \leq \alpha\}
$$

 and the randomization parameter $\gamma$ is used to “top off” the Type I error rate if $T(X)$ is discrete and $\PP_{\theta_0}(T(X) > c_\alpha) < \alpha$. In the rest of this section we will ignore randomization and assume that we just accept a conservative test in case $\PP_{\theta_0}(T(X) > c_\alpha) < \alpha$ (as is generally done in practice).

A generic one-parameter model $\cP$ does not have MLR in any statistic $T(X)$; e.g. the LRT for testing $\theta=0$ vs $\theta=1$ does not coincide with the LRT for testing $\theta=0$ vs $\theta=  2$. Then we cannot maximize power for both alternative values $1$ and $2$ simultaneously.

In such cases, we could still come up with a test that rejects for large values of some other test statistic $T(X)$, that tends to be larger when $\theta$ is larger. Formally, we say that $T(X)$ is *stochastically increasing in $\theta$* if $\PP_\theta(T(X) > c)$ is non-decreasing in $\theta$, for every $c \in \RR$. The power function of $\phi(X) = 1\{T(X) > c_\alpha\}$, then, is also non-decreasing in $\theta$, and $\phi(X)$ is a valid test of $H_0:\;\theta\leq \theta_0$ vs $H_1:\;\theta > \theta_0$.

## 2.1 Score test {.anchored number="2.1" anchor-id="score-test"}

Suppose we observe $X_1,\ldots,X_n \simiid P_\theta$ for large $n$, and we want to test $H_0:\;\theta\leq \theta_0$ vs $H_1:\;\theta > \theta_0$, but $\cP$ does not have MLR so we cannot maximize the power over the entirety of $H_1$. One idea is to use the heuristic of maximizing the power for alternatives near $\theta_0$; if $n$ is large, then we have a lot of information about $\theta$ so our power will be close to $1$ no matter what we do. So we might prioritize maximizing the power at $\theta_0 + \varepsilon$ for small $\varepsilon$.

The LRT for $\theta_0$ vs $\theta_0 + \varepsilon$ rejects for large values of

$$
\log\frac{p_{\theta_0+\varepsilon}(X)}{p_{\theta_0}(X)} =\ell(\theta_0+\varepsilon; X) - \ell(\theta_0; X)\approx \varepsilon \dot\ell(\theta_0;X),
$$

 so a natural idea is to reject for large values of $S_{\theta_0}(X)=\dot\ell(\theta_0;X)$, provided we can show that the power of that test is monotone, for example because $S_{\theta_0}(X)$ is stochastically increasing in $\theta$. Using the score statistic can give simple and appealing tests in certain situations.

**Example: Laplace**

Suppose $X_1,\ldots,X_n \simiid \text{Laplace}(\theta) = \frac{1}{2}e^{-|x-\theta|}$ and we want to test $H_0:\theta \leq 0$ vs $H_1:\;\theta > 0$. We can calculate the likelihood ratio test for a given fixed alternative $\theta_1 > 0$ as

$$
\log \frac{p_{\theta_1}(X)}{p_0(X)} = \sum_i |X_i| - |X_i-\theta_1| = \theta_1\sum_i T_{\theta_1}(X_i),
$$

 so the optimal test rejects for large $\sum_i T_{\theta_1}(X_i)$, where

$$
T_{\theta}(x) = \begin{cases} -1 & \text{ if } x \leq 0 \\ \frac{2x}{\theta} -1 & \text{ if } 0 \leq x \leq \theta \\ +1 &\text{ if } x \geq \theta \end{cases}.
$$

 We can visualize the univariate version of the test statistic $T_{\theta_1}(x)$ for several different values of $\theta_1>0$:

![](https://raw.githubusercontent.com/berkeley-stat210a/fall-2025/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter_files/figure-html/unnamed-chunk-1-1.png)

Note that this test implicitly caps the influence of any single observation $X_i$. Once $X_i > \theta_1$, it gives the same evidence in favor of $\theta_1$ and against $\theta_0$ regardless of how much it exceeds $\theta_1$. Compare this with the sample mean, where the influence of a single observation $X_i$ is unbounded. It is easy to see that $f(X_i)$ is stochastically increasing in $\theta$ for *any* non-decreasing function $f$, so any LRT gives a valid level-$\alpha$ test on the entire null distribution.

If we take $\theta_1\downarrow 0$, the univariate test statistic approaches

$$
T_{0^+}(x) = \begin{cases} -1 & \text{ if } x \leq 0\\ +1 &\text{ if } x > 0\end{cases},
$$

 which gives the score test since

$$
S_0(X) = \dot{\ell}(0;X) = \left.\frac{d}{d\theta} \sum_i -|X_i-\theta|\right|_{\theta=0} = \sum_i T_{0^+}(X_i)
$$

 This test is called the **sign test**, and it is equivalent to rejecting when the number of positive $X_i$ values is larger than a binomial threshold, since:

$$
B(X) = \frac{S_0(X)+n}{2} = #\{X_i > 0\} \stackrel{H_0}{\sim} \text{Binom}\left(n,\frac{1}{2}\right).
$$

We can also plot the power curves for $n = 100$ and $\alpha = 0.1$, for these tests and for the test that rejects for large values of $\sum_i X_i$. As we see, the score test performs noticeably better than the test that rejects for large values of the sample mean $\overline{X}$, especially at “moderately hard” alternative values like $\theta_1=0.2$. But the LRT for $\theta_1 = 0.2$ does even better there, as it must since it is optimal for that alternative.

![](https://raw.githubusercontent.com/berkeley-stat210a/fall-2025/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter_files/figure-html/unnamed-chunk-2-1.png)

## 2.2 The sign test as a nonparametric test {.anchored number="2.2" anchor-id="the-sign-test-as-a-nonparametric-test"}

The test based on the binomial statistic $S_0(X)$ (or $B(X)$) is called the *sign test*, and is generally an appealing test for a *nonparametric* testing problem. Suppose $X_1,\ldots,X_n \simiid F$, where $F$ represents an unknown cdf for their distribution. Assume for simplicity that $F$ is continuous and strictly increasing on its support, so that the median $\theta(F) = F^{-1}(1/2)$ is well-defined, and consider testing $H_0:\; \theta(F) \leq 0$ vs $H_1:\; \theta(F) > 0$.

Then $B(X) \sim \text{Binom}(n, 1-F(0))$, where the probability parameter $1-F(0)$ is no more than $1/2$ if $H_0$ is true, but strictly greater than $1/2$ if $H_1$ is true. Then the test that rejects when $S(X)$ is above the upper $1-\alpha$ quantile of the $\text{Binom}(n,1/2)$ distribution (randomizing at the boundary if desired) is level-$\alpha$ on $H_0$.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [3 Two-sided alternatives →](03-3-two-sided-alternatives.md)
