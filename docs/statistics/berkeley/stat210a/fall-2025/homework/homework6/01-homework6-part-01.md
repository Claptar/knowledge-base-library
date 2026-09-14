---
title: Homework6 Part 01 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework6.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework6.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Homework6 Part 01 —

**Source:** [`homework/homework6.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework6.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

See the standing homework instructions on the course web page

**Problem 1** (Gamma-Poisson empirical Bayes).

Consider a hierarchical Bayes model with $$\begin{align*}
  \sigma &\sim \lambda_0\\
  \theta_i \mid \sigma &\overset{\text{i.i.d.}}{\sim}\text{Gamma}(k,\sigma) = , \;\; i=1,\ldots,n\\
  X_{ij} \mid \sigma, \theta &\overset{\text{ind.}}{\sim}\text{Pois}(\theta_i) = \frac{\theta_i^{x}e^{-\theta_i}}{x!}, \;\; i=1,\ldots,n, \quad j = 1,\ldots,m,
\end{align*}$$ where $$\text{Gamma}(k,\sigma) = \frac{1}{\Gamma(k)\sigma^{k}} x^{k - 1}e^{-x/\sigma} \quad \text{ on } x>0,$$ and $$\text{Pois}(\theta) = \frac{\theta^{x}e^{-\theta}}{x!}, \quad \text{ on } x=0,1,2,\ldots.$$

Assume $k > 0$ (shape parameter) is known. We’ll consider three possible ways an analyst could handle $\sigma$:

1.  a point mass on a fixed, known value $\sigma$ (no learning across problem instances)

2.  a point mass on a fixed, estimated value $\hat\sigma^{-1}$, estimated by maximum likelihood (empirical Bayes)

3.  a hyperprior $\sigma^{-1} \sim \text{Exp}(1)$ (hierarchical Bayes)

All Bayes estimators will be calculated with respect to squared error loss (i.e., use the posterior mean).

Here, the maximum likelihood estimator of $\sigma$ is the estimator that maximizes $p_\sigma(X)$, where we implicitly marginalize over the latent parameters $\theta_1,\ldots,\theta_n$ (called *random effects* in the frequentist model). You may use that the distribution of $X_{ij}$ given $\sigma$ is negative binomial: $$X_{ij} \mid \sigma \sim \text{NB}\left(k,\frac{1}{\sigma + 1}\right),$$ where the $\text{NB}(k,p)$ distribution has pmf $$\binom{k+x-1}{x}(1-p)^xp^k, \quad \text{ on } x=0,1,2,\ldots,$$ mean $\frac{k(1-p)}{p}$, and variance $\frac{k(1-p)}{p^2}$.

**Note:** $X_{i1}$ and $X_{i2}$ are *not* independent conditional on $\sigma$ because they are correlated through $\theta_i$.

1.  First, consider the estimator with fixed and known $\sigma$. Show that the Bayes estimator for $\theta_i$ is $$\delta_{i,\sigma}(X) = \frac{\sigma}{m\sigma + 1}\left(k+\sum_j X_{ij}\right) = \frac{\overline{X}_i + k/m}{1 + (\sigma m)^{-1}}, \quad \text{ where } \overline{X}_i = m^{-1}\sum_{j} X_{ij}.$$

2.  Show that the empirical Bayes posterior mean for $\theta_i$ is $$\frac{\overline X}{\overline{X} + k/m} (k/m + \overline{X}_i), \quad \text{ where } \overline{X}_i = m^{-1}\sum_{j} X_{ij} \quad \text{ and } \overline{X} = (nm)^{-1}\sum_{ij} X_{ij}.$$ **Hint:** To calculate the MLE, it may help to start with $m=1$, then make a sufficiency reduction remembering that if $Y\sim \text{Gamma}(k,\sigma)$ then $cY \sim \text{Gamma}(k,c\sigma)$ ($\sigma$ is a scale parameter).

    You may assume $\sum_{ij} X_{ij} > 0$ (though the formulae below would be basically correct in a limiting sense if the sum were zero, too).

3.  Now, consider the hierarchical Bayes problem where $\sigma^{-1}\sim \text{Exp}(1)$. Give an explicit algorithm for one full iteration of the Gibbs sampler, with closed-form updates. It may be helpful to look up the inverse gamma distribution on Wikipedia.

4.  Implement the Gibbs sampler in a programming language of your choice (R is recommended since it is easy to draw random draws from standard distributions; Python or Matlab will probably also work fine). For $k=m=3$ and $n=100$, download the matrix $X \in \mathbb{R}^{n \times m}$, in `gibbspoisson.csv` from the course website and implement the Gibbs sampler (the standard version where you update all variables in every round; use 100 rounds of burn-in and take the next 10,000 rounds of sampling, without thinning). Make a trace plot of your draws from $\sigma$ and $\theta_1$ and include them in your homework submission. Report the following three estimators of $\theta_1$, to three significant digits:

    1.  the hierarchical Bayes estimator (for squared error loss),

    2.  the empirical Bayes estimator, and

    3.  the UMVU estimator for $\theta_1$ in the model where $\theta$ is fixed and unknown.

5.  Next, carry out a Monte Carlo simulation to estimate the Bayes risk conditional on $\sigma$, for four estimators: (i–iii) from part (b), plus the “oracle Bayes” estimator where the value of $\sigma$ is known. That is, for each estimator $\delta_1^{(\ell)}(X)$ of $\theta_1$, approximately evaluate: $$R^{(\ell)}(\sigma) = \mathbb{E}[(\delta_1^{(\ell)}(X) - \theta_1)^2 \mid \sigma] = \mathbb{E}\left[n^{-1}\sum_i(\delta_i^{(\ell)}(X) - \theta_i)^2 \mid \sigma\right],$$ where the expectation is taken over $\theta$ and $X$ (but *not* $\sigma$, since we are conditioning on that). The second equality follows from the exchangeability over different values of $i$ (you do not need to prove it yourself, but you should use it to save yourself computation).

    **Note:** for the hierarchical Bayes estimator, this does *not* mean you should hold $\sigma$ fixed in your MCMC chain: you should compute it as an analyst who did not know the value of $\sigma$ would, and just as you did in part (d).

    Use the values $\sigma = 0.1, 0.2, 0.5, 1, 2, 5, 10$ and include a $4\times 7$ table of risk values, each reported to at least 3 significant figures, in your answer.

    For each of the three non-oracle estimators, plot the relative excess risk $$\frac{R^{(\ell)}(\sigma)}{R^{(\text{oracle})}(\sigma)} - 1$$ against $\sigma$ for the values above. Make analogous plots for the scenarios $(m,n) = (30,100)$, $(m,n)=(3,10)$, and $(m,n)=(30,10)$. I recommend using a log scale for the horizontal and vertical axis.

    **Note:** This exercise should not take you an absurd amount of computer time; using 100 MC runs per value of $\sigma$ and the 7 values of $\sigma$ above, takes my three-year-old laptop computer less than three minutes to produce each of the three plots requested above. If it is taking your computer much much longer you are probably doing something very inefficiently.

**Moral:** The hierarchical Bayes and oracle Bayes do almost the same thing: get a highly precise estimate for $\sigma$ by pooling all $n$ problems, and then carrying out the Bayes rule at the estimated value. They perform almost as well as the oracle Bayes rule because they are effective at figuring out what the true value of $\sigma$ is. This is least true for $m=3,n=10$, because there simply aren’t that many $\theta_i$ values from which to estimate $\sigma$. Note that from the perspective of estimating $\sigma$, increasing $n$ has a bigger effect on the accuracy of $\hat\sigma$ (empirical or hierarchical Bayes estimate) than increasing $m$: getting to see more $\theta_i$ values helps more than just getting to estimate each one more accurately. But increasing $m$ has a large effect on the absolute risk, because we observe each $\theta_i$ with a great deal of accuracy even before shrinking them toward the average $\theta$ value. This is also when the UMVU estimator does almost as well as oracle Bayes.

**Problem 2** (Effective degrees of freedom).

We can write a standard Gaussian sequence model in the form $$Y_i = \mu_i + \varepsilon_i, \quad \varepsilon_i \overset{\text{i.i.d.}}{\sim}N(0,\sigma^2), \quad i = 1,\ldots,n$$ with $\mu\in\mathbb{R}^n$ and $\sigma^2 > 0$ possibly unknown. If we estimate $\mu$ by some estimator $\hat\mu(Y)$, we can compute the residual sum of squares (RSS): $$\text{RSS}(\hat\mu,Y) = \|\hat\mu(Y)-Y\|^2 = \sum_{i=1}^n (\hat\mu_i(Y) - Y_i)^2.$$ If we were to observe the same signal with independent noise $Y^* = \mu + \varepsilon^*$, the expected prediction error (EPE) is defined as $$\text{EPE}(\mu,\hat\mu) = \mathbb{E}_\mu\left[\| \hat\mu(Y) - Y^*\|^2\right] = \mathbb{E}_\mu\left[\|\hat\mu(Y)-\mu\|^2\right] + n\sigma^2.$$

Because $\hat\mu$ is typically chosen to make RSS small for the observed data $Y$ (i.e., to fit $Y$ well), the RSS is usually an optimistic estimator of the EPE, especially if $\hat\mu$ tends to overfit. To quantify how much $\hat\mu$ overfits, we can define the *effective degrees of freedom* (or simply the *degrees of freedom*) of $\hat\mu$ as $$\text{DF}(\mu,\hat\mu) = \frac{1}{2\sigma^2}\mathbb{E}\left[\text{EPE} - \text{RSS}\right],$$ which uses optimism as a proxy for overfitting.

For the following questions assume we also have a predictor matrix $X\in \mathbb{R}^{n\times d}$, which is simply a matrix of fixed real numbers. Suppose that $d\leq n$ and $X$ has full column rank.

1.  Show that if $\hat\mu$ is differentiable with $\mathbb{E}_\mu\|D\hat\mu(Y)\|_F < \infty$ then $$\sum_{i=1}^n \frac{\partial \hat\mu_i(Y)}{\partial Y_i}$$ is an unbiased estimator of the DF. (Recall $D\hat\mu(Y)$ is the Jacobian matrix from class).

2.  Suppose $\hat\mu = X\hat\beta$, where $\hat\beta$ is the ordinary least squares estimator (i.e., chosen to minimize the RSS). Show that the DF is $d$. (This confirms that DF generalizes the intuitive notion of degrees of freedom as “the number of free variables”).

3.  Suppose $\hat\mu = X\hat\beta$, where $\hat\beta$ minimizes the penalized least squares criterion: $$\hat\beta = \arg\min_\beta \|Y - X\beta\|_2^2 + \rho \|\beta\|_2^2,$$ for some $\rho \geq 0$. Show that the DF is $\sum_{j=1}^d \frac{\lambda_j}{\rho+\lambda_j}$, where $\lambda_1 \geq \cdots \geq \lambda_d > 0$ are the eigenvalues of $X'X$ (counted with multiplicity) (**Hint:** use the singular value decomposition of $X$).

---

[Up: contents](index.md) · [Moral: {#moral} →](02-moral-moral.md)
