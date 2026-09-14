---
title: (4) Experimental treatment assignment assumption (ETA)
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (4) Experimental treatment assignment assumption (ETA)

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let A<sup>∗</sup> (t|A<sup>¯</sup> (t − 1)) denote the set of all marginally possible treatment assignments at time point t, i.e. the set of all a<sup>∗</sup> (t) such ( A<sup>¯</sup> (t − 1), a<sup>∗</sup> (t)) is a possible treatment regime according to our data generating mechanism. Then we require that


Thus we do not allow treatment assignment rules that, based on a subject’s history, give zero probability to certain treatment options that we would consider otherwise reasonable.

Example 4: When we show in example 2 that E[Y |A = a, W = w] = E[Ya|W = w], we need to assume that P (A = a, W = w) > 0. Otherwise, the conditional expectation E(Y | A = a, W ) on the left is undefined. Since we wont have any data of the form (Y, A = a, W = w), estimation (even when it would be defined) E[Y |A = a, W = w] is not non-parametrically possible. If we estimate E(Y | A, W ) according to a parametric regression model, then this fit will give us an estimate of E(Ya∗|W ) = E(Y | A = a∗, W ) for all (a<sup>∗</sup> , W ) for which P (A = a<sup>∗</sup> , W ) has positive probability. We can extrapolate this regression model to the data point (A = a, W = w) and hope that it will give us an approximation of E[Ya|W ].

---

[← (3) Sequential randomization assumption (SRA)](12-3-sequential-randomization-assumption-sra.md) · [Up: contents](index.md) · [The G-computation formula →](14-the-g-computation-formula.md)
