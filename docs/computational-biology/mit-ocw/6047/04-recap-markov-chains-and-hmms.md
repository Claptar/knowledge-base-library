---
title: "4. Recap: Markov Chains and HMMs"
course: "MIT 6047"
chapter: 4
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Recap: Markov Chains and HMMs

## What this covers

This "chapter" is a recap slide, not a lecture: MIT 6.047's lecture 4 opens by listing, in four
bullet groups, what the course had established by the end of the sequential-data / hidden Markov
model unit that preceded it. It assumes the reader has already met Markov chains, hidden Markov
models (HMMs), and the Viterbi algorithm elsewhere in the course — none of them is defined or
re-derived here, only named. Nothing beyond this outline was supplied for this lecture: no
transcript, no notes, no exercises, and the slide deck itself is a single recap slide plus one
uncaptioned figure.

## The recap, as given

The slide groups what had been covered into four points.

**Modeling sequential data.** The first task was recognizing that data comes as a *sequence*, and
that sequences come in different **types** — the slide lists genomic, oral, verbal, and visual as
examples of the kinds of sequence a model might need to distinguish.

**Definitions.** Two formal objects had been introduced: **Markov chains** and **hidden Markov
models (HMMs)**. The slide does not restate either definition here — they belong to the lecture(s)
this one is recapping.

**Examples of HMMs.** The class of problems HMMs had been applied to, per the slide: recognizing
GC-rich regions, preferentially-conserved elements, coding exons, protein-coding gene structures,
and chromatin states. No detail on any one of these examples is given on this slide.

**Our first computations.** Three questions about an HMM had been posed, each stated as an
input-to-output relation:

- *Running the model*: given the model, generate a sequence of a given type.
- *Evaluation*: given the model, its emissions, and its states, compute a probability.
- *Viterbi*: named only — the slide does not say here what it computes or how.

## Sources

- Slide: `computational-biology/mit-ocw/6047/lectures/04-slides.md` ("What have we learned?"),
  the single content slide of lecture 4 (page 1 of the deck; the four bullet groups reproduced
  above are the entire text of the slide).
- The deck also contains one figure, an uncaptioned portrait photograph extracted from page 8 of
  the source PDF, listed in the converted markdown without a caption or surrounding text tying it
  to a specific claim; it is not used above because nothing in the supplied material says what it
  illustrates.
- No transcript, written notes, or exercises were supplied for this lecture.
- The Markov chain and HMM definitions, and the HMM examples and computations this slide is
  recapping, were covered in an earlier lecture of this course that was not among the inputs to
  this chapter — this chapter does not reconstruct them, since they are not in the material given.

---

[← 3. Alignment Recap and BLAST Seeding](03-alignment-recap-and-blast-seeding.md) · [Contents](index.md) · [5. Training Hidden Markov Models →](05-training-hidden-markov-models.md)
