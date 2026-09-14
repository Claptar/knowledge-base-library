---
title: risk function of estimator (X + synth.heads) / (n + synth.flips)
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# risk function of estimator (X + synth.heads) / (n + synth.flips)

**Source:** [`units/reader/estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

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

<figure class="figure">
<p><img src="estimation_files/figure-html/unnamed-chunk-1-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

If we look at the vertical axis, the MSE may appear to be very small, especially considering we only have 16 flips. But recall that an MSE of <span class="math inline">\$0.01\$</span> means that we are typically missing by about <span class="math inline">\$0.1\$</span>, while estimating a parameter that is between <span class="math inline">\$0\$</span> and <span class="math inline">\$1\$</span>.

### Comparing estimators {.anchored anchor-id="comparing-estimators"}

In comparing the risk functions of these estimators, we can notice a few things. As expected, both <span class="math inline">\$\\delta\_1\$</span> and <span class="math inline">\$\\delta\_2\$</span> outperform <span class="math inline">\$\\delta\_0\$</span> for values of <span class="math inline">\$\\theta\$</span> close to <span class="math inline">\$1/2\$</span>, but underperform for more extreme values of <span class="math inline">\$\\theta\$</span>. The estimator <span class="math inline">\$\\delta\_3\$</span>, however, performs worse than <span class="math inline">\$\\delta\_0\$</span> throughout the entire parameter space; this is because we have added bias without doing anything to reduce the variance. While it is difficult to choose between the other three estimators, we can at least rule out <span class="math inline">\$\\delta\_3\$</span> on the grounds that we have no reason to ever prefer it over <span class="math inline">\$\\delta\_0\$</span>.

Formally, we say an estimator <span class="math inline">\$\\delta\$</span> is *inadmissible* if there is some other estimator <span class="math inline">\$\\delta^\*\$</span> for which

1.  <span class="math inline">\$R(\\theta; \\delta^\*) \\leq R(\\theta; \\delta)\$</span> for all <span class="math inline">\$\\theta\\in\\Theta\$</span>, and

2.  <span class="math inline">\$R(\\theta; \\delta^\*) &lt; R(\\theta; \\delta)\$</span> for some <span class="math inline">\$\\theta\\in\\Theta\$</span>.

In this case we say <span class="math inline">\$\\delta^\*\$</span> *strictly* *dominates* <span class="math inline">\$\\delta\$</span>; more generally we can say <span class="math inline">\$\\delta^\*\$</span> \*dominates\* <span class="math inline">\$\\delta\$</span> if we only have (1). An estimator is *admissible* if it is not inadmissible. We can see from our plot that <span class="math inline">\$\\delta\_3\$</span> is inadmissible because <span class="math inline">\$\\delta\_0\$</span> strictly dominates it.

Comparing the other three estimators is more difficult, however, because no one of them dominates any other. In most estimation problems, including this one, we can never hope to come up with an estimator that uniformly attains the smallest risk among all estimators. That is because, for example, we can always choose the constant estimator <span class="math inline">\$\\delta(X) \\equiv 1/2\$</span> that simply ignores the data and always guesses that <span class="math inline">\$\\theta = 1/2\$</span>. This estimator may perform poorly for other values of <span class="math inline">\$\\theta\$</span>, but it is the only estimator that has exactly zero MSE for <span class="math inline">\$\\theta = 1/2\$</span>.

If we cannot hope to minimize the risk for every value of <span class="math inline">\$\\theta\$</span> simultaneously then we must come up with some other way to resolve the inherent ambiguity in comparing all of the many estimators that we must choose among.

In our unit on estimation, we will consider two main strategies for resolving this ambiguity.

### Strategy 1: Summarizing the risk function by a scalar {.anchored anchor-id="strategy-1-summarizing-the-risk-function-by-a-scalar"}

If we can find a way to summarize the risk function for each estimator by a single real number that we want to minimize, then we can find an estimator that is optimal in this summary sense. The two main ways to summarize the risk are to examine the average-case risk and the worst-case risk.

#### Average-case risk (Bayes estimation) {.anchored anchor-id="average-case-risk-bayes-estimation"}

The first option is to minimize some (weighted) average of the risk function over the parameter space <span class="math inline">\$\\Theta\$</span> :

<span class="math display">\\$$ \\minz\_{\\delta(\\cdot)} \\int\_\\theta R(\\theta; \\delta)\\td \\Lambda(\\theta) \\$$</span>

The average is taken with respect to some measure <span class="math inline">\$\\Lambda\$</span> of our choosing. If <span class="math inline">\$\\Lambda(\\Theta) &lt; \\infty\$</span> we can assume without loss of generality that <span class="math inline">\$\\Lambda\$</span> is a probability measure, since we could always normalize it without changing the minimization problem. Then, this average is simply the estimator’s expected risk, called the *Bayes risk*, or equivalently the expected loss averaging over the joint distribution of <span class="math inline">\$\\theta\$</span> and <span class="math inline">\$X\$</span>. An estimator that minimizes the Bayes risk is called a Bayes estimator.

In the binomial problem above, <span class="math inline">\$\\delta\_1(X) = \\frac{X + 1}{n + 2}\$</span> is a Bayes estimator that minimizes the average-case risk with respect to the Lebesgue measure on <span class="math inline">\$\\Theta = $$0,1$$\$</span>. <span class="math inline">\$\\delta\_2(X) = \\frac{X+2}{n+4}\$</span> is also a Bayes estimator with respect to a different prior, specifically the <span class="math inline">\$\\textrm{Beta}(2,2)\$</span> distribution. We will show this later.

Note that minimizing the average-case risk may be a natural thing to do regardless of whether we “really believe” that <span class="math inline">\$\\theta \\sim \\Lambda\$</span>. Hence Bayes estimators are well-motivated even from a purely frequentist perspective; using them does not have to imply one has any specific position on the philosophical interpretation of probability.

If <span class="math inline">\$\\Lambda(\\Theta) = \\infty\$</span> then we call <span class="math inline">\$\\Lambda\$</span> an *improper prior*, and we can no longer interpret the corresponding Bayes risk as an expectation. But, as we will see, working with improper priors can sometimes be convenient and often leads to good estimators in practice.

#### Worst-case risk (Minimax estimation) {.anchored anchor-id="worst-case-risk-minimax-estimation"}

If we are reluctant to average over the parameter space, we can instead seek to minimize the worst-case risk over the entire parameter space:

<span class="math display">\\$$ \\minz\_{\\delta(\\cdot)} \\sup\_{\\theta\\in\\Theta} R(\\theta; \\delta) \\$$</span>

This minimization problem has a game-theoretic interpretation if we imagine that, after we choose our estimator, Nature will adversarially choose the least favorable parameter value.

As we will see, minimax estimation is closely related to Bayes estimation and the minimax estimator is commonly a Bayes estimator.

The minimax perspective pushes us to choose estimators with flat risk functions, and indeed <span class="math inline">\$\\delta\_2(X) = \\frac{X + 2}{X + 4}\$</span> is the minimax estimator when <span class="math inline">\$n = 16\$</span>.

### Strategy 2: Restricting the choice of estimators {.anchored anchor-id="strategy-2-restricting-the-choice-of-estimators"}

The second main strategy for resolving ambiguity is to restrict ourselves to choose an estimator that satisfies some additional side constraint.

#### Unbiased estimation {.anchored anchor-id="unbiased-estimation"}

One property we might want to demand of an estimator is that it be *unbiased*, meaning that <span class="math inline">\$\\EE\_\\theta $$\\delta\_0(X)$$ = g(\\theta)\$</span>, for all <span class="math inline">\$\\theta\\in\\Theta\$</span>. This rules out, for example, estimators that ignore the data and always guess the same value.

As we will see, once we requiring unbiasedness there will often be a clear winner among all remaining estimators under consideration, called the *uniformly minimum variance unbiased* (UMVU) estimator, which uniformly minimizes the risk for any convex loss function.

Of the four estimators we considered above, only <span class="math inline">\$\\delta\_0(X) = X/n\$</span> is unbiased, and it is indeed the UMVU for this problem.

---

[← Estimation in statistical models](03-estimation-in-statistical-models.md) · [Up: contents](index.md)
