---
title: '2 Detour: usual linear regression'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeventeen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSeventeen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Detour: usual linear regression

The model (2) looks just like a usual regression model:
$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i \tag{3}
$$
except we are using $\phi$ instead of $\beta$ for the coefficients, and the index is now $t$ as opposed to $i$. Let the data be denoted by $(x_i, y_i)$, $i = 1, \dots, m$ ($m$ is the number of data points).

Under the assumption $\epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$, the likelihood for (3) is:
$$
\prod_{i=1}^m \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(y_i - \beta_0 - \beta_1 x_i)^2}{2\sigma^2} \right). \tag{4}
$$
Let us take a closer look as to how the likelihood (4) is actually derived. We shall examine closely the assumptions that are made in deriving (4). Our main interest is to see whether the same assumptions are still true for AutoRegression.

The data is $(x_i, y_i)$, $i = 1, \dots, m$ ($m$ is the number of data points). The likelihood is the probability density function of the data treated as a function of the parameters $\theta = (\beta_0, \beta_1, \sigma)$ ($\sigma$ is the standard deviation of the errors):
$$
\text{Likelihood for model (3)} = f_{x_1, y_1, x_2, y_2, \dots, x_m, y_m \mid \theta}(x_1, y_1, \dots, x_m, y_m).
$$
Given that the model (3) writes each $y_i$ in terms of $x_i$, it makes sense to first condition on $x_1, \dots, x_m$:
$$
\text{Likelihood for model (3)} = f_{y_1, \dots, y_m \mid x_1, \dots, x_m, \theta}(y_1, \dots, y_m) f_{x_1, \dots, x_m \mid \theta}(x_1, \dots, x_m).
$$
Now we write $y_i = \beta_0 + \beta_1 x_i + \epsilon_i$ for each $i$ to get
$$
\begin{aligned}
&\text{Likelihood for model (3)} \\
&= f_{y_1, \dots, y_m \mid x_1, \dots, x_m, \theta}(y_1, \dots, y_n) f_{x_1, \dots, x_m \mid \theta}(x_1, \dots, x_m) \\
&= f_{\beta_0 + \beta_1 x_1 + \epsilon_1, \dots, \beta_0 + \beta_1 x_m + \epsilon_m \mid x_1, \dots, x_m, \theta}(y_1, \dots, y_n) f_{x_1, \dots, x_m \mid \theta}(x_1, \dots, x_m) \\
&= f_{\epsilon_1, \dots, \epsilon_m \mid x_1, \dots, x_m, \theta}(y_1 - \beta_0 - \beta_1 x_1, \dots, y_m - \beta_0 - \beta_1 x_m) f_{x_1, \dots, x_m \mid \theta}(x_1, \dots, x_m).
\end{aligned}
$$
To proceed further, we assume that $\epsilon_1, \dots, \epsilon_n$ are independent of $x_1, \dots, x_n$ (given the parameters). This allows us to remove the conditioning on $x_1, \dots, x_n$ in the first term above, leading to:
$$
\begin{aligned}
&\text{Likelihood for model (3)} \\
&= f_{\epsilon_1, \dots, \epsilon_m \mid \theta}(y_1 - \beta_0 - \beta_1 x_1, \dots, y_m - \beta_0 - \beta_1 x_m) f_{x_1, \dots, x_m \mid \theta}(x_1, \dots, x_m).
\end{aligned}
$$
We now use the assumption that $\epsilon_1, \dots, \epsilon_n \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$ to write:
$$
\begin{aligned}
&\text{Likelihood for model (3)} \\
&= \left[ \prod_{i=1}^m f_{\epsilon_i \mid \theta}(y_i - \beta_0 - \beta_1 x_i) \right] f_{x_1, \dots, x_m \mid \theta}(x_1, \dots, x_n) \\
&= \left[ \prod_{i=1}^m \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(y_i - \beta_0 - \beta_1 x_i)^2}{2\sigma^2} \right) \right] f_{x_1, \dots, x_m \mid \theta}(x_1, \dots, x_m).
\end{aligned}
$$
How do we deal with the last term $f_{x_1, \dots, x_m \mid \theta}(x_1, \dots, x_m)$? We simply assume that this term does not depend on $\theta$ so it only becomes a constant (in terms of $\theta$) multiplicative factor in the likelihood that can be omitted leading to:
$$
\text{Likelihood for model (3)} \propto \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^m \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^m (y_i - \beta_0 - \beta_1 x_i)^2 \right),
$$
which coincides with (4).

To summarize, we used the following assumptions to derive the likelihood (4):

1. The model equation (3)
2. Independence of the errors $\epsilon_1, \dots, \epsilon_m$ with the covariates $x_1, \dots, x_m$
3. $\epsilon_i \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$
4. The density of $x_1, \dots, x_m$ does not depend on $\theta = (\beta_0, \beta_1, \sigma)$.

Using the likelihood, frequentist inference first computes the Maximum Likelihood Estimates by maximizing the likelihood or the log-likelihood. This gives:
$$
\hat{\beta} = (X^T X)^{-1} X^T y \quad \text{and} \quad \hat{\sigma}_{\text{MLE}} := \sqrt{\frac{\text{RSS}}{n}}
$$
where $X$ is the $m \times 2$ matrix with the first column consisting of all ones, and the second column consists of $x_1, \dots, x_m$. Then the goal is to derive the distribution of the MLEs $\hat{\beta}$ and $\hat{\sigma}_{\text{MLE}}$ (given the parameters $\theta$). For this, one again needs to use the above assumptions.

Bayesian inference proceeds by combining the prior $\beta_0, \beta_1, \log \sigma \overset{\text{i.i.d}}{\sim} \text{unif}(-C, C)$ with the likelihood to compute the posterior. We have seen previously that the posterior is given by:
$$
\beta \mid \text{data} \sim t_{m-2, 2}\left(\hat{\beta}, \hat{\sigma}^2 (X^T X)^{-1}\right) \quad \text{where } \hat{\sigma} := \sqrt{\frac{\text{RSS}}{m - 2}}.
$$
A posterior for $\sigma$ can also be derived (we did this in Homework one). One important point about Bayesian inference is that once the likelihood is written, we no longer care about the assumptions that were needed for writing the likelihood. Once the likelihood is written, the subsequent inference (via the posterior distribution) only uses the likelihood. In contrast, frequentist inference uses the assumptions twice: first to write the likelihood in order to compute the MLEs, and then to derive the distribution of the MLEs.

---

[← 1 Parameter Estimation in AutoRegressive Models](01-1-parameter-estimation-in-autoregressive-models.md) · [Up: contents](index.md) · [3 Likelihood for AR(1) →](03-3-likelihood-for-ar-1.md)
