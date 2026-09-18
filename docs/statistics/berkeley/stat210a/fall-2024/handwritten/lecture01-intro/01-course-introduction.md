---
title: Course introduction
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture01-intro.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture01-intro.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture01-intro.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture01-intro.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Course introduction

### Outline:

1) Syllabus
2) Deductive vs inductive reasoning
3) The problem of induction
4) Coin flipping

---

## Deductive vs inductive reasoning

### Deduction:

Drawing inferences that follow logically from premises

**Ex:**
(1) All real, symmetric matrices have real eigenvalues
(2) $A$ is a symmetric matrix
Therefore, $A$ has real eigenvalues

**Ex:**
(1) No one in my daughter's preschool class has a peanut allergy
(2) Zoe is in my daughter's preschool class
Therefore, Zoe is not allergic to peanuts

### Risk-free:

Valid arguments + true premises $\rightarrow$ true conclusions
(Conclusion could be wrong if a premise is wrong)

Deductive reasoning can involve probability:

(1) This die has six faces: $1, 2, \dots, 6$
(2) Each side is equally likely
Therefore, the chance of rolling $4$ is $1/6$

---

## **Induction:** Observations $\rightarrow$ general claims

### **Risky!** We can (and will sometimes) be wrong

**Ex.**
(1) I ate a free sample strawberry at the supermarket
(2) It was ripe and delicious.
Therefore, I should (probably) buy a whole carton.
(Would be more convincing with a random sample)

**Ex:**
(1) Water at $1\text{ atm}$ pressure has always been observed to boil at $100^\circ\text{C}$
Therefore, all water at $1\text{ atm}$ (probably) boils at $100^\circ\text{C}$

**Ex:**
(1) I flipped this coin $1000$ times and got $502$ heads
Therefore, it (probably) has about a $50\%$ chance of landing heads

**Statistics:** mathematical science of inductive reasoning

---

## The Problem of Induction

Inductive reasoning is not logically valid

**Hume:** All inductive reasoning requires a presumption that unobserved cases will be like observed cases

How can we justify this?

Logical proof? There is none!\*
Past observation? Circular!

Hume admitted we must reason inductively all the time
Called it "custom" or "habit"

Statistics evades this problem in one of two ways

### Idea 1: Bayesian reasoning

Whatever our prior beliefs, we know how to update them in light of experience.

### Idea 2: "Inductive behavior" (frequentist statistics)

If observations are from a reasonable experiment, we can design methods that give correct conclusions with high probability (provably!)

---

---

[Up: contents](index.md) · [Coin Flipping →](02-coin-flipping.md)
