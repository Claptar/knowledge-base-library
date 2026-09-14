---
title: 4 Permutation Tests {.anchored number="4" anchor-id="permutation-tests"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-nuisance.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Permutation Tests {.anchored number="4" anchor-id="permutation-tests"}

**Source:** [`units/reader/testing-nuisance.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Even if we don’t get a UMPU test at the end, conditioning on null suff. stat. still helps

Example: <span class="math inline">\$X\_1, \\ldots, X\_n \\sim \\text{iid } P\$</span>, <span class="math inline">\$Y\_1, \\ldots, Y\_m \\sim \\text{iid } Q\$</span> <span class="math inline">\$H\_0: P=Q\$</span> vs <span class="math inline">\$H\_1: P \\neq Q\$</span>

Under <span class="math inline">\$H\_0\$</span>: <span class="math inline">\$P=Q\$</span>, <span class="math inline">\$X\_1, \\ldots, X\_n, Y\_1, \\ldots, Y\_m \\sim P\$</span>

Let <span class="math inline">\$Z = (Z\_1, \\ldots, Z\_{n+m}) = (X\_1, \\ldots, X\_n, Y\_1, \\ldots, Y\_m)\$</span>

Under <span class="math inline">\$H\_0\$</span>, <span class="math inline">\$U = Z\$</span> is complete sufficient

Let <span class="math inline">\$S\_{n+m}\$</span> = Permutations on <span class="math inline">\$n+m\$</span> elements

<span class="math inline">\$(X, Y) = (U\_{\\pi(1)}, \\ldots, U\_{\\pi(n+m)})\$</span> for <span class="math inline">\$\\pi \\in S\_{n+m}\$</span>

Thus for test stat <span class="math inline">\$T\$</span>, if <span class="math inline">\$P=Q\$</span>:

<span class="math display">\\$$\\mathbb{P}(T \\geq t \| U) = \\frac{1}{(n+m)!}\\sum\_{\\pi \\in S\_{n+m}} 1\\{T(Z\_{\\pi(1)}, \\ldots, Z\_{\\pi(n+m)}) \\geq t\\}\\$$</span>

Monte Carlo test: In practice, we sample \$\_1, , \_B

---

[← 3 Proof Sketch {.anchored number="3" anchor-id="proof-sketch"}](04-3-proof-sketch-anchored-number-3-anchor-id-proof-sketch.md) · [Up: contents](index.md)
