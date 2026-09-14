---
title: 'Subset of CPTAC study: A vs B comparison in lab 3'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.Rmd
source_file: sources/statomics-sga21/pda_robustSummarisation_peptideModels.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Subset of CPTAC study: A vs B comparison in lab 3

**Source:** [`pda_robustSummarisation_peptideModels.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## LFQ

<details><summary> Click to see background and code </summary><p>
1. Import data
```r
proteinsFile <- "https://raw.githubusercontent.com/statOmics/PDA21/data/quantification/cptacAvsB_lab3/proteinGroups.txt"

ecols <- grep("LFQ\\.intensity\\.", names(read.delim(proteinsFile)))

peLFQ <- readQFeatures(
  table = proteinsFile, fnames = 1, ecol = ecols,
  name = "proteinRaw", sep = "\t"
)

cond <- which(
  strsplit(colnames(peLFQ)[[1]][1], split = "")[[1]] == "A") # find where condition is stored

colData(peLFQ)$condition <- substr(colnames(peLFQ), cond, cond) %>%
  unlist %>%
  as.factor
```

2. Preprocessing

```r
rowData(peLFQ[["proteinRaw"]])$nNonZero <- rowSums(assay(peLFQ[["proteinRaw"]]) > 0)

peLFQ <- zeroIsNA(peLFQ, "proteinRaw") # convert 0 to NA

peLFQ <- logTransform(peLFQ, base = 2, i = "proteinRaw", name = "proteinLog")

peLFQ <- filterFeatures(peLFQ,~ Reverse != "+")
peLFQ <- filterFeatures(peLFQ,~ Potential.contaminant != "+")

peLFQ <- normalize(peLFQ,
                i = "proteinLog",
                name = "protein",
                method = "center.median")
```

3. Modeling and Inference

```r
peLFQ <- msqrob(object = peLFQ, i = "protein", formula = ~condition)

L <- makeContrast("conditionB=0", parameterNames = c("conditionB"))
peLFQ <- hypothesisTest(object = peLFQ, i = "protein", contrast = L)

volcanoLFQ <- ggplot(rowData(peLFQ[["protein"]])$conditionB,
                  aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
  geom_point(cex = 2.5) +
  scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
  theme_minimal() +
  ggtitle(paste0("maxLFQ: TP = ",sum(rowData(peLFQ[["protein"]])$conditionB$adjPval<0.05&grepl(rownames(rowData(peLFQ[["protein"]])$conditionB),pattern ="UPS"),na.rm=TRUE), " FP = ", sum(rowData(peLFQ[["protein"]])$conditionB$adjPval<0.05&!grepl(rownames(rowData(peLFQ[["protein"]])$conditionB),pattern ="UPS"),na.rm=TRUE)))
```


</p></details>

## Median & robust summarization

<details><summary> Click to see background and code </summary><p>

1. Import Data

```r
peptidesFile <- "https://raw.githubusercontent.com/statOmics/SGA2020/data/quantification/cptacAvsB_lab3/peptides.txt"

ecols <- grep(
  "Intensity\\.",
  names(read.delim(peptidesFile))
  )

pe <- readQFeatures(
  table = peptidesFile,
  fnames = 1,
  ecol = ecols,
  name = "peptideRaw", sep="\t")

cond <- which(
  strsplit(colnames(pe)[[1]][1], split = "")[[1]] == "A") # find where condition is stored

colData(pe)$condition <- substr(colnames(pe), cond, cond) %>%
  unlist %>%
  as.factor
```

2. Preprocessing

```r
rowData(pe[["peptideRaw"]])$nNonZero <- rowSums(assay(pe[["peptideRaw"]]) > 0)

pe <- zeroIsNA(pe, "peptideRaw") # convert 0 to NA

pe <- logTransform(pe, base = 2, i = "peptideRaw", name = "peptideLog")

pe <- filterFeatures(pe, ~ Proteins %in% smallestUniqueGroups(rowData(pe[["peptideLog"]])$Proteins))

pe <- filterFeatures(pe,~Reverse != "+")
pe <- filterFeatures(pe,~ Potential.contaminant != "+")

pe <- filterFeatures(pe,~ nNonZero >=2)
nrow(pe[["peptideLog"]])

pe <- normalize(pe,
                i = "peptideLog",
                name = "peptideNorm",
                method = "center.median")

pe <- aggregateFeatures(pe,
  i = "peptideNorm",
  fcol = "Proteins",
  na.rm = TRUE,
  name = "proteinMedian",
  fun = matrixStats::colMedians)

pe <- aggregateFeatures(pe,
  i = "peptideNorm",
  fcol = "Proteins",
  na.rm = TRUE,
  name = "proteinRobust")
```

3. Modeling and inference

```r
pe <- msqrob(object = pe, i = "proteinMedian", formula = ~condition)
L <- makeContrast("conditionB=0", parameterNames = c("conditionB"))
pe <- hypothesisTest(object = pe, i = "proteinMedian", contrast = L)

pe <- msqrob(object = pe, i = "proteinRobust", formula = ~condition)
pe <- hypothesisTest(object = pe, i = "proteinRobust", contrast = L)

volcanoMedian <- ggplot(rowData(pe[["proteinMedian"]])$conditionB,
                  aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
  geom_point(cex = 2.5) +
  scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
  theme_minimal() +
  ggtitle(paste0("Median: TP = ",sum(rowData(pe[["proteinMedian"]])$conditionB$adjPval<0.05&grepl(rownames(rowData(pe[["proteinMedian"]])$conditionB),pattern ="UPS"),na.rm=TRUE), " FP = ", sum(rowData(pe[["proteinMedian"]])$conditionB$adjPval<0.05&!grepl(rownames(rowData(pe[["proteinMedian"]])$conditionB),pattern ="UPS"),na.rm=TRUE)))

volcanoRobust<- ggplot(rowData(pe[["proteinRobust"]])$conditionB,
                  aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
  geom_point(cex = 2.5) +
  scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
  theme_minimal() +
  ggtitle(paste0("Robust: TP = ",sum(rowData(pe[["proteinRobust"]])$conditionB$adjPval<0.05&grepl(rownames(rowData(pe[["proteinRobust"]])$conditionB),pattern ="UPS"),na.rm=TRUE), " FP = ", sum(rowData(pe[["proteinRobust"]])$conditionB$adjPval<0.05&!grepl(rownames(rowData(pe[["proteinRobust"]])$conditionB),pattern ="UPS"),na.rm=TRUE)))
```

```r
ylims <- c(0,
           ceiling(max(c(-log10(rowData(peLFQ[["protein"]])$conditionB$pval),
               -log10(rowData(pe[["proteinMedian"]])$conditionB$pval),
               -log10(rowData(pe[["proteinRobust"]])$conditionB$pval)),
               na.rm=TRUE))
)

xlims <- max(abs(c(rowData(peLFQ[["protein"]])$conditionB$logFC,
               rowData(pe[["proteinMedian"]])$conditionB$logFC,
               rowData(pe[["proteinRobust"]])$conditionB$logFC)),
               na.rm=TRUE) * c(-1,1)
```

```r
compBoxPlot <- rbind(rowData(peLFQ[["protein"]])$conditionB %>% mutate(method="maxLFQ") %>% rownames_to_column(var="protein"),
      rowData(pe[["proteinMedian"]])$conditionB %>% mutate(method="median")%>% rownames_to_column(var="protein"),
      rowData(pe[["proteinRobust"]])$conditionB%>% mutate(method="robust")%>% rownames_to_column(var="protein")) %>%
      mutate(ups= grepl(protein,pattern="UPS")) %>%
    ggplot(aes(x = method, y = logFC, fill = ups)) +
    geom_boxplot() +
    geom_hline(yintercept = log2(0.74 / .25), color = "#00BFC4") +
    geom_hline(yintercept = 0, color = "#F8766D")

```

</p></details>

## Comparison summarization methods

```r
grid.arrange(volcanoLFQ + xlim(xlims) + ylim(ylims),
             volcanoMedian + xlim(xlims) + ylim(ylims),
             volcanoRobust + xlim(xlims) + ylim(ylims),
             ncol=1)
```

- Robust summarization: highest power and still good FDR control: $FDP = \frac{1}{20} = 0.05$.


```r
compBoxPlot
```

- Median: biased logFC estimates for spike-in proteins
- maxLFQ: more variable logFC estiamtes for spike-in proteins

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Full CPTAC study →](03-full-cptac-study.md)
