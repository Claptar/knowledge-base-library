---
title: Computation of the location quotient
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/clm.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/ps/clm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Computation of the location quotient

**Source:** [`ps/clm.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/clm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The Cohort Location Model described above theorises that younger households are more likely to locate near the city centre(s) while older households are more likely to locate near the fringe. As overall household counts are not evenly distributed by the age of the householder, simple counts of households at each location will not result in fair comparisons. Therefore, to evaluate the location choices of a given age of a household, we computed location quotients for each age group at each 1/100 of the standardised distance. Location quotients are particularly useful in this regard because they allow for differences in the underlying distribution of households by age to be held constant while comparison across distance – the focus of this research – are made. Location quotients are calculated as:


where HH is the total count of households, i is the 10-year cohort of the head of household and j is the standardised distance rounded to the nearest 0.01.

9

Estiri and Krause


Figure 2. Centres’ location and distance computation for the Atlanta-Sandy Springs-Marietta CBSA.

A location quotient of 1 indicates that a given age cohort is represented at a given distance in the same proportion as that age cohort is represented in the entire metropolitan area. Location quotients (LQs) less (greater) than 1 indicate under(over)-representation in a given area or at a given distance.

To test the applicability of the theoretical model developed above, we calculated location quotients for each age group at each of the 100 standardised distances. We then plotted these location quotients. Owing to the high variability at some distances caused by low sample sizes of households, we smoothed the overall trend lines using a locally weighted regression technique (LOWESS or LOESS, with a smoothing factor of 0.1). The LOESS-smoothed lines present a more reasonable trend regarding the changes in the frequency of household location by age over distance. Location quotient

analyses are performed on the combined 50 CBSA data set as well as individually on each CBSA. The results of these analyses are discussed below.

---

[← Computation of the distance variable](11-computation-of-the-distance-variable.md) · [Up: contents](index.md) · [Results →](13-results.md)
