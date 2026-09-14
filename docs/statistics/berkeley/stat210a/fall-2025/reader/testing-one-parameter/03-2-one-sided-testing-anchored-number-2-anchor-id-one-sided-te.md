---
title: 2 One-sided testing {.anchored number="2" anchor-id="one-sided-testing"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-one-parameter.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 One-sided testing {.anchored number="2" anchor-id="one-sided-testing"}

**Source:** [`reader/testing-one-parameter.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Last time, we showed that if the family <span class="math inline">\$\\cP\$</span> has MLR in the statistic <span class="math inline">\$T(X)\$</span>, then the one-sided test that rejects for large <span class="math inline">\$T(X)\$</span> is UMP for testing <span class="math inline">\$H\_0:\\;\\theta\\leq \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta &gt; \\theta\_0\$</span>, because:

1.  it is simultaneously the likelihood ratio test for <span class="math inline">\$H\_0:\\;\\theta = \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta = \\theta\_1\$</span>, for every <span class="math inline">\$\\theta\_1 &gt; \\theta\_0\$</span>, and

2.  it controls the Type I error for all <span class="math inline">\$\\theta &lt; \\theta\_0\$</span>.

Recall that a test *rejects for large <span class="math inline">\$T(X)\$</span>* if it is of the form <span class="math display">\\$$\\phi(X) = \\begin{cases} 1 &\\quad \\text{ if } T(X) &gt; c \\\\ 0 &\\quad \\text{ if } T(X) &lt; c\\\\ \\gamma &\\quad \\text{ if } T(X) = c\\end{cases},\\$$</span> where the critical threshold <span class="math inline">\$c\$</span> is the *upper-<span class="math inline">\$\\alpha\$</span> quantile at the boundary* <span class="math display">\\$$ c\_\\alpha = \\min \\{c \\in \\RR:\\; \\PP\_{\\theta\_0}(T(X) &gt; c) \\leq \\alpha\\} \\$$</span> and the randomization parameter <span class="math inline">\$\\gamma\$</span> is used to “top off” the Type I error rate if <span class="math inline">\$T(X)\$</span> is discrete and <span class="math inline">\$\\PP\_{\\theta\_0}(T(X) &gt; c\_\\alpha) &lt; \\alpha\$</span>. In the rest of this section we will ignore randomization and assume that we just accept a conservative test in case <span class="math inline">\$\\PP\_{\\theta\_0}(T(X) &gt; c\_\\alpha) &lt; \\alpha\$</span> (as is generally done in practice).

A generic one-parameter model <span class="math inline">\$\\cP\$</span> does not have MLR in any statistic <span class="math inline">\$T(X)\$</span>; e.g. the LRT for testing <span class="math inline">\$\\theta=0\$</span> vs <span class="math inline">\$\\theta=1\$</span> does not coincide with the LRT for testing <span class="math inline">\$\\theta=0\$</span> vs <span class="math inline">\$\\theta= 2\$</span>. Then we cannot maximize power for both alternative values <span class="math inline">\$1\$</span> and <span class="math inline">\$2\$</span> simultaneously.

In such cases, we could still come up with a test that rejects for large values of some other test statistic <span class="math inline">\$T(X)\$</span>, that tends to be larger when <span class="math inline">\$\\theta\$</span> is larger. Formally, we say that <span class="math inline">\$T(X)\$</span> is *stochastically increasing in <span class="math inline">\$\\theta\$</span>* if <span class="math inline">\$\\PP\_\\theta(T(X) &gt; c)\$</span> is non-decreasing in <span class="math inline">\$\\theta\$</span>, for every <span class="math inline">\$c \\in \\RR\$</span>. The power function of <span class="math inline">\$\\phi(X) = 1\\{T(X) &gt; c\_\\alpha\\}\$</span>, then, is also non-decreasing in <span class="math inline">\$\\theta\$</span>, and <span class="math inline">\$\\phi(X)\$</span> is a valid test of <span class="math inline">\$H\_0:\\;\\theta\\leq \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta &gt; \\theta\_0\$</span>.

### <span class="header-section-number">2.1</span> Score test {.anchored number="2.1" anchor-id="score-test"}

Suppose we observe <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid P\_\\theta\$</span> for large <span class="math inline">\$n\$</span>, and we want to test <span class="math inline">\$H\_0:\\;\\theta\\leq \\theta\_0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta &gt; \\theta\_0\$</span>, but <span class="math inline">\$\\cP\$</span> does not have MLR so we cannot maximize the power over the entirety of <span class="math inline">\$H\_1\$</span>. One idea is to use the heuristic of maximizing the power for alternatives near <span class="math inline">\$\\theta\_0\$</span>; if <span class="math inline">\$n\$</span> is large, then we have a lot of information about <span class="math inline">\$\\theta\$</span> so our power will be close to <span class="math inline">\$1\$</span> no matter what we do. So we might prioritize maximizing the power at <span class="math inline">\$\\theta\_0 + \\varepsilon\$</span> for small <span class="math inline">\$\\varepsilon\$</span>.

The LRT for <span class="math inline">\$\\theta\_0\$</span> vs <span class="math inline">\$\\theta\_0 + \\varepsilon\$</span> rejects for large values of <span class="math display">\\$$ \\log\\frac{p\_{\\theta\_0+\\varepsilon}(X)}{p\_{\\theta\_0}(X)} =\\ell(\\theta\_0+\\varepsilon; X) - \\ell(\\theta\_0; X)\\approx \\varepsilon \\dot\\ell(\\theta\_0;X),\\$$</span> so a natural idea is to reject for large values of <span class="math inline">\$S\_{\\theta\_0}(X)=\\dot\\ell(\\theta\_0;X)\$</span>, provided we can show that the power of that test is monotone, for example because <span class="math inline">\$S\_{\\theta\_0}(X)\$</span> is stochastically increasing in <span class="math inline">\$\\theta\$</span>. Using the score statistic can give simple and appealing tests in certain situations.

**Example: Laplace**

Suppose <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid \\text{Laplace}(\\theta) = \\frac{1}{2}e^{-\|x-\\theta\|}\$</span> and we want to test <span class="math inline">\$H\_0:\\theta \\leq 0\$</span> vs <span class="math inline">\$H\_1:\\;\\theta &gt; 0\$</span>. We can calculate the likelihood ratio test for a given fixed alternative <span class="math inline">\$\\theta\_1 &gt; 0\$</span> as

<span class="math display">\\$$ \\log \\frac{p\_{\\theta\_1}(X)}{p\_0(X)} = \\sum\_i \|X\_i\| - \|X\_i-\\theta\_1\| = \\theta\_1\\sum\_i T\_{\\theta\_1}(X\_i), \\$$</span> so the optimal test rejects for large <span class="math inline">\$\\sum\_i T\_{\\theta\_1}(X\_i)\$</span>, where <span class="math display">\\$$ T\_{\\theta}(x) = \\begin{cases} -1 & \\text{ if } x \\leq 0 \\\\ \\frac{2x}{\\theta} -1 & \\text{ if } 0 \\leq x \\leq \\theta \\\\ +1 &\\text{ if } x \\geq \\theta \\end{cases}. \\$$</span> We can visualize the univariate version of the test statistic <span class="math inline">\$T\_{\\theta\_1}(x)\$</span> for several different values of <span class="math inline">\$\\theta\_1&gt;0\$</span>:

<figure class="figure">
<p><img src="testing-one-parameter_files/figure-html/unnamed-chunk-1-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

Note that this test implicitly caps the influence of any single observation <span class="math inline">\$X\_i\$</span>. Once <span class="math inline">\$X\_i &gt; \\theta\_1\$</span>, it gives the same evidence in favor of <span class="math inline">\$\\theta\_1\$</span> and against <span class="math inline">\$\\theta\_0\$</span> regardless of how much it exceeds <span class="math inline">\$\\theta\_1\$</span>. Compare this with the sample mean, where the influence of a single observation <span class="math inline">\$X\_i\$</span> is unbounded. It is easy to see that <span class="math inline">\$f(X\_i)\$</span> is stochastically increasing in <span class="math inline">\$\\theta\$</span> for *any* non-decreasing function <span class="math inline">\$f\$</span>, so any LRT gives a valid level-<span class="math inline">\$\\alpha\$</span> test on the entire null distribution.

If we take <span class="math inline">\$\\theta\_1\\downarrow 0\$</span>, the univariate test statistic approaches <span class="math display">\\$$ T\_{0^+}(x) = \\begin{cases} -1 & \\text{ if } x \\leq 0\\\\ +1 &\\text{ if } x &gt; 0\\end{cases}, \\$$</span> which gives the score test since <span class="math display">\\$$ S\_0(X) = \\dot{\\ell}(0;X) = \\left.\\frac{d}{d\\theta} \\sum\_i -\|X\_i-\\theta\|\\right\|\_{\\theta=0} = \\sum\_i T\_{0^+}(X\_i) \\$$</span> This test is called the **sign test**, and it is equivalent to rejecting when the number of positive <span class="math inline">\$X\_i\$</span> values is larger than a binomial threshold, since: <span class="math display">\\$$ B(X) = \\frac{S\_0(X)+n}{2} = \\#\\{X\_i &gt; 0\\} \\stackrel{H\_0}{\\sim} \\text{Binom}\\left(n,\\frac{1}{2}\\right). \\$$</span>

We can also plot the power curves for <span class="math inline">\$n = 100\$</span> and <span class="math inline">\$\\alpha = 0.1\$</span>, for these tests and for the test that rejects for large values of <span class="math inline">\$\\sum\_i X\_i\$</span>. As we see, the score test performs noticeably better than the test that rejects for large values of the sample mean <span class="math inline">\$\\overline{X}\$</span>, especially at “moderately hard” alternative values like <span class="math inline">\$\\theta\_1=0.2\$</span>. But the LRT for <span class="math inline">\$\\theta\_1 = 0.2\$</span> does even better there, as it must since it is optimal for that alternative.

<figure class="figure">
<p><img src="testing-one-parameter_files/figure-html/unnamed-chunk-2-1.png" class="img-fluid figure-img" width="672" /></p>
</figure>

### <span class="header-section-number">2.2</span> The sign test as a nonparametric test {.anchored number="2.2" anchor-id="the-sign-test-as-a-nonparametric-test"}

The test based on the binomial statistic <span class="math inline">\$S\_0(X)\$</span> (or <span class="math inline">\$B(X)\$</span>) is called the *sign test*, and is generally an appealing test for a *nonparametric* testing problem. Suppose <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid F\$</span>, where <span class="math inline">\$F\$</span> represents an unknown cdf for their distribution. Assume for simplicity that <span class="math inline">\$F\$</span> is continuous and strictly increasing on its support, so that the median <span class="math inline">\$\\theta(F) = F^{-1}(1/2)\$</span> is well-defined, and consider testing <span class="math inline">\$H\_0:\\; \\theta(F) \\leq 0\$</span> vs <span class="math inline">\$H\_1:\\; \\theta(F) &gt; 0\$</span>.

Then <span class="math inline">\$B(X) \\sim \\text{Binom}(n, 1-F(0))\$</span>, where the probability parameter <span class="math inline">\$1-F(0)\$</span> is no more than <span class="math inline">\$1/2\$</span> if <span class="math inline">\$H\_0\$</span> is true, but strictly greater than <span class="math inline">\$1/2\$</span> if <span class="math inline">\$H\_1\$</span> is true. Then the test that rejects when <span class="math inline">\$S(X)\$</span> is above the upper <span class="math inline">\$1-\\alpha\$</span> quantile of the <span class="math inline">\$\\text{Binom}(n,1/2)\$</span> distribution (randomizing at the boundary if desired) is level-<span class="math inline">\$\\alpha\$</span> on <span class="math inline">\$H\_0\$</span>.

---

[← Testing one parameter Part 02 —](02-testing-one-parameter-part-02.md) · [Up: contents](index.md) · [3 Two-sided alternatives {.anchored number="3" anchor-id="two-sided-alternatives"} →](04-3-two-sided-alternatives-anchored-number-3-anchor-id-two-sid.md)
