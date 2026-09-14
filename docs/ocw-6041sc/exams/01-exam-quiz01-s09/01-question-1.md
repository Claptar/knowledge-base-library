---
title: Question 1
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/01-exam-quiz01-s09.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 1

**Source:** `exams/01-exam-quiz01-s09.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Multiple Choice Questions: **CLEARLY** circle the appropriate choice. Scratch paper is available if needed, though **NO** partial credit will be given for the Multiple Choice.

- a. Which of the following statements is NOT true?

   - (i) If _A ⊂ B_ , then **P** ( _A_ ) _≤_ **P** ( _B_ ).

   - (ii) If **P** ( _B_ ) _>_ 0, then **P** ( _A|B_ ) _≥_ **P** ( _A_ ).

   - (iii) **P** ( _A ∩ B_ ) _≥_ **P** ( _A_ ) + **P** ( _B_ ) _−_ 1.

   - (iv) **P** ( _A ∩ B_<sup>_c_</sup> ) = **P** ( _A ∪ B_ ) _−_ **P** ( _B_ ).

- b. We throw _n_ identical balls into _m_ urns at random, where each urn is equally likely and each throw is independent of any other throw. What is the probability that the _i_ -th urn is empty?


- c. We toss two fair coins simultaneously and independently. If the outcomes of the two coins are the same, we win; otherwise, we lose. Let _A_ be the event that the first coin comes up heads, _B_ be the event that the second coin comes up heads, and _C_ be the event that we win. Which of the following statements is false?

   - (i) Events _A_ and _B_ are independent.

   - (ii) Events _A_ and _C_ are _not_ independent.

   - (iii) Events _A_ and _B_ are _not_ conditionally independent given _C_ .

   - (iv) The probability of winning is 1/2.

- d. For a biased coin, the probability of “heads” is 1/3. Let _h_ be the number of heads in five independent coin tosses. What is the probability **P** (first toss is a head _| h_ = 1 or _h_ = 5)?

> <u>13 ( 23 )</u><sup>4</sup> (i) 5 <u>13</u> ( <u>23</u> )<sup>4</sup> +( <u>13</u> )<sup>5</sup>

> <u>13 ( 23 )</u><sup>4</sup> (ii) <u>1 2 1</u> 3 ( 3 )<sup>4</sup> +( 3 )<sup>5</sup>

> <u>13 ( 23 )</u><sup>4</sup> +( <u>13 )</u><sup>5</sup> (iii) 5<sup><u>1</u></sup> 3 (<sup><u>2</u></sup> 3 )<sup>4</sup> +( 31 )<sup>5</sup> (iv) <u>15</u>

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Quiz 1 | Spring 2009)

- e. A well-shuffled deck of 52 cards is dealt evenly to two players (26 cards each). What is the probability that player 1 gets all the aces?

> 0 48 1

> <u>@</u> 22 <u>A</u> 52 (i)<sup><u>0</u></sup> <u>1</u>

> @ 26 A

> 0 48 1 22 4<sup><u>@</u></sup> <u>A</u> 52 (ii)<sup><u>0</u></sup> <u>1</u>

> <u>@</u> 26 A (iii)<sup><u>48!</u></sup> 22!<sup><u>52!</u></sup> 26!

> 0 48 1 22 4!<sup><u>@</u></sup> <u>A</u> (iv) 52 <u>0 1</u>

> @ 26 A

- f. Suppose _X, Y_ and _Z_ are three independent discrete random variables. Then, _X_ and _Y_ + _Z_ are

   - (i) always

(ii) sometimes

(iii) never

independent.

- g. To obtain a driving licence, Mina needs to pass her driving test. Every time Mina takes a driving test, with probability 1 _/_ 2, she will clear the test independent of her past. Mina failed her first test. Given this, let _Y_ be the additional number of tests Mina takes before obtaining a licence. Then,

   - (i) _E_ [ _Y_ ] = 1.

(ii) _E_ [ _Y_ ] = 2.

(iii) _E_ [ _Y_ ] = 0.

- h. Consider two random variables _X_ and _Y_ , each taking values in _{_ 1 _,_ 2 _,_ 3 _}_ . Let their joint PMF be such that for any 1 _≤ x, y ≤_ 3,


Then,

- (i) _X_ and _Y_ can be independent or dependent depending upon the _strictly positive_ values.

- (ii) _X_ and _Y_ are always independent.

- (iii) _X_ and _Y_ can never be independent.

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Quiz 1 | Spring 2009)

- i. Suppose you play a _matching coins_ game with your friend as follows. Both you and your friend have a coin. Each time, you two reveal a side (i.e. H or T) of your coin to each other simulta­ neously. If the sides match, you WIN a 1 from your friend and if sides do not match then you lose a 1 to your friend. Your friend has a complicated (unknown) strategy in selecting the sides over time. You decide to go with the following simple strategy. Every time, you will toss your unbiased coin independently of everything else, and you will reveal its outcome to your friend (of course, your friend does not know the outcome of your random toss until you reveal it). Then,

   - (i) On average, you will lose money to your smart friend.

   - (ii) On average, you will neither lose nor win. That is, your average gain/loss is 0.

   - (iii) On average, you will make money from your friend.

- j. Let _Xi,_ 1 _≤ i ≤_ 4 be independent Bernoulli random variable each with mean _p_ = 0 _._ 1. Let _X_ =<sup>�</sup> 4 _i_ =1<sup>_Xi_.Thatis,</sup><sup>_X_isaBinomialrandomvariablewithparameters</sup><sup>_n_=4and</sup><sup>_p_=0</sup><sup>_._1.</sup> Then,

   - (i) _E_ [ _X_ 1 _|X_ = 2] = 0 _._ 1.

   - (ii) _E_ [ _X_ 1 _|X_ = 2] = 0 _._ 5.

   - (iii) _E_ [ _X_ 1 _|X_ = 2] = 0 _._ 25.

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Spring 2009)

---

[Up: contents](index.md) · [Question 2 →](02-question-2.md)
