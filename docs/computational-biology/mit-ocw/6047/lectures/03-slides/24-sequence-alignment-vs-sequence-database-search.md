---
title: Sequence Alignment vs. Sequence Database Search
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Sequence Alignment vs. Sequence Database Search

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Sequence Alignment

   - Assumes sequences have some common ancestry

   - Finding the “right” alignment between two sequences

   - Evolutionary interpretation: min # events, min cost

- Sequence Database Search

   - Given a query (new seq), and target (many old seqs), ask: which sequences (if any) are related to the query

   - – Individual alignments need not be perfect: Once initial matches are reported, we can fine-tune them later

   - Query must be very fast for a new sequence

   - Most sequences will be completely unrelated to query

- Exploit distinct nature of database search problem

27

---

[← Today’s Goal: Diving deeper into alignments](23-today-s-goal-diving-deeper-into-alignments.md) · [Up: contents](index.md) · [Speeding up your searches in dB setting →](25-speeding-up-your-searches-in-db-setting.md)
