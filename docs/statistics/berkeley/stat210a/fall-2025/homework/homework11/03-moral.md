---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework11.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework11.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework11.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework11.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Our general formula for the asymptotic distribution of the MLE allows us to quickly get good asymptotic approximations to their distributions.

**Problem 3** (Limiting distribution of $U$-statistics).

Suppose $X_{1}, \ldots, X_{n} \overset{\text{i.i.d.}}{\sim}P$ in some sample space $\mathcal{X}$. $U_{n} = U_{n}(X_{1}, \ldots, X_{n})$ is called a rank-2 $U$-statistic if $$U_{n} = \frac{1}{n(n - 1)}\sum_{i=1}^{n}\sum_{j\neq i}h(X_{i}, X_{j})$$ where $h$ is a symmetric function, i.e. $h(x_{1}, x_{2}) = h(x_{2}, x_{1})$ for any $x_{1}, x_{2}\in\mathcal{X}$.

In this problem, we denote $\theta = \mathbb{E}h(X_{1}, X_{2})$ and assume that $\mathbb{E}h(X_{1}, X_{2})^{2} < \infty$. Note that $U_n$ is the nonparametric UMVU estimator of $\theta$.

Perhaps surprisingly, we can derive the asymptotic distribution of $U_n$ in a relatively small number of steps using a technique called *Hájek projection* where we approximate it by an additive function of the independent $X_i$ variables. We walk through the proof below.

1.  Define $g(x) = \mathbb{E}h(x, X_2) - \theta = \int h(x,u)\,d P(u) - \theta$. Show that, for all $i$, $$\mathbb{E}g(X_i) = 0, \quad \text{ and } \;\;\textnormal{Var}(g(X_i)) < \infty.$$ (**Note:** $g$ is a specific function from $\mathcal{X}$ to $\mathbb{R}$. It is not a rule for naively substituting symbols into expressions. In particular, note that $g(X_i)$, a random variable, is not the same as the deterministic expression $\mathbb{E}h(X_i, X_2)-\theta$.)

2.  Define $\widehat{U}_{n} = \theta + \frac{2}{n}\sum_{i=1}^{n}g(X_{i})$. Show that $\mathbb{E}[(U_n-\widehat{U}_n)f(X_i)]=0$ for any $i$ and any measurable function $f(X_i)$ with $\mathbb{E}[f(X_i)^2] < \infty$.

    (**Hint:** Condition on $X_i$)

3.  Show that ${\sqrt{n}(U_{n} - \widehat{U}_{n})\overset{p}{\to}0}$ as $n\to\infty$. (Hint: show that $U_n$ and $\widehat{U}_n$ have the same asymptotic variance, and then apply part (b)).

4.  Conclude that $\sqrt{n}(U_{n} - \theta)\Rightarrow N(0, 4\zeta_{1})$, where $\zeta_{1} = \textnormal{Var}(g(X_{1}))$.

5.  Assume that $\mathcal{X}= \mathbb{R}$ with $\mathbb{E}X_i^4 <\infty$. Express the sample variance $S_{n}^{2} = \frac{1}{n-1}\sum_{i=1}^{n}(X_{i} - \overline{X})^{2}$ as a rank-2 U-statistic and use the above results to derive its asymptotic distribution.

(**Note:** a similar result holds in general for rank-$r$ $U$-statistics if we set $\widehat{U}_n= \theta + \frac{r}{n}\sum_i g(X_i)$ where ${g(x) = \mathbb{E}[h(x,X_2,\ldots,X_r)]-\theta}$. )

---

[← Moral](02-moral.md) · [Up: contents](index.md) · [Moral →](04-moral.md)
