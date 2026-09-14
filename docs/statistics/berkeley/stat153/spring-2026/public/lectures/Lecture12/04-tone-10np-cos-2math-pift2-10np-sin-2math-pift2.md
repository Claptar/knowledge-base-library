---
title: tone+= 10np.cos(2math.pift2) + 10np.sin(2math.pift2)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# tone+= 10np.cos(2math.pift2) + 10np.sin(2math.pift2)

**Source:** [`public/lectures/Lecture12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(t2,tone)
plt.gca().set_xlim([0,0.01])
display(Audio(tone, rate=fs2, autoplay=False))
```

```
<IPython.lib.display.Audio object>
```

*(1 figure omitted — see the original notebook.)*

```python
from scipy.signal import periodogram

fs = 100 # sampling rate
t = np.arange(0, 1, 1/fs)

---

[← Let's make three different sinusoids](03-let-s-make-three-different-sinusoids.md) · [Up: contents](index.md) · [Let's make three different sinusoids →](05-let-s-make-three-different-sinusoids.md)
