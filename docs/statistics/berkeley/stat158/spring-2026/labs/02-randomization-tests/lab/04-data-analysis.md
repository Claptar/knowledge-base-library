---
title: Data Analysis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/02-randomization-tests/lab.md
source_file: sources/berkeley-stat158/spring-2026/labs/02-randomization-tests/lab.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Analysis

**Source:** [`labs/02-randomization-tests/lab.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/02-randomization-tests/lab.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

We will analyze both the original dataset as well as our own collected
data. Ensure that you tabulate your data into a `.csv` file. This can be
done by entering your data into Google Sheets or Microsoft Excel before
saving as `.csv`.

We will be using data collected from the Many Labs study (2020), which
implemented the same question as Tversky and Kahneman. The experiment
was the same in most regards, and they expanded their sample to 6,344
participants recruited from 36 different sources including university
subject pools, Amazon Mechanical Turk, Project Implicit, and other
sources.

The dataset is stored in a `.csv` file. As earlier, use the `readr`
package, which is included inside the `tidyverse`. If you haven't
installed the tidyverse before, you can do so by running
`install.packages("tidyverse")` once.

::: cell
``` {.r .cell-code}
# load tidyverse (includes readr for CSVs)
library(tidyverse)
```
:::

::: cell
``` {.r .cell-code}
# load the data into R
framing <- read_csv("https://stat158.berkeley.edu/spring-2026/data/framing/framing.csv")
```
:::

::: cell
``` {.r .cell-code}
# load your collected data into R as well

#my_data <-
```
:::

---

[← Conducting Your Own Experiment](03-conducting-your-own-experiment.md) · [Up: contents](index.md) · [Statistical tests →](05-statistical-tests.md)
