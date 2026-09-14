---
title: 4 Lecture Four
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Lecture Four

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Recap: Derivation of the Rules of Probability for Subjective Probability**

In the last class, we sketched the derivation of the rules of probability from logical consistency **without** relying on any imagined frequency considerations for defining probability. The argument (taken from Jaynes [1, Chapter 2]) proceeded in the following way.

We denoted the “plausibility” of a proposition _A_ given some information in the form of proposition _B_ by ( _A | B_ ). We assumed that these plausibilities take values in the set of real numbers (no restriction to be in the interval [0 _,_ 1]) and that a higher value of plausibility represents greater belief.

19

To deduce the usual product rule of probability, we assumed the existence of a continuous coordinate-wise increasing function _F_ of two real variables such that


for all _A, B, C_ . This function can then be employed in two different orders to calculate ( _ABC | D_ ) for four propositions _A, B, C, D_ :


It is therefore natural to assume that the function _F_ should be such that the right hand sides of the above two equations produce the same answer. From this, one gets the condition:

_F_ ( _F_ ( _x, y_ ) _, z_ ) = _F_ ( _x, F_ ( _y, z_ )) for all real numbers _x, y, z._

As proved in Jaynes [1, Section 2.1], the only functions _F_ which satisfy the above equation are of the form


for a positive continuous increasing function _w_ .

From here, we derived the following:

1. _w_ ( _AB | C_ ) = _w_ ( _A | C_ ) _w_ ( _B | AC_ ) = _w_ ( _B | C_ ) _w_ ( _A | BC_ ).

2. _w_ ( _A | C_ ) always lies between 0 and 1 with _w_ (impossible) = 0 and _w_ (certain) = 1.

In other words, the function _w_ applied to the plausibilities leads to quantities which satisfy the first two rules of probability.

Next the goal is to derive the sum rule. Here we first assume that there exists a function _S_ : [0 _,_ 1] _→_ [0 _,_ 1] such that


for all _A_ and _C_ . Note that we are working with _w_ ( _A | C_ ) instead of the raw plausibilities ( _A | C_ ). This allows us to use the product rule which has already been derived. To set up the characterizing equation for _S_ ( _·_ ), consider the setting of Figure 2.

In this setting, there are two different ways of calculating the plausibility of the proposition _R_ = _AB_ in terms of _x_ := _w_ ( _A_ ) and _y_ := _w_ ( _B_ ) and the function _S_ . Both these calculations use the product rule. The first method for calculating _w_ ( _R_ ) = _w_ ( _AB_ ) is:


The second method for calculating _w_ ( _R_ ) = _w_ ( _AB_ ) simply switches the roles of _A_ and _B_ in the first method:


20


Figure 1: Setting for deriving the Sum Rule

It is therefore natural to assume that _S_ satisfies:


Recall that here _x_ = _w_ ( _A_ ) and _y_ = _w_ ( _B_ ). The setting is such that _x_ and _y_ cannot be completely arbitrary. Indeed because _B_<sup>_c_</sup> _⊆ A_ , we must have


Our condition on _S_ is therefore


It is now proved in Jaynes [1, Section 2.2] that the above condition implies that


for some _α >_ 0.

We have thus proved that


which is equivalent to


It can now be noted that the first two rules that are satisfied by _w_ ( _A|B_ ) are also satisfied by _w_<sup>_α_</sup> ( _A|B_ ). Thus _w_<sup>_α_</sup> ( _A|B_ ) satisfies all the three rules

21

1. 0 _≤ w_<sup>_α_</sup> ( _A|B_ ) _≤_ 1, _w_<sup>_α_</sup> (impossible) = 0, and _w_<sup>_α_</sup> (certain) = 1,

2. _w_<sup>_α_</sup> ( _AB|C_ ) = _w_<sup>_α_</sup> ( _A|C_ ) _w_<sup>_α_</sup> ( _B|AC_ ) = _w_<sup>_α_</sup> ( _B|C_ ) _w_<sup>_α_</sup> ( _A|BC_ ), and

3. _w_<sup>_α_</sup> ( _A_<sup>_c_</sup> _|C_ ) + _w_<sup>_α_</sup> ( _A|C_ ) = 1.

Denoting _w_<sup>_α_</sup> by P, we have

1. 0 _≤_ P( _A|B_ ) _≤_ 1, P(impossible) = 0, and P(certain) = 1,

2. **Product Rule** : P( _AB|C_ ) = P( _A|C_ )P( _B|AC_ ) = P( _B|C_ )P( _A|BC_ ), and

3. **Sum Rule** : P( _A_<sup>_c_</sup> _|C_ ) + P( _A|C_ ) = 1.

We have thus derived the rules of probability without invoking any relationship between probability and long-run frequency.

To summarize: If we argue in terms of plausibilities but we take care to ensure some natural constraints for logical consistency, then we cannot manipulate the plausibilities arbitrarily but have to reason according to the usual rules of probability after an appropriate transformation (this transformation is given by the function _w_<sup>_α_</sup> ).

The sum rule of probability is usually stated as


where _A ∪ B_ denotes the proposition “at least one of _A_ and _B_ is true” (Jaynes uses the notation _A_ + _B_ for _A ∪ B_ ). (14) can be derived from the stated rules as


### **4.2 Probability Assignment**

As we discussed in Lecture One, probability theory works according to the two steps: (a) probability assignment, and (b) calculation. The calculation in the second step is based on the rules of probability and we have seen just the rationale behind the rules.

We shall now make some general comments on the probability assignment step. The most important word here is “Information”. Probability assignment is always made by some specific individual based on available or assumed information. The term “assumed information” is important here because, quite often, certain aspects of available information might be hard to precisely quantify so one may choose to ignore such aspects in order work with a simpler probability assignment.

To make this first step of probability theory “rigorous”, we need precise rules for transforming available/assumed information into probability assignments. The most fundamental

22

of these rules is known as the **Principle of Indifference** or the **Principle of Insufficient Reason** and it states the following:

_If, on background information B, the propositions A_ 1 _, . . . , AN are mutually exclusive and exhaustive, and B does not favor any one of them over any other, then_


In other words, the Principle of Indifference states that if the background information _B_ is “symmetric” among _A_ 1 _, . . . , AN_ , then one should use the probability assignment (15). For a concrete example illustrating the Principle of Indifference, consider the following setting. suppose we want to assign a probability for a coin toss landing in _H_ . Let us consider the following three kinds of information:

1. **Information** _I_ 1: We don’t know anything at all about the coin. We don’t even know if it really has two sides _H_ and _T_ or both of its sides are of only one kind (either _H_ or _T_ ). In addition, we don’t know how exactly it will be tossed.

2. **Information** _I_ 2: We know that it is a “regular” coin and that it has two sides _H_ and _T_ but we don’t know how it will be tossed.

3. **Information** _I_ 3: We know that this coin has been tossed a large number of times in the past and it landed heads 70% of the time.

In the first case, the Principle of Indifference applies and we shall assign


It is very important to recognize here that (16) is not a statement of frequency. Specifically (16) does not mean that if we toss the coin a large number of times, it will land hands 50% of the time. All we are saying is that we assign the probability of 0 _._ 5 for the coin landing heads in this one specific toss that we are reasoning about. We simply do not have any information to make speculations about the behaviour of a large number of tosses. In fact, our information does not even tell us that the coin indeed has the two sides _H_ and _T_ . So it might well be the case the coin tosses will result in _HHHHH . . ._ or _TTTTT . . ._ . But we shall still assign (16) because our current information _I_ 1 does not allow us to distinguish between _H_ and _T_ .

Now let us come to _I_ 2 which is more informative than _I_ 1. However, even here, there is nothing to distinguish between _H_ and _T_ . So the Principle of Indifference applies again and we assign


Again this has nothing to do with frequency. Even though it is a regular coin, it might be tossed in a way to produce more heads than tails. So if an actual experiment were performed, then depending on how the coin tosses were performed, the frequency of heads can be pretty much anything between 0 and 1. Because our probability has nothing to do with frequency, we shall simply assign (17) as our information _I_ 2 is symmetric in _H_ and _T_ . Note that if an experiment is actually performed and the proportion of heads turns out to be different from 0.5, this does not contradict (17) at all. Because (17) is an assignment capturing our state of knowledge _I_ 2 and is perfectly sensible under _I_ 2.

Now let us come to _I_ 3. Here the Principle of Indifference obviously does not apply. If we were using the frequency definition, we would immediately assign P( _H|I_ 3) = 0 _._ 7. But

23

because our probability has nothing to do with frequency, we cannot jump to this assignment immediately. The issue is that here we need to reason about not just one toss but this imminent toss along with all the previous tosses. Specifically, in this situation _I_ 3, we are dealing with random variables _X_ 1 _, . . . , XN_ corresponding to the previous large number of tosses and the current toss _XN_ +1 about which we are reasoning. We need to calculate:


To calculate this, we need to make a more basic probability assignment for the joint distribution of _X_ 1 _, . . . , XN , XN_ +1 which allows us to compute P( _H|I_ 3). If we assume that


then _XN_ +1 will be independent from _X_ 1 _, . . . , XN_ so that (18) will be 0.5 i.e., the given frequency information is irrelevant under the model. On the other hand, under the more complicated model assumption


we shall show later that the probability (18) will be very close to 0 _._ 7 when _N_ is large.

Therefore, in the third situation, when we actually have frequency information, under the right kind of model, our analysis will lead to the frequency assignment. Thus in this theory of probability, frequency will appear naturally in probability assignments when frequency information is available and relevant to the problem.

Next we shall review standard probability distributions starting with the Hypergeometric Distribution. These standard distributions will be useful for us while making probability assignments.

### **4.3 Urn Problems: Hypergeometric Distribution**

Consider an urn with _N_ balls and assume that _R_ of the _N_ balls are red and the remaining _W_ := _N − R_ are white. Assume that the balls are identical in every other respect.

Suppose we sample _n_ balls from the urn without replacement. What is the probability of seeing exactly _r_ red balls in the sample? The answer, as we shall see, is given by


where _w_ := _n − r_ is the number of white balls in the sample. This requires 0 _≤ r ≤ R_ and 0 _≤ w ≤ W_ . If these conditions are not satisfied, the required probability will be zero.

Here is one way of proving this probability statement. Let _Ri_ denote the proposition that the _i_<sup>_th_</sup> draw results in a red ball and let _Wi_ denote the proposition that the _i_<sup>_th_</sup> draw results in a white ball. Let us first consider the probability


Using the product rule of probability we can calculate the above probability as


24

By the principle of indifference and the sum rule of probability, we get P( _R_ 1) = _R/N_ ,


and


It then follows that


It can now be checked that, by the same argument, one also has


More generally, the probability of any specific sequence _RWRRW . . ._ with exactly _r_ reds is given by


Because the number of such sequences of _R_<sup>_′_</sup> _s_ and _W_<sup>_′_</sup> _s_ with exactly _r R_<sup>_′_</sup> _s_ is

As a function of _r_ , this is known as the Hypergeometric Probability Mass Function. The mean of this distribution can be checked to be _nR/N_ . Thus the average fraction of red balls in the sample of size _n_ will match the fraction of red balls in the urn. We can also compute the most likely value of _r_ i.e., the mode of the hypergeometric distribution. For this, let


and one can easily calculate that


so that

This gives that


can be taken to be the mode of the hypergeometric distribution. When _n_ and _N_ are large, the quantity above is approximately _nR/N_ so that the most likely value of _r_ is approximately such that the sample fraction of red balls matches the fraction of red balls in the urn.

See Jaynes [1, Chapter 3] for more calculations in this urn setting.

25

---

[← 3 Lecture Three](04-3-lecture-three.md) · [Up: contents](index.md) · [5 Lecture Five →](06-5-lecture-five.md)
