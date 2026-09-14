---
title: SNAPSHOT INFERENCE
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# SNAPSHOT INFERENCE

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Technology does everything possible so that we lose sight of the chain of cause and effect.

_Turning Back the Clock: Hot Wars and Media Populism_ Umberto Eco

**This chapter is essentially complete, but I will need to ensure that the literature review is up to date.**

### **6.1 Critical analysis of RNA velocity**

This section summarizes the content of [112] by G.G., M.F., T.C., and L.P. The critique was conceptualized by G.G. and L.P. and implemented by G.G., M.F., and T.C.

The method of _RNA velocity_ [168] aims to infer directed differentiation trajectories from snapshot single-cell transcriptomic data. Although we cannot observe the transcription rate, we can count molecules of spliced and unspliced mRNA. The unspliced mRNA content is a leading indicator of spliced mRNA, meaning that it is a predictor of the spliced mRNA content in the cell’s near future. This causal relationship can be usefully exploited to identify directions of differentiation pathways without prior information about cell type relationships: “depletion” of nascent RNA suggests the gene is downregulated, whereas “accumulation” suggests it is upregulated. This qualitative premise has profound implications for the analysis of scRNA-seq data. The experimentally observed transcriptome is a snapshot of a biological process. By carefully combining snapshot data with a causal model, it is for the first time possible to reconstruct the dynamics and direction of this process without prior knowledge or dedicated experiments.

The bioinformatics field has recognized this potential, widely adopting the method and generating numerous variations on the theme. The roots of the theoretical approach date to 2011 [326], but the two most popular implementations for scRNA-seq were released in 2017–2018: _velocyto_ by La Manno et al. [168], which introduced the method, and _scVelo_ by Bergen et al. [29], which extended it to fit a more sophisticated dynamical model. Aside from these packages, a dizzying variety of auxiliary

70

methods and extensions have been developed [13, 41, 63, 77, 120, 130, 135, 171, 175, 183, 192, 229, 246, 249, 281, 311, 314, 330, 331] to incorporate additional modalities, build more complex dynamical and statistical models, and construct lowdimensional visualizations. This profusion of computational extensions has been accompanied by a much smaller volume of analytical work, including discussions of potential extensions and pitfalls [30, 50, 275, 291], as well as theoretical studies based on optimal transport [173, 329] and stochastic differential equations [178]. However, at their core, these auxiliary methods are built on top of the theory and code base from _velocyto_ or _scVelo_ .

Despite the popularity of RNA velocity [264, 311] and increasingly sophisticated attempts to combine it with more traditional methods for trajectory inference [171, 330], there has been little comprehensive investigation of the modeling assumptions that underlie the seemingly simple user-facing workflow (Figure 6.1a-b). The few dedicated critiques to date have largely focused on limitations of the inference and embedding steps [30, 192, 333], without questioning the foundational assumptions. This is an impediment to applying, interpreting, and refining the methods, as problems arise even in the simplest cases. Consider, for example, the result displayed in Figure 6.1b, where the outputs of the two most popular RNA velocity programs applied to exemplar human embryonic forebrain data [168] are qualitatively different. The inferred directions in the example should recapitulate a known differentiation trajectory from radial glia to mature neurons. However, _scVelo_ , which “generalizes” _velocyto_ , fails to identify, and even reverses the trajectory, suggesting totally different causal relationships between cell types. This type of problematic result has been reported elsewhere [29, 30, 120, 171, 175, 231], and typically used to motivate the development of new implementations. Nevertheless, the methods have produced plausible trajectories in biological studies [26, 61, 117, 126, 147, 182, 263, 317, 324], suggesting that they can identify _something_ nontrivial about the underlying signal.

Motivated by such discrepancies, we systematically investigated the method’s theoretical foundations, assumptions, and implementations, using a combination of simulated and biological datasets. The RNA velocity procedure combines numerous steps of data processing, reviewed in Section 6.1.1. Some are justified under a particular, very restrictive, physical model of transcription, whereas others are purely _ad hoc_ . We conclude that the variable performance is, in large part, an intrinsic consequence of incompatibility between these two worldviews. An _ad hoc_

71

data transformation assumes some system dynamics or distributional form, which are generally incompatible with the physical model. Occasionally, the assumptions approximately hold, yielding results consistent with known biology. However, it is _a priori_ impossible to predict whether they hold. The presence of somewhat arbitrary tunable hyperparameters at each step of the analysis provides an opportunity for confirmation bias to overrule the data, exacerbating the reliability problems.

### **6.1.1 Brief review of RNA velocity**

To characterize the challenges, we briefly outline the steps of a typical velocity workflow. First, raw reads are converted to unspliced (nascent) and spliced (mature) RNA count matrices, based on the presence or absence of intronic content. After the usual filtering and normalization steps, the mature count matrix is projected to a lower-dimensional space with principal component analysis (PCA). This projection is used to construct a nearest-neighbor graph over cells, and “impute” the data matrices by replacing each cell’s normalized counts with the average of its neighbors’ values. In other words, the preliminary data processing effects a transformation _𝑥𝑖_ → _𝑦𝑖_ , where _𝑥𝑖_ is discrete and _𝑦𝑖_ is continuous. Then, the following model is instantiated:


The functional form of _𝛼_ ( _𝑡_ ) is not precisely specified. _velocyto_ assumes that _𝛼_ ( _𝑡_ ) has fairly generic dynamics, but evolves slowly enough relative to _𝛽_ and _𝛾_ to produce identifiable near-equilibrium high-expression and low-expression states. _scVelo_ relaxes the assumption of equilibrium, but restricts the dynamics of _𝛼_ ( _𝑡_ ) to a much simpler function with a single step increase and decrease. In addition, the precise meaning of _𝑦𝑖_ differs by source: _velocyto_ treats it as _𝜇𝑖_ , such that _𝑥𝑖_ is drawn from a Poisson distribution with mean _𝜇𝑖_ , whereas _scVelo_ treats it as a true _𝑦𝑡_ , a continuous quantity that happens to be corrupted by isotropic noise.

Regardless of the interpretation, the following identity holds:


This time derivative is the “RNA velocity,” the rate of change of the mature RNA abundance. By fitting a model — either extracting the _𝑦𝑁 , 𝑦 𝑀_ values at equilibria and fitting a line ( _velocyto_ ), or using all of the data and fitting a curve ( _scVelo_ ) — it is possible to identify _𝛾_ / _𝛽_ and compute instantaneous velocity values for each cell.

72


Figure 6.1: The RNA velocity workflow and its limitations. **a.** A summary of the user-facing components of a typical RNA velocity workflow. Initial processing of sequencing reads produces nascent and mature counts for every cell, across all genes. Inference procedures fit a model of transcription and predict cell-level velocities, ascribing accumulation or depletion of RNA to induction or repression of the transcriptional driver (visualizations adapted from [129], forebrain data from [168]).

**b.** At the final stage of the workflows, cell and embedding velocities are displayed in the top two principal component dimensions, but different software implementations may disagree.

**c.** Smoothing and imputation introduce distortions into the simulated data, and do not recapitulate the simulated ground truth process average _𝜇𝑁_ .

**d.** Normalization and dimensionality reduction distort local cell neighborhood identities (eCDF: empirical cumulative distribution function; Jaccard distance: Equation 3.50, lower is better).

**e.** The nonlinear UMAP embedding distorts the global cell type structure, separating cell types along a continuous trajectory.

**f.** Nonlinear transformations and modulation of neighborhood sizes introduce distortions in the arrow directions with respect to the simplest PCA projection (histograms: distribution of cell-specific angle deviations under different pooling neighborhood sizes).

**g.** Nonlinear embeddings of cell-specific velocities into PCA space, computed from simulated data, do not appear to substantially change if only the velocity signs are used.

**h.** If a parametric fit to the dataset is available, it can be summarized by projecting the inferred time-dependent process average into a low-dimensional space.

73

Next, the velocity values are summarized in a low-dimensional representation. An embedding is constructed from the PCA projection, and each cell’s neighbors in that embedding are identified. The low-dimensional “direction” of the mature transcriptome is computed by calculating the degree of alignment between the RNA velocity of each cell and the directions to its embedding neighbors by passing these quantities through a kernel function. Finally, a low-dimensional, cell-specific velocity vector is produced by averaging the directions to the neighbors.

### **6.1.2 The velocity dynamical model is unphysical**

The procedure ultimately relies on the transformation from _𝑥𝑖_ to _𝑦𝑖_ producing a quantity that follows Equation 6.2. This premise is merely asserted, never proven or quantitatively tested by the method developers, and fails on five levels.

The transformation is not theoretically founded. There is no particular reason to believe that averaging over neighbors should eliminate biological or technical stochasticity. In addition, the _space_ used to identify the nearest neighbors is constructed from the data, and incorporates its noise sources. The premise of obtaining a better estimate by aggregating noisy data is superficially plausible; for example, such “local averages” are ubiquitous in time series analysis, including transcriptomics [102]. However, a data-based projection is not an externally determined experiment time, and the imputation of data is fundamentally circular in a way that a moving average is not. These, and other, pitfalls of imputation have been characterized elsewhere [10], and we describe further theoretical issues in Section B.3.

Regardless of its theoretical basis, the transformation does not actually accomplish its goals. Even in the best-case scenario, in discrete simulated data generated from a model that matches the _velocyto_ assumptions, with no normalization needed, the procedure only recapitulates the true expectation _𝜇𝑀_ on average, and is unreliable for any specific cell (Figure 6.1c). The performance is particularly poor for cells that are strongly out of equilibrium, i.e., those of the most interest for the procedure. The alternative continuous model is inappropriate and unphysical. Although continuous approximations are reasonable in the high-concentration regime, typical scRNA-seq experiments have very low copy numbers across the genome; for the vast majority of genes, only a small fraction of cells have nonzero RNA counts. This regime contradicts the assumptions of the approximations. Making matters worse, the additive noise term used for this model in _scVelo_ does not even match the multiplicative, abundance-dependent noise term that emerges from typical approx-

74

### imations [100].

Even if we adopt the discrete model with instantaneous Poisson noise, we contradict numerous sources that suggest transcriptional activity varies with time even in stationary cell populations [16, 65, 161, 172, 205, 210, 233, 239, 244], and is effectively described by a telegraph model that stochastically switches between active and inactive states [218, 219]. Although it is possible that certain genes key to transient differentiation and development processes exhibit time-varying constitutive transcription, using this assumption to fit thousands of genes is questionable. Therefore, some variant of the bursty model appears more physically founded.

Finally, these concerns, which collectively motivate using a statistically and physically appropriate _𝑃_ ( **x** _, 𝑡_ ), lead us to a more fundamental question: _which 𝑡_ ? In other words, we _a priori_ know that scRNA-seq datasets are snapshots, and contain cells “earlier” and “later” in the differentiation process. Previous reports reasonably assume that _𝑡_ varies between cells, but do not propose a mechanism to explain how simultaneously collected cells can reside at different times along a process.

The range of these omissions and problems fundamentally speaks to an uneasy compromise between the descriptive and mechanistic worldviews, described in more detail in Section 2.1. Although RNA velocity uses the language of stochastic biophysics, its underlying assumptions, obscured by the user-friendly software and informal, equivocal theory, have a complex and often contradictory relationship with well-attested physical phenomena.

### **6.1.3 The embedding procedure is unreliable**

Even outside the context of RNA velocity, linear as well as nonlinear embeddings distort local and global data relationships or suggest new ones not present in the underlying data (cf. Section 8.4 and [49, 58]). Nonlinear embeddings utilize sensitive hyperparameters that can be tuned, but do not provide well-defined criteria for an “optimal” choice [58, 162]. Tuning algorithm parameters can slightly improve some distortion metrics, though often at the expense of others [162]. In Figure 6.1d, we demonstrate the neighborhood preservation behavior of transformations used to construct low-dimensional embeddings. By the time the data have been summarized a two-dimensional embedding (gold and yellow lines), some 70–80% of the neighborhood relationships have been lost on average, largely in the initial normalization step (red line). In addition to these local distortions, which put into question the computation of directions to embedding neighbors, global distortions can occur. In

75

Figure 6.1e, we illustrate this point with a Uniform Manifold Approximation and Projection (UMAP) projection of the forebrain dataset, which introduces discontinuities between cell types (cf. Figure 6.1a-b). In other words, if the projection itself erases cell type relationships, RNA velocity cannot recover them.

The procedure for embedding RNA velocity in a two-dimensional space introduces further challenges, which are challenging to deconvolve. Beyond the mismatch in neighborhoods, the directions produced by the kernel-based procedure in the PCA space do not align with directions obtained by simply projecting the cell-specific velocity vectors (distribution of angle deviations shown in Figure 6.1f). Most strikingly, the embedding procedure appears to eliminate nearly all of the quantitative information obtained by the inference and velocity computation procedures: as shown using simulated data in Figure 6.1g, the results obtained using the standard _velocyto_ kernel are nearly identical to those obtained using a custom kernel that only uses the signs of the direction and velocity vectors. Finally, the “Markov chains” over cells generated by the procedure are _ad hoc_ and not motivated by any particular model of physiology; as discussed in full detail in Section B.4, they implicitly contradict the mechanism used to perform inference.

### **6.1.4 Conclusions**

The standard RNA velocity framework presupposes that the evolution of every gene’s transcriptional activity throughout a differentiation transient process can be described by a continuous model. It proceeds to normalize and smooth the data until the rough edges of single-molecule noise are filed off, and fits a continuous model of transcription and turnover assuming Gaussian residuals.

In the process, the stochastic dynamics that predominate in the low-copy number regime, and that characterize nearly all of mammalian transcription, are lost and cannot be recovered. Although parameters can be fit, they are distorted to an unknown extent, due to a combination of data transformation, suboptimal inference, and model misspecification. In _scVelo_ , parameters are estimated under a highly restrictive model, yet applied to make broad claims about complex topologies. In _velocyto_ , only the sign of the velocity is physically interpretable; if we discard everything else, we still obtain fairly consistent results, suggesting that the method fails to fully utilize valuable quantitative information. Finally, the embedding process, which produces human-interpretable visualizations, is not based on biophysics, and is not guaranteed to be stable or robust.

76

Nevertheless, sometimes RNA velocity works, and produces results consistent with biological intuition and orthogonal data. From the review above, the performance appears to rely on a combination of factors. First, the “signal” needs to be strong enough that the flaws in the dynamical model can be sufficiently “smoothed out” by the data processing. Second, the cell embedding needs to be faithful enough to recapitulate the features of interest. Third, the velocity embedding procedure needs to produce approximately correct results. These conditions are by no means guaranteed, and fair performance in any particular case may be attributable to hyperparameter tuning and confirmation bias. Therefore, the workflow does not yet appear to be sufficiently reliable to be used for biological discovery.

77

### **6.2 Self-consistent snapshot inference**

This section unifies portions of [112] by G.G., M.F., T.C., and L.P., as well as [115] by G.G., J.J.V., and L.P. G.G., M.F., and L.P. conceptualized the theoretical alternatives to RNA velocity. G.G. conceptualized, designed, and implemented the case study shown here.

_Is there no balm in Gilead?_ Given the foundational issues we have raised, how can the RNA velocity framework be reformulated to provide meaningful, biophysically interpretable insights? Fortunately, the natural match between stochastic models and UMI-aided molecule counting offers hope for quantitative and interpretable trajectory inference. We propose that discrete Markov modeling can directly and naturally address the fundamental issues. In particular, transient and stationary physiological models can be defined and solved via the approach in Chapter 4, which describes the time evolution of a discrete stochastic process. Since the “noise” is the data of interest, smoothing is not required. Rather, technical and extrinsic noise sources can be treated as stochastic processes in their own right, and explicit modeling of them can improve the understanding of batch and heterogeneity effects. Finally, within this framework, parameters can be inferred using standard and well-developed statistical machinery. Once these parameters are available — and only then — we may optionally summarize the findings in terms of typical low-dimensional visualizations, as with our visualization of the projection of the true _𝜇𝑀_ in Figure 6.1h.

The inference of transient dynamics from snapshot data is a formidable problem due to a combination of theoretical and practical factors. Most fundamentally, it is not precisely clear what a snapshot _is_ : how does a single measurement simultaneously capture the early and late states in a differentiation process? To develop an explanatory model, we take inspiration from the existing work on cyclostationary processes [66, 67], cell cycle ensemble measurement modeling [28, 220, 282], Markov chain occupation measure theory [167, 225, 320], and chemical reactor engineering [88, 237]. In the typical stochastic modeling context, we fit count data using stationary distributions _𝑃_ ( **x** ), obtained as the limit lim _𝑡_ →∞ _𝑃_ ( **x** _, 𝑡_ ) of a transient distribution. By the ergodic theorem [95], this distribution, when it exists, coincides with the occupation measure lim _𝑇_ →∞ _𝑇_<sup><u>1</u></sup> ∫0 _𝑇_<sup>_𝑃_(</sup><sup>**x**</sup><sup>_, 𝑡_)</sup><sup>_𝑑𝑡_,i.e.,observations</sup> drawn from a single trajectory over a sufficiently long time horizon, rather than from multiple trajectories at once. Conveniently, the ergodic limit has time symmetry with respect to measurement: the distribution does not depend on the timing of the experiment. In the transient case, we cannot take these limits. However, we _can_ retain time symmetry by proposing that the experiment samples cells at almost

78

surely finite times _𝑡_ since the beginning of the process. Therefore, we conceptualize data as coming from a set of independent cells, such that each cell’s time _𝑡_ c is sampled from _𝑓_ ( _𝑡_ ), and counts are drawn from some distribution _𝑃_ ( **x** _, 𝑡_ c)<sup>4</sup> . To fit a set of data, we need to specify and motivate the distribution _𝑓_ .

We illustrate some of the challenges and implications of this framework using the model system shown at the bottom of Figure 6.2a. The underlying transient structure involves transitions through three cell types, each characterized by a particular transcriptional burst size. This model is more realistic but less tractable than the constitutive model implied by RNA velocity. The transient transcription process produces nascent and mature RNA trajectories for each cell; however, we only obtain a single data point per trajectory. Formally, to infer the parameters, we simultaneously need to find Θ, the biological parameters, as well as _𝑡_ c, all of the cell times. The full data likelihood for a single gene takes the following form:


where we obtain the second line by marginalizing over { _𝑡_ c}. If multiple genes are present, but their transcriptional events are not synchronized, _𝑃_ can be decomposed into the product of gene-specific probabilities (Section 10.1). The integral is intractable. Several approaches are available. First, we can reframe the problem as a combinatorial optimization. In this case, we can define an ordering of cell times _𝜎_ , approximate the continuous distribution _𝑓_ by a uniform-weight discrete distribution placed at Nc quantiles _𝑡_ c<sup>∗, and perform the following combinatorial optimization:</sup>


As Nc grows, the quantile approximation to _𝑓_ improves. However, the combinatorial optimization becomes rather challenging, as its complexity grows exponentially in Nc. Therefore, a more practical approach may involve the expectation–maximization (EM) algorithm. Such an implementation would iterate between updating the parameter estimate Θ<sup>ˆ</sup> and cell-specific time distributions _𝑓_ c, defined over a discrete grid [64, 70].

Nevertheless, even this approach requires some careful theoretical work and simulated benchmarking. Even if we have perfect information about the cell times, it is far from clear that we can accurately reconstruct the transcriptional dynamics from

79

snapshot data (center of Figure 6.2a). This question is essential, as it controls our ability to compute estimates Θ<sup>ˆ</sup> in a given EM step.

In addition, we wish to know whether we can identify the _mechanism_ of the snapshot collection. We can imagine cells entering and exiting the observed tissue in multiple ways, which correspond to different choices of _𝑓_ ( _𝑡_ ). Some natural choices are uniform, which implies the cells stay in the tissue for a deterministic time [168]; decreasing over time, so cells can exit immediately; or uniform, then decreasing, so cells must stay in the tissue for some duration but are free to leave afterward. These choices can be modeled by Dirac, exponential, and Pareto residence distributions. In the parlance of chemical reactor engineering, these configurations are known as the plug flow reactor (PFR), the continuously-stirred tank reactor (CSTR), and the laminar flow reactor (LFR), respectively. Their _𝑓_ ( _𝑡_ ), which are the reactor internalage distributions, are well-known in the chemical engineering literature [88, 237], and shown at the top of Figure 6.2a. It is not _a priori_ obvious the configurations are mutually distinguishable from count data. If they are not, the choice of _𝑓_ ( _𝑡_ ) is immaterial for inference.

We generated snapshot data from the PFR model and fit it under all three models. To efficiently evaluate snapshot distributions, we designed an algorithm which essentially “recycles” _𝑡_ c for trapezoidal quadrature. As shown in Figure 6.2b, despite only having access to a single observation per time point, all models yield results visually close to the true marginals. However, despite these superficial similarities, quantitative model identification is possible. To quantify identifiability, we use the Akaike weight _𝑤𝜛_ (Equation 3.48), which transforms log-likelihood differences into model probabilities [38]. For example, if all Akaike weights are near 1/3, the models are indistinguishable; if the correct model’s weight is near 1, we can confidently identify the model from the data. For the simulated dataset shown, the true PFR model achieves an Akaike weight of _𝑤𝜛_ ≈ 79%, whereas the CSTR and LFR both achieve ≈ 10%. Decreasing the dataset size substantially degrades the identifiability. Even at higher sizes, spread is considerable; for example, a 150-cell dataset gives approximately even odds ( _𝑤𝜛 >_ 1/2) _on average_ , but individual realizations vary from confidently correct ( _𝑤𝜛_ ≈ 1) to confidently wrong ( _𝑤𝜛_ ≈ 0).

To understand the robustness of model identifiability, we generated synthetic datasets at random parameter values, constrained to have fairly low expression. We observed poor identifiability, with even or better odds for the correct model in only 20% of the cases (Figure 6.2d). This performance appears to be attributable to quantitative

80


Figure 6.2: The inference of biophysical parameters and reactor configurations from snapshot data.

**b.** In spite of the considerable differences between the reactor architectures, they produce nearly identical molecular count marginals (histogram: data simulated from the PFR model, 200 cells; colored lines: analytical distributions at the maximum likelihood transcriptional parameter fits for each of the three reactor models. Analytical distributions nearly overlap).

**a.** A minimal model that accounts for the observation of transient differentiation processes in scRNA-seq: cells enter a “reactor” and receive a signal to begin transitioning from cell type A through B and to C. The change in cell type is accompanied by a step change in the burst size, which leads to variation in the nascent and mature RNA copy numbers over time. Given information about the cell type abundances and the cells’ time along the process, we may fit a dynamic process to snapshot data and attempt to identify the underlying reactor type, which determines the probability of observing a cell at a particular time since the beginning of the process.

**c.** The true reactor model may be identified from molecule count data, but statistical performance is typically poor (points: Akaike weight values for _𝑛_ = 50 independent rounds of simulation and inference under a single set of parameters; blue markers and vertical lines: mean and standard deviation at each number of cells; blue line connects markers to summarize the trends; red lines: the Akaike weight values 1/3, which contains no information for model selection, and 1/2, which gives even odds for the correct model; two-species data generated from the PFR model; uniform horizontal jitter added).

**d.** The reactor models are poorly identifiable across a range of parameters, and rarely produce Akaike weights above 1/2 (histogram: Akaike weight values for _𝑛_ = 200 independent rounds of parameter generation, simulation, and inference under the true PFR model; red line: the Akaike weight values 1/3 and 1/2; two-species data for 200 cells generated from the PFR model).

**e.** The challenges in reaction identification arise because all three models produce similar likelihoods (histograms: likelihood differences between candidate models and the true PFR model for _𝑛_ = 200 independent rounds of parameter generation, simulation, and inference; red line: no likelihood difference; two-species data for 200 cells generated from the PFR model).

81

similarities between all three models’ likelihoods. As shown in Figure 6.2e, given data of this quality, we cannot even narrow the scope down to two models, as neither of the candidate models performs conspicuously worse than the true PFR configuration. Therefore, it is possible to fit snapshot data approximately equally well using a variety of models; candidates for _𝑓_ ( _𝑡_ ) are identifiable _in principle_ , but challenging to distinguish from any particular dataset. This simulated analysis implies that the details of the reactor configuration may not matter much, providing a basis for omitting this model identification problem for real data.

82

_C h a p t e r 7_

---

[← COMPUTATIONAL CONSIDERATIONS](12-computational-considerations.md) · [Up: contents](index.md) · [MODEL IDENTIFICATION AND SELECTION →](14-model-identification-and-selection.md)
