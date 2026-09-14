---
title: 7 Benjamini-Hochberg Procedure
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 7 Benjamini-Hochberg Procedure

**Source:** [`reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/multiple-testing.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

B-H also proposed a method to control FDR given ordered p-values <span class="math inline">\$p\_{(1)} \\leq p\_{(2)} \\leq \\cdots \\leq p\_{(m)}\$</span>:

<span class="math inline">\$R(X) = \\max\\{r: p\_{(r)} \\leq \\alpha r/m\\}\$</span> (called step-up procedure)

Reject <span class="math inline">\$H\_{0(1)},\\ldots,H\_{0(R)}\$</span>

This is much more liberal than Bonferroni procedure: When <span class="math inline">\$\\alpha = 0.05\$</span>, B-H rejects at least <span class="math inline">\$r\$</span> p-values if <span class="math inline">\$p\_{(r)} \\leq 0.05r/m\$</span>

### <span class="header-section-number">7.1</span> B-H as Empirical Bayes {.anchored number="7.1" anchor-id="b-h-as-empirical-bayes"}

Equivalent formulation for <span class="math inline">\$R(t) = \\#\\{p\_i \\leq t\\}\$</span>: Let <span class="math inline">\$\\hat{F}(t) = R(t)/m\$</span> = estimate of CDF of p-values

B-H rejects <span class="math inline">\$H\_i\$</span> if <span class="math inline">\$p\_i \\leq T(X) = \\max\\{t: \\hat{F}(t) \\geq t/\\alpha\\}\$</span>

When <span class="math inline">\$\\hat{F}(t)\$</span> is continuously increasing in <span class="math inline">\$t\$</span> except at jump values where it jumps down:

<span class="math inline">\$\\hat{F}(T(X)) = T(X)/\\alpha\$</span>

$$Insert graph showing <span class="math inline">\$\\hat{F}(t)\$</span> vs <span class="math inline">\$t/\\alpha\$</span>$$

Only values of <span class="math inline">\$t\$</span> that matter for the algorithm are <span class="math inline">\$t = p\_i\$</span> where <span class="math inline">\$\\hat{F}(t) = t/\\alpha\$</span>, i.e., <span class="math inline">\$\\alpha i/m = p\_{(i)}\$</span>

---

[← 6 False Discovery Rate (FDR)](07-6-false-discovery-rate-fdr.md) · [Up: contents](index.md) · [8 FDR Control →](09-8-fdr-control.md)
