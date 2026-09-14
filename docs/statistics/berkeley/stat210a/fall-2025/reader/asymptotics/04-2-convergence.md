---
title: 2 Convergence
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/asymptotics.html
source_file: sources/berkeley-stat210a/fall-2025/reader/asymptotics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Convergence

**Source:** [`reader/asymptotics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/asymptotics.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

There are two main approximations we will be interested in making: approximating a random variable as a limiting constant, and approximating it as having some limiting distribution, usually a multivariate Gaussian distribution. To make these approximations precise, we need to introduce two types of convergence: convergence in probability, and convergence in distribution.

Let <span class="math inline">\$X\_1, X\_2, \\ldots\$</span> be a sequence of random variables on a sample space <span class="math inline">\$\\cX\$</span>, which we assume is endowed with a distance <span class="math inline">\$d(x,y)\$</span>. Because we are primarily interested in <span class="math inline">\$\\cX \\subseteq \\RR^d\$</span>, we will write <span class="math inline">\$d(x,y)\$</span> as <span class="math inline">\$\\\|x-y\\\|\$</span>, and it will not matter which norm we choose, but

We say the sequence *converges in probability* to a limiting constant <span class="math inline">\$c \\in \\cX\$</span>, written as <span class="math inline">\$X \\toProb c\$</span> if <span class="math display">\\$$ \\mathbb{P}(\\\|X\_n - c\\\| &gt; \\epsilon) \\to 0 \\quad \\forall \\epsilon &gt; 0. \\$$</span> In writing the norm we are implicitly assuming \$

### <span class="header-section-number">2.1</span> Convergence in Probability {.anchored number="2.1" anchor-id="convergence-in-probability"}

We say the sequence converges in probability to <span class="math inline">\$c \\in \\mathbb{R}^d\$</span> (<span class="math inline">\$X\_n \\xrightarrow{p} c\$</span>) if:

<span class="math display">\\$$\\mathbb{P}(\\\|X\_n - c\\\| &gt; \\epsilon) \\to 0 \\quad \\forall \\epsilon &gt; 0\\$$</span>

(Could really be any distance on any <span class="math inline">\$\\cX\$</span>)

Can converge to a r.v. <span class="math inline">\$X\$</span> too, but we don’t need this.

### <span class="header-section-number">2.2</span> Convergence in Distribution {.anchored number="2.2" anchor-id="convergence-in-distribution"}

We say the sequence converges in distribution to random variable <span class="math inline">\$X\$</span> (<span class="math inline">\$X\_n \\xrightarrow{d} X\$</span>) if:

<span class="math display">\\$$\\mathbb{E}\[f(X\_n)$$ \\to \\mathbb{E}$$f(X)$$ \\text{ for all bounded continuous } f: \\cX \\to \\mathbb{R}\\\]</span>

Theorem: <span class="math inline">\$X\_n, X \\in \\mathbb{R}\$</span>. Fix <span class="math inline">\$\\mathbb{P}(X = x) = 0\$</span>. Let <span class="math inline">\$F\_n(x) = \\mathbb{P}(X\_n \\leq x)\$</span>, <span class="math inline">\$F(x) = \\mathbb{P}(X \\leq x)\$</span>. Then <span class="math inline">\$X\_n \\xrightarrow{d} X\$</span> iff <span class="math inline">\$F\_n(x) \\to F(x)\$</span> <span class="math inline">\$\\forall x: F\$</span> is continuous at <span class="math inline">\$x\$</span>.

Also known as weak convergence.

### <span class="header-section-number">2.3</span> Example {.anchored number="2.3" anchor-id="example"}

If <span class="math inline">\$X\_n \\xrightarrow{d} X \\sim g\$</span>, then <span class="math inline">\$X\_n \\xrightarrow{d} X\$</span>:

<span class="math display">\\$$F\_n(x) = \\begin{cases} 1 & \\text{if } x &gt; 0 \\\\ 1 - \\frac{1}{n} & \\text{if } x = 0 \\\\ 0 & \\text{if } x &lt; 0 \\end{cases}\\$$</span>

<span class="math display">\\$$F(x) = \\begin{cases} 1 & \\text{if } x &gt; 0 \\\\ 0 & \\text{if } x \\leq 0 \\end{cases}\\$$</span>

### <span class="header-section-number">2.4</span> Proof: <span class="math inline">\$X\_n \\xrightarrow{p} c \\implies X\_n \\xrightarrow{d} c\$</span> {.anchored number="2.4" anchor-id="proof-x_n-xrightarrowp-c-implies-x_n-xrightarrowd-c"}

Let <span class="math inline">\$f\_\\epsilon(x) = \\max\\{1 - \\frac{\\\|x-c\\\|}{\\epsilon}, 0\\}\$</span>. Then <span class="math inline">\$\\forall \\epsilon &gt; 0\$</span>:

<span class="math display">\\$$\\mathbb{P}(\\\|X\_n - c\\\| &gt; \\epsilon) \\leq \\mathbb{E}\[1 - f\_\\epsilon(X\_n)$$ \\to 0\\\]</span>

<span class="math inline">\$f\$</span> bounded continuous. Note <span class="math inline">\$\\mathbb{E}$$f(c)$$ = f(c)\$</span>.

<span class="math inline">\$\\forall \\epsilon &gt; 0\$</span>, <span class="math inline">\$\\exists \\delta &gt; 0\$</span> s.t. <span class="math inline">\$\\\|x - c\\\| &lt; \\delta \\implies \|f(x) - f(c)\| &lt; \\epsilon\$</span>

<span class="math display">\\$$\|\\mathbb{E}\[f(X\_n)$$ - f(c)\| \\leq \|\\mathbb{E}$$f(X\_n) - f(c)$$1\_{\\\|X\_n - c\\\| &lt; \\delta}\| + \|\\mathbb{E}$$(f(X\_n) - f(c))1\_{\\\|X\_n - c\\\| \\geq \\delta}$$\|\\\]</span> <span class="math display">\\$$\\leq \\epsilon + 2\\sup \|f\| \\cdot \\mathbb{P}(\\\|X\_n - c\\\| \\geq \\delta)\\$$</span>

For sufficiently large <span class="math inline">\$n\$</span>. <span class="math inline">\$\\square\$</span>

In a sequence of statistical models <span class="math inline">\$\\cP\_n = \\{P\_{n,\\theta}: \\theta \\in \\Theta\\}\$</span> with <span class="math inline">\$X\_n \\sim P\_{n,\\theta}\$</span>, we say <span class="math inline">\$\\hat{\\theta}\_n\$</span> is consistent for <span class="math inline">\$g(\\theta)\$</span> if <span class="math inline">\$\\hat{\\theta}\_n \\xrightarrow{p} g(\\theta)\$</span>, meaning:

<span class="math display">\\$$\\mathbb{P}\_\\theta(\|\\hat{\\theta}\_n - g(\\theta)\| &gt; \\epsilon) \\to 0\\$$</span>

Usually, we omit the index <span class="math inline">\$n\$</span>; sequence is implicit.

### <span class="header-section-number">2.5</span> Law of Large Numbers (LLN) {.anchored number="2.5" anchor-id="law-of-large-numbers-lln"}

Let <span class="math inline">\$\\bar{X}\_n = \\frac{1}{n} \\sum\_{i=1}^n X\_i\$</span>

If <span class="math inline">\$\\mathbb{E}\|X\_i\| &lt; \\infty\$</span>, <span class="math inline">\$\\mathbb{E}X\_i = \\mu\$</span>, then <span class="math inline">\$\\bar{X}\_n \\xrightarrow{p} \\mu\$</span>

### <span class="header-section-number">2.6</span> Central Limit Theorem (CLT) {.anchored number="2.6" anchor-id="central-limit-theorem-clt"}

If <span class="math inline">\$\\text{Var}(X\_i) = \\sigma^2 &lt; \\infty\$</span>, then <span class="math inline">\$\\sqrt{n}(\\bar{X}\_n - \\mu) \\xrightarrow{d} N(0, \\sigma^2)\$</span>

There are stronger versions of both the LLN and CLT, but this will generally be enough for us.

---

[← "True" Fisher information](03-true-fisher-information.md) · [Up: contents](index.md) · [3 Continuous Mapping Theorem →](05-3-continuous-mapping-theorem.md)
