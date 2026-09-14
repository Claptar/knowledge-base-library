---
title: Data Analysis
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_maxLFQ.Rmd
source_file: sources/statomics-sga21/cptac_maxLFQ.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Analysis

**Source:** [`cptac_maxLFQ.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_maxLFQ.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Estimation

We model the protein level expression values using `msqrob`.
By default `msqrob2` estimates the model parameters using robust regression.

We will model the data with a different group mean.
The group is incoded in the variable `condition` of the colData.
We can specify this model by using a formula with the factor condition as its predictor:
`formula = ~condition`.

Note, that a formula always starts with a symbol '~'.

```r
pe <- msqrob(object = pe, i = "protein", formula = ~condition)
```

## Inference

First, we extract the parameter names of the model by looking at the first model.
The models are stored in the row data of the assay under the default name msqrobModels.

```r
getCoef(rowData(pe[["protein"]])$msqrobModels[[1]])
```

We can also explore the design of the model that we specified using the the package `ExploreModelMatrix`

```r
library(ExploreModelMatrix)
VisualizeDesign(colData(pe),~condition)$plotlist[[1]]
```

Spike-in condition `A` is the reference class. So the mean log2 expression
for samples from condition A is '(Intercept).
The mean log2 expression for samples from condition B is '(Intercept)+conditionB'.
Hence, the average log2 fold change between condition b and
condition a is modelled using the parameter 'conditionB'.
Thus, we assess the contrast 'conditionB = 0' with our statistical test.

```r
L <- makeContrast("conditionB=0", parameterNames = c("conditionB"))
pe <- hypothesisTest(object = pe, i = "protein", contrast = L)
```


## Plots

### Volcano-plot


```r
volcano <- ggplot(rowData(pe[["protein"]])$conditionB,
                  aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
  geom_point(cex = 2.5) +
  scale_color_manual(values = alpha(c("black", "red"), 0.5)) + theme_minimal()
volcano
```

Note, that only `r sum(rowData(pe[["protein"]])$conditionB$adjPval < 0.05, na.rm = TRUE)` proteins are found to be differentially abundant.

### Heatmap

We first select the names of the proteins that were declared signficant.

```r
sigNames <- rowData(pe[["protein"]])$conditionB %>%
  rownames_to_column("protein") %>%
  filter(adjPval<0.05) %>%
  pull(protein)
heatmap(assay(pe[["protein"]])[sigNames, ])
```

The majority of the proteins are indeed UPS proteins.
1 yeast protein is returned.
Note, that the yeast protein indeed shows evidence for differential abundance.

### Boxplots

We make boxplot of the log2 FC and stratify according to the whether a protein is spiked or not.

```r
rowData(pe[["protein"]])$conditionB %>%
  rownames_to_column(var = "protein") %>%
  ggplot(aes(x=grepl("UPS",protein),y=logFC)) +
  geom_boxplot() +
  xlab("UPS") +
  geom_segment(
    x = 1.5,
    xend = 2.5,
    y = log2(0.74/0.25),
    yend = log2(0.74/0.25),
    colour="red") +
  geom_segment(
    x = 0.5,
    xend = 1.5,
    y = 0,
    yend = 0,
    colour="red") +
  annotate(
    "text",
    x = c(1,2),
    y = c(0,log2(0.74/0.25))+.1,
    label = c(
      "log2 FC Ecoli = 0",
      paste0("log2 FC UPS = ",round(log2(0.74/0.25),2))
      ),
    colour = "red")
```

What do you observe?

---

[← Preprocessing](03-preprocessing.md) · [Up: contents](index.md) · [Session Info →](05-session-info.md)
