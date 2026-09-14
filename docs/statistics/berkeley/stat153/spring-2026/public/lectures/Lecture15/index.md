---
title: 'Lecture 15: Time-Frequency Analysis with Music'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 15: Time-Frequency Analysis with Music

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Split into 32 sections.

1. [Lecture 15: Time-Frequency Analysis with Music](01-lecture-15-time-frequency-analysis-with-music.md)
2. [Quick poll - Guess the category](02-quick-poll---guess-the-category.md)
3. [Load audio here](03-load-audio-here.md)
4. [Change these paths if you have other sounds you want to use](04-change-these-paths-if-you-have-other-sounds-you-want-to-use.md)
5. [Step 1: Waveform only - what do we get from this?](05-step-1-waveform-only---what-do-we-get-from-this.md)
6. [Step 2: Periodogram - can we tell which notes are in the song?](06-step-2-periodogram---can-we-tell-which-notes-are-in-the-song.md)
7. [Could you sing the song from this or identify the melody?](07-could-you-sing-the-song-from-this-or-identify-the-melody.md)
8. [Step 3: Spectrogram](08-step-3-spectrogram.md)
9. [This is scipy.signal.spectrogram — periodogram on a sliding window.](09-this-is-scipy-signal-spectrogram-periodogram-on-a-sliding-wi.md)
10. [Let's look at how nperseg affects both ∆t and ∆f](10-let-s-look-at-how-nperseg-affects-both-t-and-f.md)
11. [This is the same Δf = fs/N relationship from when we discussed](11-this-is-the-same-δf-fs-n-relationship-from-when-we-discussed.md)
12. [periodogram frequency resolution.](12-periodogram-frequency-resolution.md)
13. [We will use the following functions](13-we-will-use-the-following-functions.md)
14. [scipy.signal.periodogram — single FFT of entire signal](14-scipy-signal-periodogram-single-fft-of-entire-signal.md)
15. [scipy.signal.welch — average periodograms over overlapping segments](15-scipy-signal-welch-average-periodograms-over-overlapping-seg.md)
16. [3a. Raw periodogram](16-3a-raw-periodogram.md)
17. [3b. Welch with different segment lengths](17-3b-welch-with-different-segment-lengths.md)
18. [--- Overlay raw periodograms from different chunks ---](18-----overlay-raw-periodograms-from-different-chunks.md)
19. [This is the key visualization: each chunk gives a DIFFERENT periodogram,](19-this-is-the-key-visualization-each-chunk-gives-a-different-p.md)
20. [even though the signal is approximately stationary.](20-even-though-the-signal-is-approximately-stationary.md)
21. [Welch averages over these to reduce variance.](21-welch-averages-over-these-to-reduce-variance.md)
22. [Welch does this averaging for us](22-welch-does-this-averaging-for-us.md)
23. [Filter design and application](23-filter-design-and-application.md)
24. [First run this cell to get the functions we need to create and apply filters to the data](24-first-run-this-cell-to-get-the-functions-we-need-to-create-a.md)
25. [scipy.signal.butter — design a Butterworth filter](25-scipy-signal-butter-design-a-butterworth-filter.md)
26. [scipy.signal.sosfiltfilt — apply it (zero-phase, so no time shift)](26-scipy-signal-sosfiltfilt-apply-it-zero-phase-so-no-time-shif.md)
27. [scipy.signal.sosfreqz — compute the filter's frequency response](27-scipy-signal-sosfreqz-compute-the-filter-s-frequency-respons.md)
28. [Apply to the dance track](28-apply-to-the-dance-track.md)
29. [Apply to the slow track](29-apply-to-the-slow-track.md)
30. [statsmodels.tsa.stattools.acf computes the sample autocorrelation function.](30-statsmodels-tsa-stattools-acf-computes-the-sample-autocorrel.md)
31. [Build a spectrogram from scratch](31-build-a-spectrogram-from-scratch.md)
32. [Compare to scipy](32-compare-to-scipy.md)

---

[Up: contents](../../../index.md)
