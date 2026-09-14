---
title: Plot predictions vs. actual response
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot predictions vs. actual response

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print("Prediction matrix shape: ", pred.shape)
print("Response matrix shape: ", ytest.shape)

fig = plt.figure(figsize=(10,5))
plt.subplot(nelecs+1,1,1)
plt.imshow(xtestd[ntimes_start:ntimes_start+ntimes,:nfeats].T, aspect='auto', cmap=cm.magma, interpolation='nearest')
xticks = np.arange(0, len(times), step=500)
plt.gca().set_xticks(xticks)
plt.gca().set_xticklabels([int(times[x]) for x in xticks])
plt.gca().invert_yaxis()

---

[← How much time to show?](21-how-much-time-to-show.md) · [Up: contents](index.md) · [Loop through the best channels →](23-loop-through-the-best-channels.md)
