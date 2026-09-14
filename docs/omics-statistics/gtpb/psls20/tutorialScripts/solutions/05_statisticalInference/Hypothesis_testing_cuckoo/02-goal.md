---
title: Goal
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Goal

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

The researchers want totest if the type of foster parent
has an effect on the average length of the cuckoo eggs.

In theory, they want to study this for all six species.
However, a t-test can only be used to study mean differences
between two groups. If we want to analyze multiple groups, there
are two options.

1. We perform t-tests on all pairwise combinations of types.
This mean we need to perform n*(n-1)/2 = 15 t-tests.

2. We perform an ANOVA analysis.

The second strategy is much more efficient and has a higher
statistical power. We will learn all about ANOVA in a later
stage of this course week.

In this tutorial, we will assess a single pairwise comparison,
between the European robin and the European wren. In a following
tutorial, we will come back to this dataset and make a full
analysis with ANOVA.

Load the required libraries

```r
library(tidyverse)
```

---

[← Cuckoo dataset](01-cuckoo-dataset.md) · [Up: contents](index.md) · [Import the data →](03-import-the-data.md)
