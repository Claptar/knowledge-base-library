---
title: Detailed Program
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/index.Rmd
source_file: sources/statomics-sga21/index.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Detailed Program

**Source:** [`index.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/index.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

1. Position of the course: [PDF](../docs/intro/index.md)

2. Recap Linear Models (Week 1)

   - Lecture: [HTML](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.html), [PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.pdf)
   - Tutorial KPNA2: [HTML](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.html),  [PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.pdf)


## Module I: Proteomics Data Analysis (Week 1-5)


1. Bioinformatics for proteomics

   - Lecture: [PDF](../docs/martens_proteomics_bioinformatics/index.md), [youtube](https://www.youtube.com/watch?v=ZgwNWRul98o)
   - Tutorials: [identification](https://www.compomics.com/bioinformatics-for-proteomics/)

\newline

2. Preprocessing & Analysis of Simple Designs (week 3)

   - Lecture: [Preprocessing](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.pdf)]
   - Tutorial: [Preprocessing](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialPreprocessing.html)
   - Wrap-up: [Peptide-based Models](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.pdf)]

\newline

3. Statistical Inference & Analysis of Factorial Designs (Week 3-4)

   - Lecture: [Differential Abundance Analysis](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_inference.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_inference.pdf)]
   - Tutorial: [Design](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_tutorialDesign.html)
   - Wrap-up: [Blocking](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_blocking_wrapup.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_blocking_wrapup.pdf)]

4. Advanced materials and reading materials

   - [Technical details: Inference upon summarization](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.html)
   - [Stage-wise testing](../docs/stagewiseTesting/index.md)

   - Papers:

      - [Sticker et al. (2020) Robust summarization and inference in proteome-wide label-free quantification](https://www.biorxiv.org/content/10.1101/668863v1)
      - [Ludger Goeminne: Extensive Background on proteomics and proteomics data analysis (Introduction of PhD)](../docs/backgroundProteomicsDataAnalysis/index.md)
      - [Van den Berge et al. (2017) Stage-wise testing: stageR paper](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-017-1277-0)

5. Solutions

   - CPTAC study: See [wrap-up preprocessing](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.html)
   - [cancer 6x6](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.html)
   - mouse: See [wrap-up blocking](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_blocking_wrapup.html)
   - [Heart study](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.html)

## Module II: Bulk RNA-sequencing


1. Introduction to sequencing technology, raw data and preprocessing.

   - Lecture: [Introduction to sequencing](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_intro.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_intro.pdf)].
   - Tutorial: [Preprocessing RNA-seq data](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_preprocessing.sh)
   - Recommended reading: [RNA Sequencing Data: Hitchhiker's Guide to Expression Analysis](https://www.annualreviews.org/doi/abs/10.1146/annurev-biodatasci-072018-021255)

\newline

2. Working with count data and generalized linear models.

   - Lecture: [Working with count data and GLMs](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.pdf)].
   - Tutorial I: Embedded within the lecture: Analysis of bike-sharing data.
   - Tutorial II: [GLM for one gene](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_lab_oneGene.html).

\newline

3. Analysis of RNA-seq data.

   - Lecture + Tutorial: [Four major challenges in the analysis of RNA-seq datasets](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.pdf)].
   - [Why we use offsets rather than count scaling](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_scalingNormalization.html).

\newline

4. Technical topics in bulk RNA-seq differential expression analysis (DEA).

   - Lecture: [Technical topics in DEA](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.pdf)].

## Module III: Single-cell RNA-sequencing

1. General concepts and analysis workflow of single-cell RNA-seq data.

   - Lecture: [Slides](https://docs.google.com/presentation/d/1sfbtw52qWgA7TcDIrGB3fWksLM0Mu9O7gBqYgGrt9fM/edit?usp=sharing).
      - [Variance stabilizing transformation for a Poisson random variable](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_varStabilization.html) [[PDF](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_varStabilization.pdf)].
      - [Understanding UMAP](https://pair-code.github.io/understanding-umap/).
      - [Post-selection inference simulation](https://statomics.github.io/singleCellCourse/postSelectionInference.html)
   - [A reproducible workflow on the Macosko Drop-seq dataset](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.html).

---

[← Software](05-software.md) · [Up: contents](index.md) · [Instructors →](07-instructors.md)
