---
title: "2. Local Alignment (BLAST) and Statistics"
course: "MIT 7.091J"
chapter: 2
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Local Alignment (BLAST) and Statistics

## What this covers

This lecture opens the course's segment on sequence alignment, and it answers two connected
questions. First, where do the sequences you would even align come from — a fast tour of Sanger
sequencing and the second-generation platforms that replaced it. Second, once you have a **local
alignment** — a short stretch of high similarity between two sequences — how do you tell whether it
means anything, as opposed to being the kind of match you'd expect to see by chance between two
sequences with no real relationship. It assumes you already know what a nucleotide sequence and a
match/mismatch score are, and are comfortable with elementary probability: expectation, a
probability distribution, a p-value.

## Reading a sequence: Sanger and second-generation platforms

**Sanger (chain-termination) sequencing.** A primer anneals to the template and DNA polymerase
extends it. The reaction is split into four pools, each supplemented with one **dideoxynucleotide**
(ddGTP, ddATP, ddCTP, or ddTTP) alongside the normal nucleotides. A dideoxynucleotide is missing the
3'-OH group that polymerase needs in order to attach the next base, so whenever one is incorporated
the growing strand stops permanently at that position. Within each of the four pools this produces
a whole population of fragments of every length that happens to end in that particular base.
Running all four pools out side by side on a gel and separating fragments by size (originally with
radiolabeling and autoradiography) turns "which lane is the next-shortest fragment in" into "what is
the next base" — reading the four lanes from shortest to longest fragment reconstructs the sequence
one base at a time. The slide's own worked fragment ladders come from a two-dimensional gel diagram
that the source conversion has flattened into a run of text, and the printed lengths in it aren't
fully self-consistent, so they aren't reproduced here as a solved example — the mechanism above is
the part that survives the conversion intact.

The technology then moved through three stages:

- **Traditional Sanger (1970s–90s):** large polyacrylamide gels, radiolabeled DNA, four physical
  lanes per read.
- **Fluorescent dye-terminator sequencing (1990s–present):** each ddNTP carries a different
  fluorescent tag, so all four reactions can run in one capillary — one lane per read instead of
  four.
- **"Next-generation" (second-generation) sequencing:** instead of one long read at a time, a cycle
  of chemistry plus imaging is repeated over millions of spatially separated DNA templates at once;
  each cycle answers "what is base $k$?" for every template simultaneously, so throughput scales
  with how many templates you can pack onto a surface rather than with how long any one read is.
  Platforms differ chiefly in three respects: how the DNA template is prepared, which modified
  nucleotides are used, and how the resulting images are captured and analyzed (Shendure & Ji,
  *Nature Biotechnology*, 2008).

**Template preparation** splits along the same lines as the platforms below: 454, SOLiD, and the
Polonator use **emulsion PCR** — one DNA molecule per bead, clonally amplified to thousands of
copies inside a droplet of an emulsion; Illumina/Solexa uses **solid-phase (bridge) amplification**
— one molecule per cluster, amplified directly on the flow cell surface; Helicos and Pacific
Biosciences sequence **single molecules** directly, with the template (Helicos) or the polymerase
itself (PacBio) immobilized, and no amplification step at all (Metzker, *Nature Reviews Genetics*,
2010).

A condensed version of the lecture's platform comparison table:

| Platform | Read length (bp) | Throughput | Machine cost | Strength | Weakness |
| --- | --- | --- | --- | --- | --- |
| Roche/454 GS FLX Titanium | ~330 | 0.45 Gb/run | $500,000 | longer reads help mapping in repetitive regions; fast runs | costly reagents; high error in homopolymer runs |
| Illumina/Solexa GA$_{\text{II}}$ | 75–100 | 18–35 Gb/run | $540,000 | most widely used platform in the field | low sample multiplexing |
| Life/APG SOLiD 3 | 50 | 30–50 Gb/run | $595,000 | two-base encoding gives inherent error correction | long run times |
| Polonator G.007 | 26 | 12 Gb/run | $170,000 | cheapest; open-source, adaptable chemistry | high maintenance burden; shortest reads |
| Helicos HeliScope | ~32 | 37 Gb/run | \$999,000 | unbiased representation of templates | high error rate vs. other reversible-terminator chemistries |
| Pacific Biosciences (2010) | ~964 | n/a | n/a | greatest potential for reads over 1 kb | highest error rate of the group |

(Metzker, *Nature Reviews Genetics*, 2009/2010.)

Two worked throughput numbers from the lecture make the scale concrete. Bead-based pyrosequencing
(454) gets roughly 400+ nucleotides per well; run across about a million wells on a plate, that is

$$400\ \text{nt} \times 1{,}000{,}000\ \text{wells} \approx 400\ \text{Mbp per run}$$

in about ten hours, for a few thousand dollars (Margulies et al., *Nature*, 2005; numbers updated
since). An Illumina HiSeq 2000 run uses 8 lanes per flow cell:

$$8\ \text{lanes} \times 2\times10^{8}\ \text{reads/lane} \times 100\ \text{bp/read} \approx 160\times10^{9}\ \text{bp}$$

in several days, for roughly \$20,000 in reagents — and this can be doubled again by paired-end
sequencing or by running two flow cells at once.

Whatever the platform, once you have reads you need to compare them — to a reference genome or to
each other — and that comparison is an alignment problem. The rest of the lecture is about the
particular kind of alignment BLAST computes, and how to decide whether a match it finds is real.

## Local alignment: finding short stretches of high similarity

Sequence alignment splits into a few standard problems, solved by dynamic programming, that differ
only in **which part of the two sequences the score is required to cover**:

- **Global alignment** requires every position of both sequences to be matched, with penalties for
  gaps anywhere, including at the ends — appropriate when the two sequences really are meant to
  correspond end to end, e.g. aligning mouse GAPDH to human GAPDH.
- **Semiglobal alignment** still requires every position to be matched, but drops the penalty for
  gaps at the very ends, so a long sequence can overhang a shorter one for free — appropriate when
  one sequence is a small piece expected to sit somewhere inside the other, e.g. aligning the
  promoter of chicken $\beta$-globin against the whole human genome.
- **Local alignment** drops the end-to-end requirement altogether: it finds the highest-scoring
  matching subsequence of one sequence against a subsequence of the other, and simply ignores the
  rest of both — appropriate when only a piece of each sequence is expected to be related at all,
  e.g. aligning just the zinc-finger domains shared between yeast Swi5 and a *Drosophila* protein.

BLAST computes local alignments — in the simple version this lecture builds, *local and ungapped*:
it looks for short, high-scoring segments and does not require the alignment to extend to cover
either whole sequence.

<figure>
<svg viewBox="0 0 360 200" role="img" aria-label="Three ways two sequences can be aligned: global, semiglobal, and local">
  <text x="8" y="28" font-size="12" fill="currentColor">global</text>
  <rect x="60" y="8" width="260" height="32" fill="currentColor" fill-opacity="0.15"/>
  <rect x="60" y="10" width="260" height="12" fill="none" stroke="currentColor"/>
  <rect x="60" y="26" width="260" height="12" fill="none" stroke="currentColor"/>

  <text x="8" y="89" font-size="12" fill="currentColor">semiglobal</text>
  <rect x="150" y="66" width="90" height="38" fill="currentColor" fill-opacity="0.15"/>
  <rect x="40" y="70" width="280" height="12" fill="none" stroke="currentColor"/>
  <rect x="150" y="90" width="90" height="12" fill="none" stroke="currentColor"/>

  <text x="8" y="149" font-size="12" fill="currentColor">local</text>
  <rect x="170" y="126" width="40" height="38" fill="currentColor" fill-opacity="0.15"/>
  <rect x="40" y="130" width="280" height="12" fill="none" stroke="currentColor"/>
  <rect x="40" y="150" width="280" height="12" fill="none" stroke="currentColor"/>

  <text x="180" y="188" text-anchor="middle" font-size="11" fill="currentColor">shaded = the part actually scored</text>
</svg>
<figcaption>Global, semiglobal, and local alignment differ only in which part of the two sequences
the score (and any gap penalty) covers. Local alignment, the kind BLAST computes, scores only the
best-matching internal stretch and charges nothing for the rest of either sequence.</figcaption>
</figure>

**The motivating example.** You are studying a newly discovered human non-coding RNA. Searching it
against the mouse genome with BLASTN (nucleotide BLAST) turns up this local alignment:

```
Q: 1   ttgacctagatgagatgtcgttcacttttactcaggtacagaaaa 45
       |||| |||||||||||| | |||||||||||| || |||||||||
S: 403 ttgatctagatgagatgccattcacttttactgagctacagaaaa 447
```

Forty of the 45 aligned positions match (about 89% identity, five mismatches scattered through the
alignment). Is this alignment significant — likely to reflect a real evolutionary relationship
(homology) between the human and mouse sequences — or is it the kind of similarity you'd stumble
into anyway between two unrelated sequences of this length? Answering that requires knowing, for
sequences with no real relationship, how good a match to expect purely by chance.

## Assessing significance: the extreme-value distribution

What is reported as "the" score of a local alignment is really the **best** score found over very
many candidate starting positions and offsets in the comparison — one number picked out as the
maximum of a large number of trials. That is a different question from the one the central limit
theorem answers (which governs sums and averages); the natural limiting theory for the *maximum* of
many roughly independent trials is extreme-value theory. That is why local alignment scores are not
expected to be normally distributed, and instead follow an **extreme value (Gumbel) distribution**:

$$P(S > x) = 1 - \exp\!\left[-KMN e^{-\lambda x}\right]$$

Here $M$ and $N$ are the lengths of the query and the database (or of the two sequences being
compared), and $K$ and $\lambda$ are positive parameters that depend on the scoring matrix and on
the composition of the sequences (Karlin & Altschul, 1990). The formula requires one condition to
hold: the **expected score of a random aligned pair must be negative**, even though individual
pairs can score positive. Without that condition, random sequence would drift to arbitrarily high
scores just by accumulating length, there would be no well-defined "best local score," and the
whole theory breaks down. With it, a positive-scoring stretch is a rare upward excursion against a
downward drift — exactly the kind of rare, sharply-decaying event an extreme-value tail describes.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A right-skewed extreme-value density with the tail beyond a score x shaded">
  <line x1="30" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <path d="M30,160 Q55,55 95,45 Q140,55 170,80 Q220,115 250,138 Q275,150 300,155" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M190,160 L190,84 Q220,115 250,138 Q275,150 300,155 L300,160 Z" fill="currentColor" fill-opacity="0.15"/>
  <line x1="190" y1="160" x2="190" y2="80" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="190" y="176" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="248" y="126" font-size="12" fill="currentColor">P(S &#62; x)</text>
  <text x="300" y="176" text-anchor="end" font-size="12" fill="currentColor">score S</text>
</svg>
<figcaption>The density of the best local-alignment score, under a null model of unrelated
sequences, is right-skewed. The p-value of an observed score $x$ is the shaded tail area.</figcaption>
</figure>

One bookkeeping point: alignment scores are discrete (sums of integer match/mismatch scores), so
"a score at least as extreme as the one observed" means $P(S \ge x) = P(S > x-1)$, not $P(S > x)$
directly. For a continuous score distribution no such off-by-one correction is needed.

**When there's no clean formula: shuffle instead.** If you don't trust, or don't have, a
closed-form null distribution for your particular scoring scheme, you can build one empirically.
Score every position of a real sequence against your model, then shuffle the sequence and rescan:
any high-scoring hits found in the shuffled version happened purely by chance, not biology, and a
histogram of the shuffled scores approximates the null distribution directly. A recitation example
of scanning human chromosome 21 for the CTCF motif made this concrete: the shuffled-genome
distribution had about 68 million scores in it, so the top real hit (score 26.30) got a p-value of
$1/(68\text{ million}) \approx 1.5\times10^{-8}$, while a weaker score of 17, exceeded by 35 shuffled
hits, got $p \approx 35/(68\text{ million}) \approx 5.5\times10^{-7}$. The same idea applies
directly to alignment: shuffle the database and see how often a match this good turns up by chance.

## Where $\lambda$ comes from

$\lambda$ is defined as the unique positive solution of a transcendental equation:

$$\sum_{i,j} p_i r_j\, e^{\lambda s_{ij}} = 1$$

where $p_i$ is the frequency of nucleotide $i$ in the query, $r_j$ the frequency of nucleotide $j$
in the subject, and $s_{ij}$ the score assigned to aligning an $i,j$ pair. "Transcendental" because
$\lambda$ sits inside an exponential: for an arbitrary $4\times4$ scoring matrix there are up to 16
distinct terms in the sum, plus a normalizing constant, and in general no closed-form solution — you
would find $\lambda$ numerically. The simple match/mismatch matrix used throughout this lecture is
the exception: with only one match score and one mismatch score, the sum collapses to two distinct
terms, and substituting $y = e^{\lambda}$ turns the equation into a quadratic in $y$ with a closed
form; only the positive root corresponds to a valid $\lambda$.

$\lambda$ also has a scaling property worth noting: doubling every score in the matrix halves
$\lambda$, exactly compensating so the sum still equals 1 (since only the product $\lambda s_{ij}$
appears). $\lambda$ is therefore not a meaningful number on its own — it is the scaling factor that
converts whatever units you chose for your scoring matrix into the units the extreme-value formula
is written in.

## Choosing a scoring matrix: target frequencies and the mismatch penalty

For nucleotide alignments the simplest scoring matrix uses just two numbers: a match score,
normalized to $s_{ii} = 1$, and a mismatch penalty $m$ (negative) for every $i \ne j$ pair. The
lecture's open question is which value of $m$ to use — $-1$? $-3$? $-5$? — and the answer comes from
asking what kind of matches you actually want to find.

Define the **target frequencies**

$$q_{ij} = p_i r_j\, e^{\lambda s_{ij}}.$$

Because the $q_{ij}$ sum to 1 by the equation that defines $\lambda$, they form a probability
distribution — specifically, the distribution of nucleotide pairs you should expect to see *within
real high-scoring alignments*, as opposed to $p_i r_j$, which is what you'd expect if the two
positions were unrelated. Inverting the relation gives the score in terms of the target frequency:

$$s_{ij} = \frac{1}{\lambda}\ln\!\left(\frac{q_{ij}}{p_i r_j}\right).$$

So choosing a scoring matrix is exactly equivalent to choosing what the pair frequencies in your
high-scoring alignments should look like.

**Tuning to a target percent identity.** Suppose you want your matrix tuned to alignments with
about $R\%$ identity, and let $r = R/100$. Split the "identical" probability mass $r$ equally over
the 4 identical pairs, $q_{ii} = r/4$, and the "different" mass $1-r$ equally over the 12 ordered
mismatched pairs, $q_{ij} = (1-r)/12$ for $i \ne j$. Fixing $s_{ii} = 1$ as the reference score and
taking the ratio of the mismatch and match versions of the score formula cancels the unknown
$\lambda$:

$$m = \frac{s_{ij}}{s_{ii}} = \frac{\ln(q_{ij}/p_ir_j)}{\ln(q_{ii}/p_ir_i)} \qquad (i \ne j).$$

Assuming equal base composition ($p_i = r_j = 1/4$ for every base), this simplifies to

$$m = \frac{\ln\!\big(4(1-r)/3\big)}{\ln(4r)}, \qquad \tfrac14 < r < 1.$$

| target identity $r$ | 0.75 | 0.95 | 0.99 |
| :---: | :---: | :---: | :---: |
| mismatch penalty $m$ | $-1$ | $-2$ | $-3$ |

This closes the loop on the earlier question. A mismatch penalty of $-1$ is tuned to find alignments
around 75% identity — useful for fairly diverged, cross-species comparisons. A penalty of $-2$
targets around 95% identity — closely related sequences. As $r \to 1$, $\ln\!\big(4(1-r)/3\big) \to
-\infty$ while $\ln(4r)$ stays finite, so $m \to -\infty$: the penalty needed to reject
chance similarity grows without bound as the target identity approaches 100%. A penalty around
$-3$ or harsher, such as $-5$, is what you would reach for when searching for near-identical
matches — recent duplicates or reads from the same genome.

## From a score to a decision

Putting the two halves of the lecture together, deciding whether a local alignment is significant
takes three steps: choose a scoring matrix tuned to the identity level you're actually looking for
(previous section); compute the alignment's score $S$; then convert $S$ to a p-value against the
real size of the search, using either the extreme-value formula with the matrix's own $K$ and
$\lambda$, or an empirical shuffled null if you don't trust the closed form for your case.

One thing this lecture raises but does not develop: a real search scans an entire genome, which
means checking the significance of one score is only half the problem — you are implicitly running
one such test at every candidate position, millions of them, and controlling for that requires a
multiple-testing correction (for example Bonferroni or Benjamini–Hochberg). That is a separate topic
taken up elsewhere in the course.

## Sources

- Slides: `lectures/02-slides/01-local-alignment-blast-and-statistics.md` and
  `02-comparison-of-platforms.md` (Lecture 2, C. Burge, Feb. 6, 2014) — Sanger sequencing, the
  evolution of sequencing technologies, the platform comparison table, next-gen templates and
  throughput examples, the motivating BLASTN alignment, the extreme-value formula, the $\lambda$
  equation, and the target-frequency/mismatch-penalty derivation all come from these two files.
  Administrative slides (office hours, problem-set logistics, the request for background emails)
  were cut as boilerplate, and the title-only "1D, 2D and 3D Representations of DNA" and "Extreme
  Value (Gumbel) Distribution" slides carried images not captured by the conversion; the Gumbel
  figure here is a reconstruction of the standard shape that slide's title names, not a
  reproduction of the original plot.
- No transcript was supplied for this lecture, so the explanatory connective tissue around the
  slides — including the extreme-value/maximum-of-many-trials argument and the reasoning about why
  the expected score must be negative — is filled in from the closely paired recitation below
  rather than from the lecturer's own words.
- Recitation `recitations/2014-02-12-slides/01-2014-02-12-slides-part-01.md`, explicitly labelled
  "CB Lectures #2 and 3" — used for the p-value definition, the constraint that the expected score
  must be negative, the discrete-score off-by-one correction, the three-way alignment taxonomy
  (global/semiglobal/local) with its worked examples, and the term-counting argument for why the
  $\lambda$ equation is generally transcendental but reduces to a quadratic for a simple
  match/mismatch matrix.
- Recitation `recitations/2014-02-11-slides/03-null-distribution.md` — used for the empirical-null
  (shuffling) idea and the CTCF motif-scanning worked example.
- The lecture's own reading pointer, "Background for next two lectures: Z&B Ch. 4 & 5," and the
  Karlin & Altschul (1990) paper that the statistics in this chapter are attributed to, are both
  named on the slides but not contained in the supplied material.
- The slide deck lists "a simple BLAST-like algorithm" as a lecture topic, but the algorithm itself
  — how BLAST actually searches for seeds and extends them — is not present in the converted slide
  text and there is no transcript to recover it from; this chapter accordingly covers only the
  statistics of matching, not the search algorithm.
- Not used: the pset 2 questions (`psets/02-questions.md` and its parts) and the recitations dated
  2014-02-11 part 1 (PWMs), 2014-02-14 (clustering, hierarchical clustering, biclustering),
  2014-02-19 (linear algebra, Markov chains, PAM vs. BLOSUM, positive/negative selection), and
  2014-02-26 (library complexity, BWT) were supplied alongside this lecture's materials but test
  content from later lectures — motif models, clustering, molecular evolution, BWT/FM-index,
  library complexity, RNA-seq, multiple hypothesis testing — that this lecture does not cover, so
  no exercises are given here.

---

[← 1. Sequence Search and Alignment Statistics](01-sequence-search-and-alignment-statistics.md) · [Contents](index.md) · [3. BLAST Statistics and Global Alignment →](03-blast-statistics-and-global-alignment.md)
