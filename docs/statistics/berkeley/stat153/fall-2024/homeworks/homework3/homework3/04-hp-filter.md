---
title: HP filter
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# HP filter

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

7. (5 pts)
Recall in lecture we saw the HP filter could be written explicitly as
$$
\hat\theta = \underbrace{(I + \lambda D^T D)^{-1}}_K \, y,
$$
where $D \in \mathbb{R}^{(n-2) \times n}$ is the second difference matrix on $n$
points. In other words, defining $K \in \mathbb{R}^{n \times n}$ as above,
$$
\hat\theta_i = \sum_{j=1}^n K_{ij} y_j, \quad i = 1,\dots,n.
$$
Compute the matrix $K$ empirically for a problem of size $n=100$, and setting
the tuning parameter to be $\lambda=100$; inspect three of its rows, at indices
$i = 25, 50, 75$. For each $i$, plot the $i^{\text{th}}$ row as a curve over the
underlying position $1,\dots,n$; that is, plot the x-y pairs
$$
(x_j, y_j) = (j, K_{ij}), \quad j = 1,\dots,n
$$
as a curve. Overlay the curves for all three rows on the same plot, each in a
different color. What do these curves look like to you? Use the plot to argue
that the HP filter acts like a kernel smoother.

8. (Bonus)
Do a literature search to find theory on the *asymptotically equivalent kernel*
for the HP filter. This should have a closed-form. Plot this and comment on
whether or not your empirical results adhere to what is known asymptotically.

---

[← Ridge and lasso](03-ridge-and-lasso.md) · [Up: contents](index.md) · [Trend filter →](05-trend-filter.md)
