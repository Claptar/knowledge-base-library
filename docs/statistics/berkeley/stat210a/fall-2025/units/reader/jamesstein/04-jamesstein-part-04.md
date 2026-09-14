---
title: Jamesstein Part 04 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/jamesstein.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/jamesstein.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Jamesstein Part 04 —

**Source:** [`units/reader/jamesstein.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/jamesstein.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We are now ready to calculate the risk of the James–Stein estimator <span class="math inline">\$\\delta\_{JS}(X) = \\left(1 - \\frac{d-2}{\\\|X\\\|^2}\\right)X\$</span>. We can drop the assumption \$^2 = \$, under the assumption <span class="math inline">\$\\sigma^2 = 1\$</span> (for general <span class="math inline">\$\\sigma^2\$</span>, we should replace the numerator <span class="math inline">\$d-2\$</span> with <span class="math inline">\$(d-2)\\sigma^2\$</span>. Then ).

Proceeding as before, we have <span class="math display">\\$$ h(X) = \\frac{d-2}{\\\|X\\\|^2}X \\Rightarrow \\\|h(X)\\\|^2 = \\frac{(d-2)^2}{\\\|X\\\|^2}, \\$$</span> Applying the quotient rule we have <span class="math display">\\$$Dh(X)\_{ii} = (d-2)\\frac{\\partial}{\\partial X\_i} \\frac{X\_i}{\\sum\_j X\_j^2} = (d-2)\\frac{\\\|X\\\|^2 - 2X\_i^2}{\\\|X\\\|^4},\\$$</span> and summing over the coordinates gives <span class="math display">\\$$\\text{tr}(Dh(X)) = (d-2) \\frac{d\\\|X\\\|^2 - 2\\\|X\\\|^2}{\\\|X\\\|^4} = -\\frac{(d-2)^2}{\\\|X\\\|^2}.\\$$</span> We thereby obtain the estimator <span class="math display">\\$$ \\widehat{\\text{MSE}}(X) = d + \\frac{(d-2)^2}{\\\|X\\\|^2} - 2\\frac{(d-2)^2}{\\\|X\\\|^2} = d - \\frac{(d-2)^2}{\\\|X\\\|^2}. \\$$</span> Taking expectations, we obtain <span class="math display">\\$$ \\text{MSE}(\\theta; \\delta\_{\\text{JS}}) = d - (d-2)^2\\EE\_\\theta\\left\[\\frac{1}{\\\|X\\\|^2}\\right$$. \\\]</span> Note this is always strictly less than <span class="math inline">\$d\$</span>, which is the MSE of <span class="math inline">\$\\delta\_0(X) = X\$</span>.

If <span class="math inline">\$\\theta = 0\$</span> then <span class="math inline">\$\\\|X\\\|^2 \\sim \\chi\_d^2\$</span> and we can apply our previous result to obtain <span class="math display">\\$$ \\text{MSE}(0; \\delta\_{\\text{JS}}) = d - (d-2)^2\\frac{1}{d-2} = 2. \\$$</span> Thus, even though we are estimating <span class="math inline">\$d\$</span> parameters, our total MSE does not rise with <span class="math inline">\$d\$</span>, because we will shrink harder and harder toward zero the larger <span class="math inline">\$d\$</span> gets. This is fairly remarkable.

On the other hand, suppose <span class="math inline">\$\\\|\\theta\\\|^2 \\to \\infty\$</span>. Then <span class="math inline">\$\\EE\_\\theta \\\|X\\\|^2 \\to \\infty\$</span> and the improvement <span class="math inline">\$(d-2)^2/\\EE\_\\theta\\\|X\\\|^2\$</span> will be driven to <span class="math inline">\$0\$</span>.

Note that, for more general <span class="math inline">\$\\sigma^2\$</span>, the James–Stein estimator is <span class="math inline">\$\\left(1-\\frac{(d-2)\\sigma^2}{\\\|X\\\|^2}\\right)X\$</span>. Then we have <span class="math display">\\$$h(X) = \\sigma^2\\frac{d-2}{\\\|X\\\|^2} \\Rightarrow \\\|h(X)\\\|^2 = \\sigma^4 \\frac{(d-2)^2}{\\\|X\\\|^2}, \\quad \\text{tr} Dh(X) = \\sigma^2 \\frac{(d-2)^2}{\\\|X\\\|^2},\\$$</span> leading to the estimator <span class="math inline">\$\\widehat{\\text{MSE}}(X) = \\sigma^2 d - \\sigma^4\\frac{(d-2)^2}{\\\|X\\\|^2}\$</span>, and plugging in <span class="math inline">\$\\EE\_0 1/\\\|X\\\|^2 = 1/(d-2)\\sigma^2\$</span>, the MSE at <span class="math inline">\$\\theta=0\$</span> is <span class="math inline">\$2\\sigma^2\$</span>.

### <span class="header-section-number">3.1</span> Final thoughts {.anchored number="3.1" anchor-id="final-thoughts"}

A few more notes: first, <span class="math inline">\$\\delta\_{JS}(X)\$</span> also inadmissible, since <span class="math inline">\$\\delta\_{+}(X) = (1 - \\frac{d-2}{\\\|X\\\|^2})\_+ X\$</span> is strictly better since we never benefit from using a shrinkage parameter <span class="math inline">\$\\zeta &gt; 1\$</span>.

A practically more useful version of James–Stein shrinks toward the central value <span class="math inline">\$\\overline{X}\$</span>:

<span class="math display">\\$$\\delta\_{JS+, i}(X) = \\overline{X} + (1 - \\frac{d-3}{V^2})\_+ (X\_i - \\overline{X})\\$$</span> This estimator dominates <span class="math inline">\$\\delta(X) = X\$</span> for <span class="math inline">\$d \\geq 4\$</span>.

Taken to its logical extreme, the James–Stein estimator seems to imply absurd things: should all scientists at Berkeley, across all different fields, pool their estimates to calculate a James–Stein estimator even if their different estimation problems have nothing to do with each other, as long as they are estimating Gaussian location parameters? The overall MSE for all of the estimates really would be better.

To avoid this conclusion we might note that even when the overall MSE is improved, the MSE for a single coordinate can certainly get worse. For example, if <span class="math inline">\$\\theta\_1 = 10\$</span> but <span class="math inline">\$\\theta\_2=\\theta\_3=\\cdots=\\theta\_{1000}=0\$</span>, it’s likely that we’ll overshrink our estimate of <span class="math inline">\$\\theta\_1\$</span> toward <span class="math inline">\$0\$</span> in order to do well on the other coordinates. So people who believe their estimands are larger than average wouldn’t want to participate in this scheme.

---

[← Jamesstein Part 03 —](03-jamesstein-part-03.md) · [Up: contents](index.md)
