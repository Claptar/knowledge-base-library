---
title: "13. Refining and Predicting Protein Structure"
course: "MIT 7.091J"
chapter: 13
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. Refining and Predicting Protein Structure

## What this covers

The previous lecture set up two philosophies for scoring a candidate protein structure — a
physics-based potential energy and a statistics-based (knowledge-based) potential, built from
fixed bond geometry, discrete rotamers and database frequencies. This chapter picks up from there
and asks two questions. First, given a crude or partially correct structure, how do you *refine*
it toward something physically sensible — energy minimization, molecular dynamics, and simulated
annealing/Metropolis sampling? Second, does any of this actually predict structure well, judged by
the field's own blind test (CASP), and how does the knowledge-heavy Rosetta approach compare with
the physics-only approach taken by Anton, D. E. Shaw's special-purpose supercomputer? The chapter
closes by turning the same question-asking habit on protein *interactions*: predicting the effect
of a point mutation on binding, predicting the structure of a complex (docking), and the problem of
reducing an otherwise combinatorial search. It assumes the two energy philosophies from the
previous lecture as background and does not re-derive them.

## Why a structure needs refining before you can score it

Suppose a lab-mate knows the true structure of a protein and won't tell you, but hands you two
candidate structures, one of which is correct. Energy should be lower for the correct one — but
only once every side chain has been placed. If the backbone is right but a side chain is pointed
the wrong way, atoms clash and the energy is spuriously enormous; a sequence placed onto the
*correct* backbone can score worse than one placed onto the wrong backbone, simply because the
side-chain packing was never optimized. So before potential energy is informative about which
structure is right, you first have to solve a smaller problem: given a backbone, find the
side-chain (and in the homology-modelling case, backbone) conformation that minimizes energy.

The harder, more realistic version of the same problem is homology modelling: you have a sequence
homologous to a known structure, and that template is never exactly your protein's structure — the
question is how far off, and how to correct for it. In both cases the task is to move a starting
structure toward a local, and ideally the global, minimum of free energy, by one of three
strategies: energy minimization, molecular dynamics, and simulated annealing.

A caveat worth keeping in view: a stable structure must be *a* local minimum of free energy — if
it weren't, forces would be pushing atoms away from it — but that does not make it *the* global
minimum. Anfinsen's Nobel-winning result, that some proteins fold spontaneously outside the cell,
shows that for those proteins the sequence encodes a structure that is (at least apparently) the
global minimum. Other proteins are now known whose commonly observed structure is only a local
minimum, trapped behind barriers too high to cross unaided, so the true global minimum is never
reached.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A rugged free-energy landscape with a local minimum and a deeper, global minimum separated by a barrier, with the Metropolis path across it">
  <defs>
    <marker id="arrow13" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="currentColor"/>
    </marker>
  </defs>
  <path d="M20,85 L40,100 C60,115 75,140 90,140 C100,140 112,118 125,95 C135,78 148,55 160,50 C180,42 205,95 220,140 C225,155 228,165 230,170 C245,178 270,180 300,178"
        fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="40" cy="100" r="3" fill="currentColor"/>
  <circle cx="90" cy="140" r="3" fill="currentColor"/>
  <circle cx="125" cy="95" r="3" fill="currentColor"/>
  <circle cx="160" cy="50" r="3" fill="currentColor"/>
  <circle cx="230" cy="170" r="3" fill="currentColor"/>
  <text x="34" y="92" font-size="11" fill="currentColor">1</text>
  <text x="84" y="128" font-size="11" fill="currentColor">2</text>
  <text x="130" y="88" font-size="11" fill="currentColor">3</text>
  <text x="165" y="42" font-size="11" fill="currentColor">4</text>
  <text x="236" y="166" font-size="11" fill="currentColor">5</text>
  <text x="55" y="92" font-size="10" fill="currentColor">P=1</text>
  <text x="95" y="112" font-size="10" fill="currentColor">P=e^(-&#916;G/kT)</text>
  <text x="155" y="75" font-size="10" fill="currentColor">P=e^(-&#916;G/kT)</text>
  <text x="195" y="150" font-size="10" fill="currentColor">P=1</text>
  <text x="70" y="158" font-size="11" fill="currentColor">local minimum</text>
  <text x="195" y="198" font-size="11" fill="currentColor">global minimum</text>
  <text x="160" y="212" text-anchor="middle" font-size="12" fill="currentColor">conformation</text>
</svg>
<figcaption>The free-energy surface the lecture drew: a local minimum (point 2) separated from a
deeper, global minimum (point 5) by a barrier. Simulated annealing accepts the downhill moves
(1&#8594;2, 4&#8594;5) with probability 1 and the uphill moves (2&#8594;3, 3&#8594;4) with probability
$e^{-\Delta G/kT}$, which is how it crosses a barrier that pure energy minimization cannot.</figcaption>
</figure>

## 1. Energy minimization

The simplest refinement strategy is literally to minimize the energy function: take the first
derivative and move toward where it is zero. Because the potential energy surface cannot be
written down and solved analytically, this is done by gradient descent — a series of small steps,
each one moving a little further toward the minimum:

$$x_i = x_{i-1} - \varepsilon f'(x_{i-1})$$

for a one-dimensional coordinate, or in $n$ dimensions, using the gradient in place of a single
derivative:

$$\vec{x}_1 = \vec{x}_0 - \varepsilon \nabla U_0(\vec{x}_0), \qquad
\nabla U = \left(\frac{\partial U}{\partial x_1}, \dots, \frac{\partial U}{\partial x_n}\right)$$

Since the force on an atom is the negative gradient of the potential energy, $F = -\nabla U$, this
is the same as

$$\vec{x}_1 = \vec{x}_0 + \varepsilon F_0(\vec{x}_0)$$

so each gradient-descent step is simply a move in the direction of the physical force. This can be
applied to a continuous function of atomic coordinates, or to a discrete optimization over
rotatable bonds (e.g. side-chain torsion angles) with the backbone held fixed.

Gradient descent is fast but is a **local search**. Applied to the misplaced side chain above,
minimization relieves the steric clash — but may simply rotate the side chain 180° into a
different local minimum that removes the clash without recovering the true hydrogen bonds. It
finds *a* nearby minimum, not necessarily the correct one, and can take many iterations with no
guarantee of fast convergence.

## 2. Molecular dynamics

Molecular dynamics tries to simulate what is actually happening to the protein in solution, rather
than just walking downhill on the energy surface. Atoms now carry velocities as well as positions,
updated at each time step from the forces (equivalently, the gradient of the potential):

$$x(t_i) = x(t_{i-1}) + v(t_{i-1}) \times (t_i - t_{i-1})$$
$$v(t_i) = v(t_{i-1}) + \frac{F(t_{i-1})}{m} \times (t_i - t_{i-1})
 = v(t_{i-1}) - \frac{\nabla U(t_{i-1})}{m} \times (t_i - t_{i-1})$$

Because it is an actual simulation of folding, done correctly it should in principle always reach
the right answer. In practice the obstacle is computational cost: folding even a small protein in
vitro can take a millisecond or more, simulating that trajectory atom-by-atom can take many days of
compute time, and modelling solvent explicitly (needed for the hydrophobic collapse that drives
folding) multiplies the cost further, since every water molecule adds degrees of freedom. The
conformational space a simulation can actually explore in available time — its **radius of
convergence** — is set by this budget: for very small proteins with enough computing power you can
reach the folded state from an unfolded one, but in most cases only local changes are tractable.

## 3. Simulated annealing and the Metropolis algorithm

The name is borrowed from metallurgy, where repeatedly raising and lowering a metal's temperature
produces a better atomic structure than cooling it once. The same idea is used here as a **search
strategy**, not a simulation: raising the "temperature" lets the system jump over energy barriers
that pure minimization cannot cross, and lowering it traps a high-probability conformation. It is
explicitly not meant to simulate anything physical — the temperatures used are far outside any
range a real protein would encounter.

At each step the algorithm proposes a neighbouring state — a small perturbation, not a wholesale
change of structure, so that there is continuity between the current and the next state — and
decides whether to accept it using the ratio of Boltzmann probabilities:

$$\frac{P(S_{\text{test}})}{P(S_n)} =
\frac{e^{-E_{\text{test}}/kT}}{Z(T)} \Big/ \frac{e^{-E_n/kT}}{Z(T)} = e^{-(E_{\text{test}} - E_n)/kT}$$

The full algorithm, iterated for a fixed number of cycles or until convergence:

1. Start in state $S_n$ with energy $E_n$.
2. Choose a neighbouring state $S_{\text{test}}$ at random, with energy $E_{\text{test}}$.
3. If $E_{\text{test}} < E_n$, accept it: $S_{n+1} = S_{\text{test}}$.
4. Otherwise accept it anyway with probability $P = e^{-(E_{\text{test}} - E_n)/kT}$; else stay at
   $S_{n+1} = S_n$.

Temperature controls how much of the space gets explored. At very high $T$ the exponent approaches
zero, so $P \to 1$ — almost every uphill move is accepted, which is what lets the search climb over
barriers. At very low $T$, $P \to 0$ — the search almost never goes uphill and behaves like plain
minimization. An annealing schedule starts at high temperature (broad exploration) and lowers it
over time, freezing the system into a high-probability conformation once the barriers have been
crossed. Exactly what schedule to use, and how far away a "neighbouring" state is allowed to be,
is not fixed by the method — it is, as presented, a matter of empirical choice for the problem at
hand.

Stripped of the physical language, this is the **Metropolis (Metropolis–Hastings) algorithm**, a
general way to sample a probability distribution $P(S)$, with no energy or temperature required:

1. Start in state $S_n$.
2. Choose a neighbouring state $S_{\text{test}}$ at random.
3. Compute the acceptance ratio $a = P(S_{\text{test}})/P(S_n)$.
4. If $a > 1$, accept: $S_{n+1} = S_{\text{test}}$.
5. Otherwise accept with probability $a$; else keep $S_{n+1} = S_n$.

The key contrast between the three methods: energy minimization only ever reaches the nearest
local minimum and is fast; molecular dynamics tries to reproduce the physical trajectory and is
computationally very expensive; simulated annealing is a shortcut that can, with some probability,
reach the global minimum by deliberately tolerating uphill moves while they are cheap to accept.

## CASP: a blind test for structure prediction

Many groups have proposed methods for predicting structure from sequence, but comparing them
fairly requires not knowing the answer in advance. In 1995 the **CASP** project (Critical
Assessment of techniques for protein Structure Prediction) set up exactly this blind test:
structures were solicited from crystallographers and NMR spectroscopists who had solved them, or
expected to, but had not yet published — information on 33 proteins was obtained, and predictions
were eventually received for 24. Sequences went to modellers before anyone knew the answer,
predictions were collected, and only afterward compared against the real structures. CASP has run
as a recurring competition since, which is what makes it possible to ask whether prediction has
actually improved over time.

## Rosetta: homology and de novo modelling

One of the methods that has consistently performed well in CASP is **Rosetta**. It splits the
prediction problem into two cases: where a reasonable **homology** template exists in the database
of known structures (even at very low sequence identity), and the **de novo** case, where nothing
detectably homologous exists.

**Homology modelling** starts by aligning the query sequence to sequences of known structure, using
several different alignment methods rather than committing to one — carrying multiple alignments
through the refinement process rather than betting everything on a single one. Templates are split
into three bands of difficulty:

- **High similarity** (>50% sequence identity): the template is already close to correct, so
  refinement is minimal, focused only on regions where the alignment is poor.
- **Medium similarity** (20–50%): several alignments are carried through refinement in parallel,
  and the best model is chosen by its final energy. Refinement concentrates on regions with gaps
  and insertions, loops in the starting model, and segments with low sequence conservation —
  places where the alignment is least trustworthy. In these regions, backbone torsion angles are
  replaced with those of a short peptide (roughly 3–9 residues) pulled from the database of known
  structures with the same local sequence, even if that peptide comes from an otherwise unrelated
  protein; the local structure is then minimized, followed by refinement of the global structure.
- **Low similarity** (<20%): many more starting models are used, and refinement is more aggressive
  — it rebuilds secondary structure elements as well, not only the gaps, loops and poorly conserved
  regions handled in the medium case, since even well-defined elements of the template may be
  wrong.

The general refinement procedure underlying all three bands: random perturbation of backbone
torsion angles, rotamer optimization of side chains (choosing among the discrete, frequently
observed rotamers before any continuous optimization), and energy minimization of torsion angles
with bond lengths and angles held fixed.

**de novo modelling** (no usable template) proceeds by Monte Carlo search over backbone angles: a
short region (3–9 residues) has its torsion angles set to match a similar peptide found in the
database, accepted or rejected by the Metropolis criterion above. This runs for 36,000 Monte Carlo
steps, repeated to produce 2,000 final structures, which are clustered and each cluster refined —
reflecting low confidence in any single trajectory. Homology modelling tends to converge on one
plausible answer; de novo more often produces several equally plausible clusters.

## Has prediction accuracy actually improved?

Comparing CASP10 against CASP5, a decade earlier: the **percentage of residues correctly modelled
where no template existed** improved substantially — CASP9 and CASP10 do markedly better than CASP5
on harder targets, where "target difficulty" is defined from the structural and sequence similarity
of a target to proteins of known structure. But **overall prediction accuracy**, measured by the
**Global Distance Test (GDT_TS)** — the average percentage of $\text{C}\alpha$ atoms in a prediction
close to the corresponding atoms in the true structure, roughly 90–100 for a perfect model and
20–30 for a random one — did *not* improve over the same decade: the CASP10 trend line across
target difficulty is close to the CASP5 one. One explanation offered is that target difficulty, as
defined, may not be a fair measure: later CASP targets are more often multi-domain or multi-chain,
so their fold may depend on interaction with partners not given to the predictor, rather than being
fully determined by sequence alone.

**Free modelling** (de novo, no homology at all) shows no clear trend either: CASP10 and CASP5
trend lines are close, and CASP9 looks almost identical to CASP5. Looking only at short targets
(<120 residues) by GDT, CASP9 did unusually well (5 of 11 above 60), CASP10 was mediocre (three
above 60, four below 40), and CASP5 managed only 1 of 5 above 60 — fluctuating rather than
trending. The cited explanation is that current free-modelling methods work best on single-domain,
regular structures, and CASP10 targets had become more irregular and more often domains of larger
proteins whose conformation depends on the rest of the structure, rather than being recoverable
from sequence alone.

## The physics-only alternative: Anton

Rosetta leans on every piece of prior knowledge available — homology, peptide fragments pulled
from the database, and a potential energy function mixing physically grounded terms with terms
that are just curve-fit to reproduce what is observed in nature (e.g. keeping hydrophobic residues
buried). The purely physics-based alternative rejects this: no homology, no borrowed fragments,
only physical forces, simulating the actual in vitro folding process for every protein.

The obstacle to doing this at scale is computational: these energy landscapes are extremely rugged,
and getting to the correct structure means crossing many local minima — fundamentally a
computing-power problem. The D. E. Shaw group's answer was special-purpose hardware: **Anton**, a
supercomputer with chips that compute pieces of the potential energy function — electrostatics, van
der Waals — directly in hardware, making each energy evaluation far faster and letting simulations
run far longer in real time (Lindorff-Larsen et al., *Science*, 2011). The structures it has
successfully folded this way are small and dominated by well-defined secondary structure — mostly
$\alpha$-helices, which (consistent with crude secondary-structure algorithms already getting
$\alpha$-helix content roughly right) encode more structural information locally than $\beta$-sheets
do, whose pairing depends on which other strand it ends up next to. This is read as a limit of
current computing speed, not of the physics-only approach: larger, more $\beta$-sheet-rich
structures were being tackled in later work.

A third approach worth naming without belonging to either camp: **FoldIt**, a video game in which
human players manipulate candidate structures by hand, leveraging the same pattern-recognition
skill humans bring to other visual problems. In a reported match, players outperformed the best
available software on a set of ten proteins.

## Predicting protein interactions

The lecture turns from single proteins toward proteins interacting with each other, as a bridge
toward later lectures on networks. Three separate prediction problems were posed:

1. Predict the effect of a point mutation on the stability of an already-known complex.
2. Predict the structure of a complex (docking) from the structures of its two partners.
3. Predict, genome-wide, which proteins interact with which.

### Predicting the effect of point mutations

This looks like the easiest of the three: you know the structure of the complex, you know where
the mutation is, and you just need to say whether it strengthens or weakens binding. A
community-wide evaluation (Moretti et al., *Proteins*, 2013) tested this directly: participants
were given the structures of two complexes (HB36 and HB80, each bound to HA), with all possible
single-point mutations introduced at 53 and 45 positions respectively, the proteins expressed on
yeast, and a high-throughput sequencing-based assay used to estimate the resulting change in
binding affinity. Before a mutant's energy can even be evaluated, the side-chain conformation at
the mutated position has to be re-optimized — otherwise the computation is dominated by spurious
steric clashes, exactly the same subtlety raised at the start of the chapter.

The results were not encouraging. Even the **top-performing** submission — looking only at
mutations right at the interface, where structural information should help most — was clearly
better at flagging mutations that reduce binding (deleterious) than at identifying mutations that
improve it, and an average group did markedly worse than the top one. To judge this objectively,
the paper compared predictions against a baseline using no structural information: scoring each
mutation by its **BLOSUM substitution matrix** value (roughly −4 to 11) and varying the cutoff to
trace a true-positive/false-positive curve, summarized by the area under it (1 for perfect, 0.5 for
random). The best energy-based method beat the BLOSUM baseline only marginally — the best groups
were only about three times better than random assignment, and mutations at polar positions were a
particular weak point.

What distinguished the better-performing approaches was modelling binding as more than a single
equilibrium between free proteins and complex. A mutation can also shift the stability of the
*unfolded* state of the protein being mutated, so the relevant equilibrium is really

$$\text{unfolded} \rightleftarrows \text{A} + \text{B} \rightleftarrows \text{AB}$$

for the wild type, and the corresponding chain with the mutant ($\text{B}^*$, $\text{AB}^*$) for the
mutant — and approaches that ignored the unfolded-state term did worse. The better-performing
groups also explicitly modelled packing, electrostatics and solvation, but the specific algorithms
used were a genuine mix: machine learning (the groups labelled G21, Fernandez-Recio; and G05s,
Bates), atom-level energy functions (G15, Weng), and coarse-grained models (G21s, Dehouck) — no
single common approach stood out.

One of the better methods, **G21**, illustrates the machine-learning route: it assembled a
database of 930 (mutation, $\Delta\Delta G$) pairs from the literature, unrelated to the proteins in
the challenge; predicted the mutant structure with an existing tool (FoldX); described each mutant
with 85 features from other programs (including PyRosetta, FireDock, PyDock, SIPPER, CHARMM, and
solvent-accessibility measures); and trained five classifiers (random forest, decision table,
Bayesian net, logistic regression, alternating decision tree), combining their outputs and
validating by cross-validation. That this all-of-the-above approach still only modestly beats a
substitution matrix is itself the point: quantitative prediction of binding-affinity change from
structure is still largely unparametrized.

### Predicting the structure of a complex: docking

Rather than asking for a precise energy change, a cruder question may be more tractable: which two
proteins interact at all, and which surfaces are involved? Solving this directly — for every
potential partner, searching all relative positions and orientations, allowing structural
rearrangement at each, and evaluating the interaction energy — is far too slow at scale, and is
also prone to false positives (a plausible-looking low-energy arrangement that is not the real
interaction). So practical methods reduce the search space: using prior knowledge of known
interfaces to restrict which residues are examined, or asking what role structural homology plays
in choosing candidate partners.

Structural homology can help more locally than expected: even when two proteins interacting with a
common partner are *not* globally similar, the regions that actually contact the partner can still
be structurally conserved. The globally unrelated inhibitors **chymotrypsin inhibitor 2** and
**eglin C** both bind **subtilisin** at the same local site as a third, more structurally similar
inhibitor — local similarity at the interface can hold even where global fold similarity does not.

A further refinement: not every interface residue contributes equally to binding. In the
growth-hormone/receptor complex (hGH/hGHbp), studied by substituting each contact residue with
alanine and measuring the change in binding free energy (Clackson & Wells, 1995), fewer than 10% of
interface residues contribute more than 2 kcal/mol — the **hot spots**. These are enriched for
tryptophan, arginine and tyrosine, sit in pockets on both proteins with complementary shape and
charge/hydrophobicity, can include buried charged residues far from solvent, and are often
surrounded by an "O-ring" of residues that excludes solvent from the interface.

## What this points toward

The lecture closes by naming, rather than developing, what comes next: template-based docking
combined with flexible refinement to predict complex structure (Tuncbag, Keskin, Nussinov and
Gursoy), and extending structure-based interaction prediction to a genome-wide scale (Zhang et
al.). The thread connecting both: once pairwise, atom-level prediction is this hard, the field
increasingly asks the cruder but more tractable question of which proteins interact at all — the
route toward the network-level material later in the course.

## Sources

- Slides: `lectures/13-slides/01-predicting-protein-structure.md` — statisticians vs. physicists
  recap, threading, the three refinement methods with their equations, CASP1, Rosetta's homology
  and de novo categories, CASP10-vs-CASP5 figures and GDT_TS, Anton/D. E. Shaw.
- Slides: `lectures/13-slides/02-de-shaw.md` — Anton hardware and the Lindorff-Larsen et al. 2011
  fast-folding-proteins table, FoldIt news coverage, the point-mutation challenge (Moretti et al.
  2013, HB36/HB80 complexes).
- Slides: `lectures/13-slides/03-13-slides-part-03.md` — BLOSUM baseline and AUC comparisons, G21,
  the unfolded-state equilibrium, docking, subtilisin/inhibitor example, hotspots (Clackson &
  Wells 1995), next-lecture pointers (Tuncbag et al., Zhang et al.).
- Transcript: `recordings/lectures/13.md`, throughout — the side-chain/energy motivating example
  (00:00–06:38); the three refinement methods with worked reasoning and class Q&A (06:38–26:01);
  CASP history and the Rosetta walkthrough, including the Twilight Zone remark and the rationale
  for 3–9-residue fragments (26:01–39:03); the CASP5/9/10 comparison and its proposed explanations
  (39:03–44:29); the physics-vs-statistics framing of Rosetta vs. Anton and why small, alpha-helical
  proteins are where Anton succeeds (44:29–48:45); and the full discussion of the mutation-effect
  challenge, BLOSUM baseline, G21, and docking/hotspots (48:45–end).
- Named but not contained in the supplied material: the molecular-dynamics folding movie shown in
  class; the "good tutorial" on side-chain restoration referenced on the slides; the external
  lecture notes on modelling binding equilibria linked from the slides (`20.320`, Fall 2012,
  "Modeling and Manipulating Biomolecular Interactions"); the Anfinsen folding result (named, not
  detailed); specific annealing-schedule choices (acknowledged in the transcript as a matter of
  practice, not something the lecture specifies).

---

[← 12. Protein Structure and Energy Functions](12-protein-structure-and-energy-functions.md) · [Contents](index.md) · [14. Predicting Protein Interactions →](14-predicting-protein-interactions.md)
