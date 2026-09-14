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


Following the new measure of split, we grow the primary tree in `rpart` :

---

[← Missing covariates in the training data](06-missing-covariates-in-the-training-data.md) · [Up: contents](index.md) · [Missing covariates in the testing data →](08-missing-covariates-in-the-testing-data.md)
