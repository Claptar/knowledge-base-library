---
title: 2 The critical function
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hypothesis-testing.html
source_file: sources/berkeley-stat210a/fall-2025/reader/hypothesis-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/hypothesis-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hypothesis-testing.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 The critical function

We can describe a test by its *critical function* (a.k.a. *test function*):

$$
\phi(x) = \begin{cases}
0 & \text{accept } H_0 \\
\gamma \in (0,1) & \text{reject w.p. } \gamma \\
1 & \text{reject } H_0
\end{cases}
$$

The option of randomizing our test by taking $\phi(x) \in (0,1)$ for some values $x \in \cX$ is helpful in theory, as we will see shortly, but it is hardly ever done in practice. A non-randomized test $\phi$ partitions $\cX$ into the *rejection region* $R = \{x \in \cX: \phi(x) = 1\}$ and the *acceptance region* $A = \{x \in \cX:\; \phi(x) = 0\}$.

Most tests are defined by choosing a real-valued *test statistic* $T(X)$ and rejecting when $T(X)$ is above some *critical threshold* $c \in \RR$. We say $\phi$ *rejects for large $T(X)$* if

$$
\phi(x) = \begin{cases}
0 & T(x) < c\\
\gamma \in (0,1) & T(x) = c \text{ (if } \phi \text{ is randomized)} \\
1 & T(x) > c
\end{cases}
$$

 Much of the art in designing a hypothesis test is in choosing a test statistic $T(X)$ that is as effective as possible at discriminating between $H_0$ and $H_1$

## 2.1 Significance level and power {.anchored number="2.1" anchor-id="significance-level-and-power"}

In carrying out a test, there are two types of errors that we can make: a *Type I error* (sometimes called a *false positive*) is when $H_0$ is true, but we reject it, and a *Type II error* (sometimes called a *false negative*) is when $H_0$ is false but we fail to reject it. One way to remember which is which is that the Type I error rate is of primary importance in deciding when to reject, and the Type II error rate is of secondary importance. Our usual goal, informally, is to make the probability of a Type II error under $H_1$ as small as we can, while controlling the Type I error rate below a prespecified value $\alpha \in [0,1]$. Note that if $H_0$ and $H_1$ are composite, we cannot necessarily speak of “the” Type I or Type II error rate, as it may depend on exactly which of the null or alternative parameter values we sample under.

The behavior of the test is fully summarized by the *power function* $\beta(\theta) = \mathbb{E}_\theta[\phi(X)] = \PP_\theta(\text{Reject } H_0)$. In terms of this power function, our goal can be formally stated as

$$
\maxz_\phi \beta_\phi(\theta) \text{ for } \theta \in \Theta_1 \quad \text{ subject to } \beta_\phi(\theta) \leq \alpha \text{ for } \theta \in \Theta_0.
$$

 We say $\phi$ is a *level-$\alpha$ test* if $\sup_{\theta\in\Theta_0} \beta_\phi(\theta) \leq \alpha$. If this supremum is strictly below $\alpha$, we say the test is *conservative*. A very common choice for $\alpha$ is $0.05$; this began with a somewhat offhand remark by Ronald Fisher in his work when he introduced hypothesis testing, that he sometimes liked to use $0.05$ in his scientific work. It has become “the most influential offhand remark in the history of science,” according to Brad Efron at Stanford.

If $H_0$ is composite, this optimization problem has multiple constraints, and if $H_1$ is composite it has multiple objectives. A major question for the remainder of this lecture is whether we can find a test $\phi^*$ that optimizes all objectives at once.

## 2.2 Example: the $Z$-test {#example-the-math79-test .anchored number="2.2" anchor-id="example-the-z-test"}

A very common setting is that we observe some statistic $Z(X) \sim N(\theta, 1)$, very often a summary statistic from a larger data set. If we are testing the one-sided hypothesis we might use the *right-tailed test* $\phi_1(z) = 1\{z > z_\alpha\}$ that rejects for large values of $Z$. Here $z_\alpha = \Phi^{-1}(1-\alpha)$ is the upper $\alpha$ quantile of the $N(0,1)$ distribution, and $\Phi(z)$ is the standard normal cdf.

If we want to test the two-sided hypothesis we might use the *two-tailed test* $\phi_2(z) = 1\{|z| > z_{\alpha/2}\}$. Now we are rejecting for large values of the test statistic $|Z|$. The rejection regions for these tests at level $\alpha = 0.1$ are plotted below, along with the alternative distribution when $\theta = 2.3$. The shaded blue region shows the power of the test under the alternative.

![](https://raw.githubusercontent.com/berkeley-stat210a/fall-2025/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hypothesis-testing_files/figure-html/unnamed-chunk-1-1.png)

The two tests’ power functions are plotted below for $\alpha = 0.1$.

![](https://raw.githubusercontent.com/berkeley-stat210a/fall-2025/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hypothesis-testing_files/figure-html/unnamed-chunk-2-1.png)

The power functions for both tests intersect the vertical axis $\theta=0$ at $\alpha$, but the right-tailed test’s power function remains below $\alpha$ for all $\theta < 0$ as well. Note that the right-tailed test is actually a valid test for the two-sided hypothesis, but we would be unlikely to want to use it since it has even less than $\alpha$ power to reject for negative values of $\theta$. But this may give us a hint that it will not be possible to maximize power throughout the alternative, because the two-tailed test is in fact losing out to the right-tailed test when $\theta > 0$.

For the one-sided hypothesis testing problem, however, we might hold out hope that the right-tailed test is the best for all values in the alternative (all $\theta > 0$), and indeed it is.

---

[← 1 Hypothesis Testing](01-1-hypothesis-testing.md) · [Up: contents](index.md) · [3 Optimal testing →](03-3-optimal-testing.md)
