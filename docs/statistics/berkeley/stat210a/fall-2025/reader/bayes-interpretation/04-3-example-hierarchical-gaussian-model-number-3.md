---
title: '3 Example: Hierarchical Gaussian model {number="3"}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Example: Hierarchical Gaussian model {number="3"}

**Source:** [`reader/bayes-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

A closely related example that is worth examining in more detail is the hierarchical Gaussian model. Again, suppose we observe <span class="math inline">\$d\$</span> Gaussian random variables with unit variance, whose location parameters we view as coming from the same Gaussian prior distribution: <span class="math display">\\$$ \\begin{aligned} \\theta\_i &\\simiid N(0,\\tau^2), \\quad \\text{ for } i = 1,\\ldots,d\\\\ X\_i \\mid \\theta &\\simind N(\\theta\_i,1), \\end{aligned} \\$$</span> Again, if <span class="math inline">\$\\tau^2\$</span> is fixed then applying our result from the previous lecture gives Bayes estimator <span class="math inline">\$\\frac{\\tau^2}{1+\\tau^2}X\_i\$</span> for <span class="math inline">\$\\theta\_i\$</span>.

## <span class="header-section-number">3.1</span> Hierarchical Bayes approach {.anchored number="3.1" anchor-id="hierarchical-bayes-approach"}

The hierarchical Bayes approach to this problem again introduces a hyperprior on <span class="math inline">\$\\tau^2\$</span>: <span class="math display">\\$$ \\begin{aligned} \\tau^2 &\\sim \\lambda\_0\\\\ \\theta\_i &\\simiid N(0,\\tau^2), \\quad \\text{ for } i = 1,\\ldots,d\\\\ X\_i \\mid \\theta &\\simind N(\\theta\_i,1) \\end{aligned} \\$$</span> Then we have the Bayes estimator <span class="math display">\\$$ \\EE\[\\theta\_i \\mid X$$ = \\EE\\left$$ \\; \\frac{\\tau^2}{1+\\tau^2} X\_i \\mid X \\;\\right$$ = \\EE\\left$$ \\frac{\\tau^2}{1+\\tau^2} \\mid X\\right$$ \\cdot X\_i. \\\]</span>

It will be convenient to parameterize using <span class="math inline">\$\\zeta(\\tau^2) = \\frac{1}{1+\\tau^2}\$</span>, giving the *linear shrinkage estimator* <span class="math display">\\$$ \\delta\_{\\zeta}(X) = (1-\\zeta)X, \\$$</span> so that <span class="math inline">\$\\zeta \\in (0,1)\$</span> reflects what we might call the *shrinkage factor*. Then we see that the hierarchical Bayesian estimator <span class="math display">\\$$ \\EE\[\\theta\_i \\mid X$$ = \\EE$$1-\\zeta\\mid X$$\\cdot X\_i = (1-\\EE$$\\zeta\\mid X$$)X\_i \\\]</span>

is simply <span class="math inline">\$\\delta\_{\\hat\\zeta}(X)\$</span>, where <span class="math inline">\$\\hat\\zeta = \\EE$$\\zeta \\mid X$$\$</span> is the posterior mean of <span class="math inline">\$\\zeta\$</span> given all the data. This case shows the very close relationship between hierarchical Bayes and empirical Bayes: here, the hierarchical Bayes solution itself amounts to plugging a (Bayes) estimate for the hyperparameter <span class="math inline">\$\\zeta\$</span> into our formula for the optimal Bayes shrinkage rule if we knew <span class="math inline">\$\\zeta\$</span>.

To find <span class="math inline">\$\\EE$$\\zeta \\mid X$$\$</span>, it is again helpful to consider the likelihood model with <span class="math inline">\$\\theta\$</span> marginalized out. Then, we have <span class="math display">\\$$ \\begin{aligned} \\zeta &\\sim \\lambda\_0^{(\\zeta)}\\\\ X\_i \\mid \\zeta &\\simiid N(0, \\zeta^{-1}), \\end{aligned} \\$$</span> since <span class="math display">\\$$ \\Var(X\_i \\mid \\zeta) = \\Var(\\theta\_i \\mid \\zeta) + \\EE\[\\Var(X\_i \\mid \\zeta, \\theta\_i)$$ = \\tau^2+1 \\\]</span> The likelihood of <span class="math inline">\$X\$</span>, then, is <span class="math display">\\$$ X\\mid \\zeta \\sim N\_d(0,I\_d/\\zeta) = \\frac{\\zeta^{d/2}}{(2\\pi)^{d/2}} e^{-\\zeta\\\|x\\\|^2/2}, \\$$</span> an exponential family with sufficient statistic <span class="math inline">\$T(X)= \\\|X\\\|^2 \\sim \\frac{1}{\\zeta}\\chi\_d^2\$</span>.

A conjugate prior for <span class="math inline">\$\\zeta\$</span> in this model is the Gamma prior, but the calculations work out slightly better if we use a scaled <span class="math inline">\$\\chi^2\$</span> prior: <span class="math display">\\$$ \\zeta \\sim \\frac{1}{s}\\chi\_k^2 = \\text{Gamma}(k/2,2/s) = \\frac{1}{\\Gamma(k/2)(2/s)^{k/2}}\\zeta^{k/2-1}e^{-\\zeta s/2}, \\$$</span> which has mean <span class="math inline">\$k/s\$</span> and variance <span class="math inline">\$2k/s^2\$</span>. Then <span class="math display">\\$$ \\lambda(\\zeta \\mid x) \\propto\_\\zeta \\zeta^{(k+d)/2-1} e^{-\\zeta (\\\|x\\\|^2 + s)/2)} \\propto\_\\zeta \\frac{1}{s+\\\|x\\\|^2}\\chi\_{k+d}^2, \\$$</span> giving <span class="math inline">\$\\EE$$\\zeta \\mid X$$ = \\frac{k+d}{s+\\\|x\\\|^2}\$</span>.

Note that to be more correct, we should truncate our prior to the unit interval since <span class="math inline">\$\\zeta \\in (0,1)\$</span>. Then our calculations would have to remain numerical, but for large <span class="math inline">\$d\$</span> the prior would be concentrated in <span class="math inline">\$(0,1)\$</span> and they would turn out much the same.

## <span class="header-section-number">3.2</span> Empirical Bayes approach {.anchored number="3.2" anchor-id="empirical-bayes-approach"}

The empirical Bayes approach would estimate <span class="math inline">\$\\zeta\$</span> and plug the estimator into the Bayes rule formula <span class="math inline">\$(1-\\zeta)X\$</span>, again based on the sufficient statistic <span class="math inline">\$T(X) = \\\|X\\\|^2 \\sim \\frac{1}{\\zeta}\\chi\_d^2\$</span>. If we used as our estimator any Bayes posterior mean for a prior <span class="math inline">\$\\lambda\_0\$</span> on <span class="math inline">\$\\zeta\$</span>, we would simply recover the hierarchical Bayes estimator from above.

Another choice is the maximum likelihood estimator, which in exponential families (as we will see) simply solves for the value of <span class="math inline">\$\\zeta\$</span> at which the sufficient statistic’s expectation <span class="math inline">\$\\EE\_\\zeta T(X) = d/\\zeta\$</span> is equal to its realized value; hence <span class="math inline">\$\\hat\\zeta\_{\\text{MLE}}(X) = \\frac{d}{\\\|X\\\|^2}\$</span>.

A third choice is the UMVU estimator. Because <span class="math inline">\$T(X)= Y/\\zeta\$</span> for <span class="math inline">\$Y \\sim \\chi\_d^2\$</span>, we must have <span class="math display">\\$$ \\EE\\left\[\\frac{1}{\\\|X\\\|^2}\\right$$ = \\EE\\left$$\\frac{1}{Y}\\right$$ \\cdot \\zeta. \\\]</span> For <span class="math inline">\$d&gt;2\$</span> we can calculate this expectation, which does not depend on <span class="math inline">\$\\zeta\$</span>: <span class="math display">\\$$ \\begin{aligned} \\EE\\left\[\\frac{1}{Y}\\right$$ &= \\int\_0^\\infty \\frac{1}{y}\\cdot \\frac{1}{\\Gamma\\left(\\frac{d}{2}\\right)2^{d/2}} y^{d/2-1}e^{-y/2}\\,dy\\\\$$7pt$$ &= \\frac{\\Gamma\\left(\\frac{d-2}{2}\\right)\\cdot 2^{(d-2)/2}}{\\Gamma\\left(\\frac{d}{2}\\right)\\cdot 2^{d/2}} \\cdot \\int\_0^\\infty \\frac{1}{\\Gamma\\left(\\frac{d-2}{2}\\right)2^{(d-2)/2}} y^{(d-2)/2-1}e^{-y/2}\\,dy\\\\$$7pt$$ &= \\frac{\\Gamma\\left(\\frac{d-2}{2}\\right)\\cdot 2^{(d-2)/2}}{\\Gamma\\left(\\frac{d}{2}\\right)\\cdot 2^{d/2}}, \\end{aligned} \\\]</span> since the last integrand is the <span class="math inline">\$\\chi\_{d-2}^2\$</span> density. Since <span class="math inline">\$\\Gamma(x+1) = x\\Gamma(x)\$</span> for all <span class="math inline">\$x&gt;0\$</span>, the final expression can be simplified to <span class="math inline">\$\\frac{1}{d-2}\$</span>. As a result, <span class="math inline">\$\\frac{d-2}{\\\|X\\\|^2}\$</span> is UMVU, giving empirical Bayes estimator <span class="math display">\\$$ \\delta\_{\\text{JS}}(X) = \\left(1-\\frac{d-2}{\\\|X\\\|^2}\\right) X. \\$$</span> This estimator, called the James–Stein estimator, is very interesting in its own right, as we will see in two lectures.

## Footnotes {#footnotes .anchored .quarto-appendix-heading}

---

[← 2 Where Does the Prior Come From? {number="2"}](03-2-where-does-the-prior-come-from-number-2.md) · [Up: contents](index.md)
