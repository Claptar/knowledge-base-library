---
title: Lab 1 - Stat 153/248 - Solutions
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab 1 - Stat 153/248 - Solutions

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Split into 43 sections.

1. [Lab 1 - Stat 153/248 - Solutions](01-lab-1---stat-153-248---solutions.md)
2. [Set the random seed, this is so you will generate the same answers](02-set-the-random-seed-this-is-so-you-will-generate-the-same-an.md)
3. [each time (for example, when generating white noise)](03-each-time-for-example-when-generating-white-noise.md)
4. [Data from Time Series Analysis and Its Applications](04-data-from-time-series-analysis-and-its-applications.md)
5. [Let's print all the possible datasets we could load from the book](05-let-s-print-all-the-possible-datasets-we-could-load-from-the.md)
6. [These are functions named loadX](06-these-are-functions-named-loadx.md)
7. [Calculate the return](07-calculate-the-return.md)
8. [Moving average and filtering](08-moving-average-and-filtering.md)
9. [Plot the white noise and the moving average of the white noise on top](09-plot-the-white-noise-and-the-moving-average-of-the-white-noi.md)
10. [Lab1 solution Part 10 —](10-lab1-solution-part-10.md)
11. [other values of n](11-other-values-of-n.md)
12. [Autoregression](12-autoregression.md)
13. [Data as signal plus white noise](13-data-as-signal-plus-white-noise.md)
14. [Random walk](14-random-walk.md)
15. [Let's plot the random walk for nt=250 time points](15-let-s-plot-the-random-walk-for-nt-250-time-points.md)
16. [What do you notice about the data? Try running this cell a few times..](16-what-do-you-notice-about-the-data-try-running-this-cell-a-fe.md)
17. [Let's now look at what happens if we simulate 100 random walks for](17-let-s-now-look-at-what-happens-if-we-simulate-100-random-wal.md)
18. [1500 time points and plot them on top of one another.](18-1500-time-points-and-plot-them-on-top-of-one-another.md)
19. [What do you see about how the mean and variance](19-what-do-you-see-about-how-the-mean-and-variance.md)
20. [of the signals change over time? How does this differ from white noise?](20-of-the-signals-change-over-time-how-does-this-differ-from-wh.md)
21. [Random Walk with Drift](21-random-walk-with-drift.md)
22. [Now let's plot a single example of the random walk. Try running a few times](22-now-let-s-plot-a-single-example-of-the-random-walk-try-runni.md)
23. [with different parameters. How does the drift parameter influence what](23-with-different-parameters-how-does-the-drift-parameter-influ.md)
24. [you get? What about the properties of the white noise itself (if you go](24-you-get-what-about-the-properties-of-the-white-noise-itself.md)
25. [back...?)](25-back.md)
26. [Let's compare the mean and variance of the random](26-let-s-compare-the-mean-and-variance-of-the-random.md)
27. [walk with drift to our example above. Let's create](27-walk-with-drift-to-our-example-above-let-s-create.md)
28. [a matrix of random walks with drift - nwalks samples](28-a-matrix-of-random-walks-with-drift---nwalks-samples.md)
29. [and nt time points for drift drift.](29-and-nt-time-points-for-drift-drift.md)
30. [Now plot the mean and variance over time. How do these change compare](30-now-plot-the-mean-and-variance-over-time-how-do-these-change.md)
31. [to the other graphs you created?](31-to-the-other-graphs-you-created.md)
32. [Load some data from Shumway and Stoffer examples](32-load-some-data-from-shumway-and-stoffer-examples.md)
33. [Try applying the moving average to the DJIA data](33-try-applying-the-moving-average-to-the-djia-data.md)
34. [(where each sample is from one day). What happens](34-where-each-sample-is-from-one-day-what-happens.md)
35. [when you apply the average over a month, a year, etc?](35-when-you-apply-the-average-over-a-month-a-year-etc.md)
36. [Does this change how you might interpret the data?](36-does-this-change-how-you-might-interpret-the-data.md)
37. [Let's do the same thing with the speech data](37-let-s-do-the-same-thing-with-the-speech-data.md)
38. [Plot the smoothed speech data](38-plot-the-smoothed-speech-data.md)
39. [Try adding white noise to some of the datasets. If we just](39-try-adding-white-noise-to-some-of-the-datasets-if-we-just.md)
40. [add the white noise with the default variance, it may not affect our signal](40-add-the-white-noise-with-the-default-variance-it-may-not-aff.md)
41. [that much, so try changing the var parameter in our whitenoise](41-that-much-so-try-changing-the-var-parameter-in-our-whitenois.md)
42. [function](42-function.md)
43. [Extra: Try adding some drift to any of these datasets](43-extra-try-adding-some-drift-to-any-of-these-datasets.md)

---

[Up: contents](../../../index.md)
