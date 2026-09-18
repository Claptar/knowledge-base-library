---
title: 2. Solution.
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2019.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2019.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2. Solution.

(a) $\overline{X}_i$ and $S_i^2$ are both functions of $(X_{i1}, \dots, X_{in})$, which are mutually independent across $i = 1, \dots, m$. Furthermore, $\overline{X}_i$ and $S_i^2$ are independent of each other within each $i$, as we have shown by e.g. Basu's theorem. Hence $(\overline{X}_1, \dots, \overline{X}_m, S_1^2, \dots, S_m^2)$ are $2m$ independent random variables, with
$$
\begin{aligned}
\overline{X}_i &\overset{\text{i.i.d.}}{\sim} N(\mu, \tau^2 + \sigma^2/n) \\
S_i^2 &\overset{\text{i.i.d.}}{\sim} \frac{\sigma^2}{n - 1} \chi_{n-1}^2.
\end{aligned}
$$
As a result, $S_B^2 \sim \frac{\tau^2 + \sigma^2/n}{m-1} \chi_{m-1}^2$, and it is independent of $(S_1^2, \dots, S_m^2)$ because it is a function of $(\overline{X}_1, \dots, \overline{X}_m)$.

(b) Because $\overline{X} = N(\mu, \tau^2/m + \sigma^2/nm)$, we have
$$
\sqrt{m} \frac{\overline{X} - \mu}{\sqrt{S_B^2}} \sim t_{m-1}.
$$
As a result, $\overline{X} \pm \sqrt{\frac{S_B^2}{m}} t_{m-1}(\alpha/2)$ is an exact $1 - \alpha$ confidence interval.

(c) (**Common mistake:** Note that we cannot use $S_B^2$ alone to do this test because its distribution depends on the nuisance parameter $\tau^2$.)

Combining evidence across the within-group sample variances gives us the combined within-group variance
$$
S_W^2 = \frac{1}{m} \sum_i S_i^2 \sim \frac{\sigma^2}{m(n - 1)} \chi_{m(n-1)}^2.
$$
Because $S_W^2$ is independent of $S_B^2$, we have
$$
\frac{S_B^2}{S_W^2} \sim \frac{\tau^2 + \sigma^2/n}{\sigma^2} F_{m-1, m(n-1)} = (\tau^2/\sigma^2 + n^{-1}) F_{m-1, m(n-1)}.
$$
As a result,
$$
n S_B^2 / S_W^2 \sim (n\tau^2/\sigma^2 + 1) F_{m-1, m(n-1)} \overset{H_0}{=} F_{m-1, m(n-1)}
$$
so we can reject the null when that statistic is above $F_{m-1, m(n-1)}(\alpha)$.

---

(d) Using the same logic, for $\tau > 0$ we can get an equal tailed test of $H_0 : \tau^2/\sigma^2 = \rho$ vs. the two-sided alternative $H_1 : \tau^2/\sigma^2 \ne \rho$ by rejecting when $T_\rho = \frac{n}{n\rho + 1} S_B^2 / S_W^2$ is either above $a = F_{m-1, m(n-1)}(\alpha/2)$ or below $b = F_{m-1, m(n-1)}(1 - \alpha/2)$. Hence the acceptance region is
$$
\left\{ b \le \frac{n}{n\rho + 1} S_B^2 / S_W^2 \le a \right\}
$$
leading to confidence interval
$$
C(X) = \left[ \frac{S_B^2}{a S_W^2} - \frac{1}{n}, \; \frac{S_B^2}{b S_W^2} - \frac{1}{n} \right].
$$

(e) Let $X_i = (X_{i1}, \dots, X_{in})$ denote the $i$th group of observations. The $X_i$ are independent multivariate Gaussians with mean $\mu \mathbf{1} = (\mu, \dots, \mu)$ and covariance matrix $\Sigma = \sigma^2 I_n + \tau^2 \mathbf{1}\mathbf{1}'$ (that is, the variance of $X_{ij}$ is $\sigma^2 + \tau^2$ and the within-group covariance is $\tau^2$). The inverse covariance matrix has the same form: $\Sigma^{-1} = \theta I_n + \zeta \mathbf{1}\mathbf{1}'$ for some $\theta(\tau^2, \sigma^2) > 0$, $\zeta(\tau^2, \sigma^2) < 0$.

As a result, the likelihood is
$$
\begin{aligned}
p(X) &= (2\pi)^{-nm/2} \prod_{i=1}^m \exp \left\{ -\frac{1}{2} (X_i - \mu \mathbf{1})' \Sigma^{-1} (X_i - \mu \mathbf{1}) \right\} \\
&= (2\pi)^{-nm/2} \prod_{i=1}^m \exp \left\{ \theta \|X_i\|^2/2 - \zeta \left( \sum_j X_{ij} \right)^2 / 2 + (n\mu\zeta + \mu\theta) \sum_j X_{ij} - A(\theta, \zeta, \mu) \right\} \\
&= (2\pi)^{-nm/2} \exp \left\{ \theta \sum_i \|X_i\|^2/2 - \zeta \frac{n^2}{2} \sum_i \overline{X}_i^2 + nm(n\mu\zeta + \mu\theta)\overline{X} - A(\theta, \zeta, \mu) \right\}.
\end{aligned}
$$
This is a full-rank three-parameter exponential family because the natural parameter space contains an open set, so $T = \left( \sum_i \|X_i\|^2, \sum_i \overline{X}_i^2, \overline{X} \right)$ is a complete sufficient statistic.

We have shown in class that $(m - 1)S_B^2 + m\overline{X}^2 = \sum_i \overline{X}_i^2$, and $(n - 1)S_i^2 + n\overline{X}_i^2 = \|X_i\|^2$. Therefore, we can reconstruct $\left( \overline{X}, S_B^2, \sum_i S_i^2 \right)$ from $T$ and vice-versa.

---

---

[← 2. ANOVA with random effects (25 points, 5 points / part).](04-2-anova-with-random-effects-25-points-5-points-part.md) · [Up: contents](index.md) · [3. "And if you ever saw it..." (24 points, 6 points / part). →](06-3-and-if-you-ever-saw-it-24-points-6-points-part.md)
