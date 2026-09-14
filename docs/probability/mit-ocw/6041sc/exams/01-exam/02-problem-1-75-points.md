---
title: 'Problem 1: (75 points)'
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/01-exam.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 1: (75 points)

**Source:** `exams/01-exam.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_Note:_ All parts can be done independently, with the exception of the last part. Just in case you made a mistake in the previous part, you can use a symbol for the expression you found there, and use that symbol in the formulas for the last part.

_Note:_ **Algebraic or numerical expressions do not need to be simplified in your answers.**

Jon and Stephen cannot help but think about their commutes using probabilistic modeling. Both of the them start promptly at 8am.

Stephen drives and thus is at the mercy of traffic lights. When all traffic lights on his route are green, the entire trip takes 18 minutes. Stephen’s route includes 5 traffic lights, each of which is red with probability 1 _/_ 3, independent of every other light. Each red traffic light that he encounters adds 1 minute to his commute (for slowing, stopping, and returning to speed).

1. **(10 points)** Find the PMF, expectation, and variance of the length (in minutes) of Stephen’s commute.

2. **(10 points)** Given that Stephen’s commute took him at most 19 minutes, what is the expected number of red lights that he encountered?

3. **(10 points)** Given that the last red light encountered by Stephen was the fourth light, what is the conditional variance of the total number of red lights he encountered?

4. **(10 points)** Given that Stephen encountered a total of three red lights, what is the probability that exactly two out of the first three lights were red?

Jon’s commuting behavior is rather simple to model. Jon walks a total of 20 minutes from his home to a station and from a station to his office. He also waits for _X_ minutes for a subway train, where _X_ has the discrete uniform distribution on _{_ 0 _,_ 1 _,_ 2 _,_ 3 _}_ . (All four values are equally likely, and independent of the traffic lights encountered by Stephen.)

5. **(5 points)** What is the PMF of the length of Jon’s commute in minutes?

6. **(10 points)** Given that there was exactly one person arriving at **exactly** 8:20am, what is the probability that this person was Jon?

7. **(10 points)** What is the probability that Stephen’s commute takes at most as long as Jon’s commute?

8. **(10 points)** Given that Stephen’s commute took at most as long as Jon’s, what is the conditional probability that Jon waited 3 minutes for his train?

**Problem 2. (30 points)** For each one of the statements below, give either a proof or a counterexample showing that the statement is not always true.

1. **(10 points)** If events _A_ and _B_ are independent, then the events _A_ and _B_<sup>_c_</sup> are also independent.

2. **(10 points)** Let _A_ , _B_ , and _C_ be events associated with a common probabilistic model, and assume that 0 _<_ **P** ( _C_ ) _<_ 1. Suppose that _A_ and _B_ are conditionally independent given _C_ . Then, _A_ and _B_ are conditionally independent given _C_<sup>_c_</sup> .

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2010)

3. **(10 points)** Let _X_ and _Y_ be independent random variables. Then, var( _X_ + _Y_ ) _≥_ var( _X_ ).

Each question is repeated in the following pages. Please write your answer on the appropriate page.

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2010)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Problem 1: (75 points) →](03-problem-1-75-points.md)
