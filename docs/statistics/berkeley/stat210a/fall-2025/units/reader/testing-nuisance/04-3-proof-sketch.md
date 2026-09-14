---
title: 3 Proof Sketch
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-nuisance.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Proof Sketch

**Source:** [`units/reader/testing-nuisance.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

1.  Any unbiased test has <span class="math inline">\$\\mathbb{P}(\\phi=1) \\leq h(t,u)\$</span> (continuity)
2.  Power = 0 on boundary <span class="math inline">\$\\implies \\mathbb{E}\_{\\theta\_0}$$T\\phi$$ = \\theta\_0\$</span> (UK complete sufficient on boundary sub-model)
3.  <span class="math inline">\$\\phi\$</span> optimal among all tests with conditional level <span class="math inline">\$\\alpha\$</span> by reduction to univariate model

### <span class="header-section-number">3.1</span> Detailed Proof {.anchored number="3.1" anchor-id="detailed-proof"}

Assume <span class="math inline">\$\\phi\$</span> any unbiased test:

1.  <span class="math inline">\$\\mathbb{E}\_\\theta$$\\phi$$ = \\alpha + f(\\theta)\$</span>, <span class="math inline">\$f(\\theta\_0) = 0\$</span>, <span class="math inline">\$f'(\\theta\_0) = 0\$</span> Keener Thm 12.4
2.  <span class="math inline">\$\\mathbb{E}\_\\theta$$\\phi$$\$</span> infinitely diff on <span class="math inline">\$\\mathbb{R}^s\$</span>, can diff under <span class="math inline">\$\\int\$</span>
3.  <span class="math inline">\$\\phi\$</span> unbiased <span class="math inline">\$\\implies \\mathbb{E}\_\\theta$$T\\phi$$ = \\frac{\\partial}{\\partial \\theta} \\mathbb{E}\_\\theta$$\\phi$$ = \\theta\$</span>

Step 1: Boundary sub-model <span class="math inline">\$\\cP\_0 = \\{p\_{\\theta\_0, \\lambda}: \\lambda \\in \\mathbb{R}^r\\}\$</span>

<span class="math inline">\$p\_{\\theta\_0, \\lambda}(x) = e^{\\lambda \\cdot U(x) - A(\\theta\_0, \\lambda)}h(x)\$</span>

<span class="math inline">\$\\cP\_0\$</span> is full rank <span class="math inline">\$r\$</span>-param exp fam, <span class="math inline">\$U(X)\$</span> complete suff

Let <span class="math inline">\$f(\\lambda) = \\mathbb{E}\_{\\theta\_0, \\lambda}$$\\phi(X) \| U(X)$$ = \\alpha\$</span>

<span class="math inline">\$\\mathbb{E}\_{\\theta\_0, \\lambda}$$\\phi(X) T(X) \| U(X)$$ = \\theta\_0\$</span> a.s.

<span class="math inline">\$\\mathbb{E}\_{\\theta\_0, \\lambda}$$\\phi(X) \| U(X)$$ = \\alpha\$</span> a.s.

Two-sided: <span class="math inline">\$\\mathbb{E}\_{\\theta\_0, \\lambda}$$g(U(X))\\phi(X)$$ = \\mathbb{E}\_{\\theta\_0, \\lambda}$$T(X)\\phi(X)$$ = \\theta\_0\$</span>

<span class="math inline">\$\\mathbb{E}\_{\\theta\_0, \\lambda}$$g(U)\\mathbb{E}\_{\\theta\_0, \\lambda}\[\\phi\|U$$\] = \\theta\_0\$</span>

<span class="math inline">\$\\mathbb{E}\_{\\theta\_0, \\lambda}$$g(U) \\alpha$$ = \\theta\_0\$</span>

<span class="math inline">\$\\mathbb{E}\_{\\theta\_0, \\lambda}$$g(U)$$ = \\frac{\\theta\_0}{\\alpha}\$</span>

One-sided: <span class="math inline">\$\\mathbb{E}\_{\\theta\_0, \\lambda}$$\\phi$$ = \\alpha\$</span> <span class="math inline">\$\\forall \\lambda\$</span>

Steps 2-3: For any value <span class="math inline">\$u\$</span>, the conditional model is:

<span class="math display">\\$$p\_\\theta(t\|u) = e^{\\theta \\cdot t} g(t,u)\\$$</span>

1-param exp fam.

In one/two-sided case, we have shown <span class="math inline">\$\\psi(t,u)\$</span> is UMP/UMPU in <span class="math inline">\$\\{p\_\\theta(\\cdot\|u)\\}\$</span>

Let <span class="math inline">\$g(t,u) = \\mathbb{E}\_{\\theta\_0}$$\\phi(X) \| T(X)=t, U(X)=u$$ \\leq 1\$</span>

<span class="math inline">\$\\mathbb{E}\_{\\theta\_0}$$\\psi(T,U) \| U$$ = \\mathbb{E}\_{\\theta\_0}$$\\phi(X) \| U(X)=u$$\$</span>

<span class="math inline">\$\\psi\$</span> if <span class="math inline">\$\\theta &gt; \\theta\_0\$</span> <span class="math inline">\$\\phi(X)\$</span> is a conditional test of <span class="math inline">\$H\_0\$</span> vs <span class="math inline">\$H\_1\$</span> in <span class="math inline">\$\\{p\_\\theta(\\cdot\|u)\\}\$</span> with power <span class="math inline">\$\\leq \\alpha\$</span> at boundary

One-sided case: For <span class="math inline">\$\\theta &gt; \\theta\_0\$</span> <span class="math inline">\$\\psi(t,u)\$</span> is the UMP test of <span class="math inline">\$\\theta=\\theta\_0\$</span> vs <span class="math inline">\$\\theta&gt;\\theta\_0\$</span> in <span class="math inline">\$\\{p\_\\theta(\\cdot\|u)\\}\$</span>, which is a 1-param exp fam

Two-sided: <span class="math inline">\$\\psi(t,u)\$</span> is the UMP test of <span class="math inline">\$\\theta=\\theta\_0\$</span> vs <span class="math inline">\$\\theta \\neq \\theta\_0\$</span> among tests with power <span class="math inline">\$\\alpha\$</span> over <span class="math inline">\$\\theta=\\theta\_0\$</span> Keener Thm 12.22 (main thm for two-sided tests)

In either case, <span class="math inline">\$\\psi\$</span> has higher cond. power than <span class="math inline">\$\\phi\$</span> a.s.

For <span class="math inline">\$\\theta \\neq \\theta\_0\$</span>:

<span class="math display">\\$$\\mathbb{E}\_\\theta\[\\phi$$ = \\mathbb{E}\_\\theta$$\\mathbb{E}\[\\phi(X) \| T(X), U(X)$$\]\\\]</span> <span class="math display">\\$$\\leq \\mathbb{E}\_\\theta\[\\mathbb{E}\[\\psi(T(X), U(X)) \| T(X), U(X)$$\]\\\]</span> <span class="math display">\\$$= \\mathbb{E}\_\\theta\[\\psi$$\\\]</span>

### <span class="header-section-number">3.2</span> Example: Normal Mean with Unknown Variance {.anchored number="3.2" anchor-id="example-normal-mean-with-unknown-variance"}

<span class="math inline">\$X \\sim N(\\mu, \\sigma^2)\$</span>, <span class="math inline">\$\\sigma^2&gt;0\$</span> unknown <span class="math inline">\$H\_0: \\mu=0\$</span> vs <span class="math inline">\$H\_1: \\mu \\neq 0\$</span>

<span class="math inline">\$T = \\frac{\\bar{X}}{\\\|X\\\|}\$</span>, <span class="math inline">\$U = \\\|X\\\|^2\$</span>

Optimal test rejects when <span class="math inline">\$\\bar{X}\$</span> is extreme given <span class="math inline">\$\\\|X\\\|^2\$</span>

If <span class="math inline">\$\\mu=0\$</span>, <span class="math inline">\$\\frac{X}{\\\|X\\\|}\$</span> is rotationally symmetric <span class="math inline">\$\\frac{X}{\\\|X\\\|} \\sim \\text{Unif}(S^{n-1})\$</span>, <span class="math inline">\$\\frac{X}{\\\|X\\\|}\$</span> indep of <span class="math inline">\$\\\|X\\\|\$</span>

Optimal test rejects when <span class="math inline">\$\\frac{\\bar{X}}{\\\|X\\\|}\$</span> extreme (marginally)

Could stop here & simulate

#### <span class="header-section-number">3.2.1</span> Geometric Picture (n=2) {.anchored number="3.2.1" anchor-id="geometric-picture-n2"}

$$Insert geometric picture here$$

Above test rejects for: - conditionally extreme <span class="math inline">\$\\bar{X}\$</span> given <span class="math inline">\$\\\|X\\\|^2\$</span> OR - marginally extreme <span class="math inline">\$\\frac{\\bar{X}}{\\\|X\\\|}\$</span>

Fact: reject for marginally extreme <span class="math inline">\$T\$</span> where

<span class="math display">\\$$T^2 = \\frac{(\\sum X\_i)^2}{\\sum X\_i^2 - \\frac{1}{n}(\\sum X\_i)^2} = \\frac{n\\bar{X}^2}{\\\|X\\\|^2 - n\\bar{X}^2} = \\frac{n\\bar{X}^2}{S^2}\\$$</span>

and <span class="math inline">\$S^2 = \\frac{1}{n-1}\\sum (X\_i - \\bar{X})^2\$</span>

#### <span class="header-section-number">3.2.2</span> Geometric Picture {.anchored number="3.2.2" anchor-id="geometric-picture"}

$$Insert second geometric picture here$$

<span class="math inline">\$T^2 = \\frac{\\\|\\text{Proj}\_\\mathbf{1}X\\\|^2}{\\\|\\text{Proj}\_{\\mathbf{1}^\\perp}X\\\|^2} \\cdot \\frac{n-1}{n}\$</span>

Next major theme: ratios of projections

---

[← 2 Theorem (Informal)](03-2-theorem-informal.md) · [Up: contents](index.md) · [4 Permutation Tests →](05-4-permutation-tests.md)
