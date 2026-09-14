---
title: risk function of estimator (X + synth.heads) / (n + synth.flips)
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# risk function of estimator (X + synth.heads) / (n + synth.flips)

**Source:** [`reader/estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

binom.mse <- function(theta, n, synth.heads, synth.flips) {
  binom.var <- theta * (1 - theta) * n / (n + synth.flips)^2
  binom.bias <- (n * theta + synth.heads) / (n + synth.flips) - theta
  return(binom.var + binom.bias^2)
}

palette <- c("black",brewer.pal(4, "Set1"))
curve(binom.mse(x, n, 0, 0), from=0, to=1, ylim=c(0,0.35/n), lwd=2, col=palette[1],
     main = "Mean squared error for binomial estimators (n=16)",
      ylab=expression(MSE(theta)),
      xlab=expression(theta))
curve(binom.mse(x, n, 1, 2), add=TRUE, col=palette[2], lwd=2)
curve(binom.mse(x, n, 2, 4), add=TRUE, col=palette[3], lwd=2)
curve(binom.mse(x, n, 1, 0), add=TRUE, col=palette[4], lwd=2)
legend("topright", col=palette, lwd=2,bty="n",
       legend=c(expression(delta[0]), expression(delta[1]), expression(delta[2]), expression(delta[3])))
```


Using the applet below, you can vary $n$, as well as the number of "pseudo-successes" and "pseudo-failures" in the

```ojs
//| echo: false

// Input controls for parameters
viewof n = Inputs.range([1, 100], {value: 20, step: 1, label: "n"})
viewof alpha = Inputs.range([0.1, 5], {value: 1, step: 0.1, label: "α"})
viewof beta = Inputs.range([0.1, 5], {value: 1, step: 0.1, label: "β"})

// Risk function for X/n (sample proportion)
riskSampleProp = (theta, n) => {
  return theta * (1 - theta) / n;
}

// Risk function for (X + alpha)/(n + alpha + beta) (Beta-binomial conjugate prior)
riskBayesian = (theta, n, alpha, beta) => {
  const bias = (alpha - theta * (alpha + beta)) / (n + alpha + beta);
  const variance = theta * (1 - theta) / n * (n / (n + alpha + beta))**2;
  return bias * bias + variance;
}

// Risk function for (X + 1)/n (add-one estimator)
riskAddOne = (theta, n) => {
  const bias = 1 / n;
  const variance = theta * (1 - theta) / n;
  return bias * bias + variance;
}

// Generate data points
data = {
  const thetaMin = 0.001;
  const thetaMax = 0.999;
  const numPoints = 1000;
  const dTheta = (thetaMax - thetaMin) / (numPoints - 1);

  return Array.from({length: numPoints}, (_, i) => {
    const theta = thetaMin + i * dTheta;
    return {
      theta: theta,
      sampleProp: riskSampleProp(theta, n),
      bayesian: riskBayesian(theta, n, alpha, beta),
      addOne: riskAddOne(theta, n)
    };
  });
}

// Calculate maximum MSE for y-axis domain
maxMSE = Math.max(...data.map(d => Math.max(d.sampleProp, d.bayesian, d.addOne)))

// Create the plot
Plot.plot({
  width: 800,
  height: 400,
  marginTop: 60,
  marginLeft: 120,
  marginBottom: 100,
  marginRight: 180,
  style: {
    fontSize: "18px"
  },
  x: {
    domain: [0, 1],
    label: "θ",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [0, maxMSE * 1.1],
    label: "MSE",
    labelAnchor: "center",
    labelOffset: 90
  },
  marks: [
    Plot.line(data, {x: "theta", y: "sampleProp", stroke: "steelblue", strokeWidth: 2}),
    Plot.line(data, {x: "theta", y: "bayesian", stroke: "red", strokeWidth: 2}),
    Plot.line(data, {x: "theta", y: "addOne", stroke: "green", strokeWidth: 2}),
    Plot.ruleY([0]),

    // Title
    Plot.text(["Risk Functions for Binomial Parameter Estimators"], {
      x: 0.5,
      y: maxMSE * 1.15,
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    }),

    // Legend background rectangle
    Plot.rect([{x1: 0.7, x2: 1, y1: maxMSE * 0.76, y2: maxMSE * 1.0}], {
      x1: "x1", x2: "x2", y1: "y1", y2: "y2",
      fill: "white", fillOpacity: 0.9, stroke: "lightgray"
    }),

    // Legend with colored lines
    Plot.lineX([{x: 0.72, y: maxMSE * 0.95}, {x: 0.78, y: maxMSE * 0.95}], {
      x: "x", y: "y",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.text(["X/n"], {
      x: 0.8,
      y: maxMSE * 0.95,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    }),

    Plot.lineX([{x: 0.72, y: maxMSE * 0.88}, {x: 0.78, y: maxMSE * 0.88}], {
      x: "x", y: "y",
      stroke: "red",
      strokeWidth: 2
    }),
    Plot.text([`(X+α)/(n+α+β)`], {
      x: 0.8,
      y: maxMSE * 0.88,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    }),

    Plot.lineX([{x: 0.72, y: maxMSE * 0.81}, {x: 0.78, y: maxMSE * 0.81}], {
      x: "x", y: "y",
      stroke: "green",
      strokeWidth: 2
    }),
    Plot.text(["(X+1)/n"], {
      x: 0.8,
      y: maxMSE * 0.81,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    })
  ]
})
```

If we look at the vertical axis, the MSE may appear to be very small, especially considering we only have 16 flips. But recall that an MSE of $0.01$ means that we are typically missing by about $0.1$, while estimating a parameter that is between $0$ and $1$.

### Comparing estimators

In comparing the risk functions of these estimators, we can notice a few things. As expected, both $\delta_1$ and $\delta_2$ outperform $\delta_0$ for values of $\theta$ close to $1/2$, but underperform for more extreme values of $\theta$. The estimator $\delta_3$, however, performs worse than $\delta_0$ throughout the entire parameter space; this is because we have added bias without doing anything to reduce the variance. While it is difficult to choose between the other three estimators, we can at least rule out $\delta_3$ on the grounds that we have no reason to ever prefer it over $\delta_0$.

Formally, we say an estimator $\delta$ is *inadmissible* if there is some other estimator $\delta^*$ for which

1.  $R(\theta; \delta^*) \leq R(\theta; \delta)$ for all $\theta\in\Theta$, and

2.  $R(\theta; \delta^*) < R(\theta; \delta)$ for some $\theta\in\Theta$.

In this case we say $\delta^*$ *strictly* *dominates* $\delta$; more generally we can say $\delta^*$ \*dominates\* $\delta$ if we only have (1). An estimator is *admissible* if it is not inadmissible. We can see from our plot that $\delta_3$ is inadmissible because $\delta_0$ strictly dominates it.

Comparing the other three estimators is more difficult, however, because no one of them dominates any other. In most estimation problems, including this one, we can never hope to come up with an estimator that uniformly attains the smallest risk among all estimators. That is because, for example, we can always choose the constant estimator $\delta(X) \equiv 1/2$ that simply ignores the data and always guesses that $\theta = 1/2$. This estimator may perform poorly for other values of $\theta$, but it is the only estimator that has exactly zero MSE for $\theta = 1/2$.

If we cannot hope to minimize the risk for every value of $\theta$ simultaneously then we must come up with some other way to resolve the inherent ambiguity in comparing all of the many estimators that we must choose among.

In our unit on estimation, we will consider two main strategies for resolving this ambiguity.

### Strategy 1: Summarizing the risk function by a scalar

If we can find a way to summarize the risk function for each estimator by a single real number that we want to minimize, then we can find an estimator that is optimal in this summary sense. The two main ways to summarize the risk are to examine the average-case risk and the worst-case risk.

#### Average-case risk (Bayes estimation)

The first option is to minimize some (weighted) average of the risk function over the parameter space $\Theta$ :

$$
\minz_{\delta(\cdot)} \int_\theta R(\theta; \delta)\td \Lambda(\theta)
$$

The average is taken with respect to some measure $\Lambda$ of our choosing. If $\Lambda(\Theta) < \infty$ we can assume without loss of generality that $\Lambda$ is a probability measure, since we could always normalize it without changing the minimization problem. Then, this average is simply the estimator's expected risk, called the *Bayes risk*, or equivalently the expected loss averaging over the joint distribution of $\theta$ and $X$. An estimator that minimizes the Bayes risk is called a Bayes estimator.

In the binomial problem above, $\delta_1(X) = \frac{X + 1}{n + 2}$ is a Bayes estimator that minimizes the average-case risk with respect to the Lebesgue measure on $\Theta = [0,1]$. $\delta_2(X) = \frac{X+2}{n+4}$ is also a Bayes estimator with respect to a different prior, specifically the $\textrm{Beta}(2,2)$ distribution. We will show this later.

Note that minimizing the average-case risk may be a natural thing to do regardless of whether we "really believe" that $\theta \sim \Lambda$. Hence Bayes estimators are well-motivated even from a purely frequentist perspective; using them does not have to imply one has any specific position on the philosophical interpretation of probability.

If $\Lambda(\Theta) = \infty$ then we call $\Lambda$ an *improper prior*, and we can no longer interpret the corresponding Bayes risk as an expectation. But, as we will see, working with improper priors can sometimes be convenient and often leads to good estimators in practice.

#### Worst-case risk (Minimax estimation)

If we are reluctant to average over the parameter space, we can instead seek to minimize the worst-case risk over the entire parameter space:

$$
\minz_{\delta(\cdot)} \sup_{\theta\in\Theta} R(\theta; \delta)
$$

This minimization problem has a game-theoretic interpretation if we imagine that, after we choose our estimator, Nature will adversarially choose the least favorable parameter value.

As we will see, minimax estimation is closely related to Bayes estimation and the minimax estimator is commonly a Bayes estimator.

The minimax perspective pushes us to choose estimators with flat risk functions, and indeed $\delta_2(X) = \frac{X + 2}{X + 4}$ is the minimax estimator when $n = 16$.

### Strategy 2: Restricting the choice of estimators

The second main strategy for resolving ambiguity is to restrict ourselves to choose an estimator that satisfies some additional side constraint.

#### Unbiased estimation

One property we might want to demand of an estimator is that it be *unbiased*, meaning that $\EE_\theta [\delta_0(X)] = g(\theta)$, for all $\theta\in\Theta$. This rules out, for example, estimators that ignore the data and always guess the same value.

As we will see, once we require unbiasedness there will often be a clear winner among all remaining estimators under consideration, called the *uniformly minimum variance unbiased* (UMVU) estimator, which uniformly minimizes the risk for any convex loss function.

Of the four estimators we considered above, only $\delta_0(X) = X/n$ is unbiased, and it is indeed the UMVU for this problem.

---

[← Estimation in statistical models](02-estimation-in-statistical-models.md) · [Up: contents](index.md)
