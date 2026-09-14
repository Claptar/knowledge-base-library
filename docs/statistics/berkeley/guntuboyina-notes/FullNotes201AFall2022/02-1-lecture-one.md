---
title: 1 Lecture One
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Lecture One

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 What is Probability Theory?**

Probability theory is what one should use when reasoning in the presence of uncertainty.

### **1.2 How does Probability Theory work?**

Suppose we are interested in knowing whether a certain proposition is true. Suppose that we do not have access to full information that would allow us to conclusively determine whether the proposition is true or not. Probability theory allows us to determine a number between 0 and 1 representing how likely it is that the proposition is true based on the available information. This is achieved by the following two steps:

1. **Step One** : The available information that we either possess or that we assume for the sake of argument is converted into **numerical assignments** for the probabilities of certain basic or elementary propositions. This step is often referred to as the **modeling** step.

2. **Step Two** : Based on the probability model, we calculate probabilities of the propositions of interest using the **rules of probability** .

4

### **1.3 Rules of Probability**

Probabilities are assigned to propositions (also known as events). Every probability is conditional on some information (this could be available information or some information that we assume for the sake of argument). We shall denote the probability of a proposition _A_ conditioned on some information _I_ by P( _A | I_ ). When the information _I_ is clear from context, we sometimes omit it and write the probability P( _A | I_ ) as simply P( _A_ ). Even when we do this, it should always be kept in mind that probabilities are always conditioned on some information.

1. The probability of a proposition always lies between 0 and 1. The probability of an impossible proposition is 0 and the probability of a certain proposition is 1.

2. **Product Rule** : P( _A ∩ B | I_ ) = P( _A | I_ )P( _B | A, I_ ) = P( _B | I_ )P( _A | B, I_ ). Here _A ∩ B_ is the proposition: “both _A_ and _B_ are true”. Also P( _A | B, I_ ) is the probability of _A_ conditioned on the truth of the proposition _B_ as well as the information _I_ . A direct consequence of the product rule is:


The above formula is known as the Bayes rule.

3. **Sum Rule** : P( _A ∪ B | I_ ) = P( _A | I_ ) + P( _B | I_ ) for disjoint propositions _A_ and _B_ . Here _A ∪ B_ denotes the proposition: “at least one of _A_ and _B_ is true”.

We shall see some justification for these rules later.

### **1.4 Example 1: Testing and Covid**

**Problem 1.1.** _Suppose I just tested positive for Covid. Do I really have Covid?_

This is a situation involving uncertainty mainly because the test may not be 100% accurate. In other words, my result could be a false positive. I need to calculate

P _{_ I have Covid _|_ I tested positive+other background information _}_

which we abbreviate as P( _C |_ + _, B_ ) for simplicity of notation. Here _B_ denotes relevant background information that I may have. For example, _B_ could include things like “I have been strictly quarantining for the past 3 weeks” etc.

We can attempt to calculate P( _C |_ + _, B_ ) as:


where we used the product rule and sum rule of probability. Here _C_<sup>_c_</sup> denotes the proposition that I do not have Covid.

In order to proceed further, we need some probability assignment. Consider the following assignment:


P( _C | B_ ) represents the probability of Covid based on background information alone. The fact that it is low (0 _._ 02) is meaningful when I know that I have been largely isolating myself

5

for the past few weeks. With this assignment, we can calculate the required probability P( _C |_ + _, B_ ) as follows:


Note that 0 _._ 3356 (33 _._ 56%) is not very high even though the test has very good false positive and false negative rates. This is because P( _C | B_ ) (which can be interpreted as probability of having Covid without taking into the account the test result) is very low (0 _._ 02).

Here is an alternative method of reasoning in this problem. We formulate this as a hypothesis testing problem with


The _p_ -value in the above testing problem equals:


Usage of the naive cutoff 0 _._ 05 on the _p_ -value would now lead to rejection of the null hypothesis and declaring that I have Covid. On the other hand, the previous argument (based on probability theory) gave a much higher probability to me not having Covid. This _p_ -value based method does not even make use of the information given on P( _C | B_ ) and P(+ _|C, B_ ). It only makes use of P(+ _|C_<sup>_c_</sup> ). Note that what we are after is P( _C_<sup>_c_</sup> _|_ +) (or P( _C|_ +)). In general, P( _A|B_ ) and P( _B|A_ ) can be quite different. Consider, for example, the case where _A_ represents the event that a person is dead and _B_ represents the event that they were hanged. It is therefore quite problematic that one can say something about _C|_ + or _C_<sup>_c_</sup> _|_ + from knowledge of P(+ _|C_<sup>_c_</sup> ) alone.

Methods such as testing based on _p_ -values (and putting arbitrary cutoffs on them) are not based on probability theory. The use of _p_ -values has been linked to serious issues such as lack of reproducibility. In this context, we can calculate the probability of reproducibility of the positive test:


Here +2 denotes the proposition that the second test results in a positive (and +1 denotes the proposition that the first test resulted in a positive). We now make the following probability assignment:


This assumption means that conditional on my Covid status, the two tests are independent. Using this assignment, it is straightforward to calculate the reproducibility probability as follows (note that we already calculated P( _C |_ +1 _, B_ ) = 1 _−_ P( _C_<sup>_c_</sup> _|_ +1 _, B_ ) = 0 _._ 3356)


Thus this positive test wil be reproducible with probability only 35.88%.

### **1.5 Example 2: Spots on a patient**

**Problem 1.2** (From the book “A tutorial introduction to Bayesian Analysis” by James Stone) **.** _Suppose you are a doctor confronted with a patient who is covered in spots. Ths_

6

_patient’s symptoms are consistent with chickenpox but they are also consistent with another, more dangerous, disease, smallpox. How would you decide if they have chickenpox or smallpox?_

This is again a situation involving uncertainty as the doctor does not know which disease the patient has. The doctor needs to calculate the probability:


where _B_ again represents background information. For example, _B_ could represent any other symptoms that the patient has such as fever. Here is one probability assignment which allows us to calculate this probability:


and

P _{_ smallpox _| B}_ = 0 _._ 001 P _{_ chickenpox _| B}_ = 0 _._ 1 P _{_ neither _| B}_ = 0 _._ 899 _._ (4)

Here “neither” refers to an underlying cause for the patient’s condition that is neither smallpox nor chickenpox.

Using this assignment, the required probability (2) can be calculated via Bayes rule and this leads to

P _{_ smallpox _|_ spots _, B} ≈_ 0 _._ 011 P _{_ chickenpox _|_ spots _, B} ≈_ 0 _._ 988 P _{_ neither _|_ spots _, B}_ = 0 _._

So probability theory with the assignment (3) and (4) says that it is highly likely that the patient has chickenpox (smallpox is basically ruled out because it is extremely rare).

Here is an alternative way of solving this problem using maximum likelihood estimation. The maximum likelihood estimate in this case is smallpox because smallpox leads to a higher probability (0.9) of the observed data (spots) compared to chickenpox (0.8). Maximum Likelihood (widely used in statistics) is not based on probability theory and also seems to be based on the wrong conditional probabilities P _{_ spots _|_ smallpox _}_ and P _{_ spots _|_ chickenpox _}_ while we really should be calculating P _{_ smallpox _|_ spots _}_ and P _{_ chickenpox _|_ spots _}_ .

---

[← Contents](01-contents.md) · [Up: contents](index.md) · [2 Lecture Two →](03-2-lecture-two.md)
