---
title: Factorization theorem {.anchored anchor-id="factorization-theorem"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/sufficiency.html
source_file: sources/berkeley-stat210a/fall-2025/reader/sufficiency.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Factorization theorem {.anchored anchor-id="factorization-theorem"}

**Source:** [`reader/sufficiency.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/sufficiency.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We didn’t really need to go to the trouble of calculating the conditional distribution in the previous examples. The easiest way to verify that a statistic is sufficient is to show that the density <span class="math inline">\$p\_\\theta\$</span> factorizes into a part that involves only <span class="math inline">\$\\theta\$</span> and <span class="math inline">\$T(x)\$</span>, and a part that involves only <span class="math inline">\$x\$</span>.

**Factorization Theorem:** Let <span class="math inline">\$\\cP\$</span> be a model having densities <span class="math inline">\$p\_\\theta(x)\$</span> with respect to a common dominating measure <span class="math inline">\$\\mu\$</span>. Then <span class="math inline">\$T(X)\$</span> is sufficient for <span class="math inline">\$\\cP\$</span> if and only if there exist non-negative functions <span class="math inline">\$g\_\\theta\$</span> and <span class="math inline">\$h\$</span> for which

<span class="math display">\\$$ p\_\\theta(x) = g\_\\theta(T(x)) h(x), \\$$</span>

for almost every <span class="math inline">\$x\$</span> under <span class="math inline">\$\\mu\$</span>.

The “almost every <span class="math inline">\$x\$</span>” qualification means that

<span class="math display">\\$$ \\mu\\left(\\{x:\\; p\_\\theta(x) \\neq g\_\\theta(T(x))h(x)\\}\\right) = 0. \\$$</span>

It is needed to avoid counterexamples where we mess with the densities on a set of points that the base measure doesn’t assign any mass, which would let us destroy the factorization structure without changing any of the distributions.

**Proof (discrete** <span class="math inline">\$\\cX\$</span>): The proof is easiest in the discrete case, so that we don’t have to deal with conditioning on measure-zero events and worry about things like Jacobians for change of variables.

We’ll assume without loss of generality that <span class="math inline">\$\\mu\$</span> is the counting measure: if <span class="math inline">\$\\mu\$</span> were some other measure, it would have to have a density <span class="math inline">\$m\$</span> with respect to the counting measure and we would just have to carry around <span class="math inline">\$m(x)\$</span> in all of our expressions.

First, assume that there exists a factorization <span class="math inline">\$p\_\\theta(x) = g\_\\theta(T(x)) h(x)\$</span>. Then we have

<span class="math display">\\$$ \\begin{aligned} \\PP\_\\theta(X = x \\mid T(X) = t) &= \\frac{\\PP\_\\theta(X = x, T(X) = t)}{\\PP\_\\theta(T(X) = t)}\\\\\[7pt$$ &= \\frac{g\_\\theta(t) h(x) 1\\{T(x) = t\\}}{g\_\\theta(t)\\displaystyle\\sum\_{z:\\;T(z) = t} h(z)}\\\\$$7pt$$ &= \\frac{h(x) 1\\{T(x) = t\\}}{\\displaystyle\\sum\_{z:\\;T(z) = t} h(z)}, \\end{aligned} \\\]</span>

which we see does not depend on <span class="math inline">\$\\theta\$</span>.

Next consider the opposite direction. If <span class="math inline">\$T(X)\$</span> is sufficient, then we can construct a factorization by writing

<span class="math display">\\$$ \\begin{aligned} g\_\\theta(t) &= \\PP\_\\theta(T(X)=t)\\\\ h(x) &= \\PP(X = x \\mid T(X) = T(x)), \\end{aligned} \\$$</span> noting that the conditional probability in the definition of <span class="math inline">\$h(x)\$</span> does not depend on <span class="math inline">\$\\theta\$</span> by sufficiency. Then we have

<span class="math display">\\$$ \\PP\_\\theta(X = x) = \\PP\_\\theta(T(X) = T(x)) \\;\\cdot\\;\\PP\_\\theta(X = x \\mid T(X) = T(x)) = g\_\\theta(T(x)) h(x), \\$$</span> so <span class="math inline">\$g\_\\theta(T(x))h(x)\$</span> is indeed the pmf <span class="math inline">\$p\_\\theta(x)\$</span>.

---

[← Visualization of sufficiency {.anchored anchor-id="visualization-of-sufficiency"}](03-visualization-of-sufficiency-anchored-anchor-id-visualizatio.md) · [Up: contents](index.md) · [Sufficiency Part 05 — →](05-sufficiency-part-05.md)
