---
title: 5 Standard dataset manipulations
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Standard dataset manipulations

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Base R provides a variety of functions for manipulating data frames, but now many researchers use add-on packages (many written by Hadley Wickham as part of a group of packages called the _tidyverse_ ) to do these manipulations in a more elegant, often more efficient way. Module 5 of the R bootcamp describes some of these new tools, but I’ll summarize them here.

### **5.1 split-apply-combine**

Often analyses are done in a stratified fashion - the same operation or analysis is done on subsets of the data set. The subsets might be different time points, different locations, different hospitals, different people, etc.

The split-apply-combine framework is intended to operate in this kind of context: first one splits the dataset by one or more variables, then one does something to each subset, and then one combines the results. The _dplyr_ package implements this framework (as does the _pandas_ package for Python). One can also do similar operations using various flavors of the _apply()_ family of functions such as _by()_ , _tapply()_ , and _aggregate()_ , but the dplyr-based tools are often nicer to use.

### **5.2 Long and wide formats**

Finally, we may want to convert between so-called ’long’ and ’wide’ formats, which we can motivate in the context of longitudinal data (multiple observations per subject) and panel data (temporal data for each of multiple units such as in econometrics). The wide format has repeated measurements for a subject in separate columns, while the long format has repeated measurements in separate rows, with a column for differentiating the repeated measurements. The wide format is useful for doing separate analyses by group, while the long format is useful for doing a single analysis that makes use of the groups, such as ANOVA or mixed models or for plotting, such as with _ggplot2_ .

38

long <- **data.frame** (id = **c** (1, 1, 2, 2), time = **c** (1980, 1990, 1980, 1990), value = **c** (5, 8, 7, 4)) wide <- **data.frame** (id = **c** (1, 2), value_1980 = **c** (5, 7), value_1990 = **c** (8, 4)) long ## id time value ## 1 1 1980 5 ## 2 1 1990 8 ## 3 2 1980 7 ## 4 2 1990 4 wide ## id value_1980 value_1990 ## 1 1 5 8 ## 2 2 7 4

There are a variety of functions for converting between wide and long formats. I recommend _pivot_longer()_ and _pivot_wider()_ from recent versions of the _tidyr_ package. There are also older _tidyr_ functions called _gather()_ and _spread()_ . There are also the _melt()_ and _cast()_ in the _reshape2_ package. These are easier to use than the functions in base R such as _reshape()_ or _stack()_ and _unstack()_ functions _._

### **5.3 Non-standard evaluation and the tidyverse**

Many tidyverse packages use non-standard evaluation to make it easier to code. For example in the following dplyr example, you can refer directly to _country_ and _unemp_ , which are variables in the data frame, without using data$country or data$unemp and without using quotes around the variable names, as in “country” or “unemp”. Referring directly to the variables in the data frame is not standard R usage, hence the term “non-standard evaluation”. One reason it is not standard is that country and unemp are not themselves independent R variables so R can’t find them in the usual way (see Section 6.6).

**library** (dplyr)

cpds <- **read.csv** ( **file.path** ('..', 'data', 'cpds.csv'),

39

stringsAsFactors = FALSE)

cpds2 <- cpds %>% **group_by** (country) %>% **mutate** (mean_unemp = **mean** (unemp)) **head** (cpds2) ## # A tibble: 6 x 7 ## # Groups: country [1] ## year country vturn outlays realgdpgr unemp ## <int> <chr> <dbl> <dbl> <dbl> <dbl> ## 1 1960 Australia 95.5 NA NA 1.42 ## 2 1961 Australia 95.3 NA -0.07 2.79 ## 3 1962 Australia 95.3 23.2 5.71 2.63 ## 4 1963 Australia 95.7 23.0 6.1 2.12 ## 5 1964 Australia 95.7 22.9 6.28 1.15 ## 6 1965 Australia 95.7 24.9 4.97 1.15 ## # ... with 1 more variable: mean_unemp <dbl>

This ’magic’ is done by capturing the code expression you write and evaluating it in a special way in the context of the data frame. I believe this uses R’s environment class (discussed in Section 6), but haven’t looked more deeply.

While this has benefits, this so-called non-standard evaluation makes it harder to program functions in the usual way, as illustrated in the following code chunk, where neither attempt to use the function works.

add_mean <- **function** (data, group_var, summarize_var) { data %>% **group_by** (group_var) %>% **mutate** (mean_of_var = **mean** (summarize_var)) }

**try** (cpds2 <- **add_mean** (cpds, country, unemp)) ## Error : Must group by variables found in ` .data ` . ## * Column ` group_var ` is not found.

**try** (cpds2 <- **add_mean** (cpds, 'country', 'unemp'))

40

---

[← R6 Object of class 'tsSimClass' with 100 time points.](23-r6-object-of-class-tssimclass-with-100-time-points.md) · [Up: contents](index.md) · [Error : Must group by variables found in .data . ## Column groupvar is not found. →](25-error-must-group-by-variables-found-in-data-column-groupvar.md)
