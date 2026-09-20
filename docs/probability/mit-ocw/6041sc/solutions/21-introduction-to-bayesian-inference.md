---
title: "Solutions — Introduction to Bayesian Inference"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — Introduction to Bayesian Inference

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 21 Solutions
## November 23, 2010

1. (a) To use the Markov inequality, let $X = \sum_{i=1}^{10} X_i$. Then,
$$\mathbf{E}[X] = 10\mathbf{E}[X_i] = 5,$$
and the Markov inequality yields
$$\mathbf{P}(X \ge 7) \le \frac{5}{7} = 0.7142.$$

(b) Using the Chebyshev inequality, we find that
$$2\mathbf{P}(X - 5 \ge 2) = \mathbf{P}(|X - 5| \ge 2)$$
$$\le \frac{\text{var}(X)}{4} = \frac{10/12}{4}$$
$$\mathbf{P}(X - 5 \ge 2) \le \frac{5}{48} = 0.1042.$$

(c) Finally, using the Central Limit Theorem, we find that
$$\mathbf{P}\left(\sum_{i=1}^{10} X_i \ge 7\right) = 1 - \mathbf{P}\left(\sum_{i=1}^{10} X_i \le 7\right)$$
$$= 1 - \mathbf{P}\left(\frac{\sum_{i=1}^{10} X_i - 5}{\sqrt{10/12}} \le \frac{7 - 5}{\sqrt{10/12}}\right)$$
$$\approx 1 - \Phi(2.19)$$
$$\approx 0.0143.$$

2. Check online solutions.

3. (a) If we interpret $X_i$ as the number of arrivals in an interval of length 1 in a Poisson process of rate 1, then, $S_n = X_1 + \dots + X_n$ can be seen as the number of arrivals in an interval of length $n$ in the Poisson process of rate 1. Therefore, $S_n$ is a Poisson random variable with mean and variance equal to $n$.

(b) We use the random variables $X_1, \dots, X_n$ and the random variable $S_n = X_1 + \dots + X_n$. Denoting by $Z$ the standard normal, and applying the central limit theorem, we have for large $n$
$$\mathbf{P}(S_n = n) = \mathbf{P}(n - 1/2 < S_n < n + 1/2)$$
$$= \mathbf{P}\left(\frac{-1}{2\sqrt{n}} < \frac{S_n - n}{\sqrt{n}} \le \frac{1}{2\sqrt{n}}\right)$$
$$\approx \mathbf{P}\left(\frac{-1}{2\sqrt{n}} < Z \le \frac{1}{2\sqrt{n}}\right)$$
$$= \frac{1}{\sqrt{2\pi}} \int_{-1/2\sqrt{n}}^{1/2\sqrt{n}} e^{-z^2/2} dz$$
$$\approx \frac{1}{\sqrt{2\pi}} \frac{1}{\sqrt{n}} e^{-z^2/2} \Bigg|_{z=0}$$
$$= \frac{1}{\sqrt{2\pi n}}$$
where the first equation follows from the fact that $S_n$ takes integer values, the first approximation is suggested by the central limit theorem, and the second approximation uses the fundamental theorem of calculus (the value of a definite integral over a small interval is equal to the length of the interval times the integrand evaluated at some point within the interval). Since $S_n$ is Poisson with mean $n$, we have
$$\mathbf{P}(S_n = n) = e^{-n} \frac{n^n}{n!},$$
and by combining the preceding relations, we see that $n! \approx n^n e^{-n} \sqrt{2\pi n} = \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$. One may show that
$$\lim_{n \to \infty} \frac{n!}{n^n e^{-n} \sqrt{2\pi n}} = 1,$$
so the relative error of the approximation tends to 0 as $n \to \infty$. A more precise estimate is that
$$n! = n^n e^{-n} \sqrt{2\pi n} \cdot e^{\lambda_n},$$
where
$$\frac{1}{12n + 1} < \lambda_n < \frac{1}{12n}.$$
However, one cannot derive these relations from the central limit theorem.

Note that the form of the approximation was first discovered by de Moivre in the form $n! \approx n^{n+1/2} e^{-n} \cdot (\text{constant})$, and gave a complicated expression for the constant. De Moivre's friend Stirling subsequently showed that the constant has the simple form $\sqrt{2\pi}$.

***

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← back to chapter 21](../21-introduction-to-bayesian-inference.md)
