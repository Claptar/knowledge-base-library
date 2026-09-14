---
title: (a) Computing ts+1 based on ts in constant time
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (a) Computing ts+1 based on ts in constant time

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
3 1 4 1 5 2<br><!-- End of picture text -->

**left shift new low-order digit**

old high-order bit

14,152 = (31,415 - **3 *** 10,000) *** 10** + **2**

**31,415**


**14,152**

14,152 =? function (31,415)

      - Middle digits of the number are already computed Shift them to the left 

      - • Remove the high-order bit

      - Add the low-order bit

- General case:

   - ts=T[s+1]2<sup>m-1</sup> +T[s+2]2<sup>m-2</sup> +…+T[s+m]2<sup>0</sup>


ts+1=T[s+2]2<sup>m-1</sup> +T[s+3]2<sup>m-2</sup> +…+T[s+m+1]2<sup>0</sup>

22

---

[← Karp-Rabin algorithm](18-karp-rabin-algorithm.md) · [Up: contents](index.md) · [(b) Dealing with long numbers in constant time →](20-b-dealing-with-long-numbers-in-constant-time.md)
