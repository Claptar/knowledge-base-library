---
title: Large difference in number of proteins that are returned
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.Rmd
source_file: sources/statomics-sga21/heartMainInteractionStageR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Large difference in number of proteins that are returned

**Source:** [`heartMainInteractionStageR.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Note, that much more proteins are returned significant for average contrast ($\log_2 FC_{V-A}$) as compared to contrast for assessing the fold change between ventriculum and atrium left and right. The power for the average contrast is larger than for the contrast left or right because the log2 FC can be estimated with higher precision.

For none of the proteins the interaction was significant (change in log2 FC between ventriculum and atrium in the right vs the left heart region). The power for the interaction is typically low.

## Reason

Part of variance covariance matrix of model parameters due to design:

```r
X <- model.matrix(~ location*tissue + patient, colData(pe))
covarUnscaled <- solve(t(X) %*% X)
```

Variance of contrasts (diagonal elements) due to design
```r
varContrasts <- t(L)%*%covarUnscaled%*%L %>%
  diag
varContrasts
sqrt(varContrasts)
```

So it is clear that the standard error of the log2 FC left and right is the same.
That of the average contrast is a factor $\sqrt{2}$ smaller!
Indeed, we use double the number of samples to estimate it!

```r
varContrasts[3]/varContrasts[2]
sqrt(varContrasts)[3]/sqrt(varContrasts)[2]
1/sqrt(2)
```

The standard error of the interaction is a factor $\sqrt{2}$ larger than that of the main effects!
```r
varContrasts[4]/varContrasts[2]
sqrt(varContrasts)[4]/sqrt(varContrasts)[2]
sqrt(2)
```

## Msqrob

This is not the case for the standard errors of protein 2???

```r
rowData(pe[["proteinRobust"]])$"tissueV"[2,]
rowData(pe[["proteinRobust"]])$"tissueV + locationR:tissueV"[2,]
rowData(pe[["proteinRobust"]])$"tissueV + 0.5 * locationR:tissueV"[2,]
rowData(pe[["proteinRobust"]])$"locationR:tissueV"[2,]
```

Because msqrob is using robust regression to assess DE!

```r
pe %>%
  colData %>%
  as_tibble %>%
  mutate(w=getModel(rowData(pe[["proteinRobust"]])$msqrobModels[[2]])$w)
```

For protein 2 the samples at the left and right side have different weights!


### Part of standard error due to design:

```r
covUnscaledRobust <- solve(
  t(X) %*%
  diag(
    getModel(rowData(pe[["proteinRobust"]])$msqrobModels[[2]])$w) %*% X)

varContrastsRobust <- t(L)%*%covUnscaledRobust%*%L %>%
  diag
varContrastsRobust
sqrt(varContrastsRobust)
```

### Standard errors Contrasts

```r
sqrt(varContrastsRobust) * getSigmaPosterior(rowData(pe[["proteinRobust"]])$msqrobModels[[2]])
```

```r
rowData(pe[["proteinRobust"]])$"tissueV"[2,]
rowData(pe[["proteinRobust"]])$"tissueV + locationR:tissueV"[2,]
rowData(pe[["proteinRobust"]])$"tissueV + 0.5 * locationR:tissueV"[2,]
rowData(pe[["proteinRobust"]])$"locationR:tissueV"[2,]
```


## Stagewise testing

[stageR paper](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-017-1277-0)

### Omnibus test

```r
source("https://raw.githubusercontent.com/statOmics/SGA2020/gh-pages/assets/topFeaturesOmnibus.R")
pe <- omnibusTest(pe, "proteinRobust", L)
```

### Heatmap significant proteins Omnibus test

We first select the names of the proteins that were declared signficant.

```r
sigNamesOmnibus <- rowData(pe[["proteinRobust"]])$omnibusTest %>%
 rownames_to_column("proteinRobust") %>%
 filter(adjPval<0.05) %>%
 pull(proteinRobust)
heatmap(assay(pe[["proteinRobust"]])[sigNamesOmnibus, ])
```

There are `r length(sigNamesOmnibus)` proteins significantly differentially expressed at the 5% FDR level.

```r
rowData(pe[["proteinRobust"]])$omnibusTest  %>%
  cbind(.,rowData(pe[["proteinRobust"]])$Protein.names) %>%
  na.exclude %>%
  filter(adjPval<0.05) %>%
  arrange(pval) %>%
  knitr::kable(.)
```

### Confirmation stage


```r
library(stageR)
pAll <- sapply(
  c("omnibusTest",
    "tissueV",
    "tissueV + locationR:tissueV",
    "tissueV + 0.5 * locationR:tissueV",
    "locationR:tissueV"),
    function(name,assay)
      pull(rowData(assay)[,name],"pval"),
  assay = pe[["proteinRobust"]])
rownames(pAll) <- rownames(pe[["proteinRobust"]])

stageWiseAnalysis <- stageR(pAll[,1], pAll[,-1])
stageWiseAnalysis <- stageWiseAdjustment(stageWiseAnalysis, method = "holm", alpha = 0.05, allowNA = TRUE)

rowData(pe[["proteinRobust"]])$stageWiseAnalysis <- data.frame(pAll)
rowData(pe[["proteinRobust"]])$stageWiseAnalysis[] <- NA
rowData(pe[["proteinRobust"]])$stageWiseAnalysis[getPScreen(stageWiseAnalysis) %>% is.na %>% `!`,] <- getAdjustedPValues(stageWiseAnalysis, onlySignificantGenes=FALSE, order=FALSE)
```

```r
sigNamesStageWise <- apply(rowData(pe[["proteinRobust"]])$stageWiseAnalysis, 2, function(x) (x < 0.05) %>% which %>% names)

sapply(sigNamesStageWise,length)

for (i in 1:length(sigNamesStageWise))
heatmap(assay(pe[["proteinRobust"]])[sigNamesStageWise[[i]], ], main=names(sigNamesStageWise)[i])
```

## Confirmation improved

Instead of the Holm correction, we can use a better correction for this specific design in the confirmation stage.
If we pass the screening stage we know that at least one null hypothesis related to the contrasts is false.
If this is not the case we have made an false positive conclusion, but the multiple testing correction in the screening stage already accounts for that.

In the confirmation stage we have to correct for the maximum number of hypotheses that we can falsely reject.
The omnibus hypothesis test essentially tests the overall null hypothesis that the log2 protein abundance is on average equal between atrium and ventriculum both in the left and right heart region.
This involves testing simultaneously two model parameters: the main effect for ventriculum and the ventriculum:location interaction.
All our hypotheses are based on these two model parameters, so the tests are not independent.
The following configurations can occur:
- None of the model parameters differ from zero, in which we can falsely reject all hypotheses. However, we already corrected for that in the screening stage!
- If only the main ventriculum effect differs from zero, we know that the average log2 fold change between  atrium and ventriculum left, right and overall differ from zero. So we falsely reject at most one null hypothesis, i.e. the interaction.
- If only interaction differs from zero, only the null hypothesis related to log2 fold change in the left heart region can be falsely rejected.
- If both the main effect and the interaction differ from zero it is possible that
    - the interaction is as large in magnitude as the main effect but opposite in sign. This would mean that the log2 fold change in the right heart region is zero, which we can falsely reject.
    - the interaction effect is twice as large in magnitude as the main effect but opposite in sign. This would mean that the log2 fold change in left and right side are equal in size but opposite in sign, implying that contrast that averages over the average log2 fold changes left and right would be zeor, which we could falsely reject
    - all effects are true.

Hence, as soon as we enter the confirmation stage that we can at maximum make one false rejection so for this design and for our hypotheses of interest we do not have to correct for multiple testing in the second stage because we only have to account for the fact that we can at most make one false rejection.

So we can set the ```method="none"```
```r
stageWiseAnalysis <- stageWiseAdjustment(stageWiseAnalysis, method = "none", alpha = 0.05, allowNA = TRUE)

rowData(pe[["proteinRobust"]])$stageWiseAnalysis <- data.frame(pAll)
rowData(pe[["proteinRobust"]])$stageWiseAnalysis[] <- NA
rowData(pe[["proteinRobust"]])$stageWiseAnalysis[getPScreen(stageWiseAnalysis) %>% is.na %>% `!`,] <- getAdjustedPValues(stageWiseAnalysis, onlySignificantGenes=FALSE, order=FALSE)
```

```r
sigNamesStageWise <- apply(rowData(pe[["proteinRobust"]])$stageWiseAnalysis, 2, function(x) (x < 0.05) %>% which %>% names)

sapply(sigNamesStageWise,length)

for (i in 1:length(sigNamesStageWise))
heatmap(assay(pe[["proteinRobust"]])[sigNamesStageWise[[i]], ], main=names(sigNamesStageWise)[i])
```

Note, that
- our more relaxed FDR correction enables us to reject more null hypotheses in the second stage.
- we can recover `r length(sigNamesStageWise[[5]])` proteins with significant interactions.

It is also very important to realise that setting the method to correct for multiple testing in the second stage at `method = none` is only correct for very specific designs and research hypotheses that are assessed. For most analyses we suggest to use the Holm method, which always we provide correct results.

---

[← Data Analysis](04-data-analysis.md) · [Up: contents](index.md)
