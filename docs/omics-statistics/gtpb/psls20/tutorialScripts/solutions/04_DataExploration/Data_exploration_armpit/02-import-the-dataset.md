---
title: Import the dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Import the dataset

**Source:** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
ap <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/armpit.csv")
```

```r
glimpse(ap)
```

---

[← Smelly armpit dataset](01-smelly-armpit-dataset.md) · [Up: contents](index.md) · [Goal →](03-goal.md)
