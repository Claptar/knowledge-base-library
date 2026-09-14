---
title: How to report?
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference-twosampleT.Rmd
source_file: sources/gtpb-psls20/theory/05-statisticalInference-twosampleT.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# How to report?

**Source:** [`theory/05-statisticalInference-twosampleT.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference-twosampleT.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- In the scientific literature there is too much attention for p-values

- It is much more informative to combine an estimate with its confidence interval.

**Rule of thumb**:

Report an estimate together with its  confidence interval (and its p-value)

1. The result of the test can be derived of the confidence interval
2. It allows the reader to judge **scientific relevance**.

```r
t.test(rel~trt,data=ap)
```

The result of an $\alpha$-level t-test is equivalent with comparing the effect size under $H_0$ with the $1-\alpha$ CI.

An effect can be extremely statistically significant, but scientifically irrelevant. With a CI you will spot this.


---

---

[← Assumptions](03-assumptions.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) {-} →](05-home-https-gtpb-github-io-psls20.md)
