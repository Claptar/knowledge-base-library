---
title: Lab 7 - Power Spectral Analysis
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab 7 - Power Spectral Analysis

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Split into 32 sections.

1. [Lab 7 - Power Spectral Analysis](01-lab-7---power-spectral-analysis.md)
2. [Create a test signal: sum of two sinusoids + noise](02-create-a-test-signal-sum-of-two-sinusoids-noise.md)
3. [Compute using your function](03-compute-using-your-function.md)
4. [Compute using numpy (adjust for our convention)](04-compute-using-numpy-adjust-for-our-convention.md)
5. [numpy uses t=0,...,n-1 and no 1/sqrt(n) normalization](05-numpy-uses-t-0-n-1-and-no-1-sqrt-n-normalization.md)
6. [Our convention uses t=1,...,n and 1/sqrt(n)](06-our-convention-uses-t-1-n-and-1-sqrt-n.md)
7. [Lab7 solution Part 07 —](07-lab7-solution-part-07.md)
8. [Check they match](08-check-they-match.md)
9. [Compute the scaled periodogram from our DFT](09-compute-the-scaled-periodogram-from-our-dft.md)
10. [TODO: Fill in the periodogram formula](10-todo-fill-in-the-periodogram-formula.md)
11. [Only plot up to the Nyquist frequency (j = 0, ..., n/2)](11-only-plot-up-to-the-nyquist-frequency-j-0-n-2.md)
12. [Compare with scipy periodogram (fs=1 so frequencies are in cycles/sample)](12-compare-with-scipy-periodogram-fs-1-so-frequencies-are-in-cy.md)
13. [Note: scipy uses a slightly different normalization. The shapes should match](13-note-scipy-uses-a-slightly-different-normalization-the-shape.md)
14. [even if the scale differs. What normalization does scipy use?](14-even-if-the-scale-differs-what-normalization-does-scipy-use.md)
15. [TODO: Verify that |d(j/n)|^2 = |d(1-j/n)|^2 for our test signal](15-todo-verify-that-d-j-n-2-d-1-j-n-2-for-our-test-signal.md)
16. [Hint: d(1 - j/n) corresponds to index (n - j) in the array](16-hint-d-1---j-n-corresponds-to-index-n---j-in-the-array.md)
17. [Generate white noise](17-generate-white-noise.md)
18. [Compute the periodogram](18-compute-the-periodogram.md)
19. [Plot periodogram vs. theoretical spectrum](19-plot-periodogram-vs-theoretical-spectrum.md)
20. [TODO: Plot the theoretical spectral density as a horizontal line](20-todo-plot-the-theoretical-spectral-density-as-a-horizontal-l.md)
21. [Hint: For white noise, f(omega) = sigmaw^2](21-hint-for-white-noise-f-omega-sigmaw-2.md)
22. [But note scipy's periodogram normalization, so you may need to adjust by a factor.](22-but-note-scipy-s-periodogram-normalization-so-you-may-need-t.md)
23. [The total area under the periodogram should equal the variance.](23-the-total-area-under-the-periodogram-should-equal-the-varian.md)
24. [Note that scipy.signal.periodogram returns a one-sided spectrum by default (only [0,1/2]),](24-note-that-scipy-signal-periodogram-returns-a-one-sided-spect.md)
25. [which folds the negative-frequency power onto the positive side,](25-which-folds-the-negative-frequency-power-onto-the-positive-s.md)
26. [effectively doubling the values.](26-effectively-doubling-the-values.md)
27. [Signal: slow sinusoid + noise](27-signal-slow-sinusoid-noise.md)
28. [Apply a moving average filter of order m](28-apply-a-moving-average-filter-of-order-m.md)
29. [TODO: Compute the filtered signal using np.convolve with weights 1/m](29-todo-compute-the-filtered-signal-using-np-convolve-with-weig.md)
30. [Plot time domain](30-plot-time-domain.md)
31. [Plot frequency domain](31-plot-frequency-domain.md)
32. [Simulate many periodograms from white noise and overlay them](32-simulate-many-periodograms-from-white-noise-and-overlay-them.md)

---

[Up: contents](../../../index.md)
