---
title: "2. Sequencing Platforms and BLAST Statistics"
course: "MIT 7.091J"
chapter: 2
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Sequencing Platforms and BLAST Statistics

## What this covers

This chapter answers two questions that sit back to back in the same lecture: how do you actually
read off a DNA sequence (from gel-based Sanger sequencing through the first wave of "next-gen"
platforms), and once you have reads, how do you decide whether a short stretch of similarity between
two sequences means anything? It assumes you know what a nucleotide and a genome are, and builds
the rest — chain-termination chemistry, the idea of a sequencing read, a simple local-alignment
algorithm, and the Karlin–Altschul statistics behind BLAST — from scratch.

## Sequencing by chain termination

DNA is usually handled as a string of bases, but it is a real three-dimensional molecule, and the
familiar two-dimensional cartoon (bases paired by hydrogen bonds, running antiparallel) is already
a simplification of that structure.

The chemistry of sequencing is the chemistry of the sugar. Number the carbons of the ribose ring
1 through 5: carbon 1 carries the base, carbon 5 connects to the phosphate backbone, and carbon 3
is where the chain is *extended* — the next nucleotide is added there. Three kinds of nucleotide
differ only at carbon 2 and carbon 3:

- **ribonucleotide** — OH at both 2′ and 3′ (RNA)
- **deoxyribonucleotide** — H at 2′, OH at 3′ (DNA; this is what a polymerase normally extends)
- **dideoxyribonucleotide (ddNTP)** — H at *both* 2′ and 3′

A ddNTP has no 3′-OH, so once one is incorporated the polymerase has nothing to attach the next
base to: the chain stops. That one fact — dideoxy nucleotides terminate chain growth — is the whole
basis of **Sanger (chain-termination) sequencing**, developed in the 1970s and the method behind
essentially all DNA sequencing up to the early 2000s.

**The classical protocol.** Clone the template into a vector so the flanking sequence (and a primer
site) is known, and set up four separate reactions, each with the template, a primer, polymerase,
all four normal deoxynucleotides, and *one* dideoxynucleotide — say ddGTP in the "G reaction." The
ddGTP must sit at a much lower concentration than the normal dGTP (around 1%): at equimolar
concentrations every chain would have a roughly 50% chance of terminating at the *first* G, leaving
exponentially less template to reach the second, the third, and so on. At low ddGTP concentration,
termination at any one G is rare, so the reaction yields a full ladder of fragments truncated at
every position where a G occurs — one fragment population per occurrence of each base, across the
four reactions.

Running all four reactions out on a polyacrylamide gel (radiolabeled primer, so only extended
products show up), smallest fragments running fastest, and reading the four lanes from the bottom
up reconstructs the sequence one base at a time. What limits the **read length** (the number of
bases obtained from one sequencing attempt — a *read*) is simply gel resolution: a 20-base fragment
and a 21-base fragment separate easily, but a 500-base and a 501-base fragment barely do, so beyond
some length the lanes can no longer be ordered.

**Dye-terminator sequencing** replaced the four gels with one: label each of the four
dideoxynucleotides with a different fluorophore instead of radiolabeling the primer, run everything
in a single lane, and read off the color at each position. Shrinking the gel to a thin capillary
(**capillary electrophoresis**) with a fluorescence detector at the end gave the ABI 3700 — the
workhorse that sequenced the human genome in the late 1990s and early 2000s. A conventional read of
about 600 bases is short next to a typical mRNA (a few kb), but long enough to span a few exons and
uniquely identify the gene locus it came from — the logic behind **EST (Expressed Sequence Tag)
sequencing**, where millions of ~600-base cDNA fragments were mapped back to loci without ever
assembling full-length transcripts.

## Next-generation sequencing: the general idea

Where Sanger sequencing reads one template per reaction, "next-gen" (second-generation) platforms
read **one base at a time across hundreds of thousands to hundreds of millions of templates in
parallel**. Each run is slower per base and the reads are shorter, but the massive parallelism makes
it orders of magnitude cheaper per base than conventional sequencing — enough that machine cost
figures understate the real economics (a year of reagents for an older instrument could exceed the
machine's own purchase price, yet the cost *per base* is still far lower).

The common skeleton across platforms:

- template DNA molecules are immobilized on a surface, typically a **flow cell**
- either a single molecule is sequenced directly, or the template is first **clonally amplified**
  into a cluster of identical copies (so that a detectable signal accumulates each cycle)
- modified nucleotides, usually carrying a fluorescent tag, are used to interrogate the next base at
  every template simultaneously, cycle after cycle

Platforms differ in (1) how the template is prepared and immobilized, (2) what kind of modified
nucleotide is used, and (3) the imaging and image-analysis step — particularly single-molecule
methods versus cluster-based ones.

### Roche/454: emulsion PCR and pyrosequencing

Template molecules sit on beads at a concentration low enough that an oil-in-water emulsion traps
one bead with one template molecule per droplet (DNA cannot cross between beads). A local PCR
amplifies each bead's template, and sequencing then proceeds one base at a time: each cycle floods
the wells with a single dNTP, and only wells whose next template base is complementary undergo
synthesis, releasing pyrophosphate. Co-immobilized enzymes (sulfurylase and luciferase) convert
that pyrophosphate into light, so the wells that light up identify which templates just incorporated
that base. There is no chemical termination — only one nucleotide type is offered per cycle — so a
homopolymer run (three Gs in a row) produces roughly three times the light of one incorporation,
and that light-to-count relationship is only reliable up to five or six repeats. This is why
**454's dominant error mode is insertions and deletions** in homopolymer runs, rather than
substitutions.

### Illumina/Solexa: bridge amplification and reversible terminators

The template anneals to one of two adapter types covalently attached to the flow cell, is extended,
denatured, and then the free end **bridges over** to hybridize the other adapter type, regenerating
a double-stranded bridge that can itself be extended and denatured — repeated rounds of **bridge
amplification** build a cluster of several hundred thousand identical molecules from one founder
template.

Sequencing adds all four dNTPs at once, but each is modified in two ways: **3′-blocked** (no free
3′-OH, so only one base is added per cycle — Sanger's termination idea, made reversible) and carrying
one of four distinct fluorescent tags. After each incorporation the whole flow cell is imaged in
four channels, the blocking group and fluor are cleaved off, and the next cycle begins. Because the
chemistry is reversible, **Illumina's dominant error mode is substitution**, not indels. A current
high-throughput instrument (HiSeq 2000) runs 8 lanes per flow cell, each yielding on the order of
$2\times10^8$ reads of length 100 bp:

$$8\text{ lanes} \times 2\times10^8\text{ reads/lane} \times 100\text{ bp/read} \approx 1.6\times10^{11}\text{ bp}$$

— more sequence than fifty human genomes from one run, which for most applications is overkill;
**barcoding** (short tags ligated onto samples before pooling) lets many samples share a lane, and
throughput can be doubled again by paired-end sequencing and by running two flow cells at once.

### Helicos and Pacific Biosciences: single-molecule methods

**Helicos** is essentially Illumina's chemistry without amplification: a single template molecule is
immobilized and a single fluorescent tag is read one base at a time directly off it — no clusters,
so no averaging benefit, but no amplification bias either.

**PacBio** is a different design: the **polymerase**, not the template, is covalently attached to
the surface, with an often-circular template threaded through it. The dNTPs carry their label on the
terminal (sixth) phosphate rather than on the base. A labeled nucleotide diffusing through the
active site gives a brief flicker of signal; one actually incorporated dwells much longer, so the
*duration* of the signal, not just its presence, distinguishes real incorporation from background
diffusion. Incorporation itself cleaves away the phosphates and the label, regenerating native DNA —
unlike Illumina, where the growing strand stays chemically modified throughout. A circular template
lets the polymerase reread it multiple times in one run, partially compensating for PacBio's higher
per-pass error rate.

A side-by-side comparison of these and related platforms (read length, run time, yield, machine
cost, pros/cons, typical uses) is given in the slide table (Metzker, *Nature Reviews Genetics*,
2009) — worth consulting directly rather than reproducing here.

## Why align sequences, and why *local* alignment

Once reads exist, aligning them answers several distinct questions: aligning reads to each other can
*assemble* a longer sequence from overlapping fragments; aligning a read to a genome (as in RNA-seq)
tells you which gene it came from; and aligning a sequence against another species' genome can turn
up a **homolog** — a human disease gene of unknown function searched against the mouse genome, say,
to find a candidate for a knockout study.

Not every alignment problem wants the two whole sequences lined up end to end (that is *global*
alignment, next lecture). Often only a *part* of one sequence resembles part of the other, and the
goal is to find that high-similarity stretch without forcing the rest to align — **local
alignment**, the algorithm underlying **BLAST**.

**Motivating example.** You have discovered a human non-coding RNA, 45 bases long, and search it
with BLASTN against the mouse genome (2.7 billion bases). You get back:

```
Q: 1   ttgacctagatgagatgtcgttcacttttactcaggtacagaaaa 45
       |||| |||||||||||| | |||||||||||| || |||||||||
S: 403 ttgatctagatgagatgccattcacttttactgagctacagaaaa 447
```

40 matches, 5 mismatches. Is this significant — strong enough evidence to call the mouse region a
homolog — or is a match this good expected by chance, given how big the mouse genome is? Answering
that requires (1) a scoring system, and (2) a way to attach a probability to a given score.

## A scoring scheme, and the question of significance

The simplest scoring system for DNA: award $+1$ for a match and $-1$ for a mismatch,
$$s_{ii} = 1, \qquad s_{ij} = -1 \ (i \neq j).$$

Given a score, one direct way to assess significance is **empirical**: randomly permute (shuffle)
the query many times (say 1000), search each shuffled version against the same database, and build
up a distribution of the best score obtained by chance. If the real query's score sits far out in
the tail of that distribution, it is significant. This is valid and BLAST is fast enough to make it
practical — but it turns out an **analytical** theory (Karlin & Altschul, 1990) gives the same
answer without the repeated searches, and that is the theory this lecture develops.

## Finding the best ungapped local alignment

Before the statistics, a more basic question: given a query and a (much longer) subject, how do you
*find* the highest-scoring local match? To keep the first algorithm simple, forbid insertions and
deletions — look only for the best **ungapped** local alignment; gaps are added next lecture.

Fix one **register** — one way of sliding the query against the subject so query position $1$ lines
up with some subject position $j$ — and look at the resulting column of matches and mismatches.
Walking along that diagonal, keep a running **cumulative score**: start at 0, add $+1$ for a match
or $-1$ for a mismatch at each step. The highest-scoring ungapped segment along the diagonal is the
one that climbs most *from a low point to a later high point*: the largest value of (cumulative
score now) $-$ (lowest cumulative score seen so far). Tracking just those two running quantities
finds that maximum in a single pass: whenever the current score exceeds the previous best, update
the best segment and record where the minimum and the current position occurred.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Cumulative match/mismatch score along one alignment diagonal, with the highest-scoring segment running from the last local minimum to the following local maximum">
  <line x1="40" y1="20" x2="40" y2="200" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="110" x2="330" y2="110" stroke="currentColor" stroke-width="1"/>
  <text x="20" y="115" font-size="11" fill="currentColor">0</text>
  <text x="340" y="195" font-size="12" fill="currentColor">position</text>
  <text x="10" y="30" font-size="11" fill="currentColor">score</text>
  <rect x="180" y="75" width="105" height="105" fill="currentColor" fill-opacity="0.15"/>
  <polyline points="40,110 75,145 110,110 145,145 180,180 215,145 250,110 285,75 320,110"
            fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="180" cy="180" r="4" fill="currentColor"/>
  <circle cx="285" cy="75" r="4" fill="currentColor"/>
  <text x="155" y="200" font-size="12" fill="currentColor">last minimum</text>
  <text x="250" y="60" font-size="12" fill="currentColor">running max</text>
  <text x="195" y="100" font-size="12" fill="currentColor">segment score = 1-(-2) = 3</text>
</svg>
<figcaption>Cumulative match/mismatch score walking along one alignment register: two mismatches,
a match, two mismatches, then three matches in a row. The highest-scoring ungapped segment is the
rise from the local minimum (-2) to the following local maximum (+1), a segment score of 3 —
exactly the "three matches in a row" visible in the diagonal.</figcaption>
</figure>

Repeating this for every register and taking the best result overall finds the best ungapped local
alignment anywhere in the comparison. With query length $m$ and subject length $n$, this is two
nested loops — for each of the $n$ registers, scan the $m$ query positions — so the running time is
$O(mn)$: a full rectangle of query-versus-subject comparisons, and there is no way to avoid comparing
every base pair in the worst case (searching *many* queries against one database is a separate
question, where indexing/hashing can help). Real BLAST uses algorithmic shortcuts for speed, but is
"morally" an algorithm of this same order.

**Why the expected score must be negative.** If matches scored $+1$ and mismatches $0$ (or anything
non-negative on average), the cumulative score would drift upward indefinitely and the "best segment"
would trivially be almost the whole sequence — the algorithm only finds a meaningful *local* feature
if long stretches tend to lose score on average, with occasional upward excursions standing out
against that drift. With $+1$/$-1$ scoring and three mismatches expected per match (a random
nucleotide matches by chance 1 time in 4), the expected score per position is negative, exactly the
condition Karlin–Altschul statistics require.

## The statistics of local alignment scores

Karlin and Altschul's theory applies whenever scores are integers and the **expected score per
aligned pair is negative** (while individual positive scores remain possible) — exactly the regime
the algorithm above needs to make sense. Under a null model of a random query against a
random database of the same composition, the score $S$ of the best local alignment follows an
**extreme value (Gumbel) distribution**:

$$P(S > x) = 1 - \exp\!\left[-KMN e^{-\lambda x}\right]$$

where $M, N$ are the lengths of the query and the database, $x$ is the score cutoff of interest
(typically the observed score, or one less than it, to ask "how likely is a match this good or
better"), and $K, \lambda$ are positive constants depending on the scoring matrix and sequence
composition. $K$ matters relatively little in practice; **$\lambda$ is the parameter that matters**,
since it sits in the exponent multiplying the score $x$.

$\lambda$ is the unique positive solution of a **transcendental equation**:

$$\sum_{i,j} p_i r_j\, e^{\lambda s_{ij}} = 1$$

where $p_i$ is the frequency of nucleotide $i$ in the query, $r_j$ the frequency of $j$ in the
subject, and $s_{ij}$ the score matrix entry. In general this has no closed form and must be solved
numerically, but in simple cases it reduces to something tractable. Take $p_i = r_j = \tfrac14$ for
all bases and the $+1/-1$ scoring matrix: there are 4 matching pairs (each contributing
$\tfrac14\cdot\tfrac14\, e^{\lambda}$) and 12 mismatching pairs (each contributing
$\tfrac14\cdot\tfrac14\, e^{-\lambda}$), so the equation becomes

$$4\cdot\tfrac{1}{16}e^{\lambda} + 12\cdot\tfrac{1}{16}e^{-\lambda} = 1 \;\Longrightarrow\; e^{\lambda} + 3e^{-\lambda} = 4.$$

Substituting $u = e^{\lambda}$ turns this into the quadratic $u^2 - 4u + 3 = 0$, with roots $u = 1, 3$;
since $\lambda$ must be positive, $u = 3$ is the one that applies, giving $\lambda = \ln 3$.

**$\lambda$ is a scale factor.** Doubling every score in the matrix ($s_{ii}'=2, s_{ij}'=-2$) does
not change which segment scores highest — the same local maxima and minima occur, just relabelled —
but it exactly halves $\lambda$ (each term in the sum has $\lambda s_{ij}$ doubled unless $\lambda$
itself is halved to compensate). In the Gumbel formula, the observed cutoff $x$ also doubles, so the
product $\lambda x$, and hence the reported significance, is unchanged. This is why choosing $+1$
for a match loses no generality: any other positive value for $s_{ii}$ just produces a compensating
$\lambda$, leaving the statistics identical.

## Choosing the mismatch penalty: target frequencies

The theory also predicts what the *matches themselves* will look like once you restrict attention to
high-scoring alignments: the expected frequency of base $i$ aligned to base $j$ in a high-scoring
segment, the **target frequency**, is

$$q_{ij} = p_i p_j\, e^{\lambda s_{ij}} \quad\Longrightarrow\quad s_{ij} = \frac{1}{\lambda}\ln\!\left(\frac{q_{ij}}{p_i p_j}\right).$$

A match ($s_{ij}>0$) inflates $q_{ij}$ above the chance level $p_ip_j$; a mismatch depresses it. This
runs the design process in reverse: instead of picking a mismatch penalty and asking what kind of
matches result, you can *specify* the target identity level you want your high-scoring hits to have,
and solve for the penalty that produces it.

Suppose you want high-scoring segments with $R\%$ identity (write $r = R/100$), and assume unbiased
composition ($p_i = \tfrac14$ for all bases). Then $q_{ii} = r/4$ (the chance of a match, scaled by
how often it should actually occur) and, since there are 12 mismatching base pairs sharing the
remaining probability, $q_{ij} = (1-r)/12$ for $i \neq j$. Fixing $s_{ii} = 1$ (recall this costs no
generality) and taking the ratio $s_{ij}/s_{ii}$ eliminates $\lambda$ entirely:

$$m = s_{ij} = \frac{\ln\big(q_{ij}/(p_ip_j)\big)}{\ln\big(q_{ii}/(p_ip_i)\big)} \;\Longrightarrow\; m = \frac{\ln\!\big(4(1-r)/3\big)}{\ln(4r)} \qquad \left(\tfrac14 < r < 1\right).$$

Note $r$ must exceed $\tfrac14$ (chance level) for this to describe anything meaningfully
above-chance, and $m$ comes out negative throughout that range, as required. Evaluating at a few
values of $r$:

| target identity $r$ | 0.75 | 0.95 | 0.99 |
|:---:|:---:|:---:|:---:|
| mismatch penalty $m$ | $-1$ | $-2$ | $-3$ |

So wanting *higher*-identity hits calls for a *more* negative mismatch penalty — a steeper penalty
makes the algorithm more reluctant to tolerate any mismatch at all, concentrating the high-scoring
segments it reports on stretches that are almost exact matches. (The lecture closes by asking
students to think through why this direction of the relationship makes sense, rather than giving the
intuition away.)

One refinement mentioned but not pursued for simplicity: a single mismatch penalty treats every
substitution the same, but transitions (A$\leftrightarrow$G, C$\leftrightarrow$T) are structurally
more similar and occur spontaneously more often than transversions — a more realistic matrix would
penalize transversions more heavily. The lecture keeps one uniform penalty to keep the algebra
simple.

## Exercises

The following is Problem set 2 as issued for the course. It was assigned across several lectures,
not only this one, and only some of it concerns material from this chapter — it is included here
under its own number, not as an exercise set for this lecture specifically.

**Problem set 2 — BWT, library complexity, RNA-seq, genome assembly, motifs, multiple hypothesis
testing (31 points)**

**Problem 1. Aligning reads to a genome using a Burrows–Wheeler transform and FM-index (9 pts).**
Using provided scaffold code, implement the core of a genome search function built on the
Burrows–Wheeler transform and an FM-index.
(A, 7 pts) Complete the LF-mapping function `_lf(self, idx, qc)` and the search function
`bounds(self, q)` in `fmindex.py`, and verify the implementation against the supplied test index and
expected output.
(B, 2 pts) Build the FM-index for a 10 kb yeast chromosome segment, map the supplied reads against
it, and submit the resulting mapped-reads file.

**Problem 2. Library complexity (5 pts).** A sequencing library constructed from a sample contains
exactly 40 million unique molecules, selected uniformly at random each time a library is built; the
model organism (*C. elegans*) has a genome of about 100 million base pairs. A given experiment
requires observing at least 12 million *unique* molecules. Sequencing is sold in lanes of 10 million
reads each, any number of lanes per library; each library preparation costs \$500 and each lane
costs \$1000.
(A, 2 pts) Assuming every molecule in a library is equally likely to be sequenced, find the most
cost-effective combination of libraries and lanes that achieves 12 million unique molecules
observed, and show the reasoning.
(B, 3 pts) Now suppose the per-molecule selection probability instead varies according to a negative
binomial distribution with rate $\lambda = 0.25$ (10 million reads over 40 million molecules) and
dispersion parameter $k = 2$. Find the most cost-effective design under this model, and comment on
how the answer differs from part (A). (A hint in the original points to the lecture slides for the
failures/success-probability parameterization of the negative binomial.)

**Problem 3. Differential gene expression (4 pts).** An RNA-seq experiment has three biological
replicates in each of two treatment conditions (six samples total), sequenced separately.
(A, 1 pt) If the sequencing reads for each condition are pooled into two combined samples before
analysis, what kind of variation becomes impossible to observe, and why might it matter?
(B, 3 pts) Propose an improved analysis strategy that keeps the six samples separate, state what
sources of variation it lets you detect, and describe how you would estimate the mean–dispersion
relationship needed for a negative-binomial model of the counts.

**Problem 4. RNA isoform quantification (3 pts).** A gene structure is given (exon sizes and
positions, two alternative transcription start sites, and exons 2 and/or 3 optionally spliced out).
(A, 1 pt) How many distinct isoforms can this gene structure produce?
(B, 1 pt) For each isoform, list the junction-spanning RNA-seq reads that would support it.
(C, 1 pt) For single-ended reads, what is the shortest read length guaranteed to unambiguously
identify every isoform, if a junction-spanning read must overlap each flanking exon by at least 5 bp?

**Problem 5. De Bruijn graphs (5 pts).** A set of ten 6 bp reads, all in the same orientation, is
given (AGCTGT, CAGCTG, TTCTGC, GCTGTA, TCAGCT, CTGTAT, TGTAGC, TTCAGC, CTGTAG, TTTCAG), obtained from
sequencing a single RNA molecule.
(A, 1 pt) Construct the de Bruijn graph for these reads with $k = 5$.
(B, 1 pt) Collapse any simple chains and remove any tips in the graph.
(C, 1 pt) Identify any bubbles, and resolve each by removing the path more likely to be a sequencing
error.
(D, 1 pt) Which read(s) contain a sequencing error, and what is the error?
(E, 1 pt) Give the sequence represented by the corrected graph.

**Problem 6. Modeling and information content of a sequence motif (5 pts).** Spliced alignment of
genomic and cDNA sequence from three protist species (A, B, C) gives 10,000 confirmed 3′ splice
sites per species. In all three, the invariant intron-terminal AG is preceded by an 8-base
polypyrimidine tract (PPT) with overall base frequencies $f_C = f_T = \tfrac12$ at every position.
Build, for each species, the *simplest* model that still reproduces the observed 8-mer frequencies,
and report its information content using $I = 2w - H(\text{model})$ bits, where $w$ is the motif
width and $H$ is the Shannon entropy of the model. (Write $\mathrm{Y}_8$ for an 8-mer made entirely
of pyrimidines.)
(A, 1 pt) In species A, every dinucleotide CC/CT/TC/TT occurs with frequency $\tfrac14$ at each of
the seven adjacent position pairs, and every $\mathrm{Y}_8$ 8-mer occurs with frequency $2^{-8}$.
Describe, in one sentence, a model for this PPT, and give its information content.
(B, 1 pt) In species B, the same dinucleotide frequencies hold at each adjacent pair
($f_{CC}=f_{CT}=f_{TC}=f_{TT}=\tfrac14$), but the 8-mer frequencies show
$f_{T_8} = f_{C_8} = f_{(TC)_4} = f_{(CT)_4} = \tfrac14$ (all other $\mathrm{Y}_8$ 8-mers absent).
Describe a model for this PPT in one sentence, and give its information content.
(C, 3 pts) In species C, $f_{CC} = f_{TT} = \tfrac38$ and $f_{TC} = f_{CT} = \tfrac18$ at each
adjacent pair, and every $\mathrm{Y}_8$ 8-mer has frequency $3^{a+b}/Z$, where $a$ and $b$ are the
number of CC and TT dinucleotides it contains and $Z$ normalizes the frequencies to sum to 1.
Describe a model for this PPT in one sentence, and give its information content.

**(Extra, 6.874) Multiple hypothesis testing (4 pts).** A differential-expression analysis (e.g. via
DESeq) returns uncorrected p-values for 20 genes:

| Gene | P-value | Gene | P-value |
|:---:|:---:|:---:|:---:|
| 1 | 0.0002 | 11 | 0.0150 |
| 2 | 0.0005 | 12 | 0.0230 |
| 3 | 0.0040 | 13 | 0.0240 |
| 4 | 0.0060 | 14 | 0.0340 |
| 5 | 0.0070 | 15 | 0.0390 |
| 6 | 0.0080 | 16 | 0.0470 |
| 7 | 0.0090 | 17 | 0.0500 |
| 8 | 0.0110 | 18 | 0.0580 |
| 9 | 0.0120 | 19 | 0.0600 |
| 10 | 0.0120 | 20 | 0.0980 |

(A, 1 pt) Apply Bonferroni correction at $\alpha = 0.05$ and list the genes called differentially
expressed, showing the cutoff used.
(B, 1 pt) Apply Benjamini–Hochberg correction at $\alpha = 0.05$ and list the genes called
differentially expressed, showing how the list was obtained.
(C, 2 pts) Compare the two lists in composition, and say what the comparison shows about the
relative stringency of the two corrections.

## Sources

- Slides: `lectures/02-slides/01-local-alignment-blast-and-statistics.md` (nucleotide chemistry,
  Sanger sequencing, next-gen overview) and `02-comparison-of-platforms.md` (platform table,
  template-preparation and 454/Illumina figures, local-alignment/BLAST-statistics slides —
  motivating example, Karlin & Altschul 1990 equations, target-frequency derivation, mismatch table).
- Transcript: `recordings/lectures/02.md`, C. Burge, Feb. 6 2014 — nucleotide chemistry and Sanger
  protocol (00:00–13:32), next-gen platforms and throughput (13:32–31:18), motivation for local
  alignment and the worked cumulative-score algorithm (31:18–56:19), and the Karlin–Altschul
  statistics including the worked $\lambda$ example and target-frequency derivation (56:19–end).
  Administrative announcements and the Creative Commons notice have been stripped as boilerplate.
- Problem set 2: `psets/02-questions-pset2-ques/01-04` and `psets/02-questions.md` (cover page and
  figures only; the problems are in the four linked files). Every problem is included exactly once
  even though the set spans multiple source files.
- Referred to but not contained in the supplied material: Metzker, "Sequencing Technologies — The
  Next Generation," *Nature Reviews Genetics* 11 (2009): 31–46; Margulies et al., "Genome Sequencing
  in Microfabricated High-density Picolitre Reactors," *Nature* 437 (2005): 376–80; Karlin & Altschul,
  *PNAS* 1990; and Zvelebil & Baum ("Z&B"), chapters 4–5, cited as background reading.

---

[← 1. Introduction to Computational Biology](01-introduction-to-computational-biology.md) · [Contents](index.md) · [3. Global Alignment and Scoring Matrices →](03-global-alignment-and-scoring-matrices.md)
