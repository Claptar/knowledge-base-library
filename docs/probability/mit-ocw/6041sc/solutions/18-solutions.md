---
title: 18 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/18-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 18 solutions

**Source:** `solutions/18-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

## Recitation 18: Solutions November 9, 2010

1. a) The number of remaining green fish at time n completely determines all the relevant infor­ mation of the system’s entire history (relevant to predicting the future state.) Therefore it is immediate that the number of green fish is the state of the system and the process has the Markov property:

P(Xm+1 = j|Xm = i, Xm−1 = im−1, . . . , X1 = i1) = P(Xm+1 = j|Xm = i).

b) For j > i clearly pij = 0, since a blue fish will never be painted green. For 0≤i, j≤k, we have the following:


c) The state 0 is an absorbing state since there is a positive probability that the system will enter it, and once it does, it will remain there forever. Therefore the state with 0 green fish is the only recurrent state, and all other states are then transient.

Textbook problem removed due to copyright restrictions. Drake, Fundamentals of Applied Probability Theory, Problem 5.02.

Page 1 of 3

# Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

3. (a) Let Ak be the event that the process enters s2 for first time on trial k. The only way to enter state s2 for the first time on the kth trial is to enter state s3 on the first trial, remain in s3 for the next k − 2 trials, and finally enter s2 on the last trial. Thus,


- (b) Let A be the event that the process never enters s4.

There are three possible ways for A to occur. The first two are if the first transition is either from s0 to s1 or s0 to s5. This occurs with probability<sup><u>2</u></sup> 3<sup>. The other is if The first</sup> transition is from s0 to s3, and that the next change of state after that is to the state s2. We know that the probability of going from s0 to s3 is<sup><u>1</u></sup> 3<sup>. Given this has occurred, and</sup> given a change of state occurs from state s3, we know that the probability that the state <u>1 4 1</u> transitioned to is the state s2 is simply <u>14</u> + 2<sup><u>1</u></sup> = 3 . Thus, the probability of transitioning from s0 to s3 and then eventually transitioning to s2 is<sup><u>1</u></sup> 9<sup>. Thus, the probability of never</sup> <u>1 7</u> entering s4 is<sup><u>2</u></sup> 3<sup>+</sup> 9 = 9 .

Page 2 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

(c) P({process enters s2 and then leaves s2 on next trial})


(d) This event can only happen if the sequence of state transitions is as follows:


<u>1 1 1</u> Thus, P({process enters s1 for first time on third trial}) = p03 · p32 · p21 =<sup><u>1</u></sup> 3 · 4 · 2 = 24 .

(e) P({process in s3 immediately after the N th trial})


†Required for 6.431; optional for 6.041

Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
