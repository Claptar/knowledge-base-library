---
title: 4 Two AR(1) Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeventeen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSeventeen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Two AR(1) Models

We therefore have two different versions of AR(1) corresponding to each of the likelihoods (6) and (7).

The first version is:
$$
\begin{aligned}
&y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t \quad \text{for } t = 2, \dots, n \\
&\epsilon_t \text{ independent of } y_1, \dots, y_{t-1} \quad \text{for } t = 2, \dots, n \\
&\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2) \text{ and } y_1 \text{ is a constant.}
\end{aligned}
$$

The second version assumes
$$
y_1 = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{1-j}.
$$

Note that this, along with $y_2 = \phi_0 + \phi_1 y_1 + \epsilon_2$ implies that
$$
y_2 = \phi_0 + \phi_1 \left( \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{1-j} \right) + \epsilon_2 = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{2-j}.
$$
By induction, one can show that
$$
y_t = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}.
$$
So the second version of the AR(1) model can be simply written as:
$$
y_t = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j} \quad \text{for all } t = \dots, -3, -2, -1, 0, 1, 2, 3, \dots \tag{8}
$$
where $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. Note that this equation automatically satisfies: $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$ and also that $\epsilon_t$ is independent of $y_{t-1}, y_{t-2}, \dots$.

It is important to note that the second model (8) only makes sense when $|\phi_1| < 1$. So this second definition is not valid unless $|\phi_1| < 1$. When $|\phi_1| = 1$, one cannot make sense of the right hand side of (8) (this is becase $\sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}$ fails to converge when $|\phi_1| \ge 1$).

We shall see in the next lecture that (8) is an example of a stationary model. We will explore in depth the notion of stationarity.

## References

[1] Shumway, R. H. and D. S. Stoffer (2010). *Time series analysis and its applications: with R examples* (fourth ed.). Springer Science & Business Media.

---

[← 3 Likelihood for AR(1)](03-3-likelihood-for-ar-1.md) · [Up: contents](index.md)
