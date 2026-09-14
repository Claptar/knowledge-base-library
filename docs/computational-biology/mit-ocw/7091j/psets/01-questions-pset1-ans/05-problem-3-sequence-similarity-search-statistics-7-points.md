---
title: Problem 3. Sequence similarity search statistics (7 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/01-questions-pset1-ans.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 3. Sequence similarity search statistics (7 points)

**Source:** `psets/01-questions-pset1-ans.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<mark>You are conducting local nucleotide sequence alignments with your favorite local alignment tool (e.g. BLAST) with match and mismatch scores of +1 and -1 respectively.  You align a 100bp query sequence to a 1Mbp genome and find that a 20-nt subsequence from your query is a perfect match.</mark>

<mark>For each of the following cases, calculate the significance of a 20-nt perfect match (assume</mark> _<mark>K</mark>_ <mark>= 1 in each case):</mark>

Note: The Gumbel distribution is continuous, so the P-value for a score _x_ , P(S ≥ x), is equal to the formula P(S > x) on the lecture slides for continuous _x_ since a single point P(S = _x_ ) has no probability mass. However, we are applying this continuous distribution to a scoring system that only takes on discrete values, so the P(S = _x_ ) values in our scoring system have nonzero mass (a reasonable value for P(S = _x_ ) would be CDF( _x_ +1) – CDF( _x_ ), where CDF is the cumulative distribution function given on the lecture slides). Thus, our intention was that the P-value is P(S ≥ 20) = P(S > 19), so 19 would be plugged into the Gumbel CDF formula; however, since the lecture slides and the textbook have different wording regarding P(S ≥ x) vs. P(S > x), we will accept P-values with either 19 or 20 used in the Gumbel formula. **<mark>(A) (</mark> 2 pts.)** <mark>Query sequence and genome both have approximately balanced base composition A=C=G=T=25%).</mark>

<mark>Since every pair of nucleotides occurs with equal probability, the probability of a match (A/A, T/T C/C or G/G) is ¼, and the probability of a mismatch is therefore ¾.  So to find λ, we need to</mark> solve ! e! + ! e!! = 1, which has solutions λ = 0 or _ln_ (3) (by substituting in y = e!).  Since λ ! ! <mark>must be positive, we use λ=</mark> _<mark>ln</mark>_ <mark>(3). The score for the perfect 20nt match is</mark> _<mark>x</mark>_ <mark>=20, so using the distribution of the scores P(S > x) = 1 - exp[-KMNe</mark> !!! <mark>], we obtain the P-value:</mark>


**(B) (1 pt.)** <mark>Query sequence and genome are both</mark> highly A-T rich (A=T=40%, C=G=10%).

<mark>A/A and T/T matches occur with probability 16/100 while C/C and G/G matches occur with probability 1/100. There are also two mismatches each with probability 16/100 (A/T and T/A) and two with probability 1/100 (C/G and G/C). The remaining 8 pairs are all mismatches with probability 4/100. Overall, the total probability of a match is 34/100 and probability of a mismatch is 66/100.   We need to solve (0.34) e</mark> ! <mark>+ (0.66)e</mark> !! <mark>= 1, which has nonzero solution λ = 0.6633.  The corresponding P-value is:</mark>


8

**<mark>(C)</mark> (1 pt.)** <mark>Query is moderately</mark> **<mark>A+T</mark>** <mark>-rich (A = T = 30%, C = G = 20%) but genome is moderately</mark> **<mark>C+G</mark>** <mark>-rich (A = T = 20%, C = G = 30%).</mark>

<mark>In this case, all matches are equiprobable with probability (0.3)(0.2) = 0.06.  Therefore the probability of a match is 4(0.06) = 0.24, and the probability of a mismatch is 1-0.24 = 0.76. Solving  (0.24)e</mark> ! <mark>+ (0.76)e</mark> !! <mark>= 1, we obtain nonzero solution λ = 1.153, and the P-value is:</mark>


**<mark>(D) (</mark> 1 pt.)** <mark>Briefly explain why the ordering of the P-values from (A) - (C) makes sense.</mark>

<mark>Since in (B) we are searching a highly A-T rich query against a highly A-T rich genome, we expect to see more similarity between the query and the genome by chance than in (A). Therefore, the match becomes much less significant than in (A). When the query is A-T rich and the genome is G-C rich as in (C), however, a match becomes less likely than if both query and genome had equiprobable base compositions as in (A), and so the P-value in (C) is smaller than in (A).</mark>

9

**<mark>(E)</mark> (2 pts.)** <mark>Design a new scoring system for application to searching a 20 nt query of unbiased composition against a highly A+T-rich genome (as in (B) above) that will increase the sensitivity for detection of matches to that genome by drawing lines from each box on the left to its new score in the right box (+1, 0, or -1 for different types of matches/mismatches). What would the P- value of a perfect match to this query (with 5 A’s, 5 C’s, 5 G’s, 5 T’s) be using your new scoring system?</mark>


Since C/C and G/G matches are unlikely by chance due to their low genome content, observing these matches provides the most evidence of a true alignment; they should therefore be given a score of +1. In contrast, because A/A and T/T matches will occur fairly often simply by chance due to their high genome content, these matches provide less evidence of a true alignment and should be given a score of 0. Mismatches generally provide evidence against a true alignment, so they should be given a score of -1.

With a query of unbiased content (A=C=G=T=25%) against the biased genome (A=T=40%, C=G=10%), there is 0.05 total probability of C/C or G/G match (score = +1), 0.2 probability of A/A or T/T match (score = 0), and 0.75 probability of a mismatch (score = -1). The equation ! ! !" !" !! e + + e = 1 leads to λ = 2.7081. !"" !"" !""

<mark>For a perfectly matched 20 nt query of unbiased</mark> content, there will be 10 matches of score +1 (C/C and G/G) and 10 matches of score 0 (A/A and T/T), for an overall score of +10. The P- value is therefore:


10

MIT OpenCourseWare http://ocw.mit.edu

7.91J  / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology

Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Problem 2. Gapped sequence alignment ( 6 points)](04-problem-2-gapped-sequence-alignment-6-points.md) · [Up: contents](index.md)
