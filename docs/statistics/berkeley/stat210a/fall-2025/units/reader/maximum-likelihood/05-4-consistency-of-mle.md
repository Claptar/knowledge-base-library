---
title: 4 Consistency of MLE
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/maximum-likelihood.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/maximum-likelihood.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Consistency of MLE

**Source:** [`units/reader/maximum-likelihood.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/maximum-likelihood.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

<span class="math inline">\$X\_1, \\ldots, X\_n \\stackrel{\\text{iid}}{\\sim} f\_{\\theta\_0}\$</span>, <span class="math inline">\$\\theta\_n \\in \\arg\\max\_{\\theta \\in \\Theta} \\ell\_n(\\theta; X)\$</span>

Will be ok if <span class="math inline">\$\\theta\_n\$</span> comes close to maximizing <span class="math inline">\$\\ell\_n\$</span>

Question: When does <span class="math inline">\$\\ell\_n \\to \\ell\$</span>?

Assume model identifiable: <span class="math inline">\$P\_\\theta = P\_{\\theta\_0}\$</span> for <span class="math inline">\$\\theta \\neq \\theta\_0\$</span>

Recall KL Divergence:

<span class="math inline">\$D(g\\\|f) = \\mathbb{E}\_g$$\\log \\frac{g(X)}{f(X)}$$ = \\int g(x) \\log \\frac{g(x)}{f(x)} dx\$</span> (note switch)

<span class="math inline">\$\\log \\frac{g}{f} \\geq 1 - \\frac{f}{g}\$</span> (strict ineq unless const, i.e., unless <span class="math inline">\$f=g\$</span>)

Let <span class="math inline">\$W\_i(\\theta) = \\ell\_i(\\theta; X\_i) - \\ell\_i(\\theta\_0; X\_i)\$</span>, <span class="math inline">\$W(\\theta) = \\mathbb{E}\_{\\theta\_0}$$W\_i(\\theta)$$\$</span>

Note: <span class="math inline">\$\\theta\_0 = \\arg\\max\_{\\theta \\in \\Theta} W(\\theta)\$</span>

<span class="math inline">\$W(\\theta\_0) = 0\$</span>

<span class="math inline">\$W(\\theta) = -\\mathbb{E}\_{\\theta\_0}$$\\log \\frac{f\_{\\theta\_0}(X)}{f\_\\theta(X)}$$ = -D(f\_{\\theta\_0}\\\|f\_\\theta) \\leq 0\$</span>

<span class="math inline">\$= 0\$</span> iff <span class="math inline">\$\\theta = \\theta\_0\$</span>

But not enough: 1. MLE <span class="math inline">\$\\hat{\\theta}\_n\$</span> depends on entire function <span class="math inline">\$\\ell\_n\$</span> 2. Need uniform convergence in <span class="math inline">\$\\theta\$</span>

### <span class="header-section-number">4.1</span> Definition: Compact Convergence {.anchored number="4.1" anchor-id="definition-compact-convergence"}

For compact <span class="math inline">\$K\$</span>, let <span class="math inline">\$C(K) = \\{f: K \\to \\mathbb{R} \\text{ cts}\\}\$</span>

For <span class="math inline">\$f \\in C(K)\$</span>, let <span class="math inline">\$\\\|f\\\| = \\sup\_{x \\in K} \|f(x)\|\$</span>

<span class="math inline">\$f\_n \\to f\$</span> in this norm if <span class="math inline">\$\\\|f\_n - f\\\| \\to 0\$</span>

### <span class="header-section-number">4.2</span> Theorem: LLN for Random Functions {.anchored number="4.2" anchor-id="theorem-lln-for-random-functions"}

Assume <span class="math inline">\$K\$</span> compact, <span class="math inline">\$W\_i, W\_2, \\ldots \\in C(K)\$</span> iid <span class="math inline">\$\\mathbb{E}$$\\\|W\_i\\\|$$ &lt; \\infty\$</span>, <span class="math inline">\$\\mathbb{E}$$W\_i(\\theta)$$ = W(\\theta)\$</span>

Then <span class="math inline">\$\\bar{W}\_n \\in C(K)\$</span> and <span class="math inline">\$\\mathbb{P}(\\\|\\bar{W}\_n - W\\\| &gt; \\epsilon) \\to 0\$</span>

i.e., <span class="math inline">\$\\ell\_n \\to \\ell\$</span> in <span class="math inline">\$\\\|\\cdot\\\|\_\\infty\$</span> norm

### <span class="header-section-number">4.3</span> Theorem (Keener 9.4) {.anchored number="4.3" anchor-id="theorem-keener-9.4"}

Let <span class="math inline">\$G\_n, G\$</span> random functions in <span class="math inline">\$K\$</span> compact 1. <span class="math inline">\$G\_n \\to g\$</span> in <span class="math inline">\$\\\|\\cdot\\\|\_\\infty\$</span>, some fixed <span class="math inline">\$g \\in C(K)\$</span>. Then: a. If <span class="math inline">\$t^\* \\in K\$</span> fixed, then <span class="math inline">\$G\_n(t^\*) \\xrightarrow{p} g(t^\*)\$</span> b. If <span class="math inline">\$g\$</span> maximized at unique value <span class="math inline">\$t^\*\$</span> and <span class="math inline">\$G\_n(t\_n) = \\max\_t G\_n(t)\$</span>, then <span class="math inline">\$t\_n \\xrightarrow{p} t^\*\$</span> 2. If <span class="math inline">\$K \\subset \\mathbb{R}\$</span>, <span class="math inline">\$g'(t) = 0\$</span> has unique sol. <span class="math inline">\$t^\*\$</span> and <span class="math inline">\$t\_n\$</span> solve <span class="math inline">\$G\_n'(t) = 0\$</span>, then <span class="math inline">\$t\_n \\xrightarrow{p} t^\*\$</span>

(Sketch of proof in purple) If <span class="math inline">\$G\_n'(t\_n) = 0\$</span>, get <span class="math inline">\$G\_n'(t^\*) = g'(t^\*) + (g'(t\_n) - g'(t^\*)) + (G\_n'(t^\*) - g'(t^\*))\$</span> <span class="math inline">\$\\to 0 + 0 + 0\$</span> by assumptions + by cts mapping

Fix <span class="math inline">\$\\epsilon &gt; 0\$</span>, let <span class="math inline">\$B\_\\epsilon = \\{t: \\\|t - t^\*\\\| &lt; \\epsilon\\}\$</span> Let <span class="math inline">\$K\_\\epsilon = K \\setminus B\_\\epsilon(t^\*)\$</span>, <span class="math inline">\$K \\setminus B\_\\epsilon\$</span> compact <span class="math inline">\$\\delta = g(t^\*) - \\max\_{t \\in K\_\\epsilon} g(t) &gt; 0\$</span>

If <span class="math inline">\$t\_n \\notin K\_\\epsilon\$</span>, then <span class="math inline">\$G\_n(t\_n) &gt; G\_n(t^\*) - \\frac{\\delta}{2} &gt; g(t^\*) - \\delta = \\max\_{t \\in K\_\\epsilon} g(t)\$</span>

<span class="math inline">\$\\mathbb{P}(t\_n \\notin K\_\\epsilon) \\leq \\mathbb{P}(\\\|G\_n - g\\\|\_\\infty &gt; \\frac{\\delta}{2}) \\to 0\$</span>

Analogous to <span class="math inline">\$\\bar{X}\_n \\xrightarrow{p} \\mu\$</span>

### <span class="header-section-number">4.4</span> Theorem: Consistency of MLE for Compact <span class="math inline">\$\\Theta\$</span> {.anchored number="4.4" anchor-id="theorem-consistency-of-mle-for-compact-theta"}

<span class="math inline">\$X\_1, \\ldots, X\_n \\stackrel{\\text{iid}}{\\sim} f\_{\\theta\_0}\$</span>, <span class="math inline">\$\\cP\$</span> has densities <span class="math inline">\$p\_\\theta\$</span>, <span class="math inline">\$\\theta \\in \\Theta\$</span>

Assume: 1. <span class="math inline">\$p\_\\theta\$</span> cts in <span class="math inline">\$\\theta\$</span> 2. <span class="math inline">\$\\Theta\$</span> compact 3. <span class="math inline">\$\\mathbb{E}\_{\\theta\_0}$$\\sup\_\\theta \|f\_\\theta(X)\|/f\_{\\theta\_0}(X)$$ &lt; \\infty\$</span> 4. <span class="math inline">\$\\mathbb{E}\_{\\theta\_0}$$\\sup\_\\theta \|W\_i(\\theta)\|$$ &lt; \\infty\$</span> 5. Model identifiable

Then <span class="math inline">\$\\hat{\\theta}\_n \\xrightarrow{p} \\theta\_0\$</span> if \$

---

[← 3 Asymptotic Distribution of MLE](04-3-asymptotic-distribution-of-mle.md) · [Up: contents](index.md)
