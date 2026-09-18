---
title: 1 Parameter Interpretation in (1)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Parameter Interpretation in (1)

Let $\mu_t$ denote the deterministic part of model (1), i.e.,
$$\mu_t = \beta_0 + \beta_1(t - 1) + \beta_2\text{ReLU}(t - 2) + \beta_3\text{ReLU}(t - 3) + \dots + \beta_{n-1}\text{ReLU}(t - (n - 1)). \tag{3}$$
The model (1) can then be written as
$$y_t = \mu_t + \epsilon_t \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2).$$
Here $\mu_t$ represents the trend function that we aim to estimate from the data. For illustration, consider $y_t$ to be the logarithm of California's population in year $t$. The trend function $\mu_t$ captures the underlying systematic pattern in the population growth, while $\epsilon_t$ accounts for random fluctuations around this trend.

Sometimes, we can also interpret $\mu_t$ as the 'actual' data and $\epsilon_t$ as the measurement error causing $\mu_t$ to be observed as $y_t$. For example, in the population example, $\mu_t$ would represent the actual population (on log scale) while $y_t$ would represent our noisy measurement of it.

The parameters $\beta_0, \beta_1, \beta_2, \dots, \beta_{n-1}$ can be interpreted in terms of $\mu_t$ as follows. We will focus on the population example here for simplicity. Plugging $t = 1$ in (3), we get
$$\beta_0 = \mu_1. \tag{4}$$
So $\beta_0$ can be interpreted as the actual population on log scale (or the value of the trend function) at time $t = 1$. Plugging $t = 2$ in (3), we get $\mu_2 = \beta_0 + \beta_1 = \mu_1 + \beta_1$ so that
$$\beta_1 = \mu_2 - \mu_1.$$
If $P_t = \exp(\mu_t)$ denotes the population on the original scale, then
$$\beta_1 = \log P_2 - \log P_1 = \log \frac{P_2}{P_1} \approx \frac{P_2}{P_1} - 1 = \frac{P_2 - P_1}{P_1}.$$
Here we used the fact that $\log x \approx x - 1$ if $x$ is close to 1. In other words, $100\beta_1$ can be interpreted as the percentage growth of the population from year 1 to year 2.

For $\beta_2$, let us plug $t = 3$ in (3) to get $\mu_3 = \beta_0 + 2\beta_1 + \beta_2$. Replacing $\beta_0 = \mu_1$ and $\beta_1 = \mu_2 - \mu_1$, we obtain
$$\beta_2 = (\mu_3 - \mu_2) - (\mu_2 - \mu_1).$$
This means that
$$100\beta_2 \approx (\text{percentage change from year 2 to 3}) - (\text{percentage change from year 1 to 2})$$
Continuing this way for $t = 4, 5, \dots, n$, we get
$$\beta_t = (\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1})$$
so that
$$100\beta_t \approx (\text{percentage change from year } t \text{ to } (t + 1)) - (\text{percentage change from year } (t - 1) \text{ to } t).$$
For example, suppose
$$\beta_0 = 7.3 \quad \beta_1 = 0.04 \quad \beta_2 = -0.001 \quad \beta_3 = -0.0005 \text{ etc.}$$
The interpretation then is that $\mu_t$ started with the value $\mu_1 = \exp(7.3) \approx 1480$ (if the population units are in thousands of persons, this means that the population at time 1 was 1.48 million). From year 1 to year 2, the population grew by $4\%$. From year 2 to year 3, the population grew by $4 - 0.1 = 3.9\%$. From year 3 to year 4, the population grew by $3.9 - 0.05 = 3.85\%$, and so on.

It is important to understand that the parameters $\beta_2, \dots, \beta_{n-1}$ are on a different scale (units) compared to $\beta_0$ and $\beta_1$. $\beta_0$ is in the scale of the data, $100\beta_1$ represents percent change, while $100\beta_j$ for $j \ge 2$ represents the change in percent change.

We next study strategies for estimating the unknown parameters $\beta_0, \beta_1, \dots, \beta_{n-1}$ (as well as $\sigma$) from the observed time series $y_1, \dots, y_n$.

---

[← STAT 153 & 248 - Time Series](01-stat-153-248---time-series.md) · [Up: contents](index.md) · [2 (Unregularized) MLE →](03-2-unregularized-mle.md)
