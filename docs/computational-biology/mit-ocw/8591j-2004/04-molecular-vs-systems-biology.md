---
title: "4. Molecular vs Systems Biology"
course: "MIT 8.591J 2004"
chapter: 4
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Molecular vs Systems Biology

## What this covers

What does it mean to study a biological *system*, rather than a biological molecule? This is an
orientation lecture, not a technical one: it assumes only ordinary molecular biology — genes,
proteins, the idea that a protein has a function — and sets up the questions the rest of the
course exists to answer.

## Systems biology as network biology

The working definition: systems biology is, to a first approximation, network biology. The goal is
a quantitative understanding of the biological function of genetic and biochemical networks, not
of their individual parts.

Take a network of input genes — the lecture's example has six, A through F — feeding into some
output. Knowing the molecular function of each gene product in detail does not reveal what the
whole network's input-output relation does. That needs a systems approach: looking past any one
gene or protein to ask what the interactions between them — feedbacks, feedforwards — are *for*,
in the context of the entire network.

Equivalently: systems biology is systems engineering combined with molecular biology, each
contributing its own concepts rather than one absorbing the other — the application of
systems-engineering ideas to biological systems.

## Two questions about the same system

The contrast is drawn through one running example, a repressor protein cI. A molecular biologist
asks about the molecule: the structure of the cI dimer, the DNA sequence it recognizes, the
residues responsible for dimerization, its binding constants, whether the sequence is conserved
across evolution.

A systems biologist asks about the same protein differently: what is the functional role of the
feedback loop cI sits in, how does that feedback produce a hysteretic switch, what role does noise
play in the switch's stability, is the switch's performance robust to small parameter changes or
finely tuned, and how do those parameters shift when the module cross-talks with others? These
are questions about network architecture, not about the molecule.

## Where the course is headed

Two stated goals: build the mathematical tools to model network modules — switches, oscillators,
filters, amplifiers — and work through recent papers' biological problems that a systems approach
can solve, starting with well-stirred systems and moving to diffusion-dominated ones.

## Sources

- Slides only: `lectures/06-notes.md` (MIT OCW 8.591J, Fall 2004, lecture 6) — the network-biology
  framing, the molecular- vs systems-biology question lists (cI example), and the course goals.
- No transcript, written notes, or exercises were supplied for this lecture; nothing beyond the
  slide content above is recorded. The slide file itself is a model's reconstruction of a PDF with
  no text layer, so treat exact wording as approximate.

---

[← 3. The Lambda Phage Bistable Switch](03-the-lambda-phage-bistable-switch.md) · [Contents](index.md) · [5. Mathematical basis of stability analysis →](05-mathematical-basis-of-stability-analysis.md)
