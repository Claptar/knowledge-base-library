---
title: 2 The critical function
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hypothesis-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hypothesis-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 The critical function

**Source:** [`units/reader/hypothesis-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hypothesis-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We can describe a test by its *critical function* (a.k.a. *test function*):

<span class="math display">\\$$ \\phi(x) = \\begin{cases} 0 & \\text{accept } H\_0 \\\\ \\gamma \\in (0,1) & \\text{reject w.p. } \\gamma \\\\ 1 & \\text{reject } H\_0 \\end{cases} \\$$</span>

The option of randomizing our test by taking <span class="math inline">\$\\phi(x) \\in (0,1)\$</span> for some values <span class="math inline">\$x \\in \\cX\$</span> is helpful in theory, as we will see shortly, but it is hardly ever done in practice. A non-randomized test <span class="math inline">\$\\phi\$</span> partitions <span class="math inline">\$\\cX\$</span> into the *rejection region* <span class="math inline">\$R = \\{x \\in \\cX: \\phi(x) = 1\\}\$</span> and the *acceptance region* <span class="math inline">\$A = \\{x \\in \\cX:\\; \\phi(x) = 0\\}\$</span>.

Most tests are defined by choosing a real-valued *test statistic* <span class="math inline">\$T(X)\$</span> and rejecting when <span class="math inline">\$T(X)\$</span> is above some *critical threshold* <span class="math inline">\$c \\in \\RR\$</span>. We say <span class="math inline">\$\\phi\$</span> *rejects for large <span class="math inline">\$T(X)\$</span>* if <span class="math display">\\$$ \\phi(x) = \\begin{cases} 0 & T(x) &lt; c\\\\ \\gamma \\in (0,1) & T(x) = c \\text{ (if } \\phi \\text{ is randomized)} \\\\ 1 & T(x) &gt; c \\end{cases} \\$$</span> Much of the art in designing a hypothesis test is in choosing a test statistic <span class="math inline">\$T(X)\$</span> that is as effective as possible at discriminating between <span class="math inline">\$H\_0\$</span> and <span class="math inline">\$H\_1\$</span>

### <span class="header-section-number">2.1</span> Significance level and power {.anchored number="2.1" anchor-id="significance-level-and-power"}

In carrying out a test, there are two types of errors that we can make: a *Type I error* (sometimes called a *false positive*) is when <span class="math inline">\$H\_0\$</span> is true, but we reject it, and a *Type II error* (sometimes called a *false negative*) is when <span class="math inline">\$H\_0\$</span> is false but we fail to reject it. One way to remember which is which is that the Type I error rate is of primary importance in deciding when to reject, and the Type II error rate is of secondary importance. Our usual goal, informally, is to make the probability of a Type II error under <span class="math inline">\$H\_1\$</span> as small as we can, while controlling the Type I error rate below a prespecified value <span class="math inline">\$\\alpha \\in $$0,1$$\$</span>. Note that if <span class="math inline">\$H\_0\$</span> and <span class="math inline">\$H\_1\$</span> are composite, we cannot necessarily speak of “the” Type I or Type II error rate, as it may depend on exactly which of the null or alternative parameter values we sample under.

The behavior of the test is fully summarized by the *power function* <span class="math inline">\$\\beta(\\theta) = \\mathbb{E}\_\\theta$$\\phi(X)$$ = \\PP\_\\theta(\\text{Reject } H\_0)\$</span>. In terms of this power function, our goal can be formally stated as <span class="math display">\\$$ \\maxz\_\\phi \\beta\_\\phi(\\theta) \\text{ for } \\theta \\in \\Theta\_1 \\quad \\text{ subject to } \\beta\_\\phi(\\theta) \\leq \\alpha \\text{ for } \\theta \\in \\Theta\_0. \\$$</span> We say <span class="math inline">\$\\phi\$</span> is a *level-<span class="math inline">\$\\alpha\$</span> test* if <span class="math inline">\$\\sup\_{\\theta\\in\\Theta\_0} \\beta\_\\phi(\\theta) \\leq \\alpha\$</span>. If this supremum is strictly below <span class="math inline">\$\\alpha\$</span>, we say the test is *conservative*. A very common choice for <span class="math inline">\$\\alpha\$</span> is <span class="math inline">\$0.05\$</span>; this began with a somewhat offhand remark by Ronald Fisher in his work when he introduced hypothesis testing, that he sometimes liked to use <span class="math inline">\$0.05\$</span> in his scientific work. It has become “the most influential offhand remark in the history of science,” according to Brad Efron at Stanford.

If <span class="math inline">\$H\_0\$</span> is composite, this optimization problem has multiple constraints, and if <span class="math inline">\$H\_1\$</span> is composite it has multiple objectives. A major question for the remainder of this lecture is whether we can find a test <span class="math inline">\$\\phi^\*\$</span> that optimizes all objectives at once.

### <span class="header-section-number">2.2</span> Example: the <span class="math inline">\$Z\$</span>-test {.anchored number="2.2" anchor-id="example-the-z-test"}

A very common setting is that we observe some statistic <span class="math inline">\$Z(X) \\sim N(\\theta, 1)\$</span>, very often a summary statistic from a larger data set. If we are testing the one-sided hypothesis we might use the *right-tailed test* <span class="math inline">\$\\phi\_1(z) = 1\\{z &gt; z\_\\alpha\\}\$</span> that rejects for large values of <span class="math inline">\$Z\$</span>. Here <span class="math inline">\$z\_\\alpha = \\Phi^{-1}(1-\\alpha)\$</span> is the upper <span class="math inline">\$\\alpha\$</span> quantile of the <span class="math inline">\$N(0,1)\$</span> distribution, and <span class="math inline">\$\\Phi(z)\$</span> is the standard normal cdf.

If we want to test the two-sided hypothesis we might use the *two-tailed test* <span class="math inline">\$\\phi\_2(z) = 1\\{\|z\| &gt; z\_{\\alpha/2}\\}\$</span>. Now we are rejecting for large values of the test statistic <span class="math inline">\$\|Z\|\$</span>. The rejection regions for these tests at level <span class="math inline">\$\\alpha = 0.1\$</span> are plotted below, along with the alternative distribution when <span class="math inline">\$\\theta = 2.3\$</span>. The shaded blue region shows the power of the test under the alternative.

<figure class="figure">
<p><img src="hypothesis-testing_files/figure-html/unnamed-chunk-1-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

The two tests’ power functions are plotted below for <span class="math inline">\$\\alpha = 0.1\$</span>.

<figure class="figure">
<p><img src="hypothesis-testing_files/figure-html/unnamed-chunk-2-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

The power functions for both tests intersect the vertical axis <span class="math inline">\$\\theta=0\$</span> at <span class="math inline">\$\\alpha\$</span>, but the right-tailed test’s power function remains below <span class="math inline">\$\\alpha\$</span> for all <span class="math inline">\$\\theta &lt; 0\$</span> as well. Note that the right-tailed test is actually a valid test for the two-sided hypothesis, but we would be unlikely to want to use it since it has even less than <span class="math inline">\$\\alpha\$</span> power to reject for negative values of <span class="math inline">\$\\theta\$</span>. But this may give us a hint that it will not be possible to maximize power throughout the alternative, because the two-tailed test is in fact losing out to the right-tailed test when <span class="math inline">\$\\theta &gt; 0\$</span>.

For the one-sided hypothesis testing problem, however, we might hold out hope that the right-tailed test is the best for all values in the alternative (all <span class="math inline">\$\\theta &gt; 0\$</span>), and indeed it is.

---

[← 1 Hypothesis Testing](02-1-hypothesis-testing.md) · [Up: contents](index.md) · [3 Optimal testing →](04-3-optimal-testing.md)
