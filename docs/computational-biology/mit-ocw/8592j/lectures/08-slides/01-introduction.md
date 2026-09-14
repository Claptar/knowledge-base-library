---
title: Introduction
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/08-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/08-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# 1.5 Sequence alignment

The dramatic increase in the number of sequenced genomes and proteomes has lead to development of various bioinformatic methods and algorithms for extracting information (data mining) from available databases. Sequence alignment methods (such as BLAST) are amongst the earliest and most widely used tools, essentially attempting to establish relations between sequences based on common ancestry, for example as a means of guessing function.

As discussed in the earlier lectures by Prof. Mirny, the explicit inputs are two (or more) sequences (or nucleotides for DNA/RNA, or amino-acids for proteins)


for example, corresponding to a query (newly sequenced gene) and a database. Implicit inputs are included as part of the scoring procedure, e.g. by assigning a similarity matrix s(a, b) between pairs of elements, and costs associated with initiating or extending gaps s(a, −). Global alignments attempt to construct the single best match that spans both sequences, while local alignments look for (possibly) multiple subsequences than are represent good local matches. In either case, recursive algorithms enable scanning the exponentially large space of possible matches in polynomial time. Within bioinformatics these methods are referred to as dynamic programming, in statistical physics they appear as transfer matrices, and have precedent in early recursive methods such as in the construction of binomial coefficients with the binomial triangle (below).


In most implementations the output of the algorithm is an optimal match, and a corresponding score S. An important question is whether this output is due to a meaningful relation between the tagged sequence (e.g. due to common ancestry, or functional convergence), or simply a matter of chance (e.g. due to the large size of database). To rule out the latter, we need to know the probability that a score S is obtained randomly. This probability can be either obtained numerically by applying the same algorithm to randomly generated (or shuffled) sequences, or if possible obtained analytically. Analytical solutions are particularly useful as significant alignment scores are likely to fall in the tails of the random distribution; a portion that is hard to access by numerical means.

20

---

[Up: contents](index.md) · [1.5.1 Significance of gapless alignments →](02-1-5-1-significance-of-gapless-alignments.md)
