---
title: Homework9 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework9.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework9.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework9 Part 01 —

**Source:** [`homework/homework9.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework9.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

See the standing homework instructions on the course web page

**Problem 1** (Fisher’s exact test). Suppose $X_i \sim \text{Binom}(n_i, \pi_i)$ independently for $i=0,1$ and $\pi_0,\pi_1\in(0,1)$. Consider testing $H_0:\; \pi_1\leq \pi_0$ vs. $H_1:\; \pi_1 > \pi_0$.

1.  A natural object of inference in this model is the *odds ratio*: $$\rho = \frac{\pi_1/(1-\pi_1)}{\pi_0/(1-\pi_0)}.$$ Write the model in exponential family form with $\theta=\log\rho$ as one of the natural parameters, and reframe $H_0$ as an equivalent hypothesis about $\theta$.

2.  The hypergeometric distribution $\text{Hypergeom}(N,K,n)$ describes the probability distribution for sampling $n$ binary values without replacement from a finite population of $N$ binary values, of which $K$ are equal to $1$ and the other $N-K$ are equal to $0$. If $X$ is the number of successes in the subsample, its probability mass function is $$p_{N,K,n}(x) = \frac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}}, \quad \text{ for } x = \max\{0,n+K-N\}, \ldots, \min\{K,n\}.$$ Find the UMPU level-$\alpha$ test of $H_0$ in part (a), show that the test statistic has a hypergeometric distribution for appropriate $N,K,n$, and describe how to find the cutoffs $c(u), \gamma(u)$.

3.  Find the conditional distribution of your test statistic for general $\theta$. Note you do not need to find a closed-form expression for the normalizing constant.

4.  Suppose $n_0=n_1=40$, $X_0=18$ and $X_1=7$. Give a $95\%$ confidence interval for the odds ratio $\rho$ by numerically inverting the two-sided, equal-tailed, conditional test of $H_0:\; \rho=\rho_0$ vs. $H_1:\; \rho \neq \rho_0$. Don’t randomize the interval, just return the conservative non-randomized interval. (Hint: it is equivalent to set up the problem in terms of $\theta$, and may be a little easier to think about that way.)

---

[Up: contents](index.md) · [Moral →](02-moral.md)
