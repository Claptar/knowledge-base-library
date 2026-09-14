---
title: 3 Lecture Three
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Lecture Three

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1 Interpretation of Probability**

There are multiple interpretations of probability and still some controversy regarding what probability really is. A proper understanding of the meaning of probability is very important for applications of probability to statistics and data analysis.

There are broadly two ways of understanding probability.

#### **3.1.1 Frequentist/Objective Understanding of Probability**

From the frequentist viewpoint, probability is applicable only in the context of “random experiments” (such as tossing coins and rolling dice). The probability P( _A_ ) of an event _A_ is defined as the relative frequency that _A_ occurs in _N_ repeated trials of the experiment in the limit as _N →∞_ :


where _nA_ is the number of trials out of _N_ where _A_ occurs. This definition of probability is the basis of frequentist statistics.

According to this definition, the statement P( _H_ ) = 0 _._ 5 means that the proportion of heads in a large number of tosses of the coin approaches 0 _._ 5.

The following are some obvious problems with the frequentist definition:

1. It is very restrictive and hardly ever applicable. In many simple situations where we would like to use probability, the frequency definition is simply does not apply:

   - a) Is the suspect X guilty?

   - b) What is the chance of rain in Berkeley today?

   - c) What is the chance that Y is cancer positive given that they tested positive?

13

For an interesting anecdote about how this restrictive notion does not simply make sense in some important problems, see deGroot [3, pages 43-44].

2. Even in situations where the frequency definition is seemingly applicable, closer thought might reveal some issues. For example, the frequentist probability that a coin comes up heads is 0.6 means that 60% of a large number of tosses of the coin should result in 0 _._ 6. But the mechanics of no two tosses are really identical and if two tosses are done exactly identically, then we would expect the same outcome by the laws of physics. So the term “identical and independent repetitions of an experiment” is ambiguous.

In the frequentist definition, probability is considered an intrinsic property of the object under investigation which is only accessible by an experiment generating samples of infinite size. The frequentist probability is also referred to as “objective probability”. The implication is that we cannot assign it arbitrarily because any probability assignment that does not agree with the frequency in infinite trials is wrong. Unfortunately, the actual frequentist probabililty is seldom known because one cannot generally observe a large number of repetitions of an experiment and so almost all probability assignments are wrong from the frequentist point of view. This is one way of understanding the statistics aphorism: “All models are wrong” (usually attributed to George Box; see `https: //en.wikipedia.org/wiki/All_models_are_wrong` ).

Here are some quotes by famous statisticians/probabilists illustrating how widespread frequentist thinking in probability is:

_The numbers pr should, in fact, be regarded as physical constants of the particular die that we are using, and the question as to their numerical values cannot be answered by the axioms of probability, any more than the size and the weight of the die are determined by the geometrical and mechanical axioms. However, experience shows that in a well-made die the frequency of any event r in any long series of throws usually approaches_ 1 _/_ 6 _, and accordingly we shall often assume that all the pr are equal to_ 1 _/_ 6... – Cram´er.

Here is Jaynes’s response to the above quote (from page 317 of his book): _To a physicist, this statement seems to show utter contempt for the known laws of mechanics. The results of tossing a die many times do_ **_not_** _tell us any definite number characteristic only of the die. They tell us also something about how the die was tossed. If you toss ’loaded’ dice in different ways, you can easily alter the relative frequencies of the faces. With only slightly more difficulty, you can still do this if your dice are perfectly ’honest’._

Here is a quote by Feller (see page 322 of the Jaynes book) illustrating the thinking that bridge hands possess physical probabilities and that the uniform probability assignment is a convention whose correctness can only be verified by observed frequencies in a random experiment : _The number of possible distributions of cards in bridge is almost_ 10<sup>30</sup> _. Usually we agree to consider them as equally probable. For a check of this convention more than_ 10<sup>30</sup> _experiments would be required – a billion of billion of years if every living person played one game every second, day and night._ – Feller.

In spite of these objections, one positive aspect of the frequentist meaning of probability is that the Rules of Probability follow easily from this definition.

#### **3.1.2 Subjective or Bayesian Understanding of Probability**

It should be clear that in order to use probability as a general method for reasoning under uncertainty, we need a much more general understanding of probability than that is allowed

14

by the frequentist notion. Expounding this general theory is the purpose of the Jaynes book [1].

The basic idea is to first give up on an objective definition of probability and just admit that _there is no such thing as a physical probability_ (Jaynes [1, page 325]). Every probability is subjective and is relative to the person who is actually reasoning under uncertainty. More specifically, probability of an event is something that a specific individual (or a robot or a computer) either assigns based on their state of knowledge (available information) or calculates based on their probability assignments for related events. Generally, probability has nothing do with frequency (unless we are in certain special situations where frequency information is available; we shall see examples of this later). Here is a quote by Harold Jeffreys (who was one of the founders of this way of thinking about probability) related to this:

_The essence of the present theory is that no probability, direct, prior, or posterior, is simply a frequency._ – Jeffreys 1939.

To give a concrete example, from the Bayesian viewpoint, the statement P( _H_ ) = 0 _._ 5 will considered to be the assignment made by some specific individual based on their background information. It means that, based on their background information, they have no reason at all to distinguish between _H_ and _T_ and thus they are totally confused about whether the specific toss will lead to an _H_ or a _T_ .

It is very interesting to note that the same statement P( _H_ ) = 0 _._ 5 is an informative objective fact in the frequentist viewpoint while it is an uninformative assignment in the Bayesian viewpoint.

To understand the Bayesian interpretation, consider developing a spam filter that classifies incoming emails as spam or regular (there are many statistics/machine learning methods for doing this including, say, logistic regression or classification trees). Suppose you have a trained spam filter and you apply it to a specific incoming email. If the filter outputs a predicted probability of the email being spam as 0.5, you would conclude that the filter has no idea whether this email is spam or regular. This is exactly the Bayesian viewpoint.

#### **3.1.3 Rules of Probability**

Let us now look at the rules of the probability when probability is viewed from the Bayesian viewpoint which has nothing with do with frequencies:

1. P( _A_ ) always lies between 0 and 1. The probability of an impossible event is 0 and the probability of a certain event is 1.

2. Product rule: P( _A ∩ B_ ) = P( _A_ )P( _B|A_ ) = P( _B_ )P( _A|B_ ).

3. Sum rule: P( _A ∪ B_ ) = P( _A_ ) + P( _B_ ) for disjoint events _A_ and _B_ .

These rules can be justified in a straightforward way if we use the frequency definition of probability. We are now using a more general form of probability which has nothing to do with frequencies and which are assignments made by a specific user. What is constraining the user to follow the above rules? The following quote by Fisher (1934) asks the same question:

_Keynes establishes the laws of addition and multiplication of probabilities, by stating these laws in the form of definitions of the processes of addition and multiplication. The important_

15

_step of showing that, when these probabilities have numerical values, “addition” and “multiplication” are so defined, are equivalent to the arithmetical processes ordinarily known by these names, is omitted. The omission is an interesting one, since it shows the difficulty of establishing the laws of mathematical probability, without basing the notion of probability on the concept of frequency, for which these laws are really true, and from which they were originally derived._

It is important to be able to justify the rules of probability for this general form of probability. Otherwise, there will be no principled way of computing probabilities of things we really care about and the whole business will be quite arbitrary.

The following justification for the rules of probability is originally due to the physicist R. T. Cox and is the content of Chapter 1 and Chapter 2 of Jaynes [1]. I will give a sketch of the argument skipping some important technical details. For the full argument, please read Jaynes [1, Chapter 1 and 2].

Let us first remove all restrictions on probabilities and even allow them to take values outside the interval [0 _,_ 1]. To avoid confusion, let us use the term “plausibilities”. We are assigning plausibilities of various events (or propositions) conditional on other events. Let us denote the plausibility of event _A_ conditional on event _B_ by ( _A|B_ ). Let us first make the assumption that plausibilities take values in the set of real numbers (no restriction now to be in the interval [0 _,_ 1]) and that a higher value of plausibility represents a greater belief.

#### **3.1.4 Product Rule**

Let us first investigate why the product rule should be true. The product rule in terms of probabilities states that


Here _AB_ denotes the event _A ∩ B_ . Should our plausibilities satisfy a similar inequality? Let us first assume that the plausibility ( _AB|C_ ) should really be determined by the two plausibilities ( _B|C_ ) and ( _A|BC_ ). This is basically because the process of deciding that _AB_ is true can be broken down into first deciding whether _B_ is true and then, having accepted _B_ as true, deciding whether _A_ is true. We shall therefore assume that there should be a function _F_ such that


We also assume that we should use the same function _F_ for all possible events _A, B, C_ (i.e., we are not using one function _F_ for some _A, B, C_ while calculating ( _AB|C_ ) from ( _B|C_ ) and ( _A|BC_ ) and using another function _F_ for different _A, B, C_ ). This means in particular that


It is also reasonable to assume that _F_ ( _x, y_ ) is monotone increasing in each of its arguments and that it is continuous. If it is not continuous, then a small change in ( _B|C_ ) (or ( _A|BC_ )) might lead to a large change in ( _AB|C_ ) which is undesirable.

Now if we have four events _A, B, C, D_ , we can write


We can also write


16

We shall now make the following important consistency assumption: **If a plausibility can be calculated via two different methods, then both methods should give the same answer** . Clearly if this assumption were violated, then our answer to a plausibility calculation would depend on the specific method chosen to calculate and this would be highly undesirable. This assumption immediately implies that


for all _A, B, C, D_ . If the individual plausibilities are arbitrary, we would get the following condition that the function _F_ should satisfy


It now turns out the only functions _F_ which satisfy the above equation are of the form


for a positive continuous increasing function _w_ . I will skip this derivation (see Section 2.1, Chapter 2 of Jaynes [1]). We thus have


This is equivalent to


Now if we take _B_ = _A_ , we get


The event _A|AC_ can be seen as certainty so we get


for all _A_ and _C_ . This can happen only if


Also if we take _B_ = _A_<sup>_c_</sup> in (8), we get


_AA_<sup>_c_</sup> _|C_ and _A|A_<sup>_c_</sup> _C_ can both be taken to represent impossibility so we get

_w_ (impossible) = _w_ ( _A_<sup>_c_</sup> _|C_ ) _w_ (impossible)

for all _A_ and _C_ which gives


(9) and (10), along with the monotonicity of _w_ , imply


We have thus proved that _w_ ( _A|B_ ) lies always between 0 and 1 (is 0 for impossibility and 1 for certainty) and it satisfies the product rule of probability:


In other words, if we apply this this function _w_ to our plausibilities, then the resulting assignments satisfy the first two rules of probability.

17

#### **3.1.5 Sum Rule**

Below we shall sketch the argument for the sum rule of probability (the full details can be found in Section 2.2 of Jaynes [1]). For a proposition _A_ , we denote its complement by _A_<sup>_c_</sup> (i.e., _A_<sup>_c_</sup> refers to the proposition that _A_ is not true). Suppose that the plausibility _w_ ( _A_<sup>_c_</sup> _|C_ ) should be a function of _w_ ( _A|C_ ):


This is intuitively meaningful as the plausibility of _A_<sup>_c_</sup> should be determined by the plausibility of _A_ . We also assume that we use the same function _S_ for every _A, C_ . This function _S_ maps [0 _,_ 1] to [0 _,_ 1] and it should be a self-reciprocal function because _S_ ( _S_ ( _w_ ( _A|C_ ))) = _S_ ( _w_ ( _A_<sup>_c_</sup> _|C_ )) = _w_ ( _A|C_ ) i.e., _S_ ( _S_ ( _x_ )) = _x_ or _S_<sup>_−_1</sup> ( _x_ ) = _S_ ( _x_ ). It should also satisfy (by taking _A_ to be certainty) _S_ (1) = 0.

There is another condition that _S_ needs to satisfy as a consequence of the fact that _w_ ( _A|B_ ) satisfies the product rule. For three propositions _A, B, C_ , we have


Switching _A_ and _B_ , we get

We thus have


for all _A, B, C_ .

Now suppose _A_ and _B_ are such that _B_<sup>_c_</sup> is contained in _A_ (or equivalently _A_<sup>_c_</sup> is contained in _B_ ). This means that whenever _B_<sup>_c_</sup> is true, _A_ is also true. So we have _AB_<sup>_c_</sup> = _B_<sup>_c_</sup> and _A_<sup>_c_</sup> _B_ = _A_<sup>_c_</sup> . Thus


which is equivalent to


The above equation should be true for all _A, B, C_ such that _B_<sup>_c_</sup> is contained in _A_ . Letting _x_ = _w_ ( _A|C_ ), _y_ = _w_ ( _B|C_ ) so that _S_ ( _y_ ) = _w_ ( _B_<sup>_c_</sup> _|C_ ) _≤ w_ ( _A|C_ ) = _x_ , we thus have


One can then show that the above condition implies that


for some _α >_ 0. This argument is somewhat technical and you can read it in Jaynes [1, Section 2.2].

We have thus proved that


18

which is equivalent to


It can now be noted that the rules (9), (10), (11) and (12) that _w_ ( _A|B_ ) satisfies are also satisfied by _w_<sup>_α_</sup> ( _A|B_ ). Thus _w_<sup>_α_</sup> ( _A|B_ ) satisfies all the three rules

1. 0 _≤ w_<sup>_α_</sup> ( _A|B_ ) _≤_ 1, _w_<sup>_α_</sup> (impossible) = 0, and _w_<sup>_α_</sup> (certain) = 1,

2. _w_<sup>_α_</sup> ( _AB|C_ ) = _w_<sup>_α_</sup> ( _A|C_ ) _w_<sup>_α_</sup> ( _B|AC_ ) = _w_<sup>_α_</sup> ( _B|C_ ) _w_<sup>_α_</sup> ( _A|BC_ ), and

3. _w_<sup>_α_</sup> ( _A_<sup>_c_</sup> _|C_ ) + _w_<sup>_α_</sup> ( _A|C_ ) = 1.

We shall therefore denote _w_<sup>_α_</sup> by P and call it probability. P then satisfies the rules:

1. 0 _≤_ P( _A|B_ ) _≤_ 1, P(impossible) = 0, and P(certain) = 1,

2. **Product Rule** : P( _AB|C_ ) = P( _A|C_ )P( _B|AC_ ) = P( _B|C_ )P( _A|BC_ ), and

3. **Sum Rule** : P( _A_<sup>_c_</sup> _|C_ ) + P( _A|C_ ) = 1.

Note that these usual laws of probability hold because of the need for logical consistency and not because our probability has anything to do with frequencies.

The sum rule of probability is usually stated as


where _A ∪ B_ denotes the proposition “at least one of _A_ and _B_ is true” (Jaynes uses the notation _A_ + _B_ for _A ∪ B_ ). (14) can be derived from the stated rules as

P( _A ∪ B|C_ ) = 1 _−_ P(( _A ∪ B_ )<sup>_c_</sup> _|C_ ) = 1 _−_ P( _A_<sup>_c_</sup> _∩ B_<sup>_c_</sup> _|C_ ) = 1 _−_ P( _B_<sup>_c_</sup> _|A_<sup>_c_</sup> _C_ )P( _A_<sup>_c_</sup> _|C_ ) = 1 _−_ (1 _−_ P( _B|A_<sup>_c_</sup> _C_ )) P( _A_<sup>_c_</sup> _|C_ ) = 1 _−_ P( _A_<sup>_c_</sup> _|C_ ) + P( _B|A_<sup>_c_</sup> _C_ )P( _A_<sup>_c_</sup> _|C_ ) = P( _A|C_ ) + P( _A_<sup>_c_</sup> _B|C_ ) = P( _A|C_ ) + P( _B|C_ )P( _A_<sup>_c_</sup> _|BC_ ) = P( _A|C_ ) + P( _B|C_ )(1 _−_ P( _A|BC_ ))

- = P( _A|C_ ) + P( _B|C_ ) _−_ P( _B|C_ )P( _A|BC_ ) = P( _A|C_ ) + P( _B|C_ ) _−_ P( _AB|C_ ) _._

---

[← 2 Lecture Two](03-2-lecture-two.md) · [Up: contents](index.md) · [4 Lecture Four →](05-4-lecture-four.md)
