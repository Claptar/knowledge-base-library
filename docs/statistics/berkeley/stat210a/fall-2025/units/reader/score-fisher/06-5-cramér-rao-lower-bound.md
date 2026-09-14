---
title: 5 Cramér-Rao Lower Bound
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5 Cramér-Rao Lower Bound

**Source:** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Let <span class="math inline">\$\\delta(X)\$</span> be any real-valued statistic. Let <span class="math inline">\$g(\\theta) = \\EE\_\\theta$$\\delta$$\$</span>, so <span class="math inline">\$\\delta\$</span> is an unbiased estimator for <span class="math inline">\$g(\\theta)\$</span>. If we repeat the idea of differentiating <span class="math inline">\$g(\\theta) = \\int \\delta(x) e^{\\ell(\\theta;x)}\\,d\\mu(x)\$</span> with respect to <span class="math inline">\$\\theta\_j\$</span> for each <span class="math inline">\$j\$</span>, and collect the resulting partial derivatives into a vector, we obtain

<span class="math display">\\$$\\nabla g(\\theta) = \\int \\delta(x) \\nabla \\ell(\\theta;x) e^{\\ell(\\theta;x)}\\,d\\mu(x) = \\EE\_\\theta\\left\[\\delta(X) \\nabla\\ell(\\theta;X)\\right$$ = \\Cov\_\\theta\\left(\\delta(X), \\nabla\\ell(\\theta;X)\\right).\\\]</span> Combining these results with the Cauchy-Schwarz inequality gives us the *Cramér-Rao Lower Bound*, also known as the *Information lower bound*. For a single parameter (<span class="math inline">\$d=1\$</span>), we have <span class="math display">\\$$\\Var\_\\theta(\\delta(X)) \\cdot \\Var\_\\theta(\\dot{\\ell}(\\theta;X)) \\geq \\Cov\_\\theta(\\delta(X), \\dot{\\ell}(\\theta; X))^2, \\$$</span> so after rearranging terms and applying identities, <span class="math display">\\$$\\Var\_\\theta(\\delta(X)) \\geq \\frac{\\dot{g}(\\theta)^2}{J(\\theta)}.\\$$</span>

For the multivariate case (<span class="math inline">\$d&gt;1\$</span>), we have more generally <span class="math display">\\$$ \\Var\_\\theta(\\delta(X) \\geq \\nabla g(\\theta)'J(\\theta)^{-1}\\nabla g(\\theta).\\$$</span> The interpretation of this identity is that no unbiased estimator for <span class="math inline">\$g(\\theta)\$</span> can have variance smaller than <span class="math inline">\$\\nabla g(\\theta)'J(\\theta)^{-1}\\nabla g(\\theta)\$</span>. In particular, if <span class="math inline">\$g(\\theta) = \\theta\_j\$</span>, no estimator can have variance smaller than <span class="math inline">\$(J(\\theta)^{-1})\_{jj}\$</span>.

<span class="math display">\\$$\\Var\_\\theta(\\delta) \\geq \\Var\_\\theta(\\delta(X)) \\Cov\_\\theta(\\delta, \\nabla l\_\\theta(X))I(\\theta)^{-1}\\Cov\_\\theta(\\delta, \\nabla l\_\\theta(X))' = g'(\\theta)I(\\theta)^{-1}g'(\\theta)'\\$$</span>

Expand to see proof

For any <span class="math inline">\$a \\in \\RR^d\$</span>, we can write <span class="math display">\\$$\\begin{aligned} \\Var\_\\theta(\\delta(X)) \\cdot a'J(\\theta)a &= \\Var\_\\theta(\\delta)\\Var\_\\theta(a'\\nabla\\ell(\\theta;X))\\\\ &\\geq \\Cov\_\\theta(\\delta(X), a'\\nabla\\ell(\\theta;X))^2\\\\ &= \\left(a'\\nabla \\Cov\_\\theta(\\delta, \\nabla\\ell(\\theta))\\right)^2\\\\ &= (a'\\nabla g(\\theta))^2. \\end{aligned}\\$$</span>

Thus we obtain for all nonzero <span class="math inline">\$a \\in \\RR^d\$</span>,

<span class="math display">\\$$\\Var\_\\theta(\\delta(X)) \\geq \\frac{(a'\\nabla g(\\theta))^2}{a'J(\\theta)a}.\\$$</span>

We obtain the result by optimizing the bound, with <span class="math inline">\$a = J(\\theta)^{-1}\\nabla g(\\theta)\$</span> (show this as an exercise).

---

[← 4 Differential Identities and the Fisher Information](05-4-differential-identities-and-the-fisher-information.md) · [Up: contents](index.md) · [6 Examples →](07-6-examples.md)
