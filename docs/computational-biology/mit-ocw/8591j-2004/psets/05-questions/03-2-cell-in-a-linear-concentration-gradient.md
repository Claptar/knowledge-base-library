---
title: 2. Cell in a linear concentration gradient
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. Cell in a linear concentration gradient

**Source:** `psets/05-questions.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The purpose of this problem is to show how the presence of a cell can influence the distribution of a chemical around it. Consider a linear concentration gradient of some chemical, specified by _c_ ( _x_ , _y_ , _z_ ) = _c0_ – _J0 x_ .

- (5)

   - �

   - _a._ Using _J_ = −∇ _c_ , calculate the flux throughout space.

- (5)

   - _b._ Consider a spherical surface of radius ρ _0_ centered at the origin (see Fig. 2). Show that the concentration along this surface is given by _c_ (ρ ,0 θ ) = _c_ 0 + _J_ 0 ρ cos(0 θ ).

- (10) _c._ Now introduce a cell of radius ρ _0_ centered at the origin. If the cell membrane is impermeable to the chemical under consideration, there will be no radial flux at the ˆ �

- cell surface. That is, ρ ⋅ _J_ (ρ ,0 θ ) = − ∂ _c_ (ρ ,θ ) ∂ρ |ρ0 = 0 . Assuming that the concentration distribution far from the cell remains unchanged, make a sketch comparing the lines of flux before and after the cell is introduced.

- (25) _d._ Calculate the new concentration distribution _c_ (ρ ,θ ).

Hint: the diffusion equation in steady state gives 0 = ∂ _c_ ∂ _t_ = ∇ 2 _c_ . That is, the concentration distribution _c_ ( _r_ � )  satisfies Laplace’s equation. The problem is therefore

analagous to one in electrostatics, with _c_ ↔ϕ , and _J_ ↔ _E_ . Outside the sphere, the potential must satisfy Laplace’s equation, and reduce to a linear potential at large distances. Inside the sphere, we must add some charge distribution so that the boundary conditions are satisfied. Convince yourself that the introduction of a dipole at the origin provides the right kind of corrrection, and calculate the resulting potential.

- (5) _e._ Show that the new concentration distribution along the cell surface has the form _c_ (ρ ,0 θ ) = _c_ 0 +α _J_ 0 ρ0 cos(θ ) , with some α > 1. The cell thus experiences a greater concentration difference across its length than we might have guessed from the unperturbed concentration distribution. Sketch the new concentration distribution along the line θ = 0 to illustrate this effect.

- (0) _f._ CHALLENGE. From problem 1 we find that the concentration distribution due to a pipette tip can be written as the potential due to a point charge with _q_ = _c pr p_ . If the cell is small compared with its distance from the pipette tip, this potential can be approximated as linear, providing the starting point for problem 2. If, however, the cell is large or close to the pipette tip, this approximation does not hold. Calculate the exact concentration distribution due to a pipette tip in the presence of a cell.

2

FA04

**Systems Biology**

**7.81/8.591/9.531**

---

[← 1. Concentration gradient due to a pipette tip.](02-1-concentration-gradient-due-to-a-pipette-tip.md) · [Up: contents](index.md) · [3. Gradient sensing →](04-3-gradient-sensing.md)
