---
title: FUTURE DIRECTIONS
source: https://thesis.library.caltech.edu/17389/
source_file: sources/fang-2025-biophysical-normalisation/Thesis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# FUTURE DIRECTIONS

**Source:** `Thesis.pdf` from [fang-2025-biophysical-normalisation](https://thesis.library.caltech.edu/17389/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Gorin, Gennady, John J Vastola, Meichen Fang, and Lior Pachter (2022). “Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments”. In: _Nat. Commun._ 13.1, p. 7620. doi: `10.1038/s41467-022-34857-7` .

In this thesis, we advocate for a balanced coexistence of the two cultures in singlecell RNA sequencing analysis. The ideal approach is a balanced integration of data models and algorithmic models based on the questions at hand. For example, we can begin by exploring the data with algorithmic models, which provide a broad overview. Then, based on those exploratory results, we can build data models to closely examine the underlying biological mechanisms. With these mechanistic insights, we can develop more suitable and biologically informed algorithmic models. Such integration can enhance both the efficiency and depth of scRNA-seq data analysis.

In line with this perspective, we present two mechanistic models for normalization and trajectory inference. Our emphasis lies in the interpretability afforded by biophysically inspired models and the rigor of principled statistical inference, which together enable more meaningful insights into the underlying biological processes. However, our models are admittedly naive and raise more questions than they answer. They are oversimplified and cannot account for all sources of variation. In the extrinsic noise model, a single random variable is insufficient even mature counts in pseudo-cells. In the process time model, the assumption of piecewiseconstant transcription rates is unlikely to hold in realistic biological systems. We can keep listing the assumptions and simplification that we made for our models. After all, models are a compromise between tractability and the complexity of the real world. A mechanistic model must be simple enough to allow full inference from the available experimental data.

This constraint can be seen as both an advantage and a limitation, as developing mechanistic models depends more heavily on an iterative interplay between experimental data and theoretical development. The limitation is that model cannot be

101

improved until more informative experiments appear. For example, in the context of scRNA-seq normalization, more experiments need to be done to characterize technical noise in each scRNA-seq methods.

In an ideal scenario, scRNA-seq would achieve the same level of precision and reproducibility as physics experiments. For example, just as all free-fall experiments conducted under the same conditions yield virtually identical measurements of gravitational acceleration, each scRNA-seq experiment using the same protocol would produce data with consistent and predictable technical noise. This would allow biological variability to be interpreted with the same confidence physicists place in natural constants.

Currently, reproducibility in single-cell RNA-seq is often assessed by comparing mean expression levels across experiments. However, what truly matters is the full distribution of gene expression, not just the average. This is analogous to measuring gravity: while all objects may hit the ground, the defining feature of gravity is the consistent acceleration, not merely the fact that they fall.

The advantage of this constraint is that it helps guide rational experimental design. As we demonstrated in (Gorin, Vastola, Fang, et al., 2022), in a closed-loop framework for the rational design of transcriptomics experiments, mathematical analysis informs the design of experiments that are maximally informative for distinguishing between competing hypotheses, such as the CIR and Γ-OU models for transcription rates (Figure 5.1). Unfortunately, our work focused on the theoretical analysis and model fitting aspects of this framework, the experimental feedback loop remains to be completed. Outside of scRNA-seq, prior work in fluorescence-based transcriptomics has demonstrated the use of Fisher information criteria to optimize experimental design and detect environmental fluctuations from time-course data (Fox, Neuert, and Munsky, 2020). These studies highlight the feasibility and value of closing the loop between model development and experimental validation, which is particularly lacking in the field of scRNA-seq.

Even in the era of big data, not all data are equally informative. The value of a dataset depends not merely on its size, but on how well it is aligned with the specific scientific question being addressed. Therefore, mechanistic models remain valuable for enabling researchers to design experiments that gather the right data, not just more data, even if their interpretability and capacity for rigorous inference are set aside.

102


<!-- Start of picture text -->
a.         Hypothesis-driven          Use data to refine          & reject models b. K ( t ) nascent RNA β mature RNA<br>transcriptomics experiment A  A’<br>γ<br>B dKdt = � reversionmean � + [ noise ] ∅<br>         Model-based rational design        of transcriptomics experiments   Interpretable & tractable models c. Candidate models: Gamma Ornstein–Uhlenbeck (Γ-OU)<br>Cox–Ingersoll–Ross (CIR)<br>ID most informative Mathematical<br>stress stress relief<br>         experiment       analysis A B Γ-OU<br>Distributions Pss ( xN , xM ) (DNA mechanics)<br>Moments µN Cov( µMXNσ, XN 2 M ) σM 2 bind unbind   bind<br>Autocorrelations RN ( τ ) RM ( τ ) CIR<br>(Gene regulation)<br><!-- End of picture text -->

Figure 5.1: Framework for the rational design of transcriptomics experiments. **a)** Model-based closed loop paradigm. A researcher begins by representing two or more competing hypotheses as interpretable and tractable mathematical models (middle right of circle). Next, they perform a detailed mathematical analysis of each model, computing quantities (e.g., RNA count distributions and moments) that can help distinguish one hypothesis from another. Using the results of that analysis as input, they identify the experiment that best distinguishes the two models. Finally, they perform this experiment on some population of cells, use the resulting data to refine and/or reject models, and repeat the process with an updated ensemble of models. **b)** Interpretable and tractable modeling framework for transcription rate variation. We consider stochastic models of transcription involving (i) nascent/unspliced RNA, (ii) mature/spliced RNA, and (iii) a stochastic and time-varying transcription rate _𝐾_ ( _𝑡_ ). The transcription rate is assumed to evolve in time according to a simple, onedimensional SDE that includes a mean-reversion term (which tends to push _𝐾_ ( _𝑡_ ) towards its mean value) and a noise term (which causes _𝐾_ ( _𝑡_ ) to randomly fluctuate). Here, we have specifically chosen dynamics for which the long-time probability distribution of _𝐾_ ( _𝑡_ ) is a gamma distribution (gray curve), because this assumption yields empirically plausible negative binomial-like RNA distributions. However, the framework does not require this in general. **c)** Two plausible models studied in this paper. The gamma Ornstein–Uhlenbeck (Γ-OU) model describes DNA m echanics, whereas the Cox–Ingersoll–Ross (CIR) model describes regulation by a high copy number regulator.

103

BIBLIOGRAPHY

- 10x Genomics (2021a). _10k 1:1 Mixture of Human HEK293T and Mouse NIH3T3 Cells, 3’ v3.1, Chromium Controller_ . Dataset published on August 9, 2021. Licensed under CC BY 4.0. url: `https://www.10xgenomics.com/datasets/ 10-k-1-1-mixture-of-human-hek-293-t-and-mouse-nih-3-t-3cells-3-v-3-1-chromium-controller-3-1-standard-6-1-0` .

- (2021b). _10k 1:1 Mixture of Human HEK293T and Mouse NIH3T3 Cells, 3’ v3.1, Chromium X_ . Dataset published on August 9, 2021. Licensed under CC BY 4.0. url: `https://www.10xgenomics.com/datasets/10-k-1-1-mixtureof- human- hek- 293- t- and- mouse- nih- 3- t- 3- cells- 3- v- 3- 1- chromium-x-3-1-standard-6-1-0` .

- (2021c). _20k 1:1 Mixture of Human HEK293T and Mouse NIH3T3 Cells, 3’ HT v3.1_ . Dataset published on August 9, 2021. Licensed under CC BY 4.0. url: `https://www.10xgenomics.com/datasets/20-k-1-1-mixture-ofhuman-hek-293-t-and-mouse-nih-3-t-3-cells-3-ht-v-3-1-3-1high-6-1-0` .

- (2022). _K562-r cells (Next GEM), Flex Gene Expression Dataset by Cell Ranger 7.0.0_ . Accessed:2025-05-11. url: `https://www.10xgenomics.com/datasets/ 10k-human-k562-r-cells-singleplex-sample-1-standard` .

- (2023). _10k Mouse Forebrain FFPE Tissue Dissociated using gentleMACS Dissociator, Singleplex Sample (Next GEM)_ . Accessed: 2025-05-11. url: `https: / / www . 10xgenomics . com / datasets / 10k - mouse - forebrain - ffpe - tissue-dissociated-using-gentlemacs-dissociator-singleplexsample-1-standard` .

- (2024). _10k Human PBMCs Stained with TotalSeq™-B Human Universal Cocktail, Singleplex Sample (Next GEM)_ . Accessed: 2025-05-11. url: `https:// www.10xgenomics.com/datasets/10k-human-pbmcs-stained-withtotalseq - b - human - universal - cocktail - singleplex - sample - 1 - standard` .

- Abu-Mostafa, Yaser S, Malik Magdon-Ismail, and Hsuan-Tien Lin (2012). _Learning from data_ . Vol. 4. AMLBook New York.

- Ahlmann-Eltze, Constantin and Wolfgang Huber (2023). “Comparison of transformations for single-cell RNA-seq data”. In: _Nat. Methods_ 20, pp. 665–672. doi: `10.1038/s41592-023-01814-1` .

- Aivazidis, Alexander et al. (2023). “Model-based inference of RNA velocity modules improves cell fate prediction”. In: _bioRxiv_ , p. 2023.08.03.551650. doi: `10. 1101/2023.08.03.551650` .

104

- Aniweh, Yaw et al. (2019). “SMIM1 at a glance; discovery, genetic basis, recent progress and perspectives”. In: _Parasite Epidemiol Control_ 5, e00101. doi: `10. 1016/j.parepi.2019.e00101` .

- Assaf, Michael and Baruch Meerson (2017). “WKB theory of large deviations in stochastic populations”. In: _J. Phys. A: Math. Theor._ 50, p. 263001. doi: `10.1088/1751-8121/aa669a` .

- Bacher, Rhonda et al. (2017). “SCnorm: robust normalization of single-cell RNAseq data”. In: _Nat. Methods_ 14, pp. 584–586. doi: `10.1038/nmeth.4263` .

- Baras, F, M Malek Mansour, and J E Pearson (1996). “Microscopic simulation of chemical bistability in homogeneous systems”. In: _J. Chem. Phys._ 105, pp. 8257– 8261. doi: `10.1063/1.472679` .

- Baron, Margaret H, Joan Isern, and Stuart T Fraser (2012). “The embryonic origins of erythropoiesis in mammals”. In: _Blood_ 119, pp. 4828–4837. doi: `10.1182/ blood-2012-01-153486` .

- Battich, Nico, Joep Beumer, et al. (2020). “Sequencing metabolically labeled transcriptsinsinglecellsrevealsmRNAturnoverstrategies”. In: _Science_ 367,pp. 1151– 1156. doi: `10.1126/science.aax3072` .

- Battich, Nico, Thomas Stoeger, and Lucas Pelkmans (2015). “Control of Transcript Variability in Single Mammalian Cells”. In: _Cell_ 163, pp. 1596–1610. doi: `10. 1016/j.cell.2015.11.018` .

- Bender, Carl M and Steven A Orszag (2010). _Advanced mathematical methods for scientists and engineers I: Asymptotic methods and perturbation theory_ . Springer. doi: `10.1007/978-1-4757-3069-2` .

- Bokes, Pavol (2022). “Stationary and Time-Dependent Molecular Distributions in Slow-Fast Feedback Circuits”. In: _SIAM J. Appl. Dyn. Syst._ 21, pp. 903–931. doi: `10.1137/21M1404338` .

- Booeshaghi, A Sina, Ingileif B Hallgrímsdóttir, et al. (2022). “Depth normalization for single-cell genomics count data”. In: _bioRxiv_ , p. 2022.05. 06.490859. doi: `10.1101/2022.05.06.490859` .

- Booeshaghi, A Sina and Lior Pachter (2021). “Normalization of single-cell RNA-seq counts by log (x+ 1) or log (1+ x)”. In: _Bioinformatics_ 37.15, pp. 2223–2224.

- Bray, Nicolas L et al. (2016). “Near-optimal probabilistic RNA-seq quantification”. In: _Nat. Biotechnol._ 34, pp. 525–527. doi: `10.1038/nbt.3519` .

- Breiman, Leo (2001). “Statistical Modeling: The Two Cultures (with comments and a rejoinder by the author)”. In: _SSO Schweiz. Monatsschr. Zahnheilkd._ 16, pp. 199–231. doi: `10.1214/ss/1009213726` .

- Brennecke, Philip et al. (2013). “Accounting for technical noise in single-cell RNAseq experiments”. In: _Nat. Methods_ 10, pp. 1093–1095. doi: `10.1038/nmeth. 2645` .

105

- Cadima, Jorge and Ian T Jolliffe (1995). “Loading and correlations in the interpretation of principle compenents”. In: _J. Appl. Stat._ 22, pp. 203–214. doi: `10.1080/757584614` .

- Campbell, Kieran R and Christopher Yau (2016). “Order Under Uncertainty: Robust Differential Expression Analysis Using Probabilistic Models for Pseudotime Inference”. In: _PLoS Comput. Biol._ 12, e1005212. doi: `10.1371/journal.pcbi. 1005212` .

- (2019). “A descriptive marker gene approach to single-cell pseudotime inference”. In: _Bioinformatics_ 35, pp. 28–35. doi: `10.1093/bioinformatics/bty498` .

- Cannoodt, Robrecht, Wouter Saelens, Louise Deconinck, et al. (2021). “Spearheading future omics analyses using dyngen, a multi-modal simulator of single cells”. In: _Nat. Commun._ 12, p. 3942. doi: `10.1038/s41467-021-24152-2` .

- Cannoodt, Robrecht, Wouter Saelens, and Yvan Saeys (2016). “Computational methods for trajectory inference from single-cell transcriptomics”. In: _Eur. J. Immunol._ 46, pp. 2496–2506. doi: `10.1002/eji.201646347` .

- Cao, Junyue et al. (2019). “The single-cell transcriptional landscape of mammalian organogenesis”. In: _Nature_ 566, pp. 496–502. doi: `10.1038/s41586- 0190969-x` .

- Chari, T and L Pachter (2021). “The specious art of single-cell genomics”. In: _PLOS Computational Biology_ 19. doi: `10.1371/journal.pcbi.1011288` .

- Chari, Tara, Gennady Gorin, and Lior Pachter (2024a). “Biophysically interpretable inference of cell types from multimodal sequencing data”. In: _Nat. Comput. Sci._ 4, pp. 677–689. doi: `10.1038/s43588-024-00689-2` .

- (2024b). “Stochastic modeling of biophysical responses to perturbation”. In: _bioRxivorg_ . doi: `10.1101/2024.07.04.602131` .

- Chen, Yiqun T and Daniela M Witten (2022). “Selective inference for k-means clustering”. In: _arXiv [stat.ME]_ .

- Dar, Roy D et al. (2012). “Transcriptional burst frequency and burst size are equally modulated across the human genome”. In: _Proc. Natl. Acad. Sci. U. S. A._ 109, pp. 17454–17459. doi: `10.1073/pnas.1213530109` .

- Deconinck, Louise et al. (2021). “Recent advances in trajectory inference from single-cell omics data”. In: _Current Opinion in Systems Biology_ 27, p. 100344. doi: `10.1016/j.coisb.2021.05.005` .

- Drummond, P D and C W Gardiner (1980). “Generalised P-representations in quantum optics”. In: _J. Phys. A Math. Gen._ 13, pp. 2353–2368. doi: `10.1088/ 0305-4470/13/7/018` .

- Du, Jin-Hong et al. (2024). “Joint trajectory inference for single-cell genomics using deep learning with a mixture prior”. In: _Proc. Natl. Acad. Sci. U. S. A._ 121, e2316256121. doi: `10.1073/pnas.2316256121` .

106

- Elowitz, Michael B et al. (2002). “Stochastic gene expression in a single cell”. In: _Science_ 297, pp. 1183–1186. doi: `10.1126/science.1070919` .

- Erhard, Florian et al. (2022). “Time-resolved single-cell RNA-seq using metabolic RNA labelling”. In: _Nat. Rev. Methods Primers_ 2, pp. 1–18. doi: `10.1038/ s43586-022-00157-z` .

- Feinberg, Martin (2019). _Foundations of chemical reaction network theory_ . 1st ed. Springer Nature. doi: `10.1007/978-3-030-03858-8` .

- Fox, Zachary R, Gregor Neuert, and Brian Munsky (2020). “Optimal design of single-cell experiments within temporally fluctuating environments”. In: _Complexity_ 2020, p. 8536365. doi: `10.1155/2020/8536365` .

- Fu, Audrey Qiuyan and Lior Pachter (2016). “Estimating intrinsic and extrinsic noise from single-cell gene expression measurements”. In: _Statistical applications in genetics and molecular biology_ 15.6, pp. 447–471.

- Gao, Lucy L, Jacob Bien, and Daniela Witten (2020). “Selective Inference for Hierarchical Clustering”. In: _arXiv [stat.ME]_ .

- Gardiner, Crispin (2009). _Stochastic Methods_ . Springer.

- Gillespie, Daniel T (2000). “The chemical Langevin equation”. In: _J. Chem. Phys._ 113, pp. 297–306. doi: `10.1063/1.481811` .

- Golding, Ido et al. (2005). “Real-time kinetics of gene activity in individual bacteria”. In: _Cell_ 123, pp. 1025–1036. doi: `10.1016/j.cell.2005.09.031` .

- Gorin, Gennady, Meichen Fang, et al. (2022). “RNA velocity unraveled”. In: _PLoS Comput. Biol._ 18, e1010492. doi: `10.1371/journal.pcbi.1010492` .

- Gorin, Gennady and Lior Pachter (2022a). “Modeling bursty transcription and splicing with the chemical master equation”. In: _Biophys. J._ 121, pp. 1056–1069. doi: `10.1016/j.bpj.2022.02.004` .

- (2022b). “Monod: mechanistic analysis of single-cell RNA sequencing count data”. In: _bioRxiv_ , p. 2022.06.11.495771. doi: `10.1101/2022.06.11.495771` .

- (2023). “Length biases in single-cell RNA sequencing of pre-mRNA”. In: _Biophys Rep (N Y)_ 3, p. 100097. doi: `10.1016/j.bpr.2022.100097` .

- (2024). “New and notable: Revisiting the “two cultures” through extrinsic noise”. In: _Biophys. J._ 123, pp. 1–3. doi: `10.1016/j.bpj.2023.11.3400` .

- Gorin, Gennady, John J Vastola, Meichen Fang, et al. (2022). “Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments”. In: _Nat. Commun._ 13, p. 7620. doi: `10.1038/ s41467-022-34857-7` .

- Gorin, Gennady, John J Vastola, and Lior Pachter (2023). “Studying stochastic systems biology of the cell with single-cell genomics data”. In: _Cell Syst._ 14, 822–843.e22. doi: `10.1016/j.cels.2023.08.004` .

107

- Graham, R and T Tél (1985). “Weak-noise limit of Fokker-Planck models and nondifferentiable potentials for dissipative dynamical systems”. In: _Phys. Rev. A Gen. Phys._ 31, pp. 1109–1122. doi: `10.1103/physreva.31.1109` .

- Griffiths, Jonathan A, Antonio Scialdone, and John C Marioni (2018). “Using singlecell genomics to understand developmental processes and cell fate decisions”. In: _Mol. Syst. Biol._ 14, e8046. doi: `10.15252/msb.20178046` .

- Grima, Ramon and Pierre-Marie Esmenjaud (2024). “Quantifying and correcting bias in transcriptional parameter inference from single-cell data”. In: _Biophys. J._ 123, pp. 4–30. doi: `10.1016/j.bpj.2023.10.021` .

- Grün, Dominic, Lennart Kester, and Alexander van Oudenaarden (2014). “Validation of noise models for single-cell transcriptomics”. In: _Nat. Methods_ 11, pp. 637–640. doi: `10.1038/nmeth.2930` .

- Grunberg, Theodore W and Domitilla Del Vecchio (2023). “A Stein’s Method approach to the Linear Noise Approximation for stationary distributions of Chemical Reaction Networks”. In: _arXiv [q-bio.QM]_ .

- Gu, Yichen, David Blaauw, and Joshua D Welch (2022). “Bayesian Inference of RNAVelocityfromMulti-LineageSingle-CellData”. In: _bioRxiv_ ,p.2022.07.08.499381. doi: `10.1101/2022.07.08.499381` .

- Hafemeister, Christoph and Rahul Satija (2019). “Normalization and variance stabilization of single-cell RNA-seq data using regularized negative binomial regression”. In: _Genome Biol._ 20, p. 296. doi: `10.1186/s13059-019-1874-1` .

- Haghverdi, Laleh et al. (2016). “Diffusion pseudotime robustly reconstructs lineage branching”. In: _Nat. Methods_ 13, pp. 845–848. doi: `10.1038/nmeth.3971` .

- Ham, Lucy et al. (2020). “Exactly solvable models of stochastic gene expression”. In: _J. Chem. Phys._ 152, p. 144106. doi: `10.1063/1.5143540` .

- Hanggi, Peter et al. (1984). “Bistable systems: Master equation versus Fokker-Planck modeling”. In: _Phys. Rev. A_ 29, pp. 371–378. doi: `10.1103/PhysRevA.29.371` .

- Hao, Yuhan et al. (2024). “Dictionary learning for integrative, multimodal and scalable single-cell analysis”. In: _Nat. Biotechnol._ 42, pp. 293–304. doi: `10. 1038/s41587-023-01767-y` .

- Hashimshony, Tamar et al. (2012). “CEL-Seq: single-cell RNA-Seq by multiplexed linear amplification”. In: _Cell Rep._ 2, pp. 666–673. doi: `10.1016/j.celrep. 2012.08.003` .

- Hilfinger, Andreas and Johan Paulsson (2011). “Separating intrinsic from extrinsic fluctuations in dynamic biological systems”. In: _Proc. Natl. Acad. Sci. U. S. A._ 108, pp. 12167–12172. doi: `10.1073/pnas.1018832108` .

- Jahnke, Tobias and Wilhelm Huisinga (2007). “Solving the chemical master equation for monomolecular reaction systems analytically”. In: _J. Math. Biol._ 54, pp. 1–26. doi: `10.1007/s00285-006-0034-x` .

108

- Ji, Zhicheng and Hongkai Ji (2016). “TSCAN: Pseudo-time reconstruction and evaluation in single-cell RNA-seq analysis”. In: _Nucleic Acids Res._ 44, e117. doi: `10.1093/nar/gkw430` .

- Jiao, Feng et al. (2024). “What can we learn when fitting a simple telegraph model to a complex gene expression model?” In: _PLoS Comput. Biol._ 20, e1012118. doi: `10.1371/journal.pcbi.1012118` .

- Johnson, Benjamin K et al. (2022). “Single-cell Total RNA Miniaturized sequencing (STORM-seq) reveals differentiation trajectories of primary human fallopian tube epithelium”. In: _bioRxiv_ , p. 2022.03.14.484332. doi: `10.1101/2022.03.14. 484332` .

- Kim, Jong Kyoung, Aleksandra A Kolodziejczyk, et al. (2015). “Characterizing noise structure in single-cell RNA-seq distinguishes genuine from technical stochastic allelic expression”. In: _Nat. Commun._ 6, p. 8687. doi: `10.1038/ ncomms9687` .

- Kim, Jong Kyoung and John C Marioni (2013). “Inferring the kinetics of stochastic gene expression from single-cell RNA-sequencing data”. In: _Genome Biol._ 14, R7. doi: `10.1186/gb-2013-14-1-r7` .

- Klein, Allon M et al. (2015). “Droplet barcoding for single-cell transcriptomics applied to embryonic stem cells”. In: _Cell_ 161, pp. 1187–1201. doi: `10.1016/ j.cell.2015.04.044` .

- Ko, M S (1991). “A stochastic model for gene induction”. In: _J. Theor. Biol._ 153, pp. 181–194. doi: `10.1016/s0022-5193(05)80421-7` .

- (1992). “Induction mechanism of a single gene molecule: stochastic or deterministic?” In: _Bioessays_ 14, pp. 341–346. doi: `10.1002/bies.950140510` .

- Ko, M S, HNakauchi,andNTakahashi(1990).“Thedosedependenceofglucocorticoidinducible gene expression results from changes in the number of transcriptionally active templates”. In: _EMBO J._ 9, pp. 2835–2842. doi: `10.1002/j.14602075.1990.tb07472.x` .

- Kriegeskorte, Nikolaus et al. (2009). “Circular analysis in systems neuroscience: the dangers of double dipping”. In: _Nat. Neurosci._ 12, pp. 535–540. doi: `10.1038/ nn.2303` .

- Kuchibhotla, Arun K, John E Kolassa, and Todd A Kuffner (2022). “Post-selection Inference”. In: _Annu. Rev. Stat. Appl._ doi: `10.1146/annurev-statistics100421-044639` .

- Kurtz, Thomas G (1972). “The relationship between stochastic and deterministic models for chemical reactions”. In: _J. Chem. Phys._ 57, pp. 2976–2978. doi: `10.1063/1.1678692` .

- (1978). “Strong approximation theorems for density dependent Markov chains”. In: _Stochastic Processes and their Applications_ 6, pp. 223–240. doi: `10.1016/ 0304-4149(78)90020-0` .

109

- La Manno, Gioele et al. (2018). “RNA velocity of single cells”. In: _Nature_ 560, pp. 494–498. doi: `10.1038/s41586-018-0414-6` .

- Lähnemann, David et al. (2020). “Eleven grand challenges in single-cell data science”. In: _Genome Biol._ 21, p. 31. doi: `10.1186/s13059-020-1926-6` .

- Larsson, Anton J M et al. (2019). “Genomic encoding of transcriptional burst kinetics”. In: _Nature_ 565, pp. 251–254. doi: `10.1038/s41586-018-0836-1` .

- Lause, Jan, Philipp Berens, and Dmitry Kobak (2021). “Analytic Pearson residuals for normalization of single-cell RNA-seq UMI data”. In: _Genome Biol._ 22, p. 258. doi: `10.1186/s13059-021-02451-7` .

- Lederer, Alex R et al. (2024). “Statistical inference with a manifold-constrained RNA velocitymodeluncoverscellcyclespeedmodulations”. In: _bioRxiv_ ,p.2024.01.18.576093. doi: `10.1101/2024.01.18.576093` .

- Li, Chenetal.(2022). “Multi-omicsingle-cellvelocitymodelsepigenome–transcriptome interactions and improves cell fate prediction”. In: _Nat. Biotechnol._ , pp. 1–12. doi: `10.1038/s41587-022-01476-y` .

- Lim, Hong Seo and Peng Qiu (2024). “Quantifying the clusterness and trajectoriness of single-cell RNA-seq data”. In: _PLoS Comput. Biol._ 20, e1011866. doi: `10. 1371/journal.pcbi.1011866` .

- Lin, Chieh and Ziv Bar-Joseph (2019). “Continuous-state HMMs for modeling time-series single-cell RNA-Seq data”. In: _Bioinformatics_ 35, pp. 4707–4715. doi: `10.1093/bioinformatics/btz296` .

- Luecken, Malte D and Fabian J Theis (2019). “Current best practices in single-cell RNA-seq analysis: a tutorial”. In: _Mol. Syst. Biol._ 15, e8746. doi: `10.15252/ msb.20188746` .

- Lun, Aaron T L, Karsten Bach, and John C Marioni (2016). “Pooling across cells to normalize single-cell RNA sequencing data with many zero counts”. In: _Genome Biol._ 17, p. 75. doi: `10.1186/s13059-016-0947-7` .

- Macosko, Evan Z et al. (2015). “Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets”. In: _Cell_ 161, pp. 1202–1214. doi: `10.1016/j.cell.2015.05.002` .

- Melsted, Páll et al. (2021). “Modular, efficient and constant-memory single-cell RNA-seq preprocessing”. In: _Nat. Biotechnol._ 39, pp. 813–818. doi: `10.1038/ s41587-021-00870-2` .

- Miller, O and S McKnight (1979). “Post-replicative nonribosomal transcription units in D. melanogaster embryos”. In: _Cell_ 17, pp. 551–563. doi: `10.1016/00928674(79)90263-0` .

- Mimitou, Eleni P et al. (2021). “Scalable, multimodal profiling of chromatin accessibility, gene expression and protein levels in single cells”. In: _Nat. Biotechnol._ 39, pp. 1246–1258. doi: `10.1038/s41587-021-00927-2` .

110

- Neufeld, Anna et al. (2023). “Inference after latent variable estimation for singlecell RNA sequencing data”. In: _Biostatistics_ 25, pp. 270–287. doi: `10.1093/ biostatistics/kxac047` .

- Öcal, Kaan (2023). “Incorporating extrinsic noise into mechanistic modelling of single-cell transcriptomics”. In: _bioRxiv_ , p. 2023.09.30.560282. doi: `10.1101/ 2023.09.30.560282` .

- Peccoud, J and B Ycart (1995). “Markovian Modeling of Gene-Product Synthesis”. In: _Theor. Popul. Biol._ 48, pp. 222–234. doi: `10.1006/tpbi.1995.1027` .

- Phillips, Rob (2015). “Theory in biology: Figure 1 or figure 7?” In: _Trends Cell Biol._ 25, pp. 723–729. doi: `10.1016/j.tcb.2015.10.007` .

- Pijuan-Sala, Blanca et al. (2019). “A single-cell molecular map of mouse gastrulation and early organogenesis”. In: _Nature_ 566, pp. 490–495. doi: `10.1038/s41586019-0933-9` .

- Qiu, Xiaojie et al. (2017). “Reversed graph embedding resolves complex single-cell trajectories”. In: _Nat. Methods_ 14, pp. 979–982. doi: `10.1038/nmeth.4402` .

- Rabani, Michal et al. (2011). “Metabolic labeling of RNA uncovers principles of RNA production and degradation dynamics in mammalian cells”. In: _Nat. Biotechnol._ 29, pp. 436–442. doi: `10.1038/nbt.1861` .

- Raj, Arjun et al. (2006). “Stochastic mRNA synthesis in mammalian cells”. In: _PLoS biology_ 4, e309.

- Ramsköld, Daniel, Gert-Jan Hendriks, et al. (2024). “Single-cell new RNA sequencing reveals principles of transcription at the resolution of individual bursts”. In: _Nat. Cell Biol._ 26, pp. 1725–1733. doi: `10.1038/s41556-024-01486-9` .

- Ramsköld, Daniel, Shujun Luo, et al. (2012). “Full-length mRNA-Seq from singlecell levels of RNA and individual circulating tumor cells”. In: _Nat. Biotechnol._ 30, pp. 777–782. doi: `10.1038/nbt.2282` .

- Riba, Andrea et al. (2022). “Cell cycle gene regulation dynamics revealed by RNA velocity and deep-learning”. In: _Nat. Commun._ 13, p. 2865. doi: `10.1038/ s41467-022-30545-8` .

- Rich, Joseph M et al. (2024). “The impact of package selection and versioning on single-cell RNA-seq analysis”. In: _bioRxivorg_ , p. 2024.04.04.588111. doi: `10.1101/2024.04.04.588111` .

- Rooij, Frank J A van et al. (2017). “Genome-wide Trans-ethnic Meta-analysis Identifies Seven Genetic Loci Influencing Erythrocyte Traits and a Role for RBPMS in Erythropoiesis”. In: _Am. J. Hum. Genet._ 100, pp. 51–63. doi: `10.1016/j. ajhg.2016.11.016` .

- Saelens, Wouter et al. (2019). “A comparison of single-cell trajectory inference methods”. In: _Nat. Biotechnol._ 37, pp. 547–554. doi: `10.1038/s41587-0190071-9` .

111

- Sarkar, Abhishek and Matthew Stephens (2021). “Separating measurement and expression models clarifies confusion in single-cell RNA sequencing analysis”. In: _Nat. Genet._ 53, pp. 770–777. doi: `10.1038/s41588-021-00873-4` .

- Schnoerr, David, Guido Sanguinetti, and Ramon Grima (2017). “Approximation and inference methods for stochastic biochemical kinetics—a tutorial review”. In: _J. Phys. A Math. Theor._ 50, p. 093001. doi: `10.1088/1751-8121/aa54d9` .

- Schofield, Jeremy A et al. (2018). “TimeLapse-seq: adding a temporal dimension to RNA sequencing through nucleoside recoding”. In: _Nat. Methods_ 15, pp. 221– 225. doi: `10.1038/nmeth.4582` .

- Setty, Manu et al. (2019). “Characterization of cell fate probabilities in single-cell data with Palantir”. In: _Nat. Biotechnol._ 37, pp. 451–460. doi: `10.1038/s41587019-0068-4` .

- Shahrezaei, Vahid and Peter S Swain (2008). “Analytical distributions for stochastic gene expression”. In: _Proc. Natl. Acad. Sci. U. S. A._ 105, pp. 17256–17261. doi: `10.1073/pnas.0803850105` .

- Singh, Abhyudai and Pavol Bokes (2012). “Consequences of mRNA transport on stochastic variability in protein levels”. In: _Biophys. J._ 103, pp. 1087–1096. doi: `10.1016/j.bpj.2012.07.015` .

- Srivastava, R et al. (2002). “Stochastic vs. deterministic modeling of intracellular viral kinetics”. In: _J. Theor. Biol._ 218, pp. 309–321. doi: `10.1006/jtbi.2002. 3078` .

- Street, Kelly et al. (2018). “Slingshot: cell lineage and pseudotime inference for single-cell transcriptomics”. In: _BMC Genomics_ 19, p. 477. doi: `10.1186/ s12864-018-4772-0` .

- Sullivan, Delaney K, Kristján Eldjárn Hjörleifsson, et al. (2025). “Accurate quantification of nascent and mature RNAs from single-cell and single-nucleus RNAseq”. In: _Nucleic Acids Res._ 53. doi: `10.1093/nar/gkae1137` .

- Sullivan, Delaney K, Kyung Hoi Joseph Min, et al. (2025). “kallisto, bustools and kb-python for quantifying bulk, single-cell and single-nucleus RNA-seq”. In: _Nat. Protoc._ 20, pp. 587–607. doi: `10.1038/s41596-024-01057-0` .

- Suter, David M et al. (2011). “Mammalian genes are transcribed with widely different bursting kinetics”. In: _Science_ 332, pp. 472–474. doi: `10.1126/science. 1198817` .

- Svensson, Valentine (2020). “Droplet scRNA-seq is not zero-inflated”. In: _Nat. Biotechnol._ 38, pp. 147–150. doi: `10.1038/s41587-019-0379-5` .

- Swain, Peter S, Michael B Elowitz, and Eric D Siggia (2002). “Intrinsic and extrinsic contributions to stochasticity in gene expression”. In: _Proc. Natl. Acad. Sci. U. S. A._ 99, pp. 12795–12800. doi: `10.1073/pnas.162041399` .

112

- Taketani, S, T Furukawa, and K Furuyama (2001). “Expression of coproporphyrinogen oxidase and synthesis of hemoglobin in human erythroleukemia K562 cells”. In: _Eur. J. Biochem._ 268, pp. 1705–1711.

- Tang, Fuchou et al. (2009). “mRNA-Seq whole-transcriptome analysis of a single cell”. In: _Nat. Methods_ 6, pp. 377–382. doi: `10.1038/nmeth.1315` .

- Tang, Wenhao et al. (2023). “Modelling capture efficiency of single-cell RNAsequencing data improves inference of transcriptome-wide burst kinetics”. In: _Bioinformatics_ 39, btad395. doi: `10.1093/bioinformatics/btad395` .

- Taniguchi, Yuichi et al. (2010). “Quantifying E. coli proteome and transcriptome with single-molecule sensitivity in single cells”. In: _Science_ 329, pp. 533–538. doi: `10.1126/science.1188308` .

- Taylor, Jonathan and Robert J Tibshirani (2015). “Statistical learning and selective inference”. In: _Proc. Natl. Acad. Sci. U. S. A._ 112, pp. 7629–7634. doi: `10.1073/ pnas.1507583112` .

- Teicher, Henry (1961). “Identifiability of Mixtures”. In: _aoms_ 32, pp. 244–248. doi: `10.1214/aoms/1177705155` .

- Tian, Luyi et al. (2019). “Benchmarking single cell RNA-sequencing analysis pipelines using mixture control experiments”. In: _Nat. Methods_ 16, pp. 479– 487. doi: `10.1038/s41592-019-0425-8` .

- Trapnell, Cole et al. (2014). “The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells”. In: _Nat. Biotechnol._ 32, pp. 381–386. doi: `10.1038/nbt.2859` .

- Tritschler, Sophie et al. (2019). “Concepts and limitations for learning developmental trajectories from single cell genomics”. In: _Development_ 146. doi: `10.1242/ dev.170506` .

- Van den Berge, Koen et al. (2020). “Trajectory-based differential expression analysis for single-cell sequencing data”. In: _Nat. Commun._ 11, p. 1201. doi: `10.1038/ s41467-020-14766-3` .

- Van Kampen, N G (2007). _Stochastic processes in physics and chemistry_ . 3rd ed. North-Holland. doi: `10.1016/b978-0-444-52965-7.x5000-4` .

- Vellela, Melissa and Hong Qian (2007). “A quasistationary analysis of a stochastic chemical reaction: Keizer’s paradox”. In: _Bull. Math. Biol._ 69, pp. 1727–1746. doi: `10.1007/s11538-006-9188-3` .

- (2009). “Stochastic dynamics and non-equilibrium thermodynamics of a bistable chemical system: the Schlögl model revisited”. In: _J. R. Soc. Interface_ 6, pp. 925– 940. doi: `10.1098/rsif.2008.0476` .

- Virtanen, Pauli et al. (2020). “SciPy 1.0: fundamental algorithms for scientific computing in Python”. In: _Nat. Methods_ 17, pp. 261–272. doi: `10.1038/s41592019-0686-2` .

113

- Wang, Jingshu et al. (2018). “Gene expression distribution deconvolution in singlecell RNA sequencing”. In: _Proc. Natl. Acad. Sci. U. S. A._ 115, E6437–E6446. doi: `10.1073/pnas.1721085115` .

- Wolf, F Alexander, Philipp Angerer, and Fabian J Theis (2018). “SCANPY: largescale single-cell gene expression data analysis”. In: _Genome Biol._ 19, p. 15. doi: `10.1186/s13059-017-1382-0` .

- Wolf, F Alexander, Fiona K Hamey, et al. (2019). “PAGA: graph abstraction reconciles clustering with trajectory inference through a topology preserving map of single cells”. In: _Genome Biol._ 20, p. 59. doi: `10.1186/s13059-019-1663-x` .

- Yip, Shun H et al. (2017). “Linnorm: improved statistical analysis for single cell RNA-seq expression data”. In: _Nucleic Acids Res._ 45, e179. doi: `10.1093/nar/ gkx828` .

- Zhang, Jesse M, Govinda M Kamath, and David N Tse (2019). “Valid Post-clustering Differential Analysis for Single-Cell RNA-Seq”. In: _Cell Syst_ 9, 383–392.e6. doi: `10.1016/j.cels.2019.07.012` .

- Zheng, Grace X Y et al. (2017). “Massively parallel digital transcriptional profiling of single cells”. In: _Nat. Commun._ 8, p. 14049. doi: `10.1038/ncomms14049` .

- Zhou, Sheng et al. (2005). “Increased expression of the Abcg2 transporter during erythroid maturation plays a role in decreasing cellular protoporphyrin IX levels”. In: _Blood_ 105, pp. 2571–2576. doi: `10.1182/blood-2004-04-1566` .

- Zhu, Ciyou et al. (1997). “Algorithm 778: L-BFGS-B: Fortran subroutines for largescale bound-constrained optimization”. In: _ACM Trans. Math. Softw._ 23, pp. 550– 560. doi: `10.1145/279232.279236` .

---

[← A PROCESS TIME MODEL FOR TRAJECTORY INFERENCE AND RNA VELOCITY](09-a-process-time-model-for-trajectory-inference-and-rna-veloci.md) · [Up: contents](index.md)
