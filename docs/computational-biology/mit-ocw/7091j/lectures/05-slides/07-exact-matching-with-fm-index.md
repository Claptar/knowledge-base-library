---
title: Exact Matching with FM Index
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Exact Matching with FM Index

**Source:** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

q = “aac” top = 0 bot = len(bwt) for qc in reverse(q): top = LF(top, qc) bot = LF(bot, qc)

**In each iteration top & bot delimit the range of rows beginning with progressively longer suffixes of q**


Courtesy of Ben Langmead. Used with permission.

27

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

---

[← Short Read Alignment](06-short-read-alignment.md) · [Up: contents](index.md) · [Exact Matching with FM Index →](08-exact-matching-with-fm-index.md)
