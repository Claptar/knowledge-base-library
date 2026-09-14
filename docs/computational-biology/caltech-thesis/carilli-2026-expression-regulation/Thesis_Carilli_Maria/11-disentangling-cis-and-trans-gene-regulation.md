---
title: DISENTANGLING CIS AND TRANS GENE REGULATION
source: https://thesis.library.caltech.edu/18729/
source_file: sources/carilli-2026-expression-regulation/Thesis_Carilli_Maria.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DISENTANGLING CIS AND TRANS GENE REGULATION

**Source:** `Thesis_Carilli_Maria.pdf` from [carilli-2026-expression-regulation](https://thesis.library.caltech.edu/18729/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This chapter discusses a different kind of variation: genetic variation, and how we can use single-cell and bulk transcriptomic data to infer gene regulatory strategy differences between homozygous strains that display genetic variability. As Mendel crossed homozygous strains and used their hybrids’ features to determine hereditary laws [1], we discuss how hybrid crosses can be used to disentangle the regulatory differences between gene expression in parental strains. Again, setting up a model guided by biological hypotheses, although at a different level of abstraction, provides crucial insight into the mechanisms of regulation. By developing a framework for testing whether strains differ in gene expression due to _cis_ (local) or _trans_ (distal) effects, it became clear that the model would change if the _trans_ regulation acted in a dominant, log-additive (multiplicative), or different way to alter gene expression: setting up a model forced us to more clearly define what we mean by _cis_ and _trans_ regulation.

This chapter summarizes work from [48]. I.B.H., M.C., L.P. participated in the development of the models and statistical tests, and writing the manuscript. M.C. performed analyses and implemented the method as a software package. I.B.H. proposed the linear transformation and use of GLMs.

### **6.1 New Axes for New Insight**

In 1961, Jacob and Monod developed a theory of gene regulation in which they distinguished local effects ( _cis_ ) from distal regulation ( _trans_ ) [187]. Their work immediately raised the question of the relative contributions of these two regulation modalities [188, 189]. One approach for assessing whether _cis_ or _trans_ regulation is responsible for differences in gene expression between strains or species is to compare differences in expression of genes in parents to allele-specific differences in _𝐹_ 1 hybrids. This approach was explored in [190], who used crosses of C57BL/6J and CAST/Ei mice to study regulatory mechanisms that could explain differences in gene expression between parental strains. Their approach was developed in [191, 192], who used pyrosequencing to study the regulation differences between _D. melanogaster_ and _D. simulans_ . With the advent of RNA-seq, genome-wide scans

74

were possible, and [193] examined RNA-seq from _𝐹_ 1 crosses of C57BL/6J and CAST/EiJ to tease apart _cis_ and _trans_ contributions to gene expression differences between the parental strains. Similarly, [194] performed such an RNA-seq analysis using _Drosophila_ lines.

Formally, the idea of using crosses to study _cis_ and _trans_ contributions to differences in gene expression between strains or species is as follows: consider a gene with expression _𝑋𝑃_ 1 in a homozygous strain 1, _𝑋𝑃_ 2 in a homozygous strain 2, and expression _𝑋𝐻_ 1 for the haplotype from strain 1 in the _𝐹_ 1 cross of 1 and 2, and expression _𝑋𝐻_ 2 for the haplotype from strain 2 in the _𝐹_ 1 cross of 1 and 2. Let _𝑅𝑃_ = log2 � _𝑋𝑋𝑃𝑃_ <u>12</u> � and _𝑅𝐻_ = log2 � _𝑋𝑋𝐻𝐻_ <u>12</u> �. That is, _𝑅𝑃_ corresponds to the log2 fold change difference in expression between the two parental strains, and _𝑅𝐻_ to the log2 fold change difference between the expression of the hybrid haplotypes in the _𝐹_ 1 offspring. The connection between _𝑅𝑃_ , _𝑅𝐻_ , and regulation is as follows: consider that a gene can be regulated via _cis_ , _trans_ , or both (Fig. 1A). Gene expression measurements in the parents and hybrid (Fig. 1B), can be used to infer the nature of regulation underlying the difference in expression in the parental strains (Fig. 1C). Specifically, amending the classification of [192], we have:

- **_conserved:_** No change in gene expression indicating there has been no change in regulation, i.e. _𝑅𝑃_ = 0 and _𝑅𝐻_ = 0, which implies _𝑅𝑃_ − _𝑅𝐻_ = 0.

- **_cis:_** The relative difference in gene expression between the parents is the same as between the haplotypes in the hybrid indicating that the difference in parents is due to local _cis_ effects, i.e. _𝑅𝐻_ ≠ 0, _𝑅𝑃_ ≠ 0, and _𝑅𝑃_ = _𝑅𝐻_ which implies _𝑅𝑃_ − _𝑅𝐻_ = 0, arises from changes only in cis-regulatory elements.

- **_trans:_** Gene expression from the two haplotypes in the hybrid is the same, indicating that differences between the parents resulted from non-local _trans_ regulation, i.e. _𝑅𝐻_ = 0 and _𝑅𝑃_ ≠ 0, which implies _𝑅𝑃_ − _𝑅𝐻_ ≠ 0, arises from a change only in _trans_ -regulatory elements.

- **_cis + trans:_** _𝑅𝐻_ ≠ 0 and _𝑅𝑃_ ≠ _𝑅𝐻_ with sgn( _𝑅𝐻_ ) = sgn( _𝑅𝑃_ − _𝑅𝐻_ ) arises as a result of change in both _cis_ - and _trans_ -regulatory elements with changes in _cis_ and _trans_ contributing to changes in gene expression between strains in the same direction.

- **_cis_** × **_trans:_** _𝑅𝐻_ ≠ 0 and _𝑅𝑃_ ≠ _𝑅𝐻_ with sgn( _𝑅𝐻_ ) ≠ sgn( _𝑅𝑃_ − _𝑅𝐻_ ) arises as a result of compensatory change in both _cis_ - and _trans_ -regulatory elements with

75

changes in _cis_ and _trans_ contributing to changes in gene expression between strains in the opposite direction.


Figure 6.1: Geometry of parental and hybrid expression ratios can be used to assess regulatory differences between homozygous crosses. A) Diagram of the _cis_ , _trans_ , _cis + trans_ , and _cis_ × _trans_ types of regulatory differences. B) Homozygous parents with haplotypes _𝑃_ 1 and _𝑃_ 2, counts of RNA molecules for a gene ( _𝑋𝑃_ 1 and _𝑋𝑃_ 2 respectively), and the haplotypes in an _𝐹_ 1 hybrid along with counts for the gene ( _𝑋𝐻_ 1 and _𝑋𝐻_ 2). C) Differences in regulation between the parents are reflected in distinct ratios between counts _𝑋𝑃_ 1 _, 𝑋𝑃_ 2 and _𝑋𝐻_ 1 _, 𝑋𝐻_ 2. D. i) Illustration of how regulation differences emerge in log-fold changes _𝑅𝑃_ and _𝑅𝐻_ , D. ii) Linear transformation of _𝑅𝑃_ = log2 � _𝑋𝑋𝑃𝑃_ <u>12</u> � and _𝑅𝐻_ = log2 � _𝑋𝑋𝐻𝐻_ <u>12</u> � to yield orthogonal _cis_ and _trans_ coordinates, D. iii) Representation of proportion _cis_ in real projective space P<sup>1</sup> .

This classification corrects [192], which fails to properly assign regulation differences to _cis + trans_ when both _𝑅𝐻 <_ 0 and _𝑅𝑃 <_ 0. The relationships between _𝑅𝑃_ and _𝑅𝐻_ in general, can be visualized as lines and regions in a 2D plot [191], as illustrated in Fig. 1D(i). While this direct representation of _𝑅𝑃_ and _𝑅𝐻_ is useful, a quantitative assessment of the gene regulatory modalities reflected in _𝑅𝑃_ and _𝑅𝐻_

76

requires a biologically meaningful notion of distance between points in Fig. 1D(i). Consider, for example, the situation where _𝑋𝑃_ 1 = 2 _𝑋𝑃_ 2 and _𝑋𝐻_ 1 = 2 _𝑋𝐻_ 2, i.e. a 2-fold change in gene expression between the parents due solely to _cis_ regulation which corresponds to the point (1 _,_ 1) in Fig. 1D(i). The distance from this point to the origin (conserved), is ~~√~~ 2, whereas the same 2-fold difference in gene expression in the parents due solely to _trans_ regulation with _𝑅𝑃_ = 1 and _𝑅𝐻_ = 0 is distance 1 from the origin. This imbalance can be corrected via a linear transformation.

### **Geometry**


Figure 6.2: Contributions of _cis_ and _trans_ regulation to differences in gene expression between yeast strains, with data from [195] (n = 285,777 gene-cross combinations from 179 unique yeast parent crosses). A) Untransformed ratios, transformed ratios, and log2 of parental fold change versus proportion _cis_ , colored by regulatory assignments from [195]. B) Comparison of the results of [195] to the assignment of genes based on the proposed hypothesis testing and geometric assignment procedure. C) Reanalysis of the 285,777 gene-cross expression data from [195] using the proposed hypothesis testing and geometric assignment procedure.

To decouple the effects of _cis_ and _trans_ regulation on _𝑅𝑃_ and _𝑅𝐻_ we begin by noting that if the difference in parental expression is solely due to _cis_ regulation, then _𝑅𝑃_ = _𝑅𝐻_ , or equivalently _𝑅𝑃_ − _𝑅𝐻_ = 0 (orange vertical line in Fig. 1D(ii)). If the difference in parental expression is solely due to _trans_ regulation, then _𝑅𝐻_ = 0

77

(blue horizontal line in Fig. 1D(ii)). Therefore, the transformation from Fig. 1D(ii) to Fig. 1D(i) is obtained by


Thus, the inverse transformation from the coordinate system in Fig. 1D(i) to the coordinate system in Fig. 1D(ii) is given by


i.e., the transformation inverts the mapping of the vertical axis to the diagonal _cis_ line.

The determination of whether a difference in parental gene expression is due to _cis_ or _trans_ can now be understood to be an assessment of whether the line passing through the origin and a point ( _𝑅𝑃_ − _𝑅𝐻, 𝑅𝐻_ ) is a perturbation (due to noise in gene expression measurement) of the line Δ _trans_ , the line Δ _cis_ or sufficiently far away from the axes in Fig. 1D(ii) to merit a designation of Δ _cis + trans_ or Δ _cis_ × _trans_ (the designations are enumerated in Supp. Table 1 of [48]). In other words, the sufficient statistic is a point in real projective space P<sup>1</sup> (Fig. 1D(iii)), and the proportion of the difference in gene expression between parents that can be attributed to _cis_ can be understood to be a scaling of the angle of the line through the origin corresponding to the point in P<sup>1</sup> , i.e.,


### **6.2 Single and Multi-Sample Hypothesis Testing**

The determination of whether a measurement ( _𝑅𝑃, 𝑅𝐻_ ) reflects a difference in gene expression between parents due to _cis_ or _trans_ regulation, or both, requires a statistical assessment [196]. Specifically, hypothesis tests can be used to reject a null hypothesis of a difference in gene expression being due solely to _trans_ or solely to _cis_ . Geometrically, as evident from the linear transformation on log-fold changes, these two tests correspond to testing whether one can reject the null hypotheses that ( _𝑅𝑃_ − _𝑅𝐻, 𝑅𝐻_ ) is located on the _𝑥_ - and _𝑦_ - axes respectively.

We first developed a framework for hypothesis testing in this case where there are no replicates of the gene expression measurements, as in [195], with two hypothesis

78

tests (one for _cis_ regulation, the binomial test, and one for _trans_ regulation, the two sample binomial test), which are outlined below.

### **Binomial test**

To test the null hypothesis that there is no difference between expression of parental alleles in hybrids (or that the difference in regulation is purely _trans_ ) was performed on rounded integer counts from [195] using the function `scipy.stats.binomtest` [197]. This tests for the probability of having observed a value at least as extreme as _𝑘_ successes given probability _𝑝_ of success and a total of _𝑁_ trials by summing over binomial probabilities:


If _𝑋𝐻_ 1 is the allelic expression in the hybrid of one parental allele and _𝑋𝐻_ 2 is the allelic expression in the hybrid of the other parental allele, the binomial test was performed with _𝑘_ = _𝑋𝐻_ 1 _, 𝑁_ = _𝑋𝐻_ 1 + _𝑋𝐻_ 2, _𝑝_ = 0 _._ 5 and a two-sided alternative hypothesis.

### **Two sample binomial ratio test**

To test the null hypothesis that there is no difference in the ratio of expression of alleles in parents and allelic expression in hybrids (or that the difference in regulation between parents is purely _𝑐𝑖𝑠_ ), we performed a two sample binomial ratio test in which we assumed both _𝑋𝑃_ 1 and _𝑋𝐻_ 1 are sampled from a binomial distribution with the same probability of success _𝑝𝑠_ . Using


we calculated the grid of probabilities over possible _𝑃_ 1 and _𝐻_ 1 values:


where _𝑁𝑃_ = _𝑋𝑃_ 1 + _𝑋𝑃_ 2 is the total number of counts from parents and _𝑁𝐻_ = _𝑋𝐻_ 1 + _𝑋𝐻_ 2 is the total number of counts from the hybrid. We then calculated the probability of having observed values at least as extreme as the observed _𝑋𝑃_ 1 and _𝑋𝐻_ 1.

79

To account for multiple testing, the significance values can be corrected using the Benjamini-Hochberg method to obtain false discovery rates [198]. In all of the reported results, rejected the null hypothesis for tests with false discovery rates less than 0.05.

### **Generalized linear models for multiple samples**

In the case where replicates have been obtained, a generalized linear model (GLM), as is commonly used for differential expression in bulk RNA-seq [199, 200], can be adapted to utilize gene expression variance estimates within parents and hybrids, providing estimates of _no cis_ and _no trans_ regulation, both overall and conditionspecific.

Our framework differs from previous applications of GLMs for _cis/trans_ distinction [201] by virtue of using one GLM for all data (parental counts, hybrid ASE values, with all conditions represented), rather than fitting three separate models to different subsets of the data (e.g., only parental counts for one test or only hybrid ASE values for another). We do this by developing a model with weights for overall and condition-specific _cis_ and _trans_ regulatory effects, as well as including condition intercepts to properly attribute observed allele expression patterns to regulation or condition. In addition, our approach allows us to propose different hypotheses about the nature of the _trans_ regulatory effect: if it is log-additive, dominant, or free (described below). To properly account for the overdispersion and discreteness of RNA-seq counts, we fit a GLM with a negative binomial likelihood function and log link function.

**One condition:** In the simplest case, we set the geometric mean of parental expression to be the intercept _𝛽_ and include weights for the _cis_ regulatory difference ( _𝛽𝐶_ ) and _trans_ regulatory difference ( _𝛽𝑇_ ) between parental strains. This allows the normalized expression from the parental alleles ( _𝑋𝑃_ 1 _, 𝑋𝑃_ 2) and normalized allelic expression from the hybrids ( _𝑋𝐻_ 1 _, 𝑋𝐻_ 2) to be modeled under three different hypotheses of _trans_ regulation.

The first hypothesis ( **log-additive** ) assumes that the _trans_ expression difference between parental strains at each allele is influenced by both sets of parental chromosomes multiplicatively, and is thus reduced to the square root of the full parental effect in the hybrids. The design matrix is accordingly

80


A second hypothesis ( **dominant** ) assumes that the _trans_ expression difference between parental strains is the same regardless of if both sets or one set of parental chromosomes are present: it is the same in the parents and hybrids, and the design matrix is


Finally, and most analogous to previous hypothesis testing methods [201], _trans_ expression differences between parental strains can have an unconstrained relationship ( **free** ) with their effects in the hybrids by allowing each hybrid to have individual specific effects (denoted below with the subscript _𝑖_ indexing the hybrid samples). The resulting design matrix is


For all models, we can test the null hypothesis of _no cis_ differences between parental strains by testing if _𝛽𝐶_ = 0 and the null hypothesis of _no trans_ differences by testing if _𝛽𝑇_ = 0.

**Multiple conditions:** As more conditions are added to the experimental design, they can be naturally incorporated into the GLM framework, with condition-specific _cis_ and _trans_ weights as well as intercepts and interaction terms. For example, we fit data for liver and BAT samples for mice grown in warm and cold environments (four separate organ/environment) using the following model under the log-additive _trans_ hypothesis:

81


The subscripts _𝐶,𝑇, 𝑂_ and _𝐸_ refer respectively to differential _cis_ regulation between strains, differential _trans_ regulation between strains, organ, and environment effects, with combinations denoting their interactions (e.g., _𝛽𝐶𝑂_ models the organ-specific _cis_ effect). This is also compatible with any of the three previously described _trans_ hypotheses (log-additive, dominant, and free).

### **Classifying genes based on statistical test results**

The results of the two tests for single sample experiments or experiments with replicates are used to categorize genes as outlined in Table 6.1.

|Single sample: Binomial<br>test|Single sample: Binomial<br>ratio test||
|---|---|---|
|Replicates: _𝛽𝐶_=0|Replicates: _𝛽𝑇_=0||
|**(null:** **_no cis_)**|**(null:** **_no trans_)**|**Classification**|
|Fail to reject|Fail to reject|conserved|
|Reject|Fail to reject|_cis_|
|Fail to reject|Reject|_trans_|
|Reject|Reject|_cis & trans_(_cis + trans_or<br>_cis_×_trans_by geometry)|


Table 6.1: Statistical assignments of gene regulatory differences. Genes assigned to _cis, trans, cis + trans_ or _cis_ × _trans_ regulation based on two statistical tests, described above for single sample or replicate experiments. If both statistical tests are rejected, regulatory assignment can be made by locating the point ( _𝑅𝑃_ − _𝑅𝐻, 𝑅𝐻_ ) in the transformed space and following the geometric assignments listed in Supp. Table 1 of [48]

Note that some care must be taken when interpreting a _cis_ or _trans_ assignment within this hypothesis testing framework. For example, a _cis_ assignment is made when "no _cis_ " can be rejected but "no _trans_ " cannot be rejected. Failure to reject "no _trans_ " does not imply that one can accept the null hypothesis, but we utilize the assignment of _cis_ in this case for simplicity for users. However, this caveat should be taken into account when interpreting the assignments of _cis_ , _trans_ , and _cis_ & _trans_ assignments.

82

### **Simulation Study**

We also performed genome-wide simulations of parental and F1 hybrid allelespecific RNA-seq count data, generating a total of 6,000 genes per simulated dataset. Genes were randomly assigned to low, medium, or high expression classes with mean counts of 20, 100, or 500. We simulated 45 parameter scenarios, varying biological replication per group (4, 6, 8, 16, and 32), negative-binomial dispersion (alpha = 0.02, 0.20, 0.50), ASE-informative read fraction (0.05, 0.20, 0.40), and absolute log2 cis and trans effect sizes (0.125, 0.25, 0.5, 1, 1.5, 2, and 3). For each of the 45 scenarios we performed a full analysis on each of the 10 datasets using XgeneR and GLM-based tests for cis and trans effects and also an analysis using parent, ASE, and parent-vs-hybrid ratio tests. Performance was evaluated using power, type I error, ROC/AUC, parameter recovery, and regulatory-class assignment accuracy. Full details of the data-generating model, parameter grid, and diagnostic results are provided in the Simulation Supplement Figures and Simulation Methods of [48].

### **Application of hypothesis testing**

We applied the single sample tests to data from [195], which consist of bulk RNA-seq performed on hybrid and parental strains of genetically divergent _Saccharomyces cerevisiae_ . Briefly, [195] generated hybrid crosses from 26 parental yeast isolates derived from diverse environmental conditions. In [195], genes were classified according to the representation shown in Fig. 1D(i). First, both _𝑅𝑃_ and _𝑅𝐻_ were tested for statistically significant differences from 0 and assigned "null" (our _conserved_ ) if both tests failed to reject the null hypothesis (one-sample allele-specific expression tests); then, changes between parental and hybrid allelic ratios were tested for significance (two-sample allele-specific expression tests). For genes that passed significance thresholds, regulatory assignments were made by dividing the untransformed 2D plane into cones (Fig. 2A). We reassigned genes based on our hypothesis tests as derived from the transformed coordinate system (Fig. 2C), with one test with the null hypothesis of _cis_ regulation and one with the null hypothesis of _trans_ regulation, thereby putting the two regulation strategies on equal footing. Compared to the original study, we found major differences in assignment (of Fig. 2B, Supp. Fig. 3 of [48]).

Interestingly, whereas [195] conclude that "the transcriptome is globally buffered at the genetic level mainly due to trans-regulatory variation in the population", we find that a considerable amount of difference in gene expression can be attributed to

83

_cis_ (Supp. Fig. 3C of [48]), with the difference due to [195] deriving assignments in the untransformed coordinate system using a statistical testing procedure that treats _cis_ and _trans_ regulation asymmetrically. Specifically [195] report 57,253 cases where gene expression difference is due to _trans_ regulation (Supp. Fig. 3A of [48]). We find 39,063 cases that can be assigned to _trans_ (Supp. Fig. 3B of [48]). These numbers are similar; however, [195] report 2,804 cases assigned to _cis_ (Supp. Fig. 3A of [48]), whereas we find _7,441_ (Supp. Fig. 3B of [48]). Furthermore, we find 2,313 cases assigned to _cis + trans_ (Supp. Fig. 3B of [48]) versus 1,727 in [195] (Supp. Fig. 3A of [48]). While these discrete classifications can be compared, reflecting the outcomes of statistical tests, there is a range of proportions _cis_ for genes within a classification (Fig. 6.2A and C). Notable, the _trans_ classifications of [195] extend up to a calculated proportion _cis_ of almost 1.0 (Fig. 6.2A), while our assignments are restricted to a region closer to the _trans_ axis, explaining the possible over-assignment of _trans_ regulation in the original study. While it has been suggested that _trans_ regulation accounts for more variation in expression within species and _cis_ regulation accounts for interspecific divergence [202], our results indicate that _cis_ regulation, with still fewer assigned instances than _trans_ , may play a larger role than previously assessed. Overall, there is a marked difference between our results and those of [195] (Supp. Fig. 3C of [48]).

We tested our approach for multiple samples on data from [201], in which two wild-derived mouse strains and their F1 hybrids were used to study the effect of genotype and environment (temperature) on gene expression divergence in rapidly evolving strains. Two inbred lines of house mice were derived from mice from a cold environment (Saratoga Springs, New York, USA) and a warm environment (Manaus, Amazonas, Brazil) [201], and two tissues, brown adipose tissue (BAT) and liver, were evaluated in each of the strains and their F1 hybrids, also raised at the two different temperatures. The experiment was performed in six replicates each of male and female parents, as well as six replicates each of male and female F1 hybrids [201] (Fig. 3A). The GLM framework allows the joint analysis of all samples (parents and hybrids) rather than requiring that separate tests be run on separate subsets of the data (e.g., differential expression between parents, differential expression between hybrid allelic expression, and a ratio test as in [201]). It further enables explicit modeling of specific biological hypotheses of _trans_ regulatory action.

Restricting our analysis to a single tissue, temperature, and sex (brown adipose tissue collected from male mice reared in the cold temperature), we fit a GLM with

84

the free hypothesis and classified genes based on the reduced models of no _cis_ or no _trans_ regulation (Fig. 3B). Consistent with our single sample analyses, we noted an increase in the number of _cis_ assigned genes from 478 in the original study [201] to 877 (Fig. 3C). This trend held in different tissue and temperatures (Supp. Fig. 7 of [48]). We further fit the free model to all male samples, including environment (cold/warm) and organ (liver/BAT) specific _cis_ and _trans_ weights (Fig. 3D). We identified genes that exhibited significant overall _cis_ and _trans_ regulatory changes (Fig. 3E, top panel), as well as those that were only significantly different in one organ (Fig. 3E, middle panel) or environment (Fig. 3E, bottom panel). Among these genes were several with functions related to body fat and temperature. For example, _Acad10_ , which was identified as having an overall significant _trans_ regulatory difference between the strains (Fig. 3E, top panel), codes for Acyl-coA dehydrogenase family member 10. This protein plays a role in lipid metabolism and fatty acid oxidation, and deficiency has been to shown to lead to abnormal weight gain and deficiency in glucose tolerance in mice [203]. _Serinc5_ , which was shown to have organ specific regulatory differences between parental strains, codes for serine incorporator 5, a protein that incorporates serine into cell membranes to facilitate the synthesis of sphingolipids [204], which themselves have been implicated in thermal adaptation and response to heat across eukaryotic organisms [205, 206]. Notably, _Notch2_ was found to have only environment (temperature) specific and not overall _cis_ regulatory differences between parental strains, concordant with [207] reporting temperature sensitivity of the Notch signaling pathway underlying species’ level differences in development and plasticity in mice. These genes are plausible candidates for differential regulation between mouse strains adapting to life in cold and warm environments. The flexibility of the GLM framework facilitates identification of genes with unique regulatory patterns, such as the tissue and organ-specific effects, a key improvement over post-hoc comparisons of multiple model fits that would be otherwise required.

### **Proportion** **_cis_**

In addition to naturally revealing the appropriate hypothesis tests to conduct for attribution of gene expression difference in parents to _cis_ or _trans_ , the linear transformation we propose leads directly to a meaningful measure of the proportion of difference in gene expression that can be attributed to _cis_ regulation (or _trans_ ) (Equation 6.3). To illustrate this, we re-analyzed a dataset of gene expression from human-chimpanzee cell line hybrids [208], calculating the proportion _cis_ according

85

to Equation 6.3. In [208], the proportion _cis_ was calculated using slope, as is natural to do when working in the untransformed coordinate framework, whereas the correct calculation (Equation 6.3) uses angle in the transformed coordinate system. While the absolute differences are small (Fig. 4A), with a maximum difference of 0.045, the relative difference is large when the proportion _cis_ is small (Fig. 4B), and can be as high as 57%. Moreover, our computation provides a biologically interpretable measure of proportion _cis_ . We found several genes in [208] exhibiting high variance in proportion _cis_ (Fig. 4C), and identified interesting differences between cell types (Supp. Fig. 8 – 11 of [48]), perhaps relating to cell cycle status or developmental stage of different cell types. For example, _Mageh1_ codes for a member a family of proteins that mediate apoptosis, cell growth, and cell cycle [209, 210]: the difference in proportion _cis_ across the assayed cell types could indicate different regulatory strategies at different stages of cell cycle, implicating it as an interesting candidate for follow-up experimental validation to explore this question. _Dnmt1_ encodes DNA methyltransferase 1, a protein that copies the methylation patterns from template DNA strands onto newly synthesized strands during cell replication [211]: its variation in proportion _cis_ across cell types may be evidence of varying regulation between actively proliferating versus quiescent cells, or cell types at different stages of development. These examples show that an analysis of the variation in proportion _cis_ across cell types allows the identification of patterns (and the genes displaying them) beyond considering classifications into discrete groups (e.g., _cis_ or _trans_ ).

### **Discussion**

The use of crosses between strains to identify the nature of differential regulation is a powerful tool for genetics studies that is particularly relevant now that single-cell RNA-seq can be used for cell type resolution. Moreover, while original studies were limited to a handful of genes, genome-wide single-cell RNA-seq assays can complement genome-wide eQTL studies.

We have shown that geometric considerations reveal the need for applying a linear transformation prior to visualization. The linear transformation highlights independent axes that lead naturally to hypothesis tests for classifying genes according to the type of regulation underlying differences in gene expression between parents. While we have focused on explaining differences between parents that fall into five categories (conserved, _cis_ , _trans_ , _cis + trans_ , _cis_ × _trans_ ), our approach can be extended to finer classifications such as in [195]. We note that in the hypothesis testing framework, referring to a gene as having differences in expression explained

86

by _cis_ or _trans_ is technically incorrect. This is because the rejection of the _cis_ null hypothesis only shows that the difference in gene expression is not due solely to _cis_ regulation. This does not mean that the difference in gene expression can or should be attributed solely to _trans_ . The same is the case for rejecting the _trans_ hypothesis. In Fig. 2, our coloring of genes as _cis_ or _trans_ is therefore not precise, but we have done so to facilitate comparisons to previous work.

Our single sample statistical tests depend on the assumption that read counts are binomially distributed, which is standard in the absence of biological replicates. However, when replicate samples are available, we can better assess the extent of technical variation and use generalized linear models. Although our results are shown using commonly applied estimation techniques for negative binomially distributed counts [199], we also measure the extent to which differing estimates of variation change the results (see the Supplement if [48]) [199, 200]. We encourage experimentalists to include enough samples in the experimental design such that heuristic estimations are unnecessary and the observed sample variation can be used for hypothesis testing.

Finally, we note that our framework is general and can be applied to more complex experimental designs, regulatory hypotheses, and phenotypes other than gene expression. For example, the versatility of our GLM framework allows modeling of _cis_ or _trans_ differences in specific conditions and in interactions between specific conditions. In terms of additional phenotypes, with single-cell RNA sequence data our approach could be used in conjunction with methods such as [212, 47] to assess the regulation mechanisms underlying differences in biophysical aspects of gene transcription, splicing and degradation. Such extensions will be particularly interesting to explore in conjunction with complementary modalities [213, 214].

87


Figure 6.3: Multi-sample regulatory assignment can be determined using generalized linear models and condition-specific hypothesis tests. A) Cartoon of experimental design set up from original study (adapted from Fig. 1C of [201]). B) Model predicted ratios colored by GLM determined regulatory assignments as described in. The free model was fit to brown adipose tissue from male mice reared in the cold (n = 6 NY mice, n = 6 BZ mice, and n = 6 hybrid crosses, and n = 5,970 genes). C) Untransformed (original) regulatory assignments (reported in [201]) derived from three independent model fits and statistical tests differ from transformed regulatory assignments derived using the unified GLM framework (genes and assignments from B, excepting genes that were categorized as conserved by both the original and our testing procedure, which are not shown). D) The free model was fit to samples from all four environment/organ pairs (BAT/cold, BAT/warm, liver/cold, liver/warm, n = 6 NY/BZ/hybrid samples per condition) with weights for environment and organ-specific regulatory effects. The negative log10 of false discovery rates (FDR) highlights several genes that exhibit significant _cis_ or _trans_ behavior overall or only in an organ or environment-specific manner. E) For the same genes, GLM predicted (bar plots) and observed gene expression (box plots with counts normalized by the total count per sample for parents and per haplotype for hybrids) for parental and hybrid alleles (n = 6 samples per box, with the box showing values’ interquartile ranges and a line at the mean and whiskers extending to min/max values).

88


Figure 6.4: In addition to broad regulatory categories, genes can display subtle differences in their proportion of _cis_ regulation. A) Comparison of slope (as previously defined [208], x-axis) and angle (y-axis) for determining proportion _cis_ . B) Ratio of slope and angle determination of proportion _cis_ (dark red line, dashed line displays equality). Note that at small values of proportion _cis_ , the slope can be over 50% the determined angle. C) Gene expression data from [208] (human-chimpanzee crossed cell lines) was used to determine cell type specific proportion _cis_ . These four genes display high variance in proportion _cis_ across cell types (black points are determined proportion _cis_ in n = 72 cell types).

89

_C h a p t e r 7_

---

[← BIOPHYSICAL MODELS IN VARIATIONAL AUTOENCODERS](10-biophysical-models-in-variational-autoencoders.md) · [Up: contents](index.md) · [REGULATION OF BIOPHYSICAL PROCESSES IN FOUNDER MOUSE STRAINS →](12-regulation-of-biophysical-processes-in-founder-mouse-strains.md)
