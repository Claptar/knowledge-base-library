---
title: 1 Gibbs sampling for motif discovery
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Gibbs sampling for motif discovery

**Source:** `psets/03-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, you will implement a Gibbs sampler to discover sequence motifs. We have provided a Python skeleton `gibbs.py` . Submit all code you write.

- (a) Recall the Gibbs sampling algorithm for this problem: Initialize the motif position in each sequence. Until convergence: re-estimate the position weight matrix (PWM) from all the motifs except one, score ev­ ery position in the excluded sequence, and sample a k-mer from the excluded sequence with probability proportional to the score.

We have intentionally not specified many of the implementation details. Describe and justify the design decisions you made in your implementation. For example, how do you choose the sequence to exclude when recomputing the position weight matrix?

- (b) We have provided four test cases. `data1` is a synthetic data set where the motif is identical across the sequences. `data2` is a synthetic data set with a degenerate motif. `data3` and `data4` are yeast transcription factor binding sites of _ACE2_ and _MBP1_ , respectively.

Run your Gibbs sampler on the test data to discover motifs of length 10. You will need to repeat this procedure several times on each data set due to the stochastic nature of Gibbs sampling.

Submit plain text files containing the most consistently found PWM for each sequence. Use Weblogo<sup>1</sup> to create a _sequence logo_ from each PWM and include them in your writeup.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Evolutionary signatures of motifs →](03-2-evolutionary-signatures-of-motifs.md)
