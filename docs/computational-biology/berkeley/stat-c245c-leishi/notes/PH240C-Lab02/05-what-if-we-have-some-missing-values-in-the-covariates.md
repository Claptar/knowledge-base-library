---
title: What if we have some missing values in the covariates?
source: https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/PH240C-Lab02.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# What if we have some missing values in the covariates?

**Source:** [`notes/PH240C-Lab02.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

|Subject|_Y_|Weight|Height|
|---|---|---|---|
|1|1|10|10|
|2|1|9|9|
|3|1|NA|8|
|4|1|7|7|
|5|1|6|5|
|6|0|5|6|
|7|0|4|4|
|8|0|3|3|
|9|0|2|2|
|10|0|1|1|


If _R_ 1 = _{_ 1 _,_ 2 _,_ 3 _, . . . ,_ 7 _}_ and _R_ 2 = _{_ 8 _,_ 9 _,_ 10 _}_ ,

▶ Without missing value, we calculate the split impurity measure as:


▶ With missing value, we calculate the split impurity measure as:


The region without missing values receives **higher** weight.

---

[← What if we have some missing values in the response?](04-what-if-we-have-some-missing-values-in-the-response.md) · [Up: contents](index.md) · [Missing covariates in the training data →](06-missing-covariates-in-the-training-data.md)
