---
title: 4 LSTM (Long Short Term Memory)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFive153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 LSTM (Long Short Term Memory)

**Source:** [`LectureTwentyFive153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

LSTM is another modification to the basic RNN for enabling long memory. It also uses gates and has one more gate compared to the GRU. Instead of a recursion directly between _rt−_ 1 and _rt_ , the LSTM recursions are between the pairs ( _st−_ 1 _, rt−_ 1) _→_ ( _st, rt_ ).

We again construct a potential version _r_ ˜ _t_ of _rt_ in the same way as RNN:


In GRU, _rt_ was defined as a convex combination of _r_ ˜ _t_ and _rt−_ 1. In LSTM, _st_ is taken to be a linear combination of _st−_ 1 and _r_ ˜ _t_ with gates controlling both coefficients of the linear combination:


where _ft_ and _it_ denote gates. _rt_ is defined usually as _σ_ tanh( _st_ ). In LSTM, one also adds a gate to _rt_ :


Putting all the terms together (and also writing the formulae for the gates), we obtain the full LSTM model:


_ft_ is called the forget gate, _it_ is called the input gate and _ot_ is called the output gate. The unknown parameters in this model are _Wr_<sup>_f, W f, bf, W_</sup> _r_<sup>_i, W i, bi, W_</sup> _r_<sup>_o, W o, bo, Wr, W, b, β_0</sup><sup>_, β_.</sup> These need to be estimated from data.

---

[← 3 GRU (Gated Recurrent Unit)](03-3-gru-gated-recurrent-unit.md) · [Up: contents](index.md) · [5 Additional Optional Reading →](05-5-additional-optional-reading.md)
