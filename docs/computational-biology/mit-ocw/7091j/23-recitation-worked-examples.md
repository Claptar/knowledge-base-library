---
title: "23. Recitation Worked Examples"
course: "MIT 7.091J"
chapter: 23
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 23. Recitation Worked Examples

## What this covers

Fourteen recitations ran alongside the 7.91J lectures from February to April 2014, each working
through the previous days' material with the numbers filled in. This chapter follows them in course
order rather than by date, keeping the worked examples the recitations actually carried out:
Bayesian motif scoring, a coin-flip hypothesis test, hand-filled alignment and RNA-folding matrices,
a Burrows-Wheeler exact-match trace, a small de Bruijn graph, a chi-squared and a Fisher's exact test
on the same SNP table, and more. It assumes the reader has met the corresponding lecture material —
PWMs, dynamic programming, HMMs for chromatin state, QTL mapping — and is here for the arithmetic
and worked reasoning the slides only sketch.

## Scanning and testing sequences: p-values and motif probability

A **position weight matrix (PWM)** scores a sequence against a motif as a product of independent
per-column multinomials. For $S=\text{GCAA}$, with $P(S\mid M)=0.01$, $P(S\mid B)=0.0016$ and prior
$P(M)=0.1$, Bayes' rule gives the posterior that the motif generated $S$:

$$P(M\mid S)=\frac{P(S\mid M)P(M)}{P(S\mid B)P(B)+P(S\mid M)P(M)}=\frac{0.01\times0.1}{0.0016\times0.9+0.01\times0.1}=0.41.$$

Scanning a genome this way scores every position, and the question becomes which scores are real.
The standard move is an **empirical null**: shuffle the chromosome and rescan, so any high score
there is known to be chance, not biology. Noble's CTCF example (*Nat. Biotechnol.* 27, 2009) reads
off p-values directly from that empirical distribution: $P(S>26.30)=1/68\text{M}=1.5\times10^{-8}$,
$P(S>17)=35/68\text{M}=5.5\times10^{-7}$.

General definition: a p-value is the probability, under $H_0$, of a statistic at least as extreme
as observed; with no canonical null, shuffle the data (or the labels) to build one. Worked directly:
flip a coin 10 times, see 8 heads. Under $H_0: p=0.5$, the one-tailed p-value is

$$P(x\ge8;10,0.5)=\sum_{x=8}^{10}\binom{10}{x}0.5^{10}=0.05469\quad(\text{not significant at }0.05),$$

and the two-tailed version (8+ heads *or* 8+ tails) gives $0.109$ — same data, different question,
different answer.

## Sequence alignment: dynamic programming and BLAST statistics

DP alignment builds each matrix entry from its left, top, and upper-left-diagonal neighbors (gap in
seq 1, gap in seq 2, match/mismatch). Three modes differ only in edge penalties and traceback start:

| | Global | Semiglobal | Local |
| :--- | :---: | :---: | :---: |
| Penalties at edges? | Yes | No | No |
| Reset negative entries to 0? | No | No | Yes |
| Traceback starts at | bottom-right | best in last row/col | best anywhere |

Worked example, `AWEK` vs `FWEF`, PAM250, gap $-2$. Local (resets to 0):

| | Gap | A | W | E | K |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Gap** | 0 | 0 | 0 | 0 | $-8$ |
| **F** | 0 | 0 | 0 | 0 | 0 |
| **W** | 0 | 0 | 17 | 15 | 13 |
| **E** | 0 | 0 | 15 | 21 | 19 |
| **F** | 0 | 0 | 13 | 19 | 17 |

giving `WE`/`WE` (score 21). Global (edge gaps charged):

| | Gap | A | W | E | K |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Gap** | 0 | $-2$ | $-4$ | $-6$ | $-8$ |
| **F** | $-2$ | $-4$ | $-2$ | $-4$ | $-6$ |
| **W** | $-4$ | $-6$ | 13 | 11 | 9 |
| **E** | $-6$ | $-4$ | $-6$ | 17 | 11 |
| **F** | $-8$ | $-6$ | $-4$ | 15 | 12 |

giving `AWEK`/`FWEF` (score 12) — forcing the whole sequence to align costs more than letting the
aligner keep only the matching core.

For local *ungapped* alignment (BLAST), $P(S>x)=1-e^{-KMNe^{-\lambda x}}$ ($M$ = query length, $N$ =
database length); discreteness needs $P(S\ge x)=P(S>x-1)$. The scale $\lambda$ solves
$\sum_{i,j}p_ir_je^{\lambda s_{ij}}=1$. With an arbitrary scoring matrix this has 16 terms and no
analytic solution; with a single match/mismatch score it reduces (via $y=e^x$) to a quadratic with a
unique positive solution; and the matrix must have negative *expected* score, or random sequences
would score positively on average and the tail statistics break down entirely.

## Clustering gene expression data

**K-means** alternates assigning points to the nearest centroid and recomputing centroids, minimizing
$J=\sum_n\sum_k r_{nk}\|x_n-\mu_k\|^2$; distance choices include Manhattan, Euclidean, Mahalanobis,
Pearson/uncentered/Spearman correlation, and absolute or squared correlation. **Hierarchical
clustering** instead starts with every point its own cluster and repeatedly fuses the least-dissimilar
pair; the *linkage* rule for comparing clusters (not points) matters — complete (max pairwise
distance), single (min), average/UPGMA (mean), or centroid (distance between means). Choosing $K$ or
where to cut the dendrogram can use

$$\text{BIC}=-2\times\text{log-likelihood}+d\log N,$$

accepting a cluster split only if BIC improves. **Biclustering** clusters rows and columns
simultaneously — a subset of genes behaving similarly across only a subset of conditions — with
structures ranging from a single bicluster to overlapping, hierarchically-nested ones (Madeira &
Oliveira's 2004 taxonomy).

## Models of molecular evolution

A Markov chain satisfies $P(S_{t+1}\mid S_1,\dots,S_t)=P(S_{t+1}\mid S_t)$; a distribution evolves as
$\vec q^{\,t+1}=\vec q^{\,t}P$, and if $P$ is strictly positive it has a stationary $\vec r=\vec rP$
(the left eigenvector at eigenvalue 1). Worked purine/pyrimidine model:

$$PAM_1=\begin{bmatrix}0.995&0.005\\0.015&0.985\end{bmatrix}\ \Rightarrow\ (P_R,P_Y)_{\text{stationary}}=(0.75,0.25)\ \Rightarrow\ PAM_\infty=\begin{bmatrix}0.75&0.25\\0.75&0.25\end{bmatrix}.$$

From 50/50 starting composition, expected identity to the $PAM_\infty$-evolved sequence is
$(0.75)(0.5)+(0.25)(0.5)=0.50$ — still half, even after "infinite" time, since self-return is
possible. PAM matrices extrapolate this way ($PAM_{250}\approx(PAM_1)^{250}$) from global alignments
of close relatives; **BLOSUM** matrices are instead built directly from local alignments at the
stated identity (BLOSUM62 from ~62%-identical blocks), which is why BLOSUM62 is BLAST's default for
moderate divergence. Reverted mutations ($A\to G\to A$) make raw differences underestimate true
substitutions; **Jukes-Cantor** corrects via $K=-\tfrac34\ln[1-\tfrac43P]$. The **$K_a/K_s$** ratio
(nonsynonymous per site over synonymous per site) diagnoses selection mode: $\ll1$ purifying (most
genes), $\approx1$ neutral (pseudogenes), $>1$ positive (e.g. immune genes vs. parasites).

## Genome assembly: from reads to a genome

**Library complexity.** With $C$ unique molecules, $N$ reads, and equal representation assumed, read
count per molecule is Poisson($\lambda=N/C$), so $P(\text{observed})=1-e^{-\lambda}$ and the MLE from
$M$ observed-unique molecules is $\hat C=M/(1-e^{-\lambda})$ — circular, since $\lambda$ itself
depends on $C$, and the equal-representation assumption fails badly in practice, motivating the
two-parameter negative binomial (overdispersion $k$) over the one-parameter Poisson.

**BWT and exact matching.** Naive read mapping costs $O(\text{genome}\times\text{reads})$ —
infeasible. For `BANANA$`, sorting all rotations lexicographically and taking the last column gives
BWT = `ANNB$AA`. Every column holds the same character multiset, so a character's **rank** (count of
identical characters above it, plus one) is the same lexical occurrence in first and last column —
which lets

$$\text{LF}(i,qc)=\text{occ}(qc)+\text{count}(i,qc)$$

map a BWT position to its first-column match ($\text{occ}$ = chars lexically smaller than $qc$;
$\text{count}$ = occurrences of $qc$ before position $i$). Exact match narrows a `[top,bottom)` range
by walking the query backward through two LF calls per step; searching `ANA` in `BANANA`
(top,bottom): $(0,7)\to(1,4)\to(5,7)\to(2,4)$ — final width 2, so two matches (`BNA` instead collapses
to top = bottom: no match). An offset is recovered by walking LF backward from `top` until `$`,
counting steps; the same walk from any index reconstructs the whole string from the BWT alone. Since
a real genome is too big for the full matrix, the **FM-index** keeps only an `occ` table and samples
`count`/offset at a subset of positions — this is what makes BWT aligners (Bowtie, BWA) feasible.

**Assembly.** An overlap graph (reads as nodes, suffix-prefix overlaps as edges) ideally wants the
shortest common superstring, but that's a Hamiltonian path (NP-hard, solved only greedily, within
~2.5× optimal) and collapses repeats longer than the overlap length regardless. A **de Bruijn graph**
instead makes each $k$-mer an edge and each $(k{-}1)$-mer a node, turning assembly into an Eulerian
path (tractable) rather than Hamiltonian. For reads `AAA, AAB, ABB, BBB, BBA`, $k=3$:

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A de Bruijn graph with 2-mer nodes AA, AB, BB, BA and 3-mer edges built from the reads AAA, AAB, ABB, BBB, BBA">
  <defs>
    <marker id="arrowDB" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="80" cy="60" r="22" fill="none" stroke="currentColor"/>
  <text x="80" y="64" text-anchor="middle" font-size="12" fill="currentColor">AA</text>
  <circle cx="240" cy="60" r="22" fill="none" stroke="currentColor"/>
  <text x="240" y="64" text-anchor="middle" font-size="12" fill="currentColor">AB</text>
  <circle cx="240" cy="160" r="22" fill="none" stroke="currentColor"/>
  <text x="240" y="164" text-anchor="middle" font-size="12" fill="currentColor">BB</text>
  <circle cx="80" cy="160" r="22" fill="none" stroke="currentColor"/>
  <text x="80" y="164" text-anchor="middle" font-size="12" fill="currentColor">BA</text>
  <path d="M 68,40 C 58,8 102,8 92,40" fill="none" stroke="currentColor" marker-end="url(#arrowDB)"/>
  <text x="80" y="14" text-anchor="middle" font-size="11" fill="currentColor">AAA</text>
  <line x1="102" y1="60" x2="218" y2="60" stroke="currentColor" marker-end="url(#arrowDB)"/>
  <text x="160" y="52" text-anchor="middle" font-size="11" fill="currentColor">AAB</text>
  <line x1="240" y1="82" x2="240" y2="138" stroke="currentColor" marker-end="url(#arrowDB)"/>
  <text x="270" y="112" text-anchor="middle" font-size="11" fill="currentColor">ABB</text>
  <path d="M 228,178 C 218,210 262,210 252,178" fill="none" stroke="currentColor" marker-end="url(#arrowDB)"/>
  <text x="240" y="206" text-anchor="middle" font-size="11" fill="currentColor">BBB</text>
  <line x1="218" y1="160" x2="102" y2="160" stroke="currentColor" marker-end="url(#arrowDB)"/>
  <text x="160" y="152" text-anchor="middle" font-size="11" fill="currentColor">BBA</text>
</svg>
<figcaption>Nodes are the 2-mers AA, AB, BB, BA; each edge is one 3-mer read, so AA→AA
(self-loop, AAA), AA→AB (AAB), AB→BB (ABB), BB→BB (self-loop, BBB), BB→BA (BBA).</figcaption>
</figure>

Choosing $k$ trades spurious overlaps from short repeats (too small) against edges broken by errors
or low coverage (too large); $k$ is kept odd so no $k$-mer equals its own reverse complement. Before
traversal, real assemblers simplify unbranched chains, trim error-caused dead-end "tips," pop
"bubbles" (redundant paths from error or real variation), and clip low-coverage nodes.

## High-throughput assays: ChIP-seq, RNA-seq, and their statistics

**ChIP-seq**: crosslink, fragment, immunoprecipitate (antibody against the protein or an epitope
tag — which risks non-native expression levels or mislocalization), reverse crosslinks, sequence.
The same logic gives MeDIP-seq (methylated DNA), CLIP-seq (RNA-protein), MeRIP-seq (RNA methylation).

**RNA-seq**: reads entirely within one exon don't reveal isoform identity, but junction-spanning
reads do directly — a read spanning exon1–exon3 implies isoform …exon3-exon4 follows; spanning
exon1–exon4 implies no exons 2/3 present; spanning exon1–exon2 is compatible with either
exon2-exon4 or exon2-exon3-exon4. Since most reads ($<$100bp) span only one junction, assembling a
full 5–10-exon isoform from short reads alone is hard.

**DESeq** models counts as negative binomial, $K_{ij}\sim NB(\mu_{ij},\sigma_{ij}^2)$, pooling
variance across regions of similar expression when replicates are too few, then tests via LRT,
$T_i=2\log\frac{P(K_{iA}\mid H_a)P(K_{iB}\mid H_a)}{P(K_{iA},K_{iB}\mid H_0)}\sim\chi^2_{df=2}$.

**Hypergeometric test** for shared gene sets: $N=500$ measured, $n_a=100$ changed under heat shock,
$n_b=150$ under oxidative stress, $k=40$ shared:

$$P(x\ge40)=\sum_{i=40}^{100}\frac{\binom{100}{i}\binom{400}{150-i}}{\binom{500}{150}}=0.0112,$$

rejecting independence at $\alpha=0.05$ — the two responses share more genes than chance predicts.

**PCA** finds the direction of maximal spread (PC1), then the orthogonal remaining maximum (PC2),
each successive component smaller; worked dataset: 2 PCs captured 22% of variance, 63 PCs needed for
90% — and apparent sample clusters should be checked against technical confounds (e.g. prep date).

**Topic models (LDA)**: single-topic $P(d)=\prod_w\theta_w^{n_w(d)}$ generalizes to per-word topics,
$P(d)=\prod_w(\sum_z\theta_z\theta_{w|z})^{n_w(d)}$, fit by EM — E-step $P(z\mid w,t)=
\theta_z^t\theta_{w|z}/\sum_{z'}\theta_{z'}^t\theta_{w|z'}$, M-step re-estimates topic mixtures and
word-topic distributions from those posteriors; topic count again chosen by BIC. Mapped to
expression: word = one gene's level, document = all genes in one experiment, topic = a co-regulated
program (immune response, stress, development, apoptosis).

**Single-cell RNA-seq** barcodes individual cells before pooling libraries, trading bulk averaging
for much stronger sampling noise: a lowly-expressed transcript may be only one molecule and easily
lost, so "undetected" and "unexpressed" become hard to tell apart.

## Motif discovery: information content and the Gibbs sampler

Shannon entropy $H(p)=-\sum_ip_i\log_2p_i$ (bits) is maximized at $\log_2n$ by the uniform
distribution, zero when one state has probability 1; uniform DNA background gives $H=2$ bits.
Information content at position $j$ is $I_j=2-H_j$, and for width $w$, $I_{\text{motif}}=2w-H_{\text{motif}}$
— a 5nt motif restricted to pyrimidines (independent positions) carries $5\times1=5$ bits. Against a
non-uniform background, relative entropy $\sum_kp_k\log_2(p_k/q_k)$ generalizes this (reducing to
$2w-H_{\text{motif}}$ when $q$ is uniform), with the rule of thumb that an $m$-bit motif recurs about
once every $2^m$ random bases. Worked example: codons forced to repeat the same base at positions 1
and 3 (16 of 64 equally likely) have motif entropy $\log_2 16=4$ bits, so with $w=3$,
$I_{\text{motif}}=2(3)-4=2$ bits — matching direct relative entropy, since the 1st position fully
determines the 3rd (one position's worth of information).

The **Gibbs sampler** finds a shared motif across $N$ sequences by guessing a start position in
each, then repeatedly: build a PWM from all sequences but one held out, resample that sequence's
motif position weighted by PWM match, rotate which sequence is held out. Randomness means different
runs can land differently (run many, compare) — but it's also what lets the sampler escape a local
optimum, unlike a deterministic method (e.g. the EM used for ChIP-seq peak-calling in GPS), which
converges wherever its initial condition leads and cannot escape.

## RNA secondary structure

RNA folds back on itself into helices, hairpin/bulge/interior/multi-branch loops, and (in some
structures) pseudoknots; structure often carries function (tRNA/rRNA invariant folds, mRNA structure
gating splicing or ribosome access, riboswitches, and ribozymes as evidence for an "RNA world").
Two routes find it. **Covariation**: structure-preserving compensatory mutations (e.g. $G{\cdot}C\to
A{\cdot}U$) should be tolerated while structure-breaking ones aren't, given enough diverged
homologs; quantified by mutual information,

$$M_{ij}=\sum_{x,y}f_{x,y}^{(i,j)}\log_2\frac{f_{x,y}^{(i,j)}}{f_x^{(i)}f_y^{(j)}},$$

zero if independent, maximal (2 bits) if uniform-but-perfectly-covarying — worked directly: 4
complementary pairs each at $f=1/4$ against $f_xf_y=1/16$ gives $4\times\tfrac14\times2=2$ bits.

**Energy minimization** (Base Pair Maximization, +1 per pair) is solved by the **Nussinov
algorithm**: for subsequence $i..j$,

$$S(i,j)=\max\begin{cases}S(i+1,j-1)+1 & i,j\text{ pair}\\S(i+1,j)\\S(i,j-1)\\\max_{i<k<j}S(i,k)+S(k+1,j)\end{cases}$$

Worked on `AAGUUCG`: initializing the diagonal to 0 and building outward, the full-sequence entry
$S(1,7)$ is reached via bifurcation at $k=5$, $S(1,5)+S(6,7)=2+1=3$ — an optimal 3-pair fold,
traceback recovering a 2-pair substructure on 1–5 joined to a 1-pair substructure on 6–7. Storage is
$O(N^2)$ (as in alignment) but the bifurcation search costs $O(N^3)$ time — an order more expensive.
Real folding programs add a minimum loop size of 3, unequal pair strengths
($G{\cdot}C>A{\cdot}U>G{\cdot}U$), base-stacking energies (which matter more than pairing itself),
bulge penalties, and terminal corrections; even so mfold gets only ~70% of bases right on average,
and the recursion as stated cannot represent pseudoknots at all.

## Protein structure

Four levels: **primary** (sequence), **secondary** ($\alpha$-helix/$\beta$-sheet from backbone
H-bonds), **tertiary** (full fold via side-chain interactions), **quaternary** (multi-chain
association). The peptide bond's partial double-bond character (resonance) makes it rigid and
planar, leaving rotation only at $\Phi$ ($C_\alpha$–N) and $\Psi$ ($C'$–$C_\alpha$), further
restricted by steric clash — mapped by the **Ramachandran plot** (glycine, with just H as its side
chain, is far less restricted; proline's ring restricts it further). $\alpha$-helices form via
$i\to i{+}4$ backbone H-bonds (3.6 residues/turn) and can be amphipathic; $\beta$-sheets form via
inter-strand backbone H-bonds, parallel or antiparallel. Tertiary structure adds disulfide bonds,
hydrophobic packing, ionic bonds, and side-chain H-bonds; quaternary structure is the same
interactions between separate chains (e.g. hemoglobin's $\alpha_2\beta_2$ tetramer).

Structures come from **X-ray crystallography** (crystal → diffraction → phased electron density →
fitted, refined model) or **NMR** (nucleus-specific resonance shifts; limited to $\lesssim$35 kDa,
but usable where crystallization fails, including disordered proteins). Energy is computed either
physically (**CHARMM**: harmonic bond/angle terms, a dihedral term, Lennard-Jones van der Waals,

$$U_{LJ}=\sum\varepsilon_{ij}\left[\left(\frac{r_{ij}^{min}}{r_{ij}}\right)^{12}-2\left(\frac{r_{ij}^{min}}{r_{ij}}\right)^6\right],$$

plus Coulomb electrostatics) or statistically (**Rosetta**: similarly-named terms fit by comparison
to observed structures rather than first principles, including discretized side-chain **rotamers** —
a Ramachandran plot analogue for side chains).

Three refinement strategies: **energy minimization** (deterministic gradient descent,
$F=-\nabla U$ — local only), **molecular dynamics** (simulate forces directly at femtosecond steps,
$x(t_i)=x(t_{i-1})+v(t_{i-1})\Delta t$, $v(t_i)=v(t_{i-1})-\frac{\nabla U}{m}\Delta t$ — accurate but
costly), and **simulated annealing** (Metropolis-Hastings: always accept downhill, accept uphill with
probability $e^{-(E_{\text{test}}-E_{\text{current}})/kT}$ from the Boltzmann distribution) — the only
one of the three that can move uphill and escape a local minimum, with temperature scheduled from
high (broad sampling) to low (fine refinement). Homology-based prediction scales effort to identity:
50%+ needs only refining misaligned regions; 20–50% tries several alignments and keeps the
lowest-energy result; below 20%, many starting structures with aggressive refinement. Without a
homolog, Rosetta's *ab initio* approach instead does Monte Carlo over 3–9-residue backbone segments
(borrowing $\Phi/\Psi$ angles from similar PDB peptides, Metropolis acceptance, 36,000 steps per
structure, 20,000 structures total), then clusters the results into representative folds.

## Modeling regulatory and signaling networks

Interaction partners are found experimentally by affinity purification: tag a bait protein, pull
down binding partners, identify by mass spectrometry, scalable proteome-wide. (The source slide cuts
off mid-sentence here, after a "~30% for 200…" success-rate figure that isn't recoverable.)

A **Boolean network** wires regulators as ON/OFF nodes through AND/OR gates, letting variables be
perturbed *in silico* to predict a therapeutic's effect:

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="A Boolean logic network combining regulators A, B and C through AND and OR gates into outputs G and S">
  <defs>
    <marker id="arrowBN" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <text x="46" y="20" font-size="13" fill="currentColor">A</text>
  <text x="146" y="20" font-size="13" fill="currentColor">B</text>
  <text x="246" y="20" font-size="13" fill="currentColor">C</text>
  <rect x="80" y="55" width="50" height="26" fill="none" stroke="currentColor"/>
  <text x="105" y="72" text-anchor="middle" font-size="11" fill="currentColor">AND</text>
  <line x1="52" y1="25" x2="95" y2="55" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <line x1="146" y1="25" x2="118" y2="55" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <line x1="105" y1="81" x2="105" y2="108" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <text x="112" y="100" text-anchor="middle" font-size="11" fill="currentColor">E</text>
  <rect x="190" y="55" width="50" height="26" fill="none" stroke="currentColor"/>
  <text x="215" y="72" text-anchor="middle" font-size="11" fill="currentColor">AND</text>
  <text x="172" y="45" font-size="10" fill="currentColor">NOT B</text>
  <line x1="150" y1="25" x2="202" y2="55" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <line x1="246" y1="25" x2="228" y2="55" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <line x1="215" y1="81" x2="215" y2="108" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <text x="222" y="100" text-anchor="middle" font-size="11" fill="currentColor">F</text>
  <rect x="135" y="115" width="50" height="26" fill="none" stroke="currentColor"/>
  <text x="160" y="132" text-anchor="middle" font-size="11" fill="currentColor">OR</text>
  <line x1="105" y1="108" x2="145" y2="115" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <line x1="215" y1="108" x2="175" y2="115" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <line x1="160" y1="141" x2="160" y2="165" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <text x="168" y="158" text-anchor="middle" font-size="12" fill="currentColor">G</text>
  <rect x="135" y="175" width="50" height="26" fill="none" stroke="currentColor"/>
  <text x="160" y="192" text-anchor="middle" font-size="11" fill="currentColor">AND</text>
  <line x1="160" y1="165" x2="160" y2="175" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <path d="M 46,30 C 6,120 6,195 133,190" fill="none" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <text x="18" y="150" font-size="10" fill="currentColor">NOT A</text>
  <line x1="160" y1="201" x2="160" y2="225" stroke="currentColor" marker-end="url(#arrowBN)"/>
  <text x="160" y="222" text-anchor="middle" font-size="12" fill="currentColor">S</text>
</svg>
<figcaption>The recitation's example Boolean network: A and B feed one AND gate, C and NOT(B)
feed a second, their outputs combine by OR into G, and a feedback arm from NOT(A) joins G to set
the final output S.</figcaption>
</figure>

Fitting such a network to phosphoproteomic data means choosing among candidate structures from
pathway databases, trading fit against size: $\theta=\theta_f+\alpha\theta_S$, with $\theta_f$ the
squared deviation between model and data and $\theta_S=\sum_kv_kP_k$ penalizing model size. Because
of noise, keep a representative family of top models rather than one best fit, then perturb edges
(genetic algorithm): a database network alone gives ~45% error, improvable below 10% — but too many
free parameters risks fitting noise instead of structure. Replacing Boolean steps with graded,
continuous response functions is more realistic but roughly doubles free parameters, demanding more
data.

## Chromatin and the 3D genome

DNA wraps **nucleosomes** (octamers of H2A, H2B, H3, H4), whose tails carry modifications combining
into a "histone code" (ENCODE's table): H2A.Z and H3K4me1/2/3 mark enhancers/promoters; H3K9ac/H3K27ac
mark active elements; H3K9me3/H3K27me3 are repressive (heterochromatin, polycomb domains);
H3K36me3/H3K79me2/H4K20me1 track transcription with different positional preferences. DNA methylation
at CpGs adds a second layer (CpG islands silencing promoters; e.g. *Nanog* demethylation in
reprogramming) — both layers are enzymatically written/erased, heritable through division, yet
reversible ("epigenetic").

Histone-mark combinations become functional annotations via an HMM (ChromHMM) or a **Dynamic
Bayesian Network** (Segway), which adds to the HMM a segment label $Q_t$, an indicator (assay has
signal here?), observation tracks $X_t^{(i)}$, a ruler marker (every 10th position), a countdown
enforcing min/max segment length, and a transition variable $J_t$ whose table forces, prevents, or
allows (geometric, rate $1/(1{+}L)$) a label change. Trained by EM on 1% of the genome, applied
genome-wide by Viterbi decoding; with 25 chosen labels the result was directly interpretable ("gene
start," "gene end," "enhancer," …).

TF binding needs open chromatin: of ~650,000 motif instances genome-wide, a typical TF occupies only
~50,000, and occupancy shifts across states (Tcf7l2: 7,633 peaks unique to mES cells, 14,837 unique
to endoderm, 1,468 shared — 16%). **DNase-seq** maps accessibility directly (DNase I cuts unprotected
chromatin); **PIQ** combines this with TF motifs — candidate sites from motifs, smooth the DNase
signal (Gaussian process), then test observed accessibility against each TF's expected
hypersensitivity signature by log-likelihood ratio (1% null tail = bound). "Pioneer" TFs open closed
chromatin for "settler" TFs to follow; a time-course "pioneer index" found only a few motifs with
strong pioneer activity, some asymmetric by strand direction.

**ChIA-PET** finds 3D contacts: ChIP a protein (e.g. Pol II), ligate tagged ends under dilute
conditions, sequence; self-ligations are discarded, inter-ligations are candidate contacts, tested by
hypergeometric significance,

$$P(I_{A,B}\mid N,c_A,c_B)=\frac{\binom{c_A}{I_{A,B}}\binom{N-c_A}{c_B-I_{A,B}}}{\binom{N}{c_B}}.$$

High false-negative rates mean repeats capture only a subset of true contacts; given two experiments'
sizes $m,n$ and overlap $k$, the MLE of the true total is $\hat N\approx mn/k$ — worked: $m=100$,
$n=200$, $k=20$ gives $\hat N=1000$. Correcting for an assumed false-positive rate $f=5\%$ first
adjusts $m'=(1-f)(m-k)+k=96$, $n'=(1-f)(n-k)+k=191$, giving the revised $\hat N=(96)(191)/20\approx869$.

## Quantitative and human genetics

A **QTL** is a marker associated with a quantitative trait (eQTL for expression; *cis* within ~kb,
*trans* beyond Mb or cross-chromosome). In a haploid, unlinked model with $N$ equally-weighted loci,
inherited alleles follow Binomial$(N,0.5)$: $E[x]=0.5$, $\sigma_x^2=0.25/N$ — breaking down for
linked loci, where independence no longer holds. With $p_i=f(g_i)+e_i$ and $E[e_i]=0$, $\sigma_p^2=
\sigma_g^2+\sigma_e^2$. **Broad-sense heritability** $H^2=\sigma_g^2/\sigma_p^2$ bounds prediction by
any model; **narrow-sense** $h^2$ (additive-only) is exactly the regression slope of offspring on
mid-parent value. For additive $f_a(g_i)=\sum_j\beta_jg_{ij}+\beta_0$, children fall at the parental
midpoint in expectation, and $h^2=\sigma_a^2/\sigma_p^2$ where $\sigma_a^2$ is the variance explained
after fitting that linear model.

QTLs are found via **LOD scores**,
$\text{LOD}=\log_{10}\prod_i\frac{P(p_i\mid g_{ij},\mu_0,\mu_1,\sigma)}{P(p_i\mid\mu,\sigma)}$,
with significance from permuting genotype-phenotype pairs 1000× for an empirical null at FDR = 0.05
(no further multiple-testing correction needed, since every locus is already in the null). Bloom *et
al.* (2013, yeast) found 5–29 QTLs per trait (median 12), explaining most narrow-sense heritability
but leaving some missing — candidates include rare and structural variants, epigenetics, and
epistasis (tested only between detected QTLs and all loci, $20\times100{,}000$, since all-pairs is
infeasible).

SNP/disease association, worked from a 2×2 table (62/80 C-allele cases/controls, 108/250 A-allele,
500 total): expected counts from marginals (e.g. $142\times170/500=48.28$) give

$$X^2=\sum\frac{(O-E)^2}{E}=8.25,\quad df=1,\quad P(\chi_1^2\ge8.25)\approx0.0041\ (\text{reject }H_0).$$

Chi-squared is only asymptotic (needs $\gtrsim5$ per cell); **Fisher's exact test**,
$p=\binom{a+b}{a}\binom{c+d}{c}/\binom{a+b+c+d}{a+c}$ summed over the table and all more extreme ones,
gives one-sided $\approx0.003$, two-sided $\approx0.0047$ on the same data — exact, but costly at
large counts (exactly where chi-squared is fine). **Population stratification** can still confound a
significant result, checked via control SNPs known unrelated to the disease.

**Linkage disequilibrium**: under independence $p_{AB}=p_Ap_B$; deviation $D=p_{AB}p_{ab}-p_{Ab}p_{aB}$
gives $p_{AB}=p_Ap_B+D$ etc., with $AB/ab$ "coupling" and $Ab/aB$ "repulsion" gametes — closer loci
stay in higher LD since crossover is less likely to separate them. **Variant phasing** (which alleles
share a chromosome) matters because two mutations in the same gene copy leave the other copy intact,
while one in each knocks out both; inferred from family data or reads long enough to span both
variants.

Under **Hardy-Weinberg equilibrium** (random mating, infinite population, no migration/mutation/
selection), $P(AA)=\psi^2$, $P(Aa)=2\psi(1-\psi)$, $P(aa)=(1-\psi)^2$ for allele frequency $\psi$.
Testing HWE uses an LRT between the unconstrained model ($df=2$) and the $\psi$-constrained model,

$$-2\ln\lambda=-2\ln\frac{P(\text{Data}\mid\psi^2,2\psi(1-\psi),(1-\psi)^2)}{P(\text{Data}\mid p_{AA},p_{Aa},p_{aa})}\sim\chi^2_{df},$$

via the multinomial likelihood (factorials cancel). The recitation's own worked numbers shift
between slides — 25 $aa$/90 $Aa$/85 $AA$ on one, but $p_A=0.7375$ and the HWE-predicted frequencies
($0.5439,0.3872,0.0689$) from 25/55/120 on the next — the method is unchanged either way: estimate
$p_A=(2n_{AA}+n_{Aa})/2n$, derive the three HWE frequencies from it, compare likelihoods. The same
LRT extends to one shared genotype-frequency set vs. two subpopulation-specific sets ($df=4-2=2$).

## Sources

- **2014-02-11** — Recitation 1: PWM/Bayesian posterior worked example; Noble (2009) CTCF null-distribution/p-value example.
- **2014-02-12** — Recitation: p-value/null-model definition, coin-flip binomial test, NGS overview, alignment modes, BLAST statistics/Karlin-Altschul $\lambda$, dynamic programming.
- **2014-02-14** — Recitation: k-means, hierarchical clustering/linkage, BIC, biclustering; biology review (selection, synonymous mutation, side chains, disulfide bonds); local/global alignment worked example (`AWEK`/`FWEF`).
- **2014-02-19** — Recitation (6.874/6.91): Markov chains, stationary distributions, the purine/pyrimidine $PAM_1\to PAM_\infty$ problem, PAM vs. BLOSUM, Jukes-Cantor, $K_a/K_s$.
- **2014-02-26** — Recitation: library complexity, the BWT construction, rank/LF function, exact matching (`ANA`/`BNA` in `BANANA`), offset recovery, the FM-index, and assembly (overlap vs. de Bruijn graphs, the `AAA/AAB/ABB/BBB/BBA` example, $k$-mer choice, graph cleanup).
- **2014-03-05** — Recitation: ChIP-seq protocol, epitope-tag caveats, related peak-calling assays.
- **2014-03-07** — Recitation (6.874): RNA-seq isoform identification, DESeq, the hypergeometric worked example, PCA, topic models/LDA and their EM fitting, single-cell RNA-seq.
- **2014-03-12** — Section: Shannon entropy and motif information content, the fixed-codon example,
  the Gibbs sampler.
- **2014-03-19** — Recitation: RNA secondary structure terminology, mutual information, the full
  worked Nussinov algorithm on `AAGUUCG`.
- **2014-04-02** — Recitation: protein structure levels, Ramachandran plot, CHARMM/Rosetta energy functions, the three refinement strategies, homology- and *ab initio*-based prediction.
- **2014-04-09** — Recitation: experimental protein-interaction methods (source cut off after
  affinity purification).
- **2014-04-16** — Recitation: the Boolean network framework, the network-fitting objective function, model improvement, extension to continuous responses.
- **2014-04-23** — Recitation: histone modifications (ENCODE table), DNA methylation, Segway's DBN, the Tcf7l2 example, DNase-seq/PIQ, pioneer TFs, ChIA-PET's hypergeometric test, the false-positive-corrected overlap estimator.
- **2014-04-30** — Recitation: the haploid/unlinked QTL model, heritability, LOD scores, Bloom *et al.* (2013); SNP/phenotype chi-squared and Fisher's exact tests, population stratification, linkage disequilibrium, variant phasing, Hardy-Weinberg equilibrium and its LRT.

All items are reconstructed-by-model conversions of the original recitation slide PDFs (MIT OCW
7.91J, Spring 2014, CC BY-NC-SA 4.0); per their own notices, prose is paraphrased in places and every
equation is unverified against the source PDF. No problem-set questions or other unsolved exercises
appear in this material — every question the recitations pose is answered within the same slide
deck, so no Exercises section is given.

---

[← 22. Engineering Genomes to Test Causality](22-engineering-genomes-to-test-causality.md) · [Contents](index.md)
