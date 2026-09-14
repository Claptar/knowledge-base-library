---
title: Least Favorable Priors
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Least Favorable Priors

**Source:** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Since $r_\Lambda$ for any prior $\Lambda$ lower-bounds the minimax risk, we have $\sup_\Lambda r_\Lambda \leq r^*$. If a prior $\Lambda^*$ attains this supremum, we call it **least favorable prior**. When the supremum is not attainable by any prior, we can still attain it in the limit by defining a sequence of priors $\Lambda_1,\Lambda_2,\ldots$ with $r_{\Lambda_n}\to \sup_\Lambda r_\Lambda$; such a sequence is called a least favorable sequence of priors.

Since $\sup_\theta R(\theta;\delta)$ for any estimator $\delta$ is also an upper bound for $r^*$, one way to show that we have a least favorable prior and a minimax estimator is to show that the Bayes risk $r_\Lambda$ and the sup-risk of  the Bayes estimator $\delta_\Lambda$ give matching lower and upper bounds:

**Theorem:** Suppose that $r_\Lambda$ and $\delta_\Lambda$ are the Bayes risk and Bayes estimator for a prior $\Lambda$, and assume that $r_\Lambda = \sup_\theta R(\theta;\delta_\Lambda)$. Then $\delta_\Lambda$ is minimax, $\Lambda$ is least favorable, and $r_\Lambda = r^*$.

Moreover, if $\delta_\Lambda$ is the unique Bayes estimator for $\Lambda$ (up to $\stackrel{\text{a.s.}}{=}$) then it is the unique minimax estimator.

*Proof:*
1. For any other estimator $\delta$, we have
$$
\begin{aligned}
\sup_\theta R(\theta;\delta)
&\geq \int R(\theta;\delta)\,d\Lambda(\theta)\\
&\geq r_\Lambda\\
&= \sup_\theta R(\theta;\delta_\Lambda),
\end{aligned}
$$
so $\delta_\Lambda$ is minimax. If $\delta_\Lambda$ is the unique Bayes estimator, then the second inequality is strict, so $\delta_\Lambda$ is the unique minimax estimator.

Moreover, we have
$$
r_\Lambda \leq r^* \leq \sup_\theta R(\theta;\delta_\Lambda) = r^*,
$$
so $r_\Lambda=r^*$ and $\Lambda$ is optimizing the lower bound.$\blacksquare$

This theorem shows that any Bayes estimator is minimax if its average-case risk is the same as its worst-case risk. The simplest way this could be true is if the risk function is constant.

More generally, it could be true if the prior puts all of its mass on parameter values that attain the worst-case risk, as in the following example:

**Example:** We observe $X\sim N(\theta,1)$ where $|\theta|\geq 1$, and we want to estimate $g(\theta)=\text{sgn}(\theta)$ under squared-error loss. Let $\Lambda$ be the prior that puts mass $1/2$ on $\theta=1$ and $\theta=-1$, and no mass anywhere else. The posterior probability that $\theta=1$ is given by
$$
\PP(\theta=1\mid X=x) = \frac{\phi(x-1)}{\phi(x-1)+\phi(x+1)},
$$
so the Bayes estimator is
$$
\EE_\Lambda[g(\theta) \mid X=x] = \frac{\phi(x-1) - \phi(x+1)}{\phi(x-1)+\phi(x+1)} = \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}} = \tanh(x).
$$
We can plot the risk function for this estimator below to verify that it attains its sup-risk at both $\theta=-1$ and $\theta=1$, and therefore on the entire support of $\Lambda$:

```r
z <- rnorm(1E5)
thet.max <- 3
curve(sapply(x, function(theta) mean( (tanh(theta+z)-1)^2)), 1,thet.max, xlim=c(-thet.max,thet.max), ylim=c(0,.5),
      xlab=expression(theta),ylab=expression(R(theta*"; "*delta[Lambda])), main=expression("Risk function for "*delta[Lambda](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/X)==tanh(X)))
curve(sapply(x, function(theta) mean( (tanh(-theta+z)-1)^2)), -thet.max,-1, add=TRUE)
abline(v=c(-1,1),lty=2)
points(x=c(-1,1), y=rep(mean( (tanh(1+z)-1)^2),2), pch=16)
```

Thus, $\delta_\Lambda(X)=\tanh(X)$ is also minimax for this problem.

**Note:** A common mistake students make is to come up with a prior $\Lambda$, then calculate $r_\Lambda$ and observe that it does not depend on $\theta$. We can apply our theorem if $R(\theta;\delta_\Lambda)$ is constant, but we haven't shown anything if we just show that $r_\Lambda$ is constant. $r_\Lambda$ for *any* prior will not depend on $\theta$, for the simple reason that we have integrated it out.

**Example (Binomial):** As a more prosaic example, consider estimating $\theta$ with squared error loss, in the model $X\sim \text{Binom}(n,\theta)$. Since we know that the Bayes estimator for the $\text{Beta}(\alpha,\beta)$ prior is $\frac{X+\alpha}{n+\alpha+\beta}$, we can see whether one of the Bayes estimators in this class has a constant risk function. If one does, it should be a symmetric prior, so we can try $\alpha=\beta$, so let $\delta_\alpha=\frac{X+\alpha}{n+2\alpha}$.

To calculate the MSE, we first calculate the mean and bias of $\delta_\alpha(X)$ as
$$
\EE_\theta \left[\frac{X+\alpha}{n+2\alpha}\right] = \frac{n\theta +\alpha}{n+2\alpha} \;\;\Longrightarrow\;\; \text{Bias}(\theta;\delta_\alpha) = \frac{\alpha (1-2\theta)}{n+2\alpha},
$$
and the variance as
$$
\Var_\theta \left(\frac{X+\alpha}{n+2\alpha}\right) =  \frac{\Var_\theta(X)}{(n+2\alpha)^{2}} = \frac{n\theta(1-\theta)}{(n+2\alpha)^{2}}.
$$

Thus, the MSE is
$$
\begin{aligned}
\text{MSE}(\theta;\delta_\alpha)
&= \frac{\alpha^2(1-2\theta)^2+ n\theta(1-\theta)}{(n+2\alpha)^{2}} \\[7pt]
&= \frac{\alpha^2+(n-4\alpha^2)\theta(1-\theta)}{(n+2\alpha)^{2}}.
\end{aligned}
$$
Setting $\alpha^* = \sqrt{n}/2$ eliminates the dependence on $\theta$, giving constant MSE of
$$
R(\theta;\delta_{\alpha^*})=\left(\frac{\alpha^*}{n+2\alpha^*}\right)^2 = \frac{n}{4(n+\sqrt{n})^2}
$$
Since $\delta_{\alpha^*}$ is the unique Bayes estimator for $\Lambda^*=\text{Beta}(\alpha^*,\alpha^*)$, we can conclude that it is the unique minimax estimator, and $\Lambda^*$ is least favorable with $r^*=r_{\Lambda^*}=\frac{n}{4(n+\sqrt{n})^2}$.

In particular, for $n=16$, we have $\alpha^*=2$ and $\delta_{\alpha^*}(X) = \frac{X+2}{X+4}$, as claimed in [Lecture 3](../estimation/index.md).

Note that while we can consider $\Lambda^*$ as a kind of "objective prior" in that it is chosen without reference to anyone's subjective opinion, it is very different from the Jeffreys prior $\text{Beta}\left(\frac{1}{2},\frac{1}{2}\right)$, which puts greatest weight on $\theta$ near $0$ and $1$ (where the Fisher information is greatest). By contrast, $\Lambda^*$ places greatest weight near $\theta=\frac{1}{2}$, where the problem of estimating $\theta$ is the most difficult (at least, as measured by squared error in the probability parameter).

```r
n <- 400
curve(dbeta(x, sqrt(n)/2,sqrt(n)/2), main=expression("Least favorable and Jeffreys priors, n = "*400), xlab=expression(theta), ylab=expression(lambda(theta)))
curve(dbeta(x, 1/2,1/2), add=TRUE, col="red")
legend("topleft",lty=1,col=1:2,legend=c("Least favorable prior","Jeffreys prior"))
```

Unfortunately, this is quite a bad estimator throughout most of the parameter space, at least for large $n$. Consider comparing the minimax estimator to the UMVU estimator $\delta_0 = X/n$, whose MSE is $\frac{\Var_\theta(X)}{n^2}=\frac{\theta(1-\theta)}{n}$:
$$
\frac{\text{MSE}(\theta;\delta_{0})}{\text{MSE}(\theta;\delta_{\alpha^*})} = \frac{\theta(1-\theta)/n}{n/4(n+\sqrt{n})^2} = 4\theta(1-\theta)\cdot (1+n^{-1/2})^2.
$$
This ratio is maximized at $\theta=\frac{1}{2}$, where the UMVU estimator is indeed suboptimal by a factor of $(1+n^{-1/2})^2\approx 1+2n^{-1/2}$ --- so the advantage increasingly minuscule as $n$ gets large. But elsewhere in the parameter space, the UMVU is dramatically better: at $\theta = 0.01$, the ratio is about $0.04$ so the UMVU estimator is beating the minimax estimator by a factor of $\approx 25$, at least for large $n$. The issue here is that the minimax estimator is overwhelmingly focusing on doing well in the center of the parameter space, where it is hardest to estimate $\theta$, at least as measured by MSE, and paying a severe price in easier regions of the parameter space.

```r
n <- 400
curve(x*(1-x)/n, main=expression("MSE for minimax and UMVU estimators, n = "*400), xlab=expression(theta), ylab=expression(MSE(theta*";"*delta)), col="red")
abline(h=n/4/(n+sqrt(n))^2)
legend("bottomright",lty=1,col=1:2,legend=c("Minimax estimator","UMVU estimator"))
```

---

[← Game theoretic interpretation](02-game-theoretic-interpretation.md) · [Up: contents](index.md) · [Least Favorable Sequence →](04-least-favorable-sequence.md)
