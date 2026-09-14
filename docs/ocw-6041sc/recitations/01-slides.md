---
title: 01 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/01-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 01 slides

**Source:** `recitations/01-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Fall</u> 2010)

# **Recitation 1**

**September 9, 2010**

1. Give a mathematical derivation of the formula

**P** (( _A ∩ B_<sup>_c_</sup> ) _∪_ ( _A_<sup>_c_</sup> _∩ B_ )) = **P** ( _A_ ) + **P** ( _B_ ) _−_ 2 **P** ( _A ∩ B_ ) _._

Your derivation should be a sequence of steps, with each step justified by appealing to one of the probability axioms.

2. Problem 1.5, page 54 in the text.

Out of the students in a class, 60% are geniuses, 70% love chocolate, and 40% fall into both categories. Determine the probability that a randomly selected student is neither a genius nor a chocolate lover.

3. A six-sided die is loaded in a way that each even face is twice as likely as each odd face. Construct a probabilistic model for a single roll of this die, and find the probability that a 1, 2, or 3 will come up.

4. Example 1.5, page 13 in the text.

Romeo and Juliet have a date at a given time, and each will arrive at the meeting place with a delay between 0 and 1 hour, with all pairs of delays being equally likely. The first to arrive will wait for 15 minutes and will leave if the other has not yet arrived. What is the probability that they will meet?

- G1<sup>_†_</sup> . Problem 1.13, page 56 in the text. **Continuity property of probabilities.**

   - (a) Let _A_ 1 _, A_ 2 _, . . ._ be an infinite sequence of events that is “monotonically increasing,” mean­ ing that _An ⊂ An_ +1 for every _n_ . Let _A_ = _∪_<sup>_∞_</sup> _n_ =1<sup>_An_.Showthat</sup><sup>**P**(</sup><sup>_A_)=lim</sup><sup>_n→∞_</sup><sup>**P**(</sup><sup>_An_).</sup> _Hint:_ Express the event _A_ as a union of countably many disjoint sets.

   - (b) Suppose now that the events are “monotonically decreasing,” i.e., _An_ +1 _⊂ An_ for every _n_ . Let _A_ = _∩_<sup>_∞_</sup> _n_ =1<sup>_An_.Showthat</sup><sup>**P**(</sup><sup>_A_)=lim</sup><sup>_n→∞_</sup><sup>**P**(</sup><sup>_An_).</sup><sup>_Hint:_Applytheresultofthe</sup> previous part to the complements of the events.

   - (c) Consider a probabilistic model whose sample space is the real line. Show that


Textbook problems are courtesy of Athena Scientific, and are used with permission.

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
