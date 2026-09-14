---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework9.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework9.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework9.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework9.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

When we have paired data, we can often make much more precise comparisons between two distributions; even more precise than our ability to infer things about either of the distributions individually. This is often worth taking into account if we are designing an experiment: for example, if we match patients into pairs on demographic characteristics and then randomize a treatment/placebo assignment within each pair, we may get a very good inference about whether the treatment is better than the placebo, much better than we would get if we randomly assigned all $2n$ subjects independently of each other.

**Problem 4** (Nonparametric tests). In this problem you will design tests for two nonparametric hypothesis testing problems. There is necessarily some wiggle room in how you choose the test statistic, and it will probably not be possible to determine the cutoff explicitly. Just choose a reasonable one, define the cutoff in terms of a quantile of a well-defined distribution, and show that your test has significance level $\alpha$.

1.  Suppose $X_1,\ldots,X_n\in \mathbb{R}$ are independent random variables with $X_i \sim P_i$. Consider testing the null hypothesis $H_0:\; P_1=P_2=\cdots=P_n$ (i.e., the observations are i.i.d.) against the alternative that there is a systematic trend toward larger values of $X_i$ as $i$ increases (this is sometimes called a *test of trend*). Design a level-$\alpha$ test.

2.  Suppose $(X_1,Y_1),\ldots,(X_n,Y_n) \overset{\text{i.i.d.}}{\sim}P$ where $P$ is an unknown joint distribution on $\mathbb{R}^2$. Consider testing the null hypothesis that $X_i$ and $Y_i$ are independent within each pair (i.e., $P = P_X \times P_Y$, with $P_X$ and $P_Y$ unknown and not necessarily the same) versus the alternative that $(X_i,Y_i)$ are positively correlated within each pair. Design a level-$\alpha$ test.

Note that the alternative is defined a little vaguely in each part above. If that troubles you, we could formally take the alternative be “$P_i$ are arbitrary but not all equal” in part (a), or “$P \neq P_X \times P_Y$” in part (b). The alternative hypotheses as I’ve defined them informally are meant to suggest which alternatives to prioritize when you design your test.

---

[← Moral](03-moral.md) · [Up: contents](index.md) · [Moral →](05-moral.md)
