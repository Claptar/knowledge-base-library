---
title: "3. Alignment Recap and BLAST Seeding"
course: "MIT 6047"
chapter: 3
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. Alignment Recap and BLAST Seeding

## What this covers

The surviving slide material from this lecture is a small fragment of a longer session on sequence
alignment and database search. It assumes the dynamic-programming alignment recursion from the
previous lecture (a matrix $M$ built from prefixes of two sequences, filled by a recursion, and
read out by tracing back through it) and asks two things: what does that recursion look like as a
concrete numerical example, and what problem does it hand off to when one sequence has to be found
inside a database of millions rather than compared to one other sequence. Only the recap and the
BLAST fragment of the lecture reconstructed with enough detail to write up honestly; the rest is
named in [Sources](#sources) rather than guessed at.

## Where this lecture sits

The course's first module builds the computational tools — dynamic programming, and then hidden
Markov models — before applying them. This week is the first application: alignment and database
search infer nucleotide-level evolutionary events and scan for regions that may share common
ancestry. The following week turns the same tools on genomes directly, to find exons and CpG
islands.

## Recap: alignment as a path through a matrix

The previous lecture's dynamic-programming recursion is presented again as a duality: an alignment
of $S_1$ and $S_2$ is the same object as a path through a matrix. Index the matrix by prefixes —
row $i$ is the prefix $S_1[1..i]$, column $j$ is the prefix $S_2[1..j]$ — and let $M[i,j]$ store the
best score of any alignment of those two prefixes. A path from the top-left corner (the two empty
prefixes) to the bottom-right corner (the two full sequences) corresponds to a complete alignment,
and the score of that alignment is the sum of the per-step scores along the path.

<figure>
<svg viewBox="0 0 360 240" role="img" aria-label="A dynamic-programming alignment matrix with one path from the top-left to the bottom-right corner">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="60" y1="40" x2="280" y2="40" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="85" x2="280" y2="85" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="130" x2="280" y2="130" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="175" x2="280" y2="175" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="40" x2="60" y2="175" stroke="currentColor" stroke-width="1"/>
  <line x1="115" y1="40" x2="115" y2="175" stroke="currentColor" stroke-width="1"/>
  <line x1="170" y1="40" x2="170" y2="175" stroke="currentColor" stroke-width="1"/>
  <line x1="225" y1="40" x2="225" y2="175" stroke="currentColor" stroke-width="1"/>
  <line x1="280" y1="40" x2="280" y2="175" stroke="currentColor" stroke-width="1"/>
  <text x="170" y="18" text-anchor="middle" font-size="13" fill="currentColor">S1[1..i]</text>
  <text x="87" y="30" text-anchor="middle" font-size="12" fill="currentColor">T</text>
  <text x="142" y="30" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <text x="197" y="30" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <text x="252" y="30" text-anchor="middle" font-size="12" fill="currentColor">C</text>
  <text x="20" y="112" text-anchor="middle" font-size="13" fill="currentColor" transform="rotate(-90 20 112)">S2[1..j]</text>
  <text x="45" y="66" text-anchor="end" font-size="12" fill="currentColor">T</text>
  <text x="45" y="111" text-anchor="end" font-size="12" fill="currentColor">A</text>
  <text x="45" y="156" text-anchor="end" font-size="12" fill="currentColor">G</text>
  <polyline points="60,40 115,85 170,130 225,130 280,175" fill="none" stroke="currentColor" stroke-width="2.5" marker-end="url(#arrow)"/>
  <circle cx="60" cy="40" r="3" fill="currentColor"/>
  <text x="66" y="52" font-size="11" fill="currentColor">M[0,0]=0</text>
  <text x="284" y="182" font-size="11" fill="currentColor">M[i,j]</text>
</svg>
<figcaption>Aligning S1 against S2 is a path from the top-left corner of the prefix matrix to the
bottom-right. A diagonal step matches or substitutes one character of each sequence; a horizontal
or vertical step gaps one sequence against a character of the other. $M[i,j]$ is the best score of
any path reaching that corner.</figcaption>
</figure>

The recursion that fills in $M[i,j]$ from its neighbours did not survive the conversion of this
slide — an empty block sits where it belonged — so it is not restated here; see
[Sources](#sources).

## A worked instance

The slide carries one concrete numerical example, worked out in full as a spreadsheet. Two
16-nucleotide sequences are aligned,

$$S_1 = \text{TAACCTTTATCTGCCA}, \qquad S_2 = \text{TAACGGCCCATCTCGA},$$

under a scoring scheme that is not simply "match +1, mismatch $-1$": it rewards a match with $+1$
and penalises a gap with $-1$, as expected, but it treats the two kinds of mismatch differently —
a transition (A$\leftrightarrow$G or C$\leftrightarrow$T, swapping one purine or pyrimidine for the
other) scores $0$, while a transversion (any other substitution) scores $-1$. The $17\times17$
table is initialized with $0,-1,-2,\dots,-16$ along its top row and left column — the cost of
aligning a growing prefix of one sequence against nothing — which is the boundary condition for a
*global* alignment, over the full length of both sequences, rather than the *local* alignment
(best-scoring substring against substring) that the agenda for this lecture also names. The
spreadsheet spells out explicitly what $S_1[1..i]$ and $S_2[1..j]$ mean by listing the growing
prefixes of each sequence next to the corresponding row and column.

Tracing arrows back from the bottom-right corner of the filled table recovers an alignment. The
slide shows this done twice, for the same pair of sequences, landing on two slightly different
alignments:

```
TAAC-CTTTATCTGCCA          TAAC-CTTTATCTGCCA
TAACGGCCCATCT-CGA          TAACGGCCCATC-TCGA
```

Both place the single gap in $S_1$ after position 4, but they place the single gap in $S_2$ one
position apart. That two tracebacks from what looks like the same filled table disagree on where
the gap in $S_2$ falls is the concrete instance of a general fact about the recursion: ties in the
scoring can make more than one path through the matrix optimal, so the alignment recovered is not
always unique.

## From alignment to database search

Comparing two given sequences is one problem; finding whether a new sequence resembles anything
already known is another, and it does not scale the same way — a database search has to compare a
query against every sequence in a collection, not just one. The slide material marks the scale of
this with two Google Scholar citation-count charts for the two founding BLAST papers (Altschul,
Gish, Miller and Myers, "Basic local alignment search tool", 1990; and Altschul, Madden, Schäffer et
al., "Gapped BLAST and PSI-BLAST", 1997) — bar charts of citations per year running from the
mid-1990s to 2015, each with 2013 singled out (3902 and 3712 citing papers that year, on the two
charts respectively) — next to a search-results screenshot showing the two papers had accumulated
55,606 and 55,519 citations in total by then. The point made by putting these figures on a slide is
simply that BLAST's answer to the database-search problem became one of the most-used pieces of
software in biology.

## BLAST's seed-and-extend idea

The one piece of BLAST's own mechanism that survives in the reconstructed material is illustrated
rather than stated: a short exact match is used to *seed* an alignment, which is then extended.

The figure marks a **query word** of length $W = 3$ — here the three letters "PQG" — inside a
protein query sequence. A search for occurrences of that same three-letter word elsewhere (in a
database sequence) finds one, and the alignment is extended outward from that seed in both
directions for as long as extending it keeps improving the score, allowing a few mismatches and
conservative substitutions along the way. The result is what the slide labels a **high-scoring
segment pair (HSP)**: in the example shown, query residues 325–365 aligned against subject residues
290–330, with the original three-letter seed sitting in the middle of a longer stretch of matches
and near-matches on either side. This is the idea that lets BLAST avoid running a full
dynamic-programming alignment against every sequence in a database: only regions that already share
a short exact word are extended at all.

## What the agenda names but this material does not cover

The title slide lists four topics for this lecture — global vs. local alignment, exact string
matching and the Karp–Rabin algorithm, database search and BLAST, and deterministic linear-time
string matching — but only the alignment recap and the BLAST fragment above survived with enough
content to write up. Karp–Rabin exact matching and deterministic linear-time string matching are
named on the title slide only; nothing in the recovered material explains either one, and the local
side of "global vs. local alignment" is likewise only implied by contrast with the worked example's
global boundary condition, never itself shown. Anything a reader wants on those three topics has to
come from the original slide deck or another source.

## Sources

- **Slides**: `computational-biology/mit-ocw/6047/lectures/03-slides.md` (course 6.047/6.878/HST.507,
  Fall 2015, MIT OCW), converted from `lectures/03-slides.pdf`. The conversion note on the file
  itself flags that the source PDF had no text layer, that a model reconstructed the markdown from
  the rendered pages, and that every equation in it is unverified — treated accordingly here: the
  matrix recursion is not restated because it did not survive conversion at all.
  - Agenda and module-overview text: the title slide and the "Module 1" slide.
  - Alignment-as-path duality and the $M[i,j]$ definition: the "Duality" slide.
  - The worked numerical example (sequences, scoring scheme, boundary condition, two tracebacks):
    figures extracted from pages 9 and 10 of the original PDF
    (`03-slides/figures/p009-1.png`, `03-slides/figures/p010-1.png`).
  - The BLAST citation charts and citation-count screenshot: figures from page 29
    (`03-slides/figures/p029-1.png`, `p029-2.png`, `p029-3.jpeg`).
  - The query-word and high-scoring-segment-pair figures: figures from page 30
    (`03-slides/figures/p030-2.jpeg`, `p030-3.jpeg`). A third figure on that page
    (`p030-1.jpeg`) is too low-resolution in the conversion to read reliably and is not used here.
- No transcript, written notes or exercises were supplied for this lecture.
- Not covered by the supplied material, though named on the title slide: the Karp–Rabin exact
  string-matching algorithm, deterministic linear-time string matching, and an explicit statement
  of the local-alignment (Smith–Waterman-style) recursion.

---

[← 2. Sequence Alignment and Dynamic Programming](02-sequence-alignment-and-dynamic-programming.md) · [Contents](index.md) · [4. Recap: Markov Chains and HMMs →](04-recap-markov-chains-and-hmms.md)
