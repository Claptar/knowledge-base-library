---
title: Introduction
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/martens_proteomics_bioinformatics.pdf
source_file: sources/statomics-sga21/docs/martens_proteomics_bioinformatics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`docs/martens_proteomics_bioinformatics.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/martens_proteomics_bioinformatics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
MS-BASED PROTEOMICS<br>DATA ANALYSIS<br>lennart martens<br>lennart.martens@vib-ugent.be<br>@compomics<br>computational omics and systems biology group<br>Ghent University and VIB, Ghent, Belgium<br><!-- End of picture text -->


<!-- Start of picture text -->
Proteomics in the central paradigm of biology<br><!-- End of picture text -->


<!-- Start of picture text -->
- Primary structure ( sequence )<br>…YSFVATAER…<br>- Secondary structure ( structural elements )<br>- Tertiairy structure ( 3D shape )<br>- Modifications ( dynamic, function )<br>phosphorylation<br>- Processing ( targetting ,  activation )<br>trypsin<br>platelet activity<br>Adapted from the NCBI Science Primer<br>http://www.ncbi.nih.gov/About/primer/genetics_cell.html<br><!-- End of picture text -->

1

**Amino acids, peptides, and proteins Mass spectrometry basics MS/MS spectra and identification Database search algorithms in three phases Sequencial search algorithms Decoys and false discovery rate calculation Protein inference: bad, ugly, and not so good**


**Amino acids, peptides, and proteins Mass spectrometry basics MS/MS spectra and identification Database search algorithms in three phases Sequencial search algorithms Decoys and false discovery rate calculation Protein inference: bad, ugly, and not so good**


2


<!-- Start of picture text -->
Amino acids vary considerably<br>in their physico-chemical properties<br><!-- End of picture text -->


http://courses.cm.utexas.edu/jrobertus/ch339k/overheads-1/ch5-amino-acids.jpg


<!-- Start of picture text -->
Protein backbones are formed through<br>amide (or peptide) bonds between residues<br><!-- End of picture text -->


<!-- Start of picture text -->
side chain R1 R2 H O H R1 H O<br>H N C C O + H N C C O H N C C N C C O H<br>H O R2<br>O<br>H O H H<br>H<br>peptide bond<br>amino group carboxyl group<br>R1 H O R3 H O R5 H O R7<br>N N N O<br>H2N N N N<br>O R2 H O R4 H O R6 H OH<br>amino<br>terminus carboxyl<br>residue terminus<br><!-- End of picture text -->


3

**Amino acids, peptides, and proteins Mass spectrometry basics**

**MS/MS spectra and identification**

**Database search algorithms in three phases**

**Sequencial search algorithms**

**Decoys and false discovery rate calculation**

**Protein inference: bad, ugly, and not so good**


A generalized mass spectrometer consists of three main parts, along with a digitizer


<!-- Start of picture text -->
sample ion source mass analyzer(s) detector digitizer<br><!-- End of picture text -->


<!-- Start of picture text -->
Generalized mass spectrometer<br><!-- End of picture text -->

All **mass analyzers** use electromagnetic fields to manipulate gas-phase ions. Results are plotted as a spectrum, with mass-over-charge ( _m/z_ ) on the X-axis and ion intensity on the Y-axis. The latter can be absolute (counts) or relative. The **ion source** ensures that (a part of) the sample molecules are ionized and brought into the gas phase. The **detector** is responsible for actually recording the presence of ions. **Digitizers** (analog to digital converters; ADC) transform the continuous, analog detector signal into a digital, discretized spectrum.

4


<!-- Start of picture text -->
Ion sources: MALDI<br>laser irradiation high vacuum<br>h <br>desorption ++ ++ ++ ++ + proton transfer+ H + ++++ +++++++++++ +<br>matrix Gas phase<br>molecule<br>analyte<br>target<br>surface<br>Matrix Assisted Laser Desorption and Ionization (MALDI)<br>MALDI sources for proteomics typically rely on a pulsed nitrogen UV laser<br>( = 337 nm) and produce singly charged peptide ions. Competitive ionisation occurs.<br><!-- End of picture text -->

The term ‘MALDI’ was coined by **Karas and Hillenkamp** ( _Anal. Chem._ , 1985) and **Koichi Tanaka** received the 2002 Nobel Prize in Chemistry for demonstrating MALDI ionization of biological macromolecules ( _Rapid Commun. Mass Spectrom._ , 1988)


<!-- Start of picture text -->
Ion sources: ESI<br>www.sitemaker.umich.edu/mass-spectrometry/sample_preparation m/z analyzer inlet<br>+ + ++ ++<br>+ + +<br>+ + droplet evaporation and<br>+ + charge-driven fission<br>+<br>3-5 kV + + + or ion expulsion<br>+ +<br>+<br>+<br>+ + evaporation only<br>sample   NN22 0+ 0 0 0 0 00 0 00 00 0   0   0    0 0 0 0 0 0 0 0<br>needle<br>nebulisation<br>barrier<br>Electospray ionization (ESI)<br>ESI sources typically heat the needle to 40 ° to 100 ° to facilitate nebulisation<br>and evaporation, and typically produce multiply charged peptide ions (2 + , 3 + , 4 + )<br>John B. Fenn  received the 2002 Nobel Prize in Chemistry for demonstrating ESI ionization of biological macromolecules<br>( Science , 1989) – ESI is also used in fine control thrusters on satellites and interstellar probes…<br><!-- End of picture text -->

5

---

[Up: contents](index.md) · [Mass resolution is an important characteristic for identification and quantification →](02-mass-resolution-is-an-important-characteristic-for-identific.md)
