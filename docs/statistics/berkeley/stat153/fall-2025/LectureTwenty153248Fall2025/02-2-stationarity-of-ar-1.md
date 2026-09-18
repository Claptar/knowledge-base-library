---
title: 2 Stationarity of AR(1)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Stationarity of AR(1)

In the last lecture, we discussed whether the $\text{AR}(1)$ model is stationary. The $\text{AR}(1)$ difference equation is $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$. This is an implicit equation because $y$ appears in both sides of the equation. To be able to calculate mean, variance and covariance etc., we need a more explicit formula for $y_t$.

One way to get such an explicit formula is to apply the difference equation recursively on the right hand side as:
$$y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$$
$$= \phi_0 + \phi_1 (\phi_0 + \phi_1 y_{t-2} + \epsilon_{t-1}) + \epsilon_t$$
$$= \phi_0(1 + \phi_1) + \phi_1^2 y_{t-2} + \epsilon_t + \phi_1 \epsilon_{t-1}$$
$$= \phi_0(1 + \phi_1) + \phi_1^2 (\phi_0 + \phi_1 y_{t-3} + \epsilon_{t-2}) + \epsilon_t + \phi_1 \epsilon_{t-1}$$
$$= \phi_0(1 + \phi_1 + \phi_1^2) + \phi_1^3 y_{t-3} + \epsilon_t + \phi_1 \epsilon_{t-1} + \phi_1^2 \epsilon_{t-2}.$$

We continue in this way writing $y_{t-3} = \phi_0 + \phi_1 y_{t-4} + \epsilon_{t-3}$ and then $y_{t-4} = \phi_0 + \phi_1 y_{t-5} + \epsilon_{t-4}$ and so on. This leads to
$$y_t = \phi_0 \sum_{j=0}^M \phi_1^j + \phi_1^{M+1} y_{t-M-1} + \sum_{j=0}^M \phi_1^j \epsilon_{t-j}. \tag{2}$$
This formula is true for every value of $M \ge 0$ and every $\phi_0, \phi_1$. The right hand side of (2) still depends on a $y$-value (specifically $y_{t-M-1}$).

Suppose now that $|\phi_1| < 1$. Then $\phi_1^{M+1}$ decays rapidly to zero. In this case, we can let $M \to \infty$ in (2) and use
$$\phi_0 \sum_{j=0}^M \phi_1^j \to \phi_0 \sum_{j=0}^\infty \phi_1^j = \frac{\phi_0}{1 - \phi_1} \quad \text{as } M \to \infty$$
$$\phi_1^{M+1} y_{t-M-1} \to 0 \quad \text{as } M \to \infty$$
$$\sum_{j=0}^M \phi_1^j \epsilon_{t-j} \to \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j} \quad \text{as } M \to \infty$$
Thus taking $M \to \infty$ in (2) leads to
$$y_t = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}. \tag{3}$$
This expression is well-defined when $|\phi_1| < 1$. It is easy to check that $y_t$ defined as (3) satisfies the $\text{AR}(1)$ equation $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$. In the last lecture, we saw that (3) is a stationary time series model with:
$$\mathbb{E}y_t = \frac{\phi_0}{1 - \phi_1} \quad \text{and} \quad \text{cov}(y_t, y_{t+h}) = \sigma^2 \frac{\phi_1^{|h|}}{1 - \phi_1^2}.$$

In the formula (3), it is clear that $y_t$ is determined by $\epsilon_t, \epsilon_{t-1}, \dots$ i.e., by the present and past values of $\epsilon_t$. For this reason, (3) is called **Causal, Stationary AR(1)** (causal here roughly means that $y_t$ is fully determined by present and past values of $\{\epsilon_t\}$). One consequence of this kind of causality is that $\epsilon_t$ is independent of the past $y$-values $y_{t-1}, y_{t-2}, y_{t-3}, \dots$ (this is because these past $y$-values only depend on $\epsilon_{t-1}, \epsilon_{t-2}, \dots$ which are all independent of $\epsilon_t$).

When $|\phi_1| \ge 1$, the terms in the right hand side of (2) do not converge when $M \to \infty$. In this case, it is not possible to get a stationary solution $y_t$ of the AR equation which depends only on present and past $\epsilon$-values $\epsilon_t, \epsilon_{t-1}, \dots$. In other words, there is no causal stationary solution to the $\text{AR}(1)$ equation when $|\phi_1| \ge 1$.

When $|\phi_1| > 1$ (note the strict inequality), there is a non-causal stationary solution for the $\text{AR}(1)$ equation. This is obtained by rewriting the $\text{AR}(1)$ equation as:
$$y_t = -\frac{\phi_0}{\phi_1} + \frac{1}{\phi_1} y_{t+1} - \frac{\epsilon_{t+1}}{\phi_1}.$$

and then recursively plugging in $y_{t+1}, y_{t+2}, \dots$ as:
$$y_t = -\frac{\phi_0}{\phi_1} + \frac{1}{\phi_1} \left( -\frac{\phi_0}{\phi_1} + \frac{1}{\phi_1} y_{t+2} - \frac{\epsilon_{t+2}}{\phi_1} \right) - \frac{\epsilon_{t+1}}{\phi_1}$$
$$= -\frac{\phi_0}{\phi_1} \left( 1 + \frac{1}{\phi_1} \right) + \frac{1}{\phi_1^2} y_{t+2} - \frac{\epsilon_{t+1}}{\phi_1} - \frac{\epsilon_{t+2}}{\phi_1^2}$$
$$= -\frac{\phi_0}{\phi_1} \left( 1 + \frac{1}{\phi_1} + \frac{1}{\phi_1^2} \right) + \frac{1}{\phi_1^3} y_{t+3} - \frac{\epsilon_{t+1}}{\phi_1} - \frac{\epsilon_{t+2}}{\phi_1^2} - \frac{\epsilon_{t+3}}{\phi_1^3}$$
$$= \dots$$
$$= -\frac{\phi_0}{\phi_1} \left( 1 + \frac{1}{\phi_1} + \frac{1}{\phi_1^2} + \dots + \frac{1}{\phi_1^M} \right) + \frac{y_{t+M+1}}{\phi_1^{M+1}} - \frac{\epsilon_{t+1}}{\phi_1} - \frac{\epsilon_{t+2}}{\phi_1^2} - \frac{\epsilon_{t+3}}{\phi_1^3} - \dots - \frac{\epsilon_{t+M+1}}{\phi_1^{M+1}} \tag{4}$$

Letting $M \to \infty$ and using $|\phi_1| > 1$ (so that $|1/\phi_1| < 1$), we get
$$y_t = \frac{\phi_0}{1 - \phi_1} - \sum_{j=1}^\infty \frac{\epsilon_{t+j}}{\phi_1^j} \tag{5}$$

It can be checked that (5) is also stationary (note now that $|\phi_1| > 1$) and satisfies the $\text{AR}(1)$ equation $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$. This $\text{AR}(1)$ process is called **non-causal** because $y_t$ depends on future values $\epsilon_{t+1}, \epsilon_{t+2}, \dots$. Here $\epsilon_t$ is not independent of the past $y$-values $y_{t-1}, y_{t-2}, \dots$.

If $|\phi_1| = 1$ (i.e., if $\phi_1 = 1$ or $\phi_1 = -1$), then neither (2) nor (4) converge as $M \to \infty$. In fact, in this case ($|\phi_1| = 1$), there cannot be a stationary solution to the $\text{AR}(1)$ equation.

## 2.1 Practical Implications

In practice, while fitting the $\text{AR}(1)$ model, we use the `AutoReg` function (from the `statsmodels` library) which works with the likelihood:
$$\prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma} \exp \left( -\frac{(y_t - \phi_0 - \phi_1 y_{t-1})^2}{2\sigma^2} \right) \tag{6}$$
This likelihood fixes the value of $y_1$ and assumes that each $\epsilon_t$ is independent of the past values $y_{t-1}, y_{t-2}, \dots$. In other words, the model considered is:
$$y_1 = \text{fixed at observed value and } y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t \tag{7}$$
where $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$ and independent of $y_{t-1}, \dots, y_1$ for each $t = 2, \dots, n$. The parameters $\phi_0, \phi_1, \sigma$ are estimated in the usual way (as is done in linear regression). For predictions, one works with the fitted model where the parameters are replaced by their estimates $\hat{\phi}_0, \hat{\phi}_1$ (and also $\hat{\sigma}$).

Based on the value of $\hat{\phi}_1$, the following things can happen:

1. **Case One:** $|\hat{\phi}_1| > 1$. This happens often when we fit the $\text{AR}(1)$ model directly to economic data (such as GDP or GNP). Here the fitted model (7) (with $\phi_0 = \hat{\phi}_0$ and $\phi_1 = \hat{\phi}_1$) is very different from the non-causal stationary $\text{AR}(1)$ model given by (5). Note again that for (5), $\epsilon_t$ becomes dependent on the past values $y_{t-1}, y_{t-2}, \dots$. The fitted model (7) is quite far from being stationary and future predictions will often exhibit explosive behavior when the prediction horizon increases.

2. **Case Two:** $|\hat{\phi}_1| < 1$. This also happens very often. For economic data, this often happens after some preprocessing (e.g., by taking logarithms of the raw data and then differences once or twice). In this case, the fitted model (7) is also non-stationary and distinct from the causal stationary model (3). However, the discrepancy is minimal and they behave similarly in many ways:

   a) The likelihood for (3) is
   $$\frac{\sqrt{1 - \phi_1^2}}{\sqrt{2\pi}\sigma} \exp \left( -\frac{1 - \phi_1^2}{2\sigma^2} \left( y_1 - \frac{\phi_0}{1 - \phi_1} \right)^2 \right) \prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma} \exp \left( -\frac{(y_t - \phi_0 - \phi_1 y_{t-1})^2}{2\sigma^2} \right) \tag{8}$$
   We saw this form of the likelihood in Lecture 17. The only difference between this likelihood and the likelihood (6) is the presence of the term involving $y_1$. When $n$ is large, this single term (which only involves the first data point) does not affect the overall likelihood significantly, so both likelihood maximizations lead to similar answers.

   b) Recursing the difference equation in (7) from $t, \dots, 2$, we obtain (basically taking $M = t - 2$ in (2))
   $$y_t = \phi_0 \sum_{j=0}^{t-2} \phi_1^j + \phi_1^{t-1} y_1 + \sum_{j=0}^{t-2} \phi_1^j \epsilon_{t-j} \quad \text{for every } t = 2, \dots, n.$$
   Because $|\phi_1| < 1$ (so that $|\phi_1|^j$ decreases rapidly), we can expect the above to be close to (3) as long as $t$ is not very small.

   c) Future predictions for the models (7) and (3) work in identical fashion (for fixed identical parameter values). These predictions only use independence of $\epsilon_t$ and past $y$-values $y_{t-1}, y_{t-2}, \dots$ which is true in both (7) and (3).

   Because of these reasons, when $|\hat{\phi}_1| < 1$, even though `AutoReg` is fitting (7), it is common to pretend as if we are working with the causal stationary $\text{AR}(1)$ model (3).

3. **Case Three:** $|\hat{\phi}_1| = 1$. This is either $\hat{\phi}_1 = 1$ or $\hat{\phi}_1 = -1$. These models are all non-stationary. The case $\hat{\phi}_1 = -1$ almost never arises in practice (unless the data has a strange wild oscillatory pattern from each time point to the next). The case $\hat{\phi}_1 = 1$ is much more applicable. `AutoReg` may not give $\hat{\phi}_1 = 1$ exactly but it might give $\hat{\phi}_1$ that is close to 1. Note that when $\phi_1 = 1$, the $\text{AR}(1)$ model equation can be rewritten as $y_t - y_{t-1} = \phi_0 + \epsilon_t$; this suggests preprocessing the data by taking successive differences $y_t - y_{t-1}$ and trying to fit models to this differenced data. $\text{AR}(1)$ predictions with $\hat{\phi}_1 = 1$ grow linearly which may be well-suited for many datasets.

Thus from the practical perspective where we only consider causal models, stationary only corresponds to $|\phi_1| < 1$. (When $|\phi_1| > 1$, mathematically speaking, there is a stationary $\text{AR}(1)$ model but this is non-causal and does not correspond to our likelihoods and fitting technique).

Next we shall look at $\text{AR}(p)$ models for $p \ge 2$ and discuss the analogue of the causal-stationarity condition $|\phi_1|$ when $p \ge 2$.

Before we do that however, let us first go over an alternative method of deriving the causal stationary $\text{AR}(1)$ model formula (3) using a formal technique involving Backshift notation.

Before describing this technique, we need to introduce the backshift notation.

---

[← 1 Moving Average (MA) Models](01-1-moving-average-ma-models.md) · [Up: contents](index.md) · [3 Backshift Notation →](03-3-backshift-notation.md)
