---
title: Jukes-Cantor model
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Jukes-Cantor model

**Source:** `recitations/2014-02-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- the number of observed differences between two homologous sequences is smaller than the actual number of changes that have occurred, due to reversions (e.g. ) - can underestimate the genetic distance between the sequences

   - How to compensate? need some model of how mutations occur

- Jukes-Cantor model assumes that all mutations are equally likely and occur with rate ; if this is true, then you can apply the following correction:


   - P = observed fraction sites that differ

   - K = actual number of substitutions

- This is very simple; other models are much more complex (e.g. Kimura, which

- 13 has transitions and occurring more frequently than transversions and ).

---

[← vs. BLOSUM](10-vs-blosum.md) · [Up: contents](index.md) · [Positive / Negative Selection →](12-positive-negative-selection.md)
