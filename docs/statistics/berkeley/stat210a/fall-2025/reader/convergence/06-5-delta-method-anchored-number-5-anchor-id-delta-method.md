---
title: 5 Delta Method {.anchored number="5" anchor-id="delta-method"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/convergence.html
source_file: sources/berkeley-stat210a/fall-2025/reader/convergence.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5 Delta Method {.anchored number="5" anchor-id="delta-method"}

**Source:** [`reader/convergence.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/convergence.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Theorem (Delta Method): If <span class="math inline">\$\\sqrt{n}(X\_n - \\mu) \\xrightarrow{d} N(0, \\sigma^2)\$</span> <span class="math inline">\$f(x)\$</span> differentiable at <span class="math inline">\$x = \\mu\$</span>

Then <span class="math inline">\$\\sqrt{n}(f(X\_n) - f(\\mu)) \\xrightarrow{d} N(0, $$f'(\\mu)$$^2 \\sigma^2)\$</span>

Instant: <span class="math inline">\$X \\sim N(\\mu, \\sigma^2/n) \\implies f(X) \\sim N(f(\\mu), $$f'(\\mu)$$^2 \\sigma^2/n + o(1/n))\$</span>

Proof: <span class="math inline">\$f(X\_n) = f(\\mu) + f'(\\mu)(X\_n - \\mu) + o(X\_n - \\mu)\$</span> <span class="math inline">\$\\sqrt{n}(f(X\_n) - f(\\mu)) = f'(\\mu)\\sqrt{n}(X\_n - \\mu) + \\sqrt{n}o(X\_n - \\mu)\$</span> <span class="math inline">\$N(0, \\sigma^2) + 0 \\xrightarrow{d} N(0, $$f'(\\mu)$$^2 \\sigma^2)\$</span>

Multivariate: <span class="math inline">\$\\sqrt{n}(X\_n - \\mu) \\xrightarrow{d} N(0, \\Sigma)\$</span>, <span class="math inline">\$f: \\mathbb{R}^d \\to \\mathbb{R}^k\$</span> Derivative <span class="math inline">\$Df(\\mu)\$</span> exists at <span class="math inline">\$\\mu\$</span>

Then <span class="math inline">\$\\sqrt{n}(f(X\_n) - f(\\mu)) \\xrightarrow{d} N(0, Df(\\mu) \\Sigma Df(\\mu)^T)\$</span>

<span class="math inline">\$N(f(\\mu), Df(\\mu) \\Sigma Df(\\mu)^T/n + o(1/n))\$</span> if <span class="math inline">\$k=1\$</span>

### <span class="header-section-number">5.1</span> Example: Delta Method Application {.anchored number="5.1" anchor-id="example-delta-method-application"}

<span class="math inline">\$X\_1, \\ldots, X\_n \\sim \\text{Unif}$$0, \\theta$$\$</span> iid <span class="math inline">\$Y\_1, \\ldots, Y\_m \\sim \\text{Unif}$$0, \\theta$$\$</span> iid <span class="math inline">\$X, Y\$</span> independent

For large <span class="math inline">\$n, m\$</span>, what is the distribution of <span class="math inline">\$T = \\frac{\\bar{X}}{\\bar{Y}}\$</span>?

1.  <span class="math inline">\$\\sqrt{n}(\\bar{X} - \\frac{\\theta}{2}) \\xrightarrow{d} N(0, \\frac{\\theta^2}{12})\$</span> as <span class="math inline">\$n \\to \\infty\$</span>
2.  <span class="math inline">\$\\sqrt{m}(\\bar{Y} - \\frac{\\theta}{2}) \\xrightarrow{d} N(0, \\frac{\\theta^2}{12})\$</span> as <span class="math inline">\$m \\to \\infty\$</span>

<span class="math inline">\$T\_n = \\frac{\\bar{X}}{\\bar{Y}} = \\frac{\\theta/2}{\\theta/2} = 1 + O\_p(n^{-1/2} + m^{-1/2})\$</span>

Let <span class="math inline">\$f(x,y) = x/y\$</span>

<span class="math inline">\$f\_x'(\\frac{\\theta}{2}, \\frac{\\theta}{2}) = \\frac{1}{\\theta/2} = \\frac{2}{\\theta}\$</span> <span class="math inline">\$f\_y'(\\frac{\\theta}{2}, \\frac{\\theta}{2}) = -\\frac{\\theta/2}{(\\theta/2)^2} = -\\frac{2}{\\theta}\$</span>

<span class="math inline">\$f'(\\frac{\\theta}{2}, \\frac{\\theta}{2}) = (\\frac{2}{\\theta}, -\\frac{2}{\\theta})\$</span>

<span class="math inline">\$\\sqrt{n}(T\_n - 1) \\xrightarrow{d} N(0, \\frac{4}{\\theta^2} \\cdot \\frac{\\theta^2}{12} \\cdot \\frac{1}{n} + \\frac{4}{\\theta^2} \\cdot \\frac{\\theta^2}{12} \\cdot \\frac{n}{m})\$</span>

<span class="math inline">\$= N(0, \\frac{1}{3n} + \\frac{1}{3m})\$</span>

More accurate: <span class="math inline">\$\\sqrt{n}(T\_n - 1) \\xrightarrow{d} N(0, \\frac{4}{3}(1 + \\frac{n}{m}))\$</span>

### <span class="header-section-number">5.2</span> What if <span class="math inline">\$\\mu = 0\$</span>? {.anchored number="5.2" anchor-id="what-if-mu-0"}

1.  What if <span class="math inline">\$\\mu\_1 = \\mu\_2 = 0\$</span>? Conclusion still holds: <span class="math inline">\$T\_n = \\frac{1 + O\_p(n^{-1/2})}{1 + O\_p(m^{-1/2})} = 1 + O\_p(n^{-1/2} + m^{-1/2})\$</span>

Note: <span class="math inline">\$\\frac{1}{1 + n^{-1/2}} \\to 1\$</span> (continuous mapping) Not Slutsky

So <span class="math inline">\$n(T\_n - 1)^2 \\xrightarrow{d} \\chi^2\_1\$</span> (continuous mapping) Why not delta method?

In general, can do higher-order Taylor expansions for delta method if derivatives <span class="math inline">\$\\neq 0\$</span>:

<span class="math inline">\$f(X\_n) = f(\\mu) + f'(\\mu)(X\_n - \\mu) + \\frac{1}{2}f''(\\mu)(X\_n - \\mu)^2 + O\_p(n^{-3/2})\$</span>

If <span class="math inline">\$f'(\\mu) = 0\$</span>, use second-order term: <span class="math inline">\$n(f(X\_n) - f(\\mu)) \\xrightarrow{d} \\frac{1}{2}f''(\\mu)\\chi^2\_1\$</span>

---

[← 4 Slutsky’s Theorem {.anchored number="4" anchor-id="slutskys-theorem"}](05-4-slutsky-s-theorem-anchored-number-4-anchor-id-slutskys-the.md) · [Up: contents](index.md)
