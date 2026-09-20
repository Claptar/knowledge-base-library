---
title: "4. Confounding, Backdoor Paths, M-Bias"
course: "Berkeley Stat 156 Fall 2024"
chapter: 4
source: "https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf"
licence: "CC BY-NC 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 156 Fall 2024](https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf), licensed CC BY-NC 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Confounding, Backdoor Paths, M-Bias

## What this covers

This is problem set 4 for Stat 156 (causal inference), due 2024-10-22. It supplies no exposition
of its own — every question exercises material that lecture already covered: directed acyclic
graphs (DAGs) as a language for causal structure, the backdoor criterion for identifying a causal
effect, the ignorability assumption, and M-bias, the case where conditioning on a variable that
looks like a safe control actually opens a path and creates bias. The set assumes the reader
already has that vocabulary, together with potential-outcomes notation $Y(1)$ and $Y(0)$ for the
outcome a unit would show under treatment and under control. Two of the problems also point to
numbered exercises in the course text, *A First Course in Causal Inference*, which this chapter
does not reproduce since it was not supplied.

## Exercises

1. Suppose you run a non-profit working to improve graduation rates in West Africa. You have read
   a study of a randomized controlled trial showing that direct cash transfers significantly
   improved graduation rates in Mexico. You are deciding whether your non-profit should roll out a
   direct-transfer program in West Africa instead. What further information would you want before
   making that decision? (There is no single right answer here — a thoughtful, well-reasoned
   answer earns full credit.)

2. Problem 15.4 from *A First Course in Causal Inference*.

3. Consider the causal graph below.

   <figure>
   <svg viewBox="0 0 320 200" role="img" aria-label="Directed graph with U pointing to X and Z, and X and Z both pointing to Y">
     <defs>
       <marker id="arrow-p3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
         <path d="M0,0L10,5L0,10z" fill="currentColor"/>
       </marker>
     </defs>
     <line x1="52" y1="130" x2="138" y2="60" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p3)"/>
     <line x1="56" y1="140" x2="134" y2="140" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p3)"/>
     <line x1="165" y1="56" x2="255" y2="89" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p3)"/>
     <line x1="165" y1="134" x2="255" y2="101" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p3)"/>
     <text x="40" y="144" text-anchor="middle" font-size="13" fill="currentColor">U</text>
     <text x="150" y="54" text-anchor="middle" font-size="13" fill="currentColor">X</text>
     <text x="150" y="144" text-anchor="middle" font-size="13" fill="currentColor">Z</text>
     <text x="270" y="99" text-anchor="middle" font-size="13" fill="currentColor">Y</text>
   </svg>
   <figcaption>The graph for problem 3: U is a common cause of X and Z, and both X and Z point
   into Y.</figcaption>
   </figure>

   A. Describe the path or paths of association between $Z$ and $Y$. Which, if any, are causal
      paths? Which, if any, are backdoor paths?
   B. Which variable, or variables, must we condition on to achieve ignorability?

4. Consider the causal graph below.

   <figure>
   <svg viewBox="0 0 340 220" role="img" aria-label="Directed graph with W pointing to X and Y, U pointing to X and Z, and Z pointing to Y">
     <defs>
       <marker id="arrow-p4" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
         <path d="M0,0L10,5L0,10z" fill="currentColor"/>
       </marker>
     </defs>
     <line x1="55" y1="37" x2="146" y2="78" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p4)"/>
     <line x1="56" y1="32" x2="284" y2="63" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p4)"/>
     <line x1="52" y1="179" x2="148" y2="96" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p4)"/>
     <line x1="56" y1="186" x2="194" y2="154" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p4)"/>
     <line x1="222" y1="139" x2="288" y2="76" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-p4)"/>
     <text x="40" y="34" text-anchor="middle" font-size="13" fill="currentColor">W</text>
     <text x="40" y="194" text-anchor="middle" font-size="13" fill="currentColor">U</text>
     <text x="160" y="89" text-anchor="middle" font-size="13" fill="currentColor">X</text>
     <text x="210" y="154" text-anchor="middle" font-size="13" fill="currentColor">Z</text>
     <text x="300" y="69" text-anchor="middle" font-size="13" fill="currentColor">Y</text>
   </svg>
   <figcaption>The graph for problem 4: W and U each point into X, W also points directly into Y,
   and U's other child Z points into Y.</figcaption>
   </figure>

   A. Is there confounding between $Z$ and $Y$ in this graph — that is, do we need to adjust for
      any variable to identify the causal relationship between $Z$ and $Y$? Explain why or why
      not.
   B. Can we identify the heterogeneous average causal effect $E[Y(1) - Y(0) \mid X]$? If so, give
      the identification; if not, explain why not.

5. Give a real-life example of M-bias. Draw the M-bias graph structure and say what each node
   corresponds to in your example.

6. Problem 16.2 from *A First Course in Causal Inference*.

7. Problem 21.1 from *A First Course in Causal Inference*.

8. Problem 21.8 from *A First Course in Causal Inference*.

9. Problem 21.9 from *A First Course in Causal Inference*.

## Sources

- Problems 1, 3, 4, 5, and the textbook pointers for 2, 6, 7, 8, 9: `HW4.md` (berkeley-stat156,
  fall-2024, due 2024-10-22), itself a model reconstruction of `HW4.pdf`, a scanned PDF with no
  text layer, licensed CC BY-NC 4.0. Treat the wording of the problems as a paraphrase of the
  original and the one displayed equation, $E[Y(1) - Y(0) \mid X]$, as unverified.
- The two causal graphs (problems 3 and 4) are redrawn as SVG from the figures extracted from
  pages 1 and 2 of the same PDF (`HW4/figures/p001-1.png`, `HW4/figures/p002-1.png`); the node
  layout and edges follow those images.
- No slides or transcript were supplied for this chapter — the source material is the problem set
  alone, so there is no lecture exposition to draw on beyond what the problems themselves state.
- Problems 2, 6, 7, 8, and 9 refer to numbered problems (15.4, 16.2, 21.1, 21.8, 21.9) in the
  course text *A First Course in Causal Inference*. That text was not supplied, so its problem
  statements are not reproduced here.

---

[← 1. Causal Inference Reading List](01-causal-inference-reading-list.md) · [Contents](index.md) · [5. Instrumental Variables and Noncompliance →](05-instrumental-variables-and-noncompliance.md)
