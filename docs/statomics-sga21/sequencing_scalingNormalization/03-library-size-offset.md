---
title: Library size offset
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd
source_file: sources/statomics-sga21/sequencing_scalingNormalization.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Library size offset

**Source:** [`sequencing_scalingNormalization.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Since library sizes are different between groups, accounting for library size results in the gene no longer being DE at the 5% significance level. Not correcting for sequencing depth would thus result in spurious results.

```r

---

[← Poisson GLM, no library size: signifcantly DE](02-poisson-glm-no-library-size-signifcantly-de.md) · [Up: contents](index.md) · [Suppose library sizes are different between groups →](04-suppose-library-sizes-are-different-between-groups.md)
