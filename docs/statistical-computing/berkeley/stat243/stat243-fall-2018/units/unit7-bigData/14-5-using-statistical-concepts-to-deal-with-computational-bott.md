---
title: 5 Using statistical concepts to deal with computational bottlenecks
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Using statistical concepts to deal with computational bottlenecks

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As statisticians, we have a variety of statistical/probabilistic tools that can aid in dealing with big data.

34

1. Usually we take samples because we cannot collect data on the entire population. But we can just as well take a sample because we don’t have the ability to process the data from the entire population. We can use standard uncertainty estimates to tell us how close to the true quantity we are likely to be. And we can always take a bigger sample if we’re not happy with the amount of uncertainty.

2. There are a variety of ideas out there for making use of sampling to address big data challenges. One idea (due in part to Prof. Michael Jordan here in Statistics/EECS) is to compute estimates on many (relatively small) bootstrap samples from the data (cleverly creating a reduced-form version of the entire dataset from each bootstrap sample) and then combine the estimates across the samples. Here’s the arXiv paper on this topic, also published as Kleiner et al. in Journal of the Royal Statistical Society (2014) 76:795.

3. Randomized algorithms: there has been a lot of attention recently to algorithms that make use of randomization. E.g., in optimizing a likelihood, you might choose the next step in the optimization based on random subset of the data rather than the full data. Or in a regression context you might choose a subset of rows of the design matrix (the matrix of covariates) and corresponding observations, weighted based on the statistical leverage [recall the discussion of regression diagnostics in a regression course] of the observations. Here’s another arXiv paper that provides some ideas in this area.

---

[← 4 Sparsity](13-4-sparsity.md) · [Up: contents](index.md) · [6 Hadoop, MapReduce, and Spark →](15-6-hadoop-mapreduce-and-spark.md)
