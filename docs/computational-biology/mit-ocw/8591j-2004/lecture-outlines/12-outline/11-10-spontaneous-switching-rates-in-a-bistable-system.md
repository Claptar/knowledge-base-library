---
title: 10. Spontaneous switching rates in a bistable system
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10. Spontaneous switching rates in a bistable system

**Source:** `lecture-outlines/12-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
250<br>200  a<br>150<br>100<br>50<br>0<br>0  1000  2000  3000  4000  5000<br>time<br>x<br><!-- End of picture text -->


<!-- Start of picture text -->
1000<br>b<br>100<br>10<br>1<br>0  20  40  60  80  100<br>< x ><br>Lifetime<br><!-- End of picture text -->

Figure 5: Stochastic transitions and escape times

We can now simulate the time evolution of the system introduced in section 7. We find that an individual cell transitions stochastically between the available steady states (Fig. 5a), while the cell population has a histogram of _x_ values as shown in Fig. 4. An important quantity to investigate is the average escape time from a given state, known as the lifetime of that state. Figure 5b shows the lifetime of the induced state as a function of the average number of _X_ molecules in that state. Once again, we can see the crossover to deterministic behavior: as the number of molecules becomes large, the escape time diverges, and the stable states become truly stable. Note that we are measuring time in units of the degradation time of _X_ , which is typically of the order of a cell lifetime. If we use Eq. 16 as a model of lysis/lysogeny network of phage-λ, then the induced state corresponds to lysogeny, and escape corresponds to spontaneous lysis. Lysogens have been measured to undergo spontaneous lysis at a rate of about 10<sup>-8</sup> per cell per generation: the switch is extremely stable. Our simple network would require about 1000 molecules to achieve comparable stability, which is consistent with measured repressor concentrations. It is possible, however, to increase the stability of a switch by other means, such as by increasing the cooperativity, or through the use of stabilizing feedback loops.

M.T. 09.24.03

---

[← 9. Stochastic simulation of chemical reactions](10-9-stochastic-simulation-of-chemical-reactions.md) · [Up: contents](index.md)
