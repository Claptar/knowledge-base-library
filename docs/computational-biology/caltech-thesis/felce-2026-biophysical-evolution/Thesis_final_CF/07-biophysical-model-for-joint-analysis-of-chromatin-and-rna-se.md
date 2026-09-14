---
title: BIOPHYSICAL MODEL FOR JOINT ANALYSIS OF CHROMATIN AND RNA SEQUENCING DATA
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# BIOPHYSICAL MODEL FOR JOINT ANALYSIS OF CHROMATIN AND RNA SEQUENCING DATA

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Felce, C., G. Gorin, and L. Pachter (Dec. 2024). “Biophysical model for joint analysis of chromatin and RNA sequencing data”. In: _Phys. Rev. E_ 110 (6), p. 064405. doi: `10.1103/PhysRevE.110.064405` . url: `https://link.aps.org/doi/ 10.1103/PhysRevE.110.064405` .

### **2.1 Introduction**

The Assay for Transposase-Accessible Chromatin using sequencing (ATAC-seq), introduced in 2013, has become a widely adopted epigenetic discovery tool that can be used to identify regions of open chromatin (Jason D Buenrostro et al., 2013). In 2015, this method was extended to allow for measurements at single-cell resolution (scATAC-seq) (Cusanovich et al., 2015; Jason D. Buenrostro et al., 2015). These techniques were initially developed and applied independently from transcriptomics experiments. As a result, ATAC-seq data are still often analyzed in this manner, often by re-purposing gene-expression tools (Gontarz et al., 2020), and several methods have emerged for analyzing ATAC-seq data in isolation (H. Chen et al., 2019; Bravo González-Blas et al., 2019).

However, since the major interest in ATAC-seq data lies in elucidating the gene expression programs within cells, the data are best understood in combination with gene expression data. The integration of bulk ATAC-seq and RNA-seq data has been carried out in various forms (Jianfang Wang et al., 2022; F. Xu et al., 2023; Ding et al., 2023). However, approaches thus far have been based on heuristics and do not consider underlying biophysical processes such as transcription factor binding, transcriptional bursting, processing and splicing of transcripts, and degradation. ATAC-seq and RNA-seq data can, in principle, inform the specifics of models for these processes. These insights can then be fed back into mechanistic models, which can be used to analyze data and provide information about the dynamics of regulation and transcription.

Approaches for integrating unregistered scATAC-seq and scRNA-seq data, i.e. data collected from different cells from the same sample, include joint analysis of dif-

8

ferentially accessible regions (DARs) (X. Chen et al., 2022) and differential gene expression. Such methods have been used to compare gene regulation across tissues between healthy and pathological conditions (Jin Wang et al., 2018; Sahinyan et al., 2022; Yu et al., 2023; Nazzari et al., 2023; Dhara et al., 2021; Amarasinghe et al., 2023), and across tissue types (Nair et al., 2021), as well as to identify new gene-regulatory pathways (Z. Xu et al., 2022; S. Wang et al., 2022). Combined use of scRNA-seq and scATAC-seq data can also help to distinguish cell-types (Duren et al., 2018; J. Li et al., 2022) and scATAC data can be used to impute scRNA data (Raevskiy et al., 2023). An exciting recent development has been the ability to perform registered scATAC-seq and scRNA-seq, identifying DNA fragments and mRNA transcripts from the same individual cells (Cao et al., 2018; Ma et al., 2020). Such methods provide a direct avenue for joint analysis of the two modalities, thus avoiding the need for “integration" of scRNA-seq and scATAC-seq (Lee, Kaestner, and M. Li, 2023), albeit raising new challenges including sparsity of registered data (Booeshaghi, Gao, and Pachter, 2023). While both registered and unregistered data have been useful for a variety of applications, analysis methods have not incorporated biophysical modeling, and have instead relied on heuristics and phenomenological inferences (J. Li et al., 2022).

On the modeling side, progress has been made in building biophysically motivated and interpretable models for RNA sequencing data (Gayoso et al., 2021; Gligorijević and Pržulj, 2015; Hao et al., 2021). Gorin et al. have outlined a rigorous and general formulation for various models of transcription with intrinsic and extrinsic noise (Gorin, Vastola, and Pachter, 2023), which are potentially distinguishable using single-cell transcriptomics data. However, in that work, the derived distributions are marginalized over DNA-state, and the distinguishability of models using data including chromatin information is not explored. Currently, no such formulation has been applied to the analysis of ATAC-seq data, or to the joint analysis of ATAC-seq and RNA-seq data.

In this work, we lay the foundations for principled and biologically interpretable joint modeling of ATAC and RNA-seq data (see Figure 2.1). This approach leverages the additional information provided by multiomic data (scATAC and scRNA in the same cells) to give insight into transcriptional rates and mechanisms, improving on current ad hoc approaches to combining the two experimental modalities. It also builds on current theoretical frameworks, allowing us to begin considering which types of models can be distinguished using both data types.

9

We propose a model for chromatin dynamics, inspired by the Ising model from physics. Building on (Gorin, Vastola, and Pachter, 2023), we extend gene-gene correlations to linear chromatin regions of arbitrary length, and encode these relationships within the chemical master equation (CME) framework. Identifying these chromatin regions with ATAC-seq peak regions allows us to consider inference techniques which leverage both DNA and RNA information to parametrize these models. After reviewing the CME formulation with a simple example, we show how it can be used to model DNA and RNA dynamics for Ising-like loci of arbitrary lengths. In our model, nearest-neighbor coupling between chromatin sites modifies the stability of the available DNA-states, to a degree which can be tuned by model parameters.

We then use a mixture of theory and simulation to explore the implications of our proposed model. We derive first and second-order moments of the system and investigate the propagation of gene-gene correlations from the level of chromatin accessibility to the level of transcript counts. We extend (Gorin, Vastola, and Pachter, 2023) by considering model identifiability in the case where chromatin information is available. By simulating the full system within our modeling framework, and constructing an inference procedure leveraging both chromatin and transcriptomic information, we explore the distinguishability of this type of model using each of these modalities, as well as both combined. We consider inference under multiomic data taken from the same or different cells (registered vs un-registered), shedding light on the value of matched single-cell measurements for the development of biophysical models.

Finally, we fit our Ising-like model to three different single-cell ATAC-seq datasets, comparing it to a simpler model with chromatin-site independence. By positing a technical noise model, we demonstrate an inference procedure which allows the theory of the previous section to be applied directly to ATAC-seq data. We demonstrate the flexibility of our approach by using the chromatin-state transition rate matrix to describe DNA loci with six closely adjacent ATAC-seq peaks. This gives us enough candidate loci to meaningfully assess the performance of our model relative to a model with independent sites. Our analysis provides support for our characterization of chromatin dynamics, and the existence of nearest-neighbor correlations.

10


Figure 2.1: Joint modeling of gene accessibility and constitutive mRNA production allows for parameter estimation using scATAC-seq and scRNA-seq data. **DNA/RNA Extraction:** Registered scATAC-seq and scRNA-seq information can be taken from the same cells in multiome data. Alternatively, scATAC-seq and scRNA-seq can be performed on separate cells within the same sample. **Data Generation:** The transcripts captured during scRNA-seq are sequenced and processed to give a cellby-gene expression matrix. The fragments of accessible chromatin captured during scATAC-seq are sequenced, and accessible regions are identified via peak calling on the bulk data. Fragments from each cell are then aligned to these peak regions, giving a binary cell-by-peak matrix, indicating whether or not each cell contained a fragment from each peak region. **Chromatin Accessibility Model:** We choose a model for chromatin accessibility where neighboring peak regions are correlated within each cell. This is reminiscent of the Ising model from physics. **Joint Modeling:** By combining a Markov chain model for chromatin-state switching, (illustrated, left), with assumptions for subsequent RNA dynamics, (e.g., constitutive transcription at accessible regions), we can estimate the joint distribution of transcript counts and chromatin accessibility across cells. The model is parameterized in terms of RNA characteristics for each transcript species (e.g., transcription rate: _𝑏_<sup>_𝑖_</sup> , decay rate: _𝑑_<sup>_𝑖_</sup> , for the _𝑖_<sup>t</sup><sup>_ℎ_</sup> species), and features of the chromatin-state transition matrix (e.g. neighbor-neighbor correlations: _𝜖_ , rate of gene switching on/off: _𝑘_ o _𝑛_ / _𝑘_ o _𝑓𝑓_ ). **Parameter Estimation:** By comparing the observed data with predicted distributions from the joint model after adding noise, we can estimate parameters. References; 1: (Klemm, Shipony, and Greenleaf, 2019), 2: (Dillinger, 2021) Created with BioRender.com (Felce, 2023).

11

### **2.2 Model Details**

### **Chromatin Neighbor Interactions**

Recruitment of active chromatin re-modelers by pioneer transcription factors could lead to expanding regions of open chromatin (see stabilizing role of secondary transcription factors in (Klemm, Shipony, and Greenleaf, 2019)). These mechanisms could bias adjacent DNA regions towards sharing the same state of transcriptional accessibility. This motivates the use of correlation structure to describe chromatin, and we consider the simplest model that could yield such correlation: first-order neighbor interactions reminiscent of the Ising model from physics. We choose to parameterize this model by a parameter _𝜖<_ 1, which encodes the preference of neighboring chromatin sites to be aligned. _𝜖_ = 1 yields site independence, and allowing _𝜖_ to differ from 1 gives us the next simplest model, where one misalignment in a configuration reduces the probability of the configuration by a factor _𝜖_ . Note that in our parametrization, a smaller value of _𝜖_ corresponds to a stronger correlation between neighboring regions. Such a formulation is supported by exploratory analysis, as shown in Section 2.5.

The Ising model from statistical mechanics describes magnetic behavior in terms of individual dipole spins which can each be in either of two opposite directions, denoted as up and down, or +1/−1. In ferromagnetic materials, it is energetically favorable for neighboring spins to be aligned. In the presence of an external magnetic field, it is also favorable for spins to align with the direction of the magnetic field, and the interplay of these two factors determines the probability distribution of different states of the system. Such systems can be simulated using Glauber dynamics, where spins are flipped with a probability proportional to e _𝑥𝑝_ (<sup>−Δ</sup> _𝑇_<sup>_<u>𝐸</u>_),whereΔ</sup><sup>_𝐸_denotes</sup> the change in the energy of the system due to the flip. In our chromatin model, up and down spins are analogous to open and closed regions of chromatin, and our model is therefore effectively the 1-D Ising model.

Ising models have been successfully applied in several areas of computational biology. Mo et al. use an Ising model approach to analyze ChIP-chip data and discover transcription factor binding sites (Mo and Liang, 2010a; Mo and Liang, 2010b). They consider a hidden Markov model (HMM) treating chromosomally consecutive probes in a microarray as neighbors in a 1-dimensional Ising chain. Although their treatment and the connection to the Ising model is similar to ours in this work, the foundation for their Ising hypothesis is technical rather than biological, as it rests on the correspondence of many consecutive enriched probes to a single protein

12

binding event. The Ising model has also been applied to modeling collective cell organization (Weber and Buceta, 2016).

In the Ising model, the external magnetic field is assumed to be constant for all spins in the lattice. However, inspection of the first-order moments for chromatin accessibility from ATAC-seq data suggests that this feature of the model is not appropriate in our context (see Appendix A.1 for figures showing the mean openness at different ATAC peak sites). Therefore, we allow the ratio of chromatin opening and closing rates to vary between sites, giving a separate ‘field strength’ parameter per site, along with a common correlation parameter between sites.

### **CME Implementation**

To build a statistical inference framework including this model of chromatin structure, we follow the chemical master equation (CME) approach of Gorin et al. (Gorin, Vastola, and Pachter, 2023). In this approach, the system is assumed to be Markovian, and we evolve the probability distribution across states in a deterministic manner. The state of the system is described by the number of transcripts present for each gene, and the state of chromatin openness for each gene. In our analysis, we have assumed a one-to-one mapping between ATAC-seq peak regions and genes. We assume constitutive transcription whenever a gene is in its open (or on-) state, and no transcription in the closed (or off-) state.

The processes of gene switching, transcription and decay occur at given rates, and these rates are the parameters of the system. These processes each contribute terms to the system of ordinary differential equations (ODEs) which govern the time evolution of the system. For example, decay processes contribute terms to the ODEs which move probability from states with higher transcript numbers to states with lower transcript numbers. These decay terms are straightforward and affect states independently from their chromatin configuration. In contrast, transcription rates at each gene can depend on the underlying state of the DNA.

### **CME Example**

To illustrate the CME framework, we give the simple example of a single-gene system: the telegraph model introduced by Peccoud and Ycard (Peccoud and Ycart, 1995). The chromatin configuration of the system consists of the single gene being either open or closed for transcription, with corresponding transcription rates of _𝑏_ or 0 respectively. The transcript decay rate for this species is _𝑑_ , and the rates of

13

chromatin opening/closing are _𝑘_ on and _𝑘_ off respectively. The system would then be governed by the following ODEs:


where _𝑃𝛼_ ( _𝑚, 𝑡_ ) represents the probability of the system to be in the gene state indexed by _𝛼_ , where here _𝛼_ = 0 _,_ 1 corresponds to the gene being closed/open for transcription respectively, with an integer number, m, of transcripts, at time t. Note that, despite the use of a full derivative, the value of _𝑚_ is fixed in each equation, and Equation 2.1 represents a system of ODEs, one for each possible value of _𝑚_ .

The first terms encode switching between gene states, whilst the decay and transcription terms represent changes in transcript number. The transcription terms only affect the evolution of probabilities in state 1, since no transcription occurs in state 0.

These equations can be summarized in a matrix form. We introduce a system probability vector **_P_** ( _𝑚, 𝑡_ ), whose components are the _𝑃𝛼_ ( _𝑚, 𝑡_ ) described above. The gene-state dynamics can then be encapsulated in the transition matrix, H, given by:


and the evolution of the system can be succinctly described via:

_𝑑_ **_P_** _𝑑𝑡_<sup>(</sup><sup>_𝑚, 𝑡_)=</sup><sup>_𝐻𝑇_</sup><sup>**_P_**(</sup><sup>_𝑚, 𝑡_) +</sup><sup>_𝑑_[(</sup><sup>_𝑚_+ 1)</sup><sup>**_P_**(</sup><sup>_𝑚_+ 1</sup><sup>_, 𝑡_) −</sup><sup>_𝑚_</sup><sup>**_P_**(</sup><sup>_𝑚, 𝑡_)] +</sup><sup>_𝐵_ˆ</sup><sup>**_P_**(</sup><sup>_𝑚, 𝑡_),(2.3)</sup>

where we have also introduced a diagonal transcription matrix, _𝐵_<sup>ˆ</sup> , defined such that _𝐵_ ˆ _𝛼𝛼_ is the transcription rate in the state indexed by _𝛼_ . In this case, _𝐵_ ˆ is given by:


14

This construction can be extended to multiple transcript species and a greater number of gene states. Although we consider only those chromatin-state transitions which can be effected through the opening or closing of a single chromatin region, the framework allows for transitions between any pairs of chromatin states, via modification of the transition matrix.

### **Encoding Chromatin Dynamics**

Working within this CME framework, we turn our attention to encoding the chromatin correlations discussed in Section 2.2.

Restricting Equation 2.3 to chromatin evolution by summing over all possible transcript numbers for each chromatin state, and generalizing to an arbitrary number of possible gene states, we arrive at the chromatin evolution equation:


where, here, **_P_** (t) is a vector whose components, _𝑃𝛼_ ( _𝑡_ ) represent the probability of the system to have chromatin configuration _𝛼_ at time _𝑡_ . We can then encode cooperation between neighboring chromatin regions within the chromatin-state transition matrix, _𝐻_ . To illustrate how this can be done, we consider a two-gene system, with correlations between the two genes.

We define a chromatin-state matrix _𝑆_ , such that _𝑆𝛼_<sup>_𝑖_</sup> gives the openness of gene _𝑖_ in chromatin-state _𝛼_ , and 1/0 correspond to open/closed genes respectively. Note that here and in what follows, for matrices we use superscript Latin indices to reference DNA sites (genes), and subscript Greek indices to reference chromatin configurations. In this work, we will consider the chromatin-state indexed by _𝛼_ as a string of 1’s and 0’s, representing the openness/closedness of adjacent DNA sites. This gives 2<sup>_𝑛_</sup> configurations for _𝑛_ DNA sites. For the two-gene example system, we would have the state matrix:


For this two-gene system we can choose the gene-state transition matrix:

15


where _𝑟𝑖_ ≡ _𝜖_<sup>−1</sup> ( _𝑘_ o _𝑛,𝑖_ + _𝑘_ o _𝑓𝑓_ ), and _𝜖_ is the correlation parameter introduced in Section 2.2. In the Ising model with positive correlations, _𝜖<_ 1, such that the two states that have adjacent chromatin with opposite openness values, (01 and 10), are destabilized relative to the other states, having decay rates and outward transition values which are divided by _𝜖_ and so are large.

Note that to reproduce the Ising stationary distribution for the case of varying siteopenness propensities, we need to set _𝑘_ o _𝑓𝑓_ as equal for all sites, and allow _𝑘_ o _𝑛_ to vary between sites. This gives a stationary distribution where the probability of each state is proportional to the product over sites of each _𝑘_ o _𝑛_ value, and _𝜖_ to the power of the number of ‘misaligned’ neighbors in the state. (See Section 2.5.)

This formulation can be extended to systems with more than two adjacent genes, by again allowing all transitions between states differing by the openness value of a single gene, such that genes ‘turn off’ at a rate _𝑘_ o _𝑓𝑓_ , and turn on at a gene specific rate, _𝑘_ o _𝑛,𝑖_ . The rows of the transition matrix should then be multiplied by a factor, _𝜖_<sup>−</sup><sup>_𝑛_m</sup><sup>_𝑖𝑠_</sup> , where _𝑛_ m _𝑖𝑠_ corresponds to the number of misalignments in the outgoing chromatin state (see Appendix A.2).

In our analysis of ATAC-seq data in Section 2.5, we consider a space of 64 (2<sup>6</sup> ) gene states corresponding to a binary openness value for six adjacent genes. By positing a kinetic relationship between each of these gene states and their RNA dynamics, we can describe the evolution of the system through a joint state space simultaneously encoding DNA configuration and transcriptome composition.

### **RNA Transcript Count Evolution**

Now that we have encoded the desired chromatin dynamics into the chromatin-state transition matrix, we can leverage the machinery of the CME formulation to solve for the resulting RNA distributions in a simple model.

Returning to the evolution of the joint probability distribution for RNA transcripts and chromatin state, as in Equation 2.3, we now expand to the case of multiple

16

genes. We define the probability generating function (PGF) with gene-state index _𝛼_ as:


where _𝑃𝛼_ ( **_m_** _, 𝑡_ ) represents the probability of the system to be in the state indexed by _𝛼_ and have _𝑚_<sup>_𝑖_</sup> RNA counts for each transcript _𝑖_ , and **_z_** represents the vector of PGF arguments, [ _𝑧_<sup>1</sup> _, ..., 𝑧_<sup>_𝑛_</sup> ], for RNA species 1 to _𝑛_ . We define **_z_**<sup>**_m_**</sup> ≡( _𝑧_<sup>1</sup> )<sup>_𝑚_1</sup> ( _𝑧_<sup>2</sup> )<sup>_𝑚_2</sup> _..._ ( _𝑧_<sup>_𝑛_</sup> )<sup>_𝑚𝑛_</sup> .

Let **_G_** represent the vector of PGFs, [ _𝐺_ 0 _, ..., 𝐺 𝑁_ −1], for gene states 0 to _𝑁_ − 1. Let _𝐵_ be the production matrix, whose entries _𝐵𝛼_<sup>_𝑖_</sup> represent the rate of production of species _𝑖_ in state _𝛼_ . For the simplest model, where transcript _𝑖_ is produced at rate _𝑏_<sup>_𝑖_</sup> for states where gene _𝑖_ is active and at rate zero otherwise, we have the relation: _𝐵_ = _𝑆_ diag( **_b_** ), for **_b_** the vector of transcription rates with components _𝑏_<sup>_𝑖_</sup> . Let **_d_** be a vector representing the decay rates of each species _𝑖_ .

Following the procedure outlined in Gorin et al. (Gorin, Vastola, and Pachter, 2023), we then have the full evolution equation:


where the Hadamard product between two matrices is ( _𝑋_ ⊙ _𝑌_ ) _𝛼𝛽_ ≡ _𝑋𝛼𝛽𝑌𝛼𝛽_ for any two matrices _𝑋_ and _𝑌_ with the same dimensions (here dimension _𝑛_ × 1 for _𝑛_ the number of RNA species). (1− **_z_** ) is the vector with components 1− _𝑧_<sup>1</sup> _,_ 1− _𝑧_<sup>2</sup> _, ...,_ 1− _𝑧_<sup>_𝑛_</sup> , and the second term on the right-hand side of Equation 2.9 involves a sum over partial derivatives with respect to PGF variables _𝑧_<sup>_𝑖_</sup> .

The cooperation of adjacent chromatin regions only affects the evolution of the system via the transition matrix, which can be chosen to be of the form in Equation 2.7. We can then solve Equation 2.9 numerically (see Section 2.4), allowing us to characterize the impact of chromatin-level correlations on RNA transcript distributions.

### **2.3 Model Implications**

Having encoded nearest-neighbor chromatin interactions into the CME framework, we can straightforwardly derive the statistical implications of our model. In particular, we consider the first and second-order moments of the system at both the

17

chromatin and RNA levels, and the behavior of correlations between genes at these two levels. The PGF evolution equation (2.9) above leads to the following moments and statistical properties, before considering noise.

### **Chromatin-State Moments**

For considering moments, we introduce the vector **_π_** , representing the steady-state probabilities of the chromatin states of the system. The vector **_π_** has the length of the entire state space, i.e. 2<sup>_𝑛_</sup> , where _𝑛_ is the number of sites in the locus. To obtain the steady state, we set the left-hand side of Equation 2.5 to zero. In terms of the chromatin-state transition matrix, _𝐻_ , this gives:


where **_π_** is normalized such that its entries sum to one. We denote the chromatinstate vector by **_σ_** , where _𝜎_<sup>_𝑖_</sup> represents the openness of the _𝑖_<sup>t</sup><sup>_ℎ_</sup> chromatin region. (For the gene state indexed by _𝛼_ , **_σ_** is equivalent to row _𝛼_ of the state matrix, _𝑆_ .) We consider a first moment of the system, the average openness value of an individual DNA site, _𝑖_ . From the state matrix _𝑆_ , defined above, we have:


where the ⟨⟩ denote expected values and _𝜎_<sup>_𝑖_</sup> represents the openness of the _𝑖_<sup>t</sup><sup>_ℎ_</sup> region. The gene-state covariance in this notation is given by:


where the variance can be obtained by setting _𝑖_ = _𝑗_ in this expression.

### **RNA Transcript Count Moments**

To findmomentsconcerningthe _𝑖_<sup>t</sup><sup>_ℎ_</sup> RNAtranscriptspecies, wedifferentiateEquation 2.9 with respect to _𝑧_<sup>_𝑖_</sup> (see Appendix A.3 for details). This gives the transcript means for each species _𝑖_ :


18

Defining the matrix:


we arrive at an expression for the transcript covariances:


and variances:


### **Correlation Propagation**

Now that we have derived the covariances between genes at both the chromatin and RNA levels, we can investigate the relationship between the gene-gene correlations at the two levels.

We define site-site correlations for accessibility and transcript count respectively via:


We define _𝑓_ as the ratio between these correlations:


and an expression for _𝑓_ , along with its value plotted for a range of parameters, is given in Appendix A.4. We might assume that correlations between the transcript numbers for different genes would be weaker than the chromatin-level correlations between the parent genes, given that transcript dynamics are downstream of chromatin-state dynamics. We might also expect that the correlations at the transcript and chromatin levels would have the same sign. These constraints together would suggest that _𝑓_ should be contained within the range 0 _< 𝑓<_ 1. However, _𝑓_ can exceed 1 for certain parameter ranges in our model. We visualize this in Appendix A.4. We also

19

explore the intuition behind this result in Appendix A.5, constructing two illustrative toy systems, with | _𝑓_ | _>_ 1 and _𝑓<_ 0 respectively, and confirming the behavior of their correlations.

### **2.4 Distinguishability Comparison: Multiome vs Unregistered**

The joint biophysical model we have outlined can also be used to inform choices related to experimental design. In this section we explore the identifiability of the _𝜖_ parameter using both registered and unregistered scRNA-seq and scATAC-seq data. First we simulate the model described in Section 2.2 for a two-gene system of known _𝜖_ , ( _𝜖_ = 0 _._ 3), and sampled steady-state gene states and RNA counts for 20 _,_ 000 cells. We then solve for the joint steady-state distribution of the system analytically (using Equation 2.9) given different values of _𝜖_ , whilst keeping the overall probabilities for each gene to be on constant (by adjusting _𝑘_ o _𝑓𝑓_ ). In this exercise, we neglect noise.

The analytical probability mass function _𝑃_ a _𝑛𝑎𝑙𝑦𝑡𝑖𝑐_ is obtained numerically. First, we define the auxiliary vector variable **_u_** := **_z_** − 1. Next, we apply the method of characteristics to Equation 2.9, obtaining a system of ordinary differential equations (cf. Eq. 51 of (Gorin, Vastola, and Pachter, 2023)):


In this notation, s is a characteristic variable, _𝑇_ (s) := _𝑡_ − s is the characteristic time defined in terms of current process time _𝑡_ , and the RNA-specific entries of **_U_** ( **_u_** _,_ s) solve the following system (cf. Eq. 52 of (Gorin, Vastola, and Pachter, 2023)):


The initial condition for Equation 2.20 is **_U_** (s = 0) = **_u_** , implying that each entry **_U_**<sup>_𝑖_</sup> = _𝑢𝑖𝑒_<sup>−</sup><sup>_𝑑𝑖_s</sup> .

To obtain the generating function at a particular time _𝑡_ and generating function coordinates **_z_** , we directly solve the system of ordinary differential equations in Equation 2.19 using the _SciPy_ function `integrate.solve_ivp` (Virtanen et al., 2020). We integrate from s = _𝑡_ to 0, yielding **_G_** ( **_U_** (0) _,𝑇_ (0)) := **_G_** ( **_u_** _, 𝑡_ ) by construction. The initial condition for this initial value problem is the overall PGF of the system at _𝑡_ = 0; to accelerate convergence, we begin with the (appropriately normalized) initial condition ker( _𝐻_<sup>_𝑇_</sup> ), i.e. the DNA states in their equilibrium distribution and

20

no molecules of RNA present. Finally, to obtain the overall distribution, we evaluate **_G_** over a grid of **_z_** , then individually convert the generating function for each state _𝜎_ to a probability mass function using an inverse fast Fourier transform (Singh and Bokes, 2012; Virtanen et al., 2020).

For each analytic solution, we assume that each sampled cell is an i.i.d. variable drawn from this distribution, and therefore that the probability of obtaining this set of simulated data is given by the product of the probabilities for each cell.

For registered data, we calculate the log-likelihood function given by:


where c indexes cells in the simulated data, **_σc_** is the gene state observed in cell c (as defined in Section 2.3), and **_mc_** is the vector of transcript numbers for cell c (as defined in Section 2.2).

To show the distinguishability achievable with scATAC-seq or scRNA-seq data alone, we repeat the same process, using the respective marginal probability distributions:


This gives the log-likelihoods:


To compare to the unregistered RNA-seq and ATAC-seq data scenario, we sum over log-likelihood contributions from both of the marginal distributions:


where these two sums are over separate groups of sampled cells.

21

To assess the information gained from each modality, we make two different comparisons. Firstly, we consider the case where the total number of sampled cells is kept constant. The log-likelihoods in eq:reg-LL,eq:ATAC-RNA-LL,eq:unreg-LL are calculated for the same 10 _,_ 000 sampled cells in each case. For the unregistered case (Equation 2.24), the first term is a sum over half of these cells, and the second term is a sum over the remaining half. These results are shown for a simulation with _𝜖_ = 0 _._ 3 in the top panel of Figure 2.2. The other parameters used were _𝑘_ o _𝑛_ = 0 _._ 1, _𝑏_ 1 = 10, _𝑏_ 2 = 15, _𝑑_ 1 = 5, _𝑑_ 2 = 7, and a value of _𝑘_ o _𝑓𝑓_ calculated to give an overall probability _𝑝𝑜𝑛_ = 0 _._ 4 for each gene to be open. The simulation was performed to a maximum simulation time of 10 divided by the slowest biological rate (here _𝑘_ o _𝑛_ ), to ensure that equilibrium had been reached.

Secondly, we consider the case of fixed experimental cost. We use publicly available prices from 10x Genomics for separate scATAC-seq and scRNA-seq vs registered multiome per cell (Genomics, n.d.[c]), to estimate the ratio of prices for the different assay types. Although the exact ratio of costs depends on the number of reactions desired, the results that follow are not sensitive to the exact ratio. We use the rounded ratio given by pricing for a single sample of 10 _,_ 000 cells:


and we take the cost for unregistered scATAC and scRNA as the average of the scATAC and scRNA prices per cell ((1 + 1 _._ 2)/2 = 1 _._ 1). We then weight the number of cells for each modality by the inverse of its price, using 10 _,_ 000 sampled cells for the multiomic case, and proportionally more, from the remaining pool of simulated cells, for the other modalities. The log-likelihood curves obtained via this process are shown in the bottom panel of Figure 2.2.

The results in Figure 2.2 reflect the fact that, whilst multiomic data provides the most distinguishing power per cell for models of this type (shown by the multiomic log-likelihood curve giving the sharpest peak around the true _𝜖_ value in the top panel), after adjusting for cost, the results are more complicated. Since the price of obtaining multiomic data is close to the sum of performing scATAC and scRNA separately, unregistered data can sample almost twice as many cells for a similar cost. However, information is also lost in the lack of registered RNA and ATAC information from the same cells. The bottom panel of Figure 2.2 shows that unregistered and registered multiomic data are comparable in their ability to distinguish

22


Figure 2.2: Distinguishability of parameter _𝜖_ under our correlative model using simulated cells at _𝜖_ = 0 _._ 3 (dotted black line). The relative log-likelihood of the simulated data at values of _𝜖_ differing from the true value are plotted for four different emulated scenarios: scATAC-seq only, scRNA-seq only, registered multiome and unregistered scATAC-seq and scRNA-seq. These scenarios are compared keeping a fixed number of cells ( **top** ), or a fixed experimental cost ( **bottom** ).

_𝜖_ in these kinds of models. scATAC-seq data alone would be the most cost-efficient method for determining _𝜖_ .

### **2.5 Application to ATAC-seq Data**

Finally, we apply our model to single-cell ATAC-seq data, and compare it to a model where adjacent chromatin loci are constrained to be uncorrelated.

### **Data Preparation**

We use three 10x Genomics single-cell ATAC-seq datasets to perform our analysis:

- 10k Human Peripheral Blood Mononuclear Cells, ATAC v2, Chromium Controller, analyzed using Cell Ranger ATAC 2.1.0, (2020, September 9) (Genomics, n.d.[b])

23

- 8k Adult Mouse Cortex Cells, ATAC v2, Chromium Controller, analyzed using Cell Ranger ATAC 2.1.0, (2022, March 29) (Genomics, n.d.[d])

- 10k 1:1 Mixture of Human GM12878 and Mouse EL4 Cells, ATAC v2, Chromium Controller, analyzed using Cell Ranger ATAC 2.1.0, (2022, March 29) (Genomics, n.d.[a])

We pre-processed these datasets using the snATAK pipeline (Booeshaghi, Gao, and Pachter, 2023). For the mixed mouse-human dataset, we first separated the human and mice cells and removed doublets. The snATAK pipeline provides a standardized process with a few parameters specifying the structure of the input FASTQ files (see Appendix A.8), and includes peak calling and pseudo-alignment. The output is a cell-by-peak matrix indicating how many read fragments were aligned to each peak region in each cell. After filtering for high quality cells, we binarized the cell-bypeak matrix. This means that if a cell had at least one read aligning to a certain peak, that peak region was considered open for that cell.

Since our model considers regions which are adjacent in space, we then restricted our focus to those peaks which were within 1.5kbp of their adjacent peak. This distance was chosen somewhat arbitrarily to admit a reasonable number of allowed groups of peaks. In particular, we examined groups of six consecutive ATAC peaks, where each was at most 1.5kbp from the next. Here and in what follows, we refer to these groups of six contiguous peak regions as ‘loci’.

The distribution at each locus was then calculated by counting the frequency of different configurations across cells. The possible configurations are given by the length-six binary strings, e.g. 110000, which would represent two consecutive open regions followed by four consecutive closed regions.

### **Exploratory Analysis for Ising-like Model**

After selecting suitable genetic loci for analysis, we investigated whether positive correlations are observed between neighboring chromatin sites. We calculated the Pearson correlation coefficient, _𝑟𝑥𝑦_ , between sites in each pair of adjacent ATACseq peak regions in the selected loci. (See Appendix A.9 for the details of this calculation.) In Figure 2.3, we plot these correlation coefficients for each pair of adjacent sites across the three datasets. This exploratory analysis lends support to the use of an Ising-like model, since a consistently positive correlation coefficient between adjacent sites is indeed observed. The proportions of pairs with positive

24


Figure 2.3: Pearson correlation coefficients between sites in each pair, for each of the three datasets (x positions within each column are random). Each point represents a pair of adjacent ATAC-seq peak regions included in our selected loci. All pairs with a positive Pearson correlation are colored in dark blue, and those with a negative or zero correlation in magenta. The number of pairs with positive correlation is 68/70, 35/35, and 137/150, for the human-mouse mixture, adult mouse cortex, and PBMC datasets respectively. The preponderance of positive correlations lends support to an Ising-like model.

Pearson correlation are 137/150, 35/35, and 68/70 for the PBMC, adult mouse cortex and human-mouse mixture datasets respectively.

### **ATAC-seq Noise Treatment**

For data analysis, we added noise to the result of the above CME dynamics in the following way. We start from the steady-state gene-state distribution **_π_** defined in Equation 2.10. Then, with the addition of technical noise, we reach a final steady-state distribution, **_π_ ˜** , arrived at via:


where we have defined a noise matrix, N . We consider the properties of this noise matrix for dropout noise which symmetrically affects all sites in a locus, giving them a probability _𝑝_ d _𝑟𝑜𝑝_ of being lost. Although this technical noise model is, in a sense, symmetrical, there is an asymmetry in the space of binary strings, since transition

25

from a state with fewer on-sites to a state with more on-sites is impossible. In this sense, the possible states of a locus form a partially ordered set. For instance,


where the partial order, _𝑎_ ≺ _𝑏_ , indicates that sequence _𝑎_ can be obtained, starting from _𝑏_ , via technical noise. In this example, the first two strings are connected by a transition encoded in N , but the second two are not: the technical noise process cannot create false positives.

In the case of a three-site locus the matrix N is eight-dimensional. Using the basis defined by the state matrix, _𝑆_ :


we would have a noise matrix N given by:


where, here, p = pd _𝑟𝑜𝑝_ , and we have assumed that dropout at each site is independent. This is a triangular matrix. See Appendix A.6 for a visualization of the effect of this type of noise.

26

### **Model Inference**

To assess the Ising model for chromatin, we compare a model fixing _𝜖_ to be one, and a model allowing _𝜖_ to vary as a parameter. We compare the models using the Bayesian Information Criterion (BIC), which quantifies goodness-of-fit whilst penalizing extra parameters (see the exact definition in Equation A.35).

Note that, from above, the probabilities for a chromatin configuration **_σ_** in this model, before technical dropout, are given by:


where _𝑛_ m _𝑖𝑠_ is the number of pairs of misaligned neighbors, and again _𝜎𝑖_ = 0 _,_ 1 for site _𝑖_ closed/open. For example,


We then add technical noise in the form of binomial dropout, where each site independently has probability _𝑝_ d _𝑟𝑜𝑝_ of flipping from _𝜎𝑖_ = 1 to _𝜎𝑖_ = 0. However, in the _𝜖_ = 1 case, when fitting based on ATAC-seq data alone, and assuming the system is at steady state, independent binomial dropout is equivalent to a change in _𝑘_ o _𝑛_ values. This is because we can express the probability of a site being accessible in terms of its biological _𝑘_ o _𝑛,𝑖_ and _𝑘_ o _𝑓𝑓_ rates, and multiply this value by (1− _𝑝_ d _𝑟𝑜𝑝_ ) to account for technical dropout. The resulting probability of measuring accessibility at a site _𝑖_ , given dropout, is then equivalent to the probability without dropout, given the substitution _𝑘_ o _𝑛,𝑖_ → _𝑘_ o<sup>′</sup> _𝑛,𝑖_<sup>, where:</sup>


Therefore, after constraining _𝜖_ = 1, the reduced model can be fully described using only six parameters ( _𝑘_ o _𝑛,𝑖_ for _𝑖_ = [1 _,_ 6]).

So we are left with two models. The simple six-parameter model has independent sites, ignoring gene-gene correlations, and the effect of loss of reads is absorbed into the ‘field strength’ at each site. The eight-parameter model includes sitesite correlations parameterized by _𝜖_ , and the probabilities from Equation 2.30 are adjusted by adding binomial loss at each site (see Appendix A.6). This model does

27

capture correlations between genes, and is reminiscent of the Ising model from physics.

### **Results**

We apply this inference procedure to the six-site loci identified in each dataset (see Section 2.5). We fit both the six-parameter and eight-parameter models at each locus, using stochastic global optimization to minimize log-likelihood, and repeated each fit ten times to check convergence.

We show example fits for the six and eight-parameter models in Figure 2.4, for one six-site locus. The locus is from chromosome 18 of the 10k Human PBMCs, ATAC v2, Chromium Controller dataset.

The bar chart shows the observed fraction of the most frequently observed chromatin configurations at this locus. The magenta and blue markers show the analytic distribution using the best-fit parameters for the six/eight-parameter models respectively. See Appendix A.7 for fits at other loci. There we also verified the reliability of the result of the optimization algorithm with an MCMC fit for one locus.

To analyze the effectiveness of the Ising hypothesis, we looked at all of the contiguous six-site loci, as defined above, across the three different 10x datasets. We calculated the BIC score for the six and eight-parameter models at each locus, and record the BIC score difference in favor of the extra parameter _𝜖_ (combined with _𝑝_ d _𝑟𝑜𝑝_ ). We show the distribution of BIC score differences for each dataset in Figure 2.5. Almost all of the loci provide support for using the eight-parameter Ising-like model over a model with independent sites. The proportions of loci with a BIC score favoring the Ising-like model are 26/30, 7/7, and 14/14 for the PBMC, mouse cortex, and humanmouse mixture datasets respectively. The particularly striking positive outlier in the PBMC plot is locus 10:69043845-69054726. The high BIC difference is due to the much better fit of the eight-parameter model for this locus, as shown in Appendix A.10.

### **2.6 Discussion**

In this work we have presented for the first time a minimal biophysical model suitable for joint analysis of RNA-seq and ATAC-seq data. These two modalities are increasingly assayed in single-cell genomics experiments, and our work explores and compares two models which, although relatively simplistic, offer a basic framework for quantitative analysis of multiomic data. We expect that these models will

28


(a)


(b)

Figure 2.4: Six-parameter ( **top** ) and eight-parameter ( **bottom** ) fits to observed distribution at locus chrom 18:77059667-77072738 from human PBMCs. N.B. The 22 most frequently observed strings of the total 64 are shown on the x-axis. The gray bars show the empirical distribution, and the magenta and blue markers the fitted distribution for the six and eight-parameter models respectively.

29


Figure 2.5: BIC score improvement with inclusion of correlations, i.e. six-parameter BIC score minus eight-parameter for each chromatin locus across three datasets. Positive values are plotted in blue, and represent loci at which the BIC score gives support for the full eight-parameter model, whilst negative values are plotted in magenta.

be elaborated on and improved, for example by the inclusion of transcription factor binding. We have already shown that the models help sharpen quantitative questions about gene expression and its relationship to chromatin dynamics, by exploring the ratio of correlations at the chromatin and transcriptome levels.

The framework we have outlined allows us to investigate the effects of DNA-level mechanistic assumptions on the expected distributions of both chromatin configuration and transcriptomics. In this case, we have investigated the effect of nearestneighbor correlations on the system dynamics. To undertake our analysis, we have made use of a form of the Ising model from physics, which has been studied at length. Inspired by its use in other areas of computational biology, we have successfully applied the Ising model in the novel context of ATAC-seq data.

After hypothesizing an Ising model for chromatin dynamics, we followed Gorin et al. (Gorin, Vastola, and Pachter, 2023), and encoded these dynamics using chemical master equations. Making simple assumptions about the corresponding RNA dynamics, we were able to formulate the behavior of both modalities in a

30

tractable and biophysically meaningful way. The first and second order moments of the system were simple to derive from the resulting matrix equations, and allowed us to explore the relationship between correlations at the DNA and at the transcript level. In particular, the mathematical tractability of this class of models allowed us to uncover the unintuitive result that downstream correlations between transcripts of different species can theoretically be higher than the correlations of their parent genes at the level of chromatin configuration.

We then used our model to explore experimental design considerations for combining scATAC and scRNA data. In the context of a two-gene system, we have illustrated the ambiguity around the relative merits of multiomic vs unregistered data at fixed cost for parameter identifiability. This brings into question the rationale for choosing multiome assays over unregistered data, depending on the question being asked, and also highlights the importance of increased data quality for refining biophysical models. The results are also resilient to small variations in pricing, and depend only on the insight that multiomic RNA-seq + ATAC-seq assays intrinsically sample on the order of half as many cells as single-modality measurements. Although this numerical experiment has important limitations - for instance, it omits the impact of dropout noise - it provides a principled foundation for multiomic experiment design. As we obtain a better understanding of technical factors, we can extend this design approach to include noise considerations.

Finally, we were able to directly compare the steady-state distributions derived from the CME formulation to real scATAC-seq datasets, using a binomial dropout model for scATAC-seq technical noise. As a proof of concept, we limited our analysis to loci with six contiguous, close ATAC peak sites. We compared a simple sixparameter model of site-independence, with our eight-parameter Ising-like model plus dropout, and found that our model was almost always preferable in terms of the Bayesian Information Criterion. Our analysis highlights the importance of site-site accessibility correlations, despite the sparsity of ATAC-seq data, and informs our understanding of relations between neighboring DNA regions. Our work does not shed light on the biological details underlying these correlations, but the assumptions implicit in our models point towards experiments that may provide more insight into mechanistic underpinnings. For example, loci with BIC scores that highly favor the model including gene correlations could be candidates for more targeted chromatin remodeling or transcription factor binding experiments. Our approach could also be extended by relaxing the criteria we have used for selecting DNA loci, and assessing

31

nearest-neighbor correlations in a more genome-wide manner.

The techniques that we’ve introduced in this paper could be usefully extended to other data types, such as Hi-C data. Due to the allowed flexibility in specifying the transition matrix, the one-dimensional Ising model discussed in this work could be generalized to an Ising model with arbitrary underlying graph structure. Coupling of chromatin sites which are not linearly adjacent could be introduced via extra factors of the correlation parameter _𝜖_ . In addition, since our framework couples RNA and chromatin dynamics in a simple and extendable way, our model can be incorporated directly into current biophysical modeling tools such as biVI (Carilli et al., 2023). By straightforward modification of our choices for chromatin and RNA dynamics (e.g. constitutive transcription), our approach can be used to explore many more complex systems in a tractable way. Our postulation of an Ising-like structure for the chromatin-state transition matrix could also be extended to analysis of other multiomic assays. Following the prescription outlined in Gorin et al. (Gorin, Vastola, and Pachter, 2023), we could further test the assumptions of this model using single-cell RNA-seq data.

Overall, although sparsity of single-cell ATAC-seq data limits the power of the conclusions reached, we have outlined a promising approach to biophysical modeling of the data type, including its use in conjunction with single-cell RNA-seq data.

### **2.7 Data Availability**

Scriptsimplementingtheseanalysesandsimulationsandreproducingfig:distingfig:BICscatter are available at `https://github.com/pachterlab/FGP_2023` .

### **References**

- Amarasinghe, Harindra E. et al. (Oct. 2023). “Mapping the epigenomic landscape of human monocytes following innate immune activation reveals context-specific mechanisms driving endotoxin tolerance”. In: _BMC Genomics_ 24.1, p. 595. issn: 1471-2164. doi: `10.1186/s12864-023-09663-0` .

- Booeshaghi, A. Sina, Fan Gao, and Lior Pachter (2023). “Assessing the multimodal tradeoff”. In: _bioRxiv_ . doi: `10.1101/2021.12.08.471788` . url: `https: //www.biorxiv.org/content/early/2023/04/18/2021.12.08.471788` .

- Bravo González-Blas, Carmen et al. (May 2019). “cisTopic: cis-regulatory topic modeling on single-cell ATAC-seq data”. In: _Nature Methods_ 16.5, pp. 397–400. issn: 1548-7091, 1548-7105. doi: `10.1038/s41592-019-0367-1` .

32

- Buenrostro, Jason D et al. (Oct. 2013). “Transposition of native chromatin for fast and sensitive epigenomic profiling of open chromatin, DNA-binding proteins and nucleosome position”. In: _Nature Methods_ 10.12, pp. 1213–1218. doi: `10.1038/ nmeth.2688` . url: `https://doi.org/10.1038/nmeth.2688` .

- Buenrostro, Jason D. et al. (June 2015). “Single-cell chromatin accessibility reveals principles of regulatory variation”. In: _Nature_ 523.7561, pp. 486–490. doi: `10. 1038/nature14590` . url: `https://doi.org/10.1038/nature14590` .

- Cao, Junyue et al. (Sept. 2018). “Joint profiling of chromatin accessibility and gene expression in thousands of single cells”. In: _Science_ 361.6409, pp. 1380–1385. issn: 0036-8075, 1095-9203. doi: `10.1126/science.aau0730` .

- Carilli, Maria et al. (Jan. 2023). “Biophysical modeling with variational autoencoders for bimodal, single-cell RNA sequencing data”. In: _Nature Methods_ . doi: `10.1101/2023.01.13.523995` . url: `http://biorxiv.org/lookup/doi/ 10.1101/2023.01.13.523995` .

- Chen, Huidong et al. (Dec. 2019). “Assessment of computational methods for the analysis of single-cell ATAC-seq data”. In: _Genome Biology_ 20.1, p. 241. issn: 1474-760X. doi: `10.1186/s13059-019-1854-5` .

- Chen, Xin et al. (Nov. 2022). “MSR1 characterized by chromatin accessibility mediates M2 macrophage polarization to promote gastric cancer progression”. In: _International Immunopharmacology_ 112, p. 109217. issn: 15675769. doi: `10.1016/j.intimp.2022.109217` .

- Cusanovich, Darren A. et al. (May 2015). “Multiplex single-cell profiling of chromatin accessibility by combinatorial cellular indexing”. In: _Science_ 348.6237, pp. 910–914. issn: 0036-8075, 1095-9203. doi: `10.1126/science.aab1601` .

- Dhara, S. et al. (May 2021). “Pancreatic cancer prognosis is predicted by an ATACarray technology for assessing chromatin accessibility”. In: _Nature Communications_ 12.1, p. 3044. issn: 2041-1723. doi: `10.1038/s41467-021-23237-2` .

- Dillinger, Stefan (2021). _Complete Guide to Understanding and Using ATAC-Seq — activemotif.com_ . `https://www.activemotif.com/blog-atac-seq` . [Accessed 20-11-2023].

- Ding, Min et al. (May 2023). “Integration of ATAC-Seq and RNA-Seq reveals FOSL2 drives human liver progenitor-like cell aging by regulating inflammatory factors”. In: _BMC Genomics_ 24.1, p. 260. issn: 1471-2164. doi: `10.1186/ s12864-023-09349-7` .

- Duren, Zhana et al. (July 2018). “Integrative analysis of single-cell genomics data by coupled nonnegative matrix factorizations”. In: _Proc Natl Acad Sci U S A_ 115.30, pp. 7723–7728.

- Felce, C. (2023). _Created in BioRender_ . `BioRender.com/r42x127` .

33

- Gayoso, Adam et al. (Mar. 2021). “Joint probabilistic modeling of single-cell multiomic data with totalVI”. In: _Nature Methods_ 18.3, pp. 272–282. issn: 1548-7091, 1548-7105. doi: `10.1038/s41592-020-01050-x` .

- Genomics, 10x (n.d.[a]). _10k 1:1 Mixture of Human GM12878 and Mouse EL4 Cells, ATAC v2, Chromium Controller, Single Cell ATAC dataset analyzed using Cell Ranger ATAC 2.1.0_ . Version cellranger-atac-2.1.0. (2022, March 29). url: `https: //www.10xgenomics.com/datasets/10k- 1- 1- mixture- of- humangm12878-and-mouse-el4-cells-atac-v2-chromium-controller-2standard` .

- (n.d.[b]). _10k Human PBMCs, ATAC v2, Chromium Controller, Single Cell ATAC dataset analyzed using Cell Ranger ATAC 2.1.0_ . Version Cell Ranger ATAC v2.1.0. (2020, September 9). url: `https://www.10xgenomics.com/ datasets / 10k - human - pbmcs - atac - v2 - chromium - controller - 2 - standard` .

- (n.d.[c]). _10x Genomics Store_ . `https://www.10xgenomics.com/store` . Accessed: 2024-10-21.

- (n.d.[d]). _8k Adult Mouse Cortex Cells, ATAC v2, Chromium Controller, Single Cell ATAC dataset analyzed using Cell Ranger ATAC 2.1.0_ . Version cellrangeratac-2.1.0. (2022,March29).url: `https://www.10xgenomics.com/datasets/ 8k-adult-mouse-cortex-cells-atac-v2-chromium-controller-2standard` .

- Gligorijević, Vladimir and Nataša Pržulj (Nov. 2015). “Methods for biological data integration: perspectives and challenges”. In: _Journal of The Royal Society Interface_ 12.112, p. 20150571. issn: 1742-5689, 1742-5662. doi: `10.1098/rsif. 2015.0571` .

- Gontarz, Paul et al. (June 2020). “Comparison of differential accessibility analysis strategies for ATAC-seq data”. In: _Scientific Reports_ 10.1, p. 10150. issn: 20452322. doi: `10.1038/s41598-020-66998-4` .

- Gorin, Gennady, John J. Vastola, and Lior Pachter (Oct. 2023). “Studying stochastic systems biology of the cell with single-cell genomics data”. In: _Cell Systems_ 14.10, 822–843.e22. issn: 24054712. doi: `10.1016/j.cels.2023.08.004` .

- Hao, Yuhan et al. (June 2021). “Integrated analysis of multimodal single-cell data”. In: _Cell_ 184.13, 3573–3587.e29. issn: 00928674. doi: `10.1016/j.cell.2021. 04.048` .

- Klemm, Sandy L., Zohar Shipony, and William J. Greenleaf (Jan. 2019). “Chromatin accessibility and the regulatory epigenome”. In: _Nature Reviews Genetics_ 20.4, pp. 207–220. doi: `10.1038/s41576-018-0089-8` . url: `https://doi.org/ 10.1038/s41576-018-0089-8` .

34

- Lee, Michelle Y. Y., Klaus H. Kaestner, and Mingyao Li (Oct. 2023). “Benchmarking algorithms for joint integration of unpaired and paired single-cell RNA-seq and ATAC-seq data”. In: _Genome Biology_ 24.1, p. 244. issn: 1474-760X. doi: `10. 1186/s13059-023-03073-x` . url: `https://doi.org/10.1186/s13059023-03073-x` .

- Li, Jinlu et al. (Apr. 2022). “Integrative Single-Cell RNA-seq and ATAC-seq Analysis of Mesenchymal Stem/Stromal Cells Derived from Human Placenta”. In: _Frontiers in Cell and Developmental Biology_ 10, p. 836887. issn: 2296-634X. doi: `10.3389/fcell.2022.836887` .

- Ma, Sai et al. (Nov. 2020). “Chromatin Potential Identified by Shared SingleCell Profiling of RNA and Chromatin”. In: _Cell_ 183.4, 1103–1116.e20. issn: 00928674. doi: `10.1016/j.cell.2020.09.056` .

- Mo, Qianxing and Faming Liang (Jan. 2010a). “A hidden Ising model for ChIP-chip data analysis”. In: _Bioinformatics_ 26.6, pp. 777–783.

- (Jan. 2010b). _Bayesian Modeling of ChIP-chip Data Through a High-Order Ising Model_ . doi: `10.1111/j.1541-0420.2009.01379.x` . url: `http://dx.doi. org/10.1111/j.1541-0420.2009.01379.x` .

- Nair, Venugopalan D. et al. (2021). “Differential analysis of chromatin accessibility and gene expression profiles identifies cis-regulatory elements in rat adipose and muscle”. In: _Genomics_ 113.6, pp. 3827–3841. issn: 0888-7543. doi: `https: //doi.org/10.1016/j.ygeno.2021.09.013` .

- Nazzari, Marta et al. (Sept. 2023). “Investigation of the effects of phthalates on in vitro thyroid models with RNA-Seq and ATAC-Seq”. In: _Frontiers in Endocrinology_ 14, p. 1200211. issn: 1664-2392. doi: `10.3389/fendo.2023.1200211` .

- Peccoud, J. and B. Ycart (Oct. 1995). “Markovian Modeling of Gene-Product Synthesis”. In: _Theoretical Population Biology_ 48.2, pp. 222–234. issn: 00405809. doi: `10.1006/tpbi.1995.1027` .

- Raevskiy, Mikhail et al. (Mar. 2023). “Epi-Impute: Single-Cell RNA-seq Imputation via Integration with Single-Cell ATAC-seq”. In: _International Journal of Molecular Sciences_ 24.7, p. 6229. issn: 1422-0067. doi: `10.3390/ijms24076229` .

- Sahinyan, Korin et al. (Feb. 2022). “Application of ATAC-Seq for genome-wide analysis of the chromatin state at single myofiber resolution”. In: _eLife_ 11. Ed. by YM Dennis Lo and Nora Yucel, e72792. issn: 2050-084X. doi: `10.7554/eLife. 72792` .

- Singh, Abhyudai and Pavol Bokes (Sept. 2012). “Consequences of mRNA transport on stochastic variability in protein levels”. In: _Biophys J_ 103.5, pp. 1087–1096.

- Virtanen, Pauli et al. (2020). “SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python”. In: _Nature Methods_ 17, pp. 261–272. doi: `10.1038/ s41592-019-0686-2` .

35

- Wang, Jianfang et al. (Aug. 2022). “Integration of RNA-seq and ATAC-seq identifies muscle-regulated hub genes in cattle”. In: _Frontiers in Veterinary Science_ 9. issn: 2297-1769. doi: `10.3389/fvets.2022.925590` . url: `https://www. frontiersin.org/journals/veterinary-science/articles/10.3389/ fvets.2022.925590/full` .

- Wang, Jin et al. (2018). “ATAC-Seq analysis reveals a widespread decrease of chromatin accessibility in age-related macular degeneration.” In: _Nature communications_ 9(1), 1364. doi: `https://doi.org/10.1038/s41467-018-03856-y` .

- Wang, Shicong et al. (Sept. 2022). “Integrating ATAC-seq and RNA-seq Reveals the Dynamics of Chromatin Accessibility and Gene Expression in Apple Response to Drought”. In: _International Journal of Molecular Sciences_ 23.19, p. 11191. issn: 1422-0067. doi: `10.3390/ijms231911191` .

- Weber, Marc and Javier Buceta (June 2016). “The cellular Ising model: a framework for phase transitions in multicellular environments”. In: _Journal of the Royal Society Interface_ 13.119, p. 20151092. issn: 1742-5689. doi: `10.1098/rsif. 2015.1092` .

- Xu, Feifei et al. (2023). “Integration of ATAC-Seq and RNA-Seq identifies key genes and pathways involved in the neuroprotection of S-adenosylmethionine against perioperative neurocognitive disorder”. In: _Computational and Structural Biotechnology Journal_ 21, pp. 1942–1954. issn: 2001-0370. doi: `10.1016/j. csbj.2023.03.001` .

- Xu, Zhong et al. (Oct. 2022). “Integration of ATAC-seq and RNA-seq analysis identifies key genes affecting intramuscular fat content in pigs”. In: _Frontiers in Nutrition_ 9, p. 1016956. issn: 2296-861X. doi: `10.3389/fnut.2022.1016956` .

- Yu, Dongdong et al. (Apr. 2023). “Co-profiling reveals distinct patterns of genomic chromatin accessibility and gene expression in pulmonary hypertension caused by chronic hypoxia”. In: _Respiratory Research_ 24.1, p. 104. issn: 1465-993X. doi: `10.1186/s12931-023-02389-3` .

36

_C h a p t e r 3_

---

[← INTRODUCTION](06-introduction.md) · [Up: contents](index.md) · [INTEGRATING PROTEIN COUNTS INTO SINGLE-CELL RNA-SEQ ANALYSIS →](08-integrating-protein-counts-into-single-cell-rna-seq-analysis.md)
