---
title: 'Moral: {#moral}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework6.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework6.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral}

**Source:** [`homework/homework6.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework6.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

When we do estimation with no shrinkage or other regularization, there is a real sense in which just counting the number of free parameters we estimate gives us a useful picture of how hard our estimator has fit (or overfit) to the data. For estimators that do a lot of regularization, however, naive parameter counting is not a good measure of overfitting. In this context, the effective degrees of freedom as defined above is a more natural generalization of the parameter dimension.

**Problem 3** (Soft thresholding).

Consider the *soft thresholding operator* with parameter $\lambda \geq 0$, defined as $$\eta_\lambda(x) =
\begin{cases}
  x - \lambda & x > \lambda\\
  0 & |x| \leq \lambda\\
  x + \lambda & x < -\lambda
\end{cases}$$ Note that, although we didn’t prove it in class, Stein’s lemma applies for continuous functions $h(x)$ which are differentiable except on a measure zero set; you can apply it here without worrying.

Assume $X \sim N_d(\theta, I_d)$ for $\theta \in \mathbb{R}^d$, which we will estimate via $\delta_\lambda(X) = (\eta_\lambda(X_1), \ldots, \eta_\lambda(X_{d}))$. Soft thresholding is sometimes used when we expect *sparsity*: a small number of relatively large $\theta_i$ values. $\lambda$ here is called a *tuning parameter* since it determines what version of the estimator we use, but doesn’t have an obvious statistical interpretation.

1.  Show that $\left|\{i:\; |X_i| > \lambda\}\right|$ is an unbiased estimator of the degrees of freedom of $\delta_\lambda$ (so, in a sense, the DF is the expected number of “free variables”).

2.  Show that $$d + \sum_i \min(X_i^2, \lambda^2) - 2 \left|\{i:\; |X_i| \leq \lambda\}\right|$$ is an unbiased estimator for the MSE of $\delta_\lambda$.

3.  Show that, if some $\theta_i \neq 0$, the risk-minimizing value $\lambda^*$ solves $$\lambda \sum_i \mathbb{P}_{\theta_i}(|X_i| > \lambda) = \sum_i \phi(\lambda - \theta_i) + \phi(\lambda + \theta_i),$$ where $\phi(z) = \frac{e^{-z^2/2}}{\sqrt{2\pi}}$ is the standard normal density.

    **Hint:** To show that there is a minimum in $(0,\infty)$, it may help to recall the Gaussian tail bound $$\left(\frac{1}{z} - \frac{1}{z^3}\right) \phi(z) \leq \mathbb{P}(Z > z) \leq \frac{1}{z}\phi(z),$$ for $Z \sim N(0,1)$. It might also help to show that $\frac{\phi(\lambda-\theta_2)}{\phi(\lambda-\theta_1)} \to 0$ as $\lambda\to\infty$, if $\theta_1>\theta_2$.

4.  Consider a problem with $\theta_1 = \cdots = \theta_{20} = 10$ and $\theta_{21} = \cdots = \theta_{500} = 0$. Compute $\lambda^*$ numerically. Then simulate a vector $X$ from the model and use it to automatically tune the value of $\lambda$ by minimizing SURE. Call the automatically tuned value $\hat\lambda(X)$ and report both $\lambda^*$ and $\hat\lambda(X)$. Finally plot the true MSE of $\delta_\lambda$ along with its SURE estimate against $\lambda$ for a reasonable range of $\lambda$ values. Add a horizontal line for the risk of the UMVU estimator.

5.  Compute and report the squared error loss $\|\delta(X) - \theta\|^2$ for the following four estimators:

    1.  the UMVU estimator $\delta_0(X) = X$,

    2.  the optimally tuned soft-thresholding estimator $\delta_{\lambda^*}(X)$,

    3.  the automatically tuned soft-thresholding estimator $\delta_{\hat{\lambda}(X)}(X)$, and

    4.  the James-Stein estimator.

    You do not need to compute the MSE. Intuitively, what do you think accounts for the good performance of soft-thresholding in this example?

---

[← Homework6 Part 01 —](01-homework6-part-01.md) · [Up: contents](index.md) · [Moral: {#moral-1} →](03-moral-moral-1.md)
