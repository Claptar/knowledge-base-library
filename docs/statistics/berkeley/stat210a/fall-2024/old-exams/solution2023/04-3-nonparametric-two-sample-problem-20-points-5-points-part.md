---
title: 3. Nonparametric two-sample problem (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2023.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3. Nonparametric two-sample problem (20 points, 5 points / part).

Some useful facts you may assume are true for this problem:

- In the one-sample model with $X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} P$, with the $X_i$ observations taking values in $\mathbb{R}$ and no further assumptions on the distribution $P$, the order statistics
$$S(X) = (X_{(1)}, \dots, X_{(n)})$$
are complete sufficient.

- If $Z_n \Rightarrow Z$ and $W_n \Rightarrow W$, and $Z_n$ is independent of $W_n$ for every $n$, then $(Z_n, W_n) \Rightarrow (Z, W)$ where $Z$ is independent of $W$.

Assume we have a non-parametric two-sample problem of the form
$$X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} P, \quad \text{and} \quad Y_1, \dots, Y_n \stackrel{\text{i.i.d.}}{\sim} Q,$$
independently, where all $X_i$ and $Y_i$ take values in $\mathbb{R}$. You may assume, without proving, that $(S(X), S(Y))$ is complete sufficient for the full model.

(a) Define the estimand $g(P, Q) = \mathbb{P}_{X\sim P, Y\sim Q}(X > Y)$, i.e. the probability that an observation from $P$ is larger than an independent observation from $Q$. Find the UMVU estimator for $g(P, Q)$ and explain why it is UMVU.

**Solution:**
We have an unbiased estimator in $\mathbf{1}\{X_1 > Y_1\}$, so all we need to do is Rao-Blackwellize it conditional on $S(X)$ and $S(Y)$. Conditional on these statistics, $X_1$ and $Y_1$ are independently uniform draws from $S(X)$ and $S(Y)$, so the UMVU estimator is
$$\frac{1}{n^2} \sum_{i,j=1}^n \mathbf{1}\{X_i > Y_j\}.$$
**Common errors:** Note that $\frac{1}{n} \sum_i \mathbf{1}\{X_i > Y_i\}$ would not be correct; it is unbiased but cannot be calculated from the complete sufficient statistic. And $\frac{1}{n} \sum_i \mathbf{1}\{X_{(i)} > Y_{(i)}\}$ is not even unbiased. However, the estimator $\frac{1}{n^2} \sum_{i,j=1}^n \mathbf{1}\{X_{(i)} > Y_{(j)}\}$ is correct; students who gave this answer or another equivalent answer got full credit as long as each of the $n^2$ pairs of $X$ and $Y$ values are represented once.

(b) Define $\mu = \mathbb{E}_P X$, $\nu = \mathbb{E}_Q Y$, $\sigma^2 = \text{Var}_P(X)$, and $\tau^2 = \text{Var}_Q(Y)$. Show that $T(X, Y) = (\overline{X}/\overline{Y})^2$ is a consistent estimator for $\theta = (\mu/\nu)^2$ as $n \to \infty$, assuming $\nu > 0$ and $\sigma^2, \tau^2 \in (0, \infty)$.

**Solution:**
This follows from the continuous mapping theorem after observing that $\overline{X} \to \mu$ and $\overline{Y} \to \nu$ in probability, by the law of large numbers, and the function $f(x, y) = (x/y)^2$ is continuous everywhere except where $y = 0$.

**Common "error":** The function $f$ is not continuous everywhere. If you said or implied in your answer that the function $f$ was continuous, without the caveat that the denominator must be nonzero (i.e. that $\nu > 0$), I deducted 1 point out of 5. I made exceptions in rare cases where it seemed that something else in the answer made implicit reference to $\nu > 0$ being necessary.

(c) Give the asymptotic distribution of $T(X, Y)$ as $n \to \infty$, appropriately normalized so that the error has a nondegenerate distribution, and justify your answer. Your answer should be given as a distribution whose parameters are explicit functions of $\mu, \nu, \tau^2, \sigma^2$, and $\theta$.

**Solution:**
For this, we have $\sqrt{n}(\overline{X}_n - \mu) \Rightarrow N(0, \sigma^2)$ and $\sqrt{n}(\overline{Y}_n - \nu) \Rightarrow N(0, \tau^2)$, so we can apply the delta method to $\sqrt{n} \left( \begin{pmatrix} \overline{X}_n \\ \overline{Y}_n \end{pmatrix} - \begin{pmatrix} \mu \\ \nu \end{pmatrix} \right) \Rightarrow N_2(0, D)$ for $D = \begin{pmatrix} \sigma^2 & 0 \\ 0 & \tau^2 \end{pmatrix}$. The function is $f(x, y) = (x/y)^2$, whose gradient (for $y \ne 0$) is $\nabla f(x, y) = (2x/y^2, -2x^2/y^3)$. As a result we have
$$\sqrt{n}(T - \theta) \Rightarrow N(0, \omega^2),$$
where
$$\omega^2 = \nabla f(\mu, \nu)' D \nabla f(\mu, \nu) = 4 \left( \frac{\mu^2\sigma^2}{\nu^4} + \frac{\mu^4\tau^2}{\nu^6} \right) = \frac{4}{\nu^2} (\theta\sigma^2 + \theta^2\tau^2).$$
**Grading note:** If you missed that we need $\nu > 0$ in (b) I didn't take points off again. If you didn't miss it in (b), then I assumed you knew it in (c). So this detail played no role in grading this part.

(d) (*) If $\mu = \nu = 0$, give the asymptotic distribution of $T(X, Y)$ as $n \to \infty$, normalized appropriately if necessary. Justify your answer.

**Solution:**
In this case we have $Z = \sqrt{n} \begin{pmatrix} \overline{X}_n \\ \overline{Y}_n \end{pmatrix} \Rightarrow N_2(0, D)$. By the continuous mapping theorem, then, $T = (Z_1/Z_2)^2 \Rightarrow \frac{\sigma^2}{\tau^2} F_{1,1}$.

**Note:** This part was graded more leniently than part (b) since I essentially gave full marks to anyone who got to the right answer, but there is a slight subtlety about applying the continuous mapping theorem here, which is worth mentioning. Why shouldn't we care about the discontinuity point anymore? The condition for the theorem can be relaxed to say just that the set of discontinuity points of the function $f$ has measure zero in the limiting probability distribution (this would not be true in part (b) where we were appealing to the fact that $\overline{X}_n \to \nu$ in probability. If you noticed this issue (and I don't think anyone mentioned it for this part) and wanted to show convergence more directly, you could replace $T$ with a truncated version $T_B(X, Y) = \min(T, B)$, since $f(x, y) = \min((x/y)^2, B)$ is continuous. Then we would have $T_B \Rightarrow \min(F_{1,1}, B)$ for every $B$, which means the cdf of $T$ is converging everywhere to the (continuous) $F_{1,1}$ cdf. But again, this level of detail was not necessary for full marks.

---

[← 2. Multivariate normal means (20 points, 5 points / part).](03-2-multivariate-normal-means-20-points-5-points-part.md) · [Up: contents](index.md) · [4. Bayes estimation for Uniform Scale family (20 points, 5 points / part). →](05-4-bayes-estimation-for-uniform-scale-family-20-points-5-poin.md)
