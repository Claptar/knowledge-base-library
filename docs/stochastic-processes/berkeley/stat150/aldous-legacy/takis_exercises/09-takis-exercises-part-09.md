---
title: Takis exercises Part 09 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 09 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Five white balls and five black balls are distributed in two urns in such a way that each urn contains five balls. At each step we draw one ball from each urn and exchange them. Let Xn be the number of white balls in the left urn at time n.

(a) Compute the transition probability for Xn.

(b) Find the stationary distribution and show that it corresponds to picking five balls at random to be in the left urn.

Solution Clearly, (X0, X1, X2, . . .) is a Markov chain with state space


27

(a) If, at some point of time, Xn = x (i.e. the number of white balls in the left urn is x) then there are 5 − x black balls in the left urn, while the right urn contains x black and 5 − x white balls. Clearly,


as long as x < 5. On the other hand,


as long as x > 0. When 0 < x < 5, we have


because there is no chance that the number of balls change by more than 1 ball. Summarising, the answer is:


If you want, you may draw the transition diagram:


On this diagram, I did not indicate the px,x.

(b) To compute the stationary distribution, cut the diagram between states x and x − 1 and equate the two flows, as usual:


i.e.


which gives


28

We thus have


We find π(0) by normalisation:


Putting everything together, we have


This is the answer for the stationary distribution. We are also asked to interpret π(x) as

From a lot of 10 (= 5 black + 5 white balls) pick 5 at random and place them in the left urn (place the rest in the right urn) and consider the chance that amongst the 5 balls x are white.

We know how to answer this problem: it is a hypergeometric distribution:

Chance that amongst the 5 balls x are white =


This is PRECISELY the distribution obtained above. Hence π(x) IS A HYPERGEOMETRIC DISTRIBUTION.

30.

An auto insurance company classifies its customers in three categories: poor, satisfactory and preferred. No one moves from poor to preferred or from preferred to poor in one year. 40% of the customers in the poor category become satisfactory, 30% of those in the satisfactory category moves to preferred, while 10% become poor; 20% of those in the preferred category are downgraded to satisfactory.

(a) Write the transition matrix for the model.

(b) What is the limiting fraction of drivers in each of these categories? (Clearly state which theorem you are applying in order to compute this.)

29

Solution. (a) The transition probabilities for this Markov chain with three states are as follows:


so that the transition probability matrix is


(b) We will find the limiting fraction of drivers in each of these categories from the components of the stationary distribution vector π, which satisfies the following equation:


The former is equivalent to the following system of linear equations:


This has the following solution: π = ( 11<sup>1,</sup> 11<sup>4,</sup> 11<sup>6).</sup> Thus, the limiting fraction of drivers in the POOR category is 111<sup>,intheSATIS-</sup> FACTORY category— 11<sup>4,andinthePREFERREDcategory—</sup> 11<sup>6.Bytheway,the</sup> proportions of the drivers in each category in 15 years approximate these numbers with two significant digits (you can check it, calculating P<sup>15</sup> and looking at its rows).

31.

The President of the United States tells person A his or her intention to run or not to run in the next election. Then A relays the news to B, who in turn relays the message to C, and so forth, always to some new person. We assume that there is a probability a that a person will change the answer from yes to no when transmitting it to the next person and a probability b that he or she will change it from no to yes. We choose as states the message, either yes or no. The transition probabilities are


The initial state represents the President’s choice. Suppose a = 0.5, b = 0.75. (a) Assume that the President says that he or she will run. Find the expected length of time before the first time the answer is passed on incorrectly.

(b) Find the mean recurrence time for each state. In other words, find the expected amount of time ri, for i = yes and i = no required to return to that state.

(c) Write down the transition probability matrix P and find limn→∞ P<sup>n</sup> .

30

- (d) Repeat (b) for general a and b.

(e) Repeat (c) for general a and b.

Solution. (a) The expected length of time before the first answer is passed on incorrectly, i.e. that the President will not run in the next election, equals the mean of the geometrically distributed random variable with parameter 1 − pyes,no = 1 − a = 0.5. Thus, the expected length of time before the first answer is passed on incorrectly is 2. What is found can be viewed as the mean first passage time from the state yes to the state no. By making the corresponding ergodic Markov chain with transition matrix


absorbing (with absorbing state being no), check that the time until absorption will be 2. This is nothing but the mean first passage time from yes to no in the original Markov chain.

(b) We use the following result to find mean recurrence time for each state:

for an ergodic Markov chain, the mean recurrence time for state i is


where π(i) is the ith component of the stationary distribution for the transition probability matrix.

The transition probability matrix (8) has the following stationary distribution:


from which we find the mean recurrence time for the state yes is 3<sup>5andforthestate</sup> no is<sup>5</sup>

2<sup>.</sup>

(c) The transition probability matrix is specified in (8)—it has no zero entries and the corresponding chain is irreducible and aperiodic. For such a chain

Thus,


(d) We apply the same arguments as in (b) and find that the transition probability matrix


has the following fixed probability vector:

so that the mean recurrence time for the state yes is 1 +<sup>a</sup> b<sup>andforthestatenois</sup> 1 + a<sup>b.</sup>

(d) Suppose a̸ = 0 and b̸ = 0 to avoid absorbing states and achieve regularity. Then the corresponding Markov chain is regular. Thus,


31

32.

A fair die is rolled repeatedly and independently. Show by the results of the Markov chain theory that the mean time between occurrences of a given number is 6.

Solution. We construct a Markov chain with the states 1, 2, . . . , 6 and transition probabilities pij =<sup>1</sup> 6<sup>foreachi, j=1, 2, . . . , 6.SuchMarkovchainhasthetransition</sup> probability matrix which has all its entries equal to 6<sup>1.Thechainisirreducibleand</sup> aperiodic and its stationary distribution is nothing but


This means that the mean time between occurrences of a given number is 6.

33.

Give an example of a three-state irreducible-aperiodic Markov chain that is not reversible.

Solution.

We will see how to choose transition probabilities in such a way that the chain would not be reversible.

If our three-state chain was a reversible chain, that would meant that the detailed balance equations hold, i.e.


From this it is easy to see that if the detailed balance equations hold, then necessarily p13p32p21 = p12p23p31. So, choose them in such a way that this does not hold. For instance, p13 = 0.7, p32 = 0.2, p21 = 0.3, p12 = 0.2, p23 = 0.2, p31 = 0.1. And these specify an ergodic Markov chain which is not reversible.

Another solution is: Consider the Markov chain with three states {1, 2, 3} and deterministic transitions: 1 → 2 → 3 → 1. Clearly, the Markov chain in reverse time moves like 1 → 3 → 2 → 1 and so its law is not the same. (We can tell the arrow of time by running the film backwards.)

34.

Let P be the transition matrix of an irreducible-aperiodic Markov chain. Let π be its stationary distribution. Suppose the Markov chain starts with P (X0 = i) = π(i), for all i ∈ S.

(a) [Review question] Show that P (Xn = i) = π(i) for all i ∈ S and all n.

(b) Fix N ≥ 1 and consider the process X0<sup>∗=XN, X</sup> 1<sup>∗=XN−1, . . .Showthatitis</sup> Markov.

(c) Let P<sup>∗</sup> be the transition probability matrix of P<sup>∗</sup> (it is called: the reverse transition matrix). Find its entries p<sup>∗</sup> i,j<sup>.</sup>

(d) Show that P and P<sup>∗</sup> they have the same stationary distribution π.

Solution. (a) By definition, π(i) satisfies


32

If P (X0 = i) = π(i), then


Hence P (X1 = i) ≡ π(i). Repeating the process we find P (X2 = i) ≡ π(i), and so on, we have P (Xn = i) ≡ π(i) for all n.

(b) Fix n and consider the future of X<sup>∗</sup> after n. This is X<sup>∗</sup> n + 1, X<sup>∗</sup> n + 2, . . .. Consider also the past of X<sup>∗</sup> before n. This is Xn<sup>∗</sup> −1<sup>, X</sup> n<sup>∗</sup> −2<sup>, . . ..But</sup>


is the past of X before time N − n. And


is the future of X after time N − n. Since X is Markov, these are independent, conditional on XN −n. But XN −n = Xn<sup>∗.Hence,givenX</sup> n<sup>∗,thefutureofX∗afternis</sup> independent of the past of X<sup>∗</sup> before n, and this is true for all n, and so X<sup>∗</sup> is also Markov.

(c) Here we assume that P (X0 = i) ≡ π(i). Hence, by (a), P (Xn = i) ≡ π(i) for all n. We have


(d) We need to check that, for all i ∈ S,

This is a matter of algebra.

35.

Consider a random walk on the following graph consisting of two nested dodecagons:


33

- (a) Explain why it is reversible (this is true for any RWonG).

- (b) Find the stationary distribution.

(c) Show that the mean recurrence time (mean time to return) to any state is the same for all states, and compute this time.

(d) Let Xn be the position of the chain at time n (it takes values in a set of 24 elements). Let Zn = 1 if Xn is in the inner dodecagon and Zn = 2 is Xn is at the outer dodecagon. Is (Zn) Markov?

Solution. (a) Our chain has 24 states. From each of the states we jump to any of three neighbouring states with equal probability<sup>1</sup> 3<sup>(seethefigurebelow:eachundirected</sup> edge combines two directed edges-arrows). The chain is reversible, i.e. it is possible to move from any state to any other state. This is obviously the case for any random walk on a connected graph. Note that the notion of reversibility of the discrete Markov chain is related to the topology of the graph on which the chain is being run.


<!-- Start of picture text -->
12<br>11 1/3 1/3 1<br>1/3<br>24<br>23 13<br>10 2<br>22 14<br>9 21 15 3<br>20 16<br>8 19 17 4<br>18<br>7 5<br>6<br><!-- End of picture text -->

(b) The stationary distribution exists and because of the symmetry the stationary vector has all components equal, and since the number of the components is 24 the stationary vector is


(c) The mean recurrence time for the state i is 1/π(i) = 24, ∀i = 1, 2, . . . , 24. (d) Observe first that


and


We now verify that (Zn) is Markov. (We shall argue directly. Alternatively, see section on “functions of Markov chains” from my lecture notes.) By the definition of conditional probability,


34

Due to the fact that (Xn) is Markov, when we know that Xn = i that the future after n is independent from the past before n. But Zn+1 belongs to the future after n, while Zn−1 = w, . . . belongs to the past before n. Hence, for i = 13, . . . , 24,

P (Zn+1 = 2|Xn = i, Zn = 1, Zn−1 = w, . . .) = P (Zn+1 = 2|Xn = i) = 1/3.

Hence


because, obviously,


(If Zn = 1 then Xn is in the inside dodecagon.) Thus,


Similarly, we can show


Hence, no matter what the value of Zn is, the future of Z after n is independent of the past of Z before n. Hence Z is Markov as well.

36.

Consider a Markov chain in the set {1, 2, 3} with transition probabilities


where 0 < p < 1. Determine whether the Markov chain is reversible.

Solution. If p = 1/2 then the chain is a random walk on a graph; so it is reversible. If p̸ = 1/2 then Kolmogorov’s loop criterion requires that


But this is equivalent to


which is not true (unless p = 1/2). Hence the chain is not reversible if p̸ = 1/2.

37.

Consider a Markov chain whose transition diagram is as below:


- (ii) Which (if any) states are absorbing?

- (v) Find the period of each essential state. Verify that essential states that belong to the same communication class have the same period.

- (vi) Are there any aperiodic communication classes? (vii) Will your answers to the questions (i)–(vi) change if we replace the positive transition probabilities by other positive probabilities and why?

35

Solution. (i) The inessential states are: 1, 2, 3, 5, 6, because each of them leads to a state from which it is not possible to return.

(ii) 4 is the only absorbing state.

(iii) As usual, let [i] denote the class of state i i.e. [i] = {j ∈ S : j ↭ i}. We have: [1] = {1}. [2] = {2}. [3] = {3}. [4] = {4}. [5] = {5, 6}. [6] = {5, 6}. [7] = {7, 8}. [8] = {7, 8}. [9] = {9, 10, 11} [10] = {9, 10, 11} [11] = {9, 10, 11}

Therefore there are 7 communication classes:


(iv) No because there are many communication classes.

(v) Recall that for each essential state i, its period d(i) is the gcd of all n such that pi,i<sup>(n)> 0.So:</sup>


Observe d(7) = d(8) = 1, and d(10) = d(11) = d(9) = 3.

(vi) Yes: {4} and {7, 8} are aperiodic communication classes (each has period 1). (vii) No the answers will not change. These questions depend only on whether, for each i, j, pi,j is positive or zero.

38.

Consider a Markov chain, with state space S the set of all positive integers, whose transition diagram is as follows:


(i) Which states are essential and which inessential?

(ii) Which states are transient and which recurrent?

(iii) Discuss the asymptotic behaviour of the chain, i.e. find the limit, as n →∞, of Pi(Xn = j) for each i and j.

36

Solution. (i) The states 3, 4, 5, . . . communicate with one another. So they are all essential. However state 1 leads to 3 but 3 does not lead to 1. Hence 1 is inessential. Likewise, 2 is inessential.

(ii) Every inessential state is transient. Hence both 1 and 2 are transient. On the other hand, the Markov chain will eventually take values only in the set {3, 4, 5, . . .}. We observe that the chain on this set is the same type of chain we discussed in gambler’s ruin problem with p = 2/3, q = 1/3. Since p > q the chain is transient. Therefore all states of the given chain are transient.

(iii) Since the states are transient, we have that Xn →∞ as n →∞, with probability 1. Therefore,


for all i and j.

39.

Consider the following Markov chain, which is motivated by the “umbrellas problem” (see–but it’s not necessary–an earlier exercise). Here, p + q = 1, 0 < p < 1.


(i) Is the chain irreducible?

(ii) Does it have a stationary distribution?

Hint: Write the balance equations, together with the normalisation condition and draw your conclusions.

(iii) Find the period d(i) of each state i.

(iv) Decide which states are transient and which recurrent.

Hint: Let τj be the first hitting time of state j. Let N ≥ 1 As in the gambler’s ruin problem, let ϕ(i) := Pi(τN < τ0). What is ϕ(0)? What is ϕ(N )? For 1 < i < N , how does ϕ(i) relate to ϕ(i − 1) and ϕ(i + 1)? Solve the equations you thus obtain to find ϕ(i). Let N →∞. What do you conclude?

Solution. (i) Yes because all states communicate with one another. (There is just one communication class).

(ii) Let us write balance equations in the form of equating flows (see handout). We have


Let π(1) = c. Then π(0) = cq and


The normalisation condition is<sup>�∞</sup> i=0<sup>π(i)=1.</sup> This implies that c = 0. Hence π(i) = 0 for all i. This is NOT a probability distribution. Hence there is no stationary distribution.

37

(iii) We only have to find the period of one state, since all states communicate with one another. Pick state 0. We have d(0) = gcd{2, 4, 6, . . .} = 2. Hence d(i) = 2 for all i.

(iv) Let ϕ(i) := Pi(τN < τ0). We have


Indeed, if X0 = 0 then τ0 = 0 and so ϕ(0) = P0(τN < 0) = 0. On the other hand, if X0 = N then τN = 0 and τ0 ≥ 1, so ϕ(N ) = PN (0 < τ0) = 1. Now, from first-step analysis, for each i ∈ [1, N − 1], we have


But pi,i+1 = pi,i−1 = p if i is odd and pi,i+1 = pi,i−1 = q if i is even and positive. So


Hence


and, in general,


Next, use the “fundamental theorem of (discrete) calculus”:

ϕ(i) = [ϕ(i) − ϕ(i − 1)] + [ϕ(i − 1) − ϕ(i − 2)] + · · · + [ϕ(2) − ϕ(1)] + ϕ(1).

If i is even then, amongst 1, 2, . . . , i there are i/2 even numbers and i/2 odd numbers.


Suppose N is even. Use ϕ(N ) = 1 to get that, if both i and N are even,


Taking the limit as N →∞, we find


This implies that Pi(τ0 < ∞) = 1. The same conclusion holds for i odd. (After all, all states communicate with one another.) Therefore all states are recurrent.

38

40.

Suppose that X1, X2 . . . are i.i.d. random variables with values, say, in Z and common distribution p(i) := P (X1 = i), i ∈ Z.

(i) Explain why the sequence has the Markov property. (ii) Let A be a subset of the integers such that<sup>�</sup> i∈A<sup>p(i)>0.Considerthefirst</sup> hitting time τA of A and the random variable Z := XτA. Show that the distribution of Z is the conditional distribution of X1 given that X1 ∈ A. Hint: Clearly, {Z = i} =<sup>�∞</sup> n=1<sup>{Z=i, τA=n},andtheeventsinthisunionare</sup> disjoint; therefore the probability of the union is the sum of the probabilities of the events comprising it.

Solution. (i) As explained in the beginning of the lectures.

(ii) Since τA is the FIRST time that A is hit, it means that


Therefore, with Z = XτA, and i ∈ A,


If i̸ ∈ A, then, obviously, P (Z = i) = 0. So it is clear that P (Z = i) = P (X1 = i|X1 ∈ A), for all i, from the definition of conditional probability.

---

[← Takis exercises Part 08 —](08-takis-exercises-part-08.md) · [Up: contents](index.md) · [Takis exercises Part 10 — →](10-takis-exercises-part-10.md)
