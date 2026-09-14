---
title: 3.1.3 Caps & Catastrophes
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.1.3 Caps & Catastrophes

**Source:** `lectures/20-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last section we treated the transitions between the growing and shrinking states as instantaneous, effectively examining the MTs at time and length scales much longer than those of individual molecules. We would like to now take a closer look at the events that initiate the catastrophes. As noted earlier, the α and β tubulin molecules that attach to the + end are bound to GTP. The presence of the GTP at, and near, the growing tip stabilizes the MT. Further away from the tip, the GTP attached to β-tubulin (but not that attached to α-tubulin) can hydrolyze to GDP, releasing some energy. This renders the MT susceptible to breakdown and shrinkage. The cap region prevents this breakdown, maintaining the GDP bound portion in a metastable state. However, if through stochastic fluctuations the cap region disappears, the protofilaments start to fray and the MT rapidly shrinks until another cap is formed (a rescue event).


Let us focus on the cap region of the MT, assumed to span a length x from the tip T at the + end to a location E which marks the start of the GDP rich portion of the MT. The length x can change due to the following processes:

- The tip T grows at a rate g(c) that depends on the concentration of tubulin.

- The end E grows at a rate h related to how fast the hydrolyzed front advances along the MT. This rate is presumably independent of the tubulin concentration.

If this is all, the cap region should grow/shrink with an average velocity of v = g(c) − h. However, there will certainly be stochastic fluctuations, which by analogy to the example considered earlier should be described by the equation


for the probability p(x, t) of a cap of length x, where D is some effective diffusion coefficient. However, for v > 0 the above equation predicts a cap that grows indefinitely and the probability of catastrophe becomes negligible, while for v < 0 a catastrophe should occur at a short time set by the initial cap length. These predictions of the model are at variance with experimental observations. For example, the model would predict longer cap lengths in solutions rich in tubulin (along with faster MT growth). If such rapidly growing MTs are then transferred to a solution poor in tubulin (such that v becomes negative), the prediction is that the onset of catastrophes should be later for solutions with faster growth (longer

63

initial caps). This contradicts the observation that the onset of catastrophes is independent of the quality of the initial solution.

One potential solution is to note that hydrolysis events may occur not just at the boundary point E, but throughout the cap.<sup>2</sup> Introducing hydrolyzed GDP at some point y along the cap, effectively fragments it, creating a shorter cap of length y (with the portion from y to x falling away). Since such events can occur at any point along the cap, they should be described by a rate per unit length, which we denote by r. The introduction of r modifies Eq. (3.14) to


The negative term takes into account the reduction in probability of MTs of length x due to hydrolysis at a rate proportional to x; the positive term adds the probabilities for appearance of a segment of length x due to fragmentation of longer segments.

Equation (3.15) is an integral–differential equation, but in terms of the cumulative probability


is equivalent to


as can be verified by applying −∂x to both sides. Equation (3.17) no longer has the integral character, and is thus easier to solve. Rather than a formal solution, we shall determine the key features of the behavior pertaining to catastrophes:

• In good solutions (rich in tubulin) v > 0, and the natural tendency of the cap is to grow longer. This is opposed mostly by the fragmentation events (and to a smaller extent by stochastic diffusion which we shall ignore initially). After a transient period, the competition between growth and fragmentation leads to a steady state distribution p<sup>∗</sup> (x) for cap sizes. Setting D = 0, this stationary solution is easily obtained from Eq. (3.17) as


(Note the boundary conditions P ∗(0) = 1 and P ∗(∞) = 0.) Because of fragmentation the cap does not grow indefinitely, but stabilizes to a typical size


which becomes longer as the tubulin concentration and v increases. For v > 0, there can be no catastrophes if diffusion is ignored. This is because while fragmentation can create short caps, the new cap starts growing away from x = 0. We thus reintroduce D as a small perturbation acting on this steady state, and note that Eq. (3.17) now gives


64

indicating a simple exponential decay. Catastrophes are thus Poisson distributed occuring at a rate Dr/v.

• The situation is very different in tubulin poor solutions with v < 0. In this case fragmented caps shrink to zero length, initiating catastrophes. Starting with a long cap, a catastrophe occurs at time t if a hydrolysis event takes place at some time 0 < τ < t at a position x(τ ) = (t − τ )|v| so that the fragment can shrink to zero in (t − τ ). The probability pcat(t)dt of a catastrophe in the interval [t, t + dt] is thus the product of the probabilities that there are no hydrolysis events in the domain 0 < x < x(τ ) for 0 < τ < t, and that there is a hydrolysis event at the border of this region. Since the area of the domain is |v|t<sup>2</sup> /2, and the hydrolysis events are Poisson distributed, we find


The mean time between catastrophes is thus


This result is quite insensitive the initial length of the cap, explaining experiments in which MTs were transported from good to poor solutions.

65

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 3.1.2 Microtubule Growth and Regulation](03-3-1-2-microtubule-growth-and-regulation.md) · [Up: contents](index.md)
