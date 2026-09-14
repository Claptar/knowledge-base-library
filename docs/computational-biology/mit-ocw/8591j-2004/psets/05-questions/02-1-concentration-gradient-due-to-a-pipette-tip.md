---
title: 1. Concentration gradient due to a pipette tip.
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Concentration gradient due to a pipette tip.

**Source:** `psets/05-questions.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A pipette is connected to a reservoir of cAMP at concentration _cp_ , and its tip is placed in a beaker of water. cAMP begins to diffuse from regions of high concentration to those of low concentration, creating a total flux _F_ out of the reservoir; the resulting drop in the reservoir concentration of cAMP is negligible. Meanwhile, a concentration gradient is set up in the beaker, with [cAMP] = _cp_ at the pipette tip, and zero far from the tip. The purpose of this problem is to calculate the resulting concentration profile.

- (10) _a._ Consider a spherical surface of radius _r_ , centered at the pipette tip, through which there flows a flux per unit area _J_ ( _r_ ) (see Fig. 1). What is the total flux _F_ ( _r_ ) through this surface?

- (10) _b._ Since cAMP is neither created nor degraded in the beaker, the total flux through a sphere at any radius must be a constant; that is, _F_ ( _r_ ) = _F_ . What does this imply about _J_ ( _r_ ) ?

- (20) _c._ Fick’s first law (with diffusion coefficient set to unity) states that _J_ ( _r_ ) = − ∂ _c_ ( _r_ ) ∂ _r_ . Integrate your answer from part ( _b_ ) to calculate _c_ ( _r_ ). If _rP_ is the radius of the pipette tip, then _c_ ( _rp_ ) = _cp_ , and _c_ (∞)=0. Calculate the value of _F_ required for _c_ ( _r_ ) to satisfy these boundary conditions. Give expressions for _c_ ( _r_ ) and _J_ ( _r_ ) in terms of _cp_ , _rp_ , and _r_ .

- (10) _d._ A spherical cell of radius ρ _0_ is placed a distance _R_ from the pipette tip, with ρ _0_ << _R_ . The flux is therefore nearly constant near the cell, and the concentration changes linearly from the leading edge to the trailing edge of the cell. That is, _J_ ( _r_ ) ≈ _J_ ( ) , _R_ and _c_ ( _r_ ) ≈ _c_ ( _R_ ) − _J_ ( _R_ ) ⋅ ( _r_ − _R_ ) . We now change coordinates, measuring the distance ρ from the center of the cell and the angle θ from its leading edge (see Fig. 2). Calculate the concentration distribution along the cell surface. You should find


<!-- Start of picture text -->
 rp  rp  ρ 0  <br>c (ρ ,0  θ ) = c p   + R  2  cos(θ) .<br> R  <br>Fig. 1  Fig. 2<br><!-- End of picture text -->

1

FA04

**Systems Biology**

**7.81/8.591/9.531**

---

[← Problem Set 5 Due in class](01-problem-set-5-due-in-class.md) · [Up: contents](index.md) · [2. Cell in a linear concentration gradient →](03-2-cell-in-a-linear-concentration-gradient.md)
