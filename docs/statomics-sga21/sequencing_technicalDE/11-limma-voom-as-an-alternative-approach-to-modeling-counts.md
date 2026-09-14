---
title: limma-voom as an alternative approach to modeling counts
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# limma-voom as an alternative approach to modeling counts

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

`limma` is a powerful linear model based framework for modeling microarray gene expression data and inferring differential expression results, and has been introduced in the proteomics module of this course. With the inception of RNA-seq, the `limma` developers got creative and extended their framework to also model count data, hence creating limma-voom.

## The limma framework for the analysis of microarrays

In the proteomics module, we have previously introduced the powerful linear model based framework `limma`, and how it uses an empirical Bayes strategy to borrow information across proteins to derive a posterior variance estimate. In its default implementation, `limma` cannot be used to model count data, as it can not account for their mean-variance relationship. The developers, however, came up with a creative approach to use the `limma` framework to model count data.

## limma-voom: extending limma for RNA-seq data

 - Count models such as `edgeR` and `DESeq2` automatically account for the mean-variance relationship of the data by assuming a proper count distribution, given that the observed mean-variance relationship is close to the one assumed by the distribution. However, they are also more complex, both computationally as well as statistically and conceptually.
 - limma-voom ([Law *et al.* (2014)](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2014-15-2-r29)) is a method that unlocks Gaussian linear models to analyze count data in the context of RNA-seq, by first estimating the mean-variance relationship of the dataset at hand, and subsequently incorporating it in the analysis through observation-level weights in a linear regression model.

```r

---

[← one before and one after sample for each](10-one-before-and-one-after-sample-for-each.md) · [Up: contents](index.md) · [All defaults →](12-all-defaults.md)
