---
title: Conditional probability {.anchored anchor-id="conditional-probability"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/probability.html
source_file: sources/berkeley-stat210a/fall-2025/reader/probability.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Conditional probability {.anchored anchor-id="conditional-probability"}

**Source:** [`reader/probability.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/probability.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

While it is beyond the scope of this course, measure theory also allows us to patch the definition of conditional probability and conditional expectation. Given two events <span class="math inline">\$A\$</span> and <span class="math inline">\$B\$</span>, if <span class="math inline">\$\\PP(B) &gt; 0\$</span>, we can unproblematically define the conditional probability of <span class="math inline">\$A\$</span> given <span class="math inline">\$B\$</span> as <span class="math inline">\$\\PP(A \\mid B) = \\PP(A \\cap B) / \\PP(B)\$</span>, but this definition obviously fails when <span class="math inline">\$\\PP(B) = 0\$</span>.

Generally speaking, we cannot necessarily define <span class="math inline">\$\\PP(A \\mid B)\$</span> for measure zero events <span class="math inline">\$B\$</span> (Homework 1 includes a problem illustrating the inherent ambiguity of this definition). But, for example, if <span class="math inline">\$X\$</span> and <span class="math inline">\$Y\$</span> are both continuous random variables with some dependence between them we would like to be able to discuss, e.g., the distribution or expectation of <span class="math inline">\$Y\$</span> given that <span class="math inline">\$X\$</span> takes on some specific value <span class="math inline">\$x\$</span>. We can do this by defining the conditional expectation <span class="math inline">\$\\EE(Y \\mid X)\$</span> as a *random variable* <span class="math inline">\$g(X)\$</span>, which has the property <span class="math inline">\$\\EE$$(Y - g(X)) 1\_A(X)$$ = 0\$</span> for all (nice) subsets <span class="math inline">\$A\$</span>. By evaluating this function <span class="math inline">\$g\$</span> at <span class="math inline">\$x\$</span> we can answer the question we asked earlier. However, note this explanation is informal and brushes many important points under the rug; for a more complete explanation, take Stat 205A.

Having defined the conditional expectation, we can also ask about the conditional distribution of <span class="math inline">\$Y\$</span> by evaluating the conditional expectation on new random variables defined with indicator functions: <span class="math inline">\$\\PP(Y \\in A \\mid X) = \\EE$$1\_A(Y) \\mid X$$\$</span> .

---

[← Probability Part 07 —](07-probability-part-07.md) · [Up: contents](index.md) · [Footnotes {#footnotes .anchored .quarto-appendix-heading} →](09-footnotes-footnotes-anchored-quarto-appendix-heading.md)
