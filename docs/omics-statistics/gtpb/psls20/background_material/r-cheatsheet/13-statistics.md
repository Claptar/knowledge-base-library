---
title: Statistics
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/r-cheatsheet.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Statistics

**Source:** [`background_material/r-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

`lm(x ~ y, data=df)` Linear model.

```
prop.test
```

`t.test(x, y)` Preform a t-test for difference between means.

Test for a difference between proportions.

`glm(x ~ y, data=df)` Generalised linear model.

`pairwise.t.test` Preform a t-test for paired data.

`summary` Get more detailed information out a model.

`aov` Analysis of variance.

---

[← Factors](12-factors.md) · [Up: contents](index.md) · [Distributions →](14-distributions.md)
