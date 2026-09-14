---
title: Multiple Comparisons
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/18-multiple-comparisons/slides.html
source_file: sources/berkeley-stat158/spring-2026/18-multiple-comparisons/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Multiple Comparisons

**Source:** [`18-multiple-comparisons/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/18-multiple-comparisons/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## While you’re waiting

What is the expected number of false positives if you conduct 20 hypothesis tests, each at a significance level of <span class="math inline">\$\\alpha = .05\$</span>?

Said another way, if in reality nothing is going on in all 20 tests, what’s the expected number of tests that would detect something going on?

> 1

##

## Making Paper

<style>#wpwuurgqfn table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#wpwuurgqfn thead, #wpwuurgqfn tbody, #wpwuurgqfn tfoot, #wpwuurgqfn tr, #wpwuurgqfn td, #wpwuurgqfn th {
  border-style: none;
}

#wpwuurgqfn p {
  margin: 0;
  padding: 0;
}

#wpwuurgqfn .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#wpwuurgqfn .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#wpwuurgqfn .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#wpwuurgqfn .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#wpwuurgqfn .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#wpwuurgqfn .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#wpwuurgqfn .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#wpwuurgqfn .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#wpwuurgqfn .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#wpwuurgqfn .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#wpwuurgqfn .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#wpwuurgqfn .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#wpwuurgqfn .gt_spanner_row {
  border-bottom-style: hidden;
}

#wpwuurgqfn .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}

#wpwuurgqfn .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#wpwuurgqfn .gt_from_md > :first-child {
  margin-top: 0;
}

#wpwuurgqfn .gt_from_md > :last-child {
  margin-bottom: 0;
}

#wpwuurgqfn .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#wpwuurgqfn .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#wpwuurgqfn .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#wpwuurgqfn .gt_row_group_first td {
  border-top-width: 2px;
}

#wpwuurgqfn .gt_row_group_first th {
  border-top-width: 2px;
}

#wpwuurgqfn .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#wpwuurgqfn .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#wpwuurgqfn .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#wpwuurgqfn .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#wpwuurgqfn .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#wpwuurgqfn .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#wpwuurgqfn .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#wpwuurgqfn .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#wpwuurgqfn .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#wpwuurgqfn .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#wpwuurgqfn .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#wpwuurgqfn .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#wpwuurgqfn .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#wpwuurgqfn .gt_left {
  text-align: left;
}

#wpwuurgqfn .gt_center {
  text-align: center;
}

#wpwuurgqfn .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#wpwuurgqfn .gt_font_normal {
  font-weight: normal;
}

#wpwuurgqfn .gt_font_bold {
  font-weight: bold;
}

#wpwuurgqfn .gt_font_italic {
  font-style: italic;
}

#wpwuurgqfn .gt_super {
  font-size: 65%;
}

#wpwuurgqfn .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#wpwuurgqfn .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#wpwuurgqfn .gt_indent_1 {
  text-indent: 5px;
}

#wpwuurgqfn .gt_indent_2 {
  text-indent: 10px;
}

#wpwuurgqfn .gt_indent_3 {
  text-indent: 15px;
}

#wpwuurgqfn .gt_indent_4 {
  text-indent: 20px;
}

#wpwuurgqfn .gt_indent_5 {
  text-indent: 25px;
}

#wpwuurgqfn .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#wpwuurgqfn div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

| strength | hard | time | pressure |
|----------|------|------|----------|
| 196.6    | 2    | 3hrs | 400      |
| 196.0    | 2    | 3hrs | 400      |
| 198.5    | 4    | 3hrs | 400      |
| 197.2    | 4    | 3hrs | 400      |
| 197.5    | 8    | 3hrs | 400      |
| 196.6    | 8    | 3hrs | 400      |
| 197.7    | 2    | 3hrs | 500      |
| 196.0    | 2    | 3hrs | 500      |
| 196.0    | 4    | 3hrs | 500      |
| 196.9    | 4    | 3hrs | 500      |
| 195.6    | 8    | 3hrs | 500      |
| 196.2    | 8    | 3hrs | 500      |
| 199.8    | 2    | 3hrs | 650      |
| 199.4    | 2    | 3hrs | 650      |
| 198.4    | 4    | 3hrs | 650      |
| 197.6    | 4    | 3hrs | 650      |
| 197.4    | 8    | 3hrs | 650      |
| 198.1    | 8    | 3hrs | 650      |
| 198.4    | 2    | 4hrs | 400      |
| 198.6    | 2    | 4hrs | 400      |
| 197.5    | 4    | 4hrs | 400      |
| 198.1    | 4    | 4hrs | 400      |
| 197.6    | 8    | 4hrs | 400      |
| 198.4    | 8    | 4hrs | 400      |
| 199.6    | 2    | 4hrs | 500      |
| 200.4    | 2    | 4hrs | 500      |
| 198.7    | 4    | 4hrs | 500      |
| 198.0    | 4    | 4hrs | 500      |
| 197.0    | 8    | 4hrs | 500      |
| 197.8    | 8    | 4hrs | 500      |
| 200.6    | 2    | 4hrs | 650      |
| 200.9    | 2    | 4hrs | 650      |
| 199.6    | 4    | 4hrs | 650      |
| 199.0    | 4    | 4hrs | 650      |
| 198.5    | 8    | 4hrs | 650      |
| 199.8    | 8    | 4hrs | 650      |

## EDA

## Three way ANOVA

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova <- aov(strength ~ time * pressure * hard, data = paper)
anova_tab <- summary(anova)
anova_tab
```

                       Df Sum Sq Mean Sq F value   Pr(>F)
    time                1 20.250  20.250  55.395 6.75e-07 ***
    pressure            2 19.374   9.687  26.499 4.33e-06 ***
    hard                2  7.764   3.882  10.619   0.0009 ***
    time:pressure       2  2.195   1.097   3.002   0.0750 .
    time:hard           2  2.082   1.041   2.847   0.0843 .
    pressure:hard       4  6.091   1.523   4.166   0.0146 *
    time:pressure:hard  4  1.973   0.493   1.350   0.2903
    Residuals          18  6.580   0.366
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

How many hypothesis tests are being conducted in this ANOVA table?

> 7

## Bonferroni

Original p-values:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_results <- data.frame(estimate = row.names(anova_tab[[1]])[1:7],
                            p_vals = anova_tab[[1]]$`Pr(>F)`[1:7])
anova_results
```

                estimate       p_vals
    1 time               6.745340e-07
    2 pressure           4.327241e-06
    3 hard               8.995614e-04
    4 time:pressure      7.495643e-02
    5 time:hard          8.425969e-02
    6 pressure:hard      1.462624e-02
    7 time:pressure:hard 2.903053e-01

## Bonferroni

Adjust p-values by multiplying them by <span class="math inline">\$K\$</span>.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_results <- anova_results |>
  mutate(bon_adjusted = pmin(p_vals * 7, 1))
anova_results
```

                estimate       p_vals bon_adjusted
    1 time               6.745340e-07 4.721738e-06
    2 pressure           4.327241e-06 3.029069e-05
    3 hard               8.995614e-04 6.296930e-03
    4 time:pressure      7.495643e-02 5.246950e-01
    5 time:hard          8.425969e-02 5.898178e-01
    6 pressure:hard      1.462624e-02 1.023837e-01
    7 time:pressure:hard 2.903053e-01 1.000000e+00

## Holm’s Procedure

Original sorted p-values:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
sorted_pvals <- sort(anova_results$p_vals)
sorted_pvals
```

    [1] 6.745340e-07 4.327241e-06 8.995614e-04 1.462624e-02 7.495643e-02
    [6] 8.425969e-02 2.903053e-01

## Holm’s Procedure

Working from smallest to largest p-values (call the rank <span class="math inline">\$j\$</span>), adjust p-values to max of <span class="math inline">\$K - j + 1\$</span> times the original p-value or the max of previous p-values.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
holm <- rep(NA, length(sorted_pvals)) # initialize
previous_max <- sorted_pvals[1]
K <- length(sorted_pvals)
for (j in 1:K) {
  holm[j] <- max(sorted_pvals[j] * (K - j + 1), previous_max, na.rm = TRUE)
  holm[j] <- max(sorted_pvals[j] * (K - j + 1), previous_max, na.rm = TRUE)
  previous_max <- max(holm, na.rm = TRUE)
}
```

## Holm’s Procedure

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_results <- anova_results |>
  arrange(p_vals) |>
  mutate(holm)
anova_results
```

                estimate       p_vals bon_adjusted         holm
    1 time               6.745340e-07 4.721738e-06 4.721738e-06
    2 pressure           4.327241e-06 3.029069e-05 2.596345e-05
    3 hard               8.995614e-04 6.296930e-03 4.497807e-03
    4 pressure:hard      1.462624e-02 1.023837e-01 5.850495e-02
    5 time:pressure      7.495643e-02 5.246950e-01 2.248693e-01
    6 time:hard          8.425969e-02 5.898178e-01 2.248693e-01
    7 time:pressure:hard 2.903053e-01 1.000000e+00 2.903053e-01

## R Shortcut

`p.adjust()` can adjust p-values using many different methods including:

- Bonferroni and Holm
- False discovery rate: Benjamini & Hochberg, Benjamini & Yekutieli

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
sapply(c("none", "holm", "bonferroni"), p.adjust, p = sorted_pvals)
```

                 none         holm   bonferroni
    [1,] 6.745340e-07 4.721738e-06 4.721738e-06
    [2,] 4.327241e-06 2.596345e-05 3.029069e-05
    [3,] 8.995614e-04 4.497807e-03 6.296930e-03
    [4,] 1.462624e-02 5.850495e-02 1.023837e-01
    [5,] 7.495643e-02 2.248693e-01 5.246950e-01
    [6,] 8.425969e-02 2.248693e-01 5.898178e-01
    [7,] 2.903053e-01 2.903053e-01 1.000000e+00

---

[← Multiple Comparisons](01-multiple-comparisons.md) · [Up: contents](index.md)
