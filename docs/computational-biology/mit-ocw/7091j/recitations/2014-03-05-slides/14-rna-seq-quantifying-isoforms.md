---
title: 'RNA-seq: quantifying isoforms'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# RNA-seq: quantifying isoforms

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- we want to find the proportions 1<sup>_,...,_</sup> _n_ of each of the _n_ isoforms _T_ 1 _, ..., Tn_ after observing _m_ reads _R_ 1 _, ..., Rm_ - In other words, find abundances that maximize the likelihood of observing our reads _R:_ = _argmaxL_ ( _R|_ )

- You can estimate the expression of each isoform using the total # of reads that map to the gene and

-for example, see Cufflinks ( http://cole-trapnell-lab.github.io/cufflinks/ ) for a common program that does this

26

---

[← RNA-seq: identifying isoforms](13-rna-seq-identifying-isoforms.md) · [Up: contents](index.md) · [Likelihood ratio test →](15-likelihood-ratio-test.md)
