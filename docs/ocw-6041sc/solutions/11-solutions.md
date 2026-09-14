---
title: 11 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/11-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 11 solutions

**Source:** `solutions/11-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Problem Set 11 Solutions

1. Check book solutions .

2. (a) To find the MAP estimate, we need to find the value x that maximizes the conditional density fX|Y (x | y) by taking its derivative and setting it to 0.


Since the only factor that depends on x which can take on the value 0 is (y − x(µ + 1)), the maximum is achieved at


It is easy to check that this value is indeed maximum (the first derivative changes from positive to negative at this value).

- (b) i. To show the given identity, we need to use Bayes’ rule. We first compute the denomi­ nator, pY (y)


Then, we can substitute into the equation we had derived in part (a)


Thus, λ = 1 + µ.

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

ii. We first manipulate xfX|Y (x | y):


Now we can find the conditional expectation estimator:


(c) The conditional expectation estimator is always higher than the MAP estimator by 1+1µ<sup>.</sup> 3. (a) The likelihood function is


To maximize the above probability we set its derivative with respect to q to zero

or equivalently


which yields Q<sup>�</sup> k = <u>Pk i=1</u><sup><u>k</u>ti</sup> . This is not different from the MAP estimate found before. Since the MAP estimate is calculated using a uniform prior, the likelihood function is a ‘scaled’ version of posterior probability and they can be maximized at the same value of q.

<u>�k</u> (b) Since<sup>1</sup> = <u>i=1</u><sup>Ti</sup> , and that each Ti is independent identically distributed, it follows that Q<sup>�</sup> k k

1 is actually a sample mean estimator. The weak law of large numbers says that, when Q<sup>�</sup> k the number of samples increases to infinity, the sample mean estimator converges to the actual mean, which is q 1∗<sup>in this case. So we can write the limit of probability as</sup>


2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

(c) Chebyshev inequality states that


So we have

To ensure the above probability to be greater than 0.95, we need that


or


The number of observations k needed depends on the variance of T1. For q close to 1, the variance is close to 0, and the required number of observations is very small (close to 0). For q = 1/2, the variance is maximum (var(T1) = 2), and we require k = 4000. Thus, to guarantee the required accuracy and confidence for all q, we need that,


4. (a) Normalization of the distribution requires:


(b) Rewriting pK(k; θ) as:


the probability distribution for the photon number is a geometric probability distribution <u>1</u> with probability of success p = 1 − e<sup>−</sup> θ , and it is shifted with 1 to the left since it starts with k = 0. Therefore the photon number expectation value is


and its variance is


3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

(c) The joint probability distribution for the ki is


The log likelihood is −n · log Z(θ) − 1/θ �ni=1 ki<sup>.</sup> We find the maxima of the log likelihood by setting the derivative with respect to the parameter θ to zero:

The log likelihood is


or


<u>1</u> For a hot body, θ ≫ 1 and <u>1</u> e θ −1<sup>≈θ, we obtain</sup>

Thus the maximum likelihood estimator Θ<sup>ˆ</sup> n for the temperature is given in this limit by the sample mean of the photon number


- (d) According to the central limit theorem, the sample mean approaches for large n a Gaussian distribution with standard deviation our root mean square error


To allow only for 1% relative root mean square error in the temperature, we need<sup><u>σK</u></sup> < ~~√~~ <u>n</u> 0.01µK. With σK<sup>2=</sup> µ2 K + µK it follows that


In general, for large temperatures, i.e. large mean photon numbers µK ≫ 1, we need about 10,000 samples.

- (e) The 95% confidence interval for the temperature estimate for the situation in part (d), i.e.


is


4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


From the standard normal table, we have Φ(1.96) = 0.975, so we obtain


Because the variance is less that 4, we have


(b) The likelihood function is


And the log-likelihood function is


The derivative with respect to θ is<sup><u>n</u></sup> θ<sup>−�</sup> n i=1<sup>wi,and by setting it to zero, we see that the</sup> maximum of log fW (w; θ) over θ ≥ 0 is attained at θ<sup>ˆ</sup> n =<sup><u>P</u></sup> ~~n~~ i=1<sup><u>n</u>wi</sup> . The resulting estimator is


In this case,


6. (a) Using the regression formulas of Section 9.2, we have


where


The resulting ML estimates are

θ<sup>ˆ</sup> 1 = 40.53, θ<sup>ˆ</sup> 0 = −65.86.

5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

(b) Using the same procedure as in part (a), we obtain


where


which for the given data yields


Figure 1 shows the data points (xi, yi), i = 1, . . . , 5, the estimated linear model


and the estimated quadratic model


Figure 1: Regression Plot

6

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
