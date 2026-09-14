---
title: 6 Doubts about unbiasedness
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 6 Doubts about unbiasedness

**Source:** [`reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

The last example raises the question: why should we require zero bias? There can be good reasons for this: it’s nice to be able to say your estimator is correct on average, especially if the estimand is strongly contested by different parties. But we shouldn’t take this constraint too seriously because in some cases the UMVUE can be inadmissible, or even ridiculous in cases where other approaches work well.

**Example:** Suppose we observe a multivariate Gaussian vector with an unknown location parameter, <span class="math inline">\$X \\sim N\_d(\\mu, I\_d)\$</span> for <span class="math inline">\$\\mu \\in \\RR^d\$</span>, where <span class="math inline">\$I\_d\$</span> is the identity matrix, and we want to estimate <span class="math inline">\$g(\\mu) = \\\|\\mu\\\|^2\$</span>.

Since <span class="math inline">\$X\$</span>, the complete sufficient statistic for this family, is a natural estimator for <span class="math inline">\$\\mu\$</span>, we can start with <span class="math inline">\$\\\|X\\\|^2\$</span> and try to make it unbiased. If we write <span class="math inline">\$X = \\mu + Z\$</span> where <span class="math inline">\$Z \\sim N\_d(0,I\_d)\$</span>, then we have <span class="math display">\\$$ \\begin{aligned} \\EE\_\\mu \\\|X\\\|^2 &= \\sum\_j \\EE (Z\_j + \\mu\_j)^2\\\\ &= \\sum\_j \\mu\_j^2 + 2\\mu\_j\\EE Z\_j + \\EE Z\_j^2\\\\ &= \\\|\\mu\\\|^2 + d, \\end{aligned} \\$$</span> since each cross-term is zero and <span class="math inline">\$\\EE Z\_j^2 = \\Var(Z\_j) = 1\$</span>. As a result, we can get an unbiased estimator by subtracting off the bias, namely <span class="math inline">\$\\delta(X) = \\\|X\\\|^2-d\$</span>. But this estimator has the very odd property that it can be negative: if <span class="math inline">\$d=10\$</span> and <span class="math inline">\$\\\|X\\\|^2=5\$</span>, which can happen, we are giving the estimate <span class="math inline">\$-5\$</span> for the non-negative estimand <span class="math inline">\$\\\|\\mu\\\|^2\$</span>. This may not seem like a big deal when we are just doing frequentist calculations, but imagine the authors’ embarrassment if such an estimate actually found its way into a journal paper!

From a dry decision theory perspective, we can also recognize this estimator as inadmissible for any reasonable loss function: whenever the estimate is zero, we will always be getting closer to the estimand if we replace it with zero; that is, <span class="math inline">\$\\delta\_+(X) = (\\\|X\\\|^2-d)\_+\$</span> will strictly dominate <span class="math inline">\$\\delta(X)\$</span>, for any reasonable loss function.

There are even sillier examples of UMVU estimators, as we see next.

**Example:** Suppose we observe <span class="math inline">\$X \\sim \\text{Bin}(1000, \\theta)\$</span>, and want to estimate <span class="math inline">\$g(\\theta) = \\PP\_\\theta(X \\geq 500)\$</span>. What is the UMVU estimator?

Expand for answer

A simple unbiased estimator for this probability is just the indicator of whether it happened, <span class="math inline">\$1\\{X \\geq 500\\}\$</span>. Since <span class="math inline">\$X\$</span> is complete sufficient, this must also be the UMVU estimator.

But this estimator makes no sense! If we see <span class="math inline">\$X=499\$</span> heads out of <span class="math inline">\$1000\$</span>, we are estimating that if we repeated the experiment by flipping the coin <span class="math inline">\$1000\$</span> more times, there is no chance we’d get more heads than we got this time. There are perfectly good estimators for this problem; for example if we have any reasonable estimator <span class="math inline">\$\\hat\\theta\$</span> for <span class="math inline">\$\\theta\$</span> (such as <span class="math inline">\$X/n\$</span>) we can use the *plug-in estimator* <span class="math inline">\$\\PP\_{\\hat\\theta}(X \\geq 500)\$</span>, and this will increase gradually with <span class="math inline">\$X\$</span>. But any such reasonable estimator cannot be unbiased, because all other unbiased estimators have to be worse than the UMVU estimator.

While it may seem like we are beating up the unbiased estimation paradigm here, in fact there is no statistical paradigm that doesn’t look a bit ridiculous on some examples. As we’ll see later, in the multivariate Gaussian location model above, both the maximum likelihood estimator and the Bayes estimator using the “objective” Jeffreys prior are even worse than the UMVU estimator. Much of the art of applied statistics is to understand the limitations of the different paradigms and choose one that’s appropriate for the problem at hand.

---

[← 5 Finding the UMVUE](06-5-finding-the-umvue.md) · [Up: contents](index.md)
