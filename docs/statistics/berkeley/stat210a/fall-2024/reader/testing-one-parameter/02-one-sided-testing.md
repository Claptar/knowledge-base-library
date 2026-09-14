---
title: One-sided testing
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-one-parameter.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/testing-one-parameter.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# One-sided testing

**Source:** [`reader/testing-one-parameter.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-one-parameter.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Last time, we showed that if the family $\cP$ has MLR in the statistic $T(X)$, then the one-sided test that rejects for large $T(X)$ is UMP for testing $H_0:\;\theta\leq \theta_0$ vs $H_1:\;\theta > \theta_0$, because:

(i) it is simultaneously the likelihood ratio test for $H_0:\;\theta = \theta_0$ vs $H_1:\;\theta = \theta_1$, for every $\theta_1 > 0$, and

(ii) it controls the Type I error for all $\theta < \theta_0$.

Recall that a test *rejects for large $T(X)$* if it is of the form
$$\phi(X) = \begin{cases} 1 &\quad \text{ if } T(X) > c \\ 0 &\quad \text{ if } T(X) < c\\ \gamma &\quad \text{ if } T(X) = c\end{cases},$$
where the critical threshold $c$ is the *upper-$\alpha$ quantile at the boundary*
$$
c_\alpha = \min \{c \in \RR:\; \PP_{\theta_0}(T(X) > c) \leq \alpha\}
$$
and the randomization parameter $\gamma$ is used to "top off" the Type I error rate if $T(X)$ is discrete and $\PP_{\theta_0}(T(X) > c_\alpha) < \alpha$. In the rest of this section we will ignore randomization and assume that we just accept a conservative test in case $\PP_{\theta_0}(T(X) > c_\alpha) < \alpha$ (as is generally done in practice).

A generic one-parameter model $\cP$ does not have MLR in any statistic $T(X)$; e.g. the LRT for testing $\theta_0$ vs $\theta_1=\theta_0 + 1$ does not coincide with the LRT for testing $\theta_0$ vs $\theta_1=\theta_0 +  2$. Then we cannot maximize power for both alternative values $\theta_0+1$ and $\theta_0+2$ simultaneously.

In such cases, we could still come up with a test that rejects for large values of some other test statistic $T(X)$, that tends to be larger when $\theta$ is larger. Formally, we say that $T(X)$ is *stochastically increasing in $\theta$* if $\PP_\theta(T(X) > c)$ is non-decreasing in $\theta$, for every $c \in \RR$. The power function of $\phi(X) = 1\{T(X) > c_\alpha\}$, then, is also non-decreasing in $\theta$, and $\phi(X)$ is a valid test of $H_0:\;\theta\leq \theta_0$ vs $H_1:\;\theta > \theta_0$.

### Score test

Suppose we observe $X_1,\ldots,X_n \simiid P_\theta$ for large $n$, and we want to test $H_0:\;\theta\leq \theta_0$ vs $H_1:\;\theta > \theta_0$, but $\cP$ does not have MLR so we cannot maximize the power over the entirety of $H_1$. One idea is to use the heuristic of maximizing the power for alternatives near $\theta_0$; if $n$ is large, then we have a lot of information about $\theta$ so our power will be close to $1$ no matter what we do. So we might prioritize maximizing the power at $\theta_0 + \varepsilon$ for small $\varepsilon$.

The LRT for $\theta_0$ vs $\theta_0 + \varepsilon$ rejects for large values of
$$ \frac{p_{\theta_0+\varepsilon}(X)}{p_{\theta_0}(X)} =\exp\{\ell(\theta_0+\varepsilon; X) - \ell(\theta_0; X)\} \approx e^{\varepsilon \dot\ell(\theta_0;X)},$$
which is equivalent to rejecting for large values of $\dot\ell(\theta_0;X)$. Using the score statistic can give simple and appealing tests in certain situations.

**Example: Laplace**

Suppose $X_1,\ldots,X_n \simiid \text{Laplace}(\theta) = \frac{1}{2}e^{-|x-\theta|}$ and we want to test $H_0:\theta \leq 0$ vs $H_1:\;\theta > 0$. We can calculate the likelihood ratio test for a given fixed alternative $\theta_1 > 0$ as

$$
\log \frac{p_{\theta_1}(X)}{p_0(X)} = \sum_i |X_i| - |X_i-\theta_1| = \theta_1\sum_i T_{\theta_1}(X_i),
$$
so the optimal test rejects for large $\sum_i T_{\theta_1}(X_i)$, where
$$
T_{\theta}(x) = \begin{cases} -1 & \text{ if } x \leq 0 \\ \frac{2x}{\theta} -1 & \text{ if } 0 \leq x \leq \theta \\ +1 &\text{ if } x \geq \theta \end{cases}.
$$
We can visualize the univariate version of the test statistic $T_{\theta}(x)$ for several different values of $\theta>0$:

```r
T.theta <- function(x, theta) {
  pmax(-1, pmin(1, 2*x/theta-1))
}
curve(T.theta(x, 0.2), from=-1, to = 3, , col="red", main="Univariate test statistic", xlab="x", ylab=expression(T[theta](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/x)), n=1001)
grid()
curve(T.theta(x, 1), add=TRUE, col="blue", n=1001, lty=2)
curve(T.theta(x, 2), add=TRUE, n=1001, lty=3)
legend("bottomright",legend=c(expression(theta==2), expression(theta==1), expression(theta==0.2)), lty=3:1,col=c("black","blue","red"))
```
Note that this test implicitly caps the influence of any single observation $X_i$. Once $X_i > \theta_1$, it gives the same evidence in favor of $\theta_1$ and against $\theta_0$ regardless of how much it exceeds $\theta_1$. Compare this with the sample mean, where the influence of a single observation $X_i$ is unbounded.  It is easy to see that $f(X_i)$ is stochastically increasing in $\theta$ for *any* non-decreasing function $f$, so any LRT gives a valid level-$\alpha$ test on the entire null distribution.

If we take $\theta_1\downarrow 0$, the univariate test statistic approaches
$$
T_0(x) = \begin{cases} -1 & \text{ if } x \leq 0\\ +1 &\text{ if } x > 0\end{cases},
$$
which gives the score test since
$$
\dot{\ell}(\theta;X) = \frac{d}{d\theta} \sum_i -|X_i-\theta| = \sum_i T_0(X_i)
$$
This is equivalent to rejecting for large values of $S(X) = \#\{X_i > 0\}$, simply the number of positive $X_i$ values.


We can also plot the power curves for $n = 100$ and $\alpha = 0.1$, for these tests and for the test that rejects for large values of $\sum_i X_i$. As we see, the score test performs noticeably better than the test that rejects for large values of the sample mean $\overline{X}$. But the LRT for $\theta_1 = 0.2$ seems to do best for this value of $n$, since $\theta_1 = 0.2$ is a moderately hard alternative value for which the power is intermediate.

```r
T.theta <- function(x, theta) {
  pmax(-1, pmin(1, 2*x/theta-1))
}
alpha <- 0.1
n <- 100
nrep <- 1e4
Z <- matrix(rexp(n*nrep) * sign(rnorm(n*nrep)), nrow=nrep)
theta1.values <- c(2, 1, 0.2, 0)

theta.grid <- c(seq(-.2,.6,by=.02),seq(0.6,1.2,by=.1))
power <- matrix(NA, nrow=length(theta.grid), ncol=length(theta1.values)+1)
power.func <- function(Z, theta, theta1.opt, cutoff, gamma) {
  Tmat <- matrix(T.theta(Z+theta, theta1.opt), nrow=nrep)
  mean(rowSums(Tmat) > cutoff) + gamma * mean(rowSums(Tmat) == cutoff)
}
for(t1.ix in 1:length(theta1.values)) {
  Tmat0 <- matrix(T.theta(Z, theta1.values[t1.ix]), nrow=nrep)
  c.alpha <- quantile(rowSums(Tmat0), 1-alpha)
  gamma.alpha <- (alpha - mean(rowSums(Tmat0) > c.alpha)) / mean(rowSums(Tmat0) == c.alpha)
  if(is.na(gamma.alpha)) {
    gamma.alpha <- 0
  }
  power[,t1.ix] <- sapply(theta.grid, function(th) power.func(Z, th, theta1.values[t1.ix], c.alpha, gamma.alpha))
}

---

[← Testing with one real parameter](01-testing-with-one-real-parameter.md) · [Up: contents](index.md) · [Sample mean →](03-sample-mean.md)
