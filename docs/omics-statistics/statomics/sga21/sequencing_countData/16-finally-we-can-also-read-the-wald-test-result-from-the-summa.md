---
title: finally, we can also read the Wald test result from the summary of the model
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# finally, we can also read the Wald test result from the summary of the model

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

summSimple
```

```r
mFull <- glm(bikers ~ workingday,
               family = "poisson",
               data = Bikeshare)

mReduced <- glm(bikers ~ 1,
               family = "poisson",
               data = Bikeshare)

---

[← note this being equal to](15-note-this-being-equal-to.md) · [Up: contents](index.md) · [manual LRT →](17-manual-lrt.md)
