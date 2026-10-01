---
title: "12. Protein Structure and Energy Functions"
course: "MIT 7.091J"
chapter: 12
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Protein Structure and Energy Functions

## What this covers

This chapter opens the course's unit on protein structure. It asks how a structure is represented
and compared once you have one, and how you would find one — by writing down a potential energy
function and asking what the lowest-energy shape of a given sequence is. It assumes the reader
already knows the vocabulary of protein structure (primary/secondary/tertiary structure, helices,
sheets, amino acids) from outside reading the lecture points to but does not repeat. It stops just
before the next lecture's three optimization techniques — energy minimization, molecular dynamics,
simulated annealing — named here only as what comes next.

## Why structure, not just sequence

The lecturer's working variant of "nothing in biology makes sense except in the light of evolution"
is that little in biology makes sense except in the light of structure. The example given is p53,
the gene most often mutated in cancer (found mutated in about half of all tumors). Before sequencing
tumors was cheap, researchers already knew p53 mutations cluster along the sequence, in a pattern
secondary structure alone did not explain — some clustered residues sat in regular secondary
structure, some did not. The clustering stayed an enigma until the three-dimensional structure of
p53 bound to DNA was solved (at MIT, by Carl Pabo and his postdoc Nikola Pavletich): every
frequently-mutated residue turned out to sit at the protein–DNA interface, so these mutations
disrupt the transcriptional regulation p53 exists to carry out. One picture settled a question that
had stood open for years.

## Where structures come from

Most solved structures come from X-ray crystallography (on the order of 80,000 by this lecture), a
much smaller number from NMR (on the order of 10,000), and only hundreds from every other technique
combined. Neither hands you a structure directly. In **X-ray crystallography**, a crystal of the
protein, grown in solution and barely visible to the eye, is hit with a high-powered X-ray beam;
most X-rays pass straight through, but the small fraction that diffract produce a pattern from which
the *electron density* can be computed. Finding atomic positions that reproduce that density — and
in turn the observed diffraction pattern — is solved iteratively: propose a structure, predict its
diffraction pattern, compare to what was observed, refine, all while keeping the structure consistent
with physics (fixed bond lengths and angles), not only with the data. **NMR** needs no crystal, only
a highly concentrated soluble sample, and yields not electron density but *distances* between pairs
of atoms (usually protons); the computational problem has the same shape: find a structure
consistent with the measured distances and with physical forces.

So solving a crystal or NMR structure is already a hard computational problem — just not the one
this unit takes on. The harder problem tackled here is **de novo prediction**: starting from
sequence alone, with no crystal and no NMR data. Several things make it hard. The search space is
continuous rather than discrete, so part of the work is reducing it back to something discrete.
Physical knowledge cannot be abstracted away as it could be in earlier, sequence-level problems in
this course. And there is no simple map from sequence to structure: homologs can keep the same fold
down to 20–30% sequence identity, sometimes as low as 4%, and proteins with no detectable
evolutionary relationship ("analogs") can converge on the same structure anyway — so this is not a
lookup against a discrete catalogue of known folds, but in principle a search over an infinite space
of chain conformations.

## Describing a structure: two coordinate systems

**Cartesian (XYZ) coordinates.** A PDB file records, for every atom, a line beginning `ATOM`, an
index, the atom type, the chain, the residue number, and then the atom's $x,y,z$ coordinates,
followed by two further numbers describing how confident the structure is at that atom, not where
it is:

- **occupancy** (0 to 1) — a crystal is many repeating copies of the molecule, and if a side chain
  sits in more than one discrete position across those copies, occupancy splits between them (e.g.
  0.5 and 0.5); occupancy 1 means a single dominant conformation;
- the **B-factor** (thermal factor), capturing continuous thermal motion rather than discrete
  alternatives — low values (the lecture's example: 20) mark rigid, usually buried positions, high
  values (the lecture's example: 80) mark flexible ones, typically at chain ends.

XYZ coordinates are precise but not unique (a structure can be rotated and translated freely without
changing it) and not concise: bond lengths and angles barely deform in real proteins, so specifying
every atom's absolute position spends most of its degrees of freedom on things that are effectively
fixed.

**Internal coordinates** exploit exactly that. The peptide bond between one residue's carbonyl
carbon and the next residue's amide nitrogen is planar, so the angle across it ($\omega$) is fixed
and need not be given at all; what does rotate are two backbone dihedral angles per residue, $\phi$
and $\psi$, so the whole backbone reduces to two numbers per amino acid. Side chains are described
the same way, by the rotation of their own rotatable bonds ($\chi$ angles) rather than by every
atom's position.

## Comparing two structures: RMSD

Comparing two structures — the same molecule solved twice, or two homologs — needs a correspondence
between atoms (trivial for one molecule solved twice; a real choice for two different proteins,
where you might restrict to heavy atoms or to backbone atoms only, depending on whether side-chain
placement matters for the question) and a rigid-body rotation and translation of one onto the
other, chosen to minimize

$$\mathrm{RMSD} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}\left[(x_i-x_i')^2+(y_i-y_i')^2+(z_i-z_i')^2\right]}$$

the root mean square deviation between corresponding atoms. Whether to include side chains or
protons is a choice driven by the question: deciding whether two proteins share a fold might only
need backbone atoms, while checking a predicted structure against an experimental one, atom for
atom, needs every atom.

## A structure is really structures

Molecules move continuously, and some proteins — especially those doing mechanical work — have more
than one well-defined structure they move between, so "the" structure of a protein is already an
approximation. What picks out a structure is physics: a stable structure is a minimum of the
potential energy, since force is the negative derivative of potential energy and at equilibrium
there is no net force. A protein with several functional conformations simply has several minima. If
the potential energy function $U$ were known exactly, the structure(s) of a protein would just be
the minima of $U$ — the rest of this chapter is about how $U$ gets written down.

## The potential energy function: two ways to write it down

The lecture frames this as two attitudes to the same problem, "the physicist" and "the
statistician," via a joke about an Institute for Quantum Mechanics whose map says "you could be
here, or here" (the physicist's irreducible uncertainty), against the statistician's version,
"data don't make sense, we'll have to resort to statistics." The physicist writes equations
approximating the real physical forces, where possible tied to an identifiable physical principle.
The statistician writes whichever function best reproduces what is observed in known structures,
regardless of whether it corresponds to any specific force. The two often agree, because a good
physical approximation and a good statistical fit to the same data can converge on the same form —
but not always.

### The physicist's terms: CHARMM

CHARMM, the lecture's example of the physicist's approach (one of the methods recognized by a
recent Nobel Prize in Chemistry), splits potential energy into **bonded** terms, between atoms
connected through a small number of bonds, and **non-bonded** terms, between atoms close in space
but not directly connected.

The simplest bonded term treats a bond length as a stiff spring:

$$U_{\text{bond}} = k_b\,(b - b_0)^2$$

where $b_0$, the equilibrium length for that pair of atom types, is measured across many
high-resolution small-molecule crystal structures, and $k_b$ penalizes deviation from it — a
quantum-mechanical quantity approximated cheaply. Further bonded terms constrain the angle between
two bonds and the dihedral geometry of groups of four atoms (including keeping backbone $\phi,\psi$
consistent with quantum mechanics, corrected for small deviations seen in real small molecules) — a
large catalogue of terms and parameters, each motivated by some underlying quantum principle even
where only approximated.

The non-bonded terms are two further forces. The **Lennard-Jones (van der Waals)** potential
combines an attractive $-1/r^6$ term (induced dipole–dipole attraction) with a repulsive $+1/r^{12}$
term (a cheap stand-in for the quantum-mechanical exclusion that keeps atoms from overlapping — cheap
because it is just the square of the $1/r^6$ term already computed). The **electrostatic** term is
Coulomb's law, proportional to the product of the two charges divided by distance, scaled by a
dielectric constant representing how much the medium screens the interaction — about 1 in vacuum, up
to about 80 in water, with the right value for a given calculation something of an art.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Combined van der Waals and electrostatic potential energy as a function of distance between two atoms, showing a steep repulsive wall at short range and a shallow attractive minimum further out">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="20" x2="40" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="120" x2="300" y2="120" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>
  <path d="M 58,25 C 75,70 85,110 100,140 C 112,160 130,172 155,166 C 180,160 200,145 220,132 C 245,117 270,113 295,112"
        fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="155" y1="120" x2="155" y2="166" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2" opacity="0.6"/>
  <text x="300" y="205" text-anchor="end" font-size="12" fill="currentColor">distance r</text>
  <text x="30" y="25" text-anchor="end" font-size="12" fill="currentColor">U</text>
  <text x="155" y="182" text-anchor="middle" font-size="11" fill="currentColor">r_min</text>
  <text x="65" y="40" text-anchor="start" font-size="11" fill="currentColor">repulsive (r⁻¹²)</text>
  <text x="235" y="100" text-anchor="start" font-size="11" fill="currentColor">attractive (r⁻⁶)</text>
</svg>
<figcaption>The sum of the Lennard-Jones and electrostatic terms: energy rises sharply as atoms are
pushed closer than their equilibrium separation, and falls into a shallow minimum at the optimal
distance before leveling off at long range.</figcaption>
</figure>

### The statistician's terms: Rosetta

Rosetta fixes bond lengths and tetrahedral bond angles at their typical values and never lets them
deform, since real deformation is negligible anyway, so the whole search is over rotatable bonds:
$\phi,\psi$ in the backbone and one or more $\chi$ angles per side chain (one for cysteine, since
only the bond to its sulfur matters; more atoms out along a side chain give $\chi_2,\chi_3$, and so
on).

Even so, rotation is not free: plotting a side chain's observed $\chi$ angles across many crystal
structures gives a highly non-uniform distribution, because some rotations create steric clashes
between atoms on either side of the bond while an offset rotation avoids them, and that propagates
through the whole side chain. The preferred angles are **rotamers** (rotational isomers), turning
a continuous rotation into a discrete choice among a handful of favored options.

With geometry fixed and rotation discretized, Rosetta still needs a potential energy function, built
statistically rather than from quantum mechanics: take many high-resolution crystal structures,
measure how often a geometric property (e.g. the distance between a pair of atom types) takes each
value, and convert that frequency into an energy via Boltzmann's law — the probability of a state
treated as a function of the logarithm of its observed frequency, relative to some reference state
that the lecture flags as itself not straightforward to define, naming it as a question for the
references rather than resolving it in class. Several terms are built this way:

- a **van der Waals-like term** (`fa_atr`/`fa_rep`), shaped like the Lennard-Jones curve but fit
  directly to observed atomic distances rather than derived from dipole physics;
- a **hydrogen-bonding term**, fit separately for backbone versus side-chain partners and for
  partners close together versus far apart along the chain — a split with no physical principle
  behind it, purely because it fits the data better;
- a term built from the **Ramachandran plot** (below), rewarding frequently-observed $\phi,\psi$
  combinations and penalizing rare ones, rather than deriving why helices and sheets form;
- a **rotamer term**, rewarding the staggered, frequently-observed $\chi$ conformations directly,
  rather than deriving the preference from steric repulsion;
- a **solvation term** — the clearest case of the statistician winning out. Burying hydrophobic
  residues is one of the dominant forces shaping structure, but very hard to derive from first
  principles: water itself is hard to simulate from first principles (even getting simulated water
  to freeze was achieved only a few years before this lecture), because water near a non-polar
  surface cannot hydrogen-bond with it and must rearrange to keep hydrogen-bonding with itself.
  Instead, the statistical term starts from measured transfer free energies — how an atom's energy
  changes moving from a non-polar to a polar solvent, measured directly by experiment — and corrects
  that value by how much surrounding volume is occupied by neighboring atoms, since even a surface
  residue is partly shielded by bulky neighbors. No water and no quantum mechanics are simulated; the
  correction is purely geometric.

Each term is fit independently and then weighted against the others to produce reasonable
structures overall — itself a curve-fitting exercise checked against known structures, with new
terms added incrementally wherever predictions are found to disagree with reality, not because a
physical argument demanded them.

## From sequence to structure: the thought experiment

Given a potential energy function, suppose you have a ~100-residue sequence and two candidate
structures for it, one predominantly alpha-helical and one predominantly beta-sheet. How would you
decide which one the sequence prefers? Three approaches came up in discussion:

- **Search for homology** — if a close homolog has a known structure, the problem may be solved.
- **Secondary-structure propensities** — count how often each amino acid occurs in a helix versus a
  sheet across known structures, and use the sequence's composition to judge which it favors (taken
  up below as secondary-structure prediction).
- **Threading** — given precise backbone coordinates for both candidates, build the actual sequence
  onto each backbone, attaching the correct side chains, compute the potential energy of each
  resulting model, and prefer the lower-energy structure.

Threading is where the real optimization problem lives, developed through a deliberately
adversarial framing: a labmate has solved two structures of the same length and challenges you to
work out, from backbone coordinates alone, which one is your sequence's true structure.

### Threading, and why it is a coupled problem

Even with the right backbone believed known, every side chain's rotatable bonds must be decided
simultaneously rather than one at a time, because the choice at one position can create or resolve
a clash with a neighboring side chain. This makes side-chain placement a highly coupled
combinatorial optimization problem, not solvable greedily.

It gets worse if the backbone itself is in doubt. If a database search only turns up homologs at
~20% identity, and different homologs at that identity can have entirely different folds, there may
be no way to tell which candidate backbone is correct from sequence alone. Then backbone and
side-chain conformations must be optimized together — moving the backbone moves the side chains
with it — over an enormous, and even discretized still very large, search space. This combined
problem is what the lecture calls **fold recognition** or **threading**.

(Recognizing a protein's domain structure directly from sequence patterns — using, for instance, the
hidden Markov models covered in an earlier lecture — is a related problem named but not developed
further here.)

### Levinthal's paradox

Why not just brute-force the search? Cyrus Levinthal (then a professor at MIT, later at Columbia)
estimated, for a simplified folding model, that a protein randomly searching all its possible
conformations, switching between them as fast as physically possible, would take roughly the
lifetime of the universe to find the folded state. Real proteins fold far faster, so they cannot be
doing anything like a random search — which is exactly why the computational problem needs smarter
optimization than exhaustive search, the subject taken up at the end of this lecture and continued
in the next.

## A short history of secondary-structure prediction

**Linus Pauling (1951)** predicted the alpha helix without a computer — reportedly while sick in
bed — using paper models and known small-molecule bond distances together with the strong
preference for hydrogen bonding and the planarity of the peptide bond, to find a repeating backbone
structure maximizing internal hydrogen bonding.

**Ramachandran** (Madras University) showed, again with paper models and geometric reasoning rather
than computation, that not every combination of the backbone angles $\phi$ and $\psi$ is physically
allowed — some combinations force atoms into steric collision. The allowed region in $(\phi,\psi)$
space is the **Ramachandran plot**, later reused as one of Rosetta's statistical terms.

A 1960s paper introduced the **helical wheel**: looking down an alpha helix's axis, successive
residues emerge rotated by about 100° from one another (roughly 3.6 residues per turn), so a
residue's position projects onto a wheel. Plotting a sequence's hydrophobic and hydrophilic residues
on the wheel shows whether they cluster on one side — an **amphipathic** helix, with one buried and
one solvent-exposed face, matching a helix that lies on a protein's surface. The pattern identifies
only that class of helix; it says nothing about helices that are fully buried or fully exposed.

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="Helical wheel projection of seven consecutive helix residues, each offset by about 100 degrees, showing them separating into two faces of the wheel">
  <circle cx="160" cy="120" r="80" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <path d="M 160,120 L 128,54 A 80,80 0 0,1 221,91 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <g font-size="12" fill="currentColor">
    <circle cx="160" cy="40" r="4"/><text x="160" y="28" text-anchor="middle">1</text>
    <circle cx="221" cy="91" r="4"/><text x="233" y="91" text-anchor="start">2</text>
    <circle cx="194" cy="194" r="4"/><text x="202" y="212" text-anchor="middle">3</text>
    <circle cx="126" cy="194" r="4"/><text x="118" y="212" text-anchor="middle">4</text>
    <circle cx="99" cy="91" r="4"/><text x="87" y="91" text-anchor="end">5</text>
    <circle cx="179" cy="47" r="4"/><text x="186" y="33" text-anchor="start">6</text>
    <circle cx="214" cy="137" r="4"/><text x="228" y="140" text-anchor="start">7</text>
  </g>
  <text x="160" y="235" text-anchor="middle" font-size="11" fill="currentColor">shaded wedge: one face of the helix</text>
</svg>
<figcaption>Projecting seven consecutive residues of an alpha helix down its axis, each offset from
the last by about 100 degrees: residues 1, 2 and 6 fall on one face of the wheel and the rest on the
other, the pattern used to spot an amphipathic helix.</figcaption>
</figure>

**Chou and Fasman (1974)** computed, for each amino acid, how often it occurs overall versus
specifically in a helix, a sheet, or neither. Rather than combining these propensities with formal
Bayesian statistics — not yet the field's habit in 1974 — they built an ad hoc algorithm motivated by
the chemistry of helix formation (a small nucleating stretch that then extends), counting strong
helix-former residues against helix-breaker residues. From a database of only 2,473 residues total,
this reached about 60% accuracy — judged by the lecture as astounding for its time and data. A
survey of secondary-structure methods from roughly a decade before this lecture found accuracy had
only risen to about 76% by the early 2000s: in thirty years, with far more structural data
available, only about sixteen points of improvement — evidence the 1974 approach had already
captured most of what is predictable this way.

## Looking ahead

The lecture closes by returning to the potential energy landscape: whichever energy function is
used, a protein's conformations define a landscape over it, and the goal is to get from an arbitrary
starting conformation to the structure(s) at its minima. The next lecture takes up three techniques
for this: **energy minimization** (small local changes refining an approximate structure toward the
nearest minimum — the side-chain problem posed above), **molecular dynamics** (simulating the
physical forces directly, in CHARMM's spirit), and **simulated annealing** (allowing jumps between
conformations far larger than an actual physical simulation would permit, to search a much larger
part of the conformational space).

## Exercises

These are drawn from the course's own problem set on protein structure in PyRosetta, which this
lecture refers to directly ("you'll actually do that in your problem set") when raising the
side-chain packing problem. Throughout, the structure is PDB entry 1YY8, with skeleton code
`pyRosetta_1YY8.py`, a cleaned structure `1YY8.clean.pdb`, and a version with one backbone angle
altered, `1YY8.rotated.pdb`.

1. Look up PDB entry 1YY8. What molecule is it, and — from the "3D View" — is its predominant
   secondary structure alpha-helical or beta-sheet?
2. `part_b()` loads `1YY8.clean.pdb` and prints the protein's backbone angles and energy score. Run
   it. What is the total energy, and which scoring categories are the largest contributors for and
   against it? (Describe the categories in words, as given in lecture, not by their program names.)
3. `part_c()` implements Monte Carlo side-chain packing. Add code to print the energy after packing,
   run it, and report the post-packing energy and which two scoring categories decreased most
   compared to part 2.
4. `1YY8.rotated.pdb` is `1YY8.clean.pdb` with one residue's $\phi$ or $\psi$ angle changed. Load it
   in `part_d()`, pack its side chains as in part 3, and report the energy before and after. Why
   does the post-packing energy differ from the one found in part 3?
5. In `part_e()`, determine which backbone angle — $\phi$ or $\psi$, at which residue — was altered
   in the rotated structure.
6. Using that residue and angle, compute in `part_f()` the energy of the structure with the angle
   set to each value from $-180$ to $180$ degrees. Which value gives the lowest energy, and does it
   agree with the corresponding angle in the original structure from part 2?

## Sources

All of this chapter comes from the transcript of lecture 12 of MIT 7.91J (Foundations of
Computational and Systems Biology, Spring 2014),
`computational-biology/mit-ocw/7091j/recordings/lectures/12.md`, timestamps 00:00-1:05:30. No slide
deck for this lecture was converted, so every item the lecturer describes as shown on a slide (the
p53 mutation plot, the PDB statistics, the PDB file excerpt, the potential plots, the Ramachandran
plot, the helical wheel, the Chou-Fasman table) is reconstructed from the spoken description rather
than seen directly; where the transcript does not pin down enough detail to reconstruct a term
precisely (the exact form of CHARMM's angle and dihedral terms, or the reference state in the
Boltzmann-inversion potentials), this chapter says only what the lecture says and no more.

Named but not contained: the textbook *Structural Bioinformatics*, cited for the comparison between
sequence-level and structure-level algorithms; the RCSB PDB's own documentation and visualization
tools (PyMOL, Swiss PDB Viewer); the CHARMM parameter files and the Rosetta/PyRosetta
documentation, cited for the full details and weights of the terms described qualitatively here; a
reference the lecturer points to, unnamed, for the physical justification of one dihedral term; the
original papers for Pauling's 1951 prediction, Ramachandran's analysis, the 1960s helical-wheel
paper, and Chou and Fasman's 1974 paper, referred to by result and (where given) author and year but
not by full title; the roughly-2003 survey of secondary-structure methods cited for the ~76% figure;
and the hidden Markov model treatment of protein domain recognition, referred to as covered in an
earlier lecture, not supplied here.

The exercises are from the course's own problem set,
`computational-biology/mit-ocw/7091j/psets/03-questions-pset3-ques/03-p3-protein-structure-with-pyrosetta-6-points.md`
(parts A–F; a fourth part of that same problem set, on queuing theory, is unrelated to this lecture
and omitted here).

---

[← 11. Real-World HMMs and RNA Structure](11-real-world-hmms-and-rna-structure.md) · [Contents](index.md) · [13. Refining and Predicting Protein Structure →](13-refining-and-predicting-protein-structure.md)
