---
title: Two-sided alternatives
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-one-parameter.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/testing-one-parameter.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Two-sided alternatives

**Source:** [`reader/testing-one-parameter.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-one-parameter.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Often we want to test a null hypothesis against the alternative that the parameter is larger *or* smaller than a null value, or range of values. This section will consider a null hypothesis of the form $H_0:\; |\theta - \theta_0| \leq \delta$ against the alternative $H_1:\; |\theta - \theta_0| > \delta$, for some tolerance $\delta \geq 0$. In the important special case $\delta = 0$ we will call $H_0$ a *point null*, and if $\delta > 0$ we will call $H_0$ an *interval null*.

### Two-tailed tests

To test a two-sided alternative, we will generally employ a *two-tailed test* based on some test statistic $T(X)$. We will say that $\phi(X)$ *rejects for extreme $T(X)$* (i.e., for large or small values of $T(X)$) if
$$
\phi(X) = \begin{cases} 1 & \quad \text{ if } T(X) < c_1 \text{ or } T(X) > c_2\\
0 & \quad \text{ if } c_1 < T(X) < c_2\\
\gamma_i &\quad \text{ if } T(X) = c_i, \; i = 1,2
\end{cases}
$$

When we test with a two-sided alternative we will generally not be able to optimize power everywhere. For example, if we test $H_0:\; \theta = 0$ vs $H_1:\; \theta \neq 0$ in the $z$-test problem $X \sim N(\theta,1)$, we can choose any test of the form
$$
\phi_{\alpha_1}(x) = 1\{x < -z_{\alpha_1}\} + 1\{x > z_{\alpha - \alpha_1}\},
$$
for any $\alpha_1 \in [0,\alpha]$. We obtain the right- and left-tailed tests in the limit where $\alpha$ is $0$ or $\alpha$ respectively, and the usual symmetric two-tailed test when $\alpha_1 = \alpha/2$.


```r
alpha <- 0.1
alpha1.vals <- c(alpha/10, alpha/2, 3*alpha/4)
plot(0,0,type="n", ylim=c(0,1), xlim=c(-5,5), main="Power for different two-tailed z-tests",
     xlab=expression(theta), ylab="Power")
grid()
abline(h=c(0,alpha,1), lty=3)
abline(v=0, lty=3)
library(RColorBrewer)
cols <- brewer.pal(length(alpha1.vals), "Set1")
for(ix in 1:length(alpha1.vals)) {
  alpha1 <- alpha1.vals[ix]
  c1 <- qnorm(alpha1)
  c2 <- qnorm(alpha-alpha1, lower.tail=FALSE)
  curve(pnorm(c1-x) + pnorm(x-c2), n=1001, add=T, col=cols[ix])
}
legend("bottomright", lty=1, col=cols, legend=c(expression(alpha[1] == alpha[1]/10),expression(alpha[1] == alpha/2), expression(alpha[1] == 3*alpha/4)))
axis(2, at=alpha, labels=expression(alpha))
```
Note that two of the three tests shown above have the undesirable property that the power falls below $\alpha$ on part of the alternative: that is, there are alternative values of $\theta$ for which our chance of rejecting the null is even less than it would be if the null were true.

None of the tests plotted above is as powerful for $\theta > 0$ as the right-tailed test ($\alpha_1 = 0$), and none is as powerful for $\theta < 0$ as the left-tailed test ($\alpha_1 = \alpha$), and intuitively it is clear that we cannot hope to find a test that maximizes power on both parts of the alternative.

As in the case with estimation, one way that we can proceed when there is no UMP test is to impose a constraint that rules out all but one test. In the $z$-test above, the test with $\alpha_1 = \alpha/2$ is symmetric in two respects:

1) It is *equal-tailed*, meaning that we have dedicated an equal portion of our total Type I error budget to the left and right lobes of the rejection region, and

2) It is *unbiased*, meaning that the power is at least $\alpha$ everywhere on the alternative.

The idea of an equal-tailed test makes sense when $H_0$ is simple, but it is not obvious how it extends to the more common situation where $H_0$ is composite. We will focus on the latter condition, unbiasedness.

### Exponential example

Consider testing $H_0:\;\theta = 1$ vs $H_1:\;\theta \neq 1$ in the model where $X \sim \text{Exp}(\theta)$, with cdf
$$F_\theta(t) = \PP_\theta(X \leq t) = 1-e^{-t/\theta}.$$
To solve for the equal-tailed test cutoffs we set $c_1^{\text{ET}}=F_1^{-1}(1-\alpha/2) = -\log(1-\alpha/2)$ and $c_2^{\text{ET}}= F_1^{-1}(\alpha/2) = -\log(\alpha/2)$. Then the power function of the equal-tailed test  $\phi^{\text{ET}}$ is

$$
\begin{aligned}
\beta_{\phi^{\text{ET}}}(\theta)
&= \PP_\theta(X < c_1^{\text{ET}}) + \PP_\theta(X > c_2^{\text{ET}})\\
&= 1 - e^{-c_1^{\text{ET}}/\theta} +e^{-c_2^{\text{ET}}/\theta}\\
&= 1 - (1-\alpha/2)^{1/\theta} + (\alpha/2)^{1/\theta}
\end{aligned}
$$
This test does indeed have power equal to $\alpha$ at $\theta = 1$, but its power is also $\alpha$ at $\theta = 1/2$, and the power is actually below $\alpha$ on $(1/2,1)$. So this is not an unbiased test. If we want an unbiased test, we need to set the *derivative* of the power equal to $0$ at $\theta = 1$. We can solve this numerically in terms of the left-lobe rejection probability $\alpha_1$, taking
$$
\begin{aligned}
c_1(\alpha_1) &=-\log(1-\alpha_1), \quad\text{ and }\\
c_2(\alpha_1) &= -\log(\alpha_2)=-\log(\alpha-\alpha_1).
\end{aligned}
$$
If $\alpha = 0.1$ we obtain $\alpha_1 = 0.080$, $c_1 = 0.083$, and $c_2 = 3.9$ for the unbiased test, vs $c_1 = 0.051$ and $c_2 = 3.0$ for the equal-tailed test. The unbiased test is not as powerful for $\theta > 1$, but it is more powerful for $\theta < 1$, and its power is minimized at $\alpha$ when $\theta = 1$. We plot both power curves below.

```r
alpha <- 0.1
curve(pexp(-log(1-alpha/2), rate=1/x) + pexp(-log(alpha/2), rate=1/x, lower.tail=FALSE), from=0, to=7, ylim=c(0,1), ylab="Power", xlab=expression(theta),
      main=expression(paste("Equal-tailed vs unbiased test for ",H[0]:theta==1," (Exponential model)")))
grid()
abline(h=c(0,alpha,1), lty=3)
abline(v=c(0,0.5,1), lty=3)
alpha1 <- uniroot(function(a1) (1-a1)*log(1-a1) - (alpha - a1)*log(alpha-a1), interval = c(0.001,alpha-.001))$root
c1.unbiased <- -log(1-alpha1)
c2.unbiased <- -log(alpha-alpha1)
curve(pexp(c1.unbiased, rate=1/x) + pexp(c2.unbiased, rate=1/x, lower.tail=FALSE), add=TRUE, col="red")
axis(2,at=alpha,labels=expression(alpha))
legend("bottomright", lty=1,col=1:2, legend=c("Equal-tailed test", "Unbiased test"))
```


### Optimal unbiased tests

If we are testing a point null against a two-sided alternative, we can take our choice between the equal-tailed and unbiased test, but the unbiasedness criterion is conceptually appealing for more general testing problems because the definition naturally extends to the case where $H_0$ is composite. For example, if we want to test an interval null against a two-sided alternative, it is not clear what it means to set $\PP_{H_0}(T(X) < c_1) = \alpha/2$, because that probability varies over the null parameter space $\Theta_0$. By contrast, the unbiased criterion is well-defined for any hypothesis testing problem.

If the power function is differentiable in $\theta$, and $\theta_0$ is in $\Theta^{\circ}$, the interior of the parameter space, then any unbiased test $\phi$ must have $\beta_\phi(\theta_0) = \alpha$ and $\dot{\beta}_{\phi}(\theta_0) = 0$. Otherwise, the power would be strictly less than $\alpha$ at either $\theta_0 +\varepsilon$ or $\theta_0- \varepsilon$, for sufficiently small $\varepsilon>0$.

In exponential family models, we can use these facts to obtain a simple characterization of the criterion that the power function has zero derivative at $\theta_0$, as. Let $X \sim p_\theta(x) = e^{\theta T(x) - A(\theta)}h(x)$, and differentiate the power function to obtain
$$
\begin{aligned}
\dot{\beta}_{\phi}(\theta_0)
&= \frac{d}{d\theta} \left. \int \phi(x)e^{\theta T(x) - A(\theta)}h(x)\,d\mu(x)\right|_{\theta=\theta_0} \\
&= \int \phi(x)(T(x)-\dot{A}(\theta_0))e^{\theta_0 T(x) - A(\theta_0)}h(x)\,d\mu(x)\\
&= \EE_{\theta_0}\left[\phi(X)(T(X) - \EE_{\theta_0}T(X))\right]\\[5pt]
&= \text{Cov}_{\theta_0}(T(X), \phi(X))\\[5pt]
&= \EE_{\theta_0}\left[(\phi(X)-\alpha)T(X)\right].
\end{aligned}
$$
Setting the last expression to 0 and massaging the equation a bit, we obtain
$$
\EE_{\theta_0}T(X) = \frac{\EE_{\theta_0}[\phi(X)T(X)]}{\alpha} = \EE_{\theta_0}[T(X) \mid \phi(X) \text{ rejects } H_0].
$$
Thus, the conditional expectation of $T(X)$ under the null, given that it falls in the rejection region, is the same as the marginal expectation. For instance, both the acceptance region and the rejection region for our unbiased test of $H_0:\;\theta=1$ in the exponential model share the same "balance point" at $\EE_{1}X = 1$. Because the right lobe is farther out from 1, it has only about 1/4 as much probability mass as the right lobe.

```r
xmax=7
curve(exp(-x), from =0, to=xmax, ylab="Density", main="Rejection region for unbiased test (Exponential)", xlab="X")
x.grid <- seq(0,c1.unbiased,by=.001)
y.grid <- exp(-x.grid)
polygon(x=c(x.grid,c1.unbiased,0), y=c(y.grid,0,0), col="red")
x.grid <- seq(c2.unbiased,xmax,by=.001)
y.grid <- exp(-x.grid)
polygon(x=c(x.grid,xmax,c2.unbiased), y=c(y.grid,0,0), col="red")
curve(exp(-x), from =0, to=xmax,add=TRUE)
lines(x=c(0,xmax),y=c(0,0))
abline(v=0:1,lty=3)
abline(h=0,lty=3)
```

Recall that when we restricted our attention to unbiased estimators, we were able to find a unique best unbiased estimator. Likewise, we can sometimes find an optimal two-sided test if we restrict our attention to unbiased tests. We say that $\phi^*$ is *UMP unbiased* (UMPU) if, for any other unbiased level $\alpha$ test $\phi$, we have $\beta_{\phi^*}(\theta) \geq \beta_{\phi}(\theta)$ for all $\theta \in \Theta_1$. UMPU tests exist, at least, for one-parameter exponential family models, as we show below.

**Theorem (UMP Unbiased tests):** Assume we want to test $H_0:\;|\theta -\theta_0| \leq \delta$ vs $H_1:\;|\theta - \theta_0| > \delta$ in the model $X \sim e^{\theta T(x)-A(\theta)}h(x)$, for $\delta \geq 0$ and $\theta_0-\delta, \theta+\delta \in \Theta^\circ$, the interior of the parameter space. Suppose that the test $\phi^*(X)$ rejects for extreme values of $T(X)$, with the cutoffs $c_1,c_2,\gamma_1,\gamma_2$ chosen so that

1. $\phi^*$ attains power $\alpha$ at the boundary of the null, i.e. $\beta_{\phi^*}(\theta_0 - \delta) = \beta_{\phi^*}(\theta_0 + \delta) = \alpha$, and

2. if $\delta> 0$, the power function is flat at $\theta_0$, i.e. $\dot{\beta}_{\phi^*}(\theta_0) = 0$.

Then $\phi^*$ is UMPU.

**Proof:** Assume without loss of generality that $\theta_0 = 0$, and first consider the case $\delta = 0$. Our proof will proceed much as it did for the Neyman-Pearson lemma. For $\theta \neq 0$, we want to solve the problem
$$
\begin{aligned}
\maxz_\phi &\int \phi(x)p_{\theta}(x)\,d\mu(x)\\
\text{ subject to } &\int \phi(x)p_0(x)\,d\mu(x) = \alpha, \quad\text{ and }\\
&\int \phi(x)(T(x)-\nu_0)p_0(x)\,d\mu(x) = 0,
\end{aligned}
$$
where $\nu_0 = \EE_0 T(X)$. Note that we have an equality constraint for the Type I error, because any unbiased test must have power exactly equal to $\alpha$ at $\theta_0$. The Lagrangian is
$$
\begin{aligned}
&\int \phi p_{\theta}\,d\mu - \lambda_1\int \phi p_0\,d\mu - \lambda_2\int \phi (T-\nu_0)p_0 \,d\mu \\
&\quad = \int \phi\left(p_\theta -\lambda_1 p_0 - \lambda_2(T-\nu_0)p_0\right)\,d\mu \\
&\quad = \int \phi\left(\frac{p_\theta}{p_0} - \lambda_1 - \lambda_2(T-\nu_0)\right)\,dP_0.
\end{aligned}
$$
Since $\frac{p_\theta}{p_0}(x) = e^{\theta T(x) - A(\theta)+A(0)}$, the test that maximizes this Lagrangian has
$$
\phi^*(x) = \begin{cases} 1 &\quad \text{ if } e^{\theta T(x)} > a_0 + a_1 T(x)\\
0 &\quad \text{ if } e^{\theta T(x)} < a_0 + a_1 T(x)\\
\text{anything} &\quad \text{ if } e^{\theta T(x)} = a_0 + a_1 T(x)
\end{cases}
$$
for $a_0 = (\lambda_1 - \lambda_2\nu_0)e^{A(0)-A(\theta)}$ and $a_1 = \lambda_2 e^{A(0)-A(\theta)}$.

For any $c_1,c_2$ we can find $a_1 > 0$ and $a_0\in \RR$ for which $e^{\theta t} = a_0 + a_1 t$ at $t = c_1,c_2$, in which case $e^{t\theta} > a_0 + a_1 t$ for $t < c_1$ and $t > c_2$ and $e^{t\theta} < a_0 + a_1 t$ otherwise; then we can solve for $\lambda_1,\lambda_2 \in \RR$ for which our $\phi^*$ maximizes the Lagrangian.

Now, for any other test $\phi$ that satisfies the unbiasedness constraints we can write
$$
\begin{aligned}
\beta_{\phi}(\theta)
&= \beta_{\phi}(\theta) - \lambda_1\left(\beta_{\phi}(0) - \alpha\right) -\lambda_2 \dot\beta_{\phi}(0)\\
&\leq \beta_{\phi^*}(\theta) - \lambda_1\left(\beta_{\phi^*}(0) - \alpha\right) -\lambda_2 \dot\beta_{\phi^*}(0)\\
&= \beta_{\phi^*}(\theta).
\end{aligned}
$$
Since $\theta$ was arbitrary, we have the result.

The proof for $\delta > 0$ is similar, with the constraints $\beta_{\phi}(0) = \alpha$ and $\dot{\beta}_{\phi}(0) = 0$ replaced by $\beta_{\phi}(-\delta) = \beta_{\phi}(\delta) =\alpha$.

---

[← Sample mean](03-sample-mean.md) · [Up: contents](index.md)
