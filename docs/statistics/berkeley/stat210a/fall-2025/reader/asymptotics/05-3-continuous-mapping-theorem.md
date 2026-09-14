---
title: 3 Continuous Mapping Theorem
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/asymptotics.html
source_file: sources/berkeley-stat210a/fall-2025/reader/asymptotics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Continuous Mapping Theorem

**Source:** [`reader/asymptotics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/asymptotics.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Theorem (Continuous Mapping): Let <span class="math inline">\$g\$</span> be continuous, <span class="math inline">\$X\_n, X\$</span> r.v.’s.

1.  If <span class="math inline">\$X\_n \\xrightarrow{d} X\$</span>, then <span class="math inline">\$g(X\_n) \\xrightarrow{d} g(X)\$</span>
2.  If <span class="math inline">\$X\_n \\xrightarrow{p} c\$</span>, then <span class="math inline">\$g(X\_n) \\xrightarrow{p} g(c)\$</span>

Proof: <span class="math inline">\$f\$</span> bounded continuous <span class="math inline">\$\\implies f \\circ g\$</span> bounded continuous If <span class="math inline">\$X\_n \\xrightarrow{d} X\$</span>, then <span class="math inline">\$\\mathbb{E}$$f(g(X\_n))$$ \\to \\mathbb{E}$$f(g(X))$$\$</span> <span class="math inline">\$X\_n \\xrightarrow{p} c\$</span> special case with <span class="math inline">\$X \\equiv c\$</span>

---

[← 2 Convergence](04-2-convergence.md) · [Up: contents](index.md) · [4 Slutsky’s Theorem →](06-4-slutsky-s-theorem.md)
