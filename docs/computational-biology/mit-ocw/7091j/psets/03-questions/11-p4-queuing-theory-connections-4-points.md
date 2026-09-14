---
title: P4. Queuing theory/connections (4 points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# P4. Queuing theory/connections (4 points).

**Source:** `psets/03-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A small bank hires a management consultant to figure out if they can afford to advertise free checking for one year (a $150 value) to any customer who has to wait in line more than 15 minutes.  The consultant observes that, each minute that the bank is open, the waiting line gets longer by one customer with probability ¼, and – if there is a line – the line gets shorter by one customer (because a customer is served by a teller) with probability ¾.  Let _X_ be the probability that the line never gets longer than 10 people in a 12-week period (this is a reference case, whose empirical frequency is known to the bank), and let _Y_ be the probability that the line never gets longer than 15 people in a 12-week period (the proposed duration of the promotion). The bank is open 2400 minutes every week.

!"  (!) Use an equation that was covered in class to calculate . !"  (!)

This scenario is analogous to finding local alignment of unrelated sequences of uniform composition, in which we expect a match with probability ¼ and a mismatch with probability ¾. That the bank line cannot go below 0 people is equivalent to resetting the local alignment score to 0 if the score becomes negative. The bank line getting longer by 1 and shorter by 1 corresponds to a match score of +1 and a mismatch score of -1, respectively.

In the Gumbel distribution for BLAST statistics, MN=(length of database)(length of query) is the total size of the search space because in local alignment you consider starting a match at every position in the database vs. every position in the query. In the bank scenario, the “high scoring” run of the line increasing to over 10 or 15 people could begin at any minute, so the search spaces (=MN in the Gumbel distribution) are each (12 weeks*2400 minutes), respectively.

Recall that λ is the unique positive solution to:

! ! ! !! e + e = 1, which corresponds to λ = ln(3) (Problem Set 1, Q3(a)). ! !

As indicated in the BLAST tutorial, K and λ can be thought of simply as natural scales for the search space size and the scoring system, respectively; because the search space and scoring system are the same for _X_ and _Y_ , K will cancel out (see below).

In local alignment, the P-value is the probability that we achieve a score at least x or greater; here were are interested in the complement of that, the probability that the score (length of the line) never reaches above x: (1-Gumbel Distribution) = exp[-KMNe<sup>-λx</sup> ].


16

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology

Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← P3. Protein structure with PyRosetta (6 points).](10-p3-protein-structure-with-pyrosetta-6-points.md) · [Up: contents](index.md)
