---
title: Mutual InformaLon (MI)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Mutual InformaLon (MI)

**Source:** `recitations/2014-03-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

MI is maximal (2 bits) if x and y appear at random (all 4 nts equally likely) but perfectly covary (e.g. always complementary)


<!-- Start of picture text -->
1<br>=<br>log2<br>X<br>4 ✓ 11 // 164 ◆<br>( x,y )=( A,U ) , ( C,G ) , ( G,C ) , ( U,A )<br>=<br>1 ⇤ 2<br>X<br>4<br>( x,y )=( A,U ) , ( C,G ) , ( G,C ) , ( U,A )<br><!-- End of picture text -->


<!-- Start of picture text -->
= 2 bits<br><!-- End of picture text -->

14

# 2 **nd approach: Energy** minimiza'on ΔGfolding = Gunfolded - Gfolded

- -­‐ Assume that RNA   will fold to its lowest energy state

- -­‐ Simplest model: all base pairs contribute equally to lowering structure’s   energy

   - -­‐ Base Pair MaximizaLon (ignores energy contribuLons of base stacking, loops, entropy, etc.): +1 for paired bases, 0 for unpaired

      - -­‐ Use the Nussinov algorithm of recursive maximizaLon of base pairing

15

See the Eddy Nature   Biotechnology Primer 2004

---

[← Mutual InformaLon (MI)](10-mutual-informalon-mi.md) · [Up: contents](index.md) · [Nussinov algorithm →](12-nussinov-algorithm.md)
