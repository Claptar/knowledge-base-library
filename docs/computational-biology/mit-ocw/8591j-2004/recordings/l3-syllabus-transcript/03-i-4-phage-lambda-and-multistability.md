---
title: I.4 Phage lambda and multistability
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l3-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# I.4 Phage lambda and multistability

**Source:** `recordings/l3-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Matlab code 2 shows that dependent on the initial conditions the steady state value that is reached can be different. In this specific example the system has two stable state and is therefore bistable. This multistability is analyzed by doing a stability analysis. Equation [III.12] can be rewritten as:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

18

The functions f(x) and g(x) represent the creation and destruction terms of cI monomer. In steady-state f(x)=g(x) and this relation is graphically solved (Fig. 6). For small γ there is only one intersection point between f(x) and g(x) reflecting one solution in the steadystate (this point is called a fixed point). This is a stable fixed point since a deviation to a higher value of x results in a larger destruction rate than creation (g(x)>f(x)). This means that there will be a net decrease in x, pushing the deviation back to the fixed point. The opposite happens for a deviation of a lower x value (g(x)<f(x)). At intermediate γ there are 3 fixed points. Using the same strategy one finds that the outer fixed points are stable and the middle fixed point is unstable. A small deviation to larger x from the middle fixed point leads to an increased x until it reaches the upper fixed point. A small deviation to a smaller x from the middle fixed point results in a decrease in x until it reaches the lower fixed point.

---

[← References](02-references.md) · [Up: contents](index.md) · [Further reading on phage lambda and multistability →](04-further-reading-on-phage-lambda-and-multistability.md)
