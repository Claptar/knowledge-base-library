---
title: 1 Completeness
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html
source_file: sources/berkeley-stat210a/fall-2025/reader/completeness.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Completeness

**Source:** [`reader/completeness.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/completeness.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

As we have seen, for a given statistical problem we may have many different sufficient statistics, some of which reduce the data more than others. We usually want to look for one that is *minimal sufficient*, meaning that it strips away as much irrelevant information as possible and only retains the information that is relevant to estimating the parameter.

In some cases the minimal sufficient statistic has an additional property called *completeness*. The definition of completeness is initially counterintuitive, but it has a number of useful implications we will explore throughout the semester.

### <span class="header-section-number">1.1</span> Definition of completeness {.anchored number="1.1" anchor-id="definition-of-completeness"}

A statistic <span class="math inline">\$T(X)\$</span> is complete for a family of distributions <span class="math inline">\$\\cP = \\{P\_\\theta: \\theta \\in \\Theta\\}\$</span> if no nontrivial function of <span class="math inline">\$T\$</span> can have expectation zero for every distribution in the family:

<span class="math display">\\$$\\EE\_\\theta \\,f(T(X)) = 0 \\quad \\forall \\theta \\in \\Theta \\implies f(T) \\eqPas 0\\$$</span>

Note

The name for complete statistics comes from a prior notion that <span class="math inline">\$\\cP^T = \\{P\_\\theta^T:\\; \\theta \\in \\Theta\\}\$</span> is \`\`complete’’ as a model if its linear span includes all possible distributions on <span class="math inline">\$T(X)\$</span>; see Homework 3.

An equivalent formulations would is that if <span class="math inline">\$\\EE\_\\theta f(T(X)) = c \\forall \\theta\$</span>, for any constant <span class="math inline">\$c\$</span>, then <span class="math inline">\$f(T) \\eqPas c\$</span>.

If <span class="math inline">\$X\$</span> itself is complete, then the definition immediately implies that there can be at most one unbiased estimator for any estimand: if <span class="math inline">\$\\EE\_\\theta \\delta\_1(X) = \\EE\_\\theta \\delta\_2(X) = g(\\theta)\$</span> for all <span class="math inline">\$\\theta \\in \\Theta\$</span>, then <span class="math inline">\$f(X) = \\delta\_1(X) - \\delta\_2(X) = 0\$</span> almost surely. More generally, if <span class="math inline">\$T(X)\$</span> is a complete statistic then there can be at most one unbiased estimator that runs through <span class="math inline">\$T\$</span>. We will return to this fact when we discuss unbiased estimation.

We will be especially interested in statistics that are both complete and sufficient. If <span class="math inline">\$T(X)\$</span> is complete and sufficient we call it a *complete sufficient statistic*.

Warning

A complete statistic need not be sufficient: the constant “statistic” <span class="math inline">\$T(X) \\equiv 0\$</span> is complete in any model. In general, to show that <span class="math inline">\$T(X)\$</span> is complete sufficient we must establish both properties.

### <span class="header-section-number">1.2</span> Examples {.anchored number="1.2" anchor-id="examples"}

**Example 1 (Laplace location family)**: Let <span class="math inline">\$X\_1,\\ldots,X\_n \\simiid \\text{Lap}(\\theta)\$</span> for <span class="math inline">\$\\theta \\in \\RR\$</span> and <span class="math inline">\$n\\geq 2\$</span>, and recall that the vector of order statistics <span class="math inline">\$S(X) = (X\_{(1)},\\ldots,X\_{(n)})\$</span> is a minimal sufficient statistic. Is <span class="math inline">\$S(X)\$</span> complete?

Expand to see answer

**No, <span class="math inline">\$S(X)\$</span> is not complete.**

One simple way to see this is that <span class="math inline">\$X\_{(n)}-X\_{(1)}\$</span> has the same distribution for every <span class="math inline">\$\\theta\$</span>, because we can write <span class="math inline">\$X\_i = \\theta + Z\_i\$</span> for <span class="math inline">\$Z\_1,\\ldots,Z\_n \\simiid \\text{Lap}(0)\$</span> and then <span class="math inline">\$X\_{(n)}-X\_{(1)} = Z\_{(n)}-Z\_{(1)}\$</span>.

Another evocative counterexample is that both the sample median <span class="math inline">\$\\text{Med}(X)\$</span> and sample mean <span class="math inline">\$\\overline{X}\$</span> can be calculated using <span class="math inline">\$S(X)\$</span> alone, and both are unbiased estimators for <span class="math inline">\$\\theta\$</span> (since the distribution is symmetric for <span class="math inline">\$\\theta=0\$</span> and <span class="math inline">\$\\text{Med}(X) = \\theta + \\text{Med}(Z)\$</span>). Hence <span class="math inline">\$f(S) = \\text{Med}(X) - \\overline{X}\$</span> has expectation zero, but is not almost surely equal to zero because the median and mean are a.s. unequal for <span class="math inline">\$n&gt;2\$</span>.

**Example 1 (Uniform scale family)**: Let <span class="math inline">\$X\_1, \\ldots, X\_n \\simiid U$$0, \\theta$$\$</span>, for <span class="math inline">\$\\theta &gt; 0\$</span>. We showed previously that the maximum <span class="math inline">\$T(X) = X\_{(n)}\$</span> is minimal sufficient. Is it complete?

Expand to see answer

**Yes, <span class="math inline">\$T(X)\$</span> is complete.**

As we showed previously, the density of <span class="math inline">\$T(X)\$</span> for <span class="math inline">\$t &gt; 0\$</span> is <span class="math display">\\$$ p\_\\theta(t) = \\frac{nt^{n-1}}{\\theta^n}\\,\\cdot \\;1\\{t \\leq \\theta\\}. \\$$</span>

Suppose we could find <span class="math inline">\$f(t)\$</span> such that <span class="math display">\\$$ 0 = \\EE\_\\theta f(T) = \\frac{n}{\\theta^n}\\int\_0^\\theta f(t) t^{n-1} \\,dt, \\quad \\text{ for all } \\theta &gt; 0. \\$$</span> Dividing the last expression by <span class="math inline">\$n/\\theta^n\$</span> and then differentiating with respect to <span class="math inline">\$\\theta\$</span>, we obtain <span class="math display">\\$$ 0 = f(\\theta) \\theta^{n-1}, \\quad \\text{ for all } \\theta &gt; 0, \\$$</span> hence <span class="math inline">\$f \\equiv 0\$</span>.

### <span class="header-section-number">1.3</span> Full-rank exponential families {.anchored number="1.3" anchor-id="full-rank-exponential-families"}

In the general case where <span class="math inline">\$T(X)\$</span> can take on infinitely many values, it can be hard to show completeness because the space of possible counterexample functions <span class="math inline">\$f\$</span> is infinite-dimensional. But there is an important class of examples where we can quickly verify complete sufficiency, as we see next.

**Definition:** Let <span class="math inline">\$\\cP = \\{P\_\\eta:\\; \\eta \\in \\Xi\\}\$</span> be an <span class="math inline">\$s\$</span>-parameter exponential family with densities <span class="math display">\\$$ p\_\\eta(x) = e^{\\eta'T(x) - A(\\eta)} h(x), \\$$</span> with respect to some carrier measure <span class="math inline">\$\\mu\$</span>. Assume further that the sufficient statistic <span class="math inline">\$T(X)\$</span> satisfies no affine constraint: that is, there is no <span class="math inline">\$\\alpha \\in \\RR\$</span> and nonzero <span class="math inline">\$\\beta \\in \\RR^s\$</span> with <span class="math inline">\$\\beta'T(x) \\eqPas \\alpha\$</span>.

If <span class="math inline">\$\\Xi\$</span> contains an open set we say <span class="math inline">\$\\cP\$</span> is *full-rank*; otherwise we say it is *curved*.

Note

If <span class="math inline">\$T(X)\$</span> does satisfy a linear constraint, that means <span class="math inline">\$\\cP\$</span> can be defined equivalently as an <span class="math inline">\$r\$</span>-parameter exponential family for some <span class="math inline">\$r &lt; s\$</span>. It may be full-rank or curved depending on the parameter space in a lower-dimensional parameterization.

**Theorem (Complete sufficiency in full-rank exponential families):** If <span class="math inline">\$\\cP\$</span> is a full-rank <span class="math inline">\$s\$</span>-parameter exponential family, then <span class="math inline">\$T(X)\$</span> is complete sufficient.

The proof is somewhat technical and uses the uniqueness of moment-generating functions.

Expand for proof

<span class="math inline">\$T(X)\$</span> is sufficient by the factorization theorem, so it remains only to prove completeness.

Assume without loss of generality that <span class="math inline">\$0\$</span> is in the interior of <span class="math inline">\$\\Xi\$</span>; otherwise we can reparameterize. Assume also that <span class="math inline">\$\\cP\$</span> is in canonical form, i.e. <span class="math inline">\$T(X) = X\$</span> and <span class="math inline">\$p\_\\eta(x) = e^{\\eta'x - A(\\eta)}\$</span>. We can always reduce to this case by making a sufficiency reduction and taking <span class="math inline">\$P\_0^T\$</span> as the carrier measure, and showing <span class="math inline">\$T(X)\$</span> is complete after a sufficiency reduction is equivalent to showing it is complete in the original model.

If <span class="math inline">\$X\$</span> is not complete then there is some nontrivial <span class="math inline">\$f(x)\$</span> for which <span class="math inline">\$\\EE\_\\eta f(X) = 0\$</span> for all <span class="math inline">\$\\eta\\in\\Xi\$</span>. Decompose <span class="math inline">\$f(x) = f^+(x) - f^-(x)\$</span> where <span class="math inline">\$f^+(x) = \\max\\{0,f(x)\\}\$</span> and <span class="math inline">\$f^{-}(x) = \\max\\{0,-f(x)\\}\$</span>.

If <span class="math inline">\$\\EE\_\\eta f(X) = \\int (f^+-f^-)p\_\\eta \\,d\\mu = 0\$</span> for all <span class="math inline">\$\\eta\\in\\Xi\$</span>, then we have <span id="eq-mgf-equality"><span class="math display">\\$$ \\int e^{\\eta'x} f^+(x) \\,d\\mu(x) = \\int e^{\\eta'x} f^-(x) \\,d\\mu(x), \\quad \\text{ for all } \\eta \\in \\Xi. \\tag{1}\\$$</span></span>

Assume wlog that <span class="math inline">\$\\int f^+(x)\\,d\\mu(x) = \\int f^-(x)\\,d\\mu(x) = 1\$</span> (otherwise normalize <span class="math inline">\$f\$</span>). Then we can define the random variables <span class="math inline">\$Y^+\$</span> and <span class="math inline">\$Y^-\$</span> with probability densities <span class="math inline">\$f^+(x)\$</span> and <span class="math inline">\$f^-(x)\$</span> respectively, and <a href="#eq-mgf-equality" class="quarto-xref">Equation 1</a> implies that <span class="math inline">\$Y^+\$</span> and <span class="math inline">\$Y^-\$</span> have equal MGFs in a neighborhood of <span class="math inline">\$0\$</span>. Hence they have the same distribution and their densities must be a.s. equal to each other. But <span class="math inline">\$f^+(x)=f^-(x)\$</span> only when both are zero, so <span class="math inline">\$f(x) \\eqmuas 0\$</span> and we have derived a contradiction.

The next figure shows three cases for exponential families with the same sufficient statistic. The set <span class="math inline">\$\\Xi\_1\$</span> indicates the full natural parameter space for a generic 2-parameter exponential family, and (A), (B), and (C) denote parameter spaces for three different subfamilies. The subfamily described by the shaded circle (A) is a full-rank exponential family, because it contains an open set. The subfamily described by the curve (B) is a typical example of a curved family, because it does not contain an open set. The subfamily described by the line segment (C) can be re-parameterized as a full-rank <span class="math inline">\$1\$</span>-parameter exponential family.

<figure class="figure">
<p><img src="completeness.png" class="img-fluid figure-img" /></p>
<figcaption>This figure shows three cases:</figcaption>
</figure>

### <span class="header-section-number">1.4</span> Complete sufficient statistics are minimal {.anchored number="1.4" anchor-id="complete-sufficient-statistics-are-minimal"}

A second convenient property of completeness is that complete sufficient statistics are always minimal sufficient.

**Theorem:** If <span class="math inline">\$T(X)\$</span> is complete sufficient for the family <span class="math inline">\$\\mathcal{P}\$</span>, then <span class="math inline">\$T(X)\$</span> is minimal sufficient for <span class="math inline">\$\\cP\$</span>.

The way that we usually use completeness in proofs is to show that two quantities are almost surely equal by showing that they have the same expectation. The next proof is an example.

*Proof:* Let <span class="math inline">\$S(X)\$</span> represent any minimal sufficient statistic, and define the conditional expectation of <span class="math inline">\$T\$</span> given <span class="math inline">\$S\$</span>: <span class="math display">\\$$ \\overline{T}(S(X)) = \\EE\[T(X) \\mid S(X)$$. \\\]</span> Note that this conditional expectation does not depend on the parameter <span class="math inline">\$\\theta\$</span>, because <span class="math inline">\$S(X)\$</span> is sufficient, so <span class="math inline">\$\\overline{T}\$</span> is a valid statistic. If we can show that <span class="math inline">\$\\overline{T} \\eqas T(X)\$</span>, that means we can calculate <span class="math inline">\$T(X)\$</span> from <span class="math inline">\$S(X)\$</span>, so <span class="math inline">\$T(X)\$</span> is also minimal sufficient.

Because <span class="math inline">\$S(X)\$</span> is minimal sufficient, we can write it as <span class="math inline">\$f(T(X))\$</span> for some function <span class="math inline">\$f\$</span>, and use <span class="math inline">\$f\$</span> to define a function <span class="math inline">\$g\$</span> giving the difference between <span class="math inline">\$T\$</span> and <span class="math inline">\$\\overline{T}\$</span>: <span class="math display">\\$$ g(t) = t - \\overline{T}(f(t)). \\$$</span> The expectation of <span class="math inline">\$g(T)\$</span> is always zero, because <span class="math display">\\$$ \\begin{aligned} \\EE\_\\theta\\; g(T(X)) &= \\EE\_\\theta\\; T(X) - \\EE\_\\theta\\; \\overline{T}(S(X)) \\\\\[5pt$$ &= \\EE\_\\theta\\; T(X) - \\EE\_\\theta\\left$$\\EE\[T(X) \\mid S(X)$$\\right\]\\\\ &= 0. \\end{aligned} \\\]</span> As a result, <span class="math inline">\$g(T) \\eqas 0\$</span> and hence <span class="math inline">\$T \\eqas \\overline{T}\$</span>, as desired.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Ancillarity →](03-2-ancillarity.md)
