---
title: 1. Laplace Location Family (24 points, 4 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2023.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1. Laplace Location Family (24 points, 4 points / part).

Some useful facts for this problem:

- The exponential distribution with scale parameter $\theta > 0$ is called $\text{Exp}(\theta)$ and has density
$$p_\theta(x) = \frac{1}{\theta} e^{-x/\theta}, \quad \text{for } x > 0.$$
The mean is $\theta$ and the variance is $\theta^2$.

- The Gamma distribution with scale parameter $\theta > 0$ and shape parameter $k > 0$ is called $\text{Gamma}(k, \theta)$ and has density
$$p_{k,\theta}(x) = \frac{1}{\Gamma(k)\theta^k} x^{k-1} e^{-x/\theta}, \quad \text{for } x > 0,$$
where $\Gamma(k) = \int_0^\infty t^{k-1} e^{-t} \, dt$. The mean and variance are $k\theta$ and $k\theta^2$.

- A sum of $k$ independent $\text{Exp}(\theta)$ random variables is $\text{Gamma}(k, \theta)$.

- If $Z \sim \text{Gamma}(k, \theta)$ then $aZ \sim \text{Gamma}(k, a\theta)$, for any $a > 0$.

Suppose that we observe an i.i.d. sample from the Laplace scale family with parameter $\theta > 0$:
$$X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} \text{Laplace}(0, \theta) = \frac{1}{2\theta} e^{-|x|/\theta}, \quad \text{for } x \in \mathbb{R}.$$
Note the density is supported on the entire real line. This is not the same as the Laplace location family that we have used as a running example in class.

(a) Show that $|X_i| \sim \text{Exp}(\theta)$ for $i = 1, \dots, n$.

**Solution:**
For $0 \le a \le b < \infty$, we have
$$\begin{aligned}
\mathbb{P}(|X_i| \in [a, b]) &= \mathbb{P}(X_i \in [-b, -a]) + \mathbb{P}(X_i \in [a, b]) \\
&= \frac{1}{2} \left( \int_{-b}^{-a} \frac{1}{\theta} e^{x/\theta} \, dx + \int_a^b \frac{1}{\theta} e^{-x/\theta} \, dx \right) \\
&= \int_a^b \frac{1}{\theta} e^{-x/\theta} \, dx \\
&= \mathbb{P}(Y \in [a, b]),
\end{aligned}$$
where $Y \sim \text{Exp}(\theta)$.

(b) Find a minimal sufficient statistic for this model. Is it complete?

**Solution:**
The likelihood is
$$p(x) = \left( \frac{1}{2\theta} \right)^n \exp\left\{ -\frac{1}{\theta} \sum_i |x_i| \right\},$$
which we can recognize as an exponential family model with sufficient statistic $\sum_i |X_i|$ and natural parameter $1/\theta$. Because $1/\theta$ ranges over the entire interval $(0, \infty)$, the sufficient statistic is complete and therefore minimal.

(c) Find the maximum likelihood estimator for $\theta$ and give its asymptotic distribution.

**Solution:**
Let $T(X) = \sum_i |X_i|$. The log-likelihood is
$$\ell_n(\theta; X) = -n \log(2\theta) - \frac{1}{\theta} T(X),$$
and its derivative is
$$\dot{\ell}_n(\theta; X) = -\frac{n}{\theta} + \frac{1}{\theta^2} T(X) = \frac{n}{\theta^2} (T(X)/n - \theta),$$
so the likelihood is maximized by setting $\dot{\ell}_n(\hat{\theta}; X) = 0$, giving
$$\hat{\theta} = T/n = \frac{1}{n} \sum_i |X_i|.$$
Moreover, we can easily see from the last expression for $\dot{\ell}_n(\theta; X)$ that its sign is the same as the sign of $T/n - \theta$, so $T/n$ is the global maximizer. The Fisher information is therefore
$$J_n(\theta) = \text{Var}_\theta(T(X)/\theta^2) = n\theta^{-4} \text{Var}_\theta(X_i) = n\theta^{-2}.$$
As a result, the asymptotic distribution of the MLE is
$$\sqrt{n}(\hat{\theta}_n - \theta) \Rightarrow N(0, \theta^2).$$

(d) Show the estimator from the previous part is unbiased. Does it achieve the Cramér-Rao Lower Bound?

**Solution:**
The estimator is unbiased because $\mathbb{E}_\theta |X_i| = \theta$, since it is exponentially distributed. So $T/n$, which is an average of $n$ random variables each having expectation $\theta$, also has expectation $\theta$ and is therefore unbiased. Its variance is $\theta^2/n$, again because it is an average of $n$ independent random variables each with variance $\theta^2$. This matches the Cramér-Rao Lower Bound based on the variance calculated above.

(e) Now, suppose that we are concerned the variance might be gradually shrinking. Specifically, we are concerned that the $i$th random variable has parameter $\theta_i = \theta_0(1 - \delta)^i$. That is, we consider an alternative model with an additional parameter $\delta \in [0, 1)$, where
$$X_i \stackrel{\text{ind.}}{\sim} \text{Laplace}(0, \theta_0(1 - \delta)^i), \quad \text{for } i = 1, \dots, n.$$
Assume (for this part only) that the value of $\theta_0$ is known.

Suppose that we want to test our original model (which has $\delta = 0$) against the alternative that $\delta > 0$. Suggest a score test, giving an explicit expression for the score statistic and a cutoff based on its asymptotic distribution. You do not need to justify why the score statistic (calculated in the usual way and appropriately normalized) is asymptotically Gaussian in this non-i.i.d. model; you can just assume that it is.

**Solution:**
Now the log-likelihood is
$$\ell_n(\delta; X) = \sum_i -\log(2\theta_0) - i \log(1 - \delta) - \frac{|X_i|/\theta_0}{(1 - \delta)^i},$$
and its derivative is
$$\dot{\ell}_n(\delta; X) = \sum_i \frac{i}{1 - \delta} - \frac{i|X_i|/\theta_0}{(1 - \delta)^{i+1}}$$
The score evaluated at $\delta = 0$ is then
$$\dot{\ell}_n(0; X) = \sum_{i=1}^n i(1 - |X_i|/\theta_0),$$
and the Fisher information at $\delta = 0$ is
$$J_n(0) = \text{Var}_0(\dot{\ell}_n(\delta; X)) = \sum_{i=1}^n i^2 \text{Var}(|X_i|/\theta_0) = \sum_{i=1}^n i^2.$$
Thus, the normalized test statistic is
$$Z = J_n^{-1/2} \dot{\ell}_n(0; X) = \frac{\sum_{i=1}^n i(1 - |X_i|/\theta_0)}{\left(\sum_{i=1}^n i^2\right)^{-1/2}} \Rightarrow N(0, 1),$$
and since we are doing a one-sided test we reject if it is larger than $z_\alpha$.

(f) (*) Now, drop the assumption that $\theta_0$ is known, so that now both $\theta_0$ and $\delta$ are unknown. Assume we want to test the same hypothesis, $H_0 : \delta = 0$ against $H_1 : \delta > 0$, with $\theta_0$ as a nuisance parameter. How can we modify the test from the previous part so that it has finite-sample control of the Type I error rate? You do not need to give an explicit cutoff, but you should give a sufficient explanation of how you would find it without knowing the value of $\theta_0$.

**Solution:**
A natural idea is to condition on the value of $T(X)$, which is a sufficient statistic for the null submodel. Then, we can calculate the same statistic from the previous part, plugging in $\hat{\theta}_0 = T/n$ for $\theta_0$:
$$W = \frac{\sum_{i=1}^n i(1 - |X_i|n/T)}{\left(\sum_{i=1}^n i^2\right)^{-1/2}}.$$
Then we can reject for large values of $W$, which is equivalent up to an affine transformation to rejecting for small values of $\sum_i i|X_i|/T$.

The statistic $W$ may have smaller than unit variance but it doesn't really matter since we can just calculate its conditional distribution by Monte Carlo or other numerical integration techniques, and reject when $W$ is larger than some quantile. In fact we can simulate directly from the conditional distribution of $W$, or of $\sum_i i|X_i|/T$, by simulating $D = (|X_1|, \dots, |X_n|)/T$ from the $\text{Dirichlet}(\mathbf{1}_n)$ distribution, but this is not necessary to get full credit.

**Alternative solution:** A natural idea is to condition on the value of $T(X)$, which is a sufficient statistic for the null submodel. Rejecting for large $Z$ is equivalent to rejecting for small values of $\sum_i i|X_i|$, so we can just simulate from the conditional distribution given $T(X)$ and reject when the statistic is above its conditional upper $\alpha$ quantile. It so happens this is equivalent to the first approach because $D$ is independent of $T$, so the conditional distribution of $(|X_1|, \dots, |X_n|)$ given $T = t$ is just $t \cdot D$.

---

[← Final Examination: QUESTION BOOKLET](01-final-examination-question-booklet.md) · [Up: contents](index.md) · [2. Multivariate normal means (20 points, 5 points / part). →](03-2-multivariate-normal-means-20-points-5-points-part.md)
