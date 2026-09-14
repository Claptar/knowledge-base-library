---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/independentFiltering.png")
```

 ---

Independent filtering has been formalized by [Bourgon *et al.* (2010)](https://www.pnas.org/content/107/21/9546), and the concept can be summarized as follows.

 - For each feature we calculate two statistics, $S_F$ and $S_T$, respectively used for two stages: filtering and testing (e.g., differential expression).
 - In order for a feature to be deemed significant, both of its statistics must be greater than some cut-off.
 - We want to control the type I error rate of the second stage (testing). But note that **the second stage is conditional on the first stage**, as we only test features passing the filter, and basically ignore the fact that filtering was performed. Indeed, one criticism is that computing and correcting the $p$-values as if filtering had not been performed may lead to overoptimistic adjusted $p$-values.
 - [Bourgon *et al.* (2010)](https://www.pnas.org/content/107/21/9546) show that filtering is only appropriate (i.e., does not inflate type I error rate) if the conditional null distribution of test statistics for features passing the filter is the same as the unconditional null distribution. Therefore, **filtering is appropriate if the statistic used for filtering is independent of the statistic used for testing under the null hypothesis**. A good filtering statistic, however, is also informative under the alternative hypothesis. Indeed, a filtering statistic that is independent of the test statistic under both the null- and alternative hypothesis will amount to a random filter, hence deteriorate the quality of the analysis.

```r

---

[← Independent filtering](02-independent-filtering.md) · [Up: contents](index.md) · [All defaults →](04-all-defaults.md)
