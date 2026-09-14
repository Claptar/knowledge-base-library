---
title: No offset
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd
source_file: sources/statomics-sga21/sequencing_scalingNormalization.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# No offset

**Source:** [`sequencing_scalingNormalization.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

The gene is extremely significantly DE between groups.

```r
set.seed(65)
nPerGroup <- 8
y <- c(rpois(n=nPerGroup, lambda = 7),
       rpois(n=nPerGroup, lambda = 11))
group <- rep(1:2, each = nPerGroup)
plot(group, y)

---

[Up: contents](index.md) · [Poisson GLM, no library size: signifcantly DE →](02-poisson-glm-no-library-size-signifcantly-de.md)
