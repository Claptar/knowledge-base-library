---
title: Extensions to the basic algorithm
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Extensions to the basic algorithm

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Ideas beyond W-mer indexing? Desirata:

   - Faster

   - Better sensitivity (fewer false negatives)

- 1) Filtering: Low complexity regions cause spurious hits

   - Filter out low complexity in your query

   - Filter most over-represented items in your database

- 2) Two-hit BLAST

   - Two smaller W-mers are more likely than one longer one

   - Therefore it’s a more sensitive searching method to look for two hits instead of one, with the same speed.

   - Improves sensitivity for any speed, speed for any sensitivity

- 3) Beyond W-mers, hashing with non-consecutive k-mers (combs)

   - Next slide

32

---

[← Why BLAST works(1): Pigeonhole and W-mers](27-why-blast-works-1-pigeonhole-and-w-mers.md) · [Up: contents](index.md) · [Extension 3: Combs and Random Projections →](29-extension-3-combs-and-random-projections.md)
