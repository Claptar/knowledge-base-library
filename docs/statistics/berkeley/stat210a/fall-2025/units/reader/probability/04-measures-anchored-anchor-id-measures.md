---
title: Measures {.anchored anchor-id="measures"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/probability.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Measures {.anchored anchor-id="measures"}

**Source:** [`units/reader/probability.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Given a set <span class="math inline">\$\\cX\$</span>, a measure <span class="math inline">\$\\mu\$</span> is a certain kind of function mapping (non-pathological[^1]) subsets <span class="math inline">\$A \\subseteq \\cX\$</span> to non-negative numbers <span class="math inline">\$\\mu(A) \\in $$0,\\infty$$\$</span>.

**Example 1 (Counting measure):** If <span class="math inline">\$\\cX\$</span> is countable, e.g. <span class="math inline">\$\\cX = \\mathbb{Z}\$</span>, then a natural measure is the *counting measure* <span class="math inline">\$\\#(A)\$</span>*,* which simply counts the number of points in a subset <span class="math inline">\$A\$</span>. That is, <span class="math inline">\$\\#(\\{0,1\\}) = 2\$</span>, and <span class="math inline">\$\\#(\\{2,4,6,8,\\ldots\\}) = \\infty\$</span> .

**Example 2 (Lebesgue measure):** If <span class="math inline">\$\\cX = \\RR^n\$</span> for some integer <span class="math inline">\$n\$</span>, a natural measure is the *Lebesgue measure* <span class="math inline">\$\\lambda(A)\$</span>, which returns the *volume* of a subset <span class="math inline">\$A\$</span>. Roughly speaking, we can write

<span class="math display">\\$$ \\lambda(A) = \\int \\cdots \\int\_A \\,d x\_1\\,d x\_2\\cdots \\,d x\_n. \\$$</span>

**Example 3 (Gaussian measure):** Now taking <span class="math inline">\$\\cX = \\RR\$</span>, we might instead want to define the “size” of a set as the probability that a standard Gaussian random variable <span class="math inline">\$Z \\sim \\cN(0,1)\$</span> is observed to be in the set <span class="math inline">\$A\$</span>. That is, we can define the measure:

<span class="math display">\\$$ P\_Z(A) = \\PP(Z \\in A) = \\int\_A \\phi(x)\\,d x, \\quad \\text{ where } \\;\\phi(x) = \\frac{1}{\\sqrt{2\\pi}} e^{-x^2/2} \\$$</span>

is the probability density function of <span class="math inline">\$Z\$</span>.

As it turns out, it is not so obvious how to define what exactly we mean by taking an integral when the set is sufficiently pathological: some sets are just called *non-measurable* and we can’t hope to meaningfully assign them a measure. Sets of this kind are important to consider when building a rigorous theory about measures but they are not the sort of thing you would stumble upon unless you went out looking for them.

One of the original motivations for measure theory was to provide a framework for excluding these pathological sets and rigorously defining integrals over the other, nicer sets. In general, the domain of a measure is not all subsets of <span class="math inline">\$\\cX\$</span> (called the power set and notated <span class="math inline">\$2^{\\cX}\$</span>), but rather a collection of “nice enough” subsets <span class="math inline">\$\\cF \\subseteq 2^{\\cX}\$</span>.

Formally, the collection <span class="math inline">\$\\cF\$</span> must be a <span class="math inline">\$\\sigma\$</span>-field, meaning that it satisfies certain closure properties. We say <span class="math inline">\$\\cF\$</span> is a <span class="math inline">\$\\sigma\$</span>-*field* (or <span class="math inline">\$\\sigma\$</span>-*algebra*) if

1.  The full set <span class="math inline">\$\\cX\$</span> is in <span class="math inline">\$\\cF\$</span>.

2.  If <span class="math inline">\$A\$</span> is in <span class="math inline">\$\\cF\$</span> then its complement <span class="math inline">\$\\cX \\setminus A\$</span> is also in <span class="math inline">\$\\cF\$</span> (i.e., <span class="math inline">\$\\cF\$</span> is *closed under complementation*)

3.  If <span class="math inline">\$A\_1,A\_2,\\ldots \\in \\cF\$</span> then <span class="math inline">\$\\bigcup\_{i=1}^\\infty A\_i\$</span> is also in <span class="math inline">\$\\cF\$</span> (i.e. <span class="math inline">\$\\cF\$</span> is *closed under countable unions*)

The details of this definition are not important for purposes of this course.

**Example:** If <span class="math inline">\$\\cX\$</span> is countable we can take <span class="math inline">\$\\cF\$</span> to be the entire power set.

**Example:** If <span class="math inline">\$\\cX = \\mathbb{R}^n\$</span> we will typically use the *Borel* <span class="math inline">\$\\sigma\$</span>-*field* <span class="math inline">\$\\cB\$</span>, defined as the smallest <span class="math inline">\$\\sigma\$</span>-field that includes all open rectangles <span class="math inline">\$(a\_1,b\_1)\\times (a\_2,b\_2) \\times \\cdots \\times (a\_n, b\_n)\$</span>, where <span class="math inline">\$a\_i &lt; b\_i\$</span> for all <span class="math inline">\$i\$</span>. That is, we start with the open rectangles and recursively apply the closure properties to obtain a very large collection of sets, which informally we can think of as containing all non-pathological subsets of <span class="math inline">\$\\mathbb{R}^n\$</span>.

We are now ready to define a measure. We call a pair of a set <span class="math inline">\$\\cX\$</span> and an associated <span class="math inline">\$\\sigma\$</span>-field <span class="math inline">\$\\cF \\subseteq 2^{\\cX}\$</span> a *measurable space*.

**Definition:** Given a measurable space <span class="math inline">\$(\\cX, \\cF)\$</span>, a *measure* is a function <span class="math inline">\$\\mu: \\cF \\to $$0,\\infty$$\$</span> (inclusive of <span class="math inline">\$+\\infty\$</span>) satisfying three properties:

1.  **Non-negativity:** <span class="math inline">\$\\mu(A) \\geq 0\$</span> for all <span class="math inline">\$A\\in \\cF\$</span>.

2.  **Countable additivity:** If <span class="math inline">\$A\_1,A\_2,\\ldots\\in \\cF\$</span> are all disjoint, then

<span class="math display">\\$$ \\mu\\left(\\bigcup\_{i=1}^\\infty A\_i\\right) = \\sum\_{i=1}^\\infty \\mu(A\_i) \\$$</span>

1.  **Empty set maps to zero:** <span class="math inline">\$\\mu(\\emptyset) = 0\$</span>[^2]

If <span class="math inline">\$\\mu\$</span> is a measure on <span class="math inline">\$(\\cX, \\cF)\$</span> we call <span class="math inline">\$(\\cX, \\cF, \\mu)\$</span> a *measure space*. In the special case <span class="math inline">\$\\mu(\\cX) = 1\$</span>, we call <span class="math inline">\$\\mu\$</span> a *probability measure* and <span class="math inline">\$(\\cX, \\cF, \\mu)\$</span> is called a *probability space*.

[^1]: A problem in the first homework will guide you step-by-step in constructing the kind of pathological set that makes the parenthetical caveat necessary when we are dealing with continuous spaces.

[^2]: The requirement that <span class="math inline">\$\\mu(\\emptyset) = 0\$</span> is redundant if <span class="math inline">\$\\mu(\\cX)\$</span> is finite. Otherwise, it prevents us from assigning infinite measure to every set including <span class="math inline">\$\\emptyset\$</span>.

---

[← Probability as a measure {.anchored anchor-id="probability-as-a-measure"}](03-probability-as-a-measure-anchored-anchor-id-probability-as-a.md) · [Up: contents](index.md) · [Integrals {.anchored anchor-id="integrals"} →](05-integrals-anchored-anchor-id-integrals.md)
