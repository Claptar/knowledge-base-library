---
title: 04 notes
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/04-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 04 notes

**Source:** `lectures/04-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```
Summary Lecture 3
```

## **`L4: Cooperativity & introduction`** λ **`phage model`**

λ phage model (Hasty et al.) as example for applying mass action law.


<!-- Start of picture text -->
K<br>K1 ⎯ 1<br>2X ←⎯→ X<br>2<br>λ λ<br>λ<br>K2 K<br>λ ⎯ 2<br>D + X ←⎯→ DX<br>2 2<br>most important<br>λ λ fast<br>K<br>*<br>OR2 OR3 step in D + X ←⎯→⎯ 3 DX<br>modeling !! 2 2<br>K<br>λ λ ⎯ 4<br>DX + X ←⎯→ DX DX<br>2 2 2 2<br>OR2 OR3<br>k<br>⎯ ⎯ t<br>DX + P ⎯→ DX + P + nX<br>2 2<br>λ λ λ λ<br>k<br>OR2 OR3 most important ⎯ ⎯ d slow<br>X ⎯→ A<br>step in<br>modeling !!<br><!-- End of picture text -->


<!-- Start of picture text -->
math<br><!-- End of picture text -->

```
biology
```


<!-- Start of picture text -->
2<br>dx αx<br>K = − γx + 1<br>2X ←⎯→⎯ 1 X dt 2 4<br>2 1 + (1 + σ )x + σ x<br>1 2<br>K K<br>D + X ←⎯→⎯ 2 DX σ = 3<br>2 2 1 K<br>2 relative binding<br>mass action<br>constants<br>K ⎯ 3 * K4<br>D + X ←⎯→ DX σ =<br>2 2 2<br>K<br>2<br>K<br>⎯ 4 nk p d<br>DX2 + X2 ←⎯→ DX2DX2 α = t 0 T ~ synthesis/basal<br>r rate<br>k<br>⎯ ⎯ t k<br>DX + P ⎯→ DX + P + nX<br>2 2 γ = d ~ degradation/basal<br>k r K1K2 rate<br>⎯ ⎯ d<br>X ⎯→ A<br><!-- End of picture text -->

graphical stability analysis

How to experimentally verify these ideas ?

Synthetic Biology Build your own designed network ‘from scratch’ and test your model

<u>Examples for synthetic genetic switches:</u> Isaacs _et al._ Prediction and measurement of an autoregulatory genetic module. PNAS **100** , 7714 (2003) Gardner _et al._ Construction of a genetic toggle switch in Escherichia coli. Nature **403** , 399 (2000)

# **First a short intro on ‘Genetic Engineering’**

**Toolbox of the genetic engineer:**

1. Restriction enzymes

2. Plasmids

3. PCR (Polymerase Chain Reaction)

4. Fluorescent proteins

---

[Up: contents](../index.md)
