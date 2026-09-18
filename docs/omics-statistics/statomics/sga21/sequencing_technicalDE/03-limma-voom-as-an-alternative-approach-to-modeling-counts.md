---
title: limma-voom as an alternative approach to modeling counts
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# limma-voom as an alternative approach to modeling counts

`limma` is a powerful linear model based framework for modeling microarray gene expression data and inferring differential expression results, and has been introduced in the proteomics module of this course. With the inception of RNA-seq, the `limma` developers got creative and extended their framework to also model count data, hence creating limma-voom.

## The limma framework for the analysis of microarrays

In the proteomics module, we have previously introduced the powerful linear model based framework `limma`, and how it uses an empirical Bayes strategy to borrow information across proteins to derive a posterior variance estimate. In its default implementation, `limma` cannot be used to model count data, as it can not account for their mean-variance relationship. The developers, however, came up with a creative approach to use the `limma` framework to model count data.

## limma-voom: extending limma for RNA-seq data

 - Count models such as `edgeR` and `DESeq2` automatically account for the mean-variance relationship of the data by assuming a proper count distribution, given that the observed mean-variance relationship is close to the one assumed by the distribution. However, they are also more complex, both computationally as well as statistically and conceptually.
 - limma-voom ([Law *et al.* (2014)](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2014-15-2-r29)) is a method that unlocks Gaussian linear models to analyze count data in the context of RNA-seq, by first estimating the mean-variance relationship of the dataset at hand, and subsequently incorporating it in the analysis through observation-level weights in a linear regression model.

```r
# All defaults
include_graphics("./images_sequencing/limmaVoomMeanVariance.png")
```

 ---

 - The mean-variance relationship is dataset-specific and needs to be estimated separately for each dataset.
 - The mean-variance trend is estimated nonparametrically across all genes, using a global mean and variance for each gene. Using this trend, observation-level variances are estimated for each individual observation.
 - These observation-level variances are then used as inverse weights in the linear modeling framework, to account for heteroscedasticity.

```r
# All defaults
include_graphics("./images_sequencing/limmaVoomWeights.png")
```

## limma-voom analysis of parathyroid data

`limma` has an extensive user's guide which can be accessed via `limma::limmaUsersGuide()`.

```r
library(limma)
library(edgeR)
se <- readRDS("data/seParathyroid.rds")
se
design <- model.matrix(~treatment*time+patient,
                       data=colData(se))

keep <- filterByExpr(se, design)
table(keep)
filtCounts <- assays(se)$counts[keep,]

dge <- DGEList(counts=filtCounts)

# normalize just as in edgeR
dge <- calcNormFactors(dge)
# fit the mean-variance trend used to calculate weights
v <- voom(dge, design, plot=TRUE)
# this mean-variance trend is then automatically incorporated into the usual limma pipeline
fit <- lmFit(v, design)
fit <- eBayes(fit)
tt <- topTable(fit, coef=(ncol(design-1):ncol(design)), number=nrow(dge)) # test interaction effects
head(tt) #similar as in edgeR, we find no DE
```

### Testing contrasts using limma-voom

When working with limma-voom, we cannot immediately test a contrast using a contrast matrix just like we did in `edgeR`.
Instead, we will reparametrize our model according to the contrasts, such that each parameter corresponds to a specific contrast, using the `contrasts.fit` function.

```r
# contrast matrix we used before
L <- matrix(0, nrow = ncol(fit$coefficients), ncol = 7)
rownames(L) <- colnames(fit$coefficients)
colnames(L) <- c("DPNvsCON24", "DPNvsCON48",
                 "OHTvsCON24", "OHTvsCON48",
                 "DPNvsCONInt", "OHTvsCONInt",
                 "OHTvsDPNInt")
# DPN vs control at 24h
L[2,"DPNvsCON24"] <- 1
# DPN vs control at 48h
L[c(2,8),"DPNvsCON48"] <- 1
# OHT vs control at 24h
L[3,"OHTvsCON24"] <- 1
# OHT vs control at 48h
L[c(3,9),"OHTvsCON48"] <- 1
# DPN control interaction
L[8,"DPNvsCONInt"] <- 1
# OHT control interaction
L[9,"OHTvsCONInt"] <- 1
# OHT DPN interaction
L[c(9,8),"OHTvsDPNInt"] <- c(1, -1)
L

fit <- lmFit(v, design)
fit2 <- contrasts.fit(fit, L)
fit2 <- eBayes(fit2)
head(fit2$coefficients) # one coefficient is one contrast
# loop over all contrasts of interest
ttList <- list()
for(cc in 1:ncol(L)){
  ttList[[cc]] <- topTable(fit2, coef=cc, number=nrow(dge))
}
names(ttList) <- colnames(L)
nDE <- unlist(lapply(ttList, function(x) sum(x$adj.P.Val <= 0.05)))
nDE
```

---

[← Aliasing](02-aliasing.md) · [Up: contents](index.md)
