---
title: SEQUENCING MODEL SPECIFICATION
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# SEQUENCING MODEL SPECIFICATION

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In spite of our assumptions throughout Chapter 7, real datasets do have various technical noise sources, which need to be accounted for. Unfortunately, even the relatively simple treatment of this topic in Section 4.4 is not tractable on a genomewide level: a fully satisfactory explanation of the multifaceted variability in singlecell datasets remains out of reach. Nevertheless, we can fruitfully attempt to treat the phenomena one at a time, assuming all others have been satisfactorily accounted for, and use biophysical hypotheses to characterize the technical noise behaviors. This incremental approach allows us to develop a more grounded alternative to typical _ad hoc_ approaches to “denoising” sequencing data.

### **8.1 Empty droplets**

This section adapts a portion of [115] by G.G., J.J.V., and L.P. G.G. conceptualized, designed, and implemented the analysis.

One of the first steps in scRNA-seq data analysis is cell quality control, which excludes cell barcodes that appear to originate from empty droplets from further analysis [187]. For computational tractability, this procedure typically uses “hard” assignment, such that barcodes associated with a total molecule count above some threshold are treated as cells, whereas barcodes below the threshold are treated as empty droplets. Threshold selection is necessary because even “empty” droplets contain ambient RNA. This ambient RNA appears to originate from cells lysed in the preparation process, and contaminates empty and cell-containing droplets alike [187]. The observation of ambient counts has led to the development of statistical methods for removing this source of noise, either by estimating and subtracting it [323] or incorporating it into a stochastic model [87, 256, 322]. Conceptually, Equation 4.38 reflects the latter approach: each droplet contains one or more cells, each with biological generating function _𝐺_ , and background, with a generating function _𝐺_ bg that depends on _𝐺_ . To accurately model the background counts, we need to propose and justify a specific functional form for _𝐺_ bg. Thus, under the assumption that empty and cell-containing droplets are similarly susceptible to contamination, the former provide a reasonable estimate of ambient distributions in the latter [323].

96


Figure 8.1: The pseudo-bulk model of background noise is quantitatively consistent with counts from a human blood cell dataset.

**a.** The simplest explanatory model for background noise invokes the lysis of cells (green), which creates a pool of RNA that reflects the overall transcriptome composition but retains none of the cell-level information. If the loose RNA molecules diffuse into droplets (blue) according to a memoryless and independent arrival process, the resulting background distribution (purple: higher probability mass; white: lower probability mass) observed in empty droplets should be a series of mutually independent Poisson distributions, with the mean controlled by the composition in non-empty droplets.

**b.** The mature transcriptome in empty droplets has a mean-variance relationship near identity (gray points, _𝑛_ = 12 _,_ 298), consistent with Poisson statistics (blue line); the non-empty droplets demonstrate considerable overdispersion (red points, _𝑛_ = 17 _,_ 393).

**c.** The mature and nascent transcripts in empty droplets have sample correlation coefficients _𝜌_ near zero, consistent with distributional independence (gray histogram, _𝑛_ = 9 _,_ 362); the non-empty droplets demonstrate nontrivial statistical relationships (red histogram, _𝑛_ = 14 _,_ 365).

**d.** The mature transcripts of different genes in empty droplets have sample correlation coefficients _𝜌_ near zero, consistent with distributional independence (gray histogram, _𝑛_ = 75 _,_ 614 _,_ 253); the non-empty droplets demonstrate nontrivial statistical relationships (red histogram, _𝑛_ = 151 _,_ 249 _,_ 528).

**e.** When both are nonzero, the mature count mean in empty droplets is highly correlated with the mean in the non-empty droplets, consistent with the pseudo-bulk interpretation (black points, _𝑛_ = 12 _,_ 107; dashed line: identity).

97

The simplest model holds _𝐺_ bg to be equivalent to a “pseudobulk” experiment, with molecules randomly sampled from the lysed cell population. If each cell is equally likely to contribute to the pool of free RNA, and diffusion occurs by a simple independent arrival process, we find that the distribution of background should be Poisson, with the mean for each species proportional to its mean in original cell population, as in, e.g., [87]. This functional form immediately induces a set of testable predictions: not only are the distributions Poisson, but they are _independent_ Poisson, with no meaningful statistical structure remaining between transcripts of a single gene, as well as between different genes, as illustrated in Fig. 8.1a.

To characterize the accuracy of these predictions, we inspected datasets pseudoaligned with _kallisto | bustools_ [197], and compared the data for barcodes passing _bustools_ quality control to data for barcodes which were filtered out. As a shorthand, we call the former “non-empty” and the latter “empty” droplets, keeping in mind that this identification is approximate. We illustrate the results for a human blood dataset generated by 10x Genomics. As shown in Figure 8.1b, data from non-empty droplets are substantially overdispersed relative to Poisson, whereas data from empty droplets are largely consistent with the Poisson identity mean–variance relationship. However, a small number of relatively high-expression genes demonstrate overdispersion. In addition, intra-gene (Figure 8.1c) and inter-gene (Figure 8.1d) correlations are typically nontrivial in non-empty droplets, but consistently near zero for empty droplets, supporting distributional independence of the background counts. Finally, the mean expression in empty droplets is highly correlated with mean expression in non-empty droplets, albeit lowered by approximately four orders of magnitude (Figure 8.1e), supporting the assumption that the original cells are lysed in a uniform fashion.

To characterize the deviations from the pseudo-bulk model, we identified the genes that demonstrated overdispersion in empty droplets. A considerable fraction of these genes were associated with mitochondria or blood cells. For example, of the 21 annotated genes overdispersed in the empty droplets of a 10x Genomics mouse neuron dataset, nine were mitochondrial ( _mt-Nd1_ , _mt-Nd2_ , _mt-Co1_ , _mt-Co2_ , _mtAtp6_ , _mt-Co3_ , _mt-Nd3_ , _mt-Nd4_ , and _mt-Cytb_ ), three coded for hemoglobin subunits ( _Hba-a1_ , _Hba-a2_ , and _Hbb-bs_ ), and two coded for blood cell-specific proteins ( _Bsg_ , _Vwf_ ) [189, 209]. On the other hand, of the 10 annotated genes overdispersed in the empty droplets of dataset generated from cultured mouse embryonic stem cells [72], six ( _mt-Nd1_ , _mt-Co2_ , _mt-Atp6_ , _mt-Co3_ , _mt-Nd4_ , _mt-Cytb_ ) were mitochondrial

98

and none were blood cell-specific [209].

Since overdispersion implies that contamination involves non-independent arrivals of these molecules, the results suggest that the cell-free debris contain, among other structures, entire mitochondria or erythrocytes, when they are present in the source tissue. These membrane-bound structures may diffuse into droplets, then lyse and release all of their contents at once. In other words, empty droplets do not merely have disproportionally high mitochondrial content, as has been noted previously [87, 133, 139]; they have _nontrivially distributed_ mitochondrial content, which can suggest the mechanism of its incorporation and improve interpretation where simple thresholds may be misleading [139]. We speculate that cases where the model fails can be leveraged to discover more complicated forms of contamination, such as molecular aggregates [322].

In addition, we examined the total UMI counts in empty droplets, which should be Poisson (Fano = 1) if each individual gene’s distribution is Poisson. For the human blood dataset demonstrated in Figure 8.1, the empty droplets had fairly significant overdispersion (Fano ≈ 43), which decreased, but did not disappear (Fano ≈ 7 _._ 6), once the 53 significantly overdispersed genes were excluded. This result suggests that, although the pseudo-bulk model is approximately valid, some residual variance, possibly due to variability in per-droplet capture rates, is present and needs to be modeled to fully describe the stochasticity in single-cell datasets.

### **8.2 Length biases**

This section summarizes the content of [107] by G.G. and L.P. The initial interest in length bias was due to L.P. and V.S.; the model was conceptualized by L.P. and G.G.; the model was designed and implemented by G.G.

In a wide variety of 10x single-cell RNA sequencing datasets, average spliced mRNA counts do not seem to show a length dependence (Fig. 8.2a, gray lines), which is consistent with previous studies of UMI-based protocols [222]. On the other hand, unspliced mRNA counts strongly correlate with gene length [119] (Fig. 8.2a, red lines). This observation prompted us to investigate whether the discrepancy has biological origins, and raised questions about the consequences of ignoring this bias.

This bias may be explained by several models (Figure 8.2b). The first has identical, gene-specific observation probabilities _𝑝_ for nascent and mature species. In this model, the inferred burst size is _𝑏𝑝_ , as these two parameters are not mutually

99


Figure 8.2: Trends in inferred transcriptional parameters allow us to distinguish between models of technical noise, and explain a pervasive length bias in molecule counts by length-dependent sequencing rates.

**a.** A variety of single-cell datasets produce consistent and counterintuitive length-dependent trends in nascent RNA observations (lines: average per-species gene expression, binned by gene length; red: nascent RNA observations; gray: mature RNA statistics; data for 2,500 genes shown for each dataset).

**b.** Two explanatory models for the trend in **a** : the species-independent bias model for length dependence in averages, which proposes nascent and mature RNA are sampled with equal probabilities, and the species-dependent bias model, which proposes nascent RNA sampling rate scales with length (top, gold: kinetics of species-independent model; bottom, blue: kinetics of species-dependent model; center, green: the source RNA molecules used to template cDNA).

**c.** Fits to the species-independent model show a strong positive gene length dependence for inferred burst sizes, whereas fits to the species-dependent model show a modest negative gene length dependence, which is more coherent with orthogonal data (lines: average per-gene burst size inferred by _Monod_ , binned by gene length; gold: results for species-independent model; blue: results for species-dependent model; only genes that passed goodness-of-fit testing shown)

**d.** The likelihood over sampling parameters can be optimized to infer the parameters, which are consistent among datasets (dark teal: lower, light teal: higher total Kullback-Leibler divergence between fit and blood cell data; highlighted yellow region: 5% quantile region for the displayed landscape; orange cross: optimal sampling parameter fit for the displayed landscape; orange points: optimal sampling parameter fits for other analyzed v3 datasets).

**e.** Biological replicates show largely concordant inferred parameter values (orange dashed line: identity; gold: lower bounds on 99% confidence intervals; gray: fits rejected by statistical testing; splicing and degradation rates are reported in units of burst frequency).

100

identifiable. The second has with a gene length _𝐿_ -dependent technical noise term for the nascent species, coarsely representing a higher rate of priming for long molecules with abundant intronic poly(A) tracts [119, 168, 207], and a shared genome-wide term for the mature species, representing priming at the poly(A) tail (Section 4.4.3). In this model, the inferred burst size is _𝑏_ . Both models produce fair fits to the data.

However, the trends in the parameters inferred by _Monod_ (Section 5.4) under the two models are strikingly different: the species-independent bias model predicts that longer genes have higher _𝑏𝑝_ (Figure 8.2c, gold lines). Ascribing this trend to the _𝑏_ term — longer genes have higher burst sizes — contradicts burst size trends from fluorescence microscopy [172]. Ascribing it to the _𝑝_ term — longer genes have higher sampling probabilities — is physically unrealistic, because mature RNA molecules are depleted of the internal poly(A) tracts necessary for priming [217].

On the other hand, the species-dependent model predicts a modest negative relationship between length and burst size, which is more coherent with orthogonal data (Figure 8.2c, blue lines). We observe similar trends for the turnover parameters _𝛽_ and _𝛾_ : striking length dependence under the species-independent model, which vanishes when using length as a scaling factor for the sampling rate<sup>6</sup> . We find that the sampling parameter optima are similar for a wide variety of datasets obtained from comparable experiments (Figure 8.2d). In addition, biological replicates [321] produce similar parameter values (Figure 8.2e).

This technical noise model is a relatively simplistic low-order approximation — all genes have the same mature molecule capture rate _𝜆𝑀_ and length scaling _𝐶𝑁_ . Nevertheless, it foregrounds a key modeling principle: in the absence of prior information, biological parameters need to be fit on a gene-by-gene basis, but technical noise should be constructed using a common genome-wide model that varies in a mechanistic, rather than arbitrary way. In sum, the mathematics enable us to define and fit systems, but to understand whether the fits are sensible, we need to contextualize and compare them with previous results and physical intuition.

### **8.3 Technology differences**

This section summarizes part of the content of [106] and [107] G.G. and L.P. The analysis was conceptualized and designed by G.G. and L.P, and implemented by G.G.

The explicit parametrization of biophysical models allows us to explain and account

101


Figure 8.3: The technical noise model fits can be interpreted to analyze experimental effects.

**a.** 10x v2 and v3 scRNA-seq replicates generated from a single sample demonstrate discordant RNA count distributions: the v2 datasets have lower mean values (orange dashed line: identity; black: genes).

**b.** The v2 datasets have higher CV<sup>2</sup> values (conventions as in **a** ).

**c.** The v2 datasets’ distributional differences can be tentatively explained by a combination of identical biological parameters and lower technical noise parameters ( _𝐶𝑁_ : coefficient for length-dependent unspliced capture rate; _𝜆𝑀_ : spliced capture rate; colors: dataset categories; intersections of grid lines indicate the sampling parameter sets evaluated in the inference process).

**d.** Counterintuitively, representative paired mouse brain single-cell and singlenucleus datasets exhibit similar mature RNA levels (gray points: genes; dashed black line: line of identity; green line: the approximate average offset observed for single-nucleus data).

**e.** The single-nucleus dataset consistently has considerably higher nascent RNA counts, which suggests the presence of a technical effect between the two technologies (conventions as in **d** ).

**f.** The single-nucleus dataset demonstrates slightly lower noise levels for mature count data (gray points: genes; dashed black line: line of identity).

**g.** The single-nucleus dataset demonstrates considerably lower noise levels for nascent count data (conventions as in **f** ).

**h.** - **i.** By fitting mechanistic models to both datasets, we can identify technical noise parameters that produce consistent burst and splicing parameters between the technologies (points: maximum likelihood estimates for burst sizes and splicing rates; error bars: conditional 99% confidence intervals for inferred parameters; dashed black line: line of identity).

**j.** At the discovered technical noise parameters, the mature RNA efflux or turnover is considerably higher for the single-nucleus dataset, consistent with this parameter’s interpretation as the rapid export from the nucleus (conventions as in **h** - **i** ).

102

for differences between technologies. By themselves, technical noise parameters demonstrate limited identifiability. However, we can investigate the technical effects more systematically by treating replicates generated by different sequencing technologies and adopting stronger priors. We found that count data generated by the higher-efficiency v3 chemistry consistently yielded higher mean levels and lower noise (CV<sup>2</sup> ) levels than those generated by the older v2 chemistry (Fig. 8.3a-b). Intuitively, these differences should be appropriately attributed to technical effects, as the source tissues were similar or identical.

Imposing the belief that the underlying biological parameters should be the identical between all technical replicates, and treating the results for large v3 samples as a putative ground truth, we identified the set of sampling parameters for the v2 datasets that produced the best agreement to these biological parameter values. The resulting inferred sampling parameter optima are shown in Figure 8.3c: as expected, v2 datasets have lower sampling parameter values. These values are somewhat challenging to identify without enforcing the consistency criterion between transcriptional parameters: the v2 KLD landscapes are more susceptible to noise than the v3 KLD landscapes, preventing _de novo_ inference. Although the current comparison is mostly relative, the framework provides a quantitative explanatory mechanism for the technical effect of sequencing chemistry.

Similarly, we can apply this approach to the analysis of single-nucleus data. The interest in single-nucleus sequencing, as well as the recognition of systematic differences in the findings from the two technologies [11, 19, 71, 286], has motivated the analysis of these differences [46] and the development of more or less _ad hoc_ data integration methods [11, 169]. At least some discrepancies appears to stem from a fundamental methodological difference: single-cell analyses typically only use exonic reads, whereas single-nucleus combine intronic and exonic reads [71, 75].

We propose that scRNA-seq and snRNA-seq data may be more analyzed in a more principled way through a mechanistic lens. For single-nucleus data, we use the results in Section 7.3 to justify the bursty model (Section 4.6.2). For single-cell data, we adopt the same model, making the usual assumption that export is sufficiently rapid enough relative to degradation. Under this pair of models, the nascent RNA dynamics — i.e., transcription and splicing — should be identical for the two technologies, as the nascent RNA are confined to the nucleus.

This axiom provides a foundation for the joint analysis of the technologies. For example, Figure 8.3d-e compares the average counts for 2,000 genes in scRNA-

103

seq and snRNA-seq datasets generated from a single mouse brain tissue sample by 10x Genomics. Surprisingly, in spite of the depletion of cytoplasmic RNA, the mature count averages were visually similar, whereas the nuclear count averages were approximately half an order of magnitude higher in the single-nucleus dataset. Quantitatively, 83% of the mature and over 99% of the nascent averages were higher in the snRNA-seq sample. To explain this difference, we adopt the usual “marker gene” paradigm, i.e., that closely related cell types typically differ in the expression of a small number of genes [187], whereas the other genes have similar distributions. Under this assumption, we are immediately led to conclude that the difference is purely technical, and cannot be attributed to enrichment of certain cell types in one or the other technology. In other words, due to the details of the nuclear sequencing protocol, the procedure retains considerably more RNA of both types. This assumption appears to be supported by Figure 8.3f-g: both species exhibited an overall decrease in the noise levels (66% of the mature and 98% of the nascent CV<sup>2</sup> values), which is consistent with decreased molecule loss. The difference in mature RNA amounts should, then, be explained by the combination of two competing effects: the depletion of cytoplasmic RNA, as well as more effective capture of remaining molecules, in the single-nucleus protocol.

To quantify the efflux rates, we fit the datasets using _Monod_ and inferred the technical noise parameters for the single-cell dataset. Next, we identified the set of singlenucleus technical noise parameters that provided the best match to the burst size and splicing rate parameters (Figure 8.3h-i); the discovered set of technical noise parameters had higher (more effective) sampling rates. The inferred efflux rates at this set were considerably higher for the single-nucleus dataset, both visually (Figure 8.3j) and statistically: the _𝑡_ -test { _𝑡, 𝑝_ } values were {−2 _._ 7 _,_ 7 _._ 3 × 10<sup>−3</sup> } for the burst size, {1 _._ 6 _,_ 0 _._ 11} for the splicing rate, and {−11 _,_ 2 _._ 1 × 10<sup>−27</sup> } for the efflux rate.

The procedure we have outlined has significant limitations: for example, we have neglected nuclear efflux in the single-cell data and cell type heterogeneity, both of which are physiologically important [17, 321] likely contributors to deviations in Figure 8.3h-i. In addition, single-nucleus sequencing may harbor as of yet poorlyunderstood technical noise phenomena particular to the technology. Nevertheless, the model formulation provides a foundation for the incorporation of more sophisticated nuclear retention phenomena [85] jointly with technical noise. In addition, the strategy provides a principled solution to the dilemma of incorporating intronic reads: all the available data should be used, with species differences encoded in a

104

multivariate mechanistic model. If its assumptions are explicitly formulated, the model can be fit, or extended to account for violations, based on experimental data.

### **8.4 Limitations of normalization procedures**

This section summarizes part of the content of [106] by G.G. and L.P. The control was conceptualized and designed by L.P.; the derivation was performed by G.G. The method was implemented by G.G.

The modeling framework provides an appealing and self-consistent alternative to typical methods for the treatment of technical variability. Due to the scale of scRNA-seq data, standard analyses heavily use data transformation and dimensionality reduction to produce a version of the data more amenable to statistics [187]. For example, a typical analysis of cell type heterogeneity may apply size normalization (e.g, proportional fitting or PF, which treats RNA counts as compositional quantities [34]), log-transformation, principal component analysis (PCA), and Uniform Manifold Approximation and Projection (UMAP) [187, 195]. Each of these steps has a specific purpose; for the four steps above, the purposes are, in turn, to remove variability due to technical heterogeneity, to obtain easily tractable normal-like logabundance distributions, to select the latent data dimensions that contain the most variability, and to visualize the cell type structure [187]. These transformations rely on implicit assumptions about the structure of the data; these assumptions may be mutually contradictory, and their violation may produce results that range from suboptimal to catastrophically incorrect.

These limitations and failure modes have previously been investigated. Size normalization privileges relative, rather than absolute RNA species abundance; occasionally, this approach produces inconsistent results across the genome [123] and retains apparently technical variation [34, 56]. Log-transformation is optimal for homogeneous, high-expression, approximately negative binomial data [4, 34, 187], and relies on an arbitrary genome-wide “pseudocount” hyperparameter that can distort the distributions [4, 34, 123, 290]. PCA is optimal for multivariate normal data, and can be misled by the large zero fractions observed in single-cell data [290]. Finally, UMAP appears to be optimal for data with uniform, low-noise coverage of a latent manifold, with risk of distortions due to violated assumptions and stochastic initialization [49, 58] (Section 6.1.3). A comprehensive treatment of the distortions induced or ameliorated by each step appears, however, to be out of reach, as the transformations’ results are heavily data-dependent and elude theoretical analysis.

105


Figure 8.4: Normalization and dimensionality reduction distort and underestimate biological variation, especially in high-expression genes.

**a.** A proposed baseline for the analysis of residual variation after data transformation: the fraction of biological variability can be bounded by a theoretical baseline, which is computed from the variation in average subpopulation expression. If this baseline is violated, the data transformation has discarded some biophysically meaningful variation.

**b.** High-expression genes have high variance (gray points: genes below the 95th percentile by mature RNA expression; red points: genes above the 95th percentile by mean mature RNA expression, red line: percentile threshold).

**c.** Proportional fitting size normalization (PF), log-transformation (log), and principal component analysis (PCA) globally deflate the squared coefficient of variation (CV<sup>2</sup> ), whereas Uniform Manifold Approximation and Projection (UMAP) globally inflates it (gray and red points: as in **b** ). **d.** - **g.** All four of the steps substantially deflate high-expression genes’ CV<sup>2</sup> relative to raw data, implicitly attributing their variability to nuisance technical effects (gray and red points: as in **b** ). **h.** - **k.** The deflation of variability results in the violation of the theoretical lower bound computed from cell subpopulation differences, particularly for high-expression genes (gray and red points: as in **b** ; curved teal line: identity baseline, below which biological variability is removed; horizontal teal line: threshold, above which variability is inflated relative to raw data).

106


Figure 8.5: The _Monod_ mechanistic analysis of biological and technical variability produces coherent results.

**a.** The baseline introduced in Figure 8.4a may be compared to point estimates of the biological variability fractions, which follow immediately from a fit to a parametric model of transcription and sequencing.

**b.** The _Monod_ fits explicitly attribute the variability in high-expression genes to biological phenomena (gray and red points: as in Figure 8.4b).

**c.** The _Monod_ results lie entirely within the admissible region (gray and red points: as in **b** ; curved teal line: identity baseline, below which inferred biological variability is lower than inter-cell population variability; horizontal teal line: threshold, above which inferred biological variability exceeds that of raw data).

107

In Figure 8.4a, we propose a procedure for the quantitative benchmarking of data transformations relative to an internal baseline. Each step transforms the data distribution, purportedly retaining relevant biological variability — such as cell type differences — and removing incidental or technical variability, quantified by the squared coefficient of variation (CV<sup>2</sup> ). Therefore, by removing some fraction of variability, a data transformation implies this component is immaterial to analysis, whereas the residual fraction of variation — the CV<sup>2</sup> ratio for the distribution after and prior to transformation, denoted by _𝜂_ ˜<sup>2</sup> / _𝜂_<sup>2</sup> — is attributed to biology. For dimensionality reduction techniques, this procedure involves some subtleties, and requires the existence of an inverse transformation that can map the lowerdimensional representation back to the high-dimensional space.

This residual fraction should not vary arbitrarily; under mild assumptions, we can bound the biological fraction of CV<sup>2</sup> from below by the variability in cell subpopulation averages. Specifically, we can write down the following identities for biological lower moments:


where _𝝅_ consists of the cell subpopulation proportions. If we assume sequencing samples evenly from the subpopulation, and rescales the mean and variance by scalars _𝜉𝜅_ and Ξ _𝜅_ , we obtain the observed moments


We further assume that _𝜉𝜅_ = _𝜉_ for all _𝜅_ . In other words, we suppose that, for a particular gene and on average, all cell types are chemically and statistically identical with respect to the sequencing process. We find that the lower moments of the observed distributions can be rewritten in terms of the lower moments of the

108

biological distributions:


Using the definition of the squared coefficient of variation (CV<sup>2</sup> = _𝜎_<sup>2</sup> / _𝜇_<sup>2</sup> := _𝜂_<sup>2</sup> ), we find that the fraction of CV<sup>2</sup> due to biology can be bounded from below:


i.e., the fraction of biological variability is at least as high as the fraction of variability attributable to the inter-population mean differences. The bound affords the consistent estimator


where _𝑆_<sup>2</sup> is the sample variance over all Nc cells, ( _𝑋 𝑀_ ) _𝜅_ is the average expression in cell subpopulation _𝜅_ , and (Nc) _𝜅_ is the number of cells in that subpopulation.

To compare the results of the transformation procedures to this baseline, we analyzed a mouse glutamatergic neuron dataset [321], using pre-annotated subtypes to produce a lower bound. We considered several thousand genes, emphasizing the top 5% by dataset-wide average; these high-variability genes are typically of most interest in single-cell analyses (Figure 8.4b). The iterative application of transformations up to PCA typically deflated the gene-specific CV<sup>2</sup> values, particularly for the high-expression genes and in the log-transformation step. However, the application of UMAP inflated CV<sup>2</sup> throughout. We found that the high-expression genes’ variability was typically deflated relative to the raw data, suggesting that the data transformations attribute overdispersion to nuisance technical effects (Figure 8.4d-g).

Log-transformation, PCA, and UMAP violated the baseline computed from intersubtype variation, particularly for the high-expression genes. In addition, a considerable fraction of genes demonstrated variability exceeding that of the original

109

data after PF and UMAP. After the final step, more than a third of the genes in the dataset had, at some point in the analysis, gone below the lower bound. This result suggests that ubiquitous transformations efface meaningful biological signal. UMAP attempts to recover it by inflating cell type differences; however, since this inflation is genome-wide, it does not restore the quantitative information lost in previous steps, and may generate false findings.

We propose that a mechanistic approach provides a more reliable avenue for the analysis of sequencing data. In this worldview, all assumptions about the noise behaviors are explicit rather than implicit; count data are not to be denoised, but fit to a first-principles model that includes biological and technical noise terms. Once a satisfactory parametric fit is available, the fractions of biological and technical variability follow immediately (Section 4.6.5, using the bursty model in Section 4.6.2). This approach is outlined schematically in Figure 8.5a: given annotations, we canseparately fitcell subtypes, obtain theirbiophysical parameters, and aggregate them to obtain the fraction of biological variability. The details of the calculation amount to applying the following definitions:


inserting the plug-in estimates of the subtype-specific means and variances with (Table 4.2) and without (Table 4.1) technical noise. The fit, implemented in _Monod_ , attributes overdispersion in high-expression genes to biological variability (Figure 8.5b), in striking contrast to the non-parametric transformations. As a consequence, the inferred fraction of biological variability coheres with the baseline (Figure 8.5c).

Interestingly, this agreement is not merely a consequence of independently fitting cell subtypes and aggregating the variance. We used _Monod_ to fit the entire glutamatergic dataset, introducing some error due to the neglect of subtype heterogeneity. Quantitatively, this approach simply compares the coefficients of variation implied by Tables 4.1 and 4.2, without using _𝝅_ . We obtain similar results, with a single violation of the bound. This control suggests that the mechanistic procedure largely explains biological variability by transcriptional bursting, rather than subtype differences.

110

_C h a p t e r 9_

---

[← MODEL IDENTIFICATION AND SELECTION](14-model-identification-and-selection.md) · [Up: contents](index.md) · [DETERMINATION OF BIOLOGICAL DIFFERENCES →](16-determination-of-biological-differences.md)
