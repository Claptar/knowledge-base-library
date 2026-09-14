---
title: 5 Probabilistic model for transcription factor binding sites (6.878 only)
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Probabilistic model for transcription factor binding sites (6.878 only)

**Source:** `psets/03-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem we will derive the probabilistic model underlying position weight matrices (PWMs) and use it to study CCCTC-binding factor ( _CTCF_ ) binding sites. CTCF is a conserved zinc-finger protein which binds to thousands of locations in the human genome and acts as an insulator/repressor.

The data provided for this problem comes from Kim _et al_ . “Analysis of the Vertebrate Insulator Protein CTCFBinding Sites in the Human Genome.” _Cell_ . 2007 Mar 23;128(6):1231–45. Submit all code you write.

- (a) Explain how to estimate the motif model M = [mij] where mij = P(position i = nucleotide j).

- (b) Describe and justify an algorithm to estimate the background model B. What assumptions does your model make? What are some of its weaknesses?

- (c) Recall that a PWM gives the log odds of observing a particular nucleotide at a particular position in the motif model against in the background distribution.

Use your algorithm from (a) to estimate M from `ctcf` ~~`b`~~ `inding` ~~`s`~~ `ite` ~~`s`~~ `equences.txt` and your algorithm from (b) to estimate B from `chr11 region.fa` . Include these distributions in your writeup.

Estimate a PWM for CTCF using M and B and include it in your writeup.

- (d) An alternative visual representation of transcription factor binding sites is a _sequence logo_ which gives the _information content_ at every position (intuitively, how important each position is for protein binding affinity).

   - Use WebLogo<sup>2</sup> to generate a sequence logo for `ctcf binding site sequences.txt` . Include it in your writeup.

- (e) Compare your sequence logo to the published logo `ctcf motif.jpg` . What could account for any differ­ ences?

- (f) Discuss the limitations of PWMs as a representation of transcription factor binding sites. What assumptions are made? Do they hold in general?

- (g) Because the entries of a PWM are log odds scores, we can score a k-mer by simply adding up the appropriate entries of the PWM.

Convert the published Position Frequency Matrix (PFM) `ctcf pwm.txt` to a PWM and use it to scan for CTCF binding sites in `chr11 region.fa` . This region flanks the gene insulin-like growth factor 2 ( _IGF2_ ). Plot the scores at every position for each strand and include the plots in your writeup.

- (h) Recall that short k-mers frequently occur by chance throughout the genome. Estimate the probability distribution of scores by randomly sampling 1 million 20-mers from chromosome 11 and scoring them using the published PWM. You may want to use the full sequence of chromosome 11 rather than the region we have provided3. Plot a histogram of this distribution.

A simple way to use this null distribution to filter out hits that occurred by chance is to only keep hits with P(score > threshold) < 10<sup>−5</sup> . Based on the distribution you estimated, what is the threshold?

In a plain text file, report the location, score, and sequence (be sure to account for strand orientation) of each 20-mer which meets the threshold.

- (i) Discuss some limitations of filtering PWM matches in this manner. Does the method by which we sample 20-mers matter? How will the sequence properties of randomly chosen genomic regions affect the answer? Can we choose regions in a more principled way to account for sequence properties? Is it possible to estimate the probability of a PWM match occurring by chance without sampling?

> 2 `http://weblogo.threeplusone.com/create.cgi`

> 3 `ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/chr11.fa.gz`

3

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 4 Upcoming project milestones](05-4-upcoming-project-milestones.md) · [Up: contents](index.md)
