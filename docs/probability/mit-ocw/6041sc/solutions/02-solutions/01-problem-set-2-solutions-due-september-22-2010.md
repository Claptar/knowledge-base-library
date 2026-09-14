---
title: 'Problem Set 2: Solutions Due September 22, 2010'
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem Set 2: Solutions Due September 22, 2010

**Source:** `solutions/02-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. (a) The tree representation during the winter can be drawn as the following:


<!-- Start of picture text -->
Rain<br>0.8<br>The forecast is<br>"Rain"<br>p<br>0.2  No Rain<br>0.1  Rain<br>1-p<br>The forecast is<br>"No Rain"<br>0.9  No Rain<br><!-- End of picture text -->

Let A be the event that the forecast was “Rain,”

let B be the event that it rained, and

let p be the probability that the forecast says “Rain.” If it is in the winter, p = 0.7 and


Similarly, if it is in the summer, p = 0.2 and


- (b) Let C be the event that Victor is carrying an umbrella. Let D be the event that the forecast is no rain.

The tree diagram in this case is:


<!-- Start of picture text -->
0.5  Umbrella<br>Missed the forecast<br>0.2<br>0.5  No umbrella<br>Rain (umbrella)<br>0.8  p<br>Saw the forecast<br>1-p<br>No Rain (no umbrella)<br><!-- End of picture text -->


Page 1 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Therefore, P(C) = P(C | D) if and only if p = 0. However, p can only be 0.7 or 0.2, which implies the events C and D can never be independent, and this result does not depend on the season.

- (c) Let us first find the probability of rain if Victor missed the forecast.

P(actually rains | missed forecast) = (0.8)p + (0.1)(1 − p) = 0.1 + 0.7p.

Then, we can extend the tree in part (b) as follows:


<!-- Start of picture text -->
0.1+0.7p  Actually rain<br>0.5  Umbrella<br>0.9-0.7p  Actually no rain<br>Missed the forecast  Actually rain<br>0.1+0.7p<br>0.2<br>0.5  No umbrella<br>0.9-0.7p  Actually no rain<br>0.8  Actually rain<br>Rain (umbrella)<br>0.8  p<br>0.2  Actually no rain<br>Saw the forecast<br>1-p  0.1  Actually rain<br>No Rain (no umbrella)<br>0.9  Actually no rain<br><!-- End of picture text -->

Therefore, given that Victor is carrying an umbrella and it is not raining, we are looking at the two shaded cases.


In fall and winter, p = 0.7, so the probability is<sup><u>112</u></sup> 153 . In summer and spring, p = 0.2, so the probability is 278 .

---

[Up: contents](index.md) · [2. (a) i. No →](02-2-a-i-no.md)
