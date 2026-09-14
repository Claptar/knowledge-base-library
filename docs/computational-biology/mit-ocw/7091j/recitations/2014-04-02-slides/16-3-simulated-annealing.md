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

- Metropolis-­‐Has'ngs   acceptance   criterion: – If   test   conforma'on   has   lower   energy,   always   accept   it – If   test   conforma'on   has   higher   energy,   accept   it   with probability:


Probability   of   each   conforma'on Z(T)   is   a   normaliza'on _k_ is   Boltzmann   constant;   can follows   Boltzmann   distribu'on constant   that   cancels refer   to _kT_ as   “temperature” – At   higher   temperature,   exponent   is   closer   to   0   so acceptance   probability   is   closer   to   1   (more   likely   to accept   higher   energy   conforma'onal   changes)

27

## Structure   discovery   using   homology

- In   determining   a   structure,   if   regions   of   your   query   protein   are homologous   (evolu'onarily   related)   to   other   proteins   of   known structure,   they   likely   adopt   the   homologous   structure/fold

- Align   your   query   protein   to   those   in   the   PDB:

   - High   (50%+)   sequence   similarity

   - Medium   (20%-­‐50%)   sequence   similarity

   - Low   (<20%)   sequence   similarity

28

## Structure   discovery   using   homology

- In   determining   a   structure,   if   regions   of   your   query   protein   are homologous   (evolu'onarily   related)   to   other   proteins   of   known structure,   they   likely   adopt   the   homologous   structure/fold

- Align   your   query   protein   to   those   in   the   PDB:

   - High   (50%+)   sequence   similarity

   - Medium   (20%-­‐50%)   sequence   similarity • Can   be   confident   the   structures   are   very   similar   –   generally   only   need   to

   - – Low   (<20%)   sequence   similarity   refine   regions   where   alignment   is   poor.

29

## Structure   discovery   using   homology

- In   determining   a   structure,   if   regions   of   your   query   protein   are homologous   (evolu'onarily   related)   to   other   proteins   of   known structure,   they   likely   adopt   the   homologous   structure/fold

- • Align   your   query   protein   to   those   in   the   PDB:

   - Medium   (20%-­‐50%)   sequence   similarity

   - Low   (<20%)   sequence   similarity • Try   several   alignments,   and   refine   structure   resul'ng   from   each.   Choose the   final   based   on   lowest   energy.

30

## Structure   discovery   using   homology

- In   determining   a   structure,   if   regions   of   your   query   protein   are homologous   (evolu'onarily   related)   to   other   proteins   of   known structure,   they   likely   adopt   the   homologous   structure/fold

- • Align   your   query   protein   to   those   in   the   PDB:

   - Low   (<20%)   sequence   similarity

      - Lots   of   possible   star'ng   structures   from   different   alignments.   Need   to   do more   aggressive   refinement   since   final   structure   may   be   significantly different   than   star'ng   structure;   choose   final   structure   based   on   lowest energy.

31

## Structure   discovery   without   homology


- Monte   Carlo   search   of   backbone   phi/psi   angles

   - Choose   small   region   of   3-­‐9   a.a.s   and   set   angles   to   those   of similar   pep'de   in   PDB

   - Calculate   energy   of   structure   with   new   angles   of   the   3-­‐9   a.a.s

   - Accept   according   to   Metropolis   criterion

- Repeat   this   36,000   'mes   to   get   1   final   structure

- Cluster   the   many   structures   into   small   number   of representa've   groups;   more   sophis'cated   refinement of   groups

32

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802 / 6.874 / HST.506 Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 3. Simulated Annealing](15-3-simulated-annealing.md) · [Up: contents](index.md)
