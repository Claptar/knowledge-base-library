---
title: 2. Multivariate normal means (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2023.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2023.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2. Multivariate normal means (20 points, 5 points / part).

Suppose that we observe two multivariate normal random vectors in $\mathbb{R}^d$, for $d \ge 3$:
$$X^{(i)} \stackrel{\text{ind.}}{\sim} N_d(\theta^{(i)}, \sigma^2 I_d), \quad \text{for } i = 1, 2.$$
where $\theta^{(1)}, \theta^{(2)} \in \mathbb{R}^d$ and $\sigma^2 > 0$, and $I_d$ is the $d \times d$ identity matrix.

For all parts below, if you refer to quantiles of a $t$, $\chi^2$, or $F$ distribution, you will need to give the relevant degrees of freedom in order to receive full credit.

(a) Assume (for this part only) that $\sigma^2$ is known but $\theta^{(1)}, \theta^{(2)}$ are unknown, and suggest a test of the hypothesis $H_0 : \theta^{(1)} = \theta^{(2)}$ (that $\theta^{(1)}_j = \theta^{(2)}_j$ for every $j = 1, \dots, d$) against the hypothesis that $\theta^{(1)} \ne \theta^{(2)}$ (that $\theta^{(1)}_j \ne \theta^{(2)}_j$ for at least one $j = 1, \dots, d$). Give your test statistic and a rejection cutoff in terms of a quantile of a $\chi^2$ distribution.

**Solution:**
We can define the variable $Y = X^{(2)} - X^{(1)} \sim N_d(\theta^{(2)}_j - \theta^{(1)}_j, 2\sigma^2 I_d)$. Under the null hypothesis, $\frac{1}{2\sigma^2} \|Y\|^2 \sim \chi^2_d$, so we can reject when this statistic is above the upper-$\alpha$ quantile of that distribution.

(b) Now drop the assumption that $\sigma^2$ is known (i.e. now it is **unknown**), and assume (for this and the next part only) that $\theta^{(2)}_j = \theta^{(1)}_j + \delta$, for some $\delta \in \mathbb{R}$ (i.e. every coordinate is shifted by the same amount $\delta$), but apart from this assumption, both $\theta^{(1)}$ and $\theta^{(2)}$ are unknown. Propose a finite-sample test of $H_0 : \delta = 0$ against the two-sided alternative $H_1 : \delta \ne 0$. Give a test statistic and cutoffs in terms of a quantile of a specific distribution.

**Note:** You do not need to prove any optimality properties for your test, but you won't receive full credit if you trivialize the problem by giving an inefficient test, even if the test is valid in the Type I error sense.

**Solution:**
Working with the same $Y$, we have $Y \sim N_d(\delta \mathbf{1}_d, 2\sigma^2 I_d)$. This is just the setup for a one-sample $t$-test, so we reject if $\frac{|\overline{Y}|}{\sqrt{S^2/d}}$ is above the upper-$\alpha/2$ quantile of a $t_{d-1}$ distribution, where $\overline{Y} = \frac{1}{d} \sum_j Y_j \sim N(\delta, 2\sigma^2/d)$ and $S^2 = \frac{1}{d-1} \sum_j (Y_j - \overline{Y})^2 \sim \frac{2\sigma^2}{d-1} \chi^2_{d-1}$, independently.

(c) Under the same assumptions as in part (b), propose a confidence interval for $\delta$. If you didn't solve part (b), or if you are not confident in your answer, you may assume that there is a valid test statistic from part (b) of the form $T(X^{(1)}, X^{(2)})$, and (non-data-dependent) cutoff values $c_1(\alpha)$ and $c_2(\alpha)$ (so the test rejects if $T < c_1$ or $T > c_2$), and give your answer in terms of these.

**Solution:**
If we want to test the point null $\delta = \delta_0$, we can just shift the problem to get $Y - \delta_0 \mathbf{1}_d \sim N_d((\delta - \delta_0)\mathbf{1}_d, 2\sigma^2 I_d)$. So we want to invert the test that rejects when $\frac{|\overline{Y} - \delta_0|}{\sqrt{S^2/d}} > t_{d-1}(\alpha/2)$. In other words, our interval should be
$$\overline{Y} \pm \sqrt{S^2/d} \cdot t_{d-1}(\alpha/2).$$

(d) (*) Now, drop the assumption about $\delta$ from the previous parts, so $\theta^{(1)}$ and $\theta^{(2)}$ are again completely unknown. And now assume (for this part only) that $\sigma^2 = 1$. Also, suppose that we believe $\theta^{(1)} \approx \theta^{(2)}$ as vectors in $\mathbb{R}^d$, but we do not have any other strong priors about it. Suggest an estimator that will have MSE less than $2d$ for all values of $\theta^{(1)}, \theta^{(2)}$, but which will have MSE $d + 2$ whenever $\theta^{(1)} = \theta^{(2)}$.

**Note:** You do not need to prove that your estimator has these properties, it is sufficient to give a correct functional form for the estimator.

**Solution:**
Let $Z = Y/\sqrt{2}$ so it has an identity covariance. We want to use a James-Stein estimator for the mean of $Z$ (which will be 0 if we're lucky) and the MLE for the mean of $W = (X^{(1)} + X^{(2)})/\sqrt{2} \sim N_d(\theta^{(1)} + \theta^{(2)}, I_d)$. Note $Z$ and $W$ are independent, which we can verify by noting that they represent two orthogonal projections of $(X^{(1)}, X^{(2)})$. Let $\mu$ denote the mean of $Z$, and $\nu$ the mean of $W$. Then $\hat{\nu} = W$ and
$$\hat{\mu} = \left( 1 - \frac{d - 2}{\|Z\|^2} \right) Z = \left( 1 - \frac{2d - 4}{\|X^{(2)} - X^{(1)}\|^2} \right) \frac{X^{(2)} - X^{(1)}}{\sqrt{2}}.$$
Since $\theta^{(2)} = (\mu + \nu)/\sqrt{2}$ and $\theta^{(1)} = (-\mu + \nu)/\sqrt{2}$, we have
$$\hat{\theta}^{(2)} = \frac{\hat{\mu} + W}{\sqrt{2}} = \frac{X^{(1)} + X^{(2)}}{2} + \left( 1 - \frac{2d - 4}{\|X^{(2)} - X^{(1)}\|^2} \right) \frac{X^{(2)} - X^{(1)}}{2},$$
and
$$\hat{\theta}^{(1)} = \frac{-\hat{\mu} + W}{\sqrt{2}} = \frac{X^{(1)} + X^{(2)}}{2} - \left( 1 - \frac{2d - 4}{\|X^{(2)} - X^{(1)}\|^2} \right) \frac{X^{(2)} - X^{(1)}}{2},$$
The MSE for estimating $(\theta^{(1)}, \theta^{(2)})$ is the sum of the MSEs for the two estimators $\hat{\mu}$ and $\hat{\nu}$. The second has MSE $d$ and the first has MSE strictly less than $d$, equaling 2 if $\mu = 0$.

---

[← 1. Laplace Location Family (24 points, 4 points / part).](02-1-laplace-location-family-24-points-4-points-part.md) · [Up: contents](index.md) · [3. Nonparametric two-sample problem (20 points, 5 points / part). →](04-3-nonparametric-two-sample-problem-20-points-5-points-part.md)
