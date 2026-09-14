---
title: 'Why BLAST works(1): Pigeonhole and W-mers'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Why BLAST works(1): Pigeonhole and W-mers

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Pigeonhole principle – If you have 2 pigeons and 3 holes, there must be at least one hole with no pigeon


<!-- Start of picture text -->
RKI          WGD         PRS<br><!-- End of picture text -->


RKI          VGD          RRS

- Pigeonholing mis-matches

   - Two sequences, each 9 amino-acids, with 7 identities

   - There is a stretch of 3 amino-acids perfectly conserved

- In general:

   - Sequence length: n

   - Identities: t

   - Can use W-mers for W= [n/(n-t+1)]

31

---

[← Blast Algorithm Overview](26-blast-algorithm-overview.md) · [Up: contents](index.md) · [Extensions to the basic algorithm →](28-extensions-to-the-basic-algorithm.md)
