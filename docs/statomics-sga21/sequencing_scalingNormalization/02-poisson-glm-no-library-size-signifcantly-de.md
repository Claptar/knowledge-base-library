---
title: 'Poisson GLM, no library size: signifcantly DE'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd
source_file: sources/statomics-sga21/sequencing_scalingNormalization.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Poisson GLM, no library size: signifcantly DE

**Source:** [`sequencing_scalingNormalization.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

m <- glm(y ~ factor(group),
         family = "poisson")
summary(m)
```

---

[← No offset](01-no-offset.md) · [Up: contents](index.md) · [Library size offset →](03-library-size-offset.md)
