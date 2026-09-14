---
title: DMH Voorbeeld
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-KruskalWallis.Rmd
source_file: sources/gtpb-psls20/theory/09-NonparametericStatistics-KruskalWallis.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# DMH Voorbeeld

**Source:** [`theory/09-NonparametericStatistics-KruskalWallis.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-KruskalWallis.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Assess genotoxicity of 1,2-dimethylhydrazine dihydrochloride (DMH)  (EU directive)

- 24 rats
- four groups with daily DMH dose
  - control
  - low
  - medium
  - high

- Genotoxicity in liver using comet assay on 150 liver cells per rat.
- Are there differences in DNA damage due to DMH dose?

## Comet Assay:

- Visualise DNA strand breaks
- Length comet tail is a proxy for strand breaks.

![Comet assay](https://raw.githubusercontent.com/GTPB/PSLS20/gh-pages/assets/figs/comet.jpg){ width=50% }


```r
dna <- read_delim("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/dna.txt",delim=" ")
dna$dose <- as.factor(dna$dose)
dna
```


```r
dna %>%
  ggplot(aes(x=dose,y=length,fill=dose))+
  geom_boxplot() +
  geom_point(position="jitter")

dna %>%
  ggplot(aes(sample=length)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~dose)
```

- Strong indication that data in control group has a lower variance.
- 6 observations per group are too few to check the assumptions

```r
plot(lm(length~dose,data=dna))
```

---

[← Comparison of $g$ groups](01-comparison-of-groups.md) · [Up: contents](index.md) · [Kruskal-Wallis Rank Test →](03-kruskal-wallis-rank-test.md)
