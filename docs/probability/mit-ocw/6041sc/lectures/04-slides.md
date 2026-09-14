---
title: 04 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/04-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 04 slides

**Source:** `lectures/04-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **LECTURE 4**

- **Readings:** Section 1.6

# **Lecture outline**

- Principles of counting

- Many examples

# **Discrete uniform law**

   - Let all sample points be equally likely

   - Then, **P** ( _A_ ) = number of elements of _A_ =<sup>_<u>|</u>_</sup> _A_<sup>_<u>|</u>_</sup> total number of sample points _|_ Ω _|_

   - Just count _. . ._

- permutations

- _k_ -permutations

- combinations

- partitions

- Binomial probabilities

**Basic counting principle**

- _r_ stages

- _ni_ choices at stage _i_


# **Example**

   - Probability that six rolls of a six-sided die all give different numbers?

   - Number of outcomes that make the event happen:

   - Number of elements in the sample space:

- Number of choices is: _n_ 1 _n_ 2 _· · · nr_

   - Answer:

- Number of license plates with 3 letters and 4 digits =

- _. . ._ if repetition is prohibited =

- **Permutations:** Number of ways of ordering _n_ elements is:

- Number of subsets of _{_ 1 _, . . . , n}_ =

1

# **Combinations**

- : number of _k_ -element subsets

- ￿ _nk_ ￿

   - of a given _n_ -element set

# **Binomial probabilities**

   - _n_ independent coin tosses

   - **P** ( _H_ ) = _p_

- Two ways of constructing an ordered sequence of _k_ **distinct** items:

- Choose the _k_ items one at a time: _n_ !

- _n_ ( _n−_ 1) _· · ·_ ( _n−k_ +1) = ( _n − k_ )! choices

      - **P** ( _HTTHHH_ ) =

   -

   - **P** (sequence) = _p_ # heads(1 _− p_ )# tails

- Choose _k_ items, then order them ( _k_ ! possible orders)


<!-- Start of picture text -->
• Hence:<br>n !<br>· k ! =<br>￿ nk ￿ ( n − k )!<br>n !<br>=<br>￿ nk ￿ k !( n − k )!<br>n<br>=<br>￿ ￿ nk ￿<br>k =0<br><!-- End of picture text -->

# **Coin tossing problem**

- event _B_ : 3 out of 10 tosses were “heads”.

- Given that _B_ occurred, what is the (conditional) probability that the first 2 tosses were heads?


# **Partitions**

   - 52-card deck, dealt to 4 players

   - Find **P** (each gets an ace)

   - Outcome: a partition of the 52 cards

   - number of outcomes:

- All outcomes in set _B_ are equally likely: probability _p_ 3(1 _− p_ )<sup>7</sup>

- Conditional probability law is uniform

52!

13! 13! 13! 13!

   - Count number of ways of distributing the four aces: 4 _·_ 3 _·_ 2

- Number of outcomes in _B_ :

- Out of the outcomes in _B_ , how many start with HH?

- Count number of ways of dealing the remaining 48 cards

48! 12! 12! 12! 12!

- Answer:

48! 4 _·_ 3 _·_ 212! 12! 12! 12! 52! 13! 13! 13! 13!

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
