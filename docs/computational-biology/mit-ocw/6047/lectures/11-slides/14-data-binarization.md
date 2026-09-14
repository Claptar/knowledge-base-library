---
title: Data Binarization
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data Binarization

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Leads to biologically interpretable models that can be robustly learned

- Let _cij_ be the number of reads for mark _i._ mapping to bin _j._ λi be the average number of reads mapping to a bin for modification _i_ . The input for feature _i_ becomes _‘_ 1 _’_ if

P( _X_ >cij)<10<sup>-4</sup>

where _X_ is a Poisson random variable with mean λi

58

---

[← Design Choice](13-design-choice.md) · [Up: contents](index.md) · [Emission Parameter Matrix ek ( ~~x~~ i ) →](15-emission-parameter-matrix-ek-x-i.md)
