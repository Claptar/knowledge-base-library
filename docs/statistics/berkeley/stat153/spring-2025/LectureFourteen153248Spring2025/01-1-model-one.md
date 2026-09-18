---
title: 1 Model One
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFourteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFourteen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFourteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFourteen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Model One

## Lecture Fourteen
### Spring 2025, UC Berkeley
### Aditya Guntuboyina
### March 6, 2025

We shall discuss three simple high-dimensional models for time series $y_1, \dots, y_n$. The first model was already discussed last week, the second model is new but very simple, and the third model is the same as the spectrum model from last lecture. The second model makes it easier to understand the third model.

This is the model
$$y_t \overset{\text{ind}}{\sim} N(\mu_t, \sigma^2)$$
where ind stands for "independently distributed as". Note that the right hand side depends on $t$ so the distribution of $y_t$ changes with $t$ and we cannot therefore use "i.i.d".

The parameters in this model are $\mu_1, \dots, \mu_n$ and $\sigma^2$. Clearly this is a high-dimensional because the number of parameters is large.

If we attempt to estimate the parameters by maximizing the likelihood without any regularization, we get $\mu_t = y_t$ and $\sigma^2 = 0$, leading to full interpolation (overfitting) to the data. Regularization is therefore necessary to obtain something useful. If we want to obtain "smooth" trend estimates, we can employ regularization terms which force neighboring values or neighboring slopes of $\mu_t$ to be close. If we focus on slopes (which leads to more smoothness compared to just imposing closeness of values), we obtain the estimators $\hat{\mu}_t^{\text{ridge}}(\lambda)$ and $\hat{\mu}_t^{\text{lasso}}(\lambda)$ which minimize:
$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} ((\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1}))^2$$
and
$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} |(\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1})|$$
respectively. We have already studied these estimators last week where we observed, among other things, that they can be alternatively represented as $\hat{\mu}_t^{\text{ridge}}(\lambda) = X \hat{\beta}^{\text{ridge}}(\lambda)$ and $\hat{\mu}_t^{\text{lasso}}(\lambda) = X \hat{\beta}^{\text{lasso}}(\lambda)$ where
$$X = \begin{pmatrix}
1 & 0 & 0 & \cdot & \cdot & 0 \\
1 & 1 & 0 & \cdot & \cdot & 0 \\
1 & 2 & 1 & \cdot & \cdot & 0 \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
1 & n-1 & n-2 & \cdot & \cdot & 1
\end{pmatrix} \quad \text{and} \quad \beta = \begin{pmatrix}
\beta_0 \\
\beta_1 \\
\beta_2 \\
\cdot \\
\cdot \\
\cdot \\
\beta_{n-1}
\end{pmatrix} \tag{1}$$
and $\hat{\beta}^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{lasso}}(\lambda)$ minimize
$$\|y - X\beta\|^2 + \sum_{t=2}^{n-1} \beta_t^2$$
and
$$\|y - X\beta\|^2 + \sum_{t=2}^{n-1} |\beta_t|$$
respectively.

This model is an example of a "Mean Model" where the focus is on estimating the mean parameters $\mu_t$. In contrast, the next two models will be examples of "Variance Models".

---

[Up: contents](index.md) · [2 Model Two →](02-2-model-two.md)
