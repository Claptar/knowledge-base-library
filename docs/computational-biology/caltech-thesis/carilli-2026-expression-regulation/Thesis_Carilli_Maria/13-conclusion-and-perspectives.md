---
title: CONCLUSION AND PERSPECTIVES
source: https://thesis.library.caltech.edu/18729/
source_file: sources/carilli-2026-expression-regulation/Thesis_Carilli_Maria.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# CONCLUSION AND PERSPECTIVES

**Source:** `Thesis_Carilli_Maria.pdf` from [carilli-2026-expression-regulation](https://thesis.library.caltech.edu/18729/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_[We were] to be redeemed by the gift of arranging words / but must be prepared for an earth without grammar._

CZESŁAW MIŁOSZ

We live in an exciting time for biology, a time of revolutions in data collection (a multitude of ‘omics) and computational advancements.

### **A brief summary**

In Chapter I, we reviewed the journey from horticulture [1] to the sequencing of the human genome [8] and the explosions of ensuing studies [29, 18, 234, 235, 31, 10] in humankind’s ambitious drive to understand how life works. We showed in Chapter II that mathematics published over a hundred years ago still has something fresh to teach us about high-dimensional data analysis [236, 50, 51]. In Chapter III, we described some fairly simple stochastic models of transcriptional processes, and how they can be powerful tools for biological discovery when fit to scRNA-seq data [99, 37]. In Chapter IV, we presented methods for approximating solutions to these models when they become slightly more complicated [46], and in Chapter V included these approximations in a variational autoencoder framework for scalable inference of biophysical rates in single cells [47]. In Chapter VI, we used RNAseq data from homozygous crosses to establish the presence or absence of distal and proximal gene regulatory differences. In Chapter VII, we demonstrated that the two lines of work are compatible and, having fit tens of thousands of genes for transcriptional parameters, interrogated the differences in regulation of these processes between founder mouse strains at tissue and cell type resolution.

### **A brief look ahead**

Given the expanding number of molecular modalities assayed in single cells (including proteins [237]; chromatin accessibility [139, 165] and modifications [238])

105

and perturbations to these cells [239, 240], it is exciting to think ahead towards what we can learn about cellular processes and their genetic basis by analyzing such data from the biophysical perspective taken in this work. While inroads have been made for some analytical solutions [241, 242], as the complexity of proposed interactions (for example, gene networks) and the number of modalities grows, combining models and machine learning approximations trained on data from fast stochastic simulation algorithms [243] could be a fruitful way forward.

Complementary to the efforts of building predictive foundation models for molecular components of the cell, and combining them to build multi-scale and multi-model AI "virtual cells" [244], will always be efforts to use all available modeling tools and computational resources to understand what is happening in the "irl" cells still being assayed.

### **A brief experiential comment**

A model is a representation of thought, forcing us to precisely define ideas and measure them against experimental data. Whether it is describing stochastic transcription, tracing RNA over the course of its lifecycle, or setting up a design matrix for modeling allelic expression from homozygous crosses, encoding hypotheses within mathematical frameworks formalizes our conception of biological processes. It further allows us to interrogate these assumptions, tweaking models that do not describe observations well, and conduct new experiments to test updated modes of thought. In the experience of my Ph.D., it did not take models with millions of parameters to make me question assumptions I had about a fundamental regulatory process, but a simple GLM with three or four learned weights and non-trivial implications. This is not to say that the complexity of biology can be contained in what we decide to write down or draw out about it; but the model is for the scientist, not for biology, and it is an interesting future challenge to maintain what modeling does for our thought processes while, with the advantages of deep learning, freeing them from the constraints of our limited hypotheses to expand their scope.

106

BIBLIOGRAPHY

- [1] Gregor Mendel. “Versuche über Pflanzen-Hybriden”. In: _Verhandlungen des naturforschenden Vereines in Brünn_ 4 (1866), pp. 3–47.

- [2] FriedrichMiescher. “UeberdiechemischeZusammensetzungderEiterzellen”. In: _Medicinisch-Chemische Untersuchungen_ 4 (1871). Published in HoppeSeyler’s Medicinisch-chemische Untersuchungen, pp. 441–460.

- [3] Oswald T Avery, Colin M MacLeod, and Maclyn McCarty. “Studies on the chemical nature of the substance inducing transformation of pneumococcal types: Induction of transformation by a desoxyribonucleic acid fraction isolated from Pneumococcus Type III”. In: _Journal of Experimental Medicine_ 79.2 (1944), pp. 137–158.

- [4] Francis Crick. “Central dogma of molecular biology”. In: _Nature_ 227.5258 (1970), pp. 561–563.

- [5] Walter Fiers, Roland Contreras, Fred Duerinck, Guy Haegeman, Dirk Iserentant, Jozef Merregaert, Willy Min Jou, Francis Molemans, Alex Raeymaekers, Alfons Van den Berghe, Guido Volckaert, and Marc Ysebaert. “Complete nucleotide sequence of bacteriophage MS2 RNA: primary and secondary structure of the replicase gene”. In: _Nature_ 260.5551 (1976). PMID: 1264203, pp. 500–507. doi: `10.1038/260500a0` . url: `https: //doi.org/10.1038/260500a0` .

- [6] F. Sanger, G. M. Air, B. G. Barrell, N. L. Brown, A. R. Coulson, J. C. Fiddes, C. A. Hutchison, P. M. Slocombe, and M. Smith. “Nucleotide sequence of bacteriophage _𝜙_ X174 DNA”. In: _Nature_ 265 (1977), pp. 687–695. doi: `10.1038/265687a0` . url: `https://www.nature.com/articles/ 265687a0` .

- [7] The C. elegans Sequencing Consortium. “Genome Sequence of the Nematode C. elegans: A Platform for Investigating Biology”. In: _Science_ 282.5396 (1998), pp. 2012–2018. doi: `10.1126/science.282.5396.2012` . url: `https://www.science.org/doi/10.1126/science.282.5396. 2012` .

- [8] International Human Genome Sequencing Consortium. “Initial sequencing and analysis of the human genome”. In: _Nature_ 409.6822 (2001), pp. 860– 921. doi: `10.1038/35057062` . url: `https://doi.org/10.1038/ 35057062` .

- [9] Sergey Nurk, Sergey Koren, Arang Rhie, Mikko Rautiainen, Andrey V. Bzikadze, et al. “The complete sequence of a human genome”. In: _Science_ 376.6588 (2022), pp. 44–53. doi: `10.1126/science.abj6987` .

107

- [10] Wen-Wei Liao, Mazloomi Asri, Jana Ebler, et al. “A draft human pangenome reference”. In: _Nature_ 617 (2023), pp. 312–324. doi: `10.1038/s41586023-05896-x` .

- [11] TheInternationalHapMapConsortium. “TheInternationalHapMapProject”. In: _Nature_ 426 (2003), pp. 789–796. doi: `10.1038/nature02168` .

- [12] The International HapMap Consortium. “A second generation human haplotype map of over 3.1 million SNPs”. In: _Nature_ 449 (2007), pp. 851–861. doi: `10.1038/nature06258` .

- [13] Richard J. Klein, Caroline Zeiss, Emily Y. Chew, Jean Y. Tsai, Richard S. Sackler, Carol Haynes, Anna K. Henning, John P. SanGiovanni, Shrikant M. Mane, Scott T. Mayne, et al. “Complement factor H polymorphism in agerelated macular degeneration”. In: _Science_ 308.5720 (2005), pp. 385–389. doi: `10.1126/science.1109557` .

- [14] The 1000 Genomes Project Consortium. “A global reference for human genetic variation”. In: _Nature_ 526 (2015), pp. 68–74. doi: `10 . 1038 / nature15393` .

- [15] Majid Nikpay et al. “A comprehensive 1,000 Genomes-based genome-wide association meta-analysis of coronary artery disease”. In: _Nature Genetics_ 47 (2015), pp. 1121–1130. doi: `10.1038/ng.3396` .

- [16] Gabriel E. Hoffman, Jaroslav Bendl, Georgios Voloudakis, Kelsey S. Montgomery, Laura Sloofman, Ying-Chih Wang, Hardik R. Shah, Mads E. Hauberg, Jessica S. Johnson, Kiran Girdhar, Lingyun Song, John F. Fullard, Robin Kramer, Chang-Gyu Hahn, Raquel Gur, Stefano Marenco, Barbara K. Lipska, David A. Lewis, Vahram Haroutunian, Scott Hemby, Patrick Sullivan, Schahram Akbarian, Andrew Chess, Joseph D. Buxbaum, Greg E. Crawford, Enrico Domenici, Bernie Devlin, Solveig K. Sieberts, Mette A. Peters, and Panos Roussos. “CommonMind Consortium provides transcriptomic and epigenomic data for schizophrenia and bipolar disorder”. In: _Scientific Data_ 6 (2019), p. 180. doi: `10.1038/sdata.2018.180` .

- [17] Andrew D. Grotzinger, Josefin Werme, Wouter J. Peyrot, Oleksandr Frei, Christiaan de Leeuw, Lucy K. Bicks, Qiuyu Guo, Michael P. Margolis, Brandon J. Coombes, Anthony Batzler, Vanessa Pazdernik, Joanna M. Biernacka, Ole A. Andreassen, Verneri Anttila, Anders D. Børglum, Gerome Breen, Na Cai, Ditte Demontis, Howard J. Edenberg, Stephen V. Faraone, Barbara Franke, Michael J. Gandal, Joel Gelernter, Alexander S. Hatoum, John M. Hettema, Emma C. Johnson, Katherine G. Jonas, James A. Knowles, Karestan C. Koenen, Adam X. Maihofer, Travis T. Mallard, Manuel Mattheisen, Karen S. Mitchell, Benjamin M. Neale, Caroline M. Nievergelt, John I. Nurnberger, Kevin S. O’Connell, Roseann E. Peterson, Elise B. Robinson, Sandra S. Sanchez-Roige, Susan L. Santangelo, Jeremiah M. Scharf, Hreinn Stefansson, Kari Stefansson, Murray B. Stein, Nora I. Strom, Laura M. Thornton, Elliot M. Tucker-Drob, Brad Verhulst, Irwin D.

108

Waldman, G. Bragi Walters, Naomi R. Wray, Dongmei Yu, Phil H. Lee, Kenneth S. Kendler, Jordan W. Smoller, et al. “Mapping the genetic landscape across 14 psychiatric disorders”. In: _Nature_ 649 (2026), pp. 406–415.

- [18] Amit Sud, Ben Kinnersley, and Richard S. Houlston. “Genome-wide association studies of cancer: current insights and future perspectives”. In: _Nature Reviews Cancer_ 17 (2017), pp. 692–704. doi: `10.1038/nrc.2017.82` .

- [19] Loïc Yengo, Sailaja Vedantam, Eirini Marouli, Julia Sidorenko, Eric Bartell, Saori Sakaue, Mariaelisa Graff, Anna U. Eliasen, Yuning Jiang, Shailaja Raghavan, et al. “A saturated map of common genetic variants associated with human height from 5.4 million individuals of diverse ancestries”. In: _Nature_ 610 (2022), pp. 704–712. doi: `10.1038/s41586-022-05275-y` .

- [20] Mengzhen Liu, Yuning Jiang, Robbee Wedow, Yue Li, David M. Brazel, Fang Chen, Gaurav Datta, Juan Davila-Velderrain, David McGuire, Chen Tian, et al. “Association studies of up to 1.2 million individuals yield new insights into the genetic etiology of tobacco and alcohol use”. In: _Nature Genetics_ 51 (2019), pp. 237–244. doi: `10.1038/s41588-018-0307-5` .

- [21] The ENCODE Project Consortium, Jill E. Moore, Michael J. Purcaro, Henry E. Pratt, Charles B. Epstein, Noam Shoresh, Jessika Adrian, Trupti Kawli, Carrie A. Davis, Alexander Dobin, Rajinder Kaul, et al. “Expanded encyclopaedias of DNA elements in the human and mouse genomes”. In: _Nature_ 583 (2020), pp. 699–710. doi: `10.1038/s41586-020-2493-4` .

- [22] Mark Schena, Darryl Shalon, Ronald W. Davis, and Patrick O. Brown. “Quantitative monitoring of gene expression patterns with a complementary DNA microarray”. In: _Science_ 270.5235 (Oct. 1995), pp. 467–470.

- [23] Ali Mortazavi, Brian A. Williams, Kenneth McCue, Lorian Schaeffer, and Barbara Wold. “Mapping and quantifying mammalian transcriptomes by RNA-Seq”. In: _Nature Methods_ 5.7 (July 2008), pp. 621–628. doi: `10. 1038/nmeth.1226` .

- [24] Gioele La Manno, Ruslan Soldatov, Amit Zeisel, Emelie Braun, Hannah Hochgerner, Viktor Petukhov, Katja Lidschreiber, Maria E. Kastriti, Peter Lönnerberg, Alessandro Furlan, Jean Fan, Lars E. Borm, Zehua Liu, David van Bruggen, Jimin Guo, Xiaoling He, Roger Barker, Erik Sundström, Gonçalo Castelo-Branco, Patrick Cramer, Igor Adameyko, Sten Linnarsson, and Peter V. Kharchenko. “RNA velocity of single cells”. In: _Nature_ 560 (2018), pp. 494–498. doi: `10.1038/s41586-018-0414-6` .

- [25] Delaney K. Sullivan, Kristján Eldjárn Hjörleifsson, Nikhila P. Swarna, Conrad Oakes, Guillaume Holley, Páll Melsted, and Lior Pachter. “Accurate quantification of nascent and mature RNAs from single-cell and singlenucleus RNA-seq”. In: _Nucleic Acids Research_ 53.1 (2025), gkae1137. doi: `10.1093/nar/gkae1137` .

109

- [26] Allon M. Klein, Linas Mazutis, Ilke Akartuna, Naren Tallapragada, Adrian Veres, Victor Li, Leonid Peshkin, David A. Weitz, and Marc W. Kirschner. “Droplet Barcoding for Single-Cell Transcriptomics Applied to Embryonic Stem Cells”. In: _Cell_ 161.5 (May 2015), pp. 1187–1201. doi: `10.1016/j. cell.2015.04.044` .

- [27] Evan Z. Macosko, Anindita Basu, Rahul Satija, James Nemesh, Karthik Shekhar, Melissa Goldman, Itay Tirosh, Allison R. Bialas, Nolan Kamitaki, Emily M. Martersteck, John J. Trombetta, David A. Weitz, Joshua R. Sanes, Alex K. Shalek, Aviv Regev, and Steven A. McCarroll. “Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets”. In: _Cell_ 161.5 (May 2015), pp. 1202–1214. doi: `10.1016/j. cell.2015.05.002` .

- [28] Jennifer E. Rood, Samantha Wynne, Lucia Robson, Anna Hupalowska, John Randell, Sarah A. Teichmann, and Aviv Regev. “The Human Cell Atlas from a cell census to a unified foundation model”. In: _Nature_ 637 (2025), pp. 1065–1071. doi: `10.1038/s41586-024-08392-9` .

- [29] The GTEx Consortium. “The GTEx Consortium atlas of genetic regulatory effects across human tissues”. In: _Science_ 369.6509 (2020), pp. 1318–1330. doi: `10.1126/science.aaz1776` .

- [30] Seyhan Yazar, Jose Alquicira-Hernandez, Kristof Wing, Anne Senabouth, M. Grace Gordon, Stacey Andersen, Qinyi Lu, Antonia Rowson, Thomas R. P. Taylor, Linda Clarke, Katia Maccora, Christine Chen, Anthony L. Cook, Chun Jimmie Ye, Kirsten A. Fairfax, Alex W. Hewitt, and Joseph E. Powell. “Single-cell eQTL mapping identifies cell type–specific genetic control of autoimmune disease”. In: _Science_ 376.6589 (2022). doi: `10. 1126/science.abf3041` .

- [31] The All of Us Research Program Genomics Investigators. “Genomic data in the All of Us Research Program”. In: _Nature_ 627 (2024), pp. 340–346. doi: `10.1038/s41586-023-06957-x` .

- [32] Rebecca L. Walker, Gokul Ramaswami, Christopher Hartl, Nicholas Mancuso, Michael J. Gandal, Luis de la Torre-Ubieta, Bogdan Pasaniuc, Jason L. Stein, and Daniel H. Geschwind. “Genetic Control of Expression and Splicing in Developing Human Brain Informs Disease Mechanisms”. In: _Cell_ 179.3 (Oct. 2019), 750–771.e22. doi: `10.1016/j.cell.2019.09.021` .

- [33] Arjun Raj, Charles S Peskin, Daniel Tranchina, Diana Y Vargas, and Sanjay Tyagi. “Stochastic mRNA Synthesis in Mammalian Cells”. en. In: _PLoS Biology_ 4.10 (Sept. 2006). Ed. by Ueli Schibler, e309. issn: 1545-7885. doi: `10.1371/journal.pbio.0040309` . url: `https://dx.plos.org/ 10.1371/journal.pbio.0040309` (visited on 08/07/2019).

110

- [34] Ido Golding, Johan Paulsson, Scott M. Zawilski, and Edward C. Cox. “RealTime Kinetics of Gene Activity in Individual Bacteria”. en. In: _Cell_ 123.6 (Dec. 2005), pp. 1025–1036. issn: 00928674. doi: `10.1016/j.cell. 2005.09.031` . url: `https://linkinghub.elsevier.com/retrieve/ pii/S0092867405010378` (visited on 08/23/2019).

- [35] R. D. Dar, B. S. Razooky, A. Singh, T. V. Trimeloni, J. M. McCollum, C. D. Cox, M. L. Simpson, and L. S. Weinberger. “Transcriptional burst frequency and burst size are equally modulated across the human genome”. en. In: _Proceedings of the National Academy of Sciences_ 109.43 (Oct. 2012), pp. 17454–17459. issn: 0027-8424, 1091-6490. doi: `10. 1073/ pnas . 1213530109` . url: `http://www.pnas.org/cgi/doi/10.1073/pnas. 1213530109` (visited on 09/03/2019).

- [36] Gennady Gorin, John J. Vastola, and Lior Pachter. “Studying stochastic systems biology of the cell with single-cell genomics data”. en. In: _Cell Systems_ 14 (Sept. 2023), pp. 1–22. issn: 24054712. doi: `10.1016/j. cels.2023.08.004` . url: `https://linkinghub.elsevier.com/ retrieve/pii/S2405471223002442` (visited on 10/03/2023).

- [37] Gennady Gorin, Tara Chari, Maria Carilli, John J. Vastola, and Lior Pachter. “Monod: model-based discovery and integration through fitting stochastic transcriptional dynamics to single-cell sequencing data”. In: _Nature Methods_ 22 (Nov. 7, 2025), pp. 2286–2300. doi: `10.1038/s41592-025-02832-x` . url: `https://doi.org/10.1038/s41592-025-02832-x` .

- [38] Tara Chari, Gennady Gorin, and Lior Pachter. _Biophysically Interpretable Inference of Cell Types from Multimodal Sequencing Data_ . en. Preprint. bioRxiv: 2023.09.17.558131, Sept. 2023. url: `http://biorxiv.org/ lookup/doi/10.1101/2023.09.17.558131` (visited on 09/22/2023).

- [39] Tara Chari and Lior Pachter. “The Specious Art of Single-Cell Genomics”. en. In: _PLOS Computational Biology_ 19.8 (Aug. 2023), e1011288. doi: `10.1371/journal.pcbi.1011288` . url: `https://journals.plos. org/ploscompbiol/article?id=10.1371/journal.pcbi.1011288` (visited on 11/25/2023).

- [40] Rory Stark, Marta Grzelak, and James Hadfield. “RNA sequencing: the teenage years”. In: _Nature Reviews Genetics_ 20 (2019), pp. 631–656. doi: `10.1038/s41576-019-0150-2` .

- [41] Anna S. E. Cuomo, Giulio Alvari, Caren B. Azodi, et al. “Optimizing expression quantitative trait locus mapping workflows for single-cell studies”. In: _Genome Biology_ 22 (2021), p. 188. doi: `10.1186/s13059-021-02407-x` .

- [42] Leo Breiman. “Statistical Modeling: The Two Cultures”. In: _Statistical Science_ 16.3 (2001), pp. 199–231. doi: `10.1214/ss/1009213726` .

111

- [43] Abhyudai Singh and Pavol Bokes. “Consequences of mRNA Transport on Stochastic Variability in Protein Levels”. en. In: _Biophysical Journal_ 103.5 (Sept. 2012), pp. 1087–1096. issn: 00063495. doi: `10.1016/j.bpj. 2012.07.015` . url: `https://linkinghub.elsevier.com/retrieve/ pii/S0006349512007904` (visited on 08/12/2019).

- [44] Maria Carilli, Kayla Jackson, and Lior Pachter. _The Rayleigh Quotient and Contrastive Principal Component Analysis I_ . Nov. 19, 2025. doi: `10.1101/ 2025.11.19.689125` . bioRxiv: `2025.11.19.689125` . url: `https: //doi.org/10.1101/2025.11.19.689125` .

- [45] Maria Carilli, Kayla Jackson, and Lior Pachter. _The Rayleigh Quotient and Contrastive Principal Component Analysis II_ . Apr. 8, 2026. doi: `10.64898/ 2026.04.08.717236` . bioRxiv: `2026.04.08.717236` . url: `https: //doi.org/10.64898/2026.04.08.717236` .

- [46] Maria Carilli, Gennady Gorin, Tara Chari, and Lior Pachter. “Spectral neural approximations for models of transcriptional dynamics”. English. In: _Biophysical Journal_ (May 2024). Publisher: Elsevier. issn: 0006-3495. doi: `10. 1016/j.bpj.2024.04.034` . url: `https://www.cell.com/biophysj/ abstract/S0006-3495(24)00314-X` (visited on 06/26/2024).

- [47] Maria Carilli, Gennady Gorin, Yongin Choi, Tara Chari, and Lior Pachter. “Biophysical modeling with variational autoencoders for bimodal, singlecell RNA sequencing data”. In: _Nature Methods_ 21.8 (2024), pp. 1466– 1469.

- [48] Ingileif B. Hallgrímsdóttir, Maria Carilli, and Lior Pachter. _Estimating cis and trans contributions to differences in gene regulation_ . Feb. 18, 2026. doi: `10.1101/2024.07.13.603403` . bioRxiv: `2024.07.13.603403` . url: `https://doi.org/10.1101/2024.07.13.603403` .

- [49] Qiqing Fu, Chenyu Dong, Yunhe Liu, Xiaoqiong Xia, Gang Liu, Fan Zhong, and Lei Liu. “A comparison of scRNA-seq annotation methods based on experimentally labeled immune cell subtype dataset”. In: _Briefings in Bioinformatics_ 25.5 (Sept. 2024), bbae392. doi: `10.1093/bib/bbae392` .

- [50] Karl Pearson. “LIII. On lines and planes of closest fit to systems of points in space”. In: _The London, Edinburgh, and Dublin philosophical magazine and journal of science_ 2.11 (1901), pp. 559–572.

- [51] Harold Hotelling. “Analysis of a complex of statistical variables into principal components.” In: _Journal of educational psychology_ 24.6 (1933), p. 417.

- [52] Abubakar Abid, Vivek Zhang, Vibhor Bagaria, and James Zou. “Contrastive principal component analysis”. In: _Advances in Neural Information Processing Systems_ 31 (2018).

- [53] Philippe Boileau, Nima S Hejazi, and Sandrine Dudoit. “Exploring highdimensional biological data with sparse contrastive principal component analysis”. In: _Bioinformatics_ 36.11 (2020), pp. 3422–3430.

112

- [54] Didong Li, Andrew Jones, and Barbara Engelhardt. “Probabilistic contrastive dimension reduction for case-control study data”. In: _The Annals of Applied Statistics_ 18.3 (2024), pp. 2207–2229.

- [55] Roger A. Horn and Charles R. Johnson. _Matrix Analysis_ . 2nd. Cambridge, UK: Cambridge University Press, 2012. isbn: 978-0-521-54823-6.

- [56] Ronald A. Fisher. “The use of multiple measurements in taxonomic problems”. In: _Annals of Eugenics_ 7.2 (1936), pp. 179–188.

- [57] Sebastian Mika, Gunnar Rätsch, Jason Weston, Bernhard Schölkopf, and Klaus-Robert Müller. “Fisher discriminant analysis with kernels”. In: _Neural Networks for Signal Processing IX_ . IEEE. 1999, pp. 41–48.

- [58] Elisabeth Rebboah, Ryan Weber, Elnaz Abdollahzadeh, Nikhila Swarna, Delaney K Sullivan, Diane Trout, Fairlie Reese, Heidi Yahan Liang, Ghassan Filimban, Parvin Mahdipoor, et al. “Systematic cell-type resolved transcriptomes of 8 tissues in 8 lab and wild-derived mouse strains captures global and local expression variation”. In: _bioRxiv_ (2025), pp. 2025–04.

- [59] Lingyun Xiong, Jing Liu, Seung Yub Han, Kari Koppitch, Jin-Jin Guo, Megan Rommelfanger, Zhen Miao, Fan Gao, Ingileif B. Hallgrímsdóttir, Lior Pachter, Junhyong Kim, Adam L. MacLean, and Andrew P. McMahon. “Direct androgen receptor control of sexually dimorphic gene expression in the mammalian kidney”. In: _Developmental Cell_ 58.21 (2023), 2338– 2358.e5. doi: `10.1016/j.devcel.2023.08.010` .

- [60] Andrew Ransick, Nils O. Lindström, Jing Liu, Qin Zhu, Jin-Jin Guo, Gregory F. Alvarado, Albert D. Kim, Hannah G. Black, Junhyong Kim, and Andrew P. McMahon. “Single-Cell Profiling Reveals Sex, Lineage, and Regional Diversity in the Mouse Kidney”. In: _Developmental Cell_ 51.3 (2019), 399–413.e7. doi: `10.1016/j.devcel.2019.10.005` .

- [61] Hirofumi Watanabe, Robert L. Paxton, Matthew R. Tolerico, Vidya K. Nagalakshmi, Shinji Tanaka, Mark D. Okusa, Shin Goto, Ichiei Narita, Seiji Watanabe, Maria Luisa S. Sequeira-López, and R. Ariel Gomez. “Expression of Acsm2, a kidney-specific gene, parallels the function and maturation of proximal tubular cells”. In: _American Journal of Physiology–Renal Physiology_ 319.4 (2020), F569–F580. doi: `10.1152/ajprenal.00348.2020` .

- [62] Siqi Chen, Ruiyang Liu, Chia-Kuei Mo, et al. “Multi-omic and spatial analysis of mouse kidneys highlights sex-specific differences in gene regulation across the lifespan”. In: _Nature Genetics_ 57 (2025), pp. 1213–1227. doi: `10.1038/s41588-025-02161-x` .

- [63] Ming-Zhi Zhang, Kensuke Sasaki, Yan Li, Zhilian Li, Yu Pan, Guan-Nan Jin, Yinqiu Wang, Aolei Niu, Suwan Wang, Xiaofeng Fan, Jian Chun Chen, Corina Borza, Haichun Yang, Ambra Pozzi, Agnes B. Fogo, and Raymond C. Harris. “The Role of the EGF Receptor in Sex Differences in Kidney

113

Injury”. In: _Journal of the American Society of Nephrology_ 30.11 (2019), pp. 2015–2033. doi: `10.1681/ASN.2018121244` .

- [64] Hannah Dueck, James Eberwine, and Junhyong Kim. “Variation is function: are single cell differences functionally important? Testing the hypothesis that single cell variation is required for aggregate function”. In: _Bioessays_ 38.2 (2016), pp. 172–180.

- [65] Zoltan J Koles, Michael S Lazar, and Steven Z Zhou. “Spatial patterns underlying population differences in the background EEG”. In: _Brain topography_ 2.4 (1990), pp. 275–284.

- [66] Michael X Cohen. “A tutorial on generalized eigendecomposition for denoising, contrast enhancement, and dimension reduction in multichannel electrophysiology”. In: _Neuroimage_ 247 (2022), p. 118809.

- [67] Fabien Lotte and Cuntai Guan. “Regularizing common spatial patterns to improve BCI designs: unified theory and new algorithms”. In: _IEEE Transactions on biomedical Engineering_ 58.2 (2010), pp. 355–362.

- [68] Trevor Hastie and Robert Tibshirani. “Discriminant analysis by Gaussian mixtures”. In: _Journal of the Royal Statistical Society Series B: Statistical Methodology_ 58.1 (1996), pp. 155–176.

- [69] Sergey Ioffe. “Probabilistic linear discriminant analysis”. In: _European Conference on Computer Vision_ . Springer. 2006, pp. 531–542.

- [70] Kristen A Severson, Soumya Ghosh, and Kenney Ng. “Unsupervised learning with contrastive latent variable models”. In: _Proceedings of the AAAI Conference on Artificial Intelligence_ . Vol. 33. 2019, pp. 4862–4869.

- [71] Michael E Tipping and Christopher M Bishop. “Probabilistic principal component analysis”. In: _Journal of the Royal Statistical Society Series B: Statistical Methodology_ 61.3 (1999), pp. 611–622.

- [72] Sam Roweis. “EM algorithms for PCA and SPCA”. In: _Advances in neural information processing systems_ 10 (1997).

- [73] James O. Ramsay and Bernard W. Silverman. _Applied Functional Data Analysis: Methods and Case Studies_ . New York: Springer, 2002.

- [74] James O Ramsay and Bernard W Silverman. _Functional data analysis_ . Springer, 2005.

- [75] Jane-Ling Wang, Jeng-Min Chiou, and Hans-Georg Müller. “Functional Data Analysis”. In: _Annual Review of Statistics and Its Application_ 3 (2016), pp. 257–295. doi: `10.1146/annurev-statistics-041715-033624` .

- [76] Fang Yao, Hans-Georg Müller, and Jane-Ling Wang. “Functional data analysis for sparse longitudinal data”. In: _Journal of the American statistical association_ 100.470 (2005), pp. 577–590.

114

- [77] Gareth M. James, Trevor J. Hastie, and Catherine A. Sugar. “Principal component models for sparse functional data”. In: _Biometrika_ 87.3 (Sept. 2000), pp. 587–602. doi: `10.1093/biomet/87.3.587` .

- [78] Ci-Ren Jiang and Jane-Ling Wang. “Covariate adjusted functional principal components analysis for longitudinal data”. In: _The Annals of Statistics_ 38.2 (Apr. 2010), pp. 1194–1226. doi: `10.1214/09-AOS742` .

- [79] Eric Zhang and Didong Li. “Contrastive Functional Principal Component Analysis”. In: _Proceedings of the AAAI Conference on Artificial Intelligence_ . Vol. 39. 2025, pp. 22380–22388.

- [80] Carl Edward Rasmussen and Christopher K. I. Williams. _Gaussian Processes for Machine Learning_ . Adaptive Computation and Machine Learning. The MIT Press, 2005. isbn: 9780262256834. doi: `10.7551/mitpress/ 3206.001.0001` .

- [81] Darawan Rinchai, Sara Deola, Gabriele Zoppoli, Basirudeen Syed Ahamed Kabeer, Sara Taleb, Igor Pavlovski, Selma Maacha, Giusy Gentilcore, Mohammed Toufiq, Lisa Mathew, Li Liu, Fazulur Rehaman Vempalli, Ghada Mubarak, Stephan Lorenz, Irene Sivieri, Gabriella Cirmena, Chiara Dentone, Paola Cuccarolo, Daniele Roberto Giacobbe, Federico Baldi, Alberto Garbarino, Benedetta Cigolini, Paolo Cremonesi, Michele Bedognetti, Alberto Ballestrero, Matteo Bassetti, Boris P. Hejblum, Tracy Augustine, Nicholas Van Panhuys, Rodolphe Thiebaut, Ricardo Branco, Tracey Chew, Maryam Shojaei, Kirsty Short, Carl G. Feng, PREDICT-19 Consortium, Susu M. Zughaier, Andrea De Maria, Benjamin Tang, Ali Ait Hssain, Davide Bedognetti, Jean-Charles Grivel, and Damien Chaussabel. “High–temporal resolution profiling reveals distinct immune trajectories following the first and second doses of COVID-19 mRNA vaccines”. In: _Science Advances_ 8.45 (2022). doi: `10.1126/sciadv.abp9961` .

- [82] Prabhu S. Arunachalam, Madeleine K. D. Scott, Thomas Hagan, Chunfeng Li, Yupeng Feng, Florian Wimmers, Lilit Grigoryan, Meera Trisal, Venkata Viswanadh Edara, Lilin Lai, Sarah Esther Chang, Allan Feng, Shaurya Dhingra, Mihir Shah, Alexandra S. Lee, Sharon Chinthrajah, Sayantani B. Sindher, Vamsee Mallajosyula, Fei Gao, Natalia Sigal, Sangeeta Kowli, Sheena Gupta, Kathryn Pellegrini, Gregory Tharp, Sofia Maysel-Auslender, Sydney Hamilton, Hadj Aoued, Kevin Hrusovsky, Mark Roskey, Steven E. Bosinger, Holden T. Maecker, Scott D. Boyd, Mark M. Davis, Paul J. Utz, Mehul S. Suthar, Purvesh Khatri, Kari C. Nadeau, and Bali Pulendran. “Systems vaccinology of the BNT162b2 mRNA vaccine in humans”. In: _Nature_ 596 (2021), pp. 410–416. doi: `10.1038/s41586-021-03791-x` .

- [83] Matthew C. Altman, Darawan Rinchai, Nicole Baldwin, Mohammed Toufiq, Elizabeth Whalen, Mathieu Garand, Basirudeen Syed Ahamed Kabeer, Mohamed Alfaki, Scott R. Presnell, Prasong Khaenam, Aaron Ayllón-Benítez, Fleur Mougin, Patricia Thébault, Laurent Chiche, Noemie Jourde-Chiche,

115

J. Theodore Phillips, Goran Klintmalm, Anne O’Garra, Matthew Berry, Chloe Bloom, Robert J. Wilkinson, Christine M. Graham, Marc Lipman, Ganjana Lertmemongkolchai, and Damien Chaussabel. “Development of a fixed module repertoire for the analysis and interpretation of blood transcriptome data”. In: _Nature Communications_ 12 (2021), p. 4385. doi: `10. 1038/s41467-021-24719-2` .

- [84] Dejan Mesner, Ann-Kathrin Reuschl, Matthew V. X. Whelan, Taylor Bronzovich, Tafhima Haider, Lucy G. Thorne, Roberta Ragazzini, Paola Bonfanti, Greg J. Towers, and Clare Jolly. “SARS-CoV-2 evolution influences GBP and IFITM sensitivity”. In: _Proceedings of the National Academy of Sciences of the United States of America_ 120.5 (2023), e2212577120. doi: `10.1073/pnas.2212577120` .

- [85] Y. Furutani, M. Toguchi, S. Higuchi, K. Yanaka, L. Gailhouste, X. Y. Qin, et al. “Establishment of a rapid detection system for ISG20-dependent SARS-CoV-2 subreplicon RNA degradation induced by interferon-alpha”. In: _International Journal of Molecular Sciences_ 22 (2021), p. 11641. doi: `10.3390/ijms222111641` .

- [86] Rashid Mir, Mohammad Fahad Ullah, Imadeldin Elfaki, Mohammad A. Alanazi, Naseh A. Algehainy, Faisal H. Altemani, Mamdoh S. Moawadh, Faris J. Tayeb, Badr A. Alsayed, Mohammad Muzaffar Mir, Jaber Alfaifi, Syed Khalid Mustafa, Jameel Barnawi, and Salma Saleh Alrdahe. “WholeExome Sequencing Reveals Rare Genetic Variants in Saudi COVID-19 Patients with Extreme Phenotypes”. In: _Viruses_ 17.9 (2025), p. 1198. doi: `10.3390/v17091198` .

- [87] Michal Witkowski, Carla Tizian, Mariana Ferreira-Gomes, et al. “Untimely TGF _𝛽_ responses in COVID-19 limit antiviral functions of NK cells”. In: _Nature_ 600 (2021), pp. 295–301. doi: `10.1038/s41586-021-04142-6` .

- [88] MateuszA.Maździarz, KatarzynaKrawczyk,EwaLepiarczyk,etal. “Poly(A) tail dynamics, non-adenine incorporation and alternative polyadenylation shape the host transcriptome in COVID-19 pathogenesis”. In: _Scientific Reports_ 15 (2025), p. 37986. doi: `10.1038/s41598-025-21969-5` .

- [89] Anru Zhang and Dong Xia. _Tensor SVD: Statistical and Computational Limits_ . 2020. arXiv: `1703.02724 [math.ST]` .

- [90] Gennady Gorin. “Stochastic foundations for single-cell RNA sequencing”. en. PhD Dissertation. Pasadena, California: California Institute of Technology, May 2023. url: `https://thesis.library.caltech.edu/16062/` .

- [91] Gennady Gorin, Mengyu Wang, Ido Golding, and Heng Xu. _Stochastic simulation platform for visualization and estimation of transcriptional kinetics_ . en. Preprint. bioRxiv: 825869, Nov. 2019. doi: `10.1101/825869` . url: `http://biorxiv.org/lookup/doi/10.1101/825869` (visited on 12/04/2019).

116

- [92] Peter Bokes, John R. King, and Martin Loose. “Exact and approximate distributions of protein and mRNA levels in the low-copy regime of gene expression”. In: _Journal of Mathematical Biology_ 64.5 (2012), pp. 829–854. doi: `10.1007/s00285-011-0433-5` .

- [93] Gennady Gorin and Lior Pachter. “Modeling bursty transcription and splicing with the chemical master equation”. In: _Biophysical Journal_ 121.6 (Feb. 2022), pp. 1056–1069. doi: `10.1016/j.bpj.2022.02.004` . url: `https: //www.cell.com/biophysj/fulltext/S0006-3495(22)00104-7` (visited on 03/26/2021).

- [94] Tobias Jahnke and Wilhelm Huisinga. “Solving the chemical master equation for monomolecular reaction systems analytically”. en. In: _Journal of Mathematical Biology_ 54 (Sept. 2006), pp. 1–26. issn: 0303-6812, 1432-1416. doi: `10.1007/s00285-006-0034-x` . url: `http://link.springer. com/10.1007/s00285-006-0034-x` (visited on 06/07/2019).

- [95] K.JayakumarandDavisAntonyMundassery. “OnMoran’sBivariateGamma and Bivariate Negative Binomial Distribution”. en. In: _Calcutta Statistical Association Bulletin_ 59.1-2 (Mar. 2007), pp. 15–28. issn: 0008-0683, 24566462. doi: `10.1177/0008068320070102` . url: `http://journals. sagepub.com/doi/10.1177/0008068320070102` (visitedon01/25/2022).

- [96] Gennady Gorin and Lior Pachter. _Intrinsic and extrinsic noise are distinguishable in a synthesis – export – degradation model of mRNA production_ . en. Preprint. bioRxiv: 2020.09.25.312868, Sept. 2020. doi: `10.1101/ 2020.09.25.312868` . url: `http://biorxiv.org/lookup/doi/10. 1101/2020.09.25.312868` (visited on 09/30/2020).

- [97] Lucy Ham, David Schnoerr, Rowan D. Brackston, and Michael P. H. Stumpf. “Exactly solvable models of stochastic gene expression”. en. In: _The Journal of Chemical Physics_ 152.14 (Apr. 2020), p. 144106. issn: 0021-9606, 10897690. doi: `10.1063/1.5143540` . url: `http://aip.scitation.org/ doi/10.1063/1.5143540` (visited on 11/22/2021).

- [98] Lucy Ham, Marcel Jackson, and Michael P.H. Stumpf. _Pathway dynamics can delineate the sources of transcriptional noise in gene expression_ . en. Preprint. bioRxiv: 2020.09.30.319814, Sept. 2020. doi: `10.1101/2020. 09.30.319814` . url: `http://biorxiv.org/lookup/doi/10.1101/ 2020.09.30.319814` (visited on 10/07/2020).

- [99] Gennady Gorin, John J. Vastola, Meichen Fang, and Lior Pachter. “Interpretable and tractable models of transcriptional noise for the rational design of single-molecule quantification experiments”. en. In: _Nature Communications_ 13.1 (Dec. 2022), p. 7620. issn: 2041-1723. doi: `10.1038/s41467022-34857-7` . url: `https://www.nature.com/articles/s41467022-34857-7` (visited on 12/15/2022).

117

- [100] Qingchao Jiang, Xiaoming Fu, Shifu Yan, Runlai Li, Wenli Du, Zhixing Cao, Feng Qian, and Ramon Grima. “Neural network aided approximation and parameter inference of non-Markovian models of gene expression”. en. In: _Nature Communications_ 12.1 (Dec. 2021), p. 2618. issn: 2041-1723. doi: `10.1038/s41467-021-22919-1` . url: `http://www.nature.com/ articles/s41467-021-22919-1` (visited on 11/06/2021).

- [101] Gennady Gorin, Shawn Yoshida, and Lior Pachter. “Assessing Markovian and Delay Models for Single-Nucleus RNA Sequencing”. en. In: _Bulletin of Mathematical Biology_ 85.11 (Oct. 2023), p. 114. doi: `10.1007/s11538023-01213-9` . url: `https://link.springer.com/article/10. 1007/s11538-023-01213-9` (visited on 10/18/2023).

- [102] Hao Lu, Hua Yan, Xiaoyu Li, Yuan Xing, Yumeng Ye, Siao Jiang, Luyu Ma, Jie Ping, Hongyan Zuo, Yanhui Hao, Chao Yu, Yang Li, Gangqiao Zhou, and Yiming Lu. “Single-cell map of dynamic cellular microenvironment of radiation-induced intestinal injury”. In: _Communications Biology_ 6 (2023), p. 1248. doi: `10.1038/s42003-023-05556-5` .

- [103] Ainhoa Arina, Michael Beckett, Christian Fernandez, Wenxin Zheng, Sean Pitroda, Steven J Chmura, Jason J Luke, Martin Forde, Yuzhu Hou, Byron Burnette, Helena Mauceri, Israel Lowy, Tasha Sims, Nikolai Khodarev, Yang-Xin Fu, and Ralph R Weichselbaum. “Tumor-reprogrammed resident T cells resist radiation to control tumors”. en. In: _Nat. Commun._ 10.1 (Sept. 2019), p. 3959.

- [104] Abobakr K Shadad, Frank J Sullivan, Joseph D Martin, and Laurence J Egan. “Gastrointestinal radiation injury: symptoms, risk factors and mechanisms”. en. In: _World J. Gastroenterol._ 19.2 (Jan. 2013), pp. 185–198.

- [105] Ryan C Augustin, Riyue Bao, and Jason J Luke. “Targeting Cbl-b in cancer immunotherapy”. en. In: _J. Immunother. Cancer_ 11.2 (Feb. 2023), e006007.

- [106] Miao Yu, Gang Guo, Lei Huang, Libin Deng, Chang-Sheng Chang, Bhagelu R Achyut, Madison Canning, Ningchun Xu, Ali S Arbab, Roni J Bollag, Paulo C Rodriguez, Andrew L Mellor, Huidong Shi, David H Munn, and Yan Cui. “CD73 on cancer-associated fibroblasts enhanced by the A2Bmediated feedforward circuit enforces an immune checkpoint”. en. In: _Nat. Commun._ 11.1 (Jan. 2020), p. 515.

- [107] Miao Yu, Gang Guo, Lei Huang, Libin Deng, Chang-Sheng Chang, Bhagelu R Achyut, Madison Canning, Ningchun Xu, Ali S Arbab, Roni J Bollag, Paulo C Rodriguez, Andrew L Mellor, Huidong Shi, David H Munn, and Yan Cui. “CD73 on cancer-associated fibroblasts enhanced by the A2Bmediated feedforward circuit enforces an immune checkpoint”. en. In: _Nat. Commun._ 11.1 (Jan. 2020), p. 515.

118

- [108] Linzhuo Qu, Huiying Che, Jingyu Zhao, Xin Lu, Zijun Ren, Yu Wu, Qian Liu, and Hongjian Guan. “NCAPD3 is a prognostic biomarker and is correlated with immune infiltrates in glioma”. en. In: _Histol. Histopathol._ 39.11 (Nov. 2024), pp. 1473–1484.

- [109] Ying Zhong, Xinyu Ren, Xi Cao, Yali Xu, Yu Song, Yidong Zhou, Feng Mao, Songjie Shen, Zhe Wang, and Qiang Sun. “Insulin-like growth factor 2 receptor is a key immune-related gene that is correlated with a poor prognosis in patients with triple-negative breast cancer: A bioinformatics analysis”. en. In: _Front. Oncol._ 12 (Oct. 2022), p. 871786.

- [110] Xiaotong Xu, Weyland Cheng, Shuai Zhao, Yuchun Liu, Lifeng Li, Xiaorui Song, Yaodong Zhang, and Cong Ding. “Pan-cancer analysis of the role of MPP7 in human tumors”. en. In: _Heliyon_ 10.16 (Aug. 2024), e36148.

- [111] Jürgen Dittmer. “The biology of the Ets1 proto-oncogene”. en. In: _Mol. Cancer_ 2.1 (Aug. 2003), p. 29.

- [112] Hyewon Phee, Marianne N Mollenauer, and Arthur Weiss. “Role of GIT2 in T cell migration and development (95.8)”. en. In: _J. Immunol._ 182.1_Supplement (Apr. 2009), pp. 95.8–95.8.

- [113] Kyle L O’Hagan, S Miller, and H Phee. “Pak2 is essential for the function of Foxp3+ regulatory T cells through maintaining a suppressive Treg phenotype”. In: _Sci. Rep._ 7 (Dec. 2017).

- [114] Germán Belenguer, Gianmarco Mastrogiovanni, Clare Pacini, Zoe Hall, Anna M Dowbaj, Robert Arnes-Benito, Aleksandra Sljukic, Nicole Prior, Sofia Kakava, Charles R Bradshaw, Susan Davies, Michele Vacca, Kourosh Saeb-Parsy, Bon-Kyoung Koo, and Meritxell Huch. “RNF43/ZNRF3 loss predisposes to hepatocellular-carcinoma by impairing liver regeneration and altering the liver lipid metabolic ground-state”. en. In: _Nat. Commun._ 13.1 (Jan. 2022), p. 334.

- [115] Fei Yue, Amy T Ku, Payton D Stevens, Megan N Michalski, Weiyu Jiang, Jianghua Tu, Zhongcheng Shi, Yongchao Dou, Yi Wang, Xin-Hua Feng, Galen Hostetter, Xiangwei Wu, Shixia Huang, Noah F Shroyer, Bing Zhang, Bart O Williams, Qingyun Liu, Xia Lin, and Yi Li. “Loss of ZNRF3/RNF43 unleashes EGFR in cancer”. en. In: _bioRxivorg_ (Jan. 2024).

- [116] Fei Yue, Amy T Ku, Payton D Stevens, Megan N Michalski, Weiyu Jiang, Jianghua Tu, Zhongcheng Shi, Yongchao Dou, Yi Wang, Xin-Hua Feng, Galen Hostetter, Xiangwei Wu, Shixia Huang, Noah F Shroyer, Bing Zhang, Bart O Williams, Qingyun Liu, Xia Lin, and Yi Li. “Loss of ZNRF3/RNF43 unleashes EGFR in cancer”. en. In: _bioRxivorg_ (Jan. 2024).

- [117] Jin-Li Wei, Si-Yu Wu, Yun-Song Yang, Yi Xiao, Xi Jin, Xiao-En Xu, Xin Hu, Da-Qiang Li, Yi-Zhou Jiang, and Zhi-Ming Shao. “GCH1 induces immunosuppression through metabolic reprogramming and IDO1 upregu-

119

lation in triple-negative breast cancer”. en. In: _J. Immunother. Cancer_ 9.7 (July 2021), e002383.

- [118] Q Zeng, L Li, Z Feng, L Luo, J Xiong, Z Jie, and Li. “LCP1 is a prognostic biomarker correlated with immune infiltrates in gastric cancer”. In: _Cancer Biomarkers_ 30.1 (2021), pp. 105–125.

- [119] Shengli Pan, Yingying Deng, Jun Fu, Yuhao Zhang, Zhijin Zhang, Xiaokun Ru, and Xianju Qin. “Decreased expression of ARHGAP15 promotes the development of colorectal cancer through PTEN/AKT/FOXO1 axis”. en. In: _Cell Death Dis._ 9.6 (June 2018), p. 673.

- [120] Bo Dou, Gang Jiang, Wang Peng, and Chentao Liu. “OTULIN deficiency: focus on innate immune system impairment”. en. In: _Front. Immunol._ 15 (May 2024), p. 1371564.

- [121] Wen-Yuan Wang, Ling Pan, Susan C Su, Emma J Quinn, Megumi Sasaki, Jessica C Jimenez, Ian R A Mackenzie, Eric J Huang, and Li-Huei Tsai. “Interaction of FUS and HDAC1 regulates DNA damage response and repair in neurons”. en. In: _Nat. Neurosci._ 16.10 (Oct. 2013), pp. 1383–1391.

- [122] Danixa Martínez, Daniela Nualart, Carlos Loncoman, Juan C Opazo, Kattina Zabala, Francisco J Morera, Gonzalo A Mardones, and Luis VargasChacoff. “Discovery of BbX transcription factor in the patagonian blennie: Exploring expression changes following combined bacterial and thermal stress exposure”. en. In: _Dev. Comp. Immunol._ 149.105056 (Dec. 2023), p. 105056.

- [123] Lab Mouse. “BIOART-000279. 10/07/2024. NIAID NIH BIOART Source”. In: (). `bioart.niaid.nih.gov/bioart/279` . url: `bioart.niaid.nih. gov/bioart/279` .

- [124] Human Anatomy. “BIOART-000519. 10/07/2024. NIAID NIH BIOART Source”. In: (). `bioart.niaid.nih.gov/bioart/519` . url: `bioart. niaid.nih.gov/bioart/519` .

- [125] GenericCells. “BIOART-000172.10/07/2024. NIAIDNIHBIOARTSource”. In: (). `bioart.niaid.nih.gov/bioart/172` . url: `bioart.niaid.nih. gov/bioart/172` .

- [126] Zizhen Yao, Hanqing Liu, Fangming Xie, Stephan Fischer, Ricky S. Adkins, Andrew I. Aldridge, Seth A. Ament, Anna Bartlett, M. Margarita Behrens, Koen Van den Berge, Darren Bertagnolli, Hector Roux de Bézieux, Tommaso Biancalani, A. Sina Booeshaghi, Héctor Corrada Bravo, Tamara Casper,CarloColantuoni, JonathanCrabtree,HeatherCreasy,KirstenCrichton, Megan Crow, Nick Dee, Elizabeth L. Dougherty, Wayne I. Doyle, Sandrine Dudoit, Rongxin Fang, Victor Felix, Olivia Fong, Michelle Giglio, Jeff Goldy, Mike Hawrylycz, Brian R. Herb, Ronna Hertzano, Xiaomeng Hou, Qiwen Hu, Jayaram Kancherla, Matthew Kroll, Kanan Lathia, Yang Eric Li, Jacinta D. Lucero, Chongyuan Luo, Anup Mahurkar, Delissa McMillen,

120

Naeem M. Nadaf, Joseph R. Nery, Thuc Nghi Nguyen, Sheng-Yong Niu, Vasilis Ntranos, Joshua Orvis, Julia K. Osteen, Thanh Pham, Antonio PintoDuarte, Olivier Poirion, Sebastian Preissl, Elizabeth Purdom, Christine Rimorin, Davide Risso, Angeline C. Rivkin, Kimberly Smith, Kelly Street, Josef Sulc, Valentine Svensson, Michael Tieu, Amy Torkelson, Herman Tung, Eeshit Dhaval Vaishnav, Charles R. Vanderburg, Cindy van Velthoven, Xinxin Wang, Owen R. White, Z. Josh Huang, Peter V. Kharchenko, Lior Pachter, John Ngai, Aviv Regev, Bosiljka Tasic, Joshua D. Welch, Jesse Gillis, Evan Z. Macosko, Bing Ren, Joseph R. Ecker, Hongkui Zeng, and Eran A. Mukamel. “A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex”. en. In: _Nature_ 598.7879 (Oct. 2021), pp. 103–110. issn: 0028-0836, 1476-4687. doi: `10.1038/s41586-021-03500-8` . url: `https://www.nature.com/articles/s41586-021-03500-8` (visited on 11/15/2021).

- [127] Valentine Svensson. “Droplet scRNA-seq is not zero-inflated”. en. In: _Nature Biotechnology_ 38.2 (Feb. 2020), pp. 147–150. issn: 1087-0156, 1546-1696. doi: `10.1038/s41587-019-0379-5` . url: `https://www.nature.com/ articles/s41587-019-0379-5` (visited on 08/29/2020).

- [128] Joseph Rodriguez and Daniel R. Larson. “Transcription in Living Cells: Molecular Mechanisms of Bursting”. In: _Annual Review of Biochemistry_ 89.Volume 89, 2020 (2020), pp. 189–212. issn: 1545-4509. doi: `https:// doi.org/10.1146/annurev-biochem-011520-105250` . url: `https: //www.annualreviews.org/content/journals/10.1146/annurevbiochem-011520-105250` .

- [129] Tae Hyun Kim, Xiang Zhou, and Mengjie Chen. “Demystifying “drop-outs” in single-cell UMI data”. en. In: _Genome Biology_ 21 (Dec. 2020), p. 196. issn: 1474-760X. doi: `10.1186/s13059-020-02096-y` . url: `https:// genomebiology.biomedcentral.com/articles/10.1186/s13059020-02096-y` (visited on 02/27/2021).

- [130] Crispin Gardiner. _Handbook of Stochastic Methods for Physics, Chemistry, and the Natural Sciences_ . Third. Springer, 2004.

- [131] Brian Munsky, Guoliang Li, Zachary R. Fox, Douglas P. Shepherd, and Gregor Neuert. “Distribution shapes govern the discovery of predictive models for gene regulation”. en. In: _Proceedings of the National Academy of Sciences_ 115.29 (2018), pp. 7533–7538. issn: 0027-8424, 1091-6490. doi: `10.1073/pnas.1804060115` . (Visited on 08/24/2019).

- [132] Xiaoming Fu, Heta P Patel, Stefano Coppola, Libin Xu, Zhixing Cao, Tineke L Lenstra, and Ramon Grima. “Quantifying how post-transcriptional noise and gene copy number variation bias transcriptional parameter inference from mRNA distributions”. en. In: _eLife_ 11 (Oct. 2022), e82493. issn: 2050084X. doi: `10.7554/eLife.82493` . url: `https://elifesciences. org/articles/82493` (visited on 01/07/2023).

121

- [133] BrianMunsky,ZacharyFox, andGregorNeuert.“Integratingsingle-molecule experiments and discrete stochastic models to understand heterogeneous gene transcription dynamics”. en. In: _Methods_ 85 (2015), pp. 12–21. issn: 10462023. doi: `10.1016/j.ymeth.2015.06.009` . url: `https:// linkinghub . elsevier . com / retrieve / pii / S1046202315002510` (visited on 06/07/2019).

- [134] Grace X. Y. Zheng, Jessica M. Terry, Phillip Belgrader, Paul Ryvkin, Zachary W. Bent, Ryan Wilson, Solongo B. Ziraldo, Tobias D. Wheeler, Geoff P. McDermott, Junjie Zhu, Mark T. Gregory, Joe Shuga, Luz Montesclaros,JasonG.Underwood, DonaldA.Masquelier,StefanieY.Nishimura, Michael Schnall-Levin, Paul W. Wyatt, Christopher M. Hindson, Rajiv Bharadwaj, Alexander Wong, Kevin D. Ness, Lan W. Beppu, H. Joachim Deeg, Christopher McFarland, Keith R. Loeb, William J. Valente, Nolan G. Ericson, Emily A. Stevens, Jerald P. Radich, Tarjei S. Mikkelsen, Benjamin J. Hindson, and Jason H. Bielas. “Massively parallel digital transcriptional profiling of single cells”. en. In: _Nature Communications_ 8.1 (Apr. 2017), p. 14049. issn: 2041-1723. doi: `10.1038/ncomms14049` . url: `http: //www.nature.com/articles/ncomms14049` (visited on 08/22/2019).

- [135] Kristján Eldjárn Hjörleifsson, Delaney K. Sullivan, Guillaume Holley, Páll Melsted, and Lior Pachter. _Accurate quantification of single-nucleus and single-cell RNA-seq transcripts_ . en. Preprint. bioRxiv: 2022.12.02.518832, Dec. 2022. url: `http://biorxiv.org/lookup/doi/10.1101/2022. 12.02.518832` (visited on 12/12/2022).

- [136] Gioele La Manno, Ruslan Soldatov, Amit Zeisel, Emelie Braun, Hannah Hochgerner, Viktor Petukhov, Katja Lidschreiber, Maria E. Kastriti, Peter Lönnerberg, Alessandro Furlan, Jean Fan, Lars E. Borm, Zehua Liu, David van Bruggen, Jimin Guo, Xiaoling He, Roger Barker, Erik Sundström, Gonçalo Castelo-Branco, Patrick Cramer, Igor Adameyko, Sten Linnarsson, and Peter V. Kharchenko. “RNA velocity of single cells”. en. In: _Nature_ 560.7719 (Aug. 2018), pp. 494–498. issn: 0028-0836, 1476-4687. doi: `10.1038/s41586-018-0414-6` . url: `http://www.nature.com/ articles/s41586-018-0414-6` (visited on 08/22/2019).

- [137] Páll Melsted, A. Sina Booeshaghi, Lauren Liu, Fan Gao, Lambda Lu, Kyung Hoi Min, Eduardo da Veiga Beltrame, Kristján Eldjárn Hjörleifsson, Jase Gehring, and Lior Pachter. “Modular, efficient and constant-memory singlecell RNA-seq preprocessing”. en. In: _Nature Biotechnology_ 39.7 (July 2021), pp. 813–818. issn: 1087-0156, 1546-1696. doi: `10.1038/s41587-02100870-2` . url: `http://www.nature.com/articles/s41587-02100870-2` (visited on 11/15/2021).

- [138] Eleni P. Mimitou, Anthony Cheng, Antonino Montalbano, Stephanie Hao, MarlonStoeckius,MateuszLegut, TimothyRoush,AlbertoHerrera,Efthymia Papalexi, Zhengqing Ouyang, Rahul Satija, Neville E. Sanjana, Sergei B.

122

Koralov, and Peter Smibert. “Multiplexed detection of proteins, transcriptomes, clonotypes and CRISPR perturbations in single cells”. en. In: _Nature Methods_ 16.5 (May 2019), pp. 409–412. issn: 1548-7091, 1548-7105. doi: `10.1038/s41592- 019- 0392- 0` . url: `http://www.nature.com/ articles/s41592-019-0392-0` (visited on 08/22/2019).

- [139] Junyue Cao, Darren A. Cusanovich, Vijay Ramani, Delasa Aghamirzaie, Hannah A. Pliner, Andrew J. Hill, Riza M. Daza, Jose L. McFaline-Figueroa, Jonathan S. Packer, Lena Christiansen, Frank J. Steemers, Andrew C. Adey, Cole Trapnell, and Jay Shendure. “Joint profiling of chromatin accessibility and gene expression in thousands of single cells”. en. In: _Science_ 361.6409 (Sept. 2018), pp. 1380–1385. issn: 0036-8075, 1095-9203. doi: `10.1126/ science.aau0730` . url: `http://www.sciencemag.org/lookup/doi/ 10.1126/science.aau0730` (visited on 06/07/2019).

- [140] HengXu,SamuelO. Skinner,AnnaMarieSokac,andIdoGolding. “Stochastic Kinetics of Nascent RNA”. en. In: _Physical Review Letters_ 117.12 (2016), p. 128101. issn: 0031-9007, 1079-7114. doi: `10.1103/PhysRevLett. 117.128101` . url: `https://journals.aps.org/prl/abstract/10. 1103/PhysRevLett.117.128101` (visited on 09/15/2019).

- [141] Yuhan Hao, Stephanie Hao, Erica Andersen-Nissen, William M. Mauck, Shiwei Zheng, Andrew Butler, Maddie J. Lee, Aaron J. Wilk, Charlotte Darby, Michael Zager, Paul Hoffman, Marlon Stoeckius, Efthymia Papalexi, Eleni P. Mimitou, Jaison Jain, Avi Srivastava, Tim Stuart, Lamar M. Fleming, Bertrand Yeung, Angela J. Rogers, Juliana M. McElrath, Catherine A. Blish, Raphael Gottardo, Peter Smibert, and Rahul Satija. “Integrated analysis of multimodal single-cell data”. en. In: _Cell_ 184.13 (June 2021), 3573–3587.e29. issn: 00928674. doi: `10 . 1016 / j . cell . 2021 . 04 . 048` . url: `https://linkinghub.elsevier.com/retrieve/pii/ S0092867421005833` (visited on 09/27/2021).

- [142] John J Vastola. “In search of a coherent theoretical framework for stochastic gene regulation”. en. PhD thesis. Vanderbilt, Mar. 2021. url: `https:// ir.vanderbilt.edu/handle/1803/16646` .

- [143] Daniel T Gillespie. “A general method for numerically simulating the stochastic time evolution of coupled chemical reactions”. en. In: _Journal of Computational Physics_ 22.4 (Dec. 1976), pp. 403–434. issn: 00219991. doi: `10.1016/0021-9991(76)90041-3` . url: `https://linkinghub. elsevier.com/retrieve/pii/0021999176900413` (visitedon08/25/2019).

- [144] Brian Munsky and Mustafa Khammash. “The finite state projection algorithm for the solution of the chemical master equation”. en. In: _The Journal of Chemical Physics_ 124.4 (2006), p. 044104. issn: 0021-9606, 1089-7690. doi: `10.1063/1.2145882` . (Visited on 08/25/2019).

123

- [145] Ankit Gupta, Jan Mikelson, and Mustafa Khammash. “A finite state projection algorithm for the stationary solution of the chemical master equation”. en. In: _The Journal of Chemical Physics_ 147.15 (Oct. 2017), p. 154101. issn: 0021-9606, 1089-7690. doi: `10.1063/1.5006484` . url: `http://aip. scitation.org/doi/10.1063/1.5006484` (visited on 07/29/2019).

- [146] Zachary Fox, Gregor Neuert, and Brian Munsky. “Finite state projection based bounds to compare chemical master equation models using singlecell data”. en. In: _The Journal of Chemical Physics_ 145.7 (Aug. 2016), p. 074101. issn: 0021-9606, 1089-7690. doi: `10.1063/1.4960505` . url: `http://aip.scitation.org/doi/10.1063/1.4960505` (visited on 07/22/2019).

- [147] Pavol Bokes, John R. King, Andrew T. A. Wood, and Matthew Loose. “Exact and approximate distributions of protein and mRNA levels in the low-copy regime of gene expression”. en. In: _Journal of Mathematical Biology_ 64.5 (Apr. 2012), pp. 829–854. issn: 0303-6812, 1432-1416. doi: `10.1007/ s00285-011-0433-5` . url: `http://link.springer.com/10.1007/ s00285-011-0433-5` (visited on 08/09/2019).

- [148] Romain Lopez, Jeffrey Regier, Michael B. Cole, Michael I. Jordan, and Nir Yosef. “Deep generative modeling for single-cell transcriptomics”. en. In: _Nature Methods_ 15.12 (Dec. 2018), pp. 1053–1058. issn: 1548-7091, 15487105. doi: `10.1038/s41592-018-0229-2` . url: `http://www.nature. com/articles/s41592-018-0229-2` (visited on 08/10/2021).

- [149] Adam Gayoso, Zoë Steier, Romain Lopez, Jeffrey Regier, Kristopher L. Nazor, Aaron Streets, and Nir Yosef. “Joint probabilistic modeling of singlecell multi-omic data with totalVI”. en. In: _Nature Methods_ 18.3 (Mar. 2021), pp. 272–282. issn: 1548-7091, 1548-7105. doi: `10.1038/s41592-02001050-x` . url: `http://www.nature.com/articles/s41592-02001050-x` (visited on 11/19/2021).

- [150] Kathleen Champion, Bethany Lusch, J. Nathan Kutz, and Steven L. Brunton. “Data-driven discovery of coordinates and governing equations”. en. In: _Proceedings of the National Academy of Sciences_ 116.45 (Nov. 2019), pp. 22445–22451. issn: 0027-8424, 1091-6490. doi: `10. 1073/ pnas . 1906995116` . url: `https://pnas.org/doi/full/10.1073/pnas. 1906995116` (visited on 06/02/2022).

- [151] ZongyiLi,NikolaKovachki, KamyarAzizzadenesheli,BurigedeLiu,Kaushik Bhattacharya, Andrew Stuart, and Anima Anandkumar. _Fourier Neural Operator for Parametric Partial Differential Equations_ . Preprint. arXiv: 2010.08895, May 2021. url: `http://arxiv.org/abs/2010.08895` (visited on 10/01/2022).

- [152] Long Cai, Nir Friedman, and X. Sunney Xie. “Stochastic protein expression in individual cells at the single molecule level”. en. In: _Nature_ 440.7082 (Mar. 2006), pp. 358–362. issn: 0028-0836, 1476-4687. doi: `10.1038/`

124

`nature04599` . url: `http://www.nature.com/articles/nature04599` (visited on 12/05/2019).

- [153] Sheel Shah, Yodai Takei, Wen Zhou, Eric Lubeck, Jina Yun, Chee-Huat Linus Eng, Noushin Koulena, Christopher Cronin, Christoph Karp, Eric J. Liaw, Mina Amin, and Long Cai. “Dynamics and Spatial Genomics of the Nascent Transcriptome by Intron seqFISH”. en. In: _Cell_ 174.2 (July 2018), 363–376.e16. issn: 00928674. doi: `10.1016/j.cell.2018.05. 035` . url: `https://linkinghub.elsevier.com/retrieve/pii/ S0092867418306470` (visited on 08/24/2019).

- [154] Yodai Takei, Yujing Yang, Jonathan White, Jina Yun, Meera Prasad, Lincoln J Ombelets, Simone Schindler, and Long Cai. _High-resolution spatial multi-omics reveals cell-type specific nuclear compartments_ . en. Tech. rep. bioRxiv, 2023. url: `https://www.biorxiv.org/content/10.1101/ 2023.05.07.539762v1` .

- [155] Shangying Wang, Sara Capponi, and Simone Bianco. “Inferring Conditional Probability Distributions of Noisy Gene Expression from Limited Observations by Deep Learning.” In: _GEN Biotechnology_ 1 (6 1984), pp. 504– 513.

- [156] Ankit Gupta, Christoph Schwab, and Mustafa Khammash. “DeepCME: A deep learning framework for computing solution statistics of the chemical master equation”. en. In: _PLOS Computational Biology_ 17.12 (Dec. 2021). Ed. by James R. Faeder, e1009623. issn: 1553-7358. doi: `10.1371/ journal.pcbi.1009623` . url: `https://dx.plos.org/10.1371/ journal.pcbi.1009623` (visited on 03/16/2022).

- [157] Augustinas Sukys, Kaan Öcal, and Ramon Grima. “Approximating solutions of the Chemical Master equation using neural networks”. In: _iScience_ 25.9 (Aug. 2022), p. 105010. issn: 2589-0042. doi: `10.1016/j.isci.2022. 105010` . url: `https://www.ncbi.nlm.nih.gov/pmc/articles/ PMC9474291/` (visited on 03/02/2023).

- [158] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy,DavidCournapeau, EvgeniBurovski,PearuPeterson,WarrenWeckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, C J Carey, Ilhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, SciPy 1.0 Contributors, Aditya Vijaykumar, Alessandro Pietro Bardelli, Alex Rothberg, Andreas Hilboll, Andreas Kloeckner, Anthony Scopatz, Antony Lee, Ariel Rokem, C. Nathan Woods, Chad Fulton, Charles Masson, Christian Häggström, Clark Fitzgerald, David A. Nicholson, David R. Hagen, Dmitrii V. Pasechnik, Emanuele Olivetti, Eric Martin, Eric Wieser, Fabrice Silva, Felix

125

Lenders, Florian Wilhelm, G. Young, Gavin A. Price, Gert-Ludwig Ingold, Gregory E. Allen, Gregory R. Lee, Hervé Audren, Irvin Probst, Jörg P. Dietrich, Jacob Silterra, James T Webber, Janko Slavič, Joel Nothman, Johannes Buchner, Johannes Kulick, Johannes L. Schönberger, José Vinícius de Miranda Cardoso, Joscha Reimer, Joseph Harrington, Juan Luis Cano Rodríguez, Juan Nunez-Iglesias, Justin Kuczynski, Kevin Tritz, Martin Thoma, Matthew Newville, Matthias Kümmerer, Maximilian Bolingbroke, Michael Tartre, Mikhail Pak, Nathaniel J. Smith, Nikolai Nowaczyk, Nikolay Shebanov, Oleksandr Pavlyk, Per A. Brodtkorb, Perry Lee, Robert T. McGibbon, Roman Feldbauer, Sam Lewis, Sam Tygier, Scott Sievert, Sebastiano Vigna, Stefan Peterson, Surhud More, et al. “SciPy 1.0: fundamental algorithms for scientific computing in Python”. en. In: _Nature Methods_ 17.3 (Mar. 2020), pp. 261–272. issn: 1548-7091, 1548-7105. doi: `10.1038/s41592-0190686-2` . url: `http://www.nature.com/articles/s41592-0190686-2` (visited on 11/15/2021).

- [159] Charles R. Harris, K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus, Stephan Hoyer, Marten H. van Kerkwijk, Matthew Brett, Allan Haldane, Jaime Fernández del Río, Mark Wiebe, Pearu Peterson, Pierre Gérard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser, Hameer Abbasi, Christoph Gohlke, and Travis E. Oliphant. “Array programming with NumPy”. en. In: _Nature_ 585.7825 (Sept. 2020), pp. 357–362. issn: 0028-0836, 1476-4687. doi: `10.1038/s41586-020-2649-2` . url: `https://www.nature.com/ articles/s41586-020-2649-2` (visited on 06/09/2022).

- [160] Lisa Amrhein, Kumar Harsha, and Christiane Fuchs. _A mechanistic model for the negative binomial distribution of single-cell mRNA counts_ . Preprint. bioRxiv: 657619, June 2019. doi: `10 . 1101 / 657619` . url: `http : / / biorxiv.org/lookup/doi/10.1101/657619` (visited on 08/24/2019).

- [161] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Kopf, Edward Yang, Zachary DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala. “PyTorch: An Imperative Style, High-Performance Deep Learning Library”. In: _Advances in Neural Information Processing Systems 32_ . Ed. by H. Wallach, H. Larochelle, A. Beygelzimer, F. d’ Alché-Buc, E. Fox, and R. Garnett. Curran Associates, Inc., 2019, pp. 8024–8035. url: `http://papers.neurips.cc/paper/ 9015-pytorch-an-imperative-style-high-performance-deeplearning-library.pdf` .

- [162] Gennady Gorin and Lior Pachter. _Distinguishing biophysical stochasticity from technical noise in single-cell RNA sequencing using Monod_ . Preprint.

126

bioRxiv: 2022.06.11.495771, Apr. 2023. url: `https://www.biorxiv. org/content/10.1101/2022.06.11.495771v2` (visitedon06/17/2022).

- [163] Zachary R Fox and Brian Munsky. “The finite state projection based Fisher information matrix approach to estimate information and optimize singlecell experiments”. en. In: _PLOS Computational Biology_ 15.1 (Jan. 2019). Ed. by Oleg A Igoshin, e1006365. issn: 1553-7358. doi: `10.1371/journal. pcbi.1006365` . url: `https://dx.plos.org/10.1371/journal. pcbi.1006365` (visited on 05/07/2021).

- [164] Jingyao Wang, Shihe Zhang, Hongfang Lu, and Heng Xu. “Differential regulation of alternative promoters emerges from unified kinetics of enhancerpromoter interaction”. en. In: _Nature Communications_ 13.1 (Dec. 2022), p. 2714. issn: 2041-1723. doi: `10.1038/s41467-022-30315-6` . url: `https://www.nature.com/articles/s41467-022-30315-6` (visited on 06/17/2022).

- [165] Florian De Rop, Joy N Ismail, Carmen Bravo González-Blas, Gert J Hulselmans, Christopher Campbell Flerin, Jasper Janssens, Koen Theunis, Valerie M Christiaens, Jasper Wouters, Gabriele Marcassa, Joris de Wit, Suresh Poovathingal, and Stein Aerts. “HyDrop enables droplet based single-cell ATAC-seq and single-cell RNA-seq using dissolvable hydrogel beads”. en. In: _eLife_ 11 (Feb. 2022), e73971. issn: 2050-084X. doi: `10.7554/eLife. 73971` . url: `https://elifesciences.org/articles/73971` (visited on 03/18/2022).

- [166] MarlonStoeckius,ChristophHafemeister, WilliamStephenson,BrianHouckLoomis, Pratip K Chattopadhyay, Harold Swerdlow, Rahul Satija, and Peter Smibert. “Simultaneous epitope and transcriptome measurement in single cells”. en. In: _Nature Methods_ 14.9 (Sept. 2017), pp. 865–868. issn: 1548-7091, 1548-7105. doi: `10.1038/nmeth.4380` . url: `http://www. nature.com/articles/nmeth.4380` (visited on 08/22/2019).

- [167] Gennady Gorin, Valentine Svensson, and Lior Pachter. “Protein velocity and acceleration from single-cell multiomics experiments”. en. In: _Genome Biology_ 21 (Feb. 2020), p. 39. issn: 1474-760X. doi: `10.1186/s13059020-1945-3` . url: `https://genomebiology.biomedcentral.com/ articles/10.1186/s13059-020-1945-3` (visited on 02/24/2020).

- [168] Vanessa M Peterson, Kelvin Xi Zhang, Namit Kumar, Jerelyn Wong, Lixia Li, Douglas C Wilson, Renee Moore, Terrill K McClanahan, Svetlana Sadekova, and Joel A Klappenbach. “Multiplexed quantification of proteins and transcripts in single cells”. en. In: _Nature Biotechnology_ 35.10 (Oct. 2017), pp. 936–939. issn: 1087-0156, 1546-1696. doi: `10.1038/nbt. 3973` . url: `http://www.nature.com/articles/nbt.3973` (visited on 08/22/2019).

127

- [169] Hattie Chung, Christopher N. Parkhurst, Emma M. Magee, Devan Phillips, Ehsan Habibi, Fei Chen, Bertrand Z. Yeung, Julia Waldman, David Artis, and Aviv Regev. “Joint single-cell measurements of nuclear proteins and RNA in vivo”. en. In: _Nature Methods_ 18.10 (Oct. 2021), pp. 1204–1212. issn: 1548-7091, 1548-7105. doi: `10.1038/s41592-021-01278-1` . url: `https://www.nature.com/articles/s41592-021-01278-1` (visited on 10/13/2021).

- [170] Valentine Svensson, Roser Vento-Tormo, and Sarah A Teichmann. “Exponential scaling of single-cell RNA-seq in the past decade”. en. In: _Nature Protocols_ 13.4 (Apr. 2018), pp. 599–604. issn: 1754-2189, 1750-2799. doi: `10.1038/nprot.2017.149` . url: `http://www.nature.com/ articles/nprot.2017.149` (visited on 09/24/2019).

- [171] Adam Gayoso, Romain Lopez, Galen Xing, Pierre Boyeau, Valeh Valiollah Pour Amiri, Justin Hong, Katherine Wu, Michael Jayasuriya, Edouard Mehlman, Maxime Langevin, Yining Liu, Jules Samaran, Gabriel Misrachi, Achille Nazaret, Oscar Clivio, Chenling Xu, Tal Ashuach, Mariano Gabitto, Mohammad Lotfollahi, Valentine Svensson, Eduardo da Veiga Beltrame, Vitalii Kleshchevnikov, Carlos Talavera-López, Lior Pachter, Fabian J. Theis, Aaron Streets, Michael I. Jordan, Jeffrey Regier, and Nir Yosef. “A Python library for probabilistic analysis of single-cell omics data”. en. In: _Nature Biotechnology_ 40.2 (Feb. 2022), pp. 163–166. issn: 1087-0156, 1546-1696. doi: `10.1038/s41587-021-01206-w` . url: `https://www.nature. com/articles/s41587-021-01206-w` (visited on 04/14/2023).

- [172] Xiang Lin, Tian Tian, Zhi Wei, and Hakon Hakonarson. “Clustering of single-cell multi-omics data with a multimodal deep learning method”. en. In: _Nature Communications_ 13.1 (Dec. 2022), p. 7705. issn: 2041-1723. doi: `10.1038/s41467-022-35031-9` . url: `https://www.nature. com/articles/s41467-022-35031-9` (visited on 12/18/2022).

- [173] Tal Ashuach, Daniel A. Reidenbach, Adam Gayoso, and Nir Yosef. “PeakVI: A deep generative model for single-cell chromatin accessibility analysis”. en. In: _Cell Reports Methods_ 2.3 (Mar. 2022), p. 100182. issn: 26672375. doi: `10.1016/j.crmeth.2022.100182` . url: `https://linkinghub. elsevier.com/retrieve/pii/S2667237522000376` (visitedon12/26/2022).

- [174] A. Sanchez and I. Golding. “Genetic Determinants and Cellular Constraints in Noisy Gene Expression”. en. In: _Science_ 342.6163 (Dec. 2013), pp. 1188– 1193. issn: 0036-8075, 1095-9203. doi: `10.1126/science.1242975` . url: `http://www.sciencemag.org/cgi/doi/10.1126/science. 1242975` (visited on 09/03/2019).

- [175] Judea Pearl. “Causal Inference in Statistics: An Overview”. In: _Statistics Surveys_ 3 (2009), pp. 96–146. issn: 1935-7516. doi: `10.1214/09-SS057` .

128

- [176] Nico Battich, Joep Beumer, Buys de Barbanson, Lenno Krenning, Chloé S. Baron, Marvin E. Tanenbaum, Hans Clevers, and Alexander van Oudenaarden. “Sequencing metabolically labeled transcripts in single cells reveals mRNA turnover strategies”. en. In: _Science_ 367.6482 (Mar. 2020), pp. 1151– 1156. issn: 0036-8075, 1095-9203. doi: `10.1126/science.aax3072` . url: `https://www.science.org/doi/10.1126/science.aax3072` (visited on 11/10/2021).

- [177] XL. Kuang, XM. Zhao, HF. Xu, YY. Shi, JB. Deng, and GT. Sun. “Spatiotemporal expression of a novel neuron-derived neurotrophic factor (NDNF) in mouse brains during development”. In: _BMC Neurosci_ 11 (2010).

- [178] T. K. Ulland and M. Colonna. “TREM2 — a key player in microglial biology and Alzheimer disease”. In: _Nature Reviews Neurology_ 14 (2018), pp. 667– 675.

- [179] Lucy Ham, Rowan D. Brackston, and Michael P. H. Stumpf. “Extrinsic Noise and Heavy-Tailed Laws in Gene Expression”. en. In: _Physical Review Letters_ 124.10 (Mar. 2020), p. 108101. issn: 0031-9007, 1079-7114. doi: `10.1103/PhysRevLett.124.108101` . url: `https://link.aps.org/ doi/10.1103/PhysRevLett.124.108101` (visited on 08/28/2020).

- [180] Michael B Elowitz, Arnold J Levine, Eric D Siggia, and Peter S Swain. “Stochastic Gene Expression in a Single Cell”. en. In: _Science_ 297.5584 (2002), pp. 1183–1186. doi: `10.1126/science.1070919` .

- [181] Gennady Gorin and Lior Pachter. “Length biases in single-cell RNA sequencing of pre-mRNA”. en. In: _Biophysical Reports_ 3.1 (Mar. 2023), p. 100097. issn: 26670747. doi: `10.1016/j.bpr.2022.100097` . url: `https://linkinghub.elsevier.com/retrieve/pii/S2667074722000544` (visited on 01/11/2023).

- [182] Valentine Svensson, Adam Gayoso, Nir Yosef, and Lior Pachter. “Interpretable factor models of single-cell RNA-seq via variational autoencoders”. en. In: _Bioinformatics_ 36.11(June2020). Ed.byAnthonyMathelier,pp.3418– 3421. issn: 1367-4803, 1460-2059. doi: `10.1093/bioinformatics/ btaa169` . url: `https : / / academic . oup . com / bioinformatics / article/36/11/3418/5807606` (visited on 01/09/2023).

- [183] Jingshu Wang, Mo Huang, Eduardo Torre, Hannah Dueck, Sydney Shaffer, John Murray, Arjun Raj, Mingyao Li, and Nancy R. Zhang. “Gene expression distribution deconvolution in single-cell RNA sequencing”. en. In: _Proceedings of the National Academy of Sciences_ 115.28 (July 2018), E6437–E6446. issn: 0027-8424, 1091-6490. doi: `10.1073/pnas.1721085115` . url: `http://www.pnas.org/lookup/doi/10.1073/pnas.1721085115` (visited on 04/09/2020).

129

- [184] Allen Institute for Brain Science. _FASTQ files for Allen v3 mouse MOp samples_ . Feb. 2020. url: `http://data.nemoarchive.org/biccn/ grant/u19_zeng/zeng/transcriptome/scell/10x_v3/mouse/raw/ MOp/` .

- [185] Allen Institute for Brain Science. _Analyses for Allen v3 mouse MOp samples_ . Feb. 2020. url: `http://data.nemoarchive.org/biccn/grant/u19_ zeng/zeng/transcriptome/scell/10x_v3/mouse/processed/ analysis/10X_cells_v3_AIBS/` .

- [186] F. Alexander Wolf, Philipp Angerer, and Fabian J. Theis. “SCANPY: largescale single-cell gene expression data analysis”. en. In: _Genome Biology_ 19.1 (Dec. 2018), p. 15. issn: 1474-760X. doi: `10.1186/s13059-017-1382-0` . url: `https://genomebiology.biomedcentral.com/articles/10. 1186/s13059-017-1382-0` (visited on 08/23/2019).

- [187] François Jacob and Jacques Monod. “Genetic regulatory mechanisms in the synthesis of proteins”. In: _Journal of molecular biology_ 3.3 (1961), pp. 318– 356.

- [188] Rita JS Phillips. “A cis-trans position effect at the A locus of the house mouse”. In: _Genetics_ 54.2 (1966), p. 485.

- [189] John S Kovach, Antonio O Ballesteros, Marilyn Meyers, Marco Soria, and Robert F Goldberger. “A cis/trans test of the effect of the first enzyme for histidine biosynthesis on regulation of the histidine operon”. In: _Journal of Bacteriology_ 114.1 (1973), pp. 351–356.

- [190] Christopher R Cowles, Joel N Hirschhorn, David Altshuler, and Eric S Lander. “Detection of regulatory variation in mouse genes”. In: _Nature genetics_ 32.3 (2002), pp. 432–437.

- [191] Patricia J Wittkopp, Belinda K Haerum, and Andrew G Clark. “Evolutionary changes in cis and trans gene regulation”. In: _Nature_ 430.6995 (2004), pp. 85–88.

- [192] Christian R Landry, Patricia J Wittkopp, Clifford H Taubes, Jose M Ranz, Andrew G Clark, and Daniel L Hartl. “Compensatory cis-trans evolution and the dysregulation of gene expression in interspecific hybrids of Drosophila”. In: _Genetics_ 171.4 (2005), pp. 1813–1822.

- [193] Angela Goncalves, Sarah Leigh-Brown, David Thybert, Klara Stefflova, Ernest Turro, Paul Flicek, Alvis Brazma, Duncan T Odom, and John C Marioni. “Extensive compensatory cis-trans regulation in the evolution of mouse gene expression”. In: _Genome research_ 22.12 (2012), pp. 2376–2384.

- [194] Andreas Massouras, Sebastian M Waszak, Monica Albarca-Aguilera, Korneel Hens, Wiebke Holcombe, Julien F Ayroles, Emmanouil T Dermitzakis, Eric A Stone, Jeffrey D Jensen, Trudy FC Mackay, et al. “Genomic variation and its impact on gene expression in Drosophila melanogaster”. In: _PLoS genetics_ 8.11 (2012), e1003055.

130

- [195] Andreas Tsouris, Gauthier Brach, Joseph Schacherer, and Jing Hou. “Nonadditive genetic components contribute significantly to population-wide gene expression variation”. In: _Cell Genomics_ 4.1 (2024).

- [196] C Joel McManus, Joseph D Coolon, Michael O Duff, Jodi Eipper-Mains, Brenton R Graveley, and Patricia J Wittkopp. “Regulatory divergence in Drosophila revealed by mRNA-seq”. In: _Genome research_ 20.6 (2010), pp. 816–825.

- [197] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy,DavidCournapeau, EvgeniBurovski,PearuPeterson,WarrenWeckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, C J Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. “SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python”. In: _Nature Methods_ 17 (2020), pp. 261–272. doi: `10.1038/s41592-0190686-2` .

- [198] Yoav Benjamini and Yosef Hochberg. “Controlling the false discovery rate: a practical and powerful approach to multiple testing”. In: _Journal of the Royal statistical society: series B (Methodological)_ 57.1 (1995), pp. 289– 300.

- [199] Mark D. Robinson, Davis J. McCarthy, and Gordon K. Smyth. “edgeR: a Bioconductor package for differential expression analysis of digital gene expression data”. In: _Bioinformatics_ 26.1 (Jan. 2010), pp. 139–140. issn: 1367-4803. doi: `10.1093/bioinformatics/btp616` . url: `https:// www.ncbi.nlm.nih.gov/pmc/articles/PMC2796818/` (visited on 02/18/2025).

- [200] Michael I. Love, Wolfgang Huber, and Simon Anders. “Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2”. In: _Genome Biology_ 15.12 (Dec. 2014), p. 550. issn: 1474-760X. doi: `10.1186/s13059-014-0550-8` . url: `https://doi.org/10.1186/ s13059-014-0550-8` (visited on 02/18/2025).

- [201] Mallory A. Ballinger, Katya L. Mack, Sylvia M. Durkin, Eric A. Riddell, and Michael W. Nachman. “Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation”. In: _Proceedings of the National Academy of Sciences_ 120.39 (2023), e2214614120. doi: `10.1073/pnas. 2214614120` . eprint: `https://www.pnas.org/doi/pdf/10.1073/ pnas.2214614120` . url: `https://www.pnas.org/doi/abs/10.1073/ pnas.2214614120` .

131

- [202] Sarah A. Signor and Sergey V. Nuzhdin. “The Evolution of Gene Expression in cis and trans”. In: _Trends in Genetics_ 34.7 (July 2018), pp. 532–544. doi: `10.1016/j.tig.2018.03.007` . url: `https://doi.org/10.1016/j. tig.2018.03.007` .

- [203] Kaitlyn Bloom, Anuradha Karunanidhi, Kimimasa Tobita, Charles Hoppel, Edda Thiels, Eloise Peet, Yudong Wang, Shrabani Basu, and Jerry Vockley. “ACAD10 protein expression and Neurobehavioral assessment of Acad10deficient mice”. In: _PLOS ONE_ 15.12 (Dec. 2020), e0242445. doi: `10. 1371/journal.pone.0242445` . url: `https://doi.org/10.1371/ journal.pone.0242445` .

- [204] Madoka Inuzuka, Minako Hayakawa, and Tatsuya Ingi. “Serinc, an activityregulated protein family, incorporates serine into membrane lipid synthesis”. In: _Journal of Biological Chemistry_ 280.42 (Oct. 2005), pp. 35776–35783. issn: 0021-9258. doi: `10.1074/jbc.M505712200` . url: `https://doi. org/10.1074/jbc.M505712200` .

- [205] João Henrique Tadini Marilhano Fabri, Nivea Pereira de Sá, Iran Malavazi, and Maurizio Del Poeta. “The dynamics and role of sphingolipids in eukaryotic organisms upon thermal adaptation”. In: _Progress in Lipid Research_ 80 (Nov. 2020), p. 101063. issn: 0163-7827. doi: `10.1016/j.plipres. 2020.101063` . url: `https://doi.org/10.1016/j.plipres.2020. 101063` .

- [206] G. M. Jenkins. “The emerging role for sphingolipids in the eukaryotic heat shock response”. In: _Cellular and Molecular Life Sciences_ 60.4 (Apr. 2003), pp. 701–710. issn: 1420-682X. doi: `10.1007/s00018-003-2239-0` . url: `https://doi.org/10.1007/s00018-003-2239-0` .

- [207] Tadashi Nomura, Kohjiro Nagao, Ryo Shirai, Hitoshi Gotoh, Masato Umeda, and Katsuhiko Ono. “Temperature sensitivity of Notch signaling underlies species-specific developmental plasticity and robustness in amniote brains”. In: _Nature Communications_ 13.1 (Jan. 2022), p. 96. doi: `10.1038/s41467021-27815-z` . url: `https://doi.org/10.1038/s41467-021-27815z` .

- [208] Kenneth A Barr, Katherine L Rhodes, and Yoav Gilad. “The relationship between regulatory changes in cis and trans and the evolution of gene expression in humans and chimpanzees”. In: _Genome Biology_ 24.1 (2023), p. 207.

- [209] Gyu-Tae Shin, Ji Eun Park, and Min-Jeong Lee. “MAGEH1 interacts with GADD45G and induces renal tubular cell apoptosis”. In: _PLOS ONE_ 16.11 (Nov. 2021), e0260135. doi: `10.1371/journal.pone.0260135` . url: `https://doi.org/10.1371/journal.pone.0260135` .

132

- [210] Anna K. Lee and Patrick Ryan Potts. “A Comprehensive Guide to the MAGE Family of Ubiquitin Ligases”. In: _Journal of Molecular Biology_ 429.8 (Apr. 2017), pp. 1114–1142. doi: `10.1016/j.jmb.2017.03.005` . url: `https: //doi.org/10.1016/j.jmb.2017.03.005` .

- [211] Amika Kikuchi, Hiroki Onoda, Kosuke Yamaguchi, Satomi Kori, Shun Matsuzawa, Yoshie Chiba, Shota Tanimoto, Sae Yoshimi, Hiroki Sato, Atsushi Yamagata, Mikako Shirouzu, Naruhiko Adachi, Jafar Sharif, Haruhiko Koseki, Atsuya Nishiyama, Makoto Nakanishi, Pierre-Antoine Defossez, and Kyohei Arita. “Structural basis for activation of DNMT1”. In: _Nature Communications_ 13 (Nov. 2022), p. 7130. doi: `10.1038/s41467-02234779-4` . url: `https://doi.org/10.1038/s41467-022-34779-4` .

- [212] Gennady Gorin, John J Vastola, and Lior Pachter. “Studying stochastic systems biology of the cell with single-cell genomics data”. In: _Cell Systems_ 14.10 (2023), pp. 822–843.

- [213] Ibai Irastorza-Azcarate, Alexander Kukalev, Rieke Kempfer, Christoph J Thieme, Guido Mastrobuoni, Julia Markowski, Gesa Loof, Thomas M Sparks, Emily Brookes, Kedar Nath Natarajan, et al. “Extensive folding variability between homologous chromosomes in mammalian cells”. In: _bioRxiv_ (2024), pp. 2024–05.

- [214] Zhenzhen Ma, Alexander Lorenzo Starr, David Gokhman, and Hunter Fraser. “The causes and consequences of human-specific DNA methylation”. In: _bioRxiv_ (2026), pp. 2026–01.

- [215] Ryan Weber, Maria Carilli, Elisabeth Rebboah, Ghassan Filimban, Heidi Yahan Liang, Diane Trout, Margaret Duffield, Parvin Mahdipoor, Erisa Taghizadeh, Negar Fattahi, Negar Mojgani, Romina Mojaverzargar, Shimako Kawauchi, Brian A. Williams, Grant R. MacGregor, Barbara J. Wold, Lior Pachter, Ingileif B. Hallgrimsdottir, and Ali Mortazavi. “Hybrid crosses reveal a cell-type-specific landscape of mouse regulatory variation”. In: _bioRxiv_ (2026). doi: `10.64898/2026.04.02.716195` .

- [216] Elissa J. Chesler, Darla R. Miller, Lisa R. Branstetter, Leslie D. Galloway, Barbara L. Jackson, Vivek M. Philip, Brynn H. Voy, Cymbeline T. Culiat, David W. Threadgill, Robert W. Williams, Gary A. Churchill, Dabney K. Johnson, and Kenneth F. Manly. “The Collaborative Cross at Oak Ridge National Laboratory: developing a powerful resource for systems genetics”. In: _Mammalian Genome_ 19.6 (2008), pp. 382–389. doi: `10.1007/s00335008-9135-8` .

- [217] David W. Threadgill, Darla R. Miller, Gary A. Churchill, and Fernando Pardo-Manuel de Villena. “The Collaborative Cross: A Recombinant Inbred Mouse Population for the Systems Genetic Era”. In: _ILAR Journal_ 52.1 (2011), pp. 24–31. issn: 1084-2020. doi: `10.1093/ilar.52.1.24` .

133

- [218] Elisabeth Rebboah, Ryan Weber, Elnaz Abdollahzadeh, Nikhila Swarna, Delaney K. Sullivan, Diane Trout, Fairlie Reese, Heidi Yahan Liang, Ghassan Filimban, Parvin Mahdipoor, Margaret Duffield, Romina Mojaverzargar, Erisa Taghizadeh, Negar Fattahi, Negar Mojgani, Haoran Zhang, Rebekah K. Loving, Maria Carilli, A. Sina Booeshaghi, Shimako Kawauchi, Ingileif B. Hallgrímsdóttir, Brian A. Williams, Grant R. MacGregor, Lior Pachter, Barbara J. Wold, and Ali Mortazavi. “Systematic cell-type resolved transcriptomes of 8 tissues in 8 lab and wild-derived mouse strains capture global and local expression variation”. In: _Cell Genomics_ (Dec. 31, 2025), p. 101108. doi: `10.1016/j.xgen.2025.101108` .

- [219] Patricia J Wittkopp, Belinda K Haerum, and Andrew G Clark. “Regulatory changes underlying expression differences within and between Drosophila species”. In: _Nature genetics_ 40.3 (2008), pp. 346–350.

- [220] Thomas M. Keane, Leo Goodstadt, Petr Danecek, Michael A. White, Kim Wong, Binnaz Yalcin, Andreas Heger, Avigail Agam, Guy Slater, Martin Goodson, Nicholas A. Furlotte, Eleazar Eskin, Christoffer Nellåker, Helen Whitley, James Cleak, Deborah Janowitz, Polinka Hernandez-Pliego, Andrew Edwards, T. Grant Belgard, Peter L. Oliver, Rebecca E. McIntyre, Amarjit Bhomra, Jérôme Nicod, Xiangchao Gan, Wei Yuan, Louise Van Der Weyden, Charles A. Steward, Sendu Bala, Jim Stalker, Richard Mott, Richard Durbin, Ian J. Jackson, Anne Czechanski, José Afonso GuerraAssunção, Leah Rae Donahue, Laura G. Reinholdt, Bret A. Payseur, Chris P. Ponting, Ewan Birney, Jonathan Flint, and David J. Adams. “Mouse genomic variation and its effect on phenotypes and gene regulation”. In: _Nature_ 477.7364 (Sept. 2011), pp. 289–294. issn: 0028-0836. doi: `10.1038/ nature10413` .

- [221] Anton J. M. Larsson, Per Johnsson, Michael Hagemann-Jensen, Leonard Hartmanis, Omid R. Faridani, Björn Reinius, Asa Segerstolpe, Chloe M. Rivera, Bing Ren, and Rickard Sandberg. “Genomic encoding of transcriptional burst kinetics”. en. In: _Nature_ 565.7738 (Jan. 2019), pp. 251–254. issn: 0028-0836, 1476-4687. doi: `10.1038/s41586-018-0836-1` . url: `http://www.nature.com/articles/s41586-018-0836-1` (visited on 06/07/2019).

- [222] J. M. Müller, K. Moos, T. Baar, K. C. Maier, K. Zumer, and A. Tresch. “Nuclear export is a limiting factor in eukaryotic mRNA metabolism”. In: _PLoS Computational Biology_ 20.5 (2024), e1012059. doi: `10.1371/journal. pcbi.1012059` .

- [223] Nikhila P. Swarna, A. Sina Booeshaghi, Elisabeth Rebboah, M. Grace Gordon, Pooja Kathail, Taibo Li, Marcus Alvarez, Chun Jimmie Ye, Barbara Wold, Ali Mortazavi, and Lior Pachter. “Determining gene specificity from multivariate single-cell RNA sequencing data”. In: _bioRxiv_ (2025). Preprint, not peer reviewed. doi: `10.1101/2025.11.21.689845` .

134

- [224] Giorgia Benegiamo, Giacomo V. G. von Alvensleben, Sandra RodríguezLópez, Ludger J. E. Goeminne, Alexis M. Bachmann, Jean-David Morel, Ellen Broeckx, Jing Ying Ma, Vinicius Carreira, Sameh A. Youssef, Nabil Azhar, Dermot F. Reilly, Katharine D’Aquino, Shannon Mullican, Maroun Bou-Sleiman, and Johan Auwerx. “The genetic background shapes the susceptibility to mitochondrial dysfunction and NASH progression”. In: _Journal of Experimental Medicine_ 220.4 (2023), e20221738. doi: `10.1084/ jem.20221738` .

- [225] Sarah Greve, Gisela A. Kuhn, Mara D. Saenz-de-Juano, Adhideb Ghosh, Ferdinand von Meyenn, and Katrin Giller. “The major urinary protein gene cluster knockout mouse as a novel model for translational metabolism research”. In: _Scientific Reports_ 12 (Aug. 2022), p. 13161. doi: `10.1038/s41598022-17385-5` .

- [226] TakashiMiwa,MitsuroKanda, DaiShimizu,ShinichiUmeda,KoichiSawaki, Haruyoshi Tanaka, Chie Tanaka, Norifumi Hattori, Masamichi Hayashi, Suguru Yamada, Goro Nakayama, Masahiko Koike, and Yasuhiro Kodera. “Hepatic metastasis of gastric cancer is associated with enhanced expression of ethanolamine kinase 2 via the p53–Bcl-2 intrinsic apoptosis pathway”. In: _British Journal of Cancer_ 124.8 (2021), pp. 1449–1460. doi: `10.1038/s41416-021-01271-7` .

- [227] George R. Uhl and Maria J. Martinez. “PTPRD: neurobiology, genetics, and initial pharmacology of a pleiotropic contributor to brain phenotypes”. In: _Annals of the New York Academy of Sciences_ 1451.1 (2019), pp. 112–129. doi: `10.1111/nyas.14002` .

- [228] Hideaki Tomita, Francisca Cornejo, Begoña Aranda-Pino, Cameron L. Woodard, Constanza C. Rioseco, Benjamin G. Neel, Alejandra R. Alvarez, David R. Kaplan, Freda D. Miller, and Gonzalo I. Cancino. “The Protein Tyrosine Phosphatase Receptor Delta Regulates Developmental Neurogenesis”. In: _Cell Reports_ 30.1 (Jan. 2020), 215–228.e5. doi: `10.1016/j. celrep.2019.12.020` .

- [229] Ayako Imai, Hironori Izumi, Nagomi Ito, and Tomoyuki Yoshida. “Alternative microexon splicing code for a four-amino acid peptide of PTPRD governs behavioral development”. In: _Proceedings of the National Academy of Sciences_ 123.15 (Apr. 2026), e2515310123. doi: `10 . 1073 / pnas . 2515310123` .

- [230] Seoyeong Kim, Jae Jin Shin, Muwon Kang, Yeji Yang, Yi Sul Cho, Hyojung Paik, Jimin Kim, Yunho Yi, Suho Lee, Hei Yeun Koo, Jinwoong Bok, Yong Chul Bae, Jin Young Kim, and Eunjoon Kim. “Alternatively spliced miniexon B in PTP _𝛿_ regulates excitatory synapses through cell-type-specific trans-synaptic PTP _𝛿_ -IL1RAP interaction”. In: _Nature Communications_ 16 (2025), p. 4415. doi: `10.1038/s41467-025-59685-3` .

135

- [231] Bastián I. Cortés, Rodrigo C. Meza, Carlos Ancatén-González, Nicolás M. Ardiles, María-Ingacia Aránguiz, Hideaki Tomita, David R. Kaplan, Francisca Cornejo, Alexia Nunez-Parra, Pablo R. Moya, Andrés E. Chávez, and Gonzalo I. Cancino. “Loss of protein tyrosine phosphatase receptor delta PTPRD increases the number of cortical neurons, impairs synaptic function and induces autistic-like behaviors in adult mice”. In: _Biological Research_ 57 (2024), p. 40. doi: `10.1186/s40659-024-00522-0` .

- [232] Sheryl S. Moy, Jessica J. Nadler, Nancy B. Young, Randal J. Nonneman, Samantha K. Segall, Gabriela M. Andrade, Jacqueline N. Crawley, and Terry R. Magnuson. “Social Approach and Repetitive Behavior in Eleven Inbred Mouse Strains”. In: _Behavioural Brain Research_ 191.1 (2008), pp. 118–129. doi: `10.1016/j.bbr.2008.03.015` .

- [233] Yichen Ge, Fuguo Wu, Mobin Cheng, Jonathan Bard, and Xiuqian Mu. “Two new genetically modified mouse alleles labeling distinct phases of retinal ganglion cell development by fluorescent proteins”. In: _Developmental Dynamics_ 249.12 (2020), pp. 1514–1528. doi: `10.1002/dvdy.233` .

- [234] MV Prasad Linga Reddy, H Wang, S Liu, B Bode, JC Reed, RD Steed, SW Anderson, L Steed, D Hopkins, and J-X She. “Association between type 1 diabetes and GWAS SNPs in the southeast US Caucasian population”. In: _Genes and Immunity_ 12.3 (Apr. 2011), pp. 208–212. doi: `10.1038/gene. 2010.70` . url: `https://doi.org/10.1038/gene.2010.70` .

- [235] H.C. Martins, A.Ö. Sungur, C. Gilardi, M. Pelzl, S. Bicker, F. Gross, J. Winterer, T.M. Kisko, N. Malikowska-Racia, M.D. Braun, K. Brosch, I. Nenadic, F. Stein, S. Meinert, R.K.W Schwarting, U. Dannlowski, T. Kircher, M. Wöhr, and G. Schratt. _Bipolar-associated miR-499-5p controls neuroplasticity by downregulating the Cav1.2 L-type voltage gated calcium channel subunit CACNB2_ . en. Preprint. bioRxiv: 2021.06.09.447782, June 2021. url: `http://biorxiv.org/lookup/doi/10.1101/2021.06.09.447782` (visited on 06/04/2022).

- [236] John William Strutt Baron Rayleigh. _The theory of sound_ . Vol. 2. Macmillan, 1896.

- [237] Eleni P. Mimitou and Peter Smibert. _Expanding the CITE-seq tool-kit: Detection of proteins, transcriptomes, clonotypes and CRISPR perturbations with multiplexing, in a single assay_ . en. Mar. 2019. url: `https://www. ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE126310` (visited on 08/22/2019).

- [238] Yang Wang, Jingyu Li, Andrew A. Malcolm, William Mansfield, Stephen J. Clark, Ricard Argelaguet, Laura Biggins, Richard J. Acton, Simon Andrews, Wolf Reik, Gavin Kelsey, and Peter J. Rugg-Gunn. “Combinatorial profiling of multiple histone modifications and transcriptome in single cells using scMTR-seq”. In: _Science Advances_ 11.32 (2025). doi: `10.1126/sciadv. adu3308` .

136

- [239] Chris J. Frangieh, Johannes C. Melms, Pratiksha I. Thakore, Kathryn R. Geiger-Schuller, Patricia Ho, Adrienne M. Luoma, Brian Cleary, Livnat Jerby-Arnon, Shruti Malu, Michael S. Cuoco, Maryann Zhao, Casey R. Ager, Meri Rogava, Lila Hovey, Asaf Rotem, Chantale Bernatchez, Kai W. Wucherpfennig, Bruce E. Johnson, Orit Rozenblatt-Rosen, Dirk Schadendorf,AvivRegev, andBenjaminIzar.“Multimodal pooled Perturb-CITE-seq screens in patient models define mechanisms of cancer immune evasion”. In: _Nature Genetics_ 53 (2021), pp. 332–341. doi: `10.1038/s41588-02100779-1` .

- [240] Atray Dixit, Oren Parnas, Biyu Li, Jenny Chen, Charles P. Fulco, Livnat Jerby-Arnon, Nemanja D. Marjanovic, Danielle Dionne, Tyler Burks, Raktima Raychowdhury, Britt Adamson, Thomas M. Norman, Eric S. Lander, Jonathan S. Weissman, Nir Friedman, and Aviv Regev. “Perturb-Seq: Dissecting Molecular Circuits with Scalable Single-Cell RNA Profiling of Pooled Genetic Screens”. In: _Cell_ 167.7 (Dec. 2016), 1853–1866.e17. doi: `10.1016/j.cell.2016.11.038` .

- [241] Catherine Felce, Gennady Gorin, and Lior Pachter. _A Biophysical Model for ATAC-seq Data Analysis_ . en. Tech. rep. bioRxiv: 2024.01.25.577262, Jan. 2024. url: `http://biorxiv.org/lookup/doi/10.1101/2024.01. 25.577262` (visited on 07/19/2024).

- [242] Catherine Felce, Meichen Fang, and Lior Pachter. “Joint Biophysical Modeling of Paired Single-Cell RNA and Protein Measurements”. In: _bioRxiv_ (2025). Preprint, not peer reviewed. doi: `10.1101/2025.11.14.688548` .

- [243] Francesco Mottes, Qian-Ze Zhu, and Michael P. Brenner. “Gradient-based optimization of exact stochastic kinetic models”. In: _arXiv_ (2026). Preprint. arXiv: `2601.14183 [physics.comp-ph]` .

- [244] Charlotte Bunne, Yusuf Roohani, Yanay Rosen, Ankit Gupta, Xikun Zhang, Marcel Roed, Theo Alexandrov, Mohammed AlQuraishi, Patricia Brennan, Daniel B. Burkhardt, Andrea Califano, Jonah Cool, Abby F. Dernburg, Kirsty Ewing, Emily B. Fox, Matthias Haury, Amy E. Herr, Eric Horvitz, Patrick D. Hsu, Viren Jain, Gregory R. Johnson, Thomas Kalil, David R. Kelley, Shana O. Kelley, Anna Kreshuk, Tim Mitchison, Stephani Otte, Jay Shendure, Nicholas J. Sofroniew, Fabian Theis, Christina V. Theodoris, Srigokul Upadhyayula, Marc Valer, Bo Wang, Eric Xing, Serena YeungLevy, Marinka Zitnik, Theofanis Karaletsos, Aviv Regev, Emma Lundberg, Jure Leskovec, and Stephen R. Quake. “How to build the virtual cell with artificial intelligence: Priorities and opportunities”. In: _Cell_ 187.25 (Dec. 2024), pp. 7045–7063. doi: `10.1016/j.cell.2024.10.032` .

---

[← REGULATION OF BIOPHYSICAL PROCESSES IN FOUNDER MOUSE STRAINS](12-regulation-of-biophysical-processes-in-founder-mouse-strains.md) · [Up: contents](index.md)
