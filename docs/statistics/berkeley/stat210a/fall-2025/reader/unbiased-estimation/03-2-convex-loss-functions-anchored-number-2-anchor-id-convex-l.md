---
title: 2 Convex Loss Functions {.anchored number="2" anchor-id="convex-loss-functions"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Convex Loss Functions {.anchored number="2" anchor-id="convex-loss-functions"}

**Source:** [`reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Recall <span class="math inline">\$f(y)\$</span> is *convex* if for all <span class="math inline">\$x\_1, x\_2\$</span> and all <span class="math inline">\$\\gamma \\in $$0,1$$\$</span>:

<span class="math display">\\$$f(\\gamma x\_1 + (1-\\gamma)x\_2) \\leq \\gamma f(x\_1) + (1-\\gamma) f(x\_2)\\$$</span> <span class="math inline">\$f\$</span> is *strictly convex* if the inequality is strict unless <span class="math inline">\$x\_1 = x\_2\$</span>.

An key fact about convex functions is **Jensen’s Inequality:** If <span class="math inline">\$f\$</span> is convex, then for *any* random variable <span class="math inline">\$X\$</span>, we have

<span class="math display">\\$$f(\\EE\[X$$) \\leq \\EE$$f(X)$$\\\]</span> If <span class="math inline">\$f\$</span> is strictly convex, then the inequality is strict unless <span class="math inline">\$X\$</span> is constant.

We say a loss function <span class="math inline">\$L(\\theta, d)\$</span> is a (strictly) convex loss if is (strictly) convex as a function of the estimate <span class="math inline">\$d\$</span>, its second argument, holding the parameter <span class="math inline">\$\\theta\$</span> fixed. Note convexity in <span class="math inline">\$\\theta\$</span> is not relevant here; <span class="math inline">\$\\theta\$</span> is just indexing the model.

**Example:** The best-known example of a convex loss function is the squared error loss. Recall that the corresponding risk, the MSE, can be decomposed as the sum of the bias squared and the variance:

<span class="math display">\\$$ \\begin{aligned} \\text{MSE}\_\\theta(\\delta) &= \\EE\_\\theta\[(\\delta(X) - g(\\theta))^2$$ \\\\$$5pt$$ &= \\text{Bias}\_\\theta(\\delta)^2 + \\text{Var}\_\\theta(\\delta(X)) \\end{aligned} \\\]</span> If <span class="math inline">\$\\delta(X)\$</span> is unbiased, then its MSE is exactly its variance, so minimizing the risk among unbiased estimators just amounts to finding one with the least variance.

---

[← Unbiased estimation Part 02 —](02-unbiased-estimation-part-02.md) · [Up: contents](index.md) · [3 The Rao-Blackwell Theorem {.anchored number="3" anchor-id="the-rao-blackwell-theorem"} →](04-3-the-rao-blackwell-theorem-anchored-number-3-anchor-id-the.md)
