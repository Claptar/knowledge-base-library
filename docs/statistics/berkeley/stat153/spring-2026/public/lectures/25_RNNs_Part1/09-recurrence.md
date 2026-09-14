---
title: Recurrence
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/25_RNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Recurrence

**Source:** [`public/lectures/25_RNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- One efficient way to tackle this is through **recurrence**


<!-- Start of picture text -->
y Output  is a function of the  hidden state<br>yt =  f ( ht )<br>h<br>ht =  g ( xt, ht− 1)<br>x<br>Hidden state  is a function of  input and<br><!-- End of picture text -->

**Hidden state** is a function of **input** _and_ **hidden state from last time point**

---

[← Time Series Prediction](08-time-series-prediction.md) · [Up: contents](index.md) · [Recurrence →](10-recurrence.md)
