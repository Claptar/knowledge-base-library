---
title: The critical function
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/hypothesis-testing.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/hypothesis-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The critical function

**Source:** [`reader/hypothesis-testing.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/hypothesis-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We can describe a test by its *critical function* (a.k.a. *test function*):

$$
\phi(x) = \begin{cases}
0 & \text{accept } H_0 \\
\gamma \in (0,1) & \text{reject w.p. } \gamma \\
1 & \text{reject } H_0
\end{cases}
$$

The option of randomizing our test by taking $\phi(x) \in (0,1)$ for some values $x \in \cX$ is helpful in theory, as we will see shortly, but it is hardly ever done in practice. A non-randomized test $\phi$ partitions $\cX$ into the *rejection region* $R = \{x \in \cX: \phi(x) = 1\}$ and the *acceptance region* $A = \{x \in \cX:\; \phi(x) = 0\}$.

Most tests are defined by choosing a real-valued *test statistic* $T(X)$ and rejecting when $T(X)$ is above some *critical threshold* $c \in \RR$. We say $\phi$ *rejects for large $T(X)$* if
$$
\phi(x) = \begin{cases}
0 & T(x) < c\\
\gamma \in (0,1) & T(x) = c \text{ (if } \phi \text{ is randomized)} \\
1 & T(x) > c
\end{cases}
$$
Much of the art in designing a hypothesis test is in choosing a test statistic $T(X)$ that is as effective as possible at discriminating between $H_0$ and $H_1$

### Significance level and power

In carrying out a test, there are two types of errors that we can make: a *Type I error* (sometimes called a *false positive*) is when $H_0$ is true, but we reject it, and a *Type II error* (sometimes called a *false negative*) is when $H_0$ is false but we fail to reject it. One way to remember which is which is that the Type I error rate is of primary importance in deciding when to reject, and the Type II error rate is of secondary importance. Our usual goal, informally, is to make the probability of a Type II error under $H_1$ as small as we can, while controlling the Type I error rate below a prespecified value $\alpha \in [0,1]$. Note that if $H_0$ and $H_1$ are composite, we cannot necessarily speak of "the" Type I or Type II error rate, as it may depend on exactly which of the null or alternative parameter values we sample under.

The behavior of the test is fully summarized by the *power function* $\beta(\theta) = \mathbb{E}_\theta[\phi(X)] = \PP_\theta(\text{Reject } H_0)$. In terms of this power function, our goal can be formally stated as
$$
\maxz_\phi \beta_\phi(\theta) \text{ for } \theta \in \Theta_1 \quad \text{ subject to } \beta_\phi(\theta) \leq \alpha \text{ for } \theta \in \Theta_0.
$$
We say $\phi$ is a *level-$\alpha$ test* if $\sup_{\theta\in\Theta_0} \beta_\phi(\theta) \leq \alpha$. If this supremum is strictly below $\alpha$, we say the test is *conservative*. A very common choice for $\alpha$ is $0.05$; this began with a somewhat offhand remark by Ronald Fisher in his work when he introduced hypothesis testing, that he sometimes liked to use $0.05$ in his scientific work. It has become "the most influential offhand remark in the history of science," according to Brad Efron at Stanford.

If $H_0$ is composite, this optimization problem has multiple constraints, and if $H_1$ is composite it has multiple objectives. A major question for the remainder of this lecture is whether we can find a test $\phi^*$ that optimizes all objectives at once.

### Example: the $Z$-test

A very common setting is that we observe some statistic $Z(X) \sim N(\theta, 1)$, very often a summary statistic from a larger data set. If we are testing the one-sided hypothesis we might use the *right-tailed test* $\phi_1(z) = 1\{z > z_\alpha\}$ that rejects for large values of $Z$. Here $z_\alpha = \Phi^{-1}(1-\alpha)$ is the upper $\alpha$ quantile of the $N(0,1)$ distribution, and $\Phi(z)$ is the standard normal cdf.

If we want to test the two-sided hypothesis we might use the *two-tailed test* $\phi_2(z) = 1\{|z| > z_{\alpha/2}\}$. Now we are rejecting for large values of the test statistic $|Z|$. The rejection regions for these tests at level $\alpha = 0.1$ are plotted below, along with the alternative distribution when $\theta = 2.3$. The shaded blue region shows the power of the test under the alternative.
```r
alpha <- 0.1
z.alpha <- qnorm(1-alpha)
z.alpha2 <- qnorm(1-alpha/2)
theta1 <- 2.3
curve(dnorm(x), from=-4, to=5.5, n=1001, main="z-test rejection regions",ylab="density", xlab="z", xaxt="n", yaxt="n")
abline(h=0, lty=2,col="gray")
abline(v=0, col="gray")
curve(dnorm(x,mean = theta1),col="blue",add=TRUE)
rr.vals <- seq(z.alpha,5.5,by=.001)
polygon(c(5.5,z.alpha,rr.vals), c(0,0,dnorm(rr.vals,mean=theta1)), col="lightblue", border="blue")
text(x=theta1,y=.2,labels=expression(beta[phi[1]](theta[1])),col="blue",cex=1.3)
polygon(c(5.5,z.alpha,rr.vals), c(0,0,dnorm(rr.vals)), col="pink")
lines(c(z.alpha,z.alpha),c(0,dnorm(z.alpha)),col="red")
rr.vals <- seq(z.alpha2,4,by=.001)
polygon(c(5.5,z.alpha2,rr.vals), c(0,0,dnorm(rr.vals)), density=20)
polygon(-c(5.5,z.alpha2,rr.vals), c(0,0,dnorm(rr.vals)), density=20)
axis(side=1,at=c(-z.alpha2, z.alpha,z.alpha2,0,theta1), labels=c(expression(-z[alpha/2]), expression(z[alpha]), expression(z[alpha/2]),0, expression(theta[1])))
legend("topleft", col=c("black","blue"), c(expression(p[0](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/z)),expression(p[theta[1]](z))))
```

The two tests' power functions are plotted below for $\alpha = 0.1$.
```r
alpha <- 0.1
curve(pnorm(x - qnorm(1-alpha/2)) + pnorm(-x - qnorm(1-alpha/2)), from=-4.5, to =4.5, n=1001, main = "Power of z-test", xlab=expression(theta), ylab="Power",yaxt="n",ylim=c(0,1))
abline(h=c(0,alpha,1), lty=c(2,3,2), col="gray")
abline(v=0,col="gray")
curve(pnorm(x - qnorm(1-alpha)), col="red", n=1001, add=TRUE)
axis(2,at=c(0,alpha,1),labels=c("0",expression(alpha),"1"))
legend("bottomright",lty=1,col=2:1,legend=c(expression(beta[phi[1]](theta)), expression(beta[phi[2]](theta))))
```
The power functions for both tests intersect the vertical axis $\theta=0$ at $\alpha$, but the right-tailed test's power function remains below $\alpha$ for all $\theta < 0$ as well. Note that the right-tailed test is actually a valid test for the two-sided hypothesis, but we would be unlikely to want to use it since it has even less than $\alpha$ power to reject for negative values of $\theta$. But this may give us a hint that it will not be possible to maximize power throughout the alternative, because the two-tailed test is in fact losing out to the right-tailed test when $\theta > 0$.

For the one-sided hypothesis testing problem, however, we might hold out hope that the right-tailed test is the best for all values in the alternative (all $\theta > 0$), and indeed it is.

---

[← Hypothesis Testing](01-hypothesis-testing.md) · [Up: contents](index.md) · [Optimal testing →](03-optimal-testing.md)
