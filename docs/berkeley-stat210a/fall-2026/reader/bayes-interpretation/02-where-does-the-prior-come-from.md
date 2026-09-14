---
title: Where Does the Prior Come From?
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/bayes-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Where Does the Prior Come From?

**Source:** [`reader/bayes-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Evading the problem of induction

We discussed in [Lecture 1](../introduction/index.md) that there are, broadly speaking, two ways that we can evade the problem of induction. So far in this semester, we have focused on the evasion of *inductive behavior*: as statistical methodologists, we can devise methods for estimation, testing, and other decision problems and analyze these methods' MSEs, or bound their Type I error rates, treating $\theta$ as an unknown quantity that can vary freely over the parameter space (and is not necessarily governed by a prior). A frequentist is willing to present an estimator, prove that it is highly precise (say, that it's off by $0.1$ no more than $1\%$ of the time), and then use it to calculate an estimate $\delta(X)$ for $\theta$ on a given data set $X$. But if you ask them whether we can say that $\theta$ is therefore probably close to the estimate they just calculated, they may deny that the question even makes sense. $X$ has already been realized so there is no more probability left in the problem to talk about; the probability statement they were making before was only with respect to its distribution.

If frequentist methods evade the problem of induction by answering a different question, Bayesian methods evade it by begging the question. In the Bayesian paradigm, we can use the posterior distribution to freely make statements about the posterior distribution of $\theta$. The only trouble is that these statements follow from an assumption we made, before seeing the data, about the prior distribution of $\theta$. So the Bayesian must be prepared to answer questions about where the prior comes from.[^1]

[^1]: Note that Bayesians often retort that coming up with the likelihood is no less problematic because it also commonly involves a great deal of subjective judgment --- this is certainly true in some cases (and less true in others), but at least we usually sample repeatedly from the likelihood so we can usually check assumptions like independence of successive observations, normality of errors, and so on.


## Subjective priors

If we take the subjectivist view, coming up with a prior boils down to introspection about what our prior beliefs actually are. For example, if we introspect about our subjective beliefs about bias of a new coin we encounter, our subjective prior might look roughly like the stylized picture below, placing most of the mass close to $0.5$, but reserving some subjective probability that the coin is a trick coin that is either going to land heads or tails with probability close to $1$, or has some other wildcard distribution. The picture below is a mixture of a $\text{Beta}(400,400)$ (the central bump), a $\text{Beta}(0.1,0.1)$ (the spikes at the extremes), and $\text{Beta}(1,1)=\text{Unif}[0,1]$ (wildcard option to cover all bases), with $90\%$, $15\%$, and $5\%$ prior mass on each theory (perhaps we are slightly suspicious of the person presenting us with the coin).

```r
alpha.big <- 400
alpha.small <- 0.1
subjective.prior <- function(x) {
  0.05 * dbeta(x, 1,1) + 0.15*dbeta(x,alpha.small,alpha.small) + .8*dbeta(x,alpha.big, alpha.big)
}
curve(subjective.prior(x), n=1001, ylim=c(0,1.05*subjective.prior(.5)), main="Subjective prior on coin bias", ylab=expression(lambda(theta)),xlab=expression(theta))
grid()
abline(v=0:1,h=0,lty=3)
curve(subjective.prior(x), 0,0.01, 101, add=TRUE)
curve(subjective.prior(x), 0.99,1, 101, add=TRUE)
```
Suppose this is our prior, and we flip the coin $10$ times, getting $7$ heads. Our posterior will then look like the following distribution:

```r
normalizing.const <- integrate(function(x) subjective.prior(x) * dbinom(7,10,x), 0, 1)$value
subjective.posterior <- function(x) {
  subjective.prior(x) * dbinom(7,10,x) / normalizing.const
}
curve(subjective.posterior(x), n=1001, main="Subjective posterior after 7 heads and 3 tails", ylab=expression(lambda(theta ~ "|" ~ X==7)), xlab=expression(theta))
grid()
abline(v=0:1,h=0,lty=3)
curve(subjective.posterior(x), 0,0.01, 101, add=TRUE)
curve(subjective.posterior(x), 0.99,1, 101, add=TRUE)
posterior.mean <- integrate(function(x) x * subjective.posterior(x), 0, 1)$value
```

The posterior mean, $\delta_{\lambda}(7)\approx 0.52$, is probably a more reasonable estimate than we'd get if we used the UMVU estimator $X/n=0.7$.

On the other hand, if we observed $10$ heads on $10$ flips, our subjective posterior would become convinced of the right extreme, and we'd get the following posterior with mean $\delta_\lambda(10)\approx 0.98$:

```r
normalizing.const <- integrate(function(x) subjective.prior(x) * dbinom(10,10,x), 0, 1)$value
subjective.posterior <- function(x) {
  subjective.prior(x) * dbinom(10,10,x) / normalizing.const
}
curve(subjective.posterior(x), n=1001, main="Subjective posterior after 10 heads and 0 tails", ylab=expression(lambda(theta ~ "|" ~ X==10)), xlab=expression(theta))
grid()
abline(v=0:1,h=0,lty=3)
curve(subjective.posterior(x), 0,0.01, 101, add=TRUE)
curve(subjective.posterior(x), 0.99,1, 101, add=TRUE)
posterior.mean <- integrate(function(x) x * subjective.posterior(x), 0, 1)$value
```

This approach has several advantages. First, if the prior reflects our beliefs before seeing the data, then the posterior has the philosophically straightforward interpretation of reflecting our beliefs after seeing the data. Another benefit of the approach is that, as we have seen, it can bring real information to bear on the problem in a useful way.

However, the approach can be difficult to carry out in practice. We saw this with the nonparametric example above, but similar issues arise in parametric problems with a large number of parameters: what is your subjective joint prior distribution over the effects of one million single nucleotide polymorphisms on a person's likelihood of suffering from diabetes?

The subjectivity of the answer we obtain through this approach is not an issue in some contexts (for example, if we are running a business) but it has limited the application of subjective Bayesian statistics in scientific endeavors. It is embarrassing to write in the abstract that "in my opinion, the mass of the Higgs boson is between..."

In response to this, some practitioners look for "objective" rules for selection of the prior:

## Objective or vague priors

If we prefer not to have our subjective beliefs influence the result, we might pick a prior that implements a kind of "principle of indifference," meaning that before we see any data we should give equal weight to all possibilities. This is simple to implement when the parameter space $\Theta$ is finite, but for the more common case of a continuous parameter space, it is less clear what it means to assign equal probability to all parameter values. Indeed, *any* continuous prior would assign zero probability to every individual value.

### Flat prior

Instead, we can try to spread probability around equally to equally sized neighborhoods. One popular choice of objective prior is the flat prior, which uses a uniform density on $\Theta$. If $\Theta$ is not bounded, we can still use $\lambda(\theta) = 1$ as an *improper* prior, meaning it is non-normalizable. Even though the prior is not normalizable, it is commonly the case that the posterior will nevertheless be normalizable because the likelihood is: for example, consider the simple problem
$$
\begin{aligned}
\theta &\sim \lambda(\theta) = 1\\
X\mid \theta &\sim N(\theta,\sigma^2) = \frac{1}{\sqrt{2\pi}}e^{-(x-\theta)^2/2\sigma^2}
\end{aligned}
$$
In this problem, if we ignore the fact that the prior is improper and just chug through the calculations, we get
$$
\lambda(\theta \mid x) \propto_\theta \lambda(\theta) p_\theta(x) = \frac{1}{\sqrt{2\pi}}e^{-(\theta-x)^2/2\sigma^2} = N(x,\sigma^2),
$$
which is a normalizable posterior.

### Jeffreys prior

The flat prior spreads mass evenly across the parameter space, but that makes it dependent on how we parameterize our model.

**Example: Different parameterizations of a binomial model**

Consider a $\text{Binom}(n,\theta)$ model, and suppose that we place a flat prior on the probability parameter $\theta$. The resulting prior on the natural parameter $\eta(\theta) = \log\frac{\theta}{1-\theta}$ is obtained by the change of variables formula with inverse $\theta(\eta) = \frac{e^{\eta}}{1+e^\eta}$:
$$
\lambda^{(\eta)}(\eta) =  |\dot\theta(\eta)|\lambda^{(\theta)}(\theta(\eta)) = \frac{e^{\eta}}{(1+e^{\eta})^2}.
$$
That is, the prior density tends to zero as $|\eta|$ tends to $\infty$. Intuitively, the portion of our model with $\eta\in [-11,-10]$ is the same as the portion with $\theta \in [1.7\times 10^{-5}, 4.5\times 10^{-5}]$, which is assigned virtually no prior mass.

By contrast, if we place a (non-normalizable) flat prior on $\eta$, we end up with an improper prior on $\theta$ that is proportional to $\frac{1}{\theta(1-\theta)}$, which we can think of as the limit of a $\text{Beta}(\alpha,\alpha)$ distribution with $\alpha\to 0$. As a prior on $\theta$, this effectively places very high mass at the extremes of the parameter space --- again intuitively, because the very small interval $\theta\in [0.0001,0.01]$ corresponds to an interval of length roughly $4.6 \approx \log(100)$ in the natural parameter space.

To address this issue, we can instead use the **Jeffreys prior**, which tries to spread the prior mass evenly over our statistical model in a way that is invariant to the parameterization. The Jeffreys prior in a given parameterization is the (possibly improper) prior that is proportional to $|J(\theta)|^{1/2}$, where $|J(\theta)|$ is the determinant of the Jacobian:
$$
\lambda_{\text{Jeff}}(\theta) \propto_\theta |J(\theta)|^{1/2}
$$
The Jeffreys prior is invariant to smooth re-parameterization of the model and, it can be shown (HW 6), corresponds to assigning equal prior mass to small neighborhoods of the same size, as measured by the KL divergence.

**Example, Continued.**
In the binomial model, the Fisher information with respect to the natural parameter is $J^{(\eta)}(\eta) = \Var_\eta(X)$, so the Fisher information with respect to $\theta$ is
$$
\dot\eta(\theta)^2 \Var_{\theta}(X) = \left(\theta(1-\theta)\right)^{-2}\cdot n\theta(1-\theta) = \frac{n}{\theta(1-\theta)}
$$
Thus, the Jeffreys prior on $\theta$ is
$$
\lambda_{\text{Jeff}}^{(\theta)}(\theta) \propto_\theta \sqrt{\frac{1}{\theta(1-\theta)}} \propto_\theta \text{Beta}\left(\frac{1}{2},\frac{1}{2}\right).
$$
If we carry out the same calculation for the natural parameter, the Fisher information is
$$
J(\eta) = \Var_\eta(X) =\theta(\eta)(1-\theta(\eta)) = n\frac{e^{\eta}}{(1+e^{\eta})^2},
$$
so the Jeffreys prior is
$$
\lambda_{\text{Jeff}}^{(\eta)}(\eta) \propto_\eta \sqrt{\frac{e^{\eta}}{(1+e^{\eta})^2}}.
$$
These two priors are the same: applying the change of variables formula to $\lambda_{\text{Jeff}}^{(\theta)}(\theta)$ gives
$$
\lambda^{(\eta)}(\eta) = |\dot\theta(\eta)|\lambda_{\text{Jeff}}^{(\theta)}(\theta(\eta)) = \sqrt{\frac{e^{\eta}}{(1+e^{\eta})^2}}
$$

### Drawbacks of vague priors

That vague priors can sometimes be improper can be a drawback. When we use an improper prior, we will not necessarily retain all of the decision-theoretic advantages of a proper prior, such as admissibility (see HW 5). For example, we can see this by returning to the example we examined when we raised doubts about unbiasedness

**Example:** We observe $X \sim N_d(\mu, I_d)$ for  $\mu \in \RR^d$, and we want to estimate $\rho^2 = g(\mu) = \|\mu\|^2$. If we use a flat prior (or a Jeffreys prior, which amounts to the same thing in this case), the posterior is again just the likelihood $\lambda(\mu \mid x) = N_d(x,I_d)$. The posterior mean of $\mu$ is $\EE[\mu \mid X] = X$, which is a very reasonable estimator, but the posterior mean of $\rho^2$ is much more questionable:
$$
\delta_\lambda(X) = \EE[\|\mu\|^2 \mid X] = \|X\|^2 + d.
$$
Recalling that the UMVU estimator was $\|X\|^2 - d$, we may be disturbed to find that we have added a bias of $2d$ without changing the variance at all, so $\text{MSE}(\mu; \delta_\lambda) = \text{MSE}(\mu; \delta_{\text{UMVU}}(X)) + 4d^2$. This penalty could be far larger than the variance of $\|X\|^2$, which is $O(d)$ for small values of $\mu$.

Why did we get such a bad estimator? One way to see this is by examining the effective prior on $\rho$: for small $\ep > 0$, the event that $\|\mu\| \in [r,r+\ep]$ is a spherical shell of width $\ep$, whose volume is proportional to $r^{d-1}\ep$, so the probability density grows rapidly in $r$. Because there are many more values of $\mu$ with large $\|\mu\|$ than with small $\|\mu\|$, the prior puts much more mass on them, and this pushes up our estimator.


Another conceptual difficulty comes when we try to interpret the posterior. If the prior was no one's subjective belief before seeing the data, the posterior is also no one's subjective belief after seeing the data. But then, what is it?


### Intersubjective Agreement

Flat priors are especially attractive in cases when the prior really doesn't matter. For example, when we have a lot of data in a relatively low-dimensional parameter space, the data may effectively rule out most $\theta$ values because the likelihood is extremely low outside of a relatively small region of the parameter space. A somewhat extreme example of this type is the coin flipping data we saw in [Lecture 1](../introduction/index.md) where $n=350,757$ and $X=178,079$, where the likelihood is proportional to $\theta^{178,079}(1-\theta)^{172,678}$, a function with an extremely narrow peak near $X/n\approx 0.508$.
```r
X <- 178079
n <- 350757
curve(dbinom(X,n,x), from=X/n-.01, X/n+.01, 10001, main="Binomial likelihood for n = 350k, X=178k", xlab=expression(theta), ylab=expression(p[theta](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/X)))
abline(h=0, lty=2)
```
If we multiply this by nearly any prior and then renormalize, we will essentially get back the likelihood again. The plot below shows the posterior for the uniform (flat) and Jeffreys on $\theta$, as well as our subjective prior from above and a strongly biased prior corresponding to 100 pseudo-successes and 0.1 psuedo-failures.

```r
library(RColorBrewer)
pal <- brewer.pal(3,"Set1")
curve(dbeta(x,X+1,n-X+1), from=X/n-.01, X/n+.01, 10001, main="Posterior for various priors", xlab=expression(theta), ylab=expression(p[theta](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/X)))
curve(dbeta(x,X+1/2,n-X+1/2), n=10001, add=TRUE, col=pal[1], lty=3,lwd=3)
normalizing.const <- integrate(function(x) subjective.prior(x) * dbinom(X,n,x), .5, .52)$value
subjective.posterior <- function(x) {
  subjective.prior(x) * dbinom(X,n,x) / normalizing.const
}
curve(subjective.posterior(x), n=10001, add=TRUE, col=pal[2], lty=2,lwd=2)
curve(dbeta(x,X+100,n-X+0.1), n=10001, add=TRUE, col=pal[3], lwd=2)
abline(h=0, lty=2)
legend("topleft", legend = c("Uniform","Jeffreys","Subjective prior","Beta(100,0.1)"), col=c("black",pal), lty=c(1,3,2,1),lwd=c(1,3,2,1))
```
The posteriors converge even though these priors entail very different prior assumptions about $\theta$, which we can see if we plot them (note the horizontal axis limits have changed to show the entire parameter space):
```r
library(RColorBrewer)
pal <- brewer.pal(3,"Set1")
curve(subjective.prior(x), from=0, to=1, 10001, col=pal[2], lty=2,lwd=2, ylim=c(0,20),main="Various priors", xlab=expression(theta), ylab=expression(p[theta](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/X)))
abline(h=0, lty=2)
curve(dbeta(x,1/2,1/2), n=10001, add=TRUE, col=pal[1], lty=3,lwd=3)
curve(dbeta(x,1,1), n=10001, add=TRUE)
curve(dbeta(x,100,0.1), n=10001, add=TRUE, col=pal[3], lwd=2)
legend("topleft", legend = c("Uniform","Jeffreys","Subjective prior","Beta(100,0.1)"), col=c("black",pal), lty=c(1,3,2,1),lwd=c(1,3,2,2))
```
These priors are very different, but what they all have in common is that they are roughly flat on the narrow interval $[0.5,0.515]$.


## Convenience priors

Because Bayesian inference is often computation-heavy, one important practical goal in choosing a prior is computational tractability. In most Bayesian models, the priors used are exponential families, often ones that are conjugate to the likelihood.

One justification people sometimes use for choosing exponential priors relates to a kind of generalization of the principle of indifference called the **maximum entropy principle**. The entropy of a density relative to some base measure $\mu$ on a sample space $\cX$ is defined as follows:
$$
H(p) = -\int_{\cX} p(x) \log p(x)\,d\mu(x),
$$
If $\mu$ is a finite measure, the entropy simply $\log\mu(\cX)$ minus the KL divergence from $p$ to the uniform density $p_{\text{unif}}(x)\equiv \frac{1}{\mu(\cX)}$:
$$
D_{\text{KL}}(p \,\|\, p_{\text{unif}}) = \int_{\cX} p(x)\log\frac{p(x)}{\mu(\cX)^{-1}}\,d\mu(x) = \log\mu(\cX)- H(p).
$$
As a result, the entropy maximizing distribution is simply the uniform distribution itself. More generally suppose we impose a constraint that some statistic $T(X) \in \RR^s$ has expectation $\nu\in \RR^s$, i.e. $\EE_p T(X) = \nu$. If the constraint is feasible, it can be shown that the constrained maximum-entropy distribution is of the form $p(x) = e^{\eta'T(x)-A(\eta)}$, where $\eta$ is chosen to satisfy the constraint; that is, constrained entropy-maximizing distributions are exponential family distributions.

Suppose that we want our prior to have mean $\EE_\lambda\theta = \nu$ and variance $\Var_\lambda\theta = \sigma^2$, but otherwise we want to remain indifferent about what functional form it should take, perhaps because we find it difficult to say what our prior beliefs about $\theta$ are in such detail. If we choose the exponential family distribution with sufficient statistics $S(\theta) = (\theta,\theta^2)$ and assign the natural parameters so $\EE_\lambda S(\theta) = (\nu, \nu^2+\sigma^2)$, we will have chosen the entropy-maximizing prior among all priors that match our mean and variance assumptions --- and the prior will likely be mathematically convenient as well! In particular, if the base measure $\mu$ is the Lebesgue measure on $\RR$, then our prior is exactly $N(\nu,\sigma^2)$.

## Prior or Concurrent Experience

The best source of a prior, when available, is prior or concurrent experience with other instances of similar statistical problems. If we assume the parameter values for those problems are drawn independently from the same prior, we can fruitfully incorporate all of the data into the model. In this case, even a frequentist might agree that it is reasonable to model the parameter values for the different problems as being drawn from a probability distribution.

There are two closely related ideas for how to learn a prior distribution from a set of similar problem instances. The more frequentist idea is called **empirical Bayes**: instead of inventing the prior, we treat it as an unknown quantity and *estimate* it from the data. The Bayesian idea, called **hierarchical Bayes**, is that we treat the parameters of the prior as additional Bayesian parameters to estimate, assign a prior to them, and learn them from the data using Bayesian inference on the full model. In practice, these two approaches can look and perform very similarly to each other.


**Example: Hierarchical Beta-binomial model**

Consider, for example, assuming that the $m=48$ coin flippers in the Bartosz et al. paper have different same-side biases $\theta_1,\ldots,\theta_m$, that these $\theta_i$ values are drawn from a common Beta distribution.
$$
\begin{aligned}
\theta_i &\simiid \text{Beta}(\alpha,\beta), \quad \text{ for } i = 1,\ldots,m\\
X_i \mid\theta &\simind \text{Binom}(n_i, \theta_i)
\end{aligned}
$$
We have already calculated the posterior mean of $\theta_i$ for fixed $\alpha$ and $\beta$:
$$
\delta_{i;\alpha,\beta}(X) = \EE[ \theta_i \mid X] = \frac{X_i+\alpha}{n_i+\alpha+\beta}.
$$
Note that this only depends on $X_i$: when $\alpha$ and $\beta$ are fixed, the $(\theta_i,X_i)$ pairs are independent, so observing $X_2,\ldots,X_m$ tells us nothing about the distribution of $(\theta_1,X_1)$.

If we were solving only one problem of this type, we might select $\alpha$ and $\beta$ to get a uniform prior ($\alpha=\beta=1$), a Jeffreys prior ($\alpha=\beta=1/2$), or an informative prior ($\alpha$ pseudo-successes and $\beta$ pseudo-failures), but if we are solving many problems at once we can learn the prior parameters.

For an empirical Bayes approach to selecting $\alpha$ and $\beta$, we would likely begin by observing that, after marginalizing out $\theta_1,\ldots,\theta_m$, we have the likelihood model:
$$
X_i \sim \text{Beta-Binom}(n_i,\alpha,\beta),
$$
and estimate $\alpha$ and $\beta$, usually by maximum likelihood. Then we would plug these values in to obtain our best estimate of the optimal Bayes estimator:
$$
\delta_{i;\hat\alpha,\hat\beta}(X) = \frac{X_i + \hat\alpha}{n_i + \hat\alpha+\hat\beta}.
$$

The hierarchical Bayes approach is that we assign them to have a common **hyperprior** $\lambda_0$:

$$
\begin{aligned}
\alpha,\beta&\sim \lambda_0(\alpha,\beta)\\
\theta_i \mid \alpha,\beta &\simiid \text{Beta}(\alpha,\beta), \quad \text{ for } i = 1,\ldots,m\\
X_i \mid \alpha,\beta,\theta &\simind \text{Binom}(n_i, \theta_i)
\end{aligned}
$$
Again, if we condition on $\alpha$ and $\beta$, the problems have nothing to do with each other. But observe what happens when the parameters $\alpha,\beta$ are unknown:

$$
\begin{aligned}
\delta_i(X) &= \EE[\theta_i \mid X]\\
&= \EE\left[ \; \EE[\theta_i \mid X, \alpha, \beta] \mid X\;\right] \\
&= \EE\left[ \; \frac{X_i+\alpha}{n_i+\alpha+\beta} \mid X\;\right] \\
&= \int_{\alpha,\beta} \frac{X_i+\alpha}{n_i+\alpha+\beta} \,d\lambda(\alpha,\beta \mid X).
\end{aligned}
$$
That is, our final estimator is a *mixture* over estimators of the form $\frac{X_i+\alpha}{n_i+\alpha+\beta}$, where $\alpha,\beta$ are sampled from their joint posterior distribution after seeing all of the data. Thus, in a sense we have learned from the full data set how to estimate $\theta_i$ from $X_i$.

If $m$ is large, then the amount of data we have all together may be much greater than the amount of data we have for each problem instance. Then we potentially have the best of both worlds: an informative prior that helps us better estimate each $\theta_i$, but strong intersubjective agreement about *which* hyperparameters $\alpha,\beta$ we should use for that prior.

---

[← Interpretations of Probability](01-interpretations-of-probability.md) · [Up: contents](index.md) · [Example: Hierarchical Gaussian model →](03-example-hierarchical-gaussian-model.md)
