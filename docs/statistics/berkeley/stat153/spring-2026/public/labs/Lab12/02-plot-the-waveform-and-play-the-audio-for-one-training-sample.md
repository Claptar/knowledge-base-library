---
title: Plot the waveform and play the audio for one training sample
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the waveform and play the audio for one training sample

**Source:** [`public/labs/Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Set the x-axis values so that they show seconds.

```python
# plot the waveform for one example (e.g., sc_training[150])

plt.figure(figsize=(5,2))
print(sc_training[150][0])
plt.plot(sc_training[150][0].t().numpy())
plt.xlabel("Time (seconds)")
plt.axis("on")

# play the audio
ipd.Audio(sc_training[150][0], rate=16000)
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Define model →](03-define-model.md)
