---
title: 2 Dilution of Proteins Due to Cell Growth
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Dilution of Proteins Due to Cell Growth

**Source:** `psets/01-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A single bacterial cell at time _t_ = 0 has volume _V_ 0 . After a time interval _TD_ , the doubling time, the cell grows and divides into two cells, each of volume _V_ 0 ; after another interval _TD_ , there are four cells, and so on.

- a. Show that the combined volume of cells at time _t_ may be written as _V_ ( _t_ ) = _V_ 0 _e_<sup>_γt_</sup> . Find _γ_ in terms of _TD_ .

- b. The protein _X_ is created at some rate _k_ ( _t_ ) , so the total number of molecules of _X_ satises _<u>dndt</u>_ = _k_ ( _t_ ) . Show that the concentration [ _X_ ] = _Vn_ satises<sup>_d_</sup><sup><u>[</u></sup> _dt_<sup>_X_</sup><sup><u>]</u></sup> =<sup>_k_</sup> _V_<sup><u>(</u></sup><sup>_t_</sup><sup><u>)</u></sup> _− γ_ [ _X_ ] . Discuss the origin of the decay term.

1

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 1

- c. In addition to the term derived in (b), there should be an extra term that takes into account the degradation of proteins by proteinases, which we can model by the eective reaction _δ_

- _X →_ ∅ . Modify the equation in part (b) to include protein degradation, and work out the steady-state protein concentration. This allows estimation of the steady-state concentration if the protein production and degradation rates, cell volume and cell doubling time are known.

- d. The model you arrived at in (b) can be applied to mRNA as well. Search the literature for the doubling time of your favorite single cell organism (or cell type of multi-cellular organisms), and also nd the creation and degradation rate of your favorite protein and mRNA in that organism or cell type. Work out the steady state protein and mRNA concentration. Give references.

---

[← 1 Transcription and Translation](02-1-transcription-and-translation.md) · [Up: contents](index.md) · [3 Binding Kinetics, Detailed Balance and Cooperation →](04-3-binding-kinetics-detailed-balance-and-cooperation.md)
