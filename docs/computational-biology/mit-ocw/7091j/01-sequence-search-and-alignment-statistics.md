---
title: "1. Sequence Search and Alignment Statistics"
course: "MIT 7.091J"
chapter: 1
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Sequence Search and Alignment Statistics

## What this covers

This chapter follows the opening lecture of 7.91J. The slides do two things: they lay out the two
halves of the course — from raw sequencing reads to genome function, and from genome to phenotype
— and preview the structural and network-biology material that comes later. The first problem set,
given alongside them, introduces the toolkit the rest of the course leans on: searching a sequence
against a genome, aligning two sequences that don't match letter for letter, and deciding whether an
alignment means anything or is just luck. This chapter previews the roadmap material as the lecture
gave it — as pointers, not full treatments — and then works the problem-set toolkit in detail. It
assumes ordinary molecular-biology vocabulary (DNA, RNA, transcription, exons, codons, open reading
frames) and elementary probability (an expectation, the tail of a distribution).

## A map of the course

### From reads to a genome

A high-throughput sequencer does not hand you a genome; it hands you tens or hundreds of millions of
short reads, and the first block of the course is about turning those into something interpretable.

One slide makes the read-mapping idea concrete: a reference genome, and a read pair whose two ends
— 35 bp each — align exactly to known positions, with 330–430 bp of unsequenced insert in between.
Knowing where the two ends sit tells you where the fragment came from before you know what the
missing middle says.

Assembling a genome *de novo* — without a reference to map against — is the harder problem of
lecture 6: start from many copies of the genome, shear them into random fragments, size-select the
fragments you want to sequence, read them, and then glue overlapping reads back together.

<figure>
<svg viewBox="0 0 760 150" role="img" aria-label="Shotgun sequencing pipeline from many genome copies to assembled scaffolds">
<defs>
<marker id="arrow1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
</marker>
</defs>
<rect x="10" y="50" width="110" height="50" rx="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="65" y="80" text-anchor="middle" font-size="11" fill="currentColor">(a) copies</text>
<line x1="120" y1="75" x2="135" y2="75" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>
<rect x="135" y="50" width="110" height="50" rx="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="190" y="80" text-anchor="middle" font-size="11" fill="currentColor">(b) shear</text>
<line x1="245" y1="75" x2="260" y2="75" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>
<rect x="260" y="50" width="110" height="50" rx="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="315" y="80" text-anchor="middle" font-size="11" fill="currentColor">(c) size-select</text>
<line x1="370" y1="75" x2="385" y2="75" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>
<rect x="385" y="50" width="110" height="50" rx="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="440" y="80" text-anchor="middle" font-size="11" fill="currentColor">(d) reads</text>
<line x1="495" y1="75" x2="510" y2="75" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>
<rect x="510" y="50" width="110" height="50" rx="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="565" y="80" text-anchor="middle" font-size="11" fill="currentColor">(e) contigs</text>
<line x1="620" y1="75" x2="635" y2="75" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>
<rect x="635" y="50" width="110" height="50" rx="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="690" y="80" text-anchor="middle" font-size="11" fill="currentColor">(f) scaffolds</text>
</svg>
<figcaption>Shotgun assembly: overlapping reads are merged into contigs, and contigs are ordered and
oriented into scaffolds ("super-contigs") using longer-range information.</figcaption>
</figure>

Two more read-based assays round out this module. In ChIP-seq (lecture 7), reads from a
chromatin-immunoprecipitation pull-down for a specific regulator — the slide's example is Oct4 and
Sox2 — pile up around the genomic positions that regulator actually occupies, and comparing that
pile-up against a whole-cell-extract control marks the binding sites. In RNA-seq (lecture 8), reads
that fall entirely inside one exon confirm that the exon is expressed, while "junction reads" split
across an exon–exon boundary reveal how the transcript was spliced; together they give both an
expression level and the isoform structure (the slide's example is the gene *Smug1*).

### From genome to phenotype

The second module turns the same kind of data toward genotype–phenotype questions. Chromatin
accessibility, tracked over a genomic window as a cell differentiates (the slide's example: an
embryonic stem cell at day 2, day 3 and day 5 across roughly 50 kb), marks functional elements —
regions that switch from closed to open, or the reverse, as the cell changes state (lecture 18).
Quantitative trait loci (QTLs) link genetic loci to a measurable trait such as growth rate, by
crossing strains and tracking which parental genotype at each locus travels with the phenotype — the
slide's example is a yeast cross used to track down "missing heritability" (Bloom et al., lecture
19). Genome-wide association studies (GWAS) scan the whole genome's worth of common variants at once
and ask which ones track with disease risk: the slide shows the classic picture for this, a
genome-wide scan across several diseases with $-\log_{10}$ of a per-SNP test statistic plotted
against chromosomal position, so that a real association shows up as a tower of points rising above
the background (lecture 20).

### Structure and networks

The lecture also previews material that comes later still, at coarser and finer scales than a
sequence: physics-based force fields at the atomic scale (the slide gives a harmonic bond-stretching
term, $U_{bond} = \sum_{\text{bonds}} K_b(b-b^0)^2$, as one term in such a model), protein structure
at the molecule scale, and interaction networks at the cell scale. On structure prediction
specifically, two contrasting stories are previewed: molecular-dynamics simulation on a
special-purpose machine (Anton) reached the hundreds-of-microseconds timescale needed to watch small
"fast-folding" proteins fold and land close to their known structures; and, separately, players of
the video game *Foldit* — humans using spatial intuition, not a fitted potential — outperformed the
best available folding algorithm on ten proteins. Later lectures also cover predicting which protein
surfaces dock together, gene-regulatory networks (the slide's example: a genome-scale network of
microRNA-mediated competition among RNAs in glioblastoma), protein-interaction networks organised by
the biological process their members serve, and encoding a signalling network as a logic model whose
consistent solutions can be enumerated exhaustively.

None of this is developed in the slides beyond a caption and a citation — it is a map of where the
course is going, not a lesson in any one of these techniques. The rest of this chapter instead works
through the one piece of technical toolkit the lecture's own problem set actually develops: how to
search for a sequence, how to align two sequences that are similar but not identical, and how to
tell whether either result means anything.

## Searching a genome: BLAST and the E-value

Suppose you have a sequence of interest — a query — and you want to know where, if anywhere, it
occurs in a genome or transcriptome. A search tool such as BLAST scores every candidate match it
finds and reports, for each hit, a score and an **E-value**: the expected number of hits with a
score at least as high as this one, if you searched a query of this length against a database of
this size purely by chance. A small E-value means a hit that good would be a surprising coincidence;
a large one means you'd expect to see hits like it even with an unrelated query.

For a hit measured as a **bit score** $S$ — a score already normalised for the scoring scheme in use
— against a query of length $m$ and a database of length $n$, the relationship is

$$E = mn\,2^{-S}.$$

This is the idealised form: real BLAST output applies further corrections for base composition,
repetitive sequence, and related effects, so a reported E-value will not match this formula exactly.
But it captures the two things that matter — the E-value grows with the size of the search space
($m$ and $n$), and it falls off exponentially in the score.

**A worked case.** A mouse strain is ill unless fed a phenylalanine-free diet. Sequencing finds that
a highly expressed 68-nucleotide non-coding RNA differs from the wild-type sequence:

> mutant: `UGUACAUGAUGAAGUCAUAGCGAACGGAGAAGGGCCGGCUGAGGAAACUGCACGUCACCCUCCUGAAA`
> wild type: `UGUACAUGAUGAAAACAGUCUCCCUCUUCUGAAUCUCGCUGAGGAAACUGCACGUCACCCUCCUGAAA`

Searching the mutant sequence against the mouse genome-plus-transcript database (BLASTn, match/mismatch
scores $+1/-3$) turns up two transcript hits and two genome hits with $E \le 0.05$. The two transcript
hits have bit scores 54 and 50.1: the 54-bit hit covers query positions 38–68 at 97% identity (30 of
31 positions), and the 50.1-bit hit covers positions 14–38 at 100% identity.

*Estimating the database size.* Reading the actual E-value for the 50.1-bit hit off the search
result ($E = 2\times10^{-4}$) and solving the formula above for $n$, with $m = 68$ and $S = 50.1$,
gives $n \approx 3.55\times10^{9}$. The mouse haploid genome is about $2.7$ billion base pairs, so a
database of genome *plus* transcripts coming out somewhat larger than that is the right order of
magnitude — the formula, crude as it is, recovers a sane answer.

*Why a shorter query is a weaker query.* Suppose a query of length $m$ matches perfectly, with score
$S$ and E-value $E_1$. If only the first half of the query is searched, both the length and the score
roughly halve ($m \to m/2$, $S \to S/2$, since there are half as many positions left to accumulate a
positive score). Writing $E_2$ for the new E-value,

$$E_1 = mn2^{-S}, \qquad E_2 = \tfrac{m}{2}n2^{-S/2} \;\Longrightarrow\; E_2 = E_1\,2^{(S/2 - 1)}.$$

So halving the query length increases the E-value **exponentially** in the lost score, with only a
linear factor of 2 working the other way — and the exponential term dominates completely. This is
the general lesson: significance tracks the *score* of a match, not simply how long the matching
region is.

## Gapped alignment: dynamic programming and substitution matrices

BLAST finds candidate regions of similarity; turning a candidate into an actual alignment — deciding
exactly where the two sequences agree, and where one has to insert a gap to keep pace with the other
— is a separate problem, solved by dynamic programming.

**Why not just count matches?** A naive scoring scheme with a constant $+1$ for a match and $-1$ for
any mismatch treats every substitution as equally bad. Real protein substitutions are not
interchangeable: some barely touch a protein's structure or function and are tolerated by evolution
often, while others disrupt it and are almost never seen. A useful scoring matrix, then, is not
guessed but *learned* — from how often each pair of residues is actually observed replacing one
another across aligned, related sequences. BLOSUM and PAM matrices are built this way, from different
sets of aligned protein families and at different evolutionary distances, which is why two "match"
scores in the same matrix can differ enormously: in PAM250, aligning tryptophan with tryptophan
scores far higher than aligning alanine with alanine, because tryptophan is large and its
substitutions are structurally disruptive and rare, while alanine is small, common among nonpolar
residues, and readily substituted without much consequence.

**The Needleman–Wunsch recurrence.** To align two sequences globally (end to end, gaps allowed
anywhere), build a grid with one sequence along the rows and the other along the columns, plus a
leading row and column for "everything so far is a gap." Each interior cell holds the best score for
aligning the prefixes up to that row and column, computed as the best of three moves into it:
extend a diagonal alignment by pairing the current row and column residues (add the substitution
score for that pair), extend from the left by placing a gap in the row sequence, or extend from
above by placing a gap in the column sequence (each gap move subtracting the gap penalty). The
leading row and column are filled in by accumulating the gap penalty outward from the corner. Once
the grid is full, tracing the choice that produced each cell's value back from the bottom-right
corner to the top-left corner recovers an optimal alignment — and if more than one choice ties at some
cell, there is more than one optimal alignment.

As a small illustration: aligning the peptides `ATWES` and `TCAET`, with a linear gap penalty of 2,
the corner and the first row of the grid accumulate the gap penalty as $0, -2, -4, -6, -8, -10$. One
interior cell — row `T`, column `T` — scores $3$: the diagonal move from the corner ($0$) plus the
substitution score for pairing T with T ($3$ in the BLOSUM62 table used here) beats either gap move
(each of which would only reach $-2-2=-4$). Carrying that recurrence across the whole grid, and then
tracing back the winning path, is exactly what problem set 1 asks you to do by hand for this pair of
peptides, first under BLOSUM62 and then under PAM250 — and it is worth doing once by hand, because
the two matrices disagree about where the gap belongs. The disagreement traces to two mismatches
scored very differently: aligning C with W costs only $-2$ under BLOSUM62 but $-8$ under PAM250, so
BLOSUM62 is willing to tolerate that pairing directly while PAM250 prefers to pay for a gap instead;
PAM250 also rewards pairing A with T more generously than BLOSUM62 does, pulling the alignment
further in that direction.

## How surprised should you be: the statistics of a match

A high score is not automatically evidence of homology — a long enough search will eventually turn
up a good-looking match to an unrelated sequence purely by chance. The question is how good a match
has to be before "purely by chance" becomes implausible, and this is answered by the statistics of
*local* alignment scores.

For ungapped local alignment with a simple match/mismatch scoring scheme, the score of the best
chance alignment between two random sequences of lengths $M$ and $N$ follows (asymptotically) an
extreme-value (Gumbel) distribution, with tail

$$P(S > x) = 1 - \exp\!\left[-KMN e^{-\lambda x}\right],$$

where $K$ is a constant that depends on the scoring scheme (taken as $1$ below), and $\lambda$ is
determined by the scoring scheme *and* the base composition, as the unique positive root of

$$p_{\text{match}}\,e^{\lambda} + p_{\text{mismatch}}\,e^{-\lambda} = 1.$$

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Right-skewed tail of the local alignment score distribution, shaded beyond the observed score">
<line x1="30" y1="160" x2="320" y2="160" stroke="currentColor" stroke-width="1.5"/>
<path d="M210,105 C230,112 250,122 270,135 C285,141 300,144 310,146 L310,160 L210,160 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
<path d="M30,155 C50,140 70,90 90,60 C102,45 112,45 122,50 C142,58 162,75 182,90 C196,100 205,103 210,105 C230,112 250,122 270,135 C285,141 300,144 310,146" fill="none" stroke="currentColor" stroke-width="1.5"/>
<line x1="210" y1="160" x2="210" y2="105" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
<text x="210" y="176" text-anchor="middle" font-size="12" fill="currentColor">S = 20</text>
<text x="266" y="128" text-anchor="middle" font-size="12" fill="currentColor">E-value</text>
<text x="175" y="192" text-anchor="middle" font-size="12" fill="currentColor">score of the best chance alignment</text>
</svg>
<figcaption>The score of the best alignment between two unrelated random sequences has a long right
tail; the E-value is (up to the constant K) the area under that tail beyond the observed score.</figcaption>
</figure>

Note the relationship to the bit-score formula above: writing a score in bits is exactly a choice of
scale that makes $\lambda = \ln 2$ and $K=1$, so that $e^{-\lambda x} = 2^{-x}$ and the two formulas
coincide. The general form above is what you fall back on when the scoring scheme is a raw
match/mismatch count rather than something already rescaled into bits.

One more subtlety before working an example: this is a *continuous* distribution being used to
judge a *discrete* score. Since a single point has no probability mass under a continuous
distribution, $P(S \ge x)$ for an integer-valued score is really $P(S > x-1)$, so it is $x - 1$, not
$x$, that should be substituted into the tail formula above. The difference is usually small, but it
is worth being deliberate about which one you are computing.

**A worked case.** A 100 bp query is searched (locally, match $+1$, mismatch $-1$, $K=1$) against a
1 Mbp genome, and a 20-nt perfect match turns up ($M = 100$, $N = 10^6$, score $x = 20$). Take the
query and genome both to have balanced base composition, $A=C=G=T=25\%$. Every base pairs with the
matching base in the other sequence with probability $\tfrac14$, so $p_{\text{match}} = \tfrac14$ and
$p_{\text{mismatch}} = \tfrac34$. The equation $\tfrac14 e^{\lambda} + \tfrac34 e^{-\lambda} = 1$ has
two roots ($\lambda = 0$, which is always a root and never the one wanted, and $\lambda = \ln 3$);
taking the positive one, $\lambda = \ln 3$. Using the continuity correction ($x - 1 = 19$),

$$P(S \ge 20) = P(S > 19) = 1 - \exp\!\left[-(100)(10^6)e^{-19\ln 3}\right] \approx 0.0824$$

(about $0.0283$ if $x=20$ is used directly instead) — a 20-nt exact match at balanced base
composition is on the edge of what you'd expect to see by chance in a genome this size, not a
striking result either way.

## Exercises

The following are the questions from problem set 1 that this chapter has not already walked through.

**1. Reading a BLAST hit (from problem 1).** The mutant RNA of the worked BLAST example above has
two transcript hits at $E \le 0.05$: one at query positions 14–38, 100% identity, antisense to the
mRNA for a named gene product; the other at positions 38–68, 97% identity, sense to a small
nucleolar RNA of the C/D box class. A pull-down from mouse cell lysate followed by mass spectrometry
shows that the mutant RNA also physically interacts with the product of the *ADAR1* gene. Determine
what ADAR1 does and what kind of RNA substrate it acts on. Then, using the strand and identity of
the two hits above, propose a hypothesis for how this mutant RNA could produce the mouse's metabolic
phenotype. (Hint: the antisense hit overlaps a codon read as UAU in the sense-strand mRNA; consider
what that codon becomes, and what amino acid change that implies, if ADAR1 acts on it.)

**2. Significance under two other base compositions (from problem 3).** Using the same setup as the
worked case above — a 100 bp query against a 1 Mbp genome, match $+1$/mismatch $-1$, $K=1$, and a
20-nt perfect match — find $\lambda$ and the resulting significance $P(S \ge 20)$ for:

  (a) a query and genome that are both strongly A/T-rich, with $A=T=40\%$ and $C=G=10\%$;

  (b) a query that is moderately A/T-rich ($A=T=30\%$, $C=G=20\%$) searched against a genome that is
      moderately C/G-rich ($A=T=20\%$, $C=G=30\%$).

  For each case, work out the probability of a match and of a mismatch first, from the base
  frequencies given, before solving for $\lambda$. Compare the three results (balanced, from the
  worked case, and these two) and comment on what they say about how much a genome's base
  composition affects whether a short exact match is worth taking seriously.

## Sources

- **Course roadmap.** All three sections of "A map of the course" are drawn from the three slide
  decks: `lectures/01-slides/01-genomic-analysis-module.md` (reads-to-genome module, lectures 5–8),
  `02-computational-genetics-module.md` (genome-to-phenotype module, lectures 18–20), and
  `03-gwas-analysis-can-identify-human-variants-associated-with-di.md` (GWAS figure, and the
  structure/network preview for lectures 12–17). These files are themselves a model's reconstruction
  of a slide PDF with no extractable text layer, and are captions and figure descriptions rather than
  a transcript — nothing beyond what each caption states is asserted here. No lecture transcript or
  written notes were supplied for this session; the roadmap section is therefore a pointer to what
  the lecture showed, not a full treatment of any one of lectures 5–20. Administrative slides
  (course cross-listing and project requirements, the MIT OpenCourseWare footer) are omitted as
  boilerplate.
- **BLAST and E-values**, including the mouse PAH/ADAR1 worked case and the query-length argument, are
  from `psets/01-questions-pset1-ans/01-problem-1-sequence-search-6-points.md`, parts (A)–(C); parts
  (D)–(E) of the same file are held back for Exercise 1.
- **Gapped alignment, substitution matrices, and the BLOSUM62/PAM250 comparison** are from
  `psets/01-questions-pset1-ans/02-problem-2-gapped-sequence-alignment-6-points.md`, all parts.
- **The statistics of a match**, including the continuity-correction note and case (A) of the worked
  example, are from `psets/01-questions-pset1-ans/03-problem-3-sequence-similarity-search-statistics-7-points.md`;
  cases (B) and (C) of that file are held back for Exercise 2. The source file's own working for case
  (C) is cut off mid-derivation, and if the problem had a further part it was not supplied.
- **Named external sources the slides pointed to but did not themselves contain**, for anyone who
  wants the originals: Burton et al., "Genome-wide Association Study of 14,000 Cases of Seven Common
  Diseases and 3,000 Shared Controls," *Nature* 447 (2007); Bloom et al., "Finding the Sources of
  Missing Heritability in a Yeast Cross," *Nature* 494 (2013); Lindorff-Larsen et al., "How
  Fast-folding Proteins Fold," *Science* 334 (2011); Markoff, "In a Video Game, Tackling the
  Complexities of Protein Folding," *New York Times* (2010); Barabási, Gulbahce & Loscalzo, "Network
  Medicine," *Nature Reviews Genetics* 12 (2011); Sumazin et al., "An Extensive MicroRNA-mediated
  Network of RNA–RNA Interactions...in Glioblastoma," *Cell* 147 (2011); Dixon et al., "Systematic
  Mapping of Genetic Interaction Networks," *Annual Review of Genetics* 43 (2009); Guziolowski et al.,
  "Exhaustively Characterizing Feasible Logic Models of a Signaling Network using Answer Set
  Programming," *Bioinformatics* 30 (2014). The pset's own answer for exercise 1 further points to
  Gersting et al., *American Journal of Human Genetics* 83 (2008), on the PAH Y414C mutation, and
  Kishore & Stamm, *Science* 311 (2006), on SNORD115/HBII-52 as the real case that inspired the
  mouse scenario.

---

[Contents](index.md) · [2. Local Alignment (BLAST) and Statistics →](02-local-alignment-blast-and-statistics.md)
