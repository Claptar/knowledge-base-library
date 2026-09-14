---
title: 07 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/07-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 07 solutions

**Source:** `solutions/07-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

Problem Set 7: Solutions

1. (a) The event of the ith success occuring before the jth failure is equivalent to the ith success occurring within the first (i + j − 1) trials (since the ith success must occur no later than the trial right before the jth failure). This is equivalent to event that i or more successes occur in the first (i + j − 1) trials (where we can have, at most, (i + j − 1) successes). Let Si be the time of the ith success, Fj be the time of the jth failure, and Nk be the number of successes in the first k trials (so Nk is a binomial random variable over k trials). So we have:


- (b) Let K be the number of successes which occur before the jth failure, and L be the number of trials to get to the jth failure. L is simply a jth order Pascal, with probability of 1 − p (since we are now interested in the failures, not the successes.) Plugging into the formula for jth order Pascal random variable,


- (c) This expression is the same as saying we need at least 42 trials to get the 17th success. Therefore, it can be rephrased as having a maximum of 16 successes in the first 41 trials. Hence b = 41, a = 16.


2. A successful call occurs with probability p =<sup>3</sup> 4

   - (a) Fred will give away his first sample on the third call if the first two calls are failures and the third is a success. Since the trials are independent, the probability of this sequence of events is simply


- (b) The event of interest requires failures on the ninth and tenth trials and a success on the eleventh trial. For a Bernoulli process, the outcomes of these three trials are independent of the results of any other trials and again our answer is


- (c) We desire the probability that L2, the time to the second arrival is equal to five trials. We know that pL2(ℓ) is a Pascal PMF of order 2, and we have


Page 1 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

- (d) Here we require the conditional probability that the experimental value of L2 is equal to 5, given that it is greater than 2.


- (e) The probability that Fred will complete at least five calls before he needs a new supply is equal to the probability that the experimental value of L2 is greater than or equal to 5.


- (f) Let discrete random variable F represent the number of failures before Fred runs out of samples on his mth successful call. Since Lm is the number of trials up to and including the mth success, we have F = Lm − m. Given that Fred makes Lm calls before he needs a new supply, we can regard each of the F unsuccessful calls as trials in another Bernoulli process with parameter r, where r is the probability of a success (a disappointed dog) obtained by


We define X to be a Bernoulli random variable with parameter r. Then, the number of dogs passed up before Fred runs out, Dm, is equal to the sum of F Bernoulli random variables each with parameter r = 13 , where F is a random variable. In other words,


Note that Dm is a sum of a random number of independent random variables. Further, F is independent of the Xi’s since the Xi’s are defined in the conditional universe where the door is not answered, in which case, whether there is a dog or not does not affect the probability of that trial being a failed trial or not. From our results in class, we can calculate its expectation and variance by


where we make the following substitutions.


Page 2 of 6

# Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Finally, substituting these values, we have


3. We view the random variables T1 and T2 as interarrival times in two independent Poisson pro­ cesses both with rate λ S as the interarrival time in a third Poisson process (independent from the first two) with rate µ. We are interested in the expected value of the time Z until either the first process has had two arrivals or the second process has had an arrival.

   - Given that the first arrival was from the second process, the expected wait time for that arrival would be µ+1 λ<sup>.Theprobability of an arrivalfromthe secondprocess is</sup> µ+µλ<sup>. Given that the first</sup> arrival time was from the first process, the expected wait time would be that for first arrival, 1 , plus the expected wait time for another arrival from the merged process. Similarily, the

   - µ+λ probability of an arrival from the first process is µ+λ λ . Thus,

E[Z] = P(Arrival from second process)E[wait time|Arrival from second process] +

P(Arrival from first process)E[wait time|Arrival from first process]


After some simplifications, we see that


4. The dot location of the yarn, as related to the size of the pieces of the yarn cut for any particular customer, can be viewed in light of the random incident paradox.

   - (a) Here, the length of each piece of yarn is exponentially distributed. As explained on page 298 of the text, due to the memorylessness of the exponential, the distribution of the length of the piece of yarn containing the red dot is a second order Erlang. Thus, the E[R] = 2E[L] = λ2 .

   - (b) Think of exponentially-spaced marks being made on the yarn, so the length requested by the customers each involve three such sections of exponentially distributed lengths (since the PDF of L is third-order Erlang). The piece of yarn with the dot will have the dot in any one of these three sections, and the expected length of that section, by (a), will be 2/λ, while the expected lengths of the other two sections will be 1/λ. Thus, the total expected length containing the dot is 4/λ.

      - In general, for processes, in which the interarrival intervals with distribution FX(x) are IID, the expected length of an arbitrarily chosen interval is<sup>E</sup> E[[XX2]] . We see that for the above parts, this formula is certainly valid.

   - (c) Using the formula stated above, E[L] = �01 ℓ2eℓ dℓ = eℓ(ℓ2 − 2ℓ + 2)]10 = e − 2 E[L<sup>2</sup> ] = �01 ℓ3eℓ dℓ = eℓ(ℓ3 − 3ℓ2 + 6ℓ − 6)]10<sup>= 6 −2e</sup> Hence,

6 − 2e E[R] = . e − 2

Page 3 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

5. (a) We know there are n arrivals in t amount of time, so we are looking for how many extra arrivals there are in s amount of time.


(b) By definition:


(c) By definition:


- (d) We want to find: P(N = n|M = m). Given M=m, we know that the m arrivals are uni­ formly distributed between 0 and t+s. Consider each arrival a success if it occurs before time t, and a failure otherwise. Therefore given M=m, N is a binomial random variable with m trials and probability of success t+t s<sup>. We have the desired probability:</sup>


- (e) We can rewrite the expectatation as:

where the second equality is obtained via the independent increment property of the poisson process.

6. The described process for cars passing the checkpoint is a Poisson process with an arrival rate of λ = 2 cars per minute.

   - (a) The first and third moments are, respectively,


where we recognized the integrand to be a 4th-order Erlang PDF and therefore integrating it over the entire range of the random variable must sum to unity.

Page 4 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- (b) The Poisson process is memoryless, and thus the history of events in the previous 4 minutes does not affect the future. So, the conditional PMF for K is equivalent to the unconditional PMF that describes the number of Poisson arrivals in an interval of time, which in this case is τ = 6 minutes and thus (λτ ) = 12:


- (c) The first dozen computer cards are used up upon the 36th car arrival. Letting D denote this total time, D = T1 + T2 + . . . + T36, where each independent Ti is exponentially distributed with parameter λ = 2, the distribution for D is therefore a 36th-order Erlang distribution with PDF and expected value of, respectively,


- (d) In both experiments, because a card completes after registering three cars, we are considering the amount of time it takes for three cars to pass the checkpoint. In the second experiment, however, note that the manner with which the particular card is selected is biased towards cards that are in service longer. That is, the time instant at which we come to the corner is more likely to fall within a longer interarrival period – one of the three interarrival times that adds up to the total time the card is in service is selected by random incidence (see the end of Section 6.2 in text).

   - i. The service time of any particular completed card is given by Y = T1 + T2 + T3, and thus Y is described by a 3rd-order Erlang distribution with paramater λ = 2:


- ii. The service time of a particular completed card with one of the three interarrival times selected by random incidence is W = T1 + T2 + L, where L is the interarrival period that contains the time instant we arrived at the corner. Following the arguments in the text, L is Erlang of order two and thus W is described by a 4th-order Erlang distribution with parameter λ = 2:


- G1<sup>†</sup> . For simplicity, introduce the notation Ni = N (Gi) for i = 1, ..., n and NG = N (G). Then


Page 5 of 6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

The result can be interpreted as a multinomial distribution. Imagine we throw an n-sided die k times, where Side i comes up with probability pi = ci/c. The probability that side i comes up ki times is given by the expression above. Now relating it back to the Poisson process that we have, each side corresponds to an interval that we sample, and the probability that we sample it depends directly on its relative length. This is consistent with the intuition that, given a number of Poisson arrivals in a specified interval, the arrivals are uniformly distributed.

†Required for 6.431; optional for 6.041

Page 6 of 6

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
