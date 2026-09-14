---
title: 3. Diffusion and cAMP waves
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/exams/final-ps-exam.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Diffusion and cAMP waves

**Source:** `exams/final-ps-exam.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

When cells are grown on a plate, cAMP diffusion is slow, and the extracellular cAMP concentration is no longer uniform. Consider a plate on which there exists a uniformly distributed population of cells. Each cell senses cAMP in its environment, and secretes fresh cAMP in response. This new batch of cAMP is able to reach neighboring cells, stimulating them to synthesize more cAMP, and so on. The situation is similar to one in which a number of radio transmitter towers (cells) are used to detect, amplify, and re-broadcast a weak radio signal (cAMP). The cAMP concentration now varies over space as well as time. For simplicity, we will analyze a 1-dimensional case, with cells uniformly distributed along a line. We can assume that the cells have fixed positions over the timescales considered, because their chemotaxis is relatively slow. This system obeys the equations


We have provided MATLAB code which simulates the time evolution of a reaction-diffusion system. Modify the code to implement these equations. The system is assumed to extend from _x_ = -1 to _x_ = +1, with no flow at the boundaries. Use the following initial conditions:


That is, provide an initial pulse of cAMP centered at the origin, and some non-zero amount of inhibitor activity in all cells.

(10)

   - _a._ Use the following parameters: β = 4 ; _k_ = 5.0 ; _D_ = 10<sup>−7</sup> ; σ = 1.0 ; _i_ 0 = 1.0 . Run the simulation to see the emergence of cAMP waves emanating from the origin. Plot out a typical cAMP profile, indicating the direction of motion of the waves.

- (5) _b._ Run the simulation again, this time with a _k_ value which produces a non-oscillating system. Describe the typical cAMP profile once the transients have died out. Can cells find the initial source of cAMP based on this type of profile?

- (5) _c._ A simple concentration gradient would allow cells to find the cAMP source. Why do you think _Dictyostelium_ uses waves of cAMP rather than a gradient in order to trigger cell aggregation?

---

[← 2. Positive feedback and oscillations](03-2-positive-feedback-and-oscillations.md) · [Up: contents](index.md) · [4. Receptor clustering and signal amplification →](05-4-receptor-clustering-and-signal-amplification.md)
