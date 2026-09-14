---
title: 3. Simulated Annealing
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Simulated Annealing

**Source:** `recitations/2014-04-02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Stochas'c   search   of   protein   conforma'ons

- • Metropolis-­‐Has'ngs   algorithm   is   an   implementa'on   of Simula'ng   Annealing   that   generates   sample   states   of   a thermodynamic   system

- Monte-­‐Carlo   method   (as   was   Gibbs   Sampler)

- • Idea:   Sample   a   new   conforma'on   by   perturbing protein’s   current   structure

   - If   lower   energy,   accept   new   conforma'on

   - If   higher   energy,   accept   it   with   probability   propor'onal   to difference   in   energy   between   two   structures

      - Unlike   Energy   Minimiza'on,   it   is   possible   to   move   upward   on   the poten'al   energy   surface,   which   may   allow   us   to   escape   a   local minimum   and   find   the   global   minimum

24

---

[← 2. Molecular Dynamics](12-2-molecular-dynamics.md) · [Up: contents](index.md) · [3. Simulated Annealing →](14-3-simulated-annealing.md)
