---
title: Analyse of Variance
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Analyse of Variance

**Source:** [`tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
model1 <- lm(prostac~dose,data=prostacyclin)
anova(model1)
```

Based on the anova analysis we can reject the omnibus null hypothesis that there is no effect of the arachidonic acid treatment on the average prostacyclin concentration in rats.
Next we continue to assess for which treatment groups the means are different using a posthoc analysis with the Tukey method to correct for multiple testing.

```r
#install.packages("multcomp")
library(multcomp)
model1.mcp<-glht(model1,linfct=mcp(dose="Tukey"))
summary(model1.mcp)
confint(model1.mcp)
plot(model1.mcp)
```

---

[← Prostacyclin Example](01-prostacyclin-example.md) · [Up: contents](index.md) · [Conclusion →](03-conclusion.md)
