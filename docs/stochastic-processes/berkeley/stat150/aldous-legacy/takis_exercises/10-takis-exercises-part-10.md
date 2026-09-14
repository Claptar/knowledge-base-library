---
title: Takis exercises Part 10 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 10 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider a random walk on the following infinite graph:


The graph continues ad infinitum in the same manner.

39

Here, each state has exactly 3 neighbouring states (i.e. its degree is 3) and so the probability of moving to one of them is 1/3.

(i) Let 0 be the “central” state. (Actually, a closer look shows that no state deserves to be central, for they are all equivalent. So we just arbitrarily pick one and call it central.) Having done that, let D(i) be the distance of a state i from 0, i.e. the number of “hops” required to reach 0 starting from i. So D(0) = 0, each neighbour i of 0 has D(i) = 1, etc. Let Xn be the position of the chain at time n. Observe that the process Zn = D(Xn) has the Markov property. (See lecture notes for criterion!) The question is:

Find its transition probabilities.

(ii) Using the results from the gambler’s ruin problem, show that (Zn) is transient. (iii) Use (ii) to explain why (Xn) is also transient.

Solution. (i) First draw a figure:


The states with the same distance from 0 are shown in this figure as belonging to the same circle.

Next observe that if Zn = k (i.e. if the distance from 0 is k) then, no matter where Xn is actually located the distance Zn+1 of the next state Xn+1 from 0 will either be k + 1 with probability 2/3 or k − 1 with probability 1/3. And, of course, if Zn = 0 then Zn+1 = 1. So


(ii) Since 2/3 > 1/3, the chain (Zn) is transient.

(iii) We have that Zn →∞ as n →∞, with probability 1. This means that for any k, there is a time n0 such that for all n ≥ n0 we have D(Xn) ≥ k, and this happens with probability 1. So, with probability 1, the chain (Xn) will visit states with distance from 0 less than k only finitely many times. This means that the chain (Xn) is transient.

42.

A company requires N employees to function properly. If an employee becomes sick then he or she is replaced by a new one. It takes 1 week for a new employee to be recruited and to start working. Time here is measured in weeks.

(i) If at the beginning of week n there are Xn employees working and Yn of them get sick during week n then show that at the beginning of week n + 1 there will be


40

employees working.

(ii) Suppose that each employee becomes sick independently with probability p. Show that


(iii) Show that (Xn) is a Markov chain with state space S = {0, 1, . . . , N } and derive its transition probabilities.

(vi) Write the balance equation for the stationary distribution π of the chain.

(v) What is the number of employees working in steady state?

Do this without using (vi) by assuming that the X is in steady state [i.e. that X0 (and therefore each Xn) has distribution π] and by taking expectations on the equation you derived in (i).

Solution. (i) This is elementary: Since every time an employee gets sick he or she is replaced by a new one, but it takes 1 week for the new employee to start working, it means that those employees who got sick during week n − 1 will be replaced by new ones who will start working sometime during week n and so, by the end of week n, the number of employees will be brought up to N , provided nobody got sick during week n. If the latter happens, then we subtract the Yn employees who got sick during week n to obtained the desired equation.

(ii) Again, this is easy: If Xn = x, at most x employees can get sick. Each one gets sick with probability p, independently of one another, so the total number, Yn, of sick employees has the Binomial(x, p) distribution.

(iii) We have that Yn depends only on Xn and not on Xn−1, Xn−2, . . ., and therefore P (Xn+1 = j|Xn = i, Xn−1 = i1, Xn−2 = i2 . . .) = P (Xn+1 = j|Xn = i). Hence X is Markov. We are asked to derive pi,j = P (Xn+1 = j|Xn = i) for all i, j ∈ S. If Xn = i then Yn ≤ i and so Xn+1 ≥ N − i, so the only possible values j for which pi,j > 0 are j = N − i, . . . , N . In fact, P (Xn+1 = j|Xn = i) = P (Yn = N − j|Xn = i) and so, using the formulae of (ii),


(vi) The balance equations are:


(v) If X0 has distribution π then Xn has distribution π for all n. So EXn ≡ µ does not depend on n. Now, if Xn = x, Yn is Binomial(x, p) and therefore E(Yn|Xn = x) = px. So


41

Since EXn+1 = N − EYn we have

µ = N − pµ,

whence


This is the mean number of employees in steady state. So, for example, if p = 10%, then µ ≈ 0.91N .

43.

(i) Let X be the number of heads in n i.i.d. coin tosses where the probability of heads is p. Find the generating function ϕ(z) := Ez<sup>X</sup> of X.

(ii) Let Y be a random variable with P (Y = k) = (1 − p)<sup>k−1</sup> p, k = 1, 2, . . . Find the generating function of Y .

Solution. (i) The random variable X, which is defined as the number of heads in n i.i.d. coin tosses where the probability of heads is p, is binomially distributed:


Thus,


(ii) The random variable Y , defined by


has the following generating function:


42

44.

A random variable X with values in {1, 2, . . . , }∪{∞} has generating function ϕ(z) = Ez<sup>X</sup> .

- (i) Express P (X = 0) in terms of ϕ.

- (ii) Express P (X = ∞) in terms of ϕ.

(iii) Express EX and varX in terms of ϕ.

∞ Solution. (i) ϕ(0) = � P (X = k)z<sup>k</sup> |z=0 = P (X = 0), thus, P (X = 0) = ϕ(0). k=0 ∞ (ii) The following must hold: � P (X = k) + P (X = ∞) = 1. This may be rewritten k=0 as follows: ϕ(1) + P (X = ∞) = 1, from which we get


(iii) By definition of the expected value of a discrete random variable


Now note, that


so that ϕ<sup>′</sup> (1) should give nothing but EX. We conclude that


Let pk := P (X = k). Now we take the second derivative of ϕ(z):


so that


45.

A random variable X with values in {1, 2, . . . , } ∪{∞} has generating function


43

where p, q ≥ 0 and p + q = 1.

- (i) Compute P (X = ∞). (Consider all possible values of p).

- (ii) For those values of p for which P (X = ∞) = 0 compute EX.

Solution.

- (i) As it was found above, P (X = ∞) = 1 − ϕ(1), and particularly


(ii) It follows that P (X = ∞) = 0 for p ≥ 2<sup>1.TheexpectedvalueofXisgivenby</sup>


and we are done.

46.

You can go up the stair by climbing 1 or 2 steps at a time. There are n steps in total. In how many ways can you climb all steps?

Hint 1: If n = 3, you can reach the 3d step by climbing 1 at a time, or 2 first and 1 next, or 1 first and 2 next, i.e. there are 3 ways.

Hint 2: if wm is the number of ways to climb m steps, how is wm related to wm−1 and wm−2?

Hint 3: Consider the generating function<sup>�</sup> m<sup>zmwm.</sup>

Solution. Just before being at step m you are either at step m − 1 or at step m − 2. Hence


Here, step 0 means being at the bottom of the stairs. So


So


How do we find a formula for wn? Here is where generating functions come to rescue. Let


be the generating of (wm, m ≥ 0). Then the generating function of (wm+1, m ≥ 0) is


44

and the generating function of (wm+2, m ≥ 0) is


From the recursion


(obtained from (10) by replacing m by m + 2) we have (and this is were linearity is used) that the generating function of (wm+2, m ≥ 0) equals the sum of the generating functions of (wm+1, m ≥ 0) and (wm, m ≥ 0), namely,


Since w0 = w1 = 1, we can solve for W (s) and find


Essentially, what generating functions have done for us is to transform the LINEAR recursion (10) into the ALGEBRAIC equation (11). This is something you have learnt in your introductory Mathematics courses. The tools and recipes associated with LINEARITY are indispensable for anyone who does anything of value. Thus, keep them always in your bag of tricks.

The question we ask is:

Which sequence (wn, n ≥ 0) has generating function W (s)? We start by noting that the polynomial s<sup>2</sup> + s − 1 has two roots:


This can be written also as


which is always an integer (why?)

45

47.

Consider a branching process starting with Z0 = 1 and branching mechanism


(Each individual gives birth to 1 or 2 children with probability 1−p or p, respectively.) Let Zn be the size of the n-th generation. Compute the probabilities P (Zn = k) for all possible values of k, the generating function ϕn(z) = Ez<sup>Zn</sup> , and the mean size of the n-th generation mn = EZn. Do the computations in whichever order is convenient for you.

Solution. The mean number of offspring of a typical individual is


Therefore


Let q = 1 − p. To compute P (Z2 = 4), we consider all possibilities to have 4 children in the second generation. There is only one possibility:


Therefore P (Z2 = 4) = p<sup>2</sup> . To compute P (Z2 = 3) we have


and so P (Z2 = 3) = pqp + ppq. For P (Z2 = 2) we have


and so P (Z2 = 2) = qp + pq<sup>2</sup> And for P (Z2 = 1) there is only one possibility,

and so P (Z2 = 2) = q<sup>2</sup> . You can continue in this manner to compute P (Z3 = k), etc. The generating function of the branching mechanism is


46

So ϕ1(z) = Ez<sup>Z1</sup> = ϕ(z). Next, we have ϕ2(z) = ϕ1(ϕ(z)) and so


Similarly, ϕ3(z) = ϕ2(ϕ(z)) and so


48.

Consider a branching process with Z0 = 1 and branching mechanism


(i) Compute probability of ultimate extinction.

(ii) Compute the mean size of the n-th generation.

(iii) Compute the standard deviation of the size of the n-th generation.

Solution. (i) The generating function of the branching mechanism is


The probability ε of ultimate extinction is the smallest positive z such that


We have to solve


Its solutions are 1, 1/2. Therefore,


(ii) The mean number of offspring of an individual is


Therefore the mean size of the n-th generation is


(iii) As in Exercise 2 above, we have that


Since ϕn(z) = ϕn−1(ϕ(z)), we have


47

Setting z = 1 and using that ϕ(1) = 1 we have


Iterating this we find


We here have m = 11/10, ϕ<sup>′′</sup> (1) = 4/10. But then


Of course, the standard deviation is the square root of this number.

49.

Consider the same branching process as above, but now start with Z0 = m, an arbitrary positive integer. Answer the same questions.

Solution. (i) The process behaves as the superposition of N i.i.d. copies of the previous process. This becomes extinct if and only if each of the N copies becomes extinct and so, by independence, the extinction probability is


(ii) The n-th generation of the new process is the sum of the populations of the n-th generations of each of the N constituent processes. Therefore the mean size of the n-th generation is


(iii) For the same reason, the standard deviation of the size of the n-th generation is

√Nσn.

50.

Show that a branching process cannot have a stationary distribution π with π(i) > 0 for some i > 0.

48

Solution. If the mean number m of offspring is ≤ 1 then we know that the process will become extinct for sure, i.e. it will be absorbed by state 0. Hence the only stationary distribution satisfies


If the mean number m of offspring is > 1 then we know that the probability that it will become extinct is ε < 1, i.e. P1(τ0 = ∞) = 1 − ε > 0. But we showed in Part (i) of Problem 8 above that Pi(τ0 = ∞) = 1 − ε<sup>i</sup> > 0 for all i. Hence the process is transient. And so there is NO stationary distribution at all.

---

[← Takis exercises Part 09 —](09-takis-exercises-part-09.md) · [Up: contents](index.md) · [Takis exercises Part 11 — →](11-takis-exercises-part-11.md)
