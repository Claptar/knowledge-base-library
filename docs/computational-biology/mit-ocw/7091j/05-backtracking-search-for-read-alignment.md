---
title: "5. Backtracking Search for Read Alignment"
course: "MIT 7.091J"
chapter: 5
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Backtracking Search for Read Alignment

## What this covers

An exact-match index — the kind built from a suffix array or a Burrows-Wheeler transform — can find a
query string in a genome very fast, but a sequencing read almost never matches the genome exactly:
sequencing errors and real polymorphisms both introduce mismatches. This chapter covers how a
short-read aligner (the running example is Bowtie) turns an exact-match search into an approximate
one by **backtracking**: retrying the search with a different base whenever the greedy path fails,
guided by how confident the sequencer was in each base call. It assumes the reader already has exact
string matching against a genome index (a backward search that extends a match one character at a
time) and knows what a base-call quality score is.

## Why exact search is not enough

A search that walks straight through a query against an index either matches all the way to the end
or dies at the first mismatch. Real reads have mismatches, so a plain exact search fails on almost
every read. The fix that gives this chapter its name is to let the search **backtrack**: when it hits
a dead end, it undoes its most recent step, tries a different next character, and continues. This
already raises two problems that the rest of the chapter is about.

First, backtracking is not guaranteed to be cheap. The lecture's opening example is a search that has
to try several wrong extensions before it eventually lands on a valid alignment of a query against
the text `acaacg`:

```
acaacg
 |   |
 ag  c
```

The point is only the shape of the story — a real search can wander a long way before it succeeds, so
an aligner needs a way to bound how much wandering it will tolerate.

Second, there can be more than one place a query approximately fits. Take $Q = $ "aaa" against
$T = $ "acaacg". Because "aaa" is not a literal substring of "acaacg", every placement of the query
against the text is an approximate one, and several different offsets give an equally plausible
one-mismatch alignment:

```
acaacg
 | |
 aaa
```
```
acaacg
 |   |
 aaa
```
```
acaacg
  | |
  aaa
```

A search that stops as soon as it completes the first path it tries has no reason to have found the
best (or only) alignment — the relevant alignments can lie along several different paths through the
search, and a backtracking algorithm has to be willing to explore more than one of them.

## Letting quality scores drive the backtrack

Not every mismatch is equally likely to be a sequencing error. Each base call in a read comes with a
**Phred quality score**,

$$Q = -10 \log(p),$$

where $p$ is the probability that the base call is wrong. A higher $Q$ means higher confidence; a low
$Q$ means the sequencer itself was unsure of that base. This gives a principled way to decide, when
the search hits a dead end, *which* earlier step to reopen: reopen the one the sequencer trusted
least, since that is the base most likely to actually be the error rather than a true mismatch against
the reference.

Bowtie's rule is exactly this: **backtrack to the leftmost position it has already visited that has
the minimal quality score**, and try the other bases there before giving up further back. The worked
example makes the mechanism concrete. Starting from a 16-base read with per-base quality scores

| G | C | C | A | T | A | C | G | G | A | T | T | A | G | C | C |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 40 | 35 | 40 | 40 | 40 | 40 | 30 | 30 | 20 | 15 | 15 | 40 | 40 | 40 | 40 |

the lowest quality score in the string, 15, is tied between positions 11 and 12; the next lowest,
20, is at position 10. When the exact search fails, Bowtie does not try substituting an arbitrary base
at an arbitrary position — its rule of backtracking to the *leftmost* visited position with minimal
quality breaks the tie in favour of position 11 over 12, producing a second candidate read with T→C
at that position. If that also fails, the search can go one step further back and reopen position 10
(quality 20) as well, layering a second correction on top of the first:

| G | C | C | A | T | A | C | G | G | A | **C** | T | A | G | C | C |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 40 | 35 | 40 | 40 | 40 | 40 | 30 | 30 | 20 | 15 | 15 | 40 | 40 | 40 | 40 |

| G | C | C | A | T | A | C | G | G | **G** | **C** | T | A | G | C | C |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 40 | 35 | 40 | 40 | 40 | 40 | 30 | 30 | 20 | 15 | 15 | 40 | 40 | 40 | 40 |

This is a **greedy, depth-first search**: at each dead end it commits to the single most plausible
correction and carries on, rather than weighing every remaining possibility at once. It is simple and
fast, but the slides are explicit that it is **not optimal** — the first valid alignment the search
happens to reach is not guaranteed to be the alignment with the fewest or the least-costly mismatches.

<figure>
<svg viewBox="0 0 380 260" role="img" aria-label="A depth-first search tree that backtracks to the lowest-quality position it has visited">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0 0, 8 4, 0 8" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="190" y1="20" x2="190" y2="80" stroke="currentColor" stroke-width="1.5"/>
  <text x="200" y="35" font-size="12" fill="currentColor">position 9 (Q=30)</text>
  <line x1="190" y1="80" x2="190" y2="140" stroke="currentColor" stroke-width="1.5"/>
  <text x="200" y="95" font-size="12" fill="currentColor">position 10 (Q=20)</text>
  <line x1="190" y1="140" x2="190" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <text x="200" y="155" font-size="12" fill="currentColor">position 11 (Q=15, tied leftmost)</text>
  <line x1="190" y1="200" x2="120" y2="240" stroke="currentColor" stroke-width="1.5"/>
  <text x="70" y="255" font-size="12" fill="currentColor">too many mismatches</text>
  <circle cx="120" cy="240" r="4" fill="none" stroke="currentColor"/>
  <path d="M 190 200 C 260 210, 270 160, 250 145" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="255" y="130" font-size="12" fill="currentColor">backtrack to lowest Q visited</text>
  <line x1="190" y1="140" x2="270" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="270" y="195" font-size="12" fill="currentColor">try alternate base at 11</text>
  <line x1="270" y1="180" x2="320" y2="220" stroke="currentColor" stroke-width="1.5"/>
  <text x="325" y="225" font-size="12" fill="currentColor">valid alignment</text>
</svg>
<figcaption>The search extends the match downward one position at a time; when a branch dies, it does
not simply retreat one step but jumps back to the most recently visited position with the lowest
quality score and tries a different base there.</figcaption>
</figure>

## Bounding the search: a Maq-like policy

Backtracking without limits can still take arbitrarily long, so Bowtie supports an alignment policy
modelled on Maq's:\*

- at most $N$ mismatches are allowed within the leftmost $L$ bases of the read (the **seed**);
- the sum of the quality scores at the mismatched positions may not exceed $E$;
- $N$, $L$ and $E$ are set with the `-n`, `-l` and `-e` options.

For a read with quality string ending `...40 25 5 5` and policy $L = 12$, $E = 50$, $N = 2$, a
candidate correction is only kept alive while it still satisfies the budget — the search is pruned
(forced to backtrack further) as soon as continuing would require $N < 2$ mismatches to become
impossible to satisfy, or would push the accumulated mismatch quality past $E < 45$ remaining, or
would need a mismatch outside the seed once $L < 9$ and $N < 2$ have already been used up. In other
words, $N$, $L$, and $E$ are exactly the three quantities the depth-first search checks at every node
to decide whether to keep going or backtrack immediately.

\* Li H, Ruan J, Durbin R, "Mapping short DNA sequencing reads and calling variants using mapping
quality scores," *Genome Research*, 2008 — the Maq paper the policy is modelled on; not contained in
the lecture materials.

## Limiting backtracking further: searching from both ends

The seed policy above is stated in terms of the read's *left* end, but a backward search over an
index conventionally extends a match by consuming the read from one fixed end. If that end happens to
be the wrong one, every mismatch that matters for the seed policy is only discovered at the very end
of a long search, after most of the read has already been matched. The slides pose this directly: how
do you match left-to-right when the natural direction of the index search runs the other way?

Bowtie's answer is **double indexing**: build a second index, the "mirror index," over the reference
with its sequence reversed, alongside the ordinary "forward index." With both available, Bowtie can
scan whichever end of the read the seed policy actually constrains using the index that lets that end
be matched without backtracking, and confine any backtracking to the seed itself rather than letting
it range over the whole read.

## The cost of building the index in the first place

All of this backward search assumes an index already exists. Bowtie's own indexing algorithm builds a
BWT/FM-index and can trade memory for time. For the human genome (NCBI build 36.3, on a 2.4 GHz AMD
Opteron), the reported figures are:

| Physical memory target | Actual peak memory footprint | Wall clock time |
|---|---|---|
| 16 GB | 14.4 GB | 4h 36m |
| 8 GB | 5.8 GB | (not given in the source) |

The table is cut off in the source material after the second row; the point it illustrates is that
building the index for a genome-scale reference is itself a multi-hour, multi-gigabyte computation,
and the algorithm's memory/time tradeoff is a design choice, not a side effect.

## Sources

- Slide deck: `lectures/05-slides.md` ("Backtracking"), MIT OCW 7.091J *Foundations of Computational
  and Systems Biology*, Spring 2014. The deck's own note applies: it was reconstructed by a model
  from a PDF with no text layer, so some prose is paraphrase and every equation is unverified; where
  a fragment of the source (e.g. the opening `acaacg` example) was too garbled to interpret with
  confidence, this chapter states only the point it was illustrating rather than the exact figure.
  No transcript or written notes were supplied for this lecture.
- External material the slides point to but do not contain: Ben Langmead's slides,
  `http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt` (the source of the worked examples and the
  Bowtie description), and Li, Ruan, Durbin, "Mapping short DNA sequencing reads and calling variants
  using mapping quality scores," *Genome Research* 2008 (the Maq policy Bowtie's `-n`/`-l`/`-e` model
  is based on).
- Problem set 5 was supplied (`psets/05-questions/` and a second converted copy,
  `psets/05-questions-pset5-ques/`) but its four questions — protein-interaction network statistics,
  the Segway chromatin-state model, heritability, and chi-square association testing — belong to
  different material than this lecture's slides and do not exercise backtracking search or read
  alignment. They are not reproduced here.

---

[← 4. Markov Chains and CRISPR Genomics](04-markov-chains-and-crispr-genomics.md) · [Contents](index.md) · [6. OLC and de Bruijn Assembly →](06-olc-and-de-bruijn-assembly.md)
