---
title: FUTURE DIRECTIONS
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# FUTURE DIRECTIONS

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Overall, I hope that this thesis exemplifies the utility of using inspiration from physics in approaching biological questions. Whilst the different kinds of complexity encountered in biological processes render description in terms of fundamental laws more difficult, there is still value in considering how much can be explained via simple, foundational models. I have used the most basic concepts from condensed matter (C. Felce, G. Gorin, and L. Pachter, 2024), and mechanics (Catherine Felce, Liorsdóttir, and Lior Pachter, 2025), to suggest new models for biological data and ecological cycles. I hope that both of these approaches will be expanded upon, as their value lies partly in the existing physics machinery which has been developed to characterize systems obeying these dynamics. For example, the linear Ising-like model introduced for chromatin in Chapter 2 could be extended to a non-linear model of chromatin connectivity informed by Hi-C data. Ising model behavior for general graph structures has been widely studied in physics (Dorogovtsev, Goltsev, and J. F. F. Mendes, 2002; Dembo and Montanari, 2010), potentially allowing us to leverage existing theory to reach new insights.

I have built on the Pachter lab’s mission to expand the purview of principled biophysical models to explain new datatypes (Catherine Felce, Fang, and Lior Pachter, 2025). I hope that this represents a contribution to building on our understanding of biology ‘from the ground up’. Whilst this is not the approach that, for example, gives the most immediate clinical applications, I think that it should be valued from the perspective of pure understanding. A biologist’s mindset towards transcription tends to focus on the causes and effects of transcription _in flux_ . Their interest lies in cases where transcriptional or translational rates change due to regulation, rather than when stochastic noise dominates in basal transcription. In contrast, physics reduces processes down to the normal, with some of the greatest advances coming from noting how objects behave _without_ external intervention (Galilei, 1957). Along with other biologists (Milo and Phillips, 2015), I believe in the value of ‘recognizing regularities’ in these fundamental biological processes, and precisely quantifying the typical transcriptional and translational function of cells using biophysical modeling.

95

Once the ‘normal’ behavior of a system has been precisely quantified, it is then that we can use anomalous behaviors to identify new biology. This methodology is the standard in physics, for example in astrophysics. As discussed in Chapter 5, deviations from the Virial theorem were used to discover dark matter. Deviations from expected spin-orbit dynamics in binary star systems can be used to infer the presence of third bodies (Catherine Felce and Fuller, 2023; Fuller and Catherine Felce, 2023). Along with Ginzburg and Colyvan (Ginzburg and Colyvan, 2004), I am optimistic that some of these approaches can be expanded to biological and ecological systems. If an inertial model with maternal effects can explain population cycles within a single species, deviations from these trajectories could help to recognize more complicated interactions. In line with this, extensions of the work in Chapter 5 include incorporating maternal effects into existing predator-prey graph models (Çelik et al., 2025).

One potentially powerful extension of the work described in this thesis lies in the combination of biophysically modeled parameters for protein expression, and phylogenetic comparative methods. As noted by (Dimayacyac et al., 2023b), whilst many PCM studies have effectively used mRNA levels as a proxy for protein expression, protein levels are closer to phenotype and the coupling of the two modalities can be complex. This idea motivated (Cope, Schraiber, and Pennell, 2024) in their study of the coevolution of protein and RNA levels. The framework introduced in (Catherine Felce, Cope, et al., 2025) could therefore be combined with biophysical parameters obtained from the inference procedure introduced in (Catherine Felce, Fang, and Lior Pachter, 2025), to corroborate and extend the insights from (Cope, Schraiber, and Pennell, 2024).

The models introduced in this thesis could also be extended to leverage more powerful machine learning techniques. Neural networks for PDE solving (Li et al., 2021) could be used to approximate the solutions of the extended chemical master equations described in Chapters 2 and 3, giving faster inference. Neural networks have also been shown to be effective at choosing between evolutionary models and constructing phylogenies, improving on the speed of maximum likelihood methods (Kulikov, Derakhshandeh, and Mayer, 2024). These and other techniques could be straightforwardly applied to the biophysical phylogenetics framework outlined in Chapter 4. With increased interest in model-based machine learning, the bayesian hierarchical approach described in Chapter 4 is well-suited for generalization to more complicated graphical models (Bishop, 2013). This is just one example

96

of how principled biophysical modeling, using inspiration and methodology from physics, allows us to create foundational frameworks which can easily be built upon to incorporate new techniques and harness new data types. These biophysical models balance interpretability and statistical power, and bring us closer to a more quantitative understanding of biology.

97

BIBLIOGRAPHY

- Abbott, B. P. et al. (Oct. 2017). “GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral”. In: _Phys. Rev. Lett._ 119 (16), p. 161101. doi: `10.1103/PhysRevLett.119.161101` . url: `https://link.aps.org/ doi/10.1103/PhysRevLett.119.161101` .

- Adams, Dean C. (Nov. 2012). “Comparing Evolutionary Rates for Different Phenotypic Traits on a Phylogeny Using Likelihood”. In: _Systematic Biology_ 62.2, pp. 181–192. issn: 1063-5157. doi: `10.1093/sysbio/sys083` . eprint: `https: / / academic . oup . com / sysbio / article - pdf / 62 / 2 / 181 / 24577504 / sys083.pdf` .

- Bergelson, Joy et al. (June 2021). “Functional Biology in Its Natural Context: A Search for Emergent Simplicity”. In: _eLife_ 10, e67646. issn: 2050-084X. doi: `10.7554/eLife.67646` .

- Bishop, Christopher M. (Feb. 2013). “Model-Based Machine Learning”. In: _Philosophical transactions. Series A, Mathematical, physical, and engineering sciences_ 371.1984, p. 20120222. issn: 1364-503X. doi: `10.1098/rsta.2012.0222` . (Visited on 11/05/2025).

- Blekhman, Ran et al. (Nov. 2008). “Gene Regulation in Primates Evolves under Tissue-Specific Selection Pressures”. In: _PLOS Genetics_ 4.11, pp. 1–13. doi: `10.1371/journal.pgen.1000271` .

- Bohrer, Christopher H. and Elijah Roberts (Feb. 2016). “A Biophysical Model of Supercoiling Dependent Transcription Predicts a Structural Aspect to Gene Regulation”. In: _BMC Biophysics_ 9.1, p. 2. issn: 2046-1682. doi: `10.1186/ s13628-016-0027-0` .

- Bullard, James H. et al. (Feb. 2010). “Evaluation of Statistical Methods for Normalization and Differential Expression in mRNA-Seq Experiments”. In: _BMC Bioinformatics_ 11.1, p. 94. issn: 1471-2105. doi: `10.1186/1471-2105-11-94` .

- Butler, Marguerite A. and Aaron A. King (2004). “Phylogenetic Comparative Analysis: A Modeling Approach for Adaptive Evolution.” In: _The American Naturalist_ 164.6, pp. 683–695. doi: `10.1086/426002` . eprint: `https://doi.org/10. 1086/426002` .

- Cao, Zhixing, Yiling Wang, and Ramon Grima (Jan. 2025). “Deterministic Patterns in Single-Cell Transcriptomic Data”. In: _npj Systems Biology and Applications_ 11.1, p. 6. issn: 2056-7189. doi: `10.1038/s41540-025-00490-5` .

- Çelik, Türkü Özlüm et al. (2025). _Strata of Ecological Coexistence via Grassmannians_ . arXiv: `2509.00165 [math.AG]` . url: `https://arxiv.org/abs/2509. 00165` .

98

- Chari and Pachter (2024). “Biophysically interpretable inference of cell types from multimodal sequencing data”. In: _Nature Computational Science_ 4.9, pp. 677– 689. doi: `10.1038/s43588-024-00689-2` .

- Chari, Tara and Lior Pachter (Aug. 2023). “The Specious Art of Single-Cell Genomics”. In: _PLOS Computational Biology_ 19.8, e1011288. issn: 1553-7358. doi: `10.1371/journal.pcbi.1011288` . (Visited on 11/05/2025).

- Cope, Alexander L., Joshua G. Schraiber, and Matthew Pennell (2024). “Macroevolutionary divergence of gene expression shaped by selection on protein abundance”. In: _bioRxiv_ . Preprint. doi: `10.1101/2024.07.08.602411` . url: `https: //doi.org/10.1101/2024.07.08.602411` .

- Cusanovich, Darren A. et al. (May 2015). “Multiplex single-cell profiling of chromatin accessibility by combinatorial cellular indexing”. In: _Science_ 348.6237, pp. 910–914. issn: 0036-8075, 1095-9203. doi: `10.1126/science.aab1601` .

- Dada, Joseph O. and Pedro Mendes (Feb. 2011). “Multi-Scale Modelling and Simulation in Systems Biology”. In: _Integrative Biology_ 3.2, pp. 86–96. issn: 17579708. doi: `10.1039/c0ib00075b` . (Visited on 11/08/2025).

- Dal Molin, Alessandra, Giacomo Baruzzo, and Barbara Di Camillo (2017). “SingleCell RNA-Sequencing: Assessment of Differential Expression Analysis Methods”. In: _Frontiers in Genetics_ 8, p. 62. issn: 1664-8021. doi: `10.3389/fgene. 2017.00062` .

- Das, Samarendra, Anil Rai, and Shesh N. Rai (July 2022). “Differential Expression Analysis of Single-Cell RNA-Seq Data: Current Statistical Approaches and Outstanding Challenges”. In: _Entropy (Basel, Switzerland)_ 24.7, p. 995. issn: 1099-4300. doi: `10.3390/e24070995` .

- Dembo, Amir and Andrea Montanari (Apr. 2010). “Ising Models on Locally Treelike Graphs”. In: _The Annals of Applied Probability_ 20.2, pp. 565–592. issn: 1050-5164, 2168-8737. doi: `10.1214/09-AAP627` . (Visited on 11/08/2025).

- Dhar, Pawan K. and Alessandro Giuliani (2010). “Laws of biology: why so few?” In: _Systems and Synthetic Biology_ 4.1, pp. 7–13. doi: `10.1007/s11693-0099049-0` .

- Dibán, María José and Luis Felipe Hinojosa (Jan. 2024). “Testing the Tropical Niche Conservatism Hypothesis: Climatic Niche Evolution of Escallonia Mutis Ex L. F. (Escalloniaceae)”. In: _Plants (Basel, Switzerland)_ 13.1, p. 133. issn: 2223-7747. doi: `10.3390/plants13010133` .

- Dimayacyac, Jose Rafael et al. (Dec. 2023a). “Evaluating the Performance of Widely Used Phylogenetic Models for Gene Expression Evolution”. In: _Genome Biology and Evolution_ 15.12, evad211. doi: `10. 1093 / gbe /evad211` . url: `https : //doi.org/10.1093/gbe/evad211` .

99

- Dimayacyac, Jose Rafael et al. (Nov. 2023b). “Evaluating the Performance of Widely Used Phylogenetic Models for Gene Expression Evolution”. In: _Genome Biology and Evolution_ 15.12, evad211. issn: 1759-6653. doi: `10.1093/gbe/evad211` . eprint: `https://academic.oup.com/gbe/article-pdf/15/12/evad211/ 54912015/evad211.pdf` .

- Dorogovtsev, S. N., A. V. Goltsev, and J. F. F. Mendes (July 2002). “Ising model on networks with an arbitrary distribution of connections”. In: _Phys. Rev. E_ 66 (1), p. 016104. doi: `10.1103/PhysRevE.66.016104` . url: `https://link.aps. org/doi/10.1103/PhysRevE.66.016104` .

- Ellis, George F. R. and Jonathan Kopel (Jan. 2019). “The Dynamical Emergence of Biology From Physics: Branching Causation via Biomolecules”. In: _Frontiers in Physiology_ 9, p. 1966. issn: 1664-042X. doi: `10.3389/fphys.2018.01966` . (Visited on 11/08/2025).

- ENCODE Project Consortium (2012). “An integrated encyclopedia of DNA elements in the human genome”. In: _Nature_ 489.7414, pp. 57–74. doi: `10.1038/ nature11247` .

- Falkowski, Adam (2023). “Lectures on SMEFT”. In: _European Physical Journal C_ 83.656. doi: `10.1140/epjc/s10052-023-11821-3` . url: `https://doi.org/ 10.1140/epjc/s10052-023-11821-3` .

- Felce, C., G. Gorin, and L. Pachter (Dec. 2024). “Biophysical model for joint analysis of chromatin and RNA sequencing data”. In: _Phys. Rev. E_ 110 (6), p. 064405. doi: `10.1103/PhysRevE.110.064405` . url: `https://link.aps.org/doi/ 10.1103/PhysRevE.110.064405` .

- Felce, Catherine, Alexander L. Cope, et al. (2025). “Biophysical Constraints on mRNA Decay Rates Shape Macroevolutionary Divergence in Steady-State Abundances”. In: _bioRxiv_ . doi: `10.1101/2025.11.24.690267` . eprint: `2025.11.24. 690267` . url: `https://doi.org/10.1101/2025.11.24.690267` .

- Felce, Catherine, Meichen Fang, and Lior Pachter (2025). “Joint Biophysical Modeling of Paired Single-Cell RNA and Protein Measurements”. In: _bioRxiv_ . doi: `10.1101/2025.11.14.688548` . eprint: `2025.11.14.688548` . url: `https: //doi.org/10.1101/2025.11.14.688548` .

- Felce, Catherine and Jim Fuller (Oct. 2023). “Slowly Rotating Close Binary Stars in Cassini States”. In: _Monthly Notices of the Royal Astronomical Society_ 526.4, pp. 6168–6180. issn: 0035-8711. doi: `10 . 1093 / mnras / stad3053` . eprint: `https : / / academic . oup . com / mnras / article - pdf / 526 / 4 / 6168 / 52633417/stad3053.pdf` .

- Felce, Catherine, Steinunn Liorsdóttir, and Lior Pachter (Nov. 2025). “Analogies between the virial theorem and the Price equation”. In: _Phys. Rev. E_ 112 (5), p. 054139. doi: `10.1103/r8bd-lhm3` . url: `https://link.aps.org/doi/10. 1103/r8bd-lhm3` .

100

- Felsenstein, Joseph (1985). “Phylogenies and the Comparative Method”. In: _The American Naturalist_ 125.1, pp. 1–15. issn: 00030147, 15375323. url: `http: //www.jstor.org/stable/2461605` (visited on 11/04/2025).

- (1988). “Phylogenies and Quantitative Characters”. In: _Annual Review of Ecology and Systematics_ 19, pp. 445–471. doi: `10.1146/annurev.es.19.110188. 002305` . url: `https://www.jstor.org/stable/2097162` .

- Fuller, Jim and Catherine Felce (Oct. 2023). “Super Slowly Spinning Stars in Close Binaries”. In: _Monthly Notices of the Royal Astronomical Society: Letters_ 527.1, pp. L103–L109. issn: 1745-3925. doi: `10.1093/mnrasl/slad150` . eprint: `https://academic.oup.com/mnrasl/article-pdf/527/1/L103/ 54610279/slad150.pdf` .

- Galilei, Galileo (1957). “On Motion”. In: _Discoveries and Opinions of Galileo_ . Ed. and trans. by Stillman Drake. New York: Doubleday, pp. 1–109.

- Gates, David M. (1975). “Introduction: Biophysical Ecology”. In: _Perspectives of Biophysical Ecology_ . Ed. by David M. Gates and Rudolf B. Schmerl. Berlin, Heidelberg: Springer Berlin Heidelberg, pp. 1–28. isbn: 978-3-642-87810-7. doi: `10.1007/978-3-642-87810-7_1` .

- Ginzburg, Lev and Mark Colyvan (2004). _Ecological orbits: How planets move and populations grow_ . Oxford University Press.

- Gorin, Gennady, Meichen Fang, et al. (2022). “RNA velocity unraveled”. In: _PLoS Computational Biology_ 18.9. Version 2, published September 12, 2022, e1010492. doi: `10.1371/journal.pcbi.1010492` . url: `https://doi.org/ 10.1371/journal.pcbi.1010492` .

- Gorin, Gennady, John J Vastola, et al. (2022). “Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments”. In: _Nature Communications_ 13.1, p. 7620. doi: `10.1038/s41467022-34857-7` .

- Grima, Ramon and Pierre-Marie Esmenjaud (2024). “Quantifying and Correcting Bias in Transcriptional Parameter Inference from Single-Cell Data”. In: _Biophysical Journal_ 123.1, pp. 4–30. issn: 0006-3495. doi: `10.1016/j.bpj.2023.10. 021` .

- GTEx Consortium (2015). “The Genotype-Tissue Expression (GTEx) pilot analysis: Multitissue gene regulation in humans”. In: _Science_ 348.6235, pp. 648–660. doi: `10.1126/science.1262110` .

- Hadfield, J. D. and S. Nakagawa (Mar. 2010). “General Quantitative Genetic Methods for Comparative Biology: Phylogenies, Taxonomies and Multi-trait Models for Continuous and Categorical Characters”. In: _Journal of Evolutionary Biology_ 23.3, pp. 494–508. issn: 1010-061X. doi: `10.1111/j.1420- 9101.2009. 01915.x` . eprint: `https://academic.oup.com/jeb/article-pdf/23/3/ 494/54530878/jevbio0494.pdf` .

101

- Hill, Mark S., Pétra Vande Zande, and Patricia J. Wittkopp (Apr. 2021). “Molecular and Evolutionary Processes Generating Variation in Gene Expression”. In: _Nature Reviews. Genetics_ 22.4, pp. 203–215. issn: 1471-0064. doi: `10.1038/s41576020-00304-w` .

- Huang,Jinghan, PhillipS.C.Yam,andNelsonL.S.Tang(2025). “‘Trans-differentiation of Neutrophils from Plasmablast’ Is an Artefact Caused by over-Reliance on Machine Algorithms in Single Cell RNA Sequencing Analysis: Lesson Learnt and Steps Ahead”. In: _bioRxiv : the preprint server for biology_ . doi: `10.1101/2025. 02.07.636761` . eprint: `https://www.biorxiv.org/content/early/2025/ 02/07/2025.02.07.636761.full.pdf` .

- Justus, James (2013). “Philosophical Issues in Ecology”. In: _The Philosophy of Biology_ . Ed. by Kostas Kampourakis. Vol. 1. Dordrecht: Springer Netherlands, pp. 343–371. isbn: 978-94-007-6536-8 978-94-007-6537-5. doi: `10.1007/97894-007-6537-5_17` . (Visited on 11/09/2025).

- Kim, Jong Kyoung and John C. Marioni (Jan. 2013). “Inferring the Kinetics of StochasticGeneExpressionfromSingle-CellRNA-sequencingData”. In: _Genome Biology_ 14.1, R7. issn: 1474-760X. doi: `10.1186/gb-2013-14-1-r7` .

- Klemm, Sandy L., Zohar Shipony, and William J. Greenleaf (Jan. 2019). “Chromatin accessibility and the regulatory epigenome”. In: _Nature Reviews Genetics_ 20.4, pp. 207–220. doi: `10.1038/s41576-018-0089-8` . url: `https://doi.org/ 10.1038/s41576-018-0089-8` .

- Kulikov, Nikita, Fatemeh Derakhshandeh, and Christoph Mayer (2024). “Machine Learning Can Be as Good as Maximum Likelihood When Reconstructing Phylogenetic Trees and Determining the Best Evolutionary Model on Four Taxon Alignments”. In: _Molecular Phylogenetics and Evolution_ 200, p. 108181. issn: 1055-7903. doi: `10.1016/j.ympev.2024.108181` .

- Lander, E. S. et al. (2001). “Initial sequencing and analysis of the human genome”. In: _Nature_ 409.6822, pp. 860–921. doi: `10.1038/35057062` .

- Larsson, Anton J. M. et al. (Jan. 2019). “Genomic Encoding of Transcriptional Burst Kinetics”. In: _Nature_ 565.7738, pp. 251–254. issn: 1476-4687. doi: `10.1038/ s41586-018-0836-1` .

- Li, Zongyi et al. (2021). _Fourier Neural Operator for Parametric Partial Differential Equations_ . arXiv: `2010.08895 [cs.LG]` . url: `https://arxiv.org/abs/ 2010.08895` .

- Lotka, Alfred J. (1920). “Analytical Note on Certain Rhythmic Relations in Organic Systems”. In: _Proceedings of the National Academy of Sciences_ 6.7, pp. 410–415. doi: `10.1073/pnas.6.7.410` . eprint: `https://www.pnas.org/doi/pdf/10. 1073/pnas.6.7.410` .

- Mahler, D. Luke et al. (2013). “Exceptional convergence on the macroevolutionary landscape in island lizard radiations”. In: _Science_ 341.6143, pp. 292–295. issn: 0036-8075. doi: `10.1126/science.1232392` .

102

- Mendes, Fábio K et al. (July 2018). “A Multispecies Coalescent Model for Quantitative Traits”. In: _eLife_ 7. Ed. by Patricia J Wittkopp, Antonis Rokas, and Matthew Pennell, e36482. issn: 2050-084X. doi: `10.7554/eLife.36482` .

- Milo, Ron and Rob Phillips (2015). _Cell Biology by the Numbers_ . 1st. Illustrated by Nigel Orme. New York: Garland Science (Taylor & Francis Group), p. 400. isbn: 9780815345374. doi: `10.1201/9780429258770` .

- Modin,KlasandMiloViviani(2022). “Canonicalscaleseparationintwo-dimensional incompressible hydrodynamics”. In: _Journal of Fluid Mechanics_ 943, A36. doi: `10.1017/jfm.2022.457` .

- Montévil, Maël et al. (Oct. 2016). “Theoretical Principles for Biology: Variation”. In: _Progress in Biophysics and Molecular Biology_ 122.1, pp. 36–50. issn: 18731732. doi: `10.1016/j.pbiomolbio.2016.08.005` .

- Mortazavi, Ali et al. (2008). “Mapping and quantifying mammalian transcriptomes by RNA-Seq”. In: _Nature Methods_ 5.7, pp. 621–628. doi: `10.1038/nmeth.1226` .

- O’Meara, Brian C. (2012). “Evolutionary Inferences from Phylogenies: A Review of Methods”. In: _Annual Review of Ecology, Evolution, and Systematics_ 43.Volume 43, 2012, pp. 267–285. issn: 1545-2069. doi: `10.1146/annurev-ecolsys110411-160331` .

- Phillips, Rob and Stephen R. Quake (May 2006). “The Biological Frontier of Physics”. In: _Physics Today_ 59.5, pp. 38–43. doi: `10.1063/1.2216960` . url: `https://physicstoday.aip.org/features/the-biological-frontierof-physics` .

- Price, Peter D. et al. (July 2022). “Detecting Signatures of Selection on Gene Expression”. In: _Nature Ecology & Evolution_ 6.7, pp. 1035–1045. issn: 2397334X. doi: `10.1038/s41559-022-01761-8` .

- Sagoff, Mark (2016). “Are There General Causal Forces in Ecology?” In: _Synthese_ 193.9. doi: `10.1007/s11229-015-0907-x` .

- Schadt, Eric E. et al. (Sept. 2010). “Computational Solutions to Large-Scale Data Management and Analysis”. In: _Nature Reviews Genetics_ 11.9, pp. 647–657. issn: 1471-0064. doi: `10.1038/nrg2857` .

- Stephens, Christopher (2004). “Selection, Drift, and the ?Forces? Of Evolution”. In: _Philosophy of Science_ 71.4, pp. 550–570. doi: `10.1086/423751` .

- Stephens, Zachary D. et al. (2015). “Big Data: Astronomical or Genomical?” In: _PLOS Biology_ 13.7, e1002195. doi: `10.1371/journal.pbio.1002195` . url: `https://doi.org/10.1371/journal.pbio.1002195` .

- Stoeckius, Marlon et al. (2017). “Simultaneous epitope and transcriptome measurement in single cells”. In: _Nature Methods_ 14, pp. 865–868. doi: `10.1038/nmeth. 4380` .

103

- Tang, Fuchou et al. (2009). “mRNA-Seq whole-transcriptome analysis of a single cell”. In: _Nature Methods_ 6.5, pp. 377–382. doi: `10.1038/nmeth.1315` .

- Wang, Tianyu et al. (Jan. 2019). “Comparative Analysis of Differential Gene Expression Analysis Tools for Single-Cell RNA Sequencing Data”. In: _BMC Bioinformatics_ 20.1, p. 40. issn: 1471-2105. doi: `10.1186/s12859-019-2599-6` .

- Wang, Xiaojing, Qi Liu, and Bing Zhang (Dec. 2014). “Leveraging the Complementary Nature of RNA-Seq and Shotgun Proteomics Data”. In: _Proteomics_ 14.0, pp. 2676–2687. issn: 1615-9853. doi: `10.1002/pmic.201400184` . (Visited on 11/04/2025).

- Wilson, Kenneth G. (2025). _Kenneth G. Wilson – Nobel Lecture_ . NobelPrize.org. Accessed 2025-12-12. url: `https://www.nobelprize.org/prizes/physics/ 1982/wilson/lecture/` .

104

_A p p e n d i x A_

---

[← PHYSICAL MODELS IN POPULATION EVOLUTION](10-physical-models-in-population-evolution.md) · [Up: contents](index.md) · [ATAC SUPPLEMENTARY INFORMATION →](12-atac-supplementary-information.md)
