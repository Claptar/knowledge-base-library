---
title: Speeding up your searches in dB setting
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Speeding up your searches in dB setting

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Exploit nature of the problem (many spurious hits)

   - If you’re going to reject any match with idperc <= 90, then why bother even looking at sequences which don’t have a stretch of 10 nucleotides in a row.

   - Pre-screen sequences for common long stretches

- Put the speed where you need it (pre-processing)

   - Pre-processing the database is off-line.

   - Once the query arrives, must act fast

- Solution:  content-based indexing and BLAST

   - Example: index 10-mers.

   - Only one 10-mer in 4<sup>10</sup> will match, one in a million (even with 500 k-mers, only 1 in 2000 will match).

   - Additional speedups are possible

28

# **BLAST**


BLAST citations per year

- Two key insights:

      - PSI-BLAST & Gapped Blast

- Hashing:

   - Like Karp-Rabin, semi-numerical string matching

- Neighborhood search:

   - Can find hits even when no exact k-mer matches

29

---

[← Sequence Alignment vs. Sequence Database Search](24-sequence-alignment-vs-sequence-database-search.md) · [Up: contents](index.md) · [Blast Algorithm Overview →](26-blast-algorithm-overview.md)
