---
title: REGULATION OF BIOPHYSICAL PROCESSES IN FOUNDER MOUSE STRAINS
source: https://thesis.library.caltech.edu/18729/
source_file: sources/carilli-2026-expression-regulation/Thesis_Carilli_Maria.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# REGULATION OF BIOPHYSICAL PROCESSES IN FOUNDER MOUSE STRAINS

**Source:** `Thesis_Carilli_Maria.pdf` from [carilli-2026-expression-regulation](https://thesis.library.caltech.edu/18729/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In Chapter II, we showed that differences in gene expression _variance_ between two groups is as revealing differences in gene expression means. In Chapters III, we showed how the _variation_ (in fact, the whole distribution!) of scRNAseq counts is appropriately modeled with a mathematical framework motivated by what we know about the data generation process, giving insight into the underlying biophysics of the system that produced the them. In Chapters IV and V, we presented strategies for scaling these models to inference loads required for genetic association tests. In Chapter VI, we developed a strategy for determining the contribution of two orthogonal gene regulatory strategies given genetic _variation_ in homozygous strains. In this Chapter, we use the theory and tools of the preceding chapters to examine differences in regulation of _biophysical mechanism_ between eight founder mouse strains. We show that distinct regulatory patterns underlie transcriptional, splicing, and export rates of RNA, and that expression changes between strains can be attributed to changes in the processing of RNA.<sup>1</sup>

### **7.1 Adapting Modeling Strategies**

In this section, we describe how strategies from the previous chapters (biophysical models including technical capture and GLM hypothesis testing framework) as they had been developed for one particular technology and setting had to be adapted for this new study. This demonstrates that analyses of transcriptomic data cannot be "plug and play," but require careful consideration of the experimental technology and values being compared.

### **The Collaborative Cross Founder Mice**

Complex human traits and diseases arise from the interaction of many naturally occurring variants in DNA and environmental factors. To facilitate the study of system genetics, or how variants interact and influence genes and biochemical pathways across contexts, the Collaborative Cross (CC) mouse strains were designed

> 1It could be argued that this a more coherent uses of the terms _cis_ and _trans_ regulation: what does "regulation of a gene" mean but the regulation of the processes that it undergoes?

90


Figure 7.1: An overview of the dataset and fitting procedure. A. The eight genetically diverse founder mice being compared. B. Eight tissues from eight individuals from each of the eight strains and 7 crosses (B6 with all others) were collected and snRNA-seq performed. C. Collected samples (cells) are aligned to a joint reference genome to produce counts for unspliced and spliced molecules, then each unique strain-individual-tissue-cell type was used to fit the a biophysical model to obtain the parameters burst size, relative splicing rate, and relative degradation rate per gene. Images in A. and B. were adapted from [215], and the sequencing step in C. from [37].

[216, 217]. The mouse is the primary model organism for human disease, with high protein-coding sequence similarity to humans and shared mammalian physiology, but even within the species, different mouse strains display different behaviors, phenotypes, and disease predispositions. The CC strains were designed to "optimally" investigate the relationship between genetic variation and complex traits by selectively interbreeding eight founder mouse strains [216, 217]. The eight founder mouse strains were chosen to capture over 90% of the genetic diversity in _Mus musculus_ and consiste of five classical inbred/lab strains: C57BL/6J (B6J, which is the most commonly used lab strain and the mouse whose genome serves as reference), A/J (AJ), NOD/LtJ (NODJ), 129S1/SvImJ (129S1J), and NZO/H1LtJ (NZOJ); and three wild-derived strains: WSB/EiJ (WSBJ), PWK/PhJ (PWKJ), CAST/EiJ (CASTJ). [216, 217]. These strains range from about 5.9 million (AJ) to 22.9 million SNPs compared to the B6J reference with at least one in 60-90% of genes [215].

To comprehensively characterize the variation in gene expression in these parental mouse strains, a recent publication of a single nucleus RNA-seq dataset (snRNA-seq) assayed 5.2 million nuclei from eight core tissues (heart, gonads, gastrocnemius,

91

adrenal gland, kidney, diencephalon and pituitary gland, liver, and cortex and hippocampus) from at least eight individuals from each of the eight strains [218]. This revealed extensive transcriptomic variation across the strains at cell type resolution, with positive correlation between transcriptomic variation and strain genetic divergence [218]. The observed gene expression variation in the parents that is due to genetic divergence can be explained by either _cis_ or _trans_ variants, as discussed in Chapter II, with _cis_ regulation attributable to sequence alteration near or within the target gene and _trans_ regulation to variants in distal regulatory regions (like enhancers or _cis_ variants that affect transcription factors).

To identify if the observed differences in CC founder strain gene expression could be attributed to _cis_ or _trans_ regulation, seven heterozygous F1 crosses were made with a dam of B6 and each of the other seven founder strains as sires, and snRNA-seq data was collected from the same eight tissues were assayed in eight individuals from each cross (and eight additional B6J samples for technical comparison with the initial study) [215]. The F1 dataset comprises 5,346,886 nuclei (after quality control) from eight tissues classified into 92 distinct cell types [215]. We applied the GLM framework developed in Chapter VI to the total counts of genes summed over unique cell types ("pseudobulk" expression per individual sample) to identify 25,777 genes (91% of detected genes) as being regulated (non-conserved) in at least one of the 92 cell types in one or more crosses [48, 215]. It was found, in agreement with previous work [201, 219], that while _cis_ regulation seems to be the primary driver of strain gene expression differences, _trans_ regulatory differences displays more cell type and tissue specificity (present in a given cell type or tissue and not in others and changes with context) [215].

While this comprehensive analysis of gene regulatory strategies over the founder mice strain will be of great utility for interpreting expression patterns in the collaborative cross lines derived from them, we can go a step deeper. Pseudobulking and comparing the mean of single-nucleus data obscures the biological signal in the distribution of counts. By applying biophysical models to the snRNA-seq data, we can link regulatory differences in cellular processes.

**Aligning to joint reference genomes for allele specific quantification.** To obtain allele specific counts of unspliced and spliced molecules, we built a strain specific reference for each of the non-B6J founder strains by incorporating variants from each of the founder mouse https://ftp.ebi.ac.uk/pub/databases/mousegenomes/REL2112-v8-SNPs_Indels/mgp_REL2021_snps.vcf.gzstrain Variant Call Format (VCF)

92

file [220] into the GRCmm39 (B6J) reference genome using `g2gtoolsv 0.2.0` . We then generated a joint alignment index per non-B6 founder strain by concatenating the strain-specific reference and the unedited GCRmm39 reference and aligned reads using `kb-python 0.28.0` [25]. This process treats genes from B6 and the other founder strains as different "genes." We note that this does not give access to all genes, but only those containing SNPs in regions that reads overlap. If a read is ambiguously assigned (compatible with genes from both strains), it is discarded, and thus not all allele specific expression can be resolved<sup>2</sup> We pseudo-aligned all data (founder and F1) to the seven joint references using the `--nac` option, which generates nascent, mature, and ambiguous counts per gene [25]. For each cross, we retained reads that mapped to the "correct" allele for the homozygous founder strains (e.g. reads we know came from a B6 mice that mapped to the GRCmm39 copy of the gene, reads we know came from a CASTJ mouse that aligned to the CASTJaltered reference), and allele specific reads that were consistent with parentage for the hybrids (e.g. for each B6-CASTJ cross F1, we had now two "cells," one set with counts from genes aligning to GRCmm39 and the other with counts aligning to the CASTJ-altered reference). We treated the nascent counts as spliced, and summed the counts belonging mature and ambiguous reads for spliced counts.

**Length biased capture of spliced molecules.** The CME technical noise model discussed and fit in Chapter III includes a technical capture rate dependent on the length of gene (length-biased capture) for nascent/unspliced molecules [37, 181]. That is, in the Poisson process of capture, each nascent molecule has a rate _𝜆𝑁𝑔_ = _𝐶𝑁_ × _𝑙𝑔_ of being captured and reported, with _𝑙𝑔_ being the gene length and _𝐶𝑁_ a constant:


were N _𝑔_<sup>′are the unspliced/nascent RNA molecules for a given gene in the cell and</sup> M _𝑔_ are the observed or captured unspliced/nascent RNA molecules for that gene.

This was motivated by the observation that in 10x Genomics scRNA-seq technologies, which capture mRNA using poly(T) probes, probes sometimes hybridize to internal poly(A) tracts within the gene body. There is thus positive correlation between the number of unspliced molecules and the gene length, as longer genes contain more poly(A) tracts [181]. Inferring parameters for these counts without correcting for this bias leads to estimates of burst sizes that _increased_ with gene

2Long-read RNA-seq data would allow better quantification of allele specific expression.

93


Figure 7.2: A. As an example of length bias in Parse snRNA-seq data, summing over all cells in the adrenal gland, unspliced RNA molecule total counts sum positively with gene length; spliced molecules also showed correlation with exonic length (union of all exons in a gene). B. For fits with no length-biased capture, length-biased capture of unspliced molecules, and length-biased capture of both spliced and unspliced molecules, the correlation of inferred burst sizes ("b"), relative splicing rates ("beta"), and relative export rates ("gamma") for sample "024 B6J 10F 08 B6J" in zona glomerulosa cells in the adrenal gland. C. Over the grid of fit sampling parameters, there was one clear optimum. D. Multiplying the optimum sampling parameter( log10-6.9,log10-5.25) by gene lengths recovers the inferred per gene capture rate.

length, while previous work suggests the opposite [181, 221]. When length-biased capture is including in the technical noise model in the CME, the positive correlation is removed for more consistent estimations [181, 221].

The snRNA-seq data for the founder and F1 datasets were generated using Parse Biosciences’ split-pool barcoding technology (Evercode WT MEga Kits v2), in which cells are put into wells on a plate, pooled and mixedl and then re-plated iteratively to generate unique barcodes per cell. This technology includes _two_

94

primers per capture well, in contrast to 10x capture, one set of poly(T) probes for mRNA poly(A) hybridization and another set of random hexamers that can bind to random (internal or non-coding) locations along RNA molecules. We noted that this introduces a length bias for spliced molecules as well: spliced molecules from genes with longer total _exonic_ lengths had longer tracts for probe hybridization, and thus are captured at a higher frequency than shorter molecules 7.2A. To account for this, we introduce a spliced/mature capture rate that depends on the total _exonic_ length of the gene (not distinguishing between isoforms, but summing over the union of all exonic content _𝑙𝑔𝑒_ ):


Here M _𝑔_<sup>′are the spliced/mature RNA molecules in the cell and M</sup><sup>_𝑔_are the observed</sup> or captured spliced/mature RNA molecules.

Examples of parameters inferred without a length-biased capture rate in the model, length-biased capture of only unspliced molecules, and length-biased capture of both spliced and unspliced molecules are shown in Fig. 7.2B. Without length-bias, the inferred parameters were unphysically large (for example, burst sizes around 10<sup>4</sup> ), or at the bounds of what we set for plausible physicality (7.2B). Including only unspliced gene length-bias correctly induced negative correlations between the inferred burst sizes and gene length ([181, 221]), but also negative correlation between the other two parameters and gene length (Fig. 7.2B). By including both spliced and unspliced length-biased capture, the inferred parameters remained within physically reasonable limits and displayed trends in line with expectations from previous work [181, 221, 222]

**_Monod_ fits.** We fit _Monod_ to all genes in all cell types per individuals in the founder and F1 dataset if the gene had at minimum two spliced and two unspliced counts and an unspliced and spliced mean over that individual’s cell type of at least 0.001. We fit over a 6 by 5 grid of technical capture rates to find the one at which genes had highest likelihood.

Overall, we performed 22,890,370 _Monod_ gene parameter inferences (each being a unique gene / individual mouse / cell type / tissue combination). As this is data collected from individual nuclei (not cells), the estimated parameters are average burst size _𝑏_ , splicing rate relative to transcriptional initiation rate _𝛽_ = _𝛽_<sup>ˆ</sup> / _𝑘_<sup>ˆ</sup> , and _export rate_ relative to transcription rate _𝛾_ = _𝛾_ ˆ/ _𝑘_<sup>ˆ</sup> , where hats indicate the underlying rates.

95

By far the most frequent technical sampling parameter optimum was log10( _𝐶𝑁_ = −6 _._ 9 _, 𝐶𝑀_ = −5 _._ 25) (see 7.2C). Multiplying these by gene lengths to recover per-gene technical capture rates, we found that on average the rate of capture for unspliced molecules was 0.003 (or, about .3% of unspliced molecules are captured) and 0.012 for spliced molecules (or, about 1.2% of spliced molecules are captured). This also corresponds with the experimental technology. Since Parse capture includes both poly(T) and random hexamer priming, the spliced molecules with poly(A) tails have higher rates of capture than the unspliced molecules.

**GLM testing for** **_cis_ vs.** **_trans_ regulation of biophysical parameters.** The inferred parameters are best represented on a log10 scale, and per gene distribution over samples of the log10 scaled parameters appeared approximately Gaussian. We thus adapted the framework discussed in Chapter VI [48] to fit a general linear model with an identity link.

The parameters inferred by fitting on counts estimated in the F1 hybrids are estimates of transcription from a single allele, while parental counts are estimates having transcription from two alleles. If we assume that the rate governing the Poisson process of transcriptional initiation is _𝑘_<sup>ˆ</sup> from each allele in the parents and initiation occurs independently, the overall rate of transcriptional initiation is 2<sup>ˆ</sup> _𝑘_ , and our steady-state inference of splicing and export rates for parents would be half of what we would infer given counts from only one allele. This makes our null hypothesis of no regulatory differences between the relative splicing and export rates representable by the following design matrix for, as one example, the model of dominant _trans_ regulation:


where one could replace log10 _𝛽_ with log10 _𝛾_ . We have changed the notation for regression weights from the previous chapter to _𝑊, 𝑊𝐶, 𝑊𝑇_ to avoid clashing with our notation for the relative splicing rate. However, to account for sample specific differences, we first perform orthogonal distance regression over all genes comparing each sample to one reference sample (as in [37]): this regression accounts for the factor of 2 before we fit _cis_ vs. _trans_ GLMs, and we thus ran the same free, dominant, and log-additive GLMs described in Chapter VI [48] per parameter, cell type, and

96

strain. We report results for the free model, as of the three it produced the highest data likelihoods.

### **7.2 Large-scale Trends and Summarization**


Figure 7.3: A. The number of overall regulatory classifications for burst size ("b"), relative splicing rate ("beta"), and relative export rate ("gamma"). B. The number of instances in which pairwise combinations of parameters (burst size and relative splicing rate, burst size and relative export rate, and relative splicing and relative export rate, from left to right) were found to be both non-conserved/significant, only one or the other significant, or both conserved. C) For the case in which both pairwise combinations were non-conserved, the number of instances in which they were classified as the same regulatory strategy, or different regulatory strategies. D) Of the times the pairwise comparisons of parameters were both non-conserved, the correlation between their inferred proportion _cis_ .

In the following section, we refer to each unique parameter-gene-cell type regulatory assignment as a "test." Across all seven strain crosses, eight tissues, 92 cell types and 30,763 genes tested, we found the most instances of regulated relative splicing

97

(26,368) and a similar number of regulated burst sizes (21,755) and relative export rate (21,744) Fig. 7.1A. Consistent with regulation of total counts, the most frequent category of regulatory strategy for non-conserved tests was _cis_ , making up 52.2% of all regulatory assignments for burst size, 52.8% for relative splicing rate, and a greater percent, 62%, for relative export rate. For all parameters, _trans_ regulation was the next most common, followed by _cisxtrans_ and a much smaller number of _cis+trans_ for burst size and relative export rate. The hierarchy of regulatory assignments for burst size and relative export rate are the same as what we observed for total counts [215]. Notably, for relative splicing rate, there were over three times more instances of _cis+trans_ regulation (which was very rare when testing total counts [215]). While burst size and degradation rate may be constrained by compensatory _cis_ and _trans_ activity to buffer overall levels of RNA, the rate of _splicing_ is one example of how transcripts can be modified without changing overall quantity. Examining this for individual isoforms or introns could be even more revealing.

Comparing overall patterns of pairwise parameter regulatory assignments for the same gene in a strain-cell type-tissue test, there was little overlap (Fig. 7.1B). For burst size and relative splicing rate, in 14,708 instances burst size was significantly regulated while relative splicing rate was not, in 19,321 instances relative splicing rate was regulated while burst size was not, and only in 7,047 were both significantly assigned. Among those 7,047 instances, in 49.1% they were assigned different regulatory classifications, in 28.0% both were classified as _cis_ , 14.1% _trans_ , 6.8% _cisxtrans_ and 2.0% _cis+trans_ . For burst size and export rate, there were similarly more instances of only one or the other having significant regulatory differences between parental strains, although of those a greater percent (66.3%) were the same rather than different. Comparing relative splicing and export rates, there was less of an overlap in assignments than when both were non-conserved (about 58.5%) than burst size and relative export rate (66.3%), but more than burst size and relative splicing rate (50.8%). This suggests that the regulation driving differences in strains’ regulatory processes of a gene in a particular context is not singly categorizable, and in fact calls into question the very terminology of " _cis_ vs. _trans_ regulation of a gene". To say that a gene’s _expression_ in a cell type is different between strains due _cis_ or _trans_ regulation is to elide particular regulation of points in the gene expression process.

We observed that the number of significant tests generally increased with the genetic

98


Figure 7.4: The number of overall significant tests for burst size ("b"), relative splicing rate (" _𝛽_ "), and relative export rate (" _𝛾_ ") for A. different strain hybrids (ordered by increasing genetic diversity), B. different tissues (ordered by the sum of significant tests over all parameters), and C. cell types within the Cortex/Hippocampus, where each dot is a different strain comparison.

diversity of the strain (summing over parameters and tissues), ranging from 2,682 significant tests for B6-AJ crosses (the most genetically similar with 5.9 million SNPs from B6), to 20,962 for B6-PWKJ (22.6 million SNPs from B6) and 17,152 for B6-CASTJ (22.9 million SNPs from B6) (Fig. 7.4A). Among tissues (summing over parameters and strains), we also classified the fewest significant instances of regulatory differences in heart (572) and the greatest in the Cortex/Hippocampus (23,912) (Fig. 7.4B). Within one tissue, we can further break down regulation at the cell type level: in the Cortex/Hippocampus, we found that glutamatergic neurons in

99

particular to have more non-conserved regulatory differences (Fig. 7.4C).


Figure 7.5: The number of overall significant tests (summed over parameters) versus the number of nuclei for A. strains, B. tissues, and C. unique cell types.

We caution in interpreting the biological meaning of the number of significant tests, as "the absence of evidence is not the evidence of absence," and, for the 92 cell types tested in all strains, there was a positive correlation between the number of nuclei in that cell type and the number of significant calls (Fig. 7.5C). Interestingly, the dependence of the number of significant tests on the number of nuclei was not as strong for strain and tissue (Fig. 7.5A and B).

### **7.3 Exploring the Processes Driving Allele Specificity**

### **Regulation of processes for genes with PWKJ allele specific expression in F1 hepatocytes.**

PWKJ mice are prone to liver disorders and are often used as a model to study nonalcoholic steatohepatitis (NASH), a non-alcoholic fatty liver disease [224]. As an example of a full pipeline of discovery for gene processes that may behave differently in different strains in specific contexts, we used the normalized (depth and log1p) total counts (summing over spliced and unspliced) per allele in all 7 haplotypes of the F1 crosses to determine those with allelic expression specific to PWKJ alleles in hepatocytes (an analysis a researcher might perform to investigate this question without biophysical models) using an entropy-based metric [223]. These genes indeed showed highest mean expression for the PWKJ allele in F1 hybrids (five are displayed in Fig. 7.6A).

For five of these genes, we explored the regulatory differences between B6 and PWK that could explain the allele specificity (Fig. 7.6B). For example, _Mup2_ , which codes for a member of the major urinary proteins whose knockout leads to increased hepatic lipid accumulation [225], had significant regulatory differences between parental strains of all three parameters: burst sizes, regulated in _cisxtrans_ , was higher for PWK parents than for B6 parents, as well as for the PWK allele

100


Figure 7.6: Exploring the biophysical basis of allele specific expression of genes in the F1 data in hepatocytes from liver samples. A. Genes whose expression was found to be highly specific to the PWK allele in B6-PWK F1 samples in hepatocytes using normalized total counts show higher mean expression (the average over total counts summed over spliced and unspliced, depth and log1p normalized) [223]. B. The allele specificty can be traced to regulatory differences in the parent strains (B6 and PWK). Boxplots show the mean and quartiles over log10 of burst size ("b"), relative splicing rate ("beta") and relative export rate ("gamma"). Bars above each subplot indicate by color the regulatory classification.

than for the B6 allele in B6-PWK F1 hybrids. Relative splicing rate and relative export rate were smaller for PWK alleles: as they are relative to transcription rate, it may be that the transcription rate (denominator) increased. An increased burst size and/or transcription rate might explain why the _Mup2_ transcript shows allele specific expression (Fig. 7.6B). By contrast, _Entk2_ , the human orthologue transcript of which was upregulated in gastric cancer patients who showed hepatic metastasis [226], only exhibits significant regulatory differences between B6 and PWK in burst size, and interestingly, the compensatory behavior ( _cisxtrans_ ) changed from smaller in PWK compared to B6 to larger for the PWK allele than for the B6 allele in F1 (Fig, 7.6B). This suggests that there was some _trans_ difference buffering the _cis_ difference between the parents; in the shared F1 environment, the un-buffered _cis_ difference led to increased expression of the PWK F1 allele.

101


Figure 7.7: _Ptprd_ regulation in the Cortex/Hippocampus across the eight founder mouse strains reveals distinct differences in regulation in GABAergic and glutamatergic neurons in the NODJ. A. Classifications of regulatory differences between parental strains (B6 vs. the indicated strain) for burst size, relative splicing rate, and relative export rate show extensive splicing regulation, with NODJ showing distinct patterns. B. Distributions of normalized (depth and log1p normalization) spliced and unspliced counts in GABAergic and glutamatergic show are similar for all six non-B6 founder strains except for NODJ. These differences can be further explored by comparing inferred relative splicing rates for alleles in the parents and hybrid F1s of each strain.

### **_Ptprd_ regulatory differences in neurons across strains.**

Focusing our analysis on the cortex/hippocampus, we found the transcript _Ptprd_ had the most significant calls (summing over strains and cell types). _Ptprd_ is a receptor type protein tyrosine phosphatase which contains an extracellular domain, a single transmembrane segment, and intracellular catalytic domains, with roles in brain development and synapse formation [227]. In humans, variants at the _PTPRD_ locus have been associated restless leg syndrome, Alzheimer’s disease, obsessivecompulsive disorder, intellectual disabilities, and attention-deficit/hyperactivity disorder (ADHD) [227, 228]. _Ptprd_ in mice and _PTPRD_ in humans are known to be regulated by extensive, cell type specific alternative splicing [229, 230], and multiple studies have shown that knock-down and knock-out of _Ptprd_ in B6 background mice led to an increase in excitatory neurons in the cortex and decrease of sociability [231, 229].

Consistent with extensive regulation by splicing, we found that in all 10 neuron cell types in the brain, across strains, there was significant regulatory differences in relative splicing rate for _Ptprd_ in 55 out of the 70 tested cell type-strains (Fig. 7.7A).

102

Particularly interesting was the regulation in excitatory glutamatergic neurons. Although glutamatergic neurons overall had the greatest number of significant tests (Fig. 7.4C), all six founder strains besides NODJ showed no significant regulatory differences compared to B6 for _any_ parameter (Fig. 7.7A). NODJ, however, displayed significant regulatory differences for _all_ parameters (Fig. 7.7A). Although _Ptprd_ expression has not been studied in NODJ mice, the NODJ strain was shown to display low sociability in behavioral tests, as opposed to B6 mice which showed significantly higher levels of preference for sociability [232] (the other six founder strains were not included in the study). This finding could indicate NODJ and the _Ptprd_ gene in glutamatergic neurons as good candidates to consider as mouse model, target gene and context for studies on behavioral (ADHD, OCD, autism-spectrum) disorders in humans.

### **Discussion and Limitations**

We have shown that genome-wide inference of the regulation of RNA processes between genetically diverse mouse strains can be achieved using high-throughput transcriptomic data. We recapitulated known results (splicing of _Ptprd_ ) as well as suggested particular processes of genes as being regulated between B6 and PWK founder strains in hepatocytes in the liver. While we focused on two examples, we expect a deeper analyses of the thousands of fit genes, cell types, strains, and tissues (Fig. 7.1 and Fig. 7.4) would yield harvests of rich insight; and we are excited to provide these inferences as a resource for the mouse biologist.

This analysis is, of course, subject to a number of limitations. Firstly, considering the low capture rates per gene (Fig. 7.2C), certainly not every RNA molecule has been accounted for; but, as the same technical capture rate was inferred for parental and hybrid alleles in the F1s, we are at least reasonably confident in the assumption that the capture technology is not biased towards one or the other allele. Secondly, alignment of reads to obtain allele specific counts using short-read snRNA-seq requires that 1) there be enough SNPs between strains to distinguish between alleles, and 2) the sections of the transcript that were captured align to the region of genes that contain those SNPs. More accurate would be fluorescent studies that can label and watch real-time RNA production from two different alleles [233]. However, labeling and obtaining live-cell fluorescent images is far more intensive than performing a snRNA-seq experiment: our analysis depends on collecting enough samples from two parental strains and their hybrids to have the

103

statistical power to make a claim about regulation, which would be prohibitive if conducting fluorescence experiments.

Another limitation is the primitive nature of our "splicing" model. With longer reads, we could more accurately assess isoform expression, and include isoform specific or intron specific rates of splicing in the model. However, this is more an experimental than a theoretical limitation (updating the CME model for improved capture technology is straightforward). Another model limitation is that we are examining genes independently and not considering gene interactions. While interactions in and of themselves should not affect the logic we are testing, they could provide insights into which genes are likely to be _cis_ vs. _trans_ , as well as the possible _trans_ acting factors, that could refine our current inferences.

Finally, we currently test the regulatory strategy of each biophysical parameter separately, but in future will change the design matrix to fit shared and independent effects for different parameters (this would be more appropriate, as we already know that the relative splicing and export rates share a denominator).

Despite the limitations, this study demonstrates an advancement in the challenge of understanding how genetic diversity results in regulated gene expression. The regulation of a gene occurs via regulation of specific processes, and it is both more precise conceptually and more biologically informative to test for regulatory differences in these processes rather than in the mean counts. While we have probed regulatory processes from the angle of genes, finding evidence of regulation but not the casual genetic variants themselves, increased sample sizes could be used to associate variants with the changed process in particular cell types [29, 41]. We expect that higher resolution data could more precisely pinpoint _how_ variation in the genome changes molecular processes in the cell.

104

_C h a p t e r 8_

---

[← DISENTANGLING CIS AND TRANS GENE REGULATION](11-disentangling-cis-and-trans-gene-regulation.md) · [Up: contents](index.md) · [CONCLUSION AND PERSPECTIVES →](13-conclusion-and-perspectives.md)
