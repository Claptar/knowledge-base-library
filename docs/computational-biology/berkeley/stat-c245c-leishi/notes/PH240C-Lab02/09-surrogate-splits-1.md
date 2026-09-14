---
title: Surrogate Splits (1)
source: https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/PH240C-Lab02.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Surrogate Splits (1)

**Source:** [`notes/PH240C-Lab02.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Decision trees can handle missing values without imputation;

- When an observation is missing, _primary tree_ cannot make a decision.

- What if we pretend this variable is just not there?

   **1.** As when the variable is missing, we cannot split based on this variable either;

   **2.** Instead, we want to find a _replacement split_ by using other variables.

- Ideally, we want the replacement split to be similar to the primary split;

- If a case with a missing variable used in a _primary split_ has to be predicted, a surrogate split is used instead.

---

[← Missing covariates in the testing data](08-missing-covariates-in-the-testing-data.md) · [Up: contents](index.md) · [Surrogate Splits (2) →](10-surrogate-splits-2.md)
