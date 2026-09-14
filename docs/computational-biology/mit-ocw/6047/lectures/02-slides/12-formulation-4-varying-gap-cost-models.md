---
title: 'Formulation 4: Varying gap cost models'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Formulation 4: Varying gap cost models

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Linear gap penalty

– Same as before

2. Affine gap penalty

- Big initial cost for starting or ending a gap

- Small incremental cost for each additional character

3. General gap penalty

- Any cost function

– No longer computable using the same model 4. Frame-aware gap penalty

- Multiples of 3 disrupt coding regions

5. Seek duplicated regions, rearrangements, …

– Etc

15

---

[← Formulation 3: Sequence alignment](11-formulation-3-sequence-alignment.md) · [Up: contents](index.md) · [How many alignments are there? →](13-how-many-alignments-are-there.md)
