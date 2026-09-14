---
title: Mean-bit score of a motif
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Mean-bit score of a motif

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Use relative entropy (mean bit-score) of a distribution _p_ relative to the background distribution _q_


   - _n_ is the number of states; _n_ =4<sup>_w_</sup> for nucleotide sequence of width _w_

- The relative entropy is a measure of _information_ of one distribution _p_ relative to another _q_ , not entropy/uncertainty (defined for a single distribution)

   - Better to use this for information of motif when background is non-random: For example, you have gained more information/knowledge upon observing a sequence _k_ if it’s rare (if pk<1/n) than if it’s uniformly or highly likely or (pk≥1/n)

- For sequences with uniform background (qk=1/4<sup>w</sup> ):

Hmotif is the Shannon entropy of the motif

- A motif with _m_ bits of information generally occurs once every 2<sup>_m_</sup> bases of random sequence

6

## Non-random background sequences

- What is the information content of a motif (model) that  consists of codons that always have the same nucleotide at the 1<sup>st</sup> and 3<sup>rd</sup> position?

   - There are 16 possible codons (4 possibilities for the first/third positions, and 4 possibilities for 2<sup>nd</sup> position).

   - Assuming these are all equally likely, pk=1/16 for these codons, pk=0 otherwise (e.g. for AGT codon)


- The 1<sup>st</sup> position determines the 3<sup>rd</sup> position, so the information that we’ve gained is complete knowledge of this position given the first position (i.e., the full information content of one position, which is 2 bits)

- Also note that the Shannon entropy of the motif is


So relative to a uniform background distribution of codons (qk=1/64), the information content of this motif is:     I=2w – Hmotif = (2*3) – 4 = 2 bits (same as calculating Relative Entropy)

7

---

[← Shannon Entropy](04-shannon-entropy.md) · [Up: contents](index.md) · [Gibbs Sampler →](06-gibbs-sampler.md)
