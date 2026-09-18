---
title: Power Issue Transcript Level Analysis
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf
source_file: sources/statomics-sga21/docs/stagewiseTesting.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`docs/stagewiseTesting.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Power Issue Transcript Level Analysis

Van den Berge et al. Genome Biology (2017) 18:151 Page 2 of 14

**Fig. 1** Performance curves for DTU analysis based on two simulation studies. The false discovery proportion (FDP, x-axis) is the fraction of false positive hypotheses over all rejected hypotheses. The true positive rate (TPR, y-axis) represents the fraction of false null hypotheses that have indeed been rejected. The three points on each curve represent working points on a nominal 1%, 5% and 10% FDR. The left panel a shows the results from a simulation performed in Soneson et al. (2016) [24] based on the Drosophila melanogaster transcriptome and clearly shows the increased sensitivity for tests that aggregate all transcript hypotheses on a gene level (green curve) in comparison to transcript-level tests (blue curve). The right panel b shows the results from a simulation based on the human transcriptome used in Soneson et al. (2016) [10]. Here, aggregated hypothesis tests show an even larger increase in sensitivity, possibly due to the higher complexity of the human transcriptome and thus a higher expected number of transcripts per gene for human

are differentially used; thus, higher sensitivity comes at the cost of a lower biological resolution.

In differential expression (DE) studies with complex designs, it is common practice to adopt multiple testing at the hypothesis level. This results in low power for discovering interaction effects since their standard error is typically much larger than for the main effects. Testing the treatment-time interaction effect in the cross-sectional time-series RNA-seq study from Hammer et al. (2010) [11] with limma-voom [12], for instance, returns no significant genes at a 5% FDR level, while more than 6000 genes are flagged when testing for treatment effects within a particular timepoint. Hence, the higher resolution on the hypothesis level comes at the expense of a low power for the interaction effect. In addition, FDR control on the hypothesis level does not guarantee FDR control on the gene level, because multiple hypotheses are assessed per gene, and the expected ratio of the number of genes with at least one false positive (false positive genes) to all positive genes in the union across hypotheses will be larger than the target FDR. For example, if three hypotheses are assessed with 5% false positives in the top-list for every contrast, then the aggregated top-lists will still contain 5% false positives. However, since the false positives in the different contrasts may be derived from different genes, the number of genes with false positives will increase with the number of hypotheses tested, while the total number of genes remains fixed. Thus, the gene-level FDR will be inflated if multiple hypotheses are of interest. This can lead to lower success rates of subsequent validation, since many genes without true treatment effects may be considered significant. In the RNA-seq literature, however, there is no consensus on how to combine the enhanced power of aggregation with an adequate resolution for the biological problem at hand. We argue that the multiple hypotheses at the gene level can be exploited in a two-stage testing procedure (Fig. 2) [13–15]. In the screening stage, genes with effects of interest are prioritised using an omnibus test, e.g. a global F test, a global likelihood ratio test or by aggregating p values. Assessing the aggregated null hypothesis has the advantages of (1) high sensitivity in a DTU/DTE context; (2) enriching for genes with significant interaction effects in complex DE studies, thereby boosting power; and (3) providing gene-level FDR control. In the confirmation stage, individual hypotheses are assessed for genes that pass the screening stage. Hence, it has the merit to combine the high power of aggregated hypothesis tests in stage I with the high resolution of individual hypothesis testing in stage II.

The suggested strategy positions itself in the larger framework of stage-wise testing procedures for high-throughput experiments. Lu et al. [16] previously proposed a two-stage strategy for microarrays based on mixed models, which is inapplicable to HTS data due to the violation of the distributional assumptions. Jiang and Doerge [13] proposed a generic two-stage DE analysis procedure where the first stage corresponds to testing a global null hypothesis, i.e. testing whether at least one hypothesis is false, after which post hoc tests are considered only for the significant genes. Their algorithm,

Van den berge et al. 2017 Genome Biology 18:151

Human: $> 38000$ genes and $> 173000$ transcripts

---

## Single cell transcriptomics

### nature communications

**ARTICLE**
Received 20 Sep 2016 | Accepted 23 Nov 2016 | Published 16 Jan 2017
DOI: 10.1038/ncomms14049
**OPEN**

**Massively parallel digital transcriptional profiling of single cells**

Grace X.Y. Zheng$^1$, Jessica M. Terry$^1$, Phillip Belgrader$^1$, Paul Ryvkin$^1$, Zachary W. Bent$^1$, Ryan Wilson$^1$, Solongo B. Ziraldo$^1$, Tobias D. Wheeler$^1$, Geoff P. McDermott$^1$, Junjie Zhu$^1$, Mark T. Gregory$^2$, Joe Shuga$^1$, Luz Montesclaros$^1$, Jason G. Underwood$^{1,3}$, Donald A. Masquelier$^1$, Stefanie Y. Nishimura$^1$, Michael Schnall-Levin$^1$, Paul W. Wyatt$^1$, Christopher M. Hindson$^1$, Rajiv Bharadwaj$^1$, Alexander Wong$^1$, Kevin D. Ness$^1$, Lan W. Beppu$^4$, H. Joachim Deeg$^4$, Christopher McFarland$^5$, Keith R. Loeb$^{4,6}$, William J. Valente$^{2,7,8}$, Nolan G. Ericson$^2$, Emily A. Stevens$^4$, Jerald P. Radich$^4$, Tarjei S. Mikkelsen$^1$, Benjamin J. Hindson$^1$ & Jason H. Bielas$^{2,6,8,9}$

genome.gov/sequencingcosts

---

## Single cell transcriptomics

Cell Suspension $\rightarrow$ Barcoding & Library Construction $\rightarrow$ Sequence Transcriptome

Transcriptome profile for each individual cell

| | | | |
| :--- | :--- | :--- | :--- |
| Cell 1 | Gene 1 | ... | Gene 30000 |
| Cell 10000 | Gene 1 | ... | Gene 30000 |

---

## Single cell transcriptomics

Kang et al. Nat. Biotechnol. 2018 36(1):89-94

* peripheral blood mononuclear cells
* from 8 individuals
* Stimulated vs control
* $> 29000$ cells

| Stimulated | Control |
| :--- | :--- |
| • NK cells | • NK cells |
| • FCGR3A+ Monocytes | • FCGR3A+ Monocytes |
| • CD8 T cells | • CD8 T cells |
| • CD4 T cells | • CD4 T cells |
| • CD14+ Monocytes | • CD14+ Monocytes |
| • B cells | • B cells |

---

## Single cell transcriptomics

Kang et al. Nat. Biotechnol. 2018 36(1):89-94

* peripheral blood mononuclear cells
* from 8 individuals
* Stimulated vs control
* $> 29000$ cells
* Two channels of 10x genomics chip
* Two lanes of hiseq run
* Demultiplexing individuals via SNPs

---

## Single cell transcriptomics

Kang et al. Nat. Biotechnol. 2018 36(1):89-94

* DE stimulated vs control in each cell type (6 tests/gene)
* Different stimulus effect across cell types (15 tests/gene)

---

## Many hypotheses per gene/protein in contemporary high throughput studies

Transcript-level analysis, single cell experiments and complex designs result in multiple hypotheses of interest per gene/protein.

The conventional strategy
1. assess each hypothesis separately
2. on FDR level $\alpha$
3. provide the biologist with list of top-genes for every contrast

---

## Many hypotheses per gene/protein in contemporary high throughput studies

Transcript-level analysis, single cell experiments and complex designs result in multiple hypotheses of interest per gene/protein.

The conventional strategy
1. assess each hypothesis separately
2. on FDR level $\alpha$
3. provide the biologist with list of top-genes for every contrast

However,

* Shortlist of interesting genes when we assess multiple hypotheses per gene/protein?
* Post-hoc tests for each hypothesis within a gene/protein if omnibus null hypothesis is rejected?
* Gene/protein-level FDR control required because downstream analysis and validation is done at the gene/protein-level.

---

## Simulation study conventional analysis in sequencing applications

---

## Example

* Based on Hammer et al. (2010), Genome Research
* Two conditions (control - SNL)
* Two timepoints (2 weeks - 2 months)

Interested in:
1. DE between conditions at 2 weeks ($> 7000$ DE genes)
2. DE between conditions at 2 months ($> 6500$ DE genes)
3. Different FC between timepoints (interaction, 0 $\Delta$FC genes)

**control**
**treatment**
2 weeks
2 months

---

## Example: Gene-level tests

all hypotheses
null genes

---

## Example transcript level analysis: control FDR on gene level by aggregated testing

A simple strategy would be to
1. Aggregate p-values across hypotheses (i.e. omnibus test)
2. Control FDR on level $\alpha_I$ on the aggregated p-values

---

## Example transcript level analysis: control FDR on gene level by aggregated testing

A simple strategy would be to
1. Aggregate p-values across hypotheses (i.e. omnibus test)
2. Control FDR on level $\alpha_I$ on the aggregated p-values

Additionally takes advantage of aggregated tests with higher sensitivity

However, **we lose resolution on the biology**

---

## Solution: Stage-wise testing procedure: aggregate and split evidence

```
       H_g1       ...       H_gng
         \         |         /
          v        v        v
           [Screening stage]   <-- Aggregate evidence (Omnibus test or by aggregating p-values)
                   |               Control FDR on aggregated tests across all genes
                   |
                   | Only retain significant genes
                   v
         [Confirmation stage]  <-- Control error rate within a gene on the FDR adjusted
          /        |        \      significance level from screening stage
         v         v         v
       H_g1       ...       H_gng <-- Assess each hypothesis separately
```

---

## Stage-wise testing procedure$^1$

1. **Screening Stage:**
   * Assess the screening hypothesis $H_g^S$ / global null hypothesis for all genes/proteins in the set $G$.
   * Apply the Benjamini Hochberg (BH) FDR procedure to the screening p-values at FDR level $\alpha$. Let $R$ be the number of rejected screening hypotheses.

$^1$Heller et al. 2009, Bioinformatics.

---

## Stage-wise testing procedure$^1$

1. **Screening Stage:**
   * Assess the screening hypothesis $H_g^S$ / global null hypothesis for all genes/proteins in the set $G$.
   * Apply the Benjamini Hochberg (BH) FDR procedure to the screening p-values at FDR level $\alpha$. Let $R$ be the number of rejected screening hypotheses.
2. **Confirmation Stage:** For all $R$ genes/proteins that pass the screening stage.
   * Let $\alpha_{II} = R\alpha/G$ be FDR-adjusted significance level from the first stage.
   * Adopt a multiple testing procedure to assess all $n_g$ hypotheses while controlling the within gene error rate at the adjusted level $\alpha_{II}$.

$^1$Heller et al. 2009, Bioinformatics.

---

## DGE experiments with complex designs

* Our procedure correctly controls the FDR at gene-level
* The omnibus test enriches for genes with interaction effects
* While maintaining equivalent power for main effects

---

## Stage-wise testing unlocks powerful transcript-level analysis

* Naturally unites high gene-level power with transcript-level resolution of the results
* Equal or better power at transcript level
* Better FDR control

### Drosophila

* gene-level
* tx-level
* tx-level stage-wise

### Human

* gene-level
* tx-level
* tx-level stage-wise

---

Van den Berge et al. Genome Biology (2017) 18:151
DOI 10.1186/s13059-017-1277-0

### Genome Biology

**METHOD**
**Open Access**

---

[← Omnibus testing and post-hoc tests for high throughput experiments](01-omnibus-testing-and-post-hoc-tests-for-high-throughput-exper.md) · [Up: contents](index.md) · [StagewiseTesting Part 03 — →](03-stagewisetesting-part-03.md)
