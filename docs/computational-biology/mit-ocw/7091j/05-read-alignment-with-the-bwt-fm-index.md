---
title: "5. Read Alignment with the BWT/FM Index"
course: "MIT 7.091J"
chapter: 5
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Read Alignment with the BWT/FM Index

## What this covers

Two questions sit behind this lecture. First, before trusting a pile of sequencing reads at all: how
many genuinely distinct DNA molecules went into the library that produced them, and how would you
know if the experiment had gone wrong? Second, given a good set of reads, how do you find where each
one sits in a genome of three billion bases, when there are hundreds of millions of reads and the
dynamic-programming alignment of earlier lectures is far too slow to run that many times? It assumes
Smith–Waterman-style alignment and ordinary probability (binomial, Poisson); the Burrows–Wheeler
transform and the index built on it are developed from scratch.

## Sequencing libraries, and why you can't just count

A sequencing library is a tube of DNA molecules prepared from some number of cells, with adapters
ligated to the ends so the molecules can be sequenced. Some molecules are present many times over —
because the original cell population held several copies, or because PCR amplified some fragments
more than others. The **library complexity** $C$ is the number of *distinct* molecule types in the
tube, as opposed to the number of reads $N$ eventually obtained by sequencing it (typically far
larger, often around $10^8$). Complexity is a quality-control question: a library meant to be rich in
distinct molecules but turning out to have low complexity indicates something went wrong upstream —
degraded input, poor amplification, a badly executed protocol.

The simplest model treats each of the $N$ reads as an independent draw of one of the $C$ molecule
types, each equally likely, so a given type is picked with probability $1/C$ per read. The count of
one type over $N$ reads is $\mathrm{Binomial}(N, 1/C)$, well approximated for the sample sizes
involved by a Poisson with rate $\lambda = N/C$. The catch: you only ever see what you sequence — a
type drawn zero times is invisible even though it is present. So $\lambda$ cannot be fit from a
complete histogram; the zero bin is missing. The fix is to fit $\lambda$ from the part of the
distribution that *is* visible — molecules observed between $l$ and $r$ times, excluding zero — and
then recover $C$ from the number $m$ of distinct molecules actually observed, using the Poisson
probability of being missed entirely, $e^{-\lambda}$:

$$m = C\left(1 - e^{-\lambda}\right).$$

Knowing $m$ and the fitted $\lambda$, this solves for the one remaining unknown, $C$.

### Where the simple model breaks

Applied to 1000 Genomes data — estimating complexity from 10% of an individual's reads versus all of
them — a good estimator should agree either way. It does not: the 10%-read estimate is off by roughly
a factor of two, badly underestimating complexity. The reason, as a student correctly guessed, is that
the model's core assumption — every molecule type equally likely to be sampled — is false. Repeated
sequence and unequal PCR amplification skew the true population: a few types in many copies, most in
few. A Poisson has one free parameter, setting the mean *and* variance together
($\mathrm{Var}=\mathbb{E}[\cdot]=\lambda$), so it cannot represent a distribution whose variance exceeds
its mean — exactly what over-dispersed copy numbers produce.

### A two-stage model: Gamma mixed with Poisson

The fix is to stop assuming one fixed rate $\lambda$ for every molecule type, and instead treat each
type's *relative copy number* as itself random, drawn from a Gamma distribution, with reads then
sampled from each type by a Poisson whose rate is set by that copy number. Marginalising the Gamma
rate out of the Poisson gives the **negative binomial distribution**, with two parameters instead of
one: the mean $\lambda$ as before, and a dispersion parameter $k$ controlling how unevenly copy number
is spread across types.

Fit to simulated libraries of known complexity, the Poisson estimator's error grows quickly as
dispersion increases, while the negative binomial stays close to the truth throughout; fit to the real
1000 Genomes data, negative-binomial estimates from a small subsample track the full-data estimates
almost exactly, once over-dispersion is accounted for.

This also gives a principled estimate of the **marginal value of additional sequencing**: from a
fitted $(\lambda,k)$, predict how many *more* distinct molecules an additional $r$ reads would recover,
without sequencing them. The more skewed the library (the larger $k$, in the lecture's convention),
the less is gained from sequencing deeper, since additional reads increasingly re-hit types already
seen many times — a direct, quantitative answer to "I have 50 million reads already; is it worth
sequencing more?"

## The alignment problem

Set complexity aside and assume a good set of reads. The input is a reference genome (around
$3\times10^9$ bases for human, FASTA) and a large set of reads — illustratively $2\times10^8$ reads of
around 200 bases, FASTQ. FASTQ adds a quality score per base, the **PHRED score**,

$$Q = -10\log_{10}(p),$$

$p$ being the estimated probability the base call is wrong: $Q=10$ means a 1-in-10 error chance,
$Q=20$ means 1-in-100, and so on.

The task is to produce a SAM (Sequence Alignment/Mapping) file giving each read's position in the
reference. This serves two uses: **genotyping**, where differences between aligned reads and the
reference reveal where an individual's genome differs from it (roughly one base in a thousand between
any two people); and experiments whose reads mark some biological process, where the goal after
alignment is to find regions of enrichment ("peaks") rather than point differences. Both share one
bottleneck — aligning hundreds of millions of short reads against billions of reference bases — and
the quadratic-time dynamic-programming methods used for pairwise alignment simply cannot be run that
many times.

A "good" alignment here means fewer mismatches, and more tolerance for a mismatch at a low-quality
position than a high-quality one — the genome is treated as ground truth, and the quality string is
the only information available about where an error in the *read* is likely to be.

## The Burrows–Wheeler transform

The index that makes this tractable is built from the **Burrows–Wheeler transform (BWT)**, applied
once to the whole reference (with a unique terminator `$`, sorting before every other character).
Take the example used throughout the lecture, $T=\texttt{ACAACG\$}$ (length 7):

1. Form every cyclic rotation of $T$ — one per starting position, 7 here.
2. Sort the rotations lexicographically.
3. Read the **last column** of the resulting matrix, top to bottom: that string is the BWT of $T$.

```
row  first col …          … last col
 0    $ A C A A C G           G
 1    A A C G $ A C           C
 2    A C A A C G $           $
 3    A C G $ A C A           A
 4    C A A C G $ A           A
 5    C G $ A C A A           A
 6    G $ A C A A C           C
```

so $\mathrm{BWT}(T)=\texttt{GC\$AAAC}$. Each row exposes one **suffix** of $T$ (the terminator is
unique, so sorting rotations sorts true suffixes) — the whole construction is "sort all the suffixes,
keep the character immediately before each one." No compression, no cleverness yet: rotate and sort.
It looks like the genome's structure has been thrown away. It has not.

### The property that makes it useful

The crucial, slightly counter-intuitive fact: **the $k$-th occurrence of a character in the last
column and the $k$-th occurrence of that same character in the first column are the same physical
character of $T$.** Shift the matrix one column left (conceptually) and the characters that fall off
the left edge reappear on the right, now ordered by the (alphabetically sorted) rows they sit in — so
two occurrences of, say, `A`, keep the same relative order whichever column they're read from.

This licenses the **last-to-first (LF)** function, mapping a row in the last column to the row of the
*same character* in the first column, using only the last column:

$$\mathrm{LF}(i) = \mathrm{Occ}(c) + \mathrm{count}(c, i), \qquad c = \mathrm{BWT}[i],$$

where $\mathrm{Occ}(c)$ is the number of characters in $T$ sorting before $c$ (where $c$'s block
starts in the sorted first column — four stored integers, computed once:
$\mathrm{Occ}(\$)=0,\ \mathrm{Occ}(\mathrm A)=1,\ \mathrm{Occ}(\mathrm C)=4,\ \mathrm{Occ}(\mathrm
G)=6$), and $\mathrm{count}(c,i)$ is the zero-based rank of that occurrence of $c$ among
$\mathrm{BWT}[0..i]$. Working through $\mathrm{BWT}=\texttt{GC\$AAAC}$:

| $i$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $\mathrm{BWT}[i]$ | G | C | \$ | A | A | A | C |
| $\mathrm{LF}(i)$ | 6 | 4 | 0 | 1 | 2 | 3 | 5 |

Only $\mathrm{Occ}$ and a running per-character count of the last column were used — never the first
column or the rest of the matrix.

### Rebuilding the original string from the transform alone

To show the last column really does carry the whole genome, walk LF backwards from the row whose
first-column character is `$` (row 0), emitting the *last-column* character at each row visited: row
0 emits G, going to row 6; row 6 emits C, to row 5; row 5 emits A, to row 3; row 3 emits A, to row 1;
row 1 emits C, to row 4; row 4 emits A, to row 2; row 2 emits `$` and stops. Read the emitted
characters in reverse: `A C A A C G $` — exactly $T$, recovered without ever storing the first column
or any row but the last.

## Backward search: matching a read without storing the matrix

The payoff is an algorithm testing whether a query occurs in $T$, using only the BWT and LF, in time
linear in the read's length regardless of genome size. The read is matched **backwards**, last
character to first, maintaining a row range $[\mathrm{top},\mathrm{bottom}]$: the rows whose suffix is
consistent with the query matched so far. Each step extends the match by one more character (the next
one leftward in the query), narrowing the range via $\mathrm{Occ}$ and rank exactly as LF does.

Take $Q=\texttt{AAC}$ against $T=\texttt{ACAACG\$}$, narrowing right to left:

<figure>
<svg viewBox="0 0 420 210" role="img" aria-label="Backward search narrowing the row range of the BWT matrix as the query AAC is matched right to left">
  <text x="210" y="18" text-anchor="middle" font-size="12" fill="currentColor">BWT rows, sorted order (T = ACAACG$)</text>
  <g font-size="13">
    <text x="60" y="45" text-anchor="middle" fill="currentColor">G</text>
    <text x="105" y="45" text-anchor="middle" fill="currentColor">C</text>
    <text x="150" y="45" text-anchor="middle" fill="currentColor">$</text>
    <text x="195" y="45" text-anchor="middle" fill="currentColor">A</text>
    <text x="240" y="45" text-anchor="middle" fill="currentColor">A</text>
    <text x="285" y="45" text-anchor="middle" fill="currentColor">A</text>
    <text x="330" y="45" text-anchor="middle" fill="currentColor">C</text>
  </g>
  <g font-size="11" fill="currentColor">
    <text x="60" y="30" text-anchor="middle">0</text>
    <text x="105" y="30" text-anchor="middle">1</text>
    <text x="150" y="30" text-anchor="middle">2</text>
    <text x="195" y="30" text-anchor="middle">3</text>
    <text x="240" y="30" text-anchor="middle">4</text>
    <text x="285" y="30" text-anchor="middle">5</text>
    <text x="330" y="30" text-anchor="middle">6</text>
  </g>
  <line x1="40" y1="65" x2="350" y2="65" stroke="currentColor" stroke-width="0.5" opacity="0.3"/>

  <line x1="40" y1="90" x2="350" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="84" x2="40" y2="96" stroke="currentColor" stroke-width="1.5"/>
  <line x1="350" y1="84" x2="350" y2="96" stroke="currentColor" stroke-width="1.5"/>
  <text x="360" y="94" font-size="12" fill="currentColor">start: rows 0–6 (every suffix)</text>

  <line x1="220" y1="125" x2="305" y2="125" stroke="currentColor" stroke-width="1.5"/>
  <line x1="220" y1="119" x2="220" y2="131" stroke="currentColor" stroke-width="1.5"/>
  <line x1="305" y1="119" x2="305" y2="131" stroke="currentColor" stroke-width="1.5"/>
  <text x="360" y="129" font-size="12" fill="currentColor">after matching "C": rows 4–5</text>

  <line x1="130" y1="160" x2="215" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <line x1="130" y1="154" x2="130" y2="166" stroke="currentColor" stroke-width="1.5"/>
  <line x1="215" y1="154" x2="215" y2="166" stroke="currentColor" stroke-width="1.5"/>
  <text x="360" y="164" font-size="12" fill="currentColor">after "AC": rows 2–3</text>

  <line x1="85" y1="195" x2="125" y2="195" stroke="currentColor" stroke-width="2"/>
  <line x1="85" y1="189" x2="85" y2="201" stroke="currentColor" stroke-width="2"/>
  <line x1="125" y1="189" x2="125" y2="201" stroke="currentColor" stroke-width="2"/>
  <text x="360" y="199" font-size="12" fill="currentColor">after "AAC": row 1 only — one hit</text>
</svg>
<figcaption>Backward search for the read AAC against the BWT of ACAACG$. The matched range
(top, bottom) shrinks by one character of the query at each step, computed purely from the last
column and the LF function, until a single row remains.</figcaption>
</figure>

If the range collapses to $\mathrm{top}=\mathrm{bottom}$ with query characters still unmatched, the
lookup has failed — no suffix matches, and the range stays collapsed. If the final range spans more
than one row, the read maps to multiple genome locations (likely, since roughly half of a genome like
human's is repetitive), and all or just the first can be reported.

## Locating a hit in the genome

A matching row says which row of the conceptual sorted matrix the read's suffix sits in — not where
in the genome that is, which is what anyone actually wants. Walking left (via LF) from that row to
the terminator, counting steps, recovers the offset — but that is linear in genome length *per
query*, defeating the purpose.

The practical compromise is a **sampled suffix array**: store the genome position for only every so
many rows (the lecture's example: every 25th), instead of every row. To locate an unsampled row, walk
left via LF until a sampled row is hit, and add the steps walked to its stored position — a small
per-query cost for a large saving in index size.

## Computing rank quickly: checkpoints

LF also needs $\mathrm{count}(c,i)$, the rank of a character occurrence up to row $i$ — scanning the
whole transform backwards each time would defeat the index just as badly. The same sampling idea
applies: store **checkpoints** periodically — running totals of each base seen so far in the BWT — and
compute an arbitrary rank by jumping to the nearest checkpoint and counting only the short remaining
stretch directly.

## What a full FM index contains

A complete index — an **FM index** (the name, from its originators' initials, stands for "full-text
minute-size") — is exactly three things: the BWT of the genome (chromosomes separated by terminators),
a sampled suffix array, and rank checkpoints. Nothing else from the conceptual rotation matrix is kept.
The result is compact — under twice the genome's size, far smaller than an unsampled suffix array or
suffix tree — while matching runs linear in read length. Building it is the expensive one-off step:
for human (NCBI build 36.3) on a 2.4 GHz AMD Opteron, the lecture's figures are

| Physical memory target | Actual peak memory | Wall-clock build time |
|---|---|---|
| 16 GB | 14.4 GB | 4h 36m |
| 8 GB | 5.8 GB | not given in the supplied slide (table cut off at the source) |

(independently, the lecture gives "about five hours" as the order of magnitude for the whole human
genome). In practice the cost is paid once — indices are usually downloaded pre-built — after which
matching runs at roughly 100 million reads per hour on a four-processor machine, linear in bases
processed.

## Living with mismatches: backtracking

Exact backward search is elegant but useless alone: real reads carry sequencing errors and real
genomes carry real variation, neither of which is an exact match. When the range collapses with query
characters left unmatched, aligners such as Bowtie and BWA **backtrack**: retry the failed step with a
different base, and continue from there. This is greedy and depth-first — not optimal, but simple —
and cut off after a bound on attempted backtracks (Bowtie's practical limit is around 125) to stay
fast. Because different backtracking choices can lead to different valid alignments of the same read,
nothing guarantees the alignment returned is the best available — only *a* valid one found within
budget.

Where to backtrack is informed by the PHRED string: Bowtie backtracks to the **leftmost
previously-visited position with the lowest quality score**, on the reasoning that a mismatch is most
plausible where the base call is least trustworthy. More generally (following a scheme from the Maq
aligner), the policy exposes tunable parameters: at most $N$ mismatches within the first $L$ bases
from one end, provided the sum of PHRED qualities at mismatched positions stays under a budget $E$ —
set in Bowtie via `-n`, `-l`, `-e`, and chosen per run rather than fixed once and for all.

### The asymmetry backward search creates, and the mirror index

Matching strictly right-to-left creates a bias: the search gives up as soon as it hits a mismatch near
the end it started from — the 3′ end — but because sequencing runs 5′ to 3′, quality is typically
*highest* near the 5′ (left) end and degrades toward the 3′ end. Right-to-left search therefore tends
to exhaust the backtracking budget on the noisier end before reaching the more trustworthy one. The
fix is a **mirror index**: a second FM index built on the reversed genome, letting the same machinery
match left-to-right too. Running forward and mirror indices in parallel — tolerating, say, up to two
mismatches total — guarantees at least half the read matches exactly in one of the two indices before
any backtracking is needed, cutting the amount actually required.

Gaps (insertions/deletions) are handled separately and treated as markedly less important than
substitutions here: rarer, often absent from other reads covering the same locus even when present in
one, and more suggestive of structural variation than a simple error or SNP. BWA supports gapped
alignment directly; the details are aligner-specific rather than one settled method.

## Paired-end reads and other practical considerations

Many protocols produce **paired-end reads**: two reads per molecule, one from each 5′ end, with an
unobserved, only approximately known stretch between them (the **insert size**: full molecule length,
5′ end to 5′ end). Processing typically aligns both reads independently, then orients them against the
reference (lower genomic coordinate versus higher). If one read fails to align uniquely, the
approximate insert size narrows the search enough to run a full Smith–Waterman alignment just in the
expected neighborhood of the other, already-placed read — exactly where the slower method stays
affordable, since it now applies to a small window rather than the whole genome.

More generally, because roughly half of a genome like human's is repetitive, a read commonly maps to
more than one location (the final search range spans more than one row); an aligner may report all
such locations or only the first. Setting a workable mismatch tolerance, and configuring an aligner's
parameters generally, is empirical and somewhat ad hoc here — there is no clean optimality criterion of
the kind dynamic-programming alignment enjoys, and good settings depend on the reads being aligned.

## Exercises

**Problem set 5.** Assigned across several lectures, spanning topics beyond this one — network
statistics, chromatin-state segmentation, heritability, association testing — not all covered in this
chapter. Reproduced here as the course's own problem set, not as practice for the read-alignment
material above.

**P1 — Network statistics (10 points).** High-throughput protein–protein interaction databases carry
known biases: poorly studied proteins are under-represented, and the many assay types used to generate
evidence are themselves biased toward particular kinds of proteins. Using a supplied UniProt citation
file and seven STRING interaction networks (one per evidence type — neighborhood, fusion,
co-occurrence, co-expression, experimental, database, text-mining):

(a) *(2 points)* For each protein in the UniProt file, count the number of distinct PubMed IDs mapped
to it. Plot a histogram of citations per protein, and report the median and maximum citation counts
and the most-cited protein.

(b) *(4 points)* For each of the seven evidence networks, report the number of edges and nodes with no
score cutoff, and again restricted to edges scoring above 0.4 and above 0.8. Comment on what the
differences across evidence types and cutoffs say about the reliability of each kind of evidence.

(c) *(4 points)* For each network, compute each protein's node degree, then — after removing proteins
with no citation data or no interactions — compute the Spearman rank correlation between node degree
and citation count, with no cutoff and again restricted to edges above 0.4 and above 0.8. Is there a
relationship between citation count and degree? Does its strength vary across evidence types, and if
so, why might that be?

**P2 — Analysis of chromatin structure (5 points).**

(A) Suppose the Segway segmentation model is run with fewer states than the true number of distinct
chromatin-mark patterns. How would the resulting labelling change?

(B) Segway's $C$, $M$, $t$, $J$ variables implement a "countdown" mechanism. How does this improve on a
plain HMM's ability to model the duration of genomic states?

For the rest of this problem, suppose the $C$, $M$, $t$, $J$ countdown variables are removed from the
model.

(C) Draw the resulting graphical model.

(D) Suppose $J$ is a binary variable that either forces or prevents a label change, and there are 50
possible segment labels. Compare the number of parameters needed for the segment-label conditional
probability table in the original model against this reduced model.

(E) Which other core feature of the Segway model does this reduced model still retain, that a plain HMM
lacks?

**P3 — Heritability (5 points).**

(A) *(3 points)*
(i) A single locus in a haploid organism controls a trait: the positive allele gives phenotype 1, the
neutral allele gives phenotype 0. Compute the genetic variance $V_G$ in an infinite population of
$F_1$ offspring of one parent of each type.
(ii) Now suppose three unlinked loci each contribute $\frac{1}{3}$ (positive allele) or $0$ (neutral
allele) to the phenotype. Compute $V_G$.
(iii) Generalize to $N$ unlinked loci, each contributing $0$ or $\frac{1}{N}$. Give $V_G$ in terms of
$N$, and state how many distinct phenotype values are possible.

(B) *(1 point)* You regress a phenotype $y$ on a set of binary genotype variables $x_1,\dots,x_N$.
Show how the resulting $R^2$ relates to the narrow-sense heritability of the trait.

(C) *(1 point)* Assuming the genetic components of part (A) are purely additive, and the genetic and
environmental components are uncorrelated, give the environmental contribution to the phenotypic
variance in terms of $R^2$.

**P4 — Association studies (5 points).**

(A) *(3 points)* The table below gives case–control genotype counts at a SNP with alleles A and T.

| | A | T |
|---|---|---|
| Case | 90 | 110 |
| Control | 50 | 250 |

(i) Compute the counts expected under independence of disease status and genotype.
(ii) Compute the chi-square statistic and state your conclusion at a p-value cutoff of 0.05.

(B) *(1 point)* Given a list of significant SNPs from a large-scale association study, how could you
use what you learned about the Segway model to prioritize them for further study?

(C) *(1 point)* Why is it preferable to test for association using a likelihood computed directly from
the sequencing reads, rather than first calling genotypes and then testing the resulting binary calls?

## Sources

- Slides `lectures/05-slides.md` ("Backtracking" and surrounding pages): Bowtie's quality-driven
  backtracking policy and example, the Maq-style $N$/$L$/$E$ quality policy, the mirror-index diagram,
  and the BWT/FM-index build-time table. The converted deck keeps only the later, text-bearing pages —
  library complexity and the core BWT construction are largely diagrams in the original and were not
  recovered as text, so the transcript is the primary source there. The slides credit
  `cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt` for several figures and cite Li, Ruan, Durbin, "Mapping
  short DNA sequencing reads and calling variants using mapping quality scores," *Genome Research*
  2008, for the quality policy — neither is in the supplied material.
- Transcript `recordings/lectures/05.md`: 00:00–08:14 (library complexity, Poisson and negative
  binomial, 1000 Genomes example); 17:08–20:22 (alignment problem, PHRED, genotyping/peak-finding, why
  Smith–Waterman does not scale); 21:24–46:00 (BWT construction, rank preservation, the LF function,
  walk-left reconstruction of $T=\texttt{ACAACG\$}$); 46:00–57:22 (backward search, linear-time
  matching, failed/multiply-mapped lookups); 57:22–1:02:51 (suffix-array sampling, rank checkpointing);
  1:02:51–1:13:46 (FM index contents, build/search times); 1:03:56–1:12:41 (backtracking, the
  quality-driven backtrack position, gaps, the mirror index); 1:13:46–1:18:33 (paired-end alignment,
  closing notes). A BWA paper posted to the course's Stellar site, and the next day's recitation on
  gapped alignment and fast BWT construction, are referred to but not supplied.
- Problem set 5: `psets/05-questions/01–04-*.md` and the duplicate conversion
  `psets/05-questions-pset5-ques/01–03-*.md` — the same four problems, each included once above, using
  the blank student-facing wording where both conversions overlap and the fuller conversion for the one
  problem (P2) missing from the second directory.

---

[← 4. Markov Models and Comparative Genomics](04-markov-models-and-comparative-genomics.md) · [Contents](index.md) · [6. OLC and De Bruijn Assembly →](06-olc-and-de-bruijn-assembly.md)
