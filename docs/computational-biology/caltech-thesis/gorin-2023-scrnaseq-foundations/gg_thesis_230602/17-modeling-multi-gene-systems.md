---
title: MODELING MULTI-GENE SYSTEMS
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MODELING MULTI-GENE SYSTEMS

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **10.1 Key** **<u>goals and context</u>**

This section summarizes a portion of [115] by G.G., J.J.V. and L.P. The analysis was conceptualized, designed, and implemented by G.G. The models proposed originate from [112] by G.G., M.F., T.C., and L.P., [105] by G.G. and L.P., [44] by M.C.<sup>_★_</sup> , G.G.<sup>_★_</sup> , Y.C., T.C., and L.P., [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P., and unpublished research undertaken by C.F. and G.G.

In Chapters 8 and 9, we have shown that fitting fairly simple, two-species models can provide some insight into the biophysics of transcription and the chemistry of single-cell sequencing. However, throughout the process, we have essentially focused on statistically homogeneous populations, treating cells as independent and identically distributed draws from a common distribution and treating the genes as independent. As discussed in Section 5.4, this approach omits all gene–gene relationships by design, and breaks with standard analyses, which use these relationships to characterize dataset structure [187].

For a multitude of reasons, we cannot build a comprehensive model using the tools in Chapter 4. To do so, we would need to explicitly represent regulation, which is excluded from these models (as discussed in Section 4.3.1). In addition, regulation typically proceeds through protein signaling cascades; as we do not have protein data, a regulation model would be woefully underdetermined for a sequencing assay. The construction, parametrization, and inference of such models falls under the purview of the whole-cell modeling and systems biology fields [260, 269, 303]. We anticipate that a full synthesis of systems biology, bioinformatics, and stochastic biophysics, if not altogether futile, will require some decades of interdisciplinary work.

Nevertheless, certain kinds of co-regulation _can_ be represented in this framework. To leverage the master equation models outlined in Chapter 4 to describe correlations between genes, we need to specify how upstream interactions lead to co-expression. As the simplest illustrative model system, we can consider the co-regulation of two genes, indexed by _𝑗_ , with _𝑈 𝑗_ = _𝑢 𝑗 𝑒_<sup>−</sup><sup>_𝛾𝑗_s</sup> . We outline several relatively simple classes of candidate models which induce expression coupling.

118

In the simplest case, H ( **u** _, 𝑡_ ) =<sup>�</sup> _𝑗_<sup>H</sup> _𝑗_<sup>(</sup><sup>_𝑢_</sup> _𝑗_<sup>_, 𝑡_).In other words, the genes’ dynamics</sup> are fully separable, and produce solutions in the form _𝐺_ ( **u** _, 𝑡_ ) =<sup>�</sup> _𝑗_<sup>_𝐺_</sup> _𝑗_<sup>(</sup><sup>_𝑢_</sup> _𝑗_<sup>_, 𝑡_).</sup> This formulation produces independent distributions at each _𝑡_ , but the _trajectories_ may possess nontrivial statistical relationships. For example, if both genes start at _𝑥_ 1 = _𝑥_ 2 = 0, their trajectories will be correlated over a finite timespan [0 _,𝑇_ ], with the correlation decaying as _𝑇_ →∞. This is the model implicit in the RNA velocity framework (Chapter 6). Therefore, this model class ascribes gene–gene relationships to transient phenomena, but cannot produce nontrivial stationary correlations.

In the next simplest case, co-regulation is the consequence of parameter differences in subpopulations. For example, the full cell population may consist of cell types indexed by _𝜅_ . If we suppose each cell type has the abundance _𝜋𝜅_ and transcriptional parameters Θ _𝜅_ , we yield


i.e., the generating function decomposes into a product of independent generating functions _conditional on_ a particular cell type, but not globally. In other words, even if transcriptional processes are independent, cell type structure can produce nontrivial relationships between genes. However, this model cannot produce correlations _within_ a cell type.

Equation 10.1 is immediately recognizable as the special discrete case of a more general mixture model:


In other words, the cell types do not have to be point masses: the variation of parameters throughout the cell population may well be continuous, with higher- _𝑓_ Θ regions corresponding to “cell states.” This is the model implicit in the _scVI_ variational autoencoder framework [185].

Alternatively, we can propose a model of co-regulation by the categorical variables. For example, two neighboring genes may prefer to have the same or opposite accessibility, depending on the polymeric properties of DNA. Assuming, for the purposes of illustration, that the system is symmetric, we yield the following _𝑁_ = 4

119

### form:

_𝑠_ ∈{both off _,_ gene 1 on _,_ gene 2 on _,_ both on}


This form encodes the co-regulation of two genes. If _𝜀_ ≪ 1, the intermediate states are unstable and the genes tend to be either both on or both off. If _𝜀_ ≫ 1, the intermediate states are particularly stable, and only one of the genes tends to be on at a time. If _𝜀_ = 1, we recover the independent case.

We can define a similar model for co-regulation by a continuous variable _𝑦_ 1, as an extension of Chapter 7.2 or the paired activation motif discussed in [205]. For example, there may be a latent regulator, such as the concentration of an activator, that controls multiple loci: if it is high, both have a high transcription rate; otherwise, both are inactive. This amounts to appending the following reactions to the master equation:


where the _𝐶_<sup>_𝑐𝑑_</sup> matrix encodes the relationship between the concentration and the transcription rate. Therefore, the genes become mutually correlated through the trajectory of _𝑦_ 1, although the extent of correlation depends on the dynamics.

If the categorical or continuous driving process is bursty, we can approximate it by a co-bursting module. For example, in the limit of _𝜀_ → 0, the dynamics of the system in Equation 10.3 converge to the _𝑁_ = 2 formulation


If, in addition, _𝑘_ off<sup>∗</sup><sup>_, 𝑘_init→∞, we obtain the</sup><sup>_𝑁_= 1 module characterized by</sup>


120

where _𝑏_ := _𝑘_ init/ _𝑘_ off<sup>∗.This is the bursty limit of Equation 10.3, which possesses the</sup> more general form


where each transcription event produces _𝐵 𝑗_ molecules of X _𝑗_ , with _𝐵 𝑗_ drawn from a geometric distribution with mean _𝑏 𝑗_ . Due to the structure of the burst distribution, the different gene products’ burst sizes are correlated.

Interestingly, that mechanism also possesses a slow mixture limit. If _𝜀_ →∞ while _𝑘_ on _, 𝑘_ off → 0, we obtain a special case of Equation 10.1, with _𝜋𝜅_ = 1/2 and mutually exclusive expression in the “cell types,” or long-lived gene states.

Even when we restrict our analysis to simple feed-forward regulation, this outline of motifs is nowhere near exhaustive. Nevertheless, the “mixture” and “bursty” limits are particularly natural starting points, as their distributions are straightforward to construct. In other words, we speculate that the careful analysis of co-expression models can distinguish relationships due to “slow” variation between cell types and “fast” variation due to coupled transcriptional events.

### **10.2 Biophysical constraints on “fast” transcript–transcript covariation**

This section summarizes a portion of [105] by G.G. and L.P. The data analysis was conceptualized, designed, and implemented by G.G.

We cannot directly fit the “fast” variation models, as they are severely underspecified: we do not know _which_ genes are co-regulated in this fashion. However, we can treat certain closely related problems and use the functional form of Equation 10.7 to _constrain_ gene–gene relationships. In other words, although we cannot possibly fit all genes, if a particular pair of genes _were_ expressed in simultaneous bursts, their expression must meet certain constraints. It turns out that the correlation between the two species has the correlation coefficient


As the marginals are negative binomial, we could easily estimate _𝑏𝑖_ and _𝛾𝑖_ from the marginals, without having to fit the full distribution. Once we have these estimates, we could predict the correlation between the genes. Interestingly, this equation is invariant under Bernoulli technical noise, with _𝑝 𝑗 𝑏 𝑗_ taking the place of _𝑏 𝑗_ . Nevertheless, as the set of assumptions is fairly severe, Equation 10.8 should be

121

treated as the upper bound on correlation coefficients between genes for this model class, in the spirit of [137, 138]. If real genes routinely violate this upper bound, the co-bursting model is insufficient to describe the gene–gene relationships in the dataset, and other model components need to be invoked.

This class of models can also describe _intra_ -gene correlations. Specifically, a single “parent” transcript X0 can give rise to multiple downstream transcripts X _𝑗_ :


where the first line represents the bursty transcription of X0, the second encodes multiple splicing routes, and the third represents the degradation or isomerization to secondary transcript forms, which we do not consider. If all _𝛽 𝑗_ are high relative to all _𝛾 𝑗_ , the distribution of each X _𝑗_ is negative binomial with shape _𝛼_ / _𝛾 𝑗_ and scale _𝑏𝛽 𝑗_ / _𝛽_ , where _𝛽_ :=<sup>�</sup> _𝑗_<sup>_𝛽_</sup> _𝑗_<sup>is the total efflux rate from X</sup> 0<sup>.In addition, the correlation</sup> between any two transcripts is given by Equation 10.8, with _𝑏𝛽 𝑗_ / _𝛽_ taking the place of _𝑏 𝑗_ .

To understand whether real systems actually follow this bound on transcript– transcript correlations, we obtained data from the recent FLT-seq (full-length transcript sequencing by sampling) protocol [287], which uses nanopore technology to obtain long reads amenable to the identification of transient transcripts. As this experimental technique has molecular and cellular barcodes, the data are interpretable as discrete transcript counts sampled from a distribution. To minimize transient effects, such as cell cycling and differentiation, we selected a dataset generated from cultured mouse stem cells. To limit biological heterogeneity due to discrete cell subpopulations (as in Equation 10.1), we filtered for cell barcodes corresponding to the activated cell subset (136 barcodes) according to the authors’ annotations. In all downstream analyses, we treated this filtered dataset as biologically homogeneous up to endogenous stochasticity.

The FLT-seq protocol produces full-length reads, which can be used to discover new isoforms, but does not reveal causal relationships between those isoforms. Nevertheless, we can use the tools of discrete mathematics to partially infer these relationships. Splicing removes introns, but cannot insert them. We can use this relationship to constrain the splicing graph: if transcript X _𝑗_ can be obtained by removing part of the sequence in transcript X _𝑖_ , there must be a path from X _𝑖_ to X _𝑗_ .

122

On the other hand, if X _𝑖_ contains the sequence _𝐼𝑖_ but omits the sequence _𝐼 𝑗_ , whereas X _𝑗_ contains the sequence _𝐼 𝑗_ but omits the sequence _𝐼𝑖_ , the transcripts are _mutually exclusive_ and must be generated from the parent transcript by distinct pathways.

For each gene, we enumerate the transcripts observed in the data and split them into elementary intervals, contiguous stretches that are either present or absent in each transcript (denoted by the colors in Figure 10.1a). These elementary intervals constrain the relationships between transcripts, and we can use their presence or absence in each transcript to construct an accessibility graph. The internal structure of this graph is underspecified, but immaterial: the negative binomial model implied by the operator in Equation 10.7 describes the _roots_ , mutually exclusive transcripts that must be generated directly from the parent transcript (indicated in orange in Figure 10.1b). We fit the distributions of these roots, discarding any data that are underdispersed, overly sparse, or fail to converge to a fit. The satisfactory fits for the sample gene _Rpl13_ are shown in Figure 10.1c.

The negative binomial fit yields burst sizes _𝑏𝑖_ and non-dimensionalized efflux rates _𝛾𝑖_ . We substitute these quantities into Equation 10.8, compute hypothetical correlations _𝜌_ theo, and compare them to sample correlations _𝜌_ samp in Figure 10.1d. These results represent the 4,885 nontrivial correlation matrix entries between 1,978 transcripts from 500 genes. 302 transcripts were rejected due to underdispersion, 542 due to sparsity, and 100 due to poor fits. The theoretical constraint (sample correlation equal to or lower than predicted correlation) was met in 4,606 cases (94.3%).

The results suggest that the model is not sufficient to recapitulate the full dynamics, but _does_ provide an effective, and nontrivial, theoretical constraint. We hypothesize that the “consistent” regime ( _𝜌_ samp ∈(0 _, 𝜌_ theo), 3,856 entries) represents the degradation of correlations due to technical noise in the sequencing process and stochastic intermediates. The “inconsistent” regime ( _𝜌_ samp ∈( _𝜌_ theo _,_ 1), 279 entries) may stem from model misidentification, and could be explained by coupling between splicing events. Some of these apparently inconsistent correlations may also be due to the small sample sizes, as the bootstrap 95% confidence intervals only rarely lie outside the theoretical bound (29 entries). Finally, the “negative” regime ( _𝜌_ samp _<_ 0, 750 entries) technically meets the constraint, but cannot actually be reproduced by the model. This does not appear to be an artifact of sample sizes. Instead, we speculate that enrichment in negative correlations is the signature of a more complicated regulatory schema which preferentially synthesizes some isoforms to the exclusion of others, rather than choosing the splicing pathway randomly.

123


Figure 10.1: The synchronized-burst model can be leveraged to constrain transcripttranscript correlations.

**a.** By inspecting exon co-expression structures in long-read sequencing data, we can split genes into elementary intervals.

**b.** Although sequencing data are not sufficient to identify the relationships between various transcripts, they can provide information about “roots” of the splicing graph (highlighted in orange), which must be produced from the parent transcript by mutually exclusive pathways.

**c.** The root transcript copy number distributions are well-described by negative binomial laws (gray histograms: raw marginal count data; red lines: fits).

**d.** The co-bursting model is not sufficient to accurately predict transcript-transcript correlations, but does serve as a nontrivial upper bound: few sample correlations exceed the model-based predictions obtained from Equation 10.8 (points: transcript-transcript correlation matrix entries for mutually exclusive “root” transcripts of a single gene; error bars: bootstrap 95% confidence intervals; red line: theory/experiment identity line).

**e.** The highest-expressed transcripts across the top 500 genes show distinctive, and generally positive, correlation patterns.

**f.** We can use an analogous model to predict and reconstruct the gene–gene correlation matrix based solely on marginal data.

**g.** As before, the model is not sufficient to accurately predict gene–gene correlations, but provides an effective and nontrivial upper bound (points: gene–gene correlation matrix entries; error bars: bootstrap 95% confidence intervals; red line: theory/experiment identity line).

124

Analogously, we can exploit the inter-gene model encoded in Equation 10.7 to predict the gene-gene correlation matrix (Figure 10.1e) based solely on the marginals, supposing _all_ pairs of 500 highest-expressed genes fire simultaneously as a limiting case. For each gene, we consider the highest-abundance root transcript that can be fit by a negative binomial distribution, and identify its marginal burst size and efflux rate. Substituting these parameter estimates into Equation 10.8, we obtain theoretical correlations _𝜌_ theo and reconstruct the correlation matrix (Figure 10.1f). Finally, we compare the intra-gene sample correlations _𝜌_ samp to the theoretical values in Figure 10.1g. These results represent the 119,805 nontrivial correlation matrix entries based on the 490 genes with well-fit roots. The theoretical constraint (sample correlation equal to or lower than predicted correlation) was met in 119,503 cases (99.7%), with only five confidence intervals above the bound.

Yet again, the model provides a nontrivial bound. We hypothesize that the “consistent” regime ( _𝜌_ samp ∈(0 _, 𝜌_ theo), 117,542 entries) represents the degradation of correlations due to stochastic effects outside the model, much as before. The correlations in the “inconsistent” regime ( _𝜌_ samp ∈( _𝜌_ theo _,_ 1), 302 entries) lie very close to the identity line, so we hypothesize they are mostly explained by small sample sizes. Finally, the “negative” regime ( _𝜌_ samp _<_ 0, 1,961 entries) is rare, and we expect these observations also emerge from small sample sizes.

This model is extremely simple: we have largely omitted the realistic description of technical noise, the modeling of transient intermediates, and the accurate inference of parameters. Nevertheless, for nearly every pair of transcripts we observe, the distribution shapes are consistent with the nontrivial bound obtained by assuming the co-bursting model holds. This model cannot recapitulate the precise quantitative details; such an effort would require considerably more involved modeling and statistics. Nevertheless, it does suggest that the conception of “fast” gene–gene variation has some predictive value, and provides a foundation for developing more sophisticated models. In addition, the analytical procedure provides a framework for testing the consistency of models prior to performing a computationally intensive full fit.

### **<u>10.3 Multimodal variational autoencoder models for “slow” covariation</u>**

This section summarizes the content of [44] by M.C.<sup>_★_</sup> , G.G.<sup>_★_</sup> , Y.C., T.C., and L.P. The _biVI_ approach was conceptualized by G.G., designed by G.G., M.C., Y.C., and T.C., and implemented by M.C., Y.C., and T.C. The statistical derivations were performed by G.G. and M.C.

125

Alternatively, we may explain co-variation in gene expression by cell type differences within a sample. This approach may be as simple as fitting a mixture model to Equation 10.1, but one promising alternative direction has used neural networks to approximate the more general mixture in Equation 10.2. For example, the popular tool _scVI_ is a variational autoencoder (VAE) that uses neural networks to encode scRNA-seq counts to a low-dimensional representation. This representation is decoded by another neural network to a set of cell- and gene- specific parameters for conditional likelihood distributions of observed counts. These Poisson or negative binomial<sup>7</sup> distributions are chosen _post hoc_ to be consistent with the discrete, overdispersed nature of scRNA-seq counts, but can be derived from biophysical models (Sections 2.1 and 4.6).

Extensions of _scVI_ to bimodal data have been attempted for protein [96] and chromatin measurements [12] by jointly encoding data modalities to a single latent space, then employing two decoding networks to produce parameters for _independent_ conditional likelihoods specific to each datatype. Nascent and mature transcripts [168, 197] could be similarly treated (Figure 10.2a). However, using independent conditional likelihoods for bimodal measurements derived from the same gene ignores the inherent causality between observations and has no biophysical basis: the generative model is merely part of a neural “black box” used to summarize data.

Nevertheless, good causal model candidates for the nascent–mature distributions are available, such as the extensively validated [65, 233, 244] bursty model of transcription (Section 4.6.2). While the joint steady-state distribution induced by the bursty model is analytically intractable [261], we have previously shown that it can be approximated by a set of basis functions with neural-network learned weights (Section 5.3). To that end, we introduce _biVI_ , a strategy that adapts _scVI_ to work with well-characterized stochastic models of transcription.

First, we propose a parameterization of the bursty process that could give rise to bivariate count distributions for nascent and mature transcripts, such that the univariate case matches the _scVI_ assumptions. Specifically, _scVI_ assumes that the conditional distribution represents contributions from a gene-specific dispersion parameter _𝜈_ g, a cell-specific “size” parameter _ℓ_ c, and cell- and gene-specific compositional parameter _𝜌_ cg, such that the distribution is negative binomial with shape _𝜈_ g and mean _𝜇_ cg = _ℓ_ c _𝜌_ cg.

Formalizing this descriptive model requires specifying the precise mechanistic meaning of _ℓ_ g. Previous reports equivocate [96], appealing to a combination of

126


Figure 10.2: _biVI_ reinterprets and extends _scVI_ to infer biophysical parameters. **a.** _scVI_ can take in concatenated nascent ( _𝑋𝑁_ ) and mature ( _𝑋𝑀_ ) RNA count matrices, encode each cell to a low-dimensional space **z** , and learn per-cell parameters _𝜇𝑁_ and _𝜇𝑀_ and per-gene parameters _𝜈𝑁_ and _𝜈𝑀_ for independent nascent and mature count distributions. This approach is not motivated by any specific biophysical model.

**b.** Operating conditional on the bursty model of transcription, _biVI_ can take in nascent and mature count matrices, produce a low-dimensional representation for each cell, and output per-cell parameters _𝑏_ and _𝛾_ / _𝑘_ , as well as the per-gene parameters _𝛽_ / _𝑘_ , for a mechanistically motivated joint distribution of nascent and mature counts.

“cell size,” cell-wide effects on the biology (in the spirit of [81, 124]), or “sequencing depth,” technical variability in the sequencing process (in the spirit of [308]). In other words, the former scenario represents, e.g., systematic differences in the concentrations of relevant macromolecules, such as RNA polymerase, whereas the latter scenario represents random differences in the amount of sequencing primers between 10x beads.

For simplicity, we only treat the first case here, although either one may be used as the basis for a mechanistic formulation. If we introduce a genome-wide scaling factor _𝐶_ and recall the basis of the bursty model (Section A.8.1), we find that the

127

following interpretation of the parameters matches _scVI_ for a univariate model:


In other words, the burst size consists of a cell- and gene-specific term, which describes the _scaling_ of the burst size with respect with respect to the polymerase concentration [RNAP]c, as well as a cell-specific term, which encodes this concentration. The dependence on c encodes the mixture model in Equation 10.2. By setting the units appropriately and making _𝐶_ fairly large, we can find small _𝜌_ cg and large _ℓ_ c that produce acceptable fits to the data under the usual _scVI_ priors and functional assumptions. The rest of the variability is encoded in _𝜈_ g, and implicitly assumes that the burst frequency and degradation rate do not change between cells.

Next, we construct a two-species bursty model that retains these assumptions. The simplest one, with no technical noise, takes the following form:


and _𝑏_ cg defined as in Equation 10.10. We have somewhat arbitrarily assumed that the fixed _𝜈_ should correspond to a fixed nascent negative binomial marginal shape parameter in the bivariate case. This yields the following parameter definitions:


128

Given a particular set of _𝜈_ g, _𝜌_ cg<sup>(</sup><sup>_𝑁_),</sup><sup>_𝜌_</sup> cg<sup>(</sup><sup>_𝑀_),and</sup><sup>_ℓ_c,wecanimmediatelycomputethe</sup> cell- and gene-specific parameters:


Using the neural solver in Section 5.3, we can compute distributions and incrementally increasing the likelihood of data Dcg under the model by training the network and updating the parameters; _𝜈_ values are treated as deterministic, while _ℓ_ values may treated as probabilistic or simply use the total molecule count as a plug-in estimate. Each latent vector **z** c is decoded to a pair of _𝜌_ cg<sup>(</sup><sup>_𝑁_)</sup><sup>_, 𝜌_</sup> cg<sup>(</sup><sup>_𝑀_), such that</sup> �g _𝜌_ cg<sup>(</sup><sup>_𝑁_)+</sup><sup>_𝜌_</sup> cg<sup>(</sup><sup>_𝑀_)</sup> = 1. � �

Per Equation 10.13, the inferred likelihood parameters have biophysical interpretations under a specific mechanistic model of transcriptional dynamics. Although we focus on the bursty model, _biVI_ also implements the closed-form constitutive (Section 4.6.1) and extrinsic (Section 4.6.3) noise models [81, 124].

129


Figure 10.3: _biVI_ successfully fits single-cell neuron data and suggests the biophysical basis for expression differences.

**a.** - **b.** Observed, _scVI_ , and _biVI_ reconstructed distributions of _Foxp2_ , a marker gene for L6 CT (layer 6 corticothalamic) cells, and _Rorb_ , a marker gene for L5 IT (layer 5 intratelencephalic) cells, restricted to respective cell type.

**c.** - **d.** Cell-specific parameters inferred for _Foxp2_ and _Rorb_ demonstrate identifiable differences in means and parameters in the marked cell types.

**e.** Cell subclasses show different modulation patterns, with especially pronounced distinctions in non-neuronal cells (top: fractions of genes exhibiting differences in each parameter; bottom: number of cells in each subclass).

**f.** _biVI_ allows the identification of cells which exhibit differences in burst size or relative degradation rate, without necessarily demonstrating differences in mature mean expression. Hundreds of genes demonstrate this modulation behavior, with variation across cell subclasses.

**g.** Histograms of _biVI_ parameters and _scVI_ mature means for two genes that exhibit parameter modulation without identifiable mature mean modulation. _Trem2_ (top) shows differences in the degradation rate in L5 IT cells, whereas _Ndnf_ (bottom) shows differences in burst size in L6 CT cells.

130

Under comparable conditions, _biVI_ recapitulates observed bivariate RNA distributions better than _scVI_ (Figure 10.3a-b). In addition, the latent space structure effectively recapitulates cell subtypes from existing annotations of the mouse neuron dataset under consideration [321]. Beyond this empirical agreement, it allows us to _interpret_ differences in the generative model parameters in terms of biophysics, in the spirit of Section 9.2. For example, in Figure 10.3c-d, we illustrate that the upregulation of markers _Foxp2_ and _Rorb_ can be ascribed to an increase in burst size; these differences are starkly evident in the distribution of parameters but much less so in the distribution of averages.

We extend and exploit this approach to find “marker genes” that demonstrate substantial modulation in the values of _𝑏_ cg _,_ RNAP and _𝛾_ cg/ _𝑘_ g between cell types using a Bayesian procedure analogous to the approach in [96]. The results are visualized in Figure 10.3e. Surprisingly, even in this high-level summary, variation between cell types is quite considerable: neuronal cells appear to regulate gene expression via a mix of regulatory strategies, while non-neuronal cells seem to preferentially modulate burst size.

As in Section 9.2, many genes that demonstrated substantial parameter differences did not demonstrate strong differences in the mature RNA averages. For some cell subclasses, there were several hundred such genes (Figure 10.3f). For example, the relative degradation rate of the gene coding for the triggering receptor expressed on myeloid cells-2 (TREM2), variants of which are strongly associated with increased risk of Alzheimer’s disease [296], was found to be greater in L5 IT neurons than in other subclasses (Figure 10.3g, top row). Similarly, the gene _Ndnf_ , which codes for the neuron derived neurotrophic factor NDNF and promotes the growth, migration, and survival of neurons [165], demonstrated a statistically significant difference in the _biVI_ inferred burst size, but not _scVI_ inferred mature mean, in L6 CT neurons (Figure 10.3g, bottom row).

Such a mechanistic description provides a framework for characterizing the connection between a gene’s role and a cell’s regulatory strategies beyond a mere change in mean expression [204, 206]. The neural framework enables us to relax many of the assumptions of simple mechanistic models, treat non-homogeneous cell populations, and _discover_ internal differences. This marriage of the neural and the mechanistic provides an actionable implementation of the themes developed in [137, 156]: the known physics are represented explicitly; the obscure unspecified networks and parameters are relegated to a neural network “black box.” This network can, in

131

turn, be made more “transparent” by using a linear, rather than neural decoder to map from the low-dimensional latent space to the biophysical parameters, and we obtained reasonable results by implementing such an architecture [276].

We believe that the design of variational autoencoders with neural and mechanistic components presents an exciting avenue for single-cell data analysis: this approach already scales to hundreds of thousands of cells [97] and can easily be extended to more sophisticated models by working through the necessary mathematics. However, the construction of compatible likelihood functions (Section 5.3 and [271, 310]) is no trivial task, and typically requires developing bespoke routines and training approximators anew with each addition. We anticipate that the development of more realistic technical noise models is necessary, especially in light of Section 8.2.

On the other hand, the conclusions we can draw are only as good as the models. The bursty model of transcription is fairly well-attested, but other assumptions we have made may not be. The first implementation of _biVI_ strives to be consistent with _scVI_ ; in this quest for consistency, it sacrifices the ability to describe variation in burst frequencies, which are surely important to the differences between cell types (Chapter 9 and [65]). We could, for example, conceptualize a model that allows the transcriptional parameters to vary while keeping the turnover rates constant:


keeping _𝛽_ g/ _𝛾_ g constant. In this case, we may be able to interpret the “cell size” scaling as mass constraint. In a “strong” mass constraint, we would not allow the total number of molecules to exceed some preset bound; this form of constraint gives rise to intractable distributions. Instead, we would impose a “weak” mass constraint, such that genes cannot have simultaneously have arbitrarily high averages. This implies the following form:


such that<sup>�</sup> g<sup>_𝜌_</sup> cg<sup>_𝜇_= 1, whereas</sup><sup>_𝜌_</sup> cg<sup>_𝑏_∈(0</sup><sup>_,_1) but not otherwise constrained.It remains</sup> to learn or specify _𝛽_ g and _𝛾_ g, which may not be mutually identifiable. Overall, the “correct” way to implement such a constraint is far from clear, and this direction remains an area of active research.

132

In addition to representing more realistic biological phenomena, we anticipate that the VAE framework can be relatively straightforwardly integrated with technical noise phenomena discussed in Sections 4.4.2 and 8.1. Specifically, if the biological RNA distribution is negative binomial with shape _𝜈_ and scale _𝜃_ , whereas the background distribution is Poisson with mean _𝜇_ , the PGF of the overall distribution is given by the product of the individual PGFs:


By directly applying Equation 3.12 and the definition of Kummer’s confluent hypergeometric function _𝑀_ in Equation 3.19, we find that the molecule generative distribution is


Whenever _𝜇_ = 0, the hypergeometric and exponential terms are unity, yielding the expected negative binomial distribution. We expect that a reasonable estimate for _𝜇_ can be obtained by rescaling the dataset-wide average expression. However, the optimal way to implement Equation 10.17 is somewhat obscure. Although Kummer’s function _𝑀_ can be written down in closed form for _𝑥_ ∈ N0, the expression is somewhat unwieldy; to integrate this form of variation into a VAE, it may be more fruitful to use an approximation of the function tailored to the low- _𝜇_ regime. Whatever the implementation, the design of such a generative model requires careful consideration of the basis and meaning of “cell size” effects, and remains a compelling target for future investigations.

133

_C h a p t e r 11_

---

[← DETERMINATION OF BIOLOGICAL DIFFERENCES](16-determination-of-biological-differences.md) · [Up: contents](index.md) · [MODELING FURTHER CLASSES OF MULTIOMIC DATA →](18-modeling-further-classes-of-multiomic-data.md)
