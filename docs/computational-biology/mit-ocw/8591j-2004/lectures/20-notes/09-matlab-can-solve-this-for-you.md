---
title: MATLAB can solve this for you
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/20-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MATLAB can solve this for you

**Source:** `lectures/20-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```
>> dsolve('D2x=a*x-b-c*t','Dx(0)=0,Dx(1)=0')
```

```
ans=
```

```
(b+c*t)/a+c*(-1+cosh(a^(1/2)))/a^(3/2)/sinh(a^(1/2))*cosh(a^(1/2)*t)
-c/a^(3/2)*sinh(a^(1/2)*t)
```

11

− _kI_ ⎛ ⎛ sinh σ _x_ cosh σ _x_ cosh σ 1 ⎞⎞ = − _I x s_ + _s x_ + ( ) _o_ 1 ⎜ ⎟ ⎜<sup>⎜</sup> ⎟<sup>⎟</sup> _k_ − _I_ ⎝ ⎝ σ σ sinh σ ⎠⎠


<!-- Start of picture text -->
kI/k-I=1<br>s0=1 µM<br>s1=0.1 µM<br> σ=0.25 (µm)<br><!-- End of picture text -->

kI/k-I=1 s0=1 µM s1=0.1 µM σ=0.25 (µm)<sup>-1</sup>

I(x)


<!-- Start of picture text -->
≡<br>σ D<br>−<br>k I /<br><!-- End of picture text -->

x

12

---

[← steady-state](08-steady-state.md) · [Up: contents](index.md) · [Remember: Perfect adaptation module →](10-remember-perfect-adaptation-module.md)
