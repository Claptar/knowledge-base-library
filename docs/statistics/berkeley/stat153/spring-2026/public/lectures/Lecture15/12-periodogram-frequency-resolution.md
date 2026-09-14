---
title: periodogram frequency resolution.
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# periodogram frequency resolution.

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print('Time-Frequency Resolution Tradeoff')
print('=' * 55)
print(f'{"nperseg":>10} | {"Δt (s)":>10} | {"Δf (Hz)":>10} | {"Δt × Δf":>10}')
print('-' * 55)
for nps in [128, 2048, 8192]:
    dt = nps / sr     # time resolution in ms
    df = sr / nps            # freq resolution in Hz
    print(f'{nps:>10} | {dt:>10.3f} | {df:>10.1f} | {dt*df:>10.2f}')

print()
print('Δt × Δf = 1 for all segment lengths.')
print('The periodogram is the extreme: N = len(signal) → best Δf, but Δt = entire signal.')
```

```
Time-Frequency Resolution Tradeoff
=======================================================
   nperseg |     Δt (s) |    Δf (Hz) |    Δt × Δf
-------------------------------------------------------
       128 |      0.006 |      172.3 |       1.00
      2048 |      0.093 |       10.8 |       1.00
      8192 |      0.372 |        2.7 |       1.00

Δt × Δf = 1 for all segment lengths.
The periodogram is the extreme: N = len(signal) → best Δf, but Δt = entire signal.
```

### Connection to prior datasets

Remember when we discussed `periodogram(sunspots, fs=2.0)` — the frequency resolution was $\Delta f = 2/N$ cycles per year. The whole signal gave us fine frequency resolution. But we lost all information about *when* the 11-year cycle was strong or weak.

The spectrogram is just a periodogram computed on a **sliding window**. A shorter window means we have better time resolution but coarser frequency resolution. The periodogram is the limit case: window = entire signal.

## Welch vs. Raw Periodogram

Now we will show the same `periodogram` vs. `welch` comparison we've done in class, but now on music instead of simulated data.

```python

---

[← This is the same Δf = fs/N relationship from when we discussed](11-this-is-the-same-δf-fs-n-relationship-from-when-we-discussed.md) · [Up: contents](index.md) · [We will use the following functions →](13-we-will-use-the-following-functions.md)
