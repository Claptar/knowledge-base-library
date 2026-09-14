---
title: 'Poisson GLM with library size offset: no longer significantly DE on 5% level.'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd
source_file: sources/statomics-sga21/sequencing_scalingNormalization.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Poisson GLM with library size offset: no longer significantly DE on 5% level.

**Source:** [`sequencing_scalingNormalization.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

m <- glm(y ~ factor(group) + offset(log(libSize)),
         family = "poisson")
summary(m)
```

---

[← Suppose library sizes are different between groups](04-suppose-library-sizes-are-different-between-groups.md) · [Up: contents](index.md) · [Scaling versus offsets →](06-scaling-versus-offsets.md)
