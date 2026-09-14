---
title: MODELING FURTHER CLASSES OF MULTIOMIC DATA
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MODELING FURTHER CLASSES OF MULTIOMIC DATA

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There was set before me a mighty hill, And long days I climbed Through regions of snow. When I had before me the summit-view, It seemed that my labour Had been to see gardens Lying at impossible distances.

#### _The Black Riders and Other Lines, XXVI_ Stephen Crane

Technology hardly stands still, and recent years have seen the development of assays that quantify RNA alongside other modalities, such as chromatin accessibility, epigenetic modifications, and protein content [213]. These technological advances have been accompanied by a variety of more or less _ad hoc_ methods for data integration [12, 96, 128, 180]. Although these methods produce correlated results, they are not perfect proxies for each other [198], nor should they be treated as such: their sources of technical and biological stochasticity are fundamentally different.

There is some hope that we can “integrate” these data types by appealing to the central dogma, and treating observations as realizations of a common process. This strategy extends our discussion thus far: there are conventional models for a single RNA species; to represent nascent and mature RNA, we merely append another reaction; to represent other modalities, we can extend the stochastic systems further, by appending chromatin state transitions to represent DNA states and translation reactions to represent proteins. However, although this conceptual picture is very much in line with the rest of the thesis, the details — i.e., the “correct” ways to represent these phenomena — are as of yet obscure. In this chapter, we speculate about some promising directions for modeling and data analysis.

### **11.1 Protein velocity and acceleration**

This section summarizes the content of [109] by G.G., V.S., and L.P. The method was conceptualized by V.S. and L.P., and designed and implemented by G.G.

134

The RNA velocity pipeline, reviewed in Section 6.1.1, can be easily, and selfconsistently, extended to protein species with abundance _𝑦𝑃_ [275]:


where _𝛽𝑃_ is the translation rate and _𝛾𝑃_ is the protein degradation rate. In other words, if we have protein observations, we can define an “RNA velocity” and a “protein velocity.” The key distinction involves the interpretation. The RNA velocity allows us to extrapolate into the future, because the current nascent RNA content is a leading indicator of the mature RNA content. On the other hand, the protein velocity allows us to extrapolate into the past, because the current protein content is a lagging indicator of the mature RNA content.

Thus, in the standard implementation of RNA velocity, we extrapolate the mature RNA matrix into the future, compare the direction of the extrapolation vector to the directions of the embedding neighbors in mature RNA space, and use this comparison to build a low-dimensional projection of the “future.” In the case of proteins — treating this as more of an analogy then a rigorous derivation — we extrapolate the protein matrix into the past, compare the direction to the directions of the embedding neighbors in protein space, and construct another low-dimensional projection, now reflecting the “past” of the system. We obtain two vectors per cell, whose directions may not match. If they are particularly misaligned, the system exhibits high “acceleration,” which is a second-order, mostly qualitative, characterization of changes in the mature transcriptome.

This approach is theoretically consistent with RNA velocity, easily generalizes, and produces apparently reproducible trends across a variety of datasets. Although our description extends the _velocyto_ assumptions, this line of argument appears to have inspired an alternative, _scVelo_ -based approach to such trivariate models [313]. However, the usual pitfalls of these techniques apply (Section 6.1). The data processing and inference procedures are _ad hoc_ , although the simplistic noise and dynamics assumptions may actually be more legitimate for high-abundance proteins than for low-abundance RNA. The embedding procedure is arbitrary in much the same ways as elsewhere.

More problematically, there is somewhat of a mismatch between the modalities. RNA sequencing captures genome-wide, endogenous nuclear and cytoplasmic RNA,

135

as well as various background noise. On the other hand, the protein quantification technologies built on top of scRNA-seq exploit synthetic, oligo-tagged antibodies bound to membrane proteins. Therefore, key features of the system, such as the cytoplasmic protein content and the precise stoichiometry of antibody binding, are obscure and apparently impossible to determine from the data. In addition to these factors, previous attempts to model this data type have found that proteins exhibit unique and fairly complicated technical artifacts [96, 322]. Much more fundamentally, the process chemistry restricts the approach to _a priori_ well-characterized cell types with commercially available antibodies, i.e., blood cell immune profiling, which somewhat limits the breadth of investigations.

The strategy set out in [31, 253] and outlined in Chapter 4 may hold more promise: RNA and proteins have a causal relationship, so fitting a model of transcription and translation may tell us about the underlying biophysics. However, given the considerable difficulties of solving such models, we anticipate that a study of model behaviors and feasibility would be more appropriate at these early stages, in the spirit of [138].

### **11.2 Chromatin accessibility**

This section summarizes unpublished research undertaken by C.F. and G.G. The form of the model is due to C.F.; the overarching motivation and connection to Glauber dynamics is due to G.G.

In addition to molecular modalities, we would like to self-consistently “integrate” DNA measurements, such as epigenetic markers or chromatin accessibility. For example, if we are interested in the latter, we need to propose a model that defines the dynamics of chromatin opening and closing, and endow it with realistic technical noise. Thus far, statistical approaches to this problem have been largely descriptive [12, 181], with limited use of mechanistic models.

In Section 10.1, we discussed potentially promising ways to model multi-gene systems. In particular, a cursory examination of Equation 10.3 reveals that coregulation by categorical variables, with a parameter _𝜀_ controlling the strength of neighbor interactions, is essentially identical to the continuous-time Glauber formulation [101, 132] of the Ising model of lattice spins [48, 234]. The Ising model is familiar from statistical thermodynamics, and encodes interacting spins on a lattice. At equilibrium, the distribution of states is Boltzmann:


136

where _𝜎_ is a particular combination of spin states, _𝛽_ is the inverse temperature, and _𝐻_ ( _𝜎_ ) is the energy associated with _𝜎_ , encoded in the Hamiltonian. The Hamiltonian, in turn, encodes the interactions between adjacent spins, which drive them to align in a parallel or anti-parallel way, and the field strength, which drives them to align with to the field. Although the Ising model is typically studied at steady state, the Glauber formulation constructs a continuous-time Markov chain with the correct steady state, and allows us to couple the spin dynamics to downstream transcription processes. With some algebra, it is straightforward to see that _𝑘_ on and _𝑘_ off control the field strength, whereas _𝜀_ controls the interactions. Therefore, it seems legitimate to associate the “on” state with open chromatin and the “off” state with closed chromatin, and attempt to fit joint distributions of RNA counts and DNA states.

Ising-style models are appealing and provide certain advantages. The model structure is simple, but encodes two key ideas: on one hand, neighboring genes are co-regulated [84]; on the other, they are bursty when considered individually. The statistics of the Ising model are well-understood, and it is likely that we can obtain important properties of the RNA distributions in terms of the underlying state kinetics. Although the technical noise behaviors for ATAC and RNA-seq technologies are likely quite different, we can begin to construct simple hypotheses. For example, if 00110 denotes a state vector with three occluded and two exposed sites, we should be able to obtain measurements of 00110, 00100, 00010, and 00000, where the exposed sites are erroneously reported as occluded due to stochastic loss of reads; on the other hand, we should not obtain measurements like 10110. However, the details are somewhat obscure and require further study; for example, it is likely that polymerase and transcription factor occupancy can interfere with ATAC readouts, and systematically lead to active sites being reported as occluded.

Usefully, the approach generalizes: the Ising approach has intuitive “knobs” that can be “tuned” to incorporate more sophisticated phenomena. If the model is too simplistic to fit data, we can easily relax certain assumptions, e.g., allow the field or interaction strengths to vary between sites. Most interestingly, once we have begun to operate in the Ising framework, we are not restricted to simple lattice models: we may be able to leverage chromatin structure measurements, such as HiC [176], to construct generic gene–gene interaction graphs and model co-regulation accordingly.

Although rare, this class of models is precedented in bioinformatics, and has been

137

applied to the study of methylation [148] and DNA–protein interactions [199]. Ultimately, however, this direction is very much in its nascence, and considerable further research will be necessary to understand whether Glauber-like dynamics are at all consistent with real data.

### **11.3 Spatial transcriptomics**

This section summarizes unpublished research undertaken by K.J. and G.G.

Finally, it is worthwhile to discuss the compatibility between the mechanistic approach and the recent spate of sequencing-based spatial transcriptomics technologies [202]. Essentially, the commercial methods provide a grid, rather than suspension, of barcoded beads; a tissue is placed on a grid and its RNA is reverse-transcribed and sequenced; the barcode design allows for the reconstruction of the original spatial configuration of the beads. We can begin to construct a model by proposing that a single cell’s RNA content, for a particular gene g, is drawn from a negative binomial distribution with shape _𝑘_ g/ _𝛾_ g and scale _𝑏_ g _𝑝_ . All of these parameters vary with twodimensional location **z** , but in different fashions: intuitively, we should expect the endogenous parameters _𝑘_ g, _𝛾_ g, and _𝑏_ g to depend on the cell type, and the technical parameter _𝑝_ to only depend on the grid. Of course, some beads may be associated with more than one cell, in which case the molecule distribution per barcode would be a sum of negative binomials. In addition, if RNA freely diffuse and contaminate non-cell-associated regions, we may also append a Poisson technical noise term, in the spirit of Section 4.4.2. Therefore, the full generating function may take the following form:


where _𝐺_ bg( **z** ) encodes the background at the grid point **z** , _𝐺_ bc encodes the density of cells captured per bead at **z** (where we have assumed that a single bead can only capture cells from a single cell type), _𝑝_ ( **z** ) is the local molecule capture probability, and _𝐺_ is the negative binomial PGF. This formula is fairly generic, but can be used to, e.g., generate synthetic spatial data by making assumptions about the biological and technical components of variability. For example, we can make _𝐺_ bc degenerate (one cell per barcode), _𝑝_ ( **z** ) a low-frequency Gaussian process transformed to be within (0 _,_ 1), _𝐺_ bg the usual pseudobulk Poisson distribution (Section 8.1), and _𝐺_ the negative binomial PGF, with parameters that are piecewise constant functions of **z** .

138

The extension of the modeling framework to spatial transcriptomic data is an active area of research, and the optimal way to actually fit distributions is far from clear for now. However, we note that the use of the notation **z** , matching Section 10.3, is not incidental: we may be able to treat the location as a predictor, then use a generic neural function to learn the parameters’ dependence on **z** , hopefully recapitulating the cell types. Further, the underlying assumption of cell–cell independence appears to be somewhat restrictive in this context, and it is plausible that agent-based models, in the spirit of [283, 285] are more appropriate for spatial data.

139

_C h a p t e r 12_

---

[← MODELING MULTI-GENE SYSTEMS](17-modeling-multi-gene-systems.md) · [Up: contents](index.md) · [DISCUSSION AND CONCLUSION →](19-discussion-and-conclusion.md)
