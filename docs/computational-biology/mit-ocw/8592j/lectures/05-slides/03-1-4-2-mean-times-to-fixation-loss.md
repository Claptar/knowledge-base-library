---
title: 1.4.2 Mean times to fixation/loss
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.4.2 Mean times to fixation/loss

**Source:** `lectures/05-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

When there is an absorbing state in the dynamics, we can ask how long it takes for the process to terminate at such a state. In the context of random walks, this is known as the first passage time, and can be visualized as the time it takes for a random walker to fall into a trap. Actually, since the process is stochastic, the time to fixation (or loss) is itself a random quantity with a probability distribution. Here we shall compute an easier quantity, the mean of this distribution, as an indicator of a typical time scale.

Let us consider an absorbing state at xa, and the difference p(xa, t + dt|y) − p(xa, t|y) = dt∂p(xa, t|y)/∂t. Clearly the probability to be at xa only changes due to absorption of particles, and thus ∂p(xa, t|y)/∂t is proportional to the probability density function (PDF) for fixation at time t. The conditional PDF that the process terminates at xa must be

17

properly normalized, and we have to divide by the integral �0∞<sup>dt∂p(xa, t|y)/∂t,whichis</sup> simply Π<sup>∗</sup> (xa, y). Thus the normalized conditional PDF for fixation at time t at xa is


The mean fixation time is now computed from


Following Kimura and Ohta (1968)<sup>3</sup> , we first examine the numerator of the above expression, defined as


(Writing limT →∞ �0T<sup>ratherthansimply</sup> �0∞ is for later convenience.) We can integrate this equation by parts to get


Let us denote the operations involved on the right-hand side of the backward Kolmogorov equation by the short-hand By, i.e.


Acting with By on both sides of Eq. (1.77), we find


But ByΠ<sup>∗</sup> (xa, y) = 0 according to Eq. (1.68), while Byp(xa, t|y) = ∂p(xa, t|y)/∂t from Eq. (1.67). Integrating the latter over time leads to


For example, let us consider a population with no selection (s = 0), for which the probability to lose a mutation is Π0 = (1 − y). In this case, Eq. (1.80) reduces to


> 3M. Kimura and T. Ohta, Genetics 61, 763 (1969).

18

After two integrations we obtains


where the constants of integration are set by the boundary conditions T0(0) = T0(1) = 0, which follow from Eq. (1.76). From Eq. (1.75), we then obtain the mean time to loss of a mutation as


A single mutation appearing in a diploid population corresponds to y = 1/(2N), for which the mean number of generations to loss is ⟨τ (y)⟩0 ≈ 2 ln(2N). The mean time to fixation is obtained simply by replacing y with (1 − y) in Eq. (1.83) as


The mean time for fixation of a newly appearing mutation (y = 1/(2N)) is thus ⟨τ (y)⟩1 ≈ (4N).

We can also examine the amount of time that the mutation survives in the population. The net probability that the mutation is still present at time t is


where the integrations exclude the absorbing points at 0 and 1. Conversely, the PDF that the mutation disappears (by loss or fixation) at time t is


(Note that the above PDF is properly normalized as S(∞) = 0, while S(0) = 1.) The mean survival time is thus given by


where we have performed integration by parts and noted that the boundary terms are zero. Applying the backward Kolmogorov operator to both sides of the above equation gives


19

In the absence of selection, we obtain


After two integrations we obtains


where the constants of integration are set by the boundary conditions ⟨τ (0)⟩× = ⟨τ (1)⟩× = 0. Note the interesting relation


20

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 1.4.1 Fixation probability](02-1-4-1-fixation-probability.md) · [Up: contents](index.md)
