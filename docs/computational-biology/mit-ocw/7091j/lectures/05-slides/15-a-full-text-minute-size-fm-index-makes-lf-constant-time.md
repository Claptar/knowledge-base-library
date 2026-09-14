---
title: A Full-text Minute-size (FM) index makes LF constant time
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# A Full-text Minute-size (FM) index makes LF constant time

**Source:** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Solution: pre-calculate cumulative counts for A/C/G/T up to periodic **checkpoints** in BWT

**Rank: 242**

**Rank: 309**

- **LF** (i, **qc** ) is now constant-time (if space between checkpoints is considered constant)

Courtesy of Ben Langmead. Used with permission.

35

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

---

[← The FM index makes LF fast](14-the-fm-index-makes-lf-fast.md) · [Up: contents](index.md) · [An FM Index is Small →](16-an-fm-index-is-small.md)
