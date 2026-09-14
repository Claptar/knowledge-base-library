---
title: 2 Classification of conserved regions
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Classification of conserved regions

**Source:** `psets/02-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, we will use simulation to study the problem of classifying conserved sequence fragments given multiple alignments of four species. Submit all code you write.

- (a) To simplify our classification problem, we will consider _alignment scores_ at each position. We define the alignment score of a column of a multiple alignment to be the number of unique pairs that share the same symbol. An example multiple alignment and the score for each column is given below:

```
GACTA
TACTA
AGTTA
CTTAA
01236
```

Consider two models C for conserved regions and N for unconserved regions. Assuming the alignment score at every position is independent, the conditional probability of observing a particular score in a column given each model is tabulated below:

|Score|N|C|
|---|---|---|
|0|0.1|0.05|
|1|0.35|0.15|
|2|0.25|0.2|
|3|0.2|0.3|
|6|0.1|0.3|


Compute the conditional probabilities of observing each of the following alignments given each of the models:

|`ACGACGACTA`<br>`CAGACGCTGA`|
|---|
|`TTCCTCTGAT`|
|`AGATGTGACT`|
|`ACAACGAGTA`|
|`AAAACGAATA`|
|`TCATCGAGTT`<br>`ACATCTAACT`|


- (b) Simulate 10,000 sequences S of alignment scores of length 10 from N. How often is P(S | C) > P(S | N)?

- (c) Simulate 10,000 sequences S of alignment scores of length 10 from C. How often is P(S | N) > P(S | C)?

- (d) How could we reduce the rate of classification errors on these short fragments? What about for much longer sequences?

---

[← 1 Naive Bayes Classification](02-1-naive-bayes-classification.md) · [Up: contents](index.md) · [3 K-means clustering →](04-3-k-means-clustering.md)
