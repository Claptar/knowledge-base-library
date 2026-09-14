---
title: Let's make three different sinusoids
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let's make three different sinusoids

**Source:** [`public/lectures/Lecture12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

freqs = [261.6, 329.7, 392] # Frequencies of the sinusoids
#freqs = [200, 400, 800]

tone = np.zeros(len(t2),)
for f in freqs:
    tone+= 1*np.cos(2*math.pi*f*t2) + 1*np.sin(2*math.pi*f*t2)

---

[← Let's make three different sinusoids](02-let-s-make-three-different-sinusoids.md) · [Up: contents](index.md) · [tone+= 10np.cos(2math.pift2) + 10np.sin(2math.pift2) →](04-tone-10np-cos-2math-pift2-10np-sin-2math-pift2.md)
