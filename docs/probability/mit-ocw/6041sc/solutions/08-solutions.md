---
title: 08 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/08-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 08 solutions

**Source:** `solutions/08-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Problem Set 8: Solutions

1. (a) We consider a Markov chain with states 0, 1, 2, 3, 4, 5, where state i indicates that there are i shoes available at the front door in the morning before Oscar leaves on his run. Now we can determine the transition probabilities. Assuming i shoes are at the front door before Oscar sets out on his run, with probability<sup><u>1</u></sup> 2<sup>Oscar will return to the same door from</sup> which he set out, and thus before his next run there will still be i shoes at the front door. Alternatively, with probability<sup><u>1</u></sup> 2<sup>Oscar returns to a different door, and in this case, with</sup> equal probability there will be min{i + 1, 5} or max{i − 1, 0} shoes at the front door before his next run. These transition probabilities are illustrated in the following Markov chain:


<!-- Start of picture text -->
3 1 1 1 1 3<br>4 2 2 2 2 4<br>1 1 1 1 1<br>4 4 4 4 4<br>0 1 2 3 4 5<br>1 1 1 1 1<br>4 4 4 4 4<br><!-- End of picture text -->

- (b) When there are either 0 or 5 shoes at the front door, with probability<sup><u>1</u></sup> 2<sup>Oscar will leave on his</sup> run from the door with 0 shoes and hence run barefooted. To find the long-term probability of Oscar running barefooted, we must find the steady-state probabilities of being in states 0 and 5, π0 and π5, respectively. Note that the steady-state probabilities exist because the chain is recurrent and aperiodic.

Since this is a birth-death process, we can use the local balance equations. We have


implying that


and similarly,


As


it follows that πi =<sup><u>1</u></sup> 6<sup>fori= 0, 1, . . . ,5. Hence,</sup>


2. (a) Consider any possible sequence of values x1, x2, . . . , xt−1, i for X1, X2, . . . , Xt, and note that


Page 1 of 8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


P(|Xt+1| = j |Xt = i, Xt−1 = xt−1, . . . X1 = x1 ) = 0 , ||i| − j| > 1 .

As the conditional probabilities above only depend on |i|, where |Xt| = |i|, it follows that |X1|, |X2|, . . . satisfy the Markov property. The associated Markov chain is illustrated below.


(b) Note that Y1, Y2, . . . is not a Markov chain for m > 1, because


does not equal

P(Yt+1 = d + 1|Yt = d, Yt−1 = d, Yt−2 = d − 1) = 0 ,

for 0 < d < m (the idea is that if Yt−2 = d − 1, Yt−1 = d, and Yt = d, then |Xt| = d − 1, while if Yt−1 = d − 1, and Yt = d, then |Xt| = d). If, however, we keep track of |Xt| and Yt, we do have a Markov chain, because for any possible sequence of pairs of values (x1, y1), . . . , (xt−1, yt−1), (i1, i2) for (|X1|, Y1), . . . , (|Xt−1|, Yt−1), (|Xt|, Yt),


from which it is clear that the conditional probabilities only depend on (i1, i2), the values of |Xt| and Yt, respectively. The corresponding Markov chain is illustrated below.

Page 2 of 8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)


<!-- Start of picture text -->
1/2<br>1 1/2 1/2 1/2<br>(0, m) (1, m) (m-1,m) (m, m)<br>1/2 1/2 1/2 1/2<br>1 1/2 1/2 1/2<br>(0, m-1) (1, m-1) (m-1, m-1)<br>1/2 1/2 1/2<br>1/2<br>1<br>1/2<br>(0, 1) (1, 1)<br>1/2<br>1<br>(0, 0)<br><!-- End of picture text -->

3. (a) If m out of n individuals are infected, then there must be n − m susceptible individuals. Each one of these individuals will be independently infected over the course of the day with probability ρ = 1 − (1 − p)<sup>m</sup> . Thus the number of new infections, I, will be a binomial random variable with parameters n − m and ρ. That is,


- (b) Let the state of the SIS model be the number of infected individuals. For n = 2, the corresponding Markov chain is illustrated below.


<!-- Start of picture text -->
1 pq+(1- p)(1- q) (1- q) 2<br>p(1-q)<br>0 1 2<br>q(1- p) 2q(1- q)<br>q 2<br><!-- End of picture text -->

- (c) The only recurrent state is the state with 0 infected individuals.

- (d) Let the state of the SIR model be (S, I), where S is the number of susceptible individuals and I is the number of infected individuals. For n = 2, the corresponding Markov chain is illustrated below.

Page 3 of 8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


<!-- Start of picture text -->
1 1 1<br>(0,0) (1, 0) (2, 0)<br>q pq (1- p)q<br>2<br>q (0,1) (1, 1)<br>2q(1- q)<br>(1- q) (1- p)(1- q)<br>(0,2) p(1- q)<br>(1- q) 2<br><!-- End of picture text -->

If one did not wish to keep track of the breakdown of susceptible and recovered individuals when no one was infected, the three states free of infections could be consolidated into a single state as illustrated below.


<!-- Start of picture text -->
1<br>(∗,0)<br>q pq (1- p)q<br>2<br>q (0,1) (1, 1)<br>2q(1- q)<br>(1- q) (1- p)(1- q)<br>(0,2) p(1- q)<br>(1- q) 2<br><!-- End of picture text -->

   - (e) Any state where the number of infected individuals equals 0 is a recurrent state. For n = 2, there are either one or three recurrent states, depending on the Markov chain drawn in part (d).

4. (a) The process is in state 3 immediately before the first transition. After leaving state 3 for the first time, the process cannot go back to state 3 again. Hence J, which represents the number of transitions up to and including the transition on which the process leaves state 3 for the last time is a geometric random variable with success probability equal to 0.6. The variance for J is given by:


Page 4 of 8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

- (b) There is a positive probability that we never enter state 4; i.e., P (K < ∞) < 1. Hence the expected value of K is ∞.

- (c) The Markov chain has 3 different recurrent classes. The first recurrent class consists of states {1, 2}, the second recurrent class consists of state {7} and the third recurrent class consists of states {4, 5, 6}. The probability of getting absorbed into the first recurrent class starting from the transient state 3 is,


which is the probability of transition to the first recurrent class given there is a change of state. Similarly, probability of absorption into second and third recurrent classes are<sup><u>3</u></sup> 6<sup>and</sup> 62 respectively.

Now, we solve the balance equations within each recurrent class, which give us the probabili­ ties conditioned on getting absorbed from state 3 to that recurrent class. The unconditional steady-state probabilities are found by weighing the conditional steady-state probabilities by the probability of absorption to the recurrent classes.

The first recurrent class is a birth-death process. We write the following equations and solve for the conditional probabilities, denoted by p1 and p2.


Solving these equations, we get p1 =<sup><u>1</u></sup> 3<sup>,p2=</sup> 3<sup><u>2</u>. For the second recurrent class,p7= 1. The</sup> third recurrent class is also a birth-death process, we can find the conditional steady-state probabilities as follows,


and thus, p4 = 74 , p5 = 72 , p6 = <u>17</u> .

Using these data, the unconditional steady-state probabilities for all the states are found as follows:


Page 5 of 8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

- (d) The given conditional event, that the process never enters state 4, changes the absorption probabilities to the recurrent classes. The probability of getting absorbed to the first re­ current class is<sup><u>1</u></sup> 4<sup>, to the second recurrent class is</sup><sup><u>3</u></sup> 4<sup>, and to the third recurrent class is 0.</sup> Hence, the steady state probabilities are given by,


For pedagogical purposes, let us actually draw what the new Markov chain would look like, given the event that the process never enters state 4. The resulting chain is shown below. Let us see how we came up with these transition probabilities.


<!-- Start of picture text -->
1/2  4/10<br>1<br> S1  S2  S3<br>1/2  3/20<br>9/20<br> S7<br>1<br><!-- End of picture text -->

We need to be careful when rescaling the new transition probabilities. First of all, it is clear that the probabilities within the recurrent classes {S1, S2} and {S7} don’t get affected. We also note that the self loop transition probability of the transient state S3 doesn’t get changed either.(this would be true for any other transient state)

To see that the self loop probability p3,3 doesn’t get changed, we condition on the event that we eventually enter S2 or S7. Let’s call the new self loop probability, q3,3. Then,


Now, we calculate q3,7 and q3,2.

q3,7 = P (X1 = S7| absorbed into 2 or 7, X0 = S3) =<sup><u>p3,7∗P(absorbed into</u>2or7</sup><sup><u>|X1=S7, X0=S3)</u></sup> P (absorbed into 2 or 7 | X0=S3)


Page 6 of 8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


Now, we can calculate the absorption probabilities of this new Markov chain.

The probability of getting absorbed into the recurrent class {1, 2}, starting from S3, is <u>3</u> 203 <u>20+</u> 209<sup>=</sup> <u>14</u><sup>. The probability of getting absorbed into the recurrent class{7}, starting from</sup> <u>9</u> S3, is 203 <u>20+</u> 209<sup>=</sup> 43<sup>. Thus, our calculated absorption probabilities match the probabilities we</sup> intuited earlier. The important thing to take away from this example is that, when doing problems of this sort, (i.e given we do/don’t enter a particular set of recurrent classes), it is neccessary to rescale the transition probabilities of the new chain, coming out of ALL the transient states. In other words, to find each of the new transition probabilities, we condition on the given event, that we do or do not enter particular recurrent classes.

G1<sup>†</sup> . a) First let the pij’s be the transition probabilities of the Markov chain.

Then


and thus in general mk+1(c) = g(c) + �ni=1<sup>pcimk(i)whenc∈{1, ..., n}.</sup>

Note that the third equality simply uses the total expectation theorem. b)


Page 7 of 8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

E[V ar[g(X0) + g(X1) + ... + g(Xk+1)|X0 = 1, X1]]

- = V ar[g(1) + E[g(X1) + ... + g(Xk+1)|X0 = 1, X1]] +

   - E[V ar[g(1) + g(X1) + ... + g(Xk+1)|X0 = 1, X1]]

- = V ar[E[g(X1) + ... + g(Xk+1)|X0 = 1, X1]] + E[V ar[g(X1) + ... + g(Xk+1)|X0 = 1, X1]]

- = V ar[E[g(X1) + ... + g(Xk+1)|X1]] + E[V ar[g(X1) + ... + g(Xk+1)|X1]]


so in general vk+1(c) = �ni=1<sup>pcim2</sup> k<sup>(i) −(</sup> �ni=1<sup>pcimk(i))2+</sup> �ni=1<sup>pcivk(i)whenc∈{1, ..., n}.</sup>

†Required for 6.431; optional for 6.041

Page 8 of 8

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
