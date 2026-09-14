---
title: 4 LSTM (Long Short Term Memory)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyFive153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 LSTM (Long Short Term Memory)

**Source:** [`LectureTwentyFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyFive153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

LSTM is another modification to the basic RNN for enabling long memory. It also uses gates and has one more gate compared to the GRU. Instead of a recursion directly between _rt−_ 1 and _rt_ , the LSTM recursions are between the pairs ( _st−_ 1 _, rt−_ 1) _→_ ( _st, rt_ ). We will look at the formulas for LSTM in the next lecture.

---

[← 3 GRU (Gated Recurrent Unit)](03-3-gru-gated-recurrent-unit.md) · [Up: contents](index.md) · [5 Additional Optional Reading →](05-5-additional-optional-reading.md)
