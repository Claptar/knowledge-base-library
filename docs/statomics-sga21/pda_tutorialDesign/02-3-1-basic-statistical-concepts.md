---
title: 3.1 Basic Statistical Concepts
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialDesign.Rmd
source_file: sources/statomics-sga21/pda_tutorialDesign.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3.1 Basic Statistical Concepts

**Source:** [`pda_tutorialDesign.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialDesign.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

The actual design of an experiment strongly impacts the data analysis and its power to discover differentially abundant proteins. Therefore, we first cover some basic concepts on experimental design. Next, we provide a general step-by-step overview of a typical quantitative proteomics data analysis workflow. The monthly column “Points of significance” in Nature Methods is a useful primer on statistical design for researchers in life sciences to which we extensively refer in this section (http://www.nature.com/collections/qghhqm/pointsofsignificance).

For proteomics experiments it is important to differentiate between experimental units and observational units. Experimental units are the subjects/objects on which one applies a given treatment, often also denoted as biological repeats. In a proteomics experiment, the number of experimental units is typically rather limited (e.g. three biological repeats of a knockout and three for a wild-type sample). The measurements, however, are gathered on the observational units. In a shotgun proteomics experiment, these are the individual peptide intensities.

For many proteins, there are thus multiple observations/peptide intensities for each experimental unit, which can be considered as technical replicates or pseudo-replicates.
There are two methods to deal with pseudo-replication at the peptide-level.

1. Summarize the peptide intensities into a protein expression value for each protein in the preprocessing and specify the statistical model at the protein level. Indeed, we no-longer have pseudo-replication at the protein level.

2. Model the peptide intensities using a mixed model with a random effect for sample, which will model the correlation between peptides for the same protein in the same sample.

Both approaches are possible with msqrob2. But, in the tutorial we focus on the summariztion method which is computationally less demanding and the statistical model is less complex to teach.

In a typical proteomics data set one can make very precise estimates on the technical variability of the intensity measurements; i.e. how strongly intensity measurements fluctuate for the peptides of a particular protein. However, the power to generalize the effects observed in the sample to the whole population remains limited as most biological experiments typically only have a limited number of biological repeats.

We thus strongly advise researchers to think upfront about their experimental design and to maximize the number of biological repeats (we suggest at least three biological repeats, and preferably more).

A very powerful concept in experimental design is that of blocking. In randomized complete block design one randomizes the different treatments to experimental units that are arranged within groups/blocks (e.g. batches, time periods) that are similar to each other. Due to practical constraints, it is often impossible to perform all experiments on the same day, or even on the same HPLC column or mass spectrometer, leading to unwanted sources of technical variation. In other experiments, researchers might test the treatment in multiple cultures or in big experiments that involve multiple labs. A good experimental design aims to mitigate unwanted sources of variability by including all or as many treatments as possible within each block. That way, variability between blocks can be factored out from the analysis when assessing treatment effects (Figure 1). It is of prime importance that all treatments are present within each block, otherwise confounding can occur between the treatment and block e.g. (Figure 1).


![Figure 1. Blocking](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/blocking.png)

Figure 1. is an example of a good (A) and a bad (B) design. In design A, both the green and orange treatments are divided equally within each block. That way, the treatment effect can be estimated within a block. In design B, each block contains only one treatment, so the treatment effect is entirely confounded with the blocking effect and it is thus impossible to draw meaningful conclusions on the treatment (unless one would be willing to assume that the blocking effect is negligible, which is a very strong assumption that cannot be verified based on the design).

---

[← 3. Analysis of more complex designs with MSqRob](01-3-analysis-of-more-complex-designs-with-msqrob.md) · [Up: contents](index.md) · [3.2 Blocking: Mouse T-cell example →](03-3-2-blocking-mouse-t-cell-example.md)
