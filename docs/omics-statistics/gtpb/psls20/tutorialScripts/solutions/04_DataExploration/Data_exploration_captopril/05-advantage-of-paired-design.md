---
title: Advantage of paired design
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Advantage of paired design

**Source:** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Every patient acts as their own control: we can estimate the effect of the treatment
for each patient

```r
captopril %>%
  ggplot(aes(SBPb,SBPa)) +
  geom_point() +
  ggtitle(paste("correlation = ",round(cor(captopril$SBPb,captopril$SBPa),3)))
```

```r
captopril %>%
  mutate(bp_diff = SBPa-SBPb) %>%
  select(SBPb,SBPa,bp_diff) %>%
  summarize_all(sd)
```

Calculate variance based on fact that data are paired.

```r
captopril %>% summarise(sd_diff=sqrt(sd(SBPb)^2 + sd(SBPa)^2-2*sd(SBPa)*sd(SBPb)*cor(SBPa,SBPb)))
```

Note, that the standard deviations on the blood pressure measurements are more than
twice as large as the standard deviations on the difference.
This is because each patient acts as their own control. As such, we can correct for
their baseline blood pressure when estimating the effect of the treatment.

---

[← Wrap-up](04-wrap-up.md) · [Up: contents](index.md)
