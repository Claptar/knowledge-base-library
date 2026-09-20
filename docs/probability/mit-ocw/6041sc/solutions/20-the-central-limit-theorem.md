---
title: "Solutions — The Central Limit Theorem"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — The Central Limit Theorem

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 20 Solutions: November 18, 2010

1. (a) Let $X_i$ be a random variable indicating the quality of the $i$th bulb ("1" for good bulbs, "0" for bad ones). $X_i$'s are independent Bernoulli random variables. Let $Z_n$ be
$$Z_n = \frac{X_1 + X_2 + \dots + X_n}{n}.$$
$$\mathbf{E}[Z_n] = p \qquad \text{var}(Z_n) = \frac{n\text{var}(X_i)}{n^2} = \frac{\sigma^2}{n},$$
where $\sigma^2$ is the variance of $X_i$.

Applying Chebyshev's inequality yields,
$$\mathbf{P}\left(|Z_n - p| \ge \epsilon\right) \le \frac{\sigma^2}{n\epsilon^2},$$
As $n \to \infty$, $\frac{\sigma^2}{n\epsilon^2} \to 0$ and $\mathbf{P}\left(|Z_n - p| \ge \epsilon\right) \to 0$.
Hence, $Z_n$ converges to $p$ in probability.

(b) By Chebychev's inequality,
$$\mathbf{P}\left(|Z_{50} - p| \ge 0.1\right) \le \frac{\sigma^2}{50(0.1)^2},$$
Since $X_i$ is a Bernoulli random variable, its variance $\sigma^2$ is $p(1 - p)$, which is less than or equal to $\frac{1}{4}$. Thus,
$$\mathbf{P}\left(|Z_{50} - p| \ge 0.1\right) \le \frac{1/4}{50(0.1)^2} = 0.5$$

(c) By Chebychev's inequality,
$$\mathbf{P}\left(|Z_n - p| \ge 0.1\right) \le \frac{\sigma^2}{n\epsilon^2} \le \frac{1/4}{n(0.1^2)}$$
To guarantee a probability $0.95$ of falling in the desired range,
$$\frac{1/4}{n(0.1)^2} < 0.05,$$
which yields $n \ge 500$. Note that $n \ge 500$ guarantees the accuracy specification even for the highest variance, namely $1/4$. For smaller variances, we need smaller values of $n$ to guarantee the desired accuracy. For example, if $\sigma^2 = 1/16$, $n \ge 125$ would suffice.

2. (a) $\mathbf{E}[X_n] = 0 \cdot \left(1 - \frac{1}{n}\right) + 1 \cdot \frac{1}{n} = \frac{1}{n}$
$\text{var}(X_n) = \left(0 - \frac{1}{n}\right)^2 \cdot \left(1 - \frac{1}{n}\right) + \left(1 - \frac{1}{n}\right)^2 \cdot \left(\frac{1}{n}\right) = \frac{n-1}{n^2}$
$\mathbf{E}[Y_n] = 0 \cdot \left(1 - \frac{1}{n}\right) + n \cdot \frac{1}{n} = 1$
$\text{var}(Y_n) = (0 - 1)^2 \cdot \left(1 - \frac{1}{n}\right) + (n - 1)^2 \cdot \left(\frac{1}{n}\right) = n - 1$

(b) Using Chebyshev's inequality, we have
$$\lim_{n\to\infty} \mathbf{P}\left(\left|X_n - \frac{1}{n}\right| \ge \epsilon\right) \le \lim_{n\to\infty} \frac{n-1}{n^2\epsilon^2} = 0$$
Moreover, $\lim_{n\to\infty} \frac{1}{n} = 0$.
It follows that $X_n$ converges to $0$ in probability. For $Y_n$, Chebyshev suggests that,
$$\lim_{n\to\infty} \mathbf{P}\left(|Y_n - 1| \ge \epsilon\right) \le \lim_{n\to\infty} \frac{n-1}{\epsilon^2} = \infty,$$
Thus, we cannot conclude anything about the convergence of $Y_n$ through Chebychev's inequality.

(c) For every $\epsilon > 0$,
$$\lim_{n\to\infty} \mathbf{P}(|Y_n| \ge \epsilon) \le \lim_{n\to\infty} \frac{1}{n} = 0,$$
Thus, $Y_n$ converges to zero in probability.

(d) The statement is false. A counter example is $Y_n$. It converges in probability to $0$ yet its expected value is $1$ for all $n$.

(e) Using the Markov bound, we have
$$\mathbf{P}\left(|X_n - c| \ge \epsilon\right) = \mathbf{P}\left(|X_n - c|^2 \ge \epsilon^2\right) \le \frac{\mathbf{E}\left[(X_n - c)^2\right]}{\epsilon^2}.$$
Taking the limit as $n \to \infty$, we obtain
$$\lim_{n\to\infty} \mathbf{P}\left(|X_n - c| \ge \epsilon\right) = 0,$$
which establishes convergence in probability.

(f) A counter example is $Y_n$. $Y_n$ converges to $0$ in probability, but
$$\mathbf{E}\left[(Y_n - 0)^2\right] = 0 \cdot \left(1 - \frac{1}{n}\right) + (n^2) \cdot \frac{1}{n} = n$$
Thus,
$$\lim_{n\to\infty} \mathbf{E}\left[(Y_n - 0)^2\right] = \infty,$$
and $Y_n$ does not converge to $0$ in the mean square.

3. (a) No. Since $X_i$ for any $i \ge 1$ is uniformly distributed between -1.0 and 1.0.

(b) Yes, to 0. Since for $\epsilon > 0$,
$$\begin{aligned}
\lim_{i\to\infty} \mathbf{P}(|Y_i - 0| > \epsilon) &= \lim_{i\to\infty} \mathbf{P}\left(\left|\frac{X_i}{i} - 0\right| > \epsilon\right) \\
&= \lim_{i\to\infty} [\mathbf{P}(X_i > i\epsilon) + \mathbf{P}(X_i < -i\epsilon)] = 0.
\end{aligned}$$

(c) Yes, to 0. Since for $\epsilon > 0$,
$$\begin{aligned}
\lim_{i\to\infty} \mathbf{P}(|Z_i - 0| > \epsilon) &= \lim_{i\to\infty} \mathbf{P}\left(\left|(X_i)^i - 0\right| > \epsilon\right) \\
&= \lim_{i\to\infty} \left[\mathbf{P}\left(X_i > \epsilon^{\frac{1}{i}}\right) + \mathbf{P}\left(X_i < -(\epsilon)^{\frac{1}{i}}\right)\right] \\
&= \lim_{i\to\infty} \left[\frac{1}{2}\left(1 - \epsilon^{\frac{1}{i}}\right) + \frac{1}{2}\left(1 - \epsilon^{\frac{1}{i}}\right)\right] = \lim_{i\to\infty} \left(1 - \sqrt[i]{\epsilon}\right) \\
&= 0.
\end{aligned}$$

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← back to chapter 20](../20-the-central-limit-theorem.md)
