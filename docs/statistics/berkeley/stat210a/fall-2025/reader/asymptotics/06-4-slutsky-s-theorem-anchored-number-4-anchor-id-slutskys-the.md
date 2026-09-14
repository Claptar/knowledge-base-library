---
title: 4 Slutsky’s Theorem {.anchored number="4" anchor-id="slutskys-theorem"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/asymptotics.html
source_file: sources/berkeley-stat210a/fall-2025/reader/asymptotics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 4 Slutsky’s Theorem {.anchored number="4" anchor-id="slutskys-theorem"}

**Source:** [`reader/asymptotics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/asymptotics.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Theorem (Slutsky): Assume <span class="math inline">\$X\_n \\xrightarrow{d} X\$</span>, <span class="math inline">\$Y\_n \\xrightarrow{p} c\$</span>. Then:

1.  <span class="math inline">\$X\_n + Y\_n \\xrightarrow{d} X + c\$</span>
2.  <span class="math inline">\$X\_n Y\_n \\xrightarrow{d} cX\$</span>
3.  <span class="math inline">\$X\_n / Y\_n \\xrightarrow{d} X/c\$</span> if <span class="math inline">\$c \\neq 0\$</span>

Proof: Show <span class="math inline">\$(X\_n, Y\_n) \\xrightarrow{d} (X, c)\$</span>, apply continuous mapping.

Wouldn’t normally be true that <span class="math inline">\$X\_n \\xrightarrow{d} X\$</span>, <span class="math inline">\$Y\_n \\xrightarrow{d} Y\$</span> implies <span class="math inline">\$X\_n + Y\_n \\xrightarrow{d} X + Y\$</span> without specifying joint dist.

---

[← 3 Continuous Mapping Theorem {.anchored number="3" anchor-id="continuous-mapping-theorem"}](05-3-continuous-mapping-theorem-anchored-number-3-anchor-id-con.md) · [Up: contents](index.md) · [5 Delta Method {.anchored number="5" anchor-id="delta-method"} →](07-5-delta-method-anchored-number-5-anchor-id-delta-method.md)
