---
title: 2. find stability matrix (Jacobian)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/17-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. find stability matrix (Jacobian)

**Source:** `lectures/17-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
'<br>−<br>⎡ σ σ D σ ⎤<br>1 1 1<br>⎢ ' σ 2 e 0 ' 2 + σ 2 d ⎥<br>1 + σ e + σ e<br>1 1( 1 )<br>⎢ ' ⎥<br>σ σ D σ<br>⎢ 1 1 1 ⎥<br>− − −<br>' σ 2 e 0 ' 2 σ 2 d<br>⎢ ⎥<br>1 + σ e + σ e<br>1 1( 1 )<br>=<br>A ⎢ ' ⎥<br>σ e σ σ<br>⎢− 4 4 − − 4 ⎥<br>' 2 σ 3 E 0 σ 3 D '<br>⎢ + σ D 1 + σ D ⎥<br>1( 4 ) 4<br>'<br>⎢ ⎥<br>σ e σ σ<br>4 4 4<br>−<br>⎢+ ' 2 + σ 3 E 0 σ 3 D ' ⎥<br>⎢⎣ 1( + σ 4 D ) 1 + σ 4 D ⎥⎦<br><!-- End of picture text -->

23

---

[← stability analysis](20-stability-analysis.md) · [Up: contents](index.md) · [3. test stability of fluctuations around homogeneous solution →](22-3-test-stability-of-fluctuations-around-homogeneous-solution.md)
