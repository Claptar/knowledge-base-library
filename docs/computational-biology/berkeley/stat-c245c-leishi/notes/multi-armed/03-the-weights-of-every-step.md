---
title: the weights of every step
source: https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd
source_file: sources/berkeley-stat-c245c-leishi/notes/multi-armed.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# the weights of every step

**Source:** [`notes/multi-armed.Rmd`](https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

output
```

As we can see, even from the 5th step the algorithm started to assign more weight to the variant 4 and almost nothing to the variant 1 and variant 2.


### Compared with a classical strategy: A/B test

In an A/B test, the customer base is divided into two or more groups, each of which is served a different version of whatever is being tested (such as a special offer, or the layout of an advertising campaign). At the end of the test, whichever variant was most successful is pursued for the customer base at large.

The following example is taken from https://www.r-bloggers.com/2019/09/multi-armed-bandits-as-an-a-b-testing-solution/.

To illustrate, let’s use a simplified example to compare a more traditional A/B test to Epsilon Greedy and Thompson Sampling. In this scenario, a customer can be shown one of five variants of an advertisement. For our purposes, we will assume that Ad 1 performs the worst, with a 5% conversion rate. Each ad performs 5% better than the last, with the best performer being Ad 5, at 25% conversion. We’ll do 1,000 trials, which means that in an idealized, hypothetical world, the number of conversions we could get by only showing the optimal ad would be 250 (given a 25% conversion rate over 1,000 trials).


```r

---

[← for bandit](02-for-bandit.md) · [Up: contents](index.md) · [A/B TEST →](04-a-b-test.md)
