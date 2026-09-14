---
title: An FM Index is Small
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# An FM Index is Small

**Source:** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Entire FM Index on DNA reference consists of:

   - BWT (same size as T)

Assuming 2-bit-per-base encoding and no compression, as in Bowtie

- Checkpoints (~15% size of T)

Assuming a 16-byte checkpoint every 448 characters, as in Bowtie

- Suffix array sample

- (~50% size of T)

Assuming Bowtie defaults for suffixarray sampling rate, etc

- Total: ~1.65x the size of T


**~1.65x**

**>45x**

**>15x**

**>15x**

Courtesy of Ben Langmead. Used with permission.

36

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

---

[← A Full-text Minute-size (FM) index makes LF constant time](15-a-full-text-minute-size-fm-index-makes-lf-constant-time.md) · [Up: contents](index.md) · [FM Index in Bioinformatics →](17-fm-index-in-bioinformatics.md)
