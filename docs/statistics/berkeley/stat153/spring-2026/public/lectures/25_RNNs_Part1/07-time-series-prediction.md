---
title: Time Series Prediction
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/25_RNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Time Series Prediction

**Source:** [`public/lectures/25_RNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_yt_ = _f_ ( _xt_ , _xt_ −1, _xt_ −2, …)

- If you think there’s a fixed time horizon (e.g. you only need to look back 20 days), you could try building a standard feedforward model

   - This would involve stacking 21 { _xt_ −20, …, _xt_ −1, _xt_ } vectors together into a single “input” vector

   - <sup>Explosion of weights! If each  is length</sup> _xt n_ , you would need 21*n weights in the first layer. If _n_ is big, this is a disaster.


<!-- Start of picture text -->
…<br>xt −20 xt −19 xt −1 xt<br>length n length n length n length n length n<br>Concatenated input vector<br>length 21n<br>21 n  ×  m<br>… weights<br>h 1 h 2 h 3 hm<br>m  weights<br>yt ̂<br><!-- End of picture text -->

---

[← Time Series Prediction](06-time-series-prediction.md) · [Up: contents](index.md) · [Time Series Prediction →](08-time-series-prediction.md)
