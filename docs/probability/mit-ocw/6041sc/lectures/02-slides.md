---
title: LECTURE 2
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# LECTURE 2

**Source:** `lectures/02-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Readings: Sections 1.3-1.4

# Lecture outline

# Review of probability models

   - Sample space Ω

   - Mutually exclusive Collectively exhaustive

   - Right granularity

- Review

   - Event: Subset of the sample space

- Conditional probability

- Three important tools:

- Multiplication rule

- Total probability theorem

- Bayes’ rule

- Allocation of probabilities to events

- 1. P( _A_ ) _≥_ 0

2. P(Ω) = 1

3. If _A ∩ B_ = Ø, then P( _A ∪ B_ ) = P( _A_ ) + P( _B_ )

- 3’. If _A_ 1 _, A_ 2 _, . . ._ are disjoint events, then: P( _A_ 1 _∪ A_ 2 _∪· · ·_ ) = P( _A_ 1) + P( _A_ 2) + _· · ·_

- Problem solving:

- Specify sample space

- Define probability law

- Identify event of interest

- Calculate...

# Conditional probability


<!-- Start of picture text -->
A<br>B<br><!-- End of picture text -->

- P( _A | B_ ) = probability of _A_ , given that _B_ occurred

- _B_ is our new universe

- Definition: Assuming P( _B_ ) = 0,

   - P( _A ∩ B_ <u>)</u>

   - P( _A | B_ ) = P( _B_ )

   - P( _A | B_ ) undefined if P( _B_ ) = 0

# Die roll example


<!-- Start of picture text -->
4<br>3<br>Y = Second<br>        roll<br>2<br>1<br>1 2 3 4<br>X = First roll<br><!-- End of picture text -->

- Let _B_ be the event: min( _X, Y_ ) = 2

- Let _M_ = max( _X, Y_ )

- P( _M_ = 1 _| B_ ) =

- P( _M_ = 2 _| B_ ) =

1

# Models based on conditional probabilities

- Event _A_ : Airplane is flying above Event _B_ : Something registers on radar screen


<!-- Start of picture text -->
P(B | A)=0.99<br>P(B | A)=0.01c<br>P(A)=0.05<br>P(Ac)=0.95<br>P(B | Ac)=0.10<br>P(B | Ac c)=0.90<br><!-- End of picture text -->

P( _A ∩ B_ ) =

# Multiplication rule

P( _A ∩ B ∩ C_ ) = P( _A_ ) _·_ P( _B | A_ ) _·_ P( _C | A ∩ B_ )


<!-- Start of picture text -->
A B P(C | A   B)<br>A B C<br>P(B | A)<br>A<br>P(B | A)c<br>P(A) A Bc C<br>A Bc<br>A Bc Cc<br>P(Ac)<br>Ac<br>U U<br>U U<br>U U<br>U<br>U U<br><!-- End of picture text -->

P( _B_ ) =

P( _A | B_ ) =

# Total probability theorem

- Divide and conquer

# Bayes’ rule

   - “Prior” probabilities P( _Ai_ )

   - – initial “beliefs”

- Partition of sample space into _A_ 1 _, A_ 2 _, A_ 3

- Have P( _B | Ai_ ), for every _i_


<!-- Start of picture text -->
A<br>1<br>B<br>A2 A3<br><!-- End of picture text -->

- One way of computing P( _B_ ):

   - P( _B_ ) = P( _A_ 1)P( _B | A_ 1) + P( _A_ 2)P( _B | A_ 2) + P( _A_ 3)P( _B | A_ 3)

- We know P( _B | Ai_ ) for each _i_

- Wish to compute P( _Ai | B_ )

- revise “beliefs”, given that _B_ occurred


<!-- Start of picture text -->
A1<br>B<br>A2 A3<br><!-- End of picture text -->


- = P( _Ai_ <u>)P(</u> _B_ _<u>| Ai</u>_ <u>)</u> P( _B_ )

- = P( _Ai_ <u>)P(</u> _B_ _<u>|</u> Ai_ <u>)</u> ~~�~~ _j_<sup>P(</sup><sup>_A_</sup> _j_<sup>)P(</sup><sup>_B| A_</sup> _j_<sup>)</sup>

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
