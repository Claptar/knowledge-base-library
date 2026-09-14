---
title: Systems Biology
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/01-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Systems Biology

**Source:** `lectures/01-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Introducing ...

<u>Lectures:</u>

TR 1:00 -2:30 PM

Alexander van Oudenaarden

<u>Recitations:</u>

W 4:00 - 5:00 PM

Juan Pedraza

Text books: none

Handouts will be available on-line

Good reference (biology textbook): Molecular biology of the cell Alberts et al.

Matlab will be used intensively during the course, make sure you known (or learn) how to use it (necessary for problem sets)

Intrinsic challenge of this class:

mixed audience with wildly different backgrounds

⇒ read up on your biology or math if needed

⇒ recitations (W 4PM,) are intended to close the gaps and prepare for homework

```
Systems Biology ?
```

#### **Systems Biology** ≈ **Network Biology**

**GOAL** : develop a quantitative understanding of the biological function of genetic and biochemical networks

###### INPUT


<!-- Start of picture text -->
g ene A g ene B<br>g ene C gene D<br>gene E gene F<br>OUTPUT<br><!-- End of picture text -->

- function of gene product A-F can be known in detail but this is not sufficient to reveal the biological function of the INPUT-OUTPUT relation

- - a system approach (looking beyond one gene/protein) is necessary to reveal the biological function of this whole network

- what is the function of the individual interactions (feedbacks and feedforwards) in the context of the entire network ?

#### **Three levels of complexity**

I Systems Microbiology (14 Lectures)

_‘The cell as a well-stirred biochemical reactor’_ II Systems Cell Biology (8 Lectures)

_‘The cell as a compartmentalized system with concentration gradients’_

III Systems Developmental Biology (3 Lectures)

_‘The cell in a social context communicating with neighboring cells’_

##### I Systems Microbiology (14 Lectures)

_‘The cell as a well-stirred biochemical reactor’_

L1 Introduction L2 Chemical kinetics, Equilibrium binding, cooperativity L3 Lambda phage L4 Stability analysis

- L5-6 Genetic switches

- L7 _E. coli_ chemotaxis

- L8 Fine-tuned versus robust models

- L9 Receptor clustering

L10-11 Stochastic chemical kinetics

L12-13 Genetic oscillators L14 Circadian rhythms

##### I Systems Microbiology (14 Lectures)

_‘The cell as a well-stirred biochemical reactor’_

L1 Introduction L2 Chemical kinetics, Equilibrium binding, cooperativity <mark>L3 Lambda phage</mark> L4 Stability analysis L5-6 Genetic switches L7 _E. coli_ chemotaxis L8 Fine-tuned versus robust models L9 Receptor clustering L10-11 Stochastic chemical kinetics

L12-13 Genetic oscillators

L14 Circadian rhythms

##### Introduction phage biology

Phage genome: 48512 base pairs ~ 12 kB ‘phage.jpg’ ~ 10 kB

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda._ 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

DNA


<!-- Start of picture text -->
REPLICATION<br>DNA Duplicates<br>Information<br>DNA<br>Information<br>TRANSCRIPTION<br>RNA Synthesis<br>RNA<br>mRNA<br>Nucleus<br>Information<br>Cytoplasm<br>Nuclear Envelope<br>TRANSLATION<br>Ribosome<br>Protein Synthesis<br>Protein<br><!-- End of picture text -->


<!-- Start of picture text -->
Protein<br><!-- End of picture text -->

The central dogma defines three major groups of biomolecules (biopolymers):

**1. DNA (passive library, 6×10**<sup>**9**</sup> **bp, 2 m/cell, 75×10**<sup>**12**</sup> **cells/human, total length 150×10**<sup>**12**</sup> **m/human ~ 1000 rsun-earth)**

###### **2. RNA (‘passive’ intermediate) 3. Proteins (active work horses)**

The fourth (and final) group consists of so-called ‘small molecules’.

**4. Small molecules (sugars, hormones, vitamines, ‘substrates’ etc.)**

##### The lysis-lysogeny decision:


As the phage genome is injected phage genes are transcribed and translated by using the host’s machinery.

Which set of phage proteins are expressed determines the fate of the phage: lysis or lysogeny


The lysis-lysogeny decision is a genetic switch

###### Single repressor dimer bound - three cases:

I

Negative control, dimer binding to OR2 inhibits RNAp binding to right PR promoter. Positive control, dimer binding to OR2 enhances RNAp binding to left PRM promoter.

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda._ 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

II

Negative control, dimer binding to OR1 inhibits RNAp binding to right PR promoter. Negative control, dimer binding to OR1 inhibits RNAp binding to left PRM promoter (too distant).

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

III

Negative control, dimer binding to OR3 inhibits RNAp binding to left PRM promoter. Positive control, dimer binding to OR3 allows RNAp binding to right PR promoter.

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

###### Repressor-DNA binding is highly cooperative

intrinsic association constants: KOR1 ~ 10 KOR2 ~ 10 KOR3 However KOR2* >> KOR2 (positive cooperativity)

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

###### **Flipping the switch by UV:**


Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

In lysogenic state, [repressor] is maintained at constant level by negative feedback

UV radiation induces SOS response (DNA damage) protein RecA becomes specific protease for λ repressor

Images removed due to copyright considerations. See Ptashne, Mark. _A genetic switch : phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

after cleavage monomers cannot dimerize anymore, [repressor dimers] decreases, when all repressors vacate DNA, Cro gene switches on.

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

###### Cooperative effects make sharp switch (‘well defined’ decision)


<!-- Start of picture text -->
99.7% repression 1.0 nH=3, positively cooperative<br>promoter controlled by a<br>single repressor-operator system  0.8<br>100<br>0.6 nH=1, non cooperative<br>λ PD 0.4<br>50<br>0.2<br>lysogen<br>0.0<br>0 1 2 3 4 5<br>Repressor concentration [S]   (mM)<br>Y<br>% Repression<br><!-- End of picture text -->

Images by MIT OCW.

Note: several layers of cooperativity: dimerization, cooperative repressor binding

##### I Systems Microbiology (14 Lectures)

_‘The cell as a well-stirred biochemical reactor’_

L1 Introduction L2 Chemical kinetics, Equilibrium binding, cooperativity L3 Lambda phage L4 Stability analysis L5-6 Genetic switches <mark>L7</mark> _<mark>E. coli</mark>_ <mark>chemotaxis</mark> L8 Fine-tuned versus robust models L9 Receptor clustering L10-11 Stochastic chemical kinetics L12-13 Genetic oscillators L14 Circadian rhythms

Images removed due to copyright considerations.

# The Flagellum

Image removed due to copyright considerations.

---

[Up: contents](index.md) · [Absence of chemical attractant →](02-absence-of-chemical-attractant.md)
