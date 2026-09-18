---
title: 6 Cross-validation for selecting $\lambda$
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEleven153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureEleven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 6 Cross-validation for selecting $\lambda$

The behavior of $\hat{\beta}^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{lasso}}(\lambda)$ depend crucially on the choice of the tuning parameter $\lambda$. One can visually tune $\lambda$ in order to obtain $\hat{\mu}_t^{\text{ridge}}(\lambda), \hat{\mu}_t^{\text{lasso}}(\lambda)$ that is simple (not too wiggly) and which fits the data well (for example, one can start with $\lambda = 1$ and either increase or decrease $\lambda$ by factors of 10 until a visually appealing trend estimate is obtained). Another popular approach is to use cross-validation.

The basic idea behind cross validation is the following. First split the total set of time points $T = \{1, \dots, n\}$ into two disjoint groups $T_{\text{train}}$ and $T_{\text{test}}$. Generally $T_{\text{train}}$ will be much larger than $T_{\text{test}}$ (e.g., $T_{\text{train}}$ will contain about 80% of the data and $T_{\text{test}}$ will contain about 20% of the data). For this split, fit the model to the time indices in $T_{\text{train}}$ and obtain $\hat{\beta}_{\text{train}}^{\text{ridge}}(\lambda)$ as the minimizer of
$$\sum_{t \in T_{\text{train}}} (y_t - \beta_0 - \beta_1(t - 1) - \beta_2\text{ReLU}(t - 2) - \dots - \beta_{n-1}\text{ReLU}(t - (n - 1)))^2 + \lambda (\beta_2^2 + \beta_3^2 + \dots + \beta_{n-1}^2) \tag{7}$$
and $\hat{\beta}_{\text{train}}^{\text{ridge}}(\lambda)$ as the minimizer of
$$\sum_{t \in T_{\text{train}}} (y_t - \beta_0 - \beta_1(t - 1) - \beta_2\text{ReLU}(t - 2) - \dots - \beta_{n-1}\text{ReLU}(t - (n - 1)))^2 + \lambda (|\beta_2| + |\beta_3| + \dots + |\beta_{n-1}|) \tag{8}$$
Using these estimates, predict the values of $y_t$ for $t \in T_{\text{test}}$:
$$\hat{y}_t^{\text{ridge}}(\lambda) = \hat{\beta}_{\text{train},0}^{\text{ridge}}(\lambda) + \hat{\beta}_{\text{train},1}^{\text{ridge}}(\lambda)(t - 1) + \hat{\beta}_{\text{train},2}^{\text{ridge}}(\lambda)\text{ReLU}(t - 2) + \dots + \hat{\beta}_{\text{train},n-1}^{\text{ridge}}(\lambda)\text{ReLU}(t - (n - 1))$$
and
$$\hat{y}_t^{\text{lasso}}(\lambda) = \hat{\beta}_{\text{train},0}^{\text{lasso}}(\lambda) + \hat{\beta}_{\text{train},1}^{\text{lasso}}(\lambda)(t - 1) + \hat{\beta}_{\text{train},2}^{\text{lasso}}(\lambda)\text{ReLU}(t - 2) + \dots + \hat{\beta}_{\text{train},n-1}^{\text{lasso}}(\lambda)\text{ReLU}(t - (n - 1))$$
The discrepancy between the actual values of $y_t$ and the predicted values can be calculated as:
$$\text{Test-Error}^{\text{ridge}}(\lambda) = \sum_{t \in T_{\text{test}}} \left( y_t - \hat{y}_t^{\text{ridge}}(\lambda) \right)^2 \quad \text{and} \quad \text{Test-Error}^{\text{lasso}}(\lambda) = \sum_{t \in T_{\text{test}}} \left( y_t - \hat{y}_t^{\text{lasso}}(\lambda) \right)^2$$
This test error is for a single train-test split. One can consider multiple train-test splits and add the test errors to obtain one measure of the test error for each value of $\lambda$:
$$\text{AllSplit-Test-Error}^{\text{ridge}}(\lambda) = \sum_{\text{all splits}} \text{Test-Error}^{\text{ridge}}(\lambda)$$
and
$$\text{AllSplit-Test-Error}^{\text{lasso}}(\lambda) = \sum_{\text{all splits}} \text{Test-Error}^{\text{lasso}}(\lambda)$$
This test error over all splits would be calculated for a set of candidate $\lambda$ values (e.g., $\lambda = 10^a$ for $a = -5, -4, \dots, 4, 5$) and then choose the value of $\lambda$ which gives the smallest test error (this would give one choice of $\lambda$ for ridge, and one choice of $\lambda$ for lasso).

One common choice of selecting the splits is the following:
1. **Split 1**: $T_{\text{test}}$ is $\{1, 6, 11, \dots \}$ and $T_{\text{train}}$ is all other $t$.
2. **Split 2**: $T_{\text{test}}$ is $\{2, 7, 12, \dots \}$ and $T_{\text{train}}$ is all other $t$.
3. **Split 3**: $T_{\text{test}}$ is $\{3, 8, 13, \dots \}$ and $T_{\text{train}}$ is all other $t$.
4. **Split 4**: $T_{\text{test}}$ is $\{4, 9, 14, \dots \}$ and $T_{\text{train}}$ is all other $t$.
5. **Split 5**: $T_{\text{test}}$ is $\{5, 10, 15, \dots \}$ and $T_{\text{train}}$ is all other $t$.

This method gives 5 different train-test splits, commonly known as 5-fold cross-validation.

---

[← 5 Ridge vs LASSO](03-5-ridge-vs-lasso.md) · [Up: contents](index.md)
