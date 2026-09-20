---
title: Recitation 4-2
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-02-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-04-02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Recitation 4-2

EF lectures #12 & 13
Fundamentals of Protein Structure

---

## Announcements

- Pset #3 was due today at noon
- Pset #4 should be released sometime Friday

---

## Intro to Protein Structure

**Four levels of protein structure:**

- **Primary:** the amino acid sequence

- **Secondary:** structures formed through interactions of the peptide backbone ($\alpha$-helix, $\beta$-sheet most common)

- **Tertiary:** folding due to side chain interactions

- **Quaternary:** noncovalent association of 2+ folded polypeptides (may or may not be relevant)

Primary Protein structure
sequence of a chain of animo acids

Secondary Protein structure
hydrogen bonding of the peptide backbone causes the amino acids to fold into a repeating pattern

Tertiary protein structure
three-dimensional folding pattern of a protein due to side chain interactions

Quaternary protein structure
protein consisting of more than one amino acid chain

Figure 9: The four levels of protein structure can be observed in these illustrations. (credit: modification of work by National Human Genome Research Institute)

Courtesy of National Human Genome Research Institute. Image is in the public domain.

---

## Amino acid (=residue) structure

### Amino Acid Structure

$$\begin{array}{ccccc}
\text{H} & \text{H} & \text{O} & & \\
| & | & || & & \\
\text{H}-\text{N} & - & \text{C} & - & \text{C}-\text{OH} \\
& & | & & \\
& & \text{R} & &
\end{array}$$

Amino Group
Carboxylic Acid Group
$\alpha$ - carbon
Side Chain

http://legacy.owensboro.kctcs.edu/gcaplan/anat/notes/amino_acid_structure_2.jpg

- 20 naturally occurring side chains; each has its own 3 letter (e.g. Met) and 1 letter (e.g. M) abbreviation

- Chemical properties (polar/nonpolar/aromatic ring/charge) and size are important for protein structure and function

PROTEIN AMINO ACIDS

Nonpolar, aliphatic R groups
- Glycine
- Alanine
- Valine
- Leucine
- Methionine
- Isoleucine

Polar, uncharged R groups
- Serine
- Threonine
- Cysteine
- Proline
- Asparagine
- Glutamine

Positively charged R groups
- Lysine
- Arginine
- Histidine

Negatively charged R groups
- Aspartate
- Glutamate

Nonpolar, aromatic R groups
- Phenylalanine
- Tyrosine
- Tryptophan

Courtesy of Rice University. License: CC-BY.

http://cnx.org/content/m44522/latest/Figure_15_01_01.jpg

---

## Biochemistry Review

- Covalent bonds share electrons between atoms to fill their outer electron orbitals
  - Single bond: $2\text{ e}^-$ (1 pair) shared
  - Double bond: $4\text{ e}^-$ (2 pairs) shared
- Single bonds can rotate around bond axis; double bonds are more restricted and cannot
- Amino acids have resonance structures: electrons are delocalized within the molecule and cannot be represented by one single structure

The resonance structure gives the peptide bond *partial double bond character*, and its rotation is restricted

---

## Amino acids and the peptide bond

- Amino acids are connected by **peptide bonds**
- Polypeptide chains are extended from the **N-terminus** to the **C-terminus**
- Due to resonance, the peptide bond is rigid, meaning that rotation can only occur along the $\text{C}'$-$\text{C}_\alpha$ and $\text{C}_\alpha$-$\text{N}$ bonds, not the $\text{N}$-$\text{C}'$ bonds

$\text{C}'$-$\text{C}_\alpha$ : $\Psi$ (psi)
$\text{C}_\alpha$-$\text{N}$ : $\Phi$ (phi)

---

## Peptide chain

Can imagine each peptide as a planar "square", with rotation allowed only at the two opposite corners of the square (see below)

Amino terminus $\leftarrow$
$\rightarrow$ Carboxyl terminus

The $\Psi$ and $\Phi$ angles are further restricted due to steric hindrance between the side chains and the peptide backbone – actual possible conformations are quite limited

We can explore the set of $\Psi$ and $\Phi$ conformations that are favorable using a Ramachandran plot

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Ramachandran Plot

Shows which values of $\Psi$ and $\Phi$ are possible for one type (or more generally, all) amino acids in a protein – most combinations of $\Psi$ and $\Phi$ are forbidden due to steric hindrance

**General case plot:** uses data from nearly 100,000 residues from 500 structures (excluding Gly, Pro, and a.a. before Pro)

**(left) Plot for glycine** – gly side group is just -H, so has less restricted conformations due to less steric hindrance

**(right) Proline** has an unusual structure (amine N bound to 2, not 1 C) that restricts its possible conformations

Courtesy of Jane S. Richardson. License: CC-BY.

---

## Secondary structure: $\alpha$-helices and $\beta$-sheets

Form due to favorable interactions (hydrogen bonding) between molecules of the peptide backbone (not the side chains)

### $\alpha$-helix
$i \rightarrow i+4$ H-bonds;
3.6 a.a./turn

H-bonds

### $\beta$-sheet
N- and C-termini at same ends of sheet: parallel
N-terminus of one strand adjacent to C-terminus of next: anti-parallel

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Secondary structure: $\alpha$-helices and $\beta$-sheets

Form due to favorable interactions (hydrogen bonding) between molecules of the peptide backbone (not the side chains)

### $\alpha$-helix
- Hemoglobin
  © Richard Wheeler. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
  http://en.wikipedia.org/wiki/Alpha-helix
- Rhodopsin
  © Andrei Lomize. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

### $\beta$-sheet
- Courtesy of Isabella Daidone. Image in the public domain.
  http://en.wikipedia.org/wiki/Beta-sheet
- Courtesy of Jason Koval & Kevin Cartwright. Images in the public domain.
- GFP: $\beta$-barrel
  http://en.wikipedia.org/wiki/Beta_barrel
  Courtesy of Christopher King. License: CC-BY.

---

## Secondary structure: $\alpha$-helices and $\beta$-sheets

Form due to favorable interactions (hydrogen bonding) between molecules of the peptide backbone (not the side chains)

### $\alpha$-helix

- If one side of helix faces interior of protein and one faces aqueous exterior, the helix will likely be **amphipathic** (=possesses both hydrophilic and hydrophobic properties)

Image of helical wheel representation of an amino acid sequence removed due to copyright restrictions.

http://lectures.molgen.mpg.de

---

## Tertiary structure: side-chain interactions

- Helices, sheets and other secondary structure elements are combined to produce the complete structure, largely through side chain interactions between amino acids that are far apart along the peptide chain:
  - **Disulfide bridge (bond):** strong covalent bonds that form between 2 Cysteine residues (S-S bond)
  - **Hydrophobic interactions:** hydrophobic side chains tend to be packed away inside the protein, hydrophilic side chains on the outside so $\text{H}_2\text{O}$ can form H-bonds with them
  - **Interactions between charged residues** (ionic bonds)
  - **Hydrogen bonding** between side chains

Hydrogen bond
Hydrophobic interactions (clustering of hydrophobic groups away from water) and van der Waals interactions
Polypeptide backbone
Disulfide bridge
Ionic bond

© Pearson Education, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Quaternary Structure: assembling multiple peptide subunits

- Many proteins contain more than one polypeptide chain (subunits) which interact to form the functional protein
  - Maintained by interchain interactions

The $\alpha_2\beta_2$ Tetramer of Human Hemoglobin
From Biochemistry. 5th edition.
© W. H. Freeman and Company. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

The ribosome consists of a large (orange) and small (green) protein subunit (also contains RNA)
© Albion E. Baucom. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
http://publications.nigms.nih.gov/thenewgenetics/chapter1.html

---

## Protein structure computationally inferred through 2 methods

- 1. **X-ray crystallography (most common)**
  - Crystalline atoms cause a beam of incident X-rays to diffract into many specific direction
  - Crystallizing a protein is difficult!

crystal
$\downarrow$ x-rays
diffraction pattern
$\downarrow$ phases
electron density map
$\downarrow$ fitting
atomic model
$\uparrow$ refinement

Courtesy of Thomas Splettstößer. Used with Permission.
http://en.wikipedia.org/wiki/X-ray_crystallography

---

## Protein structure computationally inferred through 2 methods

- 2. **NMR (nuclear magnetic resonance) spectroscopy:** exploits the magnetic properties of atomic nuclei
  - Intramolecular magnetic field around an atom in a molecule changes the resonance frequency, giving access to details of the electronic structure of a molecule
  - Usually limited to small (<35 kDa) proteins (more common for small, organic molecules)
  - Used for intrinsically disordered proteins or others that can't be crystallized

Ethanol

http://en.wikipedia.org/wiki/NMR_spectroscopy
© T.vanschaik. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Proteins usually assume structures that minimize potential energy

If we could map all possible conformations of a protein onto 2-dimensions with Potential energy as the $3^{\text{rd}}$ (z-) dimension, the protein would fold downward along the potential energy surface to the global minimum

Courtesy of Nature Publishing Group. Used with permission.
Source: Dill, Ken A., and Hue Sun Chan. "From Levinthal to Pathways to Funnels." *Nature Structural Biology* 4, no. 1 (1997): 10-9.

For a particular structure, how do we compute its potential energy? 2 main approaches:
1. Physical explanation for forces (CHARMM)
2. Statistical comparison of structure's components to those observed in other proteins (Rosetta)

---

## 1. CHARMM (Physicist's Approach)

- Chemistry at HARvard Macromolecular Mechanics (developed by Martin Karplus's group – 2013 Nobel Prize in Chemistry)
- Describe physical force fields, which may be approximate but represent identifiable sources
- $U_{\text{CHARMM}} = U_{\text{bonded}} + U_{\text{non-bonded}}$

bonded terms describe interactions between chemically bonded neighbors

$$\left.
\begin{aligned}
U_{\text{bond}} &= \sum_{\text{bonds}} K_b(b - b^0)^2, \\
U_{\text{angle}} &= \sum_{\text{angles}} K_\theta(\theta - \theta^0)^2,
\end{aligned}
\right\} \quad \text{Bond stretching and angle bending modeled as harmonic oscillators}$$

$$U_{UB} = \sum_{\text{Urey-Bradley}} K_{UB}(b^{1-3} - b^{1-3,0})^2,$$

$$U_{\text{dihedral}} = \sum_{\text{dihedrals}} K_\varphi(1 + \cos(n\varphi - \delta)),$$

$$U_{\text{improper}} = \sum_{\text{impropers}} K_\omega(\omega - \omega^0)^2, \text{ and}$$

$$U_{\text{CMAP}} = \sum_{\text{residues}} u_{\text{CMAP}}(\Phi, \Psi)$$

---

## 1. CHARMM (Physicist's Approach)

- Describe physical force fields, which may be approximate but represent identifiable sources
- $U_{\text{CHARMM}} = U_{\text{bonded}} + U_{\text{non-bonded}}$

Lennard-Jones Potential – approximates interactions between a pair of neutral atoms or molecules

$$U_{vdw} \equiv U_{LJ} = \sum_{nonb.\text{pairs}} \varepsilon_{ij} \left[ \left( \frac{r_{ij}^{min}}{r_{ij}} \right)^{12} - 2 \left( \frac{r_{ij}^{min}}{r_{ij}} \right)^6 \right],$$

- $r^{-12}$ term: describes repulsion at short ranges due to overlapping electron orbitals
- $r^{-6}$ term: describes attraction at long ranges (van der Waals force, or dispersion force)

potential energy due to electrostatic interactions:

$$U_{elec} = \sum_{nonb.\text{pairs}} \frac{q_i q_j}{\epsilon r_{ij}}$$

---

## 2. Rosetta (Statistician's Approach)

- Assigns energy values for many of the same forces as CHARMM, but does so by comparing the protein's conformation with those of other observed structures instead of from first principles (e.g. modeling forces as harmonic oscillators, etc.)

**Rotamers:**
Use discrete angles when bonds rotate

Example: angles of methionine side chain are observed to only take on a small number of conformations (rotamers)

- Analogous to Ramachandran plot, but for side chain angles instead of phi/psi angles of protein backbone

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

---

[Up: contents](index.md) · [2. Rosetta (Statistician's Approach) →](02-2-rosetta-statistician-s-approach.md)
