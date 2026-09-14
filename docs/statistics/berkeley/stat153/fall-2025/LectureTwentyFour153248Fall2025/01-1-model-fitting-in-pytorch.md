---
title: 1 Model Fitting in PyTorch
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyFour153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Model Fitting in PyTorch

**Source:** [`LectureTwentyFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyFour153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Model fitting in `PyTorch` is usually based on the following steps:

1. Create model and define the parameters (which need to be estimated based on the data)

2. Define the loss function

3. Specify initial values of the parameters

4. Use of an optimization algorithm (some variant of gradient descent such as `Adam` ). This algorithm has two steps:

   - a) Compute gradient of the loss function with respect to the parameters ( `PyTorch` performs gradient calculations using reverse-mode automatic differentiation via `backward` )

   - b) Update parameters based on the gradient. The update rule depends on the specific optimization algorithm being used and requires choosing a tuning parameter known as the **learning rate** . If the learning rate is too small, convergence will be very slow; if it is too large, the algorithm may oscillate or fail to converge.

As stepping stones for RNNs, let us first review some more basic models that we already studied in the course.

---

[Up: contents](index.md) · [2 Regression with t as covariate →](02-2-regression-with-t-as-covariate.md)
