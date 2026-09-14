---
title: Homework7 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework7.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework7.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework7 Part 01 —

**Source:** [`homework/homework7.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework7.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

See the standing homework instructions on the course web page

**Problem 1** (Minimax estimation for the exponential).

Assume we observe $X\sim \text{Exp}(\theta)$ and want to

In this problem we’ll consider minimax estimation of $\theta$ in the exponential scale family $$X \sim \text{Exp}(\theta) = \frac{1}{\theta}e^{-x/\theta}, \quad x>0,$$ under the relative squared error loss $L(\theta, d) = \left(\frac{d-\theta}{\theta}\right)^2$. The mean and variance of an $\text{Exp}(\theta)$ random variable are $\theta$ and $\theta^2$, respectively.

1.  Consider linear scaling estimators of the form $\delta(x) = cx$, for $c\in[0,1]$. Show that one of these estimators dominates all others, find the optimal $c$ and give its risk function.

2.  A conjugate prior for this problem is the inverse-Gamma prior, which has parameters $\alpha,\beta>0$ and density $$\theta \sim \text{Inv-Gamma}(\alpha,\beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} \theta^{-\alpha-1}e^{-\beta/\theta}.$$ Note $\theta\sim \text{Inv-Gamma}(\alpha,\beta)$ when $\theta^{-1}\sim \text{Gamma}(\alpha,1/\beta)$. Find the posterior distribution and Bayes estimator.

    **Note:** Since we are not using squared error loss, the Bayes estimator is not just the posterior mean.

    **Hint:** It may help to recall that if $Y \sim\text{Gamma}(k,\sigma)$ then $\mathbb{E}Y = k\sigma$ and $\textnormal{Var}(Y)=k\sigma^2$.

3.  Find the Bayes risk for the inverse-Gamma prior with parameters $\alpha,\beta$.

4.  Use the previous results to show that your estimator from part (a) is minimax.

5.  Now find the objective Bayes estimator, using the Jeffreys prior, and give its risk function. Can you relate the result to the results in the previous parts?

    **Hint:** It may help to recall the general result you showed on a previous homework regarding the Jeffreys prior for scale families.

---

[Up: contents](index.md) · [Moral →](02-moral.md)
