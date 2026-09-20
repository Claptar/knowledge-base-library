---
title: "Solutions — Linear Regression and Hypothesis Testing"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — Linear Regression and Hypothesis Testing

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 24: Solutions
## December 7, 2010

1. (a) Normalization of the distribution requires:
$$1 = \sum_{k=0}^{\infty} p_K(k; \theta) = \sum_{k=0}^{\infty} \frac{e^{-k/\theta}}{Z(\theta)} = \frac{1}{Z(\theta)} \sum_{k=0}^{\infty} e^{-k/\theta} = \frac{1}{Z(\theta) \cdot (1 - e^{-1/\theta})},$$
so $Z(\theta) = \frac{1}{1 - e^{-1/\theta}}$.

(b) Rewriting $p_K(k; \theta)$ as:
$$p_K(k; \theta) = \left(e^{-1/\theta}\right)^k \left(1 - e^{-1/\theta}\right), \quad k = 0, 1, \dots$$
the probability distribution for the photon number is a geometric probability distribution with probability of success $p = 1 - e^{-1/\theta}$, and it is shifted with 1 to the left since it starts with $k = 0$. Therefore the photon number expectation value is
$$\mu_K = \frac{1}{p} - 1 = \frac{1}{1 - e^{-1/\theta}} - 1 = \frac{1}{e^{1/\theta} - 1}$$
and its variance is
$$\sigma_K^2 = \frac{1 - p}{p^2} = \frac{e^{-1/\theta}}{(1 - e^{-1/\theta})^2} = \mu_K^2 + \mu_K.$$

(c) The joint probability distribution for the $k_i$ is
$$p_K(k_1, \dots, k_n; \theta) = \frac{1}{Z(\theta)^n} \prod_{i=1}^n e^{-k_i/\theta} = \frac{1}{Z(\theta)^n} e^{-\frac{1}{\theta} \sum_{i=1}^n k_i}.$$
The log likelihood is $-n \cdot \log Z(\theta) - 1/\theta \sum_{i=1}^n k_i$.
We find the maxima of the log likelihood by setting the derivative with respect to the parameter $\theta$ to zero:
$$\frac{d}{d\theta} \log p_K(k_1, \dots, k_n; \theta) = -n \cdot \frac{e^{-1/\theta}}{\theta^2(1 - e^{-1/\theta})} + \frac{1}{\theta^2} \sum_{i=1}^n k_i = 0$$
or
$$\frac{1}{e^{1/\theta} - 1} = \frac{1}{n} \sum_{i=1}^n k_i = s_n.$$
For a hot body, $\theta \gg 1$ and $\frac{1}{e^{1/\theta} - 1} \approx \theta$, we obtain
$$\theta \approx \frac{1}{n} \sum_{i=1}^n k_i = s_n.$$
Thus the maximum likelihood estimator $\hat{\Theta}_n$ for the temperature is given in this limit by the sample mean of the photon number

$$\hat{\Theta}_n = \frac{1}{n} \sum_{i=1}^n K_i.$$

(d) According to the central limit theorem, the sample mean for large enough $n$ (in the limit) approaches a Gaussian distribution with standard deviation our root mean square error
$$\sigma_{\hat{\Theta}_n} = \frac{\sigma_K}{\sqrt{n}}.$$
To allow only for 1% relative root mean square error in the temperature, we need $\frac{\sigma_K}{\sqrt{n}} < 0.01\mu_K$. With $\sigma_K^2 = \mu_K^2 + \mu_K$ it follows that
$$\sqrt{n} > \frac{\sigma_K}{0.01\mu_K} = 100 \frac{\sqrt{\mu_K^2 + \mu_K}}{\mu_K} = 100 \sqrt{1 + \frac{1}{\mu_K}}.$$
In general, for large temperatures, i.e. large mean photon numbers $\mu_K \gg 1$, we need about 10,000 samples.

(e) The 95% confidence interval for the temperature estimate for the situation in part (d), i.e.
$$\sigma_{\hat{\Theta}_n} = \frac{\sigma_K}{\sqrt{n}} = 0.01\mu_K,$$
is
$$[\hat{K} - 1.96\sigma_{\hat{K}}, \hat{K} + 1.96\sigma_{\hat{K}}] = [\hat{K} - 0.0196\mu_K, \hat{K} + 0.0196\mu_K].$$

2. (a) Using the regression formulas of Section 9.2, we have
$$\hat{\theta}_1 = \frac{\sum_{i=1}^5 (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^5 (x_i - \bar{x})^2}, \quad \hat{\theta}_0 = \bar{y} - \hat{\theta}_1\bar{x},$$
where
$$\bar{x} = \frac{1}{5} \sum_{i=1}^5 x_i = 4.94, \quad \bar{y} = \frac{1}{5} \sum_{i=1}^5 y_i = 134.38.$$
The resulting ML estimates are
$$\hat{\theta}_1 = 40.53, \quad \hat{\theta}_0 = -65.86.$$

(b) Using the same procedure as in part (a), we obtain
$$\hat{\theta}_1 = \frac{\sum_{i=1}^5 (x_i^2 - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^5 (x_i^2 - \bar{x})^2}, \quad \hat{\theta}_0 = \bar{y} - \hat{\theta}_1\bar{x},$$
where
$$\bar{x} = \frac{1}{5} \sum_{i=1}^5 x_i^2 = 33.60, \quad \bar{y} = \frac{1}{5} \sum_{i=1}^5 y_i = 134.38.$$
which for the given data yields
$$\hat{\theta}_1 = 4.09, \quad \hat{\theta}_0 = -3.07.$$
Figure 1 shows the data points $(x_i, y_i)$, $i = 1, \dots, 5$, the estimated linear model
$$y = 40.53x - 65.86,$$
and the estimated quadratic model
$$y = 4.09x^2 - 3.07.$$

Regression Plot

*Required for 6.431; optional for 6.041*

---

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← back to chapter 24](../24-linear-regression-and-hypothesis-testing.md)
