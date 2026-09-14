---
title: 'PART II: RESEARCH PAPERS'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf
source_file: sources/statomics-sga21/docs/backgroundProteomicsDataAnalysis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PART II: RESEARCH PAPERS

**Source:** [`docs/backgroundProteomicsDataAnalysis.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

113

114

|**8.SUMMARIZATION VS PEPTIDE-BASED MODELS IN**|
|---|
|**LABEL-FREE**<br>**QUANTITATIVE**<br>**PROTEOMICS:**|
|**PERFORMANCE,**<br>**PITFALLS,**<br>**AND**<br>**DATA**<br>**ANALYSIS**|
|**GUIDELINES**|


In chapter 8, we show that peptide-based models outperform summarization-based pipelines for the analysis of quantitative proteomics data. We also demonstrate that the predefined false discovery rate cut-offs for the detection of differentially regulated proteins can become problematic when differentially abundant (DA) proteins are highly abundant in one or more samples. We also show that care should be taken when data are interpreted from samples with spiked-in internal controls and from samples that contain a few very highly abundant proteins. For this work, I performed most of the data analysis and wrote the manuscript together with my co-authors.

Goeminne L.J.E.*, Argentini A.*, Martens L. and Clement L. (2015). **Summarization vs Peptide-Based Models in Label-Free Quantitative Proteomics: Performance, Pitfalls, and Data Analysis Guidelines.** _Journal of Proteome Research_ . 14(6), 2457-2465

* equal contributions


### **8.1. Abstract**

Quantitative label-free mass spectrometry is increasingly used to analyze the proteomes of complex biological samples. However, the choice of appropriate data analysis methods remains a major challenge. We therefore provide a rigorous comparison between peptidebased models and peptide-summarization-based pipelines. We show that peptide-based models outperform summarization-based pipelines in terms of sensitivity, specificity, accuracy, and precision. We also demonstrate that the predefined FDR cutoffs for the detection of differentially regulated proteins can become problematic when differentially expressed (DE) proteins are highly abundant in one or more samples. Care should therefore be taken when data are interpreted from samples with spiked-in internal controls and from samples that

115

contain a few very highly abundant proteins. We do, however, show that specific diagnostic plots can be used for assessing differentially expressed proteins and the overall quality of the obtained fold change estimates. Finally, our study also illustrates that imputation under the “missing by low abundance” assumption is beneficial for the detection of differential expression in proteins with low abundance, but it negatively affects moderately to highly abundant proteins. Hence, imputation strategies that are commonly implemented in standard proteomics software should be used with care.

### **8.2. Keywords**

data analysis; differential proteomics; linear model

### **8.3. Introduction**

Current high throughput mass spectrometry (MS) experiments enable the simultaneous identification and quantification of thousands of peptides and proteins in biological samples under various experimental conditions. These methods allow us to extend our understanding of biological processes and are important for the identification of biomarkers for the early detection, diagnosis, and prognosis of disease. Quantitative proteomics workflows broadly fall into two categories: labeled approaches and label-free approaches.(1) Labeled workflows rely on the labeling of proteins or peptides with isobaric or isotopic mass tags and are currently more commonly used. Label-free proteomics workflows, however, do not require these additional labor intensive and expensive sample processing steps.(2) Label-free approaches can perform quantitative proteome comparisons among an unlimited number of samples and can also be applied retroactively to previously acquired data.(3) Although label-free quantifications tend to have slightly higher coefficients of variation compared to SILAC labeling, label-free quantifications are more reproducible and can identify up to 60% more proteins than labeled quantifications.(4, 5)

A typical label-free shotgun MS-based proteomics workflow consists of (a) a protein extraction step followed by enzymatic digestion, (b) reverse phase high performance liquid chromatography (HPLC) separation, (c) mass spectrometry (MS), (d) a data analysis step involving the identification and quantification of peptides and proteins, and (e) a statistical analysis for assessing differential protein abundance.(6, 7) In a typical data-dependent analysis, selected peptides are isolated and fragmented, generating a fragmentation spectrum that is then used for peptide identification.(8) Technological constraints, however, limit the number of peptides in each fraction that can be selected for fragmentation. As the selection criteria typically involve the MS peak intensities in a particular time window, the identifications in MS-based experiments are inherently associated with the abundance of ionized peptides. Moreover, the steric effects of digestion enzymes(9) and differences in ionization efficiency favor particular peptides. Coeluting peptides heavily influence the observed MS intensities.(10) Hence, proteomics data suffer from nonrandom missing values and a large variability, rendering the development of reliable data analysis pipelines for quantitative proteomics a challenging task.(11)

The current data analysis strategies for label-free quantitative proteomics are typically based on spectral counting or peak intensities.(1) In the former approach, the number of peptide-tospectrum matches (PSMs) for a given peptide are counted, and these are then accumulated over all peptides from a given protein.(12) Even though these methods are very intuitive and easy to apply, they remain controversial.(13, 14) Moreover, these methods necessarily ignore a large part of the information available in high precision mass spectra and are not very efficient in detecting low fold changes.(15) Peak-intensity-based methods, however, use the maximum

116

intensity or the area under the peak as a proxy for peptide abundance and tend to produce more precise protein abundance estimates.(15) We therefore focus on these latter approaches.

Many peak-based data analysis methods for the preprocessing and differential analysis of quantitative label-free proteomics data have been described in the literature. Modular approaches consisting of a separate normalization, summarization, and data analysis step are commonly used.(16, 17) Peptides originating from the same protein can indeed be considered technical replicates and theoretically should lead to similar abundance estimates. However, the summarization of the peptide intensities into protein expression values is cumbersome, and most summarization-based methods do not correct for differences in peptide characteristics or for the between-sample differences in the number of peptides that are identified per protein. This might introduce bias and differences in uncertainty between the aggregated protein expression values, which are typically ignored in downstream data analysis steps. The aforementioned nonrandom character of missing peptides further exacerbates these issues.

In response, linear regression approaches have been developed that immediately estimate the differential abundance between the proteins from observed peptide intensities, and their authors have made bold claims on their performance.(18, 19) Objective comparisons and general guidelines for the practitioner are, however, still lacking, which impedes the dissemination of more efficient data analysis pipelines into the proteomics community.

In this paper, we therefore present a rigorous comparison among modular and peptide-based regression methods for analyzing label-free quantitative proteomics data. We exploit the availability of the benchmark data sets to provide insight into the performance differences and technological artifacts that often arise in label-free proteomics experiments. It should also be noted that the benchmark data used here present a range of concentration differences, which enables us to analyze the suitability of different methods for different situations (e.g., small abundance differences versus large abundance differences or few missing peptides versus many missing peptides across analyses). In section <u>2</u> we present the benchmark data, the different data analysis methods, and the performance criteria that will be used in our comparison. The results are presented and discussed in sections 3 and 4.

### **8.4. Materials and methods**

We used the publicly available data set from Study 6 of the Clinical Proteomic Technology Assessment for Cancer (CPTAC) Network(20) for assessing the performance of different data analytic workflows for quantitative label-free proteomics. In the CPTAC study, a mixture of 48 human proteins from the Sigma-Aldrich Universal Proteomics Standard 1 (UPS) was spiked into a 60 ng of protein/ μ L resuspended yeast lysate of _Saccharomyces cerevisiae_ strain BY4741 ( _MATa_ , _leu2 Δ 0_ , _met15 Δ 0_ , _ura3 Δ 0_ , and _his3 Δ 1_ ). Spike-ins were performed at five different concentrations: 0.25 fmol of UPS protein/ μ L (A), 0.74 fmol of UPS protein/ μ L (B), 2.22 fmol of UPS protein/ μ L (C), 6.67 fmol of UPS protein/ μ L (D), and 20 fmol of UPS protein/ μ L (E). The prepared samples were then sent to five different laboratories and analyzed on four different mass spectrometry platforms.

We identified peptides by searching the data using MaxQuant v1.5 against the yeast UniprotKB/Swiss-Prot protein database (v 15.14) to which the 48 UPS protein sequences were added. Detailed search settings can be found in the <u>Supporting Information. A general</u> overview of the number of identified peptides and proteins in our search can be found in Table S1, <u>Supporting Information. Statistical analyses were implemented in RStudio version</u>

117

0.98.978 (RStudio, Boston, MA) interfacing R 3.1.0 (“Spring Dance”). Standard Perseus analysis workflows were executed in Perseus version 1.5. We introduce two Perseus workflows in section 8.4.1, two different modular pipelines that aggregate peptide intensities into protein expression values in section 8.4.2, and three different peptide-based regression methods in section 8.4.3. The performance criteria used to compare the different methods can be found in section 8.4.4.

#### **8.4.1. Perseus-based workflows**

We used a typical workflow implemented in the software package Perseus. The analysis starts from (a) the LFQ intensities given in the Ma xQuant’s proteinGroups.txt file, which consist of normalized and summarized intensities at protein level. The MaxLFQ procedure then proceeds as follows: for all pairwise comparisons of a protein between samples, the median ratio for the common peptides in both samples is calculated. Next, the abundance protein profile that optimally satisfies these protein ratios is reconstructed with a least-squares regression model. The whole profile is then rescaled to the cumulative intensity across the samples with preservation of the total summed intensity for a protein across the samples. As the resulting LFQ intensities are already normalized by the MaxLFQ procedure,(21) no additional normalization step is required. In (b), the LFQ protein intensities are read into Perseus. The proteins that are only identified by a modification site, the contaminants, and the reversed sequences are removed from the data set, and the remaining intensities are log2-transformed. Next, (c) involves the imputation of missing values using Perseus’ standard settings. <u>(22)</u> Finally, (d) consists of inference by pairwise two-sample _t_ tests. The multiple testing problem is addressed using the Benjamini – Hochberg False Discovery Rate (FDR) procedure.(23) The (a) – (d) pipeline is referred to as perseusImp. We also consider a second variant, perseusNoImp, in which the imputation step (c) is omitted.

#### **8.4.2. Summarization-based workflows**

A typical modular workflow for quantitative proteomics consists of a normalization, summarization, and statistical analysis step.(6, 7) In our contribution, we assess two customized pipelines that build upon popular mean and median summarization strategies for the summarization of peptide intensities into protein expression values. The following steps are considered in the analysis pipelines: (a) the intensities from MaxQuant’s peptides.txt output file are log2-transformed and normalized using quantile normalization (with the peptides mapping to reversed sequences or mapping to multiple proteins being removed from the data), (b) peptide intensities are aggregated into protein expression values using mean or median summarization, and (c) summarized protein expression values are further analyzed using empirical Bayes moderated _t_ tests implemented in the R/Bioconductor package “limma”. <u>(24)</u> The Benjamini – Hochberg FDR procedure is used to correct for multiple testing. The two resulting methods are referred to as limmaMean and limmaMedian.

In the limma analysis, the following model is considered for each protein i:

𝑦𝑖𝑘𝑙 = 𝑡𝑟𝑒𝑎𝑡𝑖𝑘 + 𝑒𝑥𝑝𝑖𝑙 + 𝜀𝑖𝑘𝑙, (1)

with 𝑦𝑖𝑘𝑙 being the aggregated protein intensity for the k-th treatment ( _treat_ ) and the l-th experiment ( _exp_ ) correcting for (lab × instrument × repeat) batch effects. ε ikl is a random error term that is assumed to be normally distributed with mean 0 and variance 𝜎𝑖2. Note that the _treat_ effect is the effect of interest. Contrasts between _treat_ parameters can be interpreted as log2 fold changes for protein i. For instance, k = A indicates condition A (spike-in concentration of 0.25 fmol of UPS protein/μL) and k = E indicates condition E (spike-in concentration of 20

118

fmol of UPS protein/μL). If so, then 𝑡𝑟𝑒𝑎𝑡𝑖𝐸 −𝑡𝑟𝑒𝑎𝑡𝑖𝐴 indicates the expected log2 difference in concentration for protein i between group E and group A. The statistical significance of the contrasts can be addressed by using _t_ tests. The limma analysis exploits the massively parallel nature of quantitative proteomics experiments and allows for the borrowing of strength across proteins to estimate the error variance, i.e., makes use of a moderated empirical Bayes variance estimator 𝑠̃𝑖2:


with 𝑠𝑖 and 𝑑𝑖 being the standard deviation and the residual degrees of freedom for protein i, respectively, 𝑠0 the estimated prior standard deviation, and 𝑑0 the prior degrees of freedom. Both the prior standard deviation and the prior degrees of freedom are estimated using empirical Bayes by pooling information across all proteins. Hence, the protein-based variance 𝑠𝑖2 is shrunk toward a common variance 𝑠02, leading to more stable variance estimates (𝑠̃𝑖2). Note that the degrees of freedom from the moderated _t_ test also increase to _d_ 0 + _d_ i. Detailed information can be found in the work of Smyth.(24)

#### **8.4.3. Peptide-based models**

Peptide-based models use the MaxQuant peptides.txt file as input. In (a), the extracted peptide intensities are log2-transformed and quantile normalized (Figures S8 and S9, <u>Supporting Information), and peptides mapping to reversed sequences or mapping to multiple proteins are</u> removed from the data. In (b), the peptide data are modeled with three different candidate models. In (c), inference is done by pairwise contrast testing. Multiple testing is addressed using the Benjamini – Hochberg FDR.

##### **Linear Model without Sample Effect**

For each protein i, the following model is proposed:


with 𝑦𝑖𝑗𝑘𝑙𝑚 being the log2-transformed intensity for the j-th peptide sequence 𝑝𝑒𝑝𝑖𝑗 of the k-th treatment 𝑡𝑟𝑒𝑎𝑡𝑖𝑘 and the l-th experiment 𝑒𝑥𝑝𝑖𝑙. 𝜀𝑖𝑗𝑘𝑙𝑚 is a normally distributed error term with mean 0 and variance σ _i_<sup>2</sup> . The index m refers to multiple spectra that are identified for the same peptide in the same experiment and the same treatment. Contrasts in 𝑡𝑟𝑒𝑎𝑡𝑖𝑘 parameters can again be interpreted as log2 fold changes for protein i. The model also incorporates a 𝑝𝑒𝑝𝑖𝑗 effect to account for peptide-specific fluctuations around the mean protein intensity, which originate from differences in digestion and ionization efficiency, among others.(9)

##### **Linear Model with Sample Effect**

Model <u>2</u> is extended by incorporating an additional sample effect, 𝑠𝑎𝑚𝑝𝑙𝑒𝑖𝑘𝑙, to capture deviations specific to each MS run (lab × instrument × treatment × repeat):


Note that all remaining effects are similar to those of model 2.

##### **Mixed Model with Random Sample Effect**

The mixed model extends the linear model 3 by putting a normal prior on the sample effect, 𝑠𝑎𝑚𝑝𝑙𝑒𝑖𝑘𝑙 ∼𝑁(0, 𝜎𝑠𝑎𝑚𝑝𝑙𝑒,𝑖2 ). This model accounts for the correlation within samples and

119

incorporates both within- and between-sample variability when inference is performed on contrasts in the 𝑡𝑟𝑒𝑎𝑡𝑖𝑘 effects. The degrees of freedom of the _t_ tests are approximated using the Satterthwaite approximation,(25) and the Benjamini – Hochberg FDR procedure is used to account for multiple testing.(23)

#### **8.4.4. Performance**

For each method, _p_ values are converted to _q_ values using the Benjamini – Hochberg FDR procedure,(23) and a cutoff is set at 5% FDR. At this level, the number of false positives (FP), true positives (TP), false negatives (FN), and true negatives (TN) are recorded, and the nominal FDR level is compared to the observed false discovery rate FDR̅̅̅̅̅̅ = FP/(FP + TP). Note that the observed FDR equals 1 minus the positive predictive value, PPV = TP/(FP + TP).

The ROC curves are constructed on the basis of the ordering of the _p_ values. Bias (Figures S4 and S5, <u>Supporting Information), standard deviation (sd), median absolute deviation (mad),</u> and root mean squared error (RMSE) (Figures S6 and S7, <u>Supporting Information) are</u> calculated both for yeast and for UPS proteins. We also calculated the F1 score, which is defined as the harmonic mean of the PPV and the sensitivity. Higher F1 scores indicate that a method provides a good balance between the PPV and the recall (Figures S1 and S2, <u>Supporting Information).</u>

### **8.5. Results**

We investigated the sensitivity, specificity, and F1 score of the test procedure as well as the accuracy and the precision of the fold change (FC) estimates for three peptide-based methods and four summarization-based data analysis pipelines using the CPTAC Study 6 data set.(20) This data set consists of samples with a uniform yeast proteome background in which human UPS peptides are spiked at five different concentrations (0.25, 0.74, 2.22, 6.67, and 20 fmol/μL). All 10 pairwise comparisons are assessed in each analysis. The following peptide - based methods are considered: a linear model without sample effect (lmNoSamp), a linear model with sample effect (lmSamp), and a mixed model with a random sample effect (mixedSamp). The summarization-based approaches consist of mean and median summarizations of peptides into protein expression values followed by limma analyses (limmaMean and limmaMedian) as well as the more advanced MaxLFQ summarization(21) followed by a standard Perseus workflow with and without imputation (perseusImp and perseusNoImp). All peptide identifications and intensities were based on MaxQuant so as to avoid biases due to the search engine or peak intensity calculation algorithm.

Receiver operating characteristic (ROC) curves for the four comparisons with the smallest differences in spiked-in protein abundance (B – A, C – B, D – C, and E – D) are shown in Figure 1. Detecting the differential abundance of UPS proteins is most challenging in these comparisons as they only involve fold changes (FCs) very close to 3. ROC curves for the six remaining comparisons can be found in Figure S1 in the Supporting Information. Figure <u>1</u> shows that the lmNoSamp and mixedSamp models clearly outperform the other methods. The lmNoSamp, mixedSamp, and perseusImp workflows do control the FDR at 5% for comparisons B – A, C – A, and C – B, but perseusNoImp could only control the FDR for comparisons B – A and C – B, and both limmaMean and limmaMedian could only control the FDR for comparison B – A (see Tables S2 – S8 and S12 in the <u>Supporting Information). The lmSamp method is unable to</u> control the FDR. When differences in spiked-in concentrations increase, however, none of the methods are able to control the FDR correctly (Tables S2 – S8 and S12 in the <u>Supporting Information). lmSamp is more conservative but cannot control its FDR at 5%, either. The ROC</u>

120

curves also show that the mean summarization outperforms the more robust but less efficient median summarization.


**Figure 8.1.** Receiver operating characteristic (ROC) curves for the seven analysis methods in comparisons B – A, C – B, D – C, and E – D. The UPS proteins in these comparisons were spiked in at a ratio close to 3:1. Dots denote the estimated cutoff for each method at 5% FDR. The termination of the curve before the point (1, 1) indicates either that proteins are prematurely removed from the analysis (e.g., for the Perseus workflows) or that there is an inability of the models to fit a protein with too few observations (e.g., for peptide-based models).

As only a part of the ROC curve is relevant in practice, i.e., that experimenters typically want to restrict the number of candidate proteins for validation in follow-up experiments, we also compared the relative partial areas under the curve (rpAUC) for FPR <0.1. Relative pAUCs (Table 8.1) are obtained by dividing pAUC values (Table S13, Supporting Information) by the maximum pAUC value of 0.1. Table 8.1 also demonstrates that the lmNoSamp and mixedSamp models are superior to the competing pipelines in terms of pAUC. Their power is higher in spite of the fact that no information is borrowed across proteins for estimating the variance (as compared to the limma workflows) and that there is an absence of imputation (as

121

compared to the standard Perseus method). perseusImp outperforms limmaMean and limmaMedian in terms of pAUC when differential expression in very-low-abundance proteins needs to be detected (e.g., comparison B – A). In these situations, imputation under the assumption of low abundance strongly boosts the performance of the method. The perseusImp workflow outperforms the perseusNoImp workflow for all comparisons involving A, i.e., when very-low-abundance differentially expressed (DE) proteins are involved in the comparison. But in comparisons with more abundant UPS spikes, the opposite is observed, and perseusImp shows a suboptimal performance compared to that of perseusNoImp.

**Table 8.1.** Relative Partial Area under the Curve (rpAUC) for FPR <0.1 for All Seven Models for Each of the Ten Comparisons<sup>34</sup> .

|**CP**|**lm**<br>**NoSamp**|**lmSamp**|**mixed**<br>**Samp**|**perseus**<br>**Imp**|**perseus**<br>**NoImp**|**limma**<br>**Mean**|**limma**<br>**Median**|
|---|---|---|---|---|---|---|---|
|B-A|83.01%|12.41%|83.93%|69.65%|55.70%|68.14%|56.21%|
|C-A|98.33%|49.31%|98.60%|85.93%|59.76%|87.22%|77.26%|
|D-A|99.20%|72.65%|99.26%|86.31%|63.42%|96.79%|95.18%|
|E-A|99.72%|89.06%|99.72%|89.62%|63.79%|97.92%|95.93%|
|C-B|95.10%|77.81%|94.60%|52.45%|70.08%|61.79%|50.54%|
|D-B|97.05%|89.60%|96.72%|71.00%|72.06%|89.21%|83.54%|
|E-B|96.98%|93.50%|95.90%|77.68%|72.41%|90.94%|87.69%|
|D-C|96.51%|84.85%|96.01%|64.48%|67.09%|59.77%|54.25%|
|E-C|97.34%|94.48%|96.21%|72.92%|74.85%|81.94%|79.23%|
|E-D|94.06%|79.45%|92.76%|71.13%|78.02%|74.16%|71.21%|
|Mean|95.73%|74.31%|95.37%|74.12%|67.72%|80.79%|75.11%|


When the F1 score is examined, the lmNoSamp and mixedSamp models show very comparable patterns (Figure S2, <u>Supporting Information). In comparisons E</u> – A, E – B, E – C, and D – B, the lmSamp is superior to the other peptide-based models. This is most likely due to its more conservative nature. lmNoSamp and mixedSamp suffer from many false positives for these comparisons. For the summarization-based models (Figure S3, <u>Supporting Information),</u> we notice that perseusNoImp outperforms the other summarization-based methods for most comparisons. In comparisons D – A, D – B, E – A, E – B, and E – C, perseusImp shows a higher F1 score than Perseus without imputation. Again, the mean summarization method almost consistently outperforms the median summarization in terms of F1 score, although the differences are generally not very large.

The accuracy and precision of the pipelines are assessed by comparing the differential expression estimates to the true log2 fold changes of the spiked UPS peptides [log2 FC ≈ log2(3), log2(9), log2(27), and log2(80)] and the yeast peptides (log2 FC = 0). Figures 8.2 and 8.3 show boxplots of the different DE estimates of the different methods for UPS and yeast proteins, respectively. The actual log2 FC is also indicated in the plot.

> 34 The UPS proteins were spiked in at concentrations ranging from 0.25 –20 fmol/μL (conditions A– E).

122


**Figure 8.2.** Boxplots showing the distributions of the DE estimates of the UPS proteins for each of the seven methods in each of the 10 comparisons. Outliers are not shown. The actual fold changes of the spikes are indicated with the yellow horizontal lines.


**Figure 8.3.** Boxplots showing the distributions of the DE estimates of the yeast proteins for each of the seven methods in each of the 10 comparisons. Outliers are not shown. All samples consisted of the same yeast background. Hence, no differential expression should occur for these proteins.

Figure 8.2 illustrates that the lmNoSamp and mixedSamp models are superior to the other methods in terms of both the accuracy and the precision of the FC estimates for the differentially abundant UPS proteins. The mean and median summarization methods systematically show a downward bias (Figure S4, Supporting Information). The bias is more pronounced in comparisons involving condition A. In condition A, the lowest concentration UPS (0.25 fmol/μL) is spiked in and, consequently, fewer UPS peptides are identified. Missingness, however, can be expected to involve peptides with a lower ionization efficiency, which typically display lower peak intensities than other peptides of the same protein. The simple mean and median summarization methods do not correct for differences in peptide characteristics, leading to an overestimation of the expression value for UPS proteins in condition A. This leads to moderation of the log2 fold change estimates involving condition A. Peptide-based pipelines

123

correcting for peptide effects also suffer from a slight negative bias in comparisons that involve condition A. Note that imputation has a severe impact on the precision. Figure S7 in the <u>Supporting Information</u> also shows that summarization-based limmaMean and limmaMedian methods give the highest root mean squared error (RMSE = [bias<sup>2</sup> /variance]<sup>1/2</sup> ) among all methods that were evaluated.

Figure 8.3 confirms that the lmNoSamp and the mixedSamp models are favorable in terms of accuracy and precision. For the yeast proteins (non-DE), the median and mean summarization methods show a bias similar to that of competing methods. An increasing downward bias of the log2 FC estimates can be observed for the null proteins (yeast) in comparisons involving increasing UPS concentrations. This becomes very apparent for comparisons that involve condition E. In this condition, a very high fraction of the total protein mass in the sample consists of UPS proteins. Hence, yeast peptides are likely to be masked by UPS, leading to an underestimation of the abundance of yeast peptides in the D and E mix. Most false positive yeast proteins had negative log2 FC estimates as opposed to the spiked UPS proteins, which show positive log2 FC estimates in each comparison. Therefore, issues involving the FDR are likely to be linked to the extreme sample composition under conditions D and E, which invokes an MS bias.(10) The F1 score masks this artifact, as it combines PPV and sensitivity. The same trend is also visible in MA plots for the linear model without sample effect (Figures S10 and S11, <u>Supporting Information). In these graphs, the average FC is plotted in function of the</u> average protein expression for a particular comparison. These graphs are therefore very helpful for screening for artifacts induced by the technical and data analysis workflows. Figure 8.3 also illustrates that the precision reduces with increasing FC, i.e., for comparisons involving conditions D and E. Finally, the lmSamp method shows a dramatic decrease in precision for comparison B – A. This is a data analysis artifact; the model is overidentified for many proteins, leading to the aliasing of sample and treatment effects. Due to the specific model parametrization, the overidentification has a larger impact on comparisons involving condition A.

We also investigated alternative data analysis strategies to alleviate this problem. For the peptide-based lmNoSamp method, we assessed the impact of testing against the median log2 FC of all proteins instead of testing against 0. This slightly improves the observed FDR except for comparisons C – A and D – B and improves the rpAUC except for comparisons D – A, D – B, D – C, and E – C (Table S14, <u>Supporting Information). However, the method still returns too</u> many false positives for the comparisons involving high concentrations (Table S9, Supporting <u>Information). For the summarization-based methods, we assessed the impact of switching the</u> order of the normalization and summarization steps. When the quantile normalization is performed after summarization, the observed FDR improved for comparisons involving D and E, but the performance decreased dramatically for comparisons B – A and C – A (Tables S10 – S12. Supporting Information). The ROC curves also suggest that switching the order of the normalization and summarization steps deteriorates the performance of the limmaMean and limmaMedian workflows (Figure S12, Supporting Information).

### **8.6. Discussion**

Our analysis showed that peptide-based models perspicuously outperform summarizationbased methods. Both the linear model without sample effect and the mixed model outperform the other methods in terms of accuracy, precision, sensitivity, and specificity. The ROC curves clearly indicate that these methods produce a more reliable ordering of DE proteins than the competing methods. The linear model with sample effect has a suboptimal performance but still outperforms the other methods in comparisons that do not involve A. Due to selective and periodic sampling in both MS stages, not all peptides are being observed or identified in all

124

samples. Moreover, intensities from different peptides of the same protein vary considerably due to differences in cleavage and ionization efficiency among others.(26, 27) Summarization thus typically involves different peptides and a different number of peptides in each sample. This leads to protein expression values with distinct characteristics, which induces bias and incorrect precision of the fold change estimates.

Peptide-based models are superior in correcting for individual peptide effects, which are typically quite strong(18, 19) and accounting for the different number of peptides in each sample. Thus, bias is reduced and improved precision estimates are provided, leading to higher sensitivity and specificity. The mixed model can also account for the correlation that is present in peptides from the same protein within a sample. The peptide-based models with a fixed sample effect suffer from the unstable estimation of fold changes and variance components due to the overfitting of sparse proteins identified by a few peptides. Moreover, the inclusion of a fixed sample effect eliminates the between-sample variability from the analysis. Inference between the samples will be based on an underestimated variance, leading to a higher number of false positives in a top list. In the linear model without sample effect, fewer parameters have to be estimated, and the variances within and between samples are combined in the error term. Hence, the method is less prone to overfitting and incorporates both within- and between-sample variability in the test statistics, leading to a better control of the number of false positives. However, the method does not account for the correlation between peptides from a particular protein within a sample. The mixed modeling approach with a random sample effect does incorporate within- and between-sample variances as well as the within-sample correlation between peptides of the same protein. The mixed model and the linear model without sample effect are more or less on par in terms of all assessed performance criteria. Hence, the increased computational complexity of the mixed model cannot be justified for this particular application. However, in real experiments, more correlation can be expected due to the additional biological variation among samples.

We also showed that the use of FDR thresholds might be flawed under certain experimental conditions. This was observed for comparisons involving conditions D and E, i.e., the samples with the highest spiked-in UPS concentrations. Under these conditions, the UPS proteins correspond to a considerable fraction of the total protein mass in the sample. The ROC curves show that peptide-based methods still produce reliable top lists with a superb ordering, but the use of a 5% FDR threshold was too liberal. Hence, long protein lists are produced with many false positives. The majority of these false positives, however, had FC estimates in the opposite direction as those of spiked UPS proteins. This was due to a systematic downward bias in the FC estimates of nondifferentially expressed yeast proteins. Competitive ionization makes the identification and quantification of yeast peptides cumbersome in samples with highly concentrated UPS spikes. Thus, the majority of false positives originate from technological artifacts rather than from flaws in the data analysis pipeline. We therefore recommend that researchers who are planning to use internal controls in their MS experiments avoid overspiking, as this can have detrimental effects on the quantification of the proteins of interest. Moreover, artifacts similar to those from spiked UPS proteins are bound to occur in certain experimental setups (e.g., undepleted blood plasma proteomic samples are known to be dominated by a few highly abundant proteins, and undepleted green tissue samples from plants will suffer from the omnipresence of RuBisCo). Our analysis showed that experimenters should interpret proteins further down the DE list with care. We therefore advise data analysts to use diagnostic plots based on all fold change estimates for assessing the quality of the FC estimates and for detecting potential artifacts. MA plots and boxplots were shown to be well suited for evaluating candidate DE proteins, to flag critical experimental conditions as well as flaws in the data analysis pipeline.

125

The myriad missing values in quantitative proteomic experiments present severe challenges to the data analysis. The standard MaxQuant pipeline therefore utilizes the match-between runs option to boost the number of peptide intensities that different samples have in common. Moreover, Perseus also incorporates imputation-based routines to deal with missing protein expression values. We showed that imputation is beneficial for detecting differentially expressed proteins with low abundance but performs suboptimally for moderately to highly abundant proteins. Perseus’ standard imputation algorithm assumes that missing values originate from lower intensity values. Hence, the imputation can lead to a downward bias for more abundant proteins. Moreover, experimenters should also be aware that imputation comes at the cost of a decreased precision for the FC estimates.

In general, the current peptide-based methods are prone to overfitting and rely on protein-byprotein variance estimates. Hence, the development of robust methods that can borrow information across peptides and proteins would enable proteomics researchers to further deploy label-free quantitative proteomics.

In summary, we have shown that issues inherent to the methodology create challenges in quantitative proteomics, even in highly controlled and standardized samples such as the CPTAC ones. We then go on to show that downstream statistical data analysis approaches differ in their ability to cope with these different issues, and that the importance of these issues depends on the characteristics of the sample under study (e.g., the dominance of a few highly abundant proteins or large protein concentration ratio differences between two samples). Crucial, perhaps, is the fact that although peptide-based approaches fare better than summarization methods, no single method currently exists that can easily tackle all possible issues in quantitative proteomics data. Hence, more sophisticated data processing approaches that recognize these various issues are needed and can compensate for such issues more successfully across the board.

### **8.7. Conclusion**

In this paper, we compared the performance of peptide-based linear models, mean and median summarization followed by limma analysis, and the standard MaxQuant/Perseus workflow for assessing differential abundance in label-free quantitative proteomics experiments. The evaluation of the performance was assessed using the CPTAC benchmark data set. Peptidebased models outperformed the competing data analysis pipelines in terms of sensitivity, specificity, accuracy, and precision. Modeling quantitative proteomics data at the peptide level allows for the correction of strong peptide-specific effects, which avoids the bias associated with summarization-based methods that aggregate different types of peptide intensities into a single value. Moreover, peptide-based models also improve the precision estimates by accounting for the different numbers of peptides that are identified in a sample. We have also shown that the FDR cutoffs used to determine the length of lists with significant differentially expressed (DE) proteins could become problematic in experimental setups with samples that are dominated by a few very abundant proteins. Technological artifacts might induce bias in the non-DE proteins, which can inflate the number of false positives that are returned at a particular FDR level. However, the ordering of the top DE proteins in the lists was shown to remain valid. We therefore advise proteomics researchers to be careful when spiking internal controls, to deplete the highly abundant proteins, and to use diagnostic plots for assessing the candidate DE proteins as well as the overall quality of the obtained fold change estimates. Finally, standard proteomics software provides experimenters with the ability to impute missing values. Perseus’ imputation strategy was shown to be beneficial for detecting DE proteins with low abundance but at the cost of reduced precision as well as a suboptimal performance for

126

moderately to highly abundant DE proteins. Hence, we advise proteomics data analysts to use imputation strategies with care.

### **8.8. Supporting information**

Figures showing the receiver operating characteristic (ROC) curves for the seven analysis methods in comparisons, F1 scores for the studied models, comparison of the bias terms for yeast and UPS proteins, comparisons of the root mean squared error for yeast and UPS proteins, boxplots showing log2 peptide intensities, MA plots for linear models, and ROC curves for normalization on the peptide and protein level with mean and median aggregation. Tables showing a general overview per spike-in conditions for UPS and yeast proteins, characteristics for various models and workflows, an explanation of the outlined characteristics, partial areas under the curves for a false positive rate, and relative partial areas under the curves for a false positive rate. The Supporting Information is available free of charge on the ACS Publications <u>website</u> at DOI: 10.1021/pr501223t.

<u>pr501223t_si_001.pdf (1.38 MB)</u>

### **8.9. Acknowledgement**

Part of this research was supported by IAP research network “StUDyS” grant no. P7/06 of the Belgian government (Belgian Science Policy) and the Multidisciplinary Research Partnership “Bioinformatics: From Nucleotides to Networks” of Ghent University. A.A. is supported by the IWT SBO grant “INSPECTOR” (120025). L.J.E.G. is supported by the IWT SBO grant “Differential Proteomics at Peptide, Protein, and Module Level” (141573). L.M. acknowledges the PRIME-XS project, grant agreement no. 262067, funded by the European Union Seventh Framework Program.

### **8.10. References**

This article references 27 other publications.

**1.** Vaudel, M.; Sickmann, A.; Martens, L. Peptide and protein quantification: A map of the minefield Proteomics 2010, 10 (4) 650 – 670

**2.** Bluemlein, K.; Ralser, M. Monitoring protein expression in whole-cell extracts by targeted label- and standard-free LC-MS/MS Nat. Protoc. 2011, 6 (6) 859 – 869

**3.** Cox, J.; Hein, M. Y.; Luber, C. A.; Paron, I.; Nagaraj, N.; Mann, M. Accurate proteome-wide label-free quantification by delayed normalization and maximal peptide ratio extraction, termed MaxLFQ Mol. Cell. Proteomics 2014, 13 (9) 2513 – 2526

**4.** Liu, N. Q.; Dekker, L. J. M.; Stingl, C.; Güzel, C.; De Marchi, T.; Martens, J. W. M.; Foekens, J. A.; Luider, T. M.; Umar, A. Quantitative Proteomic Analysis of Microdissected Breast Cancer Tissues: Comparison of Label-Free and SILAC-based Quantification with Shotgun, Directed, and Targeted MS Approaches J. Proteome Res. 2013, 12 (10) 4627 – 4641

**5.** Mosley, A. L.; Sardiu, M. E.; Pattenden, S. G.; Workman, J. L.; Florens, L.; Washburn, M. P. Highly Reproducible Label Free Quantitative Proteomic Analysis of RNA Polymerase Complexes Mol. Cell. Proteomics 2011, DOI: 10.1074/mcp.M110.000687

**6.** Wang, G.; Wu, W. W.; Zeng, W.; Chou, C.-L.; Shen, R.-F. Label-Free Protein Quantification Using LC-Coupled Ion Trap or FT Mass Spectrometry: Reproducibility, Linearity, and Application with Complex Proteomes J. Proteome Res. 2006, 5 (5) 1214 – 1223

127

**7.** Silva, J. C.; Gorenstein, M. V.; Li, G.-Z.; Vissers, J. P. C.; Geromanos, S. J. Absolute Quantification of Proteins by LCMSE: A Virtue of Parallel ms Acquisition Mol. Cell. Proteomics 2006, 5 (1) 144 – 156

**8.** Vaudel, M.; Sickmann, A.; Martens, L. Current methods for global proteome identification Expert Rev. Proteomics 2012, 9 (5) 519 – 532

**9.** Peng, M.; Taouatas, N.; Cappadona, S.; van Breukelen, B.; Mohammed, S.; Scholten, A.; Heck, A. J. R. Protease bias in absolute protein quantitation Nat. Methods 2012, 9 (6) 524 – 525

**10.** Schliekelman, P.; Liu, S. Quantifying the Effect of Competition for Detection between Coeluting Peptides on Detection Probabilities in Mass-Spectrometry-Based Proteomics J. Proteome Res. 2013, 13 (2) 348 – 361

**11.** Kumar, C.; Mann, M. Bioinformatics analysis of mass spectrometry-based proteomics data sets FEBS Lett. 2009, 583 (11) 1703 – 1712

**12.** Liu, H.; Sadygov, R. G.; Yates, J. R. A Model for Random Sampling and Estimation of Relative Protein Abundance in Shotgun Proteomics Anal. Chem. 2004, 76 (14) 4193 – 4201

**13.** Bantscheff, M.; Schirle, M.; Sweetman, G.; Rick, J.; Kuster, B. Quantitative mass spectrometry in proteomics: a critical review Anal. Bioanal. Chem. 2007, 389 (4) 1017 – 31

**14.** Mueller, L. N.; Brusniak, M.-Y.; Mani, D. R.; Aebersold, R. An Assessment of Software Solutions for the Analysis of Mass Spectrometry Based Quantitative Proteomics Data J. Proteome Res. 2008, 7 (1) 51 – 61

**15.** Old, W. M.; Meyer-Arendt, K.; Aveline-Wolf, L.; Pierce, K. G.; Mendoza, A.; Sevinsky, J. R.; Resing, K. A.; Ahn, N. G. Comparison of Label-free Methods for Quantifying Human Proteins by Shotgun Proteomics Mol. Cell. Proteomics 2005, 4 (10) 1487 – 1502

**16.** Théron, L.; Gueugneau, M.; Coudy, C.; Viala, D.; Bijlsma, A.; Butler-Browne, G.; Maier, A.; Béchet, D.; Chambon, C. Label-free Quantitative Protein Profiling of vastus lateralis Muscle During Human Aging Mol. Cell. Proteomics 2014, 13 (1) 283 – 294

**17.** Hubner, N. C.; Bird, A. W.; Cox, J.; Splettstoesser, B.; Bandilla, P.; Poser, I.; Hyman, A.; Mann, M. Quantitative proteomics combined with BAC TransgeneOmics reveals in vivo protein interactions J. Cell Biol. 2010, 189 (4) 739 – 754

**18.** Clough, T.; Key, M.; Ott, I.; Ragg, S.; Schadow, G.; Vitek, O. Protein Quantification in LabelFree LC-MS Experiments J. Proteome Res. 2009, 8 (11) 5275 – 5284

**19.** Karpievitch, Y.; Stanley, J.; Taverner, T.; Huang, J.; Adkins, J. N.; Ansong, C.; Heffron, F.; Metz, T. O.; Qian, W.-J.; Yoon, H.; Smith, R. D.; Dabney, A. R. A statistical framework for protein quantitation in bottom-up MS-based proteomics Bioinformatics 2009, 25 (16) 2028 – 2034

**20.** Paulovich, A. G.; Billheimer, D.; Ham, A.-J. L.; Vega-Montoto, L.; Rudnick, P. A.; Tabb, D. L.; Wang, P.; Blackman, R. K.; Bunk, D. M.; Cardasis, H. L.; Clauser, K. R.; Kinsinger, C. R.; Schilling, B.; Tegeler, T. J.; Variyath, A. M.; Wang, M.; Whiteaker, J. R.; Zimmerman, L. J.; Fenyo, D.; Carr, S. A.; Fisher, S. J.; Gibson, B. W.; Mesri, M.; Neubert, T. A.; Regnier, F. E.; Rodriguez, H.; Spiegelman, C.; Stein, S. E.; Tempst, P.; Liebler, D. C. Interlaboratory Study Characterizing a Yeast Performance Standard for Benchmarking LC-MS Platform Performance Mol. Cell. Proteomics 2010, 9 (2) 242 – 254

128

**21.** Cox, J.; Hein, M. Y.; Luber, C. A.; Paron, I.; Nagaraj, N.; Mann, M. Accurate Proteomewide Label-free Quantification by Delayed Normalization and Maximal Peptide Ratio Extraction, Termed MaxLFQ Mol. Cell. Proteomics 2014, 13 (9) 2513 – 2526

**22.** Cox, J.; Mann, M. MaxQuant enables high peptide identification rates, individualized p.p.b.range mass accuracies and proteome-wide protein quantification Nat. Biotechnol. 2008, 26 (12) 1367 – 1372

**23.** Benjamini, Y.; Hochberg, Y. Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing J. R. Stat. Soc.: Series B 1995, 57 (1) 289 – 300

**24.** Smyth, G. K., Linear models and empirical bayes methods for assessing differential expression in microarray experiments. Stat Appl. Genet. Mol. Biol. 2004, 3, Article 3.

**25.** Satterthwaite, F. E. An approximate distribution of estimates of variance components Biometrics 1946, 2 (6) 110 – 4

**26.** Rodriguez, J.; Gupta, N.; Smith, R. D.; Pevzner, P. A. Does Trypsin Cut Before Proline? J. Proteome Res. 2008, 7 (1) 300 – 305

**27.** Abaye, D. A.; Pullen, F. S.; Nielsen, B. V. Peptide polarity and the position of arginine as sources of selectivity during positive electrospray ionisation mass spectrometry Rapid Commun. Mass Spectrom. 2011, 25 (23) 3597 – 3608

129

130

## **9. ROBUST** **<u>QUANTIFICATION FOR LABEL-FREE MASS SPECTROMETRY-BASED PROTEOMICS</u>**

Chapter 9 describes MSqRob, our R software package for improved differential protein abundance analysis in label-free MS-based proteomics. MSqRob is freely available on GitHub (https://github.com/statOmics/MSqRob) and is implemented in a "Shiny" user-friendly graphical interface.

In section 9.1, I introduce MSqRob as a new algorithm for the analysis of quantitative proteomics data that improves protein quantification by combining three innovative statistical approaches: ridge regression, empirical Bayes variance estimation, and M-estimation with Huber weights. MSqRob is both more precise and more accurate than state-of-the-art tools. I developed and implemented MSqRob as an R package and wrote the manuscript together with my supervisors.

Section 9.2 is published as an invited tutorial paper in which I outline key statistical concepts to help researchers to design proteomics experiments and showcases of quantitative proteomics data analysis with MSqRob. For this manuscript, I designed and performed analyses, set up the GitHub repository and wrote the paper together with my supervisors.

### **9.1. Peptide-level Robust Ridge Regression Improves Estimation, Sensitivity, and Specificity in Data-dependent Quantitative Label-free Shotgun Proteomics**

Goeminne L.J.E., Gevaert K. and Clement L. (2016). **Peptide-level Robust Ridge Regression Improves Estimation, Sensitivity, and Specificity in Data-dependent Quantitative Label-free Shotgun Proteomics.** _Molecular & Cellular Proteomics_ . 15(2), 657668

#### **9.1.1. Associated data**

<u>Supplementary Materials</u>

Supplemental Data

<u>supp_15_2_657__index.html (2.4K)</u> GUID: 9B15C066-3091-4E71-980A-55F4B6EE0B27 <u>10.1074_M115.055897_mcp.M115.055897-1.pdf</u> (7.0M) GUID: 401B1F9E-2C1B-4FA6-9374-9048987008F2 <u>10.1074_M115.055897_mcp.M115.055897-2.xlsx</u> (208K) GUID: B2490BE1-84E1-49D7-8951-5CB1D9597D83 <u>10.1074_M115.055897_mcp.M115.055897-3.zip</u> (72M) GUID: 6BF2E185-A0C2-4F19-B71D-5999CF7F6AF2

131

#### **9.1.2. Abstract**

Peptide intensities from mass spectra are increasingly used for relative quantitation of proteins in complex samples. However, numerous issues inherent to the mass spectrometry workflow turn quantitative proteomic data analysis into a crucial challenge. We and others have shown that modeling at the peptide level outperforms classical summarization-based approaches, which typically also discard a lot of proteins at the data preprocessing step. Peptide-based linear regression models, however, still suffer from unbalanced datasets due to missing peptide intensities, outlying peptide intensities and overfitting. Here, we further improve upon peptide-based models by three modular extensions: ridge regression, improved variance estimation by borrowing information across proteins with empirical Bayes and M-estimation with Huber weights. We illustrate our method on the CPTAC spike-in study and on a study comparing wild-type and ArgP knock-out _Francisella tularensis_ proteomes. We show that the fold change estimates of our robust approach are more precise and more accurate than those from state-of-the-art summarization-based methods and peptide-based regression models, which leads to an improved sensitivity and specificity. We also demonstrate that ionization competition effects come already into play at very low spike-in concentrations and confirm that analyses with peptide-based regression methods on peptide intensity values aggregated by charge state and modification status ( _e.g._ MaxQuant's peptides.txt file) are slightly superior to analyses on raw peptide intensity values ( _e.g._ MaxQuant's evidence.txt file).

#### **9.1.3. Introduction**

High-throughput LC-MS-based proteomic workflows are widely used to quantify differential protein abundance between samples. Relative protein quantification can be achieved by stable isotope labeling workflows such as metabolic (1, <u>2) and postmetabolic labeling (3</u> – <u>6). These</u> types of experiments generally avoid run-to-run differences in the measured peptide (and thus protein) content by pooling and analyzing differentially labeled samples in a single run. Labelfree quantitative (LFQ)<sup><u>1</u></sup> workflows become increasingly popular as the often expensive and time-consuming labeling protocols are omitted. Moreover, LFQ proteomics allows for more flexibility in comparing samples and tends to cover a larger area of the proteome at a higher dynamic range (7, <u>8). Nevertheless, the nature of the LFQ protocol makes shotgun proteomic</u> data analysis a challenging task. Missing values are omnipresent in proteomic data generated by data-dependent acquisition workflows, for instance because of low-abundant peptides that are not always fragmented in complex peptide mixtures and a limited number of modifications and mutations that can be accounted for in the feature search. Moreover, the overall abundance of a peptide is determined by the surroundings of its corresponding cleavage sites as these influence protease cleavage efficiency (9). Similarly, some peptides are more easily ionized than others (10). These issues not only lead to missing peptides, but also increase variability in individual peptide intensities. The discrete nature of MS1 sampling following continuous elution of peptides from the LC column leads to increased variability in peptide quantifications. Finally, competition for ionization and co-elution of other peptides with similar _m_ / _z_ values may cause biased quantifications (11). However, note that in this respect, using data-independent acquisition (DIA), all peptide ions (or all peptide ions within a certain m/z range, depending on the method used) are fragmented simultaneously, resulting in multiplexed MS/MS spectra (12, 13). Hence, issues of missing fragment spectra are less a problem with DIA, however, some of its challenges lie in deconvoluting MS/MS spectra and mapping their features to their corresponding peptides (14).

Standard data analysis pipelines for DDA-LFQ proteomics can be divided into two groups: spectral counting techniques, which are based on counting the number of peptide features as

132

a proxy for protein abundance (15), and intensity-based methods that quantify peptide features by measuring their corresponding spectral intensities or areas under the peaks in either MS or MS/MS spectra. Spectral counting is intuitive and easy to perform, but, the determination of differences in peptide and thus protein levels is not as precise as intensity-based methods, especially when analyzing rather small differences (16). More fundamentally, spectral counting ignores a large part of the information that is available in high-precision mass spectra. Further, dynamic exclusion during LC-MS/MS analysis, meant to increase the overall number of peptides that are analyzed, can worsen the linear dynamic range of these methods (17). Also, any changes in the MS/MS sampling conditions will prevent comparisons between runs. Intensity-based methods are more sensitive than spectral counting (18). Among intensitybased methods, quantification on the MS-level is somewhat more accurate than summarizing the MS/MS-level feature intensities (19). Therefore, we further focus on improving data analysis methods for MS-level quantification.

Typical intensity-based workflows summarize peptide intensities to protein intensities before assessing differences in protein abundances (20). Peptide-based linear regression models estimate protein fold changes directly from peptide intensities and outperform summarizationbased methods by reducing bias and generating more correct precision estimates (21, <u>22).</u> However, peptide-based linear regression models suffer from overfitting due to extreme observations and the unbalanced nature of proteomics data; _i.e._ different peptides and a different number of peptides are typically identified in each sample. We illustrate this using the CPTAC spike-in data set where 48 human UPS1 proteins were spiked at five different concentrations in a 60 ng protein/μl yeast lysate. Thus, when comparing different spike -in concentrations, only the human proteins should be flagged as differentially abundant (DA), whereas the yeast proteins should not be flagged as DA (null proteins). Fig. 9.1 illustrates the structure of missing data in label-free shotgun proteomics experiments using a representative DA UPS1 protein from the CPTAC spike-in study: missing peptides in the lowest spike-in condition tend to have rather low log2 intensity values in higher spike-in conditions compared to peptides that were not missing in both conditions, which supports the fact that the missing value problem in label-free shotgun proteomic data is largely intensity-dependent (23).


**Figure 9.1. Missing peptides are often low abundant.** The boxplots show the log2 intensity distributions for each of the 33 identified peptides corresponding to the human UPS1 protein cytoplasmic Histidyl-tRNA synthetase (P12081) from the CPTAC dataset in conditions 6A (spike-in concentration

133

0.25 fmol UPS1 protein/μl) and 6B (spike - in concentration 0.74 fmol UPS1 protein/μl). Vertical dotted lines indicate peptides present in both conditions. Note, that most peptides that were not detected in condition 6A exhibit low log2 intensity values in condition 6B (colored in red).

Fig. 9.2 shows the quantile normalized log2 intensity values for the peptides corresponding to the yeast null protein CG121 together with average log2 intensity estimates for each condition based on protein-level MaxLFQ intensities, as well as estimates derived from a peptide-based linear model. Here, three important remarks can be made:

(1) CG121 is a yeast background protein, for which the true concentration is thus equal in all conditions, which appears to be monitored as such by MaxLFQ, except in conditions 6B and 6E (for the latter, no estimate is available). The LM estimate, however, is more reliable but seems to suffer from overfitting.

(2) A lot of shotgun proteomic datasets are very sparse, causing a large sample-to-sample variability. Constructing a linear model based on a limited number of observations will thus lead to unstable variance estimates. Intuitively, a small sample drawn from a given populati on might “accidentally” show a very small variance while another small sample from the same population might display a very large variance just by random chance. This effect is clear from the sizes of the boxes. The interquartile range is twice as large in condition 6E compared to condition 6C. This issue leads to false positives since some proteins with very few observations are flagged as DA with very high statistical evidence solely due to their low observed variance (24).

(3) Two observed features at log2 intensities 14.0 and 14.3 in condition 6B have a strong influence on the parameter estimate for this condition. Without these extreme observations, the 6B estimate lies closer to the estimates in the other conditions. As missingness is strongly intensity-dependent, these low intensity values could easily become missing values in subsequent experiments. More generally, a strong influence of only one or two peptides on the average protein level intensity estimate for a condition is an unfavorable property.

134


**Figure 9.2. Effect of outliers, variability, and sparsity of peptide intensities on abundance estimations.** The figure shows log2 transformed quantile normalized peptide intensities for the yeast null protein CG121 from the CPTAC data set for spike-in conditions 6A, 6B, 6C, 6D, and 6E. Each color denotes a different condition. Connected crosses: average protein log2 intensity estimates for each condition are provided for a traditional protein level workflow where the mean of the protein-level MaxLFQ values was calculated (MaxLFQ, blue), the estimates of the peptide-based regression model fitted with ordinary least squares (LM, black) and the estimates of the peptide based ordinary least squares fit after omitting the two lowest observations in condition 6B (LM-extremes, orange). In condition 6E there were not enough data points to provide a MaxLFQ protein-level estimate. Boxes denote the interquartile range (IQR) of the log2 transformed quantile normalized peptide intensities in each condition with the median indicated as a thick horizontal line inside each box. Whiskers extend to the most extreme data point that lies no more than 1.5 times the IQR from the box. Points lying beyond the whiskers are generally considered as outliers. Note, that the presence of two low-intensity peptide observations in concentration 6B has a strong effect on the estimates for both MaxLFQ and LM.

These issues illustrate that state-of-the-art analysis methods experience difficulties in coping with peptide imbalances that are inherent to DDA LFQ proteomics data. We here propose three modular improvements to deal with the problems of overfitting, sample-to-sample variability and outliers:

- (1) Ridge regression, which penalizes the size of the model parameters. Shrinkage estimators can strongly improve reproducibility and overall performance as they have a lower overall mean squared error compared to ordinary least squares estimators (25 – <u>27).</u>

- (2) Empirical Bayes variance estimation, which shrinks the individual protein variances toward a common prior variance, hence stabilizing the variance estimation.

- (3) M-estimation with Huber weights, which will make the estimators more robust toward outliers (28).

We illustrate our method on the CPTAC Study 6 spike-in data and a published ArgP knock-out _Francisella tularensis_ proteomics experiment and show that our method provides more stable log2 FC estimates and a better DA ranking than competing methods.

135

#### **9.1.4. Experimental procedures**

##### **CPTAC Spike-in Data Set**

The publicly available Study 6 of the Clinical Proteomic Technology Assessment for Cancer (29) is used to evaluate the performance of our method. Raw data can be accessed at <u>https://cptac-data-portal.georgetown.edu/cptac/public?scope=Phase+I. In this study, the</u> Sigma Universal Protein Standard mixture 1 (UPS1, Sigma-Aldrich, St. Louis, MO) containing 48 different human proteins was spiked into a 60 ng protein/μl _Saccharomyces cerevisiae_ strain BY4741 (MATa, leu2Δ0, met15Δ0, ura3Δ0, his3Δ1) lysate in five different concentrations (6A: 0.25 fmol UPS1 proteins/μl; 6B: 0.74 fmol UPS1 proteins/μl; 6C: 2.22 fmol UPS1 proteins/μl; 6D: 6.67 fmol UPS1 proteins/μl; and 6E: 20 fmol UPS1 proteins/μl). These samples were sent to five independent laboratories and analyzed on seven different instruments. For convenience, we limited ourselves to the data originating from the LTQ-Orbitrap at site 86, LTQ-Orbitrap O at site 65 and LTQ-Orbitrap W at site 56. Samples were run three times on each instrument. The used dataset thus features five different samples, each analyzed in threefold on three different instruments. Raw data files were searched using MaxQuant version 1.5.2.8 (30) with the following settings. As variable modifications we allowed acetylation (protein N terminus), methionine oxidation (to methionine-sulfoxide) and N-terminal glutamine to pyroglutamate conversion. As a fixed modification, we selected carbamidomethylation on cysteine residues as all samples were treated with iodoacetamide. We used the enzymatic rule of trypsin/P with a maximum of 2 missed cleavages and allowed MaxQuant to perform matching between runs with a match time window of 0.7 min and an alignment time window of 20 min. The main search peptide tolerance was set to 4.5 ppm and the ion trap MS/MS match tolerance was set to 0.5 Da. Peptide-to-spectrum match level was set at 1% FDR with an additional minimal Andromeda score of 40 for modified peptides as these settings are most commonly used by researchers. Protein FDR was set at 1% and estimated by using the reversed search sequences. We performed label-free quantitation with MaxQuant's standard settings. The maximal number of modifications per peptide was set to 5. As a search FASTA file we used the 6718 reviewed proteins present in the _Saccharomyces cerevisiae_ (strain ATCC 204508/S288c) proteome downloaded from Uniprot at March 27, 2015 supplemented with the 48 human UPS1 protein sequences. Potential contaminants present in the contaminants.fasta file that comes with MaxQuant were automatically added to the search space by the software. For protein quantification in the proteinGroups.txt file, we used unique and razor peptides and allowed all modifications as all samples originate in essence from the same yeast lysate and the same UPS1 spike-in sample.

##### **_Francisella tularensis_ Data Set**

The data of Ramond _et al._ (31) is used to illustrate our method on a real biological experiment. Both raw and processed data are publicly available and can be found in the PRIDE repository at <u>http://www.ebi.ac.uk/pride/archive/projects/PXD001584. The authors explored changes in</u> the proteome of the facultative intracellular pathogenic coccobacillus _Francisella tularensis_ after gene deletion of a newly identified arginine transporter, ArgP. Both wild-type and ArgP mutants were grown in biological triplicate. Each biological replicate was analyzed in technical triplicate via label-free LC-MS/MS. Data were processed with MaxQuant version 1.4.1.2 and potential contaminants and reverse sequences were removed. In addition, only proteins present with at least two peptides in at least 9 out of the 18 replicates were retained. Subsequent data analysis via t-tests on imputed LFQ intensities was performed.

136

##### **Summarization-based Analysis**

##### **MaxLFQ+Perseus**

This is a standard summarization-based analysis pipeline that is available in the popular MaxQuant-Persues software package (21). Briefly, the MaxQuant ProteinGroups.txt file was loaded into Perseus version 1.5.1.6, potential contaminants that did not correspond to any UPS1 protein as well as reversed sequences and proteins that were only identified by site (thus only by a peptide carrying a modified residue) were removed from the data set. MaxLFQ intensities (32) were log2 transformed and pairwise comparisons between conditions were done via _t_ -tests.

##### **MaxLFQ+limma**

The MaxQuant ProteinGroups.txt file is used as input for R version 3.1.2 (Pumpkin Helmet) (33). Potential contaminants and reversed sequences (see above) were removed from the data set. The MaxLFQ intensities were log2 transformed and analyzed in limma, an R/Bioconductor package for the analysis of microarray and next-generation sequencing data (34). Limma makes use of posterior variance estimators to stabilize the naive variance estimator by borrowing strength across proteins (see also below).

##### **Peptide-based Model Analysis**

##### **Data Preprocessing**

MaxQuant's peptides.txt file was read into R version 3.1.2, the peptide intensities were log2 transformed and quantile normalized (35, <u>36). Many other normalization approaches do exist,</u> however, comparing them is beyond the scope of this paper (24, 36 – <u>38). Reversed sequences</u> and potential contaminants were removed from the data. For the CPTAC dataset, we only removed potential contaminants that did not map to any UPS1 protein. MaxQuant assigns proteins to protein groups using an Occam's razor approach. However, to avoid the added complexity of proteins mapped to multiple protein groups, we discarded peptides belonging to protein groups that contained one or more proteins that were also present in a smaller protein group. Next, peptides were grouped per protein group in a data frame. Finally, values belonging to peptide sequences that appeared only once were removed as the model parameter for the peptide effect for these sequences is unidentifiable. For notational convenience, a unique protein or protein group is referred to as a protein in the remainder of this article.

##### **Benchmark Peptide-based Model**

We start from the peptide-based linear regression models as proposed by Daly _et al._ (39) Clough _et al._ (22) and Karpievitch _et al._ (40), of which we have independently proven their superior performance compared to summarization-based workflows (21). In general, the following model is proposed:


with _yijklmn_ the _n_<sup>th</sup> log2-transformed normalized feature intensity for the _i_<sup>th</sup> protein under the _j_<sup>th</sup> treatment ( _treat),_ the _k_<sup>th</sup> peptide sequence ( _pep_ ), the _l_<sup>th</sup> biological repeat ( _biorep_ ) and the _m_<sup>th</sup> technical repeat ( _techrep_ ) and ε _ijklmn_ a normally distributed error term with mean zero and protein specific variance σ _i_<sup>2</sup> . The 𝛽's denote the effect sizes for _treat, pep, biorep_ and _techrep_ for the _i_<sup>th</sup> protein.

137

##### **Robust Ridge Model**

Our novel approach improves the estimation of the model parameters in (Eq. 1) via three extensions: (1) ridge regression, which leads to shrunken yet more stable log2 fold change (FC) estimates, (2) Empirical Bayes estimation of the variance, which further stabilizes variance estimators, and (3) M-estimation with Huber weights, which reduces the impact of outlying peptide intensities. For the robust ridge model, degrees of freedom are calculated using the trace of the hat matrix.

##### _1. Ridge Regression_

The ordinary least squares (OLS) estimates for protein _i_ are defined as the parameter estimates that minimize the following loss function:


With _eijklmn_ the residual errors and _Xijklmn_ the row of the design matrix corresponding to observation _yijklmn_ .

Ridge regression shrinks the regression parameters by imposing a penalty on their magnitude. The ridge regression estimator is obtained by minimizing a penalized least squares loss function:


With each 𝜆 a ridge penalty for the parameter estimator 𝛽̂ corresponding to an effect in Eq. 1. When the 𝜆s are larger than zero, the ridge estimators for 𝛽̂ will be shrunken toward 0. This introduces some bias but reduces the variability of the parameter estimator, which makes shrinkage estimators theoretically more stable and more accurate ( _i.e._ they tend to have a lower root mean squared error (RMSE) compared to the OLS estimator) (25 – <u>27). On the one</u> hand, 𝛽̂'s estimated by only a few observations will experience a strong correction toward 0, protecting against overfitting. On the other hand, 𝛽̂'s that can be estimated based on many observations will exhibit a negligible bias because the ridge penalty will be dominated by the sum of the squared errors, which reflects that these 𝛽̂'s can be estimated more reliably. We choose to tune each 𝜆 separately because the variability on the peptide effect seems generally much larger than the variability on the other effect terms. 𝜆 penalties can be tuned via crossvalidation, but in this work, we exploit the link between mixed models and ridge regression (41) and estimate the penalties by implementing ridge regression within the lme4 package (42) in 2 𝜎̂𝑖 2 R. 𝜆𝑡𝑟𝑒𝑎𝑡 then equals 2 with 𝜎̂𝑖 the estimated residual variance and 𝜎̂𝛽𝑡𝑟𝑒𝑎𝑡,𝑖 the estimated 𝜎̂𝛽𝑡𝑟𝑒𝑎𝑡,𝑖 variance captured by the treatment effect for peptide intensities from protein _i_ (Chapter 5, 41). The standard errors of the parameter estimators and contrasts of interest are based on the bias-adjusted variance estimator (Chapter 6, 41).

##### _2. Empirical Bayes Variance Estimations_

In the introduction we argued that data sparsity can lead to unstable variance estimates. In order to stabilize the residual variance estimation, we shrink the estimated protein specific

138

variances toward a pooled estimate over all proteins using an empirical Bayesian approach (43) implemented in the limma R/Bioconductor-package (44). In that way, the information contained in all proteins is borrowed to stabilize the variance estimates of proteins with few observations. Hence, the small variances will increase, while large variances will decrease. This avoids that proteins that exhibit a small FC and a tiny variance will appear highly significantly. Also, the number of degrees of freedom for all these so-called moderated t-tests will increase compared to normal _t_ -tests.

##### _3. M-estimation With Huber Weights_

As we have shown in the introduction (see Fig. 9.2), outlying peptides might have a severe impact on the parameter estimates, especially in conditions with few identified features. We therefore propose to adopt M-estimation with Huber weights to diminish the impact of outlying observations. Combining ridge regression with M-estimation leads to the following penalized weighted least squares loss function:


Herein, _wijklmn_ is a Huber weight that weighs down observations with high residuals.

##### **False Discovery Rate**

For both peptide-based models and MaxLFQ+limma, _p_ values are adjusted for multiple testing with the Benjamini-Hochberg FDR procedure (45). Perseus uses a permutation-based FDR that turns out to be very close to the Benjamini-Hochberg procedure. The FDR is controlled at the 5% level in all analyses.

#### **9.1.5. Results**

We decided to compare our method to three competing methods using data from the CPTAC spike-in benchmark study. Additionally, its advantages are demonstrated in a case study that was originally analyzed with a standard summarization-based approach. For peptide-based models the use of MaxQuant's peptides.txt file, which contains summed up peptide level data, slightly increased the discriminative power as compared to analyses using the MaxQuant's evidence.txt file, which contains individual intensities for each identified feature (supplemental <u>Fig. S7, File S1). Therefore, all peptide-based models are based on the peptides.txt file.</u>

##### **1. Evaluation Using Data From a Spike-in Benchmark Study**

The performances of the different methods are assessed by comparing different spike-in concentrations in the CPTAC Study 6 data set. This data set consists of identical samples containing a trypsin-digested _Saccharomyces cerevisiae_ proteome spiked with different conce ntrations (0.25, 0.74, 2.22, 6.67, and 20 fmol/μl) of a trypsin -digested UPS1 mix containing 48 human proteins. As the high spike-in concentrations are known to suffer from ionization competition effects (18, <u>21), we focus mainly on comparing 6B-6A, 6C-6A and 6C-</u> 6B, which have the lowest spike-in concentrations.

We compared our robust ridge approach to three competing approaches: (1) MaxLFQPerseus, (2) MaxLFQ-limma, and (3) a petide based linear model (LM). (1) MaxLFQ-Perseus

139

is a standard summarization-based approach where MaxLFQ normalized log2 protein intensities are compared between conditions by FDR-corrected t-tests. (2) MaxLFQ-limma is a summarization-based approach in which MaxLFQ protein level data are analyzed via limma (34), an R/Bioconductor package that can stabilize variance estimation by borrowing information across proteins via an empirical Bayesian approach. (3) The linear model (LM) is a peptide-based linear regression model (Eq. 1) that is known to outperform summarizationbased approaches (21). This model contains a treatment effect, a peptide effect and an instrument effect, and its structure is motivated in supplemental File S1. Note, that our robust ridge method (RR) is an improvement of the LM approach by implementing ridge regression, empirical Bayes variance estimation and M-estimation with Huber weights. We compared the results of the four methods in terms of precision and accuracy of the log2 fold change estimates, as well as sensitivity and specificity.

##### _Precision and Accuracy_

Log2 fold change (FC) estimates using our robust ridge model for yeast null proteins are clearly more precise compared to the other methods; the interquartile range of the log2 FC estimates is on average three times smaller compared to the LM fit and 4.5 times smaller for comparison 6B-6A; Fig. 9.3). The accuracy is also increased as most DA estimates for yeast null proteins are estimated very close to zero. This is due to an effect of the ridge penalty, which strongly shrinks the estimates for null proteins identified by a few peptides toward zero. Fig. 9.3 also shows a general trend for each method: as spike-in concentration differences increase, a negative bias of the log2 FC estimates appears. This likely reflects ionization suppression effects (18, 21). Note that for our method, the log2 FC distributions in all comparisons (including 6B _versus_ 6A) in Fig. 9.3 are skewed toward negative fold changes and that the skewness increases with higher spike-in concentrations, suggesting that ionization suppression effects already occur at very low spike-in concentrations.


**Figure 9.3. Precision and accuracy of fold change (FC) estimates for null proteins in the CPTAC study.** The boxplots show the distributions of the FC estimates of the null yeast proteins for each of the ten comparisons for 4 different approaches. Outliers (here defined as data points that lie more than 1.5 times the interquartile range from the box) are not shown. The horizontal dotted green line denotes the true log2 fold change for the yeast proteins (log2 FC = 0). Blue (MaxLFQ+Perseus): protein-level analysis consisting of MaxLFQ normalization followed by _t_ -tests in Perseus, yellow (MaxLFQ+limma): proteinlevel analysis consisting of MaxLFQ normalization followed by limma analysis, black (LM): peptidebased linear regression model containing treatment, peptide and instrument effects, purple (RR): peptide-based ridge regression model containing treatment, peptide and instrument effects with

140

empirical Bayes variance estimator and M-estimation with Huber weights. An identical figure with outliers is provided in supplemental Fig. S12, File S1.

When assessing the DA UPS1 proteins (Fig. 9.4), the log2 FC estimates for the summarizationbased approaches MaxLFQ-Perseus and MaxLFQ-limma are always more biased and more variable compared to the LM and RR methods, except in condition 6B-6A, where MaxLFQlimma has the lowest bias of all approaches. Median log2 FC estimates for UPS proteins are very comparable between our RR and the LM method. For eight out of ten comparisons, the RR estimates are even closer to the true log2 FC. The interquartile range of the log2 FC estimates of the DA proteins for RR is on average 1.2 times smaller compared to those of the LM model. Thus, shrinkage estimation does not negatively affect estimates for proteins with a strong evidence for DA.


**Figure 9.4.** **<u>Precision and accuracy of fold change (FC) estimates for differential abundant</u> proteins in the CPTAC study.** The boxplots show the distributions of the FC estimates of the spikedin UPS1 proteins for each of the ten comparisons for four different approaches. Outliers (here defined as data points that lie more than 1.5 times the interquartile range from the box) are not shown. The horizontal dotted green lines denote the true log2 FC for the UPS1 proteins in each comparison. Blue (MaxLFQ+Perseus): protein-level analysis consisting of MaxLFQ normalization followed by _t_ -tests in Perseus, yellow (MaxLFQ+limma): protein-level analysis consisting of MaxLFQ normalization followed by limma analysis, black (LM): peptide-based linear regression model containing treatment, peptide and instrument effects, purple (RR): peptide-based ridge regression model containing treatment, peptide and instrument effects with empirical Bayes variance estimator and M-estimation with Huber weights. An identical figure with outliers is provided in supplemental Fig. S13, File S1.

##### _Sensitivity and Specificity_

The sensitivity and specificity of the different methods are assessed using receiver operator characteristics (ROC) curves (Fig. 9.5, Tables 9.1 and 9.2). For the summarization-based approaches, it turns out that MaxLFQ+limma outperforms MaxLFQ+Perseus. This is not surprising, as it has been shown that limma outperforms standard t-tests, also in proteomics data sets (46). As we have shown before, both peptide-based regression models outperform the summarization-based approaches (21). Our RR method further improves on the LM model in comparison 6B-6A, in which the detection of DA is most challenging since it involves the two lowest spike-in concentrations. For all other comparisons LM and RR have a similar performance (Table 9.2), which was expected because the ROC curves of the LM method for these comparisons are already very steep.

141


**Figure 9.5.** **<u>Comparison of sensitivity and specificity.</u>** Receiver operator characteristic (ROC) curves show the superior performance of our robust ridge approach compared to other standard data analysis techniques for comparisons of conditions 6B-6A, 6C-6A, and 6C-6B in the CPTAC spike in study. Stars denote the cut-offs at an estimated 5% FDR level. Blue (MaxLFQ+Perseus): protein-level analysis consisting of MaxLFQ normalization followed by _t_ -tests in Perseus, yellow (MaxLFQ+limma): proteinlevel analysis consisting of MaxLFQ normalization followed by limma analysis, black (LM): peptidebased linear regression model containing treatment, peptide and instrument effects, purple (RR): peptide-based ridge regression model containing treatment, peptide and instrument effects with empirical Bayes variance estimator and M-estimation with Huber weights.

**Table 9.1.** Total areas under the curve (AUC) for three standard approaches and our robust ridge method for comparisons 6B-6A, 6C-6A and 6C-6B in the CPTAC spike-in study. MaxLFQ+Perseus: protein-level analysis consisting of MaxLFQ normalization followed by t-tests in Perseus, MaxLFQ+limma: protein-level analysis consisting of MaxLFQ normalization followed by limma analysis, LM: peptide-based linear regression model containing treatment, peptide and instrument effects, RR: peptide-based ridge regression model containing treatment, peptide and instrument effects with empirical Bayes variance estimator and M-estimation with Huber weights.

|**Comparison**|**MaxLFQ+Perseus**|**MaxLFQ+limma**|**LM**|**RR**|
|---|---|---|---|---|
|**6B-6A**|0.536|0.634|0.817|0.862|
|**6C-6A**|0.583|0.672|0.877|0.869|
|**6D-6A**|0.583|0.680|0.880|0.878|
|**6E-6A**|0.564|0.660|0.883|0.880|
|**6C-6B**|0.607|0.655|0.860|0.861|
|**6D-6B**|0.618|0.657|0.858|0.859|
|**6E-6B**|0.601|0.644|0.863|0.863|
|**6D-6C**|0.654|0.680|0.856|0.860|
|**6E-6C**|0.663|0.678|0.864|0.864|
|**6E-6D**|0.683|0.685|0.836|0.837|


142

**Table 9.2.** Partial areas under the curve (pAUC) for a false positive rate (FPR) < 0.1 for three standard approaches and our robust ridge method by comparing conditions 6B-6A, 6C-6A and 6C-6B in the CPTAC spike-in study. MaxLFQ+Perseus: protein-level analysis consisting of MaxLFQ normalization followed by t-tests in Perseus, MaxLFQ+limma: protein-level analysis consisting of MaxLFQ normalization followed by limma analysis, LM: peptide-based linear regression model containing treatment, peptide and instrument effects, RR: peptide-based ridge regression model containing treatment, peptide and instrument effects with empirical Bayes variance estimator and M-estimation with Huber weights.

|**Comparison**|**MaxLFQ+Perseus**|**MaxLFQ+limma**|**LM**|**RR**|
|---|---|---|---|---|
|**6B-6A**|0.061|0.075|0.083|0.091|
|**6C-6A**|0.076|0.088|0.096|0.097|
|**6D-6A**|0.077|0.089|0.098|0.097|
|**6E-6A**|0.076|0.089|0.097|0.097|
|**6C-6B**|0.081|0.086|0.096|0.097|
|**6D-6B**|0.082|0.086|0.096|0.096|
|**6E-6B**|0.081|0.087|0.096|0.096|
|**6D-6C**|0.076|0.083|0.094|0.095|
|**6E-6C**|0.088|0.090|0.095|0.095|
|**6E-6D**|0.090|0.092|0.092|0.093|


##### _FDR Control_

None of the adopted methods are able to control the true FDR at the nominal 5% level in the majority of the comparisons (Table 9.3). MaxLFQ+Perseus can only control the FDR at the 5% level in comparisons 6C-6A and 6C-6B. MaxLFQ+limma only controls the FDR accurately in comparison 6C-6B and both LM and RR can control the FDR only in comparisons 6B-6A and 6C-6B. When comparing RR and LM, RR does a better job in controlling the FDR in comparisons 6B-6A, 6C-6A, 6D-6B and 6D-6C, but not for the other comparisons.

143

**Table 9.3.** Observed FDR when using a 5% FDR cut-off level for each of the three standard approaches and our robust ridge method for all pairwise comparisons between conditions 6A, 6B, 6C, 6D and 6E. MaxLFQ+Perseus: protein-level analysis consisting of MaxLFQ normalization followed by t-tests in Perseus, MaxLFQ+limma: protein-level analysis consisting of MaxLFQ normalization followed by limma analysis, LM: peptide-based linear regression model containing treatment, peptide and instrument effects, RR: peptide-based ridge regression model containing treatment, peptide and instrument effects with empirical Bayes variance estimator and M-estimation with Huber weights. This table shows that most methods are unable to control the FDR at 5%, especially for comparisons involving higher spikein concentrations (e.g. 6D and 6E).

|**Comparison**|**MaxLFQ+Perseus**|**MaxLFQ+limma**|**LM**|**RR**|
|---|---|---|---|---|
|**6B-6A**|0.071|0.048|0.034|0.030|
|**6C-6A**|0.040|0.083|0.095|0.050|
|**6D-6A**|0.456|0.794|0.466|0.050|
|**6E-6A**|0.917|0.922|0.870|0.883|
|**6C-6B**|0.037|0|0|0.024|
|**6D-6B**|0.640|0.879|0.528|0.494|
|**6E-6B**|0.918|0.924|0.863|0.870|
|**6D-6C**|0.429|0.799|0.481|0.434|
|**6E-6C**|0.886|0.906|0.842|0.848|
|**6E-6D**|0.321|0.584|0.386|0.561|


##### **2. Case Study**

We further illustrate the performance of our novel method on true biological data in which a single trigger was expected to have an impact on several tightly regulated, but highly interconnected pathways. Thus, contrary to a spike-in data set where differential abundance typically heads in one direction (either up or down-regulated) and stays limited to the spikedin proteins, a biological dataset consists of a plethora of both strongly as well as weakly differentially regulated proteins. Moreover, in the CPTAC data set, the same sample was always used to spike in different amounts of UPS1 proteins in the same yeast background instead of isolating a new yeast proteome each time. Hence, variability in biological repeats will be much larger compared to the spike-in data set. Although detection of differential abundance in real biological data is the ultimate goal, there is no known ground truth available for these data sets and our evaluation is based on visual inspection of selected findings.

We made use of the publicly available data published by Ramond _et al._ (31) in which the authors compared the proteome of _Francisella tularensis_ mutant for the arginine transporter ArgP to wild-type (WT) bacteria in biological triplicate. For each biological repeat, three technical replicates were also available. We compared the authors' results with the results of our RR method based on the authors-supplied peptides.txt instead of re-searching the raw spectra. In their study, Ramond _et al._ (31) performed the analysis at the protein level using intensities of at least two different peptides and keeping those proteins with at least 9 out of 18 valid values, and as such analyzed 842 proteins in total. With our approach — analysis at the peptide level and filtering out peptides that appeared only once in the data set — we were able to analyze a total of 989 proteins. Both the results of our ranking as well as the ranking from the original _Francisella_ article can be found in supplemental File S2. When we compared the top 100 proteins with the lowest _p_ values in both methods, only 52 proteins overlapped. Ramond _et al._ (31) found 309 DA proteins at the 5% FDR level, whereas we only found 159 proteins significantly DA at the same FDR level. Thus, our method appears to be more conservative.

144

We evaluated the differential abundance of the ten proteins that were present in the RR DA list, but not in the original DA list, as well as the ten highest ranked proteins from the original DA list missing in our list. The ten proteins that were only discovered with our method were all lost during the preprocessing procedure of Ramond _et al._ (31). Among those proteins, six are more highly abundant in the mutant: exodeoxyribonuclease V subunit gamma and ABC transporter membrane protein, as well as four hypothetical proteins (the membrane protein FTN_0835, an AAA<sup>+</sup> superfamily member FTN_0274, an alpha/beta hydrolase FTN_0721 and FTN_1244). Four out of the ten proteins that were only discovered by our method have a lower abundance in the mutant. These proteins are Radical SAM superfamily protein, DNA helicase II, C32 tRNA thiolase and the hypothetical protein FTN_0400. Log2 intensity plots of the individual peptide intensities suggest a differential abundance for most of these proteins (supplemental Figs. S14-S23, File S1).

Eight out of the ten highest-ranked proteins in the original DA list all seem to be highly abundant gauged by the number of peptides identified (supplemental Figs. S24-S33, File S1). Further inspection reveals that most of these proteins do not appear to bear strong evidence for DA between WT and mutant. Except for the hypothetical protein FTN_1397 and the Mur ligase family protein, all variance estimates are smaller than 0.01, which leads to extreme T statistics. Empirical Bayesian variance estimation does increase these small variances, but not enough to make them insignificant at the 5% significance level. There seems to be a relatively clear effect for hypothetical protein FTN_1397 (supplemental Fig. S31, File S1), which in our method just did not pass the 5% FDR level ( _p_ value of 9.4*10<sup>−3</sup> and FDR adjusted _p_ value 0.057). The Mur ligase family protein shows no strong visual DA (supplemental Fig. S32, File S1), but combines a moderate DA estimate (-0.34) with a small variance (0.01). The two other proteins only present in the list of Ramond _et al._ (31) are rather low-abundant. DNA-binding protein HUbeta (supplemental Fig. S30, File S1) shows no visual evidence for DA at all, but hypothetical protein FTN_1199 (supplemental Fig. S33, File S1) might possess weak evidence for DA.

Ramond _et al._ (31) also noted that several protein modules had an increased enrichment in DA proteins. In fact, all ribosomal proteins and all proteins involved in branched-chain amino acid (BCAA) synthesis were either unchanged (as the _p_ value did not reach the 5% FDR cutoff) or present in lower amounts in the mutant. Based on their data, one could also suspect an up-regulation of several tricarboxylic acid (TCA) cycle proteins (nine out of 12) in the mutant.

##### _Ribosomal Proteins_

It is known that a global down-regulation of ribosome synthesis is a common response to nutrient starvation in Bacteria and Eukarya (47, <u>48). One might thus expect a similar drop in</u> abundance in the arginine transporter-mutated _F. tularensis_ as its delay in phagosomal escape can be fully restored by supplementation of the medium with excess arginine (31). When considering all 30S and 50S ribosomal proteins (both significant and insignificant in terms of DA), both our method and the original article report log2 FC estimates for 49 ribosomal proteins. As expected, all log2 FC estimates from our method pointed toward down-regulation in the mutant. Contrary, in the analysis of Ramond _et al._ (31), two proteins, ribosomal protein L7/L12 and 30S ribosomal protein S18 showed, although deemed insignificant, quite large log2 FCs (0.12 resp. 0.54) in favor of up-regulation in the mutant. This again suggest a more stable log2 FC estimation by our method (supplemental Fig. S34, File S1).

##### _BCAA Synthesis Proteins_

Based on KEGG, we could only identify nine proteins as BCAA synthesis proteins although the authors report on 12 BCAA synthesis proteins. As we were unable to find the remaining 3 proteins in this pathway, we further focus on nine proteins only. Supplemental Fig. S35, File

145

<u>S1</u> shows the distribution of the log2 FC estimates for both the methodology of Ramond _et al._ (31) and our method. Here, one insignificant protein, dihydroxy-acid dehydratase shows a log2 FC of 0.22. Using our method, all log2 FCs indicate either down-regulation in the mutant ( _i.e._ log2 FCs smaller than 0) or no change at all (log2 FCs smaller than 1*10<sup>−17</sup> ). On average, log2 FC estimates for BCAA synthesis proteins are more negative in our method. Thus, our method provides stronger evidence for down-regulation of some BCAA synthesis proteins in the mutant compared to the method of the original article.

_TCA Cycle Proteins_

Based on KEGG, we identified 13 TCA cycle proteins, while Ramond _et al._ (31) reported 12 proteins. When assessing the log2 FC estimates of these authors for the 13 proteins, 10 TCA cycle proteins appear to be up-regulated in the mutant (supplemental Fig. S36, File S1), 8 of which are declared significant. Contrary, in our method, only 1 protein of the TCA cycle (2oxoglutarate dehydrogenase complex, E2 component, dihydrolipoyltranssuccinase) is found significant. Strikingly, 8 out of 13 TCA cycle proteins even show log2 FC estimates that are in absolute value smaller than 1× 10<sup>−9</sup> . We therefore zoomed in onthe individual log2 FC estimates of the peptides mapping to these proteins (supplemental Figs. S37-S50, File S1).

2-oxoglutarate dehydrogenase complex, E2 component, dihydrolipoyltranssuccinase (supplemental Fig. S37, File S1) is the only TCA cycle protein that is found at significantly different levels by our analysis. It is also denoted as significant in the original paper's methodology. Nonetheless, the evidence does not seem to be very strong. 2-oxoglutarate dehydrogenase E1 component, dihydrolipoamide acetyltransferase and succinate dehydrogenase iron-sulfur subunit are also denoted as significant in the original analysis with _p_ values of 5.3 × 10<sup>−10</sup> , 8.1 × 10<sup>−4</sup> and 1.1 × 10<sup>−3</sup> respectively, although the spectral evidence also appears quite weak (supplemental Figs. S38, S40, and S41, File S1). In our opinion, any visual evidence for differential abundance for malate dehydrogenase, aconitate hydratase, succinyl-CoA synthetase, alpha subunit and isocitrate dehydrogenase is negligible. Nonetheless, _p_ values corresponding to DA for these proteins are estimated at 7.4 × 10<sup>−4</sup> , 3.6 × 10<sup>−3</sup> , 0.02 and 0.02 respectively in the paper of Ramond _et al._ (31) (supplemental Figs. S42, <u>S43, and S47, File S1).</u>

#### **9.1.6. Discussion**

In this work, we introduced three extensions to existing peptide-based linear models that significantly improve stability and precision of fold change estimates. These extensions include minimizing a penalized least squares loss function (ridge regression), weighing down outliers via M-estimation with Huber weights and variance stabilization via empirical Bayes. Our estimation approach is inevitably computationally more complex than the linear regression model, albeit much faster than fully Bayesian approaches that have to be fitted by computationally intensive Markov chain Monte Carlo algorithms (49). In this contribution, we normalized log2 transformed peptide intensities using quantile normalization. Many other types of transformation and normalization exist and can be adopted prior to applying our method. Our focus however, is on robust estimation procedures for peptide-based linear models. Therefore, a thorough comparison of preprocessing methods is beyond the scope of this paper.

We compared our novel estimation method to three other methods: a standard protein-level summarization followed by t-tests (MaxLFQ+Perseus), a standard protein-level summarization followed by limma (MaxLFQ+limma) and a peptide-based linear regression model. Evaluation was done based on the CPTAC Study 6 data set, where the ground truth is known as well as on a biological data set, where ArgP mutated _versus_ wild-type _Francisella tularensis_ proteomes

146

are compared. For the CPTAC dataset, we found our method to give more precise and more stable log2 FC estimates for both the yeast null proteins and the spiked-in UPS1 proteins. Thus, our method sufficiently shrinks abundance estimates that are driven by data sparsity in the null proteins, while retaining good DA estimates when sufficient evidence is present (such as for most UPS1 proteins in the CPTAC spike-in study). These findings are supported by theory as ridge regression shrinkage indeed reduces the variability of the estimator and generates overall more precise FC estimates (lower overall RMSE compared to ordinary least squares estimators) (25 – <u>27). Furthermore, empirical Bayes variance estimation squeezes the</u> individual residual variances of all models toward a pooled variance which stabilizes the variance estimation. Finally, M-estimation with Huber weights weakens the impact of individual outliers.

The systematic underestimation of the log2 FC estimates provided by our method, even in comparison 6B-6A (Fig. 3), suggests that ionization competition effects can already come into play at spike- in concentration levels of 0.74 fmol/μl (condition 6B). These effects might partly explain why none of the considered methods performs well in controlling the FDR at the nominal 5% level. When analyzing the _Francisella_ dataset, RR is more conservative than the method used by Ramond _et al._ (31), which might suggest a better protection against false positives. Indeed, ionization competition effects are also relevant for true biological data sets as an increase in a number of highly abundant proteins in a certain condition might generate a downwards bias in peptide intensities corresponding to non-DA proteins in this condition. Researchers should thus carefully reflect whether a low log2 fold change is truly biologically relevant, as ionization suppression effects already seem to appear at low differences in concentration. Indeed, even when disregarding these effects, the abundance of a protein typically has to differ by a reasonable amount to be of interest to a researcher. Therefore, we suggest testing against a minimal log2 FC value that is biologically interesting in a particular experiment; _e.g._ 0.5 or 1 (50). A similar approach can be easily adopted within our framework, but we have chosen to test against an FC of 0 to make our results comparable with the analysis of Ramond _et al._ (31).

In practice, only a handful of true positives will typically be selected for further experimental validation. Therefore, the ranking that is produced by a method is more important than its capability to accurately control the FDR at the 5% level. Here, RR produces superior ranking lists compared to all other methods except in comparisons 6D-6A, 6E-6A and 6E-6B, where large ionization suppression effects are expected due to huge spike-in concentration differences. Hence, it will be very difficult to discern the ionization bias from real DA for these comparisons. Each component of our model contributes to an improvement in performance. ROC curves in <u>supplemental Fig. S4, File S1 show that empirical Bayesian variance estimation</u> slightly but consistently improves the performance of the LM model, while M-estimation seems to cause the largest gain (supplemental Fig. S5, File S1). Ridge regression clearly improves the LM model, EB variance estimation slightly improves the ridge regression model while M- estimation again seems to deliver the largest gain in performance. Corresponding AUC and pAUC values can be found in (supplemental Tables S7-S10, File S1).

In the CPTAC case study, we also confirmed that a peptide-based model starting from summed up intensities over different charge states and modifications but corresponding to identical peptide sequences in the same sample (peptides.txt file) tends to have a higher discriminative ability than a model starting from the individual feature intensities (evidence.txt file, see <u>supplemental Fig. S7, File S1). Others have also shown that analysis on the lowest level of</u> summarization does not automatically lead to the best performance (18).

147

We also applied our method on a biological dataset and compared our results to the performance of the MaxLFQ summarization-based method used in the original publication (31). Proteins identified as DA by our method that were missed in the original publication were all filtered out because too few peptides were identified. Most of these proteins contain relatively strong evidence for DA based on visual inspection of the individual quantile normalized peptide intensities, illustrating that our method can reliably discover DA in proteins that suffer considerably from missing peptides across samples. Proteins which were denoted as DA in the original article but not by our method were typically identified by a lot of peptides but with a weak visual evidence for DA. Indeed, when a lot of peptide intensities are present, modeling at the peptide level does not contribute much to stabilize the overall log2 FC estimate. Mostly though, these small fold changes are not biologically relevant. However, when one seeks DA in sparse data, as is the case in most experiments, our method clearly outperforms classical approaches. We indeed identify possibly interesting effects in low abundant proteins without overfitting, omitting the need for extensive _a priori_ data filtering ( _e.g._ dropping proteins with less than two peptides present in at least nine out of 18 samples as done by Ramond _et al._ (31)). Consequently, our ability to detect DA in low abundant proteins combined with robustness against irrelevant changes in high abundant proteins is a favorable property.

We also showed that our fold change estimates are more stable for both the ribosomal and the BCAA synthesis modules, which are denoted as DA by Ramond _et al._ <u>(31). For TCA cycle</u> proteins, nine out of 12 were described as significantly more abundant in the mutant by these authors, while in our method, eight out of 13 TCA cycle proteins have log2 FC estimates that are in absolute value smaller than 1 × 10<sup>−9</sup> . Upon visual inspection, most of these proteins indeed contain very limited evidence for DA. Our method thus appears to provide more reliable data for follow-up analysis, thereby aiding researchers in drawing more correct conclusions. The fact that almost 82% of the proteins in our DA list of _Francisella_ proteins indeed contain less peptides in the condition with the lowest abundance of this protein, advocates the inclusion of imputation or censoring approaches, or even the combination of our method with estimates derived from spectral counting, which could be used as a rough but very simple validation technique. For example, hypothetical protein FTN_0400 could be a false positive because more peptides are identified in the mutant, although it appears to be less abundant (supplemental Fig. S18, File S1). This could be an indication of intensity-dependent censoring in the WT. Just like the peptide-based linear regression model, our RR model can handle missing values. The models we presented here assume missingness completely at random, an assumption that is flawed when analyzing shotgun proteomics data. Note, however, that peptide-based models partially correct for this by incorporating peptide-specific effects. Moreover, our strategies to improve robustness of the estimators can be easily plugged into censored regression methods or estimation approaches that adopt advanced imputation techniques for handling missing data (40).

Another interesting outlook is to model all proteins together by incorporating pathway or module level effects in the model in order to make stronger inferences on individual proteins belonging to a certain pathway. Finally, we want to stress the importance of data exploration. Plots of log2 peptide intensities for proteins that are flagged as differential abundant are very useful for assessing the biological relevance and the degree of belief one can have in the DA proteins that are returned by a method.

We are currently preparing an R/Bioconductor package for our method. Meanwhile, all code and data needed to repeat the data analysis in this manuscript is available in Supplemental <u>File 3.</u>

148

#### **9.1.7. Footnotes**

Author contributions: L.J.G. and L.C. designed research; L.J.G. and L.C. performed research; L.J.G. analyzed data; L.J.G., K.G., and L.C. wrote the paper.

* This research was supported in part by IAP research network “StUDyS” grant no. P7/06 of the Belgian government (Belgian Science Policy) and the Multidisciplinary Research Partnership “Bioinformatics: from nucleotides to networks” of Ghent University. L.G. is supported by a Ph.D. grant from the Institute for the Promotion of Innovation through Science and Technology in Flanders (IWT- Vlaanderen) entitled “Differential proteomics at peptide, protein and module level” (141573).

This article contains <u>supplemental Files S1 to S3.</u>

#### **9.1.8. References**

1. Oda Y., Huang K., Cross F. R., Cowburn D., and Chait B. T. (1999) Accurate quantitation of protein expression and site-specific phosphorylation. Proc. Natl. Acad. Sci. U.S.A. 96, 6591 – 6596

2. Ong S.-E., Blagoev B., Kratchmarova I., Kristensen D. B., Steen H., Pandey A., and Mann M. (2002) Stable isotope labeling by amino acids in cell culture, SILAC, as a simple and accurate approach to expression proteomics. Mol. Cell. Proteomics 1, 376 – 386

3. Gygi S. P., Rist B., Gerber S. A., Turecek F., Gelb M. H., and Aebersold R. (1999) Quantitative analysis of complex protein mixtures using isotope-coded affinity tags. Nat. Biotech. 17, 994 – 999

4. Hsu J.-L., Huang S.-Y., Chow N.-H., and Chen S.-H. (2003) Stable-isotope dimethyl labeling for quantitative proteomics. Anal. Chem. 75, 6843 – 6852

5. Ross P. L., Huang Y. N., Marchese J. N., Williamson B., Parker K., Hattan S., Khainovski N., Pillai S., Dey S., Daniels S., Purkayastha S., Juhasz P., Martin S., Bartlet-Jones M., He F., Jacobson A., and Pappin D. J. (2004) Multiplexed protein quantitation in Saccharomyces cerevisiae using amine-reactive isobaric tagging reagents. Mol. Cell. Proteomics 3, 1154 – 1169

6. Thompson A., Schäfer J., Kuhn K., Kienle S., Schwarz J., Schmidt G., Neumann T., and Hamon C. (2003) Tandem mass tags: A novel quantification strategy for comparative analysis of complex protein mixtures by MS/MS. Anal. Chem. 75, 1895 – 1904

7. Bantscheff M., Schirle M., Sweetman G., Rick J., and Kuster B. (2007) Quantitative mass spectrometry in proteomics: a critical review. Anal. Bioanal. Chem. 389, 1017 – 1031

8. Patel V. J., Thalassinos K., Slade S. E., Connolly J. B., Crombie A., Murrell J. C., and Scrivens J. H. (2009) A comparison of labeling and label-free mass spectrometry-based proteomics approaches. J. Proteome Res. 8, 3752 – 3759

9. Rodriguez J., Gupta N., Smith R. D., and Pevzner P. A. (2008) Does trypsin cut before proline? J. Proteome Res. 7, 300 – 305

10. Abaye D. A., Pullen F. S., and Nielsen B. V. (2011) Peptide polarity and the position of arginine as sources of selectivity during positive electrospray ionisation mass spectrometry. Rapid Commun. Mass Spectrom. 25, 3597 – 3608

149

11. Schliekelman P., and Liu S. (2013) Quantifying the effect of competition for detection between coeluting peptides on detection probabilities in mass-spectrometry-based proteomics. J. Proteome Res. 13, 348 – 361

12. Venable J. D., Dong M.-Q., Wohlschlegel J., Dillin A., and Yates J. R. (2004) Automated approach for quantitative analysis of complex peptide mixtures from tandem mass spectra. Nat. Meth. 1, 39 – 45

13. Gillet L. C., Navarro P., Tate S., Röst H., Selevsek N., Reiter L., Bonner R., and Aebersold R. (2012) Targeted data extraction of the MS/MS spectra generated by data-independent acquisition: A new concept for consistent and accurate proteome analysis. Mol. Cell. Proteomics 11, 1 – 17

14. Bilbao A., Varesio E., Luban J., Strambio-De-Castillia C., Hopfgartner G., Müller M., and Lisacek F. (2015) Processing strategies and software solutions for data-independent acquisition in mass spectrometry. Proteomics 15, 964 – 980

15. Liu H., Sadygov R. G., and Yates J. R. (2004) A Model for Random Sampling and Estimation of Relative Protein Abundance in Shotgun Proteomics. Anal. Chem. 76, 4193 – 4201

16. Old W. M., Meyer-Arendt K., Aveline-Wolf L., Pierce K. G., Mendoza A., Sevinsky J. R., Resing K. A., and Ahn N. G. (2005) Comparison of label-free methods for quantifying human proteins by shotgun proteomics. Mol. Cell. Proteomics 4, 1487 – 1502

17. Bantscheff M., Lemeer S., Savitski M., and Kuster B. (2012) Quantitative mass spectrometry in proteomics: critical review update from 2007 to the present. Anal. Bioanal. Chem. 404, 939 – 965

18. Milac T. I., Randolph T. W., and Wang P. (2012) Analyzing LC-MS/MS data by spectral count and ion abundance: two case studies. Statistics Interface 5, 75 – 87

19. Krey J. F., Wilmarth P. A., Shin J.-B., Klimek J., Sherman N. E., Jeffery E. D., Choi D., David L. L., and Barr-Gillespie P. G. (2014) Accurate label-free protein quantitation with highand low-resolution mass spectrometers. J. Proteome Res. 13, 1034 – 1044

20. Zhang Y., Fonslow B. R., Shan B., Baek M.-C., and Yates J. R. (2013) Protein analysis by shotgun/bottom-up proteomics. Chem. Rev. 113, 2343 – 2394

21. Goeminne L. J. E., Argentini A., Martens L., and Clement L. (2015) Summarization vs peptide-based models in label-free quantitative proteomics: Performance, pitfalls, and data analysis guidelines. J. Proteome Res. 14, 2457 – 2465

22. Clough T., Key M., Ott I., Ragg S., Schadow G., and Vitek O. (2009) Protein quantification in label-free LC-MS experiments. J. Proteome Res. 8, 5275 – 5284

23. Karpievitch Y. V., Dabney A. R., and Smith R. D. (2012) Normalization and missing value imputation for label-free LC-MS analysis. BMC Bioinformatics 13, S5.

24. Ting L., Cowley M. J., Hoon S. L., Guilhaus M., Raftery M. J., and Cavicchioli R. (2009) Normalization and statistical analysis of quantitative proteomics data generated by metabolic labeling. Mol. Cell. Proteomics 8, 2227 – 2242

25. Ahmed S. E., and Raheem S. M. E. (2012) Shrinkage and absolute penalty estimation in linear regression models. Computational Stat. 4, 541 – 553

26. Stein C. (1956) Inadmissibility of the usual estimator for the mean of a multivariate normal distribution. Proceedings of the Third Berkeley Symposium on Mathematical Statistics and

150

Probability, Volume 1: Contributions to the Theory of Statistics, pp. 197 – 206, University of California Press, Berkeley, Calif.

27. Copas J. B. (1983) Regression, prediction and shrinkage. J. Roy. Statist. Soc.. 45, 311 – 354

28. Huber P. J. (1964) Robust estimation of a location parameter. The Annals of Mathematical Statistics. 35, 73 – 101

29. Paulovich A. G., Billheimer D., Ham A.-J. L., Vega-Montoto L., Rudnick P. A., Tabb D. L., Wang P., Blackman R. K., Bunk D. M., Cardasis H. L., Clauser K. R., Kinsinger C. R., Schilling B., Tegeler T. J., Variyath A. M., Wang M., Whiteaker J. R., Zimmerman L. J., Fenyo D., Carr S. A., Fisher S. J., Gibson B. W., Mesri M., Neubert T. A., Regnier F. E., Rodriguez H., Spiegelman C., Stein S. E., Tempst P., and Liebler D. C. (2010) Interlaboratory study characterizing a yeast performance standard for benchmarking LC-MS platform performance. Mol. Cell. Proteomics 9, 242 – 254

30. Cox J., and Mann M. (2008) MaxQuant enables high peptide identification rates, individualized p.p.b.-range mass accuracies and proteome-wide protein quantification. Nat. Biotechnol. 26, 1367 – 1372

31. Ramond E., Gesbert G., Guerrera I. C., Chhuon C., Dupuis M., Rigard M., Henry T., Barel M., and Charbit A. (2015) Importance of host cell arginine uptake in Francisella phagosomal escape and ribosomal protein amounts. Mol. Cell. Proteomics 14, 870 – 881

32. Cox J., Hein M. Y., Luber C. A., Paron I., Nagaraj N., and Mann M. (2014) Accurate proteome-wide label-free quantification by delayed normalization and maximal peptide ratio extraction, termed MaxLFQ. Mol. Cell. Proteomics 13, 2513 – 2526

33. R Core Team (2014) R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria

34. Ritchie M. E., Phipson B., Wu D., Hu Y., Law C. W., Shi W., and Smyth G. K. (2015) limma powers differential expression analyses for RNA-sequencing and microarray studies. Nucleic Acids Res. 43, e47.

35. Amaratunga D., and Cabrera J. (2001) Analysis of data from viral DNA microchips. J. Am. Statist. Assoc. 96, 1161 – 1170

36. Bolstad B. M., Irizarry R. A., Åstrand M., and Speed T. P. (2003) A comparison of normalization methods for high density oligonucleotide array data based on variance and bias. Bioinformatics 19, 185 – 193

37. Callister S. J., Barry R. C., Adkins J. N., Johnson E. T., Qian W.-j., Webb-Robertson B.-J. M., Smith R. D., and Lipton M. S. (2006) Normalization approaches for removing systematic biases associated with mass spectrometry and label-free proteomics. J. Proteome Res. 5, 277 – 286

38. Rudnick P. A., Wang X., Yan X., Sedransk N., and Stein S. E. (2014) Improved normalization of systematic biases affecting ion current measurements in label-free proteomics data. Mol. Cell. Proteomics 13, 1341 – 1351

39. Daly D. S., Anderson K. K., Panisko E. A., Purvine S. O., Fang R., Monroe M. E., and Baker S. E. (2008) Mixed-effects statistical model for comparative LC-MS proteomics studies. J. Proteome Res. 7, 1209 – 1217

151

40. Karpievitch Y., Stanley J., Taverner T., Huang J., Adkins J. N., Ansong C., Heffron F., Metz T. O., Qian W.-J., Yoon H., Smith R. D., and Dabney A. R. (2009) A statistical framework for protein quantitation in bottom-up MS-based proteomics. Bioinformatics 25, 2028 – 2034

41. Ruppert D., Wand M. P., and Carroll R. J. (2003) Semiparametric Regression, Cambridge University Press, New York

42. Bates D M. M., Bolker BM, Walker S. (2014) lme4: Linear mixed-effects models using Eigen and S4. J. Statistical Software 67, 1 – 48

43. Lönnstedt I., and Speed T. (2002) Replicated microarray data. Statistica Sinica 12, 31 – 46

44. Smyth G. K. (2004) Linear models and empirical bayes methods for assessing differential expression in microarray experiments. Stat. Appl. Genet. Mol. Biol. 3, Article3

45. Benjamini Y., and Hochberg Y. (1995) Controlling the false discovery rate: A practical and powerful approach to multiple testing. J. Royal Statist. Soc. 57, 289 – 300

46. Schwämmle V., León I. R., and Jensen O. N. (2013) Assessment and improvement of statistical tools for comparative proteomics analysis of sparse data sets with few experimental replicates. J. Proteome Res. 12, 3874 – 3883

47. Rudra D., and Warner J. R. (2004) What better measure than ribosome synthesis? Genes Dev. 18, 2431 – 2436

48. Dressaire C., Redon E., Gitton C., Loubiere P., Monnet V., and Cocaign-Bousquet M. (2011) Investigation of the adaptation of Lactococcus lactis to isoleucine starvation integrating dynamic transcriptome and proteome information. Microbial Cell Factories 10, S18.

49. Henao R., Thompson J. W., Moseley M. A., Ginsburg G. S., Carin L., and Lucas J. E. (2012) Hierarchical factor modeling of proteomics data. Computational Advances in Bio and Medical Sciences (ICCABS), 2012 IEEE 2nd International Conference on, pp. 1 – 6

50. McCarthy D. J., and Smyth G. K. (2009) Testing significance relative to a fold-change threshold is a TREAT. Bioinformatics 25, 765 – 771

#### **9.1.9. Appendix**

##### **Ridge regression**

The untransformed, preprocessed intensities for each peptide 𝑝 in each run 𝑟 are assumed to follow a log-normal distribution. After log-transformation, these intensities become normally distributed. In all generality, for each protein, we propose the following peptide-based regression model that has also been proposed by Daly _et al._ (2008) [1]:


Herein, <mark>𝒙𝑝𝑟</mark><sup>is a row matrix with the covariate pattern related to peptide</sup> 𝑝 in run <mark>𝑟, 𝜷 =</mark> T 0 1 1 1 𝑔 𝑔 𝐺 [𝛽 , 𝛽1 … , 𝛽𝑚1 … , 𝛽𝑀1, … , 𝛽𝑚𝑔, … , 𝛽𝑀𝑔, … , 𝛽𝑀𝐺𝐺] is a vector with 1 + 𝑀 = 1 + ∑𝑔=1 <mark>𝑀𝑔</mark> parameters denoting the effects of 𝑀 predictors corresponding to 𝐺 covariates. <mark>𝛽</mark> 𝑝peptide is a peptide-specific effect for peptide 𝑝, <mark>𝑢</mark> 𝑟run <mark>a r</mark> andom run effect to account for within-run correlation, with <mark>𝑢</mark> 𝑟run <mark>~N(0, 𝜎</mark> 𝑢2 <mark>). 𝜀</mark> 𝑝𝑟 <mark>~N(0, 𝜎</mark> 2 <mark>) is a random error term.</mark>

We now want to introduce an extra penalization on the fixed effects beta by exploiting the link between ridge regression and mixed models (see section 4.2.4). Except for a fixed intercept

152


which the 𝑝th element is equal to 1 and all other elements equal to 0. 𝒙𝑟<sup>run</sup> is a row vector of dummies with the 𝑟th element equal to 1 and all other elements equal to 0. 𝑩 is an (1 + 𝑀+ 𝑃+ 𝑅) × (1 + 𝑀+ 𝑃+ 𝑅) diagonal matrix with diagonal elements [0 <mark>𝒈 𝒑 𝒓]</mark> , with 𝒈 a vector of length 𝑀 containing the 𝜆𝑔<sup>that corresponds to each parameter estimate</sup> 𝛽̂𝑚𝑔 𝑔 for <mark>𝑚𝑔 = 1, … , 𝑀𝑔</mark> and <mark>𝑔 = 1, … , 𝐺,</mark> 𝒑 a vector of length 𝑃 containing the <mark>𝜆peptide</mark><sup>that corresponds to each</sup> parameter estimate 𝛽̂𝑝peptide for 𝑝 = 1, … , 𝑃 and <mark>𝒓</mark> a vector of length 𝑅 containing the 𝜎̂𝜎̂𝑢22 that corresponds to each parameter estimate <mark>𝑢</mark> 𝑟run <mark>for 𝑟 = 1, … , 𝑅.</mark>

##### **Robust regression with M estimation**

To robustify our procedure against outliers, we use a weighted maximum likelihood method with Huber weights, as proposed by Zhou (2009) [2].


with 𝑗= 1, … , 𝐽 an indicator for observation. This weighted log-likelihood is solved iteratively. The mixed model is fitted while the weights are kept constant. Then, the weights are recomputed using Huber’s weight function on the residuals scaled with the residual standard deviation. This procedure is repeated until convergence. After convergence, the weighted BLUP estimator is given by:


with 𝑾= [𝑤1 … 𝑤𝑗 … 𝑤𝐽]𝑰𝐽×𝐽 and 𝑤1 to 𝑤𝐽 the weights corresponding to these observations and 𝑰𝐽×𝐽 a 𝐽× 𝐽 unity matrix. Zhou (2009) [2] showed that the weighted BLUP estimator is better

153

than the unweighted one in terms of bias and efficiency when the data contains some outliers but provides the same asymptotic efficiency when the model is correctly specified. Robust M estimation with Huber weights has also been used to robustify the negative binomial model in the popular RNA sequencing R package EdgeR [3].

##### **Empirical Bayes variance estimation**

Finally, we robustify our inference with limma’s e mpirical Bayes variance estimation (see section 4.2.2). In brief, limma assumes the following prior distribution on the error variance 𝜎𝑖2 for each protein 𝑖 (𝑖= 1, … , 𝐼):


with 𝜎02 a prior variance and 𝜒𝑑20 a 𝜒2 distribution with 𝑑0 degrees of freedom. A maximum a posteriori residual standard deviation 𝑠̃𝑖 for each protein is given by:


We then plug in this posterior residual standard deviation in the estimator for the standard deviation of the model parameter of interest, 𝛽̂𝑚𝑔 𝑔 (suppressing the indicator 𝑖 for notational <mark>convenience):</mark>


Herein, 𝑚𝑔, 𝑚𝑔 denotes the 𝑚𝑔th diagonal element of the matrix. This enables statistical inference with a moderated t-test with 𝑑𝑖 + 𝑑0 degrees of freedom:


Herein, 𝑑𝑖 is calculated as 𝐽−𝑡𝑟(𝑯), with 𝐽 the total number of observations and 𝑯 the hat matrix, which is calculated as follows:


##### **Implementation**

<mark>MSqRob builds on the lme4 R package for parameter estimation and statistical inference [4]. Shrinkage on fixed effect parameters is obtained by encoding them as random effects.</mark> To allow for robust M-estimation, a loop is placed around the model fitting procedure: after model fitting, Huber weights are calculated on the residuals scaled with the residual standard deviation. These weights are provided as arguments to the lmer function of the lme4 package, which allows to estimate the parameters via weighted log-likelihood. This procedure is repeated <mark>until convergence.</mark>

##### **References for the Appendix**

1. Daly, D.S. _et al._ , _Mixed- Effects Statistical Model for Comparative LC−MS Proteomics Studies._ Journal of Proteome Research, 2008. **7** (3): p. 1209-1217.

2. Zhou, T., _Weighting Method for a Linear Mixed Model._ Communications in Statistics - Theory and Methods, 2009. **39** (2): p. 214-227.

154

3. Zhou, X., H. Lindsay, and M.D. Robinson, _Robustly detecting differential expression in RNA sequencing data using observation weights._ Nucleic Acids Research, 2014. **42** (11): p. e91-e91.

4. Bates, D. _et al._ , _Fitting Linear Mixed-Effects Models Using lme4._ Journal of Statistical Software; Vol 1, Issue 1 (2015), 2015.

155

---

[← PART I: INTRODUCTION](02-part-i-introduction.md) · [Up: contents](index.md)
