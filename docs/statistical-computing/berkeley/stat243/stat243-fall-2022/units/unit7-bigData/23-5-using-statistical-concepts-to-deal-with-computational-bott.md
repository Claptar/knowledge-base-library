---
title: 5. Using statistical concepts to deal with computational bottlenecks
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Using statistical concepts to deal with computational bottlenecks

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

As statisticians, we have a variety of statistical/probabilistic tools
that can aid in dealing with big data.

1.  Usually we take samples because we cannot collect data on the entire
    population. But we can just as well take a sample because we don't
    have the ability to process the data from the entire population. We
    can use standard uncertainty estimates to tell us how close to the
    true quantity we are likely to be. And we can always take a bigger
    sample if we're not happy with the amount of uncertainty.
2.  There are a variety of ideas out there for making use of sampling to
    address big data challenges. One idea (due in part to Prof. Michael
    Jordan here in Statistics/EECS) is to compute estimates on many
    (relatively small) bootstrap samples from the data (cleverly
    creating a reduced-form version of the entire dataset from each
    bootstrap sample) and then combine the estimates across the samples.
    Here's [the arXiv paper](http://arxiv.org/abs/1112.5016) on this
    topic, also published as Kleiner et al. in Journal of the Royal
    Statistical Society (2014) 76:795.
3.  Randomized algorithms: there has been a lot of attention recently to
    algorithms that make use of randomization. E.g., in optimizing a
    likelihood, you might choose the next step in the optimization based
    on random subset of the data rather than the full data. Or in a
    regression context you might choose a subset of rows of the design
    matrix (the matrix of covariates) and corresponding observations,
    weighted based on the statistical leverage ([recall the discussion
    of regression diagnostics in a regression course) of the
    observations. Here's another [arXiv
    paper](http://arxiv.org/abs/1104.5557) that provides some ideas in
    this area.

---

[← 4. Sparsity](22-4-sparsity.md) · [Up: contents](index.md)
