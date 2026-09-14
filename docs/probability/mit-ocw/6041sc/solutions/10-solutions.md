---
title: 10 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/10-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 solutions

**Source:** `solutions/10-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Problem Set 10 Solutions

1. A financial parable.

   - (a) The bank becomes insolvent if the asset’s gain R ≤−5 (i.e., it loses more than 5%). This probability is the CDF of R evaluated at −5. Since R is normally distributed, we can convert this CDF to be in terms of a standard normal random variable by subtracting away the mean and dividing by the standard deviation, and then look up the value in a standard normal CDF table.


Thus, by investing in just this one asset, the bank has a 11.5% chance of becoming insolvent.

(b) If we model the Ri’s as independent normal random variables, then their sum R = (R1 + · · · + R20)/20 is also a normal random variable (see Example 4.11 on page 214 of the text). Thus, we can calculate the mean and variance of this new R and proceed as in part (a). Note that since the random variables are assumed to be independent, the variance of their sum is just the sum of their individual variances.


Thus, by diversifying and assuming that the 20 assets have independent gains, the bank has seemingly decreased its probability of becoming insolvent to a palatable value.

- (c) Now, if the gains Ri are positively correlated, then we can no longer sum up the individual variances; we need to account for the covariance between pairs of random variables. The covariance is given by

From page 220 in the text, we know that the variance in this case is

Since we assume that R = (R1 + · · · + R20)/20 is still normal, we can again apply the same steps as in parts (a) and (b):

Page 1 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Thus, by taking into account the positive correlation between the assets’ gains, we are no longer as comfortable with the probability of insolvency as we thought we were in part (b).

2. Let M and N be the number of males and females, respectively, that cast a vote. We need to find P (M > N ), i.e., P (M − N > 0). The central limit theorem does not apply directly to the random variable M − N . However, the central limit theorem implies that M and N are well approximated by normal random variables. So, M − N is the difference of two independent approximately normal random variables. Since the difference of two normal random variables is itself normal, it follows that M − N is approximately normal. The mean and variance of M − N are found by


Thus, the standard deviation of M − N is 11. Let Z be a standard normal random variable. Using the central limit theorem approximation, we obtain


A slightly more refined estimate is obtained by expressing the event of interest as P(M − N ≥ 1/2). We then have


3. (a) Using the Central Limit Theorem, we obtain P(<sup><u>n</u></sup> 2<sup>−10≤Sn≤</sup><sup><u>n</u></sup> 2<sup>+10)≈Φ(</sup><sup>~~√~~</sup><sup><u>20</u></sup> <u>n</u><sup>)−Φ(−</sup><sup>~~√~~</sup><sup><u>20</u></sup> <u>n</u><sup>) →</sup> 0 as n →∞.

   - (b) The limit is 1, by the weak law of large numbers.

   - (c) Using the Central Limit Theorem, we obtain P(<sup><u>n</u></sup> 2<sup>−</sup> <u>√2n</u> ≤ Sn ≤ <u>n2</u><sup>+</sup> <u>√2n</u> ) → Φ(1) − Φ(−1) = 0.6826.

4. (a) Let C denote the coin that Bob received, so that C = 1 if Bob received the first coin, and C = 2 if Bob received the second coin. Then P(C = 1) = p and P(C = 2) = 1 − p. Given C, the number of heads Y in 3 independent tosses is a binomial random variable. We can find the probability that Bob received the first coin given that he observed k heads using Bayes’ rule.

Page 2 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


- (b) We want to find k so that the following inequality holds.


Note that if p = 0 or p = 1, there is no value of k that satisfies the inequality. We now solve it for 0 < p < 1:


For 0 < p < 1, k = 0 or k = 1 the probability that Alice sent the first coin increases. The inequality does not depend on p, and so does not change when p increases. Intuitively, this makes sense: lower values of k increase Bob’s belief he got the coin with lower probability of heads.

- (c) Given that Bob observes k heads, Bob must decide on whether the first or second coin was used. To minimize the error, he should decide it is the first coin when P(C = 1 | Y = k) ≥ P(C = 2 | Y = k). Thus, we have the decision rule given by


Page 3 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

- 3+log2 2

- (d) i. If p = 2/3, the threshold in the rule above is equal to 2 = 2. Therefore, Bob will decide that he received the first coin when he observes 0, 1 or 2 heads, and will decide that he received the second coin when he observes 3 heads. We find the probability of a correct decision using the total probability law:


- ii. In absence of any data, all Bob can do is decide he received the first coin with some probability q. Note that this rule includes the deterministic decisions that he received either the first coin (q = 1) or the second coin (q = 0).

In this case, the probability of correct decision is equal to


Clearly, the probability of the correct decision is maximized (or the probability of error is minimized) when q = 1, i.e., when Bob deterministically decides he received the first coin. In this case, P(Correct) = 2/3 ≈ .667. Observing 3 coin tosses increases the probability of the correct decision by 2/27 ≈ .074.

- (e) If p is increased, the threshold in the decision rule in part (c) goes up, i.e., the range of values of k for which Bob decides he received the first coin can only go up.

- (f) Bob will never decide he received the first coin if the threshold in the rule above is below zero:


If p < 1/9, the prior probability of receiving the first coin is so low that no amount of evidence from 3 tosses of the coin will make Bob decide he received the first coin.

- (g) Bob will always decide he received the first coin if the threshold in the rule above is equal to or above 3:


Page 4 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

If p ≥ 8/9, the prior probability of receiving the first coin is so high that no amount of evidence from 3 tosses of the coin will make Bob decide he received the second coin.

5. (a) Using the total probability theorem, we have


- (b) The least squares estimate coincides with the conditional expectation of Q given T1, which is derived as


(c) We write the posterior probability distribution of Q given T1 = t1, . . . , Tk = tk


where the denominator integrates out q so it could be viewed as a constant scalar c. To maximize the above probability we set its derivative with respect to q to zero

or equivalently


which yields the MAP estimate


For this part only assume q is sampled from the random variable Q which is now uniformly distributed over [0.5, 1]

Page 5 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

(d) The LLSE of T1 given T2 is


where the coefficients are


and from the law of total variance


and their covariance


Therefore we have derived the linear least squares estimator


6. (a) To find the normalization constant c we integrate the joint PDF:


Therefore, c = 4.

(b) To construct the conditional expectation estimator, we need to find the conditional proba­ bility density.

Thus


Page 6 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

- (c) We first note that the conditional probability does not depend on y. Therefore, X and Y are independent, and whether or not we observe Y = y does not affect the estimate in part (b). Another way to see this is to consider that if we do not observe y, we can compute the marginal fX (x) = �01<sup>4xydy= 2xwhich is equal to the conditional density, and will therefore</sup> produce the same estimate.

- (d) Since X and Y are independent, no estimator can make use of the observed value of Y to estimate X. The MAP estimator for X is equal to 1, regardless of what value y we observe, since the conditional (and the marginal) density is maximized at 1.

†Required for 6.431; optional challenge problem for 6.041

Page 7 of 7

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
