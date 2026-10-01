---
title: "3. Global Alignment and Scoring Matrices"
course: "MIT 7.091J"
chapter: 3
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. Global Alignment and Scoring Matrices

## What this covers

This chapter finishes the statistics of local alignment begun in the previous lecture — why the
choice of mismatch penalty trades sensitivity against selectivity — and then builds the main
machinery of pairwise alignment: dynamic programming for global alignment (Needleman-Wunsch) and
gapped local alignment (Smith-Waterman), and the Dayhoff PAM matrices that supply the scores those
algorithms use. It assumes the simple local-alignment algorithm and the Karlin-Altschul statistics
(the Gumbel/extreme-value distribution, the parameter $\lambda$) from the previous lecture, and
ends by opening the idea of a Markov chain, which the next lecture uses to build PAM matrices
properly. (The lecture opens with a few minutes of Q&A on sequencing library preparation — how to
put different adapters on the two ends of an insert — left over from the previous lecture; that is
not alignment and is not reconstructed here.)

## Mismatch penalties and the limits of local-alignment statistics

Recall the setup: a local-alignment algorithm (e.g. BLAST) reports high-scoring segments, and the
significance of a segment of score $S$ exceeding a cutoff $x$ is governed by an extreme-value
(Gumbel) distribution,

$$P(S > x) = 1 - \exp\!\left[-KMN e^{-\lambda x}\right],$$

for a database and query of lengths $M, N$, with $K,\lambda$ positive constants set by the scoring
system and sequence composition — this requires the *expected* score of a random alignment to be
negative while still allowing positive scores. $\lambda$ is pinned down by the scoring matrix
itself: it is the unique positive solution of

$$\sum_{i,j} p_i\, r_j\, e^{\lambda s_{ij}} = 1,$$

where $p_i, r_j$ are nucleotide frequencies in query and subject and $s_{ij}$ the score for aligning
base $i$ against base $j$ (Karlin & Altschul, 1990). The same calculation gives *target
frequencies* $q_{ij} = p_i r_j e^{\lambda s_{ij}}$, the frequency with which pair $(i,j)$ shows up
inside a genuinely high-scoring segment: large for matches, small for mismatches, so such segments
are enriched for matches relative to chance.

For a scoring system with match $=+1$ and mismatch $=m$, this theory gives an "optimal" mismatch
penalty for a target identity fraction $r$:

$$m = \frac{\ln\!\big(4(1-r)/3\big)}{\ln(4r)}, \qquad
\begin{array}{c|ccc} r & 0.75 & 0.95 & 0.99 \\ \hline m & -1 & -2 & -3 \end{array}$$

A harsher penalty is "optimal" for nearly-identical matches, a gentler one for divergent ones — but
this doesn't mean $m=-1$ or $-2$ *can't* find 99%-identical matches; what changes is the match
length needed to reach significance. Intuitively, a harsher penalty makes one mismatch cost more,
so the algorithm needs a longer run of matches to recover, which it can only afford if true
identity is very high. Formally, going from $m=-1$ to $m=-3$ *increases* $\lambda$, so a shorter
high-scoring run reaches significance — provided it is built almost entirely of matches.

This has a floor. At $m=-2$, a region only 66% identical nets an expected score per residue of
$\tfrac23(+1)+\tfrac13(-2)=0$: zero drift, so the cumulative score wanders near zero and never
reaches anything unusual, however long the sequences are — 66% is about the floor $m=-2$ can
detect. Weaker matches need $m=-1$, but then need correspondingly longer alignments to reach
significance: harsher penalties suit short, highly-conserved regions, gentler ones suit long,
weakly-conserved ones.

## Translated searches and the flavors of BLAST

A coding sequence can be easier to find by translating it and searching with a protein scoring
matrix than by searching the nucleotide sequence directly, since protein-level constraint is often
stronger than nucleotide identity (below). Since the reading frame usually isn't known in advance,
BLAST translates a query in all six frames (three forward, three on the complementary strand) and
searches the resulting "bag of peptides," splitting at stop codons:

```
ttg|acc|tag|atg|aga|tgt|cgt|tca|ctt|tta|ctg|agc|tac|aga|aaa
 L   T   x   M   R   C   R   S   L   L   L   S   Y   R   K
```

This gives a family of search programs, distinguished by whether query/database are nucleotide or
protein and whether either is translated on the fly:

| Program | Query | Database |
|---|---|---|
| BLASTP | protein | protein |
| BLASTN | nucleotide | nucleotide |
| BLASTX | nucleotide ($\to$ protein) | protein |
| TBLASTN | protein | nucleotide ($\to$ protein) |
| TBLASTX | nucleotide ($\to$ protein) | nucleotide ($\to$ protein) |
| PsiBLAST | protein (as an alignment) | protein |

Choosing among them is a judgment call about where the conservation lives. Chimp ESTs with no
chimp genome, searched against human: genomes are similar enough, even outside coding regions, that
BLASTN or BLASTX both work, and only BLASTN finds a $3'$-UTR read, since UTRs don't translate. A
human EST against the mouse genome: mouse/human exons are only ~80% identical at the nucleotide
level, but much of that divergence is synonymous (third-codon-position) and doesn't change the
amino acid, so a translating search (TBLASTX) often finds matches a nucleotide search misses.
Whether to search a translated genome or an annotated proteome then depends on annotation quality:
mouse's proteome is well annotated, so BLASTX against it usually suffices; for a poorly-annotated
genome, TBLASTX against all six translated frames can find an exon no protein database has yet.

## Why align protein sequences?

The practical motivation is functional inference: a human protein with a homologous mouse protein
of known function (from a knockout, say) lets you guess the human protein does something similar,
resting on sequence similarity $\implies$ similarity in function and/or structure. This holds almost
always above ~30% identity over a protein's full length; 20–30% is the "twilight zone," sometimes
right and sometimes not; below that it mostly shouldn't be trusted, though remote homologies
occasionally hide there.

The converse is false, and importantly so: **structural similarity does not imply sequence
similarity, or even common ancestry.** Function lives in the folded, three-dimensional protein;
conservation is recorded only in the one-dimensional string, and a strong enough functional demand
can push evolution to the same structural solution more than once. A hummingbird and a hawk moth
(an insect) converge on strikingly similar appearance and flight because they share an ecological
niche — hovering, nectar feeding — though their last common ancestor, over 500 million years ago,
had neither wings nor, probably, legs or eyes. *Haemophilus influenzae* Fe$^{3+}$-binding protein
and eukaryotic lactoferrin really are homologous (bacteria/eukaryotes diverged ~2 billion years
ago), but their ancestor bound *anions*; the iron-coordinating tyrosine and histidine evolved
independently in the two lineages to bind a cation instead (a carboxylate versus a phosphate shows
the convergence wasn't exact). And the ribosome recycling factor (RRF), an L-shaped protein that
releases the ribosome after translation, has essentially the same 3D shape as a tRNA, because it
must fit the ribosome's tRNA-binding sites — a protein and an RNA that almost certainly never
shared a molecular ancestor, converging because the functional slot did.

## Reading alignment strategy off a dot matrix

A *dot matrix* plots one sequence along each axis and marks wherever the two agree over some short
run of consecutive positions (a run, not a single residue, to cut chance noise). The picture, not
the sequence, tells you which alignment to use.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Dot matrix with a diagonal broken by two short perpendicular jumps, showing two indels in otherwise colinear sequences">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="208" text-anchor="middle" font-size="12" fill="currentColor">sequence 1 (1 to n)</text>
  <text x="16" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 16 105)">sequence 2 (1 to m)</text>
  <g fill="currentColor">
    <circle cx="55" cy="175" r="2.2"/><circle cx="65" cy="165" r="2.2"/><circle cx="75" cy="155" r="2.2"/>
    <circle cx="85" cy="145" r="2.2"/><circle cx="95" cy="135" r="2.2"/>
    <circle cx="95" cy="123" r="2.2"/><circle cx="95" cy="111" r="2.2"/><circle cx="95" cy="99" r="2.2"/>
    <circle cx="105" cy="89" r="2.2"/><circle cx="115" cy="79" r="2.2"/><circle cx="125" cy="69" r="2.2"/>
    <circle cx="135" cy="59" r="2.2"/>
    <circle cx="147" cy="59" r="2.2"/><circle cx="159" cy="59" r="2.2"/>
    <circle cx="169" cy="49" r="2.2"/><circle cx="179" cy="39" r="2.2"/><circle cx="189" cy="29" r="2.2"/>
  </g>
  <text x="100" y="116" font-size="11" fill="currentColor">insertion in seq 2</text>
  <text x="152" y="76" text-anchor="middle" font-size="11" fill="currentColor">insertion in seq 1</text>
</svg>
<figcaption>A single broken diagonal: the sequences are colinear and similar almost end to end,
with a short run of extra residues in each — the case for a global alignment.</figcaption>
</figure>

A vertical run of dots at fixed $x$ means extra residues in sequence 2 with nothing to match in
sequence 1 (or equally a deletion in 1 — the picture can't say which); a horizontal run means the
reverse. A single diagonal broken by a few such runs says the sequences are homologous end to end
and differ mainly by a few indels.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Dot matrix with two parallel diagonals sharing the same vertical span, showing one segment of sequence 2 matching two separate regions of sequence 1">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="208" text-anchor="middle" font-size="12" fill="currentColor">sequence 1 (1 to n)</text>
  <text x="16" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 16 105)">sequence 2 (1 to m)</text>
  <g fill="currentColor">
    <circle cx="65" cy="175" r="2.2"/><circle cx="75" cy="160" r="2.2"/><circle cx="85" cy="145" r="2.2"/>
    <circle cx="95" cy="130" r="2.2"/><circle cx="105" cy="115" r="2.2"/><circle cx="115" cy="100" r="2.2"/>
    <circle cx="205" cy="175" r="2.2"/><circle cx="215" cy="160" r="2.2"/><circle cx="225" cy="145" r="2.2"/>
    <circle cx="235" cy="130" r="2.2"/><circle cx="245" cy="115" r="2.2"/><circle cx="255" cy="100" r="2.2"/>
  </g>
  <text x="90" y="95" text-anchor="middle" font-size="11" fill="currentColor">copy 1</text>
  <text x="230" y="95" text-anchor="middle" font-size="11" fill="currentColor">copy 2</text>
</svg>
<figcaption>Two parallel diagonals spanning the same stretch of sequence 2: that segment occurs
twice in sequence 1 — a repeated domain, the case for a local alignment.</figcaption>
</figure>

Here the same segment of sequence 2 lines up against two separate, non-adjacent regions of
sequence 1. A global alignment, which must decide on one correspondence between every residue of
one protein and every residue of the other, has no principled way to choose which copy to align to
and gets confused; a local alignment, free to report only the well-matched regions, correctly finds
both.

## Gaps and their penalties

An inserted or deleted run of residues ("indel") is scored separately from substitutions, by one of
two standard schemes: **linear**, $\gamma(n) = nA$ for $n$ gap positions and a (negative) per-gap
penalty $A$; or **affine**, $W_n = G + n\gamma$ (or $G+(n-1)\gamma$, with the opening cost defined
differently), with a gap-opening penalty $G$ and a smaller extension penalty $\gamma$.

Gaps are penalized more harshly than an average mismatch because indel mutations are rarer than
substitutions — roughly tenfold rarer even at the single-nucleotide level — and an in-frame
amino-acid indel needs a whole codon's worth of change, rarer still. Affine, rather than a bigger
linear penalty, reflects that indels cluster: one mutational event often inserts or deletes several
residues at once, so a four-residue insertion shouldn't cost four times a one-residue insertion —
only one event occurred. Affine charges the rare "decision to open a gap" once and something
smaller per additional residue; both schemes see use in practice.

## Needleman-Wunsch: global alignment by dynamic programming

The question is how to find the single best end-to-end alignment of two sequences, written one
across the top of a grid and one down the side. The key idea, elicited step by step in lecture, is
*dynamic programming*: break the expensive problem of aligning whole sequences into cheap
subproblems of aligning their *prefixes*, solve the smallest first, and build outward.

Let $S_{i,j}$ be the optimal alignment score of the first $i$ residues of sequence 1 against the
first $j$ of sequence 2. Given $S_{i-1,j-1}$, $S_{i-1,j}$, $S_{i,j-1}$, the next cell is whichever
move is best — align residue $i$ with $j$ (diagonal), gap in sequence 2 opposite $i$ (horizontal),
or gap in sequence 1 opposite $j$ (vertical):

$$S_{i,j} = \max\left\{\, S_{i-1,j-1} + \sigma(x_i, y_j),\ \ S_{i-1,j} + A,\ \ S_{i,j-1} + A \,\right\},$$

with $\sigma$ the substitution matrix (e.g. PAM250) and $A$ the linear gap penalty. The first
row/column are unambiguous ($i$ or $j$ gaps against nothing else), so $S_{i,0}=iA$, $S_{0,j}=jA$.
Each cell also records which option won (an arrow). $S_{n,m}$, the bottom-right corner, is the
optimal global score; tracing the arrows back to the origin — the **traceback** — reads off the
alignment: diagonal = aligned pair, horizontal/vertical = a gap.

**Worked example.** Align `VDSCY` (top) against `VESLCY` (side), PAM250, linear gap $A=-8$. First
row/column: $0,-8,-16,\dots$ First cell, V against V:

$$S_{1,1} = \max(0+\sigma(V,V),\ -16,\ -16) = \max(4,-16,-16)=4 \quad(\text{diagonal}),$$

using $\sigma(V,V)=+4$. Next, the second top-sequence residue (D) against the first side residue
(V):

$$S_{2,1} = \max(4-8,\ -8+\sigma(D,V),\ -16-8) = \max(-4,-10,-24) = -4 \quad(\text{horizontal}),$$

using $\sigma(D,V)=-2$. Filling the rest of the grid the same way and tracing back from the
bottom-right corner gives this path, with running score:

| step | pair | PAM250 score | running total |
|---|---|---|---|
| 1 | V / V | $+4$ | 4 |
| 2 | D / E | $+3$ | 7 |
| 3 | S / S | $+2$ | 9 |
| 4 | – / L (gap) | $-8$ | 1 |
| 5 | C / C | ($+12$)$^{*}$ | 13 |
| 6 | Y / Y | $+10$ | 23 |

($^{*}$never read out loud, but the running totals given — 1, then 13 — pin it down: this PAM250's
cysteine–cysteine entry is $+12$.) The optimal global alignment, score 23:

```
V D S - C Y
V E S L C Y
```

The gap falls exactly where it must: the top sequence is one residue short, and the only way to let
both serines and both cysteines line up is to place that shortfall opposite the L.

## Semiglobal alignment

A variant for proteins well conserved across a shared core but with a few extra residues dangling
off one end — a signal peptide, a tag, N/C-terminal "flutter" that doesn't matter functionally.
Semiglobal alignment runs the identical recursion but initializes the first row/column to $0$ (no
penalty for leading gaps) and lets the traceback start at the highest score anywhere in the *last*
row or column, rather than forcing it to the bottom-right corner — the alignment still runs to the
end of one sequence, with unpenalized overhang on the other.

## Smith-Waterman: gapped local alignment

Two proteins can share a well-matched internal region without being homologous end to end (the
repeated-domain dot matrix above). Smith-Waterman modifies Needleman-Wunsch to find such a region
directly: add a fourth option, $0$, resetting whenever the other three would all be negative —

$$S_{i,j} = \max\left\{\, S_{i-1,j-1} + \sigma(x_i,y_j),\ \ S_{i-1,j}+A,\ \ S_{i,j-1}+A,\ \ 0 \,\right\}.$$

A cell landing on $0$ gets no arrow — a fresh potential start, the same "reset to zero" trick used
for ungapped local alignment. The traceback starts at whichever cell in the *entire* matrix holds
the highest score and runs backward until it hits a $0$.

This keeps the constraint that made ungapped local alignment work: the average score of a random
residue pair must be negative, or the matrix would grow everywhere, the reset would almost never
trigger, and no region would stand out. Unlike Needleman-Wunsch, which tolerates an all-positive
matrix and still traverses the whole grid regardless of sign, Smith-Waterman genuinely needs that
negative drift.

## Amino acid substitution matrices: where the scores come from

Scoring identical residues as matches and everything else as a flat mismatch is a poor model:
cysteines form disulfide bonds and are structurally far more consequential than their raw frequency
suggests, so a matrix ought to reward a cysteine match more than an alanine match. More generally,
any scoring system carries an implicit model of molecular evolution: a high score for a pair is, in
effect, a claim that the pair interchanges relatively often, and a good scoring system makes that
claim deliberately.

Dayhoff's PAM matrices (1978) made the model explicit, and PAM250's structure is visible just by
inspection: it is **symmetric** (A$\to$B assumed as frequent as B$\to$A); the **diagonal**
(self-match) scores vary widely, roughly 2 to 17 — tryptophan scores far higher against itself than
serine, because tryptophans are rare and structurally demanding (two aligned is unlikely to be
chance), and cysteines are similarly conserved for their disulfide bonds; and **off-diagonal
positive scores cluster by side-chain chemistry**, not alphabetically — basic residues (His, Arg,
Lys) together, acidic/amide residues (Asp, Glu, Asn, Gln) together (Asp$\to$Glu scores $+3$, nearly
as good as a true match), and small hydrophobics (Met, Ile, Leu, Val) scoring positively against
each other, consistent with being interchangeable inside, say, a transmembrane helix.

The construction: start from alignments confident enough to need no statistics — protein families
around 85% identical, unambiguous by eye — and count raw substitution events ($n_{ab}$): e.g. of
1000 aligned phenylalanines, 900 stayed, 100 changed (80 to tyrosine, 3 to tryptophan, 2 to
histidine, ...). These alignments are ~15% diverged, so scaling the frequencies down by roughly
that factor gives the **PAM1** matrix — substitutions for proteins 1% diverged. Treating
substitution as (approximately) a Markov process — the next residue depends only on the current
one, not its history — lets PAM1 be raised to higher matrix powers for greater distances: PAM10,
PAM100, PAM250. "PAM250" sounds paradoxical (over 100% changed?), but it describes a process run
long enough that *on average* each position changes 2.5 times: many positions never change, a few
change repeatedly, and some that changed may revert, so observed divergence saturates well below
100% even as the underlying process accumulates "250% worth" of events.

## Markov chains: the model underneath the matrix

The matrix-powers trick above works only because substitution is (approximately) a Markov chain,
introduced with a genealogical cartoon: a mutation at one locus arises between "Grandpa" and his
son, a second between the son and his own child. Treat the genotype at that locus in each
generation as a random variable — $X_1$ Grandpa, $X_2$ the son, $X_3$ the grandchild — so that
$X_1,X_2,X_3,\dots$, indexed by generation, form a **discrete stochastic process**.

A Markov chain is a stochastic process with the **Markov property**: the conditional distribution
of the next state given the entire past depends only on the current state,

$$P(X_{n+1} = j \mid X_1=x_1,\dots,X_n=x_n) \;=\; P(X_{n+1}=j \mid X_n = x_n)$$

for all states and all $n$ — the future is conditionally independent of the past given the present.
In the pedigree, the grandchild's genotype depends on the son's and nothing else: Grandpa's is
irrelevant once the son's is known, because the son is the one who transmits DNA. This is exactly
the property licensing independent 1%-divergence steps to be chained by matrix multiplication into
PAM100 or PAM250. It leans on conditional probability, $P(A\mid B)$, which the next lecture
(comparative genomics) develops properly.

## Exercises

**Problem set 3** — set across several lectures; only part of it exercises this chapter's material.
Rewritten here without solutions.

**P1. Gibbs sampler (10 points).** You are studying longevity in species A and B. A transcription
factor, AGE, regulates aging- and stress-related pathways in both by binding target-gene
promoters. Two FASTA files hold 30 bp sequences immediately upstream of AGE target genes —
`seqsA.fa` (species A), `seqsB.fa` (species B) — and the goal is an enriched motif in each,
found by implementing a Gibbs sampler.

- *(A, 6 points)* Complete the skeleton `gibbsSampler.py` (a FASTA file and motif length as input).
  Run 1000 iterations on `seqsA.fa` with motif length 7, repeat ~10 times, keep the highest-scoring
  run. Report its background distribution, final weight matrix, motif score, and relative entropy,
  and plot relative entropy against iteration. What shape is the plot? What is the consensus motif?
- *(B, 1 point)* Using `printToLogo()`, produce aligned motifs after 1000 iterations and render each
  as a WebLogo sequence logo, for at least three separate runs, reporting relative entropy and score
  alongside each. What differences appear between runs, and why does the sampler return different
  motifs on different runs?
- *(C, 2 points)* Repeat the search (length 7) on `seqsB.fa`. Report the background distribution,
  final weight matrix, motif score, and relative entropy for a representative run. How does the
  relative entropy compare to species A's, and does that make the motif easier or harder to find in
  B? Why?
- *(D, 1 point)* Assuming one motif occurrence per sequence still holds, what happens if the
  sequences get longer? Run the sampler on `seqsAext.fa` (length 90, not 30) several times and plot
  relative entropy against iteration for a high-scoring run. How does this differ from part (A), and
  why?

**P2. RNA secondary-structure prediction (5 points).**

- *(A, 3 points)* Using the Nussinov algorithm, find the secondary structure maximizing the number
  of Watson-Crick base pairs in `CGAGUCGGAGUC`. Show your work.
- *(B, 2 points)* Submit the same sequence to the mfold RNA-folding server (default parameters);
  its top two structures will not match the Nussinov structure from (A). Using the real RNA
  secondary structures shown elsewhere in the course, hypothesize which feature of mfold's
  thermodynamic model rules out the Nussinov structure, and test it by inserting the minimum number
  of adenosines at strategic positions (loops, between stems, across bulges) so mfold's top
  structure pairs the same bases the Nussinov structure did.

**P3. Protein structure with PyRosetta (6 points).** Throughout, the protein under study is PDB
entry 1YY8.

- *(A, 1 point)* Look up 1YY8 in the Protein Data Bank. What is this molecule, and — from its 3D
  view — is its predominant secondary structure $\alpha$-helix or $\beta$-sheet?
- *(B, 1 point)* Using `pyRosetta_1YY8.py`'s `part_b()`, load `1YY8.clean.pdb` and print its
  backbone angles and energy score. What is the total energy, and which categories are the largest
  contributors for and against it (in words, not short codes)?
- *(C, 1 point)* `part_c()` performs Monte Carlo side-chain packing. Add code to print the
  post-packing energy score. What is the energy after packing, and which two categories decreased
  most relative to part (B)?
- *(D, 1 point)* `1YY8.rotated.pdb` is identical to the clean structure except that one residue's
  $\phi$ or $\psi$ angle differs. Complete `part_d()` to load it, pack side chains, and print the
  energy before and after. What are those energies, and why doesn't the post-packing energy match
  the one from part (C)?
- *(E, 1 point)* Complete `part_e()` to identify which residue and which backbone angle ($\phi$ or
  $\psi$) differs between the clean and rotated structures.
- *(F, 1 point)* Using that residue and angle, complete `part_f()` to compute the energy for every
  integer angle from $-180$ to $180$, feeding the `energy_vs_angle.pdf` plot. Which angle gives the
  lowest energy, and does it agree with that residue's angle in the original (part B) structure?

**P4. Queuing theory and connections (4 points).** A bank is deciding whether it can afford to
promise free checking for a year (worth \$150) to any customer who waits more than 15 minutes.
Each minute the bank is open, the line grows by one customer with probability $\tfrac14$ and —
if a line exists — shrinks by one with probability $\tfrac34$. Let $X$ be the probability that,
over a 12-week reference period, the line never exceeds 10 people, and $Y$ the probability that,
over a 12-week promotional period, it never exceeds 15. The bank is open 2400 minutes per week.
Using an equation covered in class, calculate $\ln(X)/\ln(Y)$.

## Sources

- Slides: `lectures/03-slides.md` (MIT 7.91J, Spring 2014, Lecture 3, C. Burge, Feb. 11 2014) —
  local-alignment recap and statistics, mismatch-penalty formula, BLAST flavors table, "Why align
  protein sequences", convergent-evolution examples, dot-matrix examples, gap-penalty definitions,
  the Needleman-Wunsch dynamic-programming setup, the PAM1-construction slide (Phe substitution
  counts), the DNA-pedigree slide, and the formal Markov-chain definition.
- Transcript: `recordings/lectures/03.md` — the worked reasoning used throughout: the
  lambda/mismatch-penalty discussion including the 66%-identity, $m=-2$ example (`[08:44]`–
  `[13:02]`), translated-search examples with chimp and mouse (`[17:23]`–`[23:01]`),
  convergent-evolution discussion (`[24:09]`–`[31:55]`), dot-matrix reasoning (`[31:55]`–`[36:22]`),
  gap-penalty rationale (`[36:22]`–`[40:44]`), the full Needleman-Wunsch worked example with running
  scores (`[44:51]`–`[1:02:22]`), semiglobal alignment (`[1:02:22]`–`[1:03:30]`), Smith-Waterman
  (`[1:03:30]`–`[1:08:55]`), the PAM250 discussion (`[1:08:55]`–`[1:14:39]`), and the Markov-chain
  introduction (`[1:14:39]`–`[1:19:12]`).
- Exercises: `psets/03-questions-pset3-ques/01-p1-gibbs-sampler-10-points.md`,
  `02-p2-rna-secondary-structure-prediction-5-points.md`,
  `03-p3-protein-structure-with-pyrosetta-6-points.md`, and `psets/03-questions.md` (Problem Set 3,
  due Thursday April 3; P4 is taken from `03-questions.md`, the only one of the two conversions
  that includes it — the pset's own worked solutions were not reproduced here).
- Not reconstructed here: the sequencing-library Q&A at the start of the lecture (transcript
  `[00:00]`–`[04:08]`); the BLASTN web-interface screenshots (slide images only, no text); the
  textbook pages the slides point to (Z&B — Zvelebil & Baum, *Understanding Bioinformatics* —
  Chapters 4–5, especially pp. 119–125, not supplied as course material here).

---

[← 2. Sequencing Platforms and BLAST Statistics](02-sequencing-platforms-and-blast-statistics.md) · [Contents](index.md) · [4. Markov Models and Comparative Genomics →](04-markov-models-and-comparative-genomics.md)
