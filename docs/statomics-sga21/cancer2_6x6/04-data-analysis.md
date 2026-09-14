---
title: Data Analysis
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd
source_file: sources/statomics-sga21/cancer2_6x6.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Analysis

**Source:** [`cancer2_6x6.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Estimation

We model the protein level expression values using `msqrob`.
By default `msqrob2` estimates the model parameters using robust regression.

```r
pe <- msqrob(object = pe, i = "proteinRobust", formula = ~outcome)
```

## Inference

First, we extract the parameter names of the model.
```r
getCoef(rowData(pe[["proteinRobust"]])$msqrobModels[[1]])
```

Contrast?

```r
library(ExploreModelMatrix)
VisualizeDesign(colData(pe),~outcome)$plotlist[[1]]
```

The mean log2 expression for samples from outcome B is '(Intercept)+outcomePD'.
Hence, the average log2 fold change between outcome b and
outcome a is modelled using the parameter 'outcomePD'.
Thus, we assess the contrast 'outcomePD=0' with our statistical test.

```r
L <- makeContrast("outcomePD = 0", parameterNames = c("outcomePD"))
pe <- hypothesisTest(object = pe, i = "proteinRobust", contrast = L)
```

## Plots

### Volcano-plot


```r
volcano <- ggplot(rowData(pe[["proteinRobust"]])$outcomePD,
                 aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) + theme_minimal()
volcano
```

### Heatmap

We first select the names of the proteins that were declared signficant.

```r
sigNames <- rowData(pe[["proteinRobust"]])$outcomePD %>%
 rownames_to_column("proteinRobust") %>%
 filter(adjPval<0.05) %>%
 pull(proteinRobust)
heatmap(assay(pe[["proteinRobust"]])[sigNames, ])
```

There are `r length(sigNames)` proteins significantly differentially expressed at the 5% FDR level.

### Detail plots

We first extract the normalized peptideRaw expression values for a particular protein.


```r
for (protName in sigNames[1:5])
{
pePlot <- pe[protName, , c("peptideNorm","proteinRobust")]
pePlotDf <- data.frame(longFormat(pePlot))
pePlotDf$assay <- factor(pePlotDf$assay,
                       levels = c("peptideNorm", "proteinRobust"))
pePlotDf$outcome <- as.factor(colData(pePlot)[pePlotDf$colname, "outcome"])

---

[← Preprocessing](03-preprocessing.md) · [Up: contents](index.md) · [plotting →](05-plotting.md)
