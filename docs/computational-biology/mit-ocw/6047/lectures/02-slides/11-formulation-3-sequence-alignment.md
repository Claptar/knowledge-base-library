---
title: 'Formulation 3: Sequence alignment'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Formulation 3: Sequence alignment

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Allow gaps (fixed penalty)

   - Insertion & deletion operations

   - Unit cost for each character inserted or deleted

- Varying penalties for edit operations

   - Transitions (PyrimidinePyrimidine, PurinePurine)

   - Transversions (Purine  Pyrimidine changes)

   - Polymerase confuses Aw/G and Cw/T more often

|Scoring function:||A|G|T|C|**Transitions**:|
|---|---|---|---|---|---|---|
|Match(x,x) = +1|A|+1|-½|-1|-1|AG, CTcommon|
|Mismatch(A,G)= -½|G|-½|+1|-1|-1|(lower penalty)|
|Mismatch(C,T)= -½|T|-1|-1|+1|-½|**Transversions**:|
|Mismatch(x,y) = -1|C|-1|-1|-½|+1|All other operations|


purine pyrimid.

14

---

[← Formulation 2: Longest common subsequence](10-formulation-2-longest-common-subsequence.md) · [Up: contents](index.md) · [Formulation 4: Varying gap cost models →](12-formulation-4-varying-gap-cost-models.md)
