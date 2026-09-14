---
title: 'Simulation 1: the performance of the t -test'
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Simulation 1: the performance of the t -test

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We will start with a simulation study to examine the coverage of the lowly one-sample _t_ -test. _Coverage_ is the chance of a confidence interval capturing the true parameter value. Let’s first look at our test on some fake data:

```
#makefakedata
dat=rnorm(10,mean=3,sd=1)
#conductthetest
tt=t.test(dat)
tt
```

```

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [OneSamplet-test →](03-onesamplet-test.md)
