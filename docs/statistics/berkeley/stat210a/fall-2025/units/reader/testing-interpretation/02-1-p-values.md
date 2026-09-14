---
title: 1 p-Values
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 p-Values

**Source:** [`units/reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">1.1</span> Informal Definition {.anchored number="1.1" anchor-id="informal-definition"}

Suppose <span class="math inline">\$\\phi(x)\$</span> rejects for <span class="math inline">\$T(x) &gt; c\$</span>. The p-value is:

<span class="math display">\\$$p(x) = \\mathbb{P}\_0(T(X) \\geq T(x)\_{\\text{observed}}) = \\mathbb{P}\_0(T(X) \\geq t)\\$$</span>

Example: <span class="math inline">\$X \\sim N(\\theta, 1)\$</span>, <span class="math inline">\$H\_0: \\theta = 0\$</span> vs <span class="math inline">\$H\_1: \\theta \\neq 0\$</span>

Two-sided test rejects for large <span class="math inline">\$\|T(X)\| = \|X\|\$</span>:

<span class="math display">\\$$p(x) = \\mathbb{P}\_0(\|X\| \\geq \|x\|) = 2(1 - \\Phi(\|x\|))\\$$</span>

The two-sided p-value is <span class="math inline">\$p(X)\$</span>, where:

<span class="math display">\\$$p(x) = \\mathbb{P}\_0(\|X\| \\geq \|x\|) = 2\\min\\{\\Phi(x), 1-\\Phi(x)\\}\\$$</span>

### <span class="header-section-number">1.2</span> Formal Definition {.anchored number="1.2" anchor-id="formal-definition"}

Assume we have a test <span class="math inline">\$\\phi\_\\alpha\$</span> for each significance level <span class="math inline">\$\\alpha\$</span>: <span class="math inline">\$\\mathbb{E}\_0$$\\phi\_\\alpha(X)$$ \\leq \\alpha\$</span>

In the non-randomized case: <span class="math inline">\$\\phi\_\\alpha(x) = 1\\{x \\in R\_\\alpha\\}\$</span>

Assume tests are monotone in <span class="math inline">\$\\alpha\$</span>: if <span class="math inline">\$\\alpha \\leq \\alpha'\$</span>, then <span class="math inline">\$\\phi\_\\alpha(x) \\leq \\phi\_{\\alpha'}(x)\$</span>

(In non-randomized case: <span class="math inline">\$R\_\\alpha \\subseteq R\_{\\alpha'}\$</span>)

Then:

<span class="math display">\\$$p(x) = \\inf\\{\\alpha \\in \[0,1$$: \\phi\_\\alpha(x) = 1\\} = \\inf\\{\\alpha: x \\in R\_\\alpha\\}\\\]</span>

It’s possible to define randomized p-value, but not worth it.

Note: <span class="math inline">\$p(x) \\leq \\alpha \\iff \\phi\_\\alpha(x) = 1\$</span>

For <span class="math inline">\$\\theta = \\theta\_0\$</span>: <span class="math inline">\$\\mathbb{P}\_0(p(X) \\leq \\alpha) = \\mathbb{E}\_0$$\\phi\_\\alpha(X)$$ \\leq \\alpha\$</span>

p-value stochastically dominates <span class="math inline">\$U(0,1)\$</span>

If <span class="math inline">\$\\phi\_\\alpha\$</span> rejects for large <span class="math inline">\$T(X)\$</span>, reduces to original definition.

Note: The p-value depends on: - The model - Null hypothesis - The data AND - The choice of test

Example: <span class="math inline">\$X \\sim N(\\theta, I\_d)\$</span>, <span class="math inline">\$H\_0: \\theta = 0\$</span> vs <span class="math inline">\$H\_1: \\theta \\neq 0\$</span>

We can use <span class="math inline">\$T(x) = \\\|x\\\|\_2^2\$</span> (<span class="math inline">\$\\chi^2\$</span> test) or <span class="math inline">\$T(x) = \\max\_i \|x\_i\|\$</span> (max test)

Very different p-values, power if <span class="math inline">\$d\$</span> large Choice reflects belief about whether <span class="math inline">\$\\theta\$</span> is sparse

### <span class="header-section-number">1.3</span> Accept/Reject Decisions {.anchored number="1.3" anchor-id="acceptreject-decisions"}

Accept/reject decisions are not interesting Usually, we care how big <span class="math inline">\$\\theta\$</span> is Tiny p-value doesn’t imply big <span class="math inline">\$\\theta\$</span> Big p-value doesn’t imply small <span class="math inline">\$\\theta\$</span> either

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Confidence Regions →](03-2-confidence-regions.md)
