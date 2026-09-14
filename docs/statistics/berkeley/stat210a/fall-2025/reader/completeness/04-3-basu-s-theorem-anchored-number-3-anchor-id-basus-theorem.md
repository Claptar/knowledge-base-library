---
title: 3 Basu’s Theorem {.anchored number="3" anchor-id="basus-theorem"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html
source_file: sources/berkeley-stat210a/fall-2025/reader/completeness.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Basu’s Theorem {.anchored number="3" anchor-id="basus-theorem"}

**Source:** [`reader/completeness.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Basu’s Theorem gives us a simple way to prove that statistics are independent of one another using the definitions introduced above.

**Theorem (Basu):** If <span class="math inline">\$T(X)\$</span> is complete sufficient and <span class="math inline">\$V(X)\$</span> ancillary for the model <span class="math inline">\$\\cP\$</span>, then <span class="math inline">\$V(X) \\indep T(X)\$</span> for all <span class="math inline">\$\\theta \\in \\Theta\$</span>.

Again, for this proof our strategy will be to show that two quantities are almost surely equal to each other, by showing that they have the same expectation for all <span class="math inline">\$\\theta\$</span>.

*Proof:* Define the following two quantities representing the marginal and conditional probabilities that <span class="math inline">\$V\$</span> falls into a generic set <span class="math inline">\$A\$</span>. <span class="math display">\\$$ \\begin{aligned} p\_A &= \\PP(V \\in A)\\\\\[5pt$$ q\_A(T(X)) &= \\PP(V \\in A \\mid T(X)) \\end{aligned} \\\]</span> Note that <span class="math inline">\$p\_A\$</span> does not depend on <span class="math inline">\$\\theta\$</span> by ancillarity of <span class="math inline">\$V\$</span>, while <span class="math inline">\$q\_A\$</span> does not depend on <span class="math inline">\$\\theta\$</span> by sufficiency of <span class="math inline">\$T\$</span>.

The expectation of their difference is <span class="math display">\\$$ \\EE\_\\theta\\left\[q\_A(T) - p\_A\\right$$ = p\_A - p\_A = 0, \\quad \\text{ for all } \\theta. \\\]</span> By completeness of <span class="math inline">\$T\$</span>, this implies that <span class="math inline">\$q\_A(T) \\eqas p\_A\$</span>: the conditional probability equals the marginal probability. Hence, for any <span class="math inline">\$B\$</span>, we have <span class="math display">\\$$ \\begin{aligned} \\PP\_\\theta(V \\in A, T \\in B) &= \\int q\_A(t) 1\\{t \\in B\\}\\,dP\_\\theta^T(t)\\\\ &= \\int p\_A 1\\{t \\in B\\}\\,dP\_\\theta^T(t)\\\\ &= \\PP\_\\theta(V \\in A) \\PP\_\\theta(T \\in B). \\end{aligned} \\$$</span>

### <span class="header-section-number">3.1</span> Using Basu’s Theorem {.anchored number="3.1" anchor-id="using-basus-theorem"}

Basu’s Theorem can be helpful in proving independence. To use it, remember that the hypotheses of the theorem (sufficiency, completeness, and ancillarity) are all defined with respect to a *family* <span class="math inline">\$\\cP\$</span>. The conclusion, however, is defined with respect to individual *distributions*. As a result, when we apply the theorem we can often benefit from being a little clever about how to define <span class="math inline">\$\\cP\$</span>. The following example should make this clear:

**Example (Independence of sample mean and sample variance for Gaussian):** Assume <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid \\cN(\\mu, \\sigma^2)\$</span> for <span class="math inline">\$\\mu \\in \\RR\$</span> and <span class="math inline">\$\\sigma^2 &gt; 0\$</span>. Define the *sample mean* and *sample variance* as <span class="math display">\\$$ \\begin{aligned} \\overline{X} &= \\frac{1}{n}\\sum\_{i=1}^n X\_i\\\\\[5pt$$ S^2 &= \\frac{1}{n-1}\\sum\_{i=1}^n (X\_i - \\overline{X})^2 \\end{aligned} \\\]</span> We would like to show <span class="math inline">\$\\overline{X} \\indep S^2\$</span>.

Initially the approach of applying Basu’s Theorem appears hopeless because, in the model with <span class="math inline">\$\\mu\$</span> and <span class="math inline">\$\\sigma^2\$</span> unknown, neither of these two statistics is ancillary *or* sufficient. However, we can nevertheless apply Basu’s Theorem if we are just a bit more clever:

Expand for answer

Consider the model <span class="math inline">\$\\cP\$</span> with *known* <span class="math inline">\$\\sigma^2 &gt; 0\$</span> and unknown <span class="math inline">\$\\mu\\in \\RR\$</span>. This <span class="math inline">\$\\cP\$</span> is a one-parameter full-rank exponential family with complete sufficient statistic <span class="math inline">\$\\overline{X}\$</span>. Moreover, <span class="math inline">\$S^2\$</span> is ancillary, since we can write <span class="math display">\\$$ S^2 = \\sum\_{i=1}^n (Z\_i - \\overline{Z})^2, \\quad \\text{ for } Z\_i = X\_i - \\mu. \\$$</span> Because the distribution of <span class="math inline">\$Z\_1,\\ldots,Z\_n \\simiid N(0,\\sigma^2)\$</span> is known, it follows that the distribution of <span class="math inline">\$S^2\$</span> is known as well (specifically, <span class="math inline">\$S^2/\\sigma^2\$</span> is a <span class="math inline">\$\\chi^2\$</span> random variable with <span class="math inline">\$n-1\$</span> degrees of freedom). Since <span class="math inline">\$\\mu\$</span> is the only unknown parameter, <span class="math inline">\$S^2\$</span> is therefore ancillary in <span class="math inline">\$\\cP\$</span>. Applying Basu’s theorem, we have <span class="math inline">\$\\overline{X} \\indep S^2\$</span> for any <span class="math inline">\$\\mu \\in \\RR\$</span>. But <span class="math inline">\$\\sigma^2\$</span> was arbitrary, so we have the result for all <span class="math inline">\$\\mu\$</span> and <span class="math inline">\$\\sigma^2\$</span>.

---

[← 2 Ancillarity {.anchored number="2" anchor-id="ancillarity"}](03-2-ancillarity-anchored-number-2-anchor-id-ancillarity.md) · [Up: contents](index.md)
