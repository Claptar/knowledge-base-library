---
title: Missing covariates in the training data
source: https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/PH240C-Lab02.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Missing covariates in the training data

**Source:** [`notes/PH240C-Lab02.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- When we have missing covariates in the training data, we need to adjust the impurity measure;

- The impurity measures (either Gini index or Entrooy) are calculated only over the observations which are not missing a particular predictor.

- To weight the calculated impurity measures, the weighting probabilities are also calculated only over the non-missing observations.

- Problems? Issues with this construction? Can you identify a case that this construction is flawed? Hint: What happens if one variable has only two observations which are not missing? (Homework question)

---

[← What if we have some missing values in the covariates?](05-what-if-we-have-some-missing-values-in-the-covariates.md) · [Up: contents](index.md) · [What if we have some missing values in the covariates? →](07-what-if-we-have-some-missing-values-in-the-covariates.md)
