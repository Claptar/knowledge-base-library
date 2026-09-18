---
title: 3 Likelihood for AR(1)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeventeen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSeventeen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Likelihood for AR(1)

Let us now write the likelihood for the AR(1) model (2). Superficially, (2) looks the same as (3) with $i = t$, $x_i = y_{t-1}$ and $\beta_0 = \phi_0$ and $\beta_1 = \phi_1$. However, some of the other regression assumptions listed above do not hold for (2):

1. The density of $x_t = y_{t-1}$ will depend on $\theta$ (because $y_{t-1} = \phi_0 + \phi_1 y_{t-2} + \epsilon_{t-1}$ so $\phi_0, \phi_1$ and $\sigma$ certainly affect $y_{t-1}$).
2. It is also unclear why $\epsilon_2, \dots, \epsilon_n$ should be independent of $x_2 = y_1, \dots, x_n = y_{n-1}$.

As a result, we cannot use the same principles as in usual linear regression to write the likelihood for AR models. Instead we shall proceed as follows (using a different set of assumptions). As the data is $y_1, \dots, y_n$, the likelihood is given by (below $\theta = (\phi_0, \phi_1, \sigma)$ denotes the set of parameters)
$$
&\text{Likelihood for Model (2)} \\
&= f_{y_1, \dots, y_n \mid \theta}(y_1, \dots, y_n) \\
&= f_{y_1 \mid \theta}(y_1) f_{y_2 \mid y_1, \theta}(y_2) f_{y_3 \mid y_1, y_2, \theta}(y_3) \dots f_{y_n \mid y_1, \dots, y_{n-1}, \theta}(y_n) \\
&= f_{y_1 \mid \theta}(y_1) \prod_{t=2}^n f_{y_t \mid y_1, \dots, y_{t-1}, \theta}(y_t) \\
&= f_{y_1 \mid \theta}(y_1) \prod_{t=2}^n f_{\phi_0 + \phi_1 y_{t-1} + \epsilon_t \mid y_1, \dots, y_{t-1}, \theta}(y_t) \\
&= f_{y_1 \mid \theta}(y_1) \prod_{t=2}^n f_{\epsilon_t \mid y_1, \dots, y_{t-1}, \theta}(y_t - \phi_0 - \phi_1 y_{t-1}).
$$
Now we assume that $\epsilon_t$ is independent of $y_1, \dots, y_{t-1}$. This gives
$$
&\text{Likelihood for Model (2)} \\
&= f_{y_1 \mid \theta}(y_1) \prod_{t=2}^n f_{\epsilon_t \mid y_1, \dots, y_{t-1}, \theta}(y_t - \phi_0 - \phi_1 y_{t-1}) = f_{y_1 \mid \theta}(y_1) \prod_{t=2}^n f_{\epsilon_t}(y_t - \phi_0 - \phi_1 y_{t-1}).
$$
With $\epsilon_t \sim N(0, \sigma^2)$, we get
$$
\text{Likelihood for Model (2)} = f_{y_1 \mid \theta}(y_1) \prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{1}{2\sigma^2}(y_t - \phi_0 - \phi_1 y_{t-1})^2 \right)
$$
which is equivalent to:
$$
\text{Likelihood for (2)} = f_{y_1 \mid \theta}(y_1) \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{n-1} \exp\left( -\frac{1}{2\sigma^2} \sum_{t=2}^n (y_t - \phi_0 - \phi_1 y_{t-1})^2 \right). \tag{5}
$$
To sum up, we used the following assumptions to derive the likelihood (5):

1. The model equation (2).
2. Independence of $\epsilon_t$ and $y_1, \dots, y_{t-1}$ for each $t = 2, \dots, n - 1$.
3. $\epsilon_t \sim N(0, \sigma^2)$.

The likelihood (5) has the term $f_{y_1 \mid \theta}(y_1)$ which we should make explicit before we can compute estimators. Note that the model equation (2) is only for $t = 2, \dots, n$ which means that $y_1$ never appears on the left side. So it is not possible to compute $f_{y_1 \mid \theta}(y_1)$ using (2). There are two approaches of dealing with $f_{y_1 \mid \theta}(y_1)$.

## 3.1 Approach One: Assume $f_{y_1 \mid \theta}(y_1)$ does not depend on $\theta$

Here one simply assumes that $f_{y_1 \mid \theta}(y_1)$ does not depend on $\theta$. Then $f_{y_1 \mid \theta}(y_1)$ becomes a constant factor in (5) that can be ignored in proportionality leading to
$$
\text{Likelihood for (2)} \propto \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{n-1} \exp\left( -\frac{1}{2\sigma^2} \sum_{t=2}^n (y_t - \phi_0 - \phi_1 y_{t-1})^2 \right). \tag{6}
$$
This likelihood is identical to the likelihood in usual regression with $x_t = y_{t-1}$ (even though the assumptions that led to the likelihood are different from the case of linear regression).

Because of this, Bayesian inference here (with the prior $\phi_0, \phi_1, \log \sigma \overset{\text{i.i.d}}{\sim} \text{uniform}(-C, C)$ will lead to identical results as in the case of linear regression. In other words, the posterior for $(\phi_0, \phi_1)$ will be:
$$
(\phi_0, \phi_1) \mid y_1, \dots, y_n \sim t_{n-3, 2}\left( (\hat{\phi}_0, \hat{\phi}_1), \hat{\sigma}^2 (X^T X)^{-1} \right)
$$
where $\hat{\phi}_0$ and $\hat{\phi}_1$ represent the least squares estimates obtained by regressing $y_t$ on $y_{t-1}$. Note that the residual degrees of freedom (i.e., the degrees of freedom of the $t$-distribution) equal $n - 3$ because the number of observations in this regression equals $n - 1$ (as $t = 2, \dots, n$) and the number of columns of $X$ equals 2.

Frequentist inference for AutoRegression will be quite different from inference in linear regression. First note that, under the likelihood (6), the MLEs of $\phi_0, \phi_1, \sigma$ will be identical to the MLEs in linear regression (because the likelihood (6) is the same as for linear regression). However, in order to derive the distribution of the MLEs, we now have to use the AR assumptions which are more complicated. This part is usually done by asymptotics i.e., by letting $n \to \infty$ (see for example Shumway and Stoffer [1, Chapter 4]). In this analysis, inference is based on the normal distribution and justified in the large sample limit as $n \to \infty$; in other words, $t$-distributions no longer arise.

This is one concrete problem where Bayesian inference and frequentist inference differ. Bayesian inference is simpler while frequentist inference is more complicated and uses asymptotic arguments (specifically, Central Limit Theorems and Laws of Large Numbers for dependent random variables).

Usual library functions for AutoRegression (such as the function `AutoReg` in the `statsmodels` library) use the frequentist formulas so they give different results from those obtained by just running the OLS function for regressing $y_t$ on $x_t = y_{t-1}$. For example, they give standard errors and z-scores as opposed to t-scores. Most of the time in practice, the difference between the two kinds of inferences is negligible. However, strictly speaking, they are different.

## 3.2 Approach Two: Computing $f_{y_1 \mid \theta}(y_1)$ by extending (2) to $t \le 1$

So far we assumed the model equation (2) only for $t = 2, \dots, n$. With this, $y_1$ never appears on the left hand side in (2) which means that we have not assumed anything about $f_{y_1 \mid \theta}(y_1)$. In order to be able to compute it, a natural idea is to extend the model equation for $t = 1, 0, -1, \dots$. This allows computation of $f_{y_1 \mid \theta}(y_1)$ in the following way. Applying (2) for $t = 1, 0, -1, -2, \dots$ recursively, we get
$$
y_1 &= \phi_0 + \phi_1 y_0 + \epsilon_1 \\
&= \phi_0 + \phi_1 (\phi_0 + \phi_1 y_{-1} + \epsilon_0) + \epsilon_1 \\
&= \phi_0(1 + \phi_1) + \phi_1^2 y_{-1} + \phi_1 \epsilon_0 + \epsilon_1 \\
&= \phi_0(1 + \phi_1) + \phi_1^2 (\phi_0 + \phi_1 y_{-2} + \epsilon_{-1}) + \phi_1 \epsilon_0 + \epsilon_1 \\
&= \phi_0(1 + \phi_1 + \phi_1^2) + \phi_1^3 y_{-2} + \phi_1^2 \epsilon_{-1} + \phi \epsilon_0 + \epsilon_1.
$$
Continuing this way with using (2) for $t = -2, -3, \dots, -M$ (for some large $M$), we get
$$
y_1 &= \phi_0(1 + \phi_1 + \phi_1^2 + \dots + \phi_1^M) + \phi_1^{M+1} y_{-M} + \phi_1^M \epsilon_{-M+1} + \phi_1^{M-1} \epsilon_{-M+2} + \dots + \phi \epsilon_0 + \epsilon_1 \\
&= \phi_0 \sum_{j=0}^M \phi_1^j + \phi_1^{M+1} y_{-M} + \sum_{j=0}^M \phi_1^j \epsilon_{1-j}.
$$

This equation is not enough to allow us to deduce $f_{y_1 \mid \theta}(y_1)$ because it involves the unknown quantity $y_{-M}$. If $|\phi_1| < 1$, then the coefficient $\phi_1^{M+1}$ in front of $y_{-M}$ is very small. In this case, it might make sense to ignore the term $\phi_1^{M+1} y_{-M}$ when $M$ is large. This allows us to write
$$
y_1 \approx \phi_0 \sum_{j=0}^M \phi_1^j + \sum_{j=0}^M \phi_1^j \epsilon_{1-j} \approx \phi_0 \sum_{j=0}^\infty \phi_1^j + \sum_{j=0}^\infty \phi_1^j \epsilon_{1-j} = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{1-j}.
$$
The term $\sum_{j=0}^\infty \phi_1^j \epsilon_{1-j}$ is the sum of independent normal random variables, so it is Normal with mean zero (as each $\epsilon_{1-j}$ has mean zero) and with variance:
$$
\text{var}\left(\sum_{j=0}^\infty \phi_1^j \epsilon_{1-j}\right) = \sum_{j=0}^\infty \text{var}\left(\phi_1^j \epsilon_{1-j}\right) = \sum_{j=0}^\infty \phi_1^{2j} \text{var}(\epsilon_{1-j}) = \sigma^2 \sum_{j=0}^\infty \phi_1^{2j} = \frac{\sigma^2}{1 - \phi_1^2}.
$$
Thus when $|\phi_1| < 1$, we can write
$$
y_1 \sim N\left( \frac{\phi_0}{1 - \phi_1}, \frac{\sigma^2}{1 - \phi_1^2} \right).
$$
which gives
$$
f_{y_1 \mid \theta}(y_1) = \frac{\sqrt{1 - \phi_1^2}}{\sqrt{2\pi}\sigma} \exp\left( -\frac{1 - \phi_1^2}{2\sigma^2} \left(y_1 - \frac{\phi_0}{1 - \phi_1}\right)^2 \right).
$$
Plugging this in (5), we get
$$
&\text{Likelihood for (2)} \\
&= \frac{\sqrt{1 - \phi_1^2}}{\sqrt{2\pi}\sigma} \exp\left( -\frac{1 - \phi_1^2}{2\sigma^2} \left(y_1 - \frac{\phi_0}{1 - \phi_1}\right)^2 \right) \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{n-1} \exp\left( -\frac{1}{2\sigma^2} \sum_{t=2}^n (y_t - \phi_0 - \phi_1 y_{t-1})^2 \right). \tag{7}
$$
This is a more complicated likelihood compared to (6). This is applicable only when $|\phi_1| < 1$. We shall see later the implications of this assumption.

---

[← 2 Detour: usual linear regression](02-2-detour-usual-linear-regression.md) · [Up: contents](index.md) · [4 Two AR(1) Models →](04-4-two-ar-1-models.md)
