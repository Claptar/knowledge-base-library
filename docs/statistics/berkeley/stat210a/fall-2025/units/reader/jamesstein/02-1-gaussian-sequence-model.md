---
title: 1 Gaussian sequence model
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/jamesstein.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/jamesstein.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Gaussian sequence model

**Source:** [`units/reader/jamesstein.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/jamesstein.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Recall that we have discussed a variety of estimators for <span class="math inline">\$\\theta \\in \\RR^d\$</span> in the *Gaussian sequence model*

<span class="math display">\\$$X \\sim N\_d(\\theta, I\_d)\\$$</span>

Note that this model is somewhat more general than it appears. If <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid N\_d(\\theta, \\sigma^2 I\_d)\$</span> for known <span class="math inline">\$\\sigma^2&gt; 0\$</span>, we could make a sufficiency reduction to obtain

<span class="math display">\\$$Z = \\frac{1}{\\sigma\\sqrt{n}} \\sum\_i X\_i \\sim N\_d(\\theta, I\_d).\\$$</span> For simplicity we will discuss the \`\`vanilla’’ version here, but we can always translate our results to the more general setting via this transformation.

We’ll generally assume in what follows that the loss we care about is the squared error loss, summed over the coordinates: <span class="math display">\\$$L(\\theta, d) = \\\|\\delta(X) - \\theta\\\|^2 = \\sum\_j (\\delta\_j(X) - \\theta\_j)^2\\$$</span>

The most obvious estimator is <span class="math inline">\$\\delta\_0(X) = X\$</span> itself, which we could justify in a variety of ways: we’ve shown that it is the UMVU estimator for <span class="math inline">\$\\theta\$</span> and also the objective Bayes estimator, since the flat prior on <span class="math inline">\$\\theta\$</span> coincides with the Jeffreys prior (as it does for any location model). It also happens to be the maximum likelihood estimator (MLE), which we’ll discuss later in the course.

### <span class="header-section-number">1.1</span> Bayes estimators {.anchored number="1.1" anchor-id="bayes-estimators"}

If we introduce the Bayesian prior <span class="math inline">\$\\theta\_i \\simiid N(0,\\tau^2)\$</span> then we have seen that we arrive at the Bayes estimator <span class="math inline">\$\\frac{\\tau^2}{1+\\tau^2}X\$</span>.

We can think of this as a tuning parameter for a generic *linear shrinkage estimator* <span class="math display">\\$$\\delta\_\\zeta(X) = (1-\\zeta)X,\\$$</span> where <span class="math inline">\$\\zeta \\in $$0,1$$\$</span> is in effect a tuning parameter we will call the *shrinkage parameter*. Taking <span class="math inline">\$\\zeta = 0\$</span> corresponds to using <span class="math inline">\$X\$</span> as our estimator for <span class="math inline">\$\\theta\$</span>, and taking <span class="math inline">\$\\zeta = 1/(1+\\tau^2)\$</span> corresponds to the Bayes estimator where <span class="math inline">\$\\tau^2\$</span> is known.

If we aren’t sure which <span class="math inline">\$\\zeta\$</span> to use, for example because we have some *a priori* uncertainty about <span class="math inline">\$\\tau^2\$</span>, we can try to estimate it from the data using hierarchical Bayes, which we’ve seen would give the final estimator <span class="math display">\\$$\\delta(X) = (1 - \\EE\[\\zeta \\mid X$$) X = \\delta\_{\\hat\\zeta\_{\\text{Bayes}}(X)}(X),\\\]</span> so we are in effect estimating <span class="math inline">\$\\zeta\$</span> from the whole data set and then plugging it in as a data-adaptive tuning parameter.

The hierarchical Bayes estimator uses a Bayes estimator for <span class="math inline">\$\\zeta\$</span>, but if we take an empirical Bayes approach we could try other estimators, such as the MLE or UMVU. If <span class="math inline">\$d \\geq 3\$</span> then the UMVU estimator for <span class="math inline">\$\\zeta\$</span> is <span class="math display">\\$$\\hat{\\zeta}\_{\\text{UMVU}}(X) = \\frac{d-2}{\\\|X\\\|^2},\\$$</span> which we can verify using the identity <span class="math display">\\$$\\EE\[1/Y$$ = \\frac{1}{d-2}, \\quad \\text{ if } Y \\sim \\chi\_d^2 = \\text{Gamma}(d/2, 2), \\text{ for } d &gt; 2,\\\]</span> which is proved in the handwritten notes. Plugging in <span class="math inline">\$\\hat\\zeta\_\\text{UMVU}\$</span> results in an estimator called the *James-Stein* estimator, <span class="math display">\\$$ \\delta\_{\\text{JS}}(X)= \\left(1 - \\frac{d-2}{\\\|X\\\|^2}\\right)X = \\delta\_{\\hat\\zeta\_{\\text{UMVU}}}(X) \\$$</span>

### <span class="header-section-number">1.2</span> James-Stein Paradox {.anchored number="1.2" anchor-id="james-stein-paradox"}

While the James-Stein estimator can be motivated as an empirical Bayes estimator, it is surprisingly good even without making any Bayesian assumptions at all.

For <span class="math inline">\$d \\geq 3\$</span>, the estimator <span class="math inline">\$X\$</span> is actually *inadmissible* as an estimator of <span class="math inline">\$\\theta\$</span> under squared error loss:

<span class="math display">\\$$\\text{MSE}(\\theta, \\delta\_{JS}) &lt; \\text{MSE}(\\theta, X) \\quad \\text{ for all } \\theta \\in \\mathbb{R}^d.\\$$</span>

It is not surprising for a Bayes estimator to beat the UMVU estimator *an average* with respect to some prior, but this result holds for *every fixed value* of the parameter <span class="math inline">\$\\theta\$</span>.

In fact, since there is nothing special about shrinking towards <span class="math inline">\$0\$</span>. We could use a version of the estimator that shrinks toward any other <span class="math inline">\$\\theta\_0 \\in \\RR^d\$</span>, i.e. <span class="math display">\\$$ \\tilde delta(X) = \\theta\_0 + \\left(1 - \\frac{d-2}{\\\|X - \\theta\_0\\\|^2}\\right) (X - \\theta\_0)\\$$</span>. This also dominates <span class="math inline">\$\\delta\_0\$</span> because it is just the James-Stein estimator we’d get if we made the substitution <span class="math display">\\$$Y = X - \\theta\_0 \\sim N\_d(\\mu, I\_d), \\quad \\text{ for } \\mu = \\theta - \\theta\_0.\\$$</span> The translation-invariance of the Gaussian location model means that the James-Stein estimator for <span class="math inline">\$\\mu\$</span> using <span class="math inline">\$Y\$</span> also dominates the estimator <span class="math inline">\$\\hat\\mu\_0(Y) = Y\$</span>, which corresponds to the estimator <span class="math inline">\$\\delta\_0(X) = \\hat\\mu\_0 + \\theta\_0 = X\$</span> for <span class="math inline">\$\\theta\$</span>.

This result was received as a shock in the 1950s when it first came out. It was regarded for a long time as a curiosity, but it was eventually understood to carry the deep implication that shrinkage makes sense, especially in higher-dimensional problems, even when we don’t have a Bayes justification for it.

### <span class="header-section-number">1.3</span> Linear shrinkage estimators {.anchored number="1.3" anchor-id="linear-shrinkage-estimators"}

Even without introducing a Bayesian prior for <span class="math inline">\$\\theta\$</span>, we can motivate our linear shrinkage estimator purely from the perspective of trading a bit of bias for a reduction in variance.

We can start by calculating the MSE (considered as a purely frequentist risk function) for a single coordinate, using the bias-variance tradeoff: <span class="math display">\\$$ \\begin{aligned} \\EE\_\\theta\[(\\theta - \\delta\_i(X))^2$$ &= (\\theta\_i - \\EE\_\\theta (1-\\zeta)X\_i)^2 + \\text{Var}\_\\theta (1-\\zeta)X\_i\\\\ &= (\\zeta\\theta\_i)^2 + (1-\\zeta)^2 \\end{aligned} \\\]</span> Summing over the <span class="math inline">\$d\$</span> coordinates gives <span class="math display">\\$$\\text{MSE}(\\theta; \\delta) = \\zeta^2\\\|\\theta\\\|^2 + d(1-\\zeta)^2,\\$$</span> where the first term represents the squared bias and the second is the variance.

Note that the risk is a quadratic in <span class="math inline">\$\\zeta\$</span> with positive second derivative, so we can minimize it by setting <span class="math display">\\$$0 = \\frac{d}{d\\zeta}\\text{MSE}(\\theta) = 2\\zeta\\\|\\theta\\\|^2 - 2(1-\\zeta)d,\\$$</span> leading to <span class="math display">\\$$\\zeta^\*(\\theta) = \\frac{d}{d+\\\|\\theta\\\|^2} = \\frac{1}{1+\\\|\\theta\\\|^2/d},\\$$</span> which looks remarkably similar to <span class="math inline">\$\\frac{1}{1+\\tau^2}\$</span>, which is the Bayes-optimal <span class="math inline">\$\\zeta\$</span> under the Gaussian prior from the last section.

One thing to notice is that <span class="math inline">\$\\zeta^\*(\\theta) &gt; 0\$</span>, so a small amount of shrinkage helps. But the correct amount of shrinkage depends on <span class="math inline">\$\\\|\\theta\\\|^2\$</span>: if <span class="math inline">\$\\\|\\theta\\\|^2 \\to \\infty\$</span>, the correct amount of shrinkage goes to <span class="math inline">\$0\$</span>, so any fixed <span class="math inline">\$\\zeta\$</span> would overshoot for some <span class="math inline">\$\\theta\$</span> parameters.

It turns out the James-Stein estimator manages to estimate the correct amount of shrinkage from the data, in such a way that we avoid overshooting most of the time, and thereby improve on the MSE for *any* <span class="math inline">\$\\theta\$</span>.

To understand why, we need a general way to calculate the MSE for an estimator with an adaptive <span class="math inline">\$\\hat\\zeta(X)\$</span>. Stein’s unbiased risk estimator will give us that.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Stein’s Unbiased Risk Estimator →](03-2-stein-s-unbiased-risk-estimator.md)
