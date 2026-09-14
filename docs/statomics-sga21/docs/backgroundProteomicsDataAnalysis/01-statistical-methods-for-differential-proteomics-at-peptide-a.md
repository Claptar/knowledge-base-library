---
title: STATISTICAL METHODS FOR DIFFERENTIAL PROTEOMICS AT PEPTIDE AND PROTEIN LEVEL
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf
source_file: sources/statomics-sga21/docs/backgroundProteomicsDataAnalysis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# STATISTICAL METHODS FOR DIFFERENTIAL PROTEOMICS AT PEPTIDE AND PROTEIN LEVEL

**Source:** [`docs/backgroundProteomicsDataAnalysis.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Ir. Ludger Goeminne Student number: 00802186

Supervisors: Prof. Dr. Ir. Lieven Clement, Prof. Dr. Kris Gevaert

A dissertation submitted to Ghent University in partial fulfilment of the requirements for the degree of Doctor of Statistical Data Analysis

Academic year: 2018 - 2019


## **<u>SUMMARY</u>**

Proteins are very diverse biomolecules that facilitate nearly all cellular processes of life. They interact with each other in complex networks in which disruption of a single protein can severely impact an organism. Therefore, quantitative information of a proteome (i.e. the entire set of proteins present in an organism) is extremely important to gain insights in the functioning of an organism in both healthy and diseased states.

Mass spectrometry (MS)-based proteomics is the method of choice for the high-throughput identification and quantification of thousands of proteins in a single analysis. When deep proteome coverage on many samples is needed, the analysis is often performed without any stable isotope labels, label-free. Here, proteins are extracted and digested into peptides that are subsequently loaded onto a reverse-phase high-performance liquid chromatography column (HPLC) coupled to a mass spectrometer, by which they are separated, ionized and have their MS spectra recorded. The intensity peaks in these MS spectra are proxies for peptide abundance. Subsequently, (some) peptides are targeted for fragmentation and the resulting MS² spectra enable their identification. As a result, label-free proteomics data are hierarchical: the data are at the peptide ion level, while inference typically happens at the protein level. Important to note is that signal intensities are strongly peptide-dependent as some peptides ionize more efficiently than others. Furthermore, missing values are very common and a large fraction of this missingness is not at random. Indeed, intensities of lowabundant and poorly ionizing peptides are more likely to go missing and competition for ionization makes missingness also context-dependent.

Many _ad hoc_ data analysis workflows for differential protein quantification do not handle labelfree proteomics data in a statistically rigorous way, which leads to suboptimal ranking of differentially abundant proteins. Consequently, many biologically relevant proteins remain unnoticed and valuable resources are wasted by needlessly trying to validate false positive hits.

In chapter 8, we demonstrate the necessity of properly taking peptide-specific effects into account in differential protein quantification analyses. Peptide-based models, which naturally account for these effects, perform better than methods that summarize peptide intensities to the protein level prior to the statistical analysis. We further illustrate that controlling the false discovery rate becomes problematic when highly-abundant proteins are differentially abundant due to suppression of the intensity of the background proteome. Finally, we show that missing values should be handled with care as imputing these under wrong assumptions leads to worse results compared to not imputing missing values at all.

Most peptide-based models suffer from overfitting, unstable estimations of residual variances and a disproportionate impact of outlying peptide intensities. To address these issues, I developed the versatile R package MSqRob, which adds three modular improvements to existing peptide-based models: ridge regression stabilizes fold change estimates, empirical Bayes variance estimations stabilize the variances of the test statistics and M-estimation with Huber weights reduces the impa ct of outliers. MSqRob’s algorithm has been described in detail in section 9.1 and it not only improves the fold change estimates in terms of precision and accuracy, but also the protein ranking, leading to a better discrimination between true and false positives. MSqRob is freely available on GitHub (https://github.com/statOmics/MSqRob) and has a user-friendly graphical interface that is made in "Shiny", an R package developed by RStudio that allows smooth integration of the R programming language with an HTML interface.

xiii

In section 9.2, I pinpoint important aspects of both experimental design and data analysis. Furthermore, I provide a step-by-step guide on how to use the MSqRob graphical user interface for both simple as well as more complex experimental designs. I also provide welldocumented scripts to run analyses in bash mode, enabling the integration of MSqRob in automated pipelines on cluster environments.

In my latest, unpublished work (chapter 10), I focus on the missing value problem. Indeed, missingness in label-free proteomics is a mix of missingness completely at random and missingness not at random. However, the exact contributions of both mechanisms are unknown and dataset-specific, and imputing under the wrong assumptions is detrimental for the downstream protein quantifications. Therefore, I developed a hurdle model that combines the power of MSqRob with the complementary information that is available in peptide counts without having to rely on undeterminable assumptions. This enables MSqRob to quantify proteins that are completely missing in one condition in a statistically rigorous manner. Moreover, it opens new possibilities to detect the sudden appearance of post-translationally modified peptides in addition to traditional protein fold change estimation.

With the development of MSqRob, I have made an important contribution to enabling experimenters to get the most out of their proteomics data. And, even though MSqRob is already one of the most versatile differential proteomics quantification tools, there are ample opportunities to broaden MSqRob’s scope, both towards new types of (prote)omics data and towards more complicated experimental designs.

xiv

## **<u>ABBREVIATIONS</u>**

|AUC|area under the curve|
|---|---|
|CID|collision-induced dissociation|
|CPTAC|Clinical Proteomic Technology Assessment for Cancer Network|
|DA|differential abundance|
|DE|differential expression|
|DDA|data-dependent acquisition|
|DIA|data-independent acquisition|
|ESI|electrospray ionization|
|ETD|electron-transfer dissociation|
|FC|fold change|
|FDR|false discovery rate|
|FN|false negatives|
|FP|false positives|
|GFP|green fluorescent protein|
|HCD|higher-energy collisional dissociation|
|HILIC|hydrophilic interaction liquid chromatography|
|HPLC|high-performance liquid chromatography|
|IMAC|immobilized metal affinity chromatography|
|IQR|interquartile range|
|iTRAQ|isobaric tag for relative and absolute quantitation|
|LC|liquid chromatography|
|LFQ|label-free quantification|
|kNN|k-nearest neighbors|
|KO|knock-out|
|MALDI|matrix-assisted laser desorption|
|MCAR|missingness completely at random|
|MCMC|Markov Chain Monte Carlo|
|MDS|multidimensional scaling|
|MNAR|missingness not at random|
|MS|mass spectrometry|


xvii

|MOAC|metal-oxide affinity chromatography|
|---|---|
|NETD|negative electron-transfer dissociation|
|OR|odds ratio|
|pAUC|partial area under the curve|
|PPV|positive predictive values|
|PSM|peptide-to-spectrum match|
|QRILC|quantile regression imputation of left censored data|
|ROC|receiver operating curve|
|rpAUC|relative partial area under the curve|
|RP-HPLC|reverse-phase high-performance liquid chromatography|
|RR|robust ridge|
|SAX|strong anion exchange|
|SCX|strong cation exchange|
|SILAC|stable isotope labeling of amino acids in cell culture|
|SWATH-MS|sequential windowed acquisition<br>of all theoretical fragment ion mass spectra|
|TMT|tandem mass tags|
|TN|true negatives|
|TOF|time-of-flight|
|TP|true positives|
|UPS|Universal Proteomics Standard|
|UPS1|Universal Proteomics Standard 1|
|WT|wild type|


xviii

## **<u>SHORT TABLE OF CONTENTS</u>**

|**Foreword– woord vooraf ................................................................................................ viii**|
|---|
|**Summary ........................................................................................................................... xiii**|
|**Samenvatting ..................................................................................................................... xv**|
|**Abbreviations .................................................................................................................. xvii**|
|**Short table of contents .................................................................................................... xix**|
|**Long table of contents ...................................................................................................... xx**|
|**PART I: INTRODUCTION**|
|**1. Biological context  ........................................................................................................... 5**|
|**2. Technical context .......................................................................................................... 23**|
|**3. From spectra to data ..................................................................................................... 37**|
|**4. Differential protein abundance analysis ...................................................................... 49**|
|**5. Research hypothesis .................................................................................................... 83**|
|**6. Outline ............................................................................................................................ 87**|
|**7. References part I ........................................................................................................... 89**|
|**PART II: RESEARCH PAPERS**|
|**8. Summarization vs Peptide-Based Models in Label-Free Quantitative Proteomics:**<br>**Performance, Pitfalls, and Data Analysis Guidelines ................................................... 115**|
|**9. Robust quantification for label-free mass spectrometry-based proteomics  .......... 131**|
|**10. MSqRob takes the missing hurdle: uniting intensity- and count-based proteomics**<br>**.......................................................................................................................................... 187**|
|**PART III: DISCUSSION AND RESEARCH PERSPECTIVES**|
|**11. Discussion ................................................................................................................. 203**|
|**12. Future research perspectives ................................................................................... 221**|
|**13. References part III ..................................................................................................... 227**|


xix

## **<u>LONG TABLE OF CONTENTS</u>**

|**Foreword– woord vooraf ................................................................................................ viii**|
|---|
|**Summary ........................................................................................................................... xiii**|
|**Samenvatting ..................................................................................................................... xv**|
|**Abbreviations .................................................................................................................. xvii**|
|**Short table of contents .................................................................................................... xix**|
|**Long table of contents ...................................................................................................... xx**|
|**PART I: INTRODUCTION**|
|**1. Biological context  ........................................................................................................... 5**|
|_1.1. Proteins as the central effectors of life_.......................................................................... 5|
|1.1.1. The molecular structure and origin of proteins ....................................................... 5|
|1.1.2. Protein folding ....................................................................................................... 9|
|1.1.3. The JAK-STAT pathway as an example of a protein network  ............................. 10|
|1.1.4. Proteins in diseases ............................................................................................ 11|
|1.1.5. Applications of protein research .......................................................................... 13|
|_1.2. The nature of mass spectrometry-based proteomics_................................................. 14|
|1.2.1. General principles of liquid chromatography and mass spectrometry .................. 14|
|1.2.2. The MS-based proteomics workflow .................................................................... 16|
|1.2.3. Proteomics in relation to other omics ................................................................... 19|
|_1.3. Applications of mass spectrometry-based proteomics_............................................... 20|
|1.3.1. The analysis of protein and peptide abundance ................................................... 21|
|1.3.2. The analysis of protein modifications ................................................................... 21|
|**2. Technical context .......................................................................................................... 23**|
|_2.1. Label-based mass spectrometry-based proteomics_................................................... 23|
|2.1.1. Metabolic labeling ................................................................................................ 24|
|2.1.2. Post-metabolic labeling ....................................................................................... 26|
|_2.2. Label-free mass spectrometry-based proteomics_...................................................... 29|
|2.2.1. The label-free proteomics workflow ..................................................................... 29|
|2.2.2. Advantages and disadvantages of label-free MS-based proteomics .................... 34|
|2.2.3. Other label-free approaches ................................................................................ 34|


xx

|**3. From spectra to data ..................................................................................................... 37**|
|---|
|_3.1. Peptide ion identification_............................................................................................ 37|
|_3.2. Protein inference_........................................................................................................ 40|
|_3.3. Peptide quantification_................................................................................................. 41|
|_3.4. The nature of the data_............................................................................................... 43|
|_3.5. The need for benchmarking_....................................................................................... 46|
|**4. Differential protein abundance analysis ...................................................................... 49**|
|_4.1. Preprocessing_............................................................................................................ 49|
|4.1.1. Transformation .................................................................................................... 49|
|4.1.2. Filtering ............................................................................................................... 51|
|4.1.3. Normalization ...................................................................................................... 52|
|4.1.4. Imputation ........................................................................................................... 55|
|4.1.5. Summarization .................................................................................................... 57|
|_4.2. Methods for differential protein abundance analysis_.................................................. 61|
|4.2.1. The importance of study design ........................................................................... 61|
|4.2.2. Summarization-based methods ........................................................................... 63|
|4.2.3. Peptide-based methods ....................................................................................... 70|
|4.2.4. Ridge regression ................................................................................................. 73|
|4.2.5. Robust regression with M estimation ................................................................... 76|
|4.2.6. Counting-based methods .................................................................................... 79|
|4.2.7. Controlling the false discovery rate ...................................................................... 81|
|**5. Research hypothesis .................................................................................................... 83**|
|_5.1. Setting the stage_........................................................................................................ 83|
|_5.2. Aims of my PhD research_........................................................................................... 85|
|**6. Outline ............................................................................................................................ 87**|
|**7. References part I ........................................................................................................... 89**|
|**PART II: RESEARCH PAPERS**|
|**8. Summarization vs Peptide-Based Models in Label-Free Quantitative Proteomics:**|
|**Performance, Pitfalls, and Data Analysis Guidelines ................................................... 115**|
|_8.1. Abstract_................................................................................................................... 115|
|_8.2. Keywords_................................................................................................................. 116|
|_8.3. Introduction_.............................................................................................................. 116|
|_8.4. Materials and methods_............................................................................................ 117|


xxi

|8.4.1. Perseus-based workflows .................................................................................. 118|
|---|
|8.4.2. Summarization-based workflows ....................................................................... 118|
|8.4.3. Peptide-based models ....................................................................................... 119|
|8.4.4. Performance  ..................................................................................................... 120|
|_8.5. Results_..................................................................................................................... 120|
|_8.6. Discussion_.............................................................................................................. 124|
|_8.7. Conclusion_............................................................................................................... 126|
|_8.8. Supporting information_............................................................................................ 127|
|_8.9. Acknowledgement_................................................................................................... 127|
|_8.10. References_............................................................................................................ 127|
|**9. Robust quantification for label-free mass spectrometry-based proteomics  .......... 131**|
|_9.1. Peptide-level Robust Ridge Regression Improves Estimation, Sensitivity, and Specificity_<br>_in Data-dependent Quantitative Label-free Shotgun Proteomics_.................................... 131|
|9.1.1. Associated data  ................................................................................................ 131|
|9.1.2. Abstract ............................................................................................................. 132|
|9.1.3. Introduction ....................................................................................................... 132|
|9.1.4. Experimental procedures ................................................................................... 136|
|9.1.5. Results .............................................................................................................. 139|
|9.1.6. Discussion ......................................................................................................... 146|
|9.1.7. Footnotes .......................................................................................................... 149|
|9.1.8. References ........................................................................................................ 149|
|9.1.9. Appendix ........................................................................................................... 152|
|_9.2. Experimental design and data-analysis in label-free quantitative LC/MS proteomics:_|
|_A tutorial with MSqRob_.................................................................................................... 156|
|9.2.1. Highlights .......................................................................................................... 156|
|9.2.2. Abstract ............................................................................................................. 156|
|9.2.3. Significance ....................................................................................................... 156|
|9.2.4. Graphical abstract  ............................................................................................ 157|
|9.2.5. Keywords .......................................................................................................... 157|
|9.2.6. Historical background  ....................................................................................... 157|
|9.2.7. Basic concepts .................................................................................................. 160|
|9.2.8. How is MSqRob used in research? .................................................................... 163|
|9.2.9. Case studies ..................................................................................................... 164|
|9.2.10. Current limitations and useful working limits .................................................... 176|
|9.2.11. Future developments ....................................................................................... 176|
|9.2.12. Acknowledgements ......................................................................................... 177|
|9.2.13. Appendix A  ..................................................................................................... 177|
|9.2.14. References  ..................................................................................................... 177|
|9.2.15. Appendix ......................................................................................................... 185|


xxii

|**10. MSqRob takes the missing hurdle: uniting intensity- and count-based proteomics**|
|---|
|**.......................................................................................................................................... 187**|
|_10.1. Abstract_................................................................................................................. 187|
|_10.2. Introduction_............................................................................................................ 187|
|_10.3. Results and discussion_.......................................................................................... 189|
|_10.4. Methods_................................................................................................................ 192|
|10.4.1. Missing values in recent PRIDE projects ......................................................... 192|
|10.4.2. Data availability ............................................................................................... 192|
|10.4.3. Preprocessing for MSqRob and the quasibinomial model ................................ 193|
|10.4.4. Imputation methods  ........................................................................................ 193|
|10.4.5. Statistical inference ......................................................................................... 194|
|10.4.6. Code availability .............................................................................................. 197|
|_10.5. Acknowledgements_................................................................................................ 197|
|_10.6. Author contributions_............................................................................................... 197|
|_10.7. References_............................................................................................................ 497|
|_10.8. Appendix_................................................................................................................ 199|
|**PART III: DISCUSSION AND RESEARCH PERSPECTIVES**|
|**11. Discussion ................................................................................................................. 203**|
|_11.1. Comparing performances_....................................................................................... 203|
|_11.2. The impact of MSqRob_.......................................................................................... 206|
|_11.3. The impact of the hurdle model_.............................................................................. 209|
|_11.4. Controlling the false discovery rate_........................................................................ 210|
|_11.5. MSqRob compared to other methods_..................................................................... 211|
|_11.6. The impact of technological and algorithmic innovations_........................................ 217|
|**12. Future research perspectives ................................................................................... 221**|
|**13. References part III ..................................................................................................... 227**|


xxiii

---

[Up: contents](index.md) · [PART I: INTRODUCTION →](02-part-i-introduction.md)
