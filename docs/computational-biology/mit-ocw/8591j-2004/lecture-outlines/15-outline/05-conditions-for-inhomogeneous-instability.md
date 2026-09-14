---
title: Conditions for inhomogeneous instability
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/15-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Conditions for inhomogeneous instability

**Source:** `lecture-outlines/15-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us explore the conditions for inhomogeneous instability. To obtain an instable system we have to obey the reverse of [VIII.19]:


where α ≡ l2 . The function f(α) is a parabola that is concave upward. For f(α) to be negative the parabola should have two real roots of which at least one is positive. The roots of f(α) are found by solving:


The roots of [VIII.21] are therefore both real if:


According to [VIII.19] this means that both roots are positive and therefore:


This is the instability condition. So if [VIII.23] is true, f(α) will be negative for certain values of α. Condition [VIII.23] defines a critical value for R. For R>Rc [VIII.23] holds.


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

47

In the following discussion we will assume strong autocatalytic reaction (R>>1). In that case [VIII.23] reduces to:


This means that


The ratio ( _Da_ /γ _a_ )1/ 2 has units of length and can be interpreted as the a typical distance that activator molecules diffusion before they decay. This distance is often called the activator range. Equation [VIII.26] tells us that it is necessary for the instability of the uniform state that the inhibition range is about 2.5 times larger than the activator range.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

48

---

[← Spatially inhomogeneous solutions](04-spatially-inhomogeneous-solutions.md) · [Up: contents](index.md)
