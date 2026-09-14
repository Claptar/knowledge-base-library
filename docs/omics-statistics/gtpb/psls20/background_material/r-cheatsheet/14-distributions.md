---
title: Distributions
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/r-cheatsheet.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Distributions

**Source:** [`background_material/r-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

||Random<br>Variates|Density<br>Function|Cumulative<br>Distribution|Quantile|
|---|---|---|---|---|
|Normal|`rnorm`|`dnorm`|`pnorm`|`qnorm`|
|Poison|`rpois`|`dpois`|`ppois`|`qpois`|
|Binomial|`rbinom`|`dbinom`|`pbinom`|`qbinom`|
|Uniform|`runif`|`dunif`|`punif`|`qunif`|

---

[← Statistics](13-statistics.md) · [Up: contents](index.md) · [Plotting →](15-plotting.md)
