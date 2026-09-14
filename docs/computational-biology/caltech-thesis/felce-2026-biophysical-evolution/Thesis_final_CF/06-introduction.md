---
title: INTRODUCTION
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# INTRODUCTION

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In physics, we celebrate finding the most universal, yet simplest principles which govern the behavior of complex inanimate systems. The search for such general principles underlying biology has historically been elusive (Dhar and Giuliani, 2010). Whilst scale separation often makes physics problems tractable (Modin and Viviani, 2022; Falkowski, 2023; Wilson, 2025), biologically interesting processes combine intricate webs of interaction spanning multiple length and time-scales (Bergelson et al., 2021; Dada and P. Mendes, 2011). The consistent laws and fungible fundamental particles of physics are far from the reality of biology, where organismal history and context have persistent effects (Ellis and Kopel, 2019), and variation between biological objects has been described as a ‘fundamental theoretical principle’ (Montévil et al., 2016).

However, as the abundance and resolution of biological data increases, more quantifiable biological models are within reach. Biologists are calling for the methodologies from physics to be brought to bear on fundamental questions in cellular biology (Phillips and Quake, 2006). Perhaps biology’s most closely analogous field in physics is astrophysics, where a similar explosion of quantitative data has brought new opportunities and challenges (Schadt et al., 2010; Z. D. Stephens et al., 2015). In astrophysics, as in cellular biology, each observed phenomenom must be described via the integration of multiple physical theories. Neutron star mergers demand understanding of both general relativity, particle and dense matter physics (B. P. Abbott et al., 2017). Main sequence star binary descriptions may be incomplete without both classical mechanics and magnetohydronamics (Catherine Felce and Fuller, 2023). And similarly, the process of DNA transcription cannot be understood outside of an understanding of chromatin remodeling, transcription factor binding and polymerase recruitment (to name only the high level processes involved).

Since the primary foci of investigation in astrophysics and cellular biology are, in a way, fixed (i.e. the existing astronomical objects and organisms), both fields evade a completely reductionist treatment. Whereas particle physicists can create new phenomena by experiments at higher and higher energies, in astrophysics, as in cellular

2

biology, our path to greater insight is through greater resolution measurements of existing systems. As Phillips and Quake compare, increasingly comprehensive genomics assays could play a similar role to spectrometry, which allows astronomers to precisely ascertain both the speeds and chemical compositions of astrophysical bodies. Indeed, exact DNA sequencing and the precise quantification of RNA transcripts have already transformed the field of genomics and precipitated remarkable discoveries (Lander et al., 2001; Mortazavi et al., 2008; F. Tang et al., 2009; ENCODE Project Consortium, 2012; GTEx Consortium, 2015) .

In the next section, I will discuss how to build well-motivated models for transcriptomic data, moving closer to the level of rigor of physical theories available to analyze astrophysical observations. When considering such models, a difference between astrophysical and biological data is brought into focus, namely the difference in physical scale. This obvious but important discrepancy has implications for the kinds of models appropriate to each field. Whereas most astrophysical phenomena are on a large enough scale that we can ‘average’ over enough of the underlying randomness (quantum mechanics or individual particles within astrophysical fluids) that the dynamics appear deterministic, in biological systems, stochasticity is vitally important. In addition, the focus of biophysical modeling is on non-equilibrium systems. These differences imply that principled stochastic modeling, rather than deterministic laws, are the basis of a large class of models for cellular biology. We hope that such models can form the basis of a more ‘bottom-up’ approach to our understanding of cellular processes.

While ‘top-down’ research will remain essential in applications like medical research, with increasing resolution of genomic data, an improved theoretical understanding of the normal operation of cells and their gene expression is within reach. In biology, as in physics, although reductive models are not applicable to every regime, they can bring important insights with the correct application.

### **1.1 Biophysical modeling**

Historically, most single-cell gene expression analysis has consisted in simply identifying differentially expressed genes between groups of cells (T. Wang et al., 2019; Das, A. Rai, and S. N. Rai, 2022; Dal Molin, Baruzzo, and Di Camillo, 2017). Model-agnostic mathematical tools, for example in dimension reduction and trajectory inference, have been applied to single-cell expression data with problematic results (Huang, Yam, and N. L. Tang, 2025; Gennady Gorin, Fang, et al., 2022; T.

3

Chari and Lior Pachter, 2023). Biophysical modeling attempts to replace heuristic descriptions of biological systems with principled foundational models. In particular, biophysical modeling of DNA transcription can allow us to distinguish between simple but distinct transcriptional mechanisms (Gennady Gorin, Vastola, et al., 2022). Analyzing single-cell RNA-seq datasets using these models can allow us to determine delineations between subpopulations that cannot be detected at the level of mean expression (Chari and Pachter, 2024). Precise biophysical modeling has proven useful in identifying and distinguishing technical, statistical and biological effects in transcriptional data (Cao, Yiling Wang, and Grima, 2025; Kim and Marioni, 2013; Bohrer and Roberts, 2016). It has been particularly effective in quantifying transcriptional bursting in terms of burst size and frequency (Larsson et al., 2019; Grima and Esmenjaud, 2024).

In (Phillips and Quake, 2006), the authors identify “understanding the collective effects that give rise to the exquisite organization in space and time revealed by cellular life”, as an area for investigation in physics. They highlight that the ‘final arrow’ in the central dogma, which should connect the products of translation back to the DNA, is often neglected. They express the hope that, with increasingly quantitative data, these phenomena will become accessible to rigorous characterization. We have attempted to answer this call by integrating new experimental techniques into existing biophysical modeling frameworks. In particular, I investigate the analysis of data from two experimental techniques, ATAC-seq and protein sequencing (CITE-seq), which both shed light on ‘closing the loop’ of the central dogma.

ATAC-seq (Cusanovich et al., 2015), an assay for accessible chromatin regions, is a quantitative measure of chromatin configuration. Whilst chromatin configuration affects the transcriptional activity of different genes, it is also impacted by the proteins these genes produce. Chromatin binding factors play a key role in determining DNA configuration (Klemm, Shipony, and Greenleaf, 2019), and jointly modeling chromatin accessibility and gene expression therefore provides insight into the complex feedback loops that result in time-organized cellular processes. By considering gene-gene correlations at the DNA level in a statistical mechanical framework in Chapter 2, we cohere with the analogy given in (Phillips and Quake, 2006) between emergent phenomena in physics and collective organization in biology.

Direct measurement of expressed proteins represents another tool for investigation of the central dogma loop. CITE-seq (Stoeckius et al., 2017) gives simultaneous RNA and surface protein counts for individual cells, allowing for joint modeling of

4

the proteome and transcriptome at single-cell resolution. Since RNA counts have historically been used as a proxy for protein expression, disentangling the processes of transcription and translation has the potential for significant impact (Xiaojing Wang, Liu, and Zhang, 2014).

### **1.2 Biophysical modeling and evolution**

Similarly to with gene expression, biological studies of evolution initially stopped short of rigorous quantification. As Felsenstein bemoans in his seminal work, ‘Phylogenies and Quantitative Characters’ (Felsenstein, 1988), species-level trait analysis was initially kept separate from the quantitative methods of evolutionary genetics. Whilst systematists grouped species by morphological traits, evolutionary geneticists restricted their precise gene-level observations to within-population studies. An entire school of thought (pattern cladism) rejected the notion of phylogenetic inference from similarity of traits between species. Before Felsenstein and others developed tools for their unification, the study of quantitative genetics and systematics were therefore entirely separate.

Felsenstein saw that, with the increasing availability of molecular data (e.g. DNA sequences) across species, evolutionary genetic models could now be extended ‘across the species boundary’. His initial models, including the Brownian motion model for genetic drift, were perhaps overly simplistic, using restrictive assumptions and outright ignoring important dynamics such as selection itself. Nevertheless, the methodological tools developed by Felsenstein and others to bridge the gap between these top-down (systematist) and bottom-up (evolutionary genetics) approaches are now the foundations of the entire field of phylogenetic comparative methods (PCMs).

Whilst phylogenetic correlations were initially seen simply as a problem to be overcome to obtain independent trait measurements between species (Felsenstein, 1985), quantitative traits in combination with phylogenetic trees are now used to infer the dynamics of evolutionary processes (F. K. Mendes et al., 2018; Hadfield and Nakagawa, 2010; O’Meara, 2012). Many of these studies are based on Brownian motion, or Ornstein-Uhlenbeck (Brownian motion with the addition of mean-reversion), models of trait evolution (Butler and King, 2004; D. C. Adams, 2012; Dibán and Hinojosa, 2024). More complex models, including varying evolutionary optima across clades, have allowed us to identify and describe complicated phenomena such as convergent adaptive radiations (Mahler et al., 2013).

Many of these phylogenetic models use gene expression levels, determined from

5

mRNA measurements, as their quantitative trait of interest (Price et al., 2022; Hill, Vande Zande, and Wittkopp, 2021; Blekhman et al., 2008). However, using the level of gene expression itself as an evolving trait obscures the underlying biophysical mechanisms for transcription. The same problems with the normalization of gene expression values which motivate biophysical modeling (Bullard et al., 2010) have been known to affect PCMs using gene expression as continuous characters (Dimayacyac et al., 2023a). In Chapter 4, I explore the integration of biophysical modeling and phylogenetic comparative methods. Similarly to initial models for integrating systematics and evolutionary genetics, the proposed approach is simple, but I hope that it too may provide a useful bridge between these currently disjoint fields. Our approach can then be refined to capture more complicated histories and develop an increasingly nuanced picture of the evolution of transcriptional dynamics.

### **1.3 Physical models and ecology**

The search for more quantitative descriptions for biological phenomena also extends to population genetics and ecology. As early as 1975, there have been calls for the use of more quantitative methods for ecology (Gates, 1975), under the name ‘biophysical ecology’. A biologist and a physicist, Gates endorses the use of mathematical tools from physics and chemistry for building theoretical models in ecology. He emphasizes that these models should be predictive, and amenable to experimental investigation.

Ginzburg and Colyvan adhere closely to this philosophy in their book, ‘Ecological orbits: How planets move and populations grow’ (Ginzburg and Colyvan, 2004). In it, they propose a new ecological theory, which they believe more efficiently explains observed ecological allometries than pre-existing theories. In particular, they present a new foundational model for population cycles, inspired by analogy to inertial motion in physics. They especially draw a connection between ecological cycles and astronomical orbits, suggesting that environmental ‘forces’ might produce populational ‘acceleration’, rather than impacting the ‘velocity’ (population growth rate) directly. Using this framework, they are able to explain population cycles via maternal effects in a single species, without needing to posit interactions with any additional species, such as traditional predator-prey models (Lotka, 1920). Analogies between physical and evolutionary ‘forces’ have also been explored in the philosophy of ecology and evolution (C. Stephens, 2004; Justus, 2013; Sagoff, 2016). In Chapter 5 we introduce one such analogy, as well as extending a form of the model from (Ginzburg and Colyvan, 2004).

6

### **1.4 Outline**

This thesis covers my work in developing biophysical models for RNA-seq data analysis and evolution. We begin with a joint model for integrating RNA-seq and ATAC-seq data, and exploring an extension of the telegraph model to correlated gene neighbors. This model draws inspiration from the Ising model in physics. Chapter 3 then explores the extension of current biophysical models to another modality, protein counts, by combining bursty transcription and constitutive translation. This is work carried out along with Meichen Fang, and we show theoretical results for this extended model, as well as fits to experimental data. Chapter 4 explores the integration of biophysical modeling into phylogenetic inference techniques. I explore the question of disentangling the different mechanisms involved in gene expression evolution. In the final chapter, I continue my focus on evolution, this time using the equivalence of two equations, the virial theorem in physics, and the Price equation in evolutionary biology, to inspire new models. I suggest that a gestational maternal effect should be included in our most basic second-order models for population growth, and join Ginzburg and Colyvan in suggesting that analogies between ecology and astrophysics could be illuminating in describing complex populational dynamics. Finally, I summarize the implications of this work, as well as possible future directions.

7

_C h a p t e r 2_

---

[← TABLE OF CONTENTS](05-table-of-contents.md) · [Up: contents](index.md) · [BIOPHYSICAL MODEL FOR JOINT ANALYSIS OF CHROMATIN AND RNA SEQUENCING DATA →](07-biophysical-model-for-joint-analysis-of-chromatin-and-rna-se.md)
