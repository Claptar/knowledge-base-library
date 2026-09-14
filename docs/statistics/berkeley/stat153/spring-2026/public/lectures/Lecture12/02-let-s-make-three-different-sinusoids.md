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

f = [6,10,39] # Frequencies of the sinusoids
x1 = 2*np.cos(2*math.pi*f[0]*t) + 3*np.sin(2*math.pi*f[0]*t)
x2 = 4*np.cos(2*math.pi*f[1]*t) + 5*np.sin(2*math.pi*f[1]*t)
x3 = 6*np.cos(2*math.pi*f[2]*t) +7*np.sin(2*math.pi*f[2]*t)

plt.figure(figsize=(5,3))
plt.subplot(2,2,1)
plt.plot(t,x1)
plt.axhline(-np.sqrt(2**2+3**2),color='r')
plt.axhline(np.sqrt(2**2+3**2),color='r')
plt.title(f'f={f[0]}')
plt.subplot(2,2,2)
plt.plot(t,x2)
plt.title(f'f={f[1]}')
plt.subplot(2,2,3)
plt.plot(t,x3)
plt.title(f'f={f[2]}')
plt.xlabel('Time (s)')
plt.ylabel('Amp')
plt.subplot(2,2,4)
plt.plot(t,x1+x2+x3)
plt.axhline(np.sqrt(2**2+3**2)+np.sqrt(4**2+5**2)+np.sqrt(6**2+7**2), color='r')
plt.title('x1+x2+x3')
plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

Note that the amplitudes of each of these series are defined by $\sqrt{U_1^2+U_2^2}$. For the sum of sinusoids, it's theoretical maximum amplitude is given by the sum of the amplitudes of each of the components, but this maximum will only be reached if the peaks of the sinusoids are in phase (which does not always happen if they aren't harmonically related - meaning they aren't integer multiples of some underlying frequency).

```python
from IPython.display import Audio, display

fs2 = 44100 # sampling rate
t2 = np.arange(0, 1, 1/fs2)

---

[← Stat153/248 Lecture 12 - Power spectral analysis](01-stat153-248-lecture-12---power-spectral-analysis.md) · [Up: contents](index.md) · [Let's make three different sinusoids →](03-let-s-make-three-different-sinusoids.md)
