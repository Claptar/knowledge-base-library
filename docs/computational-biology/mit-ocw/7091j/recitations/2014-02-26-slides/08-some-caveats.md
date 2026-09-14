---
title: Some caveats
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Some caveats

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- how to calculate occ( _qc_ ) and count( _i_ , _qc_ ) when the genome is huge?

   - for occ( _qc_ ), need only to know where each character in the genome begins, for example as a dictionary in python:

occ = {"A": 1, "C": 345, "G": 768, "T": 981}

means there is only 1 char ("$") lexigraphically smaller than "A", there are 345 smaller than "C", 768 smaller than "G" etc.

   - count( _i_ , _qc_ ) is trickier – naïvely, you could store for each ACGT a genomelength array containing count( _i_ , _qc_ ) at location _i_ , but these would be huge! Instead, store counts for only a subset of positions, then count # of _qc_ s between _i_ and closest stored count

- similarly, the method we showed for recovering the offset of a match using the LF function requires "walking back" to the beginning of the string – quite a long time, using a whole genome!

   - naïvely again, could keep genome-length mapping of BWT to original string indices -> lookup table

   - since genome is huge, instead store indices for every _i_ th row Together, these improvements comprise the FM-index

19

### Genome Assembly (“shotgun sequencing”)

- First sequencing of human genome

   - _De novo_ assembly of sample from field work

- This is in contrast to most experiments in labs these days in which you generally are mapping your sequenced reads to the known reference genome of yeast, _C. elegans_ , mouse, human, etc.

- May be situations in which you don’t do full genome assembly but partial assembly for reads that don’t map to reference genome to discover, for example, translocations, inversions, etc. in cancer tumor samples

- Longer reads and more depth is better, but limited by: – Experimental cost

   - Errors in longer reads (higher errors from bases ~50 onward)

20

---

[← Last to First (LF) function](07-last-to-first-lf-function.md) · [Up: contents](index.md) · [Two main approaches →](09-two-main-approaches.md)
