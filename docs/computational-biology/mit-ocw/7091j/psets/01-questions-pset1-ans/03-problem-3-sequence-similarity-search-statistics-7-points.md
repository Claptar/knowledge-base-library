---
title: Problem 3. Sequence similarity search statistics (7 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/01-questions-pset1-ans.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/01-questions-pset1-ans.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Problem 3. Sequence similarity search statistics (7 points)

You are conducting local nucleotide sequence alignments with your favorite local alignment tool (e.g. BLAST) with match and mismatch scores of +1 and -1 respectively. You align a 100bp query sequence to a 1Mbp genome and find that a 20-nt subsequence from your query is a perfect match.

For each of the following cases, calculate the significance of a 20-nt perfect match (assume $K = 1$ in each case):

Note: The Gumbel distribution is continuous, so the P-value for a score $x$, $P(S \ge x)$, is equal to the formula $P(S > x)$ on the lecture slides for continuous $x$ since a single point $P(S = x)$ has no probability mass. However, we are applying this continuous distribution to a scoring system that only takes on discrete values, so the $P(S = x)$ values in our scoring system have nonzero mass (a reasonable value for $P(S = x)$ would be $\text{CDF}(x+1) - \text{CDF}(x)$, where CDF is the cumulative distribution function given on the lecture slides). Thus, our intention was that the P-value is $P(S \ge 20) = P(S > 19)$, so 19 would be plugged into the Gumbel CDF formula; however, since the lecture slides and the textbook have different wording regarding $P(S \ge x)$ vs. $P(S > x)$, we will accept P-values with either 19 or 20 used in the Gumbel formula.

**(A) (2 pts.)** Query sequence and genome both have approximately balanced base composition A=C=G=T=25%).

Since every pair of nucleotides occurs with equal probability, the probability of a match (A/A, T/T C/C or G/G) is 1/4, and the probability of a mismatch is therefore 3/4. So to find $\lambda$, we need to solve $\frac{1}{4}e^{\lambda} + \frac{3}{4}e^{-\lambda} = 1$, which has solutions $\lambda = 0$ or $\ln(3)$ (by substituting in $y = e^{\lambda}$). Since $\lambda$ must be positive, we use $\lambda = \ln(3)$. The score for the perfect 20nt match is $x=20$, so using the distribution of the scores $P(S > x) = 1 - \exp[-KMN e^{-\lambda x}]$, we obtain the P-value:

$$P(S \ge 20) = P(S > 19) = 1 - \exp[-(100)(1000000)e^{-19\ln(3)}] = 0.0824.$$
$$(0.0283\text{ for }x = 20)$$

**(B) (1 pt.)** Query sequence and genome are both highly A-T rich (A=T=40%, C=G=10%).

A/A and T/T matches occur with probability 16/100 while C/C and G/G matches occur with probability 1/100. There are also two mismatches each with probability 16/100 (A/T and T/A) and two with probability 1/100 (C/G and G/C). The remaining 8 pairs are all mismatches with probability 4/100. Overall, the total probability of a match is 34/100 and probability of a mismatch is 66/100. We need to solve $(0.34)e^{\lambda} + (0.66)e^{-\lambda} = 1$, which has nonzero solution $\lambda = 0.6633$. The corresponding P-value is:

$$P(S \ge 20) = P(S > 19) = 1 - \exp[-(100)(1000000)e^{-19(0.6633)}] \approx 1.$$
$$(\text{also }\approx 1\text{ for }x = 20)$$

**(C) (1 pt.)** Query is moderately A+T-rich (A = T = 30%, C = G = 20%) but genome is moderately C+G-rich (A = T = 20%, C = G = 30%).

In this case, all matches are equiprobable with probability $(0.3)(0.2) = 0.06$. Therefore the probability of a match is $4(0.06) = 0.24$, and the probability of a mismatch is $1 - 0.24 = 0.76$. Solving \$(0.24)e^{\lambda} + (0.76)e

---

[← Problem 2. Gapped sequence alignment (6 points)](02-problem-2-gapped-sequence-alignment-6-points.md) · [Up: contents](index.md)
