---
title: 1 Generalized suffix trees (10pts)
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Generalized suffix trees (10pts)

**Source:** `psets/04-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, we will study some generalizations of suffix trees which allow searching multiple strings and approximate string matching.

- (a) Describe a modification to the suffix tree data structure which will allow queries on multiple strings. For example, we may want to search for occurrences of a particular query sequence in multiple reference genomes.

- (b) Recall that in the case of a suffix tree on one string, we can construct an equivalent suffix array which will require less space to store. Can your generalized suffix tree be transformed into a suffix array? If so, give an algorithm to do so. Is it possible to directly use a suffix array to solve this problem?

- (c) Suppose we are instead interested in allowing only certain mismatches in certain positions (e.g., looking for motif instances). Describe how to build a suffix tree which can handle these queries. Can this tree be transformed into a suffix array?

- (d) Suppose we want to search for approximate occurrences of a query string within _Hamming distance_ k (number of mismatches at most k). Describe an algorithm to perform this query on a suffix tree. **Extra credit:** Describe an algorithm to perform this query on a suffix array.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Finding eQTLs (20pts) →](03-2-finding-eqtls-20pts.md)
