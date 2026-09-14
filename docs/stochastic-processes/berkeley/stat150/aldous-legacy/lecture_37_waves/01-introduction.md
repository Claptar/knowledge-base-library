---
title: Introduction
source: https://www.stat.berkeley.edu/~aldous/150/lecture_37_waves.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_37_waves.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`lecture_37_waves.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_37_waves.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Waves in a Spatial Queue: Stop-and-Go at Airport Security


David Aldous

Hajekfest 3 October 2015

Waves in a Spatial Queue: Stop-and-Go at Airport Security

David Aldous


<!-- Start of picture text -->
17 minutes in line at security at Oakland airport<br>16<br>14<br>12<br>10<br>time<br>(min.) 8<br>6<br>4<br>2<br>20 40 60 80 100 120 140 160<br>rank in line<br><!-- End of picture text -->

David Aldous Waves in a Spatial Queue: Stop-and-Go at Airport Security


This phenomenon is easy to understand qualitatively. When a person leaves the checkpoint, the next person moves up to the checkpoint, the next person moves up and stops behind the now-first person, and so on, but this “wave” of motion often does not extend through the entire long line; instead, some person will move only a short distance, and the person behind will decide not to move at all.

Intuitively, when you are around the _k_ ’th position in line, there must be some number _a_ ( _k_ )


- _a_ ( _k_ ) = average time between your moves


_a_ ( _k_ ) = average distance you move when you do move


- P( _W > k_ ) = 1 _/a_ ( _k_ ) for length of typical wave.

You are moving forwards at average speed 1 [unit time = service time, unit distance = average distance between people in queue]. This immediately suggests the question of how fast _a_ ( _k_ ) grows with _k_ .

- I will present a stochastic model in which _a_ ( _k_ ) grows as order _k_<sup>1</sup><sup>_/_2</sup> .

Waves in a Spatial Queue: Stop-and-Go at Airport Security

David Aldous


<!-- Start of picture text -->
11<br>10<br>9<br>8<br>7<br>6<br>5<br>time t<br>4<br>3<br>2<br>1<br>0<br>0 2 4 6 8 10<br>position x<br>Space-time trajectories of alternate customers near the head of the queue.<br><!-- End of picture text -->

Waves in a Spatial Queue: Stop-and-Go at Airport Security

David Aldous


In classical _queueing theory_ randomness enters via assumed randomness of arrival and service times. In contrast, even though we are modeling a literal queue, randomness in our model arises in a quite different way, via each customer’s choice of exactly how far behind the preceding customer they choose to stand, after each move. That is, we assume that “how far behind” is chosen (independently for each person and time) from a given probability density function _µ_ on an interval [ _c−, c_<sup>+</sup> ] where _c− >_ 0. We interpret this interval as a “comfort zone” for proximity to other people. By scaling we may assume _µ_ has mean 1, and then (excluding the deterministic case) _µ_ has some variance 0 _< σ_<sup>2</sup> _< ∞_ . In words, the model is

_when the person in front of you moves forward to a new position, then you move to a new position at a random distance (chosen from distribution µ) behind them, unless their new position is less than distance c_<sup>+</sup> _in front of your existing position, in which case you don’t move, and therefore nobody behind you moves._

Waves in a Spatial Queue: Stop-and-Go at Airport Security

David Aldous


Model **could** have been studied 60 years ago – but I can’t find any closely related literature. Some traffic models loosely similar; also TASEP.


Model as infinite queue.


- You might guess process has stationary distribution with inter-customer distances IID _µ_ – **no** .


Not obvious how to start analysis.


Seem obvious that process time-converges to some unique stationary distribution – **cannot prove** .

It turns out there is a non-obvious picture which explains everything (intuitively).

Waves in a Spatial Queue: Stop-and-Go at Airport Security

David Aldous


A configuration **x** = (0 = _x_ 0 _< x_ 1 _< x_ 2 _< x_ 3 _. . ._ ) of customer positions can be represented by its centered counting function


<!-- Start of picture text -->
1<br>0<br>-1<br>2 4 6 8 10<br>position x<br><!-- End of picture text -->

At each time _t_ , let us consider the centered counting function _Ft_ ( _x_ ) and plot the graph of the upward-translated function


In other words, we draw the function starting at the point (0 _, t_ ) instead of the origin. Taking the same process realization as in the first Figure 1, superimposing all these graphs, gives the next Figure.

David Aldous Waves in a Spatial Queue: Stop-and-Go at Airport Security


<!-- Start of picture text -->
11<br>10<br>9<br>8<br>7<br>6<br>5<br>time t<br>4<br>3<br>2<br>1<br>0<br>0 2 4 6 8 10<br>position x<br><!-- End of picture text -->

David Aldous Waves in a Spatial Queue: Stop-and-Go at Airport Security


Picture shows **coalescing Brownian motion** (CBM). Note trick: **we switched space** _↔_ **time** .

Assuming convergence of “coded” process to CBM, how do we decode?

David Aldous Waves in a Spatial Queue: Stop-and-Go at Airport Security


Rank and position same to first order – we are studying a second-order behavior.


Space-time trajectories become vertical in the scaling limit. To study trajectory of individual at rank/position _≈ k_ there is a _k_<sup>1</sup><sup>_/_2</sup> scaling in the vertical direction.

Waves in a Spatial Queue: Stop-and-Go at Airport Security

David Aldous


Trajectory of individual at rank/position _≈ k_ is Times between moves are _k_<sup>1</sup><sup>_/_2</sup> _×_ intervals _ti_ +1 _− ti_ on left. Distances of moves are _k_<sup>1</sup><sup>_/_2</sup> _×_ intervals _wi_ +1 _− wi_ on right.

David Aldous Waves in a Spatial Queue: Stop-and-Go at Airport Security


How to actually prove the CBM limit?

# AAAARGH !

30 pages with some details missing. Markov intuition fallible because of space _↔_ time switch. Must be some simpler proof ideas . . . . . .

---

[Up: contents](index.md) · [Step -1. →](02-step--1.md)
