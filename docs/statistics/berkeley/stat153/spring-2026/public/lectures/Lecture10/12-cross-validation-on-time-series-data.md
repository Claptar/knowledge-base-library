---
title: Cross-validation on time series data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Cross-validation on time series data

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

As we discussed, it's often best to try and predict new data based on past observations rather than "cheating" by using future data to predict the past. So, choosing a way of splitting our data into training and testing should be done thoughtfully if we're working with time series.

Why can't we just split our data randomly into training and test data? Let's try by getting 80% of our data as the training set and the remaining 20% as test and then think about why this is problematic.

```python
mask = np.zeros(len(y), dtype=bool)
mask[np.random.choice(len(y), size=int(0.8*len(y)), replace=False)] = True

---

[← use t2 as our new time observations, then calculate our new estimate of y](11-use-t2-as-our-new-time-observations-then-calculate-our-new-e.md) · [Up: contents](index.md) · [Lecture 10 — Part 13 — →](13-lecture-10-part-13.md)
