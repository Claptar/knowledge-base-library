---
title: 01 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/01-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 01 slides

**Source:** `lectures/01-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **LECTURE 1**

- **Readings:** Sections 1.1, 1.2

**Sample space** Ω

- “List” (set) of possible outcomes

- List must be:

# **Lecture outline**

- Probability as a mathematical framework for:

- reasoning about uncertainty

   - Mutually exclusive

   - Collectively exhaustive

   - Art: to be at the “right” granularity

- developing approaches to inference problems

- Probabilistic models

- sample space

- probability law

- Axioms of probability

- Simple examples

# **Sample space: Discrete example**

- Two rolls of a tetrahedral die

# **Sample space: Continuous example**


<!-- Start of picture text -->
Ω = { ( x, y ) | 0 ≤ x, y ≤ 1 }<br><!-- End of picture text -->

- Sample space vs. sequential description


<!-- Start of picture text -->
1,1<br>1  1,2<br>1,3<br>1,4<br>4  2<br>Y = Second  3<br>roll<br>3<br>2<br>1<br>1  2  3  4  4<br>X = First roll  4,4<br><!-- End of picture text -->


<!-- Start of picture text -->
y<br>1<br>1  x<br><!-- End of picture text -->

1

# **Probability axioms**

- **Event:** a subset of the sample space

- Probability is assigned to events

# **Axioms:**

1. **Nonnegativity: P** ( _A_ ) _≥_ 0

2. **Normalization: P** (Ω) = 1

3. **Additivity:** If _A ∩ B_ = Ø, then **P** ( _A ∪ B_ ) = **P** ( _A_ )+ **P** ( _B_ )

# **Probability law: Example with finite sample space**


<!-- Start of picture text -->
4<br>Y = Second  3<br>roll<br>2<br>1<br>1  2  3  4<br>X = First roll<br><!-- End of picture text -->

   - Let every possible outcome have probability 1 _/_ 16

   - **P** (( _X, Y_ ) is (1,1) or (1,2)) =

- **P** ( _{s_ 1 _, s_ 2 _, . . . , sk}_ ) = **P** ( _{s_ 1 _}_ ) + _· · ·_ + **P** ( _{sk}_ ) = **P** ( _s_ 1) + _· · ·_ + **P** ( _sk_ )

   - **P** ( _{X_ = 1 _}_ ) =

   - **P** ( _X_ + _Y_ is odd) =

- Axiom 3 needs strengthening

   - **P** (min( _X, Y_ ) = 2) =

- Do weird sets have probabilities?

# **Discrete uniform law**

- Let all outcomes be equally likely

# **Continuous uniform law**

- Two “random” numbers in [0 _,_ 1].


<!-- Start of picture text -->
y<br><!-- End of picture text -->

- Then,

      - number of elements of _A_

   - **P** ( _A_ ) = total number of sample points

- Computing probabilities _≡_ counting

- Defines fair coins, fair dice, well-shuffled card decks


<!-- Start of picture text -->
1<br>1  x<br><!-- End of picture text -->

- **Uniform** law: Probability = Area

- **P** ( _X_ + _Y ≤_ 1 _/_ 2) = ?

- **P** ( ( _X, Y_ ) = (0 _._ 5 _,_ 0 _._ 3) )

2

**Probability law: Ex. w/countably infinite sample space**

- Sample space: _{_ 1 _,_ 2 _, . . .}_

- We are given **P** ( _n_ ) = 2<sup>_−n_</sup> , _n_ = 1 _,_ 2 _, . . ._

- Find **P** (outcome is even)

p 1/2 1/4 1/8 1/16 ….. 1 2 3 4 1 1 1 **P** ( _{_ 2 _,_ 4 _,_ 6 _, . . .}_ ) = **P** (2) + **P** (4) + _· · ·_ = + + + _·_ 2<sup>2</sup> 2<sup>4</sup> 2<sup>6</sup>

- Countable additivity axiom (needed for this calcu­ lation): If _A_ 1 _, A_ 2 _, . . ._ are disjoint events, then: **P** ( _A_ 1 _∪ A_ 2 _∪ · · ·_ ) = **P** ( _A_ 1) + **P** ( _A_ 2) + _· · ·_

3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
