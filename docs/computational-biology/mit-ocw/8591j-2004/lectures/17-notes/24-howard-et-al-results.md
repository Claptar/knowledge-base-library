---
title: 'Howard et al. : Results'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/17-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Howard et al. : Results

**Source:** `lectures/17-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### Image removed due to copyright considerations.

27

Huang, Meir, and Wingreen, _PNAS_ **100** , 12724 (2003). **main differences:**

- ATP cycle

- 1D versus 3D (projected on 2D)

Image removed due to copyright considerations.

28

Image removed due to copyright considerations.

ρd: membrane bound minD:ATP complexes ρde: membrane bound minD:minE:ATP complexes ρD:ADP:concentration cytoplasmic minD bound to ADP ρD:ATP :concentration cytoplasmic minD bound to ATP ρE : concentration cytoplasmic minE only minD-ATP can associate with membrane minE only binds minD-ATP oligomers in membrane

29

### <u>Reaction 1:</u>

minD-ATP binds both linearly and autocatalytically to minD-ATP in membrane

Image removed due to copyright considerations.

### minD forms polymers in membrane


<!-- Start of picture text -->
2<br>d<br>dρD:ADP ρD : ADP ADP → ATP<br>= −<br>DD 2 σ D ρD:ADP + σ de ρde<br>dt dx<br>2<br>d<br>dρD:ATP ρD : ATP ADP → ATP<br>= −<br>DD 2 + σ D ρD:ADP [σ D + σ dD (ρ d + ρ de )] ρD : ATP<br>dt dx<br>2<br>dρE d ρE<br>= −<br>DE 2 + σ de ρe σ E ρd ρE<br>dt dx<br>dρd<br>= −<br>σ E ρ d ρ E + [σ D + σ dD (ρ d + ρ de )] ρD : ATP<br>dt<br>dρde<br>= −<br>σ de ρ de + σ E ρ d ρE 30<br><!-- End of picture text -->

30

### <u>Reaction 2:</u>

minE binds minD-ATP in membrane ~ [minE]*[mind]

Image removed due to copyright considerations.


<!-- Start of picture text -->
2<br>d<br>dρD:ADP ρD : ADP ADP → ATP<br>= −<br>DD 2 σ D ρD:ADP + σ de ρde<br>dt dx<br>2<br>d<br>dρD:ATP ρD : ATP ADP → ATP<br>= −<br>DD 2 + σ D ρD:ADP [σ D + σ dD (ρ d + ρ de )] ρD : ATP<br>dt dx<br>2<br>dρE d ρE<br>= −<br>DE 2 + σ de ρe σ E ρd ρE<br>dt dx<br>dρd<br>= −<br>σ E ρ d ρ E + [σ D + σ dD (ρ d + ρ de )] ρD : ATP<br>dt<br>dρde<br>= −<br>dt σ de ρ de + σ E ρ d ρE 31<br><!-- End of picture text -->

### <u>Reaction 3:</u>

### minD-minE-ATP complex disassociates from membrane hydrolyzing ATP ~ [mine]

Image removed due to copyright considerations.


<!-- Start of picture text -->
2<br>d<br>dρD:ADP ρD : ADP ADP → ATP<br>= −<br>DD 2 σ D ρD:ADP + σ de ρde<br>dt dx<br>2<br>d<br>dρD:ATP ρD : ATP ADP → ATP<br>= −<br>DD 2 + σ D ρD:ADP [σ D + σ dD (ρ d + ρ de )] ρD : ATP<br>dt dx<br>2<br>dρE d ρE<br>= −<br>DE 2 + σ de ρde σ E ρd ρE<br>dt dx<br>dρd<br>= −<br>σ E ρ d ρ E + [σ D + σ dD (ρ d + ρ de )] ρD : ATP<br>dt<br>dρde<br>= −<br>dt σ de ρ de + σ E ρ d ρE 32<br><!-- End of picture text -->

### <u>Reaction 4:</u>

### charging of minD in cytoplasm from  ADP to ATP bound

Image removed due to copyright considerations.


<!-- Start of picture text -->
2<br>d<br>dρD:ADP ρD : ADP ADP → ATP<br>= −<br>DD 2 σ D ρD:ADP + σ de ρde<br>dt dx<br>2<br>d<br>dρD:ATP ρD : ATP ADP → ATP<br>= −<br>DD 2 + σ D ρD:ADP [σ D + σ dD (ρ d + ρ de )] ρD : ATP<br>dt dx<br>2<br>dρE d ρE<br>= −<br>DE 2 + σ de ρde σ E ρd ρE<br>dt dx<br>dρd<br>= −<br>σ E ρ d ρ E + [σ D + σ dD (ρ d + ρ de )] ρD : ATP<br>dt<br><!-- End of picture text -->

_dρde_ = − σ _de_ ρ _de_ + σ _E_ ρ _d ρE_

33


<!-- Start of picture text -->
2<br>d d<br>ρ D ρ D<br>−<br>=  D D 2 σ A ρ D + σ P ρ D : ADP<br>dt dx<br>d<br>ρ d<br>= −<br>(σ D + sd ρ d )ρ D : ATP σ e ρ e<br>dt<br>2<br>d d<br>ρ D : ATP ρ D : ATP<br>= −<br>D D 2 (σ D + sd ρ d )ρ D : ATP + σ A ρ D<br>dt dx<br>d<br>ρ e = σ dE (ρ d − ρ e )ρ E −σ e ρ e<br>dt<br>2<br>d d<br>ρ E ρ E<br>= − −<br>D E 2 σ dE (ρ d ρ e )ρ E + σ e ρ e<br>dt dx<br>2<br>d d<br>ρ D : ADP ρ D : ADP<br>= −<br>D D 2 σ P ρ D : ADP + σ e ρ e<br>dt dx<br><!-- End of picture text -->

34

---

[← 3. test stability of fluctuations around homogeneous solution](23-3-test-stability-of-fluctuations-around-homogeneous-solution.md) · [Up: contents](index.md)
