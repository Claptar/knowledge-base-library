---
title: The G-computation formula
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The G-computation formula

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can factorize the likelihood of the observed data as


Under SRA, the second product term gives the likelihood of the observed treatment process conditional on the full data:


If we fix A<sup>¯</sup> = ¯a for some a¯, we can rewrite the first product term as


where the second equality follows from SRA (Xa(t) ⊥ A<sup>¯</sup> (t − 1)). Note that we rely on ETA for the conditional probabilities to be defined. The equality

8


is known as the G-computation formula for longitudinal data.

---

[← (4) Experimental treatment assignment assumption (ETA)](13-4-experimental-treatment-assignment-assumption-eta.md) · [Up: contents](index.md) · [September 13, 2004 Notes →](15-september-13-2004-notes.md)
