---
title: "6. Excitation and Adaptation in Chemotaxis"
course: "MIT 8.591J 2004"
chapter: 6
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. Excitation and Adaptation in Chemotaxis

## What this covers

This chapter follows the lecture that introduces the Spiro–Parkinson–Othmer (1997) model of
excitation and adaptation in *E. coli* chemotaxis. The receptor complex at the heart of the model can
be modified in three independent ways at once — ligand binding, phosphorylation, methylation — so the
"obvious" chemotaxis diagram is really a lattice of dozens of distinct chemical species. The chapter
asks two questions the lecture answers in turn: what assumptions cut that lattice down to something
tractable, and how does the resulting model account for the experimental fact that a cell's tumbling
frequency snaps down when attractant is added and then, over about a minute, climbs back to baseline
even though the attractant never leaves? It assumes the two-component chemotaxis pathway (Tar, CheA,
CheW, CheB, CheR, CheY, CheZ) from the preceding lecture.

## The receptor complex and its three switches

The key player is the **Tar–CheA–CheW complex**: the aspartate receptor Tar, permanently bound to the
histidine kinase CheA and its adaptor CheW. At any moment, three things can vary independently for one
copy of this complex:

- **ligand binding** — aspartate bound ($LT$) or not ($T$);
- **phosphorylation** — CheA has autophosphorylated, handing a phosphate onto the complex ($T_\text{p}$),
  or not;
- **methylation** — how many of the receptor's methylation sites carry a methyl group.

Downstream, whichever phosphorylated species it is, the complex passes its phosphate on the same way:
to CheY, giving $\text{CheY}_\text{p}$, which drives the flagellar motor toward clockwise rotation
(tumbling), and to CheB, giving $\text{CheB}_\text{p}$; CheZ then strips the phosphate back off
$\text{CheY}_\text{p}$. Three independent binary/graded modifications on the receptor itself, feeding a
common phosphorylation network downstream, is exactly the structure drawn in Figure 2 of Spiro et al.:

<figure>
<svg viewBox="0 0 460 250" role="img" aria-label="Lattice of receptor-complex states differing by methylation level, ligand binding, and phosphorylation">
  <line x1="90" y1="90" x2="300" y2="90" stroke="currentColor" stroke-width="1.2"/>
  <line x1="90" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="90" y1="90" x2="90" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="190" y1="90" x2="190" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="300" y1="90" x2="300" y2="170" stroke="currentColor" stroke-width="1.2"/>

  <line x1="140" y1="45" x2="350" y2="45" stroke="currentColor" stroke-width="1.2"/>
  <line x1="140" y1="125" x2="350" y2="125" stroke="currentColor" stroke-width="1.2"/>
  <line x1="140" y1="45" x2="140" y2="125" stroke="currentColor" stroke-width="1.2"/>
  <line x1="240" y1="45" x2="240" y2="125" stroke="currentColor" stroke-width="1.2"/>
  <line x1="350" y1="45" x2="350" y2="125" stroke="currentColor" stroke-width="1.2"/>

  <line x1="90" y1="90" x2="140" y2="45" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="190" y1="90" x2="240" y2="45" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="300" y1="90" x2="350" y2="45" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="90" y1="170" x2="140" y2="125" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="190" y1="170" x2="240" y2="125" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="300" y1="170" x2="350" y2="125" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>

  <text x="90" y="80" text-anchor="middle" font-size="12" fill="currentColor">T2</text>
  <text x="190" y="80" text-anchor="middle" font-size="12" fill="currentColor">T3</text>
  <text x="300" y="80" text-anchor="middle" font-size="12" fill="currentColor">T4</text>
  <text x="90" y="184" text-anchor="middle" font-size="12" fill="currentColor">LT2</text>
  <text x="190" y="184" text-anchor="middle" font-size="12" fill="currentColor">LT3</text>
  <text x="300" y="184" text-anchor="middle" font-size="12" fill="currentColor">LT4</text>

  <text x="140" y="35" text-anchor="middle" font-size="12" fill="currentColor">T2p</text>
  <text x="240" y="35" text-anchor="middle" font-size="12" fill="currentColor">T3p</text>
  <text x="350" y="35" text-anchor="middle" font-size="12" fill="currentColor">T4p</text>
  <text x="140" y="139" text-anchor="middle" font-size="12" fill="currentColor">LT2p</text>
  <text x="240" y="139" text-anchor="middle" font-size="12" fill="currentColor">LT3p</text>
  <text x="350" y="139" text-anchor="middle" font-size="12" fill="currentColor">LT4p</text>

  <text x="10" y="208" font-size="12" fill="currentColor">horizontal = methylation</text>
  <text x="10" y="224" font-size="12" fill="currentColor">vertical = ligand binding</text>
  <text x="10" y="240" font-size="12" fill="currentColor">dashed diagonal = phosphorylation</text>
</svg>
<figcaption>The receptor complex's state space: three highest methylation levels (2, 3, 4) times
bound/unbound times phosphorylated/not. Every phosphorylated state (front layer) feeds the same
phosphotransfer step to CheY and CheB, not drawn here.</figcaption>
</figure>

## Eight assumptions that make the lattice tractable

Left unconstrained, three independent modifications compound into a large reaction network. The
lecture's model is built on eight simplifications, each removing one source of bookkeeping:

1. **Tar is the only receptor type, and CheW and CheA are always bound to Tar** — so a complex's whole
   identity is its $(T/LT,\ \text{methylation level},\ \text{p or not})$ triple; there is no separate
   free-CheA or free-CheW population to track.
2. **Methylation happens in a specific order** — the receptor's methylation sites fill and empty one at
   a time along a single sequence, rather than in any of the many possible orders.
3. **Only the three highest methylation states matter** — labelled 2, 3 and 4 in the diagram above,
   rather than the full range the receptor could in principle occupy.
4. **Only $\text{CheB}_\text{p}$ demethylates** — demethylation is tied to CheB's own phosphorylation
   state, so the methylation dynamics inherit whatever happens to $\text{CheB}_\text{p}$.
5. **Phosphorylation of CheA does not affect ligand (un)binding** — the ligand-binding equilibrium is
   the same whether or not the complex is phosphorylated.
6. **CheR binding to the complex does not affect ligand (un)binding or phosphorylation of CheA** — the
   methylation machinery does not itself perturb the other two axes.
7. **CheZ is not regulated** — $\text{CheY}_\text{p}$ dephosphorylation runs at a fixed rate, not
   modulated by the signal.
8. **Phosphotransfer from the complex to CheY or CheB does not depend on occupancy or methylation
   state** — whichever phosphorylated species handed off the phosphate, it does so at the same rate.

Assumptions 5, 6 and 8 in particular decouple the three axes from each other wherever they can, which
is exactly what turns a network on three interacting modifications into the separable lattice drawn
above: a grid of methylation and ligand-binding states, one copy phosphorylated and one not, connected
by the same phosphotransfer step regardless of which grid point it started from.

## Two asymmetries hidden in the kinetics

Decoupling the axes does not make the complex's biochemistry symmetric along each of them. The lecture
singles out three rate asymmetries — read directly off Figure 2 — that are exactly what drives the
model's dynamics:

- **Ligand-bound states generally have lower autophosphorylation rates** than unbound states at the
  same methylation level: binding aspartate makes the kinase worse at its job.
- **CheR methylates ligand-bound states more rapidly** than unbound ones.
- **Higher methylation states autophosphorylate more easily** than lower ones, at the same
  ligand-binding status: methylation makes the kinase better at its job, in the opposite direction to
  binding.

Put together: binding aspartate suppresses autophosphorylation, but it also accelerates methylation,
and methylation itself restores autophosphorylation. That closed loop — one modification undermining
kinase activity, the other, slower one restoring it — is the whole mechanism of adaptation.

## A step in aspartate, on three timescales

The lecture walks through what happens to the population of complexes after a step increase in
aspartate concentration, and the three timescales involved are well separated:

- **$\sim 1\ \text{ms}$**: ligand binding is fast, so the ligand-bound fraction $[LT]$ jumps up almost
  immediately.
- **$\sim 5\ \text{s}$**: because ligand-bound complexes autophosphorylate poorly, the total number of
  phosphorylated complexes now falls gradually — $\text{CheA}_\text{p}$ drops, and with it
  $\text{CheB}_\text{p}$. Low $\text{CheA}_\text{p}$ means low $\text{CheY}_\text{p}$: tumbling is
  suppressed. This is **excitation**.
- **$\sim 50\ \text{s}$**: with $\text{CheB}_\text{p}$ now low, demethylation is effectively switched
  off (assumption 4: only $\text{CheB}_\text{p}$ demethylates), while ligand-bound complexes are being
  methylated faster than usual. Methylation climbs, slowly and unopposed. $\text{CheA}_\text{p}$ and
  $\text{CheY}_\text{p}$ stay low for now — tumbling is still suppressed.
- **Longer still**: because higher methylation states autophosphorylate more easily, the now
  more-heavily-methylated population slowly regains its ability to autophosphorylate even with the
  ligand still bound. $\text{CheA}_\text{p}$ and $\text{CheY}_\text{p}$ climb back to their original
  levels, and tumbling returns to its pre-stimulus frequency. This is **adaptation**.

<figure>
<svg viewBox="0 0 420 240" role="img" aria-label="Kinase activity dropping fast and recovering slowly after a step increase in attractant, while methylation rises slowly underneath it">
  <line x1="40" y1="200" x2="390" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <polygon points="390,200 380,196 380,204" fill="currentColor"/>
  <text x="395" y="215" font-size="12" fill="currentColor">time</text>

  <line x1="110" y1="18" x2="110" y2="205" stroke="currentColor" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="112" y="14" font-size="12" fill="currentColor">aspartate step</text>

  <path d="M40,60 L110,60 C130,60 140,150 150,150 C220,150 300,80 370,60" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <path d="M40,190 L110,190 C160,190 200,175 230,150 C280,120 330,105 370,100" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="1,3"/>

  <text x="215" y="72" font-size="12" fill="currentColor">CheA-P, CheY-P, tumbling</text>
  <text x="255" y="145" font-size="12" fill="currentColor">methylation level</text>

  <text x="150" y="222" text-anchor="middle" font-size="11" fill="currentColor">~5 s</text>
  <text x="300" y="222" text-anchor="middle" font-size="11" fill="currentColor">~50 s</text>
</svg>
<figcaption>Fast excitation, slow adaptation: kinase activity (solid) falls within seconds of the
attractant step and climbs back to baseline over tens of seconds, driven by the slower rise in
methylation (dashed) underneath it.</figcaption>
</figure>

The whole point of the mechanism is that the two responses are on different clocks. The fast
phosphorylation response is what lets the cell react to a change at all; the slow methylation response
is what lets the same cell stop reacting once it has adjusted, so that a persistent stimulus does not
leave it tumbling — or not tumbling — forever. That return to baseline in the presence of a still-bound
ligand is what "adaptation" means here.

## Where the lecture leaves it

The slide carrying this model is titled "fine-tuned model for perfect adaptation" — a name that
concedes the model reaches perfect adaptation only for particular parameter choices, not as a
structural guarantee. The lecture closes by pointing at Barkai and Leibler's 1997 "Robustness in simple
biochemical networks" as the contrasting case: a model in which adaptation does not need to be tuned.
The figures making that comparison were not available in this material (see Sources); working out
exactly what "fine-tuned" is buying, and whether it can be removed, is where the following lecture
picks up.

## Sources

- Slide deck: `08-notes.md` (MIT OCW 8.591J, Fall 2004, lecture 8), reconstructed by a model from a
  PDF with no text layer — treat the prose as paraphrase and every equation as unverified. Covers: the
  Tar–CheA–CheW complex and its title slide; the eight numbered modelling assumptions; the
  autophosphorylation/methylation rate asymmetries; the timed walkthrough of the response to a step in
  aspartate ($\sim 1\ \text{ms}$, $\sim 5\ \text{s}$, $\sim 50\ \text{s}$); the closing reference to
  Barkai and Leibler (1997).
- Figures extracted from the same source PDF: page 2 (the MCP/CheA/CheB/CheY/CheZ reaction scheme),
  page 4 (the state lattice reproduced above as an SVG), and page 11 (Figure 4 of Spiro et al.,
  simulated $\text{CheA}_\text{p}$/$\text{CheB}_\text{p}$/methylation and tumbling-probability
  timecourses, redrawn schematically above rather than reproduced).
- No transcript, written notes, or exercise sheet was supplied for this lecture.
- Named but not contained: the primary source, Spiro, P. A., Parkinson, J. S., and Othmer, H. G.,
  "A model of excitation and adaptation in bacterial chemotaxis," *PNAS* 94, no. 14 (1997): 7263–8,
  cited throughout via its figures rather than reproduced in full; and Barkai, N. and Leibler, S.,
  "Robustness in simple biochemical networks," *Nature* 387, no. 6636 (1997): 913–7, whose Figures 2
  and 3 were referred to on the closing slides but removed from the converted material for copyright
  reasons.

---

[← 5. Mathematical basis of stability analysis](05-mathematical-basis-of-stability-analysis.md) · [Contents](index.md) · [7. Perfect Adaptation by Model Reduction →](07-perfect-adaptation-by-model-reduction.md)
