---
title: Question 1
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/01-solutions-qu01-s09-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 1

**Source:** `solutions/01-solutions-qu01-s09-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Multiple Choice Questions: **CLEARLY** circle the appropriate choice. Scratch paper is available if needed, though **NO** partial credit will be given for the Multiple Choice. **Each multiple choice question is worth 4 points** .

- a. Which of the following statements is NOT true?

   - (i) If _A ⊂ B_ , then **P** ( _A_ ) _≤_ **P** ( _B_ ).

   - (ii) If **P** ( _B_ ) _>_ 0, then **P** ( _A|B_ ) _≥_ **P** ( _A_ ).

   - (iii) **P** ( _A ∩ B_ ) _≥_ **P** ( _A_ ) + **P** ( _B_ ) _−_ 1.

(iv) **P** ( _A ∩ B_<sup>_c_</sup> ) = **P** ( _A ∪ B_ ) _−_ **P** ( _B_ ).

**Solution:** A counterexample: if we have two events _A_ , _B_ such that _P_ ( _B_ ) _>_ 0 and _P_ ( _A_ ) _>_ 0, but _A ∩ B_ = _φ_ , then _P_ ( _A|B_ ) = 0, but _P_ ( _A_ ) _> P_ ( _A|B_ ). It’s easy to come up with examples like this: for example, take any sample space with event _A_ such that _P_ ( _A_ ) _>_ 0, and _P_ ( _A_<sup>_c_</sup> _>_ 0), it follows that _P_ ( _A|A_<sup>_c_</sup> ) = 0, but _P_ ( _A_ ) _>_ 0.

- b. We throw _n_ identical balls into _m_ urns at random, where each urn is equally likely and each throw is independent of any other throw. What is the probability that the _i_ -th urn is empty?


**Solution:** The probability of the _j_ th ball going into the _i_ th urn is 1 _/m_ . Hence, the probability of the _j_ th ball not going into the _i_ th urn is (1 _−_ 1 _/m_ ). Since all throws are independent from one another, we can multiply these probabilities: the probability of all _n_ balls not going into the <u>1</u><sup>_n_</sup> . _i_ th urn, i.e. it is empty, is �1 _− m_ �

- c. We toss two fair coins simultaneously and independently. If the outcomes of the two coin tosses are the same, we win; otherwise, we lose. Let _A_ be the event that the first coin comes up heads, _B_ be the event that the second coin comes up heads, and _C_ be the event that we win. Which of the following statements is true?

   - (i) Events _A_ and _B_ are not independent.

   - (ii) Events _A_ and _C_ are independent.

   - (iii) Events _A_ and _B_ are conditionally independent given _C_ .

   - (iv) The probability of winning is 3/4.

**Solution:** The sample space in this case is Ω = _{_ ( _H, H_ ) _,_ ( _H, T_ ) _,_ ( _T, H_ ) _,_ ( _T, T_ ) _}_ . The prob­ ability law is a uniform distribution over this space. We have _A_ = _{_ ( _H, H_ ) _,_ ( _H, T_ ) _}_ , _B_ = _{_ ( _H, H_ ) _,_ ( _T, H_ ) _}_ , and _C_ = _{_ ( _H, H_ ) _,_ ( _T, T_ ) _}_ . By the discrete uniform law, _P_ ( _A_ ) = _P_ ( _B_ ) =

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

_P_ ( _C_ ) = 1 _/_ 2. We also have _P_ ( _A ∩ C_ ) = 1 _/_ 4, hence _P_ ( _A ∩ C_ ) = _P_ ( _A_ ) _P_ ( _C_ ), and the two events are independent. Intuitively, knowing that you won adds no information about whether your coin turned up heads or not: stating this formally, we have _P_ ( _A|C_ ) = _P_ ( _A_ ).

- d. For a biased coin, the probability of “heads” is 1/3. Let _H_ be the number of heads in five independent coin tosses. What is the probability **P** (first toss is a head _| H_ = 1 or _H_ = 5)?


<!-- Start of picture text -->
13 ( 23 )4<br>(i) 1 2 1<br>5 3 ( 3 ) 4 +( 3 ) 5<br>13 ( 23 )4<br>(ii) 1 2 1<br>3 ( 3 ) 4 +( 3 ) 5<br>13 ( 23 ) 4 +( 13 ) 5<br>(iii) 1 2 1<br>5 3 ( 3 ) 4 +( 3 ) 5<br>(iv) 1 5<br><!-- End of picture text -->

**Solution:** Let _A_ be the event that the first toss is a head.


- e. A well-shuffled deck of 52 cards is dealt evenly to two players (26 cards each). What is the probability that player 1 gets all the aces?


<!-- Start of picture text -->
0 48 1<br>22<br>@ A = 26 × 25 × 24 × 23<br>(i) 52 52 × 51 × 50 × 49<br>0 1<br>@ 26 A<br>0 48 1<br>22<br>4 @ A<br>(ii) 52 = 4 × 26 52 × × 25 51 × × 24 50 × × 23 49<br>0 1<br>@ 26 A<br>(iii) 48! 22! 52!26!<br>0 48 1<br>22<br>4! @ A 26 × 25 × 24 × 23<br>(iv)<br>52<br>0 1 = 4! × 52 × 51 × 50 × 49<br>@ 26 A<br><!-- End of picture text -->

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

**Solution:** Let _A_ be the event that player 1 gets all aces. By the disrete uniform law,


_|_ Ω _|_ = ��5226 is the number of hands (26 cards from 52) player 1 can have. Additionally, once we have given player 1 all aces, then they must be given an additional 22 cards from the remaining 48 cards in the deck. Hence,


- f. Suppose _X, Y_ and _Z_ are three independent discrete random variables. Then, _X_ and _Y_ + _Z_ are

   - (i) always

   - (ii) sometimes

(iii) never

independent.

**Solution:** Since _X_ is independent of _Y_ and _Z_ , _X_ is independent of _g_ ( _Y, Z_ ) for any function _g_ ( _Y, Z_ ), including _g_ ( _Y, Z_ ) = _Y_ + _Z_ (see page 114 of the book).

- g. To obtain a driving licence, Mina needs to pass her driving test. Every time Mina takes a driving test, with probability 1 _/_ 2, she will clear the test independent of her past. Mina failed her first test. Given this, let _Y_ be the additional number of tests Mina takes before obtaining a licence. Then,

   - (i) _E_ [ _Y_ ] = 1.


(iii) _E_ [ _Y_ ] = 0.

**Solution:** _Y_ is defined as the number of additional tests Mina takes, so this is independent of the fact that she failed her first test. _Y_ is a geometric RV with _p_ = 1 _/_ 2. Hence, _E_ [ _Y_ ] = 1 _/p_ = 2.

- h. Consider two random variables _X_ and _Y_ , each taking values in _{_ 1 _,_ 2 _,_ 3 _}_ . Let their joint PMF be such that for any 1 _≤ x, y ≤_ 3, _PX,Y_ ( _x, y_ ) = 0 if ( _x, y_ ) _∈{_ (1 _,_ 3) _,_ (2 _,_ 1) _,_ (3 _,_ 2) _}_ , and _PX,Y_ ( _x, y_ ) _>_ 0 if ( _x, y_ ) _∈{_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ (3 _._ 3) _}_ . Then,

   - (i) _X_ and _Y_ can be independent or dependent depending upon the values of _PX,Y_ ( _x, y_ ) for ( _x, y_ ) _∈{_ (1 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 2) _,_ (2 _,_ 3) _,_ (3 _,_ 1) _,_ (3 _._ 3) _}_ .

   - (ii) _X_ and _Y_ are always independent.

   - (iii) _X_ and _Y_ can never be independent.

**Solution:** If, for example, we are given information that _X_ = 1, we know that _Y_ can never take value 3. However, without this information about _X_ the probability _pY_ (3) is strictly positive and so _pY |X_ ( _y|x_ ) = _pY_ ( _y_ ), for _x_ = 1 and _y_ = 3, i.e. _X_ and _Y_ can never be independent.

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

- i. Suppose you play a _matching coins_ game with your friend as follows. Both you and your friend each have your own coin. Each time, the two of you reveal a side (i.e. H or T) of your coin to each other simultaneously. If the sides match, you WIN $1 from your friend and if sides do not match then you lose $1 to your friend. Your friend has a complicated (unknown) strategy in selecting the sides over time. You decide to go with the following simple strategy. Every time, you will toss your unbiased coin independently of everything else, and you will reveal its outcome to your friend (of course, your friend does not know the outcome of your random toss until you reveal it). Then,

   - (i) On average, you will lose money to your smart friend.

   - (ii) On average, you will neither lose nor win. That is, your average gain/loss is 0.

   - (iii) On average, you will make money from your friend.

**Solution:** Let _Xi_ be a random variable denoting your winnings at the _i_ ’th round of the game, i.e., _Xi_ = 1 if you win, _Xi_ = _−_ 1 if you lose. At each round your friend chooses either heads or tails, using some strategy that you don’t know about. The key property is that _for any choice that you friend makes, we have pXi_ (1) = _pXi_ ( _−_ 1) = 0 _._ 5: i.e., we always have a 0 _._ 5 probability that our coin toss will match the choice made by our friend. It can be verified that **E** [ _Xi_ ] = 0, and hence your average gain/loss is 0.

- j. Let _Xi,_ 1 _≤ i ≤_ 4 be independent Bernoulli random variables each with mean _p_ = 0 _._ 1. Let _X_ = �4 _i_ =1<sup>_Xi_.Then,</sup> (i) _E_ [ _X_ 1 _|X_ = 2] = 0 _._ 1.

- (ii) _E_ [ _X_ 1 _|X_ = 2] = 0 _._ 5.

(iii) _E_ [ _X_ 1 _|X_ = 2] = 0 _._ 25.

**Solution:** We have _P_ ( _X_ 1 = 1 _|X_ = 2) = 0 _._ 5, because


(Note that ��<sup>4</sup> 2 _p_<sup>2</sup> (1 _− p_ )<sup>2</sup> is the probability of seeing 2 heads out of 4 tosses, and ��1<sup>3</sup> _p_ (1 _− p_ )<sup>2</sup> is the probability of seeing 1 head in the last 3 tosses.) Hence,

**E** [ _X_ 1 _|X_ = 2] = 1 _× P_ ( _X_ 1 = 1 _|X_ = 2) + 0 _× P_ ( _X_ 1 = 0 _|X_ = 2) = 0 _._ 5

4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

---

[Up: contents](index.md) · [Question 2 →](02-question-2.md)
