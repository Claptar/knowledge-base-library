---
title: teken een kernel density schatter
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-describe.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# teken een kernel density schatter

**Source:** [`chap-describe.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

plot(density(NHANES$BMI,na.rm=TRUE),main="",xlab="BMI")
```

<span id="fig:freqpoly"></span> <img src="Statistiek_2019_2020_files/figure-html/freqpoly-1.png" style="width:100.0%" alt="Histogram en kernel density schatter van BMI in de NHANES studie." />

Figuur 4.5: Histogram en kernel density schatter van BMI in de NHANES studie.

``` {.sourceCode .r}

---

[← teken een histogram](06-teken-een-histogram.md) · [Up: contents](index.md) · [argument na.rm=TRUE omdat er ontbrekende →](08-argument-na-rm-true-omdat-er-ontbrekende.md)
