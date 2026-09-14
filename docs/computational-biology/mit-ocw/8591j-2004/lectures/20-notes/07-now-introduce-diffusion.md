---
title: Now introduce diffusion
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/20-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Now introduce diffusion

**Source:** `lectures/20-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- only I diffuses, other components are local 2 ∂ _I x t_ ∂ _I x t_ <u>( , ) ( , )</u> = − _k_ − _I I_ ( _x_ , _t_ ) + _kI S_ ( _x_ , _t_ ) + _D_ 2 ∂ _t_ ∂ _x_

- assume signal S varies linearly with S

= _S_ ( _x_ ) _so_ + _s_ 1 _x_

- no flux boundary conditions for I

∂ _I_ <u>(0,</u> _t_ <u>)</u> ∂ _I_ <u>(1,</u> _t_ <u>)</u> = = 0 ∂ _x_ ∂ _x_

in steady state,this system can be solved analytically !

10

2 ∂ _I x t_ ∂ _I x t_ <u>( , ) ( , )</u> = − _k_ − _I I_ ( _x_ , _t_ ) + _kI S_ ( _x_ , _t_ ) + _D_ 2 ∂ _t_ ∂ _x_ 2 ∂ _I_ <u>(</u> _x_ <u>)</u> _k_ − _<u>I</u> kI_ = − _I x s_ + _s x_ 2 ( ) [ _o_ 1 ] ∂ _x D D_ 2 ∂ _I_ <u>(</u> _x_ <u>)</u> = _aI_ ( _x_ ) − _b_ − _cx_ 2 ∂ _x_

---

[← Steady state](06-steady-state.md) · [Up: contents](index.md) · [steady-state →](08-steady-state.md)
