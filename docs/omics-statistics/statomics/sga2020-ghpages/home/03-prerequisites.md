---
title: Prerequisites
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/index.md
source_file: sources/statomics-sga2020-ghpages/index.md
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Prerequisites

**Source:** [`index.md`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/index.md) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.md` (lossless)

The prerequisites for the Statistical Genomics course are the successful completion of a basic course of statistics that covers topics on data exploration and descriptive statistics, statistical modeling, and inference: linear models, confidence intervals, t-tests, F-tests, anova, chi-squared test.

The basis concepts may be revisited in my online course [https://gtpb.github.io/PSLS20/](https://gtpb.github.io/PSLS20/) and in [https://statomics.github.io/statistiekCursusNotas/](https://gtpb.github.io/PSLS20/)

A primer to R and Data visualisation  in R can be found in:

- R Basics: [https://dodona.ugent.be/nl/courses/335/](https://dodona.ugent.be/nl/courses/335/)
- R Data Exploration: [https://dodona.ugent.be/nl/courses/345/](https://dodona.ugent.be/nl/courses/345/)


---

#### Topics

**Introduction**

  - Slides: [Intro](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/intro.pdf)
  - Software: [Install and Launch Statistical Software](../pages/software4stats/index.md)
  - Recap linear models: [case study](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/recapGeneralLinearModel.html)
  - Entire analysis for KPNA2 gene: [KPNA2](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/08-multipleRegression_KPNA2.html)

**Part I: Quantitative proteomics**

  - [Download Tutorial Data](https://github.com/statOmics/SGA2019/tree/data)


  1. Bioinformatics for proteomics
  - Slides: [Bioinformatics for Proteomics](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/martens_proteomics_bioinformatics_20190923.pdf)
  - Students can sharpen their background knowledge on Mass Spectrometry, Proteomics & Bioinformatics for Proteomics
 here:[Mass Spectrometry and Bioinformatics for Proteomics](../pages/techVideos/index.md)

 2. Identification
 - Slides:  [False Discovery Rate and Target Decoy Approach](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/1_Identification_Evaluation_Target_Decoy_Approach.pdf)
 - Tutorial: [Evaluating Target Decoy Quality](../pages/Identification/index.md), [example script identification](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/identification.html),
 [All searches](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/identification_all.html)

 3. Preprocessing & Analysis of Label Free Quantitative Proteomics Experiments with Simple Designs
 - Install Software: [Installation instructions msqrob2](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/installMsqrob2.md)
 - Slides: [Preprocessing](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/2_MSqRob_data_analysisI.pdf)
 - Tutorial: [preprocessing](../pages/sdaMsqrobSimple/index.md)


 4. Statistical Inference & Analysis of Experiments with Factorial Designs
 - Slides: [Inference](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/2_MSqRob_data_analysisII.pdf)
 - Tutorial: [Statistical Data Analysis with MSqRob for Factorial Designs](../pages/sdaMsqrobDesign/index.md)

 5. Reading Material and Technical details
    - Paper: [Sticker et al. (2020) Robust summarization and inference in proteome-wide label-free quantification](https://www.biorxiv.org/content/10.1101/668863v1)
    - part of PhD dissertation: [Extensive Background on proteomics and proteomics data analysis](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/backgroundProteomicsDataAnalysis.pdf)
    - [Inference upon summarization](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/technicalDetailsProteomics.html)


6. Stagewise testing: Omnibus test and post hoc analysis: [slides](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/stagewiseTesting.pdf)

7. Solutions
  - [cptac median](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/cptac_median.html)
  - [cptac robust](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/cptac.html)
  - [cptac maxLFQ](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/cptac_maxLfQ.html)
  - [cancer 3 vs 3](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/cancer2_3x3.html)
  - [cancer 6 vs 6](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/cancer2_6x6.html)
  - [cancer 9 vs 9](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/cancer2_9x9.html)
  - [mouse CRD](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/mouseCRD2.html)
  - [mouse RCB](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/mouseRCB2.html)
  - [mouse RCB wrong analysis](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/mouseRCBwrongAnalysis.html)
  - [heart](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/heartMainInteraction.html)
  - [heart StageR](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/heartMainInteractionStageR.html)


---

**Part II: Next-generation sequencing**

  - [Download Tutorial Data](https://github.com/statOmics/SGA2020/tree/data-rnaseq)

  1. Introduction to transcriptomics with next generation sequencing

      - slides: [intro](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/rnaseq1.pdf)
      - Background: [RNA sequencing data hitchhiker's guide to expression analysis](https://www.zora.uzh.ch/id/eprint/181231/1/Ann_Rev_Biomed_Data_Science_-_RNA_sequencing_data__hitchhiker_s__guide_to_expression_analysis.pdf)
      - tutorial

        - Mapping: [html](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/elegansMappingCountTable.html)
        - Differential Analysis: [html](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/elegans.html), which source of variability is not included in the analysis and how could we account for this? Try to adjust the script accordingly.

        - Background for the airway example (count table on small fastQ files available in the Tutorial Data):
      [html](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/airwayMappingCountTable.html)

  2. More Complex Designs

      - Researchers assessed the effect of spinal nerve ligation (SNL) on the transcriptome of rats. In this experiment, transcriptome profiling occurred at two weeks and two months after treatment, for both the SNL group and a control group. Two biological replicates are used for every treatment - time combination. The researchers are interested in early and late effects and in genes for which the effect changes over time. The data can be downloaded from the ReCount project website (http://bowtie-bio.sourceforge.net/recount/, dataset Hammer et al.). The following code can be used to download an R/Bioconductor expression set object.

      ```
      file <- "http://bowtie-bio.sourceforge.net/recount/ExpressionSets/hammer_eset.RData"
      load(url(file))
      hammer.eset
      ```

      - Paired-end sequencing was performed on primary cultures from parathyroid tumors of 4 patients at 2 time points over 3 conditions (control, treatment with diarylpropionitrile (DPN) and treatment with 4-hydroxytamoxifen (OHT)). DPN is a selective estrogen receptor agonist and OHT is a selective estrogen receptor modulator. One sample (patient 4, 24 hours, control) was omitted by the paper authors due to low quality. Data, the count table and information on the experiment is available at http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37211. It is not required to do the read mapping!

3. Technical details on transcriptomics with next generation sequencing. Generalized linear models are introduced in the slides and bulk RNA-seq tools via their corresponding papers

    - [slides on GLM](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/rnaseq2.pdf)
    - [Poisson GLM and parameter estimation](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/poissonIRWLS-implemented.html)
    - [edgeR: Negative Binomial](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3378882/)
    - [DESeq2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4302049/)
    - [voom](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4053721/)
    - [edgeR: Quasi Negative Binomial](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.362.9634&rep=rep1&type=pdf)

4. DE analysis starting from transcript level counts

    - [Soneson et al. 2016](https://f1000research.com/articles/4-1521/v2)
    - Building index with salmon
    ```
    salmon index --gencode -t gencode.v32.transcripts.fa -i gencode.v32_salmon_index
    ```
    - Mapping one sample with salmon:
    ```
    salmon quant -i gencode.v32_salmon_index -l A --gcBias -1 SRR1039508_subset_1.fastq -2 SRR1039508_subset_2.fastq --validateMappings -o quant/SRR1039508_subset_quant
    ```
    - [Intro to salmon](https://combine-lab.github.io/salmon/getting_started/)
    - [airway with DESeq2](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/airway_salmon_DESeq2.html)
    - [airway with EdgeR](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/airway_salmon_edgeR.html)

5. Solutions

    - Airway Example: [GenomeIndex](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/airwayGenomeIndex.html), [read mapping and count table](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/airwayMappingCountTableCorr.html), [DE analysis](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/airway.html)
    - Hammer Example: [edgeR](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/hammer.html), [edgeQL](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/hammer_quasi.html), [DESeq2](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/hammer_DESEQ2.html)

---

**Part III: Single-cell RNA-sequencing**

1. Single-cell analysis: Concepts and a general workflow for single-cell RNA-sequencing (scRNA-seq) datasets.

    - Slides: [Introduction to general concepts, and discussion of analysis pipeline](https://docs.google.com/presentation/d/1aZJz3S3pBRcGh9Zy2Bi6HXw2Rw-5tb0XNdyeesf9YEY/edit?usp=sharing).
    - An intuitive primer on why offsets are used for normalization, as opposed to simple count scaling: [HTML file](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/singleCell/scalingNormalization.html), [RMarkdown file](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/singleCell/scalingNormalization.Rmd).
    - Main resources: [Orchestrating Single-Cell Analysis with Bioconductor](http://bioconductor.org/books/release/OSCA/) and [corresponding paper](https://www.nature.com/articles/s41592-019-0654-x).
    - A reproducible workflow for the Drop-seq dataset from [Macosko *et al.* (2015)](https://www.cell.com/fulltext/S0092-8674(15)00549-8): [HTML file](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/singleCell/MacoskoWorkflow.html), [RMarkdown file](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/singleCell/MacoskoWorkflow.Rmd).
    - Working with scRNA-seq data: Assess the effect of feature selection on (i) dimensionality reduction, (ii) clustering using the dataset from Tasic *et al.* (2016). You can download the data from the [Gene Expression Omnibus, accession number GSE71585](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE71585).
    - [Understanding UMAP](https://pair-code.github.io/understanding-umap/).

2. Selected topics in single-cell RNA-seq analysis.

    - Trajectory-based differential expression analysis: [paper](https://www.nature.com/articles/s41467-020-14766-3), [slides](https://docs.google.com/presentation/d/1V2OFnTM6srut8OyDa50Ea86uku--aL-ZJuRwhsD5AJo/edit?usp=sharing), [workshop](https://kstreet13.github.io/bioc2020trajectories/articles/workshopTrajectories.html).
    - Differential transcript usage analysis for scRNA-seq data: presentation of unpublished work.
    - [Local FDR paper](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/singleCell/euclid.ss.1215441276.pdf)

**Projects**

- [Project introduction slides](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/singleCell/projects.pptx)
- [CiteSeq Project Assignment](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/singleCell/CITESeq_assignment.pdf)

##### [Instructors](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/instructors.md)

---

[← Target Audience](02-target-audience.md) · [Up: contents](index.md)
