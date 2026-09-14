---
title: Missing Data
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Missing Data

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• What if a particular data point is missing? (Back in the old days: there was a bubble or a hair on the array)

- ignore that gene in all samples

- ignore that sample for all genes

- replace missing value with a constant

- “impute” a value

   - example:  compute the K most similar genes (arrays) using the available data;  set the missing value to the mean of that for these K genes (arrays)

39

---

[← Distance Metrics](21-distance-metrics.md) · [Up: contents](index.md) · [Outline →](23-outline.md)
