---
title: Exponential family structure {.anchored anchor-id="exponential-family-structure"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/exponential-families.html
source_file: sources/berkeley-stat210a/fall-2025/reader/exponential-families.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Exponential family structure {.anchored anchor-id="exponential-family-structure"}

**Source:** [`reader/exponential-families.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/exponential-families.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Thus far we have discussed statistical models in the abstract without making any assumptions about them. Exponential families, the topic of this lecture, are models with a special structure that makes them especially easy to work with.

We say the model <span class="math inline">\$\\cP = \\{P\_\\eta:\\eta \\in \\Xi\\}\$</span> is an <span class="math inline">\$s\$</span>*-parameter* *exponential family* if it is defined by a family of densities of the form:

<span id="eq-expo-fam"><span class="math display">\\$$ p\_\\eta(x) = e^{\\eta'T(x) - A(\\eta)}h(x), \\tag{1}\\$$</span></span>

all with respect to a common *dominating measure* <span class="math inline">\$\\mu\$</span>, i.e. a measure <span class="math inline">\$\\mu\$</span> such that <span class="math inline">\$P\_\\eta \\ll \\mu\$</span> for all <span class="math inline">\$\\eta\\in \\Xi\$</span>.

The different parts of the expression in <a href="#eq-expo-fam" class="quarto-xref">Equation 1</a> have distinct names referring to the role they play in defining the density:

<span class="math display">\\$$ \\begin{aligned} T&:\\; \\cX \\to \\RR^s &\\qquad &\\text{ is called the {\\it sufficient statistic}}\\\\ h&:\\; \\cX \\to \[0,\\infty) &\\qquad &\\text{ is called the {\\it carrier density} or {\\it base density}}\\\\ \\eta &\\in \\Xi \\subseteq \\RR^s &\\qquad &\\text{ is called the {\\it natural parameter}}\\\\ A&:\\; \\Xi \\to \\RR &\\qquad &\\text{ is called the {\\it log-partition function}} \\end{aligned} \\$$</span>

The function <span class="math inline">\$A(\\eta)\$</span> is totally determined by <span class="math inline">\$T\$</span> and <span class="math inline">\$h\$</span>, and plays the role of normalizing the density so that <span class="math inline">\$P\_\\eta(\\cX) = 1\$</span>:

<span id="eq-log-partition"><span class="math display">\\$$ A(\\eta) = \\log\\left( \\int\_\\cX e^{\\eta'T(x)}h(x)\\td\\mu(x)\\right) \\leq \\infty \\tag{2}\\$$</span></span>

If <span class="math inline">\$A(\\eta) = \\infty\$</span> then there is no way to normalize <span class="math inline">\$p\_\\eta\$</span>, so <span class="math inline">\$\\eta\$</span> is not an allowed value for the natural parameter to take. The *natural parameter space*, which we denote <span class="math inline">\$\\Xi\_1\$</span>, is the set of all <span class="math inline">\$\\eta\$</span> values for which the family is normalizable:

<span class="math display">\\$$ \\Xi\_1 = \\{\\eta:\\; A(\\eta) &lt; \\infty\\} \\subseteq \\RR^s. \\$$</span>

We will show in Homework 1 that <span class="math inline">\$A(\\eta)\$</span> is a convex function, so <span class="math inline">\$\\Xi\_1\$</span> is a convex set.

Note that, because <span class="math inline">\$\\mu\$</span> is allowed to be an arbitrary measure, <span class="math inline">\$h(x)\$</span> also plays an inessential role since we could always absorb it into the base measure <span class="math inline">\$\\mu\$</span>. More precisely, suppose we define a new dominating measure <span class="math inline">\$\\nu\$</span> whose density with respect to <span class="math inline">\$\\mu\$</span> is <span class="math inline">\$h\$</span> (informally we can write <span class="math inline">\$\\td\\nu = h\\td\\mu\$</span>). Then <span class="math inline">\$P\_\\eta\$</span>, which had density <span class="math inline">\$e^{\\eta'T(x)}h(x)\$</span> with respect to <span class="math inline">\$\\mu\$</span>, now has density <span class="math inline">\$e^{\\eta'T(x)}\$</span> with respect to <span class="math inline">\$\\nu\$</span>.

As a result, if we were aiming for maximal parsimony we could assume without loss of generality that <span class="math inline">\$h(x) = 1\$</span>, removing it from the definition <a href="#eq-expo-fam" class="quarto-xref">Equation 1</a> and replacing <span class="math inline">\$\\mu\$</span> with our new, bespoke measure <span class="math inline">\$\\nu\$</span>. However, it is convenient to leave <a href="#eq-expo-fam" class="quarto-xref">Equation 1</a> as is if it allows us to take <span class="math inline">\$\\mu\$</span> to be some simple default measure like a counting measure or Lebesgue measure. In that case, <span class="math inline">\$p\_\\eta\$</span> will be a standard pmf or pdf, so we can discuss it without going over the head of anyone who lacks a background in measure theory.

**Example (Poisson):** The Poisson distribution <span class="math inline">\$\\textrm{Pois}(\\lambda)\$</span> has probability mass function

<span class="math display">\\$$ p\_\\lambda(x) = \\frac{\\lambda^x e^{-\\lambda}}{x!}, \\quad \\textrm{ on } x = 0, 1, 2, \\ldots. \\$$</span>

Formally this pmf is a density over the counting measure on the set of non-negative integers <span class="math inline">\$\\ZZ\_+ = \\{0,1,\\ldots\\}\$</span>.

Letting <span class="math inline">\$\\lambda\$</span> range over <span class="math inline">\$$$0, \\infty)\$</span> yields an exponential family, but it is not immediately obvious from the form of the density. To see this, we need to massage <span class="math inline">\$p\_\\lambda(x)\$</span> a bit, by observing that

<span class="math display">\\\[ p\_\\lambda(x) = \\exp\\{(\\log \\lambda) x - \\lambda\\}\\frac{1}{x!}. \\$$</span>

Now we see that we can reparameterize the family by setting <span class="math inline">\$\\eta = \\log\\lambda\$</span>, leading to

<span class="math display">\\$$ p\_\\eta(x) = \\exp\\{\\eta x - e^\\eta\\} \\frac{1}{x!}. \\$$</span> At this point, we immediately recognize <span class="math inline">\$p\_\\eta\$</span> as an exponential family with sufficient statistic <span class="math inline">\$T(x) = x\$</span>, and base density <span class="math inline">\$h(x) = \\frac{1}{x!}\$</span>, and log-partition function <span class="math inline">\$A(\\eta) = e^{\\eta}\$</span>.

Note that this is not the only way to decompose the Poisson distribution as an exponential family. For example, we could just as well take <span class="math inline">\$T(x) = x/2\$</span>; then we would have <span class="math inline">\$\\eta = 2\\log\\lambda\$</span> and <span class="math inline">\$A(\\eta) = e^{\\eta/2}\$</span>. Or, we could take <span class="math inline">\$T(x) = x + 1\$</span> and <span class="math inline">\$A(\\eta) = e^{\\eta} + \\eta\$</span>.

This is not just a property of the Poisson distribution; the decomposition is generally non-unique for exponential families. For any exponential family of the form <a href="#eq-expo-fam" class="quarto-xref">Equation 1</a> , if <span class="math inline">\$U \\in \\RR^{s\\times s}\$</span> is invertible and <span class="math inline">\$v \\in \\RR^s\$</span> then we can write the same density as <span class="math inline">\$e^{\\zeta'S(x) - B(\\zeta)}h(x)\$</span>, for new sufficient statistic <span class="math inline">\$S(x) = U T(x) + v\$</span>, new natural parameter <span class="math inline">\$\\zeta = (U^{-1})'\\eta\$</span>, and and new log-partition function <span class="math inline">\$B(\\zeta) = A(U'\\zeta) + \\zeta'v\$</span>. So “the” sufficient statistic of an exponential family is defined only up to invertible affine transformations.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Differential identities {.anchored anchor-id="differential-identities"} →](03-differential-identities-anchored-anchor-id-differential-iden.md)
