---
title: Testing one parameter Part 02 —
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-one-parameter.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-one-parameter.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Testing one parameter Part 02 —

**Source:** [`units/reader/testing-one-parameter.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-one-parameter.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

This lecture concerns the general problem of testing with one real parameter. We observe <span class="math inline">\$X \\sim P\_\\theta\$</span> for <span class="math inline">\$\\theta \\in \\Theta \\subseteq \\RR\$</span>, and we might want to test a *one-sided alternative* like <span class="math inline">\$H\_0:\\; \\theta \\leq \\theta\_0\$</span> vs the one-sided alternative <span class="math inline">\$H\_1:\\; \\theta &gt; \\theta\_0\$</span>, or a *point null* hypothesis like <span class="math inline">\$H\_0:\\; \\theta = \\theta\_0\$</span> against a *two-sided alternative* <span class="math inline">\$H\_1:\\; \\theta \\neq \\theta\_0\$</span>. Or, we could test an *interval null* <span class="math inline">\$H\_0:\\; \|\\theta - \\theta\_0\| \\leq \\delta\$</span> vs the two-sided alternative <span class="math inline">\$H\_1:\\; \|\\theta-\\theta\_0\|&gt;\\delta\$</span>, for <span class="math inline">\$\\delta \\geq 0\$</span> (which reduces to the point null if <span class="math inline">\$\\delta = 0\$</span>).

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 One-sided testing {.anchored number="2" anchor-id="one-sided-testing"} →](03-2-one-sided-testing-anchored-number-2-anchor-id-one-sided-te.md)
