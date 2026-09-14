---
title: 2. Sequence hashing and dotplot visualization
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. Sequence hashing and dotplot visualization

**Source:** `psets/01-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As you have seen in problem 1, sequence alignment is a quadratic time algorithm. Full sequence alignment is therefore only feasible for sequences near the length of a single gene. To align larger regions of a genome, heuristic approximations are typically used. In this problem, you will use hashing techniques to guide the alignment of a 1 megabase (1 million nucleotides) region surrounding the HoxA cluster in human ( `human-hoxa-region.fa` ) and mouse ( `mouse-hoxa-region.fa` ). You will use dotplots to visualize the performance of various hashing methodologies.

The code provided ( `ps1-dotplot.py` ) finds all 30-mers in the human that also appear in mouse. On a dotplot, each of these matches is represented as a single dot at ( _x, y_ ), where _x_ is a coordinate for the beginning of a 30-mer in human and _y_ is a coordinate for the beginning of a matching 30-mer in mouse. We provide a plotting function that will produce dotplot images. The format of the image is determined by the file extension (*.ps, *.png, *.jpg). There is also code for heuristically judging the _specificity_ of the matches (the fraction of matches that occur near the diagonal of the dotplot).

- (a) Run the script unchanged to generate a dotplot for all exact matching 30-mers. It must be run in the same directory where it is located, since it also requires `utils.py` and `plotting.py` . This script also requires `gnuplot` which is available on athena.

Before running the script, do: `athena% add gnu`

The command to run the program is: `athena% python ps1-dotplot.py <FASTA 1> <FASTA 2> <PLOT FILE (*.ps, *.png, *.jpg)`

Alternatively, you can run on your own machine if you have gnuplot installed.

Describe what you see. How many hits are there and what percentage fall near the diagonal? Do you observe any structure in the off-diagonal hits? What types of genomic elements could cause such a pattern? Why are matches that are close to the diagonal more likely than off-diagonal matches to represent “correct”, or orthologous, alignments?

- (b) Make the following modifications to the script and report how the plot changes qualitatively and quantatively (how many hits, what percentage are near the diagonal). Also briefly describe how you implemented each change.

   - i. Modify the script to find all _exact_ matching 100-mers

   - ii. Modify the script to find all 60-mers that match every _other_ base

   - iii. Modify the script to find all 90-mers that match every _third_ base

   - iv. Modify the script to find all 120-mers that match every _fourth_ base

   - v. Modify the script to find all 100-mers that allow _at most two_ mismatches in each contiguous block of six bases. Instead of producing a plot, focus on describing how you would implement this modification.

- (c) Although parts a, b.ii, b.iii, and b.iv require the same number of matching bases (30 = 60 _/_ 2 = 90 _/_ 3 = 120 _/_ 4), one of them is more specific to the diagonal. Explain why this might be so.

- (d) Explain the trade-off you see between number of hits near the diagonal (sensitivity) and the percentage of hits near the diagonal (specificity). How is the trade-off affected by the hashing parameters?

- (e) Modify the script to also detect inversions. An inversion occurs when a stretch of DNA is spliced out and reinserted in reverse orientation. For example, CGT[GATT]AGA

_⇓_

Athena is MIT's UNIX-based computing environment. OCW does not provide access to it.

2

**6.047/6.878/HST.507 Fall 2015**

**Problem Set 1**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [CGT[AATC]AGA →](03-cgt-aatc-aga.md)
