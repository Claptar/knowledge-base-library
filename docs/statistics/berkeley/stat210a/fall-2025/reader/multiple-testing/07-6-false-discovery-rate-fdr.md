---
title: 6 False Discovery Rate (FDR)
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 6 False Discovery Rate (FDR)

**Source:** [`reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/multiple-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Problem: With 10K independent test statistics, all at level <span class="math inline">\$\\alpha = 0.001\$</span>, we expect 10 rejections just by chance. What if we get 50? Probably only ~20 of them are false rejections.

Can we accept 10 false rejections as long as most rejections are valid?

Benjamini-Hochberg (1995) proposed a more liberal error control criterion called FDR:

<span class="math inline">\$R(X) = \|R(X)\|\$</span> = rejections (“discoveries”) <span class="math inline">\$V(X) = \|R(X) \\cap H\_{0c}\|\$</span> = false discoveries

The FDP is: <span class="math inline">\$\\text{FDP} = \\begin{cases} V(X)/R(X) & \\text{if } R(X) &gt; 0 \\\\ 0 & \\text{if } R(X) = 0 \\end{cases}\$</span>

The FDR is <span class="math inline">\$\\mathbb{E}$$\\text{FDP}$$\$</span>

---

[← 5 Deduced Inference](06-5-deduced-inference.md) · [Up: contents](index.md) · [7 Benjamini-Hochberg Procedure →](08-7-benjamini-hochberg-procedure.md)
