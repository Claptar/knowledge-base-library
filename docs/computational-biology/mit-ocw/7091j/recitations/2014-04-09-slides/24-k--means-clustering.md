---
title: K-­‐means clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# K-­‐means clustering

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Determinis'c   given:

   - 1.   Choice   of _k_

   - 2.   The _k_ star'ng   points   for   the   clusters

- For   2:   Generally   want   to   run   many   'mes   with   different   star'ng points   to   obtain   most   robust   par''on

- For   1:

   - Try   many   different _k_ s   (below   and   above   what   you   think   it   might   be)

   - Intui'vely,   you   should   see   large   decreases   in   the   intra-­‐cluster   distance   when uncovering   true   underlying   clusters   &   smaller   decreases   when   overfi|ng

   - Decision   can   be   made automa'cally   through   frameworks   such   as   Bayesian   Big steps occur when we are dividing data into natural clusters

   - Informa'on   Criterion   (BIC   –   penalizes   addi'on   of   more   free   parameters; accepts   model   (i.e., _k_ )   that   op'mizes   a   tradeoff   between   increased   likelihood of   data   from   more   clu ~~sters~~ and   increased   number   of   free   parameters) Smaller steps occur when we are overclustering

32

---

[← K-­‐means clustering example ( k =4)](23-k--means-clustering-example-k-4.md) · [Up: contents](index.md) · [K-­‐means clustering →](25-k--means-clustering.md)
