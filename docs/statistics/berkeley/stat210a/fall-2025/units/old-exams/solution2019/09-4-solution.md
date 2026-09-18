---
title: 4. Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2019.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2019.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4. Solution

(a) The log likelihood is
$$
\frac{1}{2\sigma^2} \sum_{i=1}^n \left[ \frac{(Y_i - g(\alpha + \beta x_i))^2}{h(x_i)} - \frac{1}{2} \log(2\pi\sigma^2 h(x_i)) \right]
$$
The first derivative with respect to $\alpha$ is
$$
\frac{1}{\sigma^2} \sum_{i=1}^n \left[ (Y_i - g(\alpha + \beta x_i)) \frac{\dot{g}(\alpha + \beta x_i)}{h(x_i)} \right] = \frac{1}{\sigma^2} \sum_i r_i w_i,
$$
for $w_i = \dot{g}(\alpha + \beta x_i)/h(x_i)$. Similarly, the gradient with respect to $\beta$ is
$$
\frac{1}{\sigma^2} \sum_{i=1}^n r_i w_i x_i.
$$
Any local minimizer of the log-likelihood sets the gradient equal to zero. (Remark: we gave full credit for just setting the derivative to zero, but the question statement should have been clearer about the difference between local optimality and global optimality: it is a necessary but not sufficient condition that the gradient should be zero, but it is possible for there to be more than one local minimum. It is also possible, I realized later, to come up with counterexamples where there is no MLE because the likelihood is maximized at infinity.)

Note that our estimate of $\sigma^2$ plays no role in determining $\hat{\alpha}$ and $\hat{\beta}$; we would get the same estimators for $\alpha$ and $\beta$ whether we estimate $\sigma^2$ or whether it is known. This will be useful in part (c).

(b) Differentiating with respect to $\sigma^2$ gives
$$
-\frac{1}{2\sigma^4} \sum_{i=1}^n \left[ \frac{(Y_i - g(\alpha + \beta x_i))^2}{h(x_i)} \right] - \frac{n}{2\sigma^2},
$$
and setting the derivative equal to 0 while the other parameters are at their MLEs gives
$$
\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^n \left[ \frac{(Y_i - g(\hat{\alpha} + \hat{\beta} x_i))^2}{h(x_i)} \right]
$$

---

(c) First assume $\sigma^2 > 0$ is known. Then the only two unknown parameters are $\alpha$ and $\beta$, and the score is
$$
\frac{1}{\sigma^2} \left( \sum_i r_i w_i, \sum_i r_i w_i X_i \right).
$$
The variance of the score conditional on $X$ is
$$
\begin{aligned}
\text{Var}\left( \sum_i (Y_i - g(\alpha + \beta X_i)) \frac{\dot{g}(\alpha + \beta X_i)}{\sigma^2 h(X_i)} \begin{pmatrix} 1 \\ X_i \end{pmatrix} \;\middle|\; X_i \right) &= \sum_i \frac{\dot{g}(\alpha + \beta X_i)^2}{\sigma^4 h(X_i)^2} \text{Var}(Y_i - g(\alpha + \beta X_i) \mid X_i) \begin{pmatrix} 1 & X_i \\ X_i & X_i^2 \end{pmatrix} \\
&= \sum_i \frac{\dot{g}(\alpha + \beta X_i)^2}{\sigma^2 h(X_i)} \begin{pmatrix} 1 & X_i \\ X_i & X_i^2 \end{pmatrix}.
\end{aligned}
$$
The expectation of the score given $X$ is zero, so the marginal variance is simply the expectation of the conditional variance:
$$
J(\alpha, \beta) = \text{Var}_{\alpha,\beta}(\nabla \ell(\alpha, \beta)) = \frac{n}{\sigma^2} \mathbb{E} \left[ \frac{\dot{g}(\alpha + \beta X_i)^2}{h(X_i)} \begin{pmatrix} 1 & X_i \\ X_i & X_i^2 \end{pmatrix} \right].
$$
Note that the exam should have guaranteed $h(X_i)$ didn't have positive density at zero; that could make the expectation infinite. Assuming it is not infinite though, and the conditions hold for our theorem on the asymptotic distribution, then we have
$$
\sqrt{n} \left( \begin{pmatrix} \hat{\alpha} \\ \hat{\beta} \end{pmatrix} - \begin{pmatrix} \alpha \\ \beta \end{pmatrix} \right) \Rightarrow N_2(0, J(\alpha, \beta)^{-1}).
$$
If instead $\sigma^2$ is unknown, nothing actually changes because, as noted in part (a), the MLE $(\hat{\alpha}, \hat{\beta})$ is the same regardless of $\sigma^2$, which merely scales the log-likelihood up or down. Since it is the same random variable regardless of whether $\sigma^2$ is known or estimated, it also has the same limiting distribution regardless.

(d) Let $\mu_i = g(\alpha + \beta x_i)$ and assume without loss of generality that $\mu_i$ is non-decreasing in $i$. If $\beta = 0$ then $\mu_1 = \dots = \mu_n$ and the $Y_i$ values are i.i.d., but if $\beta > 0$ then the means are increasing too (and if $\beta < 0$ the means are decreasing). We can use a permutation test whose test statistic is meant to pick up correlation between $x$ and $\mu$, for example $T(Y) = x'Y$. We use a Monte Carlo version of the permutation test

---

as usual: take $B$ random permutations and reject if $T(Y)$ is among the $\lfloor a(B + 1) \rfloor$ largest of $T(Y), T(\pi_1 Y), \dots, T(\pi_B Y)$.

If $Y_i = \mu_i + \varepsilon_i$ and assume $\beta \le 0$. Then for a generic permutation $\pi$,
$$
T(\pi Y) = x'(\pi \mu) + x'(\pi \varepsilon).
$$
Note that $(x'\varepsilon, x'(\pi_1 \varepsilon), x'(\pi_B \varepsilon))$ are exchangeable no matter what, but $x'\mu \le x'(\pi \mu)$ for all $\pi$; therefore $T(Y)$ has a less than $a$ chance of being among the $\lfloor a(B + 1) \rfloor$ largest values.

---

[← 4. Nonlinear regression (24 points, 6 points / part).](08-4-nonlinear-regression-24-points-6-points-part.md) · [Up: contents](index.md)
