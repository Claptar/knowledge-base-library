---
title: 03 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/03-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 03 solutions

**Source:** `solutions/03-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Problem Set 3 Solutions Due September 29, 2010

1. The hats of n persons are thrown into a box. The persons then pick up their hats at random (i.e., so that every assignment of the hats to the persons is equally likely). What is the probability that

   - (a) every person gets his or her hat back?

<u>1</u> Answer: n!<sup>.</sup>

Solution: consider the sample space of all possible hat assignments. It has n! elements (n hat selections for the first person, after that n − 1 for the second, etc.), with every singleelement event equally likely (hence having probability 1/n!). The question is to calculate the probability of a single-element event, so the answer is 1/n!

- (b) the first m persons who picked hats get their own hats back?

<u>(n−m)!</u> Answer: . n!

Solution: consider the same sample space and probability as in the solution of (a). The probability of an event with (n − m)! elements (this is how many ways there are to disribute the remaining n − m hats after the first m are assigned to their owners) is (n − m)!/n!

(c) everyone among the first m persons to pick up the hats gets back a hat belonging to one of the last m persons to pick up the hats? Answer:<sup>m!(n</sup> n<sup>−</sup> !<sup>m)!</sup> = (mn<sup><u>1</u></sup> )<sup>=</sup> (n `−` <u>n</u><sup><u>1</u></sup> m) . .

Solution: there are m! ways to distribute m hats among the first m persons, and (n − m)! ways to distribute the remaining n − m hats. The probability of an event with m!(n − m)! elements is m!(n − m)!/n!.

Now assume, in addition, that every hat thrown into the box has probability p of getting dirty (independently of what happens to the other hats or who has dropped or picked it up). What is the probability that

- (d) the first m persons will pick up clean hats?

Answer: (1 − p)<sup>m</sup> . Solution: the probability of a given person picking up a clean hat is 1 − p. By the independence assumption, the probability of m selected persons picking up clean hats is (1 − p)<sup>m</sup> .

- (e) exactly m persons will pick up clean hats?

Answer: (1 − p)<sup>m</sup> p<sup>n−m�</sup> m<sup>n�</sup> .

m

Solution: every group G of m persons defines the event “everyone from G picks up a clean hat, everyone not from G picks up a dirty hat”. The events are disjoint. Each has probability (1 − p)<sup>m</sup> pn−m. Since there are � mn �<sup>such events, the answer follows.</sup>

2. Since 4 cards are fixed, Bob can only choose 4 more cards out of 48 remaining cards, so total number of hands Bob can have such that they include Alice’s cards is �44��484 �<sup>. The total number</sup> <u>4)(484 )</u>

of ways Bob can choose any 8 cards is �528 � . So the probability is <u>(</u><sup>4</sup> (528<sup>)</sup>

3. (a) The picture below illustrates the double sum needed to prove the statement of this problem:

Page 1 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


<!-- Start of picture text -->
infinity<br>i=k<br>i  i<br>k=1<br>i=k<br><!-- End of picture text -->


We first note that


and proceed as follows:


(b) We first compute

So


Therefore E[Y ] =<sup><u>b+</u></sup> 2a .


Page 2 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


We can also see that E[X] = 0 because the PMF is symmetric around 0. To find the variance of X, we first compute


and


- (b) Let Z = X<sup>2</sup> . By matching the possible values of X and their probabilities to the possible values of Z, we obtain


   5. Consider k out of n persons forming a club, with one being designated as the leader and another as the treasurer. We can first choose the leader (n choices), then the treasurer (n − 1 choices), and then a subset of the remaining n − 2 persons. Thus, there are n(n − 1)2<sup>n−2</sup> possible clubs. Alternatively, for any given k, there are � � nk choices for the members of the club. There are k(k − 1) choices for the leader and treasurer, so that there are k(k − 1) ��<sup>n</sup> k k-member clubs. Summing over all k, we see that there is a total of �nk=2<sup>k(k−1)</sup> � �<sup>n</sup> k<sup>possible clubs.</sup>

- G1<sup>†</sup> . A candy factory has an endless supply of red, orange, yellow, green, blue, black, white, and violet jelly beans. The factory packages the jelly beans into jars in such a way that each jar has 200 beans, equal number of red and orange beans, equal number of yellow and green beans, one more black bean than the number blue beans, and three more violet beans than the number of white

Page 3 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

beans. One possible color distribution, for example, is a jar of 50 yellow, 50 green, one black, 48 white, and 51 violet jelly beans. As a marketing gimmick, the factory guarantees that no two jars have the same color distribution. What is the maximum number of jars the factory can produce?

Answer: �1013 � = 166650.

Solution: Let N1, N2, N3, N4, N5, N6, N7, N8 denote, respectively, the numbers of red, orange, yellow, green, blue, black, white, and violet jelly beans in a jar. There is a one-to-one correspon­ dence


between the non-negative integer solutions x = (x1, x2, x3, x4) of the equation


and the sequences N = (N1, N2, N3, N4, N5, N6, N7, N8) of non-negative integers Ni satisfying the conditions


(i.e. possible color arrangements). The number of possible solutions x is �1013 � according to the solution of the more general problem given below:

Given a non-negative integer n and a positive integer k, consider the equation


to be solved with respect to non-negative integer variables x1, x2, . . . , xk. Find the total number of solutions (solutions x1 = 1, x2 = 0 and x1 = 0, x2 = 1 to the equation x1 + x2 = 1 are considered as different).


Solution: there is a one-to-one correspondence between non-negative integer solutions of equa­ tion x1 + . . . + xk = n and sequences of n + k − 1 symbols (n “o” and k − 1 “|”), where a solution x = (x1, . . . , xk) maps to the sequence in which the i-th “|” (where i ∈{1, 2, . . . , k − 1}) is in the x1 + . . . + xi + ith place: in this bijection, the numbers of “o” between the consecutive “|” correspond to the values of xi. Hence the total number of solutions equals the number of ways of selecting k − 1 places for the “|” symbols in a sequence of length n + k − 1.

†Required for 6.431; optional for 6.041

Page 4 of 4

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
