---
title: SCIENCE MEETS LIFE
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/martens_proteomics_bioinformatics.pdf
source_file: sources/statomics-sga21/docs/martens_proteomics_bioinformatics.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`docs/martens_proteomics_bioinformatics.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/martens_proteomics_bioinformatics.pdf) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# SCIENCE MEETS LIFE

## MS-BASED PROTEOMICS DATA ANALYSIS

lennart martens
lennart.martens@vib-ugent.be
@compomics
computational omics and systems biology group
Ghent University and VIB, Ghent, Belgium

VIB | GHENT UNIVERSITY | Compomics

---

## Proteomics in the central paradigm of biology

- Primary structure (sequence)
  ...YSFVATAER...
- Secondary structure (structural elements)
- Tertiary structure (3D shape)
- Modifications (dynamic, function)
  phosphorylation
- Processing (targeting, activation)
  trypsin
  platelet activity

Adapted from the NCBI Science Primer
http://www.ncbi.nih.gov/About/primer/genetics_cell.html

---

## Amino acids, peptides, and proteins

Mass spectrometry basics

MS/MS spectra and identification

Database search algorithms in three phases

Sequential search algorithms

Decoys and false discovery rate calculation

Protein inference: bad, ugly, and not so good

---

## Amino acids, peptides, and proteins

Mass spectrometry basics

MS/MS spectra and identification

Database search algorithms in three phases

Sequential search algorithms

Decoys and false discovery rate calculation

Protein inference: bad, ugly, and not so good

---

## Amino acids vary considerably in their physico-chemical properties

http://courses.cm.utexas.edu/jrobertus/ch339k/overheads-1/ch5-amino-acids.jpg

---

## Protein backbones are formed through amide (or peptide) bonds between residues

$$\text{amino group} + \text{carboxyl group} \rightarrow \text{peptide bond} + \text{H}_2\text{O}$$

side chain: R1, R2

$$\text{amino terminus} - [\text{residue}] - \text{carboxyl terminus}$$

$\text{H}_2\text{N} - \text{CH}(\text{R}_1) - \text{CO} - \text{NH} - \text{CH}(\text{R}_2) - \text{CO} - \dots - \text{COOH}$

---

Amino acids, peptides, and proteins

## Mass spectrometry basics

MS/MS spectra and identification

Database search algorithms in three phases

Sequential search algorithms

Decoys and false discovery rate calculation

Protein inference: bad, ugly, and not so good

---

## A generalized mass spectrometer consists of three main parts, along with a digitizer

```
sample -> [ ion source ] -> [ mass analyzer(s) ] -> [ detector ] -> [ digitizer ]
          \________________ Generalized mass spectrometer _________/
```

All **mass analyzers** use electromagnetic fields to manipulate gas-phase ions. Results are plotted as a spectrum, with mass-over-charge ($m/z$) on the X-axis and ion intensity on the Y-axis. The latter can be absolute (counts) or relative. The **ion source** ensures that (a part of) the sample molecules are ionized and brought into the gas phase. The **detector** is responsible for actually recording the presence of ions. **Digitizers** (analog to digital converters; ADC) transform the continuous, analog detector signal into a digital, discretized spectrum.

---

## Ion sources: MALDI

laser irradiation ($h \cdot \nu$)
desorption $\rightarrow$ proton transfer
analyte, matrix molecule
$\text{H}^+$
Gas phase
high vacuum

*Matrix Assisted Laser Desorption and Ionization (MALDI)*

MALDI sources for proteomics typically rely on a pulsed nitrogen UV laser ($\nu = 337\text{ nm}$) and produce singly charged peptide ions. Competitive ionisation occurs.

The term 'MALDI' was coined by Karas and Hillenkamp (Anal. Chem., 1985) and Koichi Tanaka received the 2002 Nobel Prize in Chemistry for demonstrating MALDI ionization of biological macromolecules (Rapid Commun. Mass Spectrom., 1988)

---

## Ion sources: ESI

sample, $\text{N}_2$
needle
nebulisation
3-5 kV
droplet evaporation and charge-driven fission or ion expulsion
$m/z$ analyzer inlet
barrier
evaporation only

*Electrospray ionization (ESI)*

ESI sources typically heat the needle to $40^\circ$ to $100^\circ$ to facilitate nebulisation and evaporation, and typically produce multiply charged peptide ions ($2+$, $3+$, $4+$)

John B. Fenn received the 2002 Nobel Prize in Chemistry for demonstrating ESI ionization of biological macromolecules (Science, 1989) – ESI is also used in fine control thrusters on satellites and interstellar probes...

---

## Mass resolution is an important characteristic for identification and quantification

Resolution in mass spectrometry is usually defined as the width of a peak at a given height (there is an alternative definition based on percent valley height). This width can be recorded at different heights, but is most often recorded at 50% peak height (FWHM).

average mass
monoisotopic mass

From: Eidhammer, Flikka, Martens, Mikalsen – Wiley 2007

---

## Detectors: electron multiplier amplification

Different variations of electron multiplier (EM) detectors are used, and these are the most common type of detector. An EM relies on several Faraday cup dynodes with increasing charges to produce an electron cascade from a few incident ions.

single ion in
20V $\rightarrow$ 40V $\rightarrow$ 60V $\rightarrow$ 80V $\rightarrow$ 100V $\rightarrow$ 120V
$10^6$ electrons out

---

## The primary principle in quantification is that detector signal relates to quantity

**Make each sample distinguishable**
introduce mass differences between the samples
perform distinct experimental runs for each sample

**Measure the intensity of the signal for each analyte in each sample**

**Statistically process the accumulated information**

1/2, 1/1, 2/1

---

## Not all peptides ionise equally, so we cannot compare signal strength across peptides

protein $\rightarrow$ peptide $\rightarrow$ MS1 signal

---

## As intensities become more extreme, the detector response starts to level off

error bar = 1 standard deviation

$\log_2(\text{measured ratio})$ vs. $\log_2(\text{expected ratio})$

Gevaert, Proteomics, 2007

---

## At the same time, the measurement error increases as the ratio deviates from 1/1

Error [%] vs. signal intensity ratio for two peaks

Vaudel, Proteomics, 2010

---

## And these effects remain quite visible, even on modern instruments (Orbitrap)

measured $\log2$ ratio vs. ratio mixing sample

---

## Raw data processing is somewhat imprecise, with expected errors on the order of 10%

**Mass spectrometer specific processing required**
**Sets the dynamic range lower limit (S/N)**
**5-10% error in the final ratios due to peak-picker are often seen**

Black: 0,02 Da
Blue: 0,04 Da
Red: 0,08 Da

Non-adapted shape -> +10% error

Vaudel, Proteomics, 2010

---

## Different model options are available in tools or libraries for MS peak detection

Decon2LS

Vaudel, Proteomics, 2010

---

## There's actually more to a peak than just m/z

OpenMS TOPPView

Vaudel, Proteomics, 2010

---

## Serum proteins are degraded over time, even with the best sampling tubes

Yi, J Prot Res, 2007

---

## Our open modification search engine ionbot shows that modifications are also an issue

| Protein name | Protein accession | Number of modifications |
| :--- | :--- | :--- |
| Glyceraldehyde-3-phosphate dehydrogenase | P04406 | 166 |
| Pyruvate kinase PKM | P14618 | 139 |
| Fructose-bisphosphate aldolase A | P04075 | 122 |
| Alpha-enolase | P06733 | 121 |
| Triosephosphate isomerase | P60174 | 117 |
| Phosphoglycerate kinase | P00558 | 111 |

*Mods found across all six proteins, between 50 and 278 distinct peptides*

carbamyl, carbamidomethyl, formyl, acetyl, oxidation, methyl, thiazolidine, amidine, dehydrated, dicarbamidomethyl, dioxidation, succinyl, ammonia-loss, ethyl, carboxymethyl, guanidinyl, gg, cation:fe[iii]

https://ionbot.cloud
Source data presented to ionbot from Kim et al., Nature, 2014

---

Amino acids, peptides, and proteins

Mass spectrometry basics

## MS/MS spectra and identification

Database search algorithms in three phases

Sequential search algorithms

Decoys and false discovery rate calculation

Protein inference: bad, ugly, and not so good

---

## Identification relies on fragmentation

```
[ source ] -> [ ion selector ] -> [ fragmentation ] -> [ fragment mass analyzer ] -> [ detector ]
```

Tandem-MS is accomplished by using two mass analyzers in series (tandem). A single ion trap can also perform tandem-MS. The first mass analyser performs the function of ion selector, by selectively allowing only ions of a given $m/z$ to pass through. The second mass analyzer is situated after fragmentation is triggered (see next slides) and is used in its normal capacity as a mass analyzer for the fragments.

---

## Peptides subjected to fragmentation analysis can yield several types of fragment ions

N-terminal ions: $a_1, b_1, c_1, a_2, b_2, c_2, a_3, b_3, c_3$
C-terminal ions: $x_3, y_3, z_3, x_2, y_2, z_2, x_1, y_1, z_1$

There are several other ion types that can be annotated, as well as 'internal fragments'. The latter are fragments that no longer contain an intact terminus. These are harder to use for 'ladder sequencing', but can still be interpreted.

This nomenclature was coined by Roepstorff and Fohlmann (Biomed. Mass Spec., 1984) and Klaus Biemann (Biomed. Environ. Mass Spec., 1988) and is commonly referred to as 'Biemann nomenclature'. Note the link with the Roman alphabet.

---

## In an ideal world, the peptide sequence will produce directly interpretable ion ladders

L

---

[Up: contents](../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 1 of the original](martens_proteomics_bioinformatics/figures/p001-1.jpeg)

![Figure from page 1 of the original](martens_proteomics_bioinformatics/figures/p001-3.jpeg)

![Figure from page 3 of the original](martens_proteomics_bioinformatics/figures/p003-2.jpeg)

![Figure from page 3 of the original](martens_proteomics_bioinformatics/figures/p003-3.jpeg)

![Figure from page 3 of the original](martens_proteomics_bioinformatics/figures/p003-4.jpeg)

![Figure from page 5 of the original](martens_proteomics_bioinformatics/figures/p005-59.jpeg)

![Figure from page 6 of the original](martens_proteomics_bioinformatics/figures/p006-2.jpeg)

![Figure from page 6 of the original](martens_proteomics_bioinformatics/figures/p006-3.jpeg)

![Figure from page 6 of the original](martens_proteomics_bioinformatics/figures/p006-4.jpeg)

![Figure from page 7 of the original](martens_proteomics_bioinformatics/figures/p007-5.jpeg)

![Figure from page 8 of the original](martens_proteomics_bioinformatics/figures/p008-2.jpeg)

![Figure from page 8 of the original](martens_proteomics_bioinformatics/figures/p008-3.jpeg)

![Figure from page 9 of the original](martens_proteomics_bioinformatics/figures/p009-2.jpeg)

![Figure from page 10 of the original](martens_proteomics_bioinformatics/figures/p010-2.jpeg)

![Figure from page 10 of the original](martens_proteomics_bioinformatics/figures/p010-3.jpeg)

![Figure from page 10 of the original](martens_proteomics_bioinformatics/figures/p010-4.jpeg)

![Figure from page 11 of the original](martens_proteomics_bioinformatics/figures/p011-2.jpeg)

![Figure from page 12 of the original](martens_proteomics_bioinformatics/figures/p012-4.jpeg)

![Figure from page 15 of the original](martens_proteomics_bioinformatics/figures/p015-3.jpeg)

![Figure from page 15 of the original](martens_proteomics_bioinformatics/figures/p015-9.jpeg)

![Figure from page 17 of the original](martens_proteomics_bioinformatics/figures/p017-2.jpeg)

![Figure from page 17 of the original](martens_proteomics_bioinformatics/figures/p017-11.jpeg)

![Figure from page 18 of the original](martens_proteomics_bioinformatics/figures/p018-2.jpeg)

![Figure from page 18 of the original](martens_proteomics_bioinformatics/figures/p018-3.jpeg)

![Figure from page 19 of the original](martens_proteomics_bioinformatics/figures/p019-2.jpeg)

![Figure from page 20 of the original](martens_proteomics_bioinformatics/figures/p020-2.jpeg)

![Figure from page 20 of the original](martens_proteomics_bioinformatics/figures/p020-3.jpeg)

![Figure from page 21 of the original](martens_proteomics_bioinformatics/figures/p021-2.jpeg)

![Figure from page 21 of the original](martens_proteomics_bioinformatics/figures/p021-3.jpeg)

![Figure from page 22 of the original](martens_proteomics_bioinformatics/figures/p022-2.jpeg)

![Figure from page 22 of the original](martens_proteomics_bioinformatics/figures/p022-3.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-2.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-3.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-4.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-5.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-6.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-7.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-8.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-9.jpeg)

![Figure from page 23 of the original](martens_proteomics_bioinformatics/figures/p023-10.jpeg)

![Figure from page 24 of the original](martens_proteomics_bioinformatics/figures/p024-2.jpeg)

![Figure from page 25 of the original](martens_proteomics_bioinformatics/figures/p025-2.jpeg)

![Figure from page 25 of the original](martens_proteomics_bioinformatics/figures/p025-3.jpeg)

![Figure from page 25 of the original](martens_proteomics_bioinformatics/figures/p025-4.jpeg)

![Figure from page 25 of the original](martens_proteomics_bioinformatics/figures/p025-5.jpeg)

![Figure from page 26 of the original](martens_proteomics_bioinformatics/figures/p026-2.jpeg)

![Figure from page 27 of the original](martens_proteomics_bioinformatics/figures/p027-2.jpeg)

![Figure from page 27 of the original](martens_proteomics_bioinformatics/figures/p027-5.jpeg)

![Figure from page 28 of the original](martens_proteomics_bioinformatics/figures/p028-2.jpeg)

![Figure from page 28 of the original](martens_proteomics_bioinformatics/figures/p028-3.jpeg)

![Figure from page 28 of the original](martens_proteomics_bioinformatics/figures/p028-4.jpeg)

![Figure from page 29 of the original](martens_proteomics_bioinformatics/figures/p029-2.jpeg)

![Figure from page 30 of the original](martens_proteomics_bioinformatics/figures/p030-2.jpeg)

![Figure from page 31 of the original](martens_proteomics_bioinformatics/figures/p031-2.jpeg)

![Figure from page 31 of the original](martens_proteomics_bioinformatics/figures/p031-3.jpeg)

![Figure from page 31 of the original](martens_proteomics_bioinformatics/figures/p031-4.jpeg)

![Figure from page 31 of the original](martens_proteomics_bioinformatics/figures/p031-5.jpeg)

![Figure from page 31 of the original](martens_proteomics_bioinformatics/figures/p031-6.jpeg)

![Figure from page 31 of the original](martens_proteomics_bioinformatics/figures/p031-7.jpeg)

