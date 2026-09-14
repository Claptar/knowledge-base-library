---
title: 2.3.5 Designed REM for protein folding
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.3.5 Designed REM for protein folding

**Source:** `lectures/11-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

It is tempting to equate the freezing of the heteropolymer with the folding transition separating denatured and folded states of a protein. There is, however, a problem with such an interpretation: As the temperature is lowered towards Tc, the number of states decreases drastically. It is unlikely that the lower energy states of the REM in the vicinity of Ec have much in common. To change its state the polymer will likely have to rearrange many of its monomers, running into high energy barriers in the process. Thus we expect that the kinetics of the REM polymer will slow down significantly on approaching Tc. This contradicts the observation that most proteins fold easily and in a short time. Of course proteins are not typical random heteropolymers, and are presumably “designed” through evolution for both function and ease of folding. Fortunately, we can mimic such “design” by a small modification of the REM; we only need to add to the continuum of random energy states, a single state with low energy (En < Ec) representing the native configuration.


With the added state at En, the system makes a transition to the native state (i.e. folds) at a temperature Tf , high enough that there are still many equivalent states to explore. The location of Tf , and the corresponding energy Ef , can be obtained by equating free energies or Boltzmann weights, and leads to the “tangent construction” whereby Tf and Ef are related

46

to En via


As depicted in the figure, the above result equates the slope of the tangent line from the point at En computed in two different ways.

To justify the above result, note that in the canonical ensemble, the probability of finding the system in the native state is


A phase transition in which pn changes discontinuously from zero to one occurs only in the thermodynamic limit of N →∞. For the system to have a well-behaved thermodynamic limit (in which case various thermodynamic identities involving entropy and temperature can be safely used), we must insist that the range of energies as well as ln Ω(E) should be proportional to N; the former implies that En ∝ N. If so, then at a particular value of β a single value of energy E completely dominates the partition function Z(β). For the partition function in Eq. (2.66), the dominant value occurs for some E ≥ Ef for β ≤ βf , and for E = En for β > βf . The probability to find the system in its native state then jumps discontinuously from 0 to 1 at the point when the corresponding contributions to the partition function are equal, i.e. at


which after taking the logarithm leads to the tangent rule in Eq. (2.65).

We can eliminate Ef in terms of βf by noting that E = Nε0−Nσ<sup>2</sup> β, and ln g<sup>′</sup> = (βcσ)<sup>2</sup> /2. Using these expressions and defining a quantity βn = (En − Nε0)/(Nσ<sup>2</sup> ), the above equation reduces to


This can be rearranged as a quadratic equation with solution


The ratio of the folding temperature to the REM freezing temperature is thus


Faster folding to the native state can be achieved at higher temperatures by increasing the energy difference between En and Ec.

47

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 2.3.4 The Random Energy Model (REM) for compact heteropolymers](03-2-3-4-the-random-energy-model-rem-for-compact-heteropolymers.md) · [Up: contents](index.md)
