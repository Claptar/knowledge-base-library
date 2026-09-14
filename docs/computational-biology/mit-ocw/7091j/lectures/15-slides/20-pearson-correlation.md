---
title: Pearson Correlation
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Pearson Correlation

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Xi,j = Expression of gene _i_ in condition _j_

- Zi = z-score of gene _i_ one experiment:

- Pearson correlation


over all experiments

   - from +1 (perfect correlation) to -1 (anti-correlated)

- Distance = 1-rA,B


34


<!-- Start of picture text -->
3.5  1.5<br>3<br>1<br>2.5<br>0.5<br>2<br>0<br>0  1  2  3  4  5  6<br>1.5<br>-0.5<br>A<br>ZA<br>1<br>C  -1<br>ZC<br>0.5<br>-1.5<br>0<br>0  1  2  3  4  5  6  -2<br>Z-score<br>Expression<br><!-- End of picture text -->


35


<!-- Start of picture text -->
3.5<br>2<br>ZA<br>3<br>1.5<br>ZB<br>A<br>ZC<br>2.5<br>1<br>B<br>2  C  0.5<br>1.5  0<br>0  1  2  3  4  5  6<br>1  -0.5<br>-1<br>0.5<br>-1.5<br>0<br>0  1  2  3  4  5  6<br>-2<br>RA,B= -0.01<br>RA,C= 0.999<br>RB,C= -0.03<br>Z-score<br>Expression<br><!-- End of picture text -->

36


<!-- Start of picture text -->
4  2<br>ZA<br>3  1.5<br>ZB<br>ZD<br>2  1<br>1  0.5<br>0  0<br>0  1  2  3  4  5  6  0  1  2  3  4  5  6<br>-1  A  -0.5<br>B<br>-2  -1<br>D<br>-3  -1.5<br>-4  -2<br>RA,B= -0.01<br>RA,D= -1.0<br>RB,D= 0.007<br>Z-score<br>Expression<br><!-- End of picture text -->

37

---

[← Pearson Correlation](19-pearson-correlation.md) · [Up: contents](index.md) · [Distance Metrics →](21-distance-metrics.md)
