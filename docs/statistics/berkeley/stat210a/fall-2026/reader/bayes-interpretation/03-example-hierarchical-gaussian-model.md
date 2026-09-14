---
title: 'Example: Hierarchical Gaussian model'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/bayes-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Example: Hierarchical Gaussian model

**Source:** [`reader/bayes-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

A closely related example that is worth examining in more detail is the hierarchical Gaussian model. Again, suppose we observe $d$ Gaussian random variables with unit variance, whose location parameters we view as coming from the same Gaussian prior distribution:
$$
\begin{aligned}
\theta_i &\simiid N(0,\tau^2), \quad \text{ for } i = 1,\ldots,d\\
X_i \mid \theta &\simind N(\theta_i,1),
\end{aligned}
$$
Again, if $\tau^2$ is fixed then applying our result from the previous lecture gives Bayes estimator $\frac{\tau^2}{1+\tau^2}X_i$ for $\theta_i$.

## Hierarchical Bayes approach

The hierarchical Bayes approach to this problem again introduces a hyperprior on $\tau^2$:
$$
\begin{aligned}
\tau^2 &\sim \lambda_0\\
\theta_i &\simiid N(0,\tau^2), \quad \text{ for } i = 1,\ldots,d\\
X_i \mid \theta &\simind N(\theta_i,1)
\end{aligned}
$$
Then we have the Bayes estimator
$$
\EE[\theta_i \mid X] = \EE\left[ \; \frac{\tau^2}{1+\tau^2} X_i \mid X \;\right] = \EE\left[ \frac{\tau^2}{1+\tau^2} \mid X\right] \cdot X_i.
$$

It will be convenient to parameterize using $\zeta(\tau^2) = \frac{1}{1+\tau^2}$, giving the *linear shrinkage estimator*
$$
\delta_{\zeta}(X) = (1-\zeta)X,
$$
so that $\zeta \in (0,1)$ reflects what we might call the *shrinkage factor*. Then we see that the hierarchical Bayesian estimator
$$
\EE[\theta_i \mid X] = \EE[1-\zeta\mid X]\cdot X_i = (1-\EE[\zeta\mid X])X_i
$$

is simply $\delta_{\hat\zeta}(X)$, where $\hat\zeta = \EE[\zeta \mid X]$ is the posterior mean of $\zeta$ given all the data. This case shows the very close relationship between hierarchical Bayes and empirical Bayes: here, the hierarchical Bayes solution itself amounts to plugging a (Bayes) estimate for the hyperparameter $\zeta$ into our formula for the optimal Bayes shrinkage rule if we knew $\zeta$.

To find $\EE[\zeta \mid X]$, it is again helpful to consider the likelihood model with $\theta$ marginalized out. Then, we have
$$
\begin{aligned}
\zeta &\sim \lambda_0^{(\zeta)}\\
X_i \mid \zeta &\simiid N(0, \zeta^{-1}),
\end{aligned}
$$
since
$$
\Var(X_i \mid \zeta) = \Var(\theta_i \mid \zeta) + \EE[\Var(X_i \mid \zeta, \theta_i)] = \tau^2+1
$$
The likelihood of $X$, then, is
$$
X\mid \zeta \sim N_d(0,I_d/\zeta) = \frac{\zeta^{d/2}}{(2\pi)^{d/2}} e^{-\zeta\|x\|^2/2},
$$
an exponential family with sufficient statistic $T(X)= \|X\|^2 \sim \frac{1}{\zeta}\chi_d^2$.

A conjugate prior for $\zeta$ in this model is the Gamma prior, but the calculations work out slightly better if we use a scaled $\chi^2$ prior:
$$
\zeta \sim \frac{1}{s}\chi_k^2 = \text{Gamma}(k/2,2/s) = \frac{1}{\Gamma(k/2)(2/s)^{k/2}}\zeta^{k/2-1}e^{-\zeta s/2},
$$
which has mean $k/s$ and variance $2k/s^2$. Then
$$
\lambda(\zeta \mid x) \propto_\zeta \zeta^{(k+d)/2-1} e^{-\zeta (\|x\|^2 + s)/2)} \propto_\zeta \frac{1}{s+\|x\|^2}\chi_{k+d}^2,
$$
giving $\EE[\zeta \mid X] = \frac{k+d}{s+\|x\|^2}$.

Note that to be more correct, we should truncate our prior to the unit interval since $\zeta \in (0,1)$. Then our calculations would have to remain numerical, but for large $d$ the prior would be concentrated in $(0,1)$ and they would turn out much the same.

## Empirical Bayes approach

The empirical Bayes approach would estimate $\zeta$ and plug the estimator into the Bayes rule formula $(1-\zeta)X$, again based on the sufficient statistic $T(X) = \|X\|^2 \sim \frac{1}{\zeta}\chi_d^2$. If we used as our estimator any Bayes posterior mean for a prior $\lambda_0$ on $\zeta$, we would simply recover the hierarchical Bayes estimator from above.

Another choice is the maximum likelihood estimator, which in exponential families (as we will see) simply solves for the value of $\zeta$ at which the sufficient statistic's expectation $\EE_\zeta T(X) = d/\zeta$ is equal to its realized value; hence $\hat\zeta_{\text{MLE}}(X) = \frac{d}{\|X\|^2}$.

A third choice is the UMVU estimator. Because $T(X)= Y/\zeta$ for $Y \sim \chi_d^2$, we must have
$$
\EE\left[\frac{1}{\|X\|^2}\right] = \EE\left[\frac{1}{Y}\right] \cdot \zeta.
$$
For $d>2$ we can calculate this expectation, which does not depend on $\zeta$:
$$
\begin{aligned}
\EE\left[\frac{1}{Y}\right]
&= \int_0^\infty \frac{1}{y}\cdot \frac{1}{\Gamma\left(\frac{d}{2}\right)2^{d/2}} y^{d/2-1}e^{-y/2}\,dy\\[7pt]
&= \frac{\Gamma\left(\frac{d-2}{2}\right)\cdot 2^{(d-2)/2}}{\Gamma\left(\frac{d}{2}\right)\cdot 2^{d/2}} \cdot \int_0^\infty \frac{1}{\Gamma\left(\frac{d-2}{2}\right)2^{(d-2)/2}} y^{(d-2)/2-1}e^{-y/2}\,dy\\[7pt]
&= \frac{\Gamma\left(\frac{d-2}{2}\right)\cdot 2^{(d-2)/2}}{\Gamma\left(\frac{d}{2}\right)\cdot 2^{d/2}},
\end{aligned}
$$
since the last integrand is the $\chi_{d-2}^2$ density. Since $\Gamma(x+1) = x\Gamma(x)$ for all $x>0$, the final expression can be simplified to $\frac{1}{d-2}$. As a result, $\frac{d-2}{\|X\|^2}$ is UMVU, giving empirical Bayes estimator
$$
\delta_{\text{JS}}(X) = \left(1-\frac{d-2}{\|X\|^2}\right) X.
$$
This estimator, called the James--Stein estimator, is very interesting in its own right, as we will see in two lectures.

---

[← Where Does the Prior Come From?](02-where-does-the-prior-come-from.md) · [Up: contents](index.md)
