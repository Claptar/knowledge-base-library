---
title: INTEGRATING PROTEIN COUNTS INTO SINGLE-CELL RNA-SEQ ANALYSIS
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# INTEGRATING PROTEIN COUNTS INTO SINGLE-CELL RNA-SEQ ANALYSIS

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Felce, Catherine, Meichen Fang, and Lior Pachter (2025). “Joint Biophysical Modeling of Paired Single-Cell RNA and Protein Measurements”. In: _bioRxiv_ . doi: `10.1101/2025.11.14.688548` . eprint: `2025.11.14.688548` . url: `https: //doi.org/10.1101/2025.11.14.688548` .

### **3.1 Abstract**

Surface protein measurements can supplement gene expression information from single-cell RNA sequencing to provide a more complete assessment of cell identity and function. Recently developed multiomic assays facilitate such measurements, and can, in principle, be utilized to understand the dynamics of transcription and translation. We develop a framework for biophysical modeling of transcription jointly with translation from single-cell data, along with a suitable technical noise model for sequencing data. We demonstrate its efficacy using simulations, and illustrate how it can be useful in practice with 10x multiomic data. Our proof-ofprinciple highlights the potential for jointly modeling transcription and translation as data quality and measurement accuracy improves.

### **3.2 Background**

Although messenger RNA has historically been used as a proxy for protein expression (Junker et al., 2014; Fu et al., 2007), many studies have highlighted the role of post-transcriptional regulation in decoupling RNA and protein levels (Wei et al., 2015; Franks, Airoldi, and Slavov, 2017), especially in embryogenesis and other developmental processes (Kuersten and Goodwin, 2003). The poor correlation between mRNA and protein counts across the genome has been extensively investigated (Maier, Güell, and Serrano, 2009), with biologists calling for principled modeling (McManus, Zhe Cheng, and Vogel, 2015; Greenbaum et al., 2003), including technical noise models (Yansheng Liu, Beyer, and Aebersold, 2016), to shed light on these discrepancies. While differentially expressed RNA has been shown to correlate more strongly with its associated proteins than non-differentially expressed RNA (Koussounadis et al., 2015), the range of correlations for individual

37

genes is still broad ( _𝑟_ = −0 _._ 95 to 0 _._ 94) and differentially expressed proteins have been shown not to reliably correlate with differentially expressed RNA (Huber et al., 2004; Ideker, 2001).

Given that combined RNA expression and proteomic data are helpful for analyzing the immune response (Wu et al., 2020) and bacterial growth (Nobori et al., 2020), there is a clear benefit to investigating the separate regulatory contributions of transcription and translation using multiomic data. Recognizing this, statistical tools have been created to disentangle RNA and protein-level regulation using time-course data (Teo et al., 2014), and studies have confirmed that RNA and protein-level regulation are both important, with some genes being regulated in opposite directions simultaneously (Zhandong Cheng et al., 2016). Cross-species studies have also highlighted the potential decoupling of mRNA and protein levels, and have tried to unravel the effects of transcriptional, translational, and posttranslational mechanisms on expression divergence (J. Wang et al., 2018).

However, time-course or cross-species measurements are difficult to obtain, and increasingly ubiquitous single-cell data offer the opportunity, in principle, to study the dynamics of transcription and translation in a complementary way. We propose a biophysical model based on single-cell multiomic data that can simultaneously describe transcriptional and translational mechanisms and untangle their contributions to controlling protein expression.

Single-cell resolution RNA measurements have already enabled biophysical modeling of nascent and mature RNA and the inference of transcriptional rate parameters (Gorin, Vastola, and L. Pachter, 2023). In that setting, the modeling relies on multimodal datasets, specifically spliced and unspliced counts measured from mature and nascent RNAs (Gorin, Vastola, Fang, et al., 2022). The inclusion of chromatin information from ATAC-seq has also been considered (Felce, Gorin, and L. S. Pachter, 2024). In this work we extend these approaches to include protein count data.

High quality single-cell protein quantification, including isoform differentiation, has become available with single-cell western blotting (Hughes et al., 2014). Since 2017, with the advent of high-throughput simultaneous proteomic and transcriptomic measurements in single-cells with REAP-seq (Peterson et al., 2017) and CITE-seq (Stoeckius et al., 2017), principled biophysical modeling of the joint modalities is now within reach.

Although models combining RNA dynamics with constitutive protein translation of

38


Figure 3.1: **Fitting a joint biophysical model for RNA and protein** . Single-cell transcriptomics and surface protein expression can be simultaneously measured using methods such as<sup>1</sup> CITE-seq (Stoeckius et al., 2017) and<sup>2</sup> DOGMA-seq (Mimitou et al., 2021). Transcriptomic data can be used to generate unspliced and spliced count matrices. We assume a bursty transcription and constitutive translations with constitutive splicing and degradation. We derive the chemical master equation (CME) following Singh et al. (Singh and Bokes, 2012) and apply continuous approximation to protein when necessary. The resultant joint probability distribution of unspliced mRNA, spliced mRNA, and protein is solved numerically and used for parameter estimation.

mature RNA transcripts have been suggested (Singh and Bokes, 2012), we solve numerically for the probability distribution for such a system and demonstrate that this can be used to reliably infer biophysically meaningful parameters on real datasets. Our approach, summarized in Figure 3.1, provides a proof of principle for fitting biophysical models to multiomic data.

39

### **3.3 Results**

### **Model**

|Symbol|Meaning|
|---|---|
|_𝑘_∈R+|Burst frequency|
|_𝐵_∈N|Burst size|
|_𝑏_∈R|Mean burst size|
|_𝛽_∈R|Splicing rate of unspliced transcripts|
|_𝛾_∈R|Decay rate of spliced transcripts|
|_𝑘𝑝_∈R|Translation rate of spliced transcripts|
|_𝛾𝑝_∈R|Decay rate of proteins|
|_𝑋𝑢_∈N|Unspliced RNA copy number|
|_𝑋𝑠_∈N|Spliced RNA copy number|
|_𝑋𝑝_∈N|Protein copy number<br>|
|_𝑃_(_𝑥𝑢, 𝑥𝑠, 𝑥𝑝, 𝑡_)|Probability density of state(_𝑥𝑢, 𝑥𝑠, 𝑥𝑝_) ∈N<sup>3 </sup>at time_𝑡_|
|_𝐺_(_𝑧𝑢, 𝑧𝑠, 𝑧𝑝, 𝑡_)|Generating function (GF) of_𝑃_(_𝑥𝑢, 𝑥𝑠, 𝑥𝑝, 𝑡_)|
|_𝜙_(_𝑢𝑢, 𝑢𝑠, 𝑢𝑝, 𝑡_)|Factorial-cumulant GF log_𝐺_(_𝑢𝑢_+1_, 𝑢𝑠_+1_, 𝑢𝑝_+1_, 𝑡_)|
|_𝐹_(_𝑧𝑢_) =<br>1<br>_𝑏_+1−_𝑏𝑧𝑢_<br>|Generating function of_𝐵_, i.e., <sup>�∞</sup><br>_𝑛_=0 <sup>_𝑧𝑛_</sup><br>_𝑢_<sup>_𝑃_(</sup><sup>_𝐵_=</sup><sup>_𝑛_)</sup>|
|_𝑀_(_𝑢𝑢_) =<br>_𝑏𝑢𝑢_<br>1−_𝑏𝑢𝑢_|Transformation of the burst PGF, i.e.,_𝑀_(_𝑢𝑢_) = _𝐹_(1+_𝑢𝑢_) −1|


Table 3.1: Notation for the joint biophysical model, and expressions used for numerical solving of the steady-state probability distribution over unspliced, spliced, and protein counts.

We consider the bursting limit of the telegraph model as in Singh and Bokes (Singh and Bokes, 2012), with RNA processing from nascent to mature transcripts at a rate _𝛽_ , and translation rate per RNA molecule _𝑘 𝑝_ (see Table 3.1 for all parameter identifications). This system can be summarized in the following reactions.


As in Singh et al. (Singh and Bokes, 2012), we define the probability mass function _𝑃_ ( _𝑥𝑢, 𝑥𝑠, 𝑥 𝑝, 𝑡_ ), which evolves in this system according to:

40


We then use generating function methods to calculate the stationary distribution. As in (Gorin, Vastola, Fang, et al., 2022; Gans, 1960), we define the probability generating function, _𝐺_ , via


where **_z_** represents the vector of arguments ( _𝑧𝑢, 𝑧𝑠, 𝑧 𝑝_ ). We then define _𝜙_ via


Using the method of characteristics (see Appendix B.1), we arrive at the following system of equations:


which can be solved numerically (see Appendix B.2).

On top of the biological model, which is summarized in Figure 3.1 **Transcription + Translation Model** , we also incorporate a technical noise model to account for noise in the sequencing process following (Gorin and L. Pachter, 2022), with both RNA and protein counts assumed to undergo Poissonian sampling, whose parameters are optimized via grid search.

41


<!-- Start of picture text -->
a<br>b<br><!-- End of picture text -->

Figure 3.2: **Inference accuracy on simulations** a) Estimated parameters versus true parameters. b) Absolute errors versus true parameters.

### **Simulation**

First, we use simulated data to assess the accuracy of estimated parameters under our model. We simulated 100 genes by first drawing their true parameters from a biologically plausible range, then generating steady-state data using the Gillespie algorithm. The application of our mean-expression filter resulted in a final set of 46 genes. We applied our inference framework to these 46 simulated genes and were able to recover all of the parameters in the full, joint model with unspliced, spliced and protein counts. The inference accuracy is shown in Figure 3.2. Parameter estimates were generally accurate, except for two outliers whose protein degradation rates converged to the optimization lower bound. The two outliers reside in a regime of low mRNA and high protein expression, where absolute parameter values are less identifiable, and only the ratio of translation to protein degradation was correctly inferred. The simulation results suggest that we should exclude parameter estimates found at the optimization bounds when fitting to real datasets.

### **Fits to Real Data**

Given the simulation results, we first sought to apply the full model to the unspliced RNA, spliced RNA and protein counts from real datasets. However, we observed that unspliced counts are generally low and noisy, making it difficult to identify genes with high expression across all modalities. Therefore, we asked whether protein and spliced RNA counts are informative enough for inference. We refit the model using only the spliced mRNA and protein counts from the 46 simulated genes and found all parameters to be identifiable, though with a loss of accuracy in the splicing rate estimates (Figure 3.3). As we are more interested in the kinetic parameters related to translation, we decided to fit our model on the protein and spliced RNA counts

42


<!-- Start of picture text -->
a<br>b<br><!-- End of picture text -->

Figure 3.3: **Inference accuracy with only spliced mRNA and protein counts on simulations** a) Estimated parameters versus true parameters b) Absolute errors versus true parameters.

of real datasets for now. The full model can be used when data quality permits in the future.

In particular, we fit our model on the protein and spliced RNA counts from the following human PBMC datasets:

- 10k Human PBMCs Stained with TotalSeq™-B Human TBNK Cocktail, Chromium GEM-X Single Cell 3’ Universal 3’ Gene Expression dataset analyzed using Cell Ranger 8.0.0 (2024, March 13) (Genomics, 2024)

- 10K Human PBMCs, Gene Expression with a Panel of TotalSeq™-B Antibodies, analyzed using Cell Ranger 3.0.0, (2018, November 19) (Genomics, 2018)

We processed the raw transcript reads using kb-python (kallisto and bustools) to obtain spliced and unspliced RNA counts. We used the cell-by-protein count matrix provided by 10x Genomics. For protein complexes with subunits, we assumed that the presence of the complex indicates the presence of all constituent subunits, so we chose from among the subunits when mapping to RNA transcripts. More details on data processing can be found in Appendix B.3.

In Figure 3.4, we show the fits of our model to a few marker genes. The technical sampling parameters to which these fits correspond, and the optimal fitted biophysical parameters, are given in Appendix (B.3). The cells were subsetted to monocytes and T cells for the 2024 and 2018 datasets respectively.

43


Figure 3.4: Fits to genes. The color map shows the calculated probability density at the optimal biological parameters, on a logarithmic scale. The red scatter points are the observed distribution of mRNA vs protein counts over cells. The cells were subsetted to monocytes and T cells for the 10x 2024 (Genomics, 2024) and 2018 (Genomics, 2018) datasets respectively.

### **3.4 Discussion**

In this work we have presented and explored the power of fitting a joint biophysical model for RNA and protein to single-cell data, and extracted biophysically meaningful parameters. We have demonstrated the robustness of our fitting procedure for the full joint biophysical model via simulation. We have then shown that most of the biophysical parameters can also be inferred to some accuracy using only spliced and protein counts. This approach could be appropriate until the available data includes sufficiently comprehensive unspliced RNA measurements. We have used this reduced model to fit transcriptional rate parameters to CITE-seq data, and have shown that we can successfully reproduce the observed spliced-protein distributions.

44

Our work highlights the compatibility of current inference frameworks (Gorin, Vastola, and L. Pachter, 2023) with biophysical models including additional modalities, and we hope that others will continue our approach, perhaps by including chromatin accessibility measurements as an additional model layer. The method described here could also be straightforwardly extended to include principled biophysical clustering using meK-Means (Chari, Gorin, and L. Pachter, 2023). One limitation of our analysis is the simplification that surface proteins are a proxy for proteins produced within the cell. A non-instantaneous process of surface protein export would add another layer to the model, and the inclusion of protein export is a potential extension of this investigation. Additionally, length-dependent translation (Rogers et al., 2017) could be added to build on the picture provided here.

Overall, the approach outlined here represents a first foray into using biophysical modeling to disentangle transcriptional and translational parameters. With development, this method could provide a convenient avenue for determining metabolic rates in systems where direct experimental measurements are difficult to obtain. The full model presented here also provides a framework for the principled integration of single-cell unspliced, spliced, and protein count information. The power of this methodology will increase with the improved reliability of these measurement techniques.

### **Data and Code Availability**

A github repository with all of the datasets, scripts for fitting parameters, and the simulations presented here is available at: `https://github.com/pachterlab/ FFP_2025` .

### **Acknowledgments**

We thank Andrew LeDuc for helpful discussions. We also thank Charles Trimble for generously funding part of C.F.’s research.

### **References**

- Chari, Tushar, Gennady Gorin, and Lior Pachter (2023). “Biophysically Interpretable Inference of Cell Types from Multimodal Sequencing Data”. In: _bioRxiv : the preprint server for biology_ . 2023.09.17.558131. doi: `10.1101/2023.09.17. 558131` . url: `https://doi.org/10.1101/2023.09.17.558131` .

- Cheng, Zhandong et al. (2016). “Differential dynamics of the mammalian mRNA and protein expression response to misfolding stress”. In: _Molecular Systems Biology_ 12.1, p. 855. doi: `10.15252/msb.20156423` .

45

- Felce, Catherine, Gennady Gorin, and Lior S. Pachter (Dec. 2024). “Biophysical model for joint analysis of chromatin and RNA sequencing data”. In: _Physical Review E_ 110.6, p. 064405. doi: `10.1103/PhysRevE.110.064405` . url: `https: //doi.org/10.1103/PhysRevE.110.064405` .

- Franks,Alexander, EdoardoAiroldi,andNikolaiSlavov(May2017).“Post-transcriptional regulationacrosshumantissues”. In: _PLoSComputationalBiology_ 13.5,e1005535. doi: `10.1371/journal.pcbi.1005535` .

- Fu, N. et al. (2007). “Comparison of Protein and mRNA Expression Evolution in Humans and Chimpanzees”. In: _PLoS ONE_ 2.2, e216. doi: `10.1371/journal. pone.0000216` .

- Gans, P. J. (1960). “Open first order Stochastic processes”. In: _The Journal of Chemical Physics_ 33, pp. 691–694. doi: `10.1063/1.1731239` .

- Genomics, 10x (Nov. 2018). _10k PBMCs from a Healthy Donor - Gene Expression with a Panel of TotalSeq-B Antibodies Universal 3’ Gene Expression_ . 10x Genomics Datasets. Version Cell Ranger v3.0.0. Dataset analyzed using Cell Ranger v3.0.0. url: `https://www.10xgenomics.com/datasets/10- k- pbm-cs-from-a-healthy-donor-gene-expression-and-cell-surfaceprotein-3-standard-3-0-0` .

- (Oct. 2024). _10k Human PBMCs Stained with TotalSeq-B Human TBNK Cocktail, Chromium GEM-X Single Cell 3’ Gene Expression_ . 10x Genomics Datasets. Version Cell Ranger v8.0.0. Dataset analyzed using Cell Ranger v8.0.0. url: `https://www.10xgenomics.com/datasets/10k-human-pbmcs-stainedwith-totalseq-B-human-TBNK-cocktail-GEM-X` .

- Gorin, Gennady and Lior Pachter (2022). “Monod: mechanistic analysis of singlecell RNA sequencing count data”. In: _bioRxivorg_ , p. 2022.06.11.495771. doi: `10.1101/2022.06.11.495771` .

- Gorin, Gennady, John J. Vastola, Mingyu Fang, et al. (2022). “Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments”. In: _Nature Communications_ 13, p. 7620. doi: `10. 1038/s41467-022-34857-7` . url: `https://doi.org/10.1038/s41467022-34857-7` .

- Gorin, Gennady, John J. Vastola, and Lior Pachter (Oct. 2023). “Studying stochastic systems biology of the cell with single-cell genomics data”. In: _Cell Systems_ 14.10, 822–843.e22. issn: 24054712. doi: `10.1016/j.cels.2023.08.004` .

- Greenbaum, Dov et al. (Aug. 2003). “Comparing Protein Abundance and mRNA Expression Levels on a Genomic Scale”. In: _Genome Biology_ 4.9, p. 117. issn: 1474-760X. doi: `10.1186/gb-2003-4-9-117` .

- Huber, Martin et al. (2004). “Comparison of proteomic and genomic analyses of the human breast cancer cell line T47D and the antiestrogen-resistant derivative T47D-r”. In: _Molecular & Cellular Proteomics_ 3, pp. 43–55.

46

- Hughes, Alex J et al. (July 2014). “Single-Cell Western Blotting”. In: _Nature Methods_ 11.7, pp. 749–755. issn: 1548-7105. doi: `10.1038/nmeth.2992` .

- Ideker, Trey (2001). “Integrated genomic and proteomic analyses of a systematically perturbed metabolic network”. In: _Science_ 292, pp. 929–934.

- Junker, Jan Philipp et al. (Nov. 2014). “A Predictive Model of Bifunctional Transcription Factor Signaling during Embryonic Tissue Patterning”. In: _Developmental Cell_ 31.4, pp. 448–460. issn: 1534-5807. doi: `10.1016/j.devcel.2014.10. 017` . (Visited on 09/23/2025).

- Koussounadis, Antonis et al. (2015). “Relationship between differentially expressed mRNA and mRNA-protein correlations in a xenograft model system”. In: _Scientific Reports_ 5, p. 10775. doi: `10.1038/srep10775` .

- Kuersten, Sebastian and Elizabeth B. Goodwin (2003). “The power of the 3 UTR: translational control and development”. In: _Nature Reviews Genetics_ 4, pp. 626– 637. doi: `10.1038/nrg1125` .

- Liu, Yansheng, Andreas Beyer, and Ruedi Aebersold (2016). “On the Dependency of Cellular Protein Levels on mRNA Abundance”. In: _Cell_ 165.3, pp. 535–550. issn: 0092-8674. doi: `10.1016/j.cell.2016.03.014` .

- Maier, Tobias, Marc Güell, and Luis Serrano (2009). “Correlation of mRNA and protein in complex biological samples”. In: _FEBS Letters_ 583.24, pp. 3966–3973. doi: `10.1016/j.febslet.2009.10.036` .

- McManus, Joel, Zhe Cheng, and Christine Vogel (2015). “Next-generation analysis of gene expression regulation – comparing the roles of synthesis and degradation”. In: _Molecular BioSystems_ . doi: `10.1039/C5MB00310E` .

- Mimitou, Eleni P et al. (2021). “Scalable, multimodal profiling of chromatin accessibility, gene expression and protein levels in single cells”. In: _Nat. Biotechnol._ 39, pp. 1246–1258. doi: `10.1038/s41587-021-00927-2` .

- Nobori, Takanori et al. (2020). “Multidimensional gene regulatory landscape of a bacterial pathogen in plants”. In: _Nature Plants_ 6, pp. 883–896. doi: `10.1038/ s41477-020-0690-7` .

- Peterson, Vanessa M et al. (Oct. 2017). “Multiplexed Quantification of Proteins and Transcripts in Single Cells”. In: _Nature Biotechnology_ 35.10, pp. 936–939. issn: 1546-1696. doi: `10.1038/nbt.3973` .

- Rogers, David W. et al. (June 2017). “Ribosome reinitiation can explain lengthdependent translation of messenger RNA”. In: _PLoS Computational Biology_ 13.6, e1005592. doi: `10.1371/journal.pcbi.1005592` . url: `https://doi.org/ 10.1371/journal.pcbi.1005592` .

- Singh, Abhyudai and Pavol Bokes (Sept. 2012). “Consequences of mRNA transport on stochastic variability in protein levels”. en. In: _Biophys. J._ 103.5, pp. 1087– 1096.

47

- Stoeckius, Marlon et al. (2017). “Simultaneous epitope and transcriptome measurement in single cells”. In: _Nature Methods_ 14, pp. 865–868. doi: `10.1038/nmeth. 4380` .

- Teo, Guangyu et al. (2014). “PECA: a novel statistical tool for deconvoluting timedependent gene expression regulation”. In: _Journal of Proteome Research_ 13.1, pp. 29–37. doi: `10.1021/pr400855q` .

- Wang, Jin et al. (2018). “ATAC-Seq analysis reveals a widespread decrease of chromatin accessibility in age-related macular degeneration.” In: _Nature communications_ 9(1), 1364. doi: `https://doi.org/10.1038/s41467-018-03856-y` .

- Wei, Y. N. et al. (Feb. 2015). “Transcript and protein expression decoupling reveals RNA binding proteins and miRNAs as potential modulators of human aging”. In: _Genome Biology_ 16.1, p. 41. doi: `10.1186/s13059-015-0608-2` .

- Wu, Michael et al. (2020). “Transcriptional and proteomic insights into the host response in fatal COVID-19 cases”. In: _Proceedings of the National Academy of Sciences of the United States of America_ 117.45, pp. 28336–28343. doi: `10. 1073/pnas.2018030117` .

48

_C h a p t e r 4_

---

[← BIOPHYSICAL MODEL FOR JOINT ANALYSIS OF CHROMATIN AND RNA SEQUENCING DATA](07-biophysical-model-for-joint-analysis-of-chromatin-and-rna-se.md) · [Up: contents](index.md) · [BIOPHYSICS OF GENE EXPRESSION EVOLUTION →](09-biophysics-of-gene-expression-evolution.md)
