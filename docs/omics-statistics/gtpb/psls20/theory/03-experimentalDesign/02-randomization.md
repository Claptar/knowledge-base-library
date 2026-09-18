---
title: Randomization
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/03-experimentalDesign.Rmd
source_file: sources/gtpb-psls20/theory/03-experimentalDesign.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`theory/03-experimentalDesign.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/03-experimentalDesign.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Randomization

- Randomization completely at random (no systematic allocation).

### Simple Randomization

- Can lead to differences in the number of experimental units in each treatment arm

- in 5% of the cases we might observe an imbalance of
    - of at least 60:40 in a study with 100 subjects, and
    - of at least 531:469 in a study with 1000 subjects.

- This imbalance is not problematic, but causes a loss in precision.

---

### Balanced Randomization

- Equal numbers of each treatment are assigned to a block of 2 or 4 patients.
    - (1) AB, (2) BA
    - (1) AABB, (2) ABAB, (3) ABBA, (4) BABA, (5) BAAB, (6) BBAA

- Balanced Randomization ensures $\pm$ the same number of people in the control and the treatment arm of the experiment.

- Does not make that we have an equal number of males with and without the treatment, etc.

- In small studies, it is possible that the groups are unbalanced in other characteristics (e.g. gender, race, age ...)

- This is not problematic because it occurs at random, but, again it causes a loss in precision.

---

### Stratified randomization**

- The imbalance according to for instance gender can be avoided using stratified Randomization: balanced randomization per stratum

![Stratified Randomizatie](https://raw.githubusercontent.com/GTPB/PSLS20/gh-pages/assets/figs/stratification.png){ width=50% }

---

## Blocking

### Gene expression example

- dm: diabetic medium, nd: non diabetic medium, co: control
- 4 bio-reps, 2 techreps/biorep
![](https://raw.githubusercontent.com/GTPB/PSLS20/gh-pages/assets/figs/qpcrBadDesign1.png){ width=100% }

- dm: diabetic medium, nd: non diabetic medium, co: control
- 4 bio-reps, 2 techreps/biorep, 2 plates A & B
- Treatment and plate almost entirely confounded

![](https://raw.githubusercontent.com/GTPB/PSLS20/gh-pages/assets/figs/qpcrBadDesign2.png){ width=100% }

### Nature methods: Points of significance - Blocking

![](https://www.nature.com/articles/nmeth.3005.pdf){ width=100% }

---

## Sample size

- The sample size and the design are crucial.

- The larger the sample size, the more precise the results.

## Wrap-up

- Sample size is very important.

- To assess the effect of a treatment, we should compare comparable and representative groups of subjects with and without the treatment (a good control!).

- In observational studies, the researcher cannot choose the treatment. It was the patient or their MD who had chosen it

- In experimental studies, the researcher assigns the treatment.

- Confounding can be avoided via randomization.

- We can also correct for confounding in the statistical analysis for the confounders that have been registered.

---

## [Home](https://gtpb.github.io/PSLS20/) {-}

---

[← Introduction](01-introduction.md) · [Up: contents](index.md)
