---
title: Question 2
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/01-solutions-qu01-s09-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 2

**Source:** `solutions/01-solutions-qu01-s09-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Alice and Bob both need to buy a bicycle. The bike store has a stock of four green, three yellow, and two red bikes. Alice randomly picks one of the bikes and buys it. Immediately after, Bob does the same. The sale price of the green, yellow, and red bikes are $300, $200 and $100, respectively.

Let _A_ be the event that Alice bought a green bike, and _B_ be the event that Bob bought a green bike.

a. (5 points) What is **P** ( _A_ )? What is **P** ( _A|B_ )?

**Solution:** We have **P** ( _A_ ) = 4 _/_ 9 (4 green bikes out of 9), and **P** ( _A|B_ ) = 3 _/_ 8 (since we know that Bob has a green bike, Alice can have one of 3 green bikes out of the remaining 8).

b. (2 points) Are _A_ and _B_ independent events? Justify your answer.

**Solution:** Since **P** ( _A_ ) = **P** ( _A|B_ ), the events are _not_ independent. Informally, since there is a fixed quantity of green bikes, if Alice buys one, then the chances that Bob buys one too are slightly decreased.

c. (5 points) What is the probability that at least one of them bought a green bike?

**Solution:** The requested probability is **P** ( _A ∪ B_ ). We have


5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

d. (5 points) What is the probability that Alice and Bob bought bicycles of different colors?

**Solution:** Let’s compute first the probability that Alice and Bob bought bikes of the same color. We have


Therefore, the probability of buying bikes of different color is

- e. (5 points) Given that Bob bought a green bike, what is the expected value of the amount of money spent by Alice?

**Solution:** If Bob bought a green bike, then the conditional probabilities of Alice buying a green, yellow, or red bike are 83 , 83 and<sup><u>2</u></sup> 8<sup>,respectively.TheexpectedamountofmoneyspentbyAlice</sup> is therefore


- f. (5 points) Let _G_ be the number of green bikes that remain in the store after Alice and Bob’s visit. Compute **P** ( _B|G_ = 3).

**Solution:** If _G_ = 3, then exactly one green bike was bought. By symmetry, there is equal chance that Alice or Bob bought it, thus **P** ( _B|G_ = 3) = <u>12</u><sup>.Alternatively,define</sup><sup>_A\B_astheelements</sup> of _A_ that are not in _B_ . We have:


6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 1 Solutions| Spring 2009)</u>

---

[← Question 1](01-question-1.md) · [Up: contents](index.md) · [Question 3 →](03-question-3.md)
