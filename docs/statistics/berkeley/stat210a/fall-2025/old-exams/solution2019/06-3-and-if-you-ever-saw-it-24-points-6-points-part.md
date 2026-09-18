---
title: 3. "And if you ever saw it..." (24 points, 6 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/solution2019.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/solution2019.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3. "And if you ever saw it..." (24 points, 6 points / part).

Some useful facts for this problem:
- For $n \in \{0, 1, \dots\}$ and $p \in [0, 1]^d$ with $\sum p_i = 1$, the multinomial density for $X \sim \text{Multinom}(n, p)$ is
  $$
  p_1^{x_1} \cdots p_d^{x_d} \frac{n!}{x_1! \cdots x_d!}, \quad \text{on } x \in \{0, \dots, n\}^d \text{ with } \sum_i x_i = n.
  $$

An ecologist is interested in estimating the total population of reindeer in a wildlife preserve near the North Pole. She makes two visits to the preserve on two consecutive days and looks for reindeer. Each time she finds a reindeer she marks it with a unique identifying tag, so she can tell if she sees the same reindeer twice (in ecology this type of study is called a capture-recapture or mark-recapture study).

Assume that the same population of $n$ of reindeer is present in the preserve on both days, and each reindeer on each day has the same probability $\pi \in (0, 1)$ of being seen by her, independently across the reindeer and the days (so the detections / non-detections are like $2n$ i.i.d. "coin flips" each with success probability $\pi$). Note that $n$ is the unknown parameter of interest and $\pi$ is an unknown nuisance parameter.

Let $N_{11}$ denote the number of reindeer she sees both days, $N_{10}$ the number she sees the first day not the second, and $N_{01}$ the number she sees the second day but not the first. (Note that $N_{00}$, the number of reindeer she sees on neither day, is not observed.)

(a) Write down the likelihood for the model as a function of $N_{01}, N_{10}$, and $N_{11}$ and show that $T = (N_{01} + N_{10}, N_{11})$ is a sufficient statistic for the model.

You do **NOT** need to show a sufficiency reduction from the Bernoulli model of detected/non-detected "coin flips" for each reindeer-day; after all we do not really get to observe the data for that model because we don't know how many reindeer went undetected on both days. Just start with $N_{01}, N_{10}, N_{11}$ as the data and $n$ and $\pi$ as the parameters.

(b) (*) Show that $T$ is minimal sufficient (for this part you may assume we already know it is sufficient).

(c) Define the estimator
$$
\hat{n} = \frac{(N_{01} + N_{10} + 2N_{11})^2}{4N_{11}}.
$$

---

Show that $\hat{n}$ is consistent in the sense that $\hat{n}/n \overset{p}{\to} 1$ as $n \to \infty$ with $\pi$ fixed.

(d) Find the asymptotic distribution of $\hat{n}$ from part (c) as $n \to \infty$ with $\pi$ fixed. You should center and scale appropriately so that it has a non-degenerate limiting distribution (that is, after centering and scaling it shouldn't converge in probability to a constant).

---

---

[← 2. Solution.](05-2-solution.md) · [Up: contents](index.md) · [3. Solution. →](07-3-solution.md)
