---
title: Using Libraries
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/r-cheatsheet.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Using Libraries

**Source:** [`background_material/r-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**`install.packages(‘dplyr’)`** Download and install a package from CRAN.

```
library(dplyr)
```

Load the package into the session, making all its functions available to use.

```
dplyr::select
```

Use a particular function from a package.

```
data(iris)
```

Load a built-in dataset into the environment.

---

[← Getting Help](01-getting-help.md) · [Up: contents](index.md) · [Working Directory →](03-working-directory.md)
