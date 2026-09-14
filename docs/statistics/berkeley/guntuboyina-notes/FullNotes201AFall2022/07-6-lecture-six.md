---
title: 6 Lecture Six
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Lecture Six

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **6.1 Random Variables**

We shall go over the Binomial and Negative Binomial distributions today. It will be convenient to use the language of random variables. The term “random variable” can be used to describe any varying quantity (taking real values) about which we are uncertain about. Many real-life quantities such as (a) The average temperature in Berkeley tomorrow, (b) The height of the tallest student in this room, (c) the number of phone calls that I will receive tomorrow, (d) the number of accidents that will occur on Hearst avenue in September, etc. can be treated as random variables. The term “random” in the phrase “random variable” refers to the uncertainty of a specific individual about the specific value that will be taken by the variable. Note, in particular, that variable may not be intrinsically random but it is random from the point of view of a specific individual because of their uncertainty. For example, it is perfectly fine for me to treat Joe Biden’s current height as a random variable even though it is actually non-random.

The _distribution_ of a random variable is, informally, a description of the set of values that the random variable takes and the probabilities with which it takes those values.

If a random variable _X_ takes a finite or countably infinite set of possible values (in this case, we say that _X_ is a _discrete_ random variable), its distribution is described by a listing of the values _a_ 1 _, a_ 2 _, . . ._ that it takes together with a specification of the probabilities:


The function which maps _ai_ to P _{X_ = _ai}_ is called the _probability mass function_ (pmf) of the discrete random variable _X_ .

If a random variable takes a continuous set of values, its distribution is often described by a function called the _probability density function_ (pdf). We shall formally define this later.

#### **6.1.1 Independence of Random Variables**

We say that random variables _X_ 1 _, . . . , Xn_ are independent if, for every subset _S ⊆{_ 1 _, . . . k}_ , conditioning on any proposition involving _Xi, i ∈/ S_ does not change the probability of any proposition involving _Xi, i ∈ S_ . From here one can easily derive properties of independence such as


for all possible choices of _A_ 1 _, . . . , Ak_ .

Independence can be a subtle concept in modeling. Suppose I am uncertain about _X_ 1 := Joe Biden’s height and _X_ 2 := Donald Trump’s height. Would it be a reasonable for me to assume that _X_ 1 and _X_ 2 are independent?

### **6.2 Common Discrete Distributions**

#### **6.2.1 Bernoulli** _Ber_ ( _p_ ) **Distribution**

A random variable _X_ is said to have the _Ber_ ( _p_ ) (Bernoulli with parameter _p_ ) distribution if it takes the two values 0 and 1 with P _{X_ = 1 _}_ = _p_ .

32

Note then that E _X_ = _p_ and _V ar_ ( _X_ ) = _p_ (1 _− p_ ). For what value of _p_ is _X_ most variable? least variable?

#### **6.2.2 Binomial** _Bin_ ( _n, p_ ) **Distribution**

A random variable _X_ is said to have the Binomial distribution with parameters _n_ and _p_ ( _n_ is a positive integer and _p ∈_ [0 _,_ 1]) if it takes the values 0 _,_ 1 _, . . . , n_ with pmf given by


Here � _nk_ � is the binomial coefficient:


The binomial distribution arises in basically two contexts:

1. **Approximation of the hypergeometric distribution** : In the last class, we looked at the hypergeometric distribution which corresponds to the probabilities


This arises as the probability of seeing exactly _r_ red balls when _n_ (= _r_ + _w_ ) balls are drawn without replacement from an urn with _R_ red balls and _N −R_ white balls. When _N_ is much larger than _n_ , we can write


and


As a result, the hypergeometric probability simplifies to


which corresponds to the binomial distribution with parameters _n_ and _p_ := _R/N_ .

2. **Number of Successes in Repeated Trials** : Suppose


where each _Xi ∼_ Ber( _p_ ) and _X_ 1 _, . . . , Xn_ are independent. Then it can be checked that _X ∼_ Bin( _n, p_ ).

**Example 6.1** (Fairness testing) **.** _Suppose a coin is tossed 12 times leading to the outcome: TTTTHTHTTTTH (this has 3 heads and 9 tails). What is your assessment of the fairness of the coin?_

33

_For the usual frequentist answer to this question, we assume that the observed sequence of outcomes are the realization of random variables X_ 1 _, . . . , Xn (with n_ = 12 _) that are independently distributed according to the Bin_ ( _n, p_ ) _distribution for some unknown p. We need to test the (null) hypothesis that p_ = 0 _._ 5 _against, say, the alternative p <_ 0 _._ 5 _. This can be done by calculating the p-value which is the probability (under the assumption p_ = 0 _._ 5 _) of getting 3 or lower heads. The distribution of the number of heads under the null distribution is Bin_ ( _n,_ 0 _._ 5) _so the p-value is_


_which does not lead to a rejection of the null hypothesis at the usual 5% level._

#### **6.2.3 Negative Binomial NB** ( _n, p_ ) **distribution**

Let _X_ denote the number of tosses (of a coin with probability of heads _p_ ) required to get the _k_<sup>_th_</sup> head. What is the probability distribution of _X_ ?

The distribution of _X_ is given by the following. _X_ takes the values _k, k_ + 1 _, . . ._ and


This is called the Negative Binomial distribution with parameters _k_ and _p_ (denoted by _NB_ ( _k, p_ )).

**Example 6.2** (Fairness Testing (continued)) **.** _Let us get back to the fairness testing problem in Example 6.1 where a coin was tossed 12 times leading to the outcome: TTTTHTHTTTTH (this has 3 heads and 9 tails). In our previous p-value calculation, we implicitly assumed that the experiment consisted of tossing the coin 12 times where 12 was a priori chosen by the coin tosser. Consider now the alternative scenario where the coin tosser wanted to toss the coin until the point where 3 heads are observed. Now for the same outcome, the p-value will change. Indeed now the random variable of interest will become N_ = _number of tosses and the p-value will equal the probability of needing to toss the coin 12 or more times to get the 3 heads (assuming fairness). This is calculated using the negative binomial distribution as:_


_and this leads to rejection of the null hypothesis at the_ 5% _level._

Note that the “likelihood function” is the same function _p_<sup>3</sup> (1 _−p_ )<sup>9</sup> whether the sample size was predetermined or whether the coin was tossed till 3 heads are observed. But the procedure obtained for testing _p_ = 0 _._ 5 has changed from the binomial to the negative binomial case. This means that _p_ -valued based frequentist inference violates the Likelihood Principle (the likelihood principle states that “all the evidence in a sample relevant to model parameters is

34

contained in the likelihood function”). Here is a story from the wikipedia article on the “Likelihood Principle” (see `https://en.wikipedia.org/wiki/Likelihood_principle` ) which puts an interesting context to these numbers:

_Suppose a number of scientists are assessing the probability of a certain outcome (which we shall call ’success’) in experimental trials. Conventional wisdom suggests that if there is no bias towards success or failure then the success probability would be one half. Adam, a scientist, conducted 12 trials and obtains 3 successes and 9 failures. One of those successes was the 12th and last observation. Then Adam left the lab._

_Bill, Adam’s boss in the same lab, continued Adam’s work and published Adam’s results, along with a significance test. He tested the null hypothesis that θ, the success probability, is equal to a half, versus θ <_ 0 _._ 5 _. The probability that out of 12 trials, 3 or fewer (i.e. more extreme) were successes, if H_ 0 _is true, is_ 7 _._ 3% _. Thus the null hypothesis is not rejected at the 5% significance level._

_Adam actually stopped immediately after 3 successes, because his boss Bill had instructed him to do so. After the publication of the statistical analysis by Bill, Adam realizes that he has missed a_ **_later instruction_** _from Bill to instead conduct 12 trials, and that Bill’s paper is based on this second instruction. Adam is very glad that he got his 3 successes after exactly 12 trials, and explains to his friend Charlotte that by coincidence he executed the second instruction. But Charlotte then explains to Adam that the p-value should now be changed to_ 3 _._ 27% _and the result becomes significant at the_ 5% _level. Adam is astonished to hear this._

For more comments on the violation of the likelihood principle by _p_ -values, read MacKay [5, Section 37.2].

To contrast with the above _p_ -value based analysis, let us look at a Bayesian/probability theory approach to this testing problem. The goal is to calculate:


where data refers to _TTTTHTHTTTTH_ . By the Bayes rule, we can write


We clearly have


What assignments do we use for


For concreteness, let us assume


This is actually a very strong assumption in favor of fairness because a coin can be not fair in many many variety of ways. So to assume that the probability of fairness is the same as the combined probability of the many variety of ways in which the coin can be non-fair seems quite strong.

Let us now come to P _{_ data _|_ not fair _}_ . If the coin is not fair, we can assume that it has a heads probability of _p_ and that the coin tosses are still independent. We can then write


35

To proceed further, we need to assign _fp|_ not fair( _p_ ). One concrete assumption might be that


This corresponds to the assumption that, under the alternative (not fair), _p_ has the uniform distribution on [0 _,_ 1]. Then (using an online integrator)

We then get


Note that this Bayesian probability calculation does not depend at all on whether the number of tosses ( _n_ = 12) was decided a priori or whether it was decided to toss until getting 3 heads. It is the same for both those cases.

Also note that the Bayesian approach (based on (26) and (27)) is only slightly supporting the alternative hypothesis (roughly 60% to the null 40%) while the frequentist _p_ -values are fairly small indicating more evidence for the alternative. This discrepancy also persists when the sample size is large. Consider the following example.

**Example 6.3.** _In a certain city, 49581 boys and 48870 girls have been born over a certain time period (note_ 49581 _/_ (49581 + 48870) = 0 _._ 5036109 _). Assuming that the number of male births is binomially distributed with parameters n_ = 49581 + 48870 = 98451 _and p, test the hypothesis H_ 0 : _p_ = 0 _._ 5 _._

_The usual frequentist p-value is:_


_which is fairly small._

_On the other hand, the Bayesian method above with the priors_ (26) _and_ (27) _gives_


_Thus the Bayesian method gives a high probability to the null while the frequentist method will reject the null hypothesis. The reason why the Bayesian method is so supportive of the null hypothesis is that the prior choice_ (26) _gives strong support to p_ = 0 _._ 5 _over nearby values of p (such as p ∈_ (0 _._ 49 _,_ 0 _._ 51) _)._

_This discrepancy between the Bayesian and Frequentist solutions in this problem is referred to as the Jeffreys-Lindley paradox (see_ _`https: // en. wikipedia. org/ wiki/ Lindley% 27s_ paradox` )._

---

[← 5 Lecture Five](06-5-lecture-five.md) · [Up: contents](index.md) · [7 Lecture Seven →](08-7-lecture-seven.md)
