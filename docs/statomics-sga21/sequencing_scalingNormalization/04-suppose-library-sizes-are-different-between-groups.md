---
title: Suppose library sizes are different between groups
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd
source_file: sources/statomics-sga21/sequencing_scalingNormalization.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Suppose library sizes are different between groups

**Source:** [`sequencing_scalingNormalization.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

libSize <- c(rpois(n=nPerGroup, lambda = 1e5),
             rpois(n=nPerGroup, lambda = 1.5e5))

---

[← Library size offset](03-library-size-offset.md) · [Up: contents](index.md) · [Poisson GLM with library size offset: no longer significantly DE on 5% level. →](05-poisson-glm-with-library-size-offset-no-longer-significantly.md)
