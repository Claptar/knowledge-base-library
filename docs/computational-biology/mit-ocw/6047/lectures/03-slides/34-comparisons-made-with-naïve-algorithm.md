---
title: Comparisons made with naïve algorithm
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Comparisons made with naïve algorithm

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<mark>b a a b a c a b</mark> s=0 <mark>a b a</mark>

- Worst case running time:

   - Test every position

<mark>b a a b a c a b</mark> s=1 <mark>a b a</mark>

<mark>b a a b a c a b</mark> s=2 <mark>a b a</mark>

   - P=aaaa, T=aaaaaaaaaaa

- Best case running time: – Test only first position – P=bbbb, T=aaaaaaaaaaa

<mark>b a a b a c a b</mark> s=3 <mark>a b a</mark>

<mark>b a a b a c a b</mark> s=4 <mark>a b a</mark>

<mark>b a a b a c a b a b a</mark>

s=5

Can we do better?

38

**Key insight:  make bigger shifts!**

• If all characters in the pattern are the **same** :

<mark>? ? ? ? ? ? ? ? ? ? a a a a</mark>

<mark>a a x ? ? ? ? ? ? ? a a a a</mark>

<mark>? ? ? x ? ? ? ? ? ? a a a a</mark>

Information gathered at every comparison

<mark>? ? ? ? a a a a ? ? a a a a ? ? ? ? ? ? a a a ? a a a a</mark>

Knowledge of the internal structure of P

Number of comparisons:  O(n)

39

---

[← The naïve string-matching algorithm](33-the-naïve-string-matching-algorithm.md) · [Up: contents](index.md) · [Key insight: make bigger shifts! →](35-key-insight-make-bigger-shifts.md)
