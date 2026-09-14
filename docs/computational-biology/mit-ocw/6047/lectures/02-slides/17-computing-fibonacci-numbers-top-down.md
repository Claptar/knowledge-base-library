---
title: 'Computing Fibonacci numbers: Top down'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Computing Fibonacci numbers: Top down

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Fibonacci numbers are defined recursively:

   - Python code

```
def fibonacci(n):
if n==1 or n==2: return 1
return fibonacci(n-1) + fibonacci(n-2)
```

- Goal:  Compute n<sup>th</sup> Fibonacci number. – F(0)=1, F(1)=1, F(n)=F(n-1)+F(n-2)

   - 1,1,2,3,5,8,13,21,34,55,89,144,233,377,…

- Analysis:

   - T(n) = T(n-1) + T(n-2) = (…) = _O(2_<sup>_n_</sup> _)_


21

---

[← Fibonacci numbers are ubiquitous in nature](16-fibonacci-numbers-are-ubiquitous-in-nature.md) · [Up: contents](index.md) · [Computing Fibonacci numbers: Bottom up →](18-computing-fibonacci-numbers-bottom-up.md)
