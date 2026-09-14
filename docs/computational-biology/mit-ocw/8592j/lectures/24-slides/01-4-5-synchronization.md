---
title: 4.5 Synchronization
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/24-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.5 Synchronization

**Source:** `lectures/24-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We have established how simple chemical reactions can create an oscillator. The phase of such simple oscillators is set by initial conditions. In certain situations, e.g. for the pacemaker cells in the heart, the oscillators must act in concert. One way to synchronize a number of oscillators is to couple them to an external source, as in the light of the sun in case of circadian rhythms. In other cases, a collection of self–coupled oscillators may spontaneously synchronize as a collective. The following Kuramoto model provides an explanation of how such synchronization may happen.

Consider a set of oscillators, each parametrized by a phase angle θi, for i = 1, 2, · · · , N. We shall assume that each oscillator advances at a uniform angular velocity ωi, taken independently from a probability distribution function p(ω), such that


In a biological context the rate ω for a collection of cells (or organisms) may well depend on the concentration of chemicals within it. While these concentrations vary between individuals, it is likely that for a specific system the range of this variation is small, and the distribution is narrowly peaked around some central frequency Ω. Without loss of mathematical rigor we can set Ω= 0, which is equivalent to measuring angles relative to a frame rotating at angular velocity Ω(i.e. after a shift θi → θi − Ωt).

To synchronize the oscillators we need a coupling between their phases. The simplest form of such coupling, pushing θi towards θj, and independent of a phase change by 2π, is sin(θj − θi). The coupled dynamics of phases of many such oscillators is now governed by


where Wij indicates the strength of the coupling to j from i. To make analytical progress, we shall assume that all interactions have the same value of K/N. (As each oscillator is coupled to N others, it makes sense to scale the interaction parameter by N.) In this case, we can re-write Eq. (4.37) as


where ℑ stands for the imaginary part, and we have indicated the average of all phase points (around the complex imaginary circle) by me<sup>iφ</sup> . The order parameter


is a measure of synchronization amongst the oscillators. If each oscillator follows its own period, perhaps somewhat altered by the others, the phases in Eq. (4.39) will shift with time

83

more or less independently, eventually coving the unit circle, in which case the average over them will be zero. If a finite fraction of the oscillators is locked to the central frequency Ω (thus appearing stationary in our rotating frame), their contributions will be time independent, and (if more or less in phase) add us to a finite value. Without loss of generality, we can set the overall phase of the sum to zero, φ = 0, resulting in the self-consistent set of equations


The solutions to this equation have two possible forms, mimicking the two populations of oscillators. The first set includes oscillators locked to the central frequency, hence with θ˙i = 0. To satisfy Eq. (4.40), these oscillators acquire a “phase lag”


Such locking is possible only if the natural frequency of the oscillator is sufficiently close to the central frequency, i.e. as long as |ωi| < Km. Oscillators with frequency difference |ωi| > Km cannot be synchronized to the central frequency, and their phases vary over time according to


We can self-consistently solve for m by summing over the phase contributions of the stationary oscillators (the moving ones do not contribute to m). Since the behavior of the locked oscillators depends only on their native frequency, we can use the probability density p(ω) to write


We can change variables to θ = arcsin(ω/Km), and expand the narrow distribution to second order around its peak to simplify the self-consistency equation to


84


A non-zero solution for m is possible only for


Below Kc, m = 0 is the only solution, and all oscillators are unlocked. For larger couplings the oscillators are synchronized and rotate together, while on reducing the coupling to its critical value the order parameter vanishes as


For example, if p(ω) can be approximated by a Gaussian distribution of width σ,

---

[Up: contents](index.md) · [4.6 Turing patterns →](02-4-6-turing-patterns.md)
