---
title: '1. Site evolution over single branch Remember: Jukes-Cantor (JC)'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/18-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Site evolution over single branch Remember: Jukes-Cantor (JC)

**Source:** `lectures/18-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- **JC is a Continuous-Time Markov Chain (CTMC)**

- Defines instantaneous rates of transition between states (bases)


<!-- Start of picture text -->
<br>A  G<br><br><br><br><br>C  T<br><br><!-- End of picture text -->

**Discrete MC version**

- Given time t, we define a discrete MC with transition matrix is S(t), also called a _substitution probability matrix._

- • Gives the probability of seeing base _a_ given initial base _b_ after duration time _t_ .


Use JC to define **single site evolution:**

“A”

t P(a=“C”|b=“A”, t) = S(t)ba

“C”

61

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Sequence evolution over single branch →](03-2-sequence-evolution-over-single-branch.md)
