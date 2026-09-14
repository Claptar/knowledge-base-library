---
title: 5 Hidden Markov Model classification of CpG islands (6.878 only)
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Hidden Markov Model classification of CpG islands (6.878 only)

**Source:** `psets/02-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, we will implement the eight-state Hidden Markov model described in lecture to annotate regions as CpG islands, or regions with high CpG dinucleotide frequency. Recall the model has states A<sup>+</sup> , C<sup>+</sup> , G<sup>+</sup> , T<sup>+</sup> which emit nucleotides within CpG islands and states A<sup>−</sup> , C<sup>−</sup> , G<sup>−</sup> , T<sup>−</sup> which emit nucleotides outside CpG islands. Submit all code you write.

- (a) Train the model by computing the maximum likelihood estimates of the model parameters (recall these are relative frequencies). Describe and justify how you handle zeroes in the estimated parameters. Estimate the initial state distribution and justify the method you used to do so.

Submit plain text files containing the transition probability matrix (space-separated entries, one row per line), the emission probability matrix (one row per state, one column per nucleotide; space-separated entries, one row per line) and the initial state distribution (one entry per line).

The training data is the sequence of human chromosome 21 and an existing CpG island annotation which we will use as ground truth (available at the URLs below):

```
ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/chr21.fa.gz
```

```
ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/cpgIslandExt.txt.gz
```

The schema for the CpG island annotation database table is available at the URL given below. You will only need columns 2–4 (“chrom”, “chromStart”, “chromEnd”).

```
ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/cpgIslandExt.sql
```

- (b) Use the Viterbi algorithm to annotate CpG islands in the region surrounding the SRY (sex determining region Y)-box 10 gene ( _SOX10_ ). We are interested in the region between positions 38,000,000–39,000,000 of human chromosome 22. The reference sequence of chromosome 22 is available at the URL below:

```
ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/chr22.fa.gz
```

Submit a BED file with your annotated regions. You only need to include chromosome and position information. The BED file format specification is available at the URL below:

```
https://genome.ucsc.edu/FAQ/FAQformat.html#format1
```

- (c) Evaluate the performance of the model by computing its false positive and false negative rates on the test data against the ground truth annotation. Define a true positive to be a predicted CpG island of which at least 50% overlaps a true CpG island.

Are these two rates equal? If not, what causes this bias?

- (d) Could we improve the performance of the model by tuning parameters? If so, describe how you would do so (you do not have to implement your suggestions). If not, describe and justify some modifications to the model which could reduce its error rate.

- (e) One alternative approach to improve the quality of annotations is combining multiple lines of evidence. Describe and justify some biological criteria for filtering the output of a sequence-based CpG island classifier to improve its performance.

4

MIT OpenCourseWare http://ocw.mit.edu

6.047 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 4 Final project preparation](05-4-final-project-preparation.md) · [Up: contents](index.md)
