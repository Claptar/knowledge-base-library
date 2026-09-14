---
title: 'Conclusions: Prostacyclin example'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd
source_file: sources/gtpb-psls20/theory/07-Anova.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conclusions: Prostacyclin example

**Source:** [`theory/07-Anova.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Entire analysis for prostacyclin example

1. Anova before posthoc tests: F-test has a higher power than  pairwise t-test

    - F-test uses all data
    - For F-test we do not need to correct for multiple testing: one test is conducted for the general omnibus hypothesis

```r
model1 <- lm(prostac~dose,data=prostacyclin)
anova(model1)
```

```r
model1.mcp<-glht(model1,linfct=mcp(dose="Tukey"))
summary(model1.mcp)
```

```r
confint(model1.mcp)
```


- There is an extreme significant effect of arachidonic acid on the average prostacyclin blood concentration in rats ($p<0.001$).
The average prostacyclin concentration is higher in the high dose group than in the low and moderate dose group (both p-values are smaller than $p<0.001$).
- The average concentration in the high dose group is `r round(confint(model1.mcp)$confint[2,1],1)`ng/ml (95% CI [`r paste(round(confint(model1.mcp)$confint[2,2:3],1),collapse=",")`]ng/ml) and `r round(confint(model1.mcp)$confint[3,1],1)`ng/ml (95% BI [`r paste(round(confint(model1.mcp)$confint[3,2:3],1),collapse=",")`]ng/ml) higher than in the low and middle dose group, respectively.
- The difference in average prostacyclin concentration between the moderate and low dose group is not significant  (p=`r round(summary(model1.mcp)$test$pvalues[1],2)`).
(All p-values and confidence intervals for post-hoc tests are corrected for multiple testing using the Tukey method).


---

---

[← Post hoc analysis: Multiple comparisons of means](04-post-hoc-analysis-multiple-comparisons-of-means.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) →](06-home-https-gtpb-github-io-psls20.md)
