---
title: Elements of a CNN
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/24_CNNs_Part2.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Elements of a CNN

**Source:** [`public/lectures/24_CNNs_Part2.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Input layer

   5. Flattening

2. Convolutional layer

   6. Fully connected (dense) layer

3. Activation layer (introduces nonlinearity)

   7. Output layer

4. Pooling layer

#### **Example convolution operations (from last time)**


<!-- Start of picture text -->
Output Output<br>Y  ∈ℝ 3×3 Y  ∈ℝ 5×5<br>Kernel<br>K  ∈ℝ 3×3<br>Kernel<br>K  ∈ℝ 3×3<br>Input X  ∈ℝ 5×5 Input X  ∈ℝ 5×5<br>padding, stride=2 “same” padding, stride=1<br><!-- End of picture text -->

---

[← STRF and time lagged regression as convolution](03-strf-and-time-lagged-regression-as-convolution.md) · [Up: contents](index.md) · [Combining multiple filters →](05-combining-multiple-filters.md)
