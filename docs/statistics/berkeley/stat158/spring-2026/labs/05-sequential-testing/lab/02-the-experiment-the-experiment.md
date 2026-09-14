---
title: The Experiment {#the-experiment}
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/05-sequential-testing/lab.tex
source_file: sources/berkeley-stat158/spring-2026/labs/05-sequential-testing/lab.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# The Experiment {#the-experiment}

**Source:** [`labs/05-sequential-testing/lab.tex`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/05-sequential-testing/lab.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

We first look at a recent [case study](https://netflixtechblog.com/sequential-a-b-testing-keeps-the-world-streaming-netflix-part-1-continuous-data-cba6c7ed49df) by Netflix from 2024 that uses sequential testing for “canary testing”. It selectively rolls out a new software version to try and identify bugs and whether play-delay increases in the update. Read through the blog post, trying to understand the setting and the role of sequential testing here. Also try to interpret their graphs and their analysis and other results.
Answer the following questions in full sentences.

1.  Identify the treatment and control here. Why do you think these are also called A/B tests?

<!-- -->

1.  What is the reason behind choosing a sequential test over classical fixed-n tests in this particular setting? Give an example of another, non-software setting where sequential testing may be similarly appropriate.

<!-- -->

1.  Recall the statistical problems with “Peeking”. Do you think the multiple testing corrections (such as Bonferroni) help correct for this? What would the Bonferroni correction be (p = 0.05) for peeking after each of a 100 data points?

<!-- -->

1.  Give an example of a Null and Alternate Hypothesis that may be applicable to the Netflix study. Interpret the results from the case study.

<!-- -->

1.  Recall the definitions of $\alpha$ and $\beta$, w.r.t Type-I and Type-II errors. Which do you think would be higher here?

---

[← Introduction {#introduction}](01-introduction-introduction.md) · [Up: contents](index.md) · [Conducting Your Own Experiment {#conducting-your-own-experiment} →](03-conducting-your-own-experiment-conducting-your-own-experimen.md)
