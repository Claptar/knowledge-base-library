---
title: "2. Sequence Alignment and Dynamic Programming"
course: "MIT 6047"
chapter: 2
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Sequence Alignment and Dynamic Programming

## What this covers

This chapter follows the first alignment lecture of 6.047: how the biological question "how have
two genomes diverged from a common ancestor?" gets turned into a well-posed computational problem,
and how dynamic programming solves that problem in polynomial time even though the number of
candidate answers is exponential. It assumes only that you know what a genome sequence is — nothing
about algorithms or evolutionary models is presumed. No transcript survives for this session, so
the chapter stays close to what the slides state and computes directly from the numbers they give,
rather than narrating around them.

## Why align genomes at all

Two genomes that share a recent common ancestor are, in effect, the same sequence viewed after
different amounts of random change. Where a stretch of sequence has stayed similar across species
that otherwise diverged long ago, that similarity is itself evidence: it is much likelier because
mutations there were selected against than because they never happened. This is the basic move of
comparative genomics — reading conservation as a signature of function. Exons, for instance, stay
recognisably similar all the way out to mouse, chicken and fish; many non-coding elements are
conserved just as strongly, and turn out to be regulatory. The lecture cites this "evolutionary
signature" as taking a different shape depending on what kind of element is under it: protein-coding
genes show codon-substitution patterns and conserved reading frames, RNA structures show
compensatory changes and tolerated silent G-U substitutions, microRNAs show a distinctive shape of
conservation around their structural loops and pairings, and regulatory motifs show mutations that
preserve the consensus and an increased branch-length score (Stark et al., *Nature* 2007). The same
idea, that evolution can be "read" to reveal functional elements, is what the lecture credits across
yeast (Kellis et al., *Nature* 2003), mammals (Xie et al., *Nature* 2005) and fly (Stark et al.,
*Nature* 2007).

Turning that idea into a method means being able to *measure* conservation: count edit operations,
substitutions and gaps between sequences; estimate the number of underlying mutations, including
ones that reversed each other (back-mutations); use the neighbourhood around a position — a
conservation "window" — rather than judging a single base in isolation; and eventually estimate the
probability that a position sits in a constrained "hidden state", using phylogeny to get a tree-wide
mutation rate and allowing different branches of the tree to mutate at different rates. All of that
machinery (hidden states, phylogenetic rates) is flagged in the slides as coming in later lectures.
What this lecture builds is the first and most basic tool underneath all of it: an algorithm that,
given two sequences, finds the best way to line them up.

## From evolutionary history to an edit-distance problem

A genome changes over time through a small vocabulary of operations. The slides walk one example
through all of them:

$$
\text{ACGTCATCA} \xrightarrow{\text{mutation}} \text{ACGTGATCA}
\xrightarrow{\text{deletion}} \text{AGTGTCA}
\xrightarrow{\text{insertion}} \text{TAGTGTCA}
$$

A single base is substituted (position 5, C to G), two bases are deleted, and a base is inserted at
the front. What alignment has to do is the *inverse* of this: given only the two ends of that chain —
the starting sequence and the ending sequence — infer a plausible history of edits connecting them,
without ever observing the intermediate steps.

That inverse problem is not, in general, solvable exactly: many different edit histories can produce
the same pair of end sequences, and there is no way to know which one actually happened. Formalising
it into something computable takes three decisions, and the lecture is explicit that all three are a
trade-off between what biology wants and what computer science can deliver:

1. **Define the set of evolutionary operations** — insertion, deletion, substitution. The natural
   choice is to make them symmetric (time-reversible): a change from A to G is exactly as likely, and
   costs exactly as much, as a change from G to A. That symmetry is a modelling choice, not a law —
   the slides flag one standing exception: methylated CpG dinucleotides mutate asymmetrically toward
   TpG or CpA, rather than reversibly, so a model that insists on symmetry everywhere would get that
   case wrong.
2. **Define an optimality criterion.** Since the true history cannot be recovered, the only honest
   move is Occam's razor: look for the edit history of minimum number, or minimum total cost, that
   explains the two observed sequences.
3. **Design an algorithm that achieves that optimum**, or a good approximation of it. How tractable
   the resulting algorithm is depends entirely on the assumptions baked into steps 1 and 2.

The slides summarise this as a standing tension — biology cares about relevance, predictability,
correctness and the special cases a clean model tends to paper over; computer science cares about
what assumptions are safe to make, which algorithms follow from them, and whether the result is
tractable, computable, and actually implementable. Not every decision pits these against each other,
though — the slides note in passing that Pevzner's and Sankoff's differing treatments of
directionality in chromosomal-inversion problems is a case where the biologically relevant choice and
the tractable one turned out to coincide, without spelling out the dispute itself.

Why is this hard in the first place? Because the number of ways to interleave insertions, deletions
and substitutions along two sequences of realistic length grows exponentially with that length. A
brute-force search over "every possible edit history" — equivalently, "every possible alignment" of
the two sequences — is infeasible even for short sequences. Making that search tractable is exactly
what dynamic programming is for.

## The dynamic-programming idea

The lecture introduces dynamic programming in general before applying it to alignment, using the
standard contrast between computing Fibonacci numbers top-down (recursively, recomputing the same
smaller Fibonacci numbers over and over as different branches of the recursion ask for them) and
bottom-up (filling a table of answers to smaller sub-problems once, in an order where each entry can
be read off from ones already filled, and never repeating work). The generalisable content of that
example is a five-step recipe the slides give explicitly, and which the rest of this chapter
instantiates for alignment:

1. **Parameterization** — choose which quantities index a sub-problem.
2. **Sub-problem space** — the full set of sub-problems that answer will ever be needed for.
3. **Traversal order** — an order to compute them in, so that whenever a sub-problem is filled in,
   everything it depends on has already been computed.
4. **Recursion formula** — how a sub-problem's answer is built from the answers to smaller ones.
5. **Trace-back** — how to recover the actual solution, not just its score, by retracing the choices
   that were recorded while filling the table.

## The alignment matrix

The key fact that makes alignment amenable to this recipe is that its score is **additive**: the
score of a whole alignment is a sum, position by position, of match, mismatch and gap contributions.
An additive score is exactly what lets a solution be built up from smaller pieces — the score of
aligning two long prefixes can be expressed in terms of the score of aligning slightly shorter
prefixes, plus one more term.

**1. Parameterization.** Index a sub-problem by a pair of prefix lengths $(i, j)$: how much of
sequence $S_1$ and how much of sequence $S_2$ has been consumed so far.

**2. Sub-problem space.** For sequences of length $M$ and $N$, there is one sub-problem — one entry
$M(i,j)$ — for every $0 \le i \le M$, $0 \le j \le N$: an $(M+1)\times(N+1)$ **prefix matrix**. This
is the resolution of the "why it's hard" problem above: there are exponentially many complete
*alignments* (paths through this matrix from corner to corner), but only polynomially many distinct
*sub-problems*, because every one of those exponentially many paths re-uses the same small set of
prefix comparisons over and over. Collapsing the search from paths to sub-problems is what turns an
exponential search into a polynomial one.

**3. Traversal order.** Fill the matrix with $i$ and $j$ increasing — row by row, say — so that by
the time $M(i,j)$ is computed, its three dependencies $M(i-1,j)$, $M(i,j-1)$ and $M(i-1,j-1)$ are
already known.

**4. Recursion formula.** With a gap penalty, a mismatch penalty and a match bonus fixed in advance,
the entry at $(i,j)$ is

$$
M(i,j) = \max
\begin{cases}
M(i-1,j) - 2 & \text{a base of } S_1 \text{ against a gap} \\
M(i,j-1) - 2 & \text{a base of } S_2 \text{ against a gap} \\
M(i-1,j-1) - 1 & \text{mismatch} \\
M(i-1,j-1) + 1 & \text{match}
\end{cases}
$$

with the border initialised by $M(i,0) = -2i$ and $M(0,j) = -2j$ — aligning a prefix against an empty
prefix can only be done with gaps — and $M(0,0) = 0$.

**5. Trace-back.** Starting at the bottom-right corner (the whole two sequences), repeatedly ask
which of the three cases achieved the maximum, step to that neighbour, and record whether the step
was a match/mismatch (diagonal) or a gap against one of the two sequences (a purely-horizontal or
purely-vertical step). Retracing all the way back to $(0,0)$ reads off one alignment achieving the
optimal score.

This is the **duality** the slides name explicitly: each entry of the matrix corresponds to the best
score of aligning two particular prefixes, and each path from the origin to that entry corresponds to
one particular way of aligning those two prefixes. Reading the bottom-right corner gives the best
score for the whole pair of sequences; re-walking whichever path attained it gives back an alignment
that achieves it.

### A worked example

The slides give a small concrete case: $S_1 = \text{AAGC}$ (the rows) against $S_2 = \text{AGT}$ (the
columns), with match $= +1$, mismatch $= -1$, gap $= -2$:

| | – | A | G | T |
|---|---|---|---|---|
| **–** | 0 | −2 | −4 | −6 |
| **A** | −2 | 1 | −1 | −3 |
| **A** | −4 | −1 | 0 | −2 |
| **G** | −6 | −3 | 0 | −1 |
| **C** | −8 | −5 | −2 | −1 |

Every interior entry follows directly from the recursion formula. For instance, $M(2,2)$ — aligning
the prefixes $S_1[1..2]=\text{AA}$ and $S_2[1..2]=\text{AG}$ — takes the best of $M(1,2)-2=-3$,
$M(2,1)-2=-3$ and $M(1,1) + \text{mismatch}(A,G) = 1-1=0$, giving $M(2,2)=0$; every other entry in the
table checks out the same way, down to the final score of $-1$ at the bottom-right corner.

Tracing back from $-1$ at $(4,3)$: only the diagonal candidate,
$M(3,2)+\text{mismatch}(C,T) = 0-1=-1$, matches, so the last column of the alignment pairs $S_1$'s
final C against $S_2$'s final T (a mismatch). The same check at $(3,2)=0$ leaves only the diagonal,
pairing G against G (a match). But at $(2,1)=-1$ there is a genuine tie: both $M(1,1)-2=-1$ (a gap
step) and $M(1,0)+\text{match}(A,A)=-1$ (a diagonal step) achieve the maximum. Following either branch
back to the origin turns out to complete into a fully optimal alignment — the two ties really are two
distinct, equally good alignments of score $-1$:

```
S1: A A G C        S1: A A G C
S2: A - G T        S2: - A G T
```

This is exactly the distinction the slides' own figure draws between path segments that merely look
locally attractive at one cell and the ones that actually connect corner-to-corner into a full,
globally optimal alignment: in this example, both branches at the tie happen to do so, so the matrix
genuinely encodes two co-optimal alignments rather than one arbitrary choice.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="The alignment matrix as a grid, with one optimal traceback path from the origin to the final score highlighted">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <!-- grid -->
  <g stroke="currentColor" stroke-width="0.75" fill-opacity="0.15">
    <line x1="60" y1="40" x2="270" y2="40"/>
    <line x1="60" y1="80" x2="270" y2="80"/>
    <line x1="60" y1="120" x2="270" y2="120"/>
    <line x1="60" y1="160" x2="270" y2="160"/>
    <line x1="60" y1="200" x2="270" y2="200"/>
    <line x1="60" y1="40" x2="60" y2="200"/>
    <line x1="130" y1="40" x2="130" y2="200"/>
    <line x1="200" y1="40" x2="200" y2="200"/>
    <line x1="270" y1="40" x2="270" y2="200"/>
  </g>
  <!-- column labels: S2 = - A G T -->
  <text x="60" y="28" text-anchor="middle" font-size="12" fill="currentColor">–</text>
  <text x="130" y="28" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <text x="200" y="28" text-anchor="middle" font-size="12" fill="currentColor">G</text>
  <text x="270" y="28" text-anchor="middle" font-size="12" fill="currentColor">T</text>
  <!-- row labels: S1 = - A A G C -->
  <text x="45" y="44" text-anchor="middle" font-size="12" fill="currentColor">–</text>
  <text x="45" y="84" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <text x="45" y="124" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <text x="45" y="164" text-anchor="middle" font-size="12" fill="currentColor">G</text>
  <text x="45" y="204" text-anchor="middle" font-size="12" fill="currentColor">C</text>
  <!-- one of the two optimal traceback paths, highlighted -->
  <polyline points="60,40 130,80 130,120 200,160 270,200" fill="none" stroke="currentColor" stroke-width="2.5" marker-end="url(#arrow)"/>
  <circle cx="60" cy="40" r="3" fill="currentColor"/>
  <circle cx="270" cy="200" r="3" fill="currentColor"/>
  <text x="90" y="55" font-size="11" fill="currentColor">match</text>
  <text x="140" y="103" font-size="11" fill="currentColor">gap</text>
  <text x="205" y="135" font-size="11" fill="currentColor">match</text>
  <text x="235" y="185" font-size="11" fill="currentColor">mismatch</text>
</svg>
<figcaption>One of the two co-optimal traceback paths through the AAGC / AGT matrix: a diagonal
step is a match or mismatch, a step that stays in the same column is a gap. The tie at the second
node means an equally good second path also exists.</figcaption>
</figure>

## From formula to spreadsheet

The lecture makes the same five-step recipe concrete by implementing it as literal spreadsheet
formulas over a longer, messier pair of sequences than the toy example above. Reading the cells by
what the slides say they are *for* (the exact cell arithmetic carries the source's own warning that
it is unverified, so it is summarised here rather than reproduced formula-by-formula):

- One formula looks up the local score $s(S_1[i], S_2[j])$ of matching the two characters at a given
  cell, from a small substitution table, using `INDEX`/`MATCH` as a two-dimensional lookup.
- A second formula is the recursion itself: the max of the diagonal, vertical and horizontal cases,
  exactly as above.
- A third formula records *which* of the three cases achieved that maximum, tagging each cell with a
  symbol for "from directly above", "from the left" and "from the diagonal" — and, deliberately, all
  three at once when there is a tie, rather than breaking it arbitrarily.
- A fourth formula asks whether a cell is actually part of *some* optimal corner-to-corner path, by
  propagating that fact backward from the known-optimal terminal cell, and simultaneously tallies how
  many distinct optimal paths run through it — the spreadsheet's way of surfacing exactly the kind of
  tie worked through above.
- The last pair of formulas walk those direction tags back into two actual strings, emitting a real
  base wherever a step consumed one and a gap character wherever it did not — the trace-back step of
  the recipe, spelled out one cell at a time.

Run over the pair of sequences $S_1 = \text{TAAC-CTTTATCTGCCA}$ and
$S_2 = \text{TAACGGCCCATCT-CGA}$, the result is a 17-column global alignment of two 16-base
sequences with one gap placed in each — the same recipe as the small worked example, just at a scale
closer to a real alignment.

## Variants for scale

Three extensions to the basic recurrence, covered as time allowed:

**Bounded (banded) dynamic programming.** If the two sequences are expected to be close in length and
highly similar, the true optimal path is unlikely to stray far from the main diagonal of the matrix.
Restricting the computation to a band $|i - j| \le k$ around the diagonal — computing $F(i,j)$ only
for $j$ ranging over $\max(1, i-k)$ to $\min(N, i+k)$ — turns the $O(MN)$ computation into $O(Nk)$.
This is a heuristic, not an exact method: it is only correct if the true optimal path really does
stay inside the chosen band. (Slide credit: Serafim Batzoglou.)

**A hard limit on doing better in general.** Can ordinary alignment be sped up below $O(MN)$ time in
the worst case? The slides report a negative result: a chain of reductions from Orthogonal Vectors,
through an intermediate problem called PATTERN, to Edit Distance shows that Edit Distance is
SETH-hard — a strongly subquadratic exact algorithm for it (running in $O(n^{2-\varepsilon})$ time)
would refute the Strong Exponential Time Hypothesis (Backurs and Indyk, *Edit Distance Cannot Be
Computed in Strongly Subquadratic Time (unless SETH is false)*, STOC 2015). The lecture's own aside:
this makes "a faster edit-distance algorithm" a poor choice of term project.

**Linear-space alignment.** Computing just the final *score* $F(M,N)$ needs only $O(N)$ space, since
filling column $i$ of the recursion only ever reads column $i-1$: two live columns suffice, and
earlier ones can be freed as soon as they are no longer needed. The catch is that this throws away
the back-pointers, so the actual alignment — not just its score — seems to need the full $O(MN)$
table after all. The way around this: run the ordinary forward recursion, in linear space, up to the
middle row $M/2$, recording $F(M/2, k)$ for every column $k$; separately run the same recursion
*backward*, from the opposite corner, to get $F^r(M/2, N-k)$, the best score of aligning the two
*suffixes* down to that same middle row. Because the true optimal path has to cross row $M/2$ through
some column, the column $k^*$ that maximises $F(M/2,k) + F^r(M/2,N-k)$ is exactly where it crosses —
found without ever storing the whole matrix. Recursing the same two-pass procedure on the two smaller
rectangles this splits the problem into (rows $0$ to $M/2$ against columns $0$ to $k^*$, and rows
$M/2$ to $M$ against columns $k^*$ to $N$) locates further way-points, and so on until each piece is
small enough to finish directly.

The time cost of this recursion is a geometric series: the first level scans the full $M \times N$
area, the next level's two subproblems together scan half that area, and so on —
$cMN + cMN/2 + cMN/4 + \cdots = 2cMN = O(MN)$ — so recovering the actual alignment costs no more,
asymptotically, than just computing its score. The space cost drops to $O(N)$ for the running
computation, plus $O(M+N)$ to store the final alignment once it is found.

<figure>
<svg viewBox="0 0 320 210" role="img" aria-label="Divide-and-conquer recursion for linear-space alignment: the optimal path crosses the middle row at a waypoint that splits the matrix into two smaller subproblems">
  <g stroke="currentColor" stroke-width="1.25" fill="none">
    <rect x="30" y="20" width="260" height="160"/>
  </g>
  <g fill="currentColor" fill-opacity="0.15" stroke="none">
    <rect x="30" y="20" width="140" height="80"/>
    <rect x="170" y="100" width="120" height="80"/>
  </g>
  <line x1="30" y1="100" x2="290" y2="100" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3"/>
  <line x1="170" y1="20" x2="170" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3"/>
  <line x1="100" y1="20" x2="100" y2="100" stroke="currentColor" stroke-width="0.75" stroke-dasharray="1 3" opacity="0.6"/>
  <line x1="230" y1="100" x2="230" y2="180" stroke="currentColor" stroke-width="0.75" stroke-dasharray="1 3" opacity="0.6"/>
  <polyline points="30,20 170,100 290,180" fill="none" stroke="currentColor" stroke-width="2.5"/>
  <circle cx="30" cy="20" r="3" fill="currentColor"/>
  <circle cx="170" cy="100" r="3.5" fill="currentColor"/>
  <circle cx="290" cy="180" r="3" fill="currentColor"/>
  <text x="10" y="102" font-size="11" fill="currentColor" text-anchor="middle" transform="rotate(-90 10 102)">M/2</text>
  <text x="170" y="196" font-size="11" fill="currentColor" text-anchor="middle">k*</text>
  <text x="230" y="196" font-size="11" fill="currentColor" text-anchor="middle">N−k*</text>
</svg>
<figcaption>The optimal path must cross the middle row M/2 through some column k*, found from two
linear-space passes; recursing on the shaded quadrants locates the next way-points without ever
storing the full matrix.</figcaption>
</figure>

## Exercises

These are drawn from Problem Set 2, which was due after the hidden-Markov-model lectures that this
chapter's slides only forward-reference. Most of them lean on Bayesian classification, clustering
and hidden Markov models rather than on the alignment algorithm above; question 2 is the closest fit,
extending this lecture's "estimating constraint" theme into a simple per-column classifier. A
purely administrative fourth question, on final-project preparation, is omitted here (see Sources).

**1. Naive Bayes classification.**
(a) Suppose sequence fragments are to be classified, by a random variable $Y$, into genes,
regulatory motifs, or repetitive elements, using three features: length $X_1$, GC content $X_2$, and
complexity $X_3$ (roughly, the fraction of possible $k$-mers observed). Does the naive Bayes
assumption hold for this choice of features? Justify your answer.

(b) Regardless of whether the assumption holds, a naive Bayes classifier can still be built. Using
the discretized training set below, write down the maximum-likelihood estimates of each conditional
distribution $P(X_i \mid Y)$ and of the prior $P(Y)$.

| GC Content | Length | Complexity | Class |
|---|---|---|---|
| Low | Long | High | Gene |
| Low | Long | Low | Gene |
| High | Long | High | Repeat |
| Medium | Short | High | Motif |
| Medium | Short | Low | Motif |
| High | Long | Low | Repeat |
| High | Short | High | Motif |
| Medium | Long | High | Gene |
| High | Long | Low | Repeat |
| High | Short | High | Motif |

(c) Using that model, find the maximum a posteriori class for a new fragment with GC content
Medium, Length Long, Complexity Low.

**2. Classifying conserved regions from alignment columns.**
(a) Define the alignment score of one column of a multiple alignment as the number of unique pairs
of sequences sharing the same symbol at that column. For example:

```
GACTA
TACTA
AGTTA
CTTAA
01236
```

Given two models, $C$ for conserved regions and $N$ for unconserved regions, and treating the score
at each column as independent, the conditional probability of a given column score under each model
is:

| Score | N | C |
|---|---|---|
| 0 | 0.1 | 0.05 |
| 1 | 0.35 | 0.15 |
| 2 | 0.25 | 0.2 |
| 3 | 0.2 | 0.3 |
| 6 | 0.1 | 0.3 |

Compute $P(\cdot \mid N)$ and $P(\cdot \mid C)$ for each of the two ten-column alignments:

```
ACGACGACTA          ACAACGAGTA
CAGACGCTGA          AAAACGAATA
TTCCTCTGAT          TCATCGAGTT
AGATGTGACT          ACATCTAACT
```

(b) Simulate 10,000 length-10 score sequences drawn from $N$. In what fraction of them is
$P(S \mid C) > P(S \mid N)$?

(c) Simulate 10,000 length-10 score sequences drawn from $C$. In what fraction of them is
$P(S \mid N) > P(S \mid C)$?

(d) How could the classification error rate on short fragments like these be reduced? Does the same
strategy help for much longer sequences?

**3. K-means clustering.**
(a) Implement $k$-means clustering (the point-assignment and centroid-recalculation steps) on
gene-expression profiles of two genes across a set of patients.

(b) Run the algorithm on the first tissue's data. A correct implementation converges in four
iterations.

(c) Run it on the second tissue's data (it should converge in six iterations this time) — but
something goes wrong. What is it, and what strategy would let the algorithm find the most obvious
clusters without seeing them ahead of time? Make the corresponding change and describe how it fixes
the problem.

(d) Describe how you would implement *fuzzy* $k$-means using the same structure of functions.
(Bonus: how would you visualize its steps — the degree of membership of each point in each cluster,
alongside the centroids?)

**5. Hidden Markov model classification of CpG islands** *(for 6.878 only).*
Consider an eight-state HMM with states $A^+, C^+, G^+, T^+$ emitting nucleotides inside CpG islands
and $A^-, C^-, G^-, T^-$ emitting nucleotides outside them.

(a) Estimate the model's parameters by maximum likelihood (relative frequencies) from a chromosome's
sequence together with an existing CpG-island annotation used as ground truth. Describe and justify
how zero counts in the estimated parameters are handled, and how the initial state distribution is
estimated.

(b) Use the Viterbi algorithm to annotate CpG islands in a one-megabase region of another
chromosome.

(c) Evaluate the model against the ground-truth annotation by computing its false-positive and
false-negative rates (counting a predicted island as a true positive if at least 50% of it overlaps
a true island). Are the two error rates equal? If not, what causes the asymmetry?

(d) Could tuning the model's parameters improve its performance? If so, how — and if not, what
modification to the model itself would you propose instead, and why?

(e) Describe and justify a biological criterion, beyond the sequence itself, that could be used to
filter the output of a sequence-based CpG-island classifier.

## Sources

- Slides, `lectures/02-slides/01-module-1-aligning-and-modeling-genomes.md` — the course-motivation
  section (conserved regions, evolutionary signatures, Stark et al. 2007, Kellis et al. 2003, Xie et
  al. 2005), the lecture's own outline, the "genomes change over time" mutation example, "formalizing
  the problem" (operations, optimality criterion, Bio/CS trade-off, the Pevzner/Sankoff aside), and
  the worked AAGC/AGT matrix with its trace-back notation. This file is machine-reconstructed from a
  PDF with no text layer (`fidelity: reconstructed`); the material between the lecture's outline and
  the worked matrix — the explicit Fibonacci example and the DP-recipe and prefix-matrix slides the
  outline promises — was not captured in the extraction, so this chapter's account of that material
  is built only from the outline's own bullet points, not from slide content that no longer exists in
  the source.
- Slides, `lectures/02-slides/02-genome-alignment-in-an-excel-spreadsheet.md` — the spreadsheet
  formulas and their stated purposes, the bounded-DP heuristic (credited to Serafim Batzoglou), the
  SETH-hardness result (Backurs and Indyk, STOC 2015 — the paper's abstract is itself redacted in the
  source for copyright reasons and is not reproduced here), and the linear-space alignment
  derivation. The closing slide "Additional insights: why the 2-dimensional parameterization worked"
  has a title but no captured body text in this source and so is not covered in this chapter.
- No lecture transcript or written notes were supplied for this session.
- Exercises: `psets/02-questions/01-1-naive-bayes-classification.md`,
  `02-2-classification-of-conserved-regions.md`, `03-3-k-means-clustering.md`, and
  `05-5-hidden-markov-model-classification-of-cpg-islands-6-878-on.md` (Problem Set 2). Question 4,
  "Final project preparation," is course logistics with no technical content and has been left out of
  the Exercises section above.

---

[← 1. Computational Biology: Course Overview](01-computational-biology-course-overview.md) · [Contents](index.md) · [3. Alignment Recap and BLAST Seeding →](03-alignment-recap-and-blast-seeding.md)
