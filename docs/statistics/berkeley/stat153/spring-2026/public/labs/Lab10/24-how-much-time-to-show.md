---
title: How much time to show?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# How much time to show?

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ntimes = int(30*fs) # Show 30 seconds of time
ntimes_start = int(5*fs)  # Start 5 seconds in since there is a lot of silence at the beginning
times = np.arange(ntimes_start, ntimes_start+ntimes)/fs

---

[← Plot a line at the maximum alpha. This should be in the middle](23-plot-a-line-at-the-maximum-alpha-this-should-be-in-the-middl.md) · [Up: contents](index.md) · [Plot predictions vs. actual response →](25-plot-predictions-vs-actual-response.md)
