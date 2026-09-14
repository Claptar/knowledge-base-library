---
title: 'Solution #2 – Dynamic programming'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution #2 – Dynamic programming

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Create a big table, indexed by (i,j)

   - Fill it in from the beginning all the way till the end

   - You know that you’ll need every subpart

   - Guaranteed to explore entire search space

- Ensures that there is no duplicated work

   - Only need to compute each sub-alignment once!

- Very simple computationally!

## **Bottom up approach**

33

#### **Key insight #4: Optimal prefix almt score**  **Matrix entry**

||S1[1..i]|i|S1[i..n]|
|---|---|---|---|
|S2[1..j]||||
|j||**S**||
|S2[ j..m]||||


34

---

[← Solution #1 – Memoization](29-solution-1-memoization.md) · [Up: contents](index.md) · [Key insight #5: Optimal alignment  Matrix path →](31-key-insight-5-optimal-alignment-matrix-path.md)
