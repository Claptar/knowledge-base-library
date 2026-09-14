---
title: DISCUSSION AND CONCLUSION
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DISCUSSION AND CONCLUSION

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

But a poem is never actually finished. It just stops moving.

_Sayori, Doki Doki Literature Club_

Dan Salvato

### **12.1 Future challenges**

The work presented here is only the first step toward a physical treatment of sequencing data. Much work remains.

Although the modeling framework is fairly generic, the connections to real data are still obscure. I have operated with “nascent” and “mature” matrices, using counts aligning to intronic and exonic counts. But this binary is questionable, and I raise many potential counterpoints in Sections B.1 and B.2. Ultimately, a comprehensive model should represent transcript elongation _and_ splicing _and_ imperfect capture _and_ ambiguities in assignment _and_ stochasticity in all of the above. In the same vein, I have alluded to the construction of more sophisticated models for RNA capture, but have not attempted this. Therefore, although the fits to real data are at least fair, many fundamental questions are still outstanding.

The “feed-forward” systems I have outlined afford fairly simple solution strategies. Explicit regulation does not. Aside from the very brief discussions in Sections 4.3.1 and A.7, I have essentially ignored this key part of biology: the mathematics are intractable, and the (usually protein-based) mechanisms cannot be constrained using (RNA) data. However, further theoretical study is certainly worthwhile.

The solutions I have outlined rely on generating functions, and can, at least in principle, be combined to represent transcription genome-wide, using the toolbox in Section 10.1 to “couple” gene modules. However, in practice, computing, inverting, and discarding the vast majority of enormous _𝑛_ -dimensional arrays is impractical, and new solvers are necessary. It is possible that the methods outlined in Sections 5.3 and 10.3 can be used to this end. However, my feeling is that the current approach

140

is still far too bespoke and reliant on brute force, and alternative strategies need to be invented.

Although I have used a handful of statistical techniques, the core of the thesis is not about statistics. Instead, it represents foundational work meant to _enable_ rigorous investigations by trained statisticians. Although the results thus far may have frustrating limitations, I believe that the general outline of the mechanistic approach provides a more promising foundation for future work than the “data science” methods critiqued at length in Sections 6.1, 8.4, and B.3, and B.4. These critiques, in turn, are still incomplete, and many other methods used in singlecell sequencing data analysis — thermodynamic, landscape, and graph analogies<sup>8</sup> , nearest-neighbor graphs, various clustering algorithms — give me pause; their compatibility with single-molecule noise is obscure. However, the comprehensive analysis of these methods is a substantial undertaking pursuing a rapidly moving target.

### **12.2 Concluding notes**

The stochastic worldview offers us a principled way to ask questions of single-cell RNA sequencing data. Even though the conclusions are limited, and do not add up to a grand theory of biology, on having read (or written) this thesis, we are not Goethe’s Faust, who “...here, poor fool! with all [his] lore... stand[s], no wiser than before” [306]. We have learned something. We know how to solve certain seemingly imposing equations, considerably reducing the mathematical ingenuity necessary to model biophysical phenomena. We have gained a healthy unease with standard practices. We have learned to think about single-cell technologies in a way that brings them closer to “full communion” with the tradition of transcriptomics.

What do I hope to actually accomplish with this thesis?

In the near term, I have raised doubts about standard analysis procedures (normalization, RNA velocity), and proposed a (flawed, limited, but precedented and principled) alternative. Where this will lead is unclear. Every week, a new velocity, graph analysis, normalization, machine learning method is released. Perhaps the critiques reported here will counteract some of the momentum and lead to more carefully weighed claims, models, and benchmarks. Per Samuel Karlin, modeling lets us “sharpen the questions” about data [289], and the critiques and hypotheses I have outlined here are intended to illustrate the power of this worldview.

In the medium term, I have attempted to draw connections across disciplines and en-

141

courage researchers in related fields — chemical engineering, physics, fluorescence transcriptomics, finance, machine learning — to seriously consider lending their experience in stochastic modeling to the single-cell RNA sequencing field. Time will tell whether this will lead to the transfer of expertise. A few people in the right places, asking the right questions, may make all the necessary difference.

In the long term, nature is a forest at dawn, veiled in mist; all of research is a stream flowing through this forest; this stream is in flux; some patches of its surface reflect the forest, some are murky, some are opaque, placid and isolated against the current, but for all that no less a part of it; and this work is a drop in the stream, painstakingly made discrete and unified for a brief moment, here clarifying its surroundings, here obscuring, but from here on ultimately dissipating at the will of the stream.

142

### **Bibliography**

- [1] 10x Genomics. Interpreting Intronic and Antisense Reads in 10x Genomics Single Cell Gene Expression Data. Technical Note CG000376, 10x Genomics, August 2021. URL `https://www.10xgenomics.com/support/single-cell-geneexpression/documentation/steps/sequencing/interpretingintronic-and-antisense-reads-in-10-x-genomics-singlecell-gene-expression-data` .

- [2] Milton Abramowitz and Irene Stegun, editors. _Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables_ . United States National Bureau of Standards, 9 edition, 1970.

- [3] Andrew K. Adams, Shelley D. Smith, Dongnhu T. Truong, Erik G. Willcutt, Richard K. Olson, John C. DeFries, Bruce F. Pennington, and Jeffrey R. Gruen. Enrichment of putatively damaging rare variants in the DYX2 locus and the reading-related genes CCDC136 and FLNC. _Human Genetics_ , 136 (11-12):1395–1405, November 2017. ISSN 0340-6717, 1432-1203. doi: 10. 1007/s00439-017-1838-z. URL `http://link.springer.com/10.1007/ s00439-017-1838-z` .

- [4] Constantin Ahlmann-Eltze and Wolfgang Huber. Comparison of transformations for single-cell RNA-seq data. _Nature Methods_ , April 2023. ISSN 1548-7091, 1548-7105. doi: 10.1038/s41592-023-01814-1. URL `https://www.nature.com/articles/s41592-023-01814-1` .

- [5] Jaroslav Albert. Path integral approach to generating functions for multistep post-transcription and post-translation processes and arbitrary initial conditions. _Journal of Mathematical Biology_ , 79(6-7):2211–2236, December 2019. ISSN 0303-6812, 1432-1416. doi: 10.1007/s00285-019-01426-4. URL `http://link.springer.com/10.1007/s00285-019-01426-4` .

- [6] Melissa J. Alldred, Karen E. Duff, and Stephen D. Ginsberg. Microarray analysis of CA1 pyramidal neurons in a mouse model of tauopathy reveals progressive synaptic dysfunction. _Neurobiology of Disease_ , 45(2):751–762, February 2012. ISSN 09699961. doi: 10.1016/j.nbd.2011.10.022. URL `https: //linkinghub.elsevier.com/retrieve/pii/S0969996111003548` .

- [7] Lisa Amrhein. _Stochastic Modeling of Heterogeneous Low-Input Gene Expression: Linking Single-Cell Probability Distributions to Transcription Mechanisms_ . PhD Dissertation, Technische Universitat Munchen, Munich, June 2021.

- [8] Lisa Amrhein, Kumar Harsha, and Christiane Fuchs. A mechanistic model for the negative binomial distribution of single-cell mRNA counts. Preprint, bioRxiv: 657619, June 2019. URL `http://biorxiv.org/lookup/doi/ 10.1101/657619` .

143

- [9] Simon Anders and Wolfgang Huber. Differential expression analysis for sequence count data. _Genome Biology_ , 11:R106, 2010.

- [10] Tallulah Andrews and Martin Hemberg. False signals induced by single-cell imputation. _F1000Research_ , 7:1740, 2019. URL `https: //f1000research.com/articles/7-1740/v2` .

- [11] Tallulah S. Andrews, Jawairia Atif, Jeff C. Liu, Catia T. Perciani, Xue-Zhong Ma, Cornelia Thoeni, Michal Slyper, Gökcen Eraslan, Asa Segerstolpe, Justin Manuel, Sai Chung, Erin Winter, Iulia Cirlan, Nicholas Khuu, Sandra Fischer, Orit Rozenblatt-Rosen, Aviv Regev, Ian D. McGilvray, Gary D. Bader, and Sonya A. MacParland. Single-Cell, Single-Nucleus, and Spatial RNA Sequencing of the Human Liver Identifies Cholangiocyte and Mesenchymal Heterogeneity. _Hepatology Communications_ , 6(4):821–840, 2022. doi: https://doi.org/10.1002/hep4.1854. URL `https://aasldpubs. onlinelibrary.wiley.com/doi/abs/10.1002/hep4.1854` .

- [12] Tal Ashuach, Daniel A. Reidenbach, Adam Gayoso, and Nir Yosef. PeakVI: A deep generative model for single-cell chromatin accessibility analysis. _Cell Reports Methods_ , 2(3):100182, March 2022. ISSN 26672375. doi: 10.1016/j.crmeth.2022.100182. URL `https://linkinghub.elsevier. com/retrieve/pii/S2667237522000376` .

- [13] Lyla Atta, Arpan Sahoo, and Jean Fan. VeloViz: RNA velocity-informed embeddings for visualizing cellular trajectories. _Bioinformatics_ , 38(2):391– 396, September 2021. doi: 10.1093/bioinformatics/btab653.

- [14] Carol Bacchi. The Turn to Problematization: Political Implications of Contrasting Interpretive and Poststructural Adaptations. _Open Journal of Political Science_ , 05(01):1–12, 2015. ISSN 2164-0505, 2164-0513. doi: 10.4236/ojps.2015.51001. URL `http://www.scirp.org/journal/doi. aspx?DOI=10.4236/ojps.2015.51001` .

- [15] Ana Badimon, Hayley J. Strasburger, Pinar Ayata, Xinhong Chen, Aditya Nair, Ako Ikegami, Philip Hwang, Andrew T. Chan, Steven M. Graves, Joseph O. Uweru, Carola Ledderose, Munir Gunes Kutlu, Michael A. Wheeler, Anat Kahan, Masago Ishikawa, Ying-Chih Wang, Yong-Hwee E. Loh, Jean X. Jiang, D. James Surmeier, Simon C. Robson, Wolfgang G. Junger, Robert Sebra, Erin S. Calipari, Paul J. Kenny, Ukpong B. Eyo, Marco Colonna, Francisco J. Quintana, Hiroaki Wake, Viviana Gradinaru, and Anne Schaefer. Negative feedback control of neuronal activity by microglia. _Nature_ , 586(7829):417–423, October 2020. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586-020-2777-8. URL `https: //www.nature.com/articles/s41586-020-2777-8` .

- [16] Keren Bahar Halpern, Sivan Tanami, Shanie Landen, Michal Chapal, Liran Szlak, Anat Hutzler, Anna Nizhberg, and Shalev Itzkovitz. Bursty

144

Gene Expression in the Intact Mammalian Liver. _Molecular Cell_ , 58 (1):147–156, April 2015. ISSN 10972765. doi: 10.1016/j.molcel.2015. 01.027. URL `https://linkinghub.elsevier.com/retrieve/pii/ S1097276515000507` .

- [17] Keren Bahar Halpern, Inbal Caspi, Doron Lemze, Maayan Levy, Shanie Landen, Eran Elinav, Igor Ulitsky, and Shalev Itzkovitz. Nuclear Retention of mRNA in Mammalian Tissues. _Cell Reports_ , 13(12):2653–2662, December 2015. ISSN 22111247. doi: 10.1016/j.celrep.2015.11.036. URL `https: //linkinghub.elsevier.com/retrieve/pii/S2211124715013510` .

- [18] Douglas H. Baird, Kenneth A. Myers, Mette Mogensen, David Moss, and Peter W. Baas. Distribution of the microtubule-related protein ninein in developing neurons. _Neuropharmacology_ , 47(5):677–683, October 2004. ISSN 00283908. doi: 10.1016/j.neuropharm.2004.07.016. URL `https: //linkinghub.elsevier.com/retrieve/pii/S0028390804002096` .

- [19] Trygve E. Bakken, Rebecca D. Hodge, Jeremy A. Miller, Zizhen Yao, Thuc Nghi Nguyen, Brian Aevermann, Eliza Barkan, Darren Bertagnolli, Tamara Casper, Nick Dee, Emma Garren, Jeff Goldy, Lucas T. Graybuck, Matthew Kroll, Roger S. Lasken, Kanan Lathia, Sheana Parry, Christine Rimorin, Richard H. Scheuermann, Nicholas J. Schork, Soraya I. Shehata, Michael Tieu, John W. Phillips, Amy Bernard, Kimberly A. Smith, Hongkui Zeng, Ed S. Lein, and Bosiljka Tasic. Single-nucleus and single-cell transcriptomes compared in matched cortical cell types. _PLOS ONE_ , 13(12):e0209648, December 2018. ISSN 1932-6203. doi: 10.1371/journal.pone.0209648. URL `https://dx.plos.org/10.1371/ journal.pone.0209648` .

- [20] O. E. Barndorff-Nielsen and J. Schmiegel. A Stochastic Differential Equation Framework for the Timewise Dynamics of Turbulent Velocities. _Theory of Probability & Its Applications_ , 52(3):372–388, January 2008. ISSN 0040585X, 1095-7219. doi: 10.1137/S0040585X9798316X. URL `http:// epubs.siam.org/doi/10.1137/S0040585X9798316X` .

- [21] Ole E Barndorff-Nielsen and Neil Shephard. Non-Gaussian OrnsteinUhlenbeck-based models and some of their uses in Financial economics. _Journal of the Royal Statistical Society: Series B_ , 63:167–241, 2001. doi: 10.1111/1467-9868.00282. URL `https://rss.onlinelibrary.wiley. com/doi/10.1111/1467-9868.00282` .

- [22] Ole E. Barndorff-Nielsen and Neil Shephard. Integrated OU Processes and Non-Gaussian OU-based Stochastic Volatility Models. _Scandinavian Journal of Statistics_ , 30(2):277–295, June 2003. ISSN 0303-6898, 1467-9469. doi: 10.1111/1467-9469.00331. URL `http://doi.wiley.com/10.1111/ 1467-9469.00331` .

145

- [23] Ole E. Barndorff-Nielsen, Sidney I. Resnick, and Thomas Mikosch, editors. _Lévy Processes_ . Birkhäuser Boston, Boston, MA, 2001. ISBN 978-1-46126657-0 978-1-4612-0197-7. doi: 10.1007/978-1-4612-0197-7. URL `http: //link.springer.com/10.1007/978-1-4612-0197-7` .

- [24] Anthony F. Bartholomay. On the linear birth and death processes of biology as Markoff chains. _The Bulletin of Mathematical Biophysics_ , 20(2):97–118, June 1958. ISSN 0007-4985, 1522-9602. doi: 10.1007/BF02477571. URL `http://link.springer.com/10.1007/BF02477571` .

- [25] Anthony F. Bartholomay. Stochastic models for chemical reactions: I. Theory of the unimolecular reaction process. _The Bulletin of Mathematical Biophysics_ , 20(3):175–190, September 1958. ISSN 0007-4985, 15229602. doi: 10.1007/BF02478297. URL `http://link.springer.com/ 10.1007/BF02478297` .

- [26] Ayse Bassez, Hanne Vos, Laurien Van Dyck, Giuseppe Floris, Ingrid Arĳs, Christine Desmedt, Bram Boeckx, Marlies Vanden Bempt, Ines Nevelsteen, Kathleen Lambein, Kevin Punie, Patrick Neven, Abhishek D. Garg, Hans Wildiers, Junbin Qian, Ann Smeets, and Diether Lambrechts. A singlecell map of intratumoral changes during anti-PD1 treatment of patients with breast cancer. _Nature Medicine_ , 27(5):820–832, May 2021. ISSN 10788956, 1546-170X. doi: 10.1038/s41591-021-01323-8. URL `http://www. nature.com/articles/s41591-021-01323-8` .

- [27] Nico Battich, Thomas Stoeger, and Lucas Pelkmans. Control of Transcript Variability in Single Mammalian Cells. _Cell_ , 163(7):1596–1610, December 2015. ISSN 00928674. doi: 10.1016/j.cell.2015.11.018. URL `https: //linkinghub.elsevier.com/retrieve/pii/S0092867415014981` .

- [28] Casper H. L. Beentjes, Ruben Perez-Carrasco, and Ramon Grima. Exact solution of stochastic gene expression models with bursting, cell cycle and replication dynamics. _Physical Review E_ , 101(3):032403, March 2020. ISSN 2470-0045, 2470-0053. doi: 10.1103/PhysRevE.101.032403. URL `https: //link.aps.org/doi/10.1103/PhysRevE.101.032403` .

- [29] Volker Bergen, Marius Lange, Stefan Peidli, F. Alexander Wolf, and Fabian J. Theis. Generalizing RNA velocity to transient cell states through dynamical modeling. _Nature Biotechnology_ , August 2020. ISSN 1087-0156, 15461696. doi: 10.1038/s41587-020-0591-3. URL `http://www.nature.com/ articles/s41587-020-0591-3` .

- [30] Volker Bergen, Ruslan A Soldatov, Peter V Kharchenko, and Fabian J Theis. RNA velocity—current challenges and future perspectives. _Molecular Systems Biology_ , 17(8), August 2021. ISSN 1744-4292, 1744-4292. doi: 10.15252/msb.202110282. URL `https://onlinelibrary.wiley.com/ doi/10.15252/msb.202110282` .

146

- [31] Pavol Bokes, John R. King, Andrew T. A. Wood, and Matthew Loose. Exact and approximate distributions of protein and mRNA levels in the low-copy regime of gene expression. _Journal of Mathematical Biology_ , 64(5):829–854, April 2012. ISSN 0303-6812, 1432-1416. doi: 10.1007/s00285-011-0433-5. URL `http://link.springer.com/10.1007/s00285-011-0433-5` .

- [32] A Sina Booeshaghi and Lior Pachter. Normalization of single-cell RNA-seq counts by log( _x_ + 1) or log(1 + _x_ ). _Bioinformatics_ , 37 (15):2223–2224, August 2021. ISSN 1367-4803, 1460-2059. doi: 10.1093/bioinformatics/btab085. URL `https://academic.oup.com/ bioinformatics/article/37/15/2223/6155989` .

- [33] A. Sina Booeshaghi, Zizhen Yao, Cindy van Velthoven, Kimberly Smith, Bosiljka Tasic, Hongkui Zeng, and Lior Pachter. Isoform cell-type specificity in the mouse primary motor cortex. _Nature_ , 598(7879):195–199, October 2021. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586-021-03969-3. URL `https://www.nature.com/articles/s41586-021-03969-3` .

- [34] A. Sina Booeshaghi, Ingileif B. Hallgrímsdóttir, Angel Gálvez-Merchán, and Lior Pachter. Depth normalization for single-cell genomics count data. Preprint, bioRxiv: 2022.05.06.490859, May 2022. URL `http://biorxiv. org/lookup/doi/10.1101/2022.05.06.490859` .

- [35] Jorge L. Borges. _Collected Fictions_ . Penguin Classics, 1999. ISBN 978-014-028680-9.

- [36] Gerard A. Bouland, Ahmed Mahfouz, and Marcel J. T. Reinders. Consequences and opportunities arising due to sparser single-cell RNA-seq datasets. _Genome Biology_ , 24(1):86, April 2023. ISSN 1474-760X. doi: 10.1186/s13059-023-02933-w. URL `https://genomebiology. biomedcentral.com/articles/10.1186/s13059-023-02933-w` .

- [37] Jérémie Breda, Mihaela Zavolan, and Erik van Nimwegen. Bayesian inference of gene expression states from single-cell RNA-seq data. _Nature Biotechnology_ , 39(8):1008–1016, August 2021. ISSN 1087-0156, 15461696. doi: 10.1038/s41587-021-00875-x. URL `https://www.nature. com/articles/s41587-021-00875-x` .

- [38] Kenneth P. Burnham and David Raymond Anderson. _Model selection and multimodel inference: a practical information-theoretic approach_ . Springer, New York, 2nd ed edition, 2002. ISBN 978-0-387-95364-9. OCLC: ocm48557578.

- [39] Xiaodong Cai. Exact stochastic simulation of coupled chemical reactions with delays. _The Journal of Chemical Physics_ , 126(12):124108, March 2007. ISSN 0021-9606, 1089-7690. doi: 10.1063/1.2710253. URL `http: //aip.scitation.org/doi/10.1063/1.2710253` .

147

- [40] Giuliana P Calia, Xinyue Chen, Binyamin Zuckerman, and Leor S Weinberger. Comparative analysis between single-cell RNA-seq and singlemolecule RNA FISH indicates that the pyrimidine nucleobase idoxuridine (IdU) globally amplifies transcriptional noise. Preprint, bioRxiv: 2023.03.14.532632, March 2023. URL `https://www.biorxiv.org/ content/10.1101/2023.03.14.532632v1.full` .

- [41] Robrecht Cannoodt, Wouter Saelens, Louise Deconinck, and Yvan Saeys. Spearheading future omics analyses using dyngen, a multi-modal simulator of single cells. _Nature Communications_ , 12(1):3942, December 2021. ISSN 2041-1723. doi: 10.1038/s41467-021-24152-2. URL `http: //www.nature.com/articles/s41467-021-24152-2` .

- [42] Zhixing Cao and Ramon Grima. Analytical distributions for detailed models of stochastic gene expression in eukaryotic cells. _Proceedings of the National Academy of Sciences_ , 117(9):4682–4692, March 2020. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas.1910888117. URL `http://www.pnas.org/ lookup/doi/10.1073/pnas.1910888117` .

- [43] Jessica Cariboni and Wim Schoutens. Jumps in intensity models: investigating the performance of Ornstein-Uhlenbeck processes in credit risk modeling. _Metrika_ , 69(2-3):173–198, March 2009. ISSN 0026-1335, 1435-926X. doi: 10.1007/s00184-008-0213-4. URL `http://link.springer.com/ 10.1007/s00184-008-0213-4` .

- [44] Maria T. Carilli, Gennady Gorin, Yongin Choi, Tara Chari, and Lior Pachter. Mechanistic modeling with a variational autoencoder for multimodal singlecell RNA sequencing data. Preprint, bioRxiv: 2023.01.13.523995, January 2023. URL `http://biorxiv.org/lookup/doi/10.1101/2023.01.13. 523995` .

- [45] Lewis Carroll. _Sylvie and Bruno Concluded_ . Macmillan and Co., London, 1894.

- [46] John T. Chamberlin, Younghee Lee, Gabor T. Marth, and Aaron R. Quinlan. Variable RNA sampling biases mediate concordance of single-cell and nucleus sequencing across cell types. Preprint, bioRxiv: 2022.08.01.502392, August 2022. URL `http://biorxiv.org/lookup/doi/10.1101/2022. 08.01.502392` .

- [47] Kathleen Champion, Bethany Lusch, J. Nathan Kutz, and Steven L. Brunton. Data-driven discovery of coordinates and governing equations. _Proceedings of the National Academy of Sciences_ , 116(45):22445–22451, November 2019. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas.1906995116. URL `https: //pnas.org/doi/full/10.1073/pnas.1906995116` .

- [48] David Chandler. _Introduction to Modern Statistical Mechanics_ . Oxford University Press, New York, 1987.

148

- [49] Tara Chari, Joeyta Banerjee, and Lior Pachter. The Specious Art of Single-Cell Genomics. Preprint, bioRxiv: 2021.08.25.457696, September 2021. URL `http://biorxiv.org/lookup/doi/10.1101/2021.08.25. 457696` .

- [50] Mohammed Charrout, Marcel J.T. Reinders, and Ahmed Mahfouz. Untangling biological factors influencing trajectory inference from single cell data. Preprint, bioRxiv: 2020.02.11.942102, February 2020. URL `http: //biorxiv.org/lookup/doi/10.1101/2020.02.11.942102` .

- [51] Yung-Sung Cheng. Bivariate Lognormal Distribution for Characterizing Asbestos Fiber Aerosols. _Aerosol Science and Technology_ , 5(3): 359–368, January 1986. ISSN 0278-6826, 1521-7388. doi: 10.1080/ 02786828608959100. URL `http://www.tandfonline.com/doi/abs/ 10.1080/02786828608959100` .

- [52] Yongin Choi, Ruoxin Li, and Gerald Quon. siVAE: interpretable deep generative models for single-cell transcriptomes. _Genome Biology_ , 24(1): 29, February 2023. ISSN 1474-760X. doi: 10.1186/s13059-023-02850y. URL `https://genomebiology.biomedcentral.com/articles/10. 1186/s13059-023-02850-y` .

- [53] Sandeep Choubey. Nascent RNA kinetics: Transient and steady state behavior of models of transcription. _Physical Review E_ , 97(2):022402, 2018. ISSN 2470-0045, 2470-0053. doi: 10.1103/PhysRevE.97.022402.

- [54] Sandeep Choubey, Jane Kondev, and Alvaro Sanchez. Deciphering Transcriptional Dynamics In Vivo by Counting Nascent RNA Molecules. _PLOS Computational Biology_ , 11(11):e1004345, 2015. ISSN 1553-7358.

- [55] Siu Yu A. Chow, Kazuki Nakayama, Tatsuya Osaki, Maki Sugiyama, Maiko Yamada, Hirotaka Takeuchi, and Yoshiho Ikeuchi. Human sensory neurons modulate melanocytes through secretion of RGMB. _Cell Reports_ , 40 (12):111366, September 2022. ISSN 22111247. doi: 10.1016/j.celrep. 2022.111366. URL `https://linkinghub.elsevier.com/retrieve/ pii/S2211124722011986` .

- [56] Michael B. Cole, Davide Risso, Allon Wagner, David DeTomaso, John Ngai, Elizabeth Purdom, Sandrine Dudoit, and Nir Yosef. Performance Assessment and Selection of Normalization Procedures for Single-Cell RNASeq. _Cell Systems_ , 8(4):315–328.e8, April 2019. ISSN 24054712. doi: 10.1016/j.cels.2019.03.010. URL `https://linkinghub.elsevier.com/ retrieve/pii/S2405471219300808` .

- [57] Rama Cont and Peter Tankov. _Financial Modeling with Jump Processes_ . Financial Mathematics. Chapman & Hall, 2004.

149

- [58] Shamus M. Cooley, Timothy Hamilton, J. Christian J. Ray, and Eric J. Deeds. A novel metric reveals previously unrecognized distortion in dimensionality reduction of scRNA-Seq data. Preprint, bioRxiv: 689851, September 2020. URL `https://www.biorxiv.org/content/10.1101/689851v4` .

- [59] Adam M Corrigan, Edward Tunnacliffe, Danielle Cannon, and Jonathan R Chubb. A continuum model of transcriptional bursting. _eLife_ , 5:e13051, February 2016. ISSN 2050-084X. doi: 10.7554/eLife.13051. URL `https: //elifesciences.org/articles/13051` .

- [60] Allison Coté, Chris Coté, Sareh Bayatpour, Heather L Drexler, Katherine A Alexander, Fei Chen, Asmamaw T Wassie, Edward S Boyden, Shelley Berger, L Stirling Churchman, and Arjun Raj. pre-mRNA spatial distributions suggest that splicing can occur post-transcriptionally. Preprint, bioRxiv: 2020.04.06.028092, June 2021. URL `https://doi.org/10.1101/2020. 04.06.028092` .

- [61] Charles P. Couturier, Shamini Ayyadhury, Phuong U. Le, Javad Nadaf, Jean Monlong, Gabriele Riva, Redouane Allache, Salma Baig, Xiaohua Yan, Mathieu Bourgey, Changseok Lee, Yu Chang David Wang, V. Wee Yong, Marie-Christine Guiot, Hamed Najafabadi, Bratislav Misic, Jack Antel, Guillaume Bourque, Jiannis Ragoussis, and Kevin Petrecca. Single-cell RNA-seq reveals that glioblastoma recapitulates a normal neurodevelopmental hierarchy. _Nature Communications_ , 11(1):3406, December 2020. ISSN 2041-1723. doi: 10.1038/s41467-020-17186-5. URL `http://www.nature.com/articles/s41467-020-17186-5` .

- [62] John C. Cox, Jonathan E. Ingersoll, and Stephen A. Ross. A Theory of the Term Structure of Interest Rates. _Econometrica_ , 53(2):385, March 1985. ISSN 00129682. doi: 10.2307/1911242. URL `https://www.jstor.org/ stable/1911242?origin=crossref` .

- [63] Haotian Cui, Hassaan Maan, and Bo Wang. DeepVelo: Deep Learning extends RNA velocity to multi-lineage systems with cell-specific kinetics. Preprint, bioRxiv: 2022.04.03.486877, April 2022. URL `http://biorxiv. org/lookup/doi/10.1101/2022.04.03.486877` .

- [64] Bernie J Daigle, Min K Roh, Linda R Petzold, and Jarad Niemi. Accelerated maximum likelihood parameter estimation for stochastic biochemical systems. _BMC Bioinformatics_ , 13(1):68, December 2012. ISSN 1471-2105. doi: 10.1186/1471-2105-13-68. URL `http://link.springer.com/10. 1186/1471-2105-13-68` .

- [65] R. D. Dar, B. S. Razooky, A. Singh, T. V. Trimeloni, J. M. McCollum, C. D. Cox, M. L. Simpson, and L. S. Weinberger. Transcriptional burst frequency and burst size are equally modulated across the human genome. _Proceedings of the National Academy of Sciences_ , 109(43):17454–17459,

150

October 2012. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas.1213530109. URL `http://www.pnas.org/cgi/doi/10.1073/pnas.1213530109` .

- [66] Justine Dattani. _Exact solutions of master equations for the analysis of gene transcription models_ . PhD Dissertation, Imperial College London, November 2015.

- [67] Justine Dattani and Mauricio Barahona. Stochastic models of gene transcription with upstream drives: exact solution and sample path characterization. _Journal of The Royal Society Interface_ , 14(126):20160833, January 2017. ISSN 1742-5689, 1742-5662. doi: 10.1098/rsif.2016.0833. URL `https: //royalsocietypublishing.org/doi/10.1098/rsif.2016.0833` .

- [68] Chiara A. De Benedictis, Claudia Haffke, Simone Hagmeyer, Ann Katrin Sauer, and Andreas M. Grabrucker. Expression Analysis of Zinc Transporters in Nervous Tissue Cells Reveals Neuronal and Synaptic Localization of ZIP4. _International Journal of Molecular Sciences_ , 22(9):4511, April 2021. ISSN 1422-0067. doi: 10.3390/ĳms22094511. URL `https://www.mdpi.com/ 1422-0067/22/9/4511` .

- [69] Mihails Delmans and Martin Hemberg. Discrete distributional differential expression (D3E) - a tool for gene expression analysis of single-cell RNAseq data. _BMC Bioinformatics_ , 17:110, December 2016. ISSN 1471-2105. doi: 10.1186/s12859-016-0944-6. URL `http://www.biomedcentral. com/1471-2105/17/110` .

- [70] A. P. Dempster, N. M. Laird, and D. B. Rubin. Maximum Likelihood from Incomplete Data via the EM Algorithm. _Journal of the Royal Statistical Society. Series B (Methodological)_ , 39(1):1–38, 1977. ISSN 0035-9246. URL `https://www.jstor.org/stable/2984875` . Publisher: [Royal Statistical Society, Wiley].

- [71] Elena Denisenko, Belinda B. Guo, Matthew Jones, Rui Hou, Leanne de Kock, Timo Lassmann, Daniel Poppe, Olivier Clément, Rebecca K. Simmons, Ryan Lister, and Alistair R. R. Forrest. Systematic assessment of tissue dissociation and storage biases in single-cell and single-nucleus RNA-seq workflows. _Genome Biology_ , 21(1):130, December 2020. ISSN 1474-760X. doi: 10.1186/s13059-020-02048-6. URL `https://genomebiology. biomedcentral.com/articles/10.1186/s13059-020-02048-6` .

- [72] Ravi V. Desai, Xinyue Chen, Benjamin Martin, Sonali Chaturvedi, Dong Woo Hwang, Weihan Li, Chen Yu, Sheng Ding, Matt Thomson, Robert H. Singer, Robert A. Coleman, Maike M. K. Hansen, and Leor S. Weinberger. A DNA repair pathway can regulate transcriptional noise to promote cell fate transitions. _Science_ , 373(6557):eabc6506, August 2021. ISSN 0036-8075, 1095-9203. doi: 10.1126/science.abc6506. URL `https: //www.sciencemag.org/lookup/doi/10.1126/science.abc6506` .

151

- [73] M. Deza and Elena Deza. _Encyclopedia of distances_ . Springer Verlag, Dordrecht : New York, 2009. ISBN 978-3-642-00233-5 978-3-642-00234-2. OCLC: ocn310400730.

- [74] Fangyuan Ding and Michael B. Elowitz. Constitutive splicing and economies of scale in gene expression. _Nature structural & molecular biology_ , 26(6): 424–432, June 2019. ISSN 1545-9993. doi: 10.1038/s41594-019-0226-x. URL `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6663491/` .

- [75] Jiarui Ding, Xian Adiconis, Sean K. Simmons, Monika S. Kowalczyk, Cynthia C. Hession, Nemanja D. Marjanovic, Travis K. Hughes, Marc H. Wadsworth, Tyler Burks, Lan T. Nguyen, John Y. H. Kwon, Boaz Barak, William Ge, Amanda J. Kedaigle, Shaina Carroll, Shuqiang Li, Nir Hacohen, Orit Rozenblatt-Rosen, Alex K. Shalek, Alexandra-Chloé Villani, Aviv Regev, and Joshua Z. Levin. Systematic comparison of single-cell and singlenucleus RNA-sequencing methods. _Nature Biotechnology_ , 38(6):737–746, June 2020. ISSN 1087-0156, 1546-1696. doi: 10.1038/s41587-020-0465-8. URL `https://www.nature.com/articles/s41587-020-0465-8` .

- [76] Heather L. Drexler, Karine Choquet, and L. Stirling Churchman. Splicing Kinetics and Coordination Revealed by Direct Nascent RNA Sequencing through Nanopores. _Molecular Cell_ , 77(5):985–998.e8, March 2020. ISSN 10972765. doi: 10.1016/j.molcel.2019.11.017. URL `https:// linkinghub.elsevier.com/retrieve/pii/S1097276519308652` .

- [77] Jin-Hong Du, Ming Gao, and Jingshu Wang. Model-based Trajectory Inference for Single-Cell RNA Sequencing Using Deep Learning with a Mixture Prior. Preprint, bioRxiv: 2020.12.26.424452, December 2020. URL `http://biorxiv.org/lookup/doi/10.1101/2020.12.26.424452` .

- [78] Jacques Dutka. The early history of the factorial function. _Archive for History of Exact Sciences_ , 43(3):225–249, 1991. ISSN 0003-9519, 14320657. doi: 10.1007/BF00389433. URL `http://link.springer.com/ 10.1007/BF00389433` .

- [79] Marcelo R. Ebert and Michael Reissig. _Methods for Partial Differential Equations_ . Springer International Publishing, Cham, 2018. ISBN 978-3319-66455-2 978-3-319-66456-9. doi: 10.1007/978-3-319-66456-9. URL `http://link.springer.com/10.1007/978-3-319-66456-9` .

- [80] Kristján Eldjárn Hjörleifsson, Delaney K. Sullivan, Guillaume Holley, Páll Melsted, and Lior Pachter. Accurate quantification of single-nucleus and single-cell RNA-seq transcripts. Preprint, bioRxiv: 2022.12.02.518832, December 2022. URL `http://biorxiv.org/lookup/doi/10.1101/2022. 12.02.518832` .

152

- [81] Michael B Elowitz, Arnold J Levine, Eric D Siggia, and Peter S Swain. Stochastic Gene Expression in a Single Cell. _Science_ , 297(5584):1183–1186, 2002. doi: 10.1126/science.1070919.

- [82] W. L. Ernst, Y. Zhang, J. W. Yoo, S. J. Ernst, and J. L. Noebels. Genetic Enhancement of Thalamocortical Network Activity by Elevating 1G-Mediated Low-Voltage-Activated Calcium Current Induces Pure Absence Epilepsy. _Journal of Neuroscience_ , 29(6):1615–1625, February 2009. ISSN 0270-6474, 1529-2401. doi: 10.1523/JNEUROSCI.208108.2009. URL `https://www.jneurosci.org/lookup/doi/10.1523/ JNEUROSCI.2081-08.2009` .

- [83] Felix Famoye. On the bivariate negative binomial regression model. _Journal of Applied Statistics_ , 37(6):969–981, June 2010. ISSN 0266-4763, 1360-0532. doi: 10.1080/02664760902984618. URL `https://www. tandfonline.com/doi/full/10.1080/02664760902984618` .

- [84] Alexander Feuerborn and Peter R. Cook. Why the activity of a gene depends on its neighbors. _Trends in Genetics_ , 31(9):483–490, September 2015. ISSN 01689525. doi: 10.1016/j.tig.2015.07.001. URL `https://linkinghub. elsevier.com/retrieve/pii/S0168952515001298` .

- [85] Tatiana Filatova, Nikola Popovic, and Ramon Grima. Statistics of Nascent and Mature RNA Fluctuations in a Stochastic Model of Transcriptional Initiation, Elongation, Pausing, and Termination. _Bulletin of Mathematical Biology_ , 83(1):3, January 2021. ISSN 0092-8240, 1522-9602. doi: 10.1007/s11538-020-00827-7. URL `http://link.springer.com/10. 1007/s11538-020-00827-7` .

- [86] Tatiana Filatova, Nikola Popović, and Ramon Grima. Modulation of nuclear and cytoplasmic mRNA fluctuations by time-dependent stimuli: Analytical distributions. _Mathematical Biosciences_ , 347:108828, May 2022. ISSN 00255564. doi: 10.1016/j.mbs.2022.108828. URL `https://linkinghub. elsevier.com/retrieve/pii/S0025556422000372` .

- [87] Stephen J. Fleming, Mark D. Chaffin, Alessandro Arduini, Amer-Denis Akkad, Eric Banks, John C. Marioni, Anthony A. Philippakis, Patrick T. Ellinor, and Mehrtash Babadi. Unsupervised removal of systematic background noise from droplet-based single-cell experiments using CellBender. Preprint, bioRxiv: 791699, October 2019. URL `http://biorxiv.org/ lookup/doi/10.1101/791699` .

- [88] H. Scott Fogler. _Elements of chemical reaction engineering_ . Prentice Hall PTR international series in the physical and chemical engineering sciences. Prentice Hall PTR, Upper Saddle River, NJ, 4th ed edition, 2006. ISBN 978-0-13-047394-3. OCLC: ocm56956313.

153

- [89] Nir Friedman, Long Cai, and X. Sunney Xie. Linking Stochastic Dynamics to Population Distribution: An Analytical Framework of Gene Expression. _Physical Review Letters_ , 97(16):168302, October 2006. ISSN 0031-9007, 1079-7114. doi: 10.1103/PhysRevLett.97.168302. URL `https://link. aps.org/doi/10.1103/PhysRevLett.97.168302` .

- [90] Xiaoming Fu, Heta P. Patel, Stefano Coppola, Libin Xu, Zhixing Cao, Tineke L. Lenstra, and Ramon Grima. Accurate inference of stochastic gene expression from nascent transcript heterogeneity. Preprint, bioRxiv: 2021.11.09.467882, November 2021. URL `http://biorxiv. org/lookup/doi/10.1101/2021.11.09.467882` .

- [91] Xiaoming Fu, Heta P Patel, Stefano Coppola, Libin Xu, Zhixing Cao, Tineke L Lenstra, and Ramon Grima. Quantifying how post-transcriptional noise and gene copy number variation bias transcriptional parameter inference from mRNA distributions. _eLife_ , 11:e82493, October 2022. ISSN 2050-084X. doi: 10.7554/eLife.82493. URL `https://elifesciences. org/articles/82493` .

- [92] Takashi Fukaya, Bomyi Lim, and Michael Levine. Enhancer Control of Transcriptional Bursting. _Cell_ , 166(2):358–368, July 2016. ISSN 00928674. doi: 10.1016/j.cell.2016.05.025. URL `https://linkinghub.elsevier. com/retrieve/pii/S0092867416305736` .

- [93] Jie Gao, Yue Ma, Hua-Lin Fu, Qian Luo, Zhen Wang, Yu-Huan Xiao, Hao Yang, Da-Xiang Cui, and Wei-Lin Jin. Non-catalytic roles for TET1 protein negatively regulating neuronal differentiation through srGAP3 in neuroblastoma cells. _Protein & Cell_ , 7(5):351–361, May 2016. ISSN 1674-8018. doi: 10.1007/s13238-016-0267-4. URL `https://doi.org/10.1007/s13238016-0267-4` .

- [94] C. W. Gardiner and S. Chaturvedi. The poisson representation. I. A new technique for chemical master equations. _Journal of Statistical Physics_ , 17(6):429–468, December 1977. ISSN 0022-4715, 1572-9613. doi: 10.1007/BF01014349. URL `http://link.springer.com/10.1007/ BF01014349` .

- [95] Crispin Gardiner. _Handbook of Stochastic Methods for Physics, Chemistry, and the Natural Sciences_ . Springer, third edition, 2004.

- [96] Adam Gayoso, Zoë Steier, Romain Lopez, Jeffrey Regier, Kristopher L. Nazor, Aaron Streets, and Nir Yosef. Joint probabilistic modeling of singlecell multi-omic data with totalVI. _Nature Methods_ , 18(3):272–282, March 2021. ISSN 1548-7091, 1548-7105. doi: 10.1038/s41592-020-01050-x. URL `http://www.nature.com/articles/s41592-020-01050-x` .

- [97] Adam Gayoso, Romain Lopez, Galen Xing, Pierre Boyeau, Valeh Valiollah Pour Amiri, Justin Hong, Katherine Wu, Michael Jayasuriya, Edouard

154

Mehlman, Maxime Langevin, Yining Liu, Jules Samaran, Gabriel Misrachi, Achille Nazaret, Oscar Clivio, Chenling Xu, Tal Ashuach, Mariano Gabitto, Mohammad Lotfollahi, Valentine Svensson, Eduardo da Veiga Beltrame, Vitalii Kleshchevnikov, Carlos Talavera-López, Lior Pachter, Fabian J. Theis, Aaron Streets, Michael I. Jordan, Jeffrey Regier, and Nir Yosef. A Python library for probabilistic analysis of single-cell omics data. _Nature Biotechnology_ , 40(2):163–166, February 2022. ISSN 1087-0156, 15461696. doi: 10.1038/s41587-021-01206-w. URL `https://www.nature. com/articles/s41587-021-01206-w` .

- [98] Daniel T Gillespie. A general method for numerically simulating the stochastic time evolution of coupled chemical reactions. _Journal of Computational Physics_ , 22(4):403–434, December 1976. ISSN 00219991. doi: 10.1016/0021-9991(76)90041-3. URL `https://linkinghub.elsevier. com/retrieve/pii/0021999176900413` .

- [99] Daniel T. Gillespie. Exact stochastic simulation of coupled chemical reactions. _The Journal of Physical Chemistry_ , 81(25):2340–2361, December 1977. ISSN 0022-3654, 1541-5740. doi: 10.1021/j100540a008. URL `https://pubs.acs.org/doi/abs/10.1021/j100540a008` .

- [100] Daniel T. Gillespie. The chemical Langevin equation. _The Journal of Chemical Physics_ , 113(1):297–306, July 2000. ISSN 0021-9606, 1089-7690. doi: 10.1063/1.481811. URL `http://aip.scitation.org/doi/10.1063/1. 481811` .

- [101] Roy J. Glauber. Time-Dependent Statistics of the Ising Model. _Journal of Mathematical Physics_ , 4(2):294–307, February 1963. ISSN 0022-2488, 1089-7658. doi: 10.1063/1.1703954. URL `http://aip.scitation.org/ doi/10.1063/1.1703954` .

- [102] Ido Golding, Johan Paulsson, Scott M. Zawilski, and Edward C. Cox. Real-Time Kinetics of Gene Activity in Individual Bacteria. _Cell_ , 123 (6):1025–1036, December 2005. ISSN 00928674. doi: 10.1016/j.cell. 2005.09.031. URL `https://linkinghub.elsevier.com/retrieve/ pii/S0092867405010378` .

- [103] Gennady Gorin and Lior Pachter. Intrinsic and extrinsic noise are distinguishable in a synthesis – export – degradation model of mRNA production. Preprint, bioRxiv: 2020.09.25.312868, September 2020. URL `http://biorxiv.org/lookup/doi/10.1101/2020.09.25.312868` .

- [104] Gennady Gorin and Lior Pachter. Special function methods for bursty models of transcription. _Physical Review E_ , 102(2):022409, August 2020. ISSN 2470-0045, 2470-0053. doi: 10.1103/PhysRevE.102.022409. URL `https: //link.aps.org/doi/10.1103/PhysRevE.102.022409` .

155

- [105] Gennady Gorin and Lior Pachter. Modeling bursty transcription and splicing with the chemical master equation. _Biophysical Journal_ , 121(6):1056–1069, February 2022. doi: 10.1016/j.bpj.2022.02.004. URL `https://www.cell. com/biophysj/fulltext/S0006-3495(22)00104-7` .

- [106] Gennady Gorin and Lior Pachter. Distinguishing biophysical stochasticity from technical noise in single-cell RNA sequencing using _Monod_ . Preprint, bioRxiv: 2022.06.11.495771, April 2023. URL `https://www.biorxiv. org/content/10.1101/2022.06.11.495771v2` .

- [107] Gennady Gorin and Lior Pachter. Length biases in single-cell RNA sequencing of pre-mRNA. _Biophysical Reports_ , 3(1):100097, March 2023. ISSN 26670747. doi: 10.1016/j.bpr.2022.100097. URL `https://linkinghub. elsevier.com/retrieve/pii/S2667074722000544` .

- [108] Gennady Gorin and Lior Pachter. The telegraph process is not a subordinator. Preprint, bioRxiv: 2023.01.17.524309, January 2023. URL `http://biorxiv.org/lookup/doi/10.1101/2023.01.17.524309` .

- [109] Gennady Gorin, Valentine Svensson, and Lior Pachter. Protein velocity and acceleration from single-cell multiomics experiments. _Genome Biology_ , 21:39, February 2020. ISSN 1474-760X. doi: 10.1186/s13059-020-19453. URL `https://genomebiology.biomedcentral.com/articles/10. 1186/s13059-020-1945-3` .

- [110] Gennady Gorin, Mengyu Wang, Ido Golding, and Heng Xu. Stochastic simulation and statistical inference platform for visualization and estimation of transcriptional kinetics. _PLOS ONE_ , 15(3):e0230736, March 2020. ISSN 1932-6203. doi: 10.1371/journal.pone.0230736. URL `https://dx.plos. org/10.1371/journal.pone.0230736` .

- [111] Gennady Gorin, Maria Carilli, Tara Chari, and Lior Pachter. Spectral neural approximations for models of transcriptional dynamics. Preprint, bioRxiv: 2022.06.16.496448, June 2022. URL `http://biorxiv.org/ lookup/doi/10.1101/2022.06.16.496448` .

- [112] Gennady Gorin, Meichen Fang, Tara Chari, and Lior Pachter. RNA velocity unraveled. _PLOS Computational Biology_ , 18(9):e1010492, September 2022. URL `https://journals.plos.org/ploscompbiol/article? id=10.1371/journal.pcbi.1010492` .

- [113] Gennady Gorin, John J. Vastola, Meichen Fang, and Lior Pachter. Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments. _Nature Communications_ , 13(1): 7620, December 2022. ISSN 2041-1723. doi: 10.1038/s41467-022-34857-7. URL `https://www.nature.com/articles/s41467-022-34857-7` .

156

- [114] Gennady Gorin, Shawn Yoshida, and Lior Pachter. Transient and delay chemical master equations. Preprint, bioRxiv: 2022.10.17.512599, October 2022. URL `http://biorxiv.org/lookup/doi/10.1101/2022.10.17. 512599` .

- [115] Gennady Gorin, John J. Vastola, and Lior Pachter. Stochastic systems biology of the cell using single-cell genomics data. Preprint, bioRxiv: in prep., April 2023. URL `Inprep.`

- [116] Dominic Grün, Lennart Kester, and Alexander van Oudenaarden. Validation of noise models for single-cell transcriptomics. _Nature Methods_ , 11(6):637– 640, June 2014. ISSN 1548-7091, 1548-7105. doi: 10.1038/nmeth.2930. URL `http://www.nature.com/articles/nmeth.2930` .

- [117] Jingtao Guo, Edward J. Grow, Hana Mlcochova, Geoffrey J. Maher, Cecilia Lindskog, Xichen Nie, Yixuan Guo, Yodai Takei, Jina Yun, Long Cai, Robin Kim, Douglas T. Carrell, Anne Goriely, James M. Hotaling, and Bradley R. Cairns. The adult human testis transcriptional cell atlas. _Cell Research_ , 28(12):1141–1157, December 2018. ISSN 1001-0602, 1748-7838. doi: 10.1038/s41422-018-0099-2. URL `http://www.nature.com/articles/ s41422-018-0099-2` .

- [118] Ankit Gupta, Jan Mikelson, and Mustafa Khammash. A finite state projection algorithm for the stationary solution of the chemical master equation. _The Journal of Chemical Physics_ , 147(15):154101, October 2017. ISSN 00219606, 1089-7690. doi: 10.1063/1.5006484. URL `http://aip.scitation. org/doi/10.1063/1.5006484` .

- [119] Anushka Gupta, Farnaz Shamsi, Nicolas Altemose, Gabriel F. Dorlhiac, Aaron M. Cypess, Andrew P. White, Nir Yosef, Mary Elizabeth Patti, Yu-Hua Tseng, and Aaron Streets. Characterization of transcript enrichment and detection bias in single-nucleus RNA-seq for mapping of distinct human adipocyte lineages. _Genome Research_ , 32(2):242–257, February 2022. ISSN 1088-9051, 1549-5469. doi: 10.1101/gr.275509.121. URL `http://genome.cshlp.org/lookup/doi/10.1101/gr.275509.121` .

- [120] R. Gupta, D. Cerletti, G. Gut, A. Oxenius, and M. Claassen. Cytopath: Simulation based inference of differentiation trajectories from RNA velocity fields. Preprint, bioRxiv: 2020.12.21.423801, December 2020. URL `http: //biorxiv.org/lookup/doi/10.1101/2020.12.21.423801` .

- [121] Mariana Gómez-Schiavon, Liang-Fu Chen, Anne E. West, and Nicolas E. Buchler. BayFish: Bayesian inference of transcription dynamics from population snapshots of single-molecule RNA FISH in single cells. _Genome Biology_ , 18(1):164, December 2017. ISSN 1474-760X. doi: 10.1186/ s13059-017-1297-9. URL `https://genomebiology.biomedcentral. com/articles/10.1186/s13059-017-1297-9` .

157

- [122] Brian J Haas, Melissa Chin, Chad Nusbaum, Bruce W Birren, and Jonathan Livny. How deep is deep enough for RNA-Seq profiling of bacterial transcriptomes? _BMC Genomics_ , 13(1):734, December 2012. ISSN 14712164. doi: 10.1186/1471-2164-13-734. URL `https://bmcgenomics. biomedcentral.com/articles/10.1186/1471-2164-13-734` .

- [123] Christoph Hafemeister and Rahul Satĳa. Normalization and variance stabilization of single-cell RNA-seq data using regularized negative binomial regression. _Genome Biology_ , 20:296, December 2019. ISSN 1474760X. doi: 10.1186/s13059-019-1874-1. URL `https://genomebiology. biomedcentral.com/articles/10.1186/s13059-019-1874-1` .

- [124] Lucy Ham, Rowan D. Brackston, and Michael P. H. Stumpf. Extrinsic Noise and Heavy-Tailed Laws in Gene Expression. _Physical Review Letters_ , 124 (10):108101, March 2020. ISSN 0031-9007, 1079-7114. doi: 10.1103/ PhysRevLett.124.108101. URL `https://link.aps.org/doi/10.1103/ PhysRevLett.124.108101` .

- [125] Lucy Ham, David Schnoerr, Rowan D. Brackston, and Michael P. H. Stumpf. Exactly solvable models of stochastic gene expression. _The Journal of Chemical Physics_ , 152(14):144106, April 2020. ISSN 0021-9606, 1089-7690. doi: 10.1063/1.5143540. URL `http://aip.scitation.org/doi/10.1063/ 1.5143540` .

- [126] Xiaoping Han, Ziming Zhou, Lĳiang Fei, Huiyu Sun, Renying Wang, Yao Chen, Haide Chen, Jingjing Wang, Huanna Tang, Wenhao Ge, Yincong Zhou, Fang Ye, Mengmeng Jiang, Junqing Wu, Yanyu Xiao, Xiaoning Jia, Tingyue Zhang, Xiaojie Ma, Qi Zhang, Xueli Bai, Shujing Lai, Chengxuan Yu, Lĳun Zhu, Rui Lin, Yuchi Gao, Min Wang, Yiqing Wu, Jianming Zhang, Renya Zhan, Saiyong Zhu, Hailan Hu, Changchun Wang, Ming Chen, He Huang, Tingbo Liang, Jianghua Chen, Weilin Wang, Dan Zhang, and Guoji Guo. Construction of a human cell landscape at single-cell level. _Nature_ , 581(7808):303–309, May 2020. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586-020-2157-4. URL `http: //www.nature.com/articles/s41586-020-2157-4` .

- [127] Maike M.K. Hansen, Ravi V. Desai, Michael L. Simpson, and Leor S. Weinberger. Cytoplasmic Amplification of Transcriptional Noise Generates Substantial Cell-to-Cell Variability. _Cell Systems_ , 7(4):384–397.e6, October 2018. ISSN 24054712. doi: 10.1016/j.cels.2018.08.002. URL `https: //linkinghub.elsevier.com/retrieve/pii/S240547121830317X` .

- [128] Yuhan Hao, Stephanie Hao, Erica Andersen-Nissen, William M. Mauck, Shiwei Zheng, Andrew Butler, Maddie J. Lee, Aaron J. Wilk, Charlotte Darby, Michael Zager, Paul Hoffman, Marlon Stoeckius, Efthymia Papalexi, Eleni P. Mimitou, Jaison Jain, Avi Srivastava, Tim Stuart, Lamar M. Fleming, Bertrand Yeung, Angela J. Rogers, Juliana M. McElrath, Catherine A. Blish,

158

Raphael Gottardo, Peter Smibert, and Rahul Satĳa. Integrated analysis of multimodal single-cell data. _Cell_ , 184(13):3573–3587.e29, June 2021. ISSN 00928674. doi: 10.1016/j.cell.2021.04.048. URL `https://linkinghub. elsevier.com/retrieve/pii/S0092867421005833` .

- [129] Ashraful Haque, Jessica Engel, Sarah A. Teichmann, and Tapio Lönnberg. A practical guide to single-cell RNA-sequencing for biomedical research and clinical applications. _Genome Medicine_ , 9(1):75, December 2017. ISSN 1756-994X. doi: 10.1186/s13073-017-04674. URL `http://genomemedicine.biomedcentral.com/articles/10. 1186/s13073-017-0467-4` .

- [130] Akdes Serin Harmanci, Arif O Harmanci, Xiaobo Zhou, Benjamin Deneen, Ganesh Rao, Tiemo Klisch, and Akash Patel. scRegulocity: Detection of local RNA velocity patterns in embeddings of single cell RNA-Seq data. Preprint, bioRxiv: 2021.06.01.446674, June 2021. URL `http://biorxiv. org/lookup/doi/10.1101/2021.06.01.446674` .

- [131] Dongze He, Charlotte Soneson, and Rob Patro. Understanding and evaluating ambiguity in single-cell and single-nucleus RNA-sequencing. Preprint, bioRxiv: 2023.01.04.522742, January 2023. URL `http://biorxiv.org/ lookup/doi/10.1101/2023.01.04.522742` .

- [132] S. P. Heims. Master Equation for Ising Model. _Physical Review_ , 138 (2A):A587–A590, April 1965. ISSN 0031-899X. doi: 10.1103/PhysRev. 138.A587. URL `https://link.aps.org/doi/10.1103/PhysRev.138. A587` .

- [133] Cody N. Heiser, Victoria M. Wang, Bob Chen, Jacob J. Hughey, and Ken S. Lau. Automated quality control and cell identification of droplet-based singlecell data using dropkick. _Genome Research_ , 31(10):1742–1752, October 2021. ISSN 1088-9051, 1549-5469. doi: 10.1101/gr.271908.120. URL `http://genome.cshlp.org/lookup/doi/10.1101/gr.271908.120` .

- [134] Lukas Heumos, Anna C. Schaar, Christopher Lance, Anastasia Litinetskaya, Felix Drost, Luke Zappia, Malte D. Lücken, Daniel C. Strobl, Juan Henao, Fabiola Curion, Single-cell Best Practices Consortium, Hananeh Aliee, Meshal Ansari, Pau Badia-i Mompel, Maren Büttner, Emma Dann, Daniel Dimitrov, Leander Dony, Amit Frishberg, Dongze He, Soroor Hediyeh-zadeh, Leon Hetzel, Ignacio L. Ibarra, Matthew G. Jones, Mohammad Lotfollahi, Laura D. Martens, Christian L. Müller, Mor Nitzan, Johannes Ostner, Giovanni Palla, Rob Patro, Zoe Piran, Ciro Ramírez-Suástegui, Julio Saez-Rodriguez, Hirak Sarkar, Benjamin Schubert, Lisa Sikkema, Avi Srivastava, Jovan Tanevski, Isaac Virshup, Philipp Weiler, Herbert B. Schiller, and Fabian J. Theis. Best practices for single-cell analysis across modalities. _Nature Reviews Genetics_ , March 2023. ISSN 1471-0056, 1471-

159

0064. doi: 10.1038/s41576-023-00586-w. URL `https://www.nature. com/articles/s41576-023-00586-w` .

- [135] Brian L. Hie, Kevin K. Yang, and Peter S. Kim. Evolutionary velocity with protein language models predicts evolutionary dynamics of diverse proteins. _Cell Systems_ , 13(4):274–285.e6, April 2022. ISSN 24054712. doi: 10.1016/j.cels.2022.01.003. URL `https://linkinghub.elsevier.com/ retrieve/pii/S2405471222000382` .

- [136] A. Hilfinger and J. Paulsson. Separating intrinsic from extrinsic fluctuations in dynamic biological systems. _Proceedings of the National Academy of Sciences_ , 108(29):12167–12172, July 2011. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas.1018832108. URL `http://www.pnas.org/cgi/doi/ 10.1073/pnas.1018832108` .

- [137] Andreas Hilfinger, Thomas M. Norman, Glenn Vinnicombe, and Johan Paulsson. Constraints on Fluctuations in Sparsely Characterized Biological Systems. _Physical Review Letters_ , 116(5):058101, February 2016. ISSN 0031-9007, 1079-7114. doi: 10.1103/PhysRevLett.116.058101. URL `https://link.aps.org/doi/10.1103/PhysRevLett.116.058101` .

- [138] Andreas Hilfinger, Thomas M. Norman, and Johan Paulsson. Exploiting Natural Fluctuations to Identify Kinetic Mechanisms in Sparsely Characterized Systems. _Cell Systems_ , 2(4):251–259, April 2016. ISSN 24054712. doi: 10.1016/j.cels.2016.04.002. URL `https://linkinghub.elsevier.com/ retrieve/pii/S2405471216301107` .

- [139] Ariel A. Hippen, Matias M. Falco, Lukas M. Weber, Erdogan Pekcan Erkan, Kaiyang Zhang, Jennifer Anne Doherty, Anna Vähärautio, Casey S. Greene, and Stephanie C. Hicks. miQC: An adaptive probabilistic framework for quality control of single-cell RNA-sequencing data. _PLOS Computational Biology_ , 17(8):e1009290, August 2021. ISSN 1553-7358. doi: 10.1371/ journal.pcbi.1009290. URL `https://dx.plos.org/10.1371/journal. pcbi.1009290` .

- [140] Bo Hu, David A. Kessler, Wouter-Jan Rappel, and Herbert Levine. How input fluctuations reshape the dynamics of a biological switching system. _Physical review. E, Statistical, nonlinear, and soft matter physics_ , 86(6 Pt 1):061910, December 2012. ISSN 1539-3755. doi: 10.1103/PhysRevE.86.061910. URL `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5836738/` .

- [141] Lifang Huang, Zhanjiang Yuan, Peĳiang Liu, and Tianshou Zhou. Feedbackinduced counterintuitive correlations of gene expression noise with bursting kinetics. _Physical Review E_ , 90(5):052702, November 2014. ISSN 1539-3755, 1550-2376. doi: 10.1103/PhysRevE.90.052702. URL `https: //link.aps.org/doi/10.1103/PhysRevE.90.052702` .

160

- [142] Virginie Imbault, Chiara Dionisi, Gilles Naeĳe, David Communi, and Massimo Pandolfo. Cerebrospinal Fluid Proteomics in Friedreich Ataxia Reveals Markers of Neurodegeneration and Neuroinflammation. _Frontiers in Neuroscience_ , 16:885313, July 2022. ISSN 1662-4548. doi: 10.3389/fnins. 2022.885313. URL `https://www.ncbi.nlm.nih.gov/pmc/articles/ PMC9326443/` .

- [143] Srividya Iyer-Biswas and C. Jayaprakash. Mixed Poisson distributions in exact solutions of stochastic auto-regulation models. _Physical Review E_ , 90 (5):052712, November 2014. ISSN 1539-3755, 1550-2376. doi: 10.1103/ PhysRevE.90.052712. URL `http://arxiv.org/abs/1110.2804` . arXiv: 1110.2804.

- [144] Srividya Iyer-Biswas, F. Hayot, and C. Jayaprakash. Stochasticity of gene products from transcriptional pulsing. _Physical Review E_ , 79(3):031911, March 2009. ISSN 1539-3755, 1550-2376. doi: 10.1103/PhysRevE.79. 031911. URL `https://link.aps.org/doi/10.1103/PhysRevE.79. 031911` .

- [145] François Jacob and Jacques Monod. Genetic regulatory mechanisms in the synthesis of proteins. _Journal of Molecular Biology_ , 3(3):318–356, June 1961. doi: 10.1016/S0022-2836(61)80072-7. URL `https://www. sciencedirect.com/science/article/pii/S0022283661800727` .

- [146] Tobias Jahnke and Wilhelm Huisinga. Solving the chemical master equation for monomolecular reaction systems analytically. _Journal of Mathematical Biology_ , 54:1–26, September 2006. ISSN 0303-6812, 1432-1416. doi: 10. 1007/s00285-006-0034-x. URL `http://link.springer.com/10.1007/ s00285-006-0034-x` .

- [147] Selina Jansky, Ashwini Kumar Sharma, Verena Körber, Andrés Quintero, Umut H. Toprak, Elisa M. Wecht, Moritz Gartlgruber, Alessandro Greco, Elad Chomsky, Thomas G. P. Grünewald, Kai-Oliver Henrich, Amos Tanay, Carl Herrmann, Thomas Höfer, and Frank Westermann. Single-cell transcriptomic analyses provide insights into the developmental origins of neuroblastoma. _Nature Genetics_ , 53(5):683–693, May 2021. ISSN 1061-4036, 1546-1718. doi: 10.1038/s41588-021-00806-1. URL `http://www.nature.com/articles/s41588-021-00806-1` .

- [148] Garrett Jenkinson, Jordi Abante, Andrew P. Feinberg, and John Goutsias. An information-theoretic approach to the modeling and analysis of whole-genome bisulfite sequencing data. _BMC Bioinformatics_ , 19(1):87, December 2018. ISSN 1471-2105. doi: 10.1186/s12859-018-2086-5. URL `https://bmcbioinformatics.biomedcentral.com/articles/ 10.1186/s12859-018-2086-5` .

161

- [149] Chen Jia. Kinetic Foundation of the Zero-Inflated Negative Binomial Model for Single-Cell RNA Sequencing Data. _SIAM Journal on Applied Mathematics_ , 80(3):1336–1355, January 2020. ISSN 0036-1399, 1095-712X. doi: 10.1137/19M1253198. URL `https://epubs.siam.org/doi/10.1137/ 19M1253198` .

- [150] Chen Jia and Ramon Grima. Coupling gene expression dynamics to cell size dynamics and cell cycle events: Exact and approximate solutions of the extended telegraph model. _iScience_ , 26(1):105746, January 2023. ISSN 25890042. doi: 10.1016/j.isci.2022.105746. URL `https://linkinghub. elsevier.com/retrieve/pii/S2589004222020193` .

- [151] Qingchao Jiang, Xiaoming Fu, Shifu Yan, Runlai Li, Wenli Du, Zhixing Cao, Feng Qian, and Ramon Grima. Neural network aided approximation and parameter inference of non-Markovian models of gene expression. _Nature Communications_ , 12(1):2618, December 2021. ISSN 2041-1723. doi: 10. 1038/s41467-021-22919-1. URL `http://www.nature.com/articles/ s41467-021-22919-1` .

- [152] Jing Jin, Priyadarshini Ravindran, Danila Di Meo, and Andreas W. Püschel. Igf1R/InsR function is required for axon extension and corpus callosum formation. _PLOS ONE_ , 14(7):e0219362, July 2019. ISSN 1932-6203. doi: 10.1371/journal.pone.0219362. URL `https://dx.plos.org/10.1371/ journal.pone.0219362` .

- [153] Fritz John. _Partial Differential Equations_ . Springer US, New York, NY, 1978. ISBN 978-1-4684-0059-5 978-1-4684-0061-8. URL `http://public. eblib.com/choice/publicfullrecord.aspx?p=3082466` . OCLC: 859156366.

- [154] Norman Lloyd Johnson, Samuel Kotz, and N. Balakrishnan. _Continuous univariate distributions, Vol. 1_ . Wiley series in probability and mathematical statistics. Wiley, New York, 2nd ed edition, 1994. ISBN 978-0-471-58495-7 978-0-471-58494-0.

- [155] Norman Lloyd Johnson, Adrienne W. Kemp, and Samuel Kotz. _Univariate discrete distributions_ . Wiley, Hoboken, N.J, 3rd ed edition, 2005. ISBN 978-0-471-27246-5.

- [156] Euan Joly-Smith, Zitong Jerry Wang, and Andreas Hilfinger. Inferring gene regulation dynamics from static snapshots of gene expression variability. _Physical Review E_ , 104(4):044406, October 2021. ISSN 2470-0045, 24700053. doi: 10.1103/PhysRevE.104.044406. URL `https://link.aps. org/doi/10.1103/PhysRevE.104.044406` .

- [157] Dimitris Karlis and Evdokia Xekalaki. Mixed Poisson Distributions. _International Statistical Review / Revue Internationale de Statistique_ , 73(1):

162

35–58, 2005. ISSN 0306-7734. URL `http://www.jstor.org/stable/ 25472639` .

- [158] O Kessler, Y Jiang, and L A Chasin. Order of intron removal during splicing of endogenous adenine phosphoribosyltransferase and dihydrofolate reductase pre-mRNA. _Molecular and Cellular Biology_ , 13(10):6211–6222, October 1993. ISSN 0270-7306, 1098-5549. doi: 10.1128/MCB.13.10.6211. URL `http://mcb.asm.org/lookup/doi/10.1128/MCB.13.10.6211` .

- [159] Jong Kim and John C Marioni. Inferring the kinetics of stochastic gene expression from single-cell RNA-sequencing data. _Genome Biology_ , 14:R7, 2013. ISSN 1465-6906. doi: 10.1186/gb-2013-14-1r7. URL `http://genomebiology.biomedcentral.com/articles/10. 1186/gb-2013-14-1-r7` .

- [160] Tae Hyun Kim, Xiang Zhou, and Mengjie Chen. Demystifying “drop-outs” in single-cell UMI data. _Genome Biology_ , 21:196, December 2020. ISSN 1474-760X. doi: 10.1186/s13059-020-02096y. URL `https://genomebiology.biomedcentral.com/articles/10. 1186/s13059-020-02096-y` .

- [161] Alena Klindziuk and Anatoly B. Kolomeisky. Understanding the molecular mechanisms of transcriptional bursting. _Physical Chemistry Chemical Physics_ , page 10.1039.D1CP03665C, 2021. ISSN 1463-9076, 14639084. doi: 10.1039/D1CP03665C. URL `http://xlink.rsc.org/?DOI= D1CP03665C` .

- [162] Dmitry Kobak and Philipp Berens. The art of using t-SNE for singlecell transcriptomics. _Nature Communications_ , 10(1):5416, December 2019. ISSN 2041-1723. doi: 10.1038/s41467-019-13056-x. URL `http://www. nature.com/articles/s41467-019-13056-x` .

- [163] Colin Koopman. Problematization. In Leonard Lawlor and John Nale, editors, _The Cambridge Foucault Lexicon_ , pages 399–403. Cambridge University Press, 1 edition, April 2014. ISBN 978-1139-02230-9 978-0-521-11921-4. doi: 10.1017/CBO9781139022309. 070. URL `https://www.cambridge.org/core/product/identifier/ 9781139022309%23c11921-68-1/type/book_part` .

- [164] Renata Kowara, Michel Ménard, Leslie Brown, and Balu Chakravarthy. Co-localization and interaction of DPYSL3 and GAP43 in primary cortical neurons. _Biochemical and Biophysical Research Communications_ , 363(1):190–193, November 2007. ISSN 0006291X. doi: 10.1016/j.bbrc. 2007.08.163. URL `https://linkinghub.elsevier.com/retrieve/ pii/S0006291X07018840` .

- [165] XL. Kuang, XM. Zhao, HF. Xu, YY. Shi, JB. Deng, and GT. Sun. Spatio-temporal expression of a novel neuron-derived neurotrophic factor

163

(ndnf) in mouse brains during development. _BMC Neuroscience_ , 11:137, 2010. doi: 10.1186/1471-2202-11-137. URL `https://bmcneurosci. biomedcentral.com/articles/10.1186/1471-2202-11-137` .

- [166] Niraj Kumar, Thierry Platini, and Rahul V. Kulkarni. Exact Distributions for Stochastic Gene Expression Models with Bursting and Feedback. _Physical Review Letters_ , 113(26):268105, December 2014. ISSN 0031-9007, 10797114. doi: 10.1103/PhysRevLett.113.268105. URL `https://link.aps. org/doi/10.1103/PhysRevLett.113.268105` .

- [167] Juan Kuntz, Philipp Thomas, Guy-Bart Stan, and Mauricio Barahona. The Exit Time Finite State Projection Scheme: Bounding Exit Distributions and Occupation Measures of Continuous-Time Markov Chains. _SIAM Journal on Scientific Computing_ , 41(2):A748–A769, January 2019. ISSN 1064-8275, 1095-7197. doi: 10.1137/18M1168261. URL `https://epubs.siam.org/ doi/10.1137/18M1168261` .

- [168] Gioele La Manno, Ruslan Soldatov, Amit Zeisel, Emelie Braun, Hannah Hochgerner, Viktor Petukhov, Katja Lidschreiber, Maria E. Kastriti, Peter Lönnerberg, Alessandro Furlan, Jean Fan, Lars E. Borm, Zehua Liu, David van Bruggen, Jimin Guo, Xiaoling He, Roger Barker, Erik Sundström, Gonçalo Castelo-Branco, Patrick Cramer, Igor Adameyko, Sten Linnarsson, and Peter V. Kharchenko. RNA velocity of single cells. _Nature_ , 560(7719): 494–498, August 2018. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586018-0414-6. URL `http://www.nature.com/articles/s41586-0180414-6` .

- [169] Blue B. Lake, Simone Codeluppi, Yun C. Yung, Derek Gao, Jerold Chun, Peter V. Kharchenko, Sten Linnarsson, and Kun Zhang. A comparative strategy for single-nucleus and single-cell transcriptomes confirms accuracy in predicted cell-type expression from nuclear RNA. _Scientific Reports_ , 7 (1):6031, July 2017. ISSN 2045-2322. doi: 10.1038/s41598-017-04426-w. URL `https://www.nature.com/articles/s41598-017-04426-w` .

- [170] Nicholas C. Lammers, Yang Joon Kim, Jiaxi Zhao, and Hernan G. Garcia. A matter of time: Using dynamics and theory to uncover mechanisms of transcriptional bursting. _Current Opinion in Cell Biology_ , 67:147–157, December 2020. ISSN 09550674. doi: 10.1016/j.ceb.2020.08.001. URL `https: //linkinghub.elsevier.com/retrieve/pii/S0955067420300971` .

- [171] Marius Lange, Volker Bergen, Michal Klein, Manu Setty, Bernhard Reuter, Mostafa Bakhti, Heiko Lickert, Meshal Ansari, Janine Schniering, Herbert B. Schiller, Dana Pe’er, and Fabian J. Theis. CellRank for directed singlecell fate mapping. _Nature Methods_ , 19(2):159–170, February 2022. ISSN 1548-7091, 1548-7105. doi: 10.1038/s41592-021-01346-6. URL `https: //www.nature.com/articles/s41592-021-01346-6` .

164

- [172] Anton J. M. Larsson, Per Johnsson, Michael Hagemann-Jensen, Leonard Hartmanis, Omid R. Faridani, Björn Reinius, Asa Segerstolpe, Chloe M. Rivera, Bing Ren, and Rickard Sandberg. Genomic encoding of transcriptional burst kinetics. _Nature_ , 565(7738):251–254, January 2019. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586-018-0836-1. URL `http: //www.nature.com/articles/s41586-018-0836-1` .

- [173] Hugo Lavenant, Stephen Zhang, Young-Heon Kim, and Geoffrey Schiebinger. Towards a mathematical theory of trajectory inference. Preprint, arXiv: 2102.09204, February 2021. URL `http://arxiv.org/abs/2102.09204` .

- [174] Sungwoo Lee, Eĳiro Nakamura, Haifeng Yang, Wenyi Wei, Michelle S. Linggi, Mini P. Sajan, Robert V. Farese, Robert S. Freeman, Bruce D. Carter, William G. Kaelin, and Susanne Schlisio. Neuronal apoptosis linked to EglN3 prolyl hydroxylase and familial pheochromocytoma genes: Developmental culling and cancer. _Cancer Cell_ , 8(2):155–167, August 2005. ISSN 15356108. doi: 10.1016/j.ccr.2005.06.015. URL `https: //linkinghub.elsevier.com/retrieve/pii/S1535610805002242` .

- [175] Chen Li, Maria Virgilio, Kathleen L. Collins, and Joshua D. Welch. Single-cell multi-omic velocity infers dynamic and decoupled gene regulation. Preprint, bioRxiv: 2021.12.13.472472, December 2021. URL `http://biorxiv.org/lookup/doi/10.1101/2021.12.13.472472` .

- [176] Fang-Zhen Li, Zhi-E Liu, Xiu-Yuan Li, Li-Mei Bu, Hong-Xia Bu, Hui Liu, and Cai-Ming Zhang. Chromatin 3D structure reconstruction with consideration of adjacency relationship among genomic loci. _BMC Bioinformatics_ , 21(1):272, December 2020. ISSN 1471-2105. doi: 10.1186/s12859-02003612-4. URL `https://bmcbioinformatics.biomedcentral.com/ articles/10.1186/s12859-020-03612-4` .

- [177] Fengrui Li, Xiaofei Tian, Yishu Zhou, Lanhui Zhu, Baojie Wang, Mei Ding, and Hao Pang. Dysregulated expression of secretogranin III is involved in neurotoxin-induced dopaminergic neuron apoptosis. _Journal of Neuroscience Research_ , 90(12):2237–2246, December 2012. ISSN 03604012. doi: 10.1002/jnr.23121. URL `https://onlinelibrary.wiley.com/doi/10. 1002/jnr.23121` .

- [178] Tiejun Li. On the Mathematics of RNA Velocity I: Theoretical Analysis. _CSIAM Transactions on Applied Mathematics_ , 2(1):1–55, June 2021. ISSN 2708-0560, 2708-0579. doi: 10.4208/csiam-am.SO-2020-0001. URL `http: //global-sci.org/intro/article_detail/csiam-am/18653.html` .

- [179] Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, Andrew Stuart, and Anima Anandkumar. Fourier Neural Operator for Parametric Partial Differential Equations. Preprint, arXiv: 2010.08895, May 2021. URL `http://arxiv.org/abs/2010.08895` .

165

- [180] Xiang Lin, Tian Tian, Zhi Wei, and Hakon Hakonarson. Clustering of single-cell multi-omics data with a multimodal deep learning method. _Nature Communications_ , 13(1):7705, December 2022. ISSN 2041-1723. doi: 10.1038/s41467-022-35031-9. URL `https://www.nature.com/ articles/s41467-022-35031-9` .

- [181] Zhixiang Lin, Mahdi Zamanighomi, Timothy Daley, Shining Ma, and Wing Hung Wong. Model-Based Approach to the Joint Analysis of SingleCell Data on Chromatin Accessibility and Gene Expression. _Statistical Science_ , 35(1), February 2020. ISSN 0883-4237. doi: 10.1214/19-STS714. URL `https://projecteuclid.org/journals/statisticalscience/volume-35/issue-1/Model-Based-Approach-to-theJoint-Analysis-of-Single-Cell/10.1214/19-STS714.full` .

- [182] Monika Litviňuková, Carlos Talavera-López, Henrike Maatz, Daniel Reichart, Catherine L. Worth, Eric L. Lindberg, Masatoshi Kanda, Krzysztof Polanski, Matthias Heinig, Michael Lee, Emily R. Nadelmann, Kenny Roberts, Liz Tuck, Eirini S. Fasouli, Daniel M. DeLaughter, Barbara McDonough, Hiroko Wakimoto, Joshua M. Gorham, Sara Samari, Krishnaa T. Mahbubani, Kourosh Saeb-Parsy, Giannino Patone, Joseph J. Boyle, Hongbo Zhang, Hao Zhang, Anissa Viveiros, Gavin Y. Oudit, Omer Ali Bayraktar, J. G. Seidman, Christine E. Seidman, Michela Noseda, Norbert Hubner, and Sarah A. Teichmann. Cells of the adult human heart. _Nature_ , 588(7838):466– 472, December 2020. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586020-2797-4. URL `https://www.nature.com/articles/s41586-0202797-4` .

- [183] Ruishan Liu, Angela Oliveira Pisco, Emelie Braun, Sten Linnarsson, and James Zou. Dynamical Systems Model of RNA Velocity Improves Inference of Single-cell Trajectory, Pseudo-time and Gene Regulation. _Journal of Molecular Biology_ , 434(15):167606, August 2022. ISSN 00222836. doi: 10.1016/j.jmb.2022.167606. URL `https://linkinghub.elsevier. com/retrieve/pii/S0022283622001863` .

- [184] Manyuan Long and Michael Deutsch. Intron-exon structures of eukaryotic model organisms. _Nucleic Acids Research_ , 27(15):3219–3228, August 1999. ISSN 1362-4962, 0305-1048. doi: 10.1093/nar/27.15.3219. URL `https: //academic.oup.com/nar/article/27/15/3219/2549228` .

- [185] Romain Lopez, Jeffrey Regier, Michael B. Cole, Michael I. Jordan, and Nir Yosef. Deep generative modeling for single-cell transcriptomics. _Nature Methods_ , 15(12):1053–1058, December 2018. ISSN 1548-7091, 15487105. doi: 10.1038/s41592-018-0229-2. URL `http://www.nature.com/ articles/s41592-018-0229-2` .

- [186] Michael I Love, Wolfgang Huber, and Simon Anders. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. _Genome_

166

_Biology_ , 15(12):550, December 2014. ISSN 1474-760X. doi: 10.1186/ s13059-014-0550-8. URL `http://genomebiology.biomedcentral. com/articles/10.1186/s13059-014-0550-8` .

- [187] Malte D Luecken and Fabian J Theis. Current best practices in single-cell RNA-seq analysis: a tutorial. _Molecular Systems Biology_ , 15(6):e8746, June 2019. ISSN 1744-4292, 1744-4292, 1744-4292. doi: 10.15252/msb. 20188746. URL `http://msb.embopress.org/lookup/doi/10.15252/ msb.20188746` .

- [188] Yudell L Luke. _The Special Functions and Their Approximations, Vol 1_ . Academic Press, London ; New York, 1969.

- [189] Gudrun Lutsch, Roland Vetter, Ulrike Offhauss, Martin Wieske, HermannJosef Gröne, Roman Klemenz, Ingolf Schimke, Joachim Stahl, and Rainer Benndorf. Abundance and Location of the Small Heat Shock Proteins HSP25 and aB-Crystallin in Rat and Human Heart. _Circulation_ , 96 (10):3466–3476, 1997. doi: 10.1161/01.CIR.96.10.3466. URL `https: //www.ahajournals.org/doi/abs/10.1161/01.CIR.96.10.3466` .

- [190] Martin Ian Paguio Malgapo. _Structure and function of the palmitoyltransferase dhhc20 and the acyl coa hydrolase mblac2_ . PhD Dissertation, Cornell, Ithaca, NY, December 2019. URL `https://ecommons.cornell. edu/handle/1813/70073` .

- [191] Aanchal Malhotra, Samarendra Das, and Shesh N. Rai. Analysis of Single-Cell RNA-Sequencing Data: A Step-by-Step Guide. _BioMedInformatics_ , 2(1):43–61, December 2021. ISSN 2673-7426. doi: 10. 3390/biomedinformatics2010003. URL `https://www.mdpi.com/26737426/2/1/3` .

- [192] Valérie Marot-Lassauzaie, Brigitte Joanne Bouman, Fearghal Declan Donaghy, Yasmin Demerdash, Marieke Alida Gertruda Essers, and Laleh Haghverdi. Towards reliable quantification of cell state velocities. _PLOS Computational Biology_ , 18(9):e1010031, September 2022. ISSN 15537358. doi: 10.1371/journal.pcbi.1010031. URL `https://dx.plos.org/ 10.1371/journal.pcbi.1010031` .

- [193] S. Mauch and M. Stalzer. An efficient method for computing steady state solutions with Gillespie’s direct method. _The Journal of Chemical Physics_ , 133(14):144108, October 2010. ISSN 0021-9606. doi: 10.1063/1.3489354. URL `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2973983/` .

- [194] Maxime Mazille, Katarzyna Buczak, Peter Scheiffele, and Oriane Mauger. Stimulus-specific remodeling of the neuronal transcriptome through nuclear intron-retaining transcripts. _The EMBO Journal_ , 41(21):e110192, 2022. doi: https://doi.org/10.15252/embj.2021110192. URL `https: //www.embopress.org/doi/abs/10.15252/embj.2021110192` .

167

- [195] Leland McInnes, John Healy, and James Melville. UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. Preprint, arXiv: 1802.03426v2, December 2018. URL `http://arxiv.org/abs/ 1802.03426` . arXiv: 1802.03426.

- [196] Páll Melsted, Vasilis Ntranos, and Lior Pachter. The barcode, UMI, set format and BUStools. _Bioinformatics_ , page btz279, 2019. doi: 10.1093/ bioinformatics/btz279.

- [197] Páll Melsted, A. Sina Booeshaghi, Lauren Liu, Fan Gao, Lambda Lu, Kyung Hoi Min, Eduardo da Veiga Beltrame, Kristján Eldjárn Hjörleifsson, Jase Gehring, and Lior Pachter. Modular, efficient and constant-memory single-cell RNA-seq preprocessing. _Nature Biotechnology_ , 39(7):813–818, July 2021. ISSN 1087-0156, 1546-1696. doi: 10.1038/s41587-021-00870-2. URL `http://www.nature.com/articles/s41587-021-00870-2` .

- [198] Eleni P. Mimitou, Caleb A. Lareau, Kelvin Y. Chen, Andre L. ZorzettoFernandes, Yuhan Hao, Yusuke Takeshima, Wendy Luo, Tse-Shun Huang, Bertrand Z. Yeung, Efthymia Papalexi, Pratiksha I. Thakore, Tatsuya Kibayashi, James Badger Wing, Mayu Hata, Rahul Satĳa, Kristopher L. Nazor, Shimon Sakaguchi, Leif S. Ludwig, Vĳay G. Sankaran, Aviv Regev, and Peter Smibert. Scalable, multimodal profiling of chromatin accessibility, gene expression and protein levels in single cells. _Nature Biotechnology_ , 39(10):1246–1258, October 2021. ISSN 1087-0156, 1546-1696. doi: 10.1038/s41587-021-00927-2. URL `https://www.nature.com/ articles/s41587-021-00927-2` .

- [199] Qianxing Mo and Faming Liang. Bayesian Modeling of ChIP-chip Data Through a High-Order Ising Model. _Biometrics_ , 66(4):1284–1294, 2010. ISSN 0006-341X. URL `https://www.jstor.org/stable/40962526` . Publisher: [Wiley, International Biometric Society].

- [200] Elliott W. Montroll. On Coupled Rate Equations with Quadratic Nonlinearities. _Proceedings of the National Academy of Sciences of the United States of America_ , 69(9):2532–2536, 1972. ISSN 0027-8424. URL `https://www.jstor.org/stable/61810` . Publisher: National Academy of Sciences.

- [201] Muir Morrison, Manuel Razo-Mejia, and Rob Phillips. Reconciling kinetic and thermodynamic models of bacterial transcription. _PLOS Computational Biology_ , 17(1):e1008572, January 2021. ISSN 1553-7358. doi: 10.1371/ journal.pcbi.1008572. URL `https://dx.plos.org/10.1371/journal. pcbi.1008572` .

- [202] Lambda Moses and Lior Pachter. Museum of spatial transcriptomics. _Nature Methods_ , 19(5):534–546, May 2022. ISSN 1548-7091, 1548-7105. doi: 10. 1038/s41592-022-01409-2. URL `https://www.nature.com/articles/ s41592-022-01409-2` .

168

- [203] Brian Munsky and Mustafa Khammash. The finite state projection algorithm for the solution of the chemical master equation. _The Journal of Chemical Physics_ , 124(4):044104, 2006. ISSN 0021-9606, 1089-7690. doi: 10.1063/ 1.2145882.

- [204] Brian Munsky, Brooke Trinh, and Mustafa Khammash. Listening to the noise: random fluctuations reveal gene network parameters. _Molecular Systems Biology_ , 5:318, October 2009. ISSN 1744-4292. doi: 10.1038/msb.2009.75. URL `https://www.embopress.org/doi/full/ 10.1038/msb.2009.75` .

- [205] Brian Munsky, Gregor Neuert, and Alexander van Oudenaarden. Using Gene Expression Noise to Understand Gene Regulation. _Science_ , 336(6078):183– 187, April 2012. doi: 10.1126/science.1216379.

- [206] Brian Munsky, Guoliang Li, Zachary R. Fox, Douglas P. Shepherd, and Gregor Neuert. Distribution shapes govern the discovery of predictive models for gene regulation. _Proceedings of the National Academy of Sciences_ , 115 (29):7533–7538, 2018. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas. 1804060115.

- [207] D. K. Nam, S. Lee, G. Zhou, X. Cao, C. Wang, T. Clark, J. Chen, J. D. Rowley, and S. M. Wang. Oligo(dT) primer generates a high frequency of truncated cDNAs through internal poly(A) priming during reverse transcription. _Proceedings of the National Academy of Sciences_ , 99(9):6152–6156, April 2002. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas.092140899. URL `http://www.pnas.org/cgi/doi/10.1073/pnas.092140899` .

- [208] Ilya Narsky and Frank C. Porter. _Statistical Analysis Techniques in Particle Physics: Fits, Density Estimation and Supervised Learning_ . Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim, Germany, November 2013. ISBN 9783-527-67732-0 978-3-527-41086-6. doi: 10.1002/9783527677320. URL `http://doi.wiley.com/10.1002/9783527677320` .

- [209] National Library of Medicine. Gene [Internet], 2004. URL `https://www. ncbi.nlm.nih.gov/gene/` .

- [210] Damien Nicolas, Nick E. Phillips, and Felix Naef. What shapes eukaryotic transcriptional bursting? _Molecular BioSystems_ , 13(7):1280–1290, 2017. ISSN 1742-206X, 1742-2051. doi: 10.1039/C7MB00154A. URL `http: //xlink.rsc.org/?DOI=C7MB00154A` .

- [211] Jun Ohkubo. Karlin-McGregor-like formula in a simple time-inhomogeneous birth–death process. _Journal of Physics A: Mathematical and Theoretical_ , 47(40):405001, October 2014. ISSN 1751-8113, 1751-8121. doi: 10. 1088/1751-8113/47/40/405001. URL `https://iopscience.iop.org/ article/10.1088/1751-8113/47/40/405001` .

169

- [212] Takumi Okamoto, Kazunori Imaizumi, and Masayuki Kaneko. The Role of Tissue-Specific Ubiquitin Ligases, RNF183, RNF186, RNF182 and RNF152, in Disease and Biological Function. _International Journal of Molecular Sciences_ , 21(11):3921, May 2020. ISSN 1422-0067. doi: 10.3390/ ĳms21113921. URL `https://www.mdpi.com/1422-0067/21/11/3921` .

- [213] Jonathan Packer and Cole Trapnell. Single-Cell Multi-omics: An Engine for New Quantitative Models of Gene Regulation. _Trends in Genetics_ , 34(9):653–665, September 2018. ISSN 01689525. doi: 10.1016/j. tig.2018.06.001. URL `https://linkinghub.elsevier.com/retrieve/ pii/S0168952518301082` .

- [214] Olivia Padovan-Merhar, Gautham P. Nair, Andrew G. Biaesch, Andreas Mayer, Steven Scarfone, Shawn W. Foley, Angela R. Wu, L. Stirling Churchman, Abhyudai Singh, and Arjun Raj. Single Mammalian Cells Compensate for Differences in Cellular Volume and DNA Copy Number through Independent Global Transcriptional Mechanisms. _Molecular Cell_ , 58(2):339–352, April 2015. ISSN 10972765. doi: 10.1016/j.molcel. 2015.03.005. URL `https://linkinghub.elsevier.com/retrieve/ pii/S1097276515001707` .

- [215] Harry H Panjer. Mixed Poisson Distributions. In _Encyclopedia of Actuarial Science_ . John Wiley & Sons, Ltd, 2004. ISBN 978-0-470-01250-5.

- [216] Nikolaos Papadopoulos, Parra R Gonzalo, and Johannes Söding. PROSSTT: probabilistic simulation of single-cell RNA-seq data for complex differentiation processes. _Bioinformatics_ , 35(18): 3517–3519, September 2019. ISSN 1367-4803, 1460-2059. doi: 10.1093/bioinformatics/btz078. URL `https://academic.oup.com/ bioinformatics/article/35/18/3517/5305637` .

- [217] Ralph Patrick, David T. Humphreys, Vaibhao Janbandhu, Alicia Oshlack, Joshua W.K. Ho, Richard P. Harvey, and Kitty K. Lo. Sierra: discovery of differential transcript usage from polyA-captured single-cell RNA-seq data. _Genome Biology_ , 21(1):167, December 2020. ISSN 1474-760X. doi: 10.1186/s13059-020-02071-7. URL `https://genomebiology. biomedcentral.com/articles/10.1186/s13059-020-02071-7` .

- [218] Johan Paulsson. Models of stochastic gene expression. _Physics of Life Reviews_ , 2(2):157–175, June 2005. ISSN 15710645. doi: 10.1016/j.plrev. 2005.03.003. URL `https://linkinghub.elsevier.com/retrieve/ pii/S1571064505000138` .

- [219] Jean Peccoud and Bernard Ycard. Markovian Modeling of Gene Product Synthesis. _Theoretical Population Biology_ , 48(2):222–234, 1995. doi: 10. 1006/tpbi.1995.1027.

170

- [220] Ruben Perez-Carrasco, Casper Beentjes, and Ramon Grima. Effects of cell cycle variability on lineage and population measurements of messenger RNA abundance. _Journal of The Royal Society Interface_ , 17(168): 20200360, July 2020. ISSN 1742-5689, 1742-5662. doi: 10.1098/rsif.2020. 0360. URL `https://royalsocietypublishing.org/doi/10.1098/ rsif.2020.0360` .

- [221] Rob Phillips. Napoleon Is in Equilibrium. _Annual Review of Condensed Matter Physics_ , 6(1):85–111, March 2015. ISSN 1947-5454, 1947-5462. doi: 10.1146/annurev-conmatphys-031214014558. URL `http://www.annualreviews.org/doi/10.1146/ annurev-conmatphys-031214-014558` .

- [222] Belinda Phipson, Luke Zappia, and Alicia Oshlack. Gene length and detection bias in single cell RNA sequencing protocols. _F1000Research_ , 6, April 2017. ISSN 2046-1402. doi: 10.12688/f1000research.11290.1. URL `https: //www.ncbi.nlm.nih.gov/pmc/articles/PMC5428526/` .

- [223] Harold Pimentel, John G. Conboy, and Lior Pachter. Keep Me Around: Intron Retention Detection and Analysis. Preprint, arXiv: 1510.00696, October 2015. URL `http://arxiv.org/abs/1510.00696` .

- [224] Harold Pimentel, Marilyn Parra, Sherry L. Gee, Narla Mohandas, Lior Pachter, and John G. Conboy. A dynamic intron retention program enriched in RNA processing genes regulates gene expression during terminal erythropoiesis. _Nucleic Acids Research_ , 44(2):838–851, January 2016. ISSN 03051048, 1362-4962. doi: 10.1093/nar/gkv1168. URL `https://academic. oup.com/nar/article-lookup/doi/10.1093/nar/gkv1168` .

- [225] J. W. Pitman. Occupation Measures for Markov Chains. _Advances in Applied Probability_ , 9(1):69–86, 1977. ISSN 0001-8678. doi: 10.2307/1425817. URL `https://www.jstor.org/stable/1425817` . Publisher: Applied Probability Trust.

- [226] Alex A Pollen, Tomasz J Nowakowski, Joe Shuga, Xiaohui Wang, Anne A Leyrat, Jan H Lui, Nianzhen Li, Lukasz Szpankowski, Brian Fowler, Peilin Chen, Naveen Ramalingam, Gang Sun, Myo Thu, Michael Norris, Ronald Lebofsky, Dominique Toppani, Darnell W Kemp, Michael Wong, Barry Clerkson, Brittnee N Jones, Shiquan Wu, Lawrence Knutsson, Beatriz Alvarado, Jing Wang, Lesley S Weaver, Andrew P May, Robert C Jones, Marc A Unger, Arnold R Kriegstein, and Jay A A West. Low-coverage singlecell mRNA sequencing reveals cellular heterogeneity and activated signaling pathways in developing cerebral cortex. _Nature Biotechnology_ , 32(10):1053– 1058, October 2014. ISSN 1087-0156, 1546-1696. doi: 10.1038/nbt.2967. URL `http://www.nature.com/articles/nbt.2967` .

- [227] A. Prados, J. J. Brey, and B. Sánchez-Rey. A Dynamical Monte Carlo Algorithm for Master Equations with Time-Dependent Transition Rates. _Journal_

171

_of Statistical Physics_ , 89(3-4):709–734, November 1997. ISSN 0022-4715, 1572-9613. doi: 10.1007/BF02765541. URL `http://link.springer. com/10.1007/BF02765541` .

- [228] Aditya Pratapa, Amogh P. Jalihal, Jeffrey N. Law, Aditya Bharadwaj, and T. M. Murali. Benchmarking algorithms for gene regulatory network inference from single-cell transcriptomic data. _Nature Methods_ , 17(2):147–154, February 2020. ISSN 1548-7091, 1548-7105. doi: 10.1038/s41592-0190690-6. URL `http://www.nature.com/articles/s41592-019-06906` .

- [229] Qian Qin, Eli Bingham, Gioele La Manno, David M Langenau, and Luca Pinello. Pyro-Velocity: Probabilistic RNA Velocity inference from singlecell data. Preprint, bioRxiv: 2022.09.12.507691, October 2022. URL `https: //www.biorxiv.org/content/10.1101/2022.09.12.507691v2` .

- [230] Peng Qiu. Embracing the dropouts in single-cell RNA-seq analysis. _Nature Communications_ , 11(1):1169, December 2020. ISSN 2041-1723. doi: 10. 1038/s41467-020-14976-9. URL `http://www.nature.com/articles/ s41467-020-14976-9` .

- [231] Xiaojie Qiu, Yan Zhang, Jorge D. Martin-Rufino, Chen Weng, Shayan Hosseinzadeh, Dian Yang, Angela N. Pogson, Marco Y. Hein, Kyung Hoi (Joseph) Min, Li Wang, Emanuelle I. Grody, Matthew J. Shurtleff, Ruoshi Yuan, Song Xu, Yian Ma, Joseph M. Replogle, Eric S. Lander, Spyros Darmanis, Ivet Bahar, Vĳay G. Sankaran, Jianhua Xing, and Jonathan S. Weissman. Mapping transcriptomic vector fields of single cells. _Cell_ , page S0092867421015774, February 2022. ISSN 00928674. doi: 10.1016/j.cell.2021.12.045. URL `https://linkinghub.elsevier.com/ retrieve/pii/S0092867421015774` .

- [232] Arjun Raj and Alexander van Oudenaarden. Nature, Nurture, or Chance: Stochastic Gene Expression and Its Consequences. _Cell_ , 135(2):216–226, October 2008. ISSN 00928674. doi: 10.1016/j.cell.2008.09.050. URL `https: //linkinghub.elsevier.com/retrieve/pii/S0092867408012439` .

- [233] Arjun Raj, Charles S Peskin, Daniel Tranchina, Diana Y Vargas, and Sanjay Tyagi. Stochastic mRNA Synthesis in Mammalian Cells. _PLoS Biology_ , 4(10):e309, September 2006. ISSN 1545-7885. doi: 10.1371/journal. pbio.0040309. URL `https://dx.plos.org/10.1371/journal.pbio. 0040309` .

- [234] Linda E Reichl. _A Modern Course in Statistical Physics_ . Wiley-VCH Verlag GmbH & Co. KGaA, 4th edition, 2016.

- [235] Kirsten A. Reimer, Claudia A. Mimoso, Karen Adelman, and Karla M. Neugebauer. Co-transcriptional splicing regulates 3’ end cleavage during mammalian erythropoiesis. _Molecular Cell_ , 81(5):998–1012.e7, March

172

2021. ISSN 10972765. doi: 10.1016/j.molcel.2020.12.018. URL `https: //linkinghub.elsevier.com/retrieve/pii/S1097276520309370` .

- [236] H. Risken. _The Fokker-Planck equation: methods of solution and applications_ . Number v. 18 in Springer series in synergetics. Springer-Verlag, New York, 2nd ed edition, 1996. ISBN 978-3-540-61530-9.

- [237] G. W. Roberts. _Chemical reactions and chemical reactors_ . John Wiley & Sons, Hoboken, NJ, 2008. ISBN 978-0-471-74220-3. OCLC: ocn176897332.

- [238] Mark D. Robinson, Davis J. McCarthy, and Gordon K. Smyth. edgeR: a Bioconductor package for differential expression analysis of digital gene expression data. _Bioinformatics_ , 26(1):139–140, January 2010. ISSN 13674811, 1367-4803. doi: 10.1093/bioinformatics/btp616. URL `https:// academic.oup.com/bioinformatics/article/26/1/139/182458` .

- [239] Joseph Rodriguez and Daniel R. Larson. Transcription in Living Cells: Molecular Mechanisms of Bursting. _Annual Review of Biochemistry_ , 89 (1):189–212, June 2020. ISSN 0066-4154, 1545-4509. doi: 10.1146/ annurev-biochem-011520-105250. URL `https://www.annualreviews. org/doi/10.1146/annurev-biochem-011520-105250` .

- [240] Laura Rubió Ferrarons. _Insights into the CREB-regulated transcription coactivators (CRTCs) in neurons and astrocytes_ . PhD Dissertation, Universitat Autònoma de Barcelona, October 2020. URL `https://ddd.uab.cat/ record/241504` .

- [241] Piergiacomo Sabino and Nicola Cufaro Petroni. Gamma-related Ornstein–Uhlenbeck processes and their simulation. _Journal of Statistical Computation and Simulation_ , 91(6):1108–1133, April 2021. ISSN 0094-9655, 1563-5163. doi: 10.1080/00949655.2020.1842408. URL `https://www. tandfonline.com/doi/full/10.1080/00949655.2020.1842408` .

- [242] Wouter Saelens, Robrecht Cannoodt, Helena Todorov, and Yvan Saeys. A comparison of single-cell trajectory inference methods. _Nature Biotechnology_ , 37(5):547–554, May 2019. ISSN 1087-0156, 1546-1696. doi: 10.1038/s41587-019-0071-9. URL `http://www.nature.com/articles/ s41587-019-0071-9` .

- [243] T. A. Samad. DRAGON: A Member of the Repulsive Guidance MoleculeRelated Family of Neuronal- and Muscle-Expressed Membrane Proteins Is Regulated by DRG11 and Has Neuronal Adhesive Properties. _Journal of Neuroscience_ , 24(8):2027–2036, February 2004. ISSN 0270-6474, 15292401. doi: 10.1523/JNEUROSCI.4115-03.2004. URL `https://www. jneurosci.org/lookup/doi/10.1523/JNEUROSCI.4115-03.2004` .

- [244] A. Sanchez and I. Golding. Genetic Determinants and Cellular Constraints in Noisy Gene Expression. _Science_ , 342(6163):1188–1193, December 2013.

173

ISSN 0036-8075, 1095-9203. doi: 10.1126/science.1242975. URL `http: //www.sciencemag.org/cgi/doi/10.1126/science.1242975` .

- [245] Sara Sanders, Kunaal Joshi, Petra Levin, and Srividya Iyer-Biswas. Single cells tell their own story: An updated framework for understanding stochastic variations in cell cycle progression in bacteria. Preprint, bioRxiv: 2022.03.15.484524, March 2022. URL `http://biorxiv.org/content/ early/2022/03/16/2022.03.15.484524.abstract` .

- [246] Mahakaran Sandhu, Matthew A. Spence, and Colin J. Jackson. Evo-velocity: Protein language modeling accelerates the study of evolution. _Cell Systems_ , 13(4):271–273, April 2022. ISSN 24054712. doi: 10.1016/j.cels. 2022.03.004. URL `https://linkinghub.elsevier.com/retrieve/ pii/S2405471222001314` .

- [247] Abhishek K Sarkar and Matthew Stephens. Separating measurement and expression models clarifies confusion in single cell RNA-seq analysis. Preprint, bioRxiv: 2020.04.07.030007, April 2020. URL `http://biorxiv.org/ lookup/doi/10.1101/2020.04.07.030007` .

- [248] Wim Schoutens. _Lévy Processes in Finance_ . Wiley Series in Probability and Statistics. John Wiley & Sons, Ltd, Chichester, UK, March 2003. ISBN 978-0-470-85156-2 978-0-470-87023-5. doi: 10.1002/0470870230. URL `http://doi.wiley.com/10.1002/0470870230` .

- [249] Daniel Schwabe, Sara Formichetti, Jan Philipp Junker, Martin Falcke, and Nikolaus Rajewsky. The transcriptome dynamics of single cells during the cell cycle. _Molecular Systems Biology_ , 16(11), November 2020. ISSN 1744-4292, 1744-4292. doi: 10.15252/msb.20209946. URL `https:// onlinelibrary.wiley.com/doi/10.15252/msb.20209946` .

- [250] Hannah J. Scott, Martin J. Stebbing, Claire E. Walters, Samuel McLenachan, Mark I. Ransome, Nancy R. Nichols, and Ann M. Turnley. Differential effects of SOCS2 on neuronal differentiation and morphology. _Brain Research_ , 1067(1):138–145, January 2006. ISSN 00068993. doi: 10.1016/j.brainres.2005.10.032. URL `https://linkinghub.elsevier. com/retrieve/pii/S0006899305014587` .

- [251] Adrien Senecal, Brian Munsky, Florence Proux, Nathalie Ly, Floriane E. Braye, Christophe Zimmer, Florian Mueller, and Xavier Darzacq. Transcription Factors Modulate c-Fos Transcriptional Bursts. _Cell Reports_ , 8(1):75–83, July 2014. ISSN 22111247. doi: 10.1016/j.celrep.2014.05.053. URL `https: //linkinghub.elsevier.com/retrieve/pii/S2211124714004471` .

- [252] Sheel Shah, Yodai Takei, Wen Zhou, Eric Lubeck, Jina Yun, Chee-Huat Linus Eng, Noushin Koulena, Christopher Cronin, Christoph Karp, Eric J. Liaw, Mina Amin, and Long Cai. Dynamics and Spatial Genomics of the Nascent Transcriptome by Intron seqFISH. _Cell_ , 174(2):363–376.e16, July

174

2018. ISSN 00928674. doi: 10.1016/j.cell.2018.05.035. URL `https: //linkinghub.elsevier.com/retrieve/pii/S0092867418306470` .

- [253] V. Shahrezaei and P. S. Swain. Analytical distributions for stochastic gene expression. _Proceedings of the National Academy of Sciences_ , 105 (45):17256–17261, November 2008. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas.0803850105. URL `http://www.pnas.org/cgi/doi/10. 1073/pnas.0803850105` .

- [254] Vahid Shahrezaei, Julien F Ollivier, and Peter S Swain. Colored extrinsic fluctuations and stochastic gene expression. _Molecular Systems Biology_ , 4(1):196, January 2008. ISSN 1744-4292, 1744-4292. doi: 10.1038/msb.2008.31. URL `https://onlinelibrary.wiley.com/doi/ 10.1038/msb.2008.31` .

- [255] L. V. Sharova, A. A. Sharov, T. Nedorezov, Y. Piao, N. Shaik, and M. S.H. Ko. Database for mRNA Half-Life of 19 977 Genes Obtained by DNA Microarray Analysis of Pluripotent and Differentiating Mouse Embryonic Stem Cells. _DNA Research_ , 16(1):45–58, January 2009. ISSN 1340-2838, 1756-1663. doi: 10.1093/dnares/dsn030. URL `https://academic.oup. com/dnaresearch/article-lookup/doi/10.1093/dnares/dsn030` .

- [256] Caibin Sheng, Rui Lopes, Gang Li, Sven Schuierer, Annick Waldt, Rachel Cuttat, Slavica Dimitrieva, Audrey Kauffmann, Eric Durand, Giorgio G. Galli, Guglielmo Roma, and Antoine de Weck. Probabilistic machine learning ensures accurate ambient denoising in droplet-based single-cell omics. Preprint, bioRxiv: 2022.01.14.476312, January 2022. URL `http://biorxiv.org/lookup/doi/10.1101/2022.01.14.476312` .

- [257] Changhong Shi, Yiguo Jiang, and Tianshou Zhou. Queuing Models of Gene Expression: Analytical Distributions and Beyond. _Biophysical Journal_ , 119(8):1606–1616, October 2020. ISSN 0006-3495. doi: 10.1016/j.bpj. 2020.09.001. URL `https://www.ncbi.nlm.nih.gov/pmc/articles/ PMC7642270/` .

- [258] Ki Shuk Shim, Margit Rosner, Angelika Freilinger, Gert Lubec, and Markus Hengstschläger. Bach2 is involved in neuronal differentiation of N1E-115 neuroblastoma cells. _Experimental Cell Research_ , 312(12):2264–2278, July 2006. ISSN 00144827. doi: 10.1016/j.yexcr.2006.03.018. URL `https: //linkinghub.elsevier.com/retrieve/pii/S0014482706001194` .

- [259] Jonathon Shlens. A Tutorial on Principal Component Analysis. Preprint, arXiv: 1404.1100, April 2014. URL `http://arxiv.org/abs/1404.1100` .

- [260] Daniel Silk, Paul D. W. Kirk, Chris P. Barnes, Tina Toni, and Michael P. H. Stumpf. Model Selection in Systems Biology Depends on Experimental Design. _PLoS Computational Biology_ , 10(6):e1003650, June 2014. ISSN

175

1553-7358. doi: 10.1371/journal.pcbi.1003650. URL `https://dx.plos. org/10.1371/journal.pcbi.1003650` .

- [261] Abhyudai Singh and Pavol Bokes. Consequences of mRNA Transport on Stochastic Variability in Protein Levels. _Biophysical Journal_ , 103 (5):1087–1096, September 2012. ISSN 00063495. doi: 10.1016/j.bpj. 2012.07.015. URL `https://linkinghub.elsevier.com/retrieve/ pii/S0006349512007904` .

- [262] Samuel O Skinner, Heng Xu, Sonal Nagarkar-Jaiswal, Pablo R Freire, Thomas P Zwaka, and Ido Golding. Single-cell analysis of transcription kinetics across the cell cycle. _eLife_ , 5:e12175, January 2016. ISSN 2050084X. doi: 10.7554/eLife.12175. URL `https://elifesciences.org/ articles/12175` .

- [263] Ruslan Soldatov, Marketa Kaucka, Maria Eleni Kastriti, Julian Petersen, Tatiana Chontorotzea, Lukas Englmaier, Natalia Akkuratova, Yunshi Yang, Martin Häring, Viacheslav Dyachuk, Christoph Bock, Matthias Farlik, Michael L. Piacentino, Franck Boismoreau, Markus M. Hilscher, Chika Yokota, Xiaoyan Qian, Mats Nilsson, Marianne E. Bronner, Laura Croci, Wen-Yu Hsiao, David A. Guertin, Jean-Francois Brunet, Gian Giacomo Consalez, Patrik Ernfors, Kaj Fried, Peter V. Kharchenko, and Igor Adameyko. Spatiotemporal structure of cell fate decisions in murine neural crest. _Science_ , 364(6444):eaas9536, June 2019. ISSN 0036-8075, 1095-9203. doi: 10.1126/science.aas9536. URL `http://www.sciencemag.org/lookup/ doi/10.1126/science.aas9536` .

- [264] Charlotte Soneson, Avi Srivastava, Rob Patro, and Michael B. Stadler. Preprocessing choices affect RNA velocity results for droplet scRNA-seq data. _PLOS Computational Biology_ , 17(1):e1008585, January 2021. ISSN 15537358. doi: 10.1371/journal.pcbi.1008585. URL `https://dx.plos.org/ 10.1371/journal.pcbi.1008585` .

- [265] J. Michael Steele. _Stochastic calculus and financial applications_ . Number 45 in Applications of mathematics. Springer, New York, 2001. ISBN 978-0387-95016-7.

- [266] Stephen M. Stigler. _The History of Statistics: The Measurement of Uncertainty before 1900_ . Belknap Press, March 1990. URL `https://www.hup. harvard.edu/catalog.php?isbn=9780674403413` .

- [267] Adam R. Stinchcombe, Charles S. Peskin, and Daniel Tranchina. Population density approach for discrete mRNA distributions in generalized switching models for stochastic gene expression. _Physical Review E_ , 85(6):061919, June 2012. ISSN 1539-3755, 1550-2376. doi: 10.1103/PhysRevE.85.061919. URL `https://link.aps.org/doi/10.1103/PhysRevE.85.061919` .

176

- [268] Marlon Stoeckius, Christoph Hafemeister, William Stephenson, Brian HouckLoomis, Pratip K Chattopadhyay, Harold Swerdlow, Rahul Satĳa, and Peter Smibert. Simultaneous epitope and transcriptome measurement in single cells. _Nature Methods_ , 14(9):865–868, September 2017. ISSN 1548-7091, 1548-7105. doi: 10.1038/nmeth.4380. URL `http://www.nature.com/ articles/nmeth.4380` .

- [269] Michael P.H. Stumpf. Inferring better gene regulation networks from singlecell data. _Current Opinion in Systems Biology_ , 27:100342, September 2021. ISSN 24523100. doi: 10.1016/j.coisb.2021.05.003. URL `https: //linkinghub.elsevier.com/retrieve/pii/S2452310021000275` .

- [270] Patrick S. Stumpf, Rosanna C.G. Smith, Michael Lenz, Andreas Schuppert, Franz-Josef Müller, Ann Babtie, Thalia E. Chan, Michael P.H. Stumpf, Colin P. Please, Sam D. Howison, Fumio Arai, and Ben D. MacArthur. Stem Cell Differentiation as a Non-Markov Stochastic Process. _Cell Systems_ , 5(3):268–282.e7, September 2017. ISSN 24054712. doi: 10.1016/j.cels.2017.08.009. URL `https://linkinghub.elsevier.com/ retrieve/pii/S2405471217303423` .

- [271] Augustinas Sukys, Kaan Öcal, and Ramon Grima. Approximating solutions of the Chemical Master equation using neural networks. _iScience_ , 25(9): 105010, August 2022. ISSN 2589-0042. doi: 10.1016/j.isci.2022.105010. URL `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9474291/` .

- [272] Xi-Ming Sun, Anthony Bowman, Miles Priestman, Francois Bertaux, Amalia Martinez-Segura, Wenhao Tang, Chad Whilding, Dirk Dormann, Vahid Shahrezaei, and Samuel Marguerat. Size-Dependent Increase in RNA Polymerase II Initiation Rates Mediates Gene Expression Scaling with Cell Size. _Current Biology_ , 30(7):1217–1230.e7, April 2020. ISSN 09609822. doi: 10.1016/j.cub.2020.01.053. URL `https://linkinghub.elsevier.com/ retrieve/pii/S096098222030097X` .

- [273] Makoto Suzuki, Yusuke Hara, Chiyo Takagi, Takamasa S. Yamamoto, and Naoto Ueno. _MID1_ and _MID2_ are required for _Xenopus_ neural tube closure through the regulation of microtubule organization. _Development_ , 138(2):385–385, January 2011. ISSN 1477-9129, 0950-1991. doi: 10.1242/dev.062976. URL `https://journals.biologists.com/dev/article/138/2/385/ 44835/MID1-and-MID2-are-required-for-Xenopus-neural-tube` .

- [274] Valentine Svensson. Droplet scRNA-seq is not zero-inflated. _Nature Biotechnology_ , 38(2):147–150, February 2020. ISSN 1087-0156, 15461696. doi: 10.1038/s41587-019-0379-5. URL `https://www.nature. com/articles/s41587-019-0379-5` .

- [275] Valentine Svensson and Lior Pachter. RNA Velocity: Molecular Kinetics from Single-Cell RNA-Seq. _Molecular Cell_ , 72(1):7–9, October

177

2018. ISSN 10972765. doi: 10.1016/j.molcel.2018.09.026. URL `https: //linkinghub.elsevier.com/retrieve/pii/S1097276518307974` .

- [276] Valentine Svensson, Adam Gayoso, Nir Yosef, and Lior Pachter. Interpretable factor models of single-cell RNA-seq via variational autoencoders. _Bioinformatics_ , 36(11):3418–3421, June 2020. ISSN 1367-4803, 1460-2059. doi: 10.1093/bioinformatics/btaa169. URL `https://academic.oup.com/ bioinformatics/article/36/11/3418/5807606` .

- [277] P. S. Swain, M. B. Elowitz, and E. D. Siggia. Intrinsic and extrinsic contributions to stochasticity in gene expression. _Proceedings of the National Academy of Sciences_ , 99(20):12795–12800, October 2002. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas.162041399. URL `http://www.pnas.org/ cgi/doi/10.1073/pnas.162041399` .

- [278] Wenhao Tang, François Bertaux, Philipp Thomas, Claire Stefanelli, Malika Saint, Samuel Marguerat, and Vahid Shahrezaei. bayNorm: Bayesian gene expression recovery, imputation and normalization for singlecell RNA-sequencing data. _Bioinformatics_ , 36(4):1174–1181, February 2020. ISSN 1367-4803, 1367-4811. doi: 10.1093/bioinformatics/btz726. URL `https://academic.oup.com/bioinformatics/article/36/4/ 1174/5581401` .

- [279] Wenhao Tang, Andreas Christ Sølvsten Jørgensen, Samuel Marguerat, Philipp Thomas, and Vahid Shahrezaei. Modelling capture efficiency of single cell RNA-sequencing data improves inference of transcriptome-wide burst kinetics. Preprint, bioRxiv: 2023.03.06.531327, March 2023. URL `http://biorxiv.org/lookup/doi/10.1101/2023.03.06.531327` .

- [280] Michael E. Taylor. _Partial differential equations_ . Number v. 115<116> in Applied mathematical sciences. Springer, New York, 2nd ed edition, 2011. ISBN 978-1-4419-7054-1 978-1-4419-7055-8 978-1-44197051-0 978-1-4419-7052-7 978-1-4419-7048-0 978-1-4419-7049-7. OCLC: ocn681675116.

- [281] Martina Tedesco, Francesca Giannese, Dejan Lazarević, Valentina Giansanti, Dalia Rosano, Silvia Monzani, Irene Catalano, Elena Grassi, Eugenia R. Zanella, Oronza A. Botrugno, Leonardo Morelli, Paola Panina Bordignon, Giulio Caravagna, Andrea Bertotti, Gianvito Martino, Luca Aldrighetti, Sebastiano Pasqualato, Livio Trusolino, Davide Cittaro, and Giovanni Tonon. Chromatin Velocity reveals epigenetic dynamics by single-cell profiling of heterochromatin and euchromatin. _Nature Biotechnology_ , October 2021. ISSN 1087-0156, 1546-1696. doi: 10.1038/s41587-021-01031-1. URL `https://www.nature.com/articles/s41587-021-01031-1` .

- [282] Philipp Thomas. Making sense of snapshot data: ergodic principle for clonal cell populations. _Journal of The Royal Society Interface_ , 14

178

(136):20170467, November 2017. ISSN 1742-5689, 1742-5662. doi: 10.1098/rsif.2017.0467. URL `https://royalsocietypublishing.org/ doi/10.1098/rsif.2017.0467` .

- [283] Philipp Thomas and Vahid Shahrezaei. Coordination of gene expression noise with cell size: analytical results for agent-based models of growing cell populations. _Journal of The Royal Society Interface_ , 18(178):20210274, May 2021. ISSN 1742-5662. doi: 10.1098/rsif.2021.0274. URL `https: //royalsocietypublishing.org/doi/10.1098/rsif.2021.0274` .

- [284] Surangrat Thongkorn, Songphon Kanlayaprasit, Pawinee Panjabud, Thanit Saeliw, Thanawin Jantheang, Kasidit Kasitipradit, Suthathip Sarobol, Depicha Jindatip, Valerie W. Hu, Tewin Tencomnao, Takako Kikkawa, Tatsuya Sato, Noriko Osumi, and Tewarit Sarachana. Sex differences in the effects of prenatal bisphenol A exposure on autism-related genes and their relationships with the hippocampus functions. _Scientific Reports_ , 11(1):1241, December 2021. ISSN 2045-2322. doi: 10.1038/s41598-020-80390-2. URL `http://www.nature.com/articles/s41598-020-80390-2` .

- [285] B. C. Thorne, A. M. Bailey, and S. M. Peirce. Combining experiments with multi-cell agent-based modeling to study biological tissue patterning. _Briefings in Bioinformatics_ , 8(4):245–257, March 2007. ISSN 1467-5463, 1477-4054. doi: 10.1093/bib/bbm024. URL `https://academic.oup. com/bib/article-lookup/doi/10.1093/bib/bbm024` .

- [286] Nicola Thrupp, Carlo Sala Frigerio, Leen Wolfs, Nathan G. Skene, Nicola Fattorelli, Suresh Poovathingal, Yannick Fourne, Paul M. Matthews, Tom Theys, Renzo Mancuso, Bart de Strooper, and Mark Fiers. Single-Nucleus RNA-Seq Is Not Suitable for Detection of Microglial Activation Genes in Humans. _Cell Reports_ , 32(13):108189, September 2020. ISSN 22111247. doi: 10.1016/j.celrep.2020.108189. URL `https://linkinghub.elsevier. com/retrieve/pii/S2211124720311785` .

- [287] Luyi Tian, Jafar S. Jabbari, Rachel Thĳssen, Quentin Gouil, Shanika L. Amarasinghe, Oliver Voogd, Hasaru Kariyawasam, Mei R. M. Du, Jakob Schuster, Changqing Wang, Shian Su, Xueyi Dong, Charity W. Law, Alexis Lucattini, Yair David Joseph Prawer, Coralina Collar-Fernández, Jin D. Chung, Timur Naim, Audrey Chan, Chi Hai Ly, Gordon S. Lynch, James G. Ryall, Casey J. A. Anttila, Hongke Peng, Mary Ann Anderson, Christoffer Flensburg, Ian Majewski, Andrew W. Roberts, David C. S. Huang, Michael B. Clark, and Matthew E. Ritchie. Comprehensive characterization of single-cell full-length isoforms in human and mouse with long-read sequencing. _Genome Biology_ , 22(1):310, December 2021. ISSN 1474-760X. doi: 10.1186/s13059-021-02525-6. URL `https://genomebiology. biomedcentral.com/articles/10.1186/s13059-021-02525-6` .

179

- [288] F. Tissir, I. Bar, A.M. Goffinet, and C. Lambert De Rouvroit. Expression of the ankyrin repeat domain 6 gene (Ankrd6) during mouse brain development. _Developmental Dynamics_ , 224(4):465–469, August 2002. ISSN 1058-8388, 1097-0177. doi: 10.1002/dvdy.10126. URL `https://onlinelibrary. wiley.com/doi/10.1002/dvdy.10126` .

- [289] Nestor V. Torres and Guido Santos. The (Mathematical) Modeling Process in Biosciences. _Frontiers in Genetics_ , 6:354, December 2015. ISSN 16648021. doi: 10.3389/fgene.2015.00354. URL `https://www.ncbi.nlm. nih.gov/pmc/articles/PMC4686688/` .

- [290] F. William Townes, Stephanie C. Hicks, Martin J. Aryee, and Rafael A. Irizarry. Feature selection and dimension reduction for single-cell RNASeq based on a multinomial model. _Genome Biology_ , 20(1):295, December 2019. ISSN 1474-760X. doi: 10.1186/s13059-019-18616. URL `https://genomebiology.biomedcentral.com/articles/10. 1186/s13059-019-1861-6` .

- [291] Sophie Tritschler, Maren Büttner, David S. Fischer, Marius Lange, Volker Bergen, Heiko Lickert, and Fabian J. Theis. Concepts and limitations for learning developmental trajectories from single cell genomics. _Development_ , 146(12):dev170506, June 2019. ISSN 0950-1991, 1477-9129. doi: 10.1242/dev.170506. URL `http://dev.biologists.org/lookup/doi/ 10.1242/dev.170506` .

- [292] S. T. Tse and Justin W. L. Wan. Low-bias simulation scheme for the Heston model by Inverse Gaussian approximation. _Quantitative Finance_ , 13(6): 919–937, June 2013. ISSN 1469-7688, 1469-7696. doi: 10.1080/14697688. 2012.696678. URL `http://www.tandfonline.com/doi/abs/10.1080/ 14697688.2012.696678` .

- [293] Edward Tunnacliffe and Jonathan R. Chubb. What Is a Transcriptional Burst? _Trends in Genetics_ , 36(4):288–297, April 2020. ISSN 01689525. doi: 10.1016/j.tig.2020.01.003. URL `https://linkinghub.elsevier.com/ retrieve/pii/S0168952520300056` .

- [294] M. Ullah and O. Wolkenhauer. Family tree of Markov models in systems biology. _IET Systems Biology_ , 1(4):247–254, July 2007. ISSN 1751-8849, 17518857. doi: 10.1049/iet-syb:20070017. URL `https://digital-library. theiet.org/content/journals/10.1049/iet-syb_20070017` .

- [295] Mukhtar Ullah and Olaf Wolkenhauer. _Stochastic approaches for systems biology_ . Springer, New York, 2011. ISBN 978-1-4614-0477-4 978-1-46140478-1. OCLC: ocn733239594.

- [296] T. K. Ulland and M. Colonna. Trem2 - a key player in microglial biology and alzheimer disease. _Nature Reviews Neurology_ , 14:667–675, 2018. doi: 10.

180

1038/s41582-018-0072-1. URL `https://www.nature.com/articles/ s41582-018-0072-1` .

- [297] N. G. Van Kampen. _Stochastic Processes in Physics and Chemistry_ . Elsevier, third edition, 2007. ISBN 978-0-444-52965-7.

- [298] Erik van Nimwegen. Inferring intrinsic and extrinsic noise from a dual fluorescent reporter. Preprint, bioRxiv: 049486, April 2016. URL `http: //biorxiv.org/lookup/doi/10.1101/049486` .

- [299] John J Vastola. _In search of a coherent theoretical framework for stochastic gene regulation_ . PhD thesis, Vanderbilt, March 2021. URL `https://ir. vanderbilt.edu/handle/1803/16646` .

- [300] John J. Vastola. Solving the chemical master equation for monomolecular reaction systems and beyond: a Doi-Peliti path integral view. _Journal of Mathematical Biology_ , 83(5):48, November 2021. ISSN 0303-6812, 1432-1416. doi: 10.1007/s00285-021-01670-7. URL `https://link.springer.com/ 10.1007/s00285-021-01670-7` .

- [301] Frits Veerman, Carsten Marr, and Nikola Popović. Time-dependent propagators for stochastic models of gene expression: an analytical method. _Journal of Mathematical Biology_ , 77(2):261–312, August 2018. ISSN 0303-6812, 1432-1416. doi: 10.1007/s00285-017-1196-4. URL `http: //link.springer.com/10.1007/s00285-017-1196-4` .

- [302] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, C J Carey, Ilhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, SciPy 1.0 Contributors, Aditya Vĳaykumar, Alessandro Pietro Bardelli, Alex Rothberg, Andreas Hilboll, Andreas Kloeckner, Anthony Scopatz, Antony Lee, Ariel Rokem, C. Nathan Woods, Chad Fulton, Charles Masson, Christian Häggström, Clark Fitzgerald, David A. Nicholson, David R. Hagen, Dmitrii V. Pasechnik, Emanuele Olivetti, Eric Martin, Eric Wieser, Fabrice Silva, Felix Lenders, Florian Wilhelm, G. Young, Gavin A. Price, Gert-Ludwig Ingold, Gregory E. Allen, Gregory R. Lee, Hervé Audren, Irvin Probst, Jörg P. Dietrich, Jacob Silterra, James T Webber, Janko Slavič, Joel Nothman, Johannes Buchner, Johannes Kulick, Johannes L. Schönberger, José Vinícius de Miranda Cardoso, Joscha Reimer, Joseph Harrington, Juan Luis Cano Rodríguez, Juan Nunez-Iglesias, Justin Kuczynski, Kevin Tritz, Martin Thoma, Matthew Newville, Matthias Kümmerer, Maximilian Bolingbroke, Michael

181

Tartre, Mikhail Pak, Nathaniel J. Smith, Nikolai Nowaczyk, Nikolay Shebanov, Oleksandr Pavlyk, Per A. Brodtkorb, Perry Lee, Robert T. McGibbon, Roman Feldbauer, Sam Lewis, Sam Tygier, Scott Sievert, Sebastiano Vigna, Stefan Peterson, Surhud More, Tadeusz Pudlik, Takuya Oshima, Thomas J. Pingel, Thomas P. Robitaille, Thomas Spura, Thouis R. Jones, Tim Cera, Tim Leslie, Tiziano Zito, Tom Krauss, Utkarsh Upadhyay, Yaroslav O. Halchenko, and Yoshiki Vázquez-Baeza. SciPy 1.0: fundamental algorithms for scientific computing in Python. _Nature Methods_ , 17(3):261–272, March 2020. ISSN 1548-7091, 1548-7105. doi: 10.1038/s41592-019-0686-2. URL `http://www.nature.com/articles/s41592-019-0686-2` .

- [303] Sean T. Vittadello and Michael P.H. Stumpf. Open problems in mathematical biology. _Mathematical Biosciences_ , 354:108926, December 2022. ISSN 00255564. doi: 10.1016/j.mbs.2022.108926. URL `https://linkinghub. elsevier.com/retrieve/pii/S0025556422001158` .

- [304] Huy D. Vo and Roger B. Sidje. An adaptive solution to the chemical master equation using tensors. _The Journal of Chemical Physics_ , 147(4):044102, July 2017. ISSN 0021-9606, 1089-7690. doi: 10.1063/1.4994917. URL `http://aip.scitation.org/doi/10.1063/1.4994917` .

- [305] Margaritis Voliotis, Philipp Thomas, Ramon Grima, and Clive G. Bowsher. Stochastic Simulation of Biomolecular Networks in Dynamic Environments. _PLOS Computational Biology_ , 12(6):e1004923, June 2016. ISSN 15537358. doi: 10.1371/journal.pcbi.1004923. URL `https://dx.plos.org/ 10.1371/journal.pcbi.1004923` .

- [306] Johann Wolfgang von Goethe. _Faust_ . The World Publishing Company, Cleveland, Ohio, 1870.

- [307] Yihan Wan, Dimitrios G. Anastasakis, Joseph Rodriguez, Murali Palangat, Prabhakar Gudla, George Zaki, Mayank Tandon, Gianluca Pegoraro, Carson C. Chow, Markus Hafner, and Daniel R. Larson. Dynamic imaging of nascent RNA reveals general principles of transcription dynamics and stochastic splice site selection. _Cell_ , 184(11):2878–2895.e20, May 2021. ISSN 00928674. doi: 10.1016/j.cell.2021.04.012. URL `https: //linkinghub.elsevier.com/retrieve/pii/S0092867421004918` .

- [308] Jingshu Wang, Mo Huang, Eduardo Torre, Hannah Dueck, Sydney Shaffer, John Murray, Arjun Raj, Mingyao Li, and Nancy R. Zhang. Gene expression distribution deconvolution in single-cell RNA sequencing. _Proceedings of the National Academy of Sciences_ , 115(28):E6437–E6446, July 2018. ISSN 0027-8424, 1091-6490. doi: 10.1073/pnas.1721085115. URL `http://www. pnas.org/lookup/doi/10.1073/pnas.1721085115` .

- [309] Mengyu Wang, Jing Zhang, Heng Xu, and Ido Golding. Measuring transcription at a single gene copy reveals hidden drivers of bacterial individuality.

182

_Nature Microbiology_ , 4:2118–2127, September 2019. ISSN 2058-5276. doi: 10.1038/s41564-019-0553-z. URL `http://www.nature.com/articles/ s41564-019-0553-z` .

- [310] Shangying Wang and Simone Bianco. AI-assisted Biology: Predict the Conditional Probability Distributions from Noisy Measurements. Preprint, bioRxiv: 2021.10.07.463577, October 2021. URL `http://biorxiv.org/ lookup/doi/10.1101/2021.10.07.463577` .

- [311] Xin Wang. Velo-Predictor: an ensemble learning pipeline for RNA velocity prediction. _BMC Bioinformatics_ , page 12, 2021.

- [312] Sumio Watanabe. _Algebraic Geometry and Statistical Learning Theory_ . Number 25 in Cambridge Monographs on Applied and Computational Mathematics. Cambridge University Press, 2009. ISBN 978-0-511-65153-3.

- [313] Philipp Weiler. Protein Velocity in Single Cells using Multi-Omics Modelling. Master’s thesis, EPFL, TU Munich, January 2021.

- [314] Guangzheng Weng, Junil Kim, and Kyoung Jae Won. VeTra: a tool for trajectory inference based on RNA velocity. _Bioinformatics_ , page btab364, May 2021. doi: 10.1093/bioinformatics/btab364.

- [315] Darren James Wilkinson. _Stochastic modelling for systems biology_ . Chapman & Hall/CRC mathematical and computational biology. CRC Press, Taylor & Francis Group, Boca Raton, third edition edition, 2019. ISBN 978-1-13854928-9.

- [316] Barbara Wold and Richard M Myers. Sequence census methods for functional genomics. _Nature Methods_ , 5(1):19–21, January 2008. ISSN 1548-7105. doi: 10.1038/nmeth1157. URL `https://doi.org/10.1038/nmeth1157` .

- [317] Haiqing Xiong, Yingjie Luo, Yanzhu Yue, Jiejie Zhang, Shanshan Ai, Xin Li, Xuelian Wang, Yun-Long Zhang, Yusheng Wei, Hui-Hua Li, Xinli Hu, Cheng Li, and Aibin He. Single-Cell Transcriptomics Reveals ChemotaxisMediated Intraorgan Crosstalk During Cardiogenesis. _Circulation Research_ , 125(4):398–410, August 2019. ISSN 0009-7330, 1524-4571. doi: 10.1161/CIRCRESAHA.119.315243. URL `https://www.ahajournals. org/doi/10.1161/CIRCRESAHA.119.315243` .

- [318] Heng Xu, Leonardo A Sepúlveda, Lauren Figard, Anna Marie Sokac, and Ido Golding. Combining protein and mRNA quantification to decipher transcriptional regulation. _Nature Methods_ , 12(8):739–742, August 2015. ISSN 1548-7091, 1548-7105. doi: 10.1038/nmeth.3446. URL `http://www.nature.com/articles/nmeth.3446` .

- [319] Heng Xu, Samuel O. Skinner, Anna Marie Sokac, and Ido Golding. Stochastic Kinetics of Nascent RNA. _Physical Review Letters_ , 117(12):128101,

183

2016. ISSN 0031-9007, 1079-7114. doi: 10.1103/PhysRevLett.117. 128101. URL `https://journals.aps.org/prl/abstract/10.1103/ PhysRevLett.117.128101` .

- [320] Yunan Yang, Levon Nurbekyan, Elisa Negrini, Robert Martin, and Mirjeta Pasha. Optimal Transport for Parameter Identification of Chaotic Dynamics via Invariant Measures. Preprint, arXiv: 2104.15138, May 2021. URL `http://arxiv.org/abs/2104.15138` .

- [321] Zizhen Yao, Hanqing Liu, Fangming Xie, Stephan Fischer, Ricky S. Adkins, Andrew I. Aldridge, Seth A. Ament, Anna Bartlett, M. Margarita Behrens, Koen Van den Berge, Darren Bertagnolli, Hector Roux de Bézieux, Tommaso Biancalani, A. Sina Booeshaghi, Héctor Corrada Bravo, Tamara Casper, Carlo Colantuoni, Jonathan Crabtree, Heather Creasy, Kirsten Crichton, Megan Crow, Nick Dee, Elizabeth L. Dougherty, Wayne I. Doyle, Sandrine Dudoit, Rongxin Fang, Victor Felix, Olivia Fong, Michelle Giglio, Jeff Goldy, Mike Hawrylycz, Brian R. Herb, Ronna Hertzano, Xiaomeng Hou, Qiwen Hu, Jayaram Kancherla, Matthew Kroll, Kanan Lathia, Yang Eric Li, Jacinta D. Lucero, Chongyuan Luo, Anup Mahurkar, Delissa McMillen, Naeem M. Nadaf, Joseph R. Nery, Thuc Nghi Nguyen, Sheng-Yong Niu, Vasilis Ntranos, Joshua Orvis, Julia K. Osteen, Thanh Pham, Antonio PintoDuarte, Olivier Poirion, Sebastian Preissl, Elizabeth Purdom, Christine Rimorin, Davide Risso, Angeline C. Rivkin, Kimberly Smith, Kelly Street, Josef Sulc, Valentine Svensson, Michael Tieu, Amy Torkelson, Herman Tung, Eeshit Dhaval Vaishnav, Charles R. Vanderburg, Cindy van Velthoven, Xinxin Wang, Owen R. White, Z. Josh Huang, Peter V. Kharchenko, Lior Pachter, John Ngai, Aviv Regev, Bosiljka Tasic, Joshua D. Welch, Jesse Gillis, Evan Z. Macosko, Bing Ren, Joseph R. Ecker, Hongkui Zeng, and Eran A. Mukamel. A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. _Nature_ , 598(7879):103–110, October 2021. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586-021-03500-8. URL `https://www.nature.com/articles/s41586-021-03500-8` .

- [322] Yuan Yin, Masanao Yajima, and Joshua D. Campbell. Characterization and decontamination of background noise in droplet-based single-cell protein expression data with DecontPro. Preprint, bioRxiv: 2023.01.27.525964v2, February 2023. URL `https://www.ncbi.nlm.nih.gov/pmc/articles/ PMC9979990/` .

- [323] Matthew D Young and Sam Behjati. SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data. _GigaScience_ , 9 (12):giaa151, December 2020. ISSN 2047-217X. doi: 10.1093/gigascience/ giaa151. URL `https://academic.oup.com/gigascience/article/ doi/10.1093/gigascience/giaa151/6049831` .

- [324] Leqian Yu, Yulei Wei, Jialei Duan, Daniel A. Schmitz, Masahiro Sakurai, Lei Wang, Kunhua Wang, Shuhua Zhao, Gary C. Hon, and Jun Wu.

184

Blastocyst-like structures generated from human pluripotent stem cells. _Nature_ , 591(7851):620–626, March 2021. ISSN 0028-0836, 1476-4687. doi: 10.1038/s41586-021-03356-y. URL `https://www.nature.com/ articles/s41586-021-03356-y` .

- [325] Christoph Zechner and Heinz Koeppl. Uncoupled Analysis of Stochastic Reaction Networks in Fluctuating Environments. _PLoS Computational Biology_ , 10(12):e1003942, December 2014. ISSN 1553-7358. doi: 10.1371/journal.pcbi.1003942. URL `https://dx.plos.org/10.1371/ journal.pcbi.1003942` .

- [326] A. Zeisel, W. J. Kostler, N. Molotski, J. M. Tsai, R. Krauthgamer, J. JacobHirsch, G. Rechavi, Y. Soen, S. Jung, Y. Yarden, and E. Domany. Coupled pre-mRNA and mRNA dynamics unveil operational strategies underlying transcriptional responses to stimuli. _Molecular Systems Biology_ , 7(1):529– 529, September 2011. ISSN 1744-4292. doi: 10.1038/msb.2011.62. URL `http://msb.embopress.org/cgi/doi/10.1038/msb.2011.62` .

- [327] Daniel Zenklusen, Daniel R Larson, and Robert H Singer. Single-RNA counting reveals alternative modes of gene expression in yeast. _Nature Structural & Molecular Biology_ , 15(12):1263–1271, 2008. ISSN 1545-9993, 1545-9985. doi: 10.1038/nsmb.1514.

- [328] Martin Jinye Zhang, Vasilis Ntranos, and David Tse. Determining sequencing depth in a single-cell RNA-seq experiment. _Nature Communications_ , 11(1): 774, February 2020. ISSN 2041-1723. doi: 10.1038/s41467-020-14482-y. URL `https://www.nature.com/articles/s41467-020-14482-y` .

- [329] Stephen Zhang, Anton Afanassiev, Laura Greenstreet, Tetsuya Matsumoto, and Geoffrey Schiebinger. Optimal transport analysis reveals trajectories in steady-state systems. _PLOS Computational Biology_ , 17(12):e1009466, December 2021. ISSN 1553-7358. doi: 10.1371/journal.pcbi.1009466. URL `https://dx.plos.org/10.1371/journal.pcbi.1009466` .

- [330] Ziqi Zhang and Xiuwei Zhang. Inference of high-resolution trajectories in single cell RNA-Seq data from RNA velocity. Preprint, bioRxiv: 2020.09.30.321125, October 2020. URL `http://biorxiv.org/lookup/ doi/10.1101/2020.09.30.321125` .

- [331] Ziqi Zhang and Xiuwei Zhang. VeloSim: Simulating single cell geneexpression and RNA velocity. Preprint, bioRxiv: 2021.01.11.426277, January 2021. URL `http://biorxiv.org/lookup/doi/10.1101/2021. 01.11.426277` .

- [332] Grace X. Y. Zheng, Jessica M. Terry, Phillip Belgrader, Paul Ryvkin, Zachary W. Bent, Ryan Wilson, Solongo B. Ziraldo, Tobias D. Wheeler, Geoff P. McDermott, Junjie Zhu, Mark T. Gregory, Joe Shuga, Luz Montesclaros, Jason G. Underwood, Donald A. Masquelier, Stefanie Y.

185

Nishimura, Michael Schnall-Levin, Paul W. Wyatt, Christopher M. Hindson, Rajiv Bharadwaj, Alexander Wong, Kevin D. Ness, Lan W. Beppu, H. Joachim Deeg, Christopher McFarland, Keith R. Loeb, William J. Valente, Nolan G. Ericson, Emily A. Stevens, Jerald P. Radich, Tarjei S. Mikkelsen, Benjamin J. Hindson, and Jason H. Bielas. Massively parallel digital transcriptional profiling of single cells. _Nature Communications_ , 8 (1):14049, April 2017. ISSN 2041-1723. doi: 10.1038/ncomms14049. URL `http://www.nature.com/articles/ncomms14049` .

- [333] Shĳie C. Zheng, Genevieve Stein-O’Brien, Leandros Boukas, Loyal A Goff, and Kasper D Hansen. Pumping the brakes on RNA velocity – understanding and interpreting RNA velocity estimates. Preprint, bioRxiv: 2022.06.19.494717, June 2022. URL `http://biorxiv.org/lookup/ doi/10.1101/2022.06.19.494717` .

- [334] Tianshou Zhou and Jiajun Zhang. Analytical Results for a Multistate Gene Model. _SIAM Journal on Applied Mathematics_ , 72(3):789–818, January 2012. ISSN 0036-1399, 1095-712X. doi: 10.1137/110852887. URL `http: //epubs.siam.org/doi/10.1137/110852887` .

- [335] Liucun Zhu, Ying Zhang, Wen Zhang, Sihai Yang, Jian-Qun Chen, and Dacheng Tian. Patterns of exon-intron architecture variation of genes in eukaryotic genomes. _BMC Genomics_ , 10(1):47, December 2009. ISSN 1471-2164. doi: 10.1186/1471-2164-10-47. URL `https://bmcgenomics. biomedcentral.com/articles/10.1186/1471-2164-10-47` .

- [336] Péter Érdi and Gábor Lente. _Stochastic chemical kinetics: theory and (mostly) systems biological applications_ . Springer Complexity. Springer, New York, 2014. ISBN 978-1-4939-0386-3.

186

_A p p e n d i x A_

---

[← MODELING FURTHER CLASSES OF MULTIOMIC DATA](18-modeling-further-classes-of-multiomic-data.md) · [Up: contents](index.md) · [SUPPLEMENTARY GENERATING FUNCTION DERIVATIONS →](20-supplementary-generating-function-derivations.md)
