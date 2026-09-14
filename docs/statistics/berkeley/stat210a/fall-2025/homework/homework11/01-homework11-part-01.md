---
title: Homework11 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework11.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework11.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework11 Part 01 —

**Source:** [`homework/homework11.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework11.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

See the standing homework instructions on the course web page

**Problem 1** (Precision-weighted average).

Suppose that we observe two independent samples $X_1,\ldots,X_n\overset{\text{i.i.d.}}{\sim}(\mu, \sigma^2)$ and $Y_1,\ldots,Y_m \overset{\text{i.i.d.}}{\sim}(\mu, \tau^2)$, with $n,m> 1$. The notation means that the expectation of a single $X_i$ or $Y_i$ is $\mu\in \mathbb{R}$, and the variance is $\sigma^2>0$ for a single $X_i$ and $\tau^2>0$ for a single $Y_i$. All three parameters are unknown, but we are primarily interested in estimating the common expectation $\mu$.

A natural estimator is to take a convex combination of the sample averages: $$\delta_\gamma(X,Y) = \gamma \overline X + (1-\gamma) \overline Y,$$ for $\gamma \in [0,1]$.

1.  Show that the optimal (variance-minimizing) choice of $\gamma$ is $$\gamma^* = \frac{n\sigma^{-2}}{n\sigma^{-2}+m\tau^{-2}} = \frac{1}{1+\rho m/n},$$ where $\rho = \sigma^2/\tau^2$. $\delta_{\gamma^*}$ is called the *precision-weighted average* because $n\sigma^{-2}$ and $m\tau^{-2}$ are the precisions (inverse variances) of $\overline{X}$ and $\overline{Y}$, respectively. Give the variance of $\delta_{\gamma^*}(X,Y)$.

2.  Since $\sigma^2$ and $\tau^2$ are unknown, we must estimate them. Let $S_X^2$ and $S_Y^2$ denote the usual sample variances for the two samples. Show that $\hat\rho = S_X^2/S_Y^2$ is a consistent estimator for $\rho$ as $m,n \to \infty$.

    **Hint:** It may help to recall the identity $(n-1)S_X^2 = \sum_i X_i^2 - n\overline{X}^2$.

    **Note:** If you are wondering what it means for both $m$ and $n$ to go to $\infty$, you may assume that we have a sequence of problems indexed by $k=1,2,\ldots$ and $\min \{m_k,n_k\} \to \infty$ as $k\to\infty$. You should feel free to work more informally than this.

3.  Let $\hat\gamma = 1/(1+\hat\rho m/n)$ and assume that $m,n\to\infty$ with $m/n \to c \in (0,\infty)$. Show that the adaptive estimator $$\delta_{\hat\gamma}(X,Y) = \hat\gamma \overline X + (1-\hat\gamma) \overline Y$$ has an asymptotic normal distribution as $n,m\to \infty$, and give its asymptotic distribution after appropriately centering and scaling it. Compare the asymptotic distribution of the adaptive estimator $\delta_{\hat\gamma}(X,Y)$ to the asymptotic distribution of the oracle estimator $\delta_{\gamma^*}(X,Y)$.

    **Hint:** Start by considering the asymptotic distribution of $(\overline X, \overline Y)$. You may use without proof the result that if $Z_n \Rightarrow P$ and $W_n \Rightarrow Q$, and $Z_n$ and $W_n$ are independent for each $n$, then $(Z_n,W_n) \to P \times Q$ (meaning the product measure between the distributions $P$ and $Q$).

    **Note:** Again, if we want to set up a formal sequence of problems in which the distribution converges, we could assume the ratio $c_k = m_k/n_k$ is converging to $c \in (0,\infty)$, in addition to our previous assumption that $\min \{m_k,n_k\}\to\infty$. As before, you can also work more informally.

---

[Up: contents](index.md) · [Moral →](02-moral.md)
