---
title: Smelly armpit dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Smelly armpit dataset

**Source:** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Smelly armpits are not caused by sweat, itself. The smell is caused
by specific micro-organisms belonging to the group of
*Corynebacterium spp.* that metabolise sweat.
Another group of abundant bacteria are the *Staphylococcus spp.*,
these bacteria do not metabolise sweat in smelly compounds.

The CMET-groep at Ghent University does research to on transplanting the armpit microbiome to save people with smelly armpits.

- Proposed Therapy:
  	1. Remove armpit-microbiome with antibiotics
    2. Influence armpit microbiome with microbial transplant
       (https://youtu.be/9RIFyqLXdVw)

- Experiment:

    - 20 students with smelly armpits are attributed to one of
      two treatment groups
    - placebo (only antibiotics)
    - transplant (antibiotica followed by microbial transplant).
    - The microbiome is sampled 6 weeks upon the treatment
    - The relative abundance of *Staphylococcus spp.* on
      *Corynebacterium spp.* + *Staphylococcus spp.* in the
      microbiome is measured via DGGE (*Denaturing Gradient Gel
      Electrophoresis*).

Load the libraries

```r
library(tidyverse)
```

---

[Up: contents](index.md) · [Import the dataset →](02-import-the-dataset.md)
