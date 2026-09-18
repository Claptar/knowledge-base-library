---
title: 1 Bayesian Inference for Simple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Bayesian Inference for Simple Linear Regression

## Lecture Four
Fall 2025, UC Berkeley

Aditya Guntuboyina

September 9, 2025

We use the prior
$$
\beta_0, \beta_1, \log \sigma \stackrel{\text{i.i.d}}{\sim} \text{Unif}(-C, C)
$$
for a large number $C$ (the exact value of $C$ will not matter in the following calculations). Note that as $\sigma$ is always positive, we have made the uniform assumption on $\log \sigma$ (by the change of variable formula, the density of $\sigma$ would be given by $f_{\sigma}(x) = f_{\log \sigma}(\log x) \frac{1}{x} = \frac{I\{-C < \log x < C\}}{2Cx} = \frac{I\{e^{-C} < x < e^C\}}{2Cx}$).

The joint posterior for all the unknown parameters $\beta_0, \beta_1, \sigma$ is then given by (below we write the term "data" for $y_1, \dots, y_n$):
$$
f_{\beta_0, \beta_1, \sigma|\text{data}}(\beta_0, \beta_1, \sigma) \propto f_{y_1, \dots, y_n|\beta_0, \beta_1, \sigma}(y_1, \dots, y_n) f_{\beta_0, \beta_1, \sigma}(\beta_0, \beta_1, \sigma).
$$
The two terms on the right hand side above are the likelihood:
$$
f_{y_1, \dots, y_n|\beta_0, \beta_1, \sigma}(y_1, \dots, y_n) \propto \sigma^{-n} \exp \left( -\frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 \right) = \sigma^{-n} \exp \left( -\frac{S(\beta_0, \beta_1)}{2\sigma^2} \right),
$$
and the prior:
$$
\begin{aligned}
f_{\beta_0, \beta_1, \sigma}(\beta_0, \beta_1, \sigma) &= f_{\beta_0}(\beta_0) f_{\beta_1}(\beta_1) f_{\sigma}(\sigma) \\
&\propto \frac{I\{-C < \beta_0 < C\}}{2C} \frac{I\{-C < \beta_1 < C\}}{2C} \frac{I\{e^{-C} < \sigma < e^C\}}{2C\sigma} \\
&\propto \frac{1}{\sigma} I\{-C < \beta_0, \beta_1, \log \sigma < C\}.
\end{aligned}
$$
Recall that $S(\beta_0, \beta_1)$ denotes the sum of squares:
$$
S(\beta_0, \beta_1) := \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2.
$$
We thus obtain
$$
f_{\beta_0, \beta_1, \sigma|\text{data}}(\beta_0, \beta_1, \sigma) \propto \sigma^{-n-1} \exp \left( -\frac{S(\beta_0, \beta_1)}{2\sigma^2} \right) I\{-C < \beta_0, \beta_1, \log \sigma < C\}.
$$

The above is the joint posterior over $\beta_0, \beta_1, \sigma$. The posterior over only the main parameters $\beta_0, \beta_1$ can be obtained by integrating (or marginalizing) the parameter $\sigma$.
$$
\begin{aligned}
f_{\beta_0, \beta_1|\text{data}}(\beta_0, \beta_1) &= \int f_{\beta_0, \beta_1, \sigma|\text{data}}(\beta_0, \beta_1, \sigma) d\sigma \\
&\propto I\{-C < \beta_0, \beta_1 < C\} \int_{e^{-C}}^{e^C} \sigma^{-n-1} \exp \left( -\frac{S(\beta_0, \beta_1)}{2\sigma^2} \right) d\sigma.
\end{aligned}
$$
When $C$ is large, the above integral can be evaluated from $0$ to $\infty$ which gives
$$
f_{\beta_0, \beta_1|\text{data}}(\beta_0, \beta_1) \propto I\{-C < \beta_0, \beta_1 < C\} \int_0^{\infty} \sigma^{-n-1} \exp \left( -\frac{S(\beta_0, \beta_1)}{2\sigma^2} \right) d\sigma.
$$
The change of variable
$$
s = \frac{\sigma}{\sqrt{S(\beta_0, \beta_1)}}
$$
allows us to write the integral as
$$
\begin{aligned}
\int_0^{\infty} \sigma^{-n-1} \exp \left( -\frac{S(\beta_0, \beta_1)}{2\sigma^2} \right) d\sigma &= \left( \frac{1}{S(\beta_0, \beta_1)} \right)^{n/2} \int_0^{\infty} s^{-n-1} \exp \left( -\frac{1}{2s^2} \right) ds \\
&\propto \left( \frac{1}{S(\beta_0, \beta_1)} \right)^{n/2},
\end{aligned}
$$
where, we are using the fact that $\int_0^{\infty} s^{-n-1} \exp(-1/(2s^2)) ds$ is a constant (in the sense that it does not depend on $\beta_0$ and $\beta_1$).

The posterior density of $(\beta_0, \beta_1)$ is thus
$$
f_{\beta_0, \beta_1|\text{data}}(\beta_0, \beta_1) \propto I\{-C < \beta_0, \beta_1 < C\} \left( \frac{1}{S(\beta_0, \beta_1)} \right)^{n/2}. \tag{1}
$$
In words, the posterior density is inversely proportional to $S(\beta_0, \beta_1)^{n/2}$. This implies that the posterior mode is just the least squares estimator $(\hat{\beta}_0, \hat{\beta}_1)$. It is nicer to write the posterior in the following equivalent form:
$$
f_{\beta_0, \beta_1|\text{data}}(\beta_0, \beta_1) \propto \left( \frac{S(\hat{\beta}_0, \hat{\beta}_1)}{S(\beta_0, \beta_1)} \right)^{n/2} I\{-C < \beta_0, \beta_1 < C\} \tag{2}
$$
Note that (1) and (2) represent exactly the same density because the term $(S(\hat{\beta}_0, \hat{\beta}_1))^{n/2}$ does not depend on $\beta_0, \beta_1$ and is thus a constant.

Generally, the density (2) will be quite sharply concentrated around the least squares estimator $(\hat{\beta}_0, \hat{\beta}_1)$ especially when $n$ is large. This is because, when $(\beta_0, \beta_1)$ is such that $S(\beta_0, \beta_1)$ is large compared to $S(\hat{\beta}_0, \hat{\beta}_1)$, the quantity
$$
\left( \frac{S(\hat{\beta}_0, \hat{\beta}_1)}{S(\beta_0, \beta_1)} \right)^{n/2}
$$
would be quite negligible because of the large power $n/2$. As a result, the posterior density $f_{\beta_0, \beta_1|\text{data}}(\beta_0, \beta_1)$ will be concentrated around those values of $(\beta_0, \beta_1)$ for which $S(\beta_0, \beta_1)$ is quite close to $S(\hat{\beta}_0, \hat{\beta}_1)$. For example, suppose $n = 791$, and that $(\beta_0, \beta_1)$ is such that $S(\beta_0, \beta_1) = (1.1)S(\hat{\beta}_0, \hat{\beta}_1)$. Then
$$
\left( \frac{S(\hat{\beta}_0, \hat{\beta}_1)}{S(\beta_0, \beta_1)} \right)^{n/2} = \left( \frac{1}{1.1} \right)^{395.5} \approx 4.26 \times 10^{-17}.
$$
Such $(\beta_0, \beta_1)$ will thus get negligible posterior probability. Even for $(\beta_0, \beta_1)$ such that $S(\beta_0, \beta_1) = (1.01)S(\hat{\beta}_0, \hat{\beta}_1)$, we have
$$
\left( \frac{S(\hat{\beta}_0, \hat{\beta}_1)}{S(\beta_0, \beta_1)} \right)^{n/2} = \left( \frac{1}{1.01} \right)^{395.5} \approx 0.02
$$
and so such $(\beta_0, \beta_1)$ will also get fairly small posterior probability.

To sum up, when $n$ is large, the posterior probability will be concentrated around those $(\beta_0, \beta_1)$ for which $S(\beta_0, \beta_1)$ is very close to $S(\hat{\beta}_0, \hat{\beta}_1)$. Generally, this would imply that $(\beta_0, \beta_1)$ would itself have to be close to $(\hat{\beta}_0, \hat{\beta}_1)$. For this reason, the indicator term in (2) has no effect when $C$ is large. From now on, we shall drop this indicator term and refer to the Bayesian posterior as simply
$$
f_{\beta_0, \beta_1|\text{data}}(\beta_0, \beta_1) \propto \left( \frac{S(\hat{\beta}_0, \hat{\beta}_1)}{S(\beta_0, \beta_1)} \right)^{n/2}. \tag{3}
$$
It turns out that this represents a multivariate $t$-density, as well shall soon. Before that, let us first note that we have essentially the same formula in multiple linear regression as well.

---

[Up: contents](index.md) · [2 Multiple Linear Regression →](02-2-multiple-linear-regression.md)
