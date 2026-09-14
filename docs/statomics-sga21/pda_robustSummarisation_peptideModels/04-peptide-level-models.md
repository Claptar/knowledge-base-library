---
title: Peptide-level models
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.Rmd
source_file: sources/statomics-sga21/pda_robustSummarisation_peptideModels.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Peptide-level models

**Source:** [`pda_robustSummarisation_peptideModels.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Summarization


<details><summary> Click to see code to make plot </summary><p>
```r
prot <- "P01031ups|CO5_HUMAN_UPS"
data <- pe[["peptideNorm"]][
  rowData(pe[["peptideNorm"]])$Proteins == prot,
  colData(pe)$lab=="lab3"] %>%
  assay %>%
  as.data.frame %>%
  rownames_to_column(var = "peptide") %>%
  gather(sample, intensity, -peptide) %>%
  mutate(condition = colData(pe)[sample,"condition"]) %>%
  na.exclude
sumPlot <- data %>%
  ggplot(aes(x = peptide, y = intensity, color = condition, group = sample, label = condition), show.legend = FALSE) +
  geom_text(show.legend = FALSE) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
  xlab("Peptide") +
  ylab("Intensity (log2)") +
  ggtitle(paste0("protein: ",prot))
```
</p></details>


Here, we will focus on the summarization of the intensities for protein `r prot`.

```r
sumPlot +
  geom_line(linetype="dashed",alpha=.4)
```

### Median summarization

We first evaluate median summarization for protein `r prot`.

<details><summary> Click to see code to make plot </summary><p>
```r
dataHlp <- pe[["peptideNorm"]][
    rowData(pe[["peptideNorm"]])$Proteins == prot,
    colData(pe)$lab=="lab3"] %>% assay

sumMedian <- data.frame(
  intensity= dataHlp
    %>% colMedians(na.rm=TRUE)
  ,
  condition= colnames(dataHlp) %>% substr(12,12) %>% as.factor )

sumMedianPlot <- sumPlot +
  geom_hline(
    data = sumMedian,
    mapping = aes(yintercept=intensity,color=condition)) +
  ggtitle("Median summarization")
```
</p></details>

```r
sumMedianPlot
```


- The sample medians are not a good estimate for the protein expression value.
- Indeed, they do not account for differences in peptide effects
- Peptides that ionize poorly are also picked up in samples with high spike-in concencentration and not in samples with low spike-in concentration
- This introduces a bias.

### Mean summarization


$$
y_{ip} = \beta_i^\text{sample} + \epsilon_{ip}
$$
<details><summary> Click to see code to make plot </summary><p>
```r
sumMeanMod <- lm(intensity ~ -1 + sample,data)

sumMean <- data.frame(
  intensity=sumMeanMod$coef[grep("sample",names(sumMeanMod$coef))],
  condition= names(sumMeanMod$coef)[grep("sample",names(sumMeanMod$coef))] %>% substr(18,18) %>% as.factor )


sumMeanPlot <- sumPlot + geom_hline(
    data = sumMean,
    mapping = aes(yintercept=intensity,color=condition)) +
    ggtitle("Mean summarization")
```
</p></details>

```r
grid.arrange(sumMedianPlot, sumMeanPlot, ncol=2)
```


### Model based summarization

We can use a linear peptide-level model to estimate the protein expression value while correcting for the peptide effect, i.e.

$$
y_{ip} = \beta_i^\text{sample}+\beta^{peptide}_{p} + \epsilon_{ip}
$$


<details><summary> Click to see code to make plot </summary><p>
```r
sumMeanPepMod <- lm(intensity ~ -1 + sample + peptide,data)

sumMeanPep <- data.frame(
  intensity=sumMeanPepMod$coef[grep("sample",names(sumMeanPepMod$coef))] + mean(data$intensity) - mean(sumMeanPepMod$coef[grep("sample",names(sumMeanPepMod$coef))]),
  condition= names(sumMeanPepMod$coef)[grep("sample",names(sumMeanPepMod$coef))] %>% substr(18,18) %>% as.factor )


fitLmPlot <-  sumPlot + geom_line(
    data = data %>% mutate(fit=sumMeanPepMod$fitted.values),
    mapping = aes(x=peptide, y=fit,color=condition, group=sample)) +
    ggtitle("fit: ~ sample + peptide")
sumLmPlot <- sumPlot + geom_hline(
    data = sumMeanPep,
    mapping = aes(yintercept=intensity,color=condition)) +
    ggtitle("Summarization: sample effect")
```
</p></details>

```r
grid.arrange(sumMedianPlot, sumMeanPlot, sumLmPlot, nrow=1)
```

- By correcting for the peptide species the protein expression values are much better separated an better reflect differences in abundance induced by the spike-in condition.

- Indeed, it shows that median and mean summarization that do not account for the peptide effect indeed overestimate the protein expression value in the small spike-in conditions and underestimate that in the large spike-in conditions.

- Still there seem to be some issues with samples that for which the expression values are not well separated according to the spike-in condition.

A residual analysis clearly indicates potential issues:

<details><summary> Click to see code to make plot </summary><p>
```r
resPlot <- data %>%
  mutate(res=sumMeanPepMod$residuals) %>%
  ggplot(aes(x = peptide, y = res, color = condition, label = condition), show.legend = FALSE) +
  geom_point(shape=21) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
  xlab("Peptide") +
  ylab("residual") +
  ggtitle("residuals: ~ sample + peptide")
```
</p></details>

```r
grid.arrange(fitLmPlot, resPlot, nrow = 1)
grid.arrange(fitLmPlot, sumLmPlot, nrow = 1)
```

- The residual plot shows some large outliers for peptide KIEEIAAK.
- Indeed, in the original plot the intensities for this peptide do not seem to line up very well with the concentration.
- This induces a bias in the summarization for some of the samples (e.g. for D and E)

### Robust summarization using a peptide-level linear model

$$
y_{ip} = \beta_i^\text{sample}+\beta^{peptide}_{p} + \epsilon_{ip}
$$


- Ordinary least squares: estimate $\beta$ that minimizes
$$
\text{OLS}: \sum\limits_{i,p} \epsilon_{ip}^2 = \sum\limits_{i,p}(y_{ip}-\beta_i^\text{sample}-\beta_p^\text{peptide})^2
$$

We replace OLS by M-estimation with loss function
$$
\sum\limits_{i,p} w_{ip}\epsilon_{ip}^2 = \sum\limits_{i,p}w_{ip}(y_{ip}-\beta_i^\text{sample}-\beta_p^\text{peptide})^2
$$

- Iteratively fit model with observation weights $w_{ip}$ until convergence
- The weights are calculated based on standardized residuals

<details><summary> Click to see code to make plot </summary><p>
```r
sumMeanPepRobMod <- MASS::rlm(intensity ~ -1 + sample + peptide,data)
resRobPlot <- data %>%
  mutate(res = sumMeanPepRobMod$residuals,
         w = sumMeanPepRobMod$w) %>%
  ggplot(aes(x = peptide, y = res, color = condition, label = condition,size=w), show.legend = FALSE) +
  geom_point(shape=21,size=.2) +
  geom_point(shape=21) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
  xlab("Peptide") +
  ylab("residual") +
  ylim(c(-1,1)*max(abs(sumMeanPepRobMod$residuals)))
weightPlot <- qplot(
  seq(-5,5,.01),
  MASS::psi.huber(seq(-5,5,.01)),
  geom="path") +
  xlab("standardized residual") +
  ylab("weight")
```
</p></details>

```r
grid.arrange(weightPlot,resRobPlot,nrow=1)
```

- We clearly see that the weights in the M-estimation procedure will down-weight errors associated with outliers for peptide KIEEIAAK.

<details><summary> Click to see code to make plot </summary><p>
```r
sumMeanPepRob <- data.frame(
  intensity=sumMeanPepRobMod$coef[grep("sample",names(sumMeanPepRobMod$coef))] + mean(data$intensity) - mean(sumMeanPepRobMod$coef[grep("sample",names(sumMeanPepRobMod$coef))]),
  condition= names(sumMeanPepRobMod$coef)[grep("sample",names(sumMeanPepRobMod$coef))] %>% substr(18,18) %>% as.factor )

sumRlmPlot <- sumPlot + geom_hline(
    data=sumMeanPepRob,
    mapping=aes(yintercept=intensity,color=condition)) +
    ggtitle("Robust")
```
</p></details>

```r
 grid.arrange(sumLmPlot + ggtitle("OLS"), sumRlmPlot, nrow = 1)
```

- Robust regresion results in a better separation between the protein expression values for the different samples according to their spike-in concentration.


### Comparison summarization methods

- maxLFQ

```r
knitr::include_graphics("./figures/maxLFQ_principle.png")
```

- MS-stats also uses a robust peptide level model to perform the summarization, however, they typically first impute missing values

- Proteus high-flyer method: mean of three peptides with highest intensity


```r
knitr::include_graphics("./figures/msqrobsum_sum_novel.png")
```

- [@sticker2020]
- doi: https://doi.org/10.1074/mcp.RA119.001624
- [pdf](https://www.mcponline.org/action/showPdf?pii=S1535-9476%2820%2934982-3)

## Estimation of differential abundance using peptide level model

- Instead of summarising the data we can also directly model the data at the peptide-level.
- But, we will have to address the pseudo-replication.

$$
y_{iclp}= \beta_0 + \beta_c^\text{condition} + \beta_l^\text{lab} + \beta_p^\text{peptide} + u_s^\text{sample} + \epsilon_{iclp}
$$

- protein-level

  - $\beta^\text{condition}_c$: spike-in condition $c=b, \ldots, e$
  - $\beta^\text{lab}_l$: lab effect $l=l_2\ldots l_3$
  - $u_{r}^\text{run}\sim N\left(0,\sigma^2_\text{run}\right) \rightarrow$ random effect addresses pseudo-replication

- peptide-level
  - $\beta_{p}^\text{peptide}$: peptide effect
  - $\epsilon_{rp} \sim N\left(0,\sigma^2_{\epsilon}\right)$ within sample (run) error


- DA estimates:
$$
\log_2FC_{B-A}=\beta^\text{condition}_B
$$
$$
\log_2FC_{C-B}=\beta^\text{condition}_C - \beta^\text{condition}_B
$$
- Mixed peptide-level models are implemented in msqrob2

- It has the advantages that

  1. it correctly addresses the difference levels of variability in the data
  2. it avoids summarization and therefore also accounts for the difference in the number of peptides that are observed in each sample
  3. more powerful analysis

- It has the disadvantage that


  1. protein summaries are no longer available for plotting
  2. it is difficult to correctly specify the degrees of freedom for the test-statistic leading to inference that is too liberal in experiments with small sample size
  3. sometimes sample level random effect variance are estimated to be zero, then the pseudo-replication is not addressed leading to inference that is too liberal for these specific proteins
  4. they are much more difficult to disseminate to users with limited background in statistics

Hence, for this course we opted to use peptide-level models for summarization, but not for directly inferring on the differential expression at the protein-level.

---

[← Full CPTAC study](03-full-cptac-study.md) · [Up: contents](index.md) · [References →](05-references.md)
