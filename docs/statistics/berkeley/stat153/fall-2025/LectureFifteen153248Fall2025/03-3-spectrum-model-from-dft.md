---
title: 3 Spectrum Model from DFT
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Spectrum Model from DFT

**Source:** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In (1) or (2), we formulated the spectrum model in terms of the periodogram or logperiodogram. We can also describe it in terms of the DFT. Specifically, in terms of the DFT _b_ 0 _, . . . , bn−_ 1 of the data _y_ 0 _, . . . , yn−_ 1, the model is given by:


for _j_ = 1 _, . . . , m_ where _m_ = ( _n −_ 1) _/_ 2 (we are assuming that _n_ is odd). The unknown parameters in this model are _γ_ 1<sup>2</sup><sup>_, . . . , γ_</sup> _m_<sup>2and</sup><sup>_γj_representsthestrengthofsinusoidsatfrequency</sup> _j/n_ .

By definition of the periodogram, we get


By the assumption (3), we get


Therefore the model (3) implies that


The is exactly the same as (1) with the identification:


Because of this equivalence, we shall treat (3) as another formulation of the spectrum model.

---

[← 2 Power Spectral Density](02-2-power-spectral-density.md) · [Up: contents](index.md) · [4 Rewriting the Model in terms of yt →](04-4-rewriting-the-model-in-terms-of-yt.md)
