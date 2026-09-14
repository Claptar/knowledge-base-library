---
title: Bayes estimation Part 02 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Bayes estimation Part 02 —

**Source:** [`reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We will motivate Bayes estimation first as a strategy for selecting an estimator in the setting of [Lecture 2](../estimation/index.md). Recall that, when we discussed possible strategies for choosing between different admissible estimators, we suggested using the *average-case risk* to reduce the risk function to a scalar summary. This average must be taken with respect to some measure <span class="math inline">\$\\Lambda\$</span> on the parameter space <span class="math inline">\$\\Theta\$</span>, which we will call the *prior*.

That is, for an estimator <span class="math inline">\$\\delta\$</span> we can define the average-case or *Bayes risk* with respect to <span class="math inline">\$\\Lambda\$</span>: <span class="math display">\\$$ r\_\\Lambda(\\delta) = \\int\_\\Theta R(\\theta; \\delta)\\,d\\Lambda(\\theta). \\$$</span> An estimator <span class="math inline">\$\\delta\_\\Lambda\$</span> that minimizes the Bayes risk is called a *Bayes estimator*. If <span class="math inline">\$\\Lambda(\\Theta) = \\infty\$</span>, we call the prior *improper*, and otherwise we assume <span class="math inline">\$\\Lambda\$</span> is normalized so that <span class="math inline">\$\\Lambda(\\Theta) = 1\$</span>. Then, <span class="math inline">\$\\Lambda\$</span> is a probability measure; in that case we call it *proper*, and the integral can be rewritten as an expectation

<span class="math display">\\$$ r\_\\Lambda(\\delta) = \\EE\_{\\theta \\sim \\Lambda}\[R(\\theta; \\delta)$$ = \\EE$$L(\\theta, \\delta(X))$$, \\\]</span> where the last expectation is taken with respect to the *joint distribution* where <span class="math inline">\$\\theta \\sim \\Lambda\$</span> and <span class="math inline">\$X \\mid \\theta \\sim P\_\\theta\$</span>. The key to finding a Bayes estimator is to calculate the conditional distribution of <span class="math inline">\$\\theta\$</span> given <span class="math inline">\$X\$</span>, which we call the *posterior*.

The prior will commonly be represented by a density <span class="math inline">\$\\lambda(\\theta)\$</span>, giving the joint density <span class="math inline">\$\\lambda(\\theta)p\_\\theta(x)\$</span>. Then the marginal distribution of <span class="math inline">\$X\$</span> is <span class="math inline">\$q(x) = \\int\_\\Theta p\_\\theta(x)\\lambda(\\theta)\\,d\\theta\$</span>, and the posterior density is given by Bayes’ rule: <span class="math display">\\$$ \\lambda(\\theta \\mid x) = \\frac{\\lambda(\\theta) p\_\\theta(x)}{q(x)}. \\$$</span>

The names “prior” and “posterior” evoke a natural epistemic interpretation that the prior represents our subjective beliefs about <span class="math inline">\$\\theta\$</span> before we observe the data, and the posterior our beliefs afterward. But nothing about the mathematical formulation of the problem requires that we endorse these interpretations: even if we are dogmatic frequentists, or if we are using a <span class="math inline">\$\\Lambda\$</span> that doesn’t really correspond to anyone’s subjective prior beliefs, the expectation still makes sense as a mathematically equivalent expression to the average-case risk.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Bayes estimator {.anchored number="2" anchor-id="bayes-estimator"} →](03-2-bayes-estimator-anchored-number-2-anchor-id-bayes-estimato.md)
