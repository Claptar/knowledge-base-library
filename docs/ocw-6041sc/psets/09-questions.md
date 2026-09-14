---
title: 09 questions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/psets/09-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 09 questions

**Source:** `psets/09-questions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Problem Set 9

Due November 22, 2010

1. Random variable X is uniformly distributed between −1.0 and 1.0. Let X1, X2, . . ., be indepen­ dent identically distributed random variables with the same distribution as X. Determine which, if any, of the following sequences (all with i = 1, 2, . . .) are convergent in probability. Fully justify your answers. Include the limits if they exist.


   - (b) Wi = max(X1, . . . , Xi) (c) Vi = X1 · X2 · . . . · Xi

2. Demonstrate that the Chebyshev inequality is tight, that is, for every µ, σ > 0, and c ≥ σ, construct a random variable X with mean µ and standard deviation σ such that


Hint: You should be able to do this with a discrete random variable that takes on only 3 distinct values with nonzero probability.

3. Assume that a fair coin is tossed repeatedly, with the tosses being independent. We want to determine the expected number of tosses necessary to first observe a head directly followed by a tail. To do so, we define a Markov chain with states S, H, T, HT , where S is a starting state, H indicates a head on the current toss, T indicates a tail on the current toss (without heads on the previous toss), and HT indicates heads followed by tails over the last two tosses. This Markov chain is illustrated below:


<!-- Start of picture text -->
1<br>2<br>1<br>2<br>S H<br>1 1 1<br>2 1 2 2<br>2<br>T HT<br>1<br>2<br>1<br>2<br><!-- End of picture text -->

We can find the expected number of tosses necessary to first observe a heads directly followed by tails by solving a mean first passage time problem for this Markov chain.

- (a) What is the expected number of tosses necessary to first observe a head directly followed by tails?

- (b) Assuming we have just observed a head followed by a tail, what is the expected number of additional tosses until we again observe a head followed directly by a tail?

Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Next, we want to answer the same questions for the event tails directly followed by tails. Set up a different Markov chain from which we could calculate the expected number of tosses necessary to first observe tails directly followed by tails.

   - (c) What is the expected number of tosses necessary to first observe a tail directly followed by a tail?

   - (d) Assuming we have just observed a tail followed by a tail, what is the expected number of additional tosses until we again observe a tail followed directly by a tail? Note that the number of additional tosses could be as little as one, if tails were to come up again.

4. Jack is a gambler who pays for his MIT tuition by spending weekends in Las Vegas. Lately he’s been playing 21 at a table that returns cards to the deck and reshuffles them all before each hand. As he has a fixed policy in how he plays, his probability of winning a particular hand remains constant, and is independent of all other hands. There is a wrinkle, however; the dealer switches between two decks (deck #2 is more unfair to Jack than deck #1), depending on whether or not Jack wins. Jack’s wins and losses can be modeled via the transitions of the following Markov chain, whose states correspond to the particular deck being used.


<!-- Start of picture text -->
7<br>15<br>(win)<br>(loss) 158 1 2 94 (win)<br>(loss)<br>5<br>9<br><!-- End of picture text -->

- (a) What is Jack’s long term probability of winning?

Given that Jack loses and the dealer is not occupied with switching decks, with probability<sup><u>2</u></sup> 8<sup>the</sup> dealer looks away for one second and with probability<sup><u>1</u></sup> 8<sup>the dealer looks away for two seconds,</sup> independently of everything else. When this happens, Jack secretly inserts additional cards into both of the dealer’s decks, transforming the decks into types 1A & 2A (when he has 1 second) or 1B & 2B (when he has 2 seconds). Jack slips cards into the decks at most once. The process can be described by the modified Markov chain in the picture. Assume in all future problems that play begins with the dealer using deck #1.

Page 2 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


<!-- Start of picture text -->
3<br>4<br>(win)<br>(loss) 14 1B 2B 87 (win)<br>(loss)<br>1<br>(loss) 151 87<br>15<br>(win)<br>(loss) 13 1 2 94 (win)<br>(loss)<br>5<br>(loss) 152 93<br>5<br>(win)<br>(loss) 25 1A 2A 54 (win)<br>(loss)<br>1<br>5<br><!-- End of picture text -->

   - (b) What is the probability of Jack eventually playing with decks 1A and 2A?

   - (c) What is Jack’s long-term probability of winning?

   - (d) What is the expected time (as in number of hands) until Jack slips additional cards into the deck?

   - (e) What is the distribution of the number of times that the dealer switches from deck 2 to deck 1?

   - (f) What is the distribution of the number of wins that Jack has before he slips extra cards into the deck? Hint: Note that after some conditioning, we have a geometric number of geometric random variables, all of which are independent.

   - (g) What is the average net losses (number of losses minus the number of wins, sometimes negative) prior to Jack slipping additional cards into the deck?

   - (h) Given that after a very long period of time Jack is playing a hand with deck 1A, what is the approximate probability that his previous hand was played with deck 2A?

- G1<sup>†</sup> . Show the following one-sided version of Chebyshev’s inequality:


where µ and σ<sup>2</sup> are the mean and variance of X respectively, and a > 0. Hint: Start by finding a bound on P (X − µ + c ≥ a + c) with c ≥ 0. Then find the c that ‘tightens’ your bound.

†Required for 6.431; optional challenge problem for 6.041

Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
