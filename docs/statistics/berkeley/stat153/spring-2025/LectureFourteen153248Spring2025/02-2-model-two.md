---
title: 2 Model Two
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFourteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFourteen153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFourteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFourteen153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Model Two

This is the model
$$y_t \overset{\text{ind}}{\sim} N(0, \tau_t^2) \tag{2}$$
The parameters are $\tau_1^2, \dots, \tau_n^2$. Since these represent variances, we refer to this as a "variance model". $\tau_t$ can be interpreted as the magnitude of $y_t$. This model is useful when we care only about the magnitudes of the observations $y_t$ (and not their signs).

Model (2) (similar to Model One from the previous section) is also a high-dimensional model because the number of parameters is large.

The likelihood is proportional to
$$\prod_{t=1}^n \frac{1}{\tau_t} \exp\left( -\frac{y_t^2}{2\tau_t^2} \right). \tag{3}$$
Note that the likelihood depends on the data only through the squares $y_1^2, \dots, y_n^2$. Therefore the squares $y_1^2, \dots, y_n^2$ form the "sufficient statistic" in this model. Under (2), we have
$$y_t^2 \overset{\text{ind}}{\sim} \tau_t^2 \chi_1^2$$
where $\chi_1^2$ denotes the chi-squared distribution with 1 degree of freedom. Instead of writing the likelihood in terms of the raw data $y_t$, we can also write the likelihood using the squares $y_t^2$. This will lead to a slightly different form for the likelihood that should still be proportional to (3). To see this, observe that the density of $\chi_1^2$ is proportional to $x^{-1/2} \exp(-x/2)$ so that the density of $\tau_t^2 \chi_1^2$ is proportional to
$$\frac{1}{\tau_t^2} \left( \frac{x}{\tau_t^2} \right)^{-1/2} \exp\left( -\frac{x}{2\tau_t^2} \right) = x^{-1/2} \frac{1}{\tau_t} \exp\left( -\frac{x}{2\tau_t^2} \right).$$

The likelihood written in terms of $y_1^2, \dots, y_n^2$ is thus
$$\prod_{t=1}^n (y_t^2)^{-1/2} \frac{1}{\tau_t} \exp\left( -\frac{y_t^2}{2\tau_t^2} \right).$$
The term $(y_t^2)^{-1/2}$ above can be dropped as it is a constant not depending on the parameters $\tau_t^2$. Dropping it leads to (3).

The log-likelihood is:
$$\sum_{t=1}^n \left( -\log \tau_t - \frac{y_t^2}{2\tau_t^2} \right).$$
It is a convention to write optimization problems for computing estimators as minimization problems (as opposed to maximization). For this, we write the negative log-likelihood which is given by:
$$\sum_{t=1}^n \left( \log \tau_t + \frac{y_t^2}{2\tau_t^2} \right).$$
As $\tau_t$ is a standard deviation parameter that is constrained to be positive, it is better to deal with $\alpha_t = \log \tau_t$ instead of $\tau_t$ directly. This reparameterization has the following benefits:

- **Unconstrained Optimization:** Unlike $\tau_t$, which must be positive, $\alpha_t$ can take any real value, allowing for more stable numerical optimization.

- **Improved Computational Stability:** Variance parameters can vary over several orders of magnitude, and working in the log scale reduces numerical precision issues.

Because of these benefits, many variance modeling approaches use log-variance transformations (see e.g., stochastic volatility models).

Writing the negative log-likelihood in terms of $\alpha_t = \log \tau_t$, we get
$$\sum_{t=1}^n \left( \alpha_t + \frac{y_t^2}{2} e^{-2\alpha_t} \right)$$
If we minimize the above (without any additional regularization) with respect to $\alpha_t$, we obtain $\alpha_t = \log |y_t|$, or equivalently, $\tau_t^2 = y_t^2$. In other words, the parameters $\tau_t^2$ will fully interpolate (overfit) the sufficient statistics $y_t^2$.

For a more useful estimation procedure, we need to introduce regularization. If we assume that $\alpha_t$ is smooth, we can add the penalty $\sum_{t=2}^{n-1} ((\alpha_{t+1} - \alpha_t) - (\alpha_t - \alpha_{t-1}))^2$ or $\sum_{t=2}^{n-1} |(\alpha_{t+1} - \alpha_t) - (\alpha_t - \alpha_{t-1})|$ to the negative log-likelihood. This leads to the estimators $\hat{\alpha}_t^{\text{ridge}}(\lambda)$ and $\hat{\alpha}_t^{\text{lasso}}(\lambda)$ which are defined as the minimizers of
$$\sum_{t=1}^n \left( \alpha_t + \frac{y_t^2}{2} e^{-2\alpha_t} \right) + \lambda \sum_{t=2}^{n-1} ((\alpha_{t+1} - \alpha_t) - (\alpha_t - \alpha_{t-1}))^2$$
and
$$\sum_{t=1}^n \left( \alpha_t + \frac{y_t^2}{2} e^{-2\alpha_t} \right) + \lambda \sum_{t=2}^{n-1} |(\alpha_{t+1} - \alpha_t) - (\alpha_t - \alpha_{t-1})|$$
respectively. The penalties encourage smoothness in $\{\alpha_t\}$, leading to more stable and interpretable variance estimates. These optimizations are convex and they can be solved, for example, using functions from the python library cvxpy just as we solved $\hat{\beta}^{\text{ridge}}(\lambda)$ and $\hat{\beta}^{\text{lasso}}(\lambda)$ from the previous section.

---

[← 1 Model One](01-1-model-one.md) · [Up: contents](index.md) · [3 Model Three →](03-3-model-three.md)
