---
title: 2 GRU (Gated Recurrent Unit)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentySix153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentySix153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 GRU (Gated Recurrent Unit)

**Source:** [`LectureTwentySix153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentySix153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

GRU is


1

_zt_ is called the update gate while _gt_ is called the reset gate. The unknown parameters in this model (which need to be estimated from the data) are _Wr_<sup>_g, W g, bg, W_</sup> _r_<sup>_z, W z, bz, Wr, W, b, β_0</sup><sup>_, β_.</sup>

Because of the presence of _zt_ , it is possible for _rt_ to be quite close to _rt−_ 1 for many time points _t_ . This allows _rt_ to have a relatively long memory.

---

[← 1 RNN](01-1-rnn.md) · [Up: contents](index.md) · [3 LSTM (Long Short Term Memory) →](03-3-lstm-long-short-term-memory.md)
