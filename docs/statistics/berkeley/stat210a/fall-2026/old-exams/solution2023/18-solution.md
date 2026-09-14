---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For this, we have<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X n − µ_ ) _⇒ N_ (0 _, σ_<sup>2</sup> <u>) and</u><sup>_√_</sup> _<u>n</u>_ <u>(</u> _Y n − ν_ ) _⇒ N_ (0 _, τ_<sup>2</sup> ), so we can apply the delta method to<sup>_√_</sup> _<u>n</u>_ �� _XY nn_ � _−_ � _µν_ �<sup>�</sup> _⇒ N_ 2(0 _, D_ ) for _D_ = 0 . The function is _f_ ( _x, y_ ) = ( _x/y_ )<sup>2</sup> , whose gradient (for _y̸_ = 0) is 0 _τ_<sup>2</sup> � _σ_ 2 � _∇f_ ( _x, y_ ) = (2 _x/y_<sup>2</sup> _, −_ 2 _x_<sup>2</sup> _/y_<sup>3</sup> ). As a result we have


where


**Grading note:** If you missed that we need _ν >_ 0 in (b) I didn’t take points off again. If you _didn’t_ miss it in (b), then I assumed you knew it in (c). So this detail played no role in grading this part.

- (d) (*) If _µ_ = _ν_ = 0, give the asymptotic distribution of _T_ ( _X, Y_ ) as _n →∞_ , normalized appropriately if necessary. Justify your answer.

---

[← Solution](17-solution.md) · [Up: contents](index.md) · [Solution →](19-solution.md)
