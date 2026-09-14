---
title: 'PART I: INTRODUCTION'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf
source_file: sources/statomics-sga21/docs/backgroundProteomicsDataAnalysis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PART I: INTRODUCTION

**Source:** [`docs/backgroundProteomicsDataAnalysis.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/backgroundProteomicsDataAnalysis.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1

2

During the five years of my PhD, I thoroughly investigated different statistical approaches to quantify proteins in label-free mass spectrometry (MS)-based shotgun proteomics. Furthermore, I developed MSqRob, an R package with graphical user interface for the statistically sound analysis of label-free proteomics data. Since I have worked on the interface of protein biology and statistics, it is important to understand both the biological and the statistical aspects of my work.

Hence, in order to place my work in its proper context, this introduction is divided into four chapters. The first chapter aims to give an overview of the biology of proteins and the wide variety of applications of present-day mass spectrometry-based proteomics. In the second chapter, I will describe the technical context of bottom-up quantitative proteomics: the different quantification strategies and the specific peculiarities of the label-free proteomics workflow. In chapter three, I will explain how the spectra are processed into interpretable data. Finally, chapter four will give an overview of how this data can be used to quantify proteins.

3

4

## **1. BIOLOGICAL CONTEXT**

Chapter 1 mainly aims at introducing proteomics to data analysists who are new to the field. In this chapter, I will first cover the very basics of protein biology (section 1.1). Then, I will give an overview of a generalized mass spectrometry-based proteomics workflow and the relationship of proteomics to other omics (section 1.2), followed by a more profound review of the possibilities of mass spectrometry-based proteomics in present-day life sciences research (section 1.3).

### **1.1. Proteins as the central effectors of life**

Before discussing the need for proteomics, I will first introduce the biology of proteins. Proteins are an extremely diverse class of biomolecules that are essential for nearly all functions of life. In this section, I will give an overview of the molecular structure of proteins and how their structures are linked to the essential roles proteins play in health and disease.

#### **1.1.1. The molecular structure and origin of proteins**

Proteins are composed of amino acids and the general chemical structure of an amino acid and a protein is given in Fig. 1.1.


**Figure 1.1.** Chemical structures of a proteinogenic<sup>1</sup> amino acid (A) and a protein (B). All amino acids share the same base structure. They all contain an α -amino group (-NH2) and an α -carboxyl group (- COOH) along with a rest group/side-chain (R). The part of the protein ending with the amino group is called the amino- or N-terminus, while the side ending in the carboxyl group is called the carboxyl- or C- terminus. Amino acids differ only in their rest group. In proteins, amino acids are joined together by peptide bonds (-CO-NH-, indicated in red).

> 1 Proteinogenic amino acids are amino acids that are translationally incorporated into proteins. All proteinogenic amino acids, except glycine, have an L-stereoisomeric configuration. This means that, when the amino acid is oriented from its N-terminus to its C-terminus as in (A), the rest group (R) will be in front of the plane while the hydrogen atom (H) will be behind the plane. Glycine has no chiral center because its rest group is a hydrogen atom, so the central carbon (α -carbon) is only linked to three different atoms.

5

There are only 20 different standard amino acids<sup>2</sup> that can be incorporated in proteins. The actual sequence by which amino acids are joined together is encoded by the corresponding gene found in the genomic DNA (deoxyribonucleic acid). Indeed, in all living organisms, genes are transcribed to RNA (ribonucleic acid) molecules. RNA molecules are composed of only four different nucleotide building blocks holding the nucleobases guanine (G), uracil (U), adenine (A) or cytosine (C). In eukaryotic<sup>3</sup> cells, protein-coding RNA, or messenger RNA (mRNA), is then transported from the nucleus (where the grand majority of the DNA resides) to the cytoplasm, where it can be translated into proteins by ribosomes (Fig. 1.2). This unidirectional transfer of information takes place in every living organism: from DNA to mRNA to proteins and has come to be known as the central dogma of molecular biology. Even though some viruses violate this dogma by directly replicating RNA using an RNA template<sup>4</sup> , or even generate DNA based on an RNA template<sup>5</sup> , the translation of mRNA to proteins remains a one-way process. RNA is however not always translated into protein. Indeed, RNA itself can have regulatory functions (e.g. micro RNA (miRNA) and long non-coding lncNRA<sup>6</sup> can induce gene silencing [7, 8]), structural functions (e.g. ribosomal rNA (rRNA) is an important component of the ribosome [9]) and even catalytic functions (e.g. peptidyl transfer by rRNA, mRNA splicing, self-splicing [10, 11]).


**Figure 1.2.** The grand majority of transcription occurs in the nucleus of a eukaryotic cell by a protein (or rather, enzyme) called RNA polymerase. Translation occurs in the cytoplasm where ribosomes, specialized cellular structures that are composed of ribosomal RNA and proteins, translate the mRNA into proteins. Both transcription and translation occur from the 5’ to the 3’ end of the oligonucleotides . 5’

> 2 There are two additional very rare non-standard amino acids that are translationally incorporated into proteins. Selenocysteine (Sec, U) is present in all domains of life [1], while pyrrolysine (Pyl, O) is only present in 9 methanogenic _Archaea_ of the _Methanosarcina_ family and 15 _Bacteria_ [2]. Both amino acids are present in only a few dozens of proteins.

> 3 Eukaryotes are cells that, unlike _Bacteria_ and _Archaea_ , have a nucleus. All multicellular organisms (e.g. humans) are eukaryotic, though some eukaryotes are also unicellular.

> 4 RNA viruses such as rhinoviruses (the most common causes of the common cold) and hepatitis C virus use a protein called RNA-dependent RNA polymerase to make new copies of their RNA genomes.

> 5 HIV uses the protein reverse transcriptase to convert its RNA genome into DNA and subsequently integrates this DNA into its host’s genome.

> 6 Note that some short open reading frames in long “non - coding” RNA were shown to generate very small proteins [3-6].

6

and 3’ refer to the conventional chemical names of the carbon atoms in the (deoxy)ribose rings. Proteins are always synthesized from their N- to their C-termini.

Transcription and translation are also unidirectional in space: they always occur from the 5’ to the 3’ terminus of the DNA and mRNA molecules respectively. Each group of three consecutive nucleotides (triplet) in the mRNA represents a codon and each codon represents one unique amino acid or encodes a stop codon. A general overview of the codons that translate into each of the 20 amino acids or are used as stop codons is given in Fig. 1.3. This genetic code is near-universal across the whole tree of life. Some minor exceptions include: yeasts from the CTG clade encode CUG partially or completely as serine instead of leucine [12] and UGA is sometimes translated into tryptophan or arginine instead of being used as a stop codon for some transcripts and some species [13, 14]. Note that all codons, except those for methionine and tryptophan, are redundant: e.g. UUA, UUG, CUU, CUC, CUA and CUG all code for leucine. This property is also called the “degeneracy” of the genetic code.


**Figure 1.3.** The genetic code. The four mRNA ribonucleosides are guanosine (G), uridine (U), adenosine (A), and cytidine (C). The 20 amino acids are phenylalanine (Phe, F), leucine (Leu, L), isoleucine (Ile, I), methionine (Met, M), valine (Val, V), serine (Ser, S), proline (Pro, P), threonine (Thr, T), alanine (Ala, A), tyrosine (Tyr, Y), histidine (His, H), glutamine (Gln, Q), asparagine (Asn, N), lysine (Lys, K), aspartic acid (Asp, D), glutamic acid (Glu, E), cysteine (Cys, C), tryptophan (Trp, W), arginine (Arg, R) and glycine (Gly, G). Note that each amino acid has both a three-letter abbreviation and a oneletter abbreviation. The AUG codon is the most common start codon and also codes for methionine. Hence, all nascent eukaryotic proteins start with a methionine at their N-terminus when being synthesized<sup>7</sup> . The three different stop codons (UAA, UAG and UGA) signal translation termination.

However, knowing the mRNA sequence sometimes does not suffice to predict the protein sequence. Indeed, in all domains of life, besides AUG, which is used in more than 80% of the

> 7 In _Bacteria_ , the start codon codes for N-formylmethionine, but this formyl group is cotranslationally removed [15]. In all domains of life, the N-terminal methionine is often cleaved off, causing more than 50% of the proteins not to have a methionine at the N-terminus [16-18].

7

cases, other codons are also used as start codons [19]. Such so-called near-cognate start codons include CUG, GUG, UUG, ACG, AUC, AUU, AAG, AUA and AGG [20]. In the bacterium _Escherichia coli_ for example, up to 40 out of the 64 codons can be used as start codons, albeit in less than 0.1% of the cases [21]. Such alternative start codons also encode for methionine or N-formylmethionine (in the case of bacteria). If translation is initiated from a downstream<sup>8</sup> (near-cognate or canonical) start codon, a shorter protein is produced from the same mRNA template. Similarly, when translation is initiated from an upstream start codon, a longer protein is produced. More rarely, a stop codon can be replaced with another amino acid in a process called translational read-through [22].

Further, in both prokaryotes and eukaryotes, certain “slippery” mRNA sequences, such as AAAAAA, might, under certain circumstances, cause a frameshift, which means that translation continues in another reading frame [23] (Fig. 1.4).


**Figure 1.4.** Example of a translational frameshift in the dnaX gene of the bacterium Escherichia coli. The dnaX gene encodes both the τ and the γ subunit of the DNA polymerase III protein. dnaX contains a slippery AAAAAA sequence (blue, italics). When the ribosome passes normally over this sequence (top), translation remains in frame and the τ subunit is produced. However, when the ribosome “slips” (bottom), a -1 frameshift occurs. Hereby, a premature stop codon (red, bold) is introduced resulting in the production of t he shorter γ subunit. In the dnaX example, ribosome slipping is stimulated by the presence of a downstream stem loop structure in the mRNA that stalls the ribosome. An upstream Shine-Dalgarno like sequence helps repositioning the ribosome in its new reading frame. Example adapted from Dinman (2006) [24].

This ribosomal frameshift is rather rare in most organisms, but very common amongst viruses as it allows them to translate many proteins from a small genome that is limited by the size of the viral particles [24]. Similarly, slippage can already occur at the level of transcription, when the RNA polymerase introduces a variable number of nucleotides in long homopolymeric stretches [25]. Further, it is now also known that amino acids in bacterial proteins can be converted into their D- stereoisomeric form and recent work demonstrates that even a protein’s backbone can be changed by introducing an α -keto- β -amino acid [26, 27].

Besides these rather infrequent phenomena discussed above, alternative RNA splicing is very common as more than 95% of all mammalian genes express alternatively spliced transcripts [28]. Splicing involves the removal of certain parts of an RNA molecule and, dependent on which parts are being spliced out from an mRNA molecule, different protein products can be

> 8 Downstream means “in the 3’ direction”, upstream is “in the 5’ direction”.

8

generated. Similarly, certain protein sequences, called inteins, are able to post-translationally cut themselves out of a protein [29]. Moreover, proteins are known to carry, often transiently, a plethora of modifications (see also 1.1.3).

Because of these phenomena, many chemically different protein molecules can result from a single gene hence, the term “proteof or m” was coined. Proteoforms are defined as “ _Highly related protein molecules arising from all combinatorial sources of variation giving rise to products arising from a single gene. These include products differing due to genetic variations, alternatively spliced RNA transcripts, and post-translational modifications_ ” [30].

The side-chain of an amino acid determines its physicochemical properties. The nature of a protein will thus not only be determined by the amino acids it contains, but also by the sequence in which they are connected to each other. The specific chemical structures for selected amino acids are given in Fig. 1.5.


**Figure 1.5.** Examples of the diversity in chemical structures of amino acids: the structures of 6 different amino acids are given. The side-chains of lysine and arginine are long aliphatic chains that are positively charged at physiological pH<sup>9</sup> . Aspartic acid has a net negative charge at this pH. Tyrosine is a very bulky amino acid that is rather hydrophobic due to the benzene ring in its structure. It is however rather polar due to its hydroxyl (-OH) group. Glycine is the smallest amino acid and the only one that lacks a chiral center as its side-chain itself is a hydrogen atom.

#### **1.1.2. Protein folding**

Proteins arrange themselves into three dimensional structures. They are rather flexible, and it is mainly their sequence of amino acids that determines their final 3D structure. The complex interplay of the different chemical properties of the different amino acids will determine a protein ’s thermodynamically most favorable 3D conformation. Known physicochemical forces that play a role in protein folding include the hydrophobic effect<sup>10</sup> , H-bridges, n→π*

> 9 The average pH inside a cell, which is approximately 7.4 and thus close to the neutral pH 7.

> 10 Since water is a polar solvent, apolar molecules do not mix well with water. Hence, apolar amino acid residues will often be found on the inside of a folded protein chain, away from the water that surrounds it. This property is called hydrophobicity (“being afraid of water”).

9

interactions, van der Waals forces, formation of disulfide bridges, the gain of conformational entropy of water on protein folding and electrostatic interactions [31]. Hydrophilic, polar amino acids will mainly be found on the surface of a folded protein, while hydrophobic, apolar amino acids will typically be present on the inside. So-called chaperones are proteins that often aid nascent proteins during the folding process<sup>11</sup> to avoid aberrant folding [33]. Sometimes, multiple proteins cluster together to form a functional protein complex (Fig. 1.6).


**Figure 1.6.** Three-dimensional structure of the protein hemoglobin. Hemoglobin consists of four folded protein s (two α subunits, red, and two β subunits, blue) that are held together by hydrogen bonds. Each subunit is folded such that it creates a pocket that strongly binds an iron-containing heme group (green). Image by Richard Wheeler (Zephyris) at the English language Wikipedia, CC BY-SA 3.0, <u>https://commons.wikimedia.org/w/index.php?curid=2300973.</u>

#### **1.1.3. The JAK-STAT pathway as an example of a protein network**

Cells are highly dynamic and thousands of biochemical processes are continuously going on in each cell. Proteins play a crucial role in nearly every one of these processes. The enormous diversity in 3D structures that are adopted by different proteins allows them to bind to other biomolecules with very high specificity. This in turn leads to an immense variety in protein functions. Well-known functions of proteins include, but are definitely not limited to, enzymatic reactions (e.g. trypsin, which digests other proteins in the stomach; kinases, proteins which add a phosphate group to protein substrates), DNA synthesis (DNA polymerases), DNA transcription (RNA polymerases, aided by different sorts of transcription factors), cellular structure (e.g. microtubules), muscle contraction (e.g. actin, myosin) and oxygen transport (hemoglobin).

Therefore, proteins interact both with each other and with other biomolecules. Indeed, most changes inside the cell are triggered by cascades of both stable and transient protein-protein interactions, termed signaling pathways. The JAK-STAT pathway is just one of many intracellular pathways and constitutes a classic example of how a cell responds to a stimulus coming from its environment (Fig. 1.7). JAK-STAT signaling actually is a simple signaling

> 11 Note that some chaperones also work after translation. Some chaperones aid in stabilizing protein structures in response to a cellular stressor, others aid in protein unfolding or revert protein aggregation [32].

10

cascade and, in reality, such cascades are highly branched, as most proteins have multiple interaction partners.


**Figure 1.7.** Simplified view of the JAK-STAT pathway. Certain events in the human body can trigger the release of small proteins, called cytokines, in the blood. Some cells are programmed to respond to these cytokines and are therefore equipped with specific cytokine receptors. After binding to an extracellular cytokine, the cytokine receptors dimerize, bringing the JAK kinases in close proximity of each other. The JAKs will subsequently phosphorylate each other on a Tyr residue. The phosphorylated JAKs will then phosphorylate a Tyr residue on the cytoplasmic side of the cytokine receptors. This allows docking of STAT proteins. These STAT proteins will also be phosphorylated by the JAKs. Phosphorylated STATs will dimerize and translocate to the nucleus, where they allow transcription of mRNA molecules encoding for proteins that are needed for the response to the stimulus. Modified after Peter Znamenkiy [Public domain], from Wikimedia Commons.

The JAK-STAT example involves phosphorylation as an illustration of a chemical group that is transferred by a protein (a kinase such as JAK) to another protein (a substrate, here the cytokine receptor, STAT, or JAK itself). In this example, phosphorylation on tyrosines occurs, though it can also occur on serine and threonine residues (as both contain a free hydroxyl (- OH) group) and on the nitrogen atoms of the imidazole ring in histidine residues [34, 35]. Phosphorylation on arginine, lysine, aspartate and glutamate are also known to occur, but are very labile in an acid environment and were therefore proven difficult to study by means of mass spectrometry [36, 37]. Recent work published on BioRxiv proposes a workflow at nearphysiological pH that allows the identification of thousands of such non-canonical phosphorylation sites [38]. Moreover, next to phosphorylation, many more co- and posttranslational modifications exist, and it is not uncommon for proteins to carry modifications across different residues. These modifications are not only important in signaling cascades, but can also affect protein stability and degradation, alter enzymatic activity and target proteins to membranes [39]. Many diseases (e.g. infectious diseases, auto-immune diseases, neurodegenerative diseases, …) have been linked to aberrant protein modification states [4043]. A comprehensive overview of all possible protein modifications can be found in the UniMod database at: http://www.unimod.org/modifications_list.php [44].

#### **1.1.4. Proteins in diseases**

The extremely complex web of interactions of proteins with each other and with other biomolecules makes that disruption of a single protein’s function often has severe outcomes [45]. Genetic diseases are often the result of a loss-of-function caused by the production of truncated or abnormally folded proteins. For instance, thalassemias are a family of genetic diseases in which an abnormal form of hemoglobin is produced that is less efficient in taking

11

up oxygen [46]. These diseases are caused by one or more mutations in the coding genes that lead to changes in hemoglobin’s amino acid sequence. Such changes can cause substitutions of one amino acid by another but can also result in shorter or longer proteins when stop codons are respectively introduced or erased. They might also impact on mRNA splicing. Large gene deletions or insertions and even fusions with other genes have been reported to cause thalassemia [47]. Such mutations inhibit the production of one or more hemoglobin chains or result in the production of abnormally folded hemoglobin. Mutations can also cause diseases by interfering with the normal modification status of a protein. For example, the severe but rare disease mandibuloacral dysplasia is caused by a single mutation in the gene encoding for the protease ZMPSTE24, which results in the accumulation of toxic farnesylated prelamin A (Fig. 1.8).


**Figure 1.8.** Left: overview of the maturation of the protein lamin A in healthy individuals. Normally, a hydrophobic farnesyl group is added to lamin A during its preprocessing. Lamin A’s C -terminal end containing the modification is then cleaved off by the ZMPSTE24 protease (here shown as a pair of scissors). Right: in mandibuloacral dysplasia a homozygous mutation<sup>12</sup> in the _ZMPSTE24_ gene causes loss-of-function, which results in the accumulation of toxic farnesylated prelamin A.

Conversely, for many diseases, genetics alone cannot fully explain disease onset. Late-onset Alzheimer’s disease, for instance, has no single genetic cause<sup>13</sup> . At the protein level, it is characterized by the aggregation of the amyloid- β protein in the brain. Other incurable brain diseases, like Creutzfeldt-Jakob, are caused by a prion, an incorrectly folded protein that causes other proteins of the same kind to take over its aberrant shape, leading to some sort of a chain reaction and massive accumulation of misfolded proteins [50].

> 12 Humans, like all mammals, have two copies of most genes [48]. ZMPSTE24 loss-of-function only occurs when both copies are affected.

> 13 Many different genes influence susceptibility, and the overall genetic heritability is estimated between 60 and 80% [49].

12

#### **1.1.5. Applications of protein research**

Proteins are so abundantly being applied throughout our daily lives, that it is nearly impossible to give a complete overview of all their applications. Moreover, researchers continuously strive to improve and broaden protein applications.

In the medical field, proteins are used for diagnosis and disease monitoring. Examples of such biomarkers in blood and plasma approved by the US Federal Drug Administration (FDA) include HE4 for ovarian cancer, CA19-9 for pancreatic cancer and thyroglobulin for thyroid cancer, amongst many others [51], and researchers keep on developing novel biomarker assays.

Determining the 3D structure of proteins is pivotal to their characterization. Indeed, not only do these models allow the prediction of a protein ’s interactions with other proteins [52], they also aid in drug development. Nowadays, companies rationally design potential drug candidates by fitting them e.g. onto a protein’s docking site [53, 54]. However, determining a protein’s structure is a non-trivial task. Indeed, although the sequence of a protein will in the end determine its 3D structure, no algorithm exists that can accurately predict 3D structures solely based on amino acid sequences. X-ray crystallography and nuclear-magnetic resonance (NMR) are the most commonly used techniques to determine protein structures, although cryoelectron microscopy is also becoming a viable option [55]. Alternatively, proteins with more than 30% sequence homology are often assumed to have a similar structure [56]. Indeed, such proteins often show an evolutionary relationship and therefore hold a similar structure and function.

Proteins can also be used as therapeutics, with monoclonal antibodies forming the largest class of therapeutic proteins (48% of all FDA approvals in 2011 – 2016) [57]. Examples include antibodies against IL-5 for the treatment of asthma [58], anti-CD319 against relapsed multiple myeloma [59] and anti-VEGFR2 against gastric cancer [60]. New artificial (“recombinant”) proteins can also be produced by modifying the DNA sequence of existing proteins. Examples include ocriplasmin against vitreomacular adhesion [61], glucarpidase against kidney failure [62] and recombinant von Willebrand factor against von Willebrand disease [63]. Proteins are also extensively used in basic biomedical research. Examples include green fluorescent protein (GFP) and its derivatives to visualize proteins inside a cell [64] and the use of CrisprCas9 to examine the function of genes by knocking them out or inducing targeted mutations [65].

However, the study of proteins is not only relevant for human diseases. Enzymes, proteins that catalyze biochemical reactions<sup>14</sup> , are used in sectors as diverse as the pharmaceutical sector, the food industry, paper production, detergent manufacturing and biofuel production [67]. For the production of pharmaceuticals, enzymes aid in the production of precursors or in chemically modifying the final compounds to increase their stability and/or bioavailability [68]. In the food industry, α -amylase is used to convert starch into sugars [69], pectinase to clarify fruit juices [70] and lactase to produce lactose-free milk [71], amongst many others. In the paper industry, xylanase is used to loosen the structure of cellulose fibers, which improves paper quality [72]. Proteases, amylases and lipases are used in laundry detergents to help break down stains of biological origin [73]. Lipases are used in biofuel production to convert free fatty acids to methyl/ethyl esters [74].

> 14 This acceleration often goes up to several trillions of orders of magnitude [66], allowing reactions that would naturally take millions of years to occur almost instantly. Previously mentioned proteins such as JAK and ZMPSTE24 are also enzymes: JAK catalyzes a phosphorylation reaction, ZMPSTE24 cleaves a peptide bond.

13

Finally, proteins are also extensively investigated in food crop research. The most well-known example is research on transgenic plants. Here, a DNA sequence coding for a protein with favorable properties is introduced into a commercial crop. This protein can for example promote crop yield or convey resistance against insects, pathogens or herbicides. A notorious example is the development of “golden rice”, a genetically engineered rice variant developed to combat vitamin A deficiency [75]. Indeed, per gram dry weight, the seeds of golden rice contain up to 37 μg β -carotene, a compound that is converted into vitamin A by the human body [76]. Although the rice genome can produce all enzymes needed for β -carotene production, four of these enzymes are not expressed in rice seeds. In golden rice, only two genes are introduced: the _psy_ gene from maize, to produce the enzyme phytoene synthase and the _crtI_ gene from the bacterium _Erwinia uredovora_ to produce the enzyme carotene desaturase. Together, these enzymes restore the β -carotene pathway in the seeds, which results in a rice plant with the typical yellow seeds. Thanks to this simple genetic modification, golden rice holds the promise to save a substantial fraction of the 250,000 to 500,000 children that become blind every year due to vitamin A deficiency, half of which die within a year [7780]. This is especially the case in Asian countries, where rice is a dominant portion of the standard diet.

Understanding how proteins interact with each other increases our understanding of a plant’s developmental pathways, which allows the breeding of high-yield variants as well as variants that produce stable yields under stress [81]. Indeed, various biotic and abiotic stresses can delay or even terminate plant growth, and even a relatively small, transient stress can markedly reduce crop yield [82]. Hence, researchers actively investigate protein networks involved in stress responses to explain why certain varieties are less stress-sensitive [83, 84]. This knowledge can then later be used for crop improvement through cross-breeding or genetic modification. The lab of my co-promoter is, amongst others, involved in research into protein signaling pathways during the germination of parasitic plants. This is expected to spur the development of germination inhibitors for these plagues [85].

### **1.2. The nature of mass spectrometry-based proteomics**

Researchers need to obtain information about the proteome to understand and act upon all these protein-related processes. Proteomics is the study of the proteome and today, MS-based proteomics is the most important proteomic technology. Here, I start by giving a very brief overview of the general principles of chromatography and MS, followed by a discussion of MSbased proteomics workflows. Then, I will situate the proteomics field with respect to the other omics fields.

#### **1.2.1. General principles of liquid chromatography and mass spectrometry**

Like every other analytical technique, mass spectrometry has its limitations on the complexity it can efficiently cope with, both in terms of the number of distinct analytes and in terms of differences in the concentrations between these analytes. Separating analytes prior to further analysis is thus essential for reaching sufficient analytical depth. For MS-driven proteomics, the analytes – which are mainly peptides – are present in solution. Hence, liquid chromatography is the method-of-choice for separating peptides prior to analysis by means of mass spectrometry. In liquid chromatographic applications for proteomics, the peptides are first loaded onto a column (also called the stationary phase) in a buffered solution (also called the mobile phase). The composition of the column is such that most (if not all) of the peptides interact with and are thus withheld by this column. By now changing the composition of this mobile phase, the column-bound peptides will start to partition in the mobile phase and are thus eluted from the column at a given composition of this mobile phase. Liquid

14

chromatography can be used to separate peptides based on different physical characteristics such as size, charge and hydrophobicity. Separating peptides based on differences in hydrophobicity is the preferred chromatographic method that is linked to mass spectrometers. In the overall majority of applications, a hydrophobic stationary phase (e.g., chromatographic beads functionalized with C18-groups) is used to bind peptides via hydrophobic interactions. Here, the buffer used to load the peptides is an aqueous buffer. By now gradually increasing the concentration of a water-miscible organic solvent, peptides will start to favor being present in the increasingly organic mobile phase and elute from the stationary phase.

To further analyze the eluted peptides, these peptides need first to be brought into the gas phase and need to get ionized. This process happens in the ionization part of a mass spectrometer. “Soft” ionization techniques, i.e. ionization techniques that transfer little residual energy onto the ions and therefore cause only minimal ion fragmentation have been extremely important for the measurement of intact ions. Indeed, John B. Fenn and Koichi Tanaka were awarded the 2002 Nobel Prize in Chemistry for the development of electrospray ionization (ESI) and soft laser desorption (SLD), respectively. Next to an ionization part, a mass spectrometer also consists of at least one analyzer and at least one detector.

Different types of analyzers have been developed to separate and detect ions based on their mass-to-charge ( _m_ / _z_ ) ratio. In a time-of-flight (TOF) mass spectrometer, ions are accelerated by a fixed electric field into a vacuum tube. The time it takes for an ion to travel (or fly) through this tube and reach a detector depends on its mass and its charge. Indeed, given the formula of kinetic energy, the higher the mass of an ion, the lower its velocity and thus the later this ion will hit the detector. Conversely, the higher the charge of an ion, the higher its velocity and thus the faster it will hit the detector. The intensity of the signal recorded by this detector is used as a proxy for the initial abundance of the recorded peptide. These signals are recorded at discrete _m_ / _z_ -values at GHz resolution.

A quadrupole mass analyzer is an example of a more complex analyzer that works as an _m_ / _z_ filter. Quadrupoles consist of four rods, which have an alternating radio frequency voltage with an offset direct current. The frequency voltage and the offset can be tuned in such a way that only ions with a specific _m_ / _z_ value follow a stable trajectory throughout the quadrupole, while all other ions are pushed out (Fig. 1.9). When the quadrupole is used to scan a beam of ions over a certain _m_ / _z_ range, a mass spectrum is recorded.


**Figure 1.9.** Working principle of a quadrupole. The rods have an alternating radio frequency voltage with a direct current offset. Due to inertia, ions with very high _m_ / _z_ values will be relatively unaffected by the alternating current but will be pushed out of the quadrupole by the non-zero direct current offset. Contrary, ions with very low _m_ / _z_ values will be pushed out of the quadrupole as they are strongly affected

15

by the alternating current. By carefully tuning the alternating and direct currents, a quadrupole works as a very specific ion filter. Figure based on Vékey _et al._ (2008) [86].

#### **1.2.2. The MS-based proteomics workflow**

Mass spectrometry-based proteomics is the method of choice for the high-throughput identification and quantification of peptides and proteins in a single analysis. Fig. 1.10 gives a general overview that encompasses the most frequently occurring steps in MS-based proteomics workflows.


**Figure 1.10.** General overview of an MS-based proteomics workflow. The workflow starts with samples (a) from which proteins (b) are extracted. These proteins can e.g. be labeled and are, for most applications, digested into smaller fragments called peptides (c). The proteins/peptides are separated onto a high-performance liquid chromatography (HPLC) column and ionized (d). Then, an MS spectrum (e) is recorded. Some ions can be fragmented into smaller ions (f) after which the resulting spectrum is recorded (MS² spectrum, g). Some of these fragments can again be targeted for fragmentation (h), after which an MS³ spectrum can be recorded (i). Note that the presence or absence of some steps in this workflow depend on the type of analysis that is performed.

Every MS-based proteomics workflow starts with one or more samples. The types of samples can vary widely, ranging from plant material over animal tissues, plasma samples, cell cultures or recombinantly produced proteins. If the sample is not a solution of (purified) proteins, the proteins will need to be extracted first. The techniques used for extraction and purification depend on the sample type. For mammalian cell cultures, for example, a rather simple lysis buffer will suffice [87]. For organisms with thick cell walls or for membrane proteins, (additional) mechanical disruption, e.g. sonication with glass or metal beads, might be necessary [88]. Techniques like ultracentrifugation or ammonium sulfate precipitation are then used to separate the proteome from other unwanted cellular components (e.g. DNA, RNA, lipids) and possible detergents that were used to disrupt cells. Solubilized intact proteins can be directly analyzed by MS (top-down proteomics) [89], but complex protein mixtures are generally enzymatically digested into smaller fragments, termed peptides, for so-called bottom-up proteomics or shotgun proteomics<sup>15</sup> .

> 15 Note that the term “bottom - up proteomics” refers to any LC -MS proteomics technique that uses prior digestion of proteins to peptides, while the term “shotgun proteomics” specifically refers to LC -MS proteomics techniques whereby complex protein mixtures are digested into peptides.

16

Peptides have the advantage that they are more chemically tractable, more easily separated by liquid chromatography and more easily ionized and fragmented as compared to intact proteins [90-92]. To limit the number of possible peptides in bottom-up proteomics to a reasonable computational search space, the commonly-used protease is highly specific. Trypsin, for instance, is ideally suited, as it cleaves with high specificity after lysine and arginine residues.

Alternative enzymes (e.g. pepsin, chymotrypsin, and the endoproteinases LysC, LysN, AspN, GluC and ArgC) have also been used, as they generate different sets of peptides and therefore revea l complementary parts of a proteome’s sequence space [93-99]. Parallel digestion of the same proteome with multiple proteases can also give a strong boost to the coverage of modification sites [100, 101]. Alternative proteases with more infrequent cleavage specificities will generate longer peptides that can be studied with middle-down proteomics [92, 102, 103]. Nonetheless, trypsin remains the dominant digestion enzyme in bottom-up proteomics. On November 2014, more than 96% of all raw files deposited in the PRIDE repository were using trypsin [102] and there is little reason to assume this percentage has drastically changed today.

To facilitate proteolytic digestion, proteins are often first denatured with urea, which disrupts a protein’s hydrogen bonds causing the protein to denature and unfold. This results in a destruction of protein-protein interactions and a solubilization of hydrophobic lipid-bilayer bound proteins. Urea has the advantage that it can easily be removed by reverse-phase chromatography [104]. However, adding too much urea might also partially denature the protease and hence reduce the digestion efficiency. Further, at higher temperatures, urea partially decomposes into isocyanic acid which carbamylates primary amine groups and thus introduces artefactual amino acid modifications that also block enzymatic digestion [105, 106]. Note that detergents such as sodium dodecyl sulphate (SDS) that are commonly used to lyse cells or to denature proteins prior to polyacrylamide gel electrophoresis (SDS-PAGE), should generally be avoided as they are incompatible with liquid chromatography (LC)-MS [91]. Indeed, even though small amounts of SDS facilitate enzymatic digestion, this detergent suppresses ion signals even at very low concentrations (< 0.01%). SDS cannot be removed with a reverse-phase high-performance liquid chromatography (HPLC) separation step [106109], although the recently-introduced suspension trapping filter S-Trap<sup>TM</sup> includes a washing step that makes it compatible with SDS denaturation [110]. Nevertheless, most digestion protocols omit the use of denaturants [111]. Other contaminants may also adversely affect the analysis [112]. It is therefore strongly advised to discuss all preprocessing protocols with proteomics specialists prior to the experiment.

If one is interested in only a subpart of the proteome, additional purification of certain proteins or peptides, e.g. by immunoprecipitation might be needed. Similarly, many protein modifications are transient, have low occupancies, are chemically unstable during standard sample preparation procedures and/or decrease a peptide’s ionization efficiency [113-116]. Therefore, detecting specific modifications requires optimized enrichment protocols [117].

Proteins or peptides are sometimes labeled to facilitate identification and quantification (see section 2.1). These labels can either be small chemical groups or heavy isotopes. They can either be incorporated during the growth of the organism (metabolic labeling, see 2.1.1) or after protein extraction (post-metabolic labeling, see 2.1.2).

Sample pre-fractionation is an option when samples are very complicated and enough protein material is available [118]. Pre-fractionation can be done with a method that is orthogonal to the standard reverse-phase liquid chromatograph that is coupled to the mass spectrometer. Strong cation exchange (SCX) chromatography is a popular pre-fractionation strategy [119]. Although the complexity of each fraction will be reduced, separation is never perfect and many

17

proteins will be present in more than one fraction, which may complicate protein quantification [120]. Each of these samples (or fractions in the case of pre-fractionation) is subsequently analyzed by the mass spectrometer. If the samples are very simple (e.g. a single protein), the proteins/peptides can be directly analyzed by matrix-assisted laser desorption (MALDI) ionization coupled to a time-of-flight mass spectrometer, by which a mass spectrum for the entire sample is obtained [121]. If the samples are more complex, the proteins/peptides are first separated onto a reverse phase liquid chromatography column that is coupled to the mass spectrometer. Upon elution, the proteins/peptides are ionized, typically with electrospray ionization (ESI) [122]. Traditionally, positively charged ions are generated, while neutral molecules and negatively charged ions are filtered out [123]. At discrete time points, the mass spectrometer will measure the mass-to-charge ratios for all the ion species eluting from the column. In the commonly used Orbitrap analyzer, this is achieved by trapping the ions in an orbital motion around a spindle-like electrode, hence the name. The ions are moved back and forth and the fluctuations in charge caused by the movement of the ions are recorded by a detector. This wavelet signal is subsequently converted into a mass spectrum by Fourier transformation. The resulting spectrum is termed an MS or MS<sup>1</sup> spectrum. It is important to note that due to the natural occurrence of heavy isotopes of all chemical elements in a fixed ratio, every ion species generates multiple isotopic peaks in the MS spectrum, resulting in a so-called isotopic envelope. Each ion’s charge state is then calculated from the _m_ / _z_ -distance between the peaks in such an isotopic envelope. The summed-up intensities of all ions in an MS spectrum is called the total ion current (TIC). The evolution of the TIC over time is used as a measure of quality control.

In most workflows, an MS spectrum will be insufficient to identify the ion species. Therefore, a single peak in the isotopic envelope of the ions of interest will be selected by the mass spectrometer and targeted for fragmentation. Typically, high intensity peaks are targeted for fragmentation to avoid selecting noise, which would lead to significant losses in operating time. To avoid sequential fragmentations of the same ion during its elution, all previously targeted _m_ / _z_ values are often excluded from being targeted again for a certain amount of time (e.g. 20 seconds). This setting is termed dynamic exclusion and substantially increases the coverage of the mass spectrometer by freeing MS time for the targeting and fragmentation of less intense MS peaks [124].

In shotgun proteomics, collision-induced dissociation (CID) [125] or higher-energy collisional dissociation (HCD) [126] are by far the most common fragmentation methods, while electrontransfer dissociation (ETD) gains popularity for phosphoproteome studies (see 1.3.2) [127, 128]. Negative electron-transfer dissociation (NETD) [123] and photo-dissociation [129-132] are examples of infrequently used fragmentation methods. With CID, ions are collided with noble gasses such as helium and argon that increase the ions’ internal vibrational energy and eventually lead to fragmentation [133]. With HCD fragmentation, the collision energies are higher than 1 keV [134]. Collision therefore occurs in a separate collision cell, typically with a heavier gas, such as dinitrogen [135]. If the peptide’s backbone is fragmented, six types of ions (a, b, c, x, y and z) can be formed, as shown in Fig. 1.11. The mass spectrum of the fragment ions is termed an MS/MS or MS² spectrum.

18


**Figure 1.11.** Left: overview of the different types of ions that can be formed after fragmentation of a peptide ion’s backbone. a -, b- and c-ions are formed if the charge is retained on the N-terminal peptide fragment. Conversely, x- y- and z- ions are formed if the charge is retained on the C-terminal fragment. Breaking the peptide bond (red) is by far the most energetically favorable fragmentation pattern. Therefore, b- and y-ions will be the most abundant ion species in every MS² spectrum generated by CID or HCD. n is the total number of amino acids in the protein. Modified after Steen and Mann (2004) [136]. Right: example fragmentation pattern for the peptide LDGER. b-ions are indicated in purple, y-ions are indicated in blue. Fragments LDG and ER have the same average mass and therefore form a single peak in the MS² spectrum.

With CID and HCD, b- and y-ions will be far more intense than the other types of ions (a-, c-, x- and z-ions) [137]. For tryptic peptides, CID fragmentation generates both b- and y-ions, while y-ions are much more prominent with HCD fragmentation [137-139].

When the intensities of certain fragment ions are to be used for quantification, MS² fragment ions can optionally be isolated and subjected to mass spectrometry (MS³ spectrum) to prevent interference of other fragment ions with the intensity of the fragment ion of interest. Such MS³ workflows are mainly useful for isobaric labeling (see 2.1.2). Identification of an ion species is typically achieved by searching the fragment ion spectra against a database (see section 3.1).

Note that MS instrumentation is evolving extremely rapidly. Only a few years ago, 20 MS² spectra per second was considered state-of-the-art [140], but the most recent machines now exceed a scanning speed of over 40 spectra per second [141]. This implies that if one MS spectrum is recorded per second, more than 40 peaks in this MS spectrum can be fragmented and thus potentially identified.

#### **1.2.3. Proteomics in relation to other omics**

Many omics techniques can provide some information about the state of the proteome, but proteomics is the most suited for this purpose. The fields of genomics, epigenomics, transcriptomics and ribosome profiling largely rely on the analysis of DNA and RNA molecules. RNA can easily be reverse transcribed to DNA and even a single molecule can be readily amplified to billions of copies with a routine polymerase chain reaction (PCR). Moreover, advanced techniques have been devised to sequence and characterize even single RNA and DNA molecules. These possibilities are currently lacking for other types of biomolecules, including proteins. Present-day proteomics relies heavily on mass spectrometry and with the ever-increasing resolutions and operating speeds of contemporary mass spectrometers, the proteomics field has evolved rapidly over the past few years [142, 143]. Other mass spectrometry-based omics fields, such as lipidomics and glycomics, are considered to be still in their infancies.

19

Since the completion of the Human Genome Project, we have an adequate view on most of the protein-coding genes<sup>16</sup> and the genomes of more and more organisms are almost routinely being added to the ever expanding genome databases [145-149]. However, the genome only provides a view on which proteins can potentially be expressed. Indeed, a retina cell is very different from a muscle cell, despite sharing the same genomes. Similarly, a caterpillar is very different from a butterfly because they both activate different genetic programs. Thus, the genome alone provides little information about the current proteomic state of a cell.

Epigenomics is the study of the modifications (e.g. methylation, acetylation) of the DNA and its associated proteins (histones amongst others) [150]. These chemical markers change the chromatin’s structure and dictate the accessibility of each gene for the transcription machinery. Within the same species, different cell types have different epigenetic patterns. However, epigenomics only provides an overview of how easily genes can be accessed, but it does not provide answers to how much of each proteoform is actually being produced.

Transcriptomics is a routine technique to quantify the amounts of (m)RNA molecules derived from each gene [151]. It can therefore be used as a rough estimate for protein production. However, a substantial amount of mRNA is not translated and there is a variety of mechanisms that modulate protein synthesis at the translation step<sup>17</sup> . The ribosome profiling technique provides a quantitative snapshot of which mRNA is getting translated. Therefore, ribosome profiling provides a much better estimate of protein translation than mRNA sequencing [153].

Metabolomics and lipidomics, the large-scale analyses of metabolites and lipids respectively, can elucidate complex metabolic processes related to health and disease [154]. Metabolic conversions are not only catalyzed by enzymes, but also closely regulated by various protein signaling cascades. Therefore, metabolomics and lipidomics can provide additional indirect information on the state of the proteome [155].

However, none of these omics’ techniques are able to determine which proteoforms will be produced, nor can they provide any information about protein degradation, the other side of the balance that governs protein steady-state. They are also not well-suited to assess protein localization and are unable to provide information ab out a protein’s interaction partners. T he only technique that is able to assess with high-throughput the properties of a protein within a proteome is MS-based proteomics.

### **1.3. Applications of mass spectrometry-based proteomics**

MS-based proteomics is the preferred method for solving numerous biological questions from the “proteome angle”. Identifying and later also quantifying proteins were and are still the main initial applications of MS-based proteomics. Over the last decade, the application of proteomics for the identification and quantification of protein modifications has also gained significant attention. The proteomics field has also been expanded to study amongst others, proteinprotein interactions [156-159], protein-compound interactions [160-163], cellular protein localization [164-167] and protein structure determination [89, 160, 168-173]. However, the identification and quantification of proteins remains the most important application of MSbased proteomics and many of these applications rely on the quantitative ability of the mass spectrometer. Since my thesis focuses on protein quantification, I will elaborate here on protein quantification and the quantification of protein modifications.

> 16 Although the detection of many small “hidden” proteins remai ns challenging [144].

> 17 These include, amongst others, RNA splicing, reading frame shifts, translational read-through, sequestration of mRNA and mRNA degradation [152].

20

#### **1.3.1. The analysis of protein and peptide abundance**

After a peptide or protein is identified, quantification is the next logical step. Typically, peptides from different biological conditions are labeled either isotopically or chemically in order to induce a mass shift in the MS, MS² or MS³ spectrum. Alternatively, if labeling is omitted (labelfree proteomics), mass spectra from different runs should be compared. The peak intensities are a proxy for peptide (and hence a protein) abundance. The peak intensities registered during the elution of a peptide therefore allow for protein quantification in each biological condition. Alternatively, quantification can be done by the less accurate, but simpler spectral or peptide counting. Relating intensities to protein concentrations is challenging because peptides can have very different ionization efficiencies, which are difficult to predict. Nonetheless, there were some attempts at absolute protein quantification [174, 175]. Since the analysis of protein abundance is the focus of my work, I have kept this section intentionally brief since more details about quantitative proteomics are given in chapters 2-4.

#### **1.3.2. The analysis of protein modifications**

Both bottom-up and top-down proteomics can be employed to study protein modifications as these cause shifts in the masses of affected peptides that can readily be detected.

As mentioned earlier under 1.1.3, proteins can carry a plethora of modifications. Most of these modifications occur too infrequently to be detected or prove to be very chemically labile. Other modifications, such as the frequently occurring, but often labile phosphorylation, are also difficult to detect because of the poor ionization of the phosphoryl group, which carries a negative charge. Therefore, when the main research goal is to study a certain protein modification, specific enrichment procedures are often required [117].

Phosphorylation is both the most common and the most intensively studied protein modification [176]. Indeed, phosphorylation is a key modification in many signaling cascades and phosphoproteomics has contributed enormously to our understanding of these pathways [177-179]. However, the negative charge of the phosphoryl group and the default usage of positive electrospray ionization makes it difficult to generate and therefore detect positivelycharged phosphorpeptides. Thus, phosphopeptides are enriched via pre-fractionation with hydrophilic interaction liquid chromatography (HILIC), Strong cation exchange (SCX) chromatography or strong anion exchange (SAX) chromatography, as well as immunoprecipitation, immobilized metal affinity chromatography (IMAC), metal-oxide affinity chromatography (MOAC), Phos-Tag chromatography, polymer-based metal ion affinity capture (PolyMAC), hydroxyapatite chromatography, enrichment by chemical modification, and/or phosphopeptide precipitation [180]. Negative electron-transfer dissociation (NETD) can also increase the MS intensities of phosphopeptides [123].

Acetylation and methylation are modifications that were first discovered on histones, proteins that are associated with the DNA and package it into structural units called nucleosomes [181, 182]. Histone acetylation is generally associated with open chromatin [183], while histone methylation, dependent on the location of the methylation site, can both be associated with open and closed chromatin [184]. Acetylation can occur both on protein N-termini and on lysine residues [183], while methylation can also occur on arginine residues [184].

Acetylation is important for protein localization [185-188], protein folding [189], protein stability [190] and interactions with other proteins [191]. Methylation is a major factor in important cell signaling pathways such as JAK-STAT, MAPK, WNT, Hippo and BMP [192] and overall protein methylation seems to be strongly intertwined with the organism’s metabolic state [193].

21

Again, enrichment procedures by e.g. (immuno)affinity purification or chromatography are preferable when assessing acetylation or methylation on a proteome-wide scale [194-196].

Glycosylation is another very important post-translational protein modification as over 50% of all mammalian proteins are glycosylated [197]<sup>18</sup> . Glycosylation plays an important role in protein structure and stability [199-201]. The presence of a glycan structure can block other modifications such as phosphorylation [202]. Glycan structures can be sensed by other proteins (leptins) and play an important role in e.g. cancer and immunity [203, 204]. They are also intensively studied in the context of therapeutic proteins, as many of these proteins carry glycan structures [200, 205]. The enormous complexity of many glycan structures has spurred the development of a new field called glyco(proteo)mics [206].

Ubiquitin is a small 8.6 kDa protein that can be covalently linked to lysine residues of other proteins. However, non-canonical ubiquitination can also occur at Ser, Thr and Cys residues and at a protein’s N -terminal amine group [207]. The earliest known function of K48-linked<sup>19</sup> polyubiquitination is the degradation of the modified proteins in the proteasome. This discovery resulted in the 2004 Nobel Prize in Chemistry for Avram Hershko, Aaron Ciechanover, and Irwin A. Rose [208]. Although K11-linked polyubiquitination can also result in proteasomal degradation [209], ubiquitin is also an important scaffold that allows recruitment of other proteins and plays an important role in cellular processes as diverse as e.g. protein trafficking, mitophagy and cell cycle control. Next to K48 and K11; K6, K27, K29, K33 and K63 linkages have also been described. Many proteins are mono-ubiquitinated, but ubiquitin chains can also be linear and branched and even combined with other small ubiquitin-like modifiers such as SUMO and NEDD-8 [210].

Detection of ubiquitination by MS is challenging because ubiquitin is often either quickly degraded by the proteasome or part of very dynamic signaling pathways [211]. Moreover, ubiquitin is much bigger than most other small modifications. Being a protein, ubiquitin is also degraded by trypsin, leaving only a small GG or LRGG tag behind [212, 213]. Finally, ubiquitination does not seem to occur on well-defined amino acid sequence motifs [214-216]. Nonetheless, protocols for proteome-wide detection of ubiquitination are now readily available thanks to innovative purification and chemical tagging strategies [211, 217]. Similarly, protocols have also been developed for the proteomic analysis of other less characterized small ubiquitin-like modifiers like SUMO [218, 219], NEDD-8 [220, 221] and ISG [222, 223].

> 18 Note that not only proteins, but also lipids can be glycosylated [198].

> 19 K48-linkage means that each ubiquitin in the chain is linked to the previous ubiquitin via the lysine (K) residue at position 48 (starting from the N-terminus).

22

## **2. TECHNICAL CONTEXT**

As amply demonstrated in the previous chapter, mass spectrometry-based proteomics has become an invaluable tool for protein researchers. In chapter 2, I will discuss the different flavors of mass spectrometry-based proteomics with a focus on their technicalities. I will specifically emphasize label-free shotgun proteomics, as all my PhD work revolves around this particular technique. This technical overview will provide a handle for chapter 3, where I will link the statistical challenges to the technology.

### **2.1. Label-based mass spectrometry-based proteomics**

Traditionally, quantitative proteomics has made use of stable-isotope coded labels. This used to be a necessity, as the peptides that were identified often differed strongly between LCMS/MS runs. Indeed, even minor differences in electrospray voltages and/or chromatographic flow rates increase the run-to-run variability in signal intensities and hence reduce the precision of label-free quantification [224, 225]. By metabolically labeling proteins from different samples and subsequently pooling these together for a single analysis, it became possible to identify the peptides in each sample analyzed and remove the inter-sample variability. In fact, one distinguishes two categories of label-based proteomics: metabolic and post-metabolic labeling.

In metabolic labeling, labels are incorporated during cell or organism expansion. By contrast, in post-metabolic labeling, a label is added after protein extraction or even after protein digestion, typically by means of a chemical reaction that targets specific reactive groups in proteins or peptides. The main advantage of metabolic labeling is that the labeled proteins can immediately be pooled together, thus any random or systematic experimental errors that occur after pooling will affect all samples equally [226]. Thereby, this unwanted variability can be factored out from the analysis, which increases the overall precision. Post-metabolic labeling, by contrast, does not affect the biology of the organism under study (see below), as labeling only occurs after protein extraction. And, although post-metabolic labeling requires more protein material, it is more broadly applicable [227]. Fig. 2.1 gives an overview of the experimental stages in which labels are introduced and samples are mixed for different labeling protocols.

23


**Figure 2.1.** Schematic overview of the labeling workflow for two experimental conditions (blue and yellow). Horizontal lines indicate when samples are combined, dashed lines indicate the protocol steps where experimental variation unequally affects both samples. Reprinted with permission from Bantscheff _et al._ (2012) [228], copyright © 2012, Springer-Verlag.

#### **2.1.1. Metabolic labeling**

In metabolic labeling, a cell culture or even an entire organism is expanded in a medium that contains nutrients composed of heavy isotopes. Metabolic incorporation of radioactive isotopes was first used to quantify proteins in gels [229], whereas<sup>15</sup> N labeling was the first MS-based quantitative proteomics approach [230]. Here, cells were grown in a medium with nutrients containing the stable<sup>15</sup> N isotope, which allows this isotope to be incorporated into the biomolecules of the cell. The heavy-labeled proteins have higher masses compared to proteins from cells expanded in a medium containing the natural<sup>14</sup> N isotope. This results in a mass shift for each peptide that is detected in the mass spectra.<sup>15</sup> N labeling is thus well-suited to compare the levels of all identified proteins between two conditions: one grown in normal (“light” or “unlabeled”) medium and the other in heavy medium. Indeed, peptides originating from digesting both proteomes are pooled and analyzed by mass spectrometry. The intensities of the<sup>14</sup> N and<sup>15</sup> N peptides are compared to infer differences in protein abundances. This approach assumes that cellular metabolism remains unaffected by the heavy isotopes. Nonetheless, several studies indicate that there might be biological effects of heavy isotopes given differential preferences of enzymes for certain isotopes [231-234]. To guard against statistical confounding due to these kinetic isotopic effects and unavoidable differences in quality<sup>20</sup> between the light- and the heavy-labeled medium, the heavy and light conditions are routinely swapped in experimental repeats.<sup>15</sup> N labeling w as originally used to quantify baker’s yeast ( _Saccharomyces cerevisiae_ ) proteins and was later also applied on bacterial and mammalian cell cultures [235], and even on whole organisms [236-238].

> 20 E.g. small deviations from the stated isotopic content might bias quantifications. Also, since the heavy and light media are stored in separate bottles, there might be small differences in biological effects since fetal bovine serum, an essential serum supplement for most cell cultures, is often added separately to each bottle. Moreover, the quality of both media might also diverge over time.

24

Incomplete labeling is a major disadvantage of all metabolic labeling strategies. Indeed, natural medium still contains a non-negligible albeit very low amount of heavy isotopes (e.g., 1%<sup>13</sup> C and 0.4%<sup>15</sup> N ) [239]. Similarly, medium highly enriched in heavy isotopes still contains a fraction of lighter isotopes. As peptides differ in their number of amino acids and different amino acids have different numbers of atoms, isotopic labeling will generate a plethora of different partially unlabeled variants for every peptide analyzed [240]. Therefore, the mass shift of a peptide after labeling depends on its composition, which complicates downstream peptide identification and quantification.

Stable Isotope Labeling by Amino acids in Cell culture (SILAC) is a metabolic labeling approach where amino acids, typically essential amino acids, containing one or more stable heavy isotopes are used for differential protein quantification [241, 242]. The use of amino acids as opposed to isotopically labeled nutrients has greatly simplified data analysis for MSbased protein quantification, and this because the labeled amino acids are incorporated into proteins, implying that a peptide’s mass shift can be directly derived from its amino acid composition. An important point is that the organism in the heavy condition needs to be exposed to the heavy-labeled amino acids for long enough to allow the complete replacement of the organism’s natural (unlabeled) amino acids by the supplied heavy amino acids. For cell cultures, seven doubling times seems to be sufficient to allow full incorporation, even for proteins with very slow turnover rates [240]. By contrasting light (e.g.<sup>12</sup> C6<sup>14</sup> ~~N4-~~ arginine), medium (e.g.<sup>13</sup> C6<sup>14</sup> N4-arginine) and heavy (e.g.<sup>13</sup> C6<sup>15</sup> N4-arginine) SILAC labeling, three different conditions can be directly compared [243]. In 2010, the introduction of 5-plex SILAC allowed the comparison of up to five different conditions in a single MS run [244]. When more than five conditions need to be compared with SILAC, a heavy-labeled standard proteome can be spiked into every condition and be used as a reference to allow calculation of the protein ratios for every comparison (super-SILAC) [245] [246]. SILAC-labeling was initially confined to cell cultures, but over time, it has been expanded to organisms such as the worm _Caenorhabditis elegans_ [247], the fruit fly _Drosophila melanogaster_ [248], mice [249] and plants [250]. Fig. 2.2 gives an overview of a typical SILAC workflow.


**Figure 2.2.** Overview of a SILAC workflow where three experimental conditions need to be compared. The proteomes from the light, medium-labeled and heavy-labeled conditions can be pooled together and analyzed in a single MS run. The intensity ratios of the triplets for each peptide ion species can then

25

be directly calculated from its corresponding MS spectrum. Reprinted with permission from Geiger _et al._ (2011) [251], copyright © 2011, Springer-Verlag.

Also, the isotopic purity of the SILAC medium is of utmost importance. When the fraction of “ heavy ” amino acids is insufficiently high, the hence-labeled proteome contains a substantial fraction of “light” amino acids, leading to quantification biases in the direction of the “light” condition [240]. Further, when using trypsin to digest an arginine-SILAC labeled proteome, a possible caveat is introduced by the metabolic conversion of arginine into proline and glutamate [252], which introduces extra stable isotopes in proline-containing peptides, thereby obstructing accurate quantification. This can be prevented by adding an excess of unlabeled proline [253, 254] and/or by reducing the arginine concentration [255].

SILAC requires dialyzed fetal bovine serum as no other variants of the selected essential amino acids other than the labeled variants must be present in the medium. Dialysis however results in the loss of growth factors, which will cause a cellular stress response that might bias the response to the treatment of interest or even completely prevent cell or organism growth altogether [227, 256].

Despite its main advantage of factoring out run-to-run variability from each comparison, SILAC seems to be slowly getting out of favor for high-throughput protein quantification. The main reason is that the quantification depth (i.e. the number of proteins identified) of SILAC is reported to be ~30 to 60% lower than the quantification depth of label-free quantification (see 2.2.1) [257, 258], although this difference also depends on sample complexity and instrument resolution. Indeed, as multiple SILAC-labeled samples are jointly analyzed in a single MS run, the amount of protein analyzed per experimental condition is two to five (for 5-plex SILAC) times lower, while the number of peaks in each MS spectrum increases with the same factor [258, 259]<sup>21</sup> . In such complex spectra, the peptide ion signals will be lower and might even become indiscernible from the background noise. Also, the more peaks, the higher the chances of co-fragmentation: i.e. two (or more) peptide ions with overlapping isotopic envelopes are fragmented together, increasing the risk of unidentifiable spectra [260]. Moreover, as all isotopic variants of the same peptide can be targeted for identification, less MS peaks might be identified due to limitations on the MS² sampling rate [261]. Another disadvantage of metabolic labeling is that its dynamic range is generally smaller than those of label-free and isobaric quantification approaches (see 2.1.2 and 2.2.1) [262-265]. Also, isobaric labeling appears to have a higher precision [265].

Recently, neutron-encoded (NeuCode) labeling has been proposed as a promising new metabolic labeling approach that relies on the ability of modern high-resolution MS to distinguish extremely small mass differences (in the orders of mDa) [261, 266]. However, NeuCode did not gain a lot of traction yet because of the extremely high cost of its reagents, which seriously limits its throughput.

#### **2.1.2. Post-metabolic labeling**

In post-metabolic labeling, a different chemical label is added to each sample after protein extraction or digestion. Post-metabolic labeling strategies are often used for large experiments in which many samples need to be compared because of their superior opportunities to simultaneously measure multiple experimental conditions in a single MS run (“multiplexing”) . In the context of high-throughput protein quantification, labels are added after digestion

> 21 The reason is that the total amount of peptides (in µg) that is spiked onto the mass spectrometer is a fixed constraint. Under-spiking will result in low signal intensities and hence low proteome coverage, while over-spiking will result in signal saturation.

26

because this allows labeling of peptides that are buried within a protein’s 3D structure, resulting in a higher peptide coverage.

Dimethylation is one of the oldest post-metabolic labeling strategies, though still widely used as it is easy to multiplex and fairly cheap [267]. Indeed, dimethylation requires relatively cheap reagents such as isotopically labeled formaldehyde and cyanoborohydride [268]. Here, all lysine side chains and peptide N-termini are dimethylated, except if the N-terminus starts with proline, in which case it will be monomethylated [269]. Originally performed in duplex [270], dimethylation was expanded to 3- [271], 4- [272] and 5-plex labeling [273]. By combining dimethylation with SILAC, 6-plex labeling has been achieved [274].  Compared to SILAC, dimethylation has a similar dynamic range and accuracy [265, 275]. Thus, the additional experimental variability introduced by post-metabolic labeling as compared to metabolic labeling seems to be limited in practice. Deuterium was used in the dimethylation approaches described above. However, compared to hydrogen-1, deuterium binds less strongly to the hydrophobic stationary phase due to the lower amplitude of its vibrational frequencies [276]. This results in a chromatographic shift as deuterium-labeled peptides elute somewhat earlier than their hydrogenated counterparts, which increases the uncertainty on the ratios of their peak intensities [277, 278]. Therefore, most contemporary isotopic labeling strategies avoid deuterium and favor e.g.<sup>13</sup> C, which does not induce a noticeable chromatographic shift [279].

18O labeling is an enzymatic post-metabolic labeling approach that was originally used to improve peptide identification [280-282]. Soon after,<sup>18</sup> O labeling also became a tool for protein quantification [283-286]. Here, protein digestion is performed either in normal water or in<sup>18</sup> O- rich water. Two<sup>18</sup> O-atoms are incorporated at the peptides’ C -termini, resulting in 4 Da mass shifts. Nowadays,<sup>18</sup> O labeling is not very common anymore as<sup>18</sup> O incorporation efficiency is variable and the technique cannot be multiplexed [287].

Isobaric labeling relies on mass differences in the fragment ions of isotopologic tags to quantify peptide ions via their MS² spectra. Indeed, the isobaric labels in each condition have the same total nominal mass, but a specific fragment ion, the reporter ion, has different masses for each label. Differentially labeled peptides thus coincide in the MS spectrum, but the reporter ions allow for quantification in the MS² spectrum. iTRAQ [288] and TMT [227] are the most wellknown and frequently used reagents for isobaric labeling (Fig. 2.3).

27


**Figure 2.3.** Left: chemical structures of 4-plex iTRAQ- (top) and 6-plex TMT- (bottom) labeled peptides. In isobaric labeling, peptide mixtures from different conditions are labeled with different isobaric labels that have the same total nominal masses but differ in the distributions of heavy isotopes within their structures (i.e. the isobaric labels are isotopologues of each other). Indeed, the reporter groups of the different isobaric labels all have different nominal masses (due to differential usage of heavy isotopes). This mass difference is balanced out by the balance group to ensure equal total nominal masses. The reporter group is constructed so that it detaches easily during fragmentation. It also has a strong preference to carry the positive charge after fragmentation so that it can be readily detected. Right: the monoisotopic<sup>22</sup> forms of differentially labeled peptide ions with identical amino acid sequences and charges will generate a single peak in the MS spectrum (top, red). However, after fragmentation of the isobaric labels, the mass difference of the reporter fragment ions will allow differential quantification in the MS² spectrum (bottom, red).

The main advantage of isobaric labeling is that it does not increase the complexity of the MS spectra and is therefore highly suitable for multiplexing [289]. Indeed, TMT readily allows 6- plex quantification [290], while iTRAQ goes up to 8-plex [291]. By making use of isotopologues, TMT-labeling has now even reached 11-plex [292, 293]. However, despite the market dominance of iTRAQ and TMT, some recent isobaric labeling alternatives such as DiArt [294] and DiLeu [295] labeling are gaining attention due to their easy synthesis, low cost, labeling efficiency and improved fragmentation efficiency. With DiLeu, up to 12 samples [296] can be compared in a single run. Isobaric labeling has also been combined with SILAC which increases its multiplexing potential even further [297].

However, in isobaric labeling, distortion of the reporter ion intensities in the MS² spectra is a major issue. Furthermore, isotopic impurities in the isobaric labeling reagents lead to isotopic

> 22 The monoisotopic form is the isotopic variant wherein all atoms of a molecule are in their most abundant isotopic form.

28

overlaps in neighboring reporter ion intensities. Prior to data analysis, each reporter ion peak should therefore be corrected for isotopic overlap using correction factors supplied by the reagent manufacturer [298]. Another issue is that co-eluting near-isobaric peptide ions are isolated and co-fragmented with the target peptide ion, skewing the ratios of the reporter ion intensities towards the median value over all proteins, which is usually very close to one<sup>23</sup> . For this reason, this phenomenon is also called ratio compression [298-300].

Several technical solutions have been developed to reduce ratio compression. Gas-phase purification [301] and ion mobility separation [302] remove interfering ion species prior to fragmentation. MS³ prevents co-fragmentation by isolating an MS² peptide fragment ion and fragmenting it again to produce an MS³ spectrum. This additional step massively reduces the chance that the selected fragment ion will again be co-isolated with a fragment ion from another peptide species. As this MS² fragment ion contains all the isobaric labels, the reporter ions in the MS³ spectrum enable more accurate and more reproducible protein quantification [303].

Even with these improvements, around 8% of the MS³ spectra remain affected by cofragmentation [265]. The introduction of synchronous precursor selection MS³ (SPS-MS³), in which multiple MS² fragment ions of a precursor peptide are co-isolated, strongly boosts MS³’s sensitivity [304]. However, despite clear progress, MS³ still requires complex instrumentation and has a slower duty cycle, resulting in a lower identification depth compared to MS² quantification [289]. TMTc and EASI tag are new strategies whereby the complement ions (i.e. peptide fragments that remain attached to the balance group) are quantified in the MS² spectrum [289, 305, 306]. These approaches avoid both the complexities of MS³ and the unwanted ratio compression because they examine the isotopic envelope of a particular labeled MS² peptide ion fragment.

Disadvantages of isobaric labeling include the loss of quantification depth and the poor accuracy for quantifying low-intensity peaks due to the lower signal-to-noise ratio in MS² spectra compared to MS spectra [265, 307]. The former can be partially alleviated by prefractionation. However, this results in longer run times and a more complicated data analysis [308, 309]. MS²-based quantification also implies that only those peptides that are selected for fragmentation can be used for quantification [266]. Hence, for the many proteins that are identified with few peptides, it is difficult to assess the precision on their differential abundance estimates. Finally, iTRAQ and TMT labeling are relatively costly [275].

### **2.2. Label-free mass spectrometry-based proteomics**

My PhD work is centered around the quantification of data-dependent label-free discoverybased shotgun proteomics data. Therefore, I will here give an extensive overview of the labelfree shotgun proteomics workflow.

#### **2.2.1. The label-free proteomics workflow**

An overview of a generalized proteomics workflow has already been given in 1.2.2. In this section, I will focus on the aspects that are specific to label-free proteomics, and more specifically on those aspects that pose challenges to the ensuing data analysis.

A label-free proteomic workflow consists of the following steps: (1) proteins are extracted from the sample, (2) these proteins are digested into peptides, (3) the peptides are separated by reverse phase HPLC (RP-HPLC), (4) eluting peptides are ionized, (5) an MS spectrum is taken, (6) a precursor ion is selected, (7) this precursor ion is fragmented and (8) an MS² spectrum

> 23 The total amounts of peptides loaded and analyzed are usually equal for all samples.

29

of its fragments is taken. Steps 6-8 are typically repeated several times for different precursor ions before a new MS spectrum is recorded. The peak intensity in the MS spectrum is used as a proxy for a peptide ion’s abundance, while its corresponding MS² spectrum is used to identify the precursor. An overview of this procedure for a quadrupole Orbitrap instrument is given in Fig. 2.4.


**Figure 2.4.** Overview of a typical label-free mass-spectrometry-based proteomics workflow on a quadrupole Orbitrap instrument. First, proteins are extracted from a sample. Then, the extracted proteins are digested into peptides, using a protease with a strong cleavage specificity (typically trypsin). This peptide mixture is loaded onto the instrument. A high-performance liquid chromatography column allows separation of the peptides by their hydrophobicity (RP-HPLC). The eluate from the column is ionized by electrospray ionization (ESI). The quadrupole ensures that only positively charged ions pass through. In the Orbitrap, an MS spectrum is taken. Each peak in the spectrum corresponds to a peptide ion. In a next step, the quadrupole will select a peptide ion with a sufficiently high peak in the MS spectrum. This peptide is fragmented and an MS² spectrum of its fragments is taken. This process is repeated for other peptides with high enough MS intensities.

Several of these steps create particular issues that are important to consider when analyzing the data. Table 2.1 presents a non-exhaustive overview of common issues in label-free proteomics workflows that have an important impact on the ensuing data. In what follows, I will elaborate on the most important issues of each data analysis step.

30

**Table 2.1.** Non-exhaustive list of issues that arise during a label-free shotgun proteomics workflow and their impact on the data.

|**Analysis step**|**Issues**|**Consequences**|
|---|---|---|
|Protein extraction|Differences<br>in<br>extraction<br>efficiencies|Variable protein concentrations<br>over different samples|
|Protein digestion|Unequal enzymatic cleavage<br>efficiencies,<br>non-canonical<br>cleavage, peptide ragging|Unequal<br>concentrations<br>of<br>peptides originating from the<br>same protein|
|RP-HPLC separation|Technical variability in elution<br>times|Difficulties<br>in<br>matching<br>unidentified<br>peptides<br>to<br>identified<br>peptides<br>across<br>different runs|
||Peptide<br>carry-over<br>due<br>to<br>peptides from previous runs that<br>did not elute from the column|Detection of peptides that were<br>not<br>present<br>(worst<br>case),<br>peptide intensities influenced<br>(increased) by the order in<br>which the samples were run|
|ESI ionization|Strong differences in peptide<br>ionization efficiencies|Strong<br>differences<br>in<br>MS<br>intensities<br>for<br>peptides<br>originating<br>from<br>the<br>same<br>protein|
||ESI<br>saturation:<br>peptides<br>compete for ionization|<br>Ionization<br>suppression:<br>a<br>peptide’s MS intensity(partially)<br>depends on the nature and<br>amount<br>of<br>other<br>co-eluting<br>peptides|
|||<br>Suppression<br>of<br>high<br>MS<br>intensities resulting in an upper<br>limit of quantification|
||Peptides ionize in different<br>charge states|<br>Intensities for different charge<br>states need to be taken into<br>account when quantifying a<br>peptide|
||Gas-phase<br>peptide<br>ions<br>undergo chemical reactions|Artificial peptide modifications,<br>which<br>are<br>possibly<br>not<br>accounted<br>for,<br>resulting<br>in<br>unidentifiable<br>spectra<br>and<br>missing values|
||Changes<br>in<br>electrospray<br>voltage<br>during<br>and<br>across<br>different runs|Increased variability in peptide<br>ionization efficiencies|
|MS recording|Discrete<br>MS<br>spectrum<br>recording|MS intensity not recorded at the<br>elution peak|
||MS detector saturation|Suppression<br>of<br>high<br>MS<br>intensities resulting in an upper<br>limit of quantification|
|MS² recording|Limited amount of MS peaks<br>targeted for fragmentation|<br>Different<br>peaks<br>fragmented<br>across different runs: missing<br>values|
||Preferential targeting of high-<br>intensity MS peaks|Intensity-dependent<br>missing<br>values|
||<br>Loss of unexpected peptide<br>fragments|Difficulties in MS² spectrum<br>identifications and thus missing<br>values|
||Co-fragmentation<br>of<br>peptide<br>ionswithsimilar m/z values|Unidentifiable<br>chimeric<br>MS²<br>spectra and thusmissingvalues|


31

The first step in the protocol, protein extraction, was shown to be responsible for 72% of all technical variability [310]. However, small differences in protein extraction efficiencies generally should not pose too much problems as an equal amount of total peptides is loaded onto the instrument for every sample. As noted in 1.2.2, it is imperative that all sample preprocessing is compatible with RP-HPLC-MS. It is therefore important to limit or avoid the use of urea [105, 106] and to avoid the use of SDS [91, 106-109] as well as other contaminants [112].

The digestion step is also critical. If the digestion efficiencies differ between samples, certain peptides might be formed to different extents. Consider for example the proteolytic cleavage of the following protein:

SESNAHFSFPKEEEKEFLESYPQNCPPDALPGTPGNLDSAQELEGFQIPTNLDWAGTSQAR

The most commonly used protease, trypsin, cleaves at the C-terminus of lysine (K) and arginine (R) (indicated in red) [311]. Depending on the digestion efficiency, varying amounts of the peptides SESNAHFSFPK and SESNAHFSFPKEEEK can be identified. Both the very short EEEK peptide and the very long EFLESYPQN… R peptide are barely or not detected by the mass spectrometer. Peptide SESNAHFSFPKEEEK is said to have one missed cleavage site, but peptides can have multiple missed cleavages. The presence of missed cleavages not only depends on the duration of the digestion, but also on the quality of the enzyme [312]. However, peptides can also be formed at non-canonical cleavage sites (i.e. not at lysine ’s or arginine ’s C -terminus) and modifications (either of biological origin or artifacts formed during sample preprocessing) may affect enzymatic digestion efficiency [311]. Next to these elements, the amino acids adjacent to a possible cleavage site, the location of a peptide in a protein’s 3D structure and chemical degradation also play a role in the kinetics of the generation and degradation of different peptide species. Moreover, unwanted chemical reactions during sample preprocessing and/or the activities of exopeptidases that might be present in the sample or as contaminants in the commercial protease batch may cause N- terminal or C- terminal peptide degradation (“peptide ragging”) [313]. For these reasons, the concentrations of most peptides are not equal to the initial protein concentration [314]. This stresses the importance of uniformity in the digestion conditions over the different samples.

Since the RP-HPLC column is typically packaged with porous silica beads coated with apolar alkyl chains (e.g. C18), peptides will be separated by their differences in hydrophobicity [315]. Protein modifications can however influence the column retention of an affected peptide [316]. Further, there is inherent variability in the chromatographic retention of a given peptide over different MS runs. This is an important factor to bear in mind when matching an identified peak in one MS run to an unidentified peak in another run; so-called matching between runs [317]. Comparing retention times over different runs is routinely done by algorithms for retention time alignment [318]. Retention times are often monitored as a general quality control measure by spiking in a known peptide or peptide mix [319, 320] and several algorithms have been developed to predict the retention times of known peptides [315, 321-323]. In order to maximize the mass spectrometer’s operation time, HPLC columns are generally not replaced between analyses. Therefore, peptides from a previous injection might partially remain retained on the column and elute during a subsequent run, thus leading to the detection of peptides that were not present in that last sample and/or biased quantifications. Little has been published in the literature about sample carry-over, even though this is a non-negligible problem [324].

Peptide elution happens continuously, while the mass spectrometer only generates mass spectra at discrete time points. As peptide elution takes around 5 – 25 seconds [325, 326] and modern mass spectrometers typically tend to record an MS spectrum every second, the intensity peak for a single peptide ion will be recorded in sequential MS spectra. To allow for

32

an accurate quantification, it is important to record at least one MS peak at or near each peptide ’s elution apex. High-resolution RP-HPLC separation concentrates peptides in narrower elution peaks and is highly beneficial for different reasons [141]. First, repeated fragmentations of the same peptide ion over its elution window are highly reduced, thus winning MS analysis time. Next, highly focused peptide elution increases ion intensities and the ability to target monoisotopic peaks, which facilitates identification. Finally, an improved separation reduces co-elution of peptides, preventing ion suppression and co-fragmentation (see below).

The quality of ionization is of utmost importance as poor ionization leads to lower quality spectra (lower signal-to-noise ratio), making it more difficult to identify and quantify peptides. The electrospray voltage should also be kept as constant as possible over different runs as even small voltage deviations aggravate the variability in ionization efficiencies of peptides over different runs, which reduces the precision of label-free quantification [225].

During electrospray ionization (ESI), peptides are endowed with a positive charge (when working in positive ionization mode) [122]. However, the ionization efficiency of peptides differs. For example, highly acidic peptides and phosphopeptides ionize more poorly [123]. Such different ionization efficiencies leads to different MS intensities across different peptides, even if their concentrations are equal. In addition, the ionization efficiency of a peptide is also influenced by the nature and the amount of co-eluting peptides as these may suppress each other’s ionization, a phenomenon known as ionization competition or ionization suppression [122, 327]. For these reasons, peptide ionization efficiencies are still difficult to predict [328]. Finally, the total amount of peptides that can be ionized simultaneously is also limited due to saturation effects during ionization [329, 330], which results in a suppression of high MS intensities and therefore an upper limit on the amount of peptides that can be quantified.

Ionization also generates different ion species from a single peptide, which differ in charge state. Indeed, ESI typically generates multiple ions with different charge states from the same peptide. For tryptic peptides, a double positive (+2) charge state is the by far most common after ESI ionization (around 75 - 90% of all ions), followed by triple positive (+3, around 10 - 20% of all ions) and single positive (+1, around 5% of all ions) [331]. The ionization step might also affect the chemical composition, and hence the mass, of an ion. Examples include insource peptide oxidation and the loss of water or ammonia from N-terminal glutamate or glutamine residues, respectively, to form pyroglutamate [332, 333].

In the MS spectrum, the intensity of every ion that eluted from the HPLC column at that particular point in time is recorded in function of its mass-to-charge ( _m_ / _z_ ) ratio. Ion intensities can be seen as proxies for abundance, with the _caveat_ that the ionization efficiencies differ strongly between different ion species. The detector of the mass spectrometer is also sensitive to saturation, which might also result in suppression of high MS intensities [329, 330].

After the generation of the MS spectrum<sup>24</sup> , a high-intensity ion species is isolated with the quadrupole and targeted for fragmentation, a process that is repeated several times before a new MS spectrum is recorded. High-intensity MS peaks are intentionally targeted for fragmentation to avoid the targeting of noise peaks and hence increase the depth of the analysis. However, the fact that not all peaks in an MS spectrum can be targeted for fragmentation and the fact that high-intensity peaks are preferentially selected, results in intensity-dependent missing values. Dynamic exclusion, whereby previously-targeted m/z

> 24 Or sometimes during the generation of the MS spectrum, if the machine has two mass analyzers.

33

values are temporarily excluded from fragmentation increases the quantification depth but does not alleviate the issue of intensity-dependent missingness.

Fragmentation also commonly results in neutral losses of water and ammonia, or even partial or complete amino acid side chains [137]. Such losses need to be taken into account when identifying a peptide ion based on its MS² spectrum. To facilitate identification, it is also preferable that the monoisotopic peak is correctly determined. For short peptides, the monoisotopic peak is often the highest one, but for longer peptides, this peak might be considerably smaller. This sometimes leads to determination of the wrong peak in the isotopic envelope and hence a wrong selection of candidate peptides during database filtering. Finally, when one or more peptides of about the same _m_ / _z_ elute together with a target peptide ion, such neighboring ions can be isolated as well, resulting in a mixed MS² spectrum [334]. Such a mixed fragmentation spectrum will also cause problems regarding identification and quantification.

#### **2.2.2. Advantages and disadvantages of label-free MS-based proteomics**

An obvious advantage of label-free MS-based proteomics is that the laborious and often costly labeling is omitted altogether [226]. Moreover, label-free analyses have a deeper coverage compared to label-based strategies. Indeed, compared to label-based quantification at the MS level, a significantly deeper coverage in label-free proteomics is caused by the decrease in spectral complexity [257, 258]. Compared to isobaric labeling strategies, the increase in coverage mainly results from the higher signal-to-noise ratios in MS spectra compared to MS² spectra [265, 307]. As noted before, label-free approaches also have a higher coverage and a higher dynamic range than label-based approaches [263, 308]. Another major advantage of label-free quantification is that there are no restrictions on the sample type. Indeed, metabolic labeling cannot be applied to every type of sample (e.g. patient blood samples), and, although the use of a labeled reference standard (e.g. super-SILAC) might be an option in certain cases, this application is destined to fail when the samples in an experiment are too different from each other. Isobaric labeling can be applied on any sample type and has reached multiplexing capacities up to 12 [296]. However, when more samples need to be compared, between-run comparisons will need to be made [335]. Moreover, for any label-based strategy, all samples should be generated prior to the MS analysis of the first sample. Label-free quantification allows for the analysis of an unlimited number of samples, even retroactively, as long as the machine’s working conditions have not been changed dramatically [317, 336].

Since labeling is omitted, each sample is analyzed separately. This results in longer overall run times and thus a lower throughput [306, 336]. Inevitably, precision will also be lower compared to label-based approaches because random run-to-run variability cannot be factored out. Thus, robustness of the instrumentation and the analytical conditions is imperative for successful label-free analyses [336]. However, after balancing the pros and the cons, most research publications that compared label-based quantification to label-free quantification seem to express a general preference for the latter [257, 258, 308, 309], although the preference of individual researchers is often driven by their own experience, i.e. the instrumentation and quantitation technology they are most comfortable with.

#### **2.2.3. Other label-free approaches**

Next to label-free discovery-based data-dependent shotgun proteomics, there are two other major label-free proteomic techniques: targeted proteomics and data-independent proteomics. For the sake of completeness, and because I briefly refer to them in my future perspectives, I will here outline their major points.

34

All techniques outlined so far in this chapter aim to identify and quantify as many proteins as possible. However, none of these techniques guarantees that a particular protein of interest will be identified, especially if this protein is very low abundant (e.g. many transcription factors) [337] or is difficult to solubilize (e.g. membrane-inserted proteins) [338]. In fact, some proteins or protein regions have never even been identified by mass spectrometry, the so-called “hidden” or “dark” proteome [337, 339, 340]. Moreover, even if a protein of interest is identified in a certain run, it is not guaranteed to be identified in another run due to inherent run-to-run variability.

Targeted proteomics aims to reproducibly monitor and precisely quantify one or more selected proteins [341]. Indeed, if the retention times and _m_ / _z_ values from peptide ions of interest are known, a mass spectrometer can be programmed to detect, fragment and record MS² spectra only for those peptide ions. This technique is called selected reaction monitoring (SRM) and is typically performed on a triple quadrupole instrument (QQQ) instrument. In this instrument, the first quadrupole is used to isolate the peptide ion, the second quadrupole serves as a collision cell to fragment this ion and the third quadrupole is used to isolate selected fragment ions. Since the QQQ only isolates selected fragment ions, SRM on a QQQ instrument has a high dynamic range and is very selective and sensitive [342]. Note that it is also possible to operate other machines in SRM mode [343]. In parallel reaction monitoring (PRM), the third quadrupole is substituted with a highly accurate mass analyzer to record all fragment ions [344]. PRM recently gained a lot of traction as PRM assays have a similar performance compared to SRM assays, but are easier to develop and possibly even more specific [345].

In data-independent acquisition (DIA), the intensity of the MS peak does not determine which ions are being fragmented. Shotgun CID, MS<sup>E</sup> and All-ion Fragmentation are DIA methods in which the complete _m_ / _z_ range of the MS spectrum is targeted for fragmentation [135, 346, 347]. Other approaches divide the _m_ / _z_ range of the MS spectrum into predetermined _m_ / _z_ isolation windows and sequentially co-fragment all ions within such windows before going on to record the next MS spectrum [120, 348, 349]. DIA methods are immensely promising because they record all fragment ion spectra. Theoretically, it is thus possible to record every possible peptide in a sample as long as its fragment ions can be identified. Moreover, DIA data can be retroactively queried for new peptides of interest (e.g. modified forms of peptides). DDA search engines have been modified to unravel the very complicated MS² spectra that result from DIA [346, 348]. However, deconvoluting such multiplexed spectra remains challenging [350].

Out of all DIA methods, Sequential Windowed Acquisition of all Theoretical fragment ion mass spectra (SWATH-MS) is the most popular [351-353]. In SWATH-MS, specific MS² fragment ion peaks are tracked over time without deconvoluting the spectra [351]. On the new Q Exactive HF-X, a single SWATH-MS run identifies on average more than twice the number of peptides of a DDA run [354]. Moreover, in a benchmark experiment where 12 human proteins were spiked in a HEK-293 background, SWATH-MS analysis had only 1.6% missing values compared to 51% missing values in the DDA analysis of the same sample [355]. SWATH-MS is also highly reproducible across different labs [356]. Compared to targeted proteomics, it has a much higher coverage, but remains slightly less sensitive [351, 357-359].

The major disadvantage of DIA is that knowledge on the chromatographic and mass spectrometric behavior of peptides of interest is required to build a spectral library needed to identify the peptides [359]. This often implies that a DDA analysis is performed prior to the DIA analysis to obtain the necessary information on the peptides expected in the sample.

35

36

## **3. FROM SPECTRA TO DATA**

In the previous chapter, I described the bottom-up shotgun proteomics workflow up to the generation of MS and MS² spectra. Given the continuous elution of peptides from the HPLC column, most peptide ions will be recorded in multiple, consecutive MS spectra. The peaks in these spectra must be converted into meaningful qualitative and quantitative information about the peptides in the samples. In this chapter, I will describe how MS and MS² spectra are used to identify peptides in label-free DDA MS-based proteomics. Then, I will show how peptides are assigned to proteins and I will describe how a single intensity value is assigned to each peptide followed by a description of the nature of the MS data. I will conclude this chapter with an explanation for the need for benchmarking and the description of the CPTAC Study 6 benchmark dataset.

### **3.1. Peptide ion identification**

In MS- based proteomics, peptide ions (also called “features”) are identified based on information present in both the MS and the MS² spectrum and only features that are deemed to be reliably identified are typically passed on to the quantification stage. Do note that a feature’s identification is actually not required for its quantification. Indeed, some workflows, such as those proposed by Sieve (Thermo Fisher Scientific) and Progenesis (Nonlinear Dynamics) adopt a feature-based quantification whereby identification efforts are primarily focused on features that are flagged as differentially abundant after the quantification stage. However, my thesis primarily focuses on the protein quantification, for which prior identification of features is required. Therefore, the remainder of this thesis describes the identificationbased workflow.

The charge state and the mass of a feature can be readily determined from its MS spectrum. Indeed, charge state variants elute simultaneously and are thus present in the same MS spectra. As mass-to-charge ratios ( _m_ / _z_ values) are recorded in MS spectra, an ion with, say, charge state +3 will have a peak at an _m_ / _z_ value exactly equal to 2/3 times the _m_ / _z_ value of the same ion with charge state +2. As mentioned in 1.2.2, the natural occurrence of stable heavier isotopes generates an isotopic envelope for each charge state of an ion. Since isotopes differ in mass by a natural number of neutrons, the minimal difference in mass between two isotopic variants is approximately 1 Dalton. This knowledge is used to infer the charge state of an ion: a difference of _m_ / _z_ = 1/2 Th between the peaks of an isotopic envelope denotes a +2 charge state, whereas a difference of _m_ / _z_ = 1/3 Th points to a triply positively charged ion. From this charge state, the monoisotopic mass of a peptide ion can be readily calculated by multiplying its corresponding monoisotopic _m_ / _z_ value by its charge state. However, knowing the mass of a peptide is not enough to identify it. Indeed, not only do all permutations of a particular amino acid sequence have exactly the same masses<sup>25</sup> , some entirely different combinations of amino acids also have the same nominal masses<sup>26</sup> . Also note that modifications change a peptide’s mass and that modified peptides often do not co -elute with their unmodified counterparts [333]. For these reasons, an MS² spectrum of a peptide is required to identify the amino acid sequence corresponding to a peptide’s MS peak.

An MS² spectrum contains the _m_ / _z_ values for all the fragment ions obtained by fragmenting a single peptide ion. To enable identification, the selected peptide ion should by preference be the monoisotopic peptide ion. Indeed, any other peak in the isotopic envelope is in fact a

> 25 E.g. the amino acid sequences LDGER, DGERL, GERLD, etc. all have a 588 Da mass.

> 26 E.g. the amino acid sequences LGD and ER both have a nominal mass of 303 Da.

37

mixture of numerous isotopic variants. For example, the _m_ +1 peak represents a mixture of ions that consist of a single heavy isotope together with only light isotopes. However, this heavy isotope can be for example a heavy carbon in the first amino acid, or a heavy carbon in the second amino acid, or a heavy nitrogen in the third amino acid, and so on.

As described in 1.2.2, the type of fragmentation determines the main type of fragment ions that will be found in the MS² spectrum (both y- and b-ions for CID, mainly y-ions for HCD [137139]). In the early days, when mass spectrometers only generated a few 100 MS² spectra, peptide identification was often done manually by printing out the MS² spectra and measuring the distances between the fragment ion peaks. The sequence could then be inferred through some sort of “ ladder sequencing ” as demonstrated in Fig. 3.1.


**Figure 3.1.** Theoretical demonstration on the inference of a peptide sequence based on some sort of ladder sequencing if all b- and y-ions are present (shown in purple and blue, respectively). The mass differences between the peaks give information about the amino acid sequence of the peptide. Since leucine (L) and isoleucine (I) have the same empirical chemical formula and thus the same masses, no direct distinction can be made between both. y-ions are often somewhat more abundant than b-ions, especially in HCD fragment spectra. Therefore, peptide sequencing based on y-ions is shown. The presence of the b-ions complicates the analysis somewhat but can also provide supporting evidence. Note that this representation is somewhat simplistic. In reality, a-, c-, x- and z-ions might also be present in the fragmentation spectrum. Moreover, some b- and y-ions might not exceed noise levels, while noise peaks (either true noise or fragments from co-isolated peptides) might obfuscate the analysis. Modifications will also influence the masses of those fragments that carry the modified amino acid.

Nowadays, manual inspection of the sheer number of MS² spectra is impossible as high-quality experiments typically generate well over 5,000 MS spectra and over 50,000 MS² spectra in a single run.

Because of the sheer amount of data, bioinformatics software is now indispensable for feature identification. One example is PeptideProphet [360], which makes use of the SEQUEST algorithm [361]. The idea behind SEQUEST is rather simple. First, a database with protein sequences is provided to the algorithm. This database clearly depends on the sample: when the sample is e.g. a human cell culture, one uses the human proteome from the UniProt Knowledgebase, whereas for an _Arabidopsis_ sample, the TAIR database is often used [362]. All proteins in the database are then _in silico_ digested according to the cleavage rules of the protease used. For trypsin, all protein sequences are thus split at lysine (K) or arginine (R) residues. Next, only those peptides are selected from the database which lie within a narrow mass tolerance range around the observed mass value of the MS peak. Then, all possible b- and y-ions are calculated for each of these peptides and a score is calculated. This score

38

increases for each theoretical b- or y-ion that, again within a certain mass tolerance, can be matched to an observed MS² peak. Similarly, the score decreases for each theoretical peak that cannot be matched to an observed peak and for any observed peak that cannot be matched to a theoretical one. All theoretical peptide candidates are then ranked according to their scores and the highest-ranking peptide is assumed to be the correct one if it scores significantly higher than the second-highest ranking peptide. This coupling of a peptide ion species to a certain MS² spectrum (and hence the corresponding MS peak) is termed a peptide-to-spectrum match (PSM) [363]. The simple idea of calculating a score based on theoretical spectra from _in silico_ digested proteins still remains the basis of all other database search algorithms today.

In reality, the SEQUEST algorithm is more complicated than described above as it also takes neutral losses such as water, ammonia and carbon dioxide into account. In its earliest version, modifications could only be considered if they were assumed to be present at every occurrence of the modification site. This was achieved by simply shifting the masses of the _in silico_ peptides. Later on, variable modifications were also introduced. This means that the algorithm searches both for the presence and the absence of certain modifications on certain amino acids in certain peptides. Phosphorylation of serine, threonine and tyrosine residues is an example of a variable modification that is often included in a search. One problem with searching for variable modifications is that they massively inflate the computational search space, especially if peptides are allowed to carry multiple modifications at multiple amino acids. For example, a variable search for phosphorylation alone may lead to a 67-fold increase in the search space [364]. Such inflations do not only drastically increase computational search times, but also increase the uncertainty on PSMs that map to unmodified peptides because of the increased probability that an _in silico_ spectrum of an unrelated modified peptide matches against the spectrum of an unmodified peptide. Researchers are therefore often advised to not search for more than two or three variable modifications. Nonetheless, search space inflation can be largely fended off with some clever optimizations because the masses of modifications rarely coincide with amino acid masses, a property that can be exploited in high-resolution MS data [365]. Other optimizations include performing a two-pass search in which the second search only probes for modifications of peptides for which an unmodified counterpart was already identified in the first search [366]. Alternatively, one could limit the search to those modifications and modification sites that have previously been confirmed and are stored in a curated database [364]. Interestingly, it has been shown that unaccounted modifications are responsible for about 20 – 50% of all false positive identifications [367]. Therefore, open modification search engines have been developed that allow users to search for mass differences [365]. That way, much more modifications and even peptides that differ by a single amino acid from the canonical sequence in the database can be detected.

The Mascot search engine was the first to introduce probability-based scoring, whereby the probability of an identification was weighted against the probability that a match between the theoretical and the observed spectrum occurred by random chance [368]. This was later on improved by incorporating the concept of target-decoy matching [369, 370]. In target-decoy matching, a set of nonsensical peptides (decoys) of the same size as the theoretical database peptide set (targets) is added to the search space. This nonsensical set can be obtained in multiple ways, e.g. by random scrambling of the original protein sequences, but is mostly obtained by simply reversing the protein sequences followed by _in silico_ digestion. In case of palindromic sequences, forward and reverse sequences would overlap, but palindromes are extremely rare in practice because the protease’s specificity typically requires peptides to end in very few specific amino acids (e.g. arginine (R) or lysine (K) in the case of trypsin). Therefore, a palindromic sequence should already display a missed cleavage after the first amino acid, which is rather uncommon. Next, the observed peaks are matched against the combined

39

database as described before. Then, an identification false discovery rate (FDR) threshold is calculated for each target-PSM. This FDR is simply calculated by dividing the number of equally- or higher-scoring decoy-PSMs by the number of equally- or higher-scoring targetPSMs. Finally, an FDR threshold is set (typically at 1%, rarely at 5%) and all PSMs under this threshold are passed on to the quantification stage, while the PSMs that exceed the threshold are removed from the data as these are deemed not certain enough. Note that for two-pass searches, this FDR calculation is way too liberal because the enrichment of targets in the first pass makes it more likely for the spectra to match to targets in the second pass. This constitutes a violation of the assumption that false matches should be equally likely to match a target or a decoy. Therefore, two-pass searches require an adjusted target-decoy database [371].

Nowadays, there are many different algorithms that enable peptide identifications from MS² spectra. These include Tide, a fast implementation of the SEQUEST algorithm [372], X!Tandem [373], MS-GF+ [374], MS Amanda [375], MyriMatch [376], Comet [377], Andromeda [378], OMSSA [379], Novor [380] and DirecTag [381]. A tool like SearchGUI [382], developed by the compOmics lab, unites all these algorithms in a graphical user interface. Furthermore, tools such as PeptideShaker [383] can be used to combine results of different search engines to boost identifications. The MaxQuant software package, which uses the Andromeda search engine, is very popular nowadays thanks to its integrated pipeline from identification to quantification and its user-friendly graphical user interface [384].

### **3.2. Protein inference**

In a typical shotgun proteomics workflow, the aim is to identify and quantify as many proteins as possible, but the data used for this are at the PSM level. Therefore, PSMs should be first assigned to one (or more) protein(s). Protein inference is straightforward for peptides that can be uniquely mapped to a protein sequence stored in a database. However, this becomes more complicated when a peptide can be mapped to several protein sequences [385], which frequently occurs for different protein isoforms that result from alternative splicing and for proteins that originate from paralogous genes<sup>27</sup> . Such peptides are called “shared peptides”, “degenerate peptides” or “razor peptides”.

PeptideProphet was the first algorithm to propose a solution to this problem [386]. Here, protein identification probabilities are first calculated under the assumption that all peptide matches are independent. Then, peptide identification probabilities are updated based on the protein identification probabilities. This updating of peptide and protein identification probabilities is then repeated until convergence. Others statistical models have also been proposed in an attempt to more reliably assign shared peptides [387, 388]. A conceptually simple way to deal with shared peptides is Occam’s razor approach. Here, each shared peptide is simply assigned to the protein which already has the highest number of identified unique peptides assigned to it. This is the approach currently implemented in MaxQuant [384]. MaxQuant also groups proteins that share a large fraction of their peptides in so- called “protein groups” . As the abundance of a shared peptide might reflect the combined abundance of multiple proteins, shared peptides are almost always removed from the dataset prior to quantification.

Another issue in protein inference is the occurrence of so- called “ one hit wonders ”: proteins that are identified by a single peptide. It is generally considered unreliable to infer a protein

> 27 Paralogous genes are genes that descend from the same ancestral gene within a species and therefore often have a high sequence homology. Their resulting protein products often execute similar functions.

40

based on a single peptide because if this identification is incorrect<sup>28</sup> , a protein is quantified that might not even be present in the sample. Therefore, such proteins are often removed from the dataset after using the so- called “ two-peptide rule ” [385], which however has also been criticized. It was indeed shown that it is more likely to find a protein with two mediocre-scoring peptides in the decoy database than it is to find a protein with a single high-scoring peptide in the decoy database [389, 390]. It was therefore proposed to abandon this two-peptide rule in favor of an approach in which the protein identification FDR is the sole criterion to accept a protein as being identified. Indeed, although in the past, all PSMs that passed a certain FDR threshold were passed on to the quantification stage, it was soon shown that if the PSM FDR is controlled at the 1% level, the protein FDR is much higher and should therefore also be taken into account [391, 392]. This is because the chance that a false positive PSM maps to a protein in the database is in theory random and therefore only dependent on that protein’s number of theoretical (tryptic) peptides. However, a protein that is truly present in a sample will typically generate multiple PSMs that will correctly map to that protein. Therefore, a fraction of the proteins in the dataset (i.e. the true positives) will be enriched in true positive PSMs, while a relatively large fraction of false positive proteins will have very little PSMs assigned to them [393].

Many different methods have been developed to estimate protein identification FDRs [386, 394-396]. However, when calculating a protein FDR, it is important to clearly define how this value is to be interpreted. As noted by The _et al._ (2016), a distinction should be made between defining a false discovery as a protein that is inferred from an incorrect PSM versus defining a false discovery as the incorrect identification of a protein that is in reality not present in the sample [397]. These are not the same, as many proteins might be present in the sample that are not assigned any correct PSM but can be assigned to one or more incorrect PSMs by random chance. These authors noted that protein FDRs can strongly differ depending on the definition.

The protein inference problem is reviewed more in depth in Huang _et al._ (2012) [398] and Serang and Noble (2012) [399].

### **3.3. Peptide quantification**

A first step in the quantification procedure is the determination of the abundance of all identified peptides. This can be done in two ways. The first way, summing up MS² intensities, is now largely deprecated for label-free DDA data. The second and by far the most common way is by using the MS intensities.

The reason why label-free approaches in which MS² fragment ion intensities are summed to determine a peptide ion’s intensity perform worse than MS peak -based methods in terms of reproducibility, missing data, quantitative dynamic range and quantitative accuracy [307] is because MS² intensities are highly data-dependent. Due to dynamic exclusion, a particular peptide ion can be targeted for fragmentation when it is relatively far from its elution apex. This makes summed-up MS² intensities much more variable from run to run and hence less suited for reliable quantification.

When quantifying peptides based on MS intensities, it is important to realize that peptides elute continuously from the RP-HPLC column, while MS spectra are recorded at discrete time points. Indeed, if an MS spectrum is recorded every second and peptide elution typically ranges from 5-25 seconds [325, 326], most peptide ion peaks will be recorded in multiple, sequential MS

> 28 At a 1% PSM identification FDR, on average 1% of all PSMs is expected to be wrong, but for each specific PSM, this probability might be significantly higher or lower.

41

spectra (see also 2.2.2). Here, every peptide ion is recorded in each MS spectrum as an isotopic envelope due to the natural isotopic occurrence. A simple way to determine an identified peptide ion’s intensity would be to sum the intensities of the isotopic envelopes in each MS spectrum and select the MS spectrum in which this summed intensity is the highest (i.e. near the peptide’s elution peak). How ever, this results in rather imprecise quantifications because for one peptide ion, an MS spectrum might be recorded very close to its elution peak, while for another ion, the MS spectrum with the ion’s highest intensity peak might be recorded up to 0.5 seconds<sup>29</sup> before or after its elution peak. As shown in Fig. 3.2, the elution profile of a peptide can be fairly easily reconstructed based on the sampled MS intensities of this peptide. Indeed, by fitting a curve to these summed intensities over time, a peptide’s elution profile can be reconstructed, which results in a much more reproducible quantification [400, 401].


**Figure 3.2.** Theoretical example demonstrating the challenges in MS<sup>1</sup> and MS² peptide quantification. A. Illustration of the elution profile of three peptides (blue, red and green). Arrows denote the discrete time points at which an MS spectrum is taken. Crosses on the elution profile indicate when that specific peptide is selected for fragmentation, which results in an MS² spectrum. MS spectra at time points a, b and c are shown in B; MS² spectra are shown in C. Due to its high abundance, the blue peptide was selected for fragmentation early in its elution profile (MS² spectrum d: dark blue). Because of dynamic exclusion, this peptide was not re-selected for fragmentation again until far beyond its elution peak (MS² spectrum f: light blue). Reprinted with permission from _Krey et al. (2014) [402]_ , © 2014 American Chemical Society.

Some methods are even more sophisticated in trying to increase the quantitative accuracy. For example, the Andromeda search engine, incorporated in MaxQuant, integrates the peak intensities of each ion’s isotopic envelope during peptide elution. More specifically, Andromeda fits a Gaussian peak to the three most central data points in each isotopic envelope. These 2D peaks are then smoothed to 3D peaks in the retention time dimension and the total intensity for a particular ion is then set equal to the volume of its corresponding 3D peak [384]. Fig. 3.3 gives a 3D visualization of the increase in intensities in the isotopic envelope at the start of the elution of a peptide ion.

> 29 This is, given that an MS spectrum is recorded every second, a typical user-defined setting.

42


**Figure 3.3.** 3D view of the isotopic peaks during the elution of the doubly charged peptide ion CCSDVFNQVVK in sequential MS spectra in the MaxQuant Viewer tab. Image adapted from Tyanova _et al._ (2015) [403]. Proteomics. Published by Wiley‐VCH Verlag GmbH & Co. KGaA, Weinheim, CC BYNC-ND 4.0.

A disadvantage of Andromeda’s algorit hm is that it is computationally intensive. Moreover, until very recently, MaxQuant was only available on Windows, which impeded its inclusion in automated Linux server pipelines [404]. These were the main motivations for the development of moFF, a platform-independent quantification algorithm that only quantifies the apex of the elution profile, making it fast, but without compromising on quality [405, 406]. Do note that many other algorithms have been developed to calculate peptide ion intensities, some of which are reviewed in Sandin _et al._ (2014) [407].

### **3.4. The nature of the data**

The previously described workflow results in specific data properties that are typical for MSbased proteomics and that are important to bear in mind when evaluating protein levels.

In bottom-up proteomics, PSMs do not correspond to peptides, but to peptide ions, whereby multiple peptide ions can map to the same peptide sequence. Indeed, the same peptide can often be identified under different charge states and/or with different modifications. Sometimes, a given modification can be detected at more than one location within the same peptide. As the (unmodified) backbone amino acid sequences of such PSMs are identical, these ion species are expected to behave more alike compared to unrelated ion species. Therefore, the intensities of these species are correlated with each other. Similarly, ion species of the same charge states will also be correlated. On a higher level, there is correlation between all peptides that are mapped to the same protein. The highest level in the hierarchy is the correlation between proteins. Indeed, since proteins interact with each other in numerous pathways, proteins that closely interact with each other, that are part of the same signaling pathway or even reside in the same subcellular location tend to behave more similarly than totally unrelated proteins. Orthogonal to the correlations between peptides and proteins, there is a strong within-run correlation due to the relatively large run-to-run variability in label-free proteomics. To keep this run-to-run variability minimal, it is necessary to tightly control the

43

instrumentation. This makes raw label-free proteomics data hierarchical with correlations on many levels in the data. Moreover, it is possible that for the same protein in the same MS run, e.g. two peptides are observed with only one PSM, three peptides with two PSMs and one peptide with three PSMs.

Even for peptides originating from the same protein, differences in intensities are often substantial. One reason for this is that differences in proteolytic cleavage efficiency cause some peptides to be generated more efficiently than others, rendering individual peptide levels not equal to protein levels. Moreover, intensities of different peptide ions also strongly differ because of large differences in ionization efficiency. Finally, the latter is context-dependent as the nature and the amount of co-eluting peptides also drive the efficiency by which a peptide is ionized (see chapter 8). Such ionization competition can be a more important driver of a peptide’s intensity than i ts actual abundance [408]. As noted in section 3.2, the intensities of shared peptide sequences arise from an unknown combination of peptide ions coming from different proteins. Therefore, shared peptides are often removed from the dataset prior to quantification.

While the raw data is at the PSM-level, quantification is typically done at the protein level. PSMlevel data thus needs to be summarized to the protein level. It is possible to summarize the PSMs directly to the protein level. However, this might be suboptimal because of the hierarchical nature of the data and the missing values that make the data unbalanced. Indeed, if the PSMs would be summarized as if they were independent observations, a bias will be introduced because some peptides will be “overrepresented” in the protein’s abundance estimate, while other peptides will be “underrepresented”. Therefore, summarization is sometimes done in two steps: in a first step, the data are summarized to the peptide level (i.e. each peptide sequence is the summary of all its potential charge states and peptideforms). MaxQuant, for example, outputs peptide-level summaries as summed raw PSM intensities. In a second step, the peptide-level data are summarized to the protein level (discussed in detail in 4.1.5). Contrary to protein summarization based on peptide-level values, PSM to peptide summarization has not been studied in detail, and commonly-used data analysis pipelines such as the MaxLFQ algorithm in MaxQuant [317] and MSstats [409] calculate protein-level summaries based on PSM intensities, ignoring possible correlation between PSMs that map to the same peptide sequence. From here on, I will assume that all data are summarized to the peptide level, unless specifically mentioned otherwise. However, note that all of the criticisms regarding peptide-to-protein summarization outlined in 4.1.5 can also be applied to PSM to peptide summarization.

The linear dynamic range of the mass spectrometer also affects the data. Indeed, within a certain concentration range, an increase in peptide concentration will result in a multiplication of the MS signal with more or less the same factor. This range is termed the linear dynamic range. Above this range, the ESI spray ionization and/or the MS detector becomes saturated, leading to a plateau in the ion’s MS intensity signal . Below the linear dynamic range, a peptide ion will not be observed. Note that the linear dynamic range will be different from peptide to peptide due to their different ionization efficiencies. Fig. 3.4 gives a graphical representation of the linear dynamic range.

44


**Figure 3.4.** The concept of linear dynamic range in proteomics. (a) Peptide ion intensities for three theoretical proteins: a low abundant, middle abundant and highly abundant protein. For the low abundant protein, many of its peptides will fall below the limit of detection (LOD) and will therefore not be identified. Its abundance will only be estimated based on the identified peptides and might therefore be overestimated. For the middle abundant protein, most of its peptides are observed and the protein’s estimated abundance will be close to its true abundance. For the highly abundant protein, some of its peptides will be more abundant than the upper limit of quantification (ULOQ), and their ion signals will be lowered. Hence, the highly abundant protein’s abundance might be unde r-estimated. (b) The dynamic range in practice. In this experiment, different known amounts of proteins were compared to each other. When the differences in concentration become large, the difference between the estimated protein abundances and the true protein abundances also increase. Such deviations from linearity are substantial for large differences in abundance. Image (a) modified after Jarnuczak _et al._ (2016) [330], © 2016 by Am erican Chemical Society (“ACS”), CC BY 4.0 and image (b) adapted from Arsova _et al._ (2012) [410] © 2012 by The American Society for Biochemistry and Molecular Biology, Inc.

The large amount of missing values in the data is a major issue in label-free DDA shotgun proteomics. Upon searching the public repository PRIDE [411] for MaxQuant datasets that applied shotgun proteomics to full or partial proteomes, we found 16 to 82% missing values at the peptide level (see chapter 10). There are multiple reasons for this missingness. A first reason is that a protein might simply not be present in certain samples. A second reason is that experimental reasons (e.g. different tissues with different protein abundance profiles are compared), biological reasons (e.g. downregulation or degradation of a protein) or technical reasons (e.g. inferior quality of a certain run) might cause the MS intensity of a peptide that is truly present to fall below the background noise level. For label-free shotgun proteomics, the limit of detection was estimated to lie around 1 fmol [412]. A third important reason is in the data-dependent nature of the sampling: a peak that was selected in one run, might not be selected for fragmentation in a next run. Indeed, the height of the peak mainly dictates if a peak is targeted for fragmentation or not [413]. This type of missingness is thus largely intensitydependent, although ionization also renders this type of missingness context-dependent. A fourth reason for missing values in label-free shotgun proteomics is that on average around 75% of all MS² spectra is not identified [414]. This happens when an MS² spectrum’s highestscoring PSM falls below the pre-set identification FDR threshold or when no distinction can be made between two or more high-scoring alternatives. Alternatively, the PSM could pass the FDR threshold but might in reality be misidentified. Poorly ionizing peptides are particularly at risk for failed or incorrect identifications. Peptides carrying a phosphate-modification, for example, ionize notoriously poorly because of the phosphoryl group’s default double negative charge state. Moreover, CID fragmentation of peptides with a phosphorylated serine residue often results in a dominant neutral loss of phosphoric acid, leaving too little energy for the efficient fragmentation of the precursor’s peptide bonds [415]. Furthermore, most peptide modifications with a biological or an artefactual origin are often unsearched for due to the

45

strong inflation in computational search space when allowing for too much modifications to occur on the peptides. It has been estimated that at least one third of all spectra cannot be assigned to a peptide due to the presence of sub-stoichiometric post-translational modifications [416]. Another cause for failed MS² identification is co-fragmentation [334]. The chimeric MS² spectra that result from co-fragmented peptide ions are either not identified, or misidentified, resulting in a missing value, or mapped onto only one of the precursor ions. As the corresponding MS peak is a mixture of more than one ion, the abundance of this ion will be estimated higher than it actually is.

All of this stresses the importance of MS² fragmentation. Indeed, all MS peaks that were not targeted for fragmentation or for which no peptide could be matched to the MS² spectrum remain unidentified. One way to alleviate such cases of missing values is by applying a feature alignment or “match -between- runs” algorithm [400, 417, 418]. Here, unidentified MS peaks in one MS run are matched, based on their masses, charges and retention times, to identified peaks of another run in which a similar sample was analyzed. Important for these algorithms is that they should be able to accurately align retention times over different runs and keep their retention time windows (i.e. the deviations in retention time to allow a match between two MS peaks) narrow enough to prevent incorrect matches. This again stresses the importance of a stable analysis workflow and sufficient quality control [419]. A match-between-runs algorithm is also frequently applied in MaxQuant searches [420].

### **3.5. The need for benchmarking**

As explained above, peptide intensities are used for differential analysis of protein abundances. However, there is an enormous variety in differential protein abundance analysis workflows, and each step in these workflows has its impact on the result. Hence, the performances of the different workflows might also differ considerably. This difference in performance is an important point. Indeed, if suboptimal workflows are used, biologically relevant proteins might remain under the radar. Therefore, I will here explain the need for benchmarking to allow comparison of the performances of different workflows.

To evaluate the sensitivities and specificities of different quantitative pipelines, a dataset is needed in which the true relative amounts of proteins in all samples (“the ground truth”) are known. Such a dataset can either be generated by simulation or by spiking in proteins of a certain organism into another organism’s proteome. Simulations have the advantage that they are very simple to generate: one only needs a computer. However, simulated datasets often do not reliably capture the complex data structures of true biological experiments. In a spikein experiment, a set of proteins from one organism is spiked into a complex protein background from another organism at different concentrations. Hence, when two different spike-in conditions are compared, only the spiked-in proteins are differentially abundant. Generating a spike-in dataset requires setting up a wet-lab experiment. Here, it is important to pick two organisms that are genetically very distinct to avoid a large number of shared peptides between both organisms.

In what follows, I will use the CPTAC study 6 dataset to demonstrate the effect of each preprocessing step. In the 6<sup>th</sup> study of the National Cancer Institute's Clinical Proteomic Tumor Analysis Consortium (CPTAC), a trypsin-digested mix of 48 human proteins (Universal Protein Standard 1, UPS1) was spiked in 5 different concentrations into a mix of trypsin-digested _Saccharomyces cerevisiae_ proteins. These concentrations were: 0.25 fmol/µL (sample 6A), 0.74 fmol/µL (sample 6B), 2.2 fmol/µL (sample 6C), 6.7 fmol/µL (sample 6D) and 20 fmol/µL (sample 6E). These samples were sent to five different labs and analyzed on six different mass

46

spectrometers<sup>30</sup> . For convenience, I only used the data from the LTQ-orbitraps at sites 56, 65 and 86. The study was conceived to provide a benchmark dataset to compare the power of different approaches to detect differential abundance and it is the most well-known quantification benchmark dataset. Indeed, Paulovich _et al._ were cited 121 times in Scopus on February 7<sup>th</sup> , 2019.

This dataset is ideal to demonstrate the statistical concept of blocking. Indeed, a typical proteomics experiment is often restricted by spatiotemporal constraints that prevent the generation of all samples simultaneously, with the same equipment, etc. Such variation causes unwanted technical variability (noise) and makes it harder to detect the effect of interest. Blocking is the experimental design choice to assign the experimental units (e.g. MS runs) to different “blocks” (e.g. batches, periods in time) in such a way that the treatments that need to be compared are present within each block. This enables to estimate the treatment effect within each block, in which the noise is lower. Blocking is therefore a way of removing unwanted variability and thus increases the power of a statistical analysis. In the CPTAC dataset, we retained the data from three different laboratories. Since the between-lab variability is not of interest, “lab” can be considered as a blocking factor, which allows to remove the between-lab variability from the analysis.

Note that there are issues with ionization competition in the CPTAC dataset [421]. Due to the relatively high spike-in concentrations of the UPS1 mix, ionization of UPS1 peptides will partially suppress the intensities of the yeast peptides. This might lead to the false positive calling of yeast proteins as DA. We indeed noticed that most quantification methods could not control their quantification false discovery rates at the 5% level when large differences in spikein concentrations were compared [422]. Fig. 3.5 gives an overview of CPTAC Study 6, which was used in all my first-author manuscripts.


**Figure 3.5.** Overview of the subset of the CPTAC Study 6 that will be used throughout this thesis. Digested human UPS1 proteins were spiked in five different concentrations (6A – 6E) into digested

> 30 “Lab 65” analyzed the samples on two diffe rent machines

47

yeast ( _Saccharomyces cerevisiae_ ) proteome. These samples were sent to three different laboratories. Each laboratory analyzed the samples in technical triplicates.

Other, more recent spike-in datasets were published in Ramus _et al._ (2016) [423] and Jarnuczak _et al._ (2016) [330].

There might be some confusion on the usage of the term “sample”. In this section, I denoted the different spike- in conditions as “samples”, which were repeatedly analyzed. However, in a biological experiment, multiple samples will be taken for each treatment condition of interest and each of these samples will be analyzed in one or more technical replicates on the mass spectrometer. Because of the ever-increasing sequencing depth, technical replication is often omitted in modern experiments, which causes each “sample” to correspond to a single MS ru n. In the literature, indicators referring to “sample” or “MS run” are therefore almost always used interchangeably. To avoid confusion, I will use the terms “condition” or “treatment” to refer to the spike-in conditions from now on.

48

## **4. DIFFERENTIAL PROTEIN ABUNDANCE ANALYSIS**

Once peptides are identified, linked to a protein and assigned an intensity value, the data can be used for the analysis of differential protein abundance. In this chapter, I will go deeper into the different steps in a typical differential protein abundance analysis workflow. I will start with data preprocessing, followed by a demonstration of the most important methods to use the preprocessed data for differential protein abundance analysis.

### **4.1. Preprocessing**

Because of the nature of the peptide-level data described in section 3.4, preprocessing is required before proteins can be quantified. There is a plethora of preprocessing workflows and many of these are often constructed _ad hoc_ . Nonetheless, in most workflows, the data typically undergo some kind of (log-)transformation, filtering, normalization, imputation and summarization. Note that the order in which each of these preprocessing steps are executed impacts on the final results. Transformation, in principle can be executed at any stage in the preprocessing workflow, but typically occurs early because it makes the data easier to handle. Similarly, filtering is done early in the workflow to remove those observations that are deemed unreliable and/or unwanted for various reasons. Furthermore, Karpievitch _et al._ (2012) showed that normalization followed by imputation generally outperforms imputation followed by normalization [424]. The rationale behind this is that imputing missing values obscures possible bias trends and therefore renders normalization less efficient. Moreover, imputing missing values does not make sense when unaccounted systematic bias is still present in the data. Finally, data summarization is best done after imputation as it is much more difficult to summarize data that contains missing values [425]. Nonetheless, some workflows, such as the default MaxQuant-Perseus workflow impute the data only after summarization (see 4.1.4). In this section, I discuss each of the preprocessing steps in more detail.

#### **4.1.1. Transformation**

The distributional properties of raw intensity measurements are often unfavorable for direct statistical modeling. Therefore, nearly every quantitative proteomics workflow involves a transformation of the raw intensity values. Log-transformation is a logical choice because raw intensity and concentration measurements are often more or less log-normally distributed: their values are always positive, they are skewed to the right and their variances increase with the mean. The strong right-skewness of the raw intensities is shown in Fig. 4.1: there are many relatively low intensities and only a few very high intensities. After log-transformation, the distributions become much more symmetrical.

49


**Figure 4.1.** Impact of log2 transformation on the raw peptide intensities in the CPTAC dataset _[426]_ . Left: the densities of the raw peptide intensities are strongly skewed to the right. Right: the densities of the log2-transformed peptide intensities are much more symmetrical. The densities are colored according to lab: red corresponds to the orbitrap at site 56, yellow to the orbitrap at site 65 and blue to the orbitrap at site 86.

Moreover, the variance structure of the raw intensities is often multiplicative: the variability in the data tends to be higher for higher intensities than for lower intensities (Fig. 4.2). Logtransformation will stabilize the variances by transforming a multiplicative error structure into an additive error structure [263]. In an additive error structure, the variability in the data is independent of the mean. The statistical property of equal variances is called homoscedasticity (as opposed to heteroscedasticity: unequal variances). The assumption of homoscedasticity opens the way to use the standard toolbox for statistical inference, such as linear regression. Such classic inference methods often provide closed-form solutions for their estimators, which makes the estimation procedures much simpler and faster. In practice, there sometimes remains a mildly positive mean-variance correlation in the log2-transformed intensities.


**Figure 4.2.** Raw intensities (left) and log2-transformed intensities (left) of peptide NVNPVALPR, which is part of the human UPS1 protein P08311 (cathepsin G) in the CPTAC dataset [426]. The variability in the peptide’s raw intensities increases with higher spike -in concentrations but remains constant for the log2-transformed intensities.

50

A final argument in favor of the log-transformation is that by modeling PSM intensities at the log-scale, one models proportional differences at the biological scale, which is also more relevant from a biological point of view. Most researchers choose a log-transformation with a base of 2. A one-unit increase in log2-abundance will then be equivalent with a factor 2 increase in protein abundance.

#### **4.1.2. Filtering**

The data are filtered prior to differential analysis to remove peptides and proteins that are _a priori_ uninformative from a biological or statistical perspective. Removing uninformative peptides increases the power to detect differential abundance in their corresponding proteins. Removing uninformative proteins reduces the number of proteins that needs to be tested for differential abundance. This will result in a less severe multiple testing correction and thus in a higher statistical power [427].

Examples of peptides or proteins that are typically filtered out include:

- decoy peptides

- typical contaminants such as keratin, which originate from the operator’s skin amongst others

- other highly abundant and possibly less informative proteins (e.g. RuBisCo in plant samples)

- shared peptides, being peptides that map to more than one protein. Sometimes, these shared peptides are assigned to a protein (group) with the most unique peptides, but this practice should be discouraged because a shared peptide’s intensity could very well represent the combined intensity of multiple proteins.

- proteins or peptides identified in only a few samples

- proteins identified with only one or a few unique peptides (e.g. the two-peptide rule)

- - proteins for which no peptides without a modification site are identified. The rationale here is that the identification FDR is more difficult to calculate for a peptide carrying a modified site or amino acid mutation. Some search engines, such as MaxQuant, are less certain about the identification of a peptide with a modification and prefer to filter out proteins that are identified with only modified peptides, rather than doing inference on a protein of which they are less certain that it is really present in the data.

- peptides with very variable retention times over different runs, as this might be an indication for misidentification [428].

According to the vignette of the R package genefilter [429], a good filtering criterion should adhere to three criteria:

1. It should be statistically independent from the test statistic under the null hypothesis (i.e. the protein is not differentially abundant).

2. It is correlated with the test statistic under the alternative hypothesis (i.e. the protein is differentially abundant).

3. Filtering based on the criterion does not notably change the dependence structure (if it exists) of the joint test statistics.

The second property provides a benefit for filtering as it enriches for differentially abundant proteins after filtering. The first and the third criterion are necessary to keep control over the false discovery rate of the subsequent analysis at the pre-specified level (see 4.2.5). Indeed, as long as these criteria are fulfilled, filtering will not result in a biased analysis. The

51

aforementioned filtering procedures all fulfill the first criterion<sup>31</sup> . However, filtering on a criterion such as fold change estimates would induce a biased downstream quantification, as the fold change is an integral part of almost every test statistic and hence strongly correlates with it, also under the null hypothesis. The effect of filtering on different quantification methods has been studied in Belouah _et al._ (2019) [430].

#### **4.1.3. Normalization**

Even in a very clean, synthetic dataset as CPTAC, where there is no biological variability and only the spiked 48 UPS1 proteins are differentially abundant, the marginal peptide distributions are quite distinct. Considering all proteins in the dataset, there are considerable effects between samples with different spike-in concentrations, even within the same lab (Fig. 4.3, left). Moreover, for replicate measurements of the same samples, there is considerable lab-tolab variability, and even the within-lab variability is non-negligible (Fig. 4.3, right).


**Figure 4.3.** Left: density plot of the log2 peptide intensities for the orbitrap at site 65 in the CPTAC dataset [426]. The densities are colored according to spike-in condition (black: spike-in condition 6A, dark red: spike-in condition 6B and green: spike-in condition 6C). Right: density plot of the log2 peptide intensities for spike-in condition 6A. The densities are colored according to lab (red: orbitrap at site 56, yellow: orbitrap at site 65 and blue: orbitrap at site 86).

Normalization aims to remove, or at least dampen, this potentially large, unwanted variability. Center mean and center median normalization subtract the respective means or medians from each distribution (Fig. 4.4). These simple normalization approaches aim to remove nonbiological variability by centering the peptide intensity distributions and do not impact on their shapes [431]. However, it is clear from Fig. 4.4 that the shapes of the distributions are also affected by technical variability. Hence, more advanced normalization procedures are needed.

A method that has proven to work well for microarray data is quantile normalization [432, 433]. Quantile normalization will impose the same density distribution upon each MS-run. Here, the peptide intensities are sorted from low to high. The lowest peptide intensity for each run is then set equal to the mean of the lowest peptide intensities over these runs. Similarly, the secondlowest peptide intensity in each run will be equal to the mean of the second-lowest peptide

> 31 In practice, criterion 3 is rarely problematic, as most filtering procedures do not noticeably change the correlation structure of the tests [429].

52

intensities in each run, and so on. Missing values are handled based on the assumption that the data are missing at random.

Linear regression is a versatile statistical framework that can also be used to normalize the data (more about linear regression in section 4.2) [424, 434, 435]. VSN normalization is an example of a regression-based normalization approach that simultaneously executes transformation and normalization [436]. In brief, VSN normalization assumes that the different raw intensities from the different MS runs can be brought onto the same scale through linear mappings. VSN normalization assumes that the variance of the raw intensities 𝜐𝑝 depends on the mean 𝜇𝑝 as follows:


with 𝑐3 > 0. Based on these assumptions, a transformation ℎ is proposed such that the variance is approximately independent of the mean. Then, the following statistical model is proposed:

ℎ𝑟(𝑌𝑝𝑟) = 𝜇𝑝 + 𝜀𝑝𝑟,                                                                                                                                    (Eq. 4.2)

for all 𝑝∈𝑝<sup>null</sup> . Here, 𝑌𝑝𝑟 is the raw intensity for peptide 𝑝 in MS run 𝑟, and 𝑝<sup>null</sup> is the set of non-differentially abundant peptides. The parameters of the model are estimated with a least trimmed sum of squares regression under the assumptions that E[𝜀𝑝𝑟] = 0 and that the variance of the error term is constant: Var[𝜀𝑝𝑟] = 𝜎<sup>2</sup> . A more detailed explanation of the VSN algorithm can be found in Huber _et al._ (2002) [436]. Both older and more recent publications that compared the performance of different normalization methods seem to indicate that linear regression-based methods, such as VSN, generally outperform other normalization methods [435, 437, 438], although the relative performance of different normalization methods is also strongly dataset-dependent [439].

53


**Figure 4.4.** Overview of the effects of different types of normalization on the peptide intensity distributions in the CPTAC dataset [426].

The MaxLFQ summarization algorithm described in 4.1.5 combines summarization with normalization, although MaxLFQ summaries are sometimes still normalized afterwards.

An important assumption of all these normalization approaches is that the abundance of the large majority of the peptides remains unchanged over the different treatments. This assumption is often reasonable because researchers are mostly interested in biological perturbations that affect very specific pathways in the cell, thus affecting a minority of proteins. Moreover, most normalization methods can tolerate quite large fractions of differentially abundant peptides, as long as there is a more or less equal number of up- and downregulated peptides. This premise is also quite reasonable since the total amounts of peptides (in µg) analyzed in each run are as equal as possible.

The assumption of no major changes in the bulk of the proteome is however problematic for specific studies. For example, in AP-MS studies, proteins are purified that specifically interact with a protein of interest (bait). The control group contains only “background proteins”, i.e. proteins that non-specifically interact with the bait. Therefore, a large fraction of the identified proteins is more abundant in the samples with the bait, while the background proteins are, in

54

theory, equally abundant between control and bait samples. In such kinds of experiments, normalization should be performed with extreme caution [407].

Note that even though normalization intends to remove the overall run-to-run variability, considerable block effects can persist at the level of the individual peptides. Fig. 4.5 shows a multidimensional scaling (MDS) plot after quantile normalization for the CPTAC dataset. Even with a radical normalization method like quantile normalization, which literally forces the log2transformed intensity distributions to be equal in each MS run, the runs clearly cluster together per lab. This demonstrates that it will be necessary to also correct for blocking effects further down the analysis pipeline.


**Figure 4.5.** Multidimensional Scaling (MDS) plot after quantile normalization for the CPTAC dataset [426]. The MDS plot shows each MS run in such a way that the distance between each pair of runs is equal to the root-mean-square deviation for the top 500 peptides that are the most distinct between the pairs of runs.

#### **4.1.4. Imputation**

To demonstrate the important aspects of missingness, we investigated the amount of missing values at the peptide level in 73 recent label-free shotgun proteomics datasets. We showed that on average 44% of all values at the peptide level are missing (see chapter 10). To cope with such large amounts of missing values, they are often replaced with substitute values in a process called imputation.

Classically, three types of missingness can be defined: missingness completely at random (MCAR), missingness at random (MAR) and missingness not at random (MNAR) [440]. MCAR assumes that the missing values cannot be explained by the nature of their underlying true values, nor by any known covariate: every value in the data matrix has an equal probability of being missing. MAR is a type of missingness whereby the probability of an observation to be missing is dependent on one or more observed covariates, but independent of the nature of the underlying values themselves. MNAR are all cases where the missingness is dependent on the underlying values (and optionally also on one or more known covariates): some values (e.g. very low values, very high values) have a higher probability of being missing than others.

Missingness in label-free shotgun proteomics datasets is a combination of missingness completely at random (MCAR) (e.g. an enzymatic modification in one experimental condition

55

might cause a peptide to be unidentified if that modification was not accounted for during the search), missingness at random (MAR) (e.g. certain peptide sequences ionize more easily than others; therefore, missingness is much more likely for poorly-ionizing peptides) and missingness not at random (MNAR) (e.g. more abundant peptides simply have a higher chance of getting fragmented and thus being identified).  Note that this MNAR is exacerbated as the probability for a peptide to be identified is also context-dependent: when co-eluting with many other highly abundant peptides, a peptide will have a smaller chance of getting identified than if these other peptides would be absent or lower in abundance.

When choosing an imputation strategy, it is important to keep in mind the assumptions of that imputation strategy as most imputation strategies make use of either a MCAR or a MNAR assumption, but not both.

k-nearest neighbors (kNN) imputation is an example of an MCAR imputation strategy. In kNN, a Euclidean distance metric is calculated on all peptide intensities. Based on this distance matrix, the _k_ most similar peptides (neighbors) are identified for each peptide that has at least one missing value. All missing values for that peptide are then imputed with the average of the corresponding (non-missing) values from the _k_ neighbors [441, 442].

Quantile Regression Imputation of Left Censored data (QRILC) imputation is an example of an MNAR-based imputation strategy [443]. In QRILC, missing values are imputed with random draws from a truncated distribution with parameters that are estimated using quantile regression. QRILC has been implemented in the MSnbase R/Bioconductor package for manipulation, processing and visualization of proteomics data [444].

The popular proteomics computational platform Perseus also makes use of an MNAR-based imputation strategy. In Perseus, imputation is achieved by imputing the data with random draws from a rescaled, down-shifted normal distribution [445]. The characteristics of this distribution are calculated based on the data. More specifically, its mean is equal to the average of all the observed data minus _d_ times the standard deviation of the observed data. Its standard deviation is equal to _w_ times the standard deviation of the observed data. The default values for _w_ and _d_ are 0.3 and 1.8, respectively.

The current version of the popular Bioconductor package MSstats (version 3.12.2) [446] uses a more advanced, model-based approach to impute missing values under a MNAR assumption. <mark>Their accelerated failure time (AFT) model (</mark> see 4.2.3) <mark>does not incorporate a random missingness component as the authors argue that due to the improved technology, the proportion of random missing values has become negligible.</mark>

Choosing for no imputation, MCAR-based imputation or MNAR imputation can have a big impact on the downstream analysis. For example, the MCAR-based kNN is more suited when the majority of the missing values is not intensity-dependent [447]. Contrary, MNAR-based methods like QRILC, Perseus and AFT model imputation, perform better in a context with relatively more intensity-dependent missing values. These MNAR-based methods might however perform poorly in detecting special cases, e.g. where a long isoform of a certain protein is absent, but a smaller isoform is strongly upregulated (Fig. 4.6). In such cases, imputation with low-intensity values might dilute the signal and obscure the classification of the given protein as DA.

56


**Figure 4.6.** Imputation with low-intensity values can dilute signals present in the data. In this theoretical example, a protein consisting of 6 tryptic peptides is present in the left condition, while only a short isoform of the same protein giving rise to tryptic peptides 1 and 2 is 4 times more abundant in the right condition. When assessing peptides 1 and 2, the protein log2 fold change is equal to 2. However, imputing the missing values ( “not assigned”, NA) with either MCAR or MNAR methods will dilute this signal.

Indeed, although imputing missing peptide values was suggested in the proteomics literature, imputation should always be used with caution. When nothing is known about the nature of the missing values, it has been suggested to use MCAR imputation approaches based on local similarity, as these perform well on average [424]. It has to be noted however, that the performance of an imputation approach is highly dataset-dependent [422, 447-449]. In reality, missing values are often caused by an unknown mix of intensity-dependent and -independent mechanisms, which is strongly dataset-specific [424, 447] and choosing the wrong imputation method for the dataset at hand can result in a severe backlash in performance [422].

Some imputation methods try to combine MCAR and MNAR imputation. For example, one of the imputation strategies in the DEP Bioconductor package by Smits and Huber suggests an imputation method whereby proteins for which the values are completely missing in one or more experimental conditions are imputed with a MNAR method, while the other missing values are imputed with a MCAR method [450]. However, this distinction is rather arbitrary, since for some proteins, all values in an experimental condition might also be missing due to random chance. Conversely, some missing values for proteins which are detected in all experimental conditions might still be due to low intensities.

A final issue with imputation is that, even if the true mechanism of missingness would be known, the uncertainty caused by replacing a missing value by a fixed value from a certain distribution is essentially ignored. A correct data analysis strategy should take this uncertainty into account. This problem might be solved by using a multiple imputation strategy [451, 452] in which the dataset is imputed multiple times and each of these imputed datasets is subsequently analyzed. The variability in the outcomes gives a good idea of the impact of the imputation on the analysis. Unfortunately, multiple imputation has not yet been widely adopted in the field. Note that it is also possible to model mechanisms of missingness explicitly (see section 4.2.3) [440].

#### **4.1.5. Summarization**

As noted in section 3.4, differential analysis mostly takes place at the protein level, but the data are at the peptide level. Therefore, most workflows involve some kind of summarization. In this section, I will focus on peptide- to protein-level summarization to show the effects of different summarization techniques. A simple way to summarize is by summing up all raw peptide intensities that correspond to each protein in each MS run [453]. Alternatively, mean summarization involves taking the mean of the peptide intensities to obtain a protein-level summary. Median summarization is also very common as a median is insensitive to outlying peptide intensities [384]. For the same reason, weighted means [454, 455] or medians [456],

57

whereby the outlying peptides are given less weight, or trimmed means [299] have also been proposed.

Although these techniques are very simple to apply, one needs to consider a few things. The first one is the intensity-dependent missingness. Indeed, in samples with a high concentration of a particular protein, more of its poorly ionizing peptides are expected to be found compared to samples with a lower concentration of that protein. However, such poorly ionizing peptides reduce the protein concentration estimates in the samples where the protein is highly abundant. Therefore, a naive mean or median summary that does not correct for peptide ionization efficiency produces fold change estimates that are biased towards 0. This fold change bias is demonstrated in Fig. 4.7.


**Figure 4.7.** Effect of intensity-dependent missingness on mean and median summarization. The figure shows the log2-transformed intensities for all identified peptide sequences of a UPS1 protein in the CPTAC dataset [426] in the low spike-in condition 6A (black) and the higher spike-in condition 6C (green and blue). Symbols denote different labs (plus: site 56, triangle: site 65, circle: site 86). All peptides identified in condition 6A were also identified in condition 6C. Blue are the peptides which are exclusively identified in condition 6C. Full lines denote the mean summaries, dashed lines the median summaries. The black lines are the summaries for condition 6A, the blue lines the summaries for condition 6C. The green lines are the summaries for condition 6C when the peptides exclusively identified in condition 6C (blue) are omitted. Omitting those peptides increases both the mean and median summaries for condition 6C.

To avoid this issue, it is of course possible to base the protein summaries only on the overlapping peptides. However, when many different conditions are compared, the number of peptides that is identified in every condition tends to be very low, which makes it impossible to obtain such a protein-level summary for many proteins in the dataset.

MaxLFQ, the algorithm that is used to summarize proteins in MaxQuant, addresses this issue by making use of only those PSMs that overlap between each pair-wise MS run comparison. [317]. A schematic overview of the MaxLFQ algorithm is given in Fig. 4.8.

58


**Figure 4.8.** (A) Example of a protein of which five peptide sequences (indicated in magenta) are detected. (B) These five peptides were identified as seven different PSMs (“peptide species”). (C) Occurrence of each of the seven PSMs in 6 exemplary samples A – F, each of which was run once on the mass spectrometer. (D) Matrix with the pairwise protein ratios. Protein ratios are calculated by taking the median of all valid normalized pair-wise PSM ratios. Valid protein ratios are ratios for which two or more PSMs are in common between both runs (green). Protein ratios for which less than two PSMs are in common are considered invalid (red). (E) System of equations that needs to be solved to obtain the MaxLFQ protein intensities per run. MaxLFQ intensities for runs for which no valid protein ratios exist (e.g. run F) will be set to zero (i.e. a missing value on the log-scale). (F) Run-wise MaxLFQ protein intensities for the given protein. MaxLFQ intensities are calculated by solving the equations in (E) through least squares and rescaling the result to maintain the total summed intensity over all runs. Image adapted from Cox _et al._ (2014) [317], © 2014 by The American Society for Biochemistry and Molecular Biology, Inc., CC BY 4.0.

The rationale behind MaxLFQ is the following:

The intensity for each PSM is calculated as the area under the isotopic envelope at the maximum intensity over the retention time profile multiplied by a run-wise normalization factor. These normalization factors are calculated by least-squares minimization of the overall pairwise log fold changes for all PSMs between all runs. As with most normalization methods, the assumption is made that the large majority of the proteome is not differentially abundant.

Then, the common PSM intensities between each run pair 𝑞 and 𝑟 are used to calculate PSM ratios. The pair-wise protein ratio 𝜚𝑞𝑟 between runs 𝑞 and 𝑟 is then equal to the median of all pair-wise PSM ratios between runs 𝑞 and 𝑟.

59

Based on all pair-wise protein ratios, it is then possible to calculate log-transformed proteinlevel intensities 𝑦𝑞 for each run 𝑞. This is done by performing the following protein-wise leastsquares analyses for each “valid” pair of runs 𝑞 and 𝑟:

log 𝜚𝑞𝑟 = 𝑦𝑟 −𝑦𝑞 + 𝜀𝑞𝑟                                                                                                                              (Eq. 4.3)

Herein, 𝜚𝑞𝑟 is the pair-wise protein ratio between runs 𝑞 and 𝑟, 𝑦𝑞 the log-transformed protein intensity in run 𝑞 and 𝑦𝑟 the log-transformed protein intensity in run 𝑟.  𝜀𝑞𝑟 is a random error term. Pairs are considered valid if they have at least two PSMs in common. Finally, the whole profile of the estimated run intensities 𝑦̂𝑞 is rescaled to maintain the total summed intensity for a protein over all runs. Important to note is that in this procedure, summaries are calculated solely based on the PSMs that are common between each pair of runs. Therefore, MaxLFQ does not suffer from a downwards bias in its summary estimates.

It is also possible to reformulate the summarization problem as follows:

𝑦𝑓𝑟 = 𝛽<sup>0</sup> + 𝛽𝑓feature + 𝛽𝑟run + 𝜀𝑓𝑟,                                                                                                           (Eq. 4.4)

Herein, 𝑦𝑓𝑟 is the log-transformed intensity for PSM (feature) 𝑓 in run 𝑟, 𝛽<sup>0</sup> is the intercept, which corresponds to the average log-transformed intensity of a certain reference PSM in a certain reference run. 𝛽𝑓feature is the effect of PSM 𝑓 relative to the intercept and 𝛽𝑟run is the effect of run 𝑟 relative to the intercept. 𝜀𝑓𝑟 is a random error term. The MaxLFQ procedure is in fact an _ad hoc_ procedure to fit such a model for the ratio 𝑦𝑓𝑟/𝑦𝑓𝑞, conditional on all PSMs 𝑓 that are in common between runs 𝑞 and 𝑟. The disadvantage of the MaxLFQ procedure is that if the PSM overlap between runs 𝑞 and 𝑟 is very limited, the MaxLFQ estimates become very imprecise. This is the reason that MaxLFQ requires an overlap of at least two PSMs before allowing a ratio to be valid.

It is however more efficient to fit model (Eq. 4.4) as it is, as this model uses the information in all the PSMs, not only those that overlap, and still corrects for peptide-specific effects thanks to the 𝛽𝑓feature effect. 𝛽0 + 𝛽𝑟run can then be interpreted as the average protein intensity in run 𝑟 for the reference PSM.

Median polish [457, 458] is a robust way of fitting model (Eq. 4.4) that is also implemented in the current version of MSstats, but still seems show a slightly downwards bias. MaxLFQ, conversely,  produces nearly unbiased protein-level estimates (Fig. 4.9).

60


**Figure 4.9.** Overview of the log2 fold change estimates between condition 6C and 6A for the 36 UPS1 proteins for which these estimates could be calculated based on log2-transformed PSM-level intensities with four different summarization methods: mean summarization, median summarization, median polish and MaxLFQ. The red line denotes the true log2 fold change based on the known spike-in concentrations (2.2 fmol/µL for 6C, 0.35 fmol/µL for 6A). Mean and mean summarization strongly underestimate the true fold change. Median polish shows a smaller downwards bias, while MaxLFQ is nearly unbiased.

To avoid the downwards bias introduced by intensity-dependent missingness, MSstats imputes the data under a missing-by-low-intensity assumption prior to median polish summarization. However, such an assumption is not always valid, as already discussed in 4.1.4.

Note that both MaxLFQ and MSstats start from PSM-level intensities without taking into account the fact that PSMs mapping to the same peptide sequence are correlated.

### **4.2. Methods for differential protein abundance analysis**

Differential analysis here aims at identifying those proteins that are differentially abundant. In proteomics, there are three main methods to perform differential analysis: summarizationbased methods, counting-based methods and peptide-based methods. However, differential analysis is only meaningful if the design of the study allows for it. Therefore, I will start this section with a note on the importance of the study design.

#### **4.2.1. The importance of study design**

In its early days, mass spectrometry was tedious, time-consuming and costly. The main reason for this was the low duty cycle of the mass spectrometers, implying that, within a given time frame, very few peptides got selected for fragmentation and could thus be identified. Intelligent approaches such as MudPIT [119] and ICAT [459], countered this by peptide pre-fractionation or by selecting for so-called protein-representative peptides respectively. The former increased the overall analysis time, whereas the latter relied on expensive reagents that also tended to interfere with peptide fragmentation and peptide identification. Hence, samples were often analyzed only once on mass spectrometers . Proteins were then declared “significant” solely based on a fold change threshold [241, 243]. Publications using this approach are sometimes still accepted in high-impact journals [460]. Alternatively, a normal distribution was fitted to all fold change estimates and fold changes for proteins in the upper and lower 2.5% quantiles

61

were declared “significant” [455, 461]. Some authors even developed advanced empirical Bayes methods to deal with single-run experiments [462]. However, these methods provide little to no evidence about which proteins are truly differentially abundant. Indeed, with no information on the biological variability between biological repeats, it is impossible to assess how an estimator varies from experiment to experiment. For all we know, a protein with a very high fold change estimate can be in fact a protein whose abundance is highly variable, but unrelated to the studied treatment [463]. Hence, experiments without biological repeats make it impossible to infer the results towards the population. It is thus of utmost importance to design a study in such a way that samples are included from multiple, independent subjects from the population on which one aspires to do inference. For instance, if properly conceived, a study containing only BALB/c mice should provide results that are valid for all BALB/c mice. However, if a researcher wants to extrapolate these results towards other mice strains, he or she should have included at least a few different mouse strains in his/her experimental design. Fig. 4.10 demonstrates how different levels of replication contribute to the total variability in the system.


**Figure 4.10.** Different levels of replication do not contribute equally and independently to the total variability in the system. In the given example, there are two biological levels of replication (animal and cell) and one technical level of replication (measurement). Although the average expression of all animals in the population is equal to 10, each of these replication levels contributes to the total measurement variability by introducing, in this example, a random error that follows a normal distribution with variances 1, 2 and 0.5 respectively (the corresponding standard deviations are shown as horizontal lines). Note that in proteomics data, these levels of replication hold for every single protein. Moreover, proteomics data has multiple levels of technical replication: MS run, peptide and PSM, as discussed in section 3.4. Reprinted with permission from Blainey _et al._ (2014) [464], copyright © 2014, SpringerVerlag.

Still too often, researchers limit themselves to conducting a few “biological” replicates on the same cell line, often from the same vial, or worse, they run only one sample in a few technical replicates on the mass spectrometer. In the first case, the results can only be extrapolated to that specific cell line in that specific lab, but at least, the experimental variability was taken into account (i.e. difference due to slightly different handling of the cells, a slightly different temperature because the repeats were performed on a different day, etc.). In case only technical replicates are used, the results can only be extrapolated to that specific sample.

62

These types of improper study designs are, in my opinion, one of the reasons for the replication crisis that plagues the biological sciences. An extensive overview of the statistical considerations to bear in mind when designing an MS-based proteomics experiment can be found in Oberg and Vitek (2009) [465].

#### **4.2.2. Summarization-based methods**

Summarization-based methods for differential analysis start from protein-level summaries. In this section, I will explain a few of the most commonly used methods.

Perseus is one of the most popular software packages amongst mass spectrometrists to perform differential analysis [445]. It seamlessly imports MaxQuant output and is equipped with a user-friendly GUI that allows for a variety of data manipulations, statistical analyses and visualizations.

Perseus’ default way to perform differential analysis between two groups is via t -tests on MaxLFQ-summarized, log2-transformed and preprocessed protein intensities. A t-test relies on three assumptions:

1. Independence. The information about any of the observations does not provide additional information about any of the other observations after correction for the treatment. This implies that all observations should be at the same level of hierarchy and that no pair of observations can be assumed (by design) to be more similar to each other than any other pair of observations (after correction for the treatment).

2. Normality. The normality assumption demands that the observations in both conditions are realizations of a normally distributed population.

3. Homoscedasticity. Homoscedasticity or equality of the variances means that the population variances in both conditions are equal. When the homoscedasticity assumption is not met, it is however still possible to use the Welch two-sample t-test (see below).

If the rigid assumptions of the t-test are not met, there is no guarantee that the inference will be correct. In practice, however, researchers seldom assess these assumptions, especially in high-throughput omics contexts. The rationale behind a t-test is to weigh the fold change of a protein by its natural variability in abundance. Indeed, as explained above, a high fold change is not very meaningful if a protein’s abundance is very variable from sample to sample (Fig. 4.11).

63


**Figure 4.11.** Illustration of signal and noise. If the signal increases, the confidence that a protein is differentially abundant between the green and the black condition will also increase. However, if for a constant signal, the noise increases, the confidence that a protein is differentially abundant will decrease. Hence, the signal-to-noise ratio is an ideal statistic to assess differential abundance.

The t-test will wrap the ratio of signal (fold change estimate) to noise (estimate of the variability in protein intensities) in a single test statistic 𝑡 that estimates the signal-to-noise ratio. The t- test statistic performs superior compared to the use of simple fold change cut-offs because it also takes the noise into account. More specifically, the t-test statistic is defined as follows:


Here, 𝑦̅1 is the average protein-level log2 intensity in the first treatment group, 𝑦̅2 the average log2 intensity in the second treatment group, 𝑅1 the number of observations (MS runs) corresponding to the first treatment and 𝑅2 the number of MS runs corresponding to the second treatment. 𝑠 is the pooled variance estimate. It is calculated as follows:


Here, 𝑡= 1,2 is the indicator for each treatment and 𝑟= 1, … , 𝑅𝑡 the indicator for each MS run in a treatment. If the assumptions are correct, the test statistic follows a t-distribution with 𝑅1 + 𝑅2 −2 degrees of freedom under the null hypothesis. If only the homoscedasticity assumption is not met, it is possible to use the Welch two-sample t-test instead. This option is also foreseen in Perseus. A Welch two-sample t-test omits the pooled variance estimator and instead calculates the t-test statistic as follows:


With 𝑠12 and 𝑠22 the sample variances in both treatments. This test statistic no longer follows a t-distribution under the null hypothesis, but it can be approximated as a t-distribution with an adjusted number of degrees of freedom through the Welch-Satterthwaite approximation.

64

The null hypothesis of a two-sample t-test states that there is, in reality, no difference in the average log2 intensities between both treatments. Next, the calculated test statistic 𝑡 is confronted with the t-distribution (Fig. 4.12).


**Figure 4.12.** Illustration of the determination of p-values based on the t-test statistic. The p-value corresponds to the area under the t-distribution for which the t-statistic is as extreme as or more extreme than the observed t-statistic. The regions for which a t-statistic would be accepted and rejected at the 5% significance level given a t-distribution with three degrees of freedom are also given.

The percentile corresponding to the calculated test statistic can be easily converted into a p- value. This p-value denotes the probability that a new test statistic, calculated based on an independent repeat of the given experiment would be as extreme as, or more extreme than the observed test statistic, given that the null hypothesis is true. If this p-value is very small, it is not very likely to observe the given result under the null hypothesis. One then chooses to reject the null hypothesis and accept the alternative hypothesis, i.e. there is a real difference in the average log2 intensities between both treatments. The p-value threshold below which one chooses to reject the null hypothesis is called the significance level. Traditionally, this significance level is often set at 5%, but in fact, the choice of the significance level is up to the researcher. Other thresholds (e.g. 1%, 10%) can also be set, depending on the relative impact of falsely reporting non-differentially abundant proteins versus not reporting truly differentially abundant proteins.

In Perseus it is possible to use a moderated t-test statistic. This statistic is calculated as follows:


with:


Hence, an offset 𝑠0 is provided to the numerator of the t-test statistic. Providing a small offset reduces the impact of a protein’s variance estimate 𝑠. Indeed, sometimes it happens that, due to random chance, the protein level estimates in the dataset are not very variable. This will

65

result in a small pooled variance estimate 𝑠, and hence a high test statistic 𝑡 and a small p- value, even if a protein’s fold change is rather small. Such proteins, with very small fold changes, but significant p-values due to small variance estimates are often not of interest to the researcher. Adding the offset 𝑠0 stabilizes the test statistic. This procedure is known as significance analysis of microarrays (SAM) [466]. By adding the offset, the test statistic no longer follows a t-distribution and p-values are calculated by permuting the log2 protein intensities across all proteins over both treatments. The widespread use of the SAM procedure in the proteomics community, whereby 𝑠0 is arbitrarily chosen by the experimenter has been criticized as it may lead to biased quantifications [467].

The use of t-tests and SAM limits Perseus analyses only to two-group comparisons. Consider the CPTAC dataset as an illustration. When comparing condition 6C to condition 6A for example, the independence assumption of the t-test is violated. Indeed, samples that were analyzed in the same lab are more similar than samples that were analyzed in different labs. Therefore, each sample contains some information about the other samples from the same lab, thereby invalidating the independence assumption. Summarizing the data from the sample- to the lab-level seems like a solution, but besides the loss of information, this does not solve the problem that data from the same lab over different conditions are more similar than data from different labs over different conditions.

Therefore, the t-test should be expanded towards a more general framework: linear regression. In the linear regression framework, every observed outcome variable 𝑦𝑟 (with index 𝑟= 1, … , 𝑅 denoting the MS run) is assumed to originate from a linear combination of covariates 𝑥𝑟𝑚 and regression coefficients (also termed “parameters” or “effects”) 𝛽<sup>0</sup> and 𝛽𝑚 (with index 𝑚= 1, … , 𝑀 denoting the model parameters) summed with a random error term 𝜀𝑟 that covers the deviation of each observation 𝑦𝑟 from its expected value under the model:


The linear regression model has four assumptions:

1. Independence: Independence again denotes that none of the observations holds additional information about any of the other observations after correction for the covariates 𝑥𝑟1 to 𝑥𝑟𝑀.

2. Linearity: Linearity between the response and predictors means that the outcome variable varies linearly in function of the predictors 𝑥𝑟𝑚 and that there are thus no higher-order trends that cannot be accounted for. Linearity implies that the residuals (i.e. fraction of the data that cannot be explained by the predictors) have a mean of 0 and that they are orthogonal on the predictors.

3. Normality: The errors are assumed to be normally distributed, i.e. <mark>ε𝑟~N(0, 𝜎2).</mark>

4. Homoscedasticity: Homoscedasticity requires that the variance of the residuals is equal for each covariate pattern. This also implicates that are no trends in the spread of the residuals when the residuals are plotted in function of the fitted outcome values.

At a first glance, the linearity assumption seems to be rather restrictive for linear regression modeling. However, linear regression models can be easily adapted to capture higher-order (e.g. quadratic effects) or even non-parametric trends (e.g. splines).

Linear regression models are often written in a compact matrix notation:

𝒚= 𝑿𝜷+ 𝜺                                                                                                                                                 (Eq. 4.11)

66

For the CPTAC dataset, our aim is to compare the different conditions to each other. Therefore, separate linear regression models can be proposed for every protein 𝑖, whereby the proteinlevel log2 intensities are modeled in function of the spike-in conditions. By including lab effects, we also account for the blocked experimental design. As the peptide-level intensities are summarized to protein-level intensities in each run, we opt here to write an indicator 𝑟 for run instead of 𝑗 and we call 𝑅 the number of runs for which a protein-level summary could be determined for protein 𝑖. Ultimately, the matrices can be specified as follows for each protein 𝑖 in the CPTAC dataset, whereby the indicator 𝑖 is suppressed for notational convenience:


Here, 𝒚 is a vector containing all log2-transformed protein-level intensities 𝑦𝑟. The vector 𝜷 contains the effect sizes: 𝛽<sup>0</sup> is a constant intercept, which refers to the average log2transformed protein intensity in a certain reference condition 1 (e.g. spike-in condition 6A) in a reference lab 1 (e.g. LTQ-orbitrap at site 86). 𝛽2condition and 𝛽3condition are the effects of the second and the third spike-in conditions relative to the reference condition after correction for lab-effects. They can be directly interpreted in terms of log2 fold changes between their corresponding spike-in condition and the condition that was chosen as a reference condition. Given a certain spike-in condition, 𝛽2lab and 𝛽3lab denote the effects on the log2 protein intensity of the second and the third labs, respectively, relative to the reference lab. To model the discrete, non-linear effects of spike-in condition and lab, we make use of so- called “dummy” variables whereby e.g. 𝑥𝑟2condition is equal to 1 if run 𝑟 corresponds to the second spike-in condition and 0 otherwise. Idem for the other dummies. 𝜺, finally, is a vector that contains the random error terms 𝜀𝑟. For the CPTAC dataset, the regression model can then be written as follows: 3 3 condition𝛽𝑡condition lab𝛽𝑏lab + 𝜀𝑟                                                                  (Eq. 4.16) 𝑦𝑟 = 𝛽<sup>0</sup> + ∑𝑥𝑟𝑡 + ∑𝑥𝑟𝑏 𝑡=2 𝑏=2

67

Regression models that contain only categorical variables<sup>32</sup> are often presented in the more condense ANOVA notation whereby the predictor variables 𝒙𝒓 are not written explicitly, but indices are used instead to denote different levels of the categorical variable. For the CPTAC dataset, the ANOVA notation of the model can be written as follows:

<mark>𝑦</mark> 𝑡𝑏𝑟 <mark>= 𝛽</mark><sup>0</sup> <mark>+ 𝛽</mark> 𝑡condition <mark>+ 𝛽</mark> 𝑏lab <mark>+ 𝜀</mark> 𝑟 <mark>(Eq. 4.17)</mark>

Here, 𝑦𝑡𝑏𝑟 is the log2-transformed protein-level intensity for protein 𝑖 in MS run 𝑟, which corresponds to condition (treatment) 𝑡= 2,3 and lab (block) 𝑏= 2,3. 𝛽<sup>0</sup> is the constant intercept. 𝛽𝑡condition is the effect of condition 𝑡 relative to the reference condition, 𝛽𝑏lab the effect of lab 𝑏 relative to the reference lab and 𝜀𝑟 the random error term. The estimated condition effects 𝛽̂𝑡condition are the effects of interest.

The most common way to estimate the parameters is by least squares, i.e. by minimizing the sum of the squared distances of the observations to the model fit:

‖𝒚−𝑿𝜷‖<sup>2</sup> = (𝒚−𝑿𝜷)<sup>T</sup> (𝒚−𝑿𝜷)                                                                                                      (Eq. 4.18) This results in the following estimator for 𝜷: 𝜷̂ = (𝑿<sup>𝐓</sup> 𝑿)−𝟏𝑿𝐓𝒚                                                                                                                                     (Eq. 4.19)

In the least-squares context, the estimator for the variance of 𝜷̂ is given by:

Var̂(𝜷̂) = 𝜎̂<sup>2</sup> (𝑿<sup>𝐓</sup> 𝑿)−1                                                                                                                              (Eq. 4.20)

Herein, 𝜎̂<sup>2</sup> is an unbiased estimator for the error variance:

𝜎̂<sup>2</sup> =<sup><u>‖𝒚−𝑿𝜷̂‖</u></sup> 2 ,                                                                                                                                      (Eq. 4.21) 𝑅−𝑀

with 𝑅 the number of runs and 𝑀 the number of estimated parameters in the mean model. The estimator for the standard error on the 𝑚th parameter estimator 𝛽̂𝑚 can also be written as:

𝜎̂𝛽̂𝑚 = 𝜎̂√𝜐𝑚,                                                                                                                                              (Eq. 4.22)

with 𝜐𝑚 = (𝑿<sup>𝐓</sup> 𝑿)−1𝑚,𝑚 the 𝑚th diagonal element of (𝑿𝐓𝑿)−1. Under the null hypothesis of no differential abundance, the following test statistics follows a t-distribution with 𝑅−𝑀 degrees of freedom:

𝛽̂𝑚 −𝑎 ~𝑡𝑅−𝑀                                                                                                                                             (Eq. 4.23) 𝜎̂𝛽̂𝑚

Here, 𝛽̂𝑚 is the estimated value for the 𝑚th model parameter 𝛽𝑚 (typically the effect of a certain treatment; in the case of the CPTAC study: the spike-in condition), 𝑎 the value of 𝛽𝑚 under the null hypothesis (typically zero) and 𝜎̂𝛽̂𝑚 the estimated variance on the estimate of 𝛽𝑚. Given the null distribution, a p-value can be calculated for each parameter, denoting its statistical significance. Note that some research questions (e.g. the difference in protein abundance between two non-reference conditions) require statistical inference on a linear combination of

> 32 Categorical variables are variables that do not correspond to any measurable quantities. Examples include gender, different compounds, different treatments, etc. This is opposed to numerical variables that correspond to measurable quantities (e.g. doses of a certain compound, time after treatment, blood pressure,).

68

multiple model parameters, so-called statistical contrasts. Just as for single parameters, t- statistics and p-values can also be calculated for contrasts.

The current version (3.12.2) of the popular Bioconductor package MSstats makes use of linear regression at the protein level. These protein-level summaries are obtained after imputation at the PSM-level data under a MNAR assumption followed by a median polish summarization [446].

The popular Bioconductor package limma was originally developed for the analysis of microarray data [468], but has also become popular for differential proteomics analyses [469]. Limma makes use of the huge amounts of data in high-throughput omics datasets to borrow strength across proteins. More specifically, limma assumes that the residual variances from each regression model are composed of a common variance shared by all proteins (models) and a protein-specific variance. This allows to obtain a more stable estimate of the error variance, which is especially beneficial for proteins identified by only a few peptides. Indeed, their variances are stabilized by relying on the variances estimated for proteins with much more data.

Limma uses an empirical Bayes framework to provide a statistically sound alternative to SAM for linear regression models. More specifically, limma proposes a Bayesian model which assumes the following prior distribution on the error variance 𝜎𝑖2 for each protein 𝑖 (𝑖= 1, … , 𝐼):


In this formula, 𝜎02 is a prior variance and 𝜒𝑑20denotes a 𝜒2 distribution with 𝑑0 degrees of freedom. In limma, the user does not define the value of the prior variance 𝜎02 and the prior degrees of freedom 𝑑0, but estimates 𝜎02 and 𝑑0 based on all protein error variance estimates 𝜎̂𝑖2 and the degrees of freedom 𝑑𝑖 = 𝑀−𝑅 of all proteins in the dataset. Statistical inference methods whereby the priors are estimated based on the data are termed empirical Bayesian methods.

Limma’s empirical Bayes estimators for the prior variance 𝜎02 and the prior degrees of freedom 𝑑0 have closed-form solutions that are computationally very fast. Furthermore, instead of estimating full posterior distributions, limma calculates a maximum a posteriori point estimate 𝑠̃𝑖 for the residual standard deviations:


Herein, 𝜎̂𝑖 is the residual standard error for protein 𝑖 and 𝜎̂02 the estimated common variance over all proteins. Substituting the residual standard deviation by its maximum a posteriori estimator results in a moderated t-test statistic:


It can be shown that the moderated t-test statistic 𝑡̃𝑖𝑚 follows a t-distribution with 𝑑𝑖 + 𝑑0 degrees of freedom, with 𝑑𝑖 equal to 𝑅−𝑀, as indicated before. Hence, not only are the variances being stabilized as in SAM, but, contrary to SAM, the null distribution follows an analytical t-distribution. Note that the degrees of freedom of this t-distribution are augmented with 𝑑0 as compared to the degrees of freedom of the null distribution of the ordinary t-test.

69

This reflects the increased power of the moderated t-test due to the borrowing of strength across proteins.

#### **4.2.3. Peptide-based models**

Summarization-based approaches, especially the naive ones such as those based on mean and median summarization, use summary values that are based on different peptides and different numbers of peptides. When such summaries are compared to each other, a bias will be introduced due to the comparison of different peptides with non-negligible differences in ionization efficiency. Also, differences in precision due to the different numbers of peptides for each summary are ignored. Instead of summarizing PSMs directly to the protein level, it is however also possible to keep the data at the PSM or peptide-level and to include the hierarchical nature of the data directly into the statistical model. We call these models peptidebased models (see chapter 8). They have the advantage that they correct for differences in ionization efficiencies between different peptides and for differences in precision due to different numbers of identified peptides in each MS run. Compared to summarization-based methods, two additional parameters need to be added to the model. A peptide-based linear regression model for each protein 𝑖 in the CPTAC experiment then looks as follows (whereby the indicator 𝑖 is again suppressed for notational convenience):


peptide The response variable 𝑦𝑝𝑟<sup>is now the log2-transformed intensity of</sup><sup>_peptide_</sup> 𝑝 in run 𝑟. <mark>𝛽</mark> 𝑝 <mark>is added to account for the effect of the 𝑝</mark><sup>th</sup> <mark>peptide. T</mark> he effect for MS run, <mark>𝑢</mark> 𝑟run <mark>, is added because for protein 𝑖, there can be multiple peptides identified in the same run. This is an important point: the run effect needs to be included because peptide intensities within the same run are expected to be positively correlated. Indeed, due to the run-specific effects described in 3.4, peptide intensities from a protein within the same run will behave more similar compared to peptide intensities that were measured across different runs. However, if the run effect were modeled as a standard fixed effect, statistical inference would only be valid for within-run comparisons because the run-to-run variability would be removed from the model.</mark> When the run effect is modeled as a random effect, whereby it is assumed that <mark>𝑢</mark> 𝑟run <mark>~N(0, 𝜎</mark> 𝑢2 <mark>)</mark> , both within- and between-run variability are taken into account. This is important in label-free proteomics experiments because the treatment will vary between runs, but not within runs. <mark>The run effect thus both accounts for</mark> the correlation of all peptides of protein 𝑖 identified within run 𝑟 and enables a correct statistical inference for between-run comparisons. Statistical models that contain both fixed and random effects are referred to as mixed models and allow to model correlation structures in the data.  This mixed model structure for peptide-level data was first proposed by Daly _et al._ (2008) [470].

Clough _et al._ (2009) [471] propose a specific parameterization for protein-wise mixed models:

<mark>𝑦</mark> 𝑓𝑟 <mark>= 𝛽</mark> 0 <mark>+𝛽</mark> 𝑓feature <mark>+ 𝛽</mark> 𝑡condition <mark>+𝛽</mark> 𝑓𝑡feature:condition <mark>+ 𝛽</mark> 𝑏biorep <mark>+ 𝜀</mark> 𝑓𝑟 (Eq. 4.28)

These authors later implemented this model in the proteomics quantification package MSstats prior to version 3, in which MSstats used to model the data directly at the feature (PSM) level [409, 472].

Herein, <mark>𝛽</mark> 𝑓feature <mark>is the effect of the 𝑓th feature (PSM). 𝛽</mark> 𝑓𝑡feature:condition <mark>is an interaction effect between feature and condition. Such an interaction allows the effect of interest (condition) to affect each feature differently. 𝛽</mark> 𝑏biorep <mark>is then the effect of the 𝑏th biological repeat. In MSstats, the experimenter can opt to encode 𝛽</mark> 𝑏biorep <mark>either as a fixed effect, which is useful when 𝛽</mark> 𝑏biorep

70

<mark>is a blocking factor, or as a random</mark> effect, which is useful in the case of biological replication. Indeed, biological replication caused by e.g. multiple measurements on the same animals also leads to correlation in the data and should therefore be modeled as random. <mark>The disadvantage of the former MSstats framework is that it does not allow to correctly model the within-sample correlation unless the samples coincide with the biological repeats. Moreover, just like the present MSstats implementation, it only allows to model experiments that fit into this specific model framework.</mark>

It has to be noted that, if the summarization step is performed correctly, the estimated differences in ionization efficiencies can in fact be removed from the data. Hence, the only clear advantage of peptide-based models is that they account for difference in precision due to different numbers in peptides. However, this advantage seems to be rather small in practice, which may be one of the reasons why MSstats in their most recent version, reverted to a faster, summarization-based workflow.

<mark>The very first peptide-based model for label-free shotgun proteomics was proposed in 2008, when Bukhman</mark> _<mark>et al.</mark>_ <mark>proposed the following model [473]:</mark>


<mark>Herein, 𝑦𝑝𝑟</mark><sup><mark>is the log-transformed intensity of peptide</mark></sup> <mark>𝑝 in sample (or MS run, assuming each sample was only run once) 𝑟, 𝛾𝑝</mark><sup><mark>the background log-transformed intensity of peptide</mark></sup> <mark>𝑝, 𝜓𝑝</mark><sup><mark>the</mark></sup> <mark>peptide-specific effect of peptide 𝑝, 𝛿𝑖𝑝</mark><sup><mark>an indicator whether peptide</mark></sup> <mark>𝑝 maps to protein 𝑖 (1 if the peptide maps and 0 if the peptide does not map), 𝜃</mark> 𝑖𝑟<sup><mark>the abundance of protein</mark></sup> <mark>𝑖 in sample 𝑟 and 𝜀𝑝𝑟</mark><sup><mark>a random error term. The inclusion of the</mark></sup> <mark>𝜓𝑝</mark><sup><mark>term allows the sample effect</mark></sup> <mark>𝜃</mark> 𝑖𝑟<sup><mark>to be</mark></sup> <mark>different from peptide to peptide. Note that in this model, all proteins are modeled together and that this model allows to use shared peptides, although the authors exclude peptides that are shared by three or more proteins.</mark>

<mark>Another peptide-based model was proposed by Henao</mark> _<mark>et al.</mark>_ <mark>(2012) [474]:</mark>

𝑦𝑝𝑠𝑏 = 𝑚𝑝𝑏 𝑎𝑙𝑝𝑧𝑙𝑠 𝑏𝑖𝑝𝑤𝑖𝑠 + 𝜀𝑝𝑠 (Eq. 4.30) + ∑ + ∑ 𝑙 𝑖

<mark>Herein, 𝑦𝑝𝑠𝑏</mark><sup><mark>is the average log-transformed intensity of peptide</mark></sup> <mark>𝑝 in sample 𝑠 in batch 𝑏. 𝑚𝑝𝑏 is the average intensity of peptide 𝑝 in batch 𝑏. This model also accounts for the correlation of certain peptides within the same sample (e.g. peptides that behave similarly due to physicochemical similarities). To capture this correlation,  𝑧</mark> 𝑙𝑠<sup><mark>represents the</mark></sup> <mark>𝑙th intra-sample effect for sample 𝑠, while 𝑎𝑙𝑝</mark><sup><mark>are the peptide-specific effects that correspond to each of these</mark></sup> <mark>intra-sample effects. 𝑤</mark> 𝑖𝑠<sup><mark>represents the effect of interest: the effect of protein</mark></sup> <mark>𝑖 in sample 𝑠, while 𝑏𝑖𝑝</mark><sup><mark>models the impact of peptide</mark></sup> <mark>𝑝 on the effect of protein 𝑖. 𝜀𝑝𝑠</mark><sup><mark>is a random error term.</mark></sup> <mark>From the model specification, it is clear that this model will be strongly over-parameterized for most, if not all proteins. These authors, however, tried to tackle the quantification problem from a Bayesian perspective. In classic frequentist statistics, the aim is to estimate the true value of one or more unknown population parameters and provide estimates on the uncertainty of these parameter estimates. Contrary, in Bayesian statistics, the population parameters are</mark> _<mark>believed</mark>_ <mark>upfront to follow certain distributions, the prior distributions. When experiments are performed, evidence (data) is collected that might confirm or challenge this prior belief. The prior distributions are then updated based on the data by making use of Bayes’ theorem and result in posterior distributions that reflect the statistician ’s new beliefs after confronting his beliefs with the data.</mark>

71

<mark>T he idea of including a researcher’s beliefs into a statistical method is very sensible because experiments are rarely, if ever, performed without any prior knowledge. Indeed, even if nothing is k nown about a protein in the literature, a protein’s true log</mark> 2 <mark>fold change will either be 0 (unregulated), or a positive or negative value rather close to zero (up- or downregulated). Very extreme log</mark> 2 <mark>fold changes such as +1000 or -1000 are highly unlikely and can therefore be given a very low prior probability. And, even if absolutely nothing is known or can be assumed about an experiment and all values are equally likely, a so-called uninformative prior can be used. In this respect, the framework of Bayesian statistics is very elegant because it allows the posterior distribution of a previous experiment to be used as a prior distribution in a follow-up experiment and thus to organically update our beliefs based on the data.</mark>

<mark>Henao</mark> _<mark>et al.</mark>_ <mark>(2012) indeed place Gaussian (normal) priors on the average abundance 𝜇</mark> 𝑖𝑚<sup><mark>and</mark></sup> <mark>the noise component 𝜀</mark> 𝑖𝑛<sup><mark>[474]. Gaussian priors are also assigned to</mark></sup> <mark>𝑎</mark> 𝑖𝑙<sup><mark>, while a Laplace prior</mark></sup> <mark>is set on 𝑧</mark> 𝑙𝑛<sup><mark>to allow these intra-sample effects to shrink to 0 if necessary.</mark></sup> <mark>𝑏</mark> 𝑖𝑘<sup><mark>is also given a</mark></sup> <mark>normal prior, but hyperpriors are set in such a way that proteins can also be correlated with each other in a hierarchical tree structure. Bayesian models have also been proposed to include the effects of shared peptides [475].</mark>

<mark>Disadvantages of the Bayesian framework are that the choice of the prior is always somewhat arbitrary and based on the beliefs of the researcher. Moreover, Bayesian inference models mostly do not have a closed-form expression for the posterior distributions. Therefore, the posterior distributions need to be approximated by repeated sampling, e.g. by making use of Markov Chain Monte Carlo (MCMC) methods, which are computationally very intensive.</mark>

Another persistent issue in the proteomics field are missing values, hence the usual custom of including an imputation step in a typical workflow. Instead of imputing missing values, it is also possible to handle missing values within the framework of the statistical model. For shotgun proteomics data, this approach was pioneered by Karpievitch _et al._ (2009) [425]. In their censored regression model, peptide intensities are assumed to be either missing completely at random, or missing not at random if a peptide’s intensity falls below a certain censoring threshold <mark>𝑐𝑖𝑝</mark><sup><mark>for each peptide</mark></sup> <mark>𝑝 corresponding to protein 𝑖. These authors model all proteins together in one model. It is assumed that all log</mark> 2 <mark>-transformed intensities originate from a normal distribution with mean 𝜇𝑖𝑝𝑡</mark><sup><mark>and standard deviation</mark></sup> <mark>𝜎𝑖𝑝</mark><sup><mark>. The expected intensity for a</mark></sup> <mark>peptide 𝑝 of a protein 𝑖 in treatment condition 𝑡 can then be described as follows:</mark>


In each MS run 𝑟 <mark>, the probability of a peak to be missing at random is assumed to be equal to 𝜋</mark> 𝑟<sup><mark>. If</mark></sup> <mark>𝑊𝑖𝑝𝑡𝑟</mark><sup><mark>is the probability that a log</mark>2</sup><sup><mark>-transformed intensity</mark></sup> <mark>𝑦𝑖𝑝𝑡𝑟</mark><sup><mark>is observed (0 if observed</mark></sup> <mark>and 1 if unobserved), the probability that intensity 𝑦𝑖𝑝𝑡𝑟</mark><sup><mark>will be missing can be written as follows:</mark></sup>

In this expression, <mark>Φ is the cumulative distribution of the normal distribution with mean equal to 0 and standard deviation equal to 1. This expression shows that peptides are missing at random (MAR, conditionally on run 𝑟) with a probability 𝜋</mark> 𝑟<sup><mark>. Any peptide that is not MAR will be</mark></sup> <mark>MNAR if its log</mark> 2 <mark>-transformed intensity is lower than the peptide-specific censoring threshold 𝑐𝑖𝑝</mark><sup><mark>. The current implementation of MSstats uses a very similar model to impute missing values</mark></sup> <mark>prior to summarization to the protein level, albeit without the random missingness component [446]. In 2012, Koopmans</mark> _<mark>et al.</mark>_ <mark>proposed an empirical Bayesian random censoring threshold model to cope with missing values in a summarization-based context, but just like most</mark>

72

<mark>Bayesian inference models, the posterior does not have a closed-form solution and needs to be constructed by repeated MCMC sampling, which makes it computationally intensive [476].</mark>

#### **4.2.4. Ridge regression**

Due to low protein abundances, limited numbers of tryptic peptides per protein and the datadependent nature of the acquisition, the number of observed peptides is relatively small for most of the proteins in a typical label-free shotgun proteomics dataset. This makes proteinwise statistical modeling challenging because even relatively simple models are prone to overfitting for such proteins. Over-fitting occurs when a model is too complex with respect to the amount of data that is available: the model is fit too closely to the observed data but will not generalize towards new data.

Ridge regression is a way to reduce over-fitting. Recall that for ordinary least squares, the following loss function is minimized:

‖𝒚−𝑿𝜷‖<sup>2</sup> = (𝒚−𝑿𝜷)<sup>T</sup> (𝒚−𝑿𝜷)                                                                                                      (Eq. 4.33)

Ridge regression adds a penalty term to this loss function (indicated in red):

(𝒚−𝑿𝜷)<sup>T</sup> (𝒚−𝑿𝜷) + 𝜆𝜷<sup>T</sup> 𝑫𝜷,                                                                                                             (Eq. 4.34) with


Herein, 𝟎 is a matrix with only zeros and 𝑰 is the unit matrix<sup>33</sup> . Matrix D allows certain parameters to be unpenalized by setting their corresponding diagonal elements to 0. In the given example, only the intercept 𝛽<sup>0</sup> remains unpenalized. The penalty term increases if the absolute values of the parameters 𝜷 increase. This prevents over-fitting by shrinking model parameters towards 0 (Fig. 4.14).


**Figure 4.14.** Graphical representation of the ridge estimate and the ordinary least squares (OLS) estimate in an example case where two model parameters 𝛽1 and 𝛽2 need to be estimated. The OLS

> 33 The unit matrix is a matrix with 1 on its diagonal elements and 0 on its off-diagonal elements. The model thus implies equal variances for all covariates and no correlation between the covariates.

73

estimate minimizes the residual sum of squares (RSS), while the ridge estimates are shrunken towards 0.

When fitting this regression model, the aim is to minimize the mean squared error (MSE):

MSE(𝜷̂) ≝E [(𝜷̂ −𝜷)2]                                                                                                                        (Eq. 4.36)

It can be shown that the MSE can also be written as [477]:


In 1956, Stein showed that for models with 3 or more parameters, certain shrinkage estimators outperform the least-squares estimator in terms of MSE [478]. Shrinkage estimators introduce a small bias but reduce the overall MSE due to a strong reduction in the variance of the estimator. Therefore, such shrinkage estimators are more stable overall. Leave-one-out crossvalidation is one way to tune the penalty parameter. Cross-validation enables to assess how accurate a model is on new, unobserved data. In leave-one-out cross-validation, the data is fitted to the dataset from which one observation 𝑗 is removed. This allows to estimate the MSE: the model’s estim ate 𝑦̂𝑗 for observation 𝑗 can be seen as a “new” data point . With crossvalidation, the following estimator for the overall mean squared error is minimized towards 𝜆 [479]:


Herein 𝜷̂<sup>(𝑗)</sup> (𝜆) is a vector of ridge parameter estimates based on the data from which the 𝑗th observation is removed and [𝑿𝜷̂<sup>(𝑗)</sup> (𝜆)]𝑗 the leave-one-out model estimate for the 𝑗th observation 𝑦𝑗. Leave-one-out cross validation requires iteratively fitting ridge models without the 𝑗th observation until convergence. It is also possible to repeatedly leave out 𝐾 observations and reduce the squared distances of the leave-𝐾-out model fit to the 𝐾 observations that were left out.

As explained in 4.2.3, peptide-based models require the inclusion of a random sample effect to allow correct statistical inference. Leave-one-out cross-validation would require iterative fitting of a mixed model. There is however a link between mixed models and ridge regression, which is tempting to exploit when introducing ridge regression in a mixed model context as this would give a big computational advantage. As a demonstration of this link, assume the following mixed model:

𝒚= 𝑿𝜷+ 𝒁𝒖+ 𝜺                                                                                                                                      (Eq. 4.40)


74

distribution, 𝟎 a 1 × 𝑁 column vector with zeros, 𝜎𝑢<sup>2</sup> the variance on the random effects and 𝑰 the unit matrix. 𝜺~MVN(𝟎, 𝜎<sup>2</sup> 𝑰) denotes the random error terms. We maximize the joint likelihood of y, 𝜷 and 𝒖 towards 𝜷 and 𝒖:

L(𝑦, 𝜷, 𝒖) = L(𝑦, 𝜷|𝒖)L(𝒖)                                                                                                                     (Eq. 4.41)


With 𝑁 the number or random effect parameters. After replacing 𝜎𝑢<sup>2</sup> by 𝜎<sup>2</sup> ⁄𝜆 and multiplying by -2, this is equivalent with minimizing the following expression:


𝒁]. Minimization to 𝜽 only involves: Set 𝜽= [<sup>𝜷</sup> 𝒖<sup>] and 𝑪= [𝑿</sup>


which is exactly the ridge regression loss function. Hence, parameters with a ridge penalty can be estimated by parameterizing them as random effects in a mixed model. In peptide-based models, where a random run effect needs to be included to account for within-run correlation, this link between mixed models and ridge regression can be exploited to estimate parameters with a ridge penalty, as we will see in Chapter 9.1. After optimizing the loss function, we obtain the following estimator:


This estimator for 𝒖̂ is termed the best linear unbiased predictor (BLUP). An estimate for 𝜎<sup>2</sup> can be obtained by plugging in the estimates 𝜽̂ into the log likelihood and solving this profile log-likelihood towards 𝜎<sup>2</sup> . In practice, we make use of the restricted maximum likelihood (REML) criterion that also accounts for the degrees of freedom due to the fixed effects in the model. Conditional on 𝒖, the variance on 𝜽̂ can be estimated as follows:


This variance estimator, however, does not account for the bias in the estimator 𝒖̂. Hence, inference based on this estimator will only be correct when the bias is negligible. However, since E(𝒖) = 0, the BLUP estimator 𝒖̂ is unbiased on average over the distribution of u. Unconditional on 𝒖, the variance estimator on 𝜽̂ is given by:


75

The estimator also accounts for the bias introduced by the penalized regression and is therefore somewhat larger than the conditional variance estimator. Ridge regression has been used in other omics fields to predict the effects of various molecular markers on organismal phenotypes [480, 481].

#### **4.2.5. Robust regression with M estimation**

Outliers are observations with extreme response values. If such observations also have a strong leverage (i.e. if they have a large distance to the average predictor values), the observation will have a strong influence on the model fit: the model will be fit close to the influential observation due to a lack of neighboring observations. Outliers are more likely to correspond to less reliable measurements. Indeed, an extremely high intensity value could for example have originated from a spike in electrospray voltage, while a very low intensity value is very likely to be missing in a repeated run due to intensity-dependent missingness. Moreover, even if the outlier is a valid measurement, it is often undesirable that a single observation has a very strong impact on the model.

Robust regression with M estimation aims to minimize the maximal bias of the estimators. With robust regression, statistical tests are only asymptotically valid. However, if the errors are normally distributed, M estimators have a high efficiency. Recall the OLS loss function:

‖𝒚−𝑿𝜷‖<sup>2</sup> = (𝒚−𝑿𝜷)<sup>T</sup> (𝒚−𝑿𝜷)                                                                                                      (Eq. 4.49)

This function is also called the L2 loss function since it minimizes the L2 norm of 𝒚−𝑿𝜷. With M estimation, the following loss function is minimized:

Ω(𝒚−𝑿𝜷)                                                                                                                                                   (Eq. 4.50)

The function Ω(𝑥) should have the following characteristics:

- Ω(𝑥) is symmetric

- Ω(𝑥) has a minimum at Ω(0) = 0

- Ω(𝑥) is positive for all 𝑥≠0

- Ω(𝑥) increases as 𝑥 increases

Given these conditions, the estimator 𝜷̂ is the solution to the equation:

ω(𝒚−𝑿𝜷) = 0                                                                                                                                          (Eq. 4.51)

Where ω is the derivative of Ω. For 𝜷̂ to possess the robustness property, ω should be bounded (i.e. there exists a real number 𝑀 such that |𝜔(𝑥)| ≤𝑀 for all values of 𝑥). However, robust ω functions are non-linear in 𝜷 and typically do not have a closed-form solution. We will therefore recast the problem.

When location parameters 𝜷 and a scale parameter 𝜎 have to be estimated simultaneously, we minimize:

Ω ~~(~~<sup>𝒚−𝑿𝜷</sup> 𝜎 ~~)~~ (Eq. 4.52) Whereby: ω ~~(~~<sup>𝒚−𝑿𝜷</sup> 𝜎 ~~)~~ = 0                                                                                                                                        (Eq. 4.53)

Whereby:

76

<u>𝒚−𝑿𝜷</u> Define 𝜼= and weight function 𝑤(𝜼) = ω(𝜼)⁄𝜼. The last estimation equation can then be 𝜎 rewritten as:

𝑤(𝜼)𝜼= 0                                                                                                                                                   (Eq. 4.54)

This expression can be solved as an iteratively reweighted least-squares (IRWLS) problem. Herein, the weights 𝑤(𝜼) are kept constant in 𝜼 and the expression is solved to 𝜷. Then, the weights are recalculated based on the new 𝜷̂ and the procedure is repeated until convergence.

Examples of robust loss functions Ω include:

- ⁄                 if |𝑥| ≤𝑘

- • Huber: Ω<sup>Huber</sup> = {𝑘(|𝑥| −𝑘/2)   if |𝑥| > 𝑘<sup>x22,                                                                      (Eq. 4.55)</sup> with 𝑘= 1.345 the default tuning constant <u>|𝑥| |𝑥|</u>

- • “Fair”: Ω<sup>Fair</sup> = 𝑐<sup>2</sup> ~~(~~ 𝑐 −log (1 + 𝑐 )),                                                                                (Eq. 4.56) with 𝑐= 1.3998 the default tuning constant 𝑐<sup>2</sup>

- • Cauchy: Ω<sup>Cauchy</sup> = (1 + (𝑥𝑐⁄ )<sup>2</sup> ),                                                                                    (Eq. 4.57) 2

- with 𝑐= 1.3849 the default tuning constant

The default tuning constants are chosen in such a way that the methods have a 95% asymptotic efficiency when applied to standard normal data. Fig. 4.15 demonstrates the impact of robust regression with M estimation with Huber weights.


**Figure 4.15.** Plot of the residuals 𝑦𝑗 −𝑦̂𝑗 in function of the model-fitted values for all log2-tranformed peptide intensities 𝑦̂𝑗 (𝑗= 1, … , 637) of yeast protein SYKC in the CPTAC dataset after fitting regression model (Eq. 4.27) robustly with Huber weights. The sizes of the datapoints are proportional to the Huber weights in the IRWLS procedure. Note that observations with large residuals have small weights, which is indicative of the robustness property.

Examples of common loss functions and their corresponding weight functions are plotted in Fig. 4.16 and 4.17, respectively. An extensive overview of robust loss functions can be found in Bolstad (2004) [482].

77


**Figure 4.16.** The default L2 loss function and examples of loss functions Ω that are commonly used in robust M estimation. Figure adapted from Bolstad (2004) [482].

78


**Figure 4.17.** Examples of the weight functions 𝑤 that are used in the IRWL procedure to obtain the corresponding loss functions in Fig. 4.15. Figure adapted from Bolstad (2004) [482].

#### **4.2.6. Counting-based methods**

To quantify proteins with any of the above-described methods, it is necessary to extract ion intensities, which generally requires, as shown in section 3.3, rather advanced algorithms that are implemented in specialized software. Moreover, reliable protein quantification with these methods requires, depending on the study design, basic to advanced statistical knowledge. It was soon noticed that simply counting the number of MS² spectra that map to a certain protein provides a reasonably good approximation of a protein’s abundance [483, 484]. This makes sense because the more abundant a protein, the more of its peptide ions that can be expected to be detectable above noise levels. Moreover, the more abundant a peptide, the longer its elution time and hence the higher the chance that it will be targeted for fragmentation more than once, thus generating more MS² spectra. Spectral counting also deals more naturally with missing values: as a zero count [90]. Spectral counting became very appealing to many researchers, not because of its reliability, but mainly because of its ease-of-use. Indeed, researchers could now simply count the number of MS² spectra mapping to a protein and directly divide these numbers in order to obtain a fold change estimate. However, when the significance of such fold changes needs to be assessed, statistics are again needed. A natural framework for handling count data is Poisson regression. Poisson regression assumes that the spectral counts 𝑥𝑖𝑟 for each protein 𝑖 in each run 𝑟 follow a Poisson distribution:

79

𝑥𝑖𝑟~Poisson(𝜇𝑖𝑡𝑏)                                                                                                                                     (Eq. 4.58)

This makes sense because a Poisson distribution is typically used to model the number of times an event occurs (detecting a spectrum that maps to protein 𝑖) during a fixed time interval (an MS run). For the CPTAC example, we can make use of the generalized linear model framework, to model the first two moments (mean and variance) of the spectral counts. As counts always have a lower bound of 0 and negative means are not meaningful for count data, we make use of a log-link function to allow unbounded estimation of the model parameters. For the CPTAC dataset, the model can be specified as follows:

<mark>log(𝜇</mark> 𝑖𝑡𝑏<sup><mark>)</mark></sup> <mark>= 𝛽</mark> 𝑖0 <mark>+ 𝛽</mark> 𝑖𝑡condition <mark>+ 𝛽</mark> 𝑖𝑏lab <mark>(Eq. 4.59)</mark>

<mark>Note that for a Poisson distribution the mean 𝜇</mark> 𝑖𝑡𝑏<sup><mark>and the variance</mark></sup> <mark>𝜐</mark> 𝑖𝑡𝑏<sup><mark>are equal.</mark></sup>

Here, 𝛽𝑖0 is the intercept, 𝛽𝑖𝑡condition is the effect of spike-in condition 𝑡 and 𝛽𝑖𝑏lab is the effect of lab 𝑏. By using a Poisson distribution, it is implied that the variance in the data <mark>𝜐𝑖𝑡𝑏</mark><sup>is equal to</sup> the mean <mark>𝜇𝑖𝑡𝑏</mark><sup><mark>.</mark>Such a mean-variance relationship is very restrictive. In reality, the residual</sup> variance is often larger (over-dispersion) or sometimes even smaller (under-dispersion) than what would be expected under the Poisson distribution. The mean-variance relationship can however be relaxed by making use of a quasi-Poisson regression model [485].

Note that quasi-Poisson regression does not model the full distribution, but only the first two moments of the distribution: the mean <mark>𝜇𝑖𝑡𝑏</mark><sup>and the variance</sup> <mark>𝜐</mark> 𝑖𝑡𝑏<sup><mark>. The specification of the</mark></sup> <mark>mean model is identical to Poisson regression.</mark> However, the variance is more flexible:

<mark>𝜐</mark> 𝑖𝑡𝑏 <mark>= 𝜑</mark> 𝑖 <mark>𝜇</mark> 𝑖𝑡𝑏<sup><mark>(Eq. 4.60)</mark></sup>

The factor <mark>𝜑</mark> 𝑖<sup><mark>allows to to correct for over- or under-dispersion.C</mark>ount data can also be</sup> proposed to follow a negative binomial distribution, which assumes a quadratic mean-variance relationship:

<mark>𝜐</mark> 𝑖𝑡𝑏 <mark>= 𝜇</mark> 𝑖𝑡𝑏 <mark>+ 𝜑</mark> 𝑖<sup><mark>𝜇</mark></sup> 𝑖𝑡𝑏2 <mark>(Eq. 4.61)</mark>

A negative binomial distribution reduces to a Poisson distribution if <mark>𝜑</mark> 𝑖<sup><mark>is zero.</mark>Negative</sup> binomial generalized linear models are implemented in the popular RNA sequencing quantification packages EdgeR [486, 487] and DESeq2 [488], which have also been applied in proteomics contexts [489].

Other statistical models have been proposed as well to deal with count data in proteomics, including a generalized linear mixed effects Poisson regression model in which all proteins are modeled together [490], a beta-binomial model [491] and Bayesian models [492].

Peptide counting is an alternative to spectral counting. In peptide counting, the number of unique peptides instead of the number of unique PSMs that match to each protein are counted. Some authors reported that spectral counting is more accurate and more reproducible than peptide counting which is in turn more reproducible than sequence coverage-based approaches [483, 493, 494]. This is probably because spectral counting is more fine-grained than peptide counting (there at least as much PSMs as peptides per protein), which might make it more feasible to quantify smaller differences in abundance.

A very simple peptide counting method is the Exponentially Modified Protein Abundance Index (emPAI). For each protein 𝑖, the emPAI is calculated as follows [174]:


80

predpep is Hereby, 𝑛𝑖pep is the number of observed unique peptides mapping to protein 𝑖 and 𝑛𝑖 the number of tryptic peptides that can theoretically map to protein 𝑖. emPAI is an example of so- called “absolute protein quantification” method. By normalizing the peptide count of each protein by its number of predicted unique tryptic peptides 𝑛𝑖predpep, emPAI claims to be able to compare the abundances of different proteins to each other (as opposed to comparing the abundances of the same proteins over different conditions, so- called “relative quantification”). The content of protein 𝑖 in mol % is then calculated as follows:


with 𝑛<sup>protein</sup> the total number of proteins in the dataset. Of course, for quantitative protein inference, peptide counting methods also require some statistical modeling. The models for peptide counting are very similar to those of spectral counting and many statistical models for spectral counting and peptide counting can be used interchangeably.

Absolute Protein Expression (APEX) is an example of an absolute quantification method based on spectral counting that has gained quite some traction [175, 495]. An APEX score for protein 𝑖 is calculated as follows:


with 𝑛𝑖MS2 the total number of MS² spectra mapping to protein 𝑖, 𝜋𝑖ID the probability that protein 𝑖 is correctly identified,  𝑛𝑖predPSM the number of computationally predicted PSMs for protein 𝑖 and 𝐶 an estimate of the total concentration of protein molecules in the cell.

Do note that although absolute quantification methods might give some indication about a protein ’ s abundance, these estimates remain generally very crude because normalizing protein abundances to each other based on e.g. the theoretical number of tryptic peptides they can generate is quite inaccurate. Also, count-based approaches have become largely obsolete in present-day proteomics given that quantification based on continuous intensity-based signals is clearly superior over discrete counts [317]. It has indeed been shown that countbased methods have a lower linear response to various protein loading amounts, a lower reproducibility, a lower quantitative accuracy, a lower precision, lower sensitivity, and a higher ratio of false positives to false negatives compared to MS intensity-based quantification [307]. This is because peptide counting disregards the inherent abundance-intensity relationship (within a certain dynamic range [496]) for each peptide. Dynamic exclusion, during which identified ions are excluded from being re-targeted for fragmentation for a certain amount of time, further obscures the relationship between spectral counts and protein abundances [497]. Counting-based approaches perform especially poorly for low-abundant proteins [228, 483, 498]. Indeed, it is not possible to calculate an accurate protein ratio between two conditions if only one or two spectra per condition are mapped to the protein of interest [497]. And, at higher levels of protein abundances, saturation effects come into play for relatively low total protein concentrations when all peptides that can theoretically be detected are in fact detected [228]. Spectral counting is reviewed extensively in Lundgren _et al._ (2010) [494].

#### **4.2.7. Controlling the false discovery rate**

Whether statistical inference is done with t-tests, linear regression models, or other statistical approaches, the fact that statistical inference is done for each protein in the dataset creates a

81

huge multiple testing problem. Imagine testing 1,000 proteins, all of which are not differentially abundant (i.e. the null hypothesis is true). When using the traditional 5% cut-off at the p-value level, on average 5%, i.e. 50 proteins, will be erroneously declared differentially abundant (false positives). Therefore, it is clear that, in the case of multiple testing, a significance threshold based on p-values will be way too liberal.

Solutions to this problem have been proposed in the form of controlling the family-wise error rate (FWER). The aim of FWER procedures is to control the probability of detecting at least a single false positive at a given level, typically 5%. An example of an FWER procedure is the simple, but somewhat conservative Bonferroni correction [499]. Here, a protein is only declared significantly differentially abundant if its p-value is smaller than 𝛼𝑛⁄<sup>protein</sup> , with 𝛼 the significant threshold (e.g. 5%) and 𝑛<sup>protein</sup> the number of proteins that are being tested. It turns out that FWER procedures are often too conservative for high-throughput applications. Indeed, the number of biological replicates in such a context is often rather low, which limits the statistical power of each individual test.

To cope with the specific context of high-throughput experiments, false discovery rate (FDR) procedures were developed. The false discovery rate aims to control the expected fraction of false positive proteins in a list of differentially abundant proteins at a certain level, again, typically 5% [500]. In practice, FDR-controlled lists are much more interesting for practitioners: a researcher will prefer a list of 20 significant proteins of which on average 1 is a false positive (i.e. the FDR is controlled at 5%) over a list of maybe 2 or 3 proteins that are not in error according to the FWER criterion. The most well-known and most widely used FDR procedure is the Benjamini-Hochberg FDR [501]. The procedure works as follows:

In a first step, the p-values are sorted from large to small. If 𝐼 p-values need to be FDR corrected, let 𝑖= 1, … , 𝐼 be the rank of the 𝑖th p-value. Then, the q-value 𝑞𝑖 for the 𝑖th p-value is calculated as follows:


for 1 ≤𝑘≤𝑖. All proteins with a q-value smaller than the proposed threshold, e.g. 5%, are then considered statistically significant.

82

## **5. RESEARCH HYPOTHESIS**

### **5.1. Setting the stage**

Many biological processes strongly depend on balanced levels of protein expression and the perturbation of a single protein can already lead to organismal malfunctioning (e.g. abnormal hemoglobin production in thalassemia [47] or extensive cellular remodeling towards a cancerous phenotype [502]). In this respect, quantitative knowledge of a proteome is very important for the unraveling of the development and progression of diseases and the identification of biomarkers, amongst others. It is fair to state that the transcriptome and the translatome only reflect the proteins that can be or are being expressed, but largely fail to provide information on a protein’s activity, function, interaction partners, localization and modification state (see 1.2.3). As proteins and their modified variants are expressed over a large concentration range, accurate quantitative information is a must to distinguish different cellular and organismal conditions [503].

Label-free shotgun proteomics leads to the identification and quantification of thousands of peptides and proteins in a single experiment. Here, analysis of differential abundance of proteins is based on ratios derived from reconstructed elution profiles based on MS intensities for all PSMs pointing to the same protein or the same protein group in a sample (see section 3.2). However, the data are highly hierarchical, and intensities can be strongly influenced by variations of peptide-specific properties. In addition, the number of peptides identified in all samples is usually limited, which leads to large numbers of missing values (Fig. 5.1), which do not occur at random. Some peptides are better detected than others and high-abundant peptide ions are more likely to yield higher numbers of fragmentation spectra. "Match between runs" algorithms can only partly compensate for this effect by reducing the number of missing values (see section 3.4).


**Figure 5.12.** The missing value problem. Left: the number of unique peptides identified per protein in the CPTAC dataset [426]. Right: the number of samples in which each protein in the CPTAT dataset is identified. The number of proteins identified in 9, 18 and all 27 samples are markedly elevated (cyan bars). This is because of the higher numbers of proteins that are exclusively identified in all MS runs from 1, 2 or 3 labs respectively.

Researchers have used a plethora of pipelines for the analysis of label-free shotgun proteomics data (see chapter 4). Indeed, since most mass spectrometry researchers do not have a background in statistics, different preprocessing and differential analysis methods are often combined _ad hoc_ without a proper motivation. Many methods analyze the data protein

83

by protein by (a) filtering out proteins as soon as they are missing in a specified number of samples (see 4.1.2), (b) summarize the peptides for each protein in a sample and ignore missing values (see 4.1.5) or (c) impute missing values based on the observed peptides for the corresponding protein in other samples (see 4.1.4). Filtering out all proteins (a) leads to substantial information loss. Indeed, as demonstrated in Fig. 5.1, removing proteins that are only identified with more than a given number of peptides or requiring proteins to be identified in all of the samples would remove a substantial amount of proteins from the dataset. Summarization (b) needs to be executed such that it correctly takes the peptide-specific effects into account. A particular challenge here are the limited numbers of peptides that are identified across different samples. If summarization does not correctly take the differences in ionization efficiencies into account, it will introduce a bias because the final data will be based on different peptides. Moreover, summarization will always ignore differences in accuracy due to the different numbers of peptides on which each summary is based. Imputation (c) is even more tedious because missing values in proteomics are a combination of missing completely at random and intensity- and even context-dependent missingness. Since it is impossible to know the exact contributions of these different types of missingness, imputation according to incorrect assumptions will lead to biased quantifications. However, if missing values are simply ignored, low-abundant proteins will be over-estimated due to the limited linear dynamic range, which will reduce the power to detect differential abundance.

In addition, a proteomics experiment typically consists of a relatively small number of biological repeats compared to the large number of proteins analyzed. This gives rise to unstable variance estimates for certain proteins, especially if these proteins are identified with only a few peptides. Indeed, a small sample drawn from a given population might display a variance that is much smaller (or much bigger) than the true population variance just by random chance. Therefore, some observations might be flagged as differentially abundant solely because of their low observed variances while other truly differentially abundant proteins might be missed due to their large observed variances. This data sparsity also leads to unstable fold change estimates: one or two outlying intensities, which can for example be caused by misidentifications or co- eluting peptides, can strongly influence a protein’s fold change.

These unstable fold change and variance estimates may cause a significant increase in the number of false positives and false negatives (see e.g. the supplementary material of Doll _et al._ (2017) [504], where SERINC3 and PNMA1 were declared significantly altered with very weak evidence based on only a single peptide). It is therefore not surprising that a recent power calculation study on four biological repeats of _Arabidopsis thaliana_ Col-0 samples analyzed in technical triplicate estimated that for MaxLFQ summaries, a minimal fold change of 1.4 is required to detect a statistically significant difference with 95% confidence and a power of 80%[463].

State-of-the-art proteomics quantification methods only focus on some of the sub-problems mentioned above. They generally remain fairly sensitive to outliers and correct for missing observations only to a limited extent. In addition, they usually prune the number of potential hits by filtering out proteins which have few peptides in common across the majority of the samples. Methods that model peptide-level data are often more sensitive because they naturally correct for the correlation present within the same samples, as well as for the peptide effects and the number of detected peptides for a given protein in each sample [425, 471].

Like summarization-based methods, many peptide-based models still produce unstable estimates of differential abundance and variance components due to over-parameterization. This especially occurs when few peptides are identified per protein: many low-abundant proteins are then falsely labeled as differentially abundant. Filtering on the basis of the number

84

of identified peptide spectra can provide a solution, but there is a risk that real hits will also be filtered out. Moreover, most peptide-based models remain very sensitive to outliers.

In addition, many methods are only suitable to analyze specific types of experimental designs. For example, in Perseus, it is possible to compare multiple groups to each other, but it is not possible to accurately analyze blocked designs, such as CPTAC. In MSstats, the user should annotate each experiment with a “Run”, “Condition” and “BioReplicate”. Hereby, “Run” refers to the MS run, “Condition” to the treatment of interest and “BioReplicate” to a grouping factor that is encoded as a random effect. While this set-up allows most simple experimental designs to be analyzed in a correct way, it is insufficiently flexible to correctly analyze more complicated designs with multiple confounding effects.

Finally, state-of-the-art data analysis methods, such as published models at the peptide level, do not always find their way to proteomic labs <mark>[474, 475].</mark> This is a non-negligible problem! Indeed, many groups only demonstrated proof-of-concept, but never developed their method into a usable software package. And, those who did often lack a convenient graphical user interface that is appealing to less-experienced users. Availability, user-friendliness, documentation, support and maintenance of software tools are very important for new methods to be effective for end users.

### **5.2. Aims of my PhD work**

Based on the previous section, it is clear that state-of-the-art proteomics quantification methods do not yet make optimal use of the data, resulting in suboptimal protein quantifications. The development of robust data analysis tools for quantitative proteomics is therefore essential for the further development of the proteomics research field because, with the current data-analytical methods, many proteins remain under the radar [505]. The overall aim of my work was to develop a more robust, easy-to use proteomics quantification method that is also usable for the analysis of proteins with a limited overlap in identified peptides.

More specifically, this method should:

- account for the hierarchical nature of the data,

- handle missing peptides in a more correct way,

- derive strength from the massive parallel availability of peptides to estimate variance components more correctly,

- be robust to outliers,

- and be able to handle complex experimental designs.

In such a method, it is important that a random effect for run is included in order to allow to correct for within-run correlation. In this respect, it is tempting to build upon the link between mixed models and ridge regression, to make use of robust regression with M estimation and to allow for empirical Bayes variance estimation. Implementing this method is expected to increase the number of truly differentially abundant proteins identified in screening experiments. The method should also be implemented and distributed in a user-friendly software tool for differential proteomics with the possibility of a graphical user interface to maximize the impact of the research.

To develop such a method, it is first necessary to thoroughly benchmark the most promising and most commonly used quantification methods. This will shed light on how preprocessing, standardization and differential analysis in a label-free proteomics quantification workflow influence a method’s performance.

85

86

## **6. OUTLINE**

The remainder of my thesis is constructed as follows: first, I will present each of my published papers. In my first paper, I demonstrate how I compared different data analysis methods for differential quantification in label-free shotgun proteomics. My second paper presents the rationale behind MSqRob, the algorithm I developed to improve quantification in label-free shotgun proteomics. In my third paper, I provide a tutorial on experimental design and data analysis with MSqRob. In my fourth, unpublished paper, I make use of the additional information of peptide counts to boost MSqRob’s power and to indicate whether a protein’s significance is mainly driven by differential abundance, differential detection or both.

In the discussion, I explore the significance of my work and place it in a broader context. In the future research perspectives, I give some indications on how my research could go on from here.

87

88

## **7. REFERENCES PART I**

1. Gladyshev, V.N. and G.V. Kryukov, _Evolution of selenocysteine-containing proteins: Significance of identification and functional characterization of selenoproteins._ BioFactors, 2001. **14** (1‐4): p. 87-92.

2. Prat, L. _et al._ , _Carbon source-dependent expansion of the genetic code in bacteria._ Proceedings of the National Academy of Sciences, 2012. **109** (51): p. 21070-21075.

3. Koch, A. _et al._ , _A proteogenomics approach integrating proteomics and ribosome profiling increases the efficiency of protein identification and enables the discovery of alternative translation start sites._ Proteomics, 2014. **14** (23-24): p. 2688-2698.

4. Ruiz-Orera, J. _et al._ , _Long non-coding RNAs as a source of new peptides._ eLife, 2014. **3** : p. e03523-e03523.

5. Rion, N. and M.A. Rüegg, _LncRNA-encoded peptides: More than translational noise?_ Cell Research, 2017. **27** : p. 604.

6. Choi, S.-W., H.-W. Kim, and J.-W. Nam, _The small peptide world in long noncoding RNAs._ Briefings in Bioinformatics, 2018: p. bby055-bby055.

7. Gebert, L.F.R. and I.J. MacRae, _Regulation of microRNA function in animals._ Nature Reviews Molecular Cell Biology, 2019. **20** (1): p. 21-37.

8. Bhat, S.A. _et al._ , _Long non-coding RNAs: Mechanism of action and functional utility._ Non-coding RNA Research, 2016. **1** (1): p. 43-50.

9. Brimacombe, R. and W. Stiege, _Structure and function of ribosomal RNA._ The Biochemical journal, 1985. **229** (1): p. 1-17.

10. Walter, N.G. and D.R. Engelke, _Ribozymes: catalytic RNAs that cut things, make things, and do odd and useful jobs._ Biologist (London, England), 2002. **49** (5): p. 199203.

11. Müller, S. _et al._ , _Thirty-five years of research into ribozymes and nucleic acid catalysis: where do we stand today?_ F1000Research, 2016. **5** : p. F1000 Faculty Rev-1511.

12. Mühlhausen, S. _et al._ , _Endogenous Stochastic Decoding of the CUG Codon by Competing Ser- and Leu-tRNAs in Ascoidea asiatica._ Current Biology, 2018. **28** (13): p. 2046-2057.e5.

13. Hofhuis, J. _et al._ , _The functional readthrough extension of malate dehydrogenase reveals a modification of the genetic code._ Open Biology, 2016. **6** (11): p. 160246.

14. Inamine, J.M. _et al._ , _Evidence that UGA is read as a tryptophan codon rather than as a stop codon by Mycoplasma pneumoniae, Mycoplasma genitalium, and Mycoplasma gallisepticum._ Journal of Bacteriology, 1990. **172** (1): p. 504-506.

15. Piatkov, K.I. _et al._ , _Formyl-methionine as a degradation signal at the N-termini of bacterial proteins._ Microbial Cell, 2015. **2** (10): p. 376-393.

16. Wingfield, P., _N-Terminal Methionine Processing._ Current Protocols in Protein Science, 2017. **88** : p. 6.14.1-6.14.3.

17. Falb, M. _et al._ , _Archaeal N-terminal Protein Maturation Commonly Involves N-terminal Acetylation: A Large-scale Proteomics Survey._ Journal of Molecular Biology, 2006. **362** (5): p. 915-924.

18. Jonckheere, V., D. Fijałkowska, and P. Van Damme, _Omics Assisted N-terminal Proteoform and Protein Expression Profiling On Methionine Aminopeptidase 1 (MetAP1) Deletion._ Molecular & Cellular Proteomics, 2018. **17** (4): p. 694-708.

19. Belinky, F., I.B. Rogozin, and E.V. Koonin, _Selection on start codons in prokaryotes and potential compensatory nucleotide substitutions._ Scientific Reports, 2017. **7** (1): p. 12422.

20. Kearse, M.G. and J.E. Wilusz, _Non-AUG translation: a new start for protein synthesis in eukaryotes._ Genes & Development, 2017. **31** (17): p. 1717-1731.

21. Hecht, A. _et al._ , _Measurements of translation initiation from all 64 codons in E. coli._ Nucleic Acids Research, 2017. **45** (7): p. 3615-3626.

22. Jungreis, I. _et al._ , _Evidence of abundant stop codon readthrough in Drosophila and other metazoa._ Genome Research, 2011. **21** (12): p. 2096-2113.

89

23. Atkins, J.F. _et al._ , _Ribosomal frameshifting and transcriptional slippage: From genetic steganography and cryptography to adventitious use._ Nucleic Acids Research, 2016. **44** (15): p. 7007-7078.

24. Dinman, J.D., _Programmed Ribosomal Frameshifting Goes Beyond Viruses: Organisms from all three kingdoms use frameshifting to regulate gene expression, perhaps signaling a paradigm shift._ Microbe (Washington, D.C.), 2006. **1** (11): p. 521527.

25. Baranov, P.V. _et al._ , _Transcriptional slippage in bacteria: distribution in sequenced genomes and utilization in IS element gene expression._ Genome Biology, 2005. **6** (3): p. R25-R25.

26. Freeman, M.F. _et al._ , _Seven enzymes create extraordinary molecular complexity in an uncultivated bacterium._ Nature Chemistry, 2016. **9** : p. 387.

27. Morinaka, B.I. _et al._ , _Natural noncanonical protein splicing yields products with diverse β -amino acid residues._ Science, 2018. **359** (6377): p. 779-782.

28. Berk, A.J., _Discovery of RNA splicing and genes in pieces._ Proceedings of the National Academy of Sciences, 2016. **113** (4): p. 801-805.

29. Vila-Perelló, M. and T.W. Muir, _Biological Applications of Protein Splicing._ Cell, 2010. **143** (2): p. 191-200.

30. Smith, L.M., N.L. Kelleher, and P. The Consortium for Top Down, _Proteoform: a single term describing protein complexity._ Nature Methods, 2013. **10** (3): p. 186-187.

31. Pace, C.N., J.M. Scholtz, and G.R. Grimsley, _Forces stabilizing proteins._ FEBS Letters, 2014. **588** (14): p. 2177-2184.

32. Saibil, H., _Chaperone machines for protein folding, unfolding and disaggregation._ Nature Reviews Molecular Cell Biology, 2013. **14** (10): p. 630-642.

33. Hartl, F.U., A. Bracher, and M. Hayer-Hartl, _Molecular chaperones in protein folding and proteostasis._ Nature, 2011. **475** : p. 324.

34. Fuhs, S.R. and T. Hunter, _pHisphorylation; The Emergence of Histidine Phosphorylation as a Reversible Regulatory Modification._ Current Opinion in Cell Biology, 2017. **45** : p. 8-16.

35. Potel, C.M. _et al._ , _Widespread bacterial protein histidine phosphorylation revealed by mass spectrometry-based proteomics._ Nature Methods, 2018. **15** : p. 187.

36. Besant, P.G., P.V. Attwood, and M.J. Piggott, _Focus on Phosphoarginine and Phospholysine._ Current Protein & Peptide Science, 2009. **10** (6): p. 536-550.

37. Attwood, P.V., P.G. Besant, and M.J. Piggott, _Focus on phosphoaspartate and phosphoglutamate._ Amino Acids, 2011. **40** (4): p. 1035-1051.

38. Hardman, G. _et al._ , _Extensive non-canonical phosphorylation in human cells revealed using strong-anion exchange-mediated phosphoproteomics._ bioRxiv, 2017.

39. Mijakovic, I., C. Grangeasse, and K. Turgay, _Exploring the diversity of protein modifications: special bacterial phosphorylation systems._ FEMS Microbiology Reviews, 2016. **40** (3): p. 398-417.

40. Jean Beltran, P.M. _et al._ , _Proteomics and integrative omic approaches for understanding host-pathogen interactions and infectious diseases._ Molecular Systems Biology, 2017. **13** (3): p. 922-922.

41. Doyle, H.A. and M.J. Mamula, _Autoantigenesis: the evolution of protein modifications in autoimmune disease._ Current Opinion in Immunology, 2012. **24** (1): p. 112-118.

42. Chung, K.K.K. _et al._ , _S-Nitrosylation of Parkin Regulates Ubiquitination and Compromises Parkin's Protective Function._ Science, 2004. **304** (5675): p. 1328-1331.

43. Ren, R.-J. _et al._ , _Proteomics of protein post-translational modifications implicated in neurodegeneration._ Translational Neurodegeneration, 2014. **3** (1): p. 23-23.

44. Creasy, D.M. and J.S. Cottrell, _Unimod: Protein modifications for mass spectrometry._ Proteomics, 2004. **4** (6): p. 1534-1536.

45. Ideker, T. and R. Sharan, _Protein networks in disease._ Genome Research, 2008. **18** (4): p. 644-652.

46. Marengo-Rowe, A.J., _The thalassemias and related disorders._ Proceedings (Baylor University. Medical Center), 2007. **20** (1): p. 27-31.

90

47. Thein, S.L., _The Molecular Basis of β -Thalassemia._ Cold Spring Harbor Perspectives in Medicine, 2013. **3** (5): p. a011700.

48. Svartman, M., G. Stone, and R. Stanyon, _Molecular cytogenetics discards polyploidy in mammals._ Genomics, 2005. **85** (4): p. 425-430.

49. Gatz, M. _et al._ , _Role of genes and environments for explaining alzheimer disease._ Archives of General Psychiatry, 2006. **63** (2): p. 168-174.

50. Diaz-Espinoza, R. _et al._ , _Treatment with a Non-toxic, Self-replicating Anti-prion Delays or Prevents Prion Disease In vivo._ Molecular psychiatry, 2018. **23** (3): p. 777-788.

51. Füzéry, A.K. _et al._ , _Translation of proteomic biomarkers into FDA approved cancer diagnostics: issues and challenges._ Clinical Proteomics, 2013. **10** (1): p. 13-13.

52. Zhang, Q.C. _et al._ , _Structure-based prediction of protein – protein interactions on a genome-wide scale._ Nature, 2012. **490** : p. 556.

53. Makley, L.N. and J.E. Gestwicki, _E xpanding the Number of “Druggable” Targets: Non - Enzymes and Protein-Protein Interactions._ Chemical Biology & Drug Design, 2013. **81** (1): p. 22-32.

54. Śledź, P. and A. Caflisch, _Protein structure-based drug design: from docking to molecular dynamics._ Current Opinion in Structural Biology, 2018. **48** : p. 93-102.

55. Murata, K. and M. Wolf, _Cryo-electron microscopy for structural analysis of dynamic biological macromolecules._ Biochimica et Biophysica Acta (BBA) - General Subjects, 2018. **1862** (2): p. 324-334.

56. Pearson, W.R. and M.L. Sierk, _The limits of protein sequence comparison?_ Current Opinion in Structural Biology, 2005. **15** (3): p. 254-260.

57. Lagassé, H.A.D. _et al._ , _Recent advances in (therapeutic protein) drug development._ F1000Research, 2017. **6** : p. 113.

58. Fala, L., _Nucala (Mepolizumab): First IL-5 Antagonist Monoclonal Antibody FDA Approved for Maintenance Treatment of Patients with Severe Asthma._ American Health & Drug Benefits, 2016. **9** (Spec Feature): p. 106-110.

59. Raedler, L.A., _Empliciti (Elotuzumab): First SLAMF7 Antibody Therapy Approved for the Treatment of Patients with Previously Treated Multiple Myeloma._ American Health & Drug Benefits, 2016. **9** (Spec Feature): p. 74-77.

60. Singh, A.D. and S. Parmar, _Ramucirumab (Cyramza): A Breakthrough Treatment for Gastric Cancer._ Pharmacy and Therapeutics, 2015. **40** (7): p. 430-468.

61. Khan, M.A. and J.A. Haller, _Ocriplasmin for Treatment of Vitreomacular Traction: An Update._ Ophthalmology and Therapy, 2016. **5** (2): p. 147-159.

62. Ramsey, L.B. _et al._ , _Consensus Guideline for Use of Glucarpidase in Patients with High_ ‐ _Dose Methotrexate Induced Acute Kidney Injury and Delayed Methotrexate Clearance._ The Oncologist, 2017.

63. Franchini, M. and P.M. Mannucci, _Von Willebrand factor (Vonvendi®): the first recombinant product licensed for the treatment of von Willebrand disease._ Expert Review of Hematology, 2016. **9** (9): p. 825-830.

64. Zimmer, M., _Green Fluorescent Protein (GFP):  Applications, Structure, and Related Photophysical Behavior._ Chemical Reviews, 2002. **102** (3): p. 759-782.

65. Hsu, P.D., E.S. Lander, and F. Zhang, _Development and Applications of CRISPR-Cas9 for Genome Engineering._ Cell, 2014. **157** (6): p. 1262-1278.

66. Robinson, R., _What Governs Enzyme Activity? For One Enzyme, Charge Contributes Only Weakly._ PLoS Biology, 2006. **4** (4): p. e133.

67. Singh, R. _et al._ , _Microbial enzymes: industrial progress in 21st century._ 3 Biotech, 2016. **6** (2): p. 174.

68. Wells, A.S. _et al._ , _Use of Enzymes in the Manufacture of Active Pharmaceutical Ingredients — A Science and Safety-Based Approach To Ensure Patient Safety and Drug Quality._ Organic Process Research & Development, 2012. **16** (12): p. 1986-1993.

69. de Souza, P.M. and P. de Oliveira Magalhães, _Application of microbial α -amylase in industry – A review._ Brazilian Journal of Microbiology, 2010. **41** (4): p. 850-861.

70. Garg, G. _et al._ , _Microbial pectinases: an ecofriendly tool of nature for industries._ 3 Biotech, 2016. **6** (1): p. 47.

91

71. Saqib, S. _et al._ , _Sources of β -galactosidase and its applications in food industry._ 3 Biotech, 2017. **7** (1): p. 79.

72. Przybysz Buzała, K. _et al._ , _Effect of Cellulases and Xylanases on Refining Process and Kraft Pulp Properties._ PLOS ONE, 2016. **11** (8): p. e0161575.

73. Olsen, H.S. and P. Falholt, _The role of enzymes in modern detergency._ Journal of Surfactants and Detergents, 1998. **1** (4): p. 555-567.

74. Noraini, M.Y. _et al._ , _A review on potential enzymatic reaction for biofuel production from algae._ Renewable and Sustainable Energy Reviews, 2014. **39** : p. 24-34.

75. Ye, X. _et al._ , _Engineering the Provitamin A (β -Carotene) Biosynthetic Pathway into (Carotenoid-Free) Rice Endosperm._ Science, 2000. **287** (5451): p. 303-305.

76. Paine, J.A. _et al._ , _Improving the nutritional value of Golden Rice through increased provitamin A content._ Nature Biotechnology, 2005. **23** : p. 482.

77. Dawe, D., R. Robertson, and L. Unnevehr, _Golden rice: what role could it play in alleviation of vitamin A deficiency?_ Food Policy, 2002. **27** (5): p. 541-560.

78. Tang, G. _et al._ , _Golden Rice is an effective source of vitamin A._ The American Journal of Clinical Nutrition, 2009. **89** (6): p. 1776-1783.

79. Tang, G. _et al._ , _β - Carotene in Golden Rice is as good as β -carotene in oil at providing vitamin A to children._ The American Journal of Clinical Nutrition, 2012. **96** (3): p. 658664.

80. _Micronutrient deficiencies_ . World Health Organization.  Acessed on: Available from: <u>http://www.who.int/nutrition/topics/vad/en (cited October 15th 2018).</u>

81. Braun, P. _et al._ , _Plant Protein Interactomes._ Annual Review of Plant Biology, 2013. **64** (1): p. 161-187.

82. Pandey, P. _et al._ , _Impact of Combined Abiotic and Biotic Stresses on Plant Growth and Avenues for Crop Improvement by Exploiting Physio-morphological Traits._ Frontiers in Plant Science, 2017. **8** : p. 537.

83. Luo, M. _et al._ , _Comparative Proteomics of Contrasting Maize Genotypes Provides Insights into Salt-Stress Tolerance Mechanisms._ Journal of Proteome Research, 2018. **17** (1): p. 141-153.

84. Michaletti, A. _et al._ , _Metabolomics and proteomics reveal drought-stress responses of leaf tissues from spring-wheat._ Scientific Reports, 2018. **8** (1): p. 5710.

85. Brun, G. _et al._ , _Seed germination in parasitic plants: what insights can we expect from strigolactone research?_ Journal of Experimental Botany, 2018. **69** (9): p. 2265-2280.

86. Vékey, K., A. Telekes, and A. Vertes, _Medical Applications of Mass Spectrometry_ . 2008, Amsterdam: Elsevier. 561-581.

87. Winter, D. and H. Steen, _Optimization of cell lysis and protein digestion protocols for the analysis of HeLa S3 cells by LC-MS/MS._ Proteomics, 2011. **11** (24): p. 4726-4730.

88. Moore, S.M., S.M. Hess, and J.W. Jorgenson, _Extraction, Enrichment, Solubilization, and Digestion Techniques for Membrane Proteomics._ Journal of Proteome Research, 2016. **15** (4): p. 1243-1252.

89. Compton, P.D. _et al._ , _Native Proteomics: A New Approach to Protein Complex Discovery and Characterization._ The FASEB Journal, 2017. **31** (1_supplement): p. 760.2-760.2.

90. Karpievitch, Y.V. _et al._ , _Liquid Chromatography Mass Spectrometry-Based Proteomics: Biological and Technological Aspects._ The annals of applied statistics, 2010. **4** (4): p. 1797-1823.

91. Zhang, Y. _et al._ , _Protein Analysis by Shotgun/Bottom-up Proteomics._ Chemical Reviews, 2013. **113** (4): p. 2343-2394.

92. Cristobal, A. _et al._ , _Toward an Optimized Workflow for Middle-Down Proteomics._ Analytical Chemistry, 2017. **89** (6): p. 3318-3325.

93. Choudhary, G. _et al._ , _Multiple Enzymatic Digestion for Enhanced Sequence Coverage of Proteins in Complex Proteomic Mixtures Using Capillary LC with Ion Trap MS/MS._ Journal of Proteome Research, 2003. **2** (1): p. 59-67.

92

94. Swaney, D.L., C.D. Wenger, and J.J. Coon, _Value of using multiple proteases for largescale mass spectrometry-based proteomics._ Journal of Proteome Research, 2010. **9** (3): p. 1323-1329.

95. López-Ferrer, D. _et al._ , _Pressurized Pepsin Digestion in Proteomics._ AN AUTOMATABLE ALTERNATIVE TO TRYPSIN FOR INTEGRATED TOP-DOWN BOTTOM-UP PROTEOMICS*, 2011. **10** (2): p. M110.001479.

96. Peng, M. _et al._ , _Protease bias in absolute protein quantitation._ Nature Methods, 2012. **9** (6): p. 524-525.

97. Meyer, J.G. _et al._ , _Expanding proteome coverage with orthogonal- specificity α -lytic proteases._ Molecular & Cellular Proteomics, 2014. **13** (3): p. 823-835.

98. Guo, X. _et al._ , _Confetti: A Multiprotease Map of the HeLa Proteome for Comprehensive Proteomics._ Molecular & Cellular Proteomics, 2014. **13** (6): p. 1573-1584.

99. Giansanti, P. _et al._ , _Six alternative proteases for mass spectrometry – based proteomics beyond trypsin._ Nature Protocols, 2016. **11** : p. 993.

100. Bian, Y. _et al._ , _Improve the Coverage for the Analysis of Phosphoproteome of HeLa Cells by a Tandem Digestion Approach._ Journal of Proteome Research, 2012. **11** (5): p. 2828-2837.

101. Huesgen, P.F. _et al._ , _LysargiNase mirrors trypsin for protein C-terminal and methylation-site identification._ Nature Methods, 2014. **12** : p. 55.

102. Tsiatsiani, L. and A.J.R. Heck, _Proteomics beyond trypsin._ The FEBS Journal, 2015. **282** (14): p. 2612-2626.

103. Wu, C. _et al._ , _A protease for 'middle-down' proteomics._ Nature Methods, 2012. **9** : p. 822.

104. Zhang, X., _Less is More: Membrane Protein Digestion Beyond Urea-Trypsin Solution for Next-level Proteomics._ Molecular & cellular proteomics, 2015. **14** (9): p. 2441-2453.

105. Chen, E.I. _et al._ , _Optimization of mass spectrometry-compatible surfactants for shotgun proteomics._ Journal of Proteome Research, 2007. **6** (7): p. 2529-2538.

106. Proc, J.L. _et al._ , _A quantitative study of the effects of chaotropic agents, surfactants, and solvents on the digestion efficiency of human plasma proteins by trypsin._ Journal of Proteome Research, 2010. **9** (10): p. 5422-5437.

107. Rundlett, K.L. and D.W. Armstrong, _Mechanism of Signal Suppression by Anionic Surfactants in Capillary Electrophoresis−Electrospray Ionization Mass Spectrom etry._ Analytical Chemistry, 1996. **68** (19): p. 3493-3497.

108. Botelho, D. _et al._ , _Top-Down and Bottom-Up Proteomics of SDS-Containing Solutions Following Mass-Based Separation._ Journal of Proteome Research, 2010. **9** (6): p. 28632870.

109. Ilavenil, S. _et al._ , _Removal of SDS from biological protein digests for proteomic analysis by mass spectrometry._ Proteome Science, 2016. **14** (1): p. 11.

110. HaileMariam, M. _et al._ , _S-Trap, an Ultrafast Sample-Preparation Approach for Shotgun Proteomics._ Journal of Proteome Research, 2018. **17** (9): p. 2917-2924.

111. Kim, S.C. _et al._ , _A Clean, More Efficient Method for In-Solution Digestion of Protein Mixtures without Detergent or Urea._ Journal of Proteome Research, 2006. **5** (12): p. 3446-3452.

112. Hodge, K. _et al._ , _Cleaning up the masses: Exclusion lists to reduce contamination with HPLC-MS/MS._ Journal of Proteomics, 2013. **88** : p. 92-103.

113. Gunawardena, H.P., J.F. Emory, and S.A. McLuckey, _Phosphopeptide Anion Characterization via Sequential Charge Inversion and Electron-Transfer Dissociation._ Analytical Chemistry, 2006. **78** (11): p. 3788-3793.

114. Chouchani, E.T. _et al._ , _Proteomic approaches to the characterization of protein thiol modification._ Current Opinion in Chemical Biology, 2011. **15** (1): p. 120-128.

115. Riley, N.M. and J.J. Coon, _Phosphoproteomics in the Age of Rapid and Deep Proteome Profiling._ Analytical Chemistry, 2016. **88** (1): p. 74-94.

116. Swaney, D.L. and J. Villén, _Proteomic Analysis of Protein Posttranslational Modifications by Mass Spectrometry._ Cold Spring Harbor Protocols, 2016. **2016** (3): p. pdb.top077743.

93

117. Doll, S. and A.L. Burlingame, _Mass Spectrometry-Based Detection and Assignment of Protein Posttranslational Modifications._ ACS Chemical Biology, 2015. **10** (1): p. 63-71.

118. Nagaraj, N. _et al._ , _System-wide perturbation analysis with nearly complete coverage of the yeast proteome by single-shot ultra HPLC runs on a bench top Orbitrap._ Molecular & Cellular Proteomics, 2012. **11** (3): p. M111.013722-M111.013722.

119. Washburn, M.P., D. Wolters, and J.R. Yates, 3rd, _Large-scale analysis of the yeast proteome by multidimensional protein identification technology._ Nature Biotechnology, 2001. **19** (3): p. 242-7.

120. Panchaud, A. _et al._ , _Precursor acquisition independent from ion count: how to dive deeper into the proteomics ocean._ Analytical Chemistry, 2009. **81** (15): p. 6481-6488.

121. Szájli, E., T. Fehér, and K.F. Medzihradszky, _Investigating the Quantitative Nature of MALDI-TOF MS._ Molecular & Cellular Proteomics, 2008. **7** (12): p. 2410-2418.

122. Wilm, M., _Principles of electrospray ionization._ Molecular & Cellular Proteomics, 2011. **10** (7): p. M111.009407.

123. Riley, N.M. _et al._ , _The Negative Mode Proteome with Activated Ion Negative Electron Transfer Dissociation (AI-NETD)._ Molecular & Cellular Proteomics, 2015. **14** (10): p. 2644-2660.

124. Wang, N. and L. Li, _Exploring the Precursor Ion Exclusion Feature of Liquid Chromatography−Electrospray Ionization Quadrupole Time -of-Flight Mass Spectrometry for Improving Protein Identification in Shotgun Proteome Analysis._ Analytical Chemistry, 2008. **80** (12): p. 4696-4710.

125. Mitchell Wells, J. and S.A. McLuckey, _Collision_ ‐ _Induced Dissociation (CID) of Peptides and Proteins_ , in _Methods in Enzymology_ . 2005, Academic Press. p. 148-185.

126. Olsen, J.V. _et al._ , _Higher-energy C-trap dissociation for peptide modification analysis._ Nature Methods, 2007. **4** (9): p. 709-712.

127. Molina, H. _et al._ , _Global proteomic profiling of phosphopeptides using electron transfer dissociation tandem mass spectrometry._ Proceedings of the National Academy of Sciences of the United States of America, 2007. **104** (7): p. 2199-2204.

128. Chi, A. _et al._ , _Analysis of phosphorylation sites on proteins from Saccharomyces cerevisiae by electron transfer dissociation (ETD) mass spectrometry._ Proceedings of the National Academy of Sciences of the United States of America, 2007. **104** (7): p. 2193-2198.

129. Smith, S.A. _et al._ , _Enhanced Characterization of Singly Protonated Phosphopeptide Ions by Femtosecond Laser-induced Ionization/Dissociation Tandem Mass Spectrometry (fs-LID-MS/MS)._ Journal of the American Society for Mass Spectrometry, 2010. **21** (12): p. 2031-2040.

130. Fort, K.L. _et al._ , _Implementation of Ultraviolet Photodissociation on a Benchtop Q Exactive Mass Spectrometer and Its Application to Phosphoproteomics._ Analytical Chemistry, 2016. **88** (4): p. 2303-2310.

131. Mayfield, J.E. _et al._ , _Mapping the Phosphorylation Pattern of Drosophila melanogaster RNA Polymerase II Carboxyl-Terminal Domain Using Ultraviolet Photodissociation Mass Spectrometry._ ACS Chemical Biology, 2017. **12** (1): p. 153-162.

132. Robinson, M.R. _et al._ , _193 nm Ultraviolet Photodissociation Mass Spectrometry for Phosphopeptide Characterization in the Positive and Negative Ion Modes._ Journal of Proteome Research, 2016. **15** (8): p. 2739-2748.

133. Pejchinovski, M. _et al._ , _Comparison of higher energy collisional dissociation and collision-induced dissociation MS/MS sequencing methods for identification of naturally occurring peptides in human urine._ PROTEOMICS – Clinical Applications, 2015. **9** (56): p. 531-542.

134. Murray Kermit, K. _et al._ , _Definitions of terms relating to mass spectrometry (IUPAC Recommendations 2013)_ , in _Pure and Applied Chemistry_ . 2013. p. 1515.

135. Geiger, T., J. Cox, and M. Mann, _Proteomics on an Orbitrap Benchtop Mass Spectrometer Using All-ion Fragmentation._ Molecular & Cellular Proteomics, 2010. **9** (10): p. 2252-2261.

94

136. Steen, H. and M. Mann, _The abc's (and xyz's) of peptide sequencing._ Nature Reviews Molecular Cell Biology, 2004. **5** : p. 699.

137. Michalski, A. _et al._ , _A Systematic Investigation into the Nature of Tryptic HCD Spectra._ Journal of Proteome Research, 2012. **11** (11): p. 5479-5491.

138. Frese, C.K. _et al._ , _Improved Peptide Identification by Targeted Fragmentation Using CID, HCD and ETD on an LTQ-Orbitrap Velos._ Journal of Proteome Research, 2011. **10** (5): p. 2377-2388.

139. Shao, C., Y. Zhang, and W. Sun, _Statistical characterization of HCD fragmentation patterns of tryptic peptides on an LTQ Orbitrap Velos mass spectrometer._ Journal of Proteomics, 2014. **109** : p. 26-37.

140. Bekker-Jensen, D.B. _et al._ , _An Optimized Shotgun Strategy for the Rapid Generation of Comprehensive Human Proteomes._ Cell Systems, 2017. **4** (6): p. 587-599.e4.

141. Shishkova, E., A.S. Hebert, and J.J. Coon, _Now, More Than Ever, Proteomics Needs Better Chromatography._ Cell Systems, 2016. **3** (4): p. 321-324.

142. Mann, M. _et al._ , _The Coming Age of Complete, Accurate, and Ubiquitous Proteomes._ Molecular Cell, 2013. **49** (4): p. 583-590.

143. Martens, L. and J.A. Vizcaíno, _A Golden Age for Working with Public Proteomics Data._ Trends in Biochemical Sciences, 2017. **42** (5): p. 333-341.

144. Matsumoto, A. _et al._ , _mTORC1 and muscle regeneration are regulated by the LINC00961-encoded SPAR polypeptide._ Nature, 2016. **541** : p. 228.

145. Feigin, C.Y. _et al._ , _Genome of the Tasmanian tiger provides insights into the evolution and demography of an extinct marsupial carnivore._ Nature Ecology & Evolution, 2018. **2** (1): p. 182-192.

146. Nowoshilow, S. _et al._ , _The axolotl genome and the evolution of key tissue formation regulators._ Nature, 2018. **554** : p. 50.

147. Gutekunst, J. _et al._ , _Clonal genome evolution and rapid invasive spread of the marbled crayfish._ Nature Ecology & Evolution, 2018. **2** (3): p. 567-573.

148. Jaiswal, S.K. _et al._ , _Genome Sequence of Indian Peacock Reveals the Peculiar Case of a Glittering Bird._ bioRxiv, 2018.

149. Edwards, R.J. _et al._ , _Draft genome assembly of the invasive cane toad, Rhinella marina._ GigaScience, 2018. **7** (9): p. giy095-giy095.

150. Stricker, S.H., A. Köferle, and S. Beck, _From profiles to function in epigenomics._ Nature Reviews Genetics, 2016. **18** : p. 51.

151. Lowe, R. _et al._ , _Transcriptomics technologies._ PLOS Computational Biology, 2017. **13** (5): p. e1005457.

152. Hershey, J.W.B., N. Sonenberg, and M.B. Mathews, _Principles of Translational Control: An Overview._ Cold Spring Harbor Perspectives in Biology, 2012. **4** (12).

153. Brar, G.A. and J.S. Weissman, _Ribosome profiling reveals the what, when, where and how of protein synthesis._ Nature Reviews Molecular Cell Biology, 2015. **16** (11): p. 651664.

154. Acharjee, A. _et al._ , _Integration of metabolomics, lipidomics and clinical data using a machine learning method._ BMC Bioinformatics, 2016. **17** (15): p. 440.

155. Coman, C. _et al._ , _Simultaneous Metabolite, Protein, Lipid Extraction (SIMPLEX): A Combinatorial Multimolecular Omics Approach for Systems Biology._ Molecular & Cellular Proteomics, 2016. **15** (4): p. 1453-1466.

156. Gingras, A.-C. and B. Raught, _Beyond hairballs: The use of quantitative mass spectrometry data to understand protein – protein interactions._ FEBS Letters, 2012. **586** (17): p. 2723-2731.

157. Wohlgemuth, I., C. Lenz, and H. Urlaub, _Studying macromolecular complex stoichiometries by peptide-based mass spectrometry._ Proteomics, 2015. **15** (5-6): p. 862-879.

158. Bauer, A. and B. Kuster, _Affinity purification-mass spectrometry._ European Journal of Biochemistry, 2003. **270** (4): p. 570-578.

159. Hein, Marco Y. _et al._ , _A Human Interactome in Three Quantitative Dimensions Organized by Stoichiometries and Abundances._ Cell, 2015. **163** (3): p. 712-723.

95

160. Schopper, S. _et al._ , _Measuring protein structural changes on a proteome-wide scale using limited proteolysis-coupled mass spectrometry._ Nature Protocols, 2017. **12** : p. 2391.

161. Dearmond, P.D. _et al._ , _Discovery of novel cyclophilin A ligands using an H/D exchangeand mass spectrometry-based strategy._ Journal of Biomolecular Screening, 2010. **15** (9): p. 1051-1062.

162. Strickland, E.C. _et al._ , _Thermodynamic analysis of protein-ligand binding interactions in complex biological mixtures using the stability of proteins from rates of oxidation._ Nature Protocols, 2012. **8** : p. 148.

163. Ong, S.-E. _et al._ , _Identifying the proteins to which small-molecule probes and drugs bind in cells._ Proceedings of the National Academy of Sciences, 2009. **106** (12): p. 4617-4622.

164. Huber, K. _et al._ , _Approaching cellular resolution and reliable identification in mass spectrometry imaging of tryptic peptides._ Analytical and Bioanalytical Chemistry, 2018. **410** (23): p. 5825-5837.

165. Bandura, D.R. _et al._ , _Mass Cytometry: Technique for Real Time Single Cell Multitarget Immunoassay Based on Inductively Coupled Plasma Time-of-Flight Mass Spectrometry._ Analytical Chemistry, 2009. **81** (16): p. 6813-6822.

166. Itzhak, D.N. _et al._ , _A Mass Spectrometry-Based Approach for Mapping Protein Subcellular Localization Reveals the Spatial Proteome of Mouse Primary Neurons._ Cell Reports, 2017. **20** (11): p. 2706-2718.

167. Mulvey, C.M. _et al._ , _Using hyperLOPIT to perform high-resolution mapping of the spatial proteome._ Nature Protocols, 2017. **12** : p. 1110.

168. Sharon, M., _How Far Can We Go with Structural Mass Spectrometry of Protein Complexes?_ Journal of the American Society for Mass Spectrometry, 2010. **21** (4): p. 487-500.

169. Painter, A.J. _et al._ , _Real-Time Monitoring of Protein Complexes Reveals their Quaternary Organization and Dynamics._ Chemistry & Biology, 2008. **15** (3): p. 246-253.

170. Skinner, O.S. _et al._ , _Top-down characterization of endogenous protein complexes with native proteomics._ Nature chemical biology, 2018. **14** (1): p. 36-41.

171. Hall, Z., A. Politis, and Carol V. Robinson, _Structural Modeling of Heteromeric Protein Complexes from Disassembly Pathways and Ion Mobility-Mass Spectrometry._ Structure, 2012. **20** (9): p. 1596-1609.

172. Kostyukevich, Y. _et al._ , _Hydrogen/deuterium exchange in mass spectrometry._ Mass Spectrometry Reviews, 2018. **37** (6): p. 811-853.

173. Leitner, A. _et al._ , _Crosslinking and Mass Spectrometry: An Integrated Technology to Understand the Structure and Function of Molecular Machines._ Trends in Biochemical Sciences, 2016. **41** (1): p. 20-32.

174. Ishihama, Y. _et al._ , _Exponentially Modified Protein Abundance Index (emPAI) for Estimation of Absolute Protein Amount in Proteomics by the Number of Sequenced Peptides per Protein._ Molecular & Cellular Proteomics, 2005. **4** (9): p. 1265-1272.

175. Braisted, J.C. _et al._ , _The APEX Quantitative Proteomics Tool: generating protein quantitation estimates from LC-MS/MS proteomics results._ BMC Bioinformatics, 2008. **9** : p. 529-529.

176. Collins, M.O., L. Yu, and J.S. Choudhary, _Analysis of protein phosphorylation on a proteome-scale._ Proteomics, 2007. **7** (16): p. 2751-2768.

177. Li, X. _et al._ , _Elucidating Human Phosphatase-Substrate Networks._ Science Signaling, 2013. **6** (275): p. rs10-rs10.

178. Klaeger, S. _et al._ , _The target landscape of clinical kinase drugs._ Science, 2017. **358** (6367): p. eaan4368.

179. Zagorac, I. _et al._ , _In vivo phosphoproteomics reveals kinase activity profiles that predict treatment outcome in triple-negative breast cancer._ Nature Communications, 2018. **9** (1): p. 3501.

180. Fíla, J. and D. Honys, _Enrichment techniques employed in phosphoproteomics._ Amino Acids, 2012. **43** (3): p. 1025-1047.

96

181. Phillips, D.M., _The presence of acetyl groups of histones._ The Biochemical journal, 1963. **87** (2): p. 258-263.

182. Allfrey, V.G., R. Faulkner, and A.E. Mirsky, _ACETYLATION AND METHYLATION OF HISTONES AND THEIR POSSIBLE ROLE IN THE REGULATION OF RNA SYNTHESIS._ Proceedings of the National Academy of Sciences of the United States of America, 1964. **51** (5): p. 786-794.

183. Drazic, A. _et al._ , _The world of protein acetylation._ Biochimica et Biophysica Acta (BBA) - Proteins and Proteomics, 2016. **1864** (10): p. 1372-1401.

184. Kouzarides, T., _Chromatin Modifications and Their Function._ Cell, 2007. **128** (4): p. 693705.

185. Behnia, R. _et al._ , _Targeting of the Arf-like GTPase Arl3p to the Golgi requires N-terminal acetylation and the membrane protein Sys1p._ Nature Cell Biology, 2004. **6** : p. 405.

186. Setty, S.R.G. _et al._ , _Golgi targeting of ARF- like GTPase Arl3p requires its Nα - acetylation and the integral membrane protein Sys1p._ Nature Cell Biology, 2004. **6** : p. 414.

187. Behnia, R. _et al._ , _The yeast orthologue of GRASP65 forms a complex with a coiled-coil protein that contributes to ER to Golgi traffic._ The Journal of Cell Biology, 2007. **176** (3): p. 255-261.

188. Forte, G.M.A., M.R. Pool, and C.J. Stirling, _N-Terminal Acetylation Inhibits Protein Targeting to the Endoplasmic Reticulum._ PLOS Biology, 2011. **9** (5): p. e1001073.

189. Holmes, W.M. _et al._ , _Loss of amino-terminal acetylation suppresses a prion phenotype by modulating global protein folding._ Nature Communications, 2014. **5** : p. 4383.

190. Kuo, H.-P. _et al._ , _ARD1 Stabilization of TSC2 Suppresses Tumorigenesis Through the mTOR Signaling Pathway._ Science Signaling, 2010. **3** (108): p. ra9-ra9.

191. Zhang, X. _et al._ , _HDAC6 Modulates Cell Motility by Altering the Acetylation Level of Cortactin._ Molecular Cell, 2007. **27** (2): p. 197-213.

192. Biggar, K.K. and S.S.C. Li, _Non-histone protein methylation as a regulator of cellular signalling and function._ Nature Reviews Molecular Cell Biology, 2014. **16** : p. 5.

193. Murn, J. and Y. Shi, _The winding path of protein methylation research: milestones and new frontiers._ Nature Reviews Molecular Cell Biology, 2017. **18** : p. 517.

194. Van Damme, P. _et al._ , _A review of COFRADIC techniques targeting protein N-terminal acetylation._ BMC proceedings, 2009. **3 Suppl 6** (Suppl 6): p. S6-S6.

195. Kori, Y. _et al._ , _Proteome-wide acetylation dynamics in human cells._ Scientific Reports, 2017. **7** (1): p. 10296.

196. Carlson, S.M. _et al._ , _Proteome-wide enrichment of proteins modified by lysine methylation._ Nature Protocols, 2014. **9** (1): p. 37-50.

197. Lu, H., Y. Zhang, and P. Yang, _Advancements in mass spectrometry-based glycoproteomics and glycomics._ National Science Review, 2016. **3** (3): p. 345-364.

198. Kopitz, J., _Lipid glycosylation: a primer for histochemists and cell biologists._ Histochemistry and Cell Biology, 2017. **147** (2): p. 175-198.

199. Shental-Bechor, D. and Y. Levy, _Effect of glycosylation on protein folding: a close look at thermodynamic stabilization._ Proceedings of the National Academy of Sciences of the United States of America, 2008. **105** (24): p. 8256-8261.

200. Solá, R.J. and K. Griebenow, _Effects of glycosylation on the stability of protein pharmaceuticals._ Journal of Pharmaceutical Sciences, 2009. **98** (4): p. 1223-1245.

201. Lee, H.S., Y. Qi, and W. Im, _Effects of N-glycosylation on protein conformation and dynamics: Protein Data Bank analysis and molecular dynamics simulation study._ Scientific Reports, 2015. **5** : p. 8926-8926.

202. Ahmad, I. _et al._ , _Phosphorylation and glycosylation interplay: Protein modifications at hydroxy amino acids and prediction of signaling functions of the human β3 integrin family._ Journal of Cellular Biochemistry, 2006. **99** (3): p. 706-718.

203. Pinho, S.S. and C.A. Reis, _Glycosylation in cancer: mechanisms and clinical implications._ Nature Reviews Cancer, 2015. **15** : p. 540.

97

204. Schnaar, R.L., _Glycans and glycan-binding proteins in immune regulation: A concise introduction to glycobiology for the allergist._ The Journal of allergy and clinical immunology, 2015. **135** (3): p. 609-615.

205. Razaghi, A. _et al._ , _Improved therapeutic efficacy of mammalian expressed-recombinant interferon gamma against ovarian cancer cells._ Experimental Cell Research, 2017. **359** (1): p. 20-29.

206. Pan, S. _et al._ , _Mass spectrometry based glycoproteomics--from a proteomics perspective._ Molecular & Cellular Proteomics, 2011. **10** (1): p. R110.003251R110.003251.

207. McDowell, G.S. and A. Philpott, _Non-canonical ubiquitylation: Mechanisms and consequences._ The International Journal of Biochemistry & Cell Biology, 2013. **45** (8): p. 1833-1842.

208. Kresge, N., R.D. Simoni, and R.L. Hill, _The Discovery of Ubiquitin-mediated Proteolysis by Aaron Ciechanover, Avram Hershko, and Irwin Rose._ Journal of Biological Chemistry, 2006. **281** (40): p. e32.

209. Jin, L. _et al._ , _Mechanism of Ubiquitin-Chain Formation by the Human AnaphasePromoting Complex._ Cell, 2008. **133** (4): p. 653-665.

210. Swatek, K.N. and D. Komander, _Ubiquitin modifications._ Cell Research, 2016. **26** : p. 399.

211. Xu, G. and S.R. Jaffrey, _Proteomic identification of protein ubiquitination events._ Biotechnology and Genetic Engineering Reviews, 2013. **29** (1): p. 73-109.

212. Esteban Warren, M.R. _et al._ , _Electrospray ionization tandem mass spectrometry of model peptides reveals diagnostic fragment ions for protein ubiquitination._ Rapid Communications in Mass Spectrometry, 2005. **19** (4): p. 429-437.

213. Denis, N.J. _et al._ , _Tryptic digestion of ubiquitin standards reveals an improved strategy for identifying ubiquitinated proteins by mass spectrometry._ Proteomics, 2007. **7** (6): p. 868-874.

214. Xu, G., J.S. Paige, and S.R. Jaffrey, _Global analysis of lysine ubiquitination by ubiquitin remnant immunoaffinity profiling._ Nature Biotechnology, 2010. **28** : p. 868.

215. Danielsen, J.M.R. _et al._ , _Mass Spectrometric Analysis of Lysine Ubiquitylation Reveals Promiscuity at Site Level._ Molecular & Cellular Proteomics, 2011. **10** (3): p. M110.003590.

216. Kim, W. _et al._ , _Systematic and Quantitative Assessment of the Ubiquitin-Modified Proteome._ Molecular Cell, 2011. **44** (2): p. 325-340.

217. Stes, E. _et al._ , _A COFRADIC Protocol To Study Protein Ubiquitination._ Journal of Proteome Research, 2014. **13** (6): p. 3107-3113.

218. Impens, F. _et al._ , _Mapping of SUMO sites and analysis of SUMOylation changes induced by external stimuli._ Proceedings of the National Academy of Sciences, 2014. **111** (34): p. 12432-12437.

219. Hendriks, I.A. and A.C.O. Vertegaal, _A comprehensive compilation of SUMO proteomics._ Nature Reviews Molecular Cell Biology, 2016. **17** : p. 581.

220. Jones, J. _et al._ , _A targeted proteomic analysis of the ubiquitin-like modifier nedd8 and associated proteins._ Journal of Proteome Research, 2008. **7** (3): p. 1274-1287.

221. Maghames, C.M. _et al._ , _NEDDylation promotes nuclear protein aggregation and protects the Ubiquitin Proteasome System upon proteotoxic stress._ Nature Communications, 2018. **9** (1): p. 4376.

222. Giannakopoulos, N.V. _et al._ , _Proteomic identification of proteins conjugated to ISG15 in mouse and human cells._ Biochemical and Biophysical Research Communications, 2005. **336** (2): p. 496-506.

223. Radoshevich, L. _et al._ , _ISG15 counteracts Listeria monocytogenes infection._ eLife, 2015. **4** : p. e06848.

224. Anderle, M. _et al._ , _Quantifying reproducibility for differential proteomics: noise analysis for protein liquid chromatography-mass spectrometry of human serum._ Bioinformatics, 2004. **20** (18): p. 3575-3582.

98

225. Marginean, I. _et al._ , _Analytical characterization of the electrospray ion source in the nanoflow regime._ Analytical Chemistry, 2008. **80** (17): p. 6573-6579.

226. Li, Z. _et al._ , _Systematic Comparison of Label-Free, Metabolic Labeling, and Isobaric Chemical Labeling for Quantitative Proteomics on LTQ Orbitrap Velos._ Journal of Proteome Research, 2012. **11** (3): p. 1582-1590.

227. Thompson, A. _et al._ , _Tandem Mass Tags:  A Novel Quantification Strategy for Comparative Analysis of Complex Protein Mixtures by MS/MS._ Analytical Chemistry, 2003. **75** (8): p. 1895-1904.

228. Bantscheff, M. _et al._ , _Quantitative mass spectrometry in proteomics: critical review update from 2007 to the present._ Analytical and Bioanalytical Chemistry, 2012. **404** (4): p. 939-965.

229. Pipkin, J.L. _et al._ , _Analysis of protein incorporation of radioactive isotopes in the chinese hamster ovary cell cycle by electronic sorting and gel microelectrophoresis._ Cytometry, 1986. **7** (2): p. 147-156.

230. Oda, Y. _et al._ , _Accurate quantitation of protein expression and site-specific phosphorylation._ Proceedings of the National Academy of Sciences, 1999. **96** (12): p. 6591-6596.

231. Farquhar, G.D., J.R. Ehleringer, and K.T. Hubick, _Carbon Isotope Discrimination and Photosynthesis._ Annual Review of Plant Physiology and Plant Molecular Biology, 1989. **40** (1): p. 503-537.

232. Conen, F. and A. Neftel, _Do increasingly depleted δ15N values of atmospheric N2O indicate a decline in soil N2O reduction?_ Biogeochemistry, 2007. **82** (3): p. 321-326.

233. Zubarev, R.A., _Role of Stable Isotopes in Life — Testing Isotopic Resonance Hypothesis._ Genomics, Proteomics & Bioinformatics, 2011. **9** (1): p. 15-20.

234. Li, X. and M.P. Snyder, _Can heavy isotopes increase lifespan? Studies of relative abundance in various organisms reveal chemical perspectives on aging._ BioEssays : news and reviews in molecular, cellular and developmental biology, 2016. **38** (11): p. 1093-1101.

235. Conrads, T.P. _et al._ , _Quantitative Analysis of Bacterial and Mammalian Proteomes Using a Combination of Cysteine Affinity Tags and_<sup>_15_</sup> _N-Metabolic Labeling._ Analytical Chemistry, 2001. **73** (9): p. 2132-2139.

236. Wu, C.C. _et al._ , _Metabolic Labeling of Mammalian Organisms with Stable Isotopes for Quantitative Proteomic Analysis._ Analytical Chemistry, 2004. **76** (17): p. 4951-4959.

237. McClatchy, D.B. _et al._ ,<sup>_15_</sup> _N metabolic labeling of mammalian tissue with slow protein turnover._ Journal of Proteome Research, 2007. **6** (5): p. 2005-2010.

238. Krijgsveld, J. _et al._ , _Metabolic labeling of C. elegans and D. melanogaster for quantitative proteomics._ Nature Biotechnology, 2003. **21** : p. 927.

239. Sonzogni, A. National Nuclear Data Center, Brookhaven National Laboratory.  Acessed on: 28-11-2018. Available from: https://www.nndc.bnl.gov/chart/.

240. Beynon, R.J. and J.M. Pratt, _Metabolic Labeling of Proteins for Proteomics._ Molecular & Cellular Proteomics, 2005. **4** (7): p. 857-872.

241. Ong, S.-E. _et al._ , _Stable Isotope Labeling by Amino Acids in Cell Culture, SILAC, as a Simple and Accurate Approach to Expression Proteomics._ Molecular & Cellular Proteomics, 2002. **1** (5): p. 376-386.

242. Ong, S.-E. and M. Mann, _A practical recipe for stable isotope labeling by amino acids in cell culture (SILAC)._ Nature Protocols, 2007. **1** (6): p. 2650-2660.

243. Blagoev, B. _et al._ , _Temporal analysis of phosphotyrosine-dependent signaling networks by quantitative proteomics._ Nature Biotechnology, 2004. **22** : p. 1139.

244. Molina, H. _et al._ , _Temporal profiling of the adipocyte proteome during differentiation using a five-plex SILAC based strategy._ Journal of Proteome Research, 2009. **8** (1): p. 48-58.

245. Geiger, T. _et al._ , _Super-SILAC mix for quantitative proteomics of human tumor tissue._ Nature Methods, 2010. **7** : p. 383.

246. Shenoy, A. and T. Geiger, _Super-SILAC: current trends and future perspectives._ Expert Review of Proteomics, 2015. **12** (1): p. 13-19.

99

247. Larance, M. _et al._ , _Stable-isotope labeling with amino acids in nematodes._ Nature Methods, 2011. **8** (10): p. 849-851.

248. Sury, M.D., J.-X. Chen, and M. Selbach, _The SILAC fly allows for accurate protein quantification in vivo._ Molecular & Cellular Proteomics, 2010. **9** (10): p. 2173-2183.

249. Krüger, M. _et al._ , _SILAC Mouse for Quantitative Proteomics Uncovers Kindlin-3 as an Essential Factor for Red Blood Cell Function._ Cell, 2008. **134** (2): p. 353-364.

250. Lewandowska, D. _et al._ , _Plant SILAC: Stable-Isotope Labelling with Amino Acids of Arabidopsis Seedlings for Quantitative Proteomics._ PLoS ONE, 2013. **8** (8): p. e72207.

251. Geiger, T. _et al._ , _Use of stable isotope labeling by amino acids in cell culture as a spikein standard in quantitative proteomics._ Nature Protocols, 2011. **6** : p. 147.

252. Scheerlinck, E. _et al._ , _Assessing the impact of minimizing arginine conversion in fully defined SILAC culture medium in human embryonic stem cells._ Proteomics, 2016. **16** (20): p. 2605-2614.

253. Bendall, S.C. _et al._ , _Prevention of amino acid conversion in SILAC experiments with embryonic stem cells._ Molecular & Cellular Proteomics, 2008. **7** (9): p. 1587-1597.

254. Lößner, C. _et al._ , _Preventing arginine-to-proline conversion in a cell-line-independent manner during cell cultivation under stable isotope labeling by amino acids in cell culture (SILAC) conditions._ Analytical Biochemistry, 2011. **412** (1): p. 123-125.

255. Blagoev, B. and M. Mann, _Quantitative proteomics to study mitogen-activated protein kinases._ Methods, 2006. **40** (3): p. 243-250.

256. Ong, S.-E. and M. Mann, _Mass spectrometry – based proteomics turns quantitative._ Nature Chemical Biology, 2005. **1** : p. 252.

257. Tebbe, A. _et al._ , _Systematic evaluation of label-free and super-SILAC quantification for proteome expression analysis._ Rapid Communications in Mass Spectrometry, 2015. **29** (9): p. 795-801.

258. Liu, N.Q. _et al._ , _Quantitative Proteomic Analysis of Microdissected Breast Cancer Tissues: Comparison of Label-Free and SILAC-based Quantification with Shotgun, Directed, and Targeted MS Approaches._ Journal of Proteome Research, 2013. **12** (10): p. 4627-4641.

259. Merl, J. _et al._ , _Direct comparison of MS-based label-free and SILAC quantitative proteome profiling strategies in primary retinal Müller cells._ Proteomics, 2012. **12** (12): p. 1902-1911.

260. Houel, S. _et al._ , _Quantifying the Impact of Chimera MS/MS Spectra on Peptide Identification in Large-Scale Proteomics Studies._ Journal of Proteome Research, 2010. **9** (8): p. 4152-4160.

261. Overmyer, K.A. _et al._ , _Multiplexed proteome analysis with neutron-encoded stable isotope labeling in cells and mice._ Nature Protocols, 2018. **13** (1): p. 293-306.

262. Turck, C.W. _et al._ , _The Association of Biomolecular Resource Facilities Proteomics Research Group 2006 Study._ Relative Protein Quantitation, 2007. **6** (8): p. 1291-1298.

263. Bantscheff, M. _et al._ , _Quantitative mass spectrometry in proteomics: a critical review._ Analytical and Bioanalytical Chemistry, 2007. **389** (4): p. 1017-31.

264. Asara, J.M. _et al._ , _A label-free quantification method by MS/MS TIC compared to SILAC and spectral counting in a proteomics screen._ Proteomics, 2008. **8** (5): p. 994-999.

265. Altelaar, A.F.M. _et al._ , _Benchmarking stable isotope labeling based quantitative proteomics._ Journal of Proteomics, 2013. **88** : p. 14-26.

266. Hebert, A.S. _et al._ , _Neutron-encoded mass signatures for multiplexed proteome quantification._ Nature Methods, 2013. **10** (4): p. 332-334.

267. Hsu, J.-L. and S.-H. Chen, _Stable isotope dimethyl labelling for quantitative proteomics and beyond._ Philosophical transactions. Series A, Mathematical, physical, and engineering sciences, 2016. **374** (2079): p. 20150364.

268. Boersema, P.J. _et al._ , _Multiplex peptide stable isotope dimethyl labeling for quantitative proteomics._ Nature Protocols, 2009. **4** : p. 484.

269. Hsu, J.L. _et al._ , _Beyond quantitative proteomics: signal enhancement of the a1 ion as a mass tag for peptide sequencing using dimethyl labeling._ Journal of Proteome Research, 2005. **4** (1): p. 101-8.

100

270. Hsu, J.-L. _et al._ , _Stable-Isotope Dimethyl Labeling for Quantitative Proteomics._ Analytical Chemistry, 2003. **75** (24): p. 6843-6852.

271. Boersema, P.J. _et al._ , _Triplex protein quantification based on stable isotope labeling by peptide dimethylation applied to cell and tissue lysates._ Proteomics, 2008. **8** (22): p. 4624-4632.

272. Hsu, J.-L., S.-Y. Huang, and S.-H. Chen, _Dimethyl multiplexed labeling combined with microcolumn separation and MS analysis for time course study in proteomics._ Electrophoresis, 2006. **27** (18): p. 3652-3660.

273. Wu, Y. _et al._ , _Five-plex isotope dimethyl labeling for quantitative proteomics._ Chemical Communications, 2014. **50** (14): p. 1708-1710.

274. Wang, F. _et al._ , _A six-plex proteome quantification strategy reveals the dynamics of protein turnover._ Scientific Reports, 2013. **3** : p. 1827-1827.

275. Lau, H.-T. _et al._ , _Comparing SILAC- and stable isotope dimethyl-labeling approaches for quantitative proteomics._ Journal of Proteome Research, 2014. **13** (9): p. 4164-4174.

276. Turowski, M. _et al._ , _Deuterium Isotope Effects on Hydrophobic In teractions:  The Importance of Dispersion Interactions in the Hydrophobic Phase._ Journal of the American Chemical Society, 2003. **125** (45): p. 13836-13849.

277. Zhang, R. _et al._ , _Fractionation of Isotopically Labeled Peptides in Quantitative Proteomics._ Analytical Chemistry, 2001. **73** (21): p. 5142-5149.

278. Zhang, R. _et al._ , _Controlling Deuterium Isotope Effects in Comparative Proteomics._ Analytical Chemistry, 2002. **74** (15): p. 3662-3669.

279. Zhang, R. and F.E. Regnier, _Minimizing Resolution of Isotopically Coded Peptides in Comparative Proteomics._ Journal of Proteome Research, 2002. **1** (2): p. 139-147.

280. Schnölzer, M., P. Jedrzejewski, and W.D. Lehmann, _Protease-catalyzed incorporation of 18O into peptide fragments and its application for protein sequencing by electrospray and matrix-assisted laser desorption/ionization mass spectrometry._ ELECTROPHORESIS, 1996. **17** (5): p. 945-953.

281. Shevchenko, A. _et al._ , _Rapid ‘de novo’ peptide sequencing by a combination of nanoelectrospray, isotopic labeling and a quadrupole/time-of-flight mass spectrometer._ Rapid Communications in Mass Spectrometry, 1997. **11** (9): p. 1015-1024.

282. Uttenweiler-Joseph, S. _et al._ , _Automated de novo sequencing of proteins using the differential scanning technique._ Proteomics, 2001. **1** (5): p. 668-682.

283. Mirgorodskaya, O.A. _et al._ , _Quantitation of peptides and proteins by matrix-assisted laser desorption/ionization mass spectrometry using 18O-labeled internal standards._ Rapid Communications in Mass Spectrometry, 2000. **14** (14): p. 1226-1232.

284. Yao, X. _et al._ , _Proteolytic 18O Labeling for Comparative Proteomics:  Model Studies with Two Serotypes of Adenovirus._ Analytical Chemistry, 2001. **73** (13): p. 2836-2842.

285. Larsen, M.R. _et al._ , _Characterization of differently processed forms of enolase 2 from Saccharomyces cerevisiae by two-dimensional gel electrophoresis and mass spectrometry._ ELECTROPHORESIS, 2001. **22** (3): p. 566-575.

286. Stewart, II, T. Thomson, and D. Figeys, _18O labeling: a tool for proteomics._ Rapid Communications in Mass Spectrometry, 2001. **15** (24): p. 2456-65.

287. Ye, X. _et al._ ,<sup>_18_</sup> _O stable isotope labeling in MS-based proteomics._ Briefings in Functional Genomics & Proteomics, 2009. **8** (2): p. 136-144.

288. Ross, P.L. _et al._ , _Multiplexed Protein Quantitation in Saccharomyces cerevisiae Using Amine-reactive Isobaric Tagging Reagents._ Molecular & Cellular Proteomics, 2004. **3** (12): p. 1154-1169.

289. Sonnett, M., E. Yeung, and M. Wühr, _Accurate, Sensitive, and Precise Multiplexed Proteomics Using the Complement Reporter Ion Cluster._ Analytical Chemistry, 2018. **90** (8): p. 5032-5039.

290. Dayon, L. _et al._ , _Relative Quantification of Proteins in Human Cerebrospinal Fluids by MS/MS Using 6-Plex Isobaric Tags._ Analytical Chemistry, 2008. **80** (8): p. 2921-2931.

291. Pierce, A. _et al._ , _Eight-channel iTRAQ Enables Comparison of the Activity of Six Leukemogenic Tyrosine Kinases._ Molecular & Cellular Proteomics, 2008. **7** (5): p. 853863.

101

292. Werner, T. _et al._ , _Ion Coalescence of Neutron Encoded TMT 10-Plex Reporter Ions._ Analytical Chemistry, 2014. **86** (7): p. 3594-3601.

293. Stepanova, E., S.P. Gygi, and J.A. Paulo, _Filter-Based Protein Digestion (FPD): A Detergent-Free and Scaffold-Based Strategy for TMT Workflows._ Journal of Proteome Research, 2018. **17** (3): p. 1227-1234.

294. Zhang, J., Y. Wang, and S. Li, _Deuterium Isobaric Amine-Reactive Tags for Quantitative Proteomics._ Analytical Chemistry, 2010. **82** (18): p. 7588-7595.

295. Xiang, F. _et al._ , _N,N-Dimethyl Leucines as Novel Isobaric Tandem Mass Tags for Quantitative Proteomics and Peptidomics._ Analytical Chemistry, 2010. **82** (7): p. 28172825.

296. Frost, D.C., T. Greer, and L. Li, _High-Resolution Enabled 12-Plex DiLeu Isobaric Tags for Quantitative Proteomics._ Analytical Chemistry, 2015. **87** (3): p. 1646-1654.

297. Savitski, M.M. _et al._ , _Multiplexed Proteome Dynamics Profiling Reveals Mechanisms Controlling Protein Homeostasis._ Cell, 2018. **173** (1): p. 260-274.e25.

298. Ow, S.Y. _et al._ , _iTRAQ Underestimation in Simple and Complex Mixtures: “The Good, the Bad and the Ugly”._ Journal of Proteome Research, 2009. **8** (11): p. 5347-5355.

299. Karp, N.A. _et al._ , _Addressing Accuracy and Precision Issues in iTRAQ Quantitation._ Molecular & Cellular Proteomics, 2010. **9** (9): p. 1885-1897.

300. Hogrebe, A. _et al._ , _Benchmarking common quantification strategies for large-scale phosphoproteomics._ Nature Communications, 2018. **9** (1): p. 1045.

301. Wenger, C.D. _et al._ , _Gas-phase purification enables accurate, multiplexed proteome quantification with isobaric tagging._ Nature Methods, 2011. **8** (11): p. 933-935.

302. Sturm, R.M., C.B. Lietz, and L. Li, _Improved isobaric tandem mass tag quantification by ion mobility mass spectrometry._ Rapid Communications in Mass Spectrometry, 2014. **28** (9): p. 1051-1060.

303. Ting, L. _et al._ , _MS3 eliminates ratio distortion in isobaric multiplexed quantitative proteomics._ Nature Methods, 2011. **8** (11): p. 937-940.

304. McAlister, G.C. _et al._ , _MultiNotch MS3 Enables Accurate, Sensitive, and Multiplexed Detection of Differential Expression across Cancer Cell Line Proteomes._ Analytical Chemistry, 2014. **86** (14): p. 7150-7158.

305. Wühr, M. _et al._ , _Accurate Multiplexed Proteomics at the MS2 Level Using the Complement Reporter Ion Cluster._ Analytical Chemistry, 2012. **84** (21): p. 9214-9221.

306. Virreira Winter, S. _et al._ , _EASI-tag enables accurate multiplexed and interference-free MS2-based proteome quantification._ Nature Methods, 2018. **15** (7): p. 527-530.

307. Tu, C. _et al._ , _Systematic Assessment of Survey Scan and MS2-Based Abundance Strategies for Label-Free Quantitative Proteomics Using High-Resolution MS Data._ Journal of Proteome Research, 2014. **13** (4): p. 2069-2079.

308. Patel, V.J. _et al._ , _A Comparison of Labeling and Label-Free Mass Spectrometry-Based Proteomics Approaches._ Journal of Proteome Research, 2009. **8** (7): p. 3752-3759.

309. Latosinska, A. _et al._ , _Comparative Analysis of Label-Free and 8-Plex iTRAQ Approach for Quantitative Tissue Proteomic Analysis._ PLoS One, 2015. **10** (9): p. e0137048.

310. Piehowski, P.D. _et al._ , _Sources of Technical Variability in Quantitative LC – MS Proteomics: Human Brain Tissue Sample Analysis._ Journal of Proteome Research, 2013. **12** (5): p. 2128-2137.

311. Rodriguez, J. _et al._ , _Does Trypsin Cut Before Proline?_ Journal of Proteome Research, 2008. **7** (1): p. 300-305.

312. Burkhart, J.M. _et al._ , _Systematic and quantitative comparison of digest efficiency and specificity reveals the impact of trypsin quality on MS-based proteomics._ Journal of Proteomics, 2012. **75** (4): p. 1454-1462.

313. Clemmer, D.E. _et al._ , _Fast and accurate identification of semi-tryptic peptides in shotgun proteomics._ Bioinformatics, 2007. **24** (1): p. 102-109.

314. Lowenthal, M.S. _et al._ , _Quantitative Bottom-Up Proteomics Depends on Digestion Conditions._ Analytical Chemistry, 2014. **86** (1): p. 551-558.

315. Moruz, L. and L. Käll, _Peptide retention time prediction._ Mass Spectrometry Reviews, 2017. **36** (5): p. 615-623.

102

316. Moruz, L. _et al._ , _Chromatographic retention time prediction for posttranslationally modified peptides._ Proteomics, 2012. **12** (8): p. 1151-1159.

317. Cox, J. _et al._ , _Accurate Proteome-wide Label-free Quantification by Delayed Normalization and Maximal Peptide Ratio Extraction, Termed MaxLFQ._ Molecular & Cellular Proteomics, 2014. **13** (9): p. 2513-2526.

318. Lai, X. _et al._ , _A Novel Alignment Method and Multiple Filters for Exclusion of Unqualified Peptides To Enhance Label-Free Quantification Using Peptide Intensity in LC – MS/MS._ Journal of Proteome Research, 2011. **10** (10): p. 4799-4812.

319. Staes, A. _et al._ , _Asn3, a Reliable, Robust, and Universal Lock Mass for Improved Accuracy in LC – MS and LC – MS/MS._ Analytical Chemistry, 2013. **85** (22): p. 1105411060.

320. Holman, S.W., L. McLean, and C.E. Eyers, _RePLiCal: A QconCAT Protein for Retention Time Standardization in Proteomics Studies._ Journal of Proteome Research, 2016. **15** (3): p. 1090-1102.

321. Krokhin, O.V. and V. Spicer, _Predicting Peptide Retention Times for Proteomics._ Current Protocols in Bioinformatics, 2010. **31** (1): p. 13.14.1-13.14.15.

322. Moruz, L., D. Tomazela, and L. Käll, _Training, Selection, and Robust Calibration of Retention Time Models for Targeted Proteomics._ Journal of Proteome Research, 2010. **9** (10): p. 5209-5216.

323. Maboudi Afkham, H. _et al._ , _Uncertainty estimation of predictions of peptides’ chromatographic retention times in shotgun proteomics._ Bioinformatics, 2017. **33** (4): p. 508-513.

324. Mitulovi ć, G. _et al._ , _Preventing Carryover of Peptides and Proteins in Nano LC-MS Separations._ Analytical Chemistry, 2009. **81** (14): p. 5955-5960.

325. Hsieh, E.J. _et al._ , _Effects of Column and Gradient Lengths on Peak Capacity and Peptide Identification in Nanoflow LC-MS/MS of Complex Proteomic Samples._ Journal of The American Society for Mass Spectrometry, 2013. **24** (1): p. 148-153.

326. Young, C., A.V. Podtelejnikov, and M.L. Nielsen, _Improved Reversed Phase Chromatography of Hydrophilic Peptides from Spatial and Temporal Changes in Column Temperature._ Journal of Proteome Research, 2017. **16** (6): p. 2307-2317.

327. Antignac, J.-P. _et al._ , _The ion suppression phenomenon in liquid chromatography – mass spectrometry and its consequences in the field of residue analysis._ Analytica Chimica Acta, 2005. **529** (1): p. 129-136.

328. Lu, W. _et al._ , _Response of peptide intensity to concentration in ESI-MS-based proteome._ Science China Chemistry, 2014. **57** (5): p. 686-694.

329. Nilsson, L.B. and P. Skansen, _Investigation of absolute and relative response for three different liquid chromatography/tandem mass spectrometry systems; the impact of ionization and detection saturation._ Rapid Communications in Mass Spectrometry, 2012. **26** (12): p. 1399-1406.

330. Jarnuczak, A.F. _et al._ , _Analysis of Intrinsic Peptide Detectability via Integrated LabelFree and SRM-Based Absolute Quantitative Proteomics._ Journal of Proteome Research, 2016. **15** (9): p. 2945-2959.

331. Liu, H. _et al._ , _The Prediction of Peptide Charge States for Electrospray Ionization in Mass Spectrometry._ Procedia Environmental Sciences, 2011. **8** : p. 483-491.

332. Morand, K., G. Talbo, and M. Mann, _Oxidation of peptides during electrospray ionization._ Rapid Communications in Mass Spectrometry, 1993. **7** (8): p. 738-743.

333. Godugu, B. _et al._ , _Effect of N-Terminal Glutamic Acid and Glutamine on Fragmentation of Peptide Ions._ Journal of the American Society for Mass Spectrometry, 2010. **21** (7): p. 1169-1176.

334. Gorshkov, V., T. Verano-Braga, and F. Kjeldsen, _SuperQuant: A Data Processing Approach to Increase Quantitative Proteome Coverage._ Analytical Chemistry, 2015. **87** (12): p. 6319-6327.

335. Plubell, D.L. _et al._ , _Extended Multiplexing of Tandem Mass Tags (TMT) Labeling Reveals Age and High Fat Diet Specific Proteome Changes in Mouse Epididymal Adipose Tissue._ Molecular & Cellular Proteomics, 2017. **16** (5): p. 873-890.

103

336. Wang, H., S. Alvarez, and L.M. Hicks, _Comprehensive Comparison of iTRAQ and Label-free LC-Based Quantitative Proteomics Approaches Using Two Chlamydomonas reinhardtii Strains of Interest for Biofuels Engineering._ Journal of Proteome Research, 2012. **11** (1): p. 487-501.

337. Boschetti, E. _et al._ , _Romancing the “hidden proteome”, Anno Domini two zero zero seven._ Journal of Chromatography A, 2007. **1153** (1): p. 277-290.

338. Rabilloud, T., _Membrane proteins and proteomics: Love is possible, but so difficult._ ELECTROPHORESIS, 2009. **30** (S1): p. S174-S180.

339. Perdigão, N. _et al._ , _Unexpected features of the dark proteome._ Proceedings of the National Academy of Sciences of the United States of America, 2015. **112** (52): p. 15898-15903.

340. Perdigão, N., A.C. Rosa, and S.I. O'Donoghue, _The Dark Proteome Database._ BioData Mining, 2017. **10** : p. 24-24.

341. Doerr, A., _Mass spectrometry – based targeted proteomics._ Nature Methods, 2012. **10** : p. 23.

342. Lange, V. _et al._ , _Selected reaction monitoring for quantitative proteomics: a tutorial._ Molecular Systems Biology, 2008. **4** : p. 222-222.

343. de Graaf, E.L. _et al._ , _Improving SRM Assay Development: A Global Comparison between Triple Quadrupole, Ion Trap, and Higher Energy CID Peptide Fragmentation Spectra._ Journal of Proteome Research, 2011. **10** (9): p. 4334-4341.

344. Peterson, A.C. _et al._ , _Parallel reaction monitoring for high resolution and high mass accuracy quantitative, targeted proteomics._ Molecular & Cellular Proteomics, 2012. **11** (11): p. 1475-1488.

345. Ronsein, G.E. _et al._ , _Parallel reaction monitoring (PRM) and selected reaction monitoring (SRM) exhibit comparable linearity, dynamic range and precision for targeted quantitative HDL proteomics._ Journal of Proteomics, 2015. **113** : p. 388-399.

346. Purvine, S. _et al._ , _Shotgun collision-induced dissociation of peptides using a time of flight mass analyzer._ Proteomics, 2003. **3** (6): p. 847-850.

347. Plumb, R.S. _et al._ , _UPLC/MSE; a new approach for generating molecular fragment information for biomarker structure elucidation._ Rapid Communications in Mass Spectrometry, 2006. **20** (13): p. 1989-1994.

348. Venable, J.D. _et al._ , _Automated approach for quantitative analysis of complex peptide mixtures from tandem mass spectra._ Nature Methods, 2004. **1** (1): p. 39-45.

349. Panchaud, A. _et al._ , _Faster, quantitative, and accurate precursor acquisition independent from ion count._ Analytical Chemistry, 2011. **83** (6): p. 2250-2257.

350. Bern, M. _et al._ , _Deconvolution of mixture spectra from ion-trap data-independentacquisition tandem mass spectrometry._ Analytical Chemistry, 2010. **82** (3): p. 833-841.

351. Gillet, L.C. _et al._ , _Targeted Data Extraction of the MS/MS Spectra Generated by Dataindependent Acquisition: A New Concept for Consistent and Accurate Proteome Analysis._ Molecular & Cellular Proteomics, 2012. **11** (6).

352. Vowinckel, J. _et al._ , _The beauty of being (label)-free: sample preparation methods for SWATH-MS and next-generation targeted proteomics._ F1000Research, 2014. **2** : p. 272-272.

353. Röst, H.L. _et al._ , _OpenSWATH enables automated, targeted analysis of dataindependent acquisition MS data._ Nature Biotechnology, 2014. **32** : p. 219.

354. Kelstrup, C.D. _et al._ , _Performance Evaluation of the Q Exactive HF-X for Shotgun Proteomics._ Journal of Proteome Research, 2018. **17** (1): p. 727-738.

355. Bruderer, R. _et al._ , _Extending the Limits of Quantitative Proteome Profiling with DataIndependent Acquisition and Application to Acetaminophen-Treated ThreeDimensional Liver Microtissues._ Molecular & Cellular Proteomics, 2015. **14** (5): p. 14001410.

356. Collins, B.C. _et al._ , _Multi-laboratory assessment of reproducibility, qualitative and quantitative performance of SWATH-mass spectrometry._ Nature Communications, 2017. **8** (1): p. 291.

104

|357.<br>358.|Liu, Y._et al._,_Quantitative measurements of N-linked glycoproteins in human plasma_<br>_by SWATH-MS._Proteomics, 2013.**13**(8): p. 1247-1256.<br>Schmidlin, T._et al._,_Assessment of SRM, MRM3, and DIA for the targeted analysis of_<br>_phosphorylation dynamics in non-small cell lung cancer._Proteomics, 2016.**16**(15-16):<br>p. 2193-2205.|
|---|---|
|359.|Ludwig, C._et al._,_Data_‐_independent acquisition_‐_based SWATH_‐_MS for quantitative_<br>_proteomics: a tutorial._Molecular Systems Biology, 2018.**14**(8): p. e8126.|
|360.|Keller, A._et al._,_Empirical Statistical Model To Estimate the Accuracy of Peptide_<br>_Identifications Made by MS/MS and Database Search._Analytical Chemistry, 2002.<br>**74**(20): p. 5383-5392.|
|361.|<br>Eng, J.K., A.L. McCormack, and J.R. Yates,_An approach to correlate tandem mass_<br>_spectral data of peptides with amino acid sequences in a protein database._Journal of<br>The American Society for Mass Spectrometry, 1994.**5**(11): p. 976-89.|
|362.|<br>Huala, E._et al._,_The Arabidopsis Information Resource (TAIR): a comprehensive_<br>_database and web-based information retrieval, analysis, and visualization system for a_<br>_model plant._Nucleic Acids Research, 2001.**29**(1): p. 102-105.|
|363.|<br>Frank, A.M.,_A ranking-based scoring function for peptide-spectrum matches._Journal<br>of Proteome Research, 2009.**8**(5): p. 2241-2252.|
|364.|<br>Shortreed, M.R._et al._,_Global Identification of Protein Post-translational Modifications_<br>_in a Single-Pass Database Search._Journal of Proteome Research, 2015.**14**(11): p.<br>4714-4720.|
|365.|David, M._et al._,_SpecOMS: A Full Open Modification Search Method Performing All-to-_<br>_All Spectra Comparisons within Minutes._Journal of Proteome Research, 2017.**16**(8):<br>p. 3030-3038.|
|366.|<br>Craig, R. and R.C. Beavis,_A method for reducing the time required to match protein_<br>_sequences with tandem mass spectra._Rapid Communications in Mass Spectrometry,<br>2003.**17**(20): p. 2310-2316.|
|367.|<br>Bogdanow, B., H. Zauber, and M. Selbach,_Systematic Errors in Peptide and Protein_<br>_Identification and Quantification by Modified Peptides._Molecular & cellular proteomics,<br>2016.**15**(8): p. 2791-2801.|
|368.|<br>Perkins, D.N._et al._,_Probability-based protein identification by searching sequence_<br>_databases using mass spectrometry data._Electrophoresis 1999.**20**(18): p. 3551-67.|
|369.|, <br>Elias, J.E. and S.P. Gygi,_Target-decoy search strategy for increased confidence in_<br>_large-scale protein identifications by mass spectrometry._Nature Methods, 2007.**4**: p.<br>207.|
|370.|Käll, L._et al._,_Assigning Significance to Peptides Identified by Tandem Mass_<br>_Spectrometry Using Decoy Databases._Journal of Proteome Research, 2008.**7**(1): p.<br>29-34.|
|371.|<br>Jeong, K., S. Kim, and N. Bandeira,_False discovery rates in spectral identification._<br>BMC Bioinformatics, 2012.**13 Suppl 16**(Suppl 16): p. S2-S2.|
|372.|<br>Diament, B.J. and W.S. Noble,_Faster SEQUEST Searching for Peptide Identification_<br>_from Tandem Mass Spectra._Journal of Proteome Research, 2011.**10**(9): p. 3871-<br>3879.|
|373.|Fenyö, D. and R.C. Beavis,_A Method for Assessing the Statistical Significance of Mass_<br>_Spectrometry-Based Protein Identifications Using General Scoring Schemes._<br>Analytical Chemistry 2003**75**(4): p 768-774|
|374.|, .. .<br>Kim, S. and P.A. Pevzner,_MS-GF+ makes progress towards a universal database_<br>_search tool for proteomics._Nature Communications, 2014.**5**: p. 5277.|
|375.|<br>Dorfer, V._et al._,_MS Amanda, a Universal Identification Algorithm Optimized for High_<br>_Accuracy Tandem Mass Spectra._Journal of Proteome Research, 2014.**13**(8): p. 3679-<br>3684.|
|376.|Tabb, D.L., C.G. Fernando, and M.C. Chambers,_MyriMatch:  Highly Accurate Tandem_<br>_Mass Spectral Peptide Identification by Multivariate Hypergeometric Analysis._Journal<br>of Proteome Research, 2007.**6**(2): p. 654-661.|


105

377. Eng, J.K., T.A. Jahan, and M.R. Hoopmann, _Comet: An open-source MS/MS sequence database search tool._ Proteomics, 2013. **13** (1): p. 22-24.

378. Cox, J. _et al._ , _Andromeda: A Peptide Search Engine Integrated into the MaxQuant Environment._ Journal of Proteome Research, 2011. **10** (4): p. 1794-1805.

379. Geer, L.Y. _et al._ , _Open Mass Spectrometry Search Algorithm._ Journal of Proteome Research, 2004. **3** (5): p. 958-964.

380. Ma, B., _Novor: Real-Time Peptide de Novo Sequencing Software._ Journal of The American Society for Mass Spectrometry, 2015. **26** (11): p. 1885-1894.

381. Tabb, D.L. _et al._ , _DirecTag: Accurate Sequence Tags from Peptide MS/MS through Statistical Scoring._ Journal of Proteome Research, 2008. **7** (9): p. 3838-3846.

382. Vaudel, M. _et al._ , _SearchGUI: An open-source graphical user interface for simultaneous OMSSA and X!Tandem searches._ Proteomics, 2011. **11** (5): p. 996-999.

383. Vaudel, M. _et al._ , _PeptideShaker enables reanalysis of MS-derived proteomics data sets._ Nature Biotechnology, 2015. **33** (1): p. 22-24.

384. Cox, J. and M. Mann, _MaxQuant enables high peptide identification rates, individualized p.p.b.-range mass accuracies and proteome-wide protein quantification._ Nature Biotechnology, 2008. **26** (12): p. 1367-1372.

385. Nesvizhskii, A.I. and R. Aebersold, _Interpretation of Shotgun Proteomic Data._ The Protein Inference Problem, 2005. **4** (10): p. 1419-1440.

386. Nesvizhskii, A.I. _et al._ , _A Statistical Model for Identifying Proteins by Tandem Mass Spectrometry._ Analytical Chemistry, 2003. **75** (17): p. 4646-4658.

387. Shen, C. _et al._ , _A hierarchical statistical model to assess the confidence of peptides and proteins inferred from tandem mass spectrometry._ Bioinformatics, 2008. **24** (2): p. 202-208.

388. Gerster, S. _et al._ , _Protein and gene model inference based on statistical modeling in k- partite graphs._ Proceedings of the National Academy of Sciences, 2010. **107** (27): p. 12101-12106.

389. Higdon, R. and E. Kolker, _A predictive model for identifying proteins by a single peptide match._ Bioinformatics, 2007. **23** (3): p. 277-280.

390. Gupta, N. and P.A. Pevzner, _False Discovery Rates of Protein Identifications: A Strike against the Two-Peptide Rule._ Journal of Proteome Research, 2009. **8** (9): p. 41734181.

391. Reiter, L. _et al._ , _Protein Identification False Discovery Rates for Very Large Proteomics Data Sets Generated by Tandem Mass Spectrometry._ Molecular & Cellular Proteomics, 2009. **8** (11): p. 2405-2417.

392. Granholm, V. _et al._ , _Determining the calibration of confidence estimation procedures for unique peptides in shotgun proteomics._ Journal of Proteomics, 2013. **80** : p. 123131.

393. Adamski, M. _et al._ , _Data management and preliminary data analysis in the pilot phase of the HUPO Plasma Proteome Project._ Proteomics, 2005. **5** (13): p. 3246-3261.

394. Li, Y.F. _et al._ , _A bayesian approach to protein inference problem in shotgun proteomics._ Journal of computational biology, 2009. **16** (8): p. 1183-1193.

395. Serang, O., M.J. MacCoss, and W.S. Noble, _Efficient marginalization to compute protein posterior probabilities from shotgun mass spectrometry data._ Journal of Proteome Research, 2010. **9** (10): p. 5346-5357.

396. Savitski, M.M. _et al._ , _A Scalable Approach for Protein False Discovery Rate Estimation in Large Proteomic Data Sets._ Molecular & cellular proteomics, 2015. **14** (9): p. 23942404.

397. The, M., A. Tasnim, and L. Käll, _How to talk about protein-level false discovery rates in shotgun proteomics._ Proteomics, 2016. **16** (18): p. 2461-2469.

398. Huang, T. _et al._ , _Protein inference: a review._ Briefings in Bioinformatics, 2012. **13** (5): p. 586-614.

399. Serang, O. and W. Noble, _A review of statistical methods for protein identification using tandem mass spectrometry._ Statistics and Its Interface, 2012. **5** (1): p. 3-20.

106

400. Tsou, C.-C. _et al._ , _IDEAL-Q, an automated tool for label-free quantitation analysis using an efficient peptide alignment approach and spectral data validation._ Molecular & Cellular Proteomics, 2010. **9** (1): p. 131-144.

401. Valot, B. _et al._ , _MassChroQ: A versatile tool for mass spectrometry quantification._ Proteomics, 2011. **11** (17): p. 3572-3577.

402. Krey, J.F. _et al._ , _Accurate Label-Free Protein Quantitation with High- and LowResolution Mass Spectrometers._ Journal of Proteome Research, 2014. **13** (2): p. 10341044.

403. Tyanova, S. _et al._ , _Visualization of LC-MS/MS proteomics data in MaxQuant._ Proteomics, 2015. **15** (8): p. 1453-1456.

404. Sinitcyn, P. _et al._ , _MaxQuant goes Linux._ Nature Methods, 2018. **15** (6): p. 401-401. 405. Argentini, A. _et al._ , _moFF: a robust and automated approach to extract peptide ion intensities._ Nature Methods, 2016. **13** (12): p. 964-966.

406. Argentini, A. _et al. Using moFF to Extract Peptide Ion Intensities from LC-MS experiments_ . Protocol Exchange, 2016.  DOI: doi:10.1038/protex.2016.085.

407. Sandin, M. _et al._ , _Data processing methods and quality control strategies for label-free LC – MS protein quantification._ Biochimica et Biophysica Acta (BBA) - Proteins and Proteomics, 2014. **1844** (1, Part A): p. 29-41.

408. Schliekelman, P. and S. Liu, _Quantifying the Effect of Competition for Detection between Coeluting Peptides on Detection Probabilities in Mass-Spectrometry-Based Proteomics._ Journal of Proteome Research, 2013. **13** (2): p. 348-361.

409. Choi, M. _et al._ , _MSstats: an R package for statistical analysis of quantitative mass spectrometry-based proteomic experiments._ Bioinformatics, 2014. **30** (17): p. 25242526.

410. Arsova, B., H. Zauber, and W.X. Schulze, _Precision, Proteome Coverage, and Dynamic Range of Arabidopsis Proteome Profiling Using 15N Metabolic Labeling and Label-free Approaches._ Molecular & Cellular Proteomics, 2012. **11** (9): p. 619-628.

411. Brazma, A. _et al._ , _The PRIDE database and related tools and resources in 2019: improving support for quantification data._ Nucleic Acids Research, 2018. **47** (D1): p. D442-D450.

412. Sandberg, A. _et al._ , _Quantitative accuracy in mass spectrometry based proteomics of complex samples: The impact of labeling and precursor interference._ Journal of Proteomics, 2014. **96** : p. 133-144.

413. Michalski, A., J. Cox, and M. Mann, _More than 100,000 Detectable Peptide Species Elute in Single Shotgun Proteomics Runs but the Majority is Inaccessible to DataDependent LC−MS/MS._ Journal of Proteome Research, 2011. **10** (4): p. 1785-1793.

414. Griss, J. _et al._ , _Recognizing millions of consistently unidentified spectra across hundreds of shotgun proteomics datasets._ Nature Methods, 2016. **13** : p. 651.

415. Leitner, A., A. Foettinger, and W. Lindner, _Improving fragmentation of poorly fragmenting peptides and phosphopeptides during collision-induced dissociation by malondialdehyde modification of arginine residues._ Journal of Mass Spectrometry, 2007. **42** (7): p. 950-9.

416. Chick, J.M. _et al._ , _A mass-tolerant database search identifies a large proportion of unassigned spectra in shotgun proteomics as modified peptides._ Nature Biotechnology, 2015. **33** (7): p. 743-749.

417. Prakash, A. _et al._ , _Signal Maps for Mass Spectrometry-based Comparative Proteomics._ Molecular & Cellular Proteomics, 2006. **5** (3): p. 423-432.

418. Mueller, L.N. _et al._ , _SuperHirn – a novel tool for high resolution LC-MS-based peptide/protein profiling._ Proteomics, 2007. **7** (19): p. 3470-3480.

419. Bielow, C., G. Mastrobuoni, and S. Kempa, _Proteomics Quality Control: Quality Control Software for MaxQuant Results._ Journal of Proteome Research, 2016. **15** (3): p. 777787.

420. Beer, L.A. _et al._ , _Efficient Quantitative Comparisons of Plasma Proteomes Using LabelFree Analysis with MaxQuant._ Methods in molecular biology (Clifton, N.J.), 2017. **1619** : p. 339-352.

107

421. Milac, T.I., T.W. Randolph, and P. Wang, _Analyzing LC-MS/MS data by spectral count and ion abundance: two case studies._ Statistics and Its Interface, 2012. **5** (1): p. 75-87.

422. Goeminne, L.J.E. _et al._ , _Summarization vs Peptide-Based Models in Label-Free Quantitative Proteomics: Performance, Pitfalls, and Data Analysis Guidelines._ Journal of Proteome Research, 2015. **14** (6): p. 2457-2465.

423. Ramus, C. _et al. Spiked proteomic standard dataset for testing label-free quantitative software and statistical methods_ . Data in Brief, 2016. **6** , 286-294 DOI: 10.1016/j.dib.2015.11.063.

424. Karpievitch, Y.V., A.R. Dabney, and R.D. Smith, _Normalization and missing value imputation for label-free LC-MS analysis._ BMC Bioinformatics, 2012. **13 Suppl 16** : p. S5.

425. Karpievitch, Y. _et al._ , _A statistical framework for protein quantitation in bottom-up MSbased proteomics._ Bioinformatics, 2009. **25** (16): p. 2028-2034.

426. Paulovich, A.G. _et al._ , _Interlaboratory Study Characterizing a Yeast Performance Standard for Benchmarking LC-MS Platform Performance._ Molecular & Cellular Proteomics, 2010. **9** (2): p. 242-254.

427. Bourgon, R., R. Gentleman, and W. Huber, _Independent filtering increases detection power for high-throughput experiments._ Proceedings of the National Academy of Sciences, 2010. **107** (21): p. 9546-9551.

428. Lai, X. _et al._ , _A novel alignment method and multiple filters for exclusion of unqualified peptides to enhance label-free quantification using peptide intensity in LC-MS/MS._ Journal of Proteome Research, 2011. **10** (10): p. 4799-4812.

429. Gentleman, R. _et al._ , _genefilter: genefilter: methods for filtering genes from highthroughput experiments_ . 2018, Bioconductor/R package.

430. Belouah, I. _et al._ , _Peptide filtering differently affects the performances of XIC-based quantification methods._ Journal of Proteomics, 2019. **193** : p. 131-141.

431. Yang, Y.H. _et al._ , _Normalization for cDNA microarray data: a robust composite method addressing single and multiple slide systematic variation._ Nucleic Acids Research, 2002. **30** (4): p. e15.

432. Amaratunga, D. and J. Cabrera, _Analysis of Data From Viral DNA Microchips._ Journal of the American Statistical Association, 2001. **96** (456): p. 1161-1170.

433. Bolstad, B.M. _et al._ , _A comparison of normalization methods for high density oligonucleotide array data based on variance and bias._ Bioinformatics, 2003. **19** (2): p. 185-193.

434. Park, T. _et al._ , _Evaluation of normalization methods for microarray data._ BMC Bioinformatics, 2003. **4** : p. 33.

435. Valikangas, T., T. Suomi, and L.L. Elo, _A systematic evaluation of normalization methods in quantitative label-free proteomics._ Briefings in Bioinformatics, 2016.

436. Huber, W. _et al._ , _Variance stabilization applied to microarray data calibration and to the quantification of differential expression._ Bioinformatics, 2002. **18 Suppl 1** : p. S96-104.

437. Callister, S.J. _et al._ , _Normalization Approaches for Removing Systematic Biases Associated with Mass Spectrometry and Label-Free Proteomics._ Journal of Proteome Research, 2006. **5** (2): p. 277-286.

438. Kultima, K. _et al._ , _Development and Evaluation of Normalization Methods for Label-free Relative Quantification of Endogenous Peptides._ Molecular & Cellular Proteomics, 2009. **8** (10): p. 2285-2295.

439. Webb-Robertson, B.-J.M. _et al._ , _A statistical selection strategy for normalization procedures in LC-MS proteomics experiments through dataset-dependent ranking of normalization scaling factors._ Proteomics, 2011. **11** (24): p. 4736-4741.

440. Little, R.J.A. and D.B. Rubin, _Statistical Analysis with Missing Data, 2nd Edition_ . Wiley Series in Probability and Statistics. 2002: Wiley.

441. Beretta, L. and A. Santaniello, _Nearest neighbor imputation algorithms: a critical evaluation._ BMC Medical Informatics and Decision Making, 2016. **16** (3): p. 74.

442. Troyanskaya, O. _et al._ , _Missing value estimation methods for DNA microarrays._ Bioinformatics, 2001. **17** (6): p. 520-525.

108

443. Lazar, C., _QRILC: a quantile regression approach for the imputation of left-censored missing data in quantitative proteomics._ to be submitted.

444. Gatto, L. and K.S. Lilley, _MSnbase-an R/Bioconductor package for isobaric tagged mass spectrometry data visualization, processing and quantitation._ Bioinformatics, 2012. **28** (2): p. 288-289.

445. Tyanova, S. _et al._ , _The Perseus computational platform for comprehensive analysis of (prote)omics data._ Nature Methods, 2016. **13** : p. 731.

446. Choi, M., _A flexible and versatile framework for statistical design and analysis of quantitative mass spectrometry-based proteomic experiments_ . 2016, Purdue University: Open Access Dissertations.

447. Lazar, C. _et al._ , _Accounting for the Multiple Natures of Missing Values in Label-Free Quantitative Proteomics Data Sets to Compare Imputation Strategies._ Journal of Proteome Research, 2016. **15** (4): p. 1116-1125.

448. Webb-Robertson, B.-J.M. _et al._ , _Review, Evaluation, and Discussion of the Challenges of Missing Value Imputation for Mass Spectrometry-Based Label-Free Global Proteomics._ Journal of Proteome Research, 2015. **14** (5): p. 1993-2001.

449. Välikangas, T., T. Suomi, and L.L. Elo, _A comprehensive evaluation of popular proteomics software workflows for label-free proteome quantification and imputation._ Briefings in Bioinformatics, 2017: p. bbx054-bbx054.

450. Zhang, X. _et al._ , _Proteome-wide identification of ubiquitin interactions using UbIA-MS._ Nature Protocols, 2018. **13** : p. 530.

451. Xiaoyan, Y. _et al._ , _Multiple imputation and analysis for high_ ‐ _dimensional incomplete proteomics data._ Statistics in Medicine, 2016. **35** (8): p. 1315-1326.

452. Wang, J. _et al._ , _In-depth method assessments of differentially expressed protein detection for shotgun proteomics data with missing values._ Scientific Reports, 2017. **7** (1): p. 3367.

453. Wu, Z. _et al._ , _Quantitative Chemical Proteomics Reveals New Potential Drug Targets in Head and Neck Cancer._ Molecular & Cellular Proteomics, 2011. **10** (12).

454. Breitwieser, F.P. _et al._ , _General Statistical Modeling of Data from Protein Relative Expression Isobaric Tags._ Journal of Proteome Research, 2011. **10** (6): p. 2758-2766.

455. Lin, W.-T. _et al._ , _Multi- Q:  A Fully Automated Tool for Multiplexed Protein Quantitation._ Journal of Proteome Research, 2006. **5** (9): p. 2328-2338.

456. Raj, D.A.A. _et al._ , _A multiplex quantitative proteomics strategy for protein biomarker studies in urinary exosomes._ Kidney Int, 2012. **81** (12): p. 1263-1272.

457. Mosteller, F. and J.W. Tukey, _Data Analysis and Regression: A Second Course in Statistics_ . 1977: Addison-Wesley Publishing Company.

458. Hoaglin, D.C., F. Mosteller, and J.W. Tukey, _Understanding robust and exploratory data analysis_ . 1983: Wiley.

459. Gygi, S.P. _et al._ , _Quantitative analysis of complex protein mixtures using isotope-coded affinity tags._ Nature Biotechnology, 1999. **17** (10): p. 994-999.

460. Najm, F.J. _et al._ , _Drug-based modulation of endogenous stem cells promotes functional remyelination in vivo._ Nature, 2015. **522** : p. 216.

461. Mertins, P. _et al._ , _Investigation of Protein-tyrosine Phosphatase 1B Function by Quantitative Proteomics._ Molecular & Cellular Proteomics, 2008. **7** (9): p. 1763-1777.

462. Margolin, A.A. _et al._ , _Empirical Bayes Analysis of Quantitative Proteomics Experiments._ PLoS ONE, 2009. **4** (10): p. e7454.

463. Al Shweiki, M.H.D.R. _et al._ , _Assessment of Label-Free Quantification in Discovery Proteomics and Impact of Technological Factors and Natural Variability of Protein Abundance._ Journal of Proteome Research, 2017. **16** (4): p. 1410-1424.

464. Blainey, P., M. Krzywinski, and N. Altman, _Points of Significance: Replication._ Nature Methods, 2014. **11** (9): p. 879-880.

465. Oberg, A.L. and O. Vitek, _Statistical Design of Quantitative Mass Spectrometry-Based Proteomic Experiments._ Journal of Proteome Research, 2009. **8** (5): p. 2144-2156.

109

466. Tusher, V.G., R. Tibshirani, and G. Chu, _Significance analysis of microarrays applied to the ionizing radiation response._ Proceedings of the National Academy of Sciences of the United States of America, 2001. **98** (9): p. 5116-5121.

467. Giai Gianetto, Q. _et al._ , _Uses and misuses of the fudge factor in quantitative discovery proteomics._ Proteomics, 2016. **16** (14): p. 1955-1960.

468. Smyth, G.K., _Linear models and empirical bayes methods for assessing differential expression in microarray experiments._ Stat Appl Genet Mol Biol, 2004. **3** : p. Article3.

469. Ting, L. _et al._ , _Normalization and Statistical Analysis of Quantitative Proteomics Data Generated by Metabolic Labeling._ Molecular & Cellular Proteomics, 2009. **8** (10): p. 2227-2242.

470. Daly, D.S. _et al._ , _Mixed- Effects Statistical Model for Comparative LC−MS Proteomics Studies._ Journal of Proteome Research, 2008. **7** (3): p. 1209-1217.

471. Clough, T. _et al._ , _Protein Quantification in Label-Free LC-MS Experiments._ Journal of Proteome Research, 2009. **8** (11): p. 5275-5284.

472. Clough, T. _et al._ , _Statistical protein quantification and significance analysis in label-free LC-MS experiments with complex designs._ BMC Bioinformatics, 2012. **13** (16): p. S6.

473. Bukhman, Y.V. _et al._ , _Design and analysis of quantitative differential proteomics investigations using LC-MS technology._ Journal of Bioinformatics and Computational Biology, 2008. **6** (1): p. 107-23.

474. Henao, R. _et al. Hierarchical factor modeling of proteomics data_ . in _Computational Advances in Bio and Medical Sciences (ICCABS), 2012 IEEE 2nd International Conference on_ . 2012.

475. Blein-Nicolas, M. _et al._ , _Including shared peptides for estimating protein abundances: A significant improvement for quantitative proteomics._ Proteomics, 2012. **12** (18): p. 2797-2801.

476. Koopmans, F. _et al._ , _Empirical Bayesian Random Censoring Threshold Model Improves Detection of Differentially Abundant Proteins._ Journal of Proteome Research, 2014.

477. Hastie, T., R. Tibshirani, and J. Friedman, _The Elements of Statistical Learning - Data Mining, Inference, and Prediction_ . Springer Series in Statistics. 2009, New York: Springer.

478. Stein, C. _Inadmissibility of the Usual Estimator for the Mean of a Multivariate Normal Distribution_ . in _Proceedings of the Third Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Contributions to the Theory of Statistics_ . 1956. Berkeley, Calif.: University of California Press.

479. Golub, G.H., M. Heath, and G. Wahba, _Generalized Cross-Validation as a Method for Choosing a Good Ridge Parameter._ Technometrics, 1979. **21** (2): p. 215-223.

480. Azevedo, C.F. _et al._ , _Ridge, Lasso and Bayesian additive-dominance genomic models._ BMC Genetics, 2015. **16** (1): p. 105.

481. Tissier, R., J. Houwing-Duistermaat, and M. Rodríguez-Girondo, _Improving stability of prediction models based on correlated omics data by using network approaches._ PloS one, 2018. **13** (2): p. e0192853-e0192853.

482. Bolstad, B.M., _Low-level Analysis of High-density Oligonucleotide Array Data: Background, Normalization and Summarization_ . 2004, University of California, Berkeley.

483. Liu, H., R.G. Sadygov, and J.R. Yates, _A Model for Random Sampling and Estimation of Relative Protein Abundance in Shotgun Proteomics._ Analytical Chemistry, 2004. **76** (14): p. 4193-4201.

484. Colinge, J. _et al._ , _Differential Proteomics via Probabilistic Peptide Identification Scores._ Analytical Chemistry, 2005. **77** (2): p. 596-606.

485. Li, M. _et al._ , _Comparative shotgun proteomics using spectral count data and quasilikelihood modeling._ Journal of Proteome Research, 2010. **9** (8): p. 4295-4305.

486. Robinson, M.D., D.J. McCarthy, and G.K. Smyth, _edgeR: a Bioconductor package for differential expression analysis of digital gene expression data._ Bioinformatics, 2010. **26** (1): p. 139-140.

110

487. McCarthy, D.J., Y. Chen, and G.K. Smyth, _Differential expression analysis of multifactor RNA-Seq experiments with respect to biological variation._ Nucleic Acids Research, 2012. **40** (10): p. 4288-4297.

488. Love, M.I., W. Huber, and S. Anders, _Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2._ Genome Biology, 2014. **15** (12): p. 550.

489. Branson, O.E. and M.A. Freitas, _Tag-Count Analysis of Large-Scale Proteomic Data._ Journal of Proteome Research, 2016. **15** (12): p. 4742-4746.

490. Choi, H., D. Fermin, and A.I. Nesvizhskii, _Significance analysis of spectral count data in label-free shotgun proteomics._ Molecular & Cellular Proteomics, 2008. **7** (12): p. 2373-2385.

491. Pham, T.V. _et al._ , _On the beta-binomial model for analysis of spectral count data in label-free tandem mass spectrometry-based proteomics._ Bioinformatics, 2010. **26** (3): p. 363-369.

492. Richardson, K. _et al._ , _A Probabilistic Framework for Peptide and Protein Quantification from Data-Dependent and Data-Independent LC-MS Proteomics Experiments._ OMICS: A Journal of Integrative Biology, 2012. **16** (9): p. 468-482.

493. Zhang, B. _et al._ , _Detecting Differential and Correlated Protein Expression in Label-Free Shotgun Proteomics._ Journal of Proteome Research, 2006. **5** (11): p. 2909-2918.

494. Lundgren, D.H. _et al._ , _Role of spectral counting in quantitative proteomics._ Expert Review of Proteomics, 2010. **7** (1): p. 39-53.

495. Lu, P. _et al._ , _Absolute protein expression profiling estimates the relative contributions of transcriptional and translational regulation._ Nature Biotechnology, 2007. **25** (1): p. 117-124.

496. Liu, K. _et al._ , _Relationship between Sample Loading Amount and Peptide Identification and Its Effects on Quantitative Proteomics._ Analytical Chemistry, 2009. **81** (4): p. 13071314.

497. Schulze, W.X. and B. Usadel, _Quantitation in Mass-Spectrometry-Based Proteomics._ Annual Review of Plant Biology, 2010. **61** (1): p. 491-516.

498. Old, W.M. _et al._ , _Comparison of Label-free Methods for Quantifying Human Proteins by Shotgun Proteomics._ Molecular & Cellular Proteomics, 2005. **4** (10): p. 1487-1502.

499. Dunn, O.J., _Multiple Comparisons Among Means._ Journal of the American Statistical Association, 1961. **56** (293): p. 52-64.

500. Burger, T., _Gentle Introduction to the Statistical Foundations of False Discovery Rate in Quantitative Proteomics._ Journal of Proteome Research, 2018. **17** (1): p. 12-22.

501. Benjamini, Y. and Y. Hochberg, _Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing._ Journal of the Royal Statistical Society. Series B (Methodological), 1995. **57** (1): p. 289-300.

502. Hart, J.R. _et al._ , _The butterfly effect in cancer: a single base mutation can remodel the cell._ Proceedings of the National Academy of Sciences of the United States of America, 2015. **112** (4): p. 1131-1136.

503. Meissner, F. and M. Mann, _Quantitative shotgun proteomics: considerations for a highquality workflow in immunology._ Nature Immunology, 2014. **15** (2): p. 112-117.

504. Doll, S. _et al._ , _Region and cell-type resolved quantitative proteomic map of the human heart._ Nature Communications, 2017. **8** (1): p. 1469.

505. Smith, R. _et al._ , _Proteomics, lipidomics, metabolomics: a mass spectrometry tutorial from a computer scientist's point of view._ BMC Bioinformatics, 2014. **15** (7): p. 1-14.

111

112

---

[← STATISTICAL METHODS FOR DIFFERENTIAL PROTEOMICS AT PEPTIDE AND PROTEIN LEVEL](01-statistical-methods-for-differential-proteomics-at-peptide-a.md) · [Up: contents](index.md) · [PART II: RESEARCH PAPERS →](03-part-ii-research-papers.md)
