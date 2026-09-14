---
title: Genome alignment in an excel spreadsheet
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Genome alignment in an excel spreadsheet

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

9


<!-- Start of picture text -->
Genome alignment<br>in an excel<br>spreadsheet<br>K15<br>AD15<br>K15  AD15<br>Max alignment score of<br>Local score of matching<br>aligning prefix S1[1..i]<br>characters S1[i] and S2[j]<br>and prefix S2[1..j]<br>AD34<br>AD34<br>K34  K34<br>Is the [i,j] part of an optimal<br>path? (i.e. are chars S1[i]<br>Is the max alignment score  and S2[j] aligned to each<br>coming from the top (“|”),  other in an optimal path)<br>(also count number of<br>from the left (“--”) or from<br>optimal paths/alignment<br>the diagonal up (“\”)<br>through [i.j], cuz we can)<br>(show all of them, cuz we can)  AD53<br>AD53<br>K53<br>K53<br><!-- End of picture text -->

Construct the optimal alignment for sequence S1 by adding in characters or gaps to increasingly large suffixes (and arbitrarily choose one path when multiple using nested if’s)

Construct the optimal alignment for sequence S2 similarly to S1 10

---

[← Finding optimal path using only linear space](06-finding-optimal-path-using-only-linear-space.md) · [Up: contents](index.md) · [Today’s Goal: Diving deeper into alignments →](08-today-s-goal-diving-deeper-into-alignments.md)
