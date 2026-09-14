---
title: More features, the merrier?
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework2/homework2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# More features, the merrier?

**Source:** [`homeworks/homework2/homework2.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework2/homework2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

15. (2 pts)
Let $y_i$ be an arbitrary response, and $x_i \in \mathbb{R}^p$ be an arbitrary
feature vector, for $i = 1,\dots,n$. Let
$$
\tilde{x}_i = (x_{i1}, \dots, x_{ip}, \tilde{x}_{i,p+1}),\quad i = 1,\dots,n
$$
be the result of appending one more feature. Let $\hat{y}_i$ denote the fitted
values from the regression of $y_i$ on $x_i$, and let $\tilde{y}_i$ denote the
fitted values from the regression of $y_i$ on $\tilde{x}_i$. Prove that
$$
\sum_{i=1}^n (y_i - \tilde{y}_i)^2 \leq \sum_{i=1}^n (y_i - \hat{y}_i)^2.
$$
In other words, *the training MSE will never get worse as we add features* to a
given sample regression problem.

16. (2 pts)
How many linearly independent features do we need (how large should $p$ be) in
order to achieve a perfect training accuracy, i.e., training MSE of zero? Why?

17. (Bonus)
Implement an example in R in order to verify your answer to Q16 empirically.
Extra bonus points if you do it on the cardiovascular mortality data, using
enough lagged features. You should be able to plot the fitted values from the
training set and see that they match the observations perfectly (and the CV
predictions should look super wild).

---

[← Cross-validation](06-cross-validation.md) · [Up: contents](index.md)
