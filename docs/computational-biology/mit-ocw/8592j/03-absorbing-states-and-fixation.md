---
title: "3. Absorbing States and Fixation"
course: "MIT 8.592J"
chapter: 3
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. Absorbing States and Fixation

## What this covers

This is a short fragment — a single paragraph — that picks up the Wright–Fisher diffusion for a
two-allele locus (alleles $A_1$, $A_2$, frequency $x$) under mutation and genetic drift exactly
where the steady-state frequency distribution derived earlier in the course (referred to here as
Eq. 1.63) stops making sense. It assumes the reader already has that steady-state distribution,
built from mutation rates $\mu_1$ (the $A_2 \to A_1$ rate) and $\mu_2$ (the $A_1 \to A_2$ rate)
together with drift, and asks what goes wrong as mutation is turned off. The source material runs
out before reaching the backward Kolmogorov equation that the slide's title promises; this chapter
covers only the motivating breakdown, not the equation itself.

## Why the steady-state formula cannot survive $\mu \to 0$

When mutation is weak relative to drift, the steady-state distribution over $x$ is peaked at the
two ends of the interval, $x=0$ and $x=1$: most of the time the population sits close to fixation
for one allele or the other. Push this further and switch mutation off entirely in one direction —
say $\mu_1 \to 0$ (the argument is symmetric for $\mu_2 \to 0$) — and the formula no longer
describes a probability distribution at all: it diverges like $1/x$ near $x=0$ (or $1/(1-x)$ near
$x=1$), and a distribution that blows up like that cannot be normalized to integrate to one. The
divergence is not a defect to patch — it is the mathematics telling you that the steady-state
expression was only ever valid away from this limit.

## Absorbing states

The reason the formula fails is a real feature of the dynamics, not an artifact of the
approximation. With no mutation at all, a population that has already fixed — every individual
$A_1$, or every individual $A_2$ — has no mechanism left to reintroduce the missing allele: random
mating within a homogeneous population cannot change it. So once the population reaches $x=0$ or
$x=1$ it stays there. In the language of stochastic dynamics, $x=0$ and $x=1$ are **absorbing
states**: transitions into an absorbing state are possible, but there are none out of it. A process
with absorbing boundaries has no genuine stationary distribution in the interior — probability mass
only ever drains toward the boundary and piles up there — which is exactly the divergence that
Eq. (1.63) develops as $\mu \to 0$.

## Sources

- All of the exposition above comes from the one paragraph of body text in
  `lectures/05-slides.md` (course `computational-biology/mit-ocw/8592j`, lecture 5, slide section
  "1.4 Backward Kolmogorov equation" — MIT OCW 8.592J, *Statistical Physics in Biology*, Spring
  2011, CC BY-NC-SA 4.0). That file is itself a model's reconstruction of a slide PDF with no text
  layer, and its own banner marks the prose as paraphrase and every equation as unverified; Eq.
  (1.63) is referred to but not restated here, since it was not supplied.
- The extracted text stops mid-sentence ("In the ...") after introducing absorbing states — the
  source material for this chapter is genuinely only about a thousand characters, and this chapter
  does not extend past what those characters say. Whatever the slide argued next (presumably the
  backward equation itself, and the fixation probability it is used to compute) is not in the
  supplied file.
- The slide file also carries one extracted figure (`05-slides/figures/p003-1.jpeg`), a hand-drawn
  plot of curves from $(0,0)$ rising to $(1, \cdot)$ against a horizontal axis $y$, labelled
  $s>0$, $s=0$, $s<0$, with a curve near the origin marked $1/(Ns)$ — consistent with a fixation-
  probability plot of the kind the backward equation is normally used to derive. It is not
  reproduced here because the paragraph of text that would explain it is missing; noted rather than
  guessed at.
- No transcript, written notes, or exercises were supplied for this lecture.

---

[← 2. Diffusion Limit of Allele Frequencies](02-diffusion-limit-of-allele-frequencies.md) · [Contents](index.md) · [4. Statistical Significance of Sequence Alignments →](04-statistical-significance-of-sequence-alignments.md)
