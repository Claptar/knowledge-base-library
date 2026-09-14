---
title: Short read alignment (mapping)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Short read alignment (mapping)

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Motivation: Common sequencing experiments: ~100 million 100bp reads to align to a billion base pair genome

- Naïve (“ctrl-F” search) method of taking a read and searching the entire genome:

   - O(genome size = 1 billion) per read (without indels) – For all reads: O(1 billion x 200 million) – infeasible! – Ideally, something that approaches O(# of reads) – approximately independent of the size of genome

- We do this through BWT transform and FM index of genome

6


7

---

[← Library Complexity](03-library-complexity.md) · [Up: contents](index.md) · [Why use the BWT? →](05-why-use-the-bwt.md)
