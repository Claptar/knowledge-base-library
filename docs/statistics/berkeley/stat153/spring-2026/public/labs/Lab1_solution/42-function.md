---
title: function
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# function

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

noise_variance = np.var(speech_data['Value'])
plt.figure()
plt.subplot(2,1,1)
plt.plot(speech_data['Value'])
plt.subplot(2,1,2)
plt.plot(speech_data['Value'] + white_noise(len(speech_data['Value']), var=noise_variance*2))
```

```
[<matplotlib.lines.Line2D at 0x148dca6e0>]
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← that much, so try changing the var parameter in our whitenoise](41-that-much-so-try-changing-the-var-parameter-in-our-whitenois.md) · [Up: contents](index.md) · [Extra: Try adding some drift to any of these datasets →](43-extra-try-adding-some-drift-to-any-of-these-datasets.md)
