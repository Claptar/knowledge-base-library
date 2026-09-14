---
title: 2 Lecture Two
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Lecture Two

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall continue our discussion of the scope of probability theory with more examples.

### **2.1 Example 3: Prisoner’s dilemma**

The following is a standard problem (see, for example, Mosteller [4, Problem 13]).

**Example 2.1** (From Mosteller’s book (Problem 13; The Prisoner’s Dilemma)) **.** _Three prisoners, A, B, and C, with apparently equally good records have applied for parole. The parole board has decided to release two of the three, and the prisoners know this but not which two. The prisoner A has a friend who is the warder of the prison and who knows which prisoners will be released. Prisoner A realizes that it would be unethical to ask the warder if he, A, is to be released, but decides to ask for the name of one prisoner other than himself who is to be released. The warder says “B will be released”. What are the chances of A being released?_

7

We need to calculate

P _{A_ will be released _|_ Warder says B will be released _} ._

By the product rule of probability, the above probability is the same as


To calculate the numerator, it is natural to make the assignment

P _{_ A and B will be released _}_ = P _{_ B and C will be released _}_ = P _{_ A and C will be released _}_ = 1 _/_ 3 _._

For the denominator, we can split as

P _{_ Warder says B will be released _}_

- = P _{_ Warder says B will be released _|_ A and B will be released _}_ P _{_ A and B will be released _}_

- + P _{_ Warder says B will be released _|_ B and C will be released _}_ P _{_ B and C will be released _}_

- + P _{_ Warder says B will be released _|_ A and C will be released _}_ P _{_ A and C will be released _}_

- = 1 _×_<sup>1</sup> 3<sup>+ P</sup><sup>_{_WardersaysBwillbereleased</sup><sup>_|_BandCwillbereleased</sup><sup>_} ×_1</sup> 3<sup>+ 0</sup><sup>_×_1</sup> 3

- =<sup>1</sup> 3<sup>+1</sup> 3<sup>P</sup><sup>_{_WardersaysBwillbereleased</sup><sup>_|_BandCwillbereleased</sup><sup>_} ._</sup>

To proceed further, we need a probability assignment for

P _{_ Warder says B will be released _|_ B and C will be released _}_

It is natural to assume that this probability equals 0 _._ 5. This means that, in the event that _B_ and _C_ are the two prisoners who will be released, the warder is equally likely to reveal the name of _B_ or _C_ to _A_ . Under this assumption, we have


leading to


Note that this means that prisoner A’s chances of being released remain the same in spite of the additional information revealed by the warder.

Here is an interesting wrinkle on this problem. Suppose that the conversation between the prisoner _A_ and the Warder was overheard by prisoner _C_ who then proceeds to calculate his own chances of being released in light of the additional information.


The denominator is the same as before so it will be 1 _/_ 2. For the numerator, note that _C_ will be released either with _A_ or with _B_ . The case where _C_ and _A_ will be released is ruled out because the Warder said “B will be released”. So the numerator equals:

P _{_ C and B will be released, Warder says B will be released _}_

- = P _{_ Warder says B will be released _|_ B and C will be released _}_ P _{_ B and C will be released _}_

- =<sup>1</sup> 2<sup>_×_1</sup> 3<sup>=1</sup> 6

   - 6<sup>_._</sup>

Therefore the probability of C’s release given the additional information is (1 _/_ 6) _/_ (1 _/_ 2) = 1 _/_ 3. The additional information therefore significantly reduces the chances of _C_ ’s release (from 2 _/_ 3 to 1 _/_ 3).

8

### **2.2 Example 4: Monty Hall Problems**

**Example 2.2** (Monty Hall Problem) **.** _Suppose you’re on a game show, and you’re given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what’s behind the doors, opens another door, say No. 3, which has a goat. He then says to you, “Do you want to pick door No. 2?” Is it to your advantage to switch your choice?_

Let us suppose that I always pick Door 1 to start the game. We then need to calculate the conditional probability:


which we can write as


We now make the following natural probability assignment:


and also


This leads to


and since this probability is more than 0.5, it makes sense for me to switch to door 2 from my original selction of door 1.

### **2.3 Example 5: MacKay sequence example**

The following application of probability theory can be seen as a way of formalizing common sense. Probability theory has been described by some (for example, Laplace) as an extension of common sense. Here is a quote by Laplace on this: _It is seen in this essay that the theory of Probabilities is at bottom only common sense reduced to calculus; it makes us appreciate with exactitude that which exact minds feel by a sort of instinct without being able ofttimes to give a reason for it._ –Laplace.

The application given below is from the book MacKay [5, Chapter 28].

**Problem 2.3.** _Find the next number in the sequence: −_ 1 _,_ 3 _,_ 7 _,_ 11 _._

Note that this is a problem of reasoning under uncertainty as we are uncertain about the way this sequence of numbers has been generated. One way of using probability theory to solve this problem is the following. We can have two models for the number generation mechanism here:

1. **Model 1** : Arithmetic Progression i.e., _a_ 1 = _α_ and _an_ +1 = _an_ + _β_ .

9

#### 2. **Model 2** : Random

Most people would look at the sequence and guess the next number as 15. In other words, they are using Model 1 (Arithmetic Progression). Probability theory can be used to justify this. We need to calculate


What probability assignments would we need to calculate the above? We can use the Bayes Rule to write


To be fair to each of the two models, we shall take


We now need to calculate P _{_ data _|_ Model _i}_ for _i_ = 1 _,_ 2. For _i_ = 1, we have (below _α_ and _β_ are the parameters in Model 1):


To calculate the above, we need to make a probability assignment for the probability with which _α_ and _β_ take various values. MacKay [5, Chapter 28] assumes that _α_ and _β_ are integervalued that they are independently uniformly distributed over the set _{−_ 50 _, −_ 49 _, . . . ,_ 49 _,_ 50 _}_ which has cardinality 101. Then


For the second model, we need to specify what we mean by “random”. We shall take this to mean that _a_ 1 _, a_ 2 _, a_ 3 _, a_ 4 are independently distributed according to the uniform distribution on _{−_ 50 _, −_ 49 _, . . . ,_ 49 _,_ 50 _}_ . Then


Plugging in the above value (as well as (6) and (7)) in (5), we get


This analysis clearly favors Model 1 compared to Model 2. The most interesting feature about this analysis is that


even though


In other words, we did not dogmatically assert that the data was generated by an arithmetic progression but we gave a fair chance to the two models to explain the observed sequence.

In this example, some people argue in favor of Model 1 on the basis that Model 1 is “simpler” than Model 2. Our analysis above (based on probability theory) does not invoke

10

any vague notion of simplicity but does some formal calculations which in this case preferred Model 1 to Model 2. In another situation, Model 2 may well be the preferred model.

One can consider other alternative models in this problem. For example, MacKay [5, Chapter 28] considered the following cubic model:

**Model 3 (Cubic)** : These numbers were generated by the formula: _a_ 1 = _a_ and _an_ +1 = _ba_<sup>3</sup> _n_<sup>+</sup><sup>_ca_2</sup> _n_<sup>+</sup><sup>_d_foraninteger</sup><sup>_a_andrationalnumbers</sup><sup>_b, c, d_.</sup>

This cubic model explains the given data perfectly if and only if its four parameters _a, b, c, d_ are chosen as _a_ = _−_ 1 _, b_ = _−_ 1 _/_ 11 _, c_ = 9 _/_ 11 _, d_ = 23 _/_ 11. As a result,


In order to explicitly calculate the above, we need to make probability assignments for _a, b, c, d_ . MacKay [5] makes the following probability assignment: we assume that these four parameters are independent with _a_ being uniform on _{−_ 50 _, −_ 49 _, . . . ,_ 49 _,_ 50 _}_ and _b, c, d_ having the distribution of _x/y_ where _x ∼_ Unif _{−_ 50 _, −_ 49 _, . . . ,_ 49 _,_ 50 _}_ and _y ∼_ Unif _{_ 1 _, . . . ,_ 50 _}_ are independent. Under this assignment:


In the above, we used P( _b_ = _−_ 1 _/_ 11) = 4 _·_ (1 _/_ 101) _·_ (1 _/_ 50) because _−_ 1 _/_ 11 = _−_ 2 _/_ 22 = _−_ 3 _/_ 33 = _−_ 4 _/_ 44 and each of these has the probability (1 _/_ 101) _·_ (1 _/_ 50). A similar reasoning is used for P _{c_ = 9 _/_ 11 _}_ and P _{d_ = 23 _/_ 11 _}_ .

If Model 1, 2, 3 are the only three models considered, the Bayes rule (5) becomes


where the denominator should be calculated as:


Under the fair assumption


we obtain


and


and


Our preference for Model 1 is still as strong as before (when we only considered the two models Model 1 and Model 2).

The analysis given here depends on the specific choices of priors used for the three models. One can of course use alternative priors but the qualitative preference for Model 1 is unlikely to change for most **reasonable** prior choices.

11

### **2.4 Interpretation of Probability**

There are multiple interpretations of probability and still some controversy regarding what probability really is. A proper understanding of the meaning of probability is very important for applications of probability to statistics and data analysis.

There are broadly two ways of understanding probability.

#### **2.4.1 Frequentist/Objective Understanding of Probability**

From the frequentist viewpoint, probability is applicable only in the context of “random experiments” (such as tossing coins and rolling dice). The probability P( _A_ ) of an event _A_ is defined as the relative frequency that _A_ occurs in _N_ repeated trials of the experiment in the limit as _N →∞_ :


where _nA_ is the number of trials out of _N_ where _A_ occurs. This definition of probability is the basis of frequentist statistics. Here are some examples:

1. The statement P( _H_ ) = 0 _._ 5 means that the proportion of heads in a large number of tosses of the coin approaches 0 _._ 5.

2. The statement


means that if the experiment generating _ϵ_ 1 _, . . . , ϵn_ is repeated a large number of times, the proportion of times the values of ( _ϵ_ 1 _, . . . , ϵn_ ) lie in a set _A_ approaches


and this should be true for all subsets _A_ of R<sup>_n_</sup> .

3. The statement


means that if we repeat the experiment generating the random variables _X_<sup>¯</sup> and _S_ a large number of times, then the proportion of times the interval


contains _θ_ approaches 0 _._ 95.

The following are some obvious problems with the frequentist definition:

1. It is very restrictive and hardly ever applicable. In many simple situations where we would like to use probability, the frequency definition is simply does not apply:

   - a) Is the suspect X guilty?

   - b) What is the chance of rain in Berkeley today?

   - c) What is the chance that Y is cancer positive given that they tested positive?

12

2. Even in situations where the frequency definition is seemingly applicable, closer thought might reveal some issues. For example, the frequentist probability that a coin comes up heads is 0.6 means that 60% of a large number of tosses of the coin should result in 0 _._ 6. But the mechanics of no two tosses are really identical and if two tosses are done exactly identically, then we would expect the same outcome by the laws of physics. So the term “identical and independent repetitions of an experiment” is ambiguous.

In the frequentist definition, probability is considered an intrinsic property of the object under investigation which is only accessible by an experiment generating samples of infinite size. The frequentist probability is also referred to as “objective probability”. The implication is that we cannot assign it arbitrarily because any probability assignment that does not agree with the frequency in infinite trials is wrong. Unfortunately, the actual frequentist probabililty is seldom known because one cannot generally observe a large number of repetitions of an experiment and so almost all probability assignments are wrong from the frequentist point of view. This is one way of understanding the statistics aphorism: “All models are wrong” (usually attributed to George Box; see `https://en.wikipedia.org/ wiki/All_models_are_wrong` ).

---

[← 1 Lecture One](02-1-lecture-one.md) · [Up: contents](index.md) · [3 Lecture Three →](04-3-lecture-three.md)
