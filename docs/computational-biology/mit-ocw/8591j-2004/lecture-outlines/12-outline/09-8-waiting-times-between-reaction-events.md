---
title: 8. Waiting times between reaction events
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8. Waiting times between reaction events

**Source:** `lecture-outlines/12-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose a chemical reaction occurs with rate _r_ . What is the time interval between successive occurrences of the reaction? The probability that the reaction occurs in some time interval _dt_ is _rdt_ ; the probability that it does not occur is therefore 1 – _rdt_ . The probability that it occurs only after some time τ can be calculated as follows:


But


Setting _Q_ (τ ) = ℘ (does not occur for _t_ < τ ), this implies ln( _Q_ (τ ))-ln( _Q_ (τ - _d_ τ )) = ln(1- _rd_ τ ) ≈ - _rd_ τ . Therefore,


where we have used _Q_ (0) = 1. Inserting this in Eq. 17, we get


The waiting times between successive reactions are therefore exponentially distributed, with mean value 2 τ = 1/ _r_ , and variance δτ = 1/ _r_ .

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

---

[← 7. Steady state of a bistable system](08-7-steady-state-of-a-bistable-system.md) · [Up: contents](index.md) · [9. Stochastic simulation of chemical reactions →](10-9-stochastic-simulation-of-chemical-reactions.md)
