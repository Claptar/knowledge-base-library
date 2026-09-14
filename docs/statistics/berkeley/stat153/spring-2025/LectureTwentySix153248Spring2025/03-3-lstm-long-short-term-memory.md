---
title: 3 LSTM (Long Short Term Memory)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentySix153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentySix153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 LSTM (Long Short Term Memory)

**Source:** [`LectureTwentySix153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentySix153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

LSTM is another modification to the basic RNN for enabling long memory. It also uses gates and has one more gate compared to the GRU. Instead of a recursion directly between _rt−_ 1 and _rt_ , the LSTM recursions are between the pairs ( _st−_ 1 _, rt−_ 1) _→_ ( _st, rt_ ):


_ft_ is called the forget gate, _it_ is called the input gate and _ot_ is called the output gate. The presence of these gates allow _rt_ to draw information from _xu_ even for _u_ quite far from _t_ .

The unknown parameters in this model are _Wr_<sup>_f, W f, bf, W_</sup> _r_<sup>_i, W i, bi, W_</sup> _r_<sup>_o, W o, bo, Wr, W, b, β_0</sup><sup>_, β_.</sup>

The LSTM unit is all the equations in (4) excluding the last linear layer _µt_ = _β_ 0 + _β_<sup>_T_</sup> _rt_ :


The output of the LSTM unit is _rt_ . In PyTorch (see `https://pytorch.org/docs/stable/ generated/torch.nn.LSTM.html` ), the notation used for the LSTM unit differs slightly from (5). The LSTM PyTorch unit is given by:


where _σ_ = _σ_ sigmoid.

2

Both (5) and (6) implement the same LSTM update, but they differ in notation. Our _rt_ is named _ht_ in PyTorch, and our _st_ is named _ct_ in PyTorch. _ht_ is referred to as the hidden state and _ct_ is referred to as the cell state.

The three gates have the same notation in both formulae: forget _ft_ , input _it_ , output _ot_ . The candidate or potential feature vector _r_ ˜ _t_ in (5) is denoted by _gt_ in (6). In (6), there are two bias vectors in each of the formulae for _it, ft, gt, ot_ . We combined these to one bias vector in (5). Other than these notational differences, the formulae (5) and (6) are identical.

---

[← 2 GRU (Gated Recurrent Unit)](02-2-gru-gated-recurrent-unit.md) · [Up: contents](index.md) · [4 Additional Optional Reading →](04-4-additional-optional-reading.md)
