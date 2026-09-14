---
title: 5 Lecture Five
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Lecture Five

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 The Hypergeometric Distribution**

In the last class, we studied the Hypergeometric Distribution in the following urn setting. There is an urn with _N_ balls of which _R_ are red and the remaining _W_ := _N − R_ are white. Assume that the balls are identical in every other respect. We then sample _n_ balls from the urn without replacement. What is the probability of seeing exactly _r_ red balls in the sample? We saw that the answer is given by:


where _w_ := _n − r_ is the number of white balls in the sample.

We can let _X_ to be the random variable denoting the number of red balls in the drawn sample of size _n_ . Then


This _X_ is said to have the Hypergeometric Distribution with parameters _N, R, n_ .

Let us go over the proof of (20) using notation that is different from last time. For each _i_ = 1 _, . . . , n_ , let _Xi_ denote the binary random variable that equals 1 if the _i_<sup>_th_</sup> draw results in a red ball and equals 0 if the _i_<sup>_th_</sup> draw results in a white ball. Then it is easy to see that


By the argument given at the end of the last lecture, we have (<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_xi_belowplaystherole</sup> of _r_ in (20)):


An important feature of (22) is that the right hand side depends on the individual _x_ 1 _, . . . , xn_ only through their sum<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_xi_.This implies that the distribution of</sup><sup>_X_1</sup><sup>_, . . . , Xn_is the same</sup> as _Xπ_ 1 _, . . . , Xπn_ for every permutation _π_ 1 _, . . . , πn_ of 1 _, . . . , n_ :


for every _x_ 1 _, . . . , xn ∈{_ 0 _,_ 1 _}_ .

Random variables having the property (22) are known as **exchangeable** . Thus _X_ 1 _, . . . , Xn_ are exchangeable random variables. Here are some consequences of exchangeability.


for every _x ∈{_ 0 _,_ 1 _}_ . The reason behind (23) is that for every _i_ = 2 _, . . . , n_ ,


26

Even though _X_ 1 _, . . . , Xn_ have identical distributions, they are not independent however because


In general,

i.i.d = _⇒_ exchangeable but exchangeable _̸_ = _⇒_ i.i.d _._


for all _u, v ∈{_ 0 _,_ 1 _}_ . This is true because, for example,


This proves that ( _X_ 3 _, X_ 4) has the same distribution as ( _X_ 1 _, X_ 2). The proof for other pairs is similar.

3. The distribution of every _k_ -tuple ( _Xi_ 1 _, . . . , Xik_ ) for any distinct indices _i_ 1 _, . . . , ik_ from _{_ 1 _, . . . , n}_ is the same. The proof is similar to that of (23) and (24).

#### **5.1.1 Mean and Variance of the Hypergeometric Distribution**

The mean and variance of the random variable _X_ having the Hypergeometric distribution (20) are given by:


These formulae can be easily derived using exchangeability of _X_ 1 _, . . . , Xn_ and the fact that _X_ = _X_ 1 + _· · ·_ + _Xn_ as follows:


27

and


From here, one can deduce that


For more calculations involving the Hypergeometric Distribution, see Jaynes [1, Chapter 3].

### **5.2 Inverse Problem**

We now address the following question. Suppose we actually draw _n_ balls from the urn and see that _r_ of them are red. What can we then infer about the contents of the original urn? Specifically, using the observed data _n_ and _r_ , what can we say about _R_ and _N_ ?

This problem has applications in survey sampling. Suppose we want to know the number of people _R_ in a city that support the republican party. We take a sample of _n_ people out of which _r_ support republican. What can we then say about _R_ ?

We shall study this in the following cases.

#### **5.2.1 Case** 1 **:** _N_ **is known and** _R_ **is unknown**

We need to calculate


where data just refers to the observed values of _n_ and _r_ . Here _R_<sup>˜</sup> denotes a specific integer lying between 0 and _N_ .

By the Bayes rule, we have


28

To proceed further with the calculation, we need to make an assignment for P _{R_ = _R_<sup>˜</sup> _| N }_ which we take to be


This means that we are not expressing any preference for all the potential values 0 _,_ 1 _, . . . , N_ that _R_ can take. This gives


where _C_ is the constant


A standard mathematical fact involving binomial coefficients (often referred to as a ChuVandermonde identity; see, for example, equation (9) in `https://en.wikipedia.org/wiki/ Binomial_coefficient#Sums_of_the_binomial_coefficients` ) now gives


We thus get the following formula for the posterior distribution of _R_ :


Note how nicely this posterior distribution corresponds to common sense. For example, we automatically get 0 for the posterior when _R_<sup>˜</sup> _< r_ and when _W_<sup>˜</sup> = _N − R_<sup>˜</sup> _< w_ . This is because � _Rr_ ˜� = 0 when _R_<sup>˜</sup> _< r_ and � _Ww_ ˜ � = 0 when _W_<sup>˜</sup> _< w_ . Also when there is no data (i.e., when _n_ = _r_ = 0), the posterior becomes equal to the prior.

We can summarize the above posterior distribution via its mean and variance which are given by (see Chapter 6 of the Jaynes book for details behind the answers below)


and

where


Observe that when _N_ (the number of balls in the urn) is large, we can write

and


29

A point estimate of _N_<sup>_<u>R</u>_canbetakentobe</sup><sup>_p_(when</sup><sup>_N_islarge)andtheuncertaintyofthis</sup> _<u>p</u>_ <u>(1</u> _−p_ <u>)</u> point estimate can be taken to be the posterior standard deviation ~~�~~ _n_ +3<sup>.These of course</sup> can be calculated from the observed data _r_ and _n_ .

Let us now do a predictive calculation. Let _Rn_ +1 denote the proposition that the ( _n_ +1)<sup>_th_</sup> draw leads to a red ball. What is the probability of _Rn_ +1 given the observed data? This is obtained by


Given _R_ = _R_<sup>˜</sup> and the data, it is clear that, just before the ( _n_ + 1)<sup>_th_</sup> draw, the urn contains _R_ ˜ _− r_ red balls and _N − r_ total balls. As a result


Thus


because of (25). This equation is known as the Laplace Rule of Succession (more details on this will be provided later). Observe that when _n_ (the sample size) is large, we have


so that P _{Rn_ +1 _|_ data _, N }_ is basically equal to the observed fraction of red balls in the sample.

We can write the above formula in slightly different notation. Let _X_ 1 _, . . . , Xn_ +1 be as before i.e., _Xi_ equals 1 if the _i_<sup>_th_</sup> draw leads to red and 0 if the _i_<sup>_th_</sup> draw leads to white. Then, when _n_ is large,


This reveals a connection between probability and observed frequency that naturally appears by a probability calculation.

#### **5.2.2 Case 2:** _N_ **is unknown and** _R_ **is known**

This situation arises in the Capture-Recapture problem in ecology. Suppose there is a given pond with some fish and we want to estimate the number of fish in the pond. We take a first fish sample of size _R_ . We then color red (or just tag by some label) all the fish in our sample and then let them back into the pond. Now the pond is like a urn with _R_ red fish

30

and the remaining _W_ = _N − R_ non-red fish. We now take a second sample of size _n_ and observe that _r_ of this second sample of fish are red. Based on knowledge of _r, n, R_ , what can we infer about _N_ ?

The relevant calculation now is


To proceed further with the calculation, we need to make an assignment for P _{N_ = _N_<sup>˜</sup> _| R}_ which we take to be


for some large number _N_ max. This gives

The presence of the binomial coefficient means that the posterior probability above is zero unless _N_<sup>˜</sup> _≥ R_ + _w_ . This posterior will give us everything that we need to know about _N_<sup>˜</sup> after observing the data. If the posterior depends on _N_ max, we need to be careful with the results as it would mean that the data is not very informative for _N_ . This would be the case for example if _r_ = 0.

#### **5.2.3 Case 3: Both** _N_ **and** _R_ **are unknown**

In this case, we need to place a prior for


If we assume that _R | N_ is uniform on _{_ 0 _, . . . , N }_ , we would get


The posterior then becomes


In this case, we can do useful inference on _R/N_ but we cannot learn anything nontrivial from the data about _N_ . To see this, calculate the marginal posterior probability of _N_ and show that


This means that the posterior for _N_ is just the prior truncated to the set _{n, n_ + 1 _, . . . }_ so we basically don’t learn anything about _N_ from the sample other than the fact that it is at least _n_ . Nontrivial inference about _N_ is only possible if we _R_ and _N_ are known to be linked in some manner and we use a prior reflecting that link.

To learn more about inference of the parameters of the hypergeometric distribution, see Jaynes [1, Chapter 6].

31

---

[← 4 Lecture Four](05-4-lecture-four.md) · [Up: contents](index.md) · [6 Lecture Six →](07-6-lecture-six.md)
