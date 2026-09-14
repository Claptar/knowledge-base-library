---
title: The lettuce dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The lettuce dataset

**Source:** [`tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

The researcher want to find out if biochar, compost and
a combination of both biochar and compost have an influence
on the growth of lettuce plants. To this end, they grew up
lettuce plants in a greenhouse. The pots were filled with
one of four soil types;

1. Soil only (control)
2. Soil supplemented with biochar (refoak)
3. Soil supplemented with compost (compost)
4. Soil supplemented with both biochar and compost (cobc)

The dataset `freshweight_lettuce.txt` contains the freshweight
(in grams) for 28 lettuce plants (7 per condition). The researchers
want to use an ANOVA test to find out whether or not there is an
effect of one or more of the treatments on the growth of lettuce
plants. If so, they will use a post-hoc test (Tuckey test) to find
which specific treatments have an effect.

Load the required libraries

```r
library(tidyverse)
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Data import →](03-data-import.md)
