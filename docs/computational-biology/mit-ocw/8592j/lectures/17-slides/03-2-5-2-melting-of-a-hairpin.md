---
title: 2.5.2 Melting of a hairpin
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2.5.2 Melting of a hairpin

**Source:** `lectures/17-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A particularly simple native RNA structure is a hairpin. For long hairpins the transition from the native form to the molten state can be described analytically using a so-called G˜o model<sup>4</sup> . In the native configuration monomers k and 2N − k +1 are paired together, while in


intermediate configurations partially melted segments alternate with segments that maintain the original bonding.


A partition function is obtained by summing over all partially melted configurations, and ignoring any interaction between the segments, takes the form


with the constraint l1 +l2+l3+· · · = N. The contribution of the molten segments comes from Eq. (2.101). For the native segments, we should add the binding energies of the segments. To make the problem analytically tractable, we assign to each native bond an energy ε < ε, and a corresponding Boltzmann weight q = e<sup>−β</sup> ε > q. With these simplifications, the problem becomes identical to the Poland–Scheraga model in Eq. (2.79) with w = q, g = 1 + 2<sup>√</sup> q and c = 3/2. It is thus possible to obtain a melting transition at a finite temperature at which the native fraction goes to zero linearly (β = 1 from Eq. (2.94)).

> 4R. Bundschuh and T. Hwa, Phys. Rev. Lett. 83, 1479 (1999).

59

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 2.5.1 Free energy of molten RNA](02-2-5-1-free-energy-of-molten-rna.md) · [Up: contents](index.md)
