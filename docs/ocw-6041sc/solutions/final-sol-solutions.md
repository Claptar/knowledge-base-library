---
title: Final sol solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/final-sol-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Final sol solutions

**Source:** `solutions/final-sol-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����

4. **(4 points)** Is the sequence _Yn_ a Markov chain? Justify your answer.

**Solution:** No. Assume the Markov process is in steady state. To satisfy the Markov property,


For large _n_ ,


since it is not possible to move upwards 3 times in a row. However in steady state,


Therefore, the sequence _Yn_ is not a Markov chain.

5. **(4 points)** Given that the _n_ th transition was a transition to the right ( _Yn_ = 1), find the probability that the previous state was state 1. (You can assume that _n_ is large.)

**Solution:** Using Bayes’ Rule,


6. **(4 points)** Suppose that _X_ 0 = 1. Let _T_ be defined as the first _positive time_ at which the state is again equal to 1. Show how to find **E** [ _T_ ]. (It is enough to write down whatever equation(s) needs to be solved; you do not have to actually solve it/them or to produce a numerical answer.)

**Solution:** In order to find the the mean recurrence time of state 1, the mean first passage times to state 1 are first calculated by solving the following system of equations:


The mean recurrence time of state 1 is then _t_<sup>_∗_</sup> 1<sup>= 1 +</sup><sup>_p_12</sup><sup>_t_2.</sup>

Solving the system of equations yields _t_ 2 = 20 and _t_ 3 = 30 and _t_<sup>_∗_</sup> 1<sup>=9.</sup>

7. **(4 points)** Does the sequence _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ converge in probability? If yes, to what? If not, just say “no” without explanation.

**Solution:** No.

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

�C���� 9��� {�������� � C��� �����

8. **(4 points)** Let _Zn_ = max _{X_ 1 _, . . . , Xn}_ . Does the sequence _Z_ 1 _, Z_ 2 _, Z_ 3 _, . . ._ converge in probability? If yes, to what? If not, just say “no” without explanation.

**Solution:** Yes. The sequence converges to 3 in probability.

For the original markov chain, states _{_ 1 _,_ 2 _,_ 3 _}_ form one single recurrent class. Therefore, the Markov process will eventually visit each state with probability 1. In this case, the sequence _Zn_ will, with probability 1, converge to 3 once _Xn_ visits 3 for the first time.

**Problem 2. (68 points)** Alice shows up at an Athena * cluster at time zero and spends her time exclusively in typing emails. The times that her emails are sent are a Poisson process with rate _λA_ per hour.

1. **(3 points)** What is the probability that Alice sent exactly three emails during the time interval [1 _,_ 2]?

**Solution:** The number of emails Alice sends in the interval [1 _,_ 2] is a Poisson random variable with parameter _λA_ . So we have:


2. Let _Y_ 1 and _Y_ 2 be the times at which Alice’s first and second emails were sent.

   - (a) **(3 points)** Find **E** [ _Y_ 2 _| Y_ 1].

**Solution:** Define _T_ 2 as the second inter-arrival time in Alice’s Poisson process. Then:

_Y_ 2 = _Y_ 1 + _T_ 2


- (b) **(3 points)** Find the PDF of _Y_ 12.

   - **Solution:** Let _Z_ = _Y_ 12. Then we first find the CDF of _Z_ and differentiate to find the PDF of _Z_ :


- (c) **(3 points)** Find the joint PDF of _Y_ 1 and _Y_ 2. **Solution:**


2

*Athena is MIT's UNIX-based computing environment. OCW does not provide access to it.

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����

3. You show up at time 1 and you are told that Alice has sent exactly one email so far. (Only give answers here, no need to justify them.)

   - (a) **(3 points)** What is the conditional expectation of _Y_ 2 given this information? **Solution:** Let _A_ be the event _{_ exactly one arrival in the interval [0,1] _}_ . Looking forward from time _t_ = 1, the time until the next arrival is simply an exponential random variable ( _T_ ). So,


- (b) **(3 points)** What is the conditional expectation of _Y_ 1 given this information? **Solution:** Given _A_ , the times in this interval are equally likely for the arrival _Y_ 1. Thus,


4. Bob just finished exercising (without email access) and sits next to Alice at time 1. He starts typing emails at time 1, and fires them according to an independent Poisson process with rate _λB_ .

   - (a) **(5 points)** What is the PMF of the total number of emails sent by the two of them together during the interval [0 _,_ 2]? **Solution:** Let _K_ be the total number of emails sent in [0 _,_ 2]. Let _K_ 1 be the total number of emails sent in [0 _,_ 1), and let _K_ 2 be the total number of emails sent in [1 _,_ 2]. Then _K_ = _K_ 1 + _K_ 2 where _K_ 1 is a Poisson random variable with parameter _λA_ and _K_ 2 is a Poisson random variable with parameter _λA_ + _λB_ (since the emails sent by both Alice and Bob after time _t_ = 1 arrive according to the merged Poisson process of Alice’s emails and Bob’s emails). Since _K_ is the sum of independent Poisson random variables, _K_ is a Poisson random variable with parameter 2 _λA_ + _λB_ . So _K_ has the distribution:


- (b) **(5 points)** What is the expected value of the total typing time associated with the email that Alice is typing at the time that Bob shows up? (Here, “total typing time” includes the time that Alice spent on that email both before and after Bob’s arrival.)

   - **Solution:** The total typing time _Q_ associated with the email that Alice is typing at the time Bob shows up is the sum of _S_ 0, the length of time between Alice’s last email or time 0 (whichever is later) and time 1, and _T_ 1, the length of time from 1 to the time at which Alice sends her current email. _T_ 1 is exponential with parameter _λA_ . and _S_ 0 = min _{T_ 0 _,_ 1 _}_ , where _T_ 0 is exponential with parameter _λA_ .

Then,


and


We have: **E** [ _T_ 1] = 1 _/λA_ .

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����

We can find **E** [ _S_ 0] via the law of total expectations:


where the above integral is evaluated by manipulating the integrand into an Erlang order 2 PDF and equating the integral of this PDF from 0 to 1 to the probability that there are 2 or more arrivals in the first hour (i.e. **P** ( _Y_ 2 _<_ 1) = 1 _−_ **P** (0 _,_ 1) _−_ **P** (1 _,_ 1)). Alternatively, one can integrate by parts and arrive at the same result. Combining the above expectations:


- (c) **(5 points)** What is the expected value of the time until each one of them has sent at least one email? (Note that we count time starting from time 0, and we take into account any emails possibly sent out by Alice during the interval [0 _,_ 1].)

**Solution:** Define _U_ as the time from _t_ = 0 until each person has sent at least one email. Define _V_ as the remaining time from when Bob arrives (time 1) until each person has sent at least one email (so _V_ = _U −_ 1).

Define _S_ as the time until Bob sends his first email after time 1.

Define the event _A_ = _{_ Alice sends one or more emails in the time interval [0 _,_ 1] _}_ = _{Y_ 1 _≤_ 1 _}_ , where _Y_ 1 is the time Alice sends her first email.

Define the event _B_ = _{_ After time 1, Bob sends his next email before Alice does _}_ , which is equivalent to the event where the next arrival in the merged process from Alice and Bob’s orginal processes (starting from time 1) comes from Bob’s process. We have:


4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����

Then,


Note that **E** [ _V | B_<sup>c</sup> _∩ A_<sup>c</sup> ] is the expected value of the time until each of them sends one email after time 1 (since, given _A_<sup>c</sup> , Alice did not send any in the interval [0 _,_ 1]) and given Alice sends an email before Bob. Then this is the expected time until an arrival in the merged process followed by the expected time until an arrival in Bob’s process. So, **E** [ _V | B_<sup>c</sup> _∩ A_<sup>c</sup> ] =

> <u>1</u> +<sup><u>1</u></sup> . _λA_ + _λB λB_ Similarly, **E** [ _V | B ∩ A_<sup>c</sup> ] is the time until each sends an email after time 1, given Bob sends an <u>1 1</u> email before Alice. So **E** [ _V | B ∩ A_<sup>c</sup> ] = _λA_ + _λB_ + _λA_ . Also, **E** [ _V | A_ ] is the expected time it takes for Bob to send his first email after time 1 (since, given _A_ , Alice already sent an email in the interval [0 _,_ 1]). So **E** [ _V | A_ ] = **E** [ _S_ ] = 1 _/λB_ . Combining all of this with the above, we have:


- (d) **(5 points)** Given that a total of 10 emails were sent during the interval [0 _,_ 2], what is the probability that exactly 4 of them were sent by Alice? **Solution:**


As the form of the solution suggests, the problem can be solved alternatively by computing the probability of a single email being sent by Alice, given it was sent in the interval [0 _,_ 2]. This can be found by viewing the number of emails sent by Alice in [0 _,_ 2] as the number of arrivals arising from a Poisson process with twice the rate (2 _λA_ ) in an interval of half the duration (particularly, the interval [1 _,_ 2]), then merging this process with Bob’s process. Then the probability that an email sent in the interval [0 _,_ 2] was sent by Alice is the probability that an arrival in this new merged process came from the newly constructed 2 _λA_ rate process:

5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����


Then, out of 10 emails, the probability that 4 came from Alice is simply a binomial probability with 4 successes in 10 trials, which agrees with the solution above.

5. **(5 points)** Suppose that _λA_ = 4. Use Chebyshev’s inequality to find an upper bound on the probability that Alice sent at least 5 emails during the time interval [0 _,_ 1]. Does the Markov inequality provide a better bound?

**Solution:**

Let _N_ be the number of emails Alice sent in the interval [0 _,_ 1]. Since _N_ is a Poisson random variable with parameter _λA_ ,


To apply the Chebyshev inequality, we recognize:


In this case, the upper-bound of 4 found by application of the Chebyshev inequality is uninformative, as we already knew **P** ( _N ≥_ 5) _≤_ 1.

To find a better bound on this probability, use the Markov inequality, which gives:


6. **(5 points)** You do not know _λA_ but you watch Alice for an hour and see that she sent exactly 5 emails. Derive the maximum likelihood estimate of _λA_ based on this information.

**Solution:**


Setting the first derivative to zero


6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����

7. **(5 points)** We have reasons to believe that _λA_ is a large number. Let _N_ be the number of emails sent during the interval [0 _,_ 1]. Justify why the CLT can be applied to _N_ , and give a precise statement of the CLT in this case.

**Solution:** With _λA_ large, we assume _λA �_ 1. For simplicity, assume _λA_ is an integer. We can divide the interval [0 _,_ 1] into _λA_ disjoint intervals, each with duration 1 _/λA_ , so that these intervals span the entire interval from [0 _,_ 1]. Let _Ni_ be the number of arrivals in the _i_ th such interval, so that the _Ni_ ’s are independent, identically distributed Poisson random variables with parameter 1. Since _N_ is defined as the number of arrivals in the interval [0 _,_ 1], then _N_ = _N_ 1 + _· · ·_ + _NλA_ . Since _λA �_ 1, then _N_ is the sum of a large number of independent and identically distributed random variables, where the distribution of _Ni_ does not change as the number of terms in the sum increases. Hence, _N_ is approximately normal with mean _λA_ and variance _λA_ .

If _λA_ is not an integer, the same argument holds, except that instead of having _λA_ intervals, we have an integer number of intervals equal to the integer part of _λA_ ( _λ_<sup>¯</sup> _A_ =floor( _λA_ )) of length 1 _/λA_ and an extra interval of a shorter length ( _λA − λ_<sup>¯</sup> _A_ ) _/λA_ .

Now, _N_ is a sum of _λA_ independent, identically distributed Poisson random variables with parameter 1 added to another Poisson random variable (also independent of all the other Poisson random variables) with parameter ( _λA − λ_<sup>¯</sup> _A_ ). In this case, _N_ would need a small correction to apply the central limit theorem as we are familiar with it; however, it turns out that even without this correction, adding the extra Poisson random variable does not preclude the distribution of _N_ from being approximately normal, for large _λA_ , and the central limit theorem still applies.

To arrive at a precise statement of the CLT, we must “standardize” _N_ by subtracting its mean then dividing by its standard deviation. After having done so, the CDF of the standardized version of _N_ should converge to the standard normal CDF as the number of terms in the sum approaches infinity (as _λA →∞_ ).

Therefore, the precise statement of the CLT when applied to _N_ is:


where Φ( _z_ ) is the standard normal CDF.

8. **(5 points)** Under the same assumption as in last part, that _λA_ is large, you can now pretend that _N_ is a normal random variable. Suppose that you observe the value of _N_ . Give an (approximately) 95% confidence interval for _λA_ . State precisely what approximations you are making. _Possibly useful facts:_ The cumulative normal distribution satisfies Φ(1 _._ 645) = 0 _._ 95 and Φ(1 _._ 96) = 0 _._ 975.

**Solution:** We begin by estimating _λA_ with its ML estimator Λ<sup>ˆ</sup> _A_ = _N_ , where **E** [ _N_ ] = _λA_ . With _λA_ large, the CLT applies, and we can assume _N_ has an approximately normal distribution. Since var( _N_ ) = _λA_ <u>,</u> we can also approximate the variance of _N_ with ML estimator for _λA_ , so var( _N_ ) _≈ N_ , and _σN ≈_ _~~√~~ N_ .

7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����

To find the 95% confidence interval, we find _β_ such that:


So, we find:


Thus, we can write:


9. You are now told that _λA_ is actually the realized value of an exponential random variable Λ, with parameter 2:


- (a) **(5 points)** Find **E** [ _N_<sup>2</sup> ]. **Solution:**


- (b) **(5 points)** Find the linear least squares estimator of Λ given _N_ . **Solution:**


Solving for the above quantities:


8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����

Substituting these into the equation above:


9

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
