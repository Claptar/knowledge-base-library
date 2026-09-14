---
title: 2 Least Favorable Priors {.anchored number="2" anchor-id="least-favorable-priors"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/minimax-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Least Favorable Priors {.anchored number="2" anchor-id="least-favorable-priors"}

**Source:** [`units/reader/minimax-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Minimax is closely related to Bayes.

Key observation: average case risk ≤ worst case risk

For proper prior <span class="math inline">\$\\pi\$</span>, the Bayes risk is:

<span class="math display">\\$$r(\\pi) = \\int\_\\Theta R(\\theta, \\delta\_\\pi) d\\pi(\\theta)\\$$</span>

<span class="math display">\\$$\\leq \\int\_\\Theta \\sup\_\\theta R(\\theta, \\delta) d\\pi(\\theta) = \\sup\_\\theta R(\\theta, \\delta)\\$$</span>

If <span class="math inline">\$\\delta\_\\pi\$</span> is Bayes, then <span class="math inline">\$r(\\pi) = \\inf\_\\delta \\int\_\\Theta R(\\theta, \\delta) d\\pi(\\theta)\$</span>

Bayes risk of any Bayes estimator lower bounds <span class="math inline">\$r\$</span>.

Least favorable prior <span class="math inline">\$\\pi\$</span> gives best lower bound: <span class="math inline">\$r(\\pi) = \\sup\_\\pi r(\\pi)\$</span>

Sup risk of any estimator upper bounds <span class="math inline">\$r\$</span>:

<span class="math display">\\$$\\sup\_\\theta R(\\theta, \\delta) \\geq r \\geq \\sup\_\\pi r(\\pi)\\$$</span>

Can exhibit minimax est. & LF prior by finding <span class="math inline">\$\\pi\$</span> and <span class="math inline">\$\\delta\$</span> that collapse these inequalities.

### <span class="header-section-number">2.1</span> Theorem {.anchored number="2.1" anchor-id="theorem"}

If <span class="math inline">\$R(\\delta\_\\pi) = \\sup\_\\theta R(\\theta, \\delta\_\\pi)\$</span> with Bayes estimator <span class="math inline">\$\\delta\_\\pi\$</span>, then:

1.  <span class="math inline">\$\\delta\_\\pi\$</span> is minimax
2.  If <span class="math inline">\$\\delta\_\\pi\$</span> is unique Bayes (up to <span class="math inline">\$\\pi\$</span>-a.e.), it is unique minimax
3.  <span class="math inline">\$\\pi\$</span> is least favorable

Proof:

1.  Any other <span class="math inline">\$\\delta\$</span>: <span class="math display">\\$$\\sup\_\\theta R(\\theta, \\delta) \\geq \\int R(\\theta, \\delta) d\\pi(\\theta) \\geq\\$$</span> <span class="math display">\\$$\\int R(\\theta, \\delta\_\\pi) d\\pi(\\theta) = r(\\pi) = \\sup\_\\theta R(\\theta, \\delta\_\\pi)\\$$</span> <span class="math inline">\$r\$</span> is minimax risk, <span class="math inline">\$\\delta\_\\pi\$</span> is minimax

2.  Replace <span class="math inline">\$\\geq\$</span> with <span class="math inline">\$=\$</span> in 2nd inequality ⟹ <span class="math inline">\$\\delta = \\delta\_\\pi\$</span> <span class="math inline">\$\\pi\$</span>-a.e.

3.  Any other prior <span class="math inline">\$\\pi'\$</span>: <span class="math display">\\$$\\inf\_\\delta r(\\pi') \\leq \\int R(\\theta, \\delta\_\\pi) d\\pi'(\\theta)\\$$</span> <span class="math display">\\$$\\leq \\sup\_\\theta R(\\theta, \\delta\_\\pi) = r(\\pi)\\$$</span>

The above theorem gives a checkable condition: does avg risk = sup risk?

Note: If <span class="math inline">\$R(\\theta, \\delta\_\\pi)\$</span> is constant, it doesn’t prove anything.

1.  <span class="math inline">\$R(\\theta, \\delta\_\\pi)\$</span> is constant
2.  Also <span class="math inline">\$R(\\theta, \\delta\_\\pi) = \\sup\_\\theta R(\\theta, \\delta\_\\pi) = r(\\pi)\$</span>

### <span class="header-section-number">2.2</span> Example: Binomial {.anchored number="2.2" anchor-id="example-binomial"}

<span class="math inline">\$X \\sim \\text{Binom}(n, \\theta)\$</span>, estimate <span class="math inline">\$\\theta\$</span> with squared error

Try Beta(<span class="math inline">\$\\alpha, \\beta\$</span>), hope to get one with constant risk

<span class="math display">\\$$\\delta\_\\pi(X) = \\frac{X + \\alpha}{n + \\alpha + \\beta}\\$$</span>

<span class="math display">\\$$R(\\theta, \\delta\_\\pi) = \\mathbb{E}\[\\theta^2$$ - \\mathbb{E}$$\\delta\_\\pi(X)^2$$ + \\text{Var}(\\delta\_\\pi(X))\\\]</span>

<span class="math display">\\$$= \\theta - \\frac{(\\alpha + \\beta + n + 1)(\\alpha + n\\theta)^2}{(\\alpha + \\beta + n)^2(n + \\alpha + \\beta + 1)} + \\frac{(\\alpha + n\\theta)(\\beta + n(1-\\theta))}{(\\alpha + \\beta + n)^2(n + \\alpha + \\beta + 1)}\\$$</span>

Set <span class="math inline">\$\\alpha + \\beta = n + 2\$</span>, <span class="math inline">\$\\alpha + \\beta = \\frac{n}{2}\$</span>

<span class="math display">\\$$\\beta = \\frac{n+2}{2}, \\alpha = \\frac{n+2}{2}\\$$</span>

Beta(<span class="math inline">\$\\frac{n+2}{2}, \\frac{n+2}{2}\$</span>) is LF, <span class="math inline">\$\\delta\_\\pi\$</span> is minimax

We got lucky.

Question: Why so much prior weight on <span class="math inline">\$\\theta \\approx \\frac{1}{2}\$</span>?

---

[← 1 Minimax Risk Estimator {.anchored number="1" anchor-id="minimax-risk-estimator"}](02-1-minimax-risk-estimator-anchored-number-1-anchor-id-minimax.md) · [Up: contents](index.md) · [3 Least Favorable Sequence {.anchored number="3" anchor-id="least-favorable-sequence"} →](04-3-least-favorable-sequence-anchored-number-3-anchor-id-least.md)
