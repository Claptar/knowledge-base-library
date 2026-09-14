---
title: (c) Dealing with collisions, due to hashing
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (c) Dealing with collisions, due to hashing

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
T=  2 3 5 9 0 2 3 1 4 1  5 2  6 7 3 9 9 2 1<br>8 9 3 11 0 1  7  8  4 5 10 11 7 9 11<br>valid match  spurious hit<br><!-- End of picture text -->

- Consequences of (mod p) ‘hashing’ – Good:  Enable fast computation (use small numbers)

   - Bad:  Leads to spurious hits (collisions)

- Dealing with the bad:

   1. Verify that a **<u>hit</u>** correspond to valid **<u>match</u>**

      -  re-compute equality for entire string (not just hash)

   2. Avoid worst-case behavior of many collisions w/ bad m

      -  Choose **random m**

- Algorithm and its analysis becomes more complex: 1. Compute expected run time, include expected cost of verification

   2. Show probability of spurious hits is small, expected run time is linear

24

---

[← (b) Dealing with long numbers in constant time](20-b-dealing-with-long-numbers-in-constant-time.md) · [Up: contents](index.md) · [Karp-Rabin algorithm: Putting it all together →](22-karp-rabin-algorithm-putting-it-all-together.md)
