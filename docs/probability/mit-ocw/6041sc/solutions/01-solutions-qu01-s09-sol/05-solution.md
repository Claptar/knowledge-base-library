---
title: Solution
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/01-solutions-qu01-s09-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** `solutions/01-solutions-qu01-s09-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (c) (2 points) Are _X_ and _Y_ independent?

**Solution:** No. One of many counter examples: _pX_ ( _x_ ) does not equal _pX|Y_ ( _x|_ 2).

7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

Zach and Wendy are intrigued by Xavier and Yvonne’s dice. They visit the store and buy a pair of dice of their own. Again, each of them picks a die in the pair; one of them then rolls the two dice together. Let _Z_ be the outcome of Zach’s die and _W_ the outcome of Wendy’s die. The joint PMF of _Z_ and _W_ , _pZ,W_ ( _z, w_ ), is given by the following figure:


<!-- Start of picture text -->
4 2 1 2 1<br>24 24 24 24<br>3 2 1 2 1<br>24 24 24 24<br>W 2 2 1 2 1<br>24 24 24 24<br>1 2 1 2 1<br>24 24 24 24<br>1 2 3 4<br>Z<br><!-- End of picture text -->

The store also sells a variety of magic coins, some fair and some crooked. Alice buys a coin that on each toss comes up heads with probability 3 _/_ 4.

- (d) (5 points) Wondering whether to buy some dice as well, Alice decides to try out her friends’ dice first. She does the following. First, she tosses her coin. If the coin comes up heads, she borrows Xavier and Yvonne’s dice pair and rolls the two dice. If the coin comes up tails, she borrows Zach and Wendy’s dice pair and rolls those instead. What is the probability that she rolls a double, i.e., that both dice in the pair she rolls show the same number?

**Solution:** Let event D be the set of all doubles, and let event A be the event that Alice’s coin toss results in heads. Using the law of total probability:


8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

- (e) (5 points) Alice has still not made up her mind about the dice. She tries another experiment. First, she tosses her coin. If the coin comes up heads, she takes Xavier and Yvonne’s dice pair and rolls the dice repeatedly until she gets a double; if the coin comes up tails, she does the same with Zach and Wendy’s dice. What is the expected number of times she will need to roll the dice pair she chooses? (Assume that if a given pair of dice is rolled repeatedly, the outcomes of the different rolls are independent.)

**Solution:** Let random variable _N_ be the number of rolls until doubles is rolled. The distribution on _N_ condition on the set of dice being rolled is a geometric random variable. Using the total expectation theorem, the expected value of N is:


- (f) (5 points) Alice is bored with the dice and decides to experiment with her coin instead. She tosses the coin until she has seen a total of 11 heads. Let _R_ be the number of tails she sees. Find **E** [ _R_ ]. (Assume independent tosses.)

**Solution:** The time _T_ until Alice sees a total of 11 heads is the sum of 11 independent and identically distributed geometric random variables with parameter _p_ =<sup><u>3</u></sup> 4<sup>.Randomvariable</sup><sup>_R_,</sup> the number of tails she sees, is _T −_ 11. Thus:


9

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

- (g) (5 points) Alice tries another experiment with her coin. Let _A_ be the event that the second head she sees occurs on the 7th coin toss, and let _S_ be the position of the first head. Find the conditional PMF of _S_ given the event _A_ , _pS|A_ ( _s_ ).

**Solution:** The probability of event A can be found by choosing one of the first 6 outcomes to be a head, the others tails, and then the outcome of the 7th toss to be head, which is ��<sup>6</sup> 1 (1 _− p_ )<sup>5</sup> _p_<sup>2</sup> , where _p_ =<sup><u>3</u></sup> 4 . The intersection of _S_ = _s_ with event A, _P_ ( _S_ = _s ∩ A_ ), is an event with probability (1 _− p_ )<sup>5</sup> _p_<sup>2</sup> for all values of _s_ ( _s_ = 1 _, . . . ,_ 6). Consequently, _pS|A_ ( _s_ ) =<sup>_P_</sup><sup><u>(</u></sup><sup>_S_</sup> _P_<sup>=</sup> ( _A_<sup>_s∩_</sup> )<sup>_A_</sup><sup><u>)</u></sup> is a uniform distribution over the range of _s_ ( _s_ = 1 _, . . . ,_ 6).


- (h) (5 points) Alice’s friend Bob buys a coin from the same store that turns out to be fair, i.e., that on any toss comes up heads with probability 1 _/_ 2. He tosses the coin repeatedly until he has seen either a total of 11 heads or a total of 11 tails. Let _U_ be the number of times he will need to toss the coin. Find the PMF of _U_ , _pU_ ( _u_ ). (Assume independent tosses.)

**Solution:** Bob must toss a coin at least 11 times and at most 21 times in order to have either 11 heads or 11 tails. The intersection of Bob requiring _u_ tosses and 11 of those tosses being heads, is the sum of probability the �<sup>_u_</sup> 10<sup>_−_1</sup> � sequences that conclude with a head and have a total of 11 heads. The probability of each of those sequences is ��12<sup>_u_</sup> . If we consider any sequence in Bob’s experiment with _u_ tosses, since the coin is fair, that sequence is equally likely to have 11 heads and _u −_ 11 tails or 11 tails and _u −_ 11 heads. Consequently, the intersection of Bob requiring _u_ tosses and 11 of those tosses being tails is identical to the probability that the sequence had 11 heads. Summing these two mutually exclusive probabilities which total _pU_ ( _u_ ):


10

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Solution](04-solution.md) · [Up: contents](index.md)
