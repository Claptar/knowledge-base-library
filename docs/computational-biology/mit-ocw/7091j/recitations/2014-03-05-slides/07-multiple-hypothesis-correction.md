---
title: Multiple Hypothesis Correction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Multiple Hypothesis Correction

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<u>Common corrections:</u>

- **Bonferroni** : Divide desired P-value cutoff by # of hypotheses

   - Conservative correction, lowers P-value more than necessary and may produce more false negatives than desired

   - example: if for a single test you would reject if p-value ≤ 0.05, and you're running 100 tests, reject those individually if p-value ≤ 0.05/100 = 0.0005

      - the probability that your 100 tests include at least one false positive due to chance is 0.05

- **Benjamini-Hochberg** (less conservative):


_Rank:_ Rank of event in list list of p-values, from most significant (rank = 1) to least (rank = Count)

- The Q-value is the False Discovery Rate (FDR) analog of the P-value

- Choose a FDR that you’re willing to tolerate (e.g. 0.05 – an expected 5% of times you reject the null will be false positives)

   - Then accept events as significant (i.e., reject the null hypothesis) for events of rank 1 through all those for which the Q-value is less than the desired FDR

   - Extra 6.874 problem on Pset2 – see answer key when released.

17

## Irreproducible Discovery Rate (IDR)

- For two replicates of an experiment, how do we choose which events are reproducible between the two replicates?

   - In each of the replicates, order the events by their significance (p-value)

   - The idea is that a reproducible event should have approximately the same rank in the two events – the most significant effect should have rank 1 in both replicates, etc.

18

## Irreproducible Discovery Rate (IDR)

- Two replicates: X and Y, each of which has _n_ events ranked by significance

   - Let _t_ vary from 0 to 1 (the proportion of the n total events we’re considering, starting with the most significant).

   - Ψn(t) = the fraction the _n_ events that are in the top (n*t) events of both replicates.


- Note that Ψn(t) = (n*t) / n = t if the top _t_ of the events are the same in both of the replicates

- Ψn(t) < t if some events are in the top _t_ of one of the replicates but not of the other

- Derivative Ψ’ n(t) = 1; these events are “reproducible”

- Ψ’ n(t) drops to below 1 beginning at the irreproducible events

19

---

[← Multiple Hypothesis Correction](06-multiple-hypothesis-correction.md) · [Up: contents](index.md) · [RNA-Seq Analysis →](08-rna-seq-analysis.md)
