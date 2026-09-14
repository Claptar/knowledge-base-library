---
title: 5. The limit of large numbers
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5. The limit of large numbers

**Source:** `lecture-outlines/12-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The mean and variance of the Poisson distribution are given by:


The relative standard deviation is therefore


This gives us a precise notion of what it means to have a ‘large number’ of molecules in our system: we can expect deviations from deterministic behavior of the order of the inverse square root of the number of molecules involved. Therefore, an ensemble of systems with an average number of 20 molecules will show a spread of 22% about this value (Fig. 3a), while one with 500 molecules will show a spread of just 4% (Fig. 3b).


<!-- Start of picture text -->
35<br>800<br>30  a  700  b<br>25  600<br>20  500<br>400<br>15<br>300<br>10<br>200<br>5  100<br>0 0.0  2.5  5.0  7.5  0 0.0  2.5  5.0  7.5<br>time  time<br>n(t)  n(t)<br><!-- End of picture text -->

Figure 3: The large number limit

---

[← 4. Steady state: the Poisson distribution](05-4-steady-state-the-poisson-distribution.md) · [Up: contents](index.md) · [6. The Fokker-Planck equation →](07-6-the-fokker-planck-equation.md)
