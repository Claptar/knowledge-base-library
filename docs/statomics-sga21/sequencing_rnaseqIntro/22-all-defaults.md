---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/empiricalBayes.png")
```

The blog post on [understanding empirical Bayes estimation using baseball statistics](http://varianceexplained.org/r/empirical_bayes_baseball/) is a great primer for further reading, as well as the [accompanying book](https://drob.gumroad.com/l/empirical-bayes) by David Robinson.

## In practice

Let's fit the model using `edgeR`.

```r
design <- model.matrix(~ treatment*time + patient, data=colData(se))


dge <- calcNormFactors(se)
dge <- estimateDisp(dge, design) # estimate dispersion estimates
plotBCV(dge)
fit <- glmFit(dge, design)
head(fit$coefficients)


```

---

[← All defaults](21-all-defaults.md) · [Up: contents](index.md) · [Challenge IV: Statistical inference across many genes →](23-challenge-iv-statistical-inference-across-many-genes.md)
