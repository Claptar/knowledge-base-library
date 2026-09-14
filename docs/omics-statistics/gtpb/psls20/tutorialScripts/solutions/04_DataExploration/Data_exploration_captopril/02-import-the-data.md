---
title: Import the data
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Import the data

**Source:** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
library(tidyverse)
```

```r
captopril <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/captopril.txt")
```

```r
head(captopril)
```

---

[← The captopril dataset](01-the-captopril-dataset.md) · [Up: contents](index.md) · [Data visualization →](03-data-visualization.md)
