---
title: BIOPHYSICS OF GENE EXPRESSION EVOLUTION
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# BIOPHYSICS OF GENE EXPRESSION EVOLUTION

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Felce, Catherine et al. (2025). “Biophysical Constraints on mRNA Decay Rates Shape Macroevolutionary Divergence in Steady-State Abundances”. In: _bioRxiv_ . doi: `10.1101/2025.11.24.690267` . eprint: `2025.11.24.690267` . url: `https://doi.org/10.1101/2025.11.24.690267` .

### **Abstract**

Evolutionary changes to gene expression are understood to be a major driver of phenotypic divergence between species. Researchers have investigated the drivers of this divergence by fitting evolutionary models to multi-species ‘omic’ datasets. It is now apparent that steady-state mRNA expression levels show patterns consistent with evolutionary constraints, likely as a consequence of stabilizing selection. However, as all previous work has used bulk RNA measurements, it has been impossible to determine which of the many cellular processes that contribute to steady-state abundances underlie the divergence between species. Here we develop a novel paradigm for addressing this open problem. Using multi-species single-cell expression data and biophysical models, we estimate mRNA transcriptional burst sizes, splicing rates, and decay rates across multiple species. We then derive phylogenetic models that describe the divergence of these rates under alternative evolutionary scenarios and fit these to the comparative data. We find evidence for biophysical constraints on the rates of mRNA decay, such that macroevolutionary divergence in expression is primarily a consequence of variation in transcriptional bursting.

**Keywords:** Biophysical modeling, single-cell transcriptomics, phylogenetics, evolutionary theory

49

### **Introduction**

Gene expression divergence is understood to be a key determinant of phenotypic divergence between species (King and Wilson, 1975; Wray et al., 2003; Carroll, 2008). Omics technologies enabled comparative analyses of gene expression across individuals and species, providing insights into the molecular and evolutionary mechanisms shaping gene expression evolution, with most studies focusing on mRNA expression evolution measured via RNA-seq. Numerous studies have investigated gene expression evolution across species, revealing both widespread stabilizing selection and lineage-specific adaptive shifts in mRNA expression levels (Gilad, Oshlack, and Rifkin, 2006; Blekhman, Oshlack, and Gilad, 2008; Brawand et al., 2011; Joshua G Schraiber et al., 2013; Barr, Rhodes, and Gilad, 2023). Furthermore, this data has been used to identify complex evolutionary patterns such as organ-specific evolution (Brawand et al., 2011; Chen et al., 2019), conserved gene regulatory modules (S. Roy et al., 2013), differential expression correlated with the emergence of complex phenotypes (Bastide et al., 2022), and gene-by-gene coevolution of gene expression (Cope, O’Meara, and Gilchrist, 2020). Recently, Cope et al. (Cope, Joshua G. Schraiber, and Pennell, 2025) developed a phylogenetic framework to explicitly model the coevolution of mRNA and protein levels, revealing the mutational and selective coupling between these two layers of gene expression, and finding that natural selection is generally stronger on mean protein expression levels.

Despite the progress made in identifying patterns of gene expression evolution and the processes that drive them, these studies have been limited by their use of bulk mRNA measurements. While mean expression levels are a useful measure for studying gene expression evolution, these obfuscate _how_ expression levels evolve and which mechanisms of gene expression are most dynamic or most constrained by natural selection. Steady-state mRNA abundances are determined by a large array of cellular processes (Furlan, de Pretis, and Pelizzola, 2020; Tippmann et al., 2012; Steinbrecht et al., 2024; Park et al., 2012; Alemu et al., 2014; Raj and van Oudenaarden, 2008), which can make different contributions to between-species expression divergence. For example, experimental work using a two-species yeast hybrid found that changes to mRNA degradation rates were often accompanied by opposite-effect changes in transcription rate (Dori-Bachash, Shema, and Tirosh, 2011). This implies that the evolution of regulatory elements has a multifaceted effect on gene expression levels (Hill, Vande Zande, and Wittkopp, 2021; Sarropoulos et al., 2021; Liu, Mosti, and Silver, 2021) that is strongly dependent on interactions between these elements across the genome, suggesting coevolution of regulatory

50

mechanisms (Barrière, Gordon, and Ruvinsky, 2012; Brown et al., 2014; Zrimec et al., 2020).

To access information about these important regulatory mechanisms from transcriptomic data, we need new approaches that explicitly consider biophysical parameters. Principled biophysical modeling is crucial for extracting biological information from RNA-seq data (Gorin, Vastola, and Pachter, 2023). The emergence of single-cell RNA-seq technologies has allowed for the estimation of key biophysical parameters, such as transcriptional burst size and frequency (Luo et al., 2022; Mahat et al., 2024; Tang et al., 2023). Single-cell snapshot experiments can effectively provide two ‘time points’, via the analysis of nascent and mature transcripts (Fang, Gorin, and Pachter, 2025; Zeisel et al., 2011; Gorin, Fang, et al., 2022). Such models have been used to estimate the relationship of transcriptional bursting to cell-cycle stage (Sukys and Grima, 2025), for principled cell-type clustering (Chari, Gorin, and Pachter, 2024), and to disentangle biological and technical noise (Gorin, Vastola, Fang, et al., 2022). The quantification of biophysical parameters from single-cell data opens up new routes for investigating mRNA expression evolution at the levels of transcriptional and post-transcriptional dynamics. With the increased availability of cross-species single-cell datasets, comparative analyses of biophysical parameters could reveal new insights into the biophysics of gene expression evolution on macroevolutionary timescales.

In this work, we introducea newparadigm forinvestigating theevolutionary interplay of different regulatory ‘levers’. Instead of bulk RNA measurements, we use singlecell data, fitting them with biophysically meaningful parameters. Specifically, we consider evolutionary hypotheses involving the coevolution of transcription and mRNA degradation across vertebrates (Figure 4.1). Motivated by experimental results, (Dori-Bachash, Shema, and Tirosh, 2011), we posit a fitness landscape that gives rise to constraining selection on the mean level of spliced mRNA expression. However, when selection acts only on mean expression, the underlying biophysical processes that result in mean expression may evolve as if unconstrained, a process known as systems drift(True and Haag, 2001; Schiffman and Ralph, 2022; Jiang et al., 2023; Veller and Muralidhar, 2025). Thus, we investigate models in which one of the biophysical parameters is under constraining selection, whilst the other is free to adapt to maintain the optimal level of spliced mRNA, to test the hypothesis that selection acts both at the level of gene expression and at the level of the biophysical determinants of gene expression. Building upon the methods of Cope et al. (Cope,

51


<!-- Start of picture text -->
Biophysical model<br>unspliced RNA spliced RNA<br>Phylogenetic<br>Modeling<br>k: b β<br>γ<br>Decay-rate-constrained hypothesis<br>unspliced RNA spliced RNA<br>θμ<br>k: b β<br>θγ<br>γ αγ<br>αb<br>Burst-size-constrained hypothesis<br>unspliced RNA spliced RNA<br>θμ Parameter Inference<br>k: b β<br>,<br>γ-constrained<br>γ<br>αb θb<br>αγ ,<br>b-constrained<br><!-- End of picture text -->

Figure 4.1: Our evolutionary model selection framework. The competing hypotheses impose different constraints on the evolution of the bursting size _𝑏_ and degradation rate _𝛾_ . The model corresponding to each hypothesis is fit to the derived _𝑏_ and _𝛾_ values for the species on the phylogenetic tree. Fitted selection matrices are obtained, and AICs suggest support for the decay-rate-constrained model. Joshua G. Schraiber, and Pennell, 2025), we investigate the joint adaptation of transcriptional burst size and mRNA decay rate, finding support for the model with stabilizing selection on mRNA decay rates and mean spliced expression. This suggests that between-species differences in mRNA levels can be largely attributed to the flexible adaptation of transcriptional burst sizes.

### **Results**

For our basic biophysical model, we chose bursty transcription with the following dynamics:


where transcriptional bursts occur at a rate _𝑘_ , producing bursts of unspliced ( _𝑈_ ) transcripts with sizes distributed according to _𝐵_ , a geometric distribution with mean

52


<!-- Start of picture text -->
Macaca mulatta<br>Homo sapiens<br>Mus musculus<br>Rattus norvegicus<br>100 Sus scrofa<br>Xenopus tropicalis<br>−2 0 2<br>Trait Value<br>log10(b) log10(β) log10(γ)<br><!-- End of picture text -->

Figure 4.2: Values of the biophysical parameters across the phylogeny. The phylogeny is taken from TimeTree(Kumar et al., 2022) (scale bar in Myr). The boxplots at each tip show the mean-centered parameter distributions over genes for mean burst size, _𝑏_ , splicing rate, _𝛽_ , and RNA decay rate, _𝛾_ , in the corresponding species. These trait values are the inputs into our phylogenetic model.

size _𝑏_ . The unspliced transcripts are converted to spliced mRNA ( _𝑆_ ) at a rate _𝛽_ , and the spliced transcripts then decay at a rate _𝛾_ . The ∅ symbol indicates that the transcript before transcription and after decay does not appear in the model.

The biophysical parameters, _𝑏_ , _𝛽_ and _𝛾_ , can be estimated from single-cell data using Monod (Gorin, Chari, et al., 2025), which optimizes the likelihood of the observed counts under the bursty model. We used Monod to infer these biophysical model parameters for single-cell transcriptomics data from Jiao et al.(Jiao et al., 2024) across the spleens of individuals from six different species. The output from this procedure were per-gene, per-species values of the biophysical parameters ( _𝑏, 𝛽, 𝛾_ ) across 167 orthologous genes (Figure 4.2).

We then developed a combined biophysical and phylogenetic model describing the evolution of log burst size (log( _𝑏_ )) and log mRNA decay rate (log( _𝛾_ )) along a tree. We chose these two parameters because together they determine the log mean spliced mRNA level


which is independent of the splicing rate, _𝛽_ (note that _𝛾_ is given in units of the burst initiation rate, _𝑘_ ). Considering these two parameters allows us to test for

53

a constrained version of quantitative systems drift (Veller and Muralidhar, 2025) (recall that the log burst size and log mRNA decay rate would be free to drift if selection only acted on log mean expression). In Appendix C.2, we show that a two dimensional Ornstein-Uhlenbeck model captures the coevolution of burst size and mRNA decay rate due to selection on the mean spliced expression and an additional constraint on one of the two biophysical parameters. Thus, we can determine the biophysical mechanism through which gene expression evolution is mediated, and test which of the contributing biophysical processes is most constrained, alongside selection on mean expression.

We adopt a hierarchical model across genes, to exploit the large number of measured genes and compensate for the limited number of species in our dataset. In particular, while we assume that evolutionary rates are shared among genes, we allow the _optimal_ biophysical parameters to vary between genes; in Appendix C.5 we show that we can analytically integrate over a Gaussian prior on the optima. When sharing information across genes, due to lineage specific adaptation as well as biological and technical noise, some genes may not have any phylogenetic signal (Eng, Bravo, and Keleş, 2009; Blomberg, Garland, and Ives, 2003; Freckleton, Harvey, and Pagel, 2002). Thus, we assume that with probability _𝑝_ w _𝑛_ the biophysical parameters for a gene are taken from a white-noise distribution (see the outlier model in Chaix et al.(Chaix et al., 2008)), and with probability 1 − _𝑝_ w _𝑛_ that they evolve corresponding to our coevolutionary model (see Methods for more details on the full model).

We used the logarithms of the biophysical parameters as continuous characters in our two hypothesized OU models (Figure 4.1; see Appendix C.2 for the derivation of these models from fitness landscapes). The first model, which we henceforth refer to as the decay-rate-constrained ( _𝛾_ -constrained) model, assumes that the primary form of selection is stabilizing selection on the mRNA decay rates. The burst size is then assumed to adjust in response, to achieve an optimal mean level of spliced mRNA expression. In this model, the selection matrix, _𝐻_ , takes the form:


The second model, which we refer to as the burst-size-constrained ( _𝑏_ -constrained) model, assumes that the fitness is most sensitive to the average value of the transcriptional burst size, _𝑏_ . The value of _𝑏_ therefore undergoes strong constraining

54

selection, whilst the decay rate is assumed to adapt to maintain the optimal mean level of spliced mRNA expression. In this model, the selection matrix takes the form:


We used simulations to assess the suitability of our model for inferring evolutionary parameters from biophysical parameters. The simulation results confirm that we can reliably distinguish between the two models described above (see Appendix C.2, Figures C.1-C.4).

### **The data support a decay-rate-constrained model of transcriptional evolution**

After fitting both phylogenetic models to the average burst sizes, _𝑏_ , and decay rates, _𝛾_ , extracted from the Jiao et al.(Jiao et al., 2024) data, we compared AIC values and found support for the decay-rate-constrained model (AIC = 2 _,_ 124), over both the independent (AIC = 2 _,_ 726) and burst-size-constrained (AIC = 3 _,_ 186) models. The fit parameters are shown in Table 4.1, and the AIC values are shown in Figure 4.3a. The out-performance of the _𝛾_ -constrained model over the independent model confirms the importance of modeling the _coevolution_ of biophysical parameters.

|Model|_𝛼𝑏_|_𝛼𝛾_|_𝜎𝑏_|_𝜎𝛾_|_𝑝_wn|
|---|---|---|---|---|---|
|_𝛾_-constrained|31.5|2.33|0.923|1.06|0.149|
|_𝑏_-constrained|0.022|3.56|3.01|0.169|0.900|
|Independent|1.36|1.59|0.651|0.831|0.329|


Table 4.1: Phylogenetic model fitted parameters: selection rates, _𝛼𝑏,𝛾_ , and mutations rates, _𝜎𝑏,𝛾_ , on average transcriptional burst size, _𝑏_ , and mRNA decay rate, _𝛾_ , along with the probability for a gene’s biophysical parameters to be drawn from a whitenoise distribution, _𝑝_ w _𝑛_ .

There are numerous lines of evidence indicating that more highly-expressed genes generally experience stronger selection pressures, such as stronger purifying selection on amino acid substitutions (Drummond and Wilke, 2008; Managadze et al., 2011), stronger bias towards fast/accurate codons (Bénitière, Lefébure, and Duret, 2025; Cope and Shah, 2025) , and more conserved _cis_ regulatory elements (Berthelot et al., 2018). In previous work, Cope et al. found that high-expression genes exhibited stronger selection on mRNA levels compared to low-expression genes. We

55


<!-- Start of picture text -->
(a)<br>(b)<br>3186<br>3000<br>2726 r = 0.97<br>15<br>2124<br>2000<br>10<br>1000<br>5<br>0<br>Low Medium High<br>Model Expression Level<br>Independent γ-constrained b-constrained<br>AIC<br>αγ<br><!-- End of picture text -->

Figure 4.3: **(a):** AIC comparison across the tested phylogenetic models. A lower AIC value indicates a better model fit. **(b):** Selection coefficient for decay rate, _𝛼𝛾_ , in the decay-rate-constrained model, for gene sub-groups ( _𝑛_ = 56 _,_ 55 _,_ 56) binned by expression level.

decide to verify this observation by using the AIC-preferred _𝛾_ -constrained model to compare the driving selection rate, _𝛼𝛾_ , across genes with varying expression levels. To test whether selection on mRNA decay rates is stronger in more highly expressed genes, we binned the genes under investigation based on their median expression levels in human spleens (GTEx Consortium, 2013) and fit our phylogenetic mixture model separately to the genes in each bin, obtaining three sets of evolutionary parameters (Figure 4.3b). Additionally, we computed dN/dS values for the genes across the six species tree and found that, as expected, the genes with higher expression are subject to stronger purifying selection than those with lower expression (See Appendix C.2, Figure C.5). These results suggest that our fitted selection rate correlates with mRNA expression level, consistent with other patterns observed in protein-coding sequence and gene regulatory evolution.

### **Discussion**

Our results reveal that the best model for mRNA expression evolution explicitly models the coevolution of mRNA burst size and decay rate. This accords with computational and experimental evidence that transcriptional evolution is a coordinated process across all regions of the genome (Zrimec et al., 2020), and that burst size and decay rates evolve in a compensatory manner (Andrie, Wakefield, and Akey, 2014;

56

Schaefke et al., 2018; Dori-Bachash, Shema, and Tirosh, 2011). We further show that this coordinated model should involve constraining selection on the decay rate, with burst sizes then adapting to maintain the desired overall expression level. This is consistent with the pleiotropy of the mechanisms of decay-rate adaptation, which suggest that decay rates may be under stabilizing selection (Agarwal and Kelley, 2022) independently from transcriptional burst sizes. For example, there is a close connection between mRNA decay and translation (Wu et al., 2019; Bae and Coller, 2022; Hanson and Coller, 2018; Carneiro et al., 2019; B. Roy and Jacobson, 2013; Chan et al., 2018; Bicknell et al., 2024). This implies that protein-level constraints may also cause stabilizing selection on RNA decay rates. In addition, alternative 3’UTRs, another determinant of RNA stability, simultaneously affect membrane protein localization (Berkovits and Mayr, 2015), mRNA localization, and translational efficiency (Mayr, 2016). This suggests that decay rates cannot adapt freely to achieve a certain level of expression, without also affecting other cellular processes.

In contrast, regulatory elements responsible for transcription are known to evolve rapidly (McQuarrie et al., 2024). For example, flexibly evolving promoter regions are thought to underlie a significant proportion of phenotypic diversity in humans (R. S. Young et al., 2022), and the frequent complete turnover of functional promoters has been observed in both humans and mice (Robert S. Young et al., 2015). These promoter regions are directly related to transcriptional burst size (Larsson et al., 2019; Hendy et al., 2017). Perhaps more so than promoters regions, comparative analysis reveal enhancer regions to experience rapid evolution (Villar et al., 2015; Uebbing et al., 2024), with multiple studies indicating that enhancers play an important role in regulating the frequency of transcriptional bursting (Bartman et al., 2016; Fukaya, Lim, and Levine, 2016; Larsson et al., 2019; Tünnermann et al., 2025). Chromatin state in regulatory regions can also be modified to influence transcriptional dynamics (Ernst et al., 2011), and has been shown to vary widely across human individuals (Kasowski et al., 2013). Chromatin state therefore represents another free ‘tuning knob’ which can affect transcriptional burst size.

Overall, this work represents a new paradigm for probing the regulatory mechanisms underlying macroevolutionary mRNA expression divergence. For the first time, we combine principled biophysical modeling on single-cell data across species with phylogenetic comparative modeling. By selecting a multivariate OU model for biophysically meaningful parameters, we have investigated the selective coupling of these traits, giving insight into how transcription and decay rates coevolve. We

57

have expanded on existing phylogenetic techniques, incorporating a multivariate OU model into a phylogenetic mixture model accounting for genes with no phylogenetic signal, as well as applying biophysical single-cell modeling in a coherent crossspecies framework.

The approach outlined here can be extended to incorporate more complicated dynamics from both the biophysical and phylogenetic perspectives. As additional single-cell data modalities become available, with their corresponding joint biophysical models, these can be straightforwardly integrated into our method. For example, joint models for single-cell RNA with protein counts (Felce, Fang, and Pachter, 2025) could be used to provide insight into the coevolution of translation and protein decay rates, along with the existing transcriptional rates. This would represent another avenue for corroborating the coevolutionary model proposed by Cope et al. (Cope, Joshua G. Schraiber, and Pennell, 2025). In addition, including an integrated biophysical model for RNA and chromatin accessibility measurements (Felce, Gorin, and Pachter, 2024) could allow us to investigate the contribution of evolving on/off rates to gene expression evolution in a full telegraph model. The power of these approaches will increase as higher quality single-cell data, including more combined modalities across a greater number of species, become available.

On the phylogenetic side, our framework could be adapted to include more complicated evolutionary models, for example including mutational coupling between biophysical parameters, or expanding the dimensionality of the OU model to include coevolution between additional traits. With the flexibility to adapt and extend the two halves of our combined approach, researchers will be able to further dissect the contributions of different regulatory processes to the evolution of gene expression. This will provide new insights into how gene regulation has been shaped over the tree of life.

### **Data and code availability**

The Genotype-Tissue Expression (GTEx) Project was supported by the Common Fund of the Office of the Director of the National Institutes of Health, and by NCI, NHGRI, NHLBI, NIDA, NIMH, and NINDS. The average expression data used for the gene binning described in this manuscript were obtained from the GTEx Portal, V10 spleen tissue, on 10/15/2025. The transcriptomic data used in our analysis is taken from Jiao et al. (Jiao et al., 2024). The code and data for the phylogenetic model used to perform these analyses, and scripts to reproduce Figures 4.2, 4.3, and

58

the supplementary figures are available at `https://github.com/pachterlab/ FCSKPP_2025/tree/main` (Pachter Lab, 2025).

### **Acknowledgements**

M.K. and M.P. were supported by NIGMS award R35GM151348 and startup funds from Cornell University. We also thank Charles Trimble for generously funding part of C.F.’s research through Caltech’s CI2 grant program.

### **Methods**

### **Data processing and biophysical modeling**

For this study we use single-cell RNA-seq data from Jiao et al. (Jiao et al., 2024), extracted from the spleen of seven different species. We processed the data using kallisto (Bray et al., 2016; Melsted et al., 2021; Delaney K Sullivan et al., 2025a; Delaney K. Sullivan et al., 2025b) to obtain spliced and unspliced count matrices. After clustering the data from each species by cell-type, we excluded the fish sample from further analysis because of an indistinct and low-count T-cell cluster, leaving six remaining species, which were filtered for T-cells. We searched for genes which had orthologs in all six species using Ensembl BioMart (Kinsella et al., 2011).

We then fit transcriptional rates for these genes in each species separately using Monod (Gorin, Chari, et al., 2025), using the bursty transcription model with Poisson technical noise. Monod is an inference framework which fits per-gene biophysical parameters for a selection of transcriptional models. The dynamics of the model are encapsulated in a chemical master equation, which can then be numerically solved to give steady-state distributions for spliced and unspliced RNA counts, including the impact of technical noise. The likelihood of the observed spliced/unspliced count matrices can then be maximized over biophysical parameters. In practice, this process is repeated over a grid of technical parameters, and the combined values which maximize the likelihood of the data are outputted.

The output of this procedure is a per-gene burst size, _𝑏_ , splicing rate _𝛽_ , and decay rate, _𝛾_ , with the rates given in units of the transcription initiation rate, _𝑘_ , all in log space. We then subtracted the mean of each parameter across genes from each species. After fitting with Monod, which filters some genes, and removing genes without a fitted ortholog in all six species, we were left with 167 genes. The meancentered log values of _𝑏_ , _𝛽_ , and _𝛾_ for each of these genes were used as the traits for the following analysis.

59

### **Phylogenetic modeling and parameter inference**

We consider the two-dimensional Ornstein-Uhlenbeck models for burst size, _𝑏_ , and decay rate, _𝛾_ described in Results. Under these models, the logarithms of _𝑏_ and _𝛾_ follow the following evolution equations:


where **_W_** _𝑡_ is a Wiener process. In our models, we set Σ as a diagonal matrix with entries _𝜎𝑏_ and _𝜎𝛾_ . **_X_** _𝑡_ represents the logarithms of the two biophysical rates:


The forms for the selection matrices in each model:


are derived from the following forms for the fitness function, _𝑤_ :


where we use _𝑏,_<sup>ˆ</sup> _𝛾_ ˆ for the logarithms of _𝑏, 𝛾_ , and for optimal log parameter values, _𝜃𝑏,𝛾_ and an optimal log spliced mean expression level, _𝜃 𝜇_ . Note that, since the optima and parameter values are in log space, _𝑏_<sup>ˆ</sup> − _𝛾_ ˆ represents the ratio of burst size to mRNA decay rate, which is proportional to the mean spliced expression level. See Appendix C.2, for the full derivation of these models, which follows Cope et al. (Cope, Joshua G. Schraiber, and Pennell, 2025).

For parameter inference, we take the values of log _𝑏_ and log _𝛾_ for each species, along with the phylogenetic tree. We fit a mixture model, where each gene is

60

generated from a white noise distribution with probability _𝑝_ w _𝑛_ , and from the relevant phylogenetic model with probability 1 − _𝑝_ w _𝑛_ . The evolutionary selection strengths, _𝛼𝑏,𝛾_ , and stochastic rates, _𝜎_ 1 _,_ 2, are constrained to be equal across genes, whereas the optima _𝜃 𝜇_ and _𝜃𝑏,𝛾_ are assumed to be drawn from normal distributions whose parameters are optimized.

We also fitted an independent OU model using MCMC for all of the biophysical parameters ( _𝑏_ , _𝛽_ and _𝛾_ ), whose details and results are included in Appendix C.3 (Figures C.6-C.8). In addition, we fit two three-parameter- _𝐻_ versions of the coevolution model, whose results are included in Appendix C.4, Figures C.9-C.12.

### **References**

- Agarwal, Vikram and David R. Kelley (Nov. 2022). “The Genetic and Biochemical Determinants of mRNA Degradation Rates in Mammals”. In: _Genome Biology_ 23.1, p. 245. issn: 1474-760X. doi: `10.1186/s13059-022-02811-x` .

- Alemu, Elfalem Y. et al. (Jan. 2014). “Determinants of Expression Variability”. In: _Nucleic Acids Research_ 42.6, pp. 3503–3514. issn: 0305-1048. doi: `10.1093/ nar/gkt1364` .

- Andrie, J. M., J. Wakefield, and J. M. Akey (2014). “Heritable variation of mRNA decay rates in yeast”. In: _Genome Research_ 24.12, pp. 2000–2010. doi: `10.1101/ gr.175802.114` .

- Bae, Haneui and Jeff Coller (2022). “Codon Optimality-Mediated mRNA Degradation: Linking Translational Elongation to mRNA Stability”. In: _Molecular Cell_ 82.8, pp. 1467–1476. issn: 1097-2765. doi: `10.1016/j.molcel.2022.03.032` .

- Barr, Kenneth A., Katherine L. Rhodes, and Yoav Gilad (Sept. 2023). “The relationship between regulatory changes in cis and trans and the evolution of gene expression in humans and chimpanzees”. In: _Genome Biology_ 24, p. 207. issn: 1474-7596. doi: `10.1186/s13059-023-03019-3` . url: `https://pmc.ncbi. nlm.nih.gov/articles/PMC10496171/` (visited on 11/19/2025).

- Barrière, Antoine, Kacy L. Gordon, and Ilya Ruvinsky (Sept. 2012). “Coevolution within and between Regulatory Loci Can Preserve Promoter Function Despite Evolutionary Rate Acceleration”. In: _PLOS Genetics_ 8.9, e1002961. issn: 15537404. doi: `10.1371/journal.pgen.1002961` . (Visited on 10/31/2025).

- Bartman, Caroline R. et al. (Apr. 2016). “Enhancer Regulation of Transcriptional Bursting Parameters Revealed by Forced Chromatin Looping”. en. In: _Molecular Cell_ 62.2, pp. 237–247. issn: 10972765. doi: `10.1016/j.molcel.2016.03. 007` . (Visited on 11/24/2025).

- Bastide, Paul et al. (Dec. 2022). “A Phylogenetic Framework to Simulate Synthetic Interspecies RNA-Seq Data”. In: _Molecular Biology and Evolution_ 40.1,

61

msac269. issn: 0737-4038. doi: `10.1093/molbev/msac269` . url: `https:// pmc.ncbi.nlm.nih.gov/articles/PMC11249980/` (visited on 11/17/2025).

- Bénitière, Florian, Tristan Lefébure, and Laurent Duret (Jan. 2025). “Variation in the Fitness Impact of Translationally Optimal Codons among Animals”. In: _Genome Research_ 35.3, pp. 446–458. issn: 1088-9051, 1549-5469. doi: `10.1101/gr. 279837.124` . (Visited on 11/20/2025).

- Berkovits, Binyamin D. and Christine Mayr (June 2015). “Alternative 3’UTRs Act as Scaffolds to Regulate Membrane Protein Localization”. In: _Nature_ 522.7556, pp.363–367. issn:0028-0836. doi: `10.1038/nature14321` . (Visitedon10/17/2025).

- Berthelot, Camille et al. (Jan. 2018). “Complexity and Conservation of Regulatory Landscapes Underlie Evolutionary Resilience of Mammalian Gene Expression”. In: _Nature Ecology & Evolution_ 2.1, pp. 152–163. issn: 2397-334X. doi: `10. 1038/s41559-017-0377-2` .

- Bicknell, Alicia A. et al. (Apr. 2024). “Attenuating Ribosome Load Improves Protein Output from mRNA by Limiting Translation-Dependent mRNA Decay”. In: _Cell Reports_ 43.4. issn: 2211-1247. doi: `10.1016/j.celrep.2024.114098` . (Visited on 11/18/2025).

- Blekhman, Ran, Alicia Oshlack, and Yoav Gilad (2008). “Segmented shifts in gene expression between human and chimpanzee”. In: _Genome Research_ 18.9, pp. 1514–1522. doi: `10.1101/gr.075713.107` .

- Blomberg, Simon P., JR. Garland Theodore, and Anthony R. Ives (Apr. 2003). “Testing for Phylogenetic Signal in Comparative Data: Behavioral Traits Are More Labile”. In: _Evolution; international journal of organic evolution_ 57.4, pp. 717–745. issn: 0014-3820. doi: `10.1111/j.0014-3820.2003.tb00285.x` .

- Brawand, D. et al. (2011). “The evolution of gene expression levels in mammalian organs”. In: _Nature_ 478, pp. 343–348. doi: `10.1038/nature10532` .

- Bray, Nicolas L et al. (2016). “Near-optimal probabilistic RNA-seq quantification”. In: _Nature biotechnology_ 34.5, pp. 525–527.

- Brown, Andrew Anand et al. (Apr. 2014). “Genetic Interactions Affecting Human Gene Expression Identified by Variance Association Mapping”. In: _eLife_ 3. Ed. by Philipp Khaitovich, e01381. issn: 2050-084X. doi: `10.7554/eLife.01381` .

- Carneiro, Rodolfo L et al. (Jan. 2019). “Codon Stabilization Coefficient as a Metric to Gain Insights into mRNA Stability and Codon Bias and Their Relationships with Translation”. In: _Nucleic Acids Research_ 47.5, pp. 2216–2228. issn: 0305-1048. doi: `10.1093/nar/gkz033` .

- Carroll, Sean B. (2008). “Evo-devo and an expanding evolutionary synthesis: a genetic theory of morphological evolution”. In: _Cell_ 134.1, pp. 25–36. doi: `10. 1016/j.cell.2008.06.030` .

62

- Chaix, R. et al. (Nov. 2008). “Evolution of Primate Gene Expression: Drift and Corrective Sweeps?” In: _Genetics_ 180.3, pp. 1379–1389. doi: `10.1534/genetics. 108.089623` . url: `https://doi.org/10.1534/genetics.108.089623` .

- Chan, Leon Y et al. (Sept. 2018). “Non-Invasive Measurement of mRNA Decay Reveals Translation Initiation as the Major Determinant of mRNA Stability”. In: _eLife_ 7. Ed. by Alan G Hinnebusch, James L Manley, and Roy Parker, e32536. issn: 2050-084X. doi: `10.7554/eLife.32536` . (Visited on 11/18/2025).

- Chari, Tara, Gennady Gorin, and Lior Pachter (Sept. 2024). “Biophysically Interpretable Inference of Cell Types from Multimodal Sequencing Data”. In: _Nature Computational Science_ 4.9, pp. 677–689. issn: 2662-8457. doi: `10.1038/ s43588-024-00689-2` .

- Chen, J. et al. (2019). “A quantitative framework for characterizing the evolutionary history of mammalian gene expression”. In: _Genome Research_ 29, pp. 53–63. doi: `10.1101/gr.238873.118` .

- Cope, Alexander L., Brian C. O’Meara, and Michael A. Gilchrist (May 2020). “Gene expression of functionally-related genes coevolves across fungal species: detecting coevolution of gene expression using phylogenetic comparative methods”. In: _BMC Genomics_ 21.1, p. 370. issn: 1471-2164. doi: `10.1186/s12864-0206761-3` . url: `https://doi.org/10.1186/s12864-020-6761-3` (visited on 11/19/2025).

- Cope, Alexander L., Joshua G. Schraiber, and Matt Pennell (2025). “Macroevolutionary Divergence of Gene Expression Driven by Selection on Protein Abundance”. In: _Science_ 387.6738. doi: `10.1126/science.ads2658` .

- Cope, Alexander L. and Premal Shah (July 2025). “Macroevolutionary Changes in Natural Selection on Codon Usage Reflect Evolution of the tRNA Pool across a Budding Yeast Subphylum”. In: _Proceedings of the National Academy of Sciences_ 122.27, e2419889122. doi: `10.1073/pnas.2419889122` . (Visited on 11/20/2025).

- Dori-Bachash, Mally, Efrat Shema, and Itay Tirosh (July 2011). “Coupled Evolution of Transcription and mRNA Degradation”. In: _PLoS Biology_ 9.7. Ed. by Jürg Bähler, e1001106. issn: 1545-7885. doi: `10.1371/journal.pbio.1001106` . (Visited on 10/16/2025).

- Drummond, Daniel A. and Claus O. Wilke (2008). “Mistranslation-Induced Protein Misfolding as a Dominant Constraint on Coding-Sequence Evolution”. In: _Cell_ 134.2, pp. 341–352. doi: `10.1016/j.cell.2008.05.042` .

- Eng, Kevin H., Héctor Corrada Bravo, and Sündüz Keleş (Oct. 2009). “A Phylogenetic Mixture Model for the Evolution of Gene Expression”. In: _Molecular Biology and Evolution_ 26.10, pp. 2363–2372. issn: 0737-4038. doi: `10.1093/ molbev/msp149` . (Visited on 11/19/2025).

63

- Ernst, Jason et al. (May 2011). “Systematic Analysis of Chromatin State Dynamics in Nine Human Cell Types”. In: _Nature_ 473.7345, pp. 43–49. issn: 0028-0836. doi: `10.1038/nature09906` . (Visited on 10/17/2025).

- Fang, Meichen, Gennady Gorin, and Lior Pachter (2025). “Trajectory inference from single-cell genomics data with a process time model”. In: _PLoS Computational Biology_ 21.1. Version 2, published 21 January 2025, e1012752. doi: `10.1371/ journal.pcbi.1012752` .

- Felce, Catherine, Meichen Fang, and Lior Pachter (2025). “Joint Biophysical Modeling of Paired Single-Cell RNA and Protein Measurements”. In: _bioRxiv : the preprint server for biology_ . doi: `10.1101/2025.11.14.688548` .

- Felce, Catherine, Gennady Gorin, and Lior Pachter (2024). “A Biophysical Model for ATAC-seq Data Analysis”. In: _bioRxiv_ . doi: `10.1101/2024.01.25.577262` . url: `https://www.biorxiv.org/content/early/2024/01/29/2024.01. 25.577262` .

- Freckleton, R. P., P. H. Harvey, and M. Pagel (Dec. 2002). “Phylogenetic Analysis and Comparative Data: A Test and Review of Evidence.” In: _The American Naturalist_ 160.6, pp. 712–726. issn: 0003-0147. doi: `10.1086/343873` . (Visited on 11/19/2025).

- Fukaya, Takashi, Bomyi Lim, and Michael Levine (July 2016). “Enhancer Control of Transcriptional Bursting”. en. In: _Cell_ 166.2, pp. 358–368. issn: 00928674. doi: `10.1016/j.cell.2016.05.025` . (Visited on 11/24/2025).

- Furlan, Mattia, Stefano de Pretis, and Mattia Pelizzola (Dec. 2020). “Dynamics of Transcriptional and Post-Transcriptional Regulation”. In: _Briefings in Bioinformatics_ 22.4, bbaa389. issn: 1477-4054. doi: `10.1093/bib/bbaa389` .

- Gilad, Yoav, Alicia Oshlack, and Scott A. Rifkin (2006). “Natural selection on gene expression”. In: _Trends in Genetics_ 22.8, pp. 456–461. doi: `10.1016/j.tig. 2006.06.002` .

- Gorin, Gennady, Tara Chari, et al. (Nov. 2025). “Monod: model-based discovery and integration through fitting stochastic transcriptional dynamics to single-cell sequencing data”. en. In: _Nature Methods_ 22.11. Publisher: Nature Publishing Group, pp. 2286–2300. issn: 1548-7105. doi: `10.1038/s41592-025-02832-x` . url: `https://www.nature.com/articles/s41592-025-02832-x` (visited on 11/23/2025).

- Gorin, Gennady, Meichen Fang, et al. (2022). “RNA velocity unraveled”. In: _PLoS Computational Biology_ 18.9. Version 2, published September 12, 2022, e1010492. doi: `10.1371/journal.pcbi.1010492` . url: `https://doi.org/ 10.1371/journal.pcbi.1010492` .

- Gorin, Gennady, John J. Vastola, Meichen Fang, et al. (Dec. 2022). “Interpretable and tractable models of transcriptional noise for the rational design of singlemolecule quantification experiments”. In: _Nature Communications_ 13.1, p. 7620.

64

issn: 2041-1723. doi: `10.1038/s41467-022-34857-7` . url: `https://doi. org/10.1038/s41467-022-34857-7` .

- Gorin, Gennady, John J. Vastola, and Lior Pachter (2023). “Studying stochastic systems biology of the cell with single-cell genomics data”. In: _Cell Systems_ 14.10, 822–843.e22. issn: 2405-4712. doi: `https://doi.org/10.1016/j. cels.2023.08.004` . url: `https://www.sciencedirect.com/science/ article/pii/S2405471223002442` .

- GTEx Consortium (2013). “The Genotype-Tissue Expression (GTEx) project”. In: _Nature Genetics_ 45.6, pp. 580–585. doi: `10.1038/ng.2653` .

- Hanson, Gavin and Jeff Coller (Jan. 2018). “Codon Optimality, Bias and Usage in Translation and mRNA Decay”. In: _Nature Reviews Molecular Cell Biology_ 19.1, pp. 20–30. issn: 1471-0072, 1471-0080. doi: `10.1038/nrm.2017.91` . (Visited on 10/16/2025).

- Hendy, Oliver et al. (Nov. 2017). “Differential Context-Specific Impact of Individual Core Promoter Elements on Transcriptional Dynamics”. In: _Molecular Biology of the Cell_ 28.23, pp. 3360–3370. issn: 1059-1524. doi: `10.1091/mbc.E17-060408` . (Visited on 10/17/2025).

- Hill, Mark S., Pétra Vande Zande, and Patricia J. Wittkopp (Apr. 2021). “Molecular and Evolutionary Processes Generating Variation in Gene Expression”. In: _Nature Reviews Genetics_ 22.4, pp. 203–215. issn: 1471-0064. doi: `10.1038/s41576020-00304-w` .

- Jiang, Daohan et al. (July 2023). “On the Decoupling of Evolutionary Changes in mRNA and Protein Levels”. In: _Molecular Biology and Evolution_ 40.8, msad169. issn: 0737-4038. doi: `10.1093/molbev/msad169` . url: `https://pmc.ncbi. nlm.nih.gov/articles/PMC10411491/` (visited on 11/19/2025).

- Jiao, Anjun et al. (Jan. 2024). “Single-cell sequencing reveals the evolution of immune molecules across multiple vertebrate species”. In: _Journal of Advanced Research_ 55. Epub 2023 Mar 4., pp. 73–87. issn: 2090-1224. doi: `10.1016/j. jare.2023.02.017` . url: `https://doi.org/10.1016/j.jare.2023.02. 017` .

- Kasowski, Maya et al. (Nov. 2013). “Extensive Variation in Chromatin States across Humans”. In: _Science (New York, N.Y.)_ 342.6159, pp. 750–752. issn: 1095-9203. doi: `10.1126/science.1242510` .

- King, Mary–Claire and Allan C. Wilson (1975). “Evolution at two levels in humans and chimpanzees”. In: _Science_ 188.4184, pp. 107–116. doi: `10.1126/science. 1090005` .

- Kinsella, Rhoda J. et al. (2011). “Ensembl BioMarts: A Hub for Data Retrieval across Taxonomic Space”. In: _Database: The Journal of Biological Databases and Curation_ 2011, bar030. issn: 1758-0463. doi: `10.1093/database/bar030` .

65

- Kumar, Sudhir et al. (Aug. 2022). “TimeTree 5: An Expanded Resource for Species Divergence Times”. In: _Molecular Biology and Evolution_ 39.8, msac174. issn: 1537-1719. doi: `10.1093/molbev/msac174` . (Visited on 10/31/2025).

- Larsson, Anton J. M. et al. (Jan. 2019). “Genomic Encoding of Transcriptional Burst Kinetics”. In: _Nature_ 565.7738, pp. 251–254. issn: 1476-4687. doi: `10.1038/ s41586-018-0836-1` .

- Liu, Jing, Federica Mosti, and Debra L. Silver (2021). “Human Brain Evolution: Emerging Roles for Regulatory DNA and RNA”. In: _Current Opinion in Neurobiology_ 71, pp. 170–177. issn: 0959-4388. doi: `10.1016/j.conb.2021.11.005` .

- Luo, Songhao et al. (Dec. 2022). “Genome-Wide Inference Reveals That Feedback Regulations Constrain Promoter-Dependent Transcriptional Burst Kinetics”. In: _Nucleic Acids Research_ 51.1, pp. 68–83. issn: 0305-1048. doi: `10.1093/nar/ gkac1204` .

- Mahat, Dig B. et al. (July 2024). “Single-Cell Nascent RNA Sequencing Unveils Coordinated Global Transcription”. In: _Nature_ 631.8019, pp. 216–223. issn: 1476-4687. doi: `10.1038/s41586-024-07517-7` .

- Managadze, D. et al. (2011). “Negative correlation between expression level and evolutionary rate of long intergenic noncoding RNAs”. In: _Genome Biology and Evolution_ 3, pp. 1390–1404. doi: `10.1093/gbe/evr116` .

- Mayr,Christine(Mar.2016). “EvolutionandBiologicalRolesofAlternative3′UTRs”. In: _Trends in cell biology_ 26.3, pp. 227–237. issn: 0962-8924. doi: `10.1016/j. tcb.2015.10.012` . (Visited on 10/17/2025).

- McQuarrie, David W. J. et al. (July 2024). “Rapid Evolution of Promoters from Germline-Specifically Expressed Genes Including Transposon Silencing Factors”. In: _BMC Genomics_ 25.1, p. 678. issn: 1471-2164. doi: `10.1186/s12864-02410584-9` . (Visited on 10/17/2025).

- Melsted, Páll et al. (2021). “Modular, efficient and constant-memory single-cell RNA-seq preprocessing”. In: _Nature biotechnology_ 39.7, pp. 813–818.

- Pachter Lab (2025). _FCSKPP_2025: Code repository_ . `https://github.com/ pachterlab/FCSKPP_2025` . GitHub repository, accessed 22 November 2025.

- Park, Jungsun et al. (Jan. 2012). “What Are the Determinants of Gene Expression Levels and Breadths in the Human Genome?” In: _Human Molecular Genetics_ 21.1, pp. 46–56. issn: 0964-6906. doi: `10.1093/hmg/ddr436` . (Visited on 11/20/2025).

- Raj, Arjun and Alexander van Oudenaarden (Oct. 2008). “Nature, Nurture, or Chance: Stochastic Gene Expression and Its Consequences”. In: _Cell_ 135.2, pp. 216–226. issn: 0092-8674. doi: `10.1016/j.cell.2008.09.050` . (Visited on 11/20/2025).

66

- Roy, B. and A. Jacobson (2013). “The intimate relationships of mRNA decay and translation”. In: _Trends in Genetics_ 29.12, pp. 691–699. doi: `10.1016/j.tig. 2013.09.002` .

- Roy, Sushmita et al. (June 2013). “Arboretum: reconstruction and analysis of the evolutionary history of condition-specific transcriptional modules”. eng. In: _Genome Research_ 23.6, pp. 1039–1050. issn: 1549-5469. doi: `10.1101/gr.146233.112` .

- Sarropoulos, Ioannis et al. (2021). “Developmental and Evolutionary Dynamics of Cis-Regulatory Elements in Mouse Cerebellar Cells”. In: _Science_ 373.6558, eabg4696. doi: `10.1126/science.abg4696` .

- Schaefke, Bernhard et al. (2018). “The Evolution of Posttranscriptional Regulation”. In: _WIREs RNA_ 9.5, e1485. doi: `10.1002/wrna.1485` .

- Schiffman, Joshua S and Peter L Ralph (2022). “System drift and speciation”. In: _Evolution_ 76.2, pp. 236–251.

- Schraiber, Joshua G et al. (2013). “Inferring evolutionary histories of pathway regulation from transcriptional profiling data”. In: _PLoS computational biology_ 9.10, e1003255.

- Steinbrecht, David et al. (Dec. 2024). “Subcellular mRNA Kinetic Modeling Reveals Nuclear Retention as Rate-Limiting”. In: _Molecular Systems Biology_ 20.12, pp. 1346–1371. issn: 1744-4292. doi: `10.1038/s44320-024-00073-2` .

- Sukys, Augustinas and Ramon Grima (Apr. 2025). “Cell-Cycle Dependence of Bursty Gene Expression: Insights from Fitting Mechanistic Models to SingleCell RNA-seq Data”. In: _Nucleic Acids Research_ 53.7, gkaf295. issn: 1362-4962. doi: `10.1093/nar/gkaf295` .

- Sullivan, Delaney K et al. (2025a). “Accurate quantification of nascent and mature RNAs from single-cell and single-nucleus RNA-seq”. In: _Nucleic acids research_ 53.1, gkae1137.

- Sullivan, Delaney K. et al. (2025b). “kallisto, bustools and kb-python for quantifying bulk, single-cell and single-nucleus RNA-seq”. In: _Nature Protocols_ 20.3, pp. 587–607. doi: `10.1038/s41596-024-01057-0` .

- Tang, Wenhao et al. (June 2023). “Modelling Capture Efficiency of Single-Cell RNA-sequencing Data Improves Inference of Transcriptome-Wide Burst Kinetics”. In: _Bioinformatics (Oxford, England)_ 39.7, btad395. issn: 1367-4811. doi: `10.1093/bioinformatics/btad395` .

- Tippmann, Sylvia C et al. (2012). “Chromatin Measurements Reveal Contributions of Synthesis and Decay to Steady-state mRNA Levels”. In: _Molecular Systems Biology_ 8.1, p. 593. doi: `10.1038/msb.2012.23` .

- True, John R and Eric S Haag (2001). “Developmental system drift and flexibility in evolutionary trajectories”. In: _Evolution & development_ 3.2, pp. 109–119.

67

- Tünnermann, Jana et al. (Mar. 2025). _Enhancer control of promoter activity and variability via frequency modulation of clustered transcriptional bursts_ . en. Pages: 2025.03.26.645410 Section: New Results. doi: `10.1101/2025.03.26.645410` . (Visited on 11/24/2025).

- Uebbing, Severin et al. (Oct. 2024). “Evolutionary Innovations in Conserved Regulatory Elements Associate With Developmental Genes in Mammals”. In: _Molecular Biology and Evolution_ 41.10, msae199. issn: 1537-1719. doi: `10.1093/molbev/ msae199` . (Visited on 11/24/2025).

- Veller, Carl and Pavitra Muralidhar (2025). “Quantitative System Drift”. In: _bioRxiv : the preprint server for biology_ . doi: `10.1101/2025.09.17.676933` .

- Villar, Diego et al. (Jan. 2015). “Enhancer Evolution across 20 Mammalian Species”. en. In: _Cell_ 160.3, pp. 554–566. issn: 00928674. doi: `10.1016/j.cell.2015. 01.006` . (Visited on 11/24/2025).

- Wray, Gregory A. et al. (2003). “The evolution of transcriptional regulation in eukaryotes”. In: _Molecular Biology and Evolution_ 20.9, pp. 1377–1419. doi: `10.1093/molbev/msg140` .

- Wu, Qiushuang et al. (2019). “Translation affects mRNA stability in a codondependent manner in human cells”. In: _eLife_ 8, e45396. doi: `10.7554/eLife. 45396` .

- Young, R. S. et al. (2022). “The contribution of evolutionarily volatile promoters to molecular phenotypes and human trait variation”. In: _Genome Biology_ 23.1, p. 89. doi: `10.1186/s13059-022-02634-w` . url: `https://doi.org/10. 1186/s13059-022-02634-w` .

- Young, Robert S. et al. (Oct. 2015). “The Frequent Evolutionary Birth and Death of Functional Promoters in Mouse and Human”. In: _Genome Research_ 25.10, pp. 1546–1557. issn: 1088-9051, 1549-5469. doi: `10.1101/gr.190546.115` . (Visited on 10/17/2025).

- Zeisel, Amit et al. (2011). “Coupled pre-mRNA and mRNA Dynamics Unveil Operational Strategies Underlying Transcriptional Responses to Stimuli”. In: _Molecular Systems Biology_ 7.1, p. 529. doi: `10.1038/msb.2011.62` .

- Zrimec, Jan et al. (Dec. 2020). “Deep Learning Suggests That Gene Expression Is Encoded in All Parts of a Co-Evolving Interacting Gene Regulatory Structure”. In: _Nature Communications_ 11.1, p. 6141. issn: 2041-1723. doi: `10.1038/s41467020-19921-4` .

68

_C h a p t e r 5_

---

[← INTEGRATING PROTEIN COUNTS INTO SINGLE-CELL RNA-SEQ ANALYSIS](08-integrating-protein-counts-into-single-cell-rna-seq-analysis.md) · [Up: contents](index.md) · [PHYSICAL MODELS IN POPULATION EVOLUTION →](10-physical-models-in-population-evolution.md)
