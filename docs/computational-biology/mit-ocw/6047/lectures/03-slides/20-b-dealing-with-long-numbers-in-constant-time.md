---
title: (b) Dealing with long numbers in constant time
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (b) Dealing with long numbers in constant time

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

new low-order 3 1 4 1 5 2 old high-order bit left shift digit **14,152 = ( 31,415 - 3 * 10,000 ) * 10 + 2 (mod 13)** = ( **7** -3* **3** )*10+2 **(mod 13)** 7 8 = **8 (mod 13)** **<u>Problem:</u>**

- To get O(n) time, need to perform each operation in O(1) time

- But if arguments are m-bit long (2<sup>m</sup> range), can take O(m) time

- Need to reduce number range to something more manageable **<u>Solution:</u>**

- <u>Hashing: Mapping keys</u> **_k_** from large universe U (of strings/numbers) into the ‘ **hash** ’ of each key **_h(k)_** , in smaller space [1..m]

- Many hash functions possible, w/ theoretical & practical properties:

   - Reproducibility: x=yh(x)=h(y) (hash of x always the same)

   - Uniform output distrib: x≠yP(h(x)=h(y))=1/m, for any input dist

**<u>New problem:</u>** Collisions

23

---

[← (a) Computing ts+1 based on ts in constant time](19-a-computing-ts-1-based-on-ts-in-constant-time.md) · [Up: contents](index.md) · [(c) Dealing with collisions, due to hashing →](21-c-dealing-with-collisions-due-to-hashing.md)
