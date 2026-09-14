---
title: BIOPHYSICAL MODELS IN VARIATIONAL AUTOENCODERS
source: https://thesis.library.caltech.edu/18729/
source_file: sources/carilli-2026-expression-regulation/Thesis_Carilli_Maria.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# BIOPHYSICAL MODELS IN VARIATIONAL AUTOENCODERS

**Source:** `Thesis_Carilli_Maria.pdf` from [carilli-2026-expression-regulation](https://thesis.library.caltech.edu/18729/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the previous Chapter, we discussed how biophysical models can be efficiently approximated for high-throughput inference of transcriptional parameters at the scale of modern day scRNA-seq data (millions of cells and tens of thousands of genes). Here, we combine this approximation strategy with deep learning architectures for data integration, dimension reduction, and parameter inference. We present _biVI_ , which combines the variational autoencoder framework of _scVI_ with CME models describing the transcription and splicing kinetics of RNA molecules. We demonstrate on simulated and experimental scRNA-seq data that _biVI_ retains the variational autoencoder’s ability to capture cell type structure in a low-dimensional space while enabling genome-wide exploration of the biophysical mechanisms, such as system burst sizes and degradation rates, that underlie observations.

This chapter summarizes [47] by M.C.<sup>∗</sup> , G.G<sup>∗</sup> , Y.C., T.C., and L.P. M. C., G.G. and Y. C. implemented the strategy. M.C. ran analyses. G. G. conceptualized the project and provided detailed feedback and project direction. T. C. and L. P. provided guidance and suggestions throughout. M. C., G. G., T. C. and L. P. wrote the manuscript.

### **5.1 Single-cell Variational Inference**

Advances in experimental methods for single-cell RNA sequencing (scRNA-seq) allow for the simultaneous quantification of multiple cellular species, such as nascent and mature transcriptomes [136, 137], surface [168, 138, 166] and nuclear [169] proteomes, and chromatin accessibility [165]. While these datasets enable insight into cell type and state in development and disease, joint analyses of distinct modalities remain challenging. We show that principled biophysical “integration” of multimodal datasets can be achieved through parameterization of interpretable mechanistic models [99], scalable to thousands of genes across tens of thousands of cells [170].

Recent approaches to integrate and reduce the dimensionality of multimodal singlecell genomics data have leveraged advances in machine learning [149, 171, 172].

58


Figure 5.1: _biVI_ reinterprets and extends _scVI_ to infer biophysical parameters. **a.** _scVI_ can take in concatenated nascent (N ) and mature (M) RNA count matrices, encode each cell to a low-dimensional space _𝑧_ , and learn per-cell parameters and per-gene parameters for independent nascent and mature count distributions. This is not motivated by a biophysical model. **b.** The telegraph model of transcription: a gene locus has the on rate _𝑘_ , the off rate _𝑘𝑜𝑓𝑓_ , and the RNA polymerase binding rate _𝑘_ RNAP. Nascent RNA molecules are produced in geometrically distributed bursts with mean _𝑏_ = _𝑘_ RNAP/ _𝑘𝑜𝑓𝑓_ , which are spliced and degraded at rates _𝛽_ and _𝛾_ , respectively. The model’s steady-state distribution can be approximated by a pre-trained neural network F and a set of basis functions. **c.** _biVI_ intakes nascent and mature count matrices, produces a low-dimensional representation for each cell, and outputs per-cell and per-gene parameters for a mechanistically motivated joint distribution of nascent and mature counts.

For example, the popular tool _scVI_ is a variational autoencoder that uses neural networks to encode scRNA-seq counts to a low-dimensional representation. This is decoded by another neural network to cell- and gene- specific parameters for conditional likelihood distributions of observed counts [148]. These distributions are chosen _post hoc_ to be consistent with the discrete, over-dispersed nature of scRNA-seq counts, but can be derived from biophysical models. Extensions of _scVI_ for protein [149] and chromatin measurements [173] jointly encode data modalities to a single latent space, then employ two decoding networks to produce parameters for _independent_ conditional likelihoods specific to each datatype. Nascent and mature transcripts, available by realigning existing scRNA-seq reads [136, 137], could be similarly treated (Figure 5.1a). However, using independent conditional likelihoods for bimodal measurements derived from the same gene ignores their inherent causality and has no biophysical basis: the generative model is a “black

59

box” representation to summarize data.

Nevertheless, good causal model candidates are available (Figure 5.1b). For example, Figure 5.1b illustrates the extensively validated [33, 35, 174] bursty model of transcription. While the joint steady-state distribution induced by the bursty model is analytically intractable [43], we have previously shown that it can be approximated by a set of basis functions with neural-network learned weights [46].

### **5.2 Adapting Variational Autoencoders for Biophysical Models**

We introduce _biVI_ , a strategy that adapts _scVI_ to work with well-characterized stochastic models of transcription. We propose models, formalized by chemical master equations (CMEs), for RNA lifecycles, then use the bivariate, CME-derived distribution as the conditional data likelihood distribution for nascent and mature counts (Figure 5.1c). The inferred conditional likelihood parameters thus have biophysical interpretations as part of a mechanistic model of transcription, moving beyond associational analyses to fit biophysical values that parameterize causal relationships based on known transcriptional dynamics [43]. The likelihood distributions cannot be obtained solely from the data distributions but require some “knowledge of the data-generating process" [175].

We used simulated data to show that _biVI_ models can recapitulate ground-truth distributions, produce latent representations that preserve cell type structure, (see Supplementary Figures 3, 4, and 5 of [47]) and recover marker genes (Supplementary Figure 6 of [47]). Several clustering metrics are slightly lower for _biVI_ than for _scVI_ , suggesting some trade-off between latent feature representation and improved interpretability (see Supplementary Figures 3, 4, and 5 of [47]). Average inferred parameters were relatively robust to error in nascent versus mature count quantification (Supplementary Figure 7 of [47]). To validate the reliability of _biVI_ inferred parameters, we showed that _biVI_ inferred burst sizes and relative degradation rates correlate with those obtained in fluorescence assays and time-series labeling data (Supplementary information and Supplementary Figures 8, 9, and 10 of [47]) [154, 176].

After validations, we applied _biVI_ to experimental datasets from mouse brain tissue [126], Supplementary Figures 11 and 12 of [47]) for Allen sample B08 using the well-attested [33, 35, 174] bursty model of transcription. _biVI_ can recapitulate empirical distribution shapes better than _scVI_ (Figure 5.2a-b) as measured by both Kullback-Leibler divergence and Hellinger distance (Supplementary Figure 13 of

60


Figure 5.2: _biVI_ fits single-cell data from mouse primary motor cortex (Allen sample B08 [126]) and suggests the biophysical basis for expression differences. **a.** - **b.** Observed, _scVI_ and _biVI_ reconstructed distributions of _Foxp2_ , a marker gene for L6 CT (layer 6 corticothalamic) cells, and _Rorb_ , a marker gene for L5 IT (layer 5 intratelencephalic) cells, restricted to respective cell type. **c.** - **d.** Cell-specific parameters inferred for _Foxp2_ and _Rorb_ demonstrate identifiable differences in means and parameters in the marked cell types (1,333 L6 CT cells and 2,395 L5 IT cells colored of 6,398 total illustrated cells). **e.** Cell subclasses show different modulation patterns, especially pronounced in non-neuronal cells (top: fractions of 2,000 highly variable genes that exhibit differences in each parameter; bottom: number of cells in each subclass). **f.** _biVI_ allows the identification of cells which exhibit differences in burst size or relative degradation rate, without detectable differences in mature mean expression. **g.** Histograms of _biVI_ parameters and _scVI_ mature means for genes that exhibit modulation in _biVI_ parameters (degradation rate in L5 IT cells for _Trem2_ , top; burst size in L6 CT cells for _Ndnf_ , bottom) but no identifiable mature mean modulation.

[47]), while allowing for interpretation of cell-specific parameters to determine _how_ genes are regulated. For example, in Figure 5.2c-d, we illustrate how the upregulation of markers _Foxp2_ and _Rorb_ can be ascribed to an increase in burst size. Figure 5.2e shows the fraction of genes in each cell subclass that exhibited significant differences in burst size, relative degradation rate, or both. Interesting trends across cell subclasses emerge: neuronal cells appear to regulate gene expression via a mix of regulatory strategies, while non-neuronal cells seem to preferentially modulate burst size.

61

Finally, _biVI_ can identify distributional differences which do not result in mean expression changes (Figure 5.2g). To identify biophysical parameters with statistically significant differences between cell subclasses, we performed Bayes factor hypothesis testing, which accounts for the uncertainty in parameter estimates by comparing multiple samples from cells’ latent space posterior distributions (see subsection "Bayes factor hypothesis testing for differential expression" and Supplementary Figure 14 of [47]). Certain cell subclasses had several hundred genes that displayed differential burst size or relative degradation rate but not differential spliced mean expression. For example, the gene _Ndnf_ , which codes for the neuron derived neurotrophic factor NDNF, demonstrated a significant difference in the _biVI_ inferred burst size, but not _scVI_ inferred mature mean, in the neuronal subclass L6 CT (Figure 5.2g, bottom row, with empirical count distributions in Supplementary Figure 15 of [47]). NDNF promotes the neuronal health [177]; characterizing its regulatory patterns could help elucidate its role in neuronal maintenance. As another example, the relative degradation rate of the gene coding for the triggering receptor expressed on myeloid cells-2 (TREM2), was found to be greater in the neuronal L5 IT subclass than in other subclasses (Figure 5.2g, top row, with empirical count distributions in Supplementary Figure 15 of [47]). TREM2 variants are associated with increased risk of Alzheimer’s disease [178]: though known to be highly expressed in microglia, finer-grained analyses could uncover cell type specific effects on Alzheimer’s development. Such mechanistic description provides a framework for characterizing the connection between a gene’s role and a cell’s regulatory strategies beyond observational changes in mean expression [131].

We have demonstrated that bivariate distributions arising from mechanistic models can be used in variational autoencoders for principled integration of nascent and mature RNA-seq data. In addition to the bursty model, _biVI_ implements constitutive and extrinsic noise models previously discussed in the literature (see Chapter III, Section "Biophysical Models for Stochastic Transcription") [179, 99, 180]. While all three biophysical models are available, one limitation of the current framework is that only one model can be fit to all genes of a input dataset at a time, requiring _post hoc_ model comparison (Supplementary Figure 13 of [47]). In addition, sources of technical noise, such as length biases shown to distort nascent RNA capture [181], are not explicitly parameterized in the current version. Finally, while the conditional data likelihood distribution has been replaced by one derived from an interpretable biophysical hypothesis, the neural encoder and decoder still perform opaque mappings between data dimensions. Complementary improvements in in-

62

terpretability can be achieved using single-layer linear decoders [182] to directly link latent variables with gene parameters via layer weights (Supplementary Figure 16 of [47]). The current _biVI_ framework can be naturally extended to model more modalities (e.g., protein counts and chromatin accessibility) and more complex regulatory hypotheses, and, as single-cell technologies expand in scale and resolution, used to build a more comprehensive picture of biophysical processes in living cells.

### **_biVI_ Implementation and Fits**

In order to extend the _scVI_ method to work with multimodal molecule count data in a way that is coherent with biology, we define bivariate likelihood functions that (i) encode a specific, precedented mechanistic model of transcriptional regulation and (ii) are admissible under the assumptions made in the standard _scVI_ pipeline. On a high level, our method entails the following steps:

1. Choose one of the _scVI_ univariate generative models (under ‘ _scVI_ models’), including the functional form of its likelihood and any assumptions about its distributional parameters.

2. Identify a one-species chemical master equation (CME) that produces this distribution as its steady state, and translate assumptions about distributional parameters into assumptions about the biophysical quantities that parameterize the CME (under ‘Master equation models interpreted for _biVI_ ’). The onespecies system and its assumptions will typically not be uniquely determined.

3. Identify a two-species CME and derive assumptions about parameter values consistent with the one-species system (under ‘Master equation models interpreted for _biVI_ ’). There will typically be multiple ways to preserve the assumptions but only a single CME.

4. Modify the autoencoder architecture to output the variables that parameterize the CME solution under the foregoing assumptions, and use this solution as the generative model (see ‘ _biVI_ modifications to _scVI_ ’).

### **Statistical preliminaries**

We use the standard parameterization of the Poisson distribution:


We use the shape-mean parameterization of the univariate negative binomial distri-

63

### bution:


We use mean parameterization of the geometric distribution on N0:


### **_scVI_ models**

A brief summary of the generative process of the standard, univariate _scVI_ pipeline is useful to contextualize the options and constraints of the bivariate model. In the Bayesian model, each cell has some posterior probability _𝑝𝑐_ ( _𝑧𝑐_ ) over a lowdimensional space and can be represented as a sample _𝑧𝑐_ from that posterior. _scVI_ uses the “decoder” neural network to map from realizations _𝑧𝑐_ to quantities _𝜌𝑐𝑔_ , which describe the compositional abundance of gene _𝑔_ in cell _𝑐_ as a function of _𝑧𝑐_ , such that<sup>�</sup> _𝑔_<sup>_𝜌_</sup> _𝑐𝑔_<sup>= 1.Furthermore, a cell-specific “size factor”</sup><sup>_ℓ_</sup> _𝑐_<sup>is sampled from a</sup> lognormal distribution parameterized by either fit or plug-in estimates of mean and variance such that the mean expression of a gene in a given cell is _𝜇𝑐𝑔_ = _𝜌𝑐𝑔ℓ𝑐_ .

The univariate workflow provides the options of three discrete generative models: Poisson with mean _𝜇𝑐𝑔_ , negative binomial with mean _𝜇𝑐𝑔_ and gene-specific dispersion parameter _𝛼𝑔_ , and zero-inflated negative binomial, with an additional Bernoulli mixture parameter. We report the master equation models consistent with the first two generative laws below, and discuss a potential basis for and reservations about the zero-inflated model in ‘The zero-inflated negative binomial model and its multi-state interpretation.’

Due to the intractability of the posterior probability _𝑝𝑐_ ( _𝑧𝑐_ ), _scVI_ uses variational inference to infer an approximate posterior _𝑞𝑧_ ( _𝑧𝑐_ ), which is a multivariate Gaussian. Models are trained via stochastic optimization of the Evidence Lower Bound, or ELBO, which minimizes the Kullback-Leibler divergence between the approximate posterior and a prior and maximizes the expected value of the conditional likelihood over the approximate posterior. The Gaussian form of the approximate posterior makes possible a reparameterization trick to calculate gradients of the ELBO over expectation estimates made by Monte Carlo sampling from the approximate posterior. Further, the encoding network amortizes inference by learning a map between data to parameters of the approximate posterior [171, 148].

64

### **Master equation models interpreted for** **_biVI_**

The one-species CMEs encode reaction schema of the following type:


where X is a generic transcript species used to instantiate a univariate _scVI_ generative model, _𝛾_ is the transcript’s Markovian degradation rate, and the specific dynamics of the transcription process (first arrow) are deliberately left unspecified for now. Such systems induce univariate probability laws of the form _𝑃_ ( _𝑥_ ).

The two-species CMEs encode reaction schema of the following type:


where N denotes a _n_ ascent species, M denotes a _m_ ature species, and _𝛽_ denotes the nascent species’ Markovian conversion rate. Such systems induce bivariate probability laws of the form _𝑃_ ( _𝑛, 𝑚_ ). We typically identify the nascent species with unspliced transcripts and the mature species with spliced transcripts. We use the nascent/mature nomenclature to simplify notation and emphasize that this identification is natural for scRNA-seq data, but not mandatory in general.

Formalizing a model in terms of the CME requires specifying the precise mechanistic meaning of _𝜌𝑐𝑔_ and _ℓ𝑐_ . Previous reports equivocate regarding the latter [149], appealing either to cell-wide effects on the biology (in the spirit of [179, 180]) or technical variability in the sequencing process (in the spirit of [183]). For completeness, we treat both cases.

Below, we present the theoretical results, including the biophysical models, the functional forms of bivariate distributions consistent with the standard _scVI_ models, and the consequences of introducing further assumptions. The full derivations are given in Supplementary information of [47].

### **_Constitutive_ : The Poisson model and its mechanistic basis**

The Poisson generative model can be recapitulated by the following schema:


where _𝑘_ is a constant transcription rate. This process converges to the bivariate Poisson stationary distribution, with the following likelihood:


65

where _𝜇𝑁_ = _𝑘_ / _𝛽_ and _𝜇𝑀_ = _𝑘_ / _𝛾_ . If we suppose each gene’s _𝛽_ and _𝛾_ are constant across cell types, the likelihoods involve a single compositional parameter _𝜌𝑐𝑔_ , such that


where _𝛾𝑔_ / _𝛽𝑔_ ∈ R<sup>+</sup> is a gene-specific parameter that can be fit or naïvely estimated by the ratio of the unspliced and spliced averages. On the other hand, if the downstream processes’ kinetics can also change between cell types, we must use two compositional parameters:


We refer to this model as “Poisson,” reflecting its functional form, or “constitutive,” reflecting its biophysical basis.

**_Extrinsic_ : The negative binomial model and a possible mixture basis**

The negative binomial generative model can be recapitulated by the following schema:


where _𝑘_ is the transcription rate, a realization of _𝐾_ , a gamma random variable with shape _𝛼_ , scale _𝜂_ , and mean ⟨ _𝐾_ ⟩ = _𝛼𝜂_ . This process converges to the bivariate negative binomial (BVNB) stationary distribution, with the following likelihood:


where _𝜇𝑁_ = ⟨ _𝐾_ ⟩/ _𝛽_ and _𝜇𝑀_ = ⟨ _𝐾_ ⟩/ _𝛾_ . If we suppose that cell type differences only involve changes in the transcription rate scaling factor _𝜂_ , with constant _𝛼_ , _𝛽_ , and _𝛾_ , the likelihoods involve a single compositional parameter _𝜌𝑐𝑔_ . The mean parameters are identical to Equation 5.8, with an analogous parameter _𝛾𝑔_ / _𝛽𝑔_ , as well as a gene-specific shape parameter _𝛼𝑔_ . On the other hand, if the downstream processes’ kinetics can also change between cell types, we must use two compositional parameters, as in Equation 5.9.

We refer to this model as “extrinsic” to reflect its biophysical basis in extrinsically stochastic rates of transcriptional initiation.

66

**_Bursty_ : The negative binomial model and a possible bursty basis**

The negative binomial generative model may be recapitulated by the alternative schema [43]:


where _𝑘_ is the burst frequency and _𝐵_ is a geometric random variable with mean _𝑏_ (Equation 5.3). This system converges to the following stationary distribution:


where system moments can be calculated _𝜇𝑁_ = _𝑘𝑏_ / _𝛽_ , _𝜇𝑀_ = _𝑘𝑏_ / _𝛾_ , and _𝛼_ is arbitrarily set to _𝑘_ / _𝛽_ , the shape parameter of the nascent marginal, for simplicity.

Although the nascent marginal is known to be negative binomial, the joint _𝑃_ ( _𝑛, 𝑚_ ) and conditional _𝑃_ ( _𝑚_ | _𝑛_ ) distributions are not available in closed form. For a given set of parameters, the joint distribution can be approximated over a finite microstate domain _𝑛, 𝑚_ ∈[0 _, 𝑆𝑁_ − 1] × [0 _, 𝑆𝑀_ − 1], with total state space size _𝑆𝑁_ × _𝑆𝑀_ . This approach is occasionally useful, if intensive, for evaluating the likelihoods of many independent and identically distributed samples. The numerical procedure entails using quadrature to calculate values of the generating function on the complex unit sphere, then performing a Fourier inversion to obtain a probability distribution [43]. However, this strategy is inefficient in the variational autoencoder framework, where each observation is associated with a distinct set of parameters. Furthermore, it is incompatible with automatic differentiation.

In the previous chapter, [46], we demonstrated that the numerical approach can be simplified by approximating _𝑃_ ( _𝑚_ | _𝑛_ ) with a learned mixture of negative binomial distributions: the weights are given by the outputs of a neural network, whereas the negative binomial bases are constructed analytically. The neural network is trained on the outputs of the generating function procedure. Although the generative model does not have a simple closed-form expression, it is represented by a partially neural, pre-trained function that is _a priori_ compatible with the VAE.

If we suppose cell type differences only involve changes in the burst size _𝑏_ , with constant _𝑘_ , _𝛽_ and _𝛾_ , we use Equation 5.13 to evaluate likelihoods. These likelihoods involve a single compositional parameter _𝜌𝑐𝑔_ , with mean parameters identical to Equation 5.8, with an analogous parameter _𝛾𝑔_ / _𝛽𝑔_ , as well as a gene-specific shape parameter _𝛼𝑔_ . On the other hand, if kinetics of the degradation process can also

67

changebetween celltypes, wemustuse twocompositional parameters, asin Equation 5.9. There is no admissible way to allow modulation in the burst frequency.

We refer to this model as “bursty,” reflecting its biophysical basis.

### **_biVI_ bursty generative model**

Following the notation of _scVI_ [148], _biVI_ ’s generative process for the bursty hypothesis models expression values of _𝑥𝑐𝑛_ and _𝑥𝑐𝑚_ of nascent and mature counts, respectively, in cell _𝑐_ as:


with a standard, multivariate normal prior on the latent space _𝑧_ vector. Here, the batch of cell _𝑐_ is denoted as _𝑠𝑐_ and _ℓ𝜇, ℓ𝜎_ 2 are by default observed mean and variance in log-sequencing depth (‘log-library size’ in _scVI_ ) across a cell’s batch, although they can be learned. Further, as in _scVI_ , _𝑓_ is neural network that produces fraction of sequencing depth parameters _𝜌𝑐𝑔_<sup>(</sup><sup>_𝑁_)</sup><sup>_, 𝜌_</sup> _𝑐𝑔_<sup>(</sup><sup>_𝑀_)</sup> for nascent and mature counts. The sum of nascent and mature fractions is constrained to be 1 over a cell _𝑐_ by a softmax applied to the network output:<sup>�</sup><sup>_𝐺_</sup> _𝑛,𝑚_ =0<sup>(</sup><sup>_𝜌_</sup> _𝑐𝑔_<sup>(</sup><sup>_𝑁_)</sup><sup>_, 𝜌_</sup> _𝑐𝑔_<sup>(</sup><sup>_𝑀_))=1, where</sup><sup>_𝐺_is the number of</sup> genes. _𝛼_ ∈ R<sup>_𝐺_</sup> is a network parameter jointly optimized across all cells during the variational inference procedure. To recover biophysical parameters, _𝛼_ is arbitrarily set to _𝑘_ / _𝛽_ . Burst size _𝑏_ and relative degradation rate _𝑘_ / _𝛾_ can be recovered according to the following conversions:


We further set _𝑘_ = 1 with no loss of generality at steady-state. Generative processes for constitutive and extrinsic noise models are discussed in Supplementary information under ‘ _biVI_ constitutive generative process’ and ‘ _biVI_ extrinsic generative process’ of [47].

68

### **_biVI_ modifications to** **_scVI_**

Our code is built upon _scVI_ version 0.18.0 [171]; the following outlines the modifications we made for _biVI_ . The _scVI_ framework already supports the constitutive model. By setting conditional likelihood to “poisson,” no modification of _scVI_ architecture is necessary. The conditional data likelihood distribution is the product of two Poisson distributions (Equation 5.7). Explicitly, unspliced and spliced count matrices can be concatenated along the cell axis to produce a matrix of shape _𝐶_ by 2 _𝐺_ , where _𝐶_ is the number of cells and _𝐺_ the number of genes. _scVI_ will then produce 2 _𝐺_ Poisson mean parameters for the two Poisson distributions of Equation 5.7.

For the extrinsic and bursty models, mean parameters for nascent and mature counts, _𝜇𝑁_ and _𝜇𝑀_ , and a single shape parameter _𝛼_ are necessary. The default _scVI_ architecture returns two independent parameters for nascent and mature counts of the same gene. _biVI_ thus modifies the _scVI_ architecture to update vectors _𝛼_ ∈ R<sup>_𝐺_</sup> ≥0<sup>ratherthan</sup><sup>_𝛼_∈R2</sup> ≥<sup>_𝐺_</sup> 0<sup>,where</sup><sup>_𝐺_isthenumberofgenes.</sup> For the extrinsic model, the conditional data likelihood distribution is set to the extrinsic likelihood _𝑃_ extrinsic( _𝑛, 𝑚_ ; _𝛼, 𝜇𝑁 , 𝜇𝑀_ ) (Equation 5.11). For the bursty model, the conditional data likelihood distribution is set to the bursty likelihood _𝑃_ bursty( _𝑛, 𝑚_ ; _𝛼, 𝜇𝑁 , 𝜇𝑀_ ) (Equation 5.13). These models also intake concatenated unspliced and spliced matrices of shape _𝐶_ by 2 _𝐺_ . We implemented _biVI_ in an environment with Python 3.8.10 and PyTorch 1.12.1+cu113 [161].

### **Preprocessing Allen sample B08**

Raw 10x v3 single-cell data were originally generated by the Allen Institute for Brain Science [126]. The raw reads in FASTQ format [184] and cluster metadata [185] were obtained from the NeMO Archive. We selected mouse library B08 (donor ID 457911) for analysis in the main text.

To obtain spliced and unspliced counts, we first obtained the pre-built mm10 mouse genome released by 10x Genomics ( `https://support.10xgenomics. com/single-cell-gene-expression/software/downloads/latest` , version 2020-A). We used _kallisto|bustools_ 0.26.0, a wrapper for _kallisto_ 0.46.2 and _bustools_ 0.40.0, [137] to build an intronic/exonic reference ( `kb ref` with the option `--lamanno` ). Next, we pseudoaligned the reads to this reference ( `kb count` with the option `--lamanno` ) to produce unspliced and spliced count matrices. We used the outputs produced by the standard _bustools_ filter. This filter was relatively per-

69

missive: all (8,424) barcodes given cell type annotations in the Allen metadata were present in the output count matrix (10,975 barcodes).

Based on previous clustering results, we selected cells that were given cell type annotations, and omitted “low quality” or “doublet” barcodes [126], for a total of 6,418 cells. Although any choice to retain or omit cells from analysis is arbitrary, our work models the generating process that produced cells’ nascent and mature counts by presupposing each barcode corresponds to a single cell. Therefore, we propose that cells identified as low-quality (empty cells) or as doublets (two cells measured in one observation) [126] have a fundamentally different data-generating process than individual single-cells, and therefore remove them before fitting VAE models. However, we stress that the stochastic nature of transcription and sequencing, the intrinsic uncertainties associated with read alignment, and the numerical compromises made in clustering large datasets mean that previous annotations are not “perfect,” merely a reasonable starting point for comparing alternative methods.

We used Scanpy 1.7.2 [186] to restrict our analysis to the most variable genes, which presumably reflect the cell type signatures of interest. The spliced count matrix for the 6,418 retained cells was normalized to sum to 10,000 counts per cell, then transformed with log1p. The top 2,000 most highly variable genes were identified using `scanpy.pp.highly_variable_genes` on spliced matrices with minimum mean of 0.0125, maximum mean of 3, and minimum dispersion of 0.5 [186]. Spliced and unspliced matrices were subset to include only the 2,000 identified highly variable genes, then concatenated along the cell axis in the order unspliced, spliced to produce a count matrix of size 6,418 by 4,000.

### **Fitting Allen sample B08**

We applied _biVI_ with the three generative models (bursty, constitutive, and extrinsic) and _scVI_ with negative binomial likelihoods to the concatenated unspliced and spliced count matrix obtained by the filtering procedures outlined above. We made the key assumption that unspliced and spliced counts could be treated as the nascent and mature species of the bursty generative model (see discussion in Supplementary information under ‘Connecting the models to transcriptome data’ of [47]). 4,622 cells were used for training with 513 validation cells, and 1,283 cells were held out for testing performance. All models were trained for 400 epochs with a learning rate of 0.01. Encoders and decoder consisted of 3 layers of 128 nodes, and each model employed a latent dimension of 10. For each model, the loss was the Evidence

70

Lower Bound (ELBO) using a multivariate standard normal prior on the latent space as in standard _scVI_ and each described generative likelihood (bursty, constitutive, extrinsic for _biVI_ models and two independent negative binomial distributions for nascent and mature RNA for the _scVI_ model) as the likelihood term in the ELBO.

### **Bayes factor hypothesis testing for differential expression**

After fitting the VAE models, we sought to identify meaningful statistical differences that distinguish cell types. We excluded cell subclasses “L6 IT Car3,” “L5 ET,” “VLMC,” and “SMC” from this analysis, as they contained fewer than ten annotated cells and may require more sophisticated statistical models to account for small sample sizes. The following analysis thus considers 6,398 cells in 16 unique subclasses. We only computed differential expression metrics under the bursty model.

Differential parameter values were tested for each assigned subclass label (as annotated in [126]) versus all others using a Bayes factor hypothesis test following [149]. We reproduce Equations (18) - (21) of [149] below for clarity.

Estimating differential values of any parameter _𝜃_<sup>_𝑔_</sup> of gene _𝑔_ in cells _𝑎_ and _𝑏_ can be done according to the following Bayesian framework. First, as in Equation (18) of [149], the log fold change (LFC) of _𝜃_<sup>_𝑔_</sup> between two cells _𝑎_ and _𝑏_ can be calculated as follows:


Then, as in Equation (19) of [149], the probability that the magnitude of the LFC is greater than some effect threshold _𝑇_ can be found by evaluating LFC<sup>_𝑔_</sup> _𝑎,𝑏_<sup>over the</sup> posterior distributions of each cell:


where, in practice, the integral is approximated with many Monte Carlo samples from the two cells’ posteriors. Two hypotheses are tested: _𝐻_ 1, or that the magnitude of the LFC is greater than or equal to threshold _𝑇_ , and _𝐻_ 0, or the null hypothesis that the magnitude of the LFC is less than _𝑇_ . A Bayes factor for gene _𝑔_ between cells _𝑎_ and _𝑏_ ( _𝐵𝐹𝑎,𝑏_<sup>_𝑔_)iscalculatedtocomparethetwohypotheses,asinEquation</sup> (20) of [149]:

71


Extending this to test differential expression between two groups of cells _𝐴_ and _𝐵_ amounts to “aggregating the posterior,” as in Equation (21) of [149], or evaluating the same _𝑃_ (|LFC<sup>_𝑔_</sup> _𝐴,𝐵_<sup>|≥</sup><sup>_𝑇_∥</sup><sup>_𝐴, 𝐵_) over</sup>


In other words, a random sample _𝑧𝑎_ can be be taken from the approximate posterior of any cell belonging to group _𝐴_ and decoded to produce parameter _𝜃𝑎_<sup>_𝑔_; likewise a</sup> random sample _𝑧𝑏_ can be taken from the approximate posterior of any cell belonging to group _𝐵_ and decoded to produce parameter _𝜃𝑎_<sup>_𝑏_.</sup> The LFC between the two parameters can then be calculated. Repeating this for many Monte Carlo samples over the aggregate posteriors allows estimation of the Bayes factor between two groups.

For the results shown in Figure 5.1, we used cutoffs of _𝑇_ ≥ 1 _._ 0, or a magnitude LFC of ≥ 2, and a Bayes factor threshold of 1.5. The Bayes factors were calculated on normalized burst size and means for _biVI_ , i.e., the fractional inferred burst size or inferred means (before scaling by sampled sequencing depth for that cell), and normalized means for _scVI_ . This controlled for differences in parameters due to sequencing depth that were not biologically meaningful. Relative degradation rate _𝛾_ / _𝑘_ is independent of sequencing depth: hypothesis tests were performed directly on inferred relative degradation rates. While batch identity can also be integrated over to compare groups of cells from different batches, our analysis did not require this as all cells were from the same batch.

### **Reconstructing gene distributions**

Let _𝜃𝜅𝑔_ be mechanistic model parameters for gene _𝑔_ in cell type _𝜅_ . In simulated data, and for consistency, let us assume it to be true of biological cell types, gene parameters are the same for all cells across a cell type, _biVI_ and _scVI_ infer unique parameters for every cell and gene: _𝜃𝑐𝑔_ , where _𝑐_ indexes over cells and _𝑔_ indexes over genes. To reconstruct distributions for a given gene in a specific cell type _𝜅_ , we sample once from the posterior distribution _𝑞𝑐_ ( _𝑧_ ) of each cell _𝑐_ ∈ _𝜅_ to obtain point-estimates of conditional parameters _𝜃𝑐𝜅 𝑔_ , where conditional refers to a single

72

sampling from a cell’s posterior, or a particular realization of _𝑧𝑐_ . We then average over the cell-specific conditional probabilities for the gene to produce a cell type marginal distribution:


where _𝑛𝜅_ is the total number of cells in cell type _𝜅_ , and _𝑐𝜅_ indexes over all cells in that cell type. This identity follows immediately from defining the cell type’s distribution as the mixture of the distributions of its constituent cells. In the case of _biVI_ , we plug in Equation 5.7, 5.11, or 5.13 for _𝑃_ ( _𝑛, 𝑚_ ; _𝜃𝑐𝜅 𝑔_ ). In the case of _scVI_ , we use a product of two independent negative binomial laws:


where _𝜇𝑁_ and _𝜇𝑀_ are cell- and gene-specific, whereas _𝛼_<sup>_𝑁_</sup> and _𝛼_<sup>_𝑀_</sup> are fit separately and take on different values. For simplicity, this comparison omits uncertainty associated with _𝜃𝑐𝑔_ , which is formally inherited from the uncertainty in the latent representation _𝑧_ for each cell _𝑐_ .

Thus, Equation 5.21 is an approximation to the posterior predictive distribution, or marginal distribution of data given the approximated posterior, if we assume Monte Carlo sampling from the approximate posterior distributions of cells within that cell type as a reasonable proxy for sampling from the cell type’s posterior distribution. The posterior predictive, or marginal, distribution is:


where _𝑞_ ( _𝑧_ ) is the approximate posterior. We further note that conditional data likelihood and the marginal distribution are _not_ necessarily of the same form (for example, if the conditional data likelihood distribution is negative binomial, the marginal distribution of genes is not necessarily negative binomial).

73

_C h a p t e r 6_

---

[← NEURAL APPROXIMATIONS FOR INTRACTABLE BIOPHYSICAL MODELS](09-neural-approximations-for-intractable-biophysical-models.md) · [Up: contents](index.md) · [DISENTANGLING CIS AND TRANS GENE REGULATION →](11-disentangling-cis-and-trans-gene-regulation.md)
