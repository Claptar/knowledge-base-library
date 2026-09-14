---
title: Problem
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps2.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/ps/ps2.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem

**Source:** [`ps/ps2.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps2.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. This problem explores file sizes and their relationship to the file format.

   - (a) Based on understanding storage in ASCII plain text versus binary formats and on the fact that numbers are stored as 8 bytes per number in binary format, explain the results below. If there are any that seem inconsistent with the class notes and our discussion in class, note that.

_## save letters in text format_ chars <- **sample** (letters, 1e6, replace = TRUE) **write.table** (chars, file = 'tmp1.csv', row.names = FALSE, quote = FALSE, col.names = FALSE)

**system** ('ls -l tmp1.csv', intern = TRUE)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [[1] "-rw-r--r-- 1 paciorek scfstaff 2000000 Sep 11 07:38 tmp1.csv" →](03-1--rw-r--r---1-paciorek-scfstaff-2000000-sep-11-07-38-tmp1-c.md)
