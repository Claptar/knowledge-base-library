---
title: BIOPHYSICAL MODELS FOR STOCHASTIC TRANSCRIPTION
source: https://thesis.library.caltech.edu/18729/
source_file: sources/carilli-2026-expression-regulation/Thesis_Carilli_Maria.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# BIOPHYSICAL MODELS FOR STOCHASTIC TRANSCRIPTION

**Source:** `Thesis_Carilli_Maria.pdf` from [carilli-2026-expression-regulation](https://thesis.library.caltech.edu/18729/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As discussed in Chapter I, the richness of single-cell data lies in distributions over single cells and the access they give to the cellular processes that generated the counts. In this chapter, we discuss how biophysical models describing stochastic transcriptional systems unlock deeper insight not present at the level of mean count comparison. First, we describe the Chemical Master Equation formulation and how it can be used to appropriately model scRNA-seq count data. Then, we show how such this can identify strategies of cellular recovery from radiation treatment at particular stages of the RNA life-cycle. We finally show how different models can be fit and compared to generate testable hypotheses about the underlying system biophysics.

### **3.1 Chemical Master Equation Models**

Transcription occurs due to the interactions of discrete, low-copy number molecular components, like two copies of a gene on homologous chromosomes and several transcription factors and RNA polymerases jostling in the nucleus. These systems can be modeled as discrete-valued, continuous time Markov chains (CTMCs), with the states defined as having a particular number of RNA molecules. The Chemical Master Equation (CME) formulation is appropriate to represent such a system as it tracks the probability over time of a system being in any given state, _𝑃_ ( _𝑥, 𝑡_ ), given rates of transitions between states:


where _𝐴_ is a matrix of rate transitions, and _𝑃_ ( _𝑥, 𝑡_ ) is column vector of probabilities over the possible states. If the set of possible states is infinite, _𝑃_ ( _𝑥, 𝑡_ ) is infinite dimensional. As a simple example, if there are two gene states, "on’" and "off" corresponding to states _𝑥_ = 1 and _𝑥_ = 1, respectively, and the gene switches "on” at a rate _𝑘 𝑜𝑛_ and "off” at a rate _𝑘 𝑜𝑓𝑓_ , the probability of being in the two states can be tracked:

26


This can be solved at steady-state (or, as _𝑡_ →∞) for probabilities over states by setting the time-derivative equal to zero: 0 = _𝐴𝑃𝑠𝑠_ ( _𝑥, 𝑡_ ). For the example above, this can be trivially solved to find _𝑃𝑠𝑠_ ( _𝑥_ = 1) = _𝑘𝑜𝑛𝑘_ + _<u>𝑜𝑛𝑘𝑜𝑓𝑓</u>_<sup>and</sup><sup>_𝑃𝑠𝑠_(</sup><sup>_𝑥_= 0)=</sup> _𝑘𝑜𝑛𝑘_ + _𝑜 𝑘𝑓𝑓𝑜𝑓𝑓_<sup>.</sup>

For scRNA-seq count data, to modeling a single species of RNA from gene _𝑔_ , N}, we define the states are all discrete integers (including zero) of RNA molecules. The one-species model includes a production step and a degradation step


where _𝛾_ is a Poisson rate of molecule decay and the dynamics of production are specifically left blank for now. For a model of one-species constitutive transcription (another Poisson process) with rate _𝑘_ model can be represented:


N _𝑔_ represents the RNA species itself, while we will use _𝑛_ to represent the associated observation (random variables) in probabilities: _𝑃_ ( _𝑛_ ). The constitutive transcription CME is written


However, as discussed in Chapter I, scRNA-seq data inherently includes _two_ (or more) count matrices: of nascent/unspliced<sup>1</sup> molecules that align to introns and mature/spliced molecules that align to exons<sup>2</sup> . Our model schema can be expanded to include a Poissonian splicing step ( _𝛽_ ) from nascent N _𝑔_ to mature M _𝑔_ molecules, which are degraded:


> 1Throughout this thesis, we use nascent and unspliced synonymously, as well as mature and spliced synonymously, although we note that the definition of a nascent or fully mature RNA molecule is not rigid.

> 2Technically, we can only assign reads that cross exon-exon boundaries as truly spliced. For the purposes of this thesis, molecules that ambiguously align to exons we assign to spliced counts, though their ambiguity can be modeled [90]

27

Thisresultsinabivariatesteady-statedistributionovernascentandmaturemolecules: _𝑃𝑠𝑠_ ( _𝑛, 𝑚_ ).

If, instead, we assume nascent molecules are produced in bursts with average size _𝑏_

To solve infinite state-space distributions such as the constitutive model (infinite number of RNA molecules) analytically, probability generating functions (PGFs) can be applied to convert infinite dimensional ODEs in time to finite dimensional PDEs. Generating functions represent infinite sequences of numbers as coefficients of a power series; for probability functions, this is:


or for nascent and mature RNA species,


For certain, simple systems (like constitutive transcription), these can be solved for exact analytical solutions using PGF rules of derivatives and partial derivatives [43, 91, 37] and comparing to PGFs of known probability distributions. For example, the above single species constitutive transcription model at steady-state results in the PGF _𝐺_ ( _𝑧_ ) = _𝑒 𝛾𝑘_<sup>(</sup><sup>_𝑧_−1)</sup> , which is the PGF of the Poisson distribution, the well-known results that constitutive transcription leads to Poisson distributed counts.

It is often helpful to convert the PGF to factorial-cumulant generating function, or log-PGF ( _𝐹_ ), and introducing a change of variables: _𝐹_ ( _𝑢, 𝑣, 𝑡_ ) = ln _𝐺_ (1 + _𝑢,_ 1 + _𝑣, 𝑡_ ) [43].

When the PGF or log-PGF cannot be solved analytically, the PGF can be solved on a large grid around the complex unit circle, then recover the probabilities by performing an inverse Fourier Transform (iFFT):


where _𝑁_ and _𝑀_ are chosen to be sufficiently larger integers (larger than the observed max of nascent and mature molecules) [43, 92].

28

To facilitate the fit of biophysical models, we built the software package _Monod_ [37]: the following outlines the biophysical models supported by _Monod_ , as well as how to include technical/sequencing noise. The following subsections are adapted from [37] Supplementary Sections 1.1 and 1.2.

### **Bursty**

The three-parameter bursty model describes the following biology:


where _𝐵_ is a geometrically-distributed random variable on N0 with mean _𝑏_ , and _𝑘_ is the burst frequency, set to unity with no loss of generality at steady state. This system has the following log-PGF [43]:


This model encodes the bursty production of mRNA, and is usually derived as the limit of a transcriptional process driven by a randomly switching promoter [33]. Specifically, if the promoter is described by a telegraph process with on rate _𝑘_ , off rate _𝑘 𝑜𝑓𝑓_ , and transcription rate in the on state _𝑘𝑖𝑛𝑖𝑡_ , then in the physiological limit of high initiation and off rates, the Chemical Master Equation (CME) reduces to the process in Equation 3.10 with _𝑏_ := _𝑘𝑖𝑛𝑖𝑡_ / _𝑘 𝑜𝑓𝑓_ (Section S1.3 of [93]).

### **Constitutive**

The two-parameter constitutive model describes the following biology:


where _𝑘_ is set to unity with no loss of generality at steady state. This system has the following PGF [94]:


i.e., the joint distribution is the product of two independent Poisson distributions. This model encodes the unregulated production of mRNA.

29

### **Extrinsic**

The three-parameter extrinsic noise model describes the following biology:


where _𝐾_ is a gamma distribution with shape _𝜈_ and scale 1. This system has the following log-PGF:


which follows immediately from the properties of generating functions [93]. This is the log-PGF of the bivariate negative binomial distribution, with negative binomial marginals [95]. This model encodes driving by a slow, Gamma-distributed transcriptional process [96, 97, 98, 99].

### **CIR-like**

The three-parameter CIR-like noise model describes the following biology:


where _𝐾𝑡_ is, informally, the time derivative of a subordinating inverse Gaussian process [99]. This system emerges in the fast limit of transcription driven by a Cox–Ingersoll–Ross process, and has the following log-PGF:


where _𝑈_ is identical to the expression in Equation 3.11, whereas _𝑏_ is a burst size-like “gain” that appears in the definition of _𝐾𝑡_ . This model encodes driving by a fast chemical Langevin equation, which in turn represents a high-concentration limit of the constitutive birth-death process [99].

### **Bursty with delayed splicing**

The three-parameter bursty model with delayed splicing describes the following biology:


where _𝜏_ is the deterministic retention time for X _𝑁_ and _𝑘_ is set to unity with no loss of generality at steady state. This model has the following log-PGF:

30


Since this equation is separable in _𝑢𝑁_ and _𝑢𝑀_ , the PGF is the product of two independent marginal PGFs; the nascent marginal is geometric-Poisson [100, 101] whereas the mature marginal is negative binomial.

### **Bursty with delayed degradation**

The three-parameter bursty model with delayed degradation describes the following biology:


where _𝜏_ is the deterministic retention time for X _𝑀_ and _𝑘_ is set to unity with no loss of generality at steady state. This model has the following log-PGF [101]:


### **Technical noise models**

In this section, we define the technical noise models of interest through their generating function definitions and solutions. These models account for the artifacts and biases introduced during the sequencing process.

To account for the imperfect sequencing process, we define a set of technical noise models. All of the models assume that the reverse transcription, amplification, and identification of the _in vitro_ mRNA pool is fundamentally an independent and identically distributed process across all cells and molecules of a single gene, although the identically distributed assumption is relaxed across genes. For inference, we define the PGF _𝐻_ , which is the function composition of _𝐺_ with the PGFs _𝐺 𝑧,𝑡_ of the sequencing processes:


31

### **Null process**

In the simplest case, the null process, the sequencing is perfect and every mRNA is captured and reported as a unique molecule:


The PGF of this process is _𝐺 𝑧,𝑡_ ( _𝑔𝑧_ ) = _𝑔𝑧_ = _𝑢𝑧_ + 1, yielding _𝐺 𝑧,𝑡_ ( _𝑢𝑧_ ) − 1 = ( _𝑢𝑧_ + 1) − 1 = _𝑢𝑁_ , i.e., _𝐺_ = _𝐻_ .

### **Bernoulli process**

In the Bernoulli process, each molecule has probability _𝑝𝑧_ of being captured and reported; multiple priming is impossible:


The PGF of this process is _𝐺 𝑧,𝑡_ ( _𝑔𝑧_ ) = _𝑝𝑧𝑔𝑧_ + (1 − _𝑝𝑧_ ) = _𝑝𝑧𝑢𝑧_ + 1, yielding _𝐺 𝑧,𝑡_ ( _𝑢𝑧_ ) − 1 = _𝑝𝑧𝑢𝑧_ .

### **Poisson process**

In the Poisson process, each molecule has a rate _𝜆𝑧_ of being captured and reported; multiple priming is possible, but rare if _𝜆𝑧_ is low:


This PGF of this process over unity time is _𝐺 𝑧,𝑡_ = _𝑒_<sup>_𝜆𝑧_(</sup><sup>_𝑔𝑧_−1)</sup> , i.e., _𝐺 𝑧,𝑡_ − 1 = _𝑒_<sup>_𝜆𝑧𝑢𝑧_</sup> − 1, which cannot be simplified further.

### **3.2 Application for Biological Insight**

In the following section, we show how the CME models of transcriptional processes can be applied to scRNA-seq data to discover modulated molecular signatures beyond mean expression. In particular, we use the _Monod_ package, which

This section summarizes section _Monod identifies strategies of resistance and recovery_ of [37] by G.G., T.C., M.C., J.J.V., and L.P. M.C. identified the application dataset, performed the analysis, and interpreted results, with discussions and suggestions from G.G., T.C., J.J.V., and L.P.

32

The expanded capabilities of biophysical DE analysis also allow the exploration more complex biological settings, where it is less clear which mechanisms are expected to change and which genes provide actionable targets for followup experiments. For example, understanding cellular strategies of recovery post-treatment aids in the selection of relevant therapies and promotion of desired cell behaviors [102].

For example, the intestine is one of the organs most sensitive to radiation damage: understanding how it heals following radiotherapy is important for promoting healthy recovery and survival of patients treated for abdominal, gastrointestinal, pelvic, and retroperitoneal tumors [102]. Particularly interesting is how immune cells are affected by and respond to radiation treatment. T cells, which are essential actors in the body’s natural response to tumor control [103, 104], are required for successful radiotherapy but are also believed to be damaged during treatment. While studies have investigated the transcriptomic landscapes of T cells following radiotherapy [103, 102], we suggest that a fuller understanding of the regulation of key genes, as revealed by biophysical parameter changes, could inform how therapeutics may be designed and more efficiently administered to enhance recovery from radiotherapy.

We re-analyze data from a study of the transcriptomic response of the intestinal microenvironment to radiation-induced intestinal injury (RIII) in wild-type C57BL/6J male mice [102] (Figure 3.1a). Mice were treated with 15 Gy of abdominal radiation, and intestinal samples were collected pre-radiation treatment (day 0) and at several time points following treatment (days 1, 3, 7 and 14 post treatment). We selected T cells based on the original study’s annotations, and inferred biophysical parameters for samples (where each sample is a unique mouse) with at least 100 T cells, leaving 11 samples across days 0, 1, 3 and 14, with at least two samples per day. We used the bursty model with Poisson technical sampling noise, and after fitting 3,000 genes shared across samples, subset to the 1,182 that passed goodness-of-fit testing in all samples, further correcting inferred parameters for sample-specific offsets (using one sample as the reference, we fit an orthogonal distance regression model over all genes for other samples and removed the per sample bias).

We first show that analysis through the lens of a biophysical model reveals more genes with differences in behavior across the timecourse of recovery. To assess the significance of parameter changes, we performed a _t_ -test with unequal variance on the log10 of each corrected parameter per gene for day 0 versus all other days. Specifically, we tested for changes in burst size ( _𝑏_ ), relative splicing rate ( _𝛽_ ), relative degradation rate ( _𝛾_ ) and normalized mature counts ( _𝜇𝑀_ ), correcting _𝑝_ -values for

33

the number of tested genes using the Benjamini Hochberg procedure (separately per parameter) to obtain false discovery rates (FDRs). Figure 3.1b shows that many genes that do not show significant differences in mature counts are detectable via parameter changes: testing the significance of inferred parameters in addition to means allows for the exploration of more genes whose significant difference between days or conditions may lie in regulatory strategy rather than mean expression change. For example, comparing day 1 to day 0, there were 380 genes with significant differences in a parameter but not in mature expression, 127 genes with differences in both, and 157 genes with significant differences in mature expression but not parameters (Figure 3.1b). We further emphasize that the analysis of parameters does not preclude testing for changes in mean, with our method adding to the list of possible genes for follow-up investigation.

In addition to identifying genes with parameter changes that are not detectable using standard mature expression comparisons, for genes which _do_ show significant differences in expression, _Monod_ can suggest what cellular regulatory strategy is responsible (e.g., an increase in burst size or a decrease in degradation rate, Figure 3.1c). For example, we show in Figure 3.1c (left) five genes which had significant increases between day 1 and day 0 in both burst size and mature RNA counts. As these genes also show increased degradation rate, the observed increase in mature counts is likely due to an increase in burst size (that exceeds the increase in degradation rate). These genes, which are upregulated early in the radiation-response timecourse (day 1 post treatment), have been studied as promising targets in cancer immunotherapy. _Cbl_ encodes the E3 ubiquitin ligase Casitas B lymphoma, which regulates immune cells and whose homologue Casitas B lymphoma-b (CBL-b) has been shown to promote immunosuppressive tumor microenvironments (TME) [105]. _Nt5e_ encodes 5’-nucleotidase (or Cd73), an immunosuppressive protein whose high expression is also associated with poor outcome of cancer patient’s TMEs [106] and is currently emerging as a novel target for immunotherapy [107]. Other genes whose high expression has been correlated with lower overall survival in cancers, are _Ncapd3_ , which is associated with reduced infiltration of immune cells into glioma [108], and the gene that codes for insulin-like growth factor 2 receptor ( _Igrf2_ ), which was found to be an indicator of poor prognosis in patients with triple-negative breast cancer [109]. On the other hand, the expression of _Mpp7_ , which codes for a scaffolding protein, has been shown to have a positive correlation with increased infiltration of T cells in melanomas [110].

34

Other notable genes show increases in mature RNA expression best explicable by decreases in degradation rate (Figure 3.1c, right). _Ets1_ encodes a transcription factor that is a proto-oncogene that promotes aggressive tumor behavior in a variety of cell types [111]. While not directly associated with cancer progression, the proteins encoded by _Pak2_ and _Git2_ are known to interact [112], and are crucial for the stability and suppressive function of regulatory T cells [113]. With knowledge about what specific point in the RNA lifecycle (e.g., bursty transcription or degradation) may lead to increased expression of a gene, researchers could design strategies to discourage known tumor promoters and encourage known tumor suppressors for increased efficacy and complementarity of radio- and immunotherapy.

Finally, we can identify genes whose parameters show similar dynamics (fold changes) over the timecourse of recovery from radiation treatment as compared to known tumor suppressing genes. For example, we found the three genes with fold change patterns most similar to _Znrf3_ (Figure 3.1), whose encoded protein negatively influences cancer progression by inhibiting key proliferative (WNT) signaling pathways [114, 115]; and another three with patterns most similar to _Tgfb1_ , which potentially suppress tumorigenesis at early cancer stages but promote tumorogenesis at advanced cancer stages [116]. Of these genes, some have been reported as important in cancer: for example, _Gch1_ is a known immunosuppression gene with upregulation previously linked to reduced survival in breast cancer [117]; _Lcp1_ encodes a prognostic biomarker in gastric cancer [118]; and _Arhgap15_ codes for a protein that is reported to slow colorectal tumor growth [119]. Other identified genes have not been as well-characterized in cancer studies: _Otulin_ encodes an immuneresponse peptidase [120], and _Fus_ and _Bbx_ are more general DNA damage-response genes [121, 122]. Analysis of biophysical parameters allows one to explore how genes that have been previously implicated in cancer prognoses are experiencing similar regulatory changes in response to radiation treatment, as well as to identify genes that have _not_ been previously implicated as targets for follow up therapeutic development.

### **3.3 Model Selection for Biophysical Hypothesis Generation**

This section summarizes section _Model selection and insight about gene regulation strategies_ of [37] by G.G., T.C., M.C., J.J.V., and L.P. M.C. identified the application dataset, performed the analysis, and interpreted results, with discussions and suggestions from G.G., T.C., J.J.V., and L.P.

35


Figure 3.1: **_Monod_ analysis of mechanisms of T cell recovery post radiation treatment. a.** Single-cell samples were taken from the intestines of mice exposed to 15 Gy of abdominal radiation before and at several time points after treatment. Illustrations adapted from NIAID NIH BIOART Source [123, 124, 125]. **b.** Two-sided _t_ -tests comparing T cells at days 1 (n=2), 3 (n=3) and 14 (n=2) post treatment to T cells before treatment (day 0, n=4) flag more genes as significant (false discovery rates, FDR ≤ 0.05) when comparing inferred parameters ( _𝑏, 𝛽, 𝛾_ ) than when merely comparing mature RNA counts ( _𝜇𝑀_ ). In the scatter plots, red dashed lines indicate a significance threshold of an FDR of 0.05. **c.** The log2 fold change (FC) of parameters (comparing day 1 to day 0) show that statistically significant changes in the mature mean expression of genes related to the progression of cancer and immune response can be attributed to statistically significant differences in parameters (i.e., burst size or degradation rate). A red asterisk indicates a FDR ≤ 0.05. **d.** Comparing genes’ parameter changes over the timecourse of recovery can identify similarly regulated genes. The top row shows the log10 of parameters and mean mature RNA expression at days 0, 1, 3 and 14. Each outlined point indicates a separate sample (mouse) with a smaller point at the mean over the log10 of samples’ parameters per day. Error bars indicate the interquartile range of the samples’ parameters per day. For certain genes, the log2 FCs of each parameter and mean mature expression for days 1, 3 and 14 from day 0 exhibit similar patterns as known tumor suppressors (bottom row).

36


<!-- Start of picture text -->
a b Fitting bursty and constitutive models<br>Biological models ⟹ Exponentially distributed waiting timeDeterministic waiting time L5/6 NPL5 IT<br>Transcription 𝒌 Splicing  𝜷 Degradation 𝜸 L6 IT<br>DNA nascent RNA mature RNA L2/3 IT d<br>Rate  (𝒌𝒐𝒏) Burst size  𝒃 Splicing  𝜷 Degradation 𝜸 L6 CT Number of rejected genes<br>DNA nascent RNA mature RNA L6b<br>Transcription 𝒌 ~ 𝚪 Splicing  Degradation<br>𝜷 𝜸 c Fitting five models<br>DNA nascent RNA mature RNA L5 IT<br>Rate  (𝒌𝒐𝒏) Burst size  𝒃 Splicing  𝜷 Degradation ⟹𝝉 L5/6 NPL6 IT Five models<br>DNA nascent RNA mature RNA L2/3 IT<br>Rate  (𝒌𝒐𝒏) Burst size  𝒃 ⟹ Splicing  𝝉 Degradation 𝜸 L6 CT<br>DNA nascent RNA mature RNA L6b<br>e<br>f N = 2,178L6b  N = 1,958L6 CT  N = 1,604L2/3 IT  Genes fit similarly  g Wip2  Ubl3 Ildr2 Eprs Ufd1<br>Delay Delay Delay well by<br>three<br>Eprs Ufd1 models.<br>Bursty Extrinsic Bursty Extrinsic Bursty Extrinsic<br>L6 IT  L5/6 NP  L5 IT<br>N = 1,776 N = 2,272 N = 2,217<br>Delay Delay Delay<br>Bursty Extrinsic Bursty Extrinsic Bursty Extrinsic # molecules<br>Constitutive<br>Bursty Number of cells per cell type<br>Extrinsic<br>Bursty and constitutive models<br>Delayed degradation (Delay)<br>Delayed splicing<br>Number of genes<br>Mature               Nascent<br><!-- End of picture text -->

Figure 3.2: **_Monod_ facilitates the comparison of different biophysical models on a per gene basis for thousands of genes across cell types.** Results are shown for Allen sample B08 [126]. **a.** Diagrams of five of the biological models implemented in _Monod_ , varying in transcription and processing kinetics. **b.** Of the 2,951 fit genes in each of six cell types, most genes display behavior more consistent with the bursty model than with the constitutive model using the Akaike information criterion (AIC) and two goodness-of-fit metrics (Hellinger distance from empirical distributions and chi-squared test). **c.** For the same six cell types and genes, the number of genes that are best fit by each of the five considered biological models, colored by model. Gray indicates genes for which all models were rejected). **d.** Fewer genes are rejected when fitting and comparing five models than fitting and comparing only the bursty and constitutive models. **e.** The same gene can exhibit different behavior in different cell types: the upset plot shows the number of genes that are best fit by a given model or combination of models across the six cell types. **f.** Ternary diagram of genes’ normalized AIC weights for the three most commonly selected models, colored by the model with the largest AIC weight. Only genes for which none of these models were rejected are displayed, with the number indicated. **g.** Predicted marginal nascent and mature distributions for each model plotted over normalized empirical histograms of molecule counts for the indicated genes in layer 6 neurons (L6 CT). _Eprs_ and _Ufd1_ , which had similar AIC weights for the bursty, extrinsic, and delay models, are noted with a red star in the ternary diagrams.

37

_Monod_ currently supports 6 sophisticated yet tractable models of transcription, previously shown to describe and distinguish between features of experimental data [99, 101, 36] for thousands of genes across multiple cell types. We emphasize that _Monod_ supports _modular_ model comparison, in the sense that one can freely modify assumptions about a specific model component (e.g., whether degradation occurs with a deterministic or stochastic waiting time) to obtain a new model to test against data. We recommend using _Monod_ with the bursty model by default, as it captures observed overdispersion [127] and known biophysics [33, 128] while only minimally complexifying the constitutive model. But the bursty model may not _always_ fit the data best, and it is worth testing to what extent a less complex, more complex, or simply different model performs better in practice.

We use _Monod_ to analyze mouse brain data with 2,951 genes and six cell types (Allen sample B08 [126]) and show that the bursty model almost always outperforms the simpler constitutive model, and tends to perform fairly well against alternative models (see Figure 3.2a for schematics of the 5 models we consider in this section). Moreover, we show that it is useful to consider a richer space of transcription models, since specific models may fit specific genes or cell types better or worse, which suggests _Monod_ -derived fits yield insight about gene- and cell-type-specific gene regulation strategies. We reject models (for a given cell type and gene) if they fail to pass the goodness-of-fit thresholds of Hellinger distance to empirical distributions and chi-square tests.

We first compare the constitutive model to the bursty model. For many genes, only the bursty model passes goodness-of-fit thresholds. When neither the bursty nor the constitutive models are rejected for a gene, the bursty model is usually a better fit according to Akaike information criterion (AIC, Figure 3.2b). It is extremely rare that the constitutive model fits the data better, perhaps unsurprisingly as the constitutive model is a special case of the bursty model and the overdispersion of single-cell count data is well known, but diverging from previous studies that advocate the Poisson model [129].

Although the transcriptional behavior of many genes is consistent with the bursty model, comparing all five of the (comparably complex) proposed models reveals that the extrinsic, delayed degradation, and delayed splicing models are better fits for some genes in different glutamatergic cell types (Figure 3.2c). This comparison also suggests differences between cell types’ transcriptional regulation strategies, with more genes best fit by the extrinsic model in layer 6 intratelencephalic (L6 IT)

38

neurons than in layer 5/6 near-projecting (L5/6 NP) neurons, for example (Figure 3.2c). Further, including the additional models increases the number of genes in each cell type for which one or more models pass goodness-of-fit thresholds: fewer genes are rejected by all models when considering more models (Figure 3.2d). As all models were compared in a standard way using the same data, fitting pipeline, and statistical rejection criteria, the discrepancies between proposed models could be evidence of real biological variety in transcriptional and post-transcriptional regulation mechanisms.

While cell type comparisons show distinctions between the number of genes best fit by each model in a given cell type, _Monod_ also provides the tools to investigate how genes exhibit expression patterns consistent with different transcriptional models across cell types (Figure 3.2e). We found the model with the largest AIC weight for every gene in every cell type, then for each gene collapsed models over cell types to a set of unique models. The upset plot in Figure 3.2e shows how many genes exhibited each combination of models preferentially across the six cell types. For example, only three genes exhibited _only_ bursty behavior preferentially, while 580 genes were best fit by the bursty model in at least one cell type and by the extrinsic model in at least one other cell type. All but 27 genes exhibited expression trends described best by at least two unique models, with the most common set (622 genes) being bursty, extrinsic, and delayed degradation. Interestingly, no genes were best fit by only the delayed splicing or only the constitutive model across the six cell types (Figure 3.2g).

While these trends may reflect biological differences, they may also highlight differences in the mutual identifiability of the proposed models. For example, the bursty, extrinsic, and delayed degradation model all account for correlation between nascent and mature counts, while in the constitutive and delayed splicing model, nascent and mature counts are uncorrelated. Thus the genes that are best fit by the three models or some subset may be in fact displaying similar behavior across different cell types, with the correlation between their nascent and mature counts, ruling out the constitutive and delayed splicing models, as the salient feature driving the fits (similarly to Gorin et al. [101]).

To explore this question, we can asses the identifiability of models, or the extent to which the “best” fit model is “better” than other models. While we can assign a gene to the model with the largest AIC weight, there is not always a clear distinction between model fits. To illustrate this, we show a simplex of normalized AIC weights

39

for the bursty, extrinsic, and delayed degradation models, colored by the assigned regulatory model: the weights for the “best” fit models are sometimes arbitrarily close to the other two models’ weights (Figure 3.2f). In this way, genes with clear preference for a given model can be distinguished from those which are similarly fit by two or more models. These results can also be verified by visualizing modelbased probabilities and normalized empirical count histograms. Figure 3.2g shows genes that were not rejected by only the bursty model ( _Wipf2_ ), only the extrinsic model ( _Ubl3_ ), and only the delayed degradation model ( _Ildr2_ ) in layer 6 neurons (L6 CT). _Eprs_ and _Ufd1_ , indicated with red stars in Figure 3.2f, were fit similarly well under the three models. In the histograms for _Wipf2_ , _Ubl3_ , and _Ildr2_ , we underline the (Poisson) constitutive model’s poor ability to recapitulate the overdispersed data, consistent with Figure 3.2b-c.

_Monod_ makes fitting subtly distinct mechanistic models of transcription for thousands of genes straightforward, thereby leading to increased ease of model comparison and selection. Performing goodness-of-fit and likelihood tests on _Monod_ fits provides a route for discerning between biophysical models that may have generated the data. However, we note that definitive model selection is beyond the scope of _Monod_ : rather than to come to definite conclusions, _Monod_ should be used to explore data and to compare and generate hypotheses that can later be tested experimentally.

40

_C h a p t e r 4_

---

[← CONTRASTIVE DIMENSIONALITY REDUCTION FOR DIFFERENTIAL VARIANCE](07-contrastive-dimensionality-reduction-for-differential-varian.md) · [Up: contents](index.md) · [NEURAL APPROXIMATIONS FOR INTRACTABLE BIOPHYSICAL MODELS →](09-neural-approximations-for-intractable-biophysical-models.md)
