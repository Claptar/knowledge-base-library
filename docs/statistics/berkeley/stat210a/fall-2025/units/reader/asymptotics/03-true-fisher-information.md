---
title: '"True" Fisher information'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/asymptotics.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/asymptotics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# "True" Fisher information

**Source:** [`units/reader/asymptotics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/asymptotics.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

sigma <- sqrt(colMeans(sigma.hat^2))
hist(beta.hat[,2], freq=FALSE, breaks=50, main = expression(paste("Simulated distribution of ", hat(beta)[1])), xlab=expression(hat(beta)[1]))
curve(dnorm(x, mean = beta[2], sd = sigma[2]), add=TRUE)
```

<figure class="figure">
<p><img src="asymptotics_files/figure-html/unnamed-chunk-1-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

``` {.sourceCode .r .code-with-copy}
hist((beta.hat[,2] - beta[2])/sigma.hat[,2], freq=FALSE, breaks=30, main = expression(paste("Simulated distribution of ", Z[1] == (hat(beta)[1]-beta[1])/hat(sigma)[1])), xlab=expression(Z[1]))
curve(dnorm(x), add=TRUE)
```

<figure class="figure">
<p><img src="asymptotics_files/figure-html/unnamed-chunk-1-2.png" class="img-fluid figure-img" width="672" /></p>
</figure>

These results about the MLE apply far beyond logistic regression, to a wide variety of other models. To begin to prove them, however, we will need to be more precise about what we mean by <span class="math inline">\$\\hat\\beta\$</span> approximately following a normal distribution, or by the estimator <span class="math inline">\$\\hat\\Sigma\$</span> being approximately equal to the estimand <span class="math inline">\$\\Sigma(\\beta)\$</span>.

---

[← Asymptotics Part 02 —](02-asymptotics-part-02.md) · [Up: contents](index.md) · [2 Convergence {.anchored number="2" anchor-id="convergence"} →](04-2-convergence-anchored-number-2-anchor-id-convergence.md)
