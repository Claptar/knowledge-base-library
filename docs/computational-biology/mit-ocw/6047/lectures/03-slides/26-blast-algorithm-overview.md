---
title: Blast Algorithm Overview
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Blast Algorithm Overview

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Receive query

   1. Split query into overlapping words of length W

   2. Find neighborhood words for each word until threshold T

   3. Look in table where these neighbor words occur: seeds S

   4. Extend seeds S until score drops off under X

- Report significance and alignment of each match


<!-- Start of picture text -->
1. Split query into words<br>W-mer<br>Database<br>2. Expand word<br>    neighborhood  PMG<br>T<br>3. Search database for<br>4. Extend each hit into alignment<br>    neighborhood matches<br><!-- End of picture text -->

30

---

[← Speeding up your searches in dB setting](25-speeding-up-your-searches-in-db-setting.md) · [Up: contents](index.md) · [Why BLAST works(1): Pigeonhole and W-mers →](27-why-blast-works-1-pigeonhole-and-w-mers.md)
