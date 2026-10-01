---
title: "1. Introduction to Systems Biology"
course: "MIT 8.591J 2004"
chapter: 1
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Introduction to Systems Biology

## What this covers

This is the opening lecture of the course, and it answers a different question from the ones that
follow: not "how does this particular system work" but "what does it mean to study a cell as a
*system*, and what kinds of question will this course keep asking of very different organisms?" It
assumes only the central dogma (DNA to RNA to protein) and enough general biology to recognize a
gene, a promoter and a receptor; no mathematical machinery is used yet. The lecture works by walking
through the syllabus and pausing at five representative lectures — one from each part of the
course — to preview, in outline, the biological system and the question attached to it. This chapter
follows the same structure: the roadmap first, then each preview in turn.

## Systems biology as network biology

The course's working definition: **systems biology $\approx$ network biology**, with the goal of
developing a *quantitative* understanding of the biological function of genetic and biochemical
networks.

Picture a network with inputs — genes $A, B, C, D, E, F$ — feeding into some output. The point of
the definition is a specific claim about what is and is not sufficient to explain that output:

- The function of each individual gene product, $A$ through $F$, can be known in complete
  biochemical detail, and that still does not reveal the biological function of the input-output
  relation for the network as a whole.
- Revealing that function requires a systems approach — looking beyond any one gene or protein to
  the network it sits in.
- The question the course keeps returning to is: what is the function of a given interaction —
  a particular feedback loop, a particular feedforward path — *in the context of the entire
  network*, not in isolation?

This is why the class draws on a genuinely mixed audience (biology and mathematics/physics
backgrounds alike): neither the biological detail nor the quantitative machinery is optional if the
goal is the input-output relation itself, rather than a catalogue of parts.

## Three levels of complexity

The syllabus is organized around three pictures of what a cell is, each with a different unit of
analysis:

**I. Systems Microbiology** (14 lectures) — *the cell as a well-stirred biochemical reactor*.
L1 Introduction; L2 Chemical kinetics, equilibrium binding, cooperativity; L3 Lambda phage;
L4 Stability analysis; L5–6 Genetic switches; L7 *E. coli* chemotaxis; L8 Fine-tuned versus robust
models; L9 Receptor clustering; L10–11 Stochastic chemical kinetics; L12–13 Genetic oscillators;
L14 Circadian rhythms.

**II. Systems Cell Biology** (8 lectures) — *the cell as a compartmentalized system with
concentration gradients*. L15 Diffusion, Fick's equations, boundary and initial conditions;
L16 Local excitation, global inhibition theory; L17–18 Models for eukaryotic gradient sensing;
L19–20 Center-finding algorithms; L21–22 Modeling cytoskeleton dynamics.

**III. Systems Developmental Biology** (3 lectures) — *the cell in a social context, communicating
with neighboring cells*. L23 Quorum sensing; L24–25 Drosophila development.

Read across the three parts, the unit of "system" is escalating: a single reactor, then a cell with
internal geometry, then a population of communicating cells. The five previews below sit at L3, L7,
L17–18, L19–20 and L24–25 respectively — one per part, except Part I gets two.

## The central dogma, and the scale of the parts list

Before any of the case studies, the lecture puts a number on the "parts list" a network is built
from. The central dogma —

$$\text{DNA} \xrightarrow{\text{replication}} \text{DNA}, \qquad \text{DNA} \xrightarrow{\text{transcription}} \text{mRNA} \xrightarrow{\text{translation}} \text{protein}$$

— defines three of the four classes of biomolecule the course will work with: **DNA** (a passive
library — a human genome is about $6\times 10^9$ base pairs, roughly $2\,\mathrm{m}$ of DNA per
cell, and with $\sim 75\times 10^{12}$ cells per human the total length works out to
$\sim 150\times 10^{12}\,\mathrm{m}$, about a thousand times the Earth–Sun distance); **RNA** (a
passive intermediate); and **proteins** (the active work-horses — the molecules that actually do
things). The fourth class, added because it doesn't fit the DNA-to-protein flow, is **small
molecules**: sugars, hormones, vitamins, substrates — everything a network of genes and proteins
acts on or is regulated by.

## Preview 1 (L3): the lambda phage lysis-lysogeny switch

Bacteriophage lambda, a virus that infects *E. coli* (genome $\sim 48{,}512$ bp, about 12 kB), makes
a binary decision after it injects its DNA: **lysis** (make more phage and kill the host cell) or
**lysogeny** (integrate into the host genome and stay dormant). Which phage genes get transcribed
and translated by the host machinery determines the outcome, and the decision is a genuine genetic
switch, controlled by two competing genes — cI and cro — that sit on either side of a shared
regulatory region, $O_R$ (the right operator), between two promoters: $P_{RM}$, which transcribes
cI leftward, and $P_R$, which transcribes cro rightward. $O_R$ contains three binding sites for the
cI repressor protein (which binds as a dimer): $O_R3$, next to $P_{RM}$; $O_R2$, in the middle; and
$O_R1$, next to $P_R$, with a 17 bp spacer between $O_R3$ and $O_R2$.

<figure>
<svg viewBox="0 0 360 170" role="img" aria-label="Layout of the lambda right operator, showing the two promoters and the three repressor dimer binding sites between them">
  <line x1="20" y1="90" x2="340" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <line x1="55" y1="90" x2="20" y2="90" stroke="currentColor" stroke-width="2"/>
  <polygon points="20,90 28,85 28,95" fill="currentColor"/>
  <text x="45" y="62" text-anchor="middle" font-size="12" fill="currentColor">cI transcript</text>
  <text x="45" y="115" text-anchor="middle" font-size="12" fill="currentColor">PRM</text>

  <rect x="110" y="82" width="26" height="16" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="123" y="112" text-anchor="middle" font-size="11" fill="currentColor">OR3</text>

  <rect x="170" y="82" width="26" height="16" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="183" y="112" text-anchor="middle" font-size="11" fill="currentColor">OR2</text>

  <rect x="225" y="82" width="26" height="16" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="238" y="112" text-anchor="middle" font-size="11" fill="currentColor">OR1</text>

  <text x="153" y="76" text-anchor="middle" font-size="10" fill="currentColor">17 bp</text>

  <line x1="285" y1="90" x2="320" y2="90" stroke="currentColor" stroke-width="2"/>
  <polygon points="320,90 312,85 312,95" fill="currentColor"/>
  <text x="303" y="62" text-anchor="middle" font-size="12" fill="currentColor">cro transcript</text>
  <text x="303" y="115" text-anchor="middle" font-size="12" fill="currentColor">PR</text>

  <text x="123" y="140" text-anchor="middle" font-size="11" fill="currentColor">-PRM  +PR</text>
  <text x="183" y="140" text-anchor="middle" font-size="11" fill="currentColor">+PRM  -PR</text>
  <text x="238" y="140" text-anchor="middle" font-size="11" fill="currentColor">-PRM  -PR</text>
</svg>
<figcaption>The three repressor-dimer sites between the two promoters. A dimer at O<sub>R</sub>3 or
O<sub>R</sub>1 sits next to one promoter and blocks it directly; only a dimer at the middle site,
O<sub>R</sub>2, is positioned to make a favorable contact with RNA polymerase at P<sub>RM</sub> while
still blocking P<sub>R</sub>.</figcaption>
</figure>

The lecture works through what a single bound repressor dimer does at each site:

- **Dimer at $O_R2$**: negative control at $P_R$ (blocks RNAp there) and **positive control** at
  $P_{RM}$ — the bound dimer *enhances* RNAp binding at the left promoter.
- **Dimer at $O_R1$**: negative control at $P_R$ (adjacent, direct block) and negative control at
  $P_{RM}$ too — inhibited even though $O_R1$ is the more distant site from $P_{RM}$.
- **Dimer at $O_R3$**: negative control at $P_{RM}$ (adjacent, direct block) and it *allows* RNAp
  binding at $P_R$ — labelled positive control, though of a more permissive kind than $O_R2$'s
  direct enhancement of $P_{RM}$.

Binding across the three sites is **highly cooperative**. The intrinsic (non-cooperative)
association constants for the dimer at each site rank $K_{O_R1} \sim 10\,K_{O_R2} \sim 10\,K_{O_R3}$
— on its own, the dimer prefers $O_R1$ most and $O_R3$ least. But once a neighboring site is
occupied, the *cooperative* constant for $O_R2$, written $K_{O_R2}^{*}$, is far larger than its
intrinsic value: $K_{O_R2}^{*} \gg K_{O_R2}$. Binding at one site helps binding at the next, and
this — stacked on top of the fact that the repressor must first dimerize before it can bind DNA at
all — is what turns a graded dependence on repressor concentration into something closer to an
on/off switch: the course's running illustration compares a single, non-cooperative
repressor-operator system against the full $\lambda P_R$ system in the lysogen, which reaches
$99.7\%$ repression, and separately plots a Hill-type binding curve at Hill coefficient $n_H=1$
(graded) against $n_H=3$ (steep, switch-like) — the machinery behind that plot belongs to L2, but the
point previewed here is that **several layers of cooperativity compound**: dimerization, then
cooperative binding across the operator sites.

That sharpness is what makes the switch a reliable decision device, and it's also what has to be
undone to flip it: **UV induction** triggers the SOS DNA-damage response, in which the protein RecA
becomes a specific protease for the lambda repressor. Cleaved monomers can no longer dimerize, so
the pool of repressor dimers falls; once repressor has vacated the operator sites entirely, the cro
gene switches on and the cell commits to lysis. In the lysogenic state, by contrast, repressor level
is held essentially constant by negative feedback (cI represses its own further activation once
enough is present) — so the switch, once set, is not just sharp but stable, and only a strong signal
like DNA damage flips it.

## Preview 2 (L7): *E. coli* chemotaxis and adaptation

*E. coli* swims by rotating flagella and alternates between two behaviors, **run** and **tumble**.
With no chemical gradient present, this alternation produces an unbiased random walk — pure
diffusion. In the presence of an attractant gradient (e.g. aspartate), the same run/tumble machinery
produces a **biased** random walk toward the source: the cell doesn't steer, it simply suppresses
tumbling (extends runs) when things are getting better.

The signal reaches the flagellar motor through a phosphorelay. Two classes of ligand are sensed:
some (maltose, galactose, glucose, ribose, dipeptide, Ni(II)) bind a periplasmic binding protein
first; others (aspartate, serine, citrate) bind a methylated receptor directly. Either way, signal
flows through a receptor complex (CheW, and the histidine kinase CheA, which converts ATP to
ADP + P$_i$) to the response regulator **CheY**: phosphorylated CheY diffuses to the motor and
controls its switching, while the phosphatase **CheZ** removes the phosphate again. In parallel, two
methylation enzymes act on the receptor itself: **CheR** adds methyl groups; **CheB**, itself a
response regulator, removes them (releasing methanol + P$_i$).

The reason for that second, slower loop is **adaptation**, and the lecture's key experiment
correlates receptor methylation with tumbling behavior across four phases: (1) baseline tumbling
and methylation; (2) add attractant — tumbling ceases almost immediately and methylation begins to
rise; (3) add more attractant — methylation climbs to a new, higher plateau; (4) remove attractant —
tumbling increases (overshoots) and then resets to baseline, while methylation falls back down. The
behavioral response (tumbling frequency) always returns to its pre-stimulus baseline even while a
constant stimulus is still present — that return-to-baseline despite a sustained input is what
"adaptation" means here.

The reaction network behind this has three distinct timescales, in the notation the lecture uses for
receptor states with $m$ methyl groups ($T_m$, or $LT_m$ once ligand-bound) and their phosphorylated
forms (subscript $p$):

- **Fast** — ligand binding/unbinding and phosphorylation equilibria:
  $$T_2 \leftrightarrow LT_2, \quad T_3 \leftrightarrow LT_3, \quad T_4 \leftrightarrow LT_4, \qquad T_{2p} \leftrightarrow LT_{2p}, \quad T_{3p} \leftrightarrow LT_{3p}, \quad T_{4p} \leftrightarrow LT_{4p}$$
- **Slow** — methylation/demethylation, ratcheting the receptor between methylation states:
  $$T_2 \to T_3 \to T_4, \qquad LT_2 \to LT_3 \to LT_4, \qquad T_{2p} \to T_{3p} \to T_{4p}, \qquad LT_{2p} \to LT_{3p} \to LT_{4p}$$
- **Intermediate** — phosphorylation/dephosphorylation of the receptor itself:
  $$T_m \leftrightarrow T_{mp}, \qquad LT_m \leftrightarrow LT_{mp}$$
- **Downstream signaling**, the phosphotransfer to the response regulators:
  $$LT_{np} + Y \to Y_p + LT_n, \qquad LT_{np} + B \to B_p + LT_n$$

The question the lecture poses about this scheme, and hands to the rest of the course, is:
*what is the simplest mathematical model that is consistent with the biology and reproduces the
four-phase experiment?*

## Preview 3 (L17–18): eukaryotic gradient sensing

*Dictyostelium* (a social amoeba) chemotaxes toward cyclic AMP (cAMP), and the lecture poses the
comparison directly: how is this different from *E. coli* chemotaxis? The answer is **temporal
versus spatial sensing**. *E. coli* is small enough that it can only compare concentration at one
point in space over time as it swims. A eukaryotic cell is large enough to compare concentration
*across its own body* at a single instant — geometrically, the cytoplasm is treated as well-stirred
but the plasma membrane as diffusion-limited, so a signal received at one patch of membrane need not
equilibrate with the rest before the cell responds.

This shows up directly in the experiment: given a **uniform step** in cAMP concentration, the
reporter (GFP-PH, which binds the membrane lipids PIP2 and PIP3) redistributes transiently and
uniformly around the whole perimeter, then returns to steady state — the same adapt-back-to-baseline
behavior seen in *E. coli*. Given a **gradient** in cAMP instead, the response is polarized toward
the source (a leading-edge arc) and, critically, **persistent** rather than transient.

The molecular pathway sketched for this: at the plasma membrane, PI is converted to PI4P
(by PI4K), then to PI4P,5P$_2$ (by PI4P5K); PI4P,5P$_2$ is split by PLC into IP$_3$ (which diffuses
into the cytosol) and DG, which DGK converts to PA. PA feeds back **positively** on PI4P5K — the one
explicit feedback loop named in the pathway. Inositol released in the cytosol, and PA, are shuttled
back to the endoplasmic reticulum via a transport protein (PITP), where PA is converted back to PI
(via CDP-DG) to complete the cycle.

## Preview 4 (L19–20): finding the middle of a cell

Center-finding is posed as a question that shows up in both a bacterial and a eukaryotic setting.
In bacteria, the division site is positioned by the oscillating **Min system**: **MinE** accumulates
in a ring (the "E ring") at the rim of a **MinC/D**-filled tube; that tube and its E ring shrink from
a central position toward one cell pole until both vanish, while a new MinC/D tube and E ring form
in the opposite half of the cell — a pole-to-pole oscillation, one full cycle taking about 50
seconds, that keeps the time-averaged concentration of the division inhibitor MinC lowest in the
middle. (More recent results, noted in passing, show the Min proteins can also assemble into
helices.) In a eukaryotic setting, the same "find the middle" question is illustrated with fission
yeast, where it is the cytoskeleton, rather than a reaction-diffusion oscillator, that does the
centering.

## Preview 5 (L24–25): patterning the Drosophila embryo

The developmental preview moves the unit of analysis up again, to a multicellular embryo. Drosophila
is useful here for a structural reason: each stripe visible in the embryo corresponds to a specific
body part in the adult fly, so a pattern seen early can be read off against the anatomy it becomes.
The pattern is set up in two stages: a **maternal** gradient (the bicoid protein gradient, laid down
before fertilization) is interpreted by **zygotic** gene expression — genes turned on by the embryo
itself reading that gradient. The gene **hunchback** is the one named as reading the bicoid gradient
directly, translating a continuous concentration profile into the discrete body-plan information
carried by the stripes.

## Sources

- Slide deck `lectures/01-notes.pdf` (three converted files), MIT OCW 8.591J/7.81J/9.531J *Systems
  Biology*, Fall 2004, lecturer Alexander van Oudenaarden:
  - `01-7-81j-8-591j-9-531j.md` — course framing, the network-biology definition, the three-level
    roadmap, the central dogma and biomolecule classes, and the opening of the lambda
    lysis/lysogeny story (operator map, promoters).
  - `02-single-repressor-dimer-bound---three-cases.md` — the three single-dimer binding cases at
    $O_R2$/$O_R1$/$O_R3$, the cooperative association constants, UV induction, the cooperativity/Hill
    plots, and the transition into *E. coli* chemotaxis (flagellum, run/tumble, the chemotactic
    pathway diagram).
  - `03-adaptation.md` — the methylation/behavior adaptation experiment and reaction scheme, the
    rest of the roadmap, eukaryotic gradient sensing in *Dictyostelium*, the Min oscillation and
    fission-yeast centering, and the Drosophila bicoid/hunchback preview.
  - No transcript, written notes or problem set were supplied for this lecture; all three slide
    files are flagged in their own frontmatter as a model's reconstruction of a PDF with no text
    layer ("fidelity: reconstructed"), so any numeric or equation-like detail reproduced here should
    be checked against the original slides rather than treated as verified.
- Named but not contained in the supplied material, referred to by the lecture as background or as
  the source of a figure it could not redistribute: Ptashne, M., *A Genetic Switch: Phage Lambda*,
  3rd ed. (Cold Spring Harbor Laboratory Press, 2004) — the lambda switch story in full;
  Alberts et al., *Molecular Biology of the Cell* — the course's suggested general biology
  reference; Mittal, Budrene, Brenner & van Oudenaarden, *PNAS* 100(23):13259–63 (2003) — chemotactic
  aggregation imagery; Falke, Bass, Butler, Chervitz & Danielson, *Annu. Rev. Cell Dev. Biol.*
  13:457–512 (1997) — source figure for the chemotactic pathway diagram; Spiro, Parkinson & Othmer,
  *PNAS* 94(14):7263–8 (1997) — the adaptation model and figure previewed at the end of the
  chemotaxis section.

---

[Contents](index.md) · [2. Cooperativity and the Lambda Switch →](02-cooperativity-and-the-lambda-switch.md)
