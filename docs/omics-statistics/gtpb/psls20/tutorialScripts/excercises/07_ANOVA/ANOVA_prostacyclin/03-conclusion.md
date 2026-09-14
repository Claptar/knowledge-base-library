---
title: Conclusion
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conclusion

**Source:** [`tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- There is an extreme significant effect of arachidonic acid on the average prostacyclin blood concentration in rats ($p<0.001$).
The average prostacyclin concentration is higher in the high dose group than in the low and moderate dose group (both p-values are smaller than $p<0.001$).
- The average concentration in the high dose group is `r round(confint(model1.mcp)$confint[2,1],1)`ng/ml (95% CI [`r paste(round(confint(model1.mcp)$confint[2,2:3],1),collapse=",")`]ng/ml) and `r round(confint(model1.mcp)$confint[3,1],1)`ng/ml (95% BI [`r paste(round(confint(model1.mcp)$confint[3,2:3],1),collapse=",")`]ng/ml) higher than in the low and middle dose group, respectively.
- The difference in average prostacyclin concentration between the moderate and low dose group is not significant  (p=`r round(summary(model1.mcp)$test$pvalues[1],2)`).
(All p-values and confidence intervals for post-hoc tests are corrected for multiple testing using the Tukey method).

---

[← Analyse of Variance](02-analyse-of-variance.md) · [Up: contents](index.md)
