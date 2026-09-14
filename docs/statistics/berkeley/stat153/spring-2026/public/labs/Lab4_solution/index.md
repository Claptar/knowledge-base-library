---
title: Lab 4
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab 4

**Source:** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Split into 39 sections.

1. [Lab 4](01-lab-4.md)
2. [summarydf has one row per observation and shows the number of taps for that observation](02-summarydf-has-one-row-per-observation-and-shows-the-number-o.md)
3. [dfall has all of the data from everyone, including all the individual taps, as well](03-dfall-has-all-of-the-data-from-everyone-including-all-the-in.md)
4. [as repeated metadata about the person ('subj') who completed the task](04-as-repeated-metadata-about-the-person-subj-who-completed-the.md)
5. [For example, the first several rows are from subj 0, who is left handed and used](05-for-example-the-first-several-rows-are-from-subj-0-who-is-le.md)
6. [their left index finger for the first part of the task](06-their-left-index-finger-for-the-first-part-of-the-task.md)
7. [dfbins is the binned data when we use 10 second bins -- this is very](07-dfbins-is-the-binned-data-when-we-use-10-second-bins----this.md)
8. [much an oversimplification of the trend over time, but for now](08-much-an-oversimplification-of-the-trend-over-time-but-for-no.md)
9. [is simple to look at](09-is-simple-to-look-at.md)
10. [For example, the first row is for subj 0, timebin 0 corresponds to the](10-for-example-the-first-row-is-for-subj-0-timebin-0-correspond.md)
11. [first 10 seconds of their attempt, and they had 66 taps in that time bin.](11-first-10-seconds-of-their-attempt-and-they-had-66-taps-in-th.md)
12. [In the second 10 seconds, they had 54 taps.](12-in-the-second-10-seconds-they-had-54-taps.md)
13. [googleform has additional data about whether they slept enough, whether](13-googleform-has-additional-data-about-whether-they-slept-enou.md)
14. [they play video games more than 10 hrs a week, and how many years they](14-they-play-video-games-more-than-10-hrs-a-week-and-how-many-y.md)
15. [played a sport. Remember this doesn't fully overlap with our other dataset](15-played-a-sport-remember-this-doesn-t-fully-overlap-with-our.md)
16. [and has a different number of rows, though we could try to match them up](16-and-has-a-different-number-of-rows-though-we-could-try-to-ma.md)
17. [later](17-later.md)
18. [Using seaborn to explore our dataset](18-using-seaborn-to-explore-our-dataset.md)
19. [Fitting regression models](19-fitting-regression-models.md)
20. [What if we just wanted to fit whether taps depend only on using dominant hand? Note](20-what-if-we-just-wanted-to-fit-whether-taps-depend-only-on-us.md)
21. [the difference in Adj. R-squared compared to the last example.](21-the-difference-in-adj-r-squared-compared-to-the-last-example.md)
22. [FILL IN](22-fill-in.md)
23. [Plots to look at balance within our data](23-plots-to-look-at-balance-within-our-data.md)
24. [Google form data](24-google-form-data.md)
25. [Investigate other model effects](25-investigate-other-model-effects.md)
26. [can you make a boxplot showing whether using your pinky vs your index finger](26-can-you-make-a-boxplot-showing-whether-using-your-pinky-vs-y.md)
27. [results in more taps for gamers vs. non gamers? Your data should be colored](27-results-in-more-taps-for-gamers-vs-non-gamers-your-data-shou.md)
28. [by gamer vs. nongamer.](28-by-gamer-vs-nongamer.md)
29. [Let's show the same data (ntaps) but change which is x and which is hue.](29-let-s-show-the-same-data-ntaps-but-change-which-is-x-and-whi.md)
30. [(Let's make the finger the color this time)](30-let-s-make-the-finger-the-color-this-time.md)
31. [Does this make you interpret the data differently or think about it](31-does-this-make-you-interpret-the-data-differently-or-think-a.md)
32. [differently? Do the two graphs make certain comparisons more obvious?](32-differently-do-the-two-graphs-make-certain-comparisons-more.md)
33. [Look at the data as a time series](33-look-at-the-data-as-a-time-series.md)
34. [Examples of how taps change as a function of time bin](34-examples-of-how-taps-change-as-a-function-of-time-bin.md)
35. [Fitting models](35-fitting-models.md)
36. [Try the regressions again but using a different binning ... what do you notice?](36-try-the-regressions-again-but-using-a-different-binning-what.md)
37. [binning of 2 seconds, 5 seconds, something else?](37-binning-of-2-seconds-5-seconds-something-else.md)
38. [What assumptions are we making?](38-what-assumptions-are-we-making.md)
39. [Relating to other topics](39-relating-to-other-topics.md)

---

[Up: contents](../../../index.md)
