---
title: Two-sided alternatives
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-one-parameter.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-one-parameter.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Two-sided alternatives

**Source:** [`reader/testing-one-parameter.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-one-parameter.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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


The following widget gives the range of options for two-tailed tests of the point hypothesis $H_0:\;\theta = 1$ for the Gamma distribution with shape parameter $k$ and scale parameter $\theta$:

```ojs
//| echo: false

// Import gamma distribution functions
jStat = require("https://cdn.jsdelivr.net/npm/jstat@latest/dist/jstat.min.js")

// Define gamma PDF
gammaPDF = (x, k, theta) => {
  if (x <= 0) return 0;
  return Math.pow(x, k-1) * Math.exp(-x/theta) / (Math.pow(theta, k) * jStat.gammafn(k));
}

// Define gamma CDF using jStat
gammaCDF = (x, k, theta) => {
  if (x <= 0) return 0;
  return jStat.gamma.cdf(x, k, theta);
}

// Define gamma quantile using jStat
gammaQuantile = (p, k, theta) => {
  return jStat.gamma.inv(p, k, theta);
}

// Fixed parameters
alpha = 0.1

// Interactive controls
viewof k = Inputs.range([0.5, 10], {value: 2, step: 0.1, label: "k (shape)"})

// For unbiased test, we need E[X | X in rejection region] = k
// This requires finding alpha1 such that the conditional expectation equals k
getUnbiasedAlpha1 = (k) => {
  // Function to compute E[X | X <= c1 or X >= c2] for given alpha1
  const conditionalExpectation = (a1) => {
    const a2 = alpha - a1;
    const c1 = gammaQuantile(a1, k, 1);
    const c2 = gammaQuantile(1 - a2, k, 1);

    // E[X * I(X <= c1)] for Gamma(k, 1)
    // This is the incomplete gamma function times k
    const leftExpectation = k * gammaCDF(c1, k + 1, 1);

    // E[X * I(X >= c2)] for Gamma(k, 1)
    const rightExpectation = k * (1 - gammaCDF(c2, k + 1, 1));

    // Total expectation in rejection region divided by total probability
    return (leftExpectation + rightExpectation) / alpha;
  };

  // Use bisection to find alpha1 where conditional expectation equals k
  let low = 0.001;
  let high = alpha - 0.001;
  let mid;
  const tolerance = 0.0001;
  const maxIter = 50;

  for (let i = 0; i < maxIter; i++) {
    mid = (low + high) / 2;
    const condExp = conditionalExpectation(mid);

    if (Math.abs(condExp - k) < tolerance) {
      break;
    }

    // For Gamma, increasing alpha1 typically decreases conditional expectation
    if (condExp > k) {
      low = mid;
    } else {
      high = mid;
    }
  }

  return mid;
}

// Calculate the unbiased value for current k
unbiasedAlpha1 = getUnbiasedAlpha1(k)

// Create the slider
viewof alpha1 = Inputs.range([0, alpha], {
  value: alpha / 2,
  step: 0.001,
  label: "α₁ (left tail mass)"
})

// Calculate alpha2 (right tail mass)
alpha2 = alpha - alpha1

// Calculate critical values under null (theta = 1)
c1 = gammaQuantile(alpha1, k, 1)
c2 = gammaQuantile(1 - alpha2, k, 1)

// Generate data for null distribution plot
nullData = {
  const xMin = 0;
  const xMax = gammaQuantile(0.999, k, 1);
  const numPoints = 1000;
  const dx = (xMax - xMin) / (numPoints - 1);

  return Array.from({length: numPoints}, (_, i) => {
    const x = xMin + i * dx;
    const density = gammaPDF(x, k, 1);
    const inRejection = (x <= c1 || x >= c2);
    return {
      x: x,
      density: density,
      densityRej: inRejection ? density : 0
    };
  });
}

// Power function calculation
powerFunction = (theta) => {
  // Power = P(reject H0 | theta) = P(X <= c1 | theta) + P(X >= c2 | theta)
  return gammaCDF(c1, k, theta) + (1 - gammaCDF(c2, k, theta));
}

// Generate data for power function plot
powerData = {
  const thetaMin = 0.1;
  const thetaMax = 3;
  const numPoints = 300;
  const dtheta = (thetaMax - thetaMin) / (numPoints - 1);

  return Array.from({length: numPoints}, (_, i) => {
    const theta = thetaMin + i * dtheta;
    return {
      theta: theta,
      power: powerFunction(theta)
    };
  });
}

// Left panel: Null distribution with rejection region
leftPlot = Plot.plot({
  width: 400,
  height: 400,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 40,
  style: { fontSize: "18px" },

  x: {
    domain: [0, Math.max(...nullData.map(d => d.x))],
    label: "x",
    labelAnchor: "center",
    labelOffset: 60,
    labelArrow: "none"
  },
  y: {
    domain: [0, Math.max(...nullData.map(d => d.density)) * 1.15],
    label: "p₁(x)",
    labelAnchor: "center",
    labelOffset: 70,
    labelArrow: "none"
  },

  marks: [
    // Fill rejection region
    Plot.areaY(nullData, {x: "x", y: "densityRej", fill: "red", opacity: 0.3}),
    // Null density curve
    Plot.line(nullData, {x: "x", y: "density", stroke: "steelblue", strokeWidth: 2}),
    // Critical values
    Plot.ruleX([c1], {stroke: "red", strokeWidth: 1.5, strokeDasharray: "5,5"}),
    Plot.ruleX([c2], {stroke: "red", strokeWidth: 1.5, strokeDasharray: "5,5"}),
    Plot.ruleY([0]),

    // Title above plot
    Plot.text(["Null Distribution (θ=1)"], {
      x: Math.max(...nullData.map(d => d.x))/2,
      y: Math.max(...nullData.map(d => d.density)) * 1.12,
      fontSize: 16,
      fontWeight: "bold",
      textAnchor: "middle"
    }),

    // Annotations for critical values (moved lower)
    Plot.text([`c₁=${c1.toFixed(2)}`], {
      x: c1,
      y: -Math.max(...nullData.map(d => d.density)) * 0.15,
      fontSize: 14,
      textAnchor: "middle"
    }),
    Plot.text([`c₂=${c2.toFixed(2)}`], {
      x: c2,
      y: -Math.max(...nullData.map(d => d.density)) * 0.15,
      fontSize: 14,
      textAnchor: "middle"
    })
  ]
})

// Right panel: Power function
rightPlot = Plot.plot({
  width: 400,
  height: 400,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 40,
  style: { fontSize: "18px" },

  x: {
    domain: [0, 3],
    label: "θ (scale parameter)",
    labelAnchor: "center",
    labelOffset: 60,
    labelArrow: "none"
  },
  y: {
    domain: [0, 1],
    label: "Power",
    labelAnchor: "center",
    labelOffset: 70,
    labelArrow: "none"
  },

  marks: [
    // Power function curve
    Plot.line(powerData, {x: "theta", y: "power", stroke: "steelblue", strokeWidth: 2}),
    // Significance level line
    Plot.ruleY([alpha], {stroke: "gray", strokeWidth: 1, strokeDasharray: "5,5"}),
    // Null hypothesis point
    Plot.dot([{theta: 1, power: powerFunction(1)}], {
      x: "theta",
      y: "power",
      r: 5,
      fill: "red"
    }),
    Plot.ruleY([0]),
    Plot.ruleX([1], {stroke: "gray", strokeWidth: 1, strokeDasharray: "3,3"}),

    // Title above plot
    Plot.text(["Power Function"], {
      x: 1.5,
      y: 0.98,
      fontSize: 16,
      fontWeight: "bold",
      textAnchor: "middle"
    }),

    // Annotation for significance level
    Plot.text([`α=${alpha}`], {
      x: 2.8,
      y: alpha + 0.03,
      fontSize: 14,
      textAnchor: "end"
    })
  ]
})

// Combine plots and buttons
html`<div>
  <div style="text-align: center; margin-bottom: 20px;">
    <h3 style="font-size: 20px; font-weight: bold;">Unbiased Two-Sided Test for Gamma Scale Parameter</h3>
    <p style="font-size: 16px;">Testing H₀: θ = 1 vs H₁: θ ≠ 1 with significance level α = ${alpha}</p>
    <p style="font-size: 14px;">Left tail: α₁ = ${alpha1.toFixed(3)}, Right tail: α₂ = ${alpha2.toFixed(3)}</p>
  </div>

  <div style="margin: 10px 0; text-align: center;">
    <span style="font-size: 14px; margin-right: 10px;">Quick presets:</span>
    <button onclick="
      const sliders = document.querySelectorAll('input[type=range]');
      if (sliders.length >= 2) {
        sliders[1].value = 0.05;
        sliders[1].dispatchEvent(new Event('input', {bubbles: true}));
      }
    "
            style="margin: 0 5px; padding: 5px 10px; background: ${Math.abs(alpha1 - 0.05) < 0.001 ? '#4682b4' : '#f0f0f0'};
                   color: ${Math.abs(alpha1 - 0.05) < 0.001 ? 'white' : 'black'};
                   border: 1px solid #ccc; border-radius: 4px; cursor: pointer;">
      Equal-tailed (α₁ = 0.050)
    </button>
    <button onclick="
      const sliders = document.querySelectorAll('input[type=range]');
      if (sliders.length >= 2) {
        sliders[1].value = ${unbiasedAlpha1};
        sliders[1].dispatchEvent(new Event('input', {bubbles: true}));
      }
    "
            style="margin: 0 5px; padding: 5px 10px; background: ${Math.abs(alpha1 - unbiasedAlpha1) < 0.001 ? '#4682b4' : '#f0f0f0'};
                   color: ${Math.abs(alpha1 - unbiasedAlpha1) < 0.001 ? 'white' : 'black'};
                   border: 1px solid #ccc; border-radius: 4px; cursor: pointer;">
      Unbiased (α₁ ≈ ${unbiasedAlpha1.toFixed(3)})
    </button>
  </div>

  <div style="display: flex; gap: 20px; justify-content: center;">
    ${leftPlot}
    ${rightPlot}
  </div>
</div>`
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
