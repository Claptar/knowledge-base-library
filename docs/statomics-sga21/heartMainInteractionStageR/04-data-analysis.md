---
title: Data Analysis
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.Rmd
source_file: sources/statomics-sga21/heartMainInteractionStageR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Analysis

**Source:** [`heartMainInteractionStageR.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Estimation

We model the protein level expression values using `msqrob`.
By default `msqrob2` estimates the model parameters using robust regression.

```r
pe <- msqrob(
  object = pe,
  i = "proteinRobust",
  formula = ~ location*tissue + patient)
```

## Inference

Explore Design
```r
library(ExploreModelMatrix)
VisualizeDesign(colData(pe),~ location*tissue + patient)$plotlist
```


```r
design <- model.matrix(~location*tissue + patient, data = colData(pe))
L <- makeContrast(
  c(
    "tissueV = 0",
    "tissueV + locationR:tissueV = 0",
    "tissueV + 0.5*locationR:tissueV = 0","locationR:tissueV = 0"),
  parameterNames = colnames(design)
  )


pe <- hypothesisTest(object = pe, i = "proteinRobust", contrast = L, overwrite=TRUE)
```

## Evaluate results contrast $\log_2 FC_{V-A}^L$

### Volcano-plot


```r
volcanoLeft <- ggplot(rowData(pe[["proteinRobust"]])$"tissueV",
                 aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) + theme_minimal()
volcanoLeft
```


### Heatmap

We first select the names of the proteins that were declared signficant.

```r
sigNamesLeft <- rowData(pe[["proteinRobust"]])$tissueV %>%
 rownames_to_column("proteinRobust") %>%
 filter(adjPval<0.05) %>%
 pull(proteinRobust)
heatmap(assay(pe[["proteinRobust"]])[sigNamesLeft, ])
```

There are `r length(sigNamesLeft)` proteins significantly differentially expressed at the 5% FDR level.

```r
rowData(pe[["proteinRobust"]])$tissueV %>%
  cbind(.,rowData(pe[["proteinRobust"]])$Protein.names) %>%
  na.exclude %>%
  filter(adjPval<0.05) %>%
  arrange(pval)  %>%
  knitr::kable(.)
```

## Evaluate results contrast $\log_2 FC_{V-A}^R$

### Volcano-plot


```r
volcanoRight <- ggplot(rowData(pe[["proteinRobust"]])$"tissueV + locationR:tissueV",
                 aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) + theme_minimal()
volcanoRight
```


### Heatmap

We first select the names of the proteins that were declared signficant.

```r
sigNamesRight <- rowData(pe[["proteinRobust"]])$"tissueV + locationR:tissueV" %>%
 rownames_to_column("proteinRobust") %>%
 filter(adjPval<0.05) %>%
 pull(proteinRobust)
heatmap(assay(pe[["proteinRobust"]])[sigNamesRight, ])
```

There are `r length(sigNamesRight)` proteins significantly differentially expressed at the 5% FDR level.

```r
rowData(pe[["proteinRobust"]])$"tissueV + locationR:tissueV"  %>%
  cbind(.,rowData(pe[["proteinRobust"]])$Protein.names) %>%
  na.exclude %>%
  filter(adjPval<0.05) %>%
  arrange(pval) %>%
  knitr::kable(.)
```


## Evaluate results average contrast $\log_2 FC_{V-A}$

### Volcano-plot


```r
volcanoAvg <- ggplot(rowData(pe[["proteinRobust"]])$"tissueV + 0.5 * locationR:tissueV",
                 aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) + theme_minimal()
volcanoAvg
```


### Heatmap

We first select the names of the proteins that were declared signficant.

```r
sigNamesAvg <- rowData(pe[["proteinRobust"]])$"tissueV + 0.5 * locationR:tissueV" %>%
 rownames_to_column("proteinRobust") %>%
 filter(adjPval<0.05) %>%
 pull(proteinRobust)
heatmap(assay(pe[["proteinRobust"]])[sigNamesAvg, ])
```

There are `r length(sigNamesAvg)` proteins significantly differentially expressed at the 5% FDR level.

```r
rowData(pe[["proteinRobust"]])$"tissueV + 0.5 * locationR:tissueV" %>%
  cbind(.,rowData(pe[["proteinRobust"]])$Protein.names) %>%
  na.exclude %>%
  filter(adjPval<0.05) %>%
  arrange(pval) %>%
  knitr::kable(.)
```


## Interaction

### Volcano-plot


```r
volcanoInt <- ggplot(rowData(pe[["proteinRobust"]])$"locationR:tissueV",
                 aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) + theme_minimal()
volcanoInt
```

### Heatmap

There were no genes significant at the 5% FDR level.
We return the top 25 genes.

```r
sigNamesInt <- rowData(pe[["proteinRobust"]])$"locationR:tissueV" %>%
 rownames_to_column("proteinRobust") %>%
 filter(adjPval<0.05) %>%
 pull(proteinRobust)
hlp <- order((rowData(pe[["proteinRobust"]])$"locationR:tissueV")[,"adjPval"])[1:25]
heatmap(assay(pe[["proteinRobust"]])[hlp, ])
```

There are `r length(sigNamesInt)` proteins significantly differentially expressed at the 5% FDR level.

```r
rowData(pe[["proteinRobust"]])$"locationR:tissueV" %>%
  cbind(.,rowData(pe[["proteinRobust"]])$Protein.names) %>%
  na.exclude %>%
  filter(adjPval<0.05) %>%
  arrange(pval)
```

---

[← Preprocessing](03-preprocessing.md) · [Up: contents](index.md) · [Large difference in number of proteins that are returned →](05-large-difference-in-number-of-proteins-that-are-returned.md)
