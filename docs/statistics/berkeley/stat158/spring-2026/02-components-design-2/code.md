---
title: Code
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/02-components-design-2/code.html
source_file: sources/berkeley-stat158/spring-2026/02-components-design-2/code.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Code

**Source:** [`02-components-design-2/code.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/02-components-design-2/code.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

# Exploratory Data Analysis {#exploratory-data-analysis .title}

``` {.sourceCode .r .code-with-copy}
library(tidyverse)
anchoring <- read_csv(file = "https://stat158.berkeley.edu/spring-2026/data/anchoring/anchoring.csv",
                      col_types = list(col_factor(), col_double()))
```

``` {.sourceCode .r .code-with-copy}
anchoring |>
    count(X)
```

``` {.sourceCode .r .code-with-copy}
anchoring |>
    group_by(X) |>
    summarize(avg = mean(Y),
              sd = sd(Y),
              med = median(Y))
```

``` {.sourceCode .r .code-with-copy}
ggplot(anchoring, aes(x = Y, fill = X)) +
    geom_density(alpha = .3)
```

---

[Up: contents](../index.md)
