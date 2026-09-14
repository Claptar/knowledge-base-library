---
title: vs. Local alignment
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# vs. Local alignment

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### **<u>Needleman-Wunsch algorithm</u>**

###### **<u>Smith-Waterman algorithm</u>**

**<u>Initialization</u>** :

F(0, 0) = 0

**<u>Initialization</u>** :

**F(0, j) = F(i, 0)** = 0

**<u>Iteration</u>** :

**<u>Iteration</u>** :

F(i – 1, j) – d F(i, j) = max F(i, j – 1) – d F(i – 1, j – 1) + s(xi, yj) **<u>Termination</u>** : Bottom right

F(i, j) = max

**<u>Termination</u>** :

**0** F(i – 1, j) – d F(i, j – 1) – d F(i – 1, j – 1) + s(xi, yj) **Anywhere**

14

---

[← Global Alignment](11-global-alignment.md) · [Up: contents](index.md) · [More variations on the theme: semi-global alignment →](13-more-variations-on-the-theme-semi-global-alignment.md)
