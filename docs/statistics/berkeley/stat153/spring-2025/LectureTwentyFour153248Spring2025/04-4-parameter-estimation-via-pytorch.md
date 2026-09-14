---
title: 4 Parameter Estimation via PyTorch
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFour153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Parameter Estimation via PyTorch

**Source:** [`LectureTwentyFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFour153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Given a time series dataset _y_ 1 _, . . . , yn_ , we estimate the parameters of these models simply by least squares. Specifically the parameters are estimated by minimizing:


Note that _µt_ depends on the parameters _W, Wr . . ._ so that these parameters need to be chosen so that the sum of squares above is as small as possible. Minimization of (10) is done in an iterative fashion using a simple algorithm such as gradient descent. This requires calculation of gradients which is done efficiently in PyTorch. This also requires an initial value of the parameters.

---

[← 3 Recurrent Neural Networks (RNNs)](03-3-recurrent-neural-networks-rnns.md) · [Up: contents](index.md) · [5 Additional Optional Reading →](05-5-additional-optional-reading.md)
