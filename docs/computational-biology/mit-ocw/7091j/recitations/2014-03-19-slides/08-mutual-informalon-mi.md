---
title: Mutual InformaLon (MI)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Mutual InformaLon (MI)

**Source:** `recitations/2014-03-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- The most common way of quanLfying sequence covariaLon for the purpose of RNA   secondary structure determinaLon

- A measure of two variables' mutual dependence

   - Measures the informaLon that _X_ and _Y_ share: it measures how much knowing one of these variables reduces uncertainty about the other

   - If _X_ and _Y_ are independent, then knowing _X_ does not give any informaLon about _Y_ and vice versa, so their MI = 0

   - At the other extreme, if _X_ is a determinisLc funcLon of _Y_ and _Y_ is   a determinisLc funcLon of _X,_ then all informaLon conveyed by _X_ is shared with _Y_ : knowing _X_ determines the value of _Y_ and vice versa

      - As a result, in this case the mutual informaLon is the same as the uncertainty contained in _Y_ (or _X_ ) alone, namely the entropy of _Y_ (= entropy of _X_ )

   - Mutual informaLon between aligned columns of nucleoLdes that are base-­‐paired should be high

      - Knowing   one of the nucleoLdes tells you everything about the other (if A, other is U; if C, other is G, etc.)

11

---

[← non-­‐coding RNAs (ncRNAs)](07-non--coding-rnas-ncrnas.md) · [Up: contents](index.md) · [Mutual InformaLon (MI) →](09-mutual-informalon-mi.md)
