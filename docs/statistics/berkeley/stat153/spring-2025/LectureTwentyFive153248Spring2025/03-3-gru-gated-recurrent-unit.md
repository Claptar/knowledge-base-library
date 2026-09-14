---
title: 3 GRU (Gated Recurrent Unit)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFive153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 GRU (Gated Recurrent Unit)

**Source:** [`LectureTwentyFive153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider again the RNN formula (6). The basic problem with this is that _rt_ depends on _rt−_ 1 through the term _Wrrt−_ 1. If _Wr_ is a matrix with spectral radius less than 1 (which it needs

3

to be for stability purposes), then the multiplier _Wrrt−_ 1 can be thought of as “reducing” _rt−_ 1 by a factor of _Wr_ . If this formula is applied repeatedly, then very soon the dependence of _rt_ on _ru_ will be very small. In order to avoid this, one needs to prevent _rt_ from depending on _rt−_ 1 only through _Wrrt−_ 1.

This leads to the following idea. First construct a potential version _r_ ˜ _t_ of _rt_ in the same way as (6):


This _r_ ˜ _t_ only depends on _rt−_ 1 through _Wrrt−_ 1. The two natural options for _rt_ now are:

1. _rt_ = _r_ ˜ _t_ : in this case, we are back to the RNN (6).

2. _rt_ = _rt−_ 1: in this case, _rt_ is exactly equal to _rt−_ 1, which means that the current input _xt_ is ignored.

The idea behind GRU is to take a “convex-like” combination of these two options in the following way:


This would be exactly a convex combination if _zt_ were a scalar in the interval [0 _,_ 1]. But we allow _zt_ to be a vector interpreting the multiplication as pointwise. Thus it is better to write


The next thing to specify _zt_ . In GRU, we take


Because _σ_ sigmoid takes values between 0 and 1, the above formula ensures that the components of _zt_ take values in [0 _,_ 1] so that (10) represents a convex combination at the level of each individual component. Further (11) implies that _zt_ is also determined by _rt−_ 1 and _xt_ . The parameters _Wr_<sup>_z, W z, b_controllingtheformula(11)arealsounknownandtheywillbe</sup> estimated along with all the other parameters of the model.

_zt_ is sometimes referred to as a gate. It controls the closeness of _rt_ to _rt−_ 1 and _r_ ˜ _t_ .

_rt−_ 1 appears in two places in the formula (10): in the term _zt ⊙ rt−_ 1 as well as in the formula (9) for _r_ ˜ _t_ . It might be redundant to have _rt−_ 1 appear in both these places. To address this, GRU modifies (9) by using one more gate as follows:


where _gt_ controls the extent to which _rt−_ 1 is used in the formula for _r_ ˜ _t_ . Similar to (11), the gate _gt_ is specified via


Putting all the formulae together, we get the following specification of the GRU model:


4

_zt_ is called the update gate while _gt_ is called the reset gate. The unknown parameters in this model (which need to be estimated from the data) are _Wr_<sup>_g, W g, bg, W_</sup> _r_<sup>_z, W z, bz, Wr, W, b, β_0</sup><sup>_, β_.</sup>

This is a more sophisticated model compared to the RNN model (6). In fact, (6) is a special case of (13) corresponding to _gt_ = 1 and _zt_ = 0. The presence of the gates _gt_ and _zt_ can alleviate the lack of long memory problem that was an issue with the RNNs.

---

[← 2 Recurrent Neural Network (RNN)](02-2-recurrent-neural-network-rnn.md) · [Up: contents](index.md) · [4 LSTM (Long Short Term Memory) →](04-4-lstm-long-short-term-memory.md)
