---
title: "11. Real-World HMMs and RNA Structure"
course: "MIT 7.091J"
chapter: 11
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. Real-World HMMs and RNA Structure

## What this covers

This lecture has two halves. The first finishes the previous lecture's tour of hidden Markov
models with two models used in practice — profile HMMs for protein families and TMHMM for
transmembrane helices — and uses TMHMM to introduce the forward–backward algorithm, which gives a
confidence value for each part of a prediction rather than just the single best parse. The second
half opens RNA secondary structure: what it is, why it matters biologically, and the two standard
ways of predicting it — comparing homologous sequences (covariation) and minimizing folding free
energy (the Nussinov algorithm). It assumes the HMM vocabulary from the previous lecture — states,
transition/emission probabilities, and the Viterbi algorithm, worked there on a toy CpG-island HMM.

## Picking up from the CpG-island HMM

The previous lecture ended on the cost of Viterbi: for a $k$-state HMM run on a sequence of length
$L$, it costs $O(k^2 L)$, since moving from position $i$ to $i+1$ requires, for each of the $k$
states, maximizing over its $k$ possible predecessor states. The slides also carry a direct
follow-up question on that same CpG-island HMM, reproduced as an exercise below.

## Two hidden Markov models used in practice

### Profile HMMs

A profile HMM is built from a multiple alignment of proteins sharing a function or a common
domain — Pfam contains such models for hundreds of domains. With enough aligned examples, the model
captures not just residue frequency at each alignment column but the probability of an insertion at
each position, what tends to get inserted, and the probability of a deletion. Each hidden state is
one of three kinds: a **match state** ($M$), emitting a residue present in the alignment column; an
**insert state** ($I$), emitting a residue not in the underlying column; and a **delete state**
($D$), emitting a gap. A query protein is threaded through a library of such models to ask whether
it matches any domain significantly — how Pfam searches work. The same insertion/deletion machinery
applies to HMMs for DNA and RNA alignments as well as protein.

### TMHMM: predicting transmembrane helices

TMHMM predicts, from sequence alone, whether a protein has transmembrane helices, how many, their
orientation (N-terminus inside or outside the cell), and their boundaries — about 97% of helices
correctly, according to the authors (Krogh et al., *J. Mol. Biol.*, 2001). Its hidden states are
regions of architecture rather than individual residues: a helix core, cytoplasmic and
non-cytoplasmic caps flanking it, and globular domains on each side. Emission probabilities differ
sharply: the core favors hydrophobic residues, the caps favor charged residues anchoring the helix
in the membrane, and the globular regions favor hydrophilic residues.

#### Getting the helix-length distribution right

A single state that emits a residue and then, with probability $1-p$, loops back to itself
generates helices whose length follows a **geometric distribution**, $P(L=n) \propto (1-p)^n$, with
mean about $1/p$. Setting $p = 1/20$ gives the right mean, about 20 residues. But the shape is wrong:
a geometric distribution is maximal at $n=1$ and falls off monotonically, while real transmembrane
helices are essentially never shorter than about 15 residues (too short to span the membrane) nor
much longer than about 25, and peak somewhere in between.

<figure>
<svg viewBox="0 0 340 190" role="img" aria-label="Geometric length distribution from a single self-looping state compared with the true, cutoff distribution of transmembrane helix lengths">
  <line x1="30" y1="160" x2="320" y2="160" stroke="currentColor" stroke-width="1"/>
  <line x1="30" y1="160" x2="30" y2="20" stroke="currentColor" stroke-width="1"/>
  <text x="170" y="182" text-anchor="middle" font-size="12" fill="currentColor">helix length n</text>
  <path d="M 40 30 Q 100 140 320 158" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="45" font-size="11" fill="currentColor">single self-looping state</text>
  <path d="M 30 160 L 150 160 L 160 55 L 220 50 L 230 155 L 320 160" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="170" y="38" text-anchor="middle" font-size="11" fill="currentColor">real distribution</text>
  <text x="150" y="176" text-anchor="middle" font-size="10" fill="currentColor">~15</text>
  <text x="230" y="176" text-anchor="middle" font-size="10" fill="currentColor">~25</text>
</svg>
<figcaption>A single self-looping state yields a geometric length distribution, peaked at n = 1;
real transmembrane helices cluster between about 15 and 25 residues.</figcaption>
</figure>

A single self-looping state can only ever produce a geometric sojourn time, whatever its self-loop
probability — only the mean is tunable, not the shape. Chaining several self-looping helix states
in series does better (the sum of several geometric waits gives a negative binomial, somewhat
peaked). TMHMM's actual fix goes further: roughly 25 helix-core states in series, with transitions
from a particular point in the chain that can skip ahead by varying amounts — skipping one state
ahead gives the longest helix the model allows, skipping further gives shorter ones — so that, by
choosing the skip probabilities, the model reproduces essentially any length distribution within a
fixed range. The cost: Viterbi is $O(k^2L)$, so going from one helix state to 25 makes each position
much more expensive, and there are many more transition parameters to fit.

#### Confidence: the forward–backward algorithm

Viterbi returns the single most probable path, not how confident the model is in any part of it. A
second quantity, $P(\text{obs})$ — the total probability of the sequence summed over *every* hidden
path — is computed by an algorithm structurally like Viterbi, but summing instead of maximizing over
incoming transitions. Run left to right this gives a forward value at each state and position; the
same summing recursion run right to left gives a backward value. Multiplying the forward and
backward values at a given state and position, divided by $P(\text{obs})$, gives the **posterior
probability** of that state at that position, summed over every path consistent with it, not just
the Viterbi path. For the mouse chloride channel CLC6, TMHMM's optimal parse predicts seven
helices, starting outside and ending inside; the posterior plot is very confident about the
N-terminus and the first two helices, and for one region assigns more than half the total
probability to a third helix that nonetheless does not appear in the single optimal parse — likely
because including it there forces other changes that lower the overall path probability. This
confidence information lets an experimentalist prioritize which predicted helices to test first.

## RNA secondary structure: what it is and how to write it down

RNA, like protein, folds into a tertiary structure that often determines function. **Secondary
structure** is simpler: just the set of hydrogen-bonded base pairs. tRNA's cloverleaf is the classic
example — specifying the base pairs produces the familiar picture and narrows down where the
functionally important anticodon loop can be, since paired bases cannot also pair with a message.

Two common notations: **dot-bracket**, a dot for an unpaired base and matching `(`/`)` for a pair,
read like balanced parentheses; and **arc notation**, an arc between every hydrogen-bonded pair.
Whether arcs cross is a fundamental classification. A nested structure — ordinary stem-loops, such
as tRNA's cloverleaf, drawn as one large arc joining the first and last bases with smaller nested
arcs inside — never crosses. A **pseudoknot** does: if position 1 pairs with 3 and 2 pairs with 4,
the two arcs necessarily cross. It is not a literal topological knot, but behaves like one
computationally — nested structures are tractable by the dynamic-programming methods below, and
pseudoknots are not.

<figure>
<svg viewBox="0 0 320 170" role="img" aria-label="Non-crossing base pairing compared with a pseudoknot, on four positions">
  <text x="10" y="20" font-size="12" fill="currentColor">nested</text>
  <line x1="30" y1="45" x2="290" y2="45" stroke="currentColor" stroke-width="1"/>
  <circle cx="50" cy="45" r="3" fill="currentColor"/>
  <circle cx="110" cy="45" r="3" fill="currentColor"/>
  <circle cx="170" cy="45" r="3" fill="currentColor"/>
  <circle cx="230" cy="45" r="3" fill="currentColor"/>
  <text x="50" y="65" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="110" y="65" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="170" y="65" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="230" y="65" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <path d="M 50 45 Q 140 5 230 45" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <path d="M 110 45 Q 140 20 170 45" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <text x="10" y="110" font-size="12" fill="currentColor">pseudoknot</text>
  <line x1="30" y1="135" x2="290" y2="135" stroke="currentColor" stroke-width="1"/>
  <circle cx="50" cy="135" r="3" fill="currentColor"/>
  <circle cx="110" cy="135" r="3" fill="currentColor"/>
  <circle cx="170" cy="135" r="3" fill="currentColor"/>
  <circle cx="230" cy="135" r="3" fill="currentColor"/>
  <text x="50" y="155" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="110" y="155" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="170" y="155" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="230" y="155" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <path d="M 50 135 Q 110 90 170 135" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <path d="M 110 135 Q 170 100 230 135" fill="none" stroke="currentColor" stroke-width="1.3"/>
</svg>
<figcaption>Four positions paired without crossing (top: 1–4, 2–3) versus a pseudoknot (bottom:
1–3, 2–4), where the arcs necessarily cross.</figcaption>
</figure>

## Why secondary structure matters: three examples

**The ribosome is a ribozyme.** Structures of the bacterial ribosome (large subunit 50S, small
subunit 30S) show three tRNA sites: A, where a new aminoacyl-tRNA enters; P, holding the tRNA
attached to the growing peptide; and E, the exit site for the tRNA that added the previous residue.
The ribosome is overwhelmingly RNA by mass, with protein decorating the outside rather than filling
the core — consistent with RNA as the original functional scaffold and protein added later. The
nearest proteins to the catalytic site are some 18–24 Å away, too far to participate directly in the
chemistry, which is the structural evidence that catalysis belongs to the RNA. RNA also builds other
structures: the ribosome's exit tunnel for the growing polypeptide is a long, narrow RNA tube,
deliberately too thin for the polypeptide to fold inside it, deferring folding until after it
emerges. Knowing ribosome structure in detail matters practically: many antibiotics exploit
structural differences between prokaryotic and eukaryotic ribosomes, inhibiting the bacterial one
while sparing the host's.

**Non-coding RNAs depend on structure for function.** tRNAs, rRNAs, UTRs, snRNAs, snoRNAs,
prokaryotic transcription terminators, RNase P, SRP RNA, tmRNA, microRNAs, long non-coding RNAs, and
riboswitches are all classes where knowing which parts of the molecule are free to base-pair in
trans, and which are already paired internally, matters for function. Conserved RNA structure
(conserved potential to pair at a distance, rather than conserved sequence) is also a signal used to
identify candidate non-coding RNA genes in a genome, as distinct from protein-coding exons or
DNA-level regulatory elements.

**Riboswitches use structure to sense the cell.** A riboswitch adopts more than one conformation
and switches between them in response to a stimulus — temperature, or binding of a small molecule or
ion — with one conformation occluding a regulatory element and the other exposing it. In the lysine
riboswitch, absence of lysine leaves the ribosome binding site exposed and lysine-biosynthesis genes
translated; once lysine accumulates, it binds the RNA and shifts its structure so a stem forms that
sequesters the ribosome binding site, shutting off further biosynthesis. Dozens of such riboswitches
are known in bacterial genomes, controlling substantial parts of metabolism.

## Predicting structure by covariation

If structure is conserved across homologs more strongly than the exact sequence, base-paired
positions should show compensatory substitutions: when one partner changes, the other changes too,
preserving the ability to pair. Given five short homologous sequences, the lecture's example shows
the first and eighth columns always complementary across all five, and likewise the second and
seventh — including one G·U pair (G·U is slightly less stable than A·U but does occur in natural
RNA, unlike in DNA). That pattern is exactly what a two-base-pair stem closing a four-base loop would
produce, and it is not visible from only two sequences; it takes several independent substitutions
to make the inference compelling.

### The mutual information statistic

For a realistic case — hundreds of bases, many homologs — the pattern cannot be seen by eye. For
every pair of alignment columns $i,j$, let $f_x^{(i)}$ be the fraction of sequences with nucleotide
$x$ in column $i$, and $f_{x,y}^{(i,j)}$ the fraction with $x$ in column $i$ *and* $y$ in column $j$
(the columns need not be adjacent in the sequence). The **mutual information** of the pair is

$$M_{ij} = \sum_{x,y \in \{A,C,G,U\}} f_{x,y}^{(i,j)} \log_2 \frac{f_{x,y}^{(i,j)}}{f_x^{(i)} f_y^{(j)}}$$

the relative entropy of the observed joint distribution against what it would be if the two columns
varied independently. If they are independent, every ratio is 1 and $M_{ij}=0$. The statistic is
non-negative and reaches its maximum of 2 bits exactly when both columns' background frequencies are
uniform ($\tfrac14$ each) and the columns covary perfectly — e.g. if only A·U, C·G, G·C, U·A
dinucleotides occur, each at frequency $\tfrac14$, giving four terms of $\tfrac14\log_2 4 = \tfrac12$
each, summing to 2. The maximum does not require complementary pairing specifically — any
sufficiently specific one-to-one relationship achieves it — but complementary covariation is what is
sought. Other dependence measures (a chi-squared statistic, say) would serve equally well.

In practice: compute $M_{ij}$ for every column pair and look for high values, especially a block of
several *consecutive* positions covarying with another block in the nested, inverse-complementary
order a stem requires — a lone isolated pair is not thermodynamically stable, but a short run is. The
full $M_{ij}$ matrix for a tRNA alignment shows exactly this: one block of covarying columns near the
two sequence ends (the acceptor stem), with further blocks nested inside it — the pattern that
reconstructs the cloverleaf.

### What covariation requires

Three conditions: the structure must be more conserved than the sequence; there must be enough
divergence for independent compensatory substitutions to have occurred (sequences too similar give
no variation — in the limit of identical sequences $M_{ij}=0$ everywhere); and there must be enough
homologs for reliable statistics. Divergence is bounded on the other side too: too far across species
and the alignment itself becomes unreliable, and a correct alignment is needed before asking whether
columns covary.

## Predicting structure by energy minimization

Covariation needs homologs; energy minimization needs only the single sequence, on the hypothesis
that it folds to its lowest free energy state among many candidates. As with protein folding,
$\Delta G = \Delta H - T\Delta S$: forming a base pair releases enthalpy (favoring folding), while
losing conformational freedom costs entropy (favoring the unfolded state), so higher temperature
favors unfolding. The earliest algorithms ignored entropy and loop/stacking effects, scoring $+1$ for
every allowed pair (C·G or A·U) and $0$ otherwise, maximizing the total — the **Nussinov algorithm**,
treating base-pair maximization as a proxy for free-energy minimization under a model that assigns
equal enthalpy to every allowed pair.

### The recursion

Base pairing breaks the left-to-right order that worked for sequence alignment and for Viterbi,
since the first base can pair with the last. The natural order works from the inside out, filling an
$n \times n$ table indexed by $(i,j)$ away from the diagonal toward the corner. Let $S(i,j)$ be the
maximum number of base pairs in the subsequence from $i$ to $j$. Four ways the optimal structure on
$(i,j)$ can be built from smaller sub-intervals:

1. $i,j$ pair: $S(i,j) = S(i+1,j-1) + 1$.
2. $i$ unpaired: $S(i,j) = S(i+1,j)$.
3. $j$ unpaired: $S(i,j) = S(i,j-1)$.
4. **Bifurcation**: $i$ and $j$ are each paired, but not to each other, each pairing with something
   inside the interval. $S(i,j) = \max_{i<k<j}\big[S(i,k) + S(k+1,j)\big]$.

$S(i,j)$ is the maximum of the four. Bifurcation is the hard case to get used to: working strictly
inward from $(i+1,j-1)$ can get trapped in a locally reasonable but globally suboptimal pairing near
the middle, when splitting at some $k$ and combining two separately-optimal halves does better.

<figure>
<svg viewBox="0 0 330 200" role="img" aria-label="Dependency structure of the Nussinov recursion on the (i,j) table">
  <defs>
    <marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0,0 6,3 0,6" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="150" y="60" width="40" height="40" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="170" y="84" text-anchor="middle" font-size="12" fill="currentColor">S(i,j)</text>
  <rect x="190" y="100" width="40" height="40" fill="none" stroke="currentColor" stroke-width="1" fill-opacity="0.15"/>
  <text x="210" y="124" text-anchor="middle" font-size="11" fill="currentColor">S(i+1,j-1)</text>
  <text x="235" y="140" font-size="10" fill="currentColor">pair i,j (+1)</text>
  <line x1="200" y1="100" x2="175" y2="98" stroke="currentColor" stroke-width="1" marker-end="url(#arr2)"/>
  <rect x="190" y="60" width="40" height="40" fill="none" stroke="currentColor" stroke-width="1" fill-opacity="0.15"/>
  <text x="210" y="84" text-anchor="middle" font-size="11" fill="currentColor">S(i+1,j)</text>
  <text x="235" y="50" font-size="10" fill="currentColor">i unpaired</text>
  <line x1="190" y1="80" x2="192" y2="80" stroke="currentColor" stroke-width="1" marker-end="url(#arr2)"/>
  <rect x="150" y="100" width="40" height="40" fill="none" stroke="currentColor" stroke-width="1" fill-opacity="0.15"/>
  <text x="170" y="124" text-anchor="middle" font-size="11" fill="currentColor">S(i,j-1)</text>
  <text x="90" y="140" font-size="10" fill="currentColor">j unpaired</text>
  <line x1="170" y1="100" x2="170" y2="102" stroke="currentColor" stroke-width="1" marker-end="url(#arr2)"/>
  <rect x="50" y="60" width="90" height="40" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2" fill-opacity="0.15"/>
  <text x="95" y="84" text-anchor="middle" font-size="11" fill="currentColor">S(i,k) + S(k+1,j)</text>
  <text x="40" y="45" font-size="10" fill="currentColor">bifurcation, any split k</text>
  <line x1="140" y1="80" x2="152" y2="80" stroke="currentColor" stroke-width="1" marker-end="url(#arr2)"/>
</svg>
<figcaption>S(i,j) is the best of four options: pair i with j and add one for the smaller interval,
leave i or j unpaired, or split at some k and add the two independently-optimal halves
(bifurcation).</figcaption>
</figure>

To fill the table: initialize the diagonal and sub-diagonal to 0 (intervals too short for a pair),
then fill outward toward the upper-right corner — any order works provided a cell's dependencies are
already filled — recording at each cell which of the four options produced its score, so the final
answer (upper-right corner) can be traced back into an actual structure.

### Complexity, and what it cannot handle

Filling the table costs $O(n^2)$ memory; each cell costs $O(n)$ because of the bifurcation check
over every split point, so the total time is $O(n^3)$ — markedly worse than the HMM algorithms, and
why some RNA-folding servers refuse sequences longer than about a thousand bases. The recursion also
cannot represent pseudoknots, since it assumes everything paired inside $(i,j)$ stays inside
$(i,j)$ — exactly what a pseudoknot violates. Pseudoknots are nonetheless biologically important:
some viral RNAs have them, and some even have "kissing loops," where two stem-loops' *loops*
interact directly. A pseudoknot can cause programmed ribosomal frameshifting — instead of simply
melting it, the ribosome can be knocked back a position and resume in a different reading frame; HIV
uses this to produce its reverse transcriptase/integrase fusion protein from the same mRNA that
encodes other viral proteins in a different frame.

## Beyond base-pair counting

More refined methods use real thermodynamic parameters (a G·C pair contributes more stabilizing
energy than an A·U pair) rather than counting every allowed pair equally, and compute more than one
structure. The Zuker algorithm, implemented in the Mfold server and the Vienna RNAfold package,
computes the minimum-energy structure together with suboptimal structures and the probability of
each individual base pair, summed over the full partition function of possible folds weighted by
free energy. It gets roughly 70% of base pairs correct — usually right, occasionally badly wrong on
a given molecule. Run on the U5 snRNA it returns one confident structure with no competing
suboptimal folds; run on the lysine riboswitch it returns several structures of comparable energy,
consistent with that molecule genuinely having more than one functional conformation.

## Exercises

1. For the CpG-island HMM (transitions $P_{gg}=0.99999$, $P_{ii}=0.999$, $P_{ig}=0.001$,
   $P_{gi}=0.00001$; initiation $P_g=0.99$, $P_i=0.01$; emissions $C,G,A,T = 0.3,0.3,0.2,0.2$ in the
   island state and $0.2,0.2,0.3,0.3$ in the genome state), find the optimal (Viterbi) parse for:
   - $(\text{ACGT})_{10000}$
   - $\text{A}_{1000}\text{C}_{80}\text{T}_{1000}\text{C}_{20}\text{A}_{1000}\text{G}_{60}\text{T}_{1000}$

   (The slide pairs this with a table of powers of 1.5 — $1.5^{20}\approx 3\times10^3$,
   $1.5^{40}\approx 1\times10^7$, $1.5^{60}\approx 3\times10^{10}$, $1.5^{80}\approx 1\times10^{14}$.)

2. Print or redraw the partially-filled Nussinov $(i,j)$ score matrix given in the Nature
   Biotechnology primer on RNA folding (the assigned reading for this topic), for its example
   sequence. Fill it in by hand — including the traceback arrows recording which base pair was added
   at each step — working outward from the diagonal to the upper-right corner, then trace back to
   recover the optimal structure. (The completed matrix is in the same source to check against; work
   it out first.)

## Sources

- Slides: `lectures/11-slides.md` (labeled "Lecture #10" in the deck) — the trellis/CpG-island
  recap, the Viterbi-example sequences and powers-of-1.5 table, the profile-HMM alignment slide,
  the TMHMM slides (help page, architecture, CLC6 output), the RNA secondary structure notation
  slide, the tRNA/ribosome slides (Cate et al. *Science* 1999; Ban et al. *Science* 2000; Nissen et
  al. *Science* 2000), the covariation example and mutual-information formula, the classes-of-ncRNA
  list, the energy-minimization and base-pair-maximization slides, and the lysine riboswitch slide
  (Serganov et al., *Nature* 2008; Caron et al., *PNAS* 2012).
- Transcript: `recordings/lectures/11.md`, 00:00–04:21 (HMM/Viterbi recap), 04:21–06:30 (profile
  HMMs), 06:30–20:25 (TMHMM, helix-length distribution, the 25-state fix, CLC6), 21:36–25:56
  (forward–backward, posterior probability), 26:05–37:15 (RNA secondary structure notation and
  biological examples), 37:15–1:01:43 (covariation, mutual information, requirements, pseudoknots,
  ncRNA classes), 1:01:43–1:20:14 (energy minimization, Nussinov recursion, complexity, frameshifting),
  1:20:14–1:21:17 (Zuker/Mfold, U5 snRNA and lysine riboswitch).
- Named but not contained in either source: the Rabiner HMM tutorial (for forward–backward detail);
  the Nature Biotechnology primer on RNA folding and Zuker & Berger (Z&B) Ch. 11.9 (course readings
  for RNA secondary structure, including the worked Nussinov matrix used in the exercise above); the
  TMHMM paper (Krogh et al., *J. Mol. Biol.*, 2001) for the exact helix-state architecture, which the
  lecturer described from memory and flagged as uncertain in places; and a board-drawn worked example
  of the Nussinov bifurcation trap, which is a chalk diagram not captured in the transcript or
  slides.

---

[← 10. Markov and Hidden Markov Models](10-markov-and-hidden-markov-models.md) · [Contents](index.md) · [12. Protein Structure and Energy Functions →](12-protein-structure-and-energy-functions.md)
