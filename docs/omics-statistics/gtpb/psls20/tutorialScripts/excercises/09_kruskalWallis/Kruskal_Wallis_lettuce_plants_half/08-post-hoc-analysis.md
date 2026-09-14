---
title: Post-hoc analysis
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Post-hoc analysis

**Source:** [`tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

We will perform a post-hoc analysis with pairwise Wilcoxon rank
sum test. As we did not want to assume the location shift, we
will interpret the outcome in terms of probabilistic indices.
Note that after the analysis, we will need to correct the acquired
p-values for multiple testing.

## Hypotheses

Formulate a correct null and alternative hypothesis for the Wilcoxon test post-hoc analysis.

## Analysis

```r
## pairwise.wilcox.test(...)
```

What do you observe?

```
## Alternative: caluculate the p-value for each treatment combination with wilcoxon_test

treatments <- levels(lettuce$treatment)
freshweight <- lettuce$freshweight

pvalues <- combn(treatments,2,function(x){

  ## Pairwise Wilcoxon test
  test = wilcox_test(freshweight~treatment,subset(lettuce,treatment%in%x), distribution = 'exact')

  ## Get and store p-value of test
  pvalue(test)
})

## Adjust for multiple testing
pvalues_bonf = p.adjust(pvalues,method = 'bonferroni')

## link the p-value with the correct pairwise test
names(pvalues_bonf) <- combn(levels(lettuce$treatment),2,paste,collapse="_VS_")
pvalues_bonf
```

Interpret.

Based on the chunk of code above, can extract the point estimates
for the probabilistic indices? Interpret those as well.

---

[← Kruskal-Wallis rank test](07-kruskal-wallis-rank-test.md) · [Up: contents](index.md) · [Conclusion →](09-conclusion.md)
