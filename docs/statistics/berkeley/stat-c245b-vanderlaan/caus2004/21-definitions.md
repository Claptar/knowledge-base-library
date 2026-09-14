---
title: Definitions
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Definitions

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In a point treatment study, the observed data for each of n subjects is O = (W, A, Y ), where W is a vector of baseline covariates, A is the treatment received, and Y is the outcome. It is assumed that W is measured before A is measured before Y .

Let A be the set of possible treatments in a study and W the set of possible values for W . Then a **dynamic treatment regime** is a function d : W →A. That is, a dynamic treatment regime is a rule or algorithm for assigning treatment based on baseline values. We use D to denote the set of dynamic treatment regimes of interest for a particular study.

This is in contrast to the **static treatment regimes** we have previously considered, in which a given treatment is assigned to all study participants, irrespective of their baseline values; e.g., assigning everyone to a study’s control treatment is a static regime. In previous lectures, when we were trying to estimate E[Y1 − Y0], we were estimating the average difference in the outcome from the static regime that assigns everyone to the active treatment with the outcome from the static regime that assigns everyone to the control treatment. Each treatment in A can thus be associated with the static regime that assigns that treatment to everyone, so A can also be used to denote the set of static treatment regimes. Note that "officially" a static treatment regime is also a (degenerate) dynamic regime, since it is a constant function from W to A.

14

The parameters of interest that we wish to estimate, which reflect the usefulness of the dynamic regimes under consideration, are

---

[← Cohort of children with asthma](20-cohort-of-children-with-asthma.md) · [Up: contents](index.md) · [(E[Yd|V ] : d ∈D, V ⊆ W ). →](22-e-yd-v-d-d-v-w.md)
