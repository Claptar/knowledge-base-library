---
title: "4. Markov Models and Comparative Genomics"
course: "MIT 7.091J"
chapter: 4
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Markov Models and Comparative Genomics

## What this covers

This lecture closes out pairwise alignment — how Dayhoff's PAM matrices and the later BLOSUM
matrices were actually built, and why multiple sequence alignment of more than a handful of
proteins is computationally hopeless by the direct generalisation of Needleman-Wunsch — and then
turns to the Markov chain as a model of sequence evolution: the stationary distribution, the
Jukes-Cantor correction for multiple hits at a site, the $K_a/K_s$ test for selection on
protein-coding sequence, and a run through several comparative-genomics case studies that this
machinery sets up. It assumes the Needleman-Wunsch and Smith-Waterman algorithms and gap penalties
from the previous lecture, and basic conditional probability and matrix-vector multiplication.

## Review: substitution matrices and the cost of multiple alignment

Pairwise alignment of two length-$n$ sequences, global or local, with linear gap penalties, costs
$O(n^2)$: the algorithm fills an $n\times n$ table. Affine gap penalties (separate gap-opening and
gap-extension costs) do not change this — they add a fixed, small number of extra quantities to
track at each cell, not a number that grows with $n$ — so the cost is still $O(n^2)$, with a larger
constant.

Dayhoff's PAM matrices come from alignments about 85% identical. She measured how often each amino
acid is observed to mutate into each other one (its "mutability"), rescaled these mutation
probabilities so that, on average, 1% of residues change in one unit of evolutionary time — that
calibration is what "1 PAM" means — and scored each substitution by the log-odds of seeing it
against background amino-acid frequency, rounded to a convenient integer. Because the underlying
object is a one-generation transition matrix $M$, longer evolutionary distances come purely from
matrix multiplication: $M^2$ gives PAM2, and recomputing the log-odds at each power gives the whole
series (PAM250, etc.) without re-deriving anything from alignments. The catch raised in lecture:
protein evolution over short and long time periods is not quite the same Markov process — this
substitution-only model ignores insertions, deletions, and whole proteins being born and lost — so
a matrix calibrated on 85%-identical pairs does not extrapolate perfectly to distant comparisons.

About twenty years later, with far more sequence available, Henikoff and Henikoff built BLOSUM
matrices from *blocks* — ungapped regions of only moderate similarity across many more, often more
distantly related, protein families (BLOSUM62 uses blocks no more than 62% identical) — rather than
near-identical alignments. For very similar proteins almost any reasonable matrix gives the same
alignment; the choice mostly matters for distant comparisons, which is the regime BLOSUM62 targets.
It has the same qualitative shape as a PAM matrix (positive diagonal, tryptophan and cysteine
scoring high), though cysteine's score is less extreme than its very low short-term mutability
would suggest — plausibly because disulphide bonding gets rewired over long evolutionary time even
though cysteines rarely change over short stretches.

Multiple sequence alignment inherits the dynamic-programming idea but not its cost. A direct
generalisation of Needleman-Wunsch to three sequences fills an $n\times n\times n$ cube, at cost
$O(n^3)$; for $k$ sequences it is $O(n^k)$ — with proteins some hundreds of residues long, aligning
even 20 sequences this way is simply impractical, not a question of a faster computer. Real
multiple aligners (ClustalW/ClustalX being the standard default) instead align the two closest
sequences first, then progressively bring in the next-closest sequence or profile. This is fast and
usually reasonable, but unlike the exhaustive $k$-dimensional program it is not guaranteed to find
the globally optimal alignment.

## Markov chains as a model of sequence evolution

A discrete stochastic process $X_1, X_2, X_3, \dots$ has the **Markov property** if
$$P(X_{n+1} = j \mid X_1=x_1, \dots, X_n = x_n) = P(X_{n+1} = j \mid X_n = x_n)$$
for all states $x_i$, $j$, and $n$: the future is conditionally independent of the past, given the
present. Genotype inheritance along a lineage is an example — conditional on a parent's genotype, a
grandchild's genotype tells you nothing extra about the grandparent's. The lecture's running example
is the base occupying one genomic site across generations: let $S_n$ be that base at generation
$n$, modelled as a Markov chain on $\{A,C,G,T\}$.

Such a chain is described by a $4\times 4$ transition matrix $P$ with $P_{ij} = P(S_{n+1} = j \mid
S_n = i)$ (rows summing to 1), together with a vector $\vec q^{\,n} = (q_A^n, q_C^n, q_G^n, q_T^n)$
of the probabilities of each base at generation $n$. The update rule is vector-matrix
multiplication,
$$\vec q^{\,n+1} = \vec q^{\,n} P, \qquad \vec q^{\,n+k} = \vec q^{\,n} P^k.$$

**Stationary distributions.** What happens to $\vec q^{\,n}$ as $n \to \infty$? The classical
answer (quoted, not derived, in lecture): if every entry of $P$ is strictly positive, there is a
unique vector $\vec r$ with $\vec r = \vec r P$ — $P$ does not move it, so $\vec r$ is the
**stationary distribution** — and $\lim_{n\to\infty} \vec q P^n = \vec r$ for *every* starting
$\vec q$, so $\vec r$ is also the **limiting distribution**, depending only on $P$, never on where
the chain started.

Worked examples, using a two-letter alphabet (purine $R$ versus pyrimidine $Y$):

- **Symmetric mutation**, $P = \begin{pmatrix} 1-p & p \\ p & 1-p\end{pmatrix}$. Guess $(1/2,1/2)$ by
  symmetry: if $R$ is more abundant, more mass flows $R\to Y$ than $Y\to R$ each generation (same
  rate $p$, unequal pools), shrinking the imbalance until the flows balance. Solving $\vec r = \vec
  r P$ for $\vec r=(x,1-x)$ gives $x = x(1-p)+(1-x)p$, i.e. $2px=p$, so $x=1/2$.
- **Asymmetric mutation**, $P = \begin{pmatrix} 1-p & p \\ q & 1-q\end{pmatrix}$, $p\neq q$. Flux
  balance now requires $xp=(1-x)q$, giving stationary distribution $\left(\tfrac{q}{p+q},
  \tfrac{p}{p+q}\right)$ — the type that mutates away more slowly ends up more abundant.
- **The identity matrix** (no mutation): every vector is trivially stationary, since $\vec r I=\vec
  r$. No contradiction — the theorem needs every entry strictly positive, which fails here.
  Wherever the chain starts is where it stays.
- **The "swap" matrix**, $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ (flips every generation):
  $(1/2,1/2)$ is stationary, but a chain started at a pure state never converges to it — it
  oscillates forever. Stationary, not limiting; again a zero entry breaks the hypothesis.

## The Jukes-Cantor model and correcting for multiple hits

Jukes and Cantor's model has a single mutation probability $\alpha$ from each base to *each* of the
other three, so the total substitution probability per generation is $3\alpha$. Writing $P_G(t)$
for the probability of still being (or having returned to) $G$ at time $t$ having started at $G$,
the recursion
$$P_G(t+1) = P_G(t)(1-3\alpha) + \big(1-P_G(t)\big)\alpha$$
(already-$G$-and-didn't-mutate, or not-$G$-and-mutated-back) solves to
$$P_G(t) = \frac14 + \frac34 e^{-4\alpha t},$$
which $\to 1/4$ as $t\to\infty$ — consistent with the uniform stationary distribution that the
model's full symmetry implies.

The useful consequence is a correction for measured sequence divergence. Let $D$ be the *observed*
fraction of differing sites between two aligned sequences, and $K$ the *true* expected number of
substitutions per site. Back-mutation and repeated hits at a site mean $D$ underestimates $K$ once
enough time has passed; algebra on the recursion gives
$$K = -\frac34 \ln\!\left(1 - \frac{4D}{3}\right).$$

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="The Jukes-Cantor corrected distance K rises nearly linearly for small D and diverges as D approaches three quarters">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="280" y1="180" x2="280" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <polyline points="40,180 72,174.8 104,168.7 136,161.4 168,152.3 200,140.1 232,121.5 248,106.7 264,81.5 270,65 277,25" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="300" y="198" text-anchor="end" font-size="12" fill="currentColor">D, fraction of sites differing</text>
  <text x="15" y="25" text-anchor="start" font-size="12" fill="currentColor">K</text>
  <text x="280" y="196" text-anchor="middle" font-size="11" fill="currentColor">3/4</text>
</svg>
<figcaption>K = -3/4 ln(1 - 4D/3): linear for small D, diverging as D approaches 3/4, the fraction of
sites expected to differ once two sequences have been randomised relative to each other.</figcaption>
</figure>

For small $D$, $K\approx D$: not enough time has passed for back-mutations to matter. As $D$ grows
the curve bends upward, diverging as $D\to 3/4$ — two sequences with no remaining correlation are
just independent draws from the uniform distribution over four bases, matching with probability
$1/4$, so $D$ cannot exceed $3/4$. This is why the correction matters: human and chimp sequences
differ at only about 1% of sites, so $D\approx K$ and no correction is needed, but human and mouse
sequences differ at perhaps half their sites, where the raw 50% badly underestimates the true
number of substitutions because many sites have mutated more than once — including back to the
ancestral base. The correction formula is what turns the raw count into a quantity proportional to
elapsed time.

Real nucleotide substitution is not quite this symmetric. Kimura's model gives transitions
(purine$\leftrightarrow$purine or pyrimidine$\leftrightarrow$pyrimidine) a higher probability than
transversions — observed roughly 2–3 times more often — and still has a uniform stationary
distribution, by the symmetry that remains. More recent models make mutability depend on a base's
neighbour: in vertebrates, methylation machinery methylates C's immediately 5′ of a G (CpG
dinucleotides), and a methylated C deaminates to T at roughly ten times the background rate —
captured only by a 16-state (dinucleotide) chain, harder to solve by hand but easy to explore by
direct simulation, since the convergence theorem guarantees a stationary distribution exists. There
are even strand-specific models, reflecting asymmetries from transcription-coupled repair.

## Measuring selection with $K_a/K_s$

Aligning two orthologous coding sequences codon by codon in a known reading frame lets every
substitution be classified as **nonsynonymous** ($K_a$, or $d_N$) — it changes the encoded amino
acid — or **synonymous** ($K_s$, or $d_S$) — it does not. Each codon *position* is likewise a
nonsynonymous or synonymous *site*, by how many of the three possible substitutions there would be
synonymous. Worked example: glycine's four-fold degenerate codon $\text{GG}N$ — the third position
is a synonymous site, the first two are nonsynonymous. To a first approximation each codon
contributes one synonymous and two nonsynonymous sites, giving
$$K_a = \frac{\text{nonsynonymous substitutions}}{\text{nonsynonymous sites}}, \qquad
K_s = \frac{\text{synonymous substitutions}}{\text{synonymous sites}},$$
each corrected for multiple hits with the Jukes-Cantor formula above, applied to codons.

$K_a/K_s$ over a whole gene (say, human against its mouse ortholog) is read as:

- **$K_a/K_s \ll 1$ — purifying (negative) selection.** Mutation has no notion of the genetic code,
  so synonymous and nonsynonymous sites mutate at the same underlying rate; far fewer observed
  nonsynonymous substitutions means most that occurred were removed by selection because they
  damaged the protein. The overwhelming majority case: most proteins are already well adapted.
- **$K_a/K_s \approx 1$ — neutral evolution.** The region may not really be protein-coding, may be a
  pseudogene no longer selected on, or — more speculatively — different parts or periods of the
  gene's history may be under opposing pressures that average out near 1, a case a $K_a/K_s$
  profile along the gene (rather than one gene-wide average) can expose.
- **$K_a/K_s \gg 1$ — positive selection.** The existing protein is actively disadvantageous, and
  selection favours change. Rare — probably under 1% of genes at a time — and tends to be recent
  and strong: host–pathogen arms races (a receptor a virus uses to enter cells, a toxin-encoding
  gene) or environmental mismatch (camouflage pigmentation after a habitat shift).

Caveat raised in discussion: the method assumes synonymous sites are neutral, which can fail too — a
synonymous change can still disrupt a splicing signal or RNA structure. One check is to compare a
gene's synonymous rate against neighbouring non-coding sequence.

## Comparative genomics: reading selection and function off whole genomes

Comparative genomics is described as an *approach* rather than a field: simple methods — aligning
or BLASTing sequences against each other — applied to the right sequences and the right question
give sharp biological insight. Several case studies followed.

**CRISPR spacers.** (Reported from the slides; the supplied transcript does not narrate this part.)
Bacterial CRISPR loci — clustered, regularly interspaced short palindromic repeats, associated with
a family of *cas* genes (Jansen et al. 2002) — carry short "spacer" sequences between the repeats.
Bolotin et al. (2005) found these spacers match sequences scattered across phage genomes (BLAST
hits along the phage map), and that, across *S. thermophilus* strains, the number of spacers in a
locus correlates with resistance to a phage panel (best-fit line $y=-0.02x+0.77$, $R^2=0.51$, for
strains short of full resistance).

**Ultraconserved elements (Bejerano et al.).** Using whole-genome alignments of human, mouse and
rat, Bejerano and colleagues asked whether anything in the mammalian genome is *completely*
conserved. They estimated a neutral background mutation rate from ancestral repetitive elements
(present before the three species diverged, and assumed free of selection), finding three-way
identity of these neutral sequences never above about 0.68 — so a run of 200 identical bases across
all three species is astronomically unlikely by chance, which is how "ultraconserved element" was
defined: hundreds of bases, 100% identical in all three genomes. Several hundred turned up: roughly
100 overlap exons ("type 1"), roughly 100 fall in introns, the rest are intergenic ("type 2"). Type
1 genes were strikingly enriched for RNA-binding proteins, especially splicing factors; type 2
elements sit near genes enriched for transcription factors, especially homeobox genes.

A follow-up from Pennacchio and Rubin's group tested 167 of these sequences as candidate enhancers,
fusing each upstream of a minimal promoter driving *lacZ* and staining whole-mount mouse embryos.
About 45% drove a reproducible expression pattern (forebrain, midbrain, neural tube, limb) — many
are developmental enhancers. Elements at 100% identity and others at merely ~95% behaved
indistinguishably: the 100% threshold was arbitrary, even though it had picked out genuinely
interesting regulatory elements.

Bejerano later noticed something unexpected comparing against the newly sequenced coelacanth — a
"living fossil" fish essentially unchanged across 300–400 million years of fossil record. Its genome
carries a common, roughly 500-base repeat resembling a SINE (like a human Alu) that closely
resembles some mammalian ultraconserved enhancers. Proposed explanation: a repeat starts out purely
parasitic, inserting randomly; but once hundreds of copies are scattered through the genome, some
will by chance sit near a set of genes worth regulating together, and a transcription factor can
then evolve relatively easily to bind the shared sequence, instantly coordinating every gene that
carries it nearby, with unwanted targets tuned out later by selection. Roughly half the human genome
derives from transposons if traced back far enough, and this may be how many regulatory elements,
not only these, originated.

Not all ultraconserved elements are intergenic: one sits inside the splicing-factor gene SRp20, in
a roughly 600-nucleotide, non-coding exon reported as essentially completely conserved across the
three species. Including this exon introduces a premature stop codon, so transcripts that include it
are degraded by nonsense-mediated decay rather than making protein — negative autoregulation, since
rising SRp20 protein promotes inclusion of its own "poison exon." Why it needs 600 nucleotides of
near-perfect conservation to do this is left open.

**MicroRNA targeting rules (Lewis et al.).** MicroRNAs are cut from hairpin precursors by the
nuclear enzyme Drosha, exported, and trimmed to their mature ~21–22 nucleotide form by Dicer; the
mature microRNA loads into RISC, which pairs it against mRNA targets — usually in the 3′ UTR — to
repress translation or trigger decay. They matter: *Drosophila bantam* represses the pro-apoptotic
gene *hid*, and flies lacking it lose almost all their cells to apoptosis. Lewis and colleagues
asked which part of a microRNA determines its targets, using human/mouse/rat alignments: counting
conserved 7-mer matches in 3′ UTRs to different windows of each known microRNA, against the count
from shuffled microRNA sequences as background. A significant excess appeared only for oligomers
matching bases 2–8 — no other window showed a signal — and alignments of paralogous microRNAs
within a family (*let-7* was shown) confirmed it: the 5′ end is the most conserved part of the whole
precursor and the loop the least, consistent with bases 2–8, the "seed," being what targeting
depends on.

**Dscam: a splicing code found by comparison (Graveley).** *Drosophila Dscam* has four clusters of
mutually exclusive alternative exons — 12 versions of exon 4, 48 of exon 6 — and any one transcript
includes exactly one exon per cluster. Sequencing this locus across flies and other insects,
Graveley found a short, strongly conserved sequence just downstream of the constant exon upstream of
a cluster (a "docking site"), and, upstream of *every* alternative exon, another short conserved
sequence (a "selector"). The docking-site consensus turned out complementary to the selector
consensus, suggesting splicing works by RNA base-pairing between the docking site and the selector
of whichever single exon is included, bringing that exon's splice site into use while the rest loop
out and are skipped — subsequently confirmed experimentally.

<figure>
<svg viewBox="0 0 380 200" role="img" aria-label="A docking site base-pairs with the selector sequence of one alternative exon, splicing it in while the others loop out and are skipped">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <polygon points="0,0 10,5 0,10" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="10" y="70" width="50" height="30" fill="none" stroke="currentColor"/>
  <text x="35" y="89" text-anchor="middle" font-size="11" fill="currentColor">exon 5</text>

  <rect x="65" y="70" width="25" height="30" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="77" y="89" text-anchor="middle" font-size="9" fill="currentColor">dock</text>

  <rect x="112" y="70" width="20" height="30" fill="none" stroke="currentColor"/>
  <text x="122" y="89" text-anchor="middle" font-size="8" fill="currentColor">sel</text>
  <rect x="135" y="70" width="55" height="30" fill="none" stroke="currentColor"/>
  <text x="162" y="89" text-anchor="middle" font-size="11" fill="currentColor">exon 6.1</text>

  <rect x="198" y="70" width="20" height="30" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="208" y="89" text-anchor="middle" font-size="8" fill="currentColor">sel</text>
  <rect x="221" y="70" width="55" height="30" fill="none" stroke="currentColor"/>
  <text x="248" y="89" text-anchor="middle" font-size="11" fill="currentColor">exon 6.2</text>

  <rect x="289" y="70" width="20" height="30" fill="none" stroke="currentColor"/>
  <text x="299" y="89" text-anchor="middle" font-size="8" fill="currentColor">sel</text>
  <rect x="312" y="70" width="55" height="30" fill="none" stroke="currentColor"/>
  <text x="339" y="89" text-anchor="middle" font-size="11" fill="currentColor">exon 6.3</text>

  <path d="M 77 70 Q 142 15 208 70" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="142" y="25" text-anchor="middle" font-size="10" fill="currentColor">selector-docking pairing</text>

  <path d="M 60 100 Q 155 165 221 100" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="155" y="152" text-anchor="middle" font-size="10" fill="currentColor">splice joins exon 5 to 6.2, skipping 6.1</text>
</svg>
<figcaption>Each alternative exon carries a short selector sequence complementary to a single
docking site upstream of the cluster; pairing with one selector brings that exon's splice site into
use and loops the others out.</figcaption>
</figure>

## Exercises

### Problem set 4

This problem set was assigned across several lectures, and its three questions are not specifically
about today's material — Bayesian networks, structure refinement in PyRosetta, and mutual
information in a multiple sequence alignment. Included here only because it shares this lecture's
number.

**P1. Bayesian networks (7 points).** Two Bayesian network structures are proposed over five binary
random variables $A,B,C,D,E$, each a gene that is ON or OFF. Network 1 has edges $A\to C$, $A\to E$,
$B\to D$, $C\to E$, $D\to E$; Network 2 has edges $A\to B$, $A\to C$, $A\to D$, $B\to D$, $D\to E$.

(a) For each of the following, write the factorisation of $P(A,B,C,D,E)$ implied, and the minimum
number of parameters needed: (i) mutual independence; (ii) Network 1's independencies; (iii)
Network 2's independencies; (iv) no independence assumptions.

(b) Using Network 2 with $P(A=\text{ON})=0.6$ and the conditional-probability tables for $B,C,D,E$
supplied with the problem, compute (i) $P(A,B,C,D,E \text{ all ON})$; (ii) $P(E=\text{ON}\mid
A=\text{ON})$; (iii) $P(A=\text{ON}\mid E=\text{ON})$.

(c) Using the Pebl package on a subset of the Gasch et al. (2000) yeast stress-response microarray
data, learn the network structure that best explains it with Pebl's greedy learner, and report its
log score.

(d) Repeat with the data for gene *tcp1* removed. Predict first how the network should change; then
compare what *mcx1*'s expression actually depends on in the learned network against your
prediction, and suggest why they agree or disagree.

**P2. Refining protein structures in PyRosetta (7 points).** You are given the *E. coli* ribosome
recycling factor (PDB 1EK8) with several backbone dihedral angles rotated away from the deposited
structure. Refine it two ways.

(a) Implement greedy energy minimisation: at each step try each residue's $\phi$ and $\psi$ angle
changed by $\pm 1^\circ$, keep whichever change lowers the energy most, and stop once the
improvement falls below 1. Report the starting and final energy, and the iterations to convergence.

(b) Choose a simulated-annealing temperature $kT$ such that a structure at twice the current energy
would be accepted with probability 50% under the Metropolis criterion.

(c) Implement the Metropolis step itself: perturb a randomly chosen $\phi$ or $\psi$ by a draw from
$\mathrm{Normal}(0,20^\circ)$, and accept or reject by the Metropolis criterion using the $kT$ from
(b).

(d) Build an annealing schedule — a fixed number of Metropolis moves at the starting $kT$, then
halve $kT$ and repeat, stopping once $kT$ first drops below 1 — and report how many halvings it
takes. Compare, in at most two sentences, the resulting energy trace to the one from (a).

(e) Compare the rotated, energy-minimised, and simulated-annealing structures against the original
deposited structure by (i) the number of $\phi,\psi$ angles differing by more than $1^\circ$ and
(ii) RMSD. Which method recovers the original structure better here, and in what scenario would the
other be expected to do better instead?

**P3. Mutual information of protein residues (7 points).** Using a multiple sequence alignment of
the Cys/Met metabolism PLP-dependent enzyme family (Pfam PF01053):

(a) Give the maximum possible information content of an alignment column, in bits, for 20 possible
amino acids, and the formula for a column's information content in terms of amino-acid frequencies
$P_{aa}$. Compute it at every well-represented column, and report the maximum and where it occurs.

(b) Compute the mutual information between every pair of well-represented columns; report the
maximum value and the pair of positions where it occurs.

(c) Find the ten consecutive well-represented positions with the highest average mutual
information, and the corresponding stretch of the human sequence. Using the enzyme's tertiary
structure (Gao et al., *BMC Bioinformatics* 2011), suggest why these positions might covary.

## Sources

- Slides: `lectures/04-slides/01-global-alignment-of-protein-sequences-nw-sw-pam-blosum.md` (Markov
  model definition, DNA-sequence-evolution example, transition-matrix notation, and the CRISPR/cas
  gene-family and spacer-matching figures) and
  `02-number-of-spacers-is-correlated-with-resistance-to-phage.md` (phage-resistance correlation
  figure). Both reconstructed by a model from a PDF with no text layer; every equation on them is
  unverified and treated here only as a pointer into the original. Background reading cited there:
  Zvelebil & Baum, chapters 4–5. The deck is internally labelled "Lecture #6"; this chapter follows
  the course's own file numbering (lecture 4).
- Transcript: `recordings/lectures/04.md` — review of alignment, PAM and BLOSUM, and alignment
  complexity ([00:00]–[19:00]); Markov chains, stationary distributions, and Jukes-Cantor
  ([19:00]–[51:10]); $K_a/K_s$ and selection ([51:10]–[1:02:24]); comparative-genomics case studies
  ([1:02:24]–[1:21:42]). Donation notice and sign-off stripped.
- The CRISPR material above is reported from the slides alone — the supplied transcript does not
  narrate it.
- The lecturer named two further comparative-genomics examples he ran out of time to present — a new
  class of trans-acting factors inferred from the genomic locations of their own genes, and a
  repetitive element's function inferred from where it matches another genome — plus a set of
  "favorite" papers and a review by Sabeti on positive selection, posted on the course site but not
  supplied as input; none is reconstructed here.
- Exercises: problem set 4, each question taken once from the two duplicate conversions
  (`psets/04-questions/01-p1…`, `02-p2…`, `03-p3…` and `psets/04-questions-pset4-ques/01-p1…`,
  `02-p2…`); the network-edge diagrams and worked numerical answers in these conversions were used
  only to identify what was being asked, and are not reproduced here.

---

[← 3. Global Alignment and Scoring Matrices](03-global-alignment-and-scoring-matrices.md) · [Contents](index.md) · [5. Read Alignment with the BWT/FM Index →](05-read-alignment-with-the-bwt-fm-index.md)
