---
title: 'Computing Fibonacci numbers: Bottom up'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Computing Fibonacci numbers: Bottom up

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### • Bottom up approach

– Python code

fib_table F[1] 1 F[2] 1 F[3] 2 F[4] 3 F[5] 5 F[6] 8 F[7] 13 F[8] 21 F[9] 34 F[10] 55 F[11] 89 F[12] **?**

```
def fibonacci(n):
fib_table[1] = 1
fib_table[2] = 1
for i in range(3,n+1):
      fib_table[i] = fib_table[i-1]+fib_table[i-2]
return fib_table[n]
```

– Analysis: T(n) = O(n)


22

---

[← Computing Fibonacci numbers: Top down](17-computing-fibonacci-numbers-top-down.md) · [Up: contents](index.md) · [Lessons from iterative Fibonacci algorithm →](19-lessons-from-iterative-fibonacci-algorithm.md)
