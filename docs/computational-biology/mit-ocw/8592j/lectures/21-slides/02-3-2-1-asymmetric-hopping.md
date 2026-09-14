---
title: 3.2.1 Asymmetric Hopping
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/21-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.2.1 Asymmetric Hopping

**Source:** `lectures/21-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Rather than working with a continuous ratchet potential, we can capture much of the same physics by examining so called asymmetric hopping models,<sup>3</sup> in which the motor makes discrete jumps along its track. However, at each site along the track, it can be in a discrete number of internal states. For example, in the system depicted below, there are 4 internal states at each site, e.g. corresponding to: MT, MT+ATP, MT+ADP+P, MT+ADP. One


then assigns rates for transitions along the track and between internal states. With proper choice of asymmetric rates the motion can be biased in one direction.

Let us demonstrate the procedure and the constraints involved for a simple model with only two internal states, say representing the motor bound to ATP or ADP. We shall denote the rates for transitions between the two internal states by u and d. As the motor moves to the next site along the track it must change its internal state, and we assign asymmetric rates of r and l for moving to the right (T→D) and the left (D→T) respectively. The Master equations governing the evolution of probabilities for these states are


For slowly varying probabilities, the continuum form of these equations is


We can extract the behavior of the above equations for slow and long wavelength variations by first noting that (relatively) rapid interconversion between internal states leads to a local equilibrium in which


or in terms of the net probability, p(x) = pT (x) + pD(x),


> 3M.E. Fisher and A.B. Kolomeisky, PNAS 96, 6597 (1999).

67

Adding the two Eqs (3.24) and substituting from Eq. (3.26) leads to a standard drift-diffusion equation for p(x, t), with drift velocity


and diffusion coefficient


The requirement of thermal equilibrium places stringent constraints on any pair of forward/backward reaction rates. In particular, assuming an activation energy ∆Ua between internal states, and an energy difference ∆Ua for the steps along the track, we must have


Substituting these forms in the equation for velocity, we find


When there is no input of energy, the two paths to go between T and D states should be equivalent, ∆a = ∆s, and there is no net velocity. The hydrolysis of ATP provides a source of energy, such that ∆Us = ∆Ua + ∆Gh, encouraging steps to the right and a positive velocity.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [3.2.2 Force of a Brownian Motor →](03-3-2-2-force-of-a-brownian-motor.md)
