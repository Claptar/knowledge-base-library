---
title: Apply to the dance track
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Apply to the dance track

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

CUTOFF_LP = 500   # Hz - this means we keep anything below this frequency for our lowpass filter (LP)
CUTOFF_HP = 3000  # Hz - this means we keep anything above this frequency for our highpass filter (HP)

y = y_dance
y_lp, sos_lp = apply_filter(y, sr, CUTOFF_LP, 'low')
y_hp, sos_hp = apply_filter(y, sr, CUTOFF_HP, 'high')

plot_filter_result(y_dance, y_lp, y_hp, sos_lp, sos_hp, sr,
                   CUTOFF_LP, CUTOFF_HP,
                   title='Filtered Dance Track')

print('Original:')
display(Audio(y, rate=sr))
print(f'Low-pass (< {CUTOFF_LP} Hz)')
display(Audio(y_lp, rate=sr))
print(f'High-pass (> {CUTOFF_HP} Hz)')
display(Audio(y_hp, rate=sr))
```

```
Original:
<IPython.lib.display.Audio object>
Low-pass (< 500 Hz)
<IPython.lib.display.Audio object>
High-pass (> 3000 Hz)
<IPython.lib.display.Audio object>
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← scipy.signal.sosfreqz — compute the filter's frequency response](27-scipy-signal-sosfreqz-compute-the-filter-s-frequency-respons.md) · [Up: contents](index.md) · [Apply to the slow track →](29-apply-to-the-slow-track.md)
