---
title: The lysis-lysogeny decision
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/03-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The lysis-lysogeny decision

**Source:** `lectures/03-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As the phage genome is injected phage genes are transcribed and translated by using the host’s machinery.

Which set of phage proteins are expressed determines the fate of the phage: lysis or lysogeny

Image removed due to copyright considerations.

A lysogen is immune to invasion of another phage. Repressor dimers turn off genes in the injected phage chromosome. High concentration of repressor keeps cell in lysogenic state.

The lysis-lysogeny decision is a genetic switch


only ‘space’ for one RNA polymerase (mutual exclusion)

Single repressor dimer bound - three cases:

I

Negative control, dimer binding to OR2 inhibits RNAp binding to right PR promoter.

Positive control, dimer binding to OR2 enhances RNAp binding to left PRM promoter.

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

II

Negative control, dimer binding to OR1 inhibits RNAp binding to right PR promoter.

Negative control, dimer binding to OR1 inhibits RNAp binding to left PRM promoter (too distant).

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

III Negative control, dimer binding to OR3 inhibits RNAp binding to left PRM promoter.

Positive control, dimer binding to OR3 allows RNAp binding to right PR promoter.

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

Repressor-DNA binding is highly cooperative

intrinsic association constants: KOR1 ~ 10 KOR2 ~ 10 KOR3 However KOR2* >> KOR2 (positive cooperativity)

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

## **`Flipping the switch by UV:`**


Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

In lysogenic state, [repressor] is maintained at constant level by negative feedback

Repressor-DNA binding is highly cooperative

intrinsic association constants: KOR1 ~ 10 KOR2 ~ 10 KOR3 However KOR2* >> KOR2 (positive cooperativity)

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

Cro dimers bind non-cooperatively to OR sites KOR3 ~ 10 KOR2 ~ 10 KOR1

```
Note for repressor:
KOR1~ 10 KOR2~ 10 KOR3
```

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

Image removed due to copyright considerations. See Ptashne, Mark. _A genetic switch: phage lambda_ . 3rd ed. Cold Spring Harbor, N.Y.: Cold Spring Harbor Laboratory Press, 2004.

Cooperative effects make sharp switch (‘well defined’ decision)


<!-- Start of picture text -->
99.7% repression 1.0 nH=3, positively cooperative<br>promoter controlled by a<br>single repressor-operator system  0.8<br>100<br>0.6 nH=1, non cooperative<br>λ PD 0.4<br>50<br>0.2<br>lysogen<br>0.0<br>0 1 2 3 4 5<br>Repressor concentration [S]   (mM)<br>Y<br>% Repression<br><!-- End of picture text -->

Images by MIT OCW.

Note: several layers of cooperativity: dimerization, cooperative repressor binding

---

[← Introduction phage biology](07-introduction-phage-biology.md) · [Up: contents](index.md) · [How to create a mathematical model that captures the essence of the switch ? →](09-how-to-create-a-mathematical-model-that-captures-the-essence.md)
