---
title: Absence of chemical attractant
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/01-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Absence of chemical attractant

**Source:** `lectures/01-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Tumble<br>Run<br><!-- End of picture text -->

Image by MIT OCW.

## Presence of chemical attractant


<!-- Start of picture text -->
Attractant<br>Tumble<br>Run<br><!-- End of picture text -->

Chemical Gradient Sensed in a Temporal Manner

Image by MIT OCW.


Figure 1A in Mittal, N., E. O. Budrene, M. P. Brenner, and A. Van Oudenaarden.

"Motility of Escherichia coli cells in clusters formed by chemotactic aggregation." _Proc Natl Acad Sci U S A_ . 100, no. 23 ( Nov 11, 2003): 13259-63. Epub 2003 Nov 03.

##### Chemotaxis of _Escherichia coli_

Images removed due to copyright considerations.

absence aspartate gradient presence aspartate gradient

random walk (diffusion) biased random walk towards aspartate source


Image by MIT OCW. After figure 4 in Falke, J. J., R. B. Bass, S. L. Butler, S. A. Chervitz, and M. A. Danielson.

##### **Adaptation:**


<!-- Start of picture text -->
add  add more remove<br>attractant attractant  attractant<br>1 2 3 4<br>tumbling<br>methylation<br><!-- End of picture text -->

Correlation of Receptor Methylation with Behavioral Response

Image by MIT OCW.

**`slow fast`** What is the simplest mathematical model that is consistent with the biology and reproduces the experiments ?

Figures 2 in Spiro, P. A., J. S. Parkinson, and H. G. Othmer. "A model of excitation and adaptation in bacterial chemotaxis." _Proc Natl Acad Sci U S A._ 94, no. 14 (Jul 8, 1997): 7263-8.

##### I Systems Microbiology (14 Lectures)

_‘The cell as a well-stirred biochemical reactor’_

L1 Introduction L2 Chemical kinetics, Equilibrium binding, cooperativity L3 Lambda phage L4 Stability analysis

L5-6 Genetic switches

- L7 _E. coli_ chemotaxis

- L8 Fine-tuned versus robust models

- L9 Receptor clustering

L10-11 Stochastic chemical kinetics

L12-13 Genetic oscillators

<mark>L14 Circadian rhythms</mark>

II Systems Cell Biology (8 Lectures)

_‘The cell as a compartmentalized system with concentration gradients’_

L15 Diffusion, Fick’s equations, boundary and initial conditions L16 Local excitation, global inhibition theory L17-18 Models for eukaryotic gradient sensing L19-20 Center finding algorithms L21-22  Modeling cytoskeleton dynamics

II Systems Cell Biology (8 Lectures)

_‘The cell as a compartmentalized system with concentration gradients’_

L15 Diffusion, Fick’s equations, boundary and initial conditions L16 Local excitation, global inhibition theory <mark>L17-18 Models for eukaryotic gradient sensing</mark> L19-20 Center finding algorithms L21-22  Modeling cytoskeleton dynamics

##### **Eukaryotic Chemotaxis**

Image removed due to copyright considerations.

How is this different from E. coli chemotaxis ?

temporal versus spatial sensing

cyclic AMP (cAMP) is an attractant for Dictyostelium (social amoeba)

Image removed due to copyright considerations.

##### Response of Dictyostelium to cAMP

initial distribution t ~ 3 s

steady-state distribution � t ∞

uniform step in cAMP


##### cAMP gradient


**uniform and transient**

**polarized and persistent**

geometry of cell: circular inside cytoplasm: well-stirred inside membrane: diffusion-limited


<!-- Start of picture text -->
Chemoattractant<br>Cell<br>GFP-Protein<br>Micropipette<br>θ<br>Trailing edge<br>Leading edge<br><!-- End of picture text -->

Image by MIT OCW.

**GFP-PH** binds special lipids in membrane: PIP2 and PIP3

##### The molecules in the model:


<!-- Start of picture text -->
Receptor Regulated Step<br>Plasma<br> Membrane PA DG PI4P,5P2 PI4P PI<br>DGK PLC PI4P5K PI4K<br>IP3<br>PITP Cytosol<br>Inositol<br>PA CDP.DG PI<br>Endoplasmic CDP.DGS PIS<br>Reticulum<br>+<br><!-- End of picture text -->

Image by MIT OCW.

II Systems Cell Biology (8 Lectures)

_‘The cell as a compartmentalized system with concentration gradients’_

L15 Diffusion, Fick’s equations, boundary and initial conditions L16 Local excitation, global inhibition theory L17-18 Models for eukaryotic gradient sensing <mark>L19-20 Center finding algorithms</mark> L21-22  Modeling cytoskeleton dynamics

how to find the middle of a cell ?

Image removed due to copyright considerations.

Most of **MinE** accumulates at the rim of this tube, in the shape of a ring (the E ring). The rim of the **MinC/D** tube and associated E ring move from a central position to the cell pole until both the tube and ring vanish. Meanwhile, a new **MinC/D** tube and associated E ring form in the opposite cell half, and the process repeats, resulting in a pole-to-pole oscillation cycle of the division inhibitor. A full cycle takes about 50 s.

Image removed due to copyright considerations.

Recent results demonstrate that the min proteins assemble in helices

Image removed due to copyright considerations.

II Systems Cell Biology (8 Lectures)

_‘The cell as a compartmentalized system with concentration gradients’_

L15 Diffusion, Fick’s equations, boundary and initial conditions L16 Local excitation, global inhibition theory L17-18 Models for eukaryotic gradient sensing L19-20 Center finding algorithms <mark>L21-22  Modeling cytoskeleton dynamics</mark>

Center finding in an eukaryotic cell: fission yeast The importance of the cytoskeleton

Image removed due to copyright considerations.

III Systems Developmental Biology (3 Lectures)

_‘The cell in a social context communicating with neighboring cells’_

L23 Quorum sensing L24-25 Drosophila development

III Systems Developmental Biology (3 Lectures) _‘The cell in a social context communicating with neighboring cells’_

L23 Quorum sensing <mark>L24-25 Drosophila development</mark>

major advantage of Drosphila:

each stripe in the embryo corresponds to certain body parts in adult fly

Image removed due to copyright considerations.

interpreting the bicoid gradient (created by maternal effects) by zygotic effect (gene expression by embryo itself)

Image removed due to copyright considerations.

##### hunchback reads the bicoid gradient

Image removed due to copyright considerations.

###### Center finding in the Drosophila embryo

Image removed due to copyright considerations.

##### I Systems Microbiology (14 Lectures)

_‘The cell as a well-stirred biochemical reactor’_

L1 Introduction <mark>L2 Chemical kinetics, Equilibrium binding, cooperativity</mark> L3 Lambda phage L4 Stability analysis L5-6 Genetic switches L7 _E. coli_ chemotaxis L8 Fine-tuned versus robust models L9 Receptor clustering L10-11 Stochastic chemical kinetics L12-13 Genetic oscillators L14 Circadian rhythms

---

[← Systems Biology](01-systems-biology.md) · [Up: contents](index.md)
