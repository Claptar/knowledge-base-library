---
title: Review of Undergraduate Probability
source: https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf
source_file: sources/berkeley-guntuboyina-notes/FullLectureNotes201AFall2019.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Review of Undergraduate Probability

**Source:** [`FullLectureNotes201AFall2019.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We will start the course by a review of undergraduate probability material. The review will be fairly quick and should be complete in about four weeks.

### **1.1 Sample spaces, Events, Probability**

Probability theory is invoked in situations that are (or can be treated as) chance or random experiments. In such a random experiment, the _sample space_ is the set of all possible outcomes and we shall denote it by Ω.

For example, suppose we are tossing a coin 2 times. Then a reasonable sample space is _{hh, ht, th, tt}_ .

Subsets of the sample space are called _Events_ . For example, in the above example, _{hh, ht}_ is an Event and it represents the event that the first of the two tosses results in a heads. Similary, the event that at least one of the two tosses results in a heads is represented by _{hh, ht, th}_ .

Given a collection of events _A_ 1 _, A_ 2 _, . . ._ ,

1. _A_<sup>_c_</sup> 1<sup>denotestheeventthat</sup><sup>_A_1doesnothappen.Wesaythat</sup><sup>_Ac_</sup> 1<sup>isthecomplementoftheevent</sup> _A_ 1.

2. _∪i≥_ 1 _Ai_ denotes the event that at least one of _A_ 1 _, A_ 2 _, . . ._ happens.

3. _∩i≥_ 1 _Ai_ denotes the event that all of _A_ 1 _, A_ 2 _, . . ._ happen.

9

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

10

Probability is defined as a function that maps (or associates) events to real numbers between 0 and 1 and which satisfies certain natural consistency properties. Specifically P is a probability provided:

1. 0 _≤_ P( _A_ ) _≤_ 1 for every event _A_ .

2. For the empty subset Φ (= the “impossible event”), P(Φ) = 0

3. For the whole sample space (= the “certain event”), P(Ω) = 1.

4. If an event _A_ is a **disjoint union** of a sequence of events _A_ 1 _, A_ 2 _, . . ._ (this means that every point in _A_ belongs to exactly one of the sets _A_ 1 _, A_ 2 _, . . ._ ), then P( _A_ ) =<sup>�</sup> _i≥_ 1<sup>P(</sup><sup>_Ai_).</sup>

**Example 1.1.1** (Nontransitive Dice) **.** _Consider the following set of dice:_

_1. Die A has sides 2, 2, 4, 4, 9, 9._

_2. Die B has sides 1, 1, 6, 6, 8, 8._

_3. Die C has sides 3, 3, 5, 5, 7, 7._

_What is the probability that A rolls a higher number than B? What is the probability that B rolls higher than C? What is the probability that C rolls higher than A? Assume that, in any roll of dice, all outcomes are equally likely._

### **1.2 Conditional Probability and Independence of Events**

Consider a probability P and an event _B_ for which P( _B_ ) _>_ 0. We can then define P( _A|B_ ) for every event _A_ as


P( _A|B_ ) is called the conditional probability of _A_ given _B_ . A straightforward consequence of the definition (1.1) is the formula


We say that two events _A_ and _B_ are independent (under the probability P) if


Equivalently, independence is given by P( _A ∩ B_ ) = P( _A_ )P( _B_ ) or P( _B|A_ ) = P( _B_ ).

Here are two very interesting problems from Mosteller’s delightful book (titled _Fifty Challenging Problems in Probability_ ) illustrating the use of conditional probabilities.

_1.3. BAYES RULE_

11

**Example 1.2.1** (From Mosteller’s book (Problem 13; The Prisoner’s Dilemma)) **.** _Three prisoners, A, B, and C, with apparently equally good records have applied for parole. The parole board has decided to release two of the three, and the prisoners know this but not which two. A warder friend of prisoner A knows who are to be released. Prisoner A realizes that it would be unethical to ask the warder if he, A, is to be released, but thinks of asking for the name of one prisoner other than himself who is to be released. He thinks that before he asks, his chances of release are_ 2 _/_ 3 _. He thinks that if the warder says ”B will be released,” his own chances have now gone down to_ 1 _/_ 2 _, because either A and B or B and C are to be released. And so A decides not to reduce his chances by asking. However, A is mistaken in his calculations. Explain._

**Example 1.2.2** (The Monty Hall Problem) **.** _Suppose you’re on a game show, and you’re given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what’s behind the doors, opens another door, say No. 3, which has a goat. He then says to you, “Do you want to pick door No. 2?” Is it to your advantage to switch your choice?_

**Example 1.2.3** (From Mosteller’s book (Problem 20: The Three-Cornered Duel)) **.** _A, B, and C are to fight a three-cornered pistol duel. All know that A’s chance of hitting his target is 0.3, C’s is 0.5, and B never misses. They are to fire at their choice of target in succession in the order A, B, C, cyclically (but a hit man loses further turns and is no longer shot at) until only one man is left unhit. What should A’s strategy be?_

### **1.3 Bayes Rule**

A very important formula involving conditional probabilities is the Bayes rule. This is arguably the most important formula in all of probability and statistics. At a high level, the Bayes rule tells us how to compute P( _B|A_ ) in terms of P( _A|B_ ) and other terms. Note that these two conditional probabilities can be quite different. For example. consider this: “What is the probability of obtaining a dead person (D) given that the person was hanged (H); that is, in symbol form, what is _p_ ( _D|H_ )? Obviously, it will be very high, perhaps .97 or higher. Now, let us reverse the question: What is the probability that a person has been hanged (H) given that the person is dead (D); that is, what is _p_ ( _H|D_ )? This time the probability will undoubtedly be very low, perhaps .01 or lower.” (this comes from one of the quotes here: `http://www.indiana.edu/~stigtsts/quotsagn.html` ).

Formally Bayes rule says that


Note that _B_<sup>_c_</sup> in the right hand side above represents the complement of the event _B_ defined as the event where _B_ does not happen. The Bayes rule (1.3) is easily derived from the definition of conditional

12

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

probability in the following way:


The Bayes rule may be simple to derive but it has quite nontrivial consequences. For example, consider this simple problem.

**Example 1.3.1.** _Consider a clinical test for cancer that can yield either a positive (+) or negative (-) result. Suppose that a patient who truly has cancer has a 1% chance of slipping past the test undetected. On the other hand, suppose that a cancer-free patient has a 5% probabiliity of getting a positive test result. Suppose also that 2% of the population has cancer. Assuming that a patient who has been given the test got a positive test result, what is the probability that they have cancer?_

_Suppose C and C_<sup>_c_</sup> _are the events that the patient has cancer and does not have cancer respectively. Also suppose that_ + _and − are the events that the test yields a positive and negative result respectively. By the information given, we have_


_We need to compute_ P( _C|_ +) _. By Bayes rule, we have_


_Therefore the probability that this patient has cancer (given that the test gave a positive result) is about 29%. This means, in particular, that it is still unlikely that they have cancer even though the test gave a positive result (note though that the probability of cancer increased from 2% to 29%)._

_Another interesting aspect of the above calculation is that_


_This means that test will yield a positive result about 7% of the time (note that only 2% of the population has cancer)._

_Suppose now that_ P( _C_ ) = 0 _._ 001 _(as opposed to_ P( _C_ ) = 0 _._ 02 _) and assume that_ P( _−|C_ ) _and_ P(+ _|C_<sup>_c_</sup> ) _stay at_ 0 _._ 01 _and_ 0 _._ 05 _as before. Then_


_Here the true cancer rate of 0.001 has yielded in an apparent rate of 0.05 (which is an increase by a factor of 50). Think about this in the setting where the National Rifle Association is taking a survey by asking a sample of citizens whether they used a gun in self-defense during the past year. Take C to be true usage and_ + _to be reported usage. If only one person in a thousand had truly used a gun in self-defense, it will appear that one in twenty did. These examples are taken from the amazing book titled “Understanding Uncertainty” by Dennis Lindley._

_1.3. BAYES RULE_

13

**Example 1.3.2.** _This example is taken from the book “A tutorial introduction to Bayesian Analysis” by James Stone. Suppose you are a doctor confronted with a patient who is covered in spots. The patient’s symptoms are consistent with chickenpox but they are also consistent with another, more dangerous, disease, smallpox. Suppose that you know that 80% of the people which chickenpox have spots, but also that 90% of people with smallpox have spots. Suppose that you know that chickenpox is a relatively common disease with an incidence rate of 10% while smallpox is much rarer with an incidence rate of 0.1%. Based on all this information, how will you decide what disease the patient probably has?_

**Example 1.3.3** (Monty Hall Problem via Bayes rule) **.** _Recall the Monty Hall problem: Suppose you’re on a game show, and you’re given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what’s behind the doors, opens another door, say No. 3, which has a goat. He then says to you, “Do you want to pick door No. 2?” Is it to your advantage to switch your choice?_

_We can use Bayes rule to solve this problem in the following way. Let us suppose that I always pick Door 1 to start the game. I then need to calculate the conditional probability:_


_By Bayes rule,_

P _<u>{host</u> door 3|car door 2}_ P _<u>{car</u> door 2}_ P _{car door 2|host door 3}_ = P _{host door 3|car door 2}_ P _{car door 2}_ + P _{host door 3|car door 1}_ P _{car door 1}_<sup>_._</sup>

_Plugging in_


_and also_


_we get_


_and since this probability is more than 0.5, it makes sense for me to switch to door 2 from my original selction of door 1._

**Example 1.3.4** (The Blinky Monty Hall problem) **.** _Here is a very interesting variant on the Monty Hall problem that I found on the internet (here:_ _`http: // allendowney. blogspot. com/ 2011/ 10/ blinky-monty-problem. html` ). The problem is as follows. Consider the same setting as the usual Monty Hall problem. Suppose I pick door 1 to start with and the host reveals the goat behind door 3. Suppose also that before the host opened door 3, the host blinked. Based on watching this game show previously many times, I note that the host blinks with probability 0.6 when the contestant picks the_

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

14

_correct door and with probability 0.25 when the contestant picks the wrong door. With this additional information, will it still be to my advantage to switch my choice from door 1 to door 2?_

_We now need to calculate_

P _{car in door 2|host opened door 3 and blinked} ._

_Again by Bayes rule_

P _<u>{host</u> 3, blinked|car 2}_ P _<u>{car</u> 2}_ P _{car 2|host 3, blinked}_ = P _{host 3, blinked|car 1}_ P _{car 1}_ + P _{host 3, blinked|car 2}_ P _{car 2}_

_With the given information, it makes sense to take_

P _{host opened 3, blinked|car 2}_ = 0 _._ 25 _and_ P _{host opened 3, blinked|car 1}_ = (0 _._ 5)(0 _._ 6) = 0 _._ 3 _._

_This gives_

0 _._ 25 _∗_ <u>(1</u> _<u>/</u>_ 3) P _{car in door 2|host opened door 3 and blinked}_ = (0 _._ 25) _∗_ (1 _/_ 3) + (0 _._ 3) _∗_ (1 _/_ 3)<sup>_≈_0</sup><sup>_._45</sup><sup>_._</sup>

_Since this probability is less than 0.5, it makes sense for me to stay with my original choice of door 1 and not switch._

### **1.4 Random Variables**

A random variable is a function that attaches a number to each element of the sample space. In other words, it is a function mapping the sample space to real numbers.

For example, in the chance experiment of tossing a coin 50 times, the number of heads is a random variable. Another random variable is the number of heads before the first tail. Another random variable is the number of times the pattern _hththt_ is seen.

Many real-life quantities such as (a) The average temperature in Berkeley tomorrow, (b) The height of a randomly chosen student in this room, (c) the number of phone calls that I will receive tomorrow, (d) the number of accidents that will occur on Hearst avenue in September, etc. can be treated as random variables.

For every event _A_ (recall that events are subsets of the sample space), one can associate a random variable which take the value 1 if _A_ occurs and 0 if _A_ does not occur. This is called the _indicator_ random variable corresponding to the event _A_ and is denoted by _I_ ( _A_ ).

The _distribution_ of a random variable is, informally, a description of the set of values that the random variable takes and the probabilities with which it takes those values.

If a random variable _X_ takes a finite or countably infinte set of possible values (in this case, we say that _X_ is a _discrete_ random variable), its distribution is described by a listing of the values _a_ 1 _, a_ 2 _, . . ._

_1.5. EXPECTATIONS OF RANDOM VARIABLES_

15

that it takes together with a specification of the probabilities:


The function which maps _ai_ to P _{X_ = _ai}_ is called the _probability mass function_ (pmf) of the discrete random variable _X_ .

If a random variable _X_ takes a continuous set of values, its _distribution_ is often described by a function called the _probability density function_ (pdf). The pdf is a function _f_ on R that satisfies _f_ ( _x_ ) _≥_ 0 for every _x ∈_ R and


The pdf _f_ of a random variable can be used to calculate P _{X ∈ A}_ for every set _A_ via


Note that if _X_ has density _f_ , then for every _y ∈_ R,


It is important to remember that a density function _f_ ( _x_ ) of a random variable does not represent probability (in particular, it is quite common for _f_ ( _x_ ) to take values much larger than one). Instead, the value _f_ ( _x_ ) can be thought of as a constant of proportionality. This is because usually (as long as _f_ is continuous at _x_ ):


The _cumulative distribution function_ (cdf) of a random variable _X_ is the function defined as

_F_ ( _x_ ) := P _{X ≤ x}_ for _−∞ < x < ∞._

This is defined for all random variables discrete or continuous. If the random variable _X_ has a density, then its cdf is given by


The cdf of every random variable has the following properties: (a) It is non-decreasing, (b) rightcontinuous, (c) lim _x↓−∞ F_ ( _x_ ) = 0 and lim _x↑_ + _∞ F_ ( _x_ ) = 1.

The cdf of a continuous random variable is continuous and differentiable and its derivative is the pdf of the random variable.

### **1.5 Expectations of Random Variables**

Let _X_ be a discrete random variable and let _g_ be a real-valued function on the range of _X_ . The expectation of _g_ ( _X_ ) is defined as


_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

16

where the summation is over all possible values _x_ of _X_ .

Analogously, if _X_ is a continuous random variable with density (pdf) _f_ , the expectation of _g_ ( _X_ ) is defined as


It is important to keep in mind that it is possible for E _g_ ( _X_ ) to be + _∞_ or _−∞_ or undefined. A famous example for when the expectation is + _∞_ is the following.

**Example 1.5.1** (Petersburg Paradox) **.** _A casino offers a game of chance for a single player in which a fair coin is tossed at each stage. The initial stake starts at 2 dollars and is doubled every time heads appears. The first time tails appears, the game ends and the player wins whatever is in the pot. Thus the player wins 2 dollars if tails appears on the first toss, 4 dollars if heads appears on the first toss and tails on the second, 8 dollars if heads appears on the first two tosses and tails on the third, and so on. Mathematically, the player wins_ 2<sup>_x_</sup> _k dollars, where k equals number of tosses (k must be a whole number and greater than zero). Suppose that X denotes the money that the player wins. What is_ E _X?_

_The pmf of the random variable X is clearly given by_


_As a result,_


It is similarly easy to construct a random variable whose expectation is _−∞_ .

Sometimes, the expectation is neither finite, nor + _∞_ or _−∞_ , it is simply undefined. To see this, consider a discrete random variable _X_ which takes the values _. . . , −_ 3 _, −_ 2 _, −_ 1 _,_ 1 _,_ 2 _,_ 3 _, . . ._ with probabilities


Then


which can not be made any sense of.

If a random variable takes only nonnegative values, then its expectation is either finite or + _∞_ .

If _A_ is an event, then recall that _I_ ( _A_ ) denotes the corresponding indicator random variable that equals 1 when A holds and 0 when A does not hold. It is convenient to note that the expectation of _I_ ( _A_ ) precisely equals P( _A_ ).

An important thing to remember is that Expectation is a _linear operator_ i.e.,

E( _aX_ + _bY_ ) = _a_ E( _X_ ) + _b_ E( _Y_ )

_1.6. VARIANCE_

17

for any two random variables _X_ and _Y_ with finite expectations and real numbers _a_ and _b_ . An implication of this is that if


then E _X_ = E _U_ 1 + _. . ._ E _Un_ . This trick is sometimes useful for calculating expectations.

**Example 1.5.2.** _Suppose I have an urn with 10000 balls labeled_ 1 _,_ 2 _, . . . ,_ 10000 _. Suppose I draw a sample of 500 balls at random with replacement. What is the expected number of balls that will not appear in the sample?_

_We need to calculate_ E _X where X is the number of balls that do not appear in the sample. For each i_ = 1 _, . . . ,_ 10000 _, let Ui be the indicator random variable of the event that the ball labeled i does not appear in the sample. Then clearly_


_and by linearity of expectation, we have_


_To calculate_ E _Ui, note that as Ui takes only the values 0 and 1, we have_


_As a result_


The Expectation of a random variable _X_ has the following variational property: it is the value of _a_ that minimizes the quantity E( _X − a_ )<sup>2</sup> over all real numbers _a_ . Do you know how to prove this?

### **1.6 Variance**

A random variable _X_ is said to have finite variance if _X_<sup>2</sup> has finite expectation (do you know that when _X_<sup>2</sup> has finite expectation, _X_ also will have finite expectation? how will you prove this?). In that case, the variance of _X_<sup>2</sup> is defined as


It is clear from the definition that Variance of a random variable _X_ measures the average squared variability in the values taken by _X_ around its mean E( _X_ ).

Suppose _X_ is a discrete random variables taking finitely many values _x_ 1 _, . . . , xn_ with equal probabilities. Then what is the variance of _X_ ?

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

18

The square root of the variance of _X_ is called the standard deviation of _X_ and is often denoted by _SD_ ( _X_ ).

If the variance of a random variable _X_ is small, then _X_ cannot deviate much from its mean (= E( _X_ ) = _µ_ ). This can be made precise by Chebyshev’s inequality which states the following.

**Chebyshev’s Inequality** : Let _X_ be a random variable with finite variance and mean _µ_ . Then for every _ϵ >_ 0, the following inequality holds:


In other words, the probability that _X_ deviates by more than _ϵ_ from its mean is bounded from above by _V ar_ ( _X_ ) _/ϵ_<sup>2</sup> .

**Proof of Chebyshev’s inequality** : Just argue that


and take expectations on both sides (on the left hand side, we have the Indicator random variable that takes the value 1 when _|X − µ| ≥ ϵ_ and 0 otherwise).

### **1.7 Independence of Random Variables**

We say that two random variables _X_ and _Y_ are independent if conditioning on any event involving _Y_ does not change the probability of any event involving _X_ i.e.,


for every _A_ and _B_ .

Equivalently, independence of _X_ and _Y_ is same as


for every _A_ and _B_ .

The following are consequences of independence. If _X_ and _Y_ are independent, then

1. _g_ ( _X_ ) and _h_ ( _Y_ ) are independent for every pair of functions _g_ and _h_ .

2. E ( _g_ ( _X_ ) _h_ ( _Y_ )) = E _g_ ( _X_ )E _h_ ( _Y_ ) for every pair of functions _g_ and _h_ .

More generally, we say that random variables _X_ 1 _, . . . , Xk_ are (mutually) independent if, for every 1 _≤ i ≤ k_ , conditioning on any event involving _Xj, j̸_ = _i_ does not change the probability of any event involving _Xi_ . From here one can easily derive properties of independence such as


_1.8. COMMON DISTRIBUTIONS_

19

for all possible choices of events _A_ 1 _, . . . , Ak_ .

### **1.8 Common Distributions**

#### **1.8.1 Bernoulli** _Ber_ ( _p_ ) **Distribution**

A random variable _X_ is said to have the _Ber_ ( _p_ ) (Bernoulli with parameter _p_ ) distribution if it takes the two values 0 and 1 with P _{X_ = 1 _}_ = _p_ .

Note then that E _X_ = _p_ and _V ar_ ( _X_ ) = _p_ (1 _− p_ ). For what value of _p_ is _X_ most variable? least variable?

#### **1.8.2 Binomial** _Bin_ ( _n, p_ ) **Distribution**

A random variable _X_ is said to have the Binomial distribution with parameters _n_ and _p_ ( _n_ is a positive integer and _p ∈_ [0 _,_ 1]) if it takes the values 0 _,_ 1 _, . . . , n_ with pmf given by


Here � _nk_ � is the binomial coefficient:


The main example of a _Bin_ ( _n, p_ ) random variable is the number of heads obtained in _n independent_ tosses of a coin with probability of heads equalling _p_ .

Here is an interesting problem about the Binomial distribution from Mosteller’s book (you can easily calculate these probabilities in R for example).

**Example 1.8.1** (From Mosteller’s book (Problem 19: Issac Newton helps Samuel Pepys)) **.** _Pepys wrote Newton to ask which of three events is more likely: that a person get (a) at least 1 six when 6 dice are rolled, (b) at least 2 sixes when 12 dice are rolled, or (c) at least 3 sixes when 18 dice are rolled. What is the answer?_

Let _X_ denote the number of heads in _n_ independent tosses of a coin with probability of heads being _p_ . Then we know that _X ∼ Bin_ ( _n, p_ ). If, now, _Xi_ denotes the binary random variable that takes 1 if the _i_<sup>_th_</sup> toss is a heads and 0 if the _i_<sup>_th_</sup> toss is a tail, then it should be clear that


Note that each _Xi_ is a _Ber_ ( _p_ ) random variable and that _X_ 1 _, . . . , Xn_ are independent. Therefore _Bin_ ( _n, p_ ) random variables can be viewed as sums of _n_ independent _Ber_ ( _p_ ) random variables. The

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

20

Central Limit Theorem (which we will study in detail later in the class) implies that the sum of a large number of i.i.d (what is i.i.d?) random variables is approximately normal. This means that when _n_ is large and _p_ is held fixed, the _Bin_ ( _n, p_ ) distribution looks like a normal distribution. We shall make this precise later. In particular, this means that Binomial probabilities can be approximately calculated via normal probabilities for _n_ large and _p_ fixed. From this point of view, what is the probability of getting _k_ or more sixes from 6 _k_ rolls of a die when _k_ is large?

What is the mean of the _Bin_ ( _n, p_ ) distribution? What is the variance of _Bin_ ( _n, p_ )?

#### **1.8.3 Poisson Distribution**

A random variable _X_ is said to have the Poisson distribution with parameter _λ >_ 0 (denoted by _Poi_ ( _λ_ )) if _X_ takes the values 0 _,_ 1 _,_ 2 _, . . ._ with pmf given by


The main utility of the Poisson distribution comes from the following fact:

**Fact** : The binomial distribution _Bin_ ( _n, p_ ) is well-approximated by the Poisson distribution _Poi_ ( _np_ ) provided that the quantity _np_<sup>2</sup> small.

To intuitively see why this is true, just see that


Note now that _np_<sup>2</sup> being small implies that _p_ is small (note that _p_ can be written as � _np_<sup>2</sup> _/n ≤_ � _np_<sup>2</sup> so small _np_<sup>2</sup> will necessarily mean that _p_ is small). When _p_ is small, we can approximate log(1 _− p_ ) as _−p − p_<sup>2</sup> _/_ 2 so we get P _{Bin_ ( _n, p_ ) = 0 _}_ = exp ( _n_ log(1 _− p_ )) _≈_ exp ( _−np_ ) exp � _−np_<sup>2</sup> _/_ 2� _._

Now because _np_<sup>2</sup> is small, we can ignore the second term above to obtain that P _{Bin_ ( _n, p_ ) = 0 _}_ is approximated by exp( _−np_ ) which is precisely equal to P _{Poi_ ( _np_ ) = 0 _}_ . One can similarly approximate P _{Bin_ ( _n, p_ ) = _k}_ by P _{Poi_ ( _np_ ) = _k}_ for every fixed _k_ = 0 _,_ 1 _,_ 2 _, . . ._ .

There is a formal theorem (known as Le Cam’s theorem) which rigorously proves that _Bin_ ( _n, p_ ) _≈ Poi_ ( _np_ ) when _np_<sup>2</sup> is small. This is stated without proof below (its proof is beyond the scope of this class).

**Theorem 1.8.2** (Le Cam’s Theorem) **.** _Suppose X_ 1 _, . . . , Xn are independent random variables such that Xi ∼ Ber_ ( _pi_ ) _for some pi ∈_ [0 _,_ 1] _for i_ = 1 _, . . . , n. Let X_ = _X_ 1 + _· · ·_ + _Xn and λ_ = _p_ 1 + _. . . pn. Then_


_1.8. COMMON DISTRIBUTIONS_

21

In the special case when _p_ 1 = _· · ·_ = _pn_ = _p_ , the above theorem says that


and thus when _np_<sup>2</sup> is small, the probability P _{Bin_ ( _n, p_ ) = _k}_ is close to P _{Poi_ ( _np_ ) = _k}_ for each _k_ = 0 _,_ 1 _, . . ._ .

An implication of this fact is that for every fixed _λ >_ 0, we have


This is because when _p_ = _λ/n_ , we have _np_<sup>2</sup> = _λ_<sup>2</sup> _/n_ which will be small when _n_ is large.

This approximation property of the Poisson distribution is the reason why the Poisson distribution is used to model counts of rare events. For example, the number of phone calls a telephone operator receives in a day, the number of accidents in a particular street in a day, the number of typos found in a book, the number of goals scored in a football game can all be modelled as _Poi_ ( _λ_ ) for some _λ >_ 0. Can you justify why these real-life random quantities can be modeled by the Poisson distribution?

The following example presents another situation where the Poisson distribution provides a good approximation.

**Example 1.8.3.** _Consider n letters numbered_ 1 _, . . . , n and n envelopes numbered_ 1 _, . . . , n. The right envelope for letter i is the envelope i. Suppose that I take a random permutation σ_ 1 _, . . . , σn of_ 1 _, . . . , n and then place the letter σi in the envelope i. Let X denote the number of letters which are in their right envelopes. What is the distribution of X?_

_Let Xi be the random variable which takes the value 1 when the i_<sup>_th_</sup> _letter is in the i_<sup>_th_</sup> _envelope and 0 otherwise. Then clearly X_ = _X_ 1 + _· · ·_ + _Xn. Note that_


_This is because the i_<sup>_th_</sup> _letter is equally likely to be in any of the n envelopes. This means therefore that_


_If the Xi’s were also independent, then X_ = _X_ 1 + _· · ·_ + _Xn will be Bin_ ( _n,_ 1 _/n_ ) _which is very close to Poi_ (1) _for large n. But the Xi’s are not independent here because for i̸_ = _j,_


_However, the dependence is relatively weak and it turns out that the distribution of X is quite close to Poi_ (1) _. We shall demonstrate this by showing that_ P _{X_ = 0 _} is approximately equal to_ P _{Poi_ (1) = 0 _}_ = _e_<sup>_−_1</sup> _. I will leave as an exercise to show that_ P _{X_ = _k} ≈_ P _{Poi_ (1) = _k} for every fixed k. To_

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

22

_compute_ P _{X_ = 0 _}, we can write_


_Note now that for every i_ 1 _< · · · < ik, we have_


_This gives_


It is an easy exercise to show that the expectation and variance of a _Poi_ ( _λ_ ) random variable are both equal to _λ_ . This also makes sense because of the connection:


as


When modeling count data via the Poisson distribution, it is possible to empirically check the assumption that the variance is equal to the mean. If the empirical variance seems much higher than the mean, then it is said that there is _overdispersion_ in which case Poisson may not be a good model for the data.

#### **1.8.4 Geometric Distribution**

We say that _X_ has the Geometric distribution with parameter _p ∈_ [0 _,_ 1] (written as _X ∼ Geo_ ( _p_ )) if _X_ takes the values 1 _,_ 2 _, . . ._ with the probabilities:


It is easy to see that the number of independent tosses (of a coin with probability of heads _p_ ) required to get the first head has the _Geo_ ( _p_ ) distribution.

_1.9. CONTINUOUS DISTRIBUTIONS_

23

The _Geo_ ( _p_ ) distribution has the interesting property of memorylessness i.e., if _X ∼ Geo_ ( _p_ ), then


This is easy to check as P _{X > m}_ = (1 _− p_ )<sup>_m_</sup> . It is also interesting that the Geometric distribution is the only distribution on _{_ 1 _,_ 2 _, . . . }_ which satisfies the memorylessness property (1.6). To see this, suppose that _X_ is a random variable satisfying (1.6) which takes values in _{_ 1 _,_ 2 _, . . . }_ . Let _G_ ( _m_ ) := P _{X > m}_ for _m_ = 1 _,_ 2 _, . . ._ . Then (1.6) is the same as


This clearly gives _G_ ( _m_ ) = ( _G_ (1))<sup>_m_</sup> for each _m_ = 1 _,_ 2 _, . . ._ . Now _G_ (1) = P _{X >_ 1 _}_ = 1 _−_ P _{X_ = 1 _}_ . If _p_ = P _{X_ = 1 _}_ , then


which means that P _{X_ = _k}_ = P _{X > k −_ 1 _} −_ P _{X > k}_ = _p_ (1 _− p_ )<sup>_k−_1</sup> for every _k ≥_ 1 meaning that _X_ is _Geo_ ( _p_ ).

#### **1.8.5 Negative Binomial Distribution**

Let _X_ denote the number of tosses (of a coin with probability of heads _p_ ) required to get the _k_<sup>_th_</sup> head. The distribution of _X_ is then given by the following. _X_ takes the values _k, k_ + 1 _, . . ._ and


This is called the Negative Binomial distribution with parameters _k_ and _p_ (denoted by _NB_ ( _k, p_ )). If _G_ 1 _, . . . , Gk_ are independent _Geo_ ( _p_ ) random variables, then _G_ 1 + _· · ·_ + _Gk ∼ NB_ ( _k, p_ ) (can you prove this?).

### **1.9 Continuous Distributions**

Next we shall look at continuous distributions.

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

24

#### **1.9.1 Normal or Gaussian Distribution**

A random variable _X_ has the normal distribution with mean _µ_ and variance _σ_<sup>2</sup> _>_ 0 if it has the following pdf:


We write _X ∼ N_ ( _µ, σ_<sup>2</sup> ). When _µ_ = 0 and _σ_<sup>2</sup> = 1, we say that _X_ has the _standard_ normal distribution and the standard normal pdf is simply denote by _φ_ ( _·_ ):


The standard normal cdf is denoted by Φ( _x_ ):


If _X ∼ N_ ( _µ, σ_<sup>2</sup> ), then E( _X_ ) = _µ_ and _V ar_ ( _X_ ) = _σ_<sup>2</sup> . See the corresponding wikipedia page for a list of numerous properties of the normal distribution. The Central Limit Theorem is the main reason why the normal distribution is the most prominent distribution in statistics.

#### **1.9.2 Uniform Distribution**

A random variable _U_ is said to have the uniform distribution on (0 _,_ 1) if it has the following pdf:


We write _U ∼ U_ [0 _,_ 1]. What is the mean of _U_ ? What is the variance of _U_ ? Where do uniform distributions arise in statistics? The _p_ -values under the null distribution are usually distributed according to the _U_ [0 _,_ 1] distribution (more on this later).

More generally, given an interval ( _a, b_ ), we say that a random variable _U_ has the uniform distribution on ( _a, b_ ) if it has the following pdf:


We write this as _U ∼ U_ ( _a, b_ ).

#### **1.9.3 The Exponential Distribution**

The exponential distribution is given by the exponential density. The exponential density with rate parameter _λ >_ 0 (denoted by _Exp_ ( _λ_ )) is given by


_1.9. CONTINUOUS DISTRIBUTIONS_

25

It is arguably the simplest density for modeling random quantities that are constrained to be nonnegative. It is used to model things such as the time of the first phone call that a telephone operator receives starting from now (this can be justified via a discretization argument).

The cdf of _Exp_ ( _λ_ ) is easily seen to be


The exponential density has the memorylessness property (just like the Geometric distribution). Indeed,


In fact, the exponential density is the only density on (0 _, ∞_ ) that has the memorylessness property (proof left as exercise). In this sense, the Exponential distributionx can be treated as the continuous analogue of the Geometric distribution.

#### **1.9.4 The Gamma Density**

It is customary to talk about the Gamma density after the exponential density. The Gamma density with shape parameter _α >_ 0 and rate parameter _λ >_ 0 is given by


To find the proportionality constant above, we need to evaluate


Now the function


is called the Gamma function in mathematics. So the constant of proportionality in (1.7) is given by


so that the Gamma density has the formula:


We shall refer to this as the _Gamma_ ( _α, λ_ ) density.

Note that the _Gamma_ ( _α, λ_ ) density reduces to the _Exp_ ( _λ_ ) density when _α_ = 1. Therefore, Gamma densities can be treated as a generalization of the Exponential density. In fact, the Gamma density can be seen as the continuous analogue of the negative binomial distribution because if _X_ 1 _, . . . , Xk_ are independent _Exp_ ( _λ_ ) random variables, then _X_ 1 + _· · ·_ + _Xn ∼ Gamma_ ( _k, λ_ ) (thus the Gamma

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

26

distribution arises as the sum of i.i.d exponentials just as the Negative Binomial distribution arises as the sum of i.i.d Geometric random variables).

Here are some elementary properties of the Gamma function that will be useful to us later. The Gamma function does not have a closed form expression for arbitrary _α >_ 0. However when _α_ is a positive integer, it can be shown that


The above inequality is a consequence of the property


and the trivial fact that Γ(1) = 1. You can easily verify (1.9) by integration by parts.

Another easy fact about the Gamma function is that Γ(1 _/_ 2) =<sup>_√_</sup> _<u>π</u>_ (this is a consequence of the fact that � _e_<sup>_−x_2</sup><sup>_/_2</sup> _dx_ = _√_ 2 _π_ ).

### **1.10 Variable Transformations**

It is often common to take functions or transformations of random variables. Consider a random variable _X_ and apply a function _u_ ( _·_ ) to _X_ to transform _X_ into another random variable _Y_ = _u_ ( _X_ ). How does one find the distribution of _Y_ = _u_ ( _X_ ) from the distribution of _X_ ?

If _X_ is a discrete random variable, then _Y_ = _u_ ( _X_ ) will also be discrete and then the pmf of _Y_ can be written directly in terms of the pmf of _X_ :


If _X_ is a continuous random variable with density _f_ and _u_ ( _·_ ) is a smooth function, then it is fairly straightforward to write down the density of _Y_ = _u_ ( _X_ ) in terms of _f_ . There are some general formulae for doing this but it is better to learn how to do it from first principles. I will illustrate the general idea using the following two examples.

**Example 1.10.1.** _Suppose X ∼ U_ ( _−π/_ 2 _, π/_ 2) _. What is the density of Y_ = tan( _X_ ) _? Here is the method for doing this from first principles. Note that the range of_ tan( _x_ ) _as x ranges over_ ( _−π/_ 2 _, π/_ 2) _is_ R _so fix y ∈_ R _and we shall find below the density g of Y at y._

_The formula for g_ ( _y_ ) _is_


_so that_


_1.10. VARIABLE TRANSFORMATIONS_

27

_Now for small δ,_


_where f is the density of X. Comparing the above with_ (1.10) _, we can conclude that_


_Using now the density of X ∼ U_ ( _−π/_ 2 _, π/_ 2) _, we deduce that_


_This is the_ **_Cauchy_** _density._

The answer derived in the above example is a special case of the following formula:


which makes sense as long as _T_ is invertible and _T_<sup>_−_1</sup> is differentiable. The method used in the example is more general however and also applies when _T_ is non-invertible. We shall see such an example in the next class.

**Example 1.10.2.** _Suppose X ∼ N_ (0 _,_ 1) _so that X has the standard normal density φ_ ( _·_ ) _. What is the density of Y_ = _X_<sup>2</sup> _? The following method does this from first principles. The range of X_<sup>2</sup> _as X ranges over_ ( _−∞, ∞_ ) _is_ [0 _, ∞_ ) _so let us fix y >_ 0 _. We shall find the density g of Y at y. Write_


_This gives_


_This is the density of the chi-squared random variable with 1 degree of freedom (or the Gamma random variable with shape parameter α_ = 1 _/_ 2 _and scale parameter β_ = 1 _/_ 2 _)._

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

28

### **1.11 Quantiles and The Quantile Transform**

The Quantiles of a distribution frequently come up in statistics. Given a random variable _X_ and a number _u ∈_ (0 _,_ 1), the _u_ -quantile of the distribution of _X_ is given by a real number _qX_ ( _u_ ) satisfying


provided such a number _qX_ ( _u_ ) exists uniquely. If _FX_ is the cdf of _X_ , the equation (1.11) simply becomes


so we can write


Here are some simple examples.

**Example 1.11.1** (Uniform) **.** _Suppose X has the uniform distribution on_ (0 _,_ 1) _. Then FX_ ( _x_ ) = _x for x ∈_ (0 _,_ 1) _and thus FX_<sup>_−_1(</sup><sup>_u_)</sup><sup>_existsuniquelyforeveryu ∈_(0</sup><sup>_,_1)</sup><sup>_andequalsu.WethushaveqX_(</sup><sup>_u_) =</sup><sup>_u_</sup> _for every u ∈_ (0 _,_ 1) _._

**Example 1.11.2** (Normal) **.** _Suppose X has the standard normal distribution. Then FX_ ( _x_ ) = Φ( _x_ ) _where_


_There is no closed form expression for_ Φ _but its values can be obtained in R (for example) using the function pnorm._ Φ _is a strictly increasing function from_ ( _−∞, ∞_ ) _to_ (0 _,_ 1) _so its inverse exists uniquely and we thus have_


_There is no closed form expression for qX_ = Φ<sup>_−_1</sup> _but its values can be obtained from R by the function qnorm._

**Example 1.11.3** (Cauchy) **.** _Suppose X has the standard Cauchy density:_


_Its cdf is given by_


_It is easy to see that this is a strictly increasing function from_ ( _∞, ∞_ ) _to_ (0 _,_ 1) _and its inverse is given by_


_Thus the quantile function for the Cauchy distribution is given by_


_1.11. QUANTILES AND THE QUANTILE TRANSFORM_

29

How to define the _u_ -quantile when there is no solution or multiple solutions to the equation _FX_ ( _q_ ) = _u_ ? No solutions for _FX_ ( _q_ ) = _u_ can happen for discrete distributions (for example, for _X ∼ Ber_ (0 _._ 5) and _u_ = 0 _._ 25, there is no _q_ satisfying P _{X ≤ q}_ = _u_ ). Multiple solutions can also happen. For example, if _X_ is uniformly distributed on the set [0 _,_ 1] _∪_ [2 _,_ 3] and _u_ = 0 _._ 5, then every _q ∈_ [1 _,_ 2] satisfies _FX_ ( _q_ ) = 0 _._ 5. In such cases, it is customary to define the _u_ -quantile via


This can be seen as a generalization of _FX_<sup>_−_1(</sup><sup>_u_).Indeed,ifthereisaunique</sup><sup>_q_suchthat</sup><sup>_FX_(</sup><sup>_q_) =</sup><sup>_u_,it</sup> is easy to see then that _qX_ ( _u_ ) = _q_ .

The function _qX_ : (0 _,_ 1) _→_ ( _−∞, ∞_ ) defined by (1.12) is called the quantile function or the quantile transform of the random variable _X_ . It can be checked that the definition (1.12) ensures that


The following result is a big reason why the quantile transform is important.

**Proposition 1.11.4.** _The following two statements are true._

_1. Suppose U is a random variable distributed according to the uniform distribution on_ (0 _,_ 1) _. Then qX_ ( _U_ ) _has the same distribution as X. In other words, the function qX transforms the uniform distribution to the distribution of X._

_2. Suppose X is a random variable with a_ **_continuous_** _cdf FX . Then FX_ ( _X_ ) _has the uniform distribution on_ (0 _,_ 1) _. In other words, the function FX transforms the distribution of X into the Unif_ (0 _,_ 1) _distribution (provided the distribution of X is continuous)._

If you want to see proofs of (1.13) and Proposition 1.11.4, you can refer to last year’s notes. The proofs are not really necessary for this course.

**Example 1.11.5** (Cauchy) **.** _We have just seen that for a standard Cauchy random variable, qX_ ( _u_ ) = tan( _π_ ( _u −_ 0 _._ 5)) _. The above result then gives that if U ∼ Unif_ (0 _,_ 1) _, then_


**Example 1.11.6** (p-values corresponding to test statistics having continuous distributions have uniform distributions under the null hypothesis) **.** _Statistical hypothesis testing problems are usually formed by calculating a relevant test statistic based on data. Suppose Tobs is the observed value of the statistic calculated from the data. The p-value corresponding to the test is defined as the probability, under the null hypothesis, of observing a value for the statistic that is more extreme compared to Tobs. Usually this is calculated as_


_where F_ 0 _is the cdf of the test statistic under the null hypothesis. If F_ 0 _is a continuous cdf, then it should be clear that p is distributed according to U_ (0 _,_ 1) _when Tobs ∼ F_ 0 _. In other words, under the null distribution (i.e., Tobs ∼ F_ 0 _), the p-value has the standard uniform distribution._

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

30

### **1.12 Joint Densities**

Joint densities are used to describe the distribution of a finite set of continuous random variables. We focus on bivariate joint densities (i.e., when there are two continuous variables _X_ and _Y_ ). The ideas are the same for the case of more than two variables.

The following are the main points to remember about joint densities:

1. _f_ ( _·, ·_ ) is called a joint density if


2. We say that two random variables _X_ and _Y_ have joint density _f_ ( _·, ·_ ) if


for every subset _B_ of R<sup>2</sup> . We shall often denote the joint density of ( _X, Y_ ) by _fX,Y_ .

3. If ∆is a small region in R<sup>2</sup> around a point ( _x_ 0 _, yo_ ), we have (under some regularity condition on the behavior of _fX,Y_ at ( _x_ 0 _, y_ 0))


More formally,


where the limit is taken as ∆shrinks to ( _x_ 0 _, y_ 0).

4. If ( _X, Y_ ) have joint density _fX,Y_ , then the density of _X_ is given by _fX_ and the density of _Y_ is _fY_ where


The densities _fX_ and _fY_ are referred to as the _marginal_ densities of _X_ and _Y_ respectively.

5. **Independence and Joint Densities** : The following statements are equivalent:

   - (a) The random variables _X_ and _Y_ are independent.

   - (b) The joint density _fX,Y_ ( _x_ ) factorizes into the product of a function depending on _x_ alone and a function depending on _y_ alone.

   - (c) _fX,Y_ ( _x, y_ ) = _fX_ ( _x_ ) _fY_ ( _y_ ) for all _x, y_ .

**Example 1.12.1.** _Consider the function_


_1.13. JOINT DENSITIES UNDER TRANSFORMATIONS_

31

_Check that this is indeed a density function. This density takes the value 1 on the unit square. If the random variables X and Y have this density f , then we say that they are uniformly distributed on the unit square. Using indicator functions, we can write this density also as:_


_The factorization above immediately says that if f_ = _fX,Y , then X and Y are independent. The marginal densities of X and Y are uniform densities on_ [0 _,_ 1] _._

_Question: If X, Y have this density f , calculate_ P _{X_<sup>2</sup> + _Y_<sup>2</sup> _≤_ 1 _} (Ans: π/_ 4 _)._

**Example 1.12.2.** _Suppose X, Y have the joint density_


_Show that the marginal density of X is given by_


_Are X and Y independent? (Ans: No. Why?)_

### **1.13 Joint Densities under Transformations**

We address the following general question. Suppose _X_ and _Y_ have the joint density _fX,Y_ . Suppose now that we consider two new random variables defined by


where _T_ : R<sup>2</sup> _→_ R<sup>2</sup> is a differentiable and invertible function. What is the joint density _fU,V_ of _U, V_ in terms of _fX,Y_ ?

The following simple example will nicely motivate the general ideas.

**Example 1.13.1.** _Suppose X, Y have joint density fX,Y . What is the joint density of U and V where U_ = _X and V_ = _X_ + _Y ?_

_We see that_ ( _U, V_ ) = _T_ ( _X, Y_ ) _where T_ ( _x, y_ ) = ( _x, x_ + _y_ ) _. This transformation T is clearly invertible and its inverse is given by S_ ( _u, v_ ) = _T_<sup>_−_1</sup> ( _u, v_ ) = ( _u, v − u_ ) _. In order to determine the joint density of_ ( _U, V_ ) _at a point_ ( _u, v_ ) _, let us consider_


_Let R denote the rectangle joining the points_ ( _u, v_ ) _,_ ( _u_ + _δ, v_ ) _,_ ( _u, v_ + _ϵ_ ) _and_ ( _u_ + _δ, v_ + _ϵ_ ) _. Then the above probability is the same as_


32

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

_What is the region S_ ( _R_ ) _? It is easy to see that this is the parallelogram joining the points_ ( _u, v − u_ ) _,_ ( _u_ + _δ, v − u − δ_ ) _,_ ( _u, v − u_ + _ϵ_ ) _and_ ( _u_ + _δ, v − u_ + _ϵ − δ_ ) _. When δ and ϵ are small, S_ ( _R_ ) _is clearly a small region around_ ( _u, v − u_ ) _which allows us to write_


_The area of the parallelogram S_ ( _R_ ) _can be computed to be δϵ (using the formula that the area of a parallelogram equals base times height) so that_


_Comparing with_ (1.14) _, we obtain_


_This gives the formula for the joint density of_ ( _U, V_ ) _in terms of the joint density of_ ( _X, Y_ ) _._

#### **1.13.1 Detour to Convolutions**

We shall come back to the general problem of finding densities of transformations after taking a short detour to convolutions.

We proved in the above example the joint density of _U_ = _X_ and _V_ = _X_ + _Y_ is given by


where _fX,Y_ is the joint density of ( _X, Y_ ). As a consequence, we see that the density of _V_ = _X_ + _Y_ is given by


Suppose now that _X_ and _Y_ are independent. Then _fX,Y_ ( _x, y_ ) = _fX_ ( _x_ ) _fY_ ( _y_ ) and consequently


where the last equality is a consequence of a simple change of variable _v − u_ = _w_ .

**Definition 1.13.2** (Convolution) **.** _Given two densities f_ 1 _and f_ 2 _, we define their convolution, f_ 1 _⋆f_ 2 _to be the density:_


The equation (1.15) therefore says, in words, that the density of _X_ + _Y_ , where _X ∼ fX_ and _Y ∼ fY_ are independent, equals the convolution of _fX_ and _fY_ .

_1.14. JOINT DENSITIES UNDER TRANSFORMATIONS_

33

**Example 1.13.3.** _Suppose X and Y are independent random variables which are exponentially distributed with rate parameter λ. What is the distribution of X_ + _Y ?_

_By the convolution formula,_


_This shows that X_ + _Y has the Gamma distribution with shape parameter_ 2 _and rate parameter λ._

**Example 1.13.4.** _Suppose X and Y are independent random variables that are uniformly distributed on_ [0 _,_ 1] _. What is the density of X_ + _Y ?_

_By the convolution formula,_


_This integral is non-zero only when_ max( _v −_ 1 _,_ 0) _≤_ min( _v,_ 1) _which is easily seen to be equivalent to_ 0 _≤ v ≤_ 2 _. When_ 0 _≤ v ≤_ 2 _, we have_


_which can be simplified as_


_This is called the triangular density._

### **1.14 Joint Densities under transformations**

In the last class, we calculated the joint density of ( _X_ + _Y, Y_ ) in terms of the joint density of ( _X, Y_ ). In this lecture, we generalize the idea behind that calculation by first calculating the joint density of a linear and invertible transformation of a pair of random variables. We also deal with the case of a non-linear and invertible transformation.

In the next subsection, we shall recall some standard properties of linear transformations.

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

34

#### **1.14.1 Linear Transformations**

By a linear transformation _L_ : R<sup>2</sup> _→_ R<sup>2</sup> , we mean a function that is given by


where _M_ is a 2 _×_ 2 matrix and _c_ is a 2 _×_ 1 vector. The first term on the right hand side above involves multiplication of the 2 _×_ 2 matrix _M_ with the 2 _×_ 1 vector with components _x_ and _y_ .

We shall refer to the 2 _×_ 2 matrix _M_ as the matrix corresponding to the linear transformation _L_ and often write _ML_ for the matrix _M_ .

The linear transformation _L_ in (1.16) is invertible if and only if the matrix _M_ is invertible. We shall only deal with invertible linear transformations in the sequel. The following are two standard properties of linear transformations that you need to familiar with for the sequel.

1. If _P_ is a parallelogram in R<sup>2</sup> , then _L_ ( _P_ ) is also a parallelogram in R<sup>2</sup> . In other words, linear transformations map parallelograms to parallelograms.

2. For every parallelogram _P_ , the following identity holds:


In other words, the ratio of the areas of _L_ ( _P_ ) to that of _P_ is given by the absolute value of the determinant of the matrix _ML_ .

#### **1.14.2 Invertible Linear Transformations**

Suppose _X, Y_ have joint density _fX,Y_ and let ( _U, V_ ) = _T_ ( _X, Y_ ) for a linear and invertible transformation _T_ : R<sup>2</sup> _→_ R<sup>2</sup> . Let the inverse transformation of _T_ be denoted by _S_ . In the example of the previous lecture, we hacd _T_ ( _x, y_ ) = ( _x, x_ + _y_ ) and _S_ ( _u, v_ ) = ( _u, v − u_ ). The fact that _T_ is assumed to be linear and invertible means that _S_ is also linear and invertible.

To compute _fU,V_ at a point ( _u, v_ ), we consider


for small _δ_ and _ϵ_ . Let _R_ denote the rectangle joining the points ( _u, v_ ) _,_ ( _u_ + _δ, v_ ) _,_ ( _u, v_ + _ϵ_ ) and ( _u_ + _δ, v_ + _ϵ_ ). Then the above probability is the same as


What is the region _S_ ( _R_ )? Clearly now _S_ ( _R_ ) is a small region (as _δ_ and _ϵ_ are small) around the point _S_ ( _u, v_ ) so that


_1.14. JOINT DENSITIES UNDER TRANSFORMATIONS_

35

By the facts mentioned in the previous subsection, we now note that _S_ ( _R_ ) is a parallelogram whose area equals _|det_ ( _MS_ ) _|_ multiplied by the area of _R_ (note that the area of _R_ equals _δϵ_ ). We thus have

_fU,V_ ( _u, v_ ) _δϵ ≈_ P _{_ ( _U, V_ ) _∈ R}_ = P _{_ ( _X, Y_ ) _∈ S_ ( _R_ ) _}_ = _fX,Y_ ( _S_ ( _u, v_ )) _|_ det( _MS_ ) _|δϵ_

which allows us to deduce that


It is helpful to remember here that _MS_ is the 2 _×_ 2 matrix corresponding to the linear transformation _S_ .

**Example 1.14.1.** _Suppose X and Y are independent standard normal random variables. Find the joint density of U_ = _X_ + _Y and V_ = _X − Y ._

_We can use the formula_ (1.17) _with T_ ( _x, y_ ) = ( _x_ + _y, x − y_ ) _whose inverse transformation is_ 1 _/_ 2 1 _/_ 2 _S_ ( _u, v_ ) = (<sup>_<u>u</u>_</sup><sup><u>+</u></sup> 2<sup>_<u>v</u>,_</sup><sup>_<u>u−</u>_</sup> 2<sup>_<u>v</u>_)</sup><sup>_andclearlythematrixcorrespondingtoSisgivenbyMS_=</sup> _. The_ �1 _/_ 2 _−_ 1 _/_ 2� _formula_ (1.17) _then gives_


_Because X and Y are independent standard normals, we have_


_so that_


_This implies that U and V are independent N_ (0 _,_ 2) _random variables._

**Example 1.14.2.** _Suppose X and Y are independent standard normal random variables. Then what is the distribution of_ ( _U, V_ ) = _T_ ( _X, Y_ ) _where_


_Geometrically the transformation T corresponds to rotating the point_ ( _x, y_ ) _by an angle θ in the counter clockwise direction. The inverse transformation S_ := _T_<sup>_−_1</sup> _of T is given by_


_and this corresponds to rotating the point_ ( _u, v_ ) _clockwise by an angle θ. The matrix corresponding to S is_


_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

36

_The formula_ (1.17) _then gives_


_This means that U and V are independent random variables each having the standard normal distribution._

We shall next study the problem of obtaining the joint densities under differentiable and invertible transformations that are not necessarily linear.

#### **1.14.3 General Invertible Transformations**

Let ( _X, Y_ ) have joint density _fX,Y_ . We transform ( _X, Y_ ) to two new random variables ( _U, V_ ) via ( _U, V_ ) = _T_ ( _X, Y_ ). What is the joint density _fU,V_ ? Suppose that _T_ is invertible (having an inverse _S_ = _T_<sup>_−_1</sup> ) and differentiable. Note that _S_ and _T_ are not necessarily linear transformations.

In order to compute _fU,V_ at a point ( _u, v_ ), we consider


for small _δ_ and _ϵ_ . Let _R_ denote the rectangle joining the points ( _u, v_ ) _,_ ( _u_ + _δ, v_ ) _,_ ( _u, v_ + _ϵ_ ) and ( _u_ + _δ, v_ + _ϵ_ ). Then the above probability is the same as


What is the region _S_ ( _R_ )? If _S_ is linear then _S_ ( _R_ ) (as we have seen previously) will be a parallelogram. For general _S_ , the main idea is that, as long as _δ_ and _ϵ_ are small, the region _S_ ( _R_ ) can be approximated by a parallelogram. This is because _S_ itself can be approximated by a linear transformation on the region _R_ . To see this, let us write the function _S_ ( _a, b_ ) as ( _S_ 1( _a, b_ ) _, S_ 2( _a, b_ )) where _S_ 1 and _S_ 2 map points in R<sup>2</sup> to R. Assuming that _S_ 1 and _S_ 2 are differentiable, we can approximate _S_ 1( _a, b_ ) for ( _a, b_ ) near ( _u, v_ ) by


Similarly, we can approximate _S_ 2( _a, b_ ) for ( _a, b_ ) near ( _u, v_ ) by


Putting the above two equations together, we obtain that, for ( _a, b_ ) close to ( _u, v_ ),


_1.15. JOINT DENSITIES UNDER GENERAL INVERTIBLE TRANSFORMATIONS_

37

Therefore _S_ can be appromixated by a linear transformation with matrix given by


for ( _a, b_ ) near ( _u, v_ ). Note that, in particular, when _δ_ and _ϵ_ are small, that this linear appximation for _S_ is valid over the region _R_ . The matrix _JS_ ( _u, v_ ) is called the Jacobian matrix of _S_ ( _u, v_ ) = ( _S_ 1( _u, v_ ) _, S_ 2( _u, v_ )) at the point ( _u, v_ ).

Because of the above linear approximation, we can write


This gives us the important formula


We will see some examples of calculations using the above formula in the next class.

### **1.15 Joint Densities under general invertible transformations**

Let ( _X, Y_ ) have joint density _fX,Y_ . We transform ( _X, Y_ ) to two new random variables ( _U, V_ ) via ( _U, V_ ) = _T_ ( _X, Y_ ). What is the joint density _fU,V_ ? Suppose that _T_ is invertible (having an inverse _S_ = _T_<sup>_−_1</sup> ) and differentiable. Note that _S_ and _T_ are not necessarily linear transformations.

In order to compute _fU,V_ at a point ( _u, v_ ), we consider


for small _δ_ and _ϵ_ . Let _R_ denote the rectangle joining the points ( _u, v_ ) _,_ ( _u_ + _δ, v_ ) _,_ ( _u, v_ + _ϵ_ ) and ( _u_ + _δ, v_ + _ϵ_ ). Then the above probability is the same as


What is the region _S_ ( _R_ )? If _S_ is linear then _S_ ( _R_ ) (as we have seen previously) will be a parallelogram. For general _S_ , the main idea is that, as long as _δ_ and _ϵ_ are small, the region _S_ ( _R_ ) can be approximated by a parallelogram. This is because _S_ itself can be approximated by a linear transformation on the region _R_ . To see this, let us write the function _S_ ( _a, b_ ) as ( _S_ 1( _a, b_ ) _, S_ 2( _a, b_ )) where _S_ 1 and _S_ 2 map points in R<sup>2</sup> to R. Assuming that _S_ 1 and _S_ 2 are differentiable, we can approximate _S_ 1( _a, b_ ) for ( _a, b_ ) near ( _u, v_ ) by


_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

38

Similarly, we can approximate _S_ 2( _a, b_ ) for ( _a, b_ ) near ( _u, v_ ) by


Putting the above two equations together, we obtain that, for ( _a, b_ ) close to ( _u, v_ ),


Therefore _S_ can be appromixated by a linear transformation with matrix given by


for ( _a, b_ ) near ( _u, v_ ). Note that, in particular, when _δ_ and _ϵ_ are small, that this linear appximation for _S_ is valid over the region _R_ . The matrix _JS_ ( _u, v_ ) is called the Jacobian matrix of _S_ ( _u, v_ ) = ( _S_ 1( _u, v_ ) _, S_ 2( _u, v_ )) at the point ( _u, v_ ).

Because of the above linear approximation, we can write


This gives us the important formula


**Example 1.15.1.** _Suppose X and Y have joint density fX,Y . What is the joint density of U_ = _X/Y and V_ = _Y ?_

_We need to compute the joint density of_ ( _U, V_ ) = _T_ ( _X, Y_ ) _where T_ ( _x, y_ ) = ( _x/y, y_ ) _. The inverse of this transformation is S_ ( _u, v_ ) = ( _uv, v_ ) _. Then formula_ (1.19) _gives_


_As a consequence, the marginal density of U_ = _X/Y is given by_


_In the special case when X and Y are independent standard normal random variables, the density of U_ = _X/Y is given by_


_This is the standard Cauchy density._

_1.16. JOINT DENSITIES UNDER NON-INVERTIBLE TRANSFORMATIONS_

39

**Example 1.15.2.** _Suppose X and Y are independent standard normal random variables. Let R_ := _√X_<sup>2</sup> + _Y_<sup>2</sup> _and let_ Θ _denote the angle made by the vector_ ( _X, Y_ ) _with the positive X-axis in the plane. What is the joint density of_ ( _R,_ Θ) _?_

_Clearly_ ( _R,_ Θ) = _T_ ( _X, Y_ ) _where the inverse of T is given by S_ ( _r, θ_ ) = ( _r_ cos _θ, r_ sin _θ_ ) _. The density of f_ ( _R,_ Θ) _at_ ( _r, θ_ ) _is zero unless r >_ 0 _and_ 0 _< θ <_ 2 _π. The formula_ (1.19) _then gives_


_It is easy to see from here that_ Θ _is uniformly distributed on_ (0 _,_ 2 _π_ ) _and R has the density_


_Moreover R and_ Θ _are independent. The density of R is called the Rayleigh density._

**Example 1.15.3.** _Here is an important fact about Gamma distributions: Suppose X ∼ Gamma_ ( _α_ 1 _, λ_ ) _and Y ∼ Gamma_ ( _α_ 2 _, λ_ ) _are independent, then X_ + _Y ∼ Gamma_ ( _α_ 1 + _α_ 2 _, λ_ ) _. This can be proved using the convolution formula for densities of sums of independent random variables. A different formula uses the Jacobian formula to derive the joint density of U and V where V_ = _X/_ ( _X_ + _Y_ ) _. The relevant inverse transformation here S_ ( _u, v_ ) = ( _uv, u − uv_ ) _so that the Jacobian formula gives:_


_Plugging in the relevant Gamma densities for fX and fY , we can deduce that_


_This implies that U ∼ Gamma_ ( _α_ 1 + _α_ 2 _, λ_ ) _. It also implies that V ∼ Beta_ ( _α_ 1 _, α_ 2) _, that U and V are independent as well as_


_where, on the right hand side above, we have the Beta function. Note that because_ Γ( _n_ ) = ( _n −_ 1)! _for when n is an integer, the above formiula gives us a way to calculate the Beta function B_ ( _α_ 1 _, α_ 2) _when α_ 1 _and α_ 2 _are positive integers._

### **1.16 Joint Densities under Non-Invertible Transformations**

In the last class, we looked at the Jacobian formula for calculating the joint density of a transformed set of continuous random variables in terms of the joint density of the original random variables. This formula assumed that the transformation is invertible. In other words, the formula does not work if the transformation is non-invertible. However, the general method based on first principles (that we used to derive the Jacobian formula) works fine. This is illustrated in the following example.

40

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

**Example 1.16.1** (Order Statistics) **.** _Suppose X and Y have joint density fX,Y . What is the joint density of U_ = min( _X, Y_ ) _and V_ = max( _X, Y_ ) _?_

_Let us find the joint density of_ ( _U, V_ ) _at_ ( _u, v_ ) _. Since U < V , the density fU,V_ ( _u, v_ ) _will be zero when u ≥ v. So let u < v. For δ and ϵ small, let us consider_


_If δ and ϵ are much smaller compared to v − u, then the above probability equals_


_which is further approximately equal to_

_fX,Y_ ( _u, v_ ) _δϵ_ + _fX,Y_ ( _v, u_ ) _δϵ._

_We have thus proved that_


_We can generalize this to the case of more than two random variables. Suppose X_ 1 _, . . . , Xn are random variables having a joint density fX_ 1 _,...,Xn_ ( _x_ 1 _, . . . , xn_ ) _. Let X_ (1) _≤· · · ≤ X_ ( _n_ ) _denote the_ **_order statistics_** _of X_ 1 _, . . . , Xn i.e., X_ (1) _is the smallest value among X_ 1 _, . . . , Xn, X_ (2) _is the next smallest value and so on with X_ ( _n_ ) _denoting the largest value. What then is the joint distribution of X_ (1) _, . . . , X_ ( _n_ ) _. The calculation above for the case of the two variables can be easily generalized to obtain_


_where the sum is over all permutations π (i.e, one-one and onto functions mapping {_ 1 _, . . . , n} to {_ 1 _, . . . , n})._

_When the variables X_ 1 _, . . . , Xn are i.i.d (independent and identically distributed), then it follows from the above that_


### **1.17 Joint Density of Order Statistics**

In the last class, we looked at the Jacobian formula for calculating the joint density of a transformed set of continuous random variables in terms of the joint density of the original random variables. This formula assumed that the transformation is invertible. In other words, the formula does not work if the transformation is non-invertible. However, the general method based on first principles (that we used to derive the Jacobian formula) works fine. This is illustrated in the following example.

_1.18. MORE ON ORDER STATISTICS: THE DENSITY OF X_ ( _I_ ) _FOR A FIXED I_

41

**Example 1.17.1** (Order Statistics) **.** _Suppose X and Y have joint density fX,Y . What is the joint density of U_ = min( _X, Y_ ) _and V_ = max( _X, Y_ ) _?_

_Let us find the joint density of_ ( _U, V_ ) _at_ ( _u, v_ ) _. Since U < V , the density fU,V_ ( _u, v_ ) _will be zero when u ≥ v. So let u < v. For δ and ϵ small, let us consider_


_If δ and ϵ are much smaller compared to v − u, then the above probability equals_


_which is further approximately equal to_


_We have thus proved that_


_We can generalize this to the case of more than two random variables. Suppose X_ 1 _, . . . , Xn are random variables having a joint density fX_ 1 _,...,Xn_ ( _x_ 1 _, . . . , xn_ ) _. Let X_ (1) _≤· · · ≤ X_ ( _n_ ) _denote the_ **_order statistics_** _of X_ 1 _, . . . , Xn i.e., X_ (1) _is the smallest value among X_ 1 _, . . . , Xn, X_ (2) _is the next smallest value and so on with X_ ( _n_ ) _denoting the largest value. What then is the joint distribution of X_ (1) _, . . . , X_ ( _n_ ) _. The calculation above for the case of the two variables can be easily generalized to obtain_


_where the sum is over all permutations π (i.e, one-one and onto functions mapping {_ 1 _, . . . , n} to {_ 1 _, . . . , n})._

_When the variables X_ 1 _, . . . , Xn are i.i.d (independent and identically distributed), then it follows from the above that_


### **1.18 More on Order Statistics: The density of** _X_ ( _i_ ) **for a fixed** _i_

Assume now that _X_ 1 _, . . . , Xn_ are i.i.d random variables with a common density _f_ and cdf _F_ . In the previous section, we derived the joint density of the order statistics _X_ (1) _, . . . , X_ ( _n_ ). Here we focus on

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

42

the problem of determining the density of _X_ ( _i_ ) for a fixed _i_ . The answer is given by


and there are three standard methods for deriving this.

#### **1.18.1 Method One**

The first method integrates the joint density _fX_ (1) _,...,X_ ( _n_ )( _u_ 1 _, . . . , ui−_ 1 _, u, ui_ +1 _, . . . un_ ) over _u_ 1 _, . . . , ui−_ 1 _, ui_ +1 _, . . . , un_ to obtain _fX_ ( _i_ )( _u_ ). More precisely, _fX_ ( _i_ )( _u_ ) = _· · · n_ ! _f_ ( _u_ 1) _. . . f_ ( _ui−_ 1) _f_ ( _u_ ) _f_ ( _ui_ +1) _. . . f_ ( _un_ ) _I{u_ 1 _< · · · < un}du_ 1 _. . . dui−_ 1 _dui_ +1 _. . . dun_ � �

Integrate the above first with respect to _u_ 1 (in the range ( _−∞, u_ 2)), then with respect to _u_ 2 (in the range of ( _−∞, u_ 3)) and all the way up to the integral with respect to _ui−_ 1. Then integrate with respect to _un_ , then with respect to _un−_ 1 and all the way to _ui_ +1. This will lead to (1.22).

#### **1.18.2 Method Two**

This method uses multinomial probabilities. Suppose that we repeat an experiment _n_ times and that the outcomes of the _n_ repetitions are independent. Suppose that each individual experiment has _k_ outcomes which we denote by _O_ 1 _, . . . , Ok_ and let the probabilities of these outcomes be given by _p_ 1 _, . . . , pk_ (note that these are nonnegative numbers which sum to one).

Now let _Ni_ denote the number of times (over the _n_ repetitions) that the outcome _Oi_ appeared (note that _N_ 1 _, . . . , Nk_ are nonnegative integers which sum to _n_ ). The joint distribution of ( _N_ 1 _, . . . , Nk_ ) is known as the multinomial distribution with parameters _n_ and _p_ 1 _, . . . , pk_ . It is an exercise to show that


whenever _n_ 1 _, . . . , nk_ are nonnegative integers which sum to _n_ .

Let us now get back to the problem of obtaining the density of _X_ ( _i_ ). Consider the probability


for a fixed _u_ and small _δ_ . If _δ_ is small, then this probability can be approximated by the probability of the event _E_ where _E_ is defined as follows. _E_ is the event where ( _i −_ 1) observations among _X_ 1 _, . . . , Xn_ are strictly smaller than _u_ , one observation among _X_ 1 _, . . . , Xn_ lies in [ _u, u_ + _δ_ ] and _n − i_ observations among _X_ 1 _, . . . , Xn_ are strictly larger than _u_ + _δ_ . This latter probability is a special case of the multinomial probability formula (1.21) and when _δ_ is small, we get that this probability equals


where _F_ is the cdf corresponding to _f_ . The formula (1.22) then immediately follows.

_1.19. ORDER STATISTICS_

43

#### **1.18.3 Method Three**

Here we first compute the cdf of _X_ ( _i_ ) and then differentiate it to get the pdf. Note that


To compute the density, we have to differentiate _FX_ ( _i_ ) with respect to _x_ . This gives (note that the derivative of _F_ is _f_ )


and thus we again get the formula (1.22).

In the next class, we shall look at some special instances of the formula (1.22) for the density of individual order statistics.

### **1.19 Order Statistics**

In the last class, we calculated the density of _X_ ( _i_ ) where _X_ (1) _, . . . , X_ ( _n_ ) are the order statistics of _n_ i.i.d random variables _X_ 1 _, . . . , Xn_ . If _f_ and _F_ are the common density and cdf of each _Xi_ , then


We now look at some special instances of the formula (1.22).

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

44

#### **1.19.1 Uniform Order Statistics**

Suppose _X_ 1 _, . . . , Xn_ are i.i.d having the uniform density on (0 _,_ 1). Then the formula (1.22) (by plugging in _f_ ( _u_ ) = 1 and _F_ ( _u_ ) = _u_ for 0 _< u <_ 1) gives the following density for _X_ ( _i_ ):


This is a Beta density with parameters _i_ and _n − i_ + 1. Generally, a Beta density with parameters _α >_ 0 and _β >_ 0 is given by


The integral in the denominator above is called the Beta function:


The Beta function does not usually have a closed form expression but we can write it in terms of the Gamma function via the formula


that we saw in the last class. This formula allows us to write _B_ ( _α, β_ ) in closed form when _α_ and _β_ are integers (note that Γ( _n_ ) = ( _n −_ 1)!). This gives, for example,


#### **1.19.2 Maximum of Independent Uniforms**

Suppose _X_ 1 _, . . . , Xn_ are independent random variables having the uniform distribution on the interval (0 _, θ_ ) for some _θ >_ 0. It turns out that the maximum order statistic, _X_ ( _n_ ), is the maximum likelihood estimate of _θ_ . The density of _X_ ( _n_ ) is easily seen to be (as a consequence of (1.22)):


What then is E( _X_ ( _n_ ))? Using the formula for the density above,


This means therefore that _X_ ( _n_ ) has a slight negative bias of _−θ/_ ( _n_ + 1) as an estimator for _θ_ and that (( _n_ + 1) _/n_ ) _X_ ( _n_ ) is an unbiased estimator of _θ_ .

_1.19. ORDER STATISTICS_

45

#### **1.19.3 Minimum of Independent Exponentials**

Recall that the exponential density with rate parameter _λ >_ 0 (denoted by _Exp_ ( _λ_ )) is given by


The cdf of _Exp_ ( _λ_ ) is easily seen to be


Suppose now that _X_ 1 _, . . . , Xn_ are i.i.d observations from _Exp_ ( _λ_ ). What is the density of _X_ (1)? From the formula (1.22):


Thus _X_ (1) has the Exponential density with rate parameter _nλ_ .

#### **1.19.4 Minimum of Independent Non-Identically Distributed Exponentials**

Suppose _X_ 1 _, . . . , Xn_ are independent random variables with _Xi_ having the _Exp_ ( _λi_ ) distribution for some _λi >_ 0. What then is the distribution of _X_ (1) := min1 _≤i≤n Xi_ . We cannot use the formula (1.22) in this case as the _Xi_ ’s have different distributions. We can however calculate the cdf of _X_ (1) easily in the following way. For _x >_ 0, we have


Differentiate this with respect to _x_ to obtain


Thus _X_ (1) _∼ Exp_ ( _λ_ 1 + _· · ·_ + _λn_ ).

#### **1.19.5 Minimum of Independent Non-identically distributed Geometrics**

Suppose _X_ 1 _, . . . , Xn_ are independent random variables with _Xi ∼ Geo_ ( _pi_ ) for _i_ = 1 _, . . . , n_ . What is the distribution of _X_ (1) := min1 _≤i≤n Xi_ . Since the random variables involved here are discrete, we cannot use any formula that we have so far derived. We have to calculate the probability P _{X_ (1) = _m}_

_CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

46

for _m_ = 1 _,_ 2 _, . . ._ from first principles. It is easy to first calculate the cdf:


where _P_ := 1 _−_ (1 _− p_ 1) _. . ._ (1 _− pn_ ). This gives


Thus _X_ (1) is a Geometric random variable with parameter _P_ = 1 _−_ (1 _− p_ 1)(1 _− p_ 2) _. . ._ (1 _− pn_ ).

### **1.20 Covariance, Correlation and Regression**

Given two random variables _X_ and _Y_ , the covariance between _X_ and _Y_ is denoted by _Cov_ ( _X, Y_ ) and is defined as


where _µX_ := E( _X_ ) and _µY_ := E( _Y_ ). In other words, _Cov_ ( _X, Y_ ) is defined as the Expectation of the random variable ( _X − µX_ )( _Y − µY_ ).

It is important to note that Covariance is a bilinear operator i.e.,


Can you prove this as a consequence of the definition (1.24) of Covariance and the linearity of the Expectation operator?

When _X_ = _Y_ , it is easy to see that _Cov_ ( _X, X_ ) is simply the Variance of _X_ . Using this connection between Covariance and Variance and (1.25), can you deduce the following standard properties of Variance:


The correlation between two random variables _X_ and _Y_


If _ρX,Y_ = 0, we say that _X_ and _Y_ are _uncorrelated_ .

_1.20. COVARIANCE, CORRELATION AND REGRESSION_

47

**Proposition 1.20.1.** _Two facts about correlation:_

_1. The correlation ρX,Y always lies between −_ 1 _and 1._

_2. ρaX_ + _b,cX_ + _d_ = _|aa| |cc|_<sup>_ρX,Yforeverya, b, c, d ∈_(</sup><sup>_−∞, ∞_)</sup><sup>_.Inwords,correlationisinvariant(upto_</sup> _sign flips) under linear transformations._

_Proof._ Write


Use the standard inequality:


This proves that _ρX,Y ≤_ 1. To prove that _ρX,Y ≥−_ 1, argue similarly by using


The fact about correlations and linear functions is left as an exercise.

**Cauchy-Schwartz Inequality** : The fact that correlation _ρX,Y_ lies between -1 and 1 is sometimes proved via the Cauchy-Schwartz inequality which states the following: For every pair of random variables _Z_ 1 and _Z_ 2, we have


The fact that _|ρX,Y | ≤_ 1 is deduced from the above inequality by taking _Z_ 1 = _X −µX_ and _Z_ 2 = _Y −µY_ . Can you prove the Cauchy-Schwarz inequality (1.28) using (1.26) and (1.27)?

**Uncorrelatedness and Independence** : The following summarizes the relation between uncorrelatedness and independence:

1. Two independent random variables _X_ and _Y_ are uncorrelated.

2. There exist numerous examples of pairs of uncorrelated random variables _X_ and _Y_ that are **NOT** independent. Can you think of a few?

3. Two random variables _X_ and _Y_ are independent **if and only if** _g_ ( _X_ ) and _h_ ( _Y_ ) are uncorrelated for **every** pair of functions _g_ and _h_ .

48 _CHAPTER 1. REVIEW OF UNDERGRADUATE PROBABILITY_

An important property of _ρX,Y_ is that it measures the strength of _linear association_ between _X_ and _Y_ . This is explained in this section. Consider the problem of _approximating_ the random variable _Y_ by a **linear** function _β_ 0 + _β_ 1 _X_ of _X_ . For given numbers _β_ 0 and _β_ 1, let us measure the accuracy of approximation of _Y_ by _β_ 0 + _β_ 1 _X_ by the _mean-squared error_ :


If _β_ 0 + _β_ 1 _X_ is a good approximation of _Y_ , then _L_ ( _β_ 0 _, β_ 1) should be low. Conversely, if _β_ 0 + _β_ 1 _X_ is a poor approximation of _Y_ , then _L_ ( _β_ 0 _, β_ 1) should be high. What is the smallest possible value of _L_ ( _β_ 0 _, β_ 1) as _β_ 0 and _β_ 1 vary over all real numbers.

It can be shown that


Do you know how to prove the above?

The fact (1.29) precisely captures the interpretation that correlation measures the strength of linear association between _Y_ and _X_ . This is because min _β_ 0 _,β_ 1 _L_ ( _β_ 0 _, β_ 1) represents the smallest possible mean squared error in approximating _Y_ by a linear combination of _X_ and (1.29) says that it is directly related to the correlation between _Y_ and _X_ .

Can you explicitly write down the values of _β_ 0 and _β_ 1 which minimize _L_ ( _β_ 0 _, β_ 1)?

Does any of the above remind you of linear regression? In what way?

## **Chapter 2**

---

[← Contents](01-contents.md) · [Up: contents](index.md) · [Conditioning →](03-conditioning.md)
