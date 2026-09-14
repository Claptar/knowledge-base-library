---
title: 2 Bayes estimator {.anchored number="2" anchor-id="bayes-estimator"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Bayes estimator {.anchored number="2" anchor-id="bayes-estimator"}

**Source:** [`reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Whatever our interpretation of the marginal expectation that defines <span class="math inline">\$r\_\\Lambda\$</span>, the way to minimize it is the same: we simply choose <span class="math inline">\$\\delta(X)\$</span> to minimize the *conditional* expectation of the loss given the data <span class="math inline">\$X\$</span>.

**Theorem: Bayes estimation**

Assume <span class="math inline">\$r\_\\Lambda(\\delta\_0) &lt; \\infty\$</span> for some estimator <span class="math inline">\$\\delta\_0\$</span>. Then <span class="math inline">\$\\delta\_{\\Lambda}\$</span> is Bayes with <span class="math inline">\$r\_\\Lambda(\\delta\_{\\Lambda}) &lt; \\infty\$</span>, if and only if <span class="math display">\\$$ \\delta\_\\Lambda(x) \\in \\argmin \\EE\[ L(\\theta, d) \\mid X=x$$, \\quad \\text{ for a.e. } x, \\\]</span> meaning the marginal probability that <span class="math inline">\$\\delta(X)\$</span> does not minimize the conditional expectation is 0.

*Proof:* First, we prove the reverse direction. If <span class="math inline">\$\\delta\$</span> is any other estimator, then by assumption we have <span class="math display">\\$$ \\EE\[L(\\theta, \\delta\_\\Lambda(X)) \\mid X$$ \\;\\stackrel{\\text{a.s.}}{\\leq}\\; \\EE$$L(\\theta, \\delta(X)) \\mid X$$, \\\]</span> and marginalizing over <span class="math inline">\$X\$</span> gives the desired result. Taking <span class="math inline">\$\\delta = \\delta\_0\$</span> establishes that <span class="math inline">\$r\_\\Lambda(\\delta\_\\Lambda) \\leq r\_\\Lambda(\\delta\_0) &lt; \\infty\$</span>.

For the forward direction, assume <span class="math inline">\$r\_\\Lambda(\\delta\_\\Lambda) &lt; \\infty\$</span>; otherwise <span class="math inline">\$\\delta\_0\$</span> has better Bayes risk and there is nothing to prove. Define <span class="math inline">\$E\_x(d) = \\EE$$L(\\theta; d) \\mid X=x$$\$</span>. By assumption, there is some <span class="math inline">\$\\varepsilon &gt; 0\$</span> with <span class="math inline">\$\\PP(X \\in A\_\\varepsilon) &gt; 0\$</span>, where <span class="math display">\\$$ A\_\\varepsilon = \\left\\{x:\\; E\_x(\\delta\_\\Lambda(x)) - \\inf\_d E\_x(d) &gt; \\varepsilon \\right\\}. \\$$</span>

For any <span class="math inline">\$x \\in A\_\\varepsilon\$</span>, we can find <span class="math inline">\$\\delta^\*(x)\$</span> such that <span class="math display">\\$$ E\_x(\\delta^\*(x)) \\leq \\min\\{E\_x(\\delta\_\\Lambda(x)) - \\varepsilon, E\_x(\\delta\_0(x))\\}, \\$$</span> and for <span class="math inline">\$x \\in A\_\\varepsilon^C\$</span> take <span class="math inline">\$\\delta^\*(x)=\\delta\_\\Lambda(x)\$</span>. Then <span class="math display">\\$$ E\_x(\\delta\_\\Lambda(x)) - E\_x(\\delta^\*(x)) \\geq \\varepsilon 1\\{x \\in A\_\\varepsilon\\}. \\$$</span> Taking expectations gives <span class="math display">\\$$ r\_\\Lambda(\\delta\_\\Lambda) - r\_\\Lambda(\\delta^\*) \\geq \\varepsilon \\PP\\{X \\in A\_\\varepsilon\\} &gt; 0, \\$$</span> so <span class="math inline">\$\\delta\_\\Lambda\$</span> is not Bayes. <span class="math inline">\$\\blacksquare\$</span>

**Example: Squared error loss**

The form of the Bayes estimator is particularly nice in the case of the squared error loss <span class="math inline">\$L(\\theta, d) = (g(\\theta)-d)^2\$</span>. Then, we can decompose the conditional expected loss as <span class="math display">\\$$ \\begin{aligned} \\EE\[(g(\\theta)-d)^2 \\mid X$$ &\\;=\\; \\EE\\Big$$\\big(g(\\theta) - \\EE\[g(\\theta) \\mid X$$ + \\EE$$g(\\theta) \\mid X$$ - d\\big)^2 \\mid X\\Big\]\\\\ &\\;=\\; \\Var(g(\\theta) \\mid X) + (\\EE$$g(\\theta) \\mid X$$ - d)^2, \\end{aligned} \\\]</span> noting that the cross-term <span class="math inline">\$(g(\\theta) - \\EE$$g(\\theta) \\mid X$$)\\cdot(\\EE$$g(\\theta) \\mid X$$ - d)\$</span> has zero conditional expectation.

The optimal choice of <span class="math inline">\$d\$</span> is <span class="math inline">\$\\EE$$g(\\theta) \\mid X$$\$</span>, which zeroes the second term, giving Bayes risk <span class="math inline">\$\\EE$$\\Var(g(\\theta) \\mid X)$$\$</span>.

**Example: Weighted squared error loss**

An alternative loss is the *weighted* squared error loss, which gives more weight to some <span class="math inline">\$\\theta\$</span> values than others: <span class="math display">\\$$ L(\\theta, d) = w(\\theta)(g(\\theta) - d)^2. \\$$</span> For example, we could care about the *relative* squared error <span class="math inline">\$\\left(\\frac{g(\\theta)-d}{g(\\theta)}\\right)^2\$</span>, in which case <span class="math inline">\$w(\\theta) = g(\\theta)^{-2}\$</span>. Then, our Bayes estimator will minimize <span class="math display">\\$$ \\EE\[w(\\theta)(g(\\theta)-d)^2 \\mid X$$ = d^2 \\EE$$w(\\theta) \\mid X$$ - 2d \\EE$$w(\\theta)g(\\theta) \\mid X$$ + \\EE$$w(\\theta)g(\\theta)^2 \\mid X$$. \\\]</span> Minimizing this quadratic in <span class="math inline">\$d\$</span> gives the Bayes estimator <span class="math display">\\$$ \\delta\_\\Lambda(X) = \\frac{\\EE\[w(\\theta)g(\\theta) \\mid X$$}{\\EE$$ w(\\theta) \\mid X$$} \\\]</span>

---

[← Bayes estimation Part 02 —](02-bayes-estimation-part-02.md) · [Up: contents](index.md) · [3 Conjugate priors {.anchored number="3" anchor-id="conjugate-priors"} →](04-3-conjugate-priors-anchored-number-3-anchor-id-conjugate-pri.md)
