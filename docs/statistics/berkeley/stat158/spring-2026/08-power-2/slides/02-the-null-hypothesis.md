---
title: The Null Hypothesis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# The Null Hypothesis

**Source:** [`08-power-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## From data to schedule {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
library(tidyverse)
library(gt)
```

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
my_data <- tibble(i = 1:10,
                  d_i = c(1, 0, 1, 0, 0, 0, 0, 1, 1, 1),
                  y_i = c(.9, -.5, 2.2, -1.4, .1, -1, 1.1, 1, 1.02, 1.5))

my_data |>
  gt() |>
  tab_header(title = "My Data")
```

<style>#sfcxvikbxu table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#sfcxvikbxu thead, #sfcxvikbxu tbody, #sfcxvikbxu tfoot, #sfcxvikbxu tr, #sfcxvikbxu td, #sfcxvikbxu th {
  border-style: none;
}

#sfcxvikbxu p {
  margin: 0;
  padding: 0;
}

#sfcxvikbxu .gt_table {
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

#sfcxvikbxu .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#sfcxvikbxu .gt_title {
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

#sfcxvikbxu .gt_subtitle {
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

#sfcxvikbxu .gt_heading {
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

#sfcxvikbxu .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#sfcxvikbxu .gt_col_headings {
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

#sfcxvikbxu .gt_col_heading {
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

#sfcxvikbxu .gt_column_spanner_outer {
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

#sfcxvikbxu .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#sfcxvikbxu .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#sfcxvikbxu .gt_column_spanner {
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

#sfcxvikbxu .gt_spanner_row {
  border-bottom-style: hidden;
}

#sfcxvikbxu .gt_group_heading {
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

#sfcxvikbxu .gt_empty_group_heading {
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

#sfcxvikbxu .gt_from_md > :first-child {
  margin-top: 0;
}

#sfcxvikbxu .gt_from_md > :last-child {
  margin-bottom: 0;
}

#sfcxvikbxu .gt_row {
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

#sfcxvikbxu .gt_stub {
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

#sfcxvikbxu .gt_stub_row_group {
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

#sfcxvikbxu .gt_row_group_first td {
  border-top-width: 2px;
}

#sfcxvikbxu .gt_row_group_first th {
  border-top-width: 2px;
}

#sfcxvikbxu .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#sfcxvikbxu .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#sfcxvikbxu .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#sfcxvikbxu .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#sfcxvikbxu .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#sfcxvikbxu .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#sfcxvikbxu .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#sfcxvikbxu .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#sfcxvikbxu .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#sfcxvikbxu .gt_footnotes {
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

#sfcxvikbxu .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#sfcxvikbxu .gt_sourcenotes {
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

#sfcxvikbxu .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#sfcxvikbxu .gt_left {
  text-align: left;
}

#sfcxvikbxu .gt_center {
  text-align: center;
}

#sfcxvikbxu .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#sfcxvikbxu .gt_font_normal {
  font-weight: normal;
}

#sfcxvikbxu .gt_font_bold {
  font-weight: bold;
}

#sfcxvikbxu .gt_font_italic {
  font-style: italic;
}

#sfcxvikbxu .gt_super {
  font-size: 65%;
}

#sfcxvikbxu .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#sfcxvikbxu .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#sfcxvikbxu .gt_indent_1 {
  text-indent: 5px;
}

#sfcxvikbxu .gt_indent_2 {
  text-indent: 10px;
}

#sfcxvikbxu .gt_indent_3 {
  text-indent: 15px;
}

#sfcxvikbxu .gt_indent_4 {
  text-indent: 20px;
}

#sfcxvikbxu .gt_indent_5 {
  text-indent: 25px;
}

#sfcxvikbxu .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#sfcxvikbxu div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Data</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="d_i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">d_i</th>
<th id="y_i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">y_i</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-0.50</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-1.40</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">0.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">-1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="d_i">0</td>
<td class="gt_row gt_right" headers="y_i">1.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="d_i">1</td>
<td class="gt_row gt_right" headers="y_i">1.50</td>
</tr>
</tbody>
</table>

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
my_obs_sched <- my_data |>
  mutate(Y_0 = ifelse(d_i == 0, y_i, NA),
         Y_1 = ifelse(d_i == 1, y_i, NA)) |>
  select(i, Y_0, Y_1)
my_obs_sched |>
  gt() |>
  tab_header(title = "My Observed Schedule")
```

<style>#ocosdvttod table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#ocosdvttod thead, #ocosdvttod tbody, #ocosdvttod tfoot, #ocosdvttod tr, #ocosdvttod td, #ocosdvttod th {
  border-style: none;
}

#ocosdvttod p {
  margin: 0;
  padding: 0;
}

#ocosdvttod .gt_table {
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

#ocosdvttod .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#ocosdvttod .gt_title {
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

#ocosdvttod .gt_subtitle {
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

#ocosdvttod .gt_heading {
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

#ocosdvttod .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ocosdvttod .gt_col_headings {
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

#ocosdvttod .gt_col_heading {
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

#ocosdvttod .gt_column_spanner_outer {
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

#ocosdvttod .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#ocosdvttod .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#ocosdvttod .gt_column_spanner {
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

#ocosdvttod .gt_spanner_row {
  border-bottom-style: hidden;
}

#ocosdvttod .gt_group_heading {
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

#ocosdvttod .gt_empty_group_heading {
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

#ocosdvttod .gt_from_md > :first-child {
  margin-top: 0;
}

#ocosdvttod .gt_from_md > :last-child {
  margin-bottom: 0;
}

#ocosdvttod .gt_row {
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

#ocosdvttod .gt_stub {
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

#ocosdvttod .gt_stub_row_group {
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

#ocosdvttod .gt_row_group_first td {
  border-top-width: 2px;
}

#ocosdvttod .gt_row_group_first th {
  border-top-width: 2px;
}

#ocosdvttod .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ocosdvttod .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#ocosdvttod .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#ocosdvttod .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ocosdvttod .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ocosdvttod .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#ocosdvttod .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#ocosdvttod .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#ocosdvttod .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ocosdvttod .gt_footnotes {
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

#ocosdvttod .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ocosdvttod .gt_sourcenotes {
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

#ocosdvttod .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ocosdvttod .gt_left {
  text-align: left;
}

#ocosdvttod .gt_center {
  text-align: center;
}

#ocosdvttod .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#ocosdvttod .gt_font_normal {
  font-weight: normal;
}

#ocosdvttod .gt_font_bold {
  font-weight: bold;
}

#ocosdvttod .gt_font_italic {
  font-style: italic;
}

#ocosdvttod .gt_super {
  font-size: 65%;
}

#ocosdvttod .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#ocosdvttod .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#ocosdvttod .gt_indent_1 {
  text-indent: 5px;
}

#ocosdvttod .gt_indent_2 {
  text-indent: 10px;
}

#ocosdvttod .gt_indent_3 {
  text-indent: 15px;
}

#ocosdvttod .gt_indent_4 {
  text-indent: 20px;
}

#ocosdvttod .gt_indent_5 {
  text-indent: 25px;
}

#ocosdvttod .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#ocosdvttod div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Observed Schedule</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="Y_0" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_0</th>
<th id="Y_1" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_1</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="Y_0">-0.5</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="Y_0">-1.4</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="Y_0">0.1</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="Y_0">-1.0</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="Y_0">1.1</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.50</td>
</tr>
</tbody>
</table>

## From data to schedule {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
my_obs_sched <- my_data |>
  mutate(Y_0 = ifelse(d_i == 0, y_i, NA),
         Y_1 = ifelse(d_i == 1, y_i, NA)) |>
  select(i, Y_0, Y_1)

my_obs_sched |>
  gt() |>
  tab_header(title = "My Observed Schedule")
```

<style>#bgnitujhpx table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#bgnitujhpx thead, #bgnitujhpx tbody, #bgnitujhpx tfoot, #bgnitujhpx tr, #bgnitujhpx td, #bgnitujhpx th {
  border-style: none;
}

#bgnitujhpx p {
  margin: 0;
  padding: 0;
}

#bgnitujhpx .gt_table {
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

#bgnitujhpx .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#bgnitujhpx .gt_title {
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

#bgnitujhpx .gt_subtitle {
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

#bgnitujhpx .gt_heading {
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

#bgnitujhpx .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#bgnitujhpx .gt_col_headings {
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

#bgnitujhpx .gt_col_heading {
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

#bgnitujhpx .gt_column_spanner_outer {
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

#bgnitujhpx .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#bgnitujhpx .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#bgnitujhpx .gt_column_spanner {
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

#bgnitujhpx .gt_spanner_row {
  border-bottom-style: hidden;
}

#bgnitujhpx .gt_group_heading {
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

#bgnitujhpx .gt_empty_group_heading {
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

#bgnitujhpx .gt_from_md > :first-child {
  margin-top: 0;
}

#bgnitujhpx .gt_from_md > :last-child {
  margin-bottom: 0;
}

#bgnitujhpx .gt_row {
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

#bgnitujhpx .gt_stub {
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

#bgnitujhpx .gt_stub_row_group {
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

#bgnitujhpx .gt_row_group_first td {
  border-top-width: 2px;
}

#bgnitujhpx .gt_row_group_first th {
  border-top-width: 2px;
}

#bgnitujhpx .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#bgnitujhpx .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#bgnitujhpx .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#bgnitujhpx .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#bgnitujhpx .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#bgnitujhpx .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#bgnitujhpx .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#bgnitujhpx .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#bgnitujhpx .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#bgnitujhpx .gt_footnotes {
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

#bgnitujhpx .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#bgnitujhpx .gt_sourcenotes {
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

#bgnitujhpx .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#bgnitujhpx .gt_left {
  text-align: left;
}

#bgnitujhpx .gt_center {
  text-align: center;
}

#bgnitujhpx .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#bgnitujhpx .gt_font_normal {
  font-weight: normal;
}

#bgnitujhpx .gt_font_bold {
  font-weight: bold;
}

#bgnitujhpx .gt_font_italic {
  font-style: italic;
}

#bgnitujhpx .gt_super {
  font-size: 65%;
}

#bgnitujhpx .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#bgnitujhpx .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#bgnitujhpx .gt_indent_1 {
  text-indent: 5px;
}

#bgnitujhpx .gt_indent_2 {
  text-indent: 10px;
}

#bgnitujhpx .gt_indent_3 {
  text-indent: 15px;
}

#bgnitujhpx .gt_indent_4 {
  text-indent: 20px;
}

#bgnitujhpx .gt_indent_5 {
  text-indent: 25px;
}

#bgnitujhpx .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#bgnitujhpx div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Observed Schedule</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="Y_0" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_0</th>
<th id="Y_1" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_1</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="Y_0">-0.5</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="Y_0">-1.4</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="Y_0">0.1</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="Y_0">-1.0</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="Y_0">1.1</td>
<td class="gt_row gt_right" headers="Y_1">NA</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="Y_0">NA</td>
<td class="gt_row gt_right" headers="Y_1">1.50</td>
</tr>
</tbody>
</table>

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
my_null_sched <- my_obs_sched |>
  mutate(Y_0 = ifelse(is.na(Y_0), Y_1, Y_0),
         Y_1 = ifelse(is.na(Y_1), Y_0, Y_1))

my_null_sched |>
  gt() |>
  tab_header(title = "My Null Schedule")
```

<style>#ioiqlptmgm table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#ioiqlptmgm thead, #ioiqlptmgm tbody, #ioiqlptmgm tfoot, #ioiqlptmgm tr, #ioiqlptmgm td, #ioiqlptmgm th {
  border-style: none;
}

#ioiqlptmgm p {
  margin: 0;
  padding: 0;
}

#ioiqlptmgm .gt_table {
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

#ioiqlptmgm .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#ioiqlptmgm .gt_title {
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

#ioiqlptmgm .gt_subtitle {
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

#ioiqlptmgm .gt_heading {
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

#ioiqlptmgm .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ioiqlptmgm .gt_col_headings {
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

#ioiqlptmgm .gt_col_heading {
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

#ioiqlptmgm .gt_column_spanner_outer {
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

#ioiqlptmgm .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#ioiqlptmgm .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#ioiqlptmgm .gt_column_spanner {
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

#ioiqlptmgm .gt_spanner_row {
  border-bottom-style: hidden;
}

#ioiqlptmgm .gt_group_heading {
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

#ioiqlptmgm .gt_empty_group_heading {
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

#ioiqlptmgm .gt_from_md > :first-child {
  margin-top: 0;
}

#ioiqlptmgm .gt_from_md > :last-child {
  margin-bottom: 0;
}

#ioiqlptmgm .gt_row {
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

#ioiqlptmgm .gt_stub {
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

#ioiqlptmgm .gt_stub_row_group {
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

#ioiqlptmgm .gt_row_group_first td {
  border-top-width: 2px;
}

#ioiqlptmgm .gt_row_group_first th {
  border-top-width: 2px;
}

#ioiqlptmgm .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ioiqlptmgm .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#ioiqlptmgm .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#ioiqlptmgm .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ioiqlptmgm .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ioiqlptmgm .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#ioiqlptmgm .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#ioiqlptmgm .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#ioiqlptmgm .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ioiqlptmgm .gt_footnotes {
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

#ioiqlptmgm .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ioiqlptmgm .gt_sourcenotes {
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

#ioiqlptmgm .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ioiqlptmgm .gt_left {
  text-align: left;
}

#ioiqlptmgm .gt_center {
  text-align: center;
}

#ioiqlptmgm .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#ioiqlptmgm .gt_font_normal {
  font-weight: normal;
}

#ioiqlptmgm .gt_font_bold {
  font-weight: bold;
}

#ioiqlptmgm .gt_font_italic {
  font-style: italic;
}

#ioiqlptmgm .gt_super {
  font-size: 65%;
}

#ioiqlptmgm .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#ioiqlptmgm .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#ioiqlptmgm .gt_indent_1 {
  text-indent: 5px;
}

#ioiqlptmgm .gt_indent_2 {
  text-indent: 10px;
}

#ioiqlptmgm .gt_indent_3 {
  text-indent: 15px;
}

#ioiqlptmgm .gt_indent_4 {
  text-indent: 20px;
}

#ioiqlptmgm .gt_indent_5 {
  text-indent: 25px;
}

#ioiqlptmgm .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#ioiqlptmgm div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Null Schedule</th>
</tr>
<tr class="gt_col_headings even">
<th id="i" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">i</th>
<th id="Y_0" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_0</th>
<th id="Y_1" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Y_1</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="odd">
<td class="gt_row gt_right" headers="i">1</td>
<td class="gt_row gt_right" headers="Y_0">0.90</td>
<td class="gt_row gt_right" headers="Y_1">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="Y_0">-0.50</td>
<td class="gt_row gt_right" headers="Y_1">-0.50</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="Y_0">2.20</td>
<td class="gt_row gt_right" headers="Y_1">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="Y_0">-1.40</td>
<td class="gt_row gt_right" headers="Y_1">-1.40</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="Y_0">0.10</td>
<td class="gt_row gt_right" headers="Y_1">0.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="Y_0">-1.00</td>
<td class="gt_row gt_right" headers="Y_1">-1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="Y_0">1.10</td>
<td class="gt_row gt_right" headers="Y_1">1.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="Y_0">1.00</td>
<td class="gt_row gt_right" headers="Y_1">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="Y_0">1.02</td>
<td class="gt_row gt_right" headers="Y_1">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="Y_0">1.50</td>
<td class="gt_row gt_right" headers="Y_1">1.50</td>
</tr>
</tbody>
</table>

## Estimate Dist under H0

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
rand_stats <- function(schedule, d_i, stat = "diff in means", reps = 1000) {
  # store treatment vector separately
  d_i_vec <- d_i

  # replicate the schedule reps times and stack them on top of one another
  randomized_exp_df <- map_dfr(1:reps, ~ schedule, .id = "experiment") |>
    mutate(experiment = factor(experiment, levels = as.character(1:reps), ordered = TRUE),
           d_i = c(replicate(n = reps, sample(d_i_vec))),  # create random assignments
           y_i = Y_1 * d_i +  Y_0 * (1 - d_i)) |>    # find observed responses
    arrange(experiment)

  # calculate test statistic for every random assignment
  if (stat == "diff in means") {
    stats <- randomized_exp_df |>
      group_by(experiment, d_i) |>
      summarize(ybar = mean(y_i),     # average within each group within each experiment
                .groups = "drop_last") |>
      summarize(ATE_hat = diff(ybar),
                .groups = "drop") |>   # take the difference between the two groups mean
      pull()
  } else {
    stop("Statistic not implemented")
  }

  return(stats)
}
```

## Estimate Dist under H0 {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
H_0 <- rand_stats(schedule = my_null_sched, d_i = my_data$d_i, reps = 5000)
H_0
```

       [1]  0.296 -0.224  0.736 -1.144  1.664  1.184 -1.064  0.216 -0.496 -1.376
      [11] -0.096  0.496  0.944  0.336 -0.336 -1.064 -1.336  0.016  0.584  0.224
      [21] -0.176  0.536  0.496  0.296 -0.144 -1.104 -0.616  0.704  0.864  0.576
      [31]  0.144  0.944 -0.104  0.256 -0.224 -0.664  1.136 -0.864 -0.296 -0.024
      [41] -0.864 -0.664  1.144  0.944 -0.496  0.856  0.856 -0.824  1.384  0.056
      [51]  1.104 -0.296 -0.664 -0.776 -1.344 -0.336  0.936 -0.096  0.104 -0.224
      [61] -0.504  0.296  0.096 -0.544  0.384 -1.104  0.664  0.424  0.384 -0.264
      [71]  0.304 -0.064  0.216 -0.576  0.224 -1.144  0.416  0.576 -0.576  0.336
      [81]  0.584  0.584 -0.096  0.744  0.576  0.944  0.104  0.904  0.704 -0.296
      [91]  0.064  0.264 -0.144  0.416 -0.216  0.336  1.104 -0.024  0.344  0.784
     [101] -0.496 -1.096  0.064 -1.384  0.576  0.096 -0.016 -1.136 -0.736  0.536
     [111] -0.224  0.384 -1.376  1.296 -1.304 -0.184 -0.136 -0.064  0.704  0.864
     [121]  0.496 -1.184 -0.264 -0.784 -0.304 -0.296 -0.384  0.264  0.176 -0.704
     [131]  0.304 -0.256  1.136  0.864  0.944  0.536  1.504  0.136  0.064  0.064
     [141] -0.576 -0.224 -0.744 -0.496 -0.304  0.664 -0.504  0.336  0.104  0.776
     [151] -0.264 -0.424 -1.344 -0.216  0.104 -1.344  0.624  0.224 -0.496 -1.144
     [161]  0.336  0.256  0.864 -0.056  1.136 -0.944  0.664 -0.584 -0.256 -0.544
     [171]  0.224  0.024  1.336  0.664 -0.096  0.464 -0.384 -0.664 -0.464 -0.024
     [181] -0.104 -0.944  1.384  0.216  1.384 -0.256  0.224 -0.856  0.336  0.696
     [191] -0.584 -1.136 -1.144  0.504 -0.544 -0.864 -1.384  0.176  0.016 -1.664
     [201] -0.944 -0.224  0.104  1.336  0.056  0.544 -0.904 -0.424  0.544 -0.576
     [211]  0.304 -0.336 -0.096 -0.664 -0.104 -0.096 -0.616 -0.504 -0.016 -0.064
     [221] -0.104 -0.336  0.176  0.744 -1.336  0.296 -0.304 -1.304 -1.144 -1.104
     [231]  0.144 -0.864  0.896  0.544  1.136  0.336  0.224  0.256  0.504  1.696
     [241] -0.496 -0.216 -0.056  0.536 -1.056 -0.776 -0.496 -0.864  0.424  0.536
     [251]  0.024  0.096 -0.304 -0.296 -0.536  1.376 -0.944 -0.736 -0.064  0.536
     [261] -0.024 -0.064 -1.344  0.216 -0.696  0.336  0.536 -0.224  0.016 -0.504
     [271]  0.904  1.224 -0.856 -0.104 -0.144 -0.336 -0.896 -0.744 -0.184 -0.696
     [281]  1.696 -0.904  0.824  1.384  0.296  0.704 -0.664 -0.064  0.176 -0.296
     [291]  0.416  0.064 -0.664 -0.264  0.216  0.296  0.416  0.256  1.096  0.856
     [301] -0.096 -0.176 -0.776  0.016 -0.464  0.744 -0.416 -0.864 -0.856 -0.056
     [311] -0.056 -0.296  0.224 -0.544  0.336 -0.104  1.136  0.344 -0.144 -0.336
     [321]  0.096 -0.776  0.504  0.376  0.056  0.056 -0.096  0.416 -0.824 -0.296
     [331]  0.576 -0.544  0.104  1.304  0.944 -0.616 -0.744 -0.224  1.336  0.576
     [341] -0.064 -0.736 -0.104  0.696 -0.496 -0.104  0.024  1.664  0.904  0.176
     [351]  0.136  0.536 -0.296 -0.536  0.464 -0.776  0.296 -0.504 -1.224 -0.704
     [361] -0.224 -0.464  1.144 -0.296 -1.336 -0.064 -0.264  0.864 -0.256  0.544
     [371]  0.696  0.184  0.064  0.176 -0.256  0.184  0.864  0.256 -0.264 -1.376
     [381]  0.536  0.384 -0.224  0.256  0.296 -0.064 -0.296  0.144 -0.176 -0.896
     [391]  0.096  0.096  0.664 -0.944  0.664 -0.136  0.776  1.056  0.536  0.776
     [401]  1.224 -0.216 -0.104  0.504  0.336  0.544 -0.064  1.304 -0.936  0.696
     [411]  0.864 -0.744  0.224  0.256  0.696  0.504  0.064 -0.056  0.256 -0.696
     [421]  0.344 -0.696 -0.904 -0.304 -0.864  0.864  0.856  0.504  1.064  0.256
     [431]  0.056 -1.144  0.616  0.096 -0.584  0.944  0.904 -0.744 -0.256 -0.304
     [441]  0.584 -1.376  0.384  0.136 -0.864 -0.256  0.376  0.144  1.144  0.304
     [451] -0.336  0.704  0.136 -0.264  1.144 -0.824 -0.144  0.576  1.744  0.696
     [461]  0.584  0.304 -1.696 -0.864 -0.464  0.344 -0.296 -0.376  1.336 -0.344
     [471] -1.136 -0.576 -0.896  0.624 -0.296 -1.056  0.296 -0.704 -0.736  0.056
     [481] -0.256 -0.896 -0.384  0.064  0.224  0.664  0.224 -0.904  0.256 -1.376
     [491]  0.104 -0.536 -0.496 -0.256 -1.144 -0.904  0.504  0.824 -0.104 -0.104
     [501] -0.224 -1.304  0.776 -0.664  0.016 -1.136  0.464  0.376 -0.064 -0.904
     [511]  0.504  0.576  0.064  0.864 -0.304 -0.256 -0.064 -0.584  0.056 -0.944
     [521] -0.864  0.024  0.296 -0.184  0.584 -0.496 -0.824  0.944 -0.296 -0.064
     [531] -0.856  0.416  0.744 -0.096 -0.256 -0.376  0.304  1.136  0.376 -0.576
     [541] -0.904 -0.896 -0.056 -0.336 -0.384 -0.576 -0.384  0.536  1.056  0.256
     [551] -0.584 -0.584  0.744 -0.864  0.304 -0.696 -0.584 -0.184 -0.416  0.704
     [561]  0.776 -0.824  0.224  1.144  1.704  0.544 -0.856  0.696 -0.344  0.696
     [571] -0.624 -0.936  1.336  0.704  0.304  1.664 -0.176  0.336  0.256 -1.104
     [581] -0.904  0.136 -0.136 -0.296 -0.424 -0.904  1.224 -0.696  1.136  0.104
     [591] -0.744 -0.536 -0.496 -0.256 -0.336 -1.104 -0.664  0.536  0.904 -0.864
     [601]  0.024  0.536 -1.104  0.136 -0.744  0.384 -0.336 -0.544  0.736 -0.536
     [611] -0.664 -1.056 -0.744 -0.536 -0.576  0.224 -0.576 -0.336  1.376  0.056
     [621] -0.944  1.224  0.024 -0.176  0.736  0.216 -0.584 -0.016  0.024  1.136
     [631] -1.664 -0.776 -0.224 -0.584  0.144 -0.256 -0.064  1.744  0.104  0.496
     [641] -0.384 -0.296 -0.064 -0.024 -0.544 -0.936  1.296 -0.216 -0.864  1.376
     [651]  0.424 -1.056 -0.704 -0.144  0.736  0.344 -0.776  1.144  0.896 -0.616
     [661] -0.104  1.136  0.376 -0.536  0.904  0.544  0.056  0.936  0.176  0.576
     [671] -1.096 -0.104 -0.696  1.704 -0.744 -0.296 -0.904 -0.344 -0.464 -1.104
     [681] -1.104 -1.344 -0.904  0.384 -1.664 -0.304  1.696  1.144 -0.504 -1.696
     [691] -0.896 -1.696 -0.944 -0.896  0.584 -0.304  1.384  0.384 -0.864 -0.784
     [701]  0.304 -0.384 -0.304 -0.464 -0.376 -0.064  0.544  0.344 -0.224 -0.776
     [711]  0.096 -0.856  1.104 -0.056 -0.224  0.544 -0.224 -1.384 -0.496  0.776
     [721]  0.304 -0.504 -0.336  1.096  0.344  1.064  0.504  0.304  0.136  0.104
     [731] -0.536 -0.264 -1.056 -0.944 -0.136  0.136  0.296  1.136  0.864  0.144
     [741] -0.096 -0.576  0.264  0.016 -0.104  0.056 -0.224  0.696 -0.424  1.384
     [751]  1.144 -0.576 -0.584 -0.064  1.224  1.696 -1.296  0.096  1.664  0.144
     [761]  1.136  1.184 -0.696  0.304 -0.576 -1.104  0.544  0.944  0.264  0.136
     [771]  0.256 -0.336  0.216  0.744  0.144  0.256  0.856  0.096 -0.056 -0.504
     [781]  0.296 -0.864 -0.776 -0.264 -0.296  0.384 -1.224  1.184  1.104 -0.664
     [791] -0.384  0.584 -0.544  0.384 -0.704 -1.144  1.744  0.496 -0.856  0.176
     [801]  0.064  0.696 -0.824 -0.664  0.224 -0.504  1.384  0.504  1.344  1.144
     [811]  0.584  1.336 -0.856 -0.904 -0.496  0.744 -0.464 -0.296 -0.696  1.184
     [821] -0.864 -0.696  1.376  0.544 -1.304 -0.744 -1.096 -0.064  0.944  0.744
     [831] -1.384  0.584  0.064  0.424 -1.664 -0.584  0.416 -0.216  0.256 -0.304
     [841]  0.144  1.104  0.296  0.616  0.856 -0.576  0.664 -1.664 -0.544 -0.744
     [851] -0.576  0.824 -0.096 -0.096  0.664 -0.584 -0.096  0.544  0.176  0.696
     [861]  0.304  1.704 -0.544  0.264 -0.376  0.744  0.376 -0.576  0.024  1.704
     [871] -0.696 -0.424 -0.376 -0.736  0.144 -0.016  0.216  0.576 -0.384  0.384
     [881] -1.704  0.744 -0.224  0.384  0.664 -1.136 -0.376 -0.296  1.104 -0.376
     [891] -0.136  0.096  0.104  0.056 -0.136 -0.944 -0.144  0.664 -0.376 -0.736
     [901]  0.904  0.336 -0.304 -0.544  0.616  1.376 -0.584 -0.416 -0.496  0.136
     [911]  0.576 -0.576 -0.536 -0.336  0.696  0.936 -0.144 -1.144  0.064  0.536
     [921]  0.136 -0.296  0.864 -0.664  0.304  0.384 -0.896  1.704  0.704 -0.336
     [931]  0.224 -0.096 -0.336  1.344 -0.544  0.224  0.224  0.664 -0.536  0.624
     [941]  1.704  0.864  0.344 -0.104  0.016  0.024  0.744 -0.896  0.256 -0.264
     [951]  0.504  1.664 -0.096  0.384 -0.536  0.176  0.696 -1.744  1.136 -0.056
     [961] -0.744  0.304 -0.256 -1.336  1.504  0.296 -0.904  0.824 -0.304  1.104
     [971] -0.216  0.056 -0.504  0.176 -0.136 -0.336  0.184 -1.056 -0.856  0.376
     [981]  0.496  0.504 -0.144  1.376 -0.304 -0.744  1.744 -0.384  0.096  1.696
     [991] -0.544 -0.096 -1.336 -0.176 -0.144  1.136 -0.216  0.696  0.224 -0.056
    [1001] -0.336 -0.256  0.384  0.904 -0.264 -0.096 -0.144 -0.376  0.784  0.504
    [1011]  0.264 -0.104 -0.544 -0.416 -0.704 -0.704 -1.704  1.696  0.856  1.096
    [1021] -0.904  0.696 -0.096  0.096  0.504  0.224 -0.384 -0.904 -0.104  0.384
    [1031]  0.864  0.304 -0.496 -0.624 -0.304 -0.696 -0.336 -0.096 -0.424 -0.464
    [1041]  0.856  0.256 -0.304 -0.384 -0.576 -0.096 -0.384 -0.696  0.216  0.144
    [1051]  0.064 -0.624  0.424 -0.296  0.696  0.664  0.536 -0.936  0.504  0.304
    [1061] -0.296 -0.664 -0.376  0.464 -1.344 -0.864 -1.064 -1.304  0.056 -0.216
    [1071]  1.224 -0.056 -0.904  0.064 -0.544 -1.384 -0.304  1.744  0.744 -0.736
    [1081] -0.864  0.696  0.304  0.104  0.336  0.136  1.136 -0.224  0.176 -0.504
    [1091] -0.664 -1.696  0.056 -0.104  0.136  0.336  1.104  0.144 -1.104  1.224
    [1101] -0.696 -0.744 -1.104 -0.576  0.304  0.136 -1.336 -0.064  1.744 -0.104
    [1111] -1.296  0.856  0.336  0.584 -0.256  1.696 -0.064  1.696 -0.784 -0.096
    [1121] -0.224 -0.104  0.304 -0.064 -1.744  1.096 -0.744  0.664  0.696  1.096
    [1131] -0.424 -0.336 -0.856 -1.136  0.296  0.856  0.224 -1.224  0.696  1.336
    [1141]  0.224 -0.664 -0.224  1.104 -0.264 -0.856  0.144 -0.416  0.224 -0.544
    [1151] -0.896  1.664  1.224  0.104 -0.024 -0.776  0.744 -0.336  1.144  1.704
    [1161]  0.784 -0.336  0.544 -0.376  0.376 -0.144  1.664 -0.144  0.856  0.744
    [1171]  0.256  0.584 -0.696 -1.336  1.064 -0.864  0.304  1.344  0.104  0.064
    [1181]  0.784  0.304  0.304  0.744 -0.736  0.256  0.176  0.176 -0.736  0.104
    [1191]  0.264  0.224  0.864 -0.224 -1.704 -0.496 -0.664  0.056  0.544 -0.424
    [1201]  0.384  0.184  0.224 -1.104 -0.136 -1.664 -0.664 -0.536 -1.384  0.144
    [1211] -1.664 -0.696  0.776 -0.584 -0.736  0.576 -0.896 -0.104  0.944 -1.136
    [1221]  0.184  1.376  0.304  0.024 -0.416 -0.056  0.904  0.296  0.544 -0.304
    [1231]  0.696 -0.304 -0.664 -0.104 -0.544  0.856 -0.376  0.224 -0.544 -1.056
    [1241]  1.504 -0.736 -0.064 -0.736  0.104  1.296  0.224 -0.664 -0.096  1.056
    [1251] -0.544  1.704  0.496  0.584  0.496 -0.056 -1.344 -0.704  0.616 -1.664
    [1261] -1.304 -0.216 -0.336  0.944 -0.056 -0.544  0.536 -0.304  0.424 -0.224
    [1271] -0.864 -0.144  1.704  1.296  0.904  1.104  1.336  0.504  0.544  0.536
    [1281] -0.736  0.904  0.096 -0.016  1.344 -0.336 -0.184 -0.936  0.296  0.136
    [1291] -0.784 -0.064 -0.904 -0.344 -0.104 -0.224 -0.224  0.184 -0.304  0.544
    [1301] -0.416 -0.584  0.784  0.904 -0.824  0.504  0.704 -0.136 -0.904  0.856
    [1311]  0.296 -0.024  0.336  1.224 -0.224  0.224  0.496  1.096 -0.784 -0.776
    [1321]  0.224 -0.536 -0.416  0.064  0.104 -0.544  0.536  1.224 -0.904  0.904
    [1331] -0.336  1.144 -0.584 -0.504 -0.664 -0.584 -1.224  0.224  0.176 -0.696
    [1341]  1.664  0.144 -0.696  0.696  0.896  0.336 -0.576 -0.936  0.416  0.744
    [1351] -0.496 -0.104  0.136  0.904  0.144  0.064 -0.176 -0.944 -0.856 -0.096
    [1361] -1.344  0.944 -1.056 -0.664  0.864  0.496  1.504 -0.176 -0.224  0.576
    [1371] -0.304 -1.224  0.384 -0.056  0.824 -0.736 -0.256 -0.216 -0.064  1.504
    [1381]  0.584 -0.944  0.144  0.864  0.576  1.504 -0.384  0.504 -1.296  0.264
    [1391] -0.304  1.344 -0.664 -0.344  1.696 -0.144  0.336 -0.064 -0.784  1.104
    [1401]  0.096 -0.056 -1.136 -0.744 -0.256  0.296 -0.376 -0.584  0.104  0.536
    [1411] -0.104  1.144  0.856  0.096 -0.104 -0.136 -0.216 -0.376  1.504 -0.536
    [1421] -0.304  0.344 -0.536  1.064 -1.336  1.336 -0.664 -0.224  0.584  1.664
    [1431]  0.064  0.624 -1.744 -0.384 -0.584  0.744 -0.264 -0.104 -1.744 -0.056
    [1441]  0.664  0.104 -1.144  0.064  0.664 -0.776  0.416  0.184  0.024 -0.864
    [1451] -0.136  0.424  1.696  0.336 -0.096  0.896 -0.664  0.576 -0.416 -1.336
    [1461]  0.784 -0.744 -0.064  0.336 -0.776  0.144 -0.264 -0.424 -0.576 -0.064
    [1471]  0.904  0.416  1.336  1.696 -0.224  0.664 -0.624 -0.864  0.384  0.536
    [1481] -0.944  0.536  0.536  0.544 -1.336 -1.136  0.304  1.336  0.176 -1.304
    [1491] -0.624 -0.104  1.064  0.744 -0.064 -0.864 -0.224 -1.144  0.304 -1.376
    [1501] -0.496 -0.536 -0.304 -0.576  0.096 -0.864 -1.144 -1.664  0.904 -0.176
    [1511] -0.184 -0.256 -0.864  0.576 -0.944  1.376 -1.376 -0.424 -0.664  0.056
    [1521]  0.904  0.896 -1.224 -0.904  0.424  0.576 -0.144  0.184  0.064 -0.664
    [1531]  0.104 -0.864  1.184  0.096 -0.464  0.256  0.104  1.224 -0.304 -0.744
    [1541]  1.096 -0.136  0.464 -0.904  0.064 -0.536  0.616 -0.624  1.384  0.544
    [1551] -1.144 -0.056  0.256  1.336 -0.944 -1.104 -0.576 -0.376  0.304 -0.104
    [1561] -0.664  0.104 -0.064  1.696  0.544 -0.384  0.264 -1.296 -0.904 -0.224
    [1571]  0.744 -1.136 -0.744  1.304 -0.104  0.256 -1.664 -0.096 -1.136 -0.224
    [1581]  0.496 -0.576 -0.144 -0.336 -0.304 -0.184  0.144  0.016  0.144  0.424
    [1591]  0.664 -1.304  0.896 -0.736  0.544 -0.736  0.144 -1.224 -0.176  0.536
    [1601] -0.696  0.216 -0.336 -0.504  1.376 -0.584  0.576 -0.224  0.776 -1.144
    [1611]  0.536  0.624  0.176  0.536 -0.184  0.144 -1.096 -1.376 -0.936 -0.864
    [1621]  0.616  1.344 -0.304 -0.744 -0.096  0.224  0.584  0.024 -0.464  0.264
    [1631]  0.344 -0.544 -0.544 -0.056 -0.584 -0.864 -0.864 -0.264  0.056  0.704
    [1641]  1.184  1.064  0.376  0.336 -0.096 -0.696 -0.944 -0.696  0.016 -0.544
    [1651] -0.944  1.136 -0.136  0.896  1.704 -0.696 -0.936 -1.696 -0.864 -0.224
    [1661]  0.384 -0.304  0.224  0.664 -0.304 -0.144 -0.824 -1.744 -0.904  0.104
    [1671]  0.016 -0.776  0.904  0.064  0.056 -0.096 -0.504 -0.744  0.904 -0.424
    [1681]  1.384 -0.864  0.776  0.856  0.136  0.216  0.424  0.336  0.496  0.624
    [1691] -0.256 -1.384  0.384  0.376 -1.136 -0.384 -0.704 -1.104 -0.056 -0.104
    [1701]  0.384 -1.224  0.704  0.256  0.736 -1.144  0.144  0.304 -1.136  0.336
    [1711] -0.376 -0.504  1.136 -0.696  0.224  1.744  0.344 -0.584 -1.296  0.496
    [1721]  0.624  0.064 -1.304 -0.104 -0.024  1.144 -0.224  0.264  0.104  0.056
    [1731] -0.744  0.864 -0.584  0.376  0.104  1.144 -0.304  0.624  1.104 -0.096
    [1741]  1.136  0.304  0.696 -0.736 -0.936  0.336  0.096  0.424 -0.936  0.544
    [1751]  0.896  1.136  0.344 -1.344 -0.424  1.296  0.144 -0.776 -0.056  0.744
    [1761] -1.144  0.224  1.096  0.424  0.136 -0.624 -0.864 -1.304  0.256 -0.936
    [1771] -0.336 -0.144  0.096 -0.304 -0.064 -0.256  0.696 -0.496  1.344  0.096
    [1781]  0.136  0.104  0.736  1.136 -0.536 -0.304  0.136  0.544 -0.304 -0.096
    [1791]  0.744  1.104 -1.504 -0.224  0.056  1.336 -0.176 -0.144  0.864  0.224
    [1801]  0.896 -0.864 -0.864 -0.264  0.944  0.504 -0.744 -0.696  0.544  0.856
    [1811] -0.296 -0.304  0.584 -0.544 -0.024 -0.504 -0.096  0.024  0.336 -0.584
    [1821]  1.104 -0.064  0.216 -0.296 -0.904 -0.104  0.576 -0.224 -0.744 -0.104
    [1831]  0.896  0.944  0.896 -1.136  0.176 -0.504 -1.384 -1.136  0.704  0.544
    [1841]  0.304 -0.544  1.344  1.096 -0.144 -0.136 -0.944  0.016  0.416  0.696
    [1851]  0.376 -0.224  0.296 -0.584  1.744 -0.664  0.096  0.096 -1.696 -0.576
    [1861]  0.776 -0.136  0.416 -0.856 -0.944 -0.304 -0.584 -0.904 -0.544  0.936
    [1871] -1.696  0.544  0.696 -0.296  0.496 -0.864  1.184 -0.216  1.296 -0.336
    [1881]  0.096 -0.424 -0.296  0.784 -0.376 -0.736 -0.056  0.744 -0.424  0.744
    [1891] -1.064 -1.224  1.136 -0.704 -0.504  0.224 -0.336  0.096  0.056  0.336
    [1901] -0.256 -0.216 -0.184  0.896  0.944 -0.304 -0.296  0.616  0.856 -0.344
    [1911]  0.384 -0.616 -0.664  0.896  1.376 -1.064 -0.696 -0.864  0.136 -1.064
    [1921] -0.864 -0.144  1.056  1.336  0.224  0.904 -0.856  0.256  0.136  1.056
    [1931] -0.664  0.144 -0.104  0.136  0.864 -0.864  0.504  0.616  0.664 -0.664
    [1941]  0.856  0.176 -0.264  0.696 -0.696 -0.064 -0.944 -0.296  0.536  0.544
    [1951]  0.336  0.144 -0.504  0.096 -0.896  1.504 -0.384 -0.664  0.664  0.944
    [1961] -0.664 -0.584  0.576  0.864  0.304 -0.624 -0.064  0.304 -0.264  0.144
    [1971]  1.104 -0.584 -0.096  0.136 -1.296  1.064 -0.424  1.744  0.336 -1.744
    [1981]  0.864 -0.576 -0.904  0.824  0.136 -0.696  0.736  0.576 -0.896 -0.536
    [1991]  0.176 -1.224  0.544  0.696 -1.384  0.144 -1.376 -0.104 -0.296  0.416
    [2001]  1.096  0.224 -0.064  0.336  0.464  0.136 -0.936  1.144  1.696  0.264
    [2011] -1.304 -0.256 -0.216  0.304 -1.704  0.576 -0.024 -0.264 -1.304 -0.096
    [2021]  0.416  0.216 -0.576 -0.736  1.344 -0.096  0.384  0.064  0.544 -0.064
    [2031]  0.664 -1.704 -0.536  0.216  0.544  0.136  0.064  0.216 -0.296  0.064
    [2041]  0.936 -1.104 -0.736  0.944  0.824 -0.744  0.256  0.424  1.224  0.304
    [2051] -0.064 -1.104 -0.544 -0.376 -0.384  1.296  0.864 -0.224 -0.136 -0.584
    [2061] -0.296  0.296 -1.184  1.504 -0.064  0.696 -0.544  0.664  0.064  0.224
    [2071]  0.376  0.216  0.696 -0.904 -0.584 -0.064  0.536  0.784  1.344 -0.936
    [2081]  0.864  0.736 -1.744 -0.144 -0.144  0.096  1.064 -1.064  0.736 -0.384
    [2091] -0.664  1.104  1.224 -0.616  0.536 -1.184 -0.736  0.296  0.056  0.624
    [2101]  0.384  0.216  0.216  0.176  0.256  0.664 -1.744 -0.856 -1.704  0.376
    [2111]  0.896 -0.736 -0.936  0.096  0.104  1.144  0.576  0.144 -0.104 -0.056
    [2121]  0.224  0.736 -0.376 -0.336  0.864  0.344 -1.096  1.744 -0.584  0.384
    [2131] -0.776  0.304  1.224  1.136  0.616  0.136 -0.704  0.184  1.056  1.504
    [2141]  0.104 -1.336 -1.376  0.864 -0.176 -0.264  0.544 -0.224 -0.504 -0.224
    [2151]  1.136 -0.256 -0.224 -0.016 -0.704  0.256  0.296  0.056  0.944  0.944
    [2161] -0.536 -0.384  0.256 -0.136 -1.104  0.376 -0.504  1.144  0.416 -0.336
    [2171]  0.944  1.184 -1.296 -0.864  0.536  0.624 -0.744 -0.264 -1.376 -1.704
    [2181] -0.384  0.856 -0.864  0.736 -1.096 -0.384 -0.216  1.096 -0.224 -0.584
    [2191]  1.104 -0.304  0.544  1.144 -1.704 -0.144 -0.904  0.256 -0.176 -0.664
    [2201]  0.936 -0.736  0.744 -0.384 -1.224  0.376  0.024 -0.624 -0.304 -0.904
    [2211]  1.376  0.104 -0.016 -0.296 -0.864 -1.184 -0.536  0.856  0.184  0.056
    [2221] -0.064  0.336 -0.064 -0.696 -1.056  0.904 -0.704  0.096 -0.096  0.384
    [2231] -0.696  0.184  0.616 -0.584  0.344 -0.856 -0.224 -0.664 -1.136  0.664
    [2241] -0.376 -1.096 -0.224 -0.744  0.936 -0.064  1.664  1.336  0.416  0.904
    [2251] -1.384 -0.424  1.104  0.096 -0.384  0.144  0.696 -0.144  1.064  1.744
    [2261] -0.544 -0.304 -1.136 -0.904  0.904  0.344 -0.504  0.904 -0.704 -0.504
    [2271]  0.896  1.144 -0.296  0.504  0.496 -0.504  0.424 -0.424  0.896  0.144
    [2281] -0.904  0.544 -0.896 -0.136 -0.144 -0.256 -0.544  1.504 -1.144 -0.304
    [2291]  1.104  0.576  0.104 -0.464 -0.144  0.416  0.144 -0.296 -1.344  0.224
    [2301] -0.224  0.336 -0.136  0.864  0.776 -1.384  0.584 -1.096  0.376 -0.584
    [2311]  0.336 -0.504  0.336  1.104  0.376 -1.224 -1.376  0.064 -0.064 -0.864
    [2321] -1.296  0.216 -0.336  0.304  0.136 -0.704 -0.224  0.896 -0.784 -0.496
    [2331]  0.384 -0.744  1.296 -0.384  0.424 -0.336 -1.304 -0.856 -0.016  0.544
    [2341]  0.544 -0.344 -0.496  0.136 -0.504  0.104 -0.376 -0.696 -0.784 -0.616
    [2351] -0.384  0.304  0.016  0.824  0.584  0.384 -0.024 -0.544  0.864 -1.304
    [2361] -1.304  1.096  0.224  0.216  0.664 -0.896 -0.904 -0.904 -0.056  0.264
    [2371] -0.536 -1.696 -1.704 -0.144 -0.504  0.176 -0.224  1.296  0.944  0.176
    [2381]  0.216 -1.664 -0.584 -0.384 -1.144  0.696  1.336 -1.104  1.184 -0.376
    [2391] -0.864 -0.056 -1.104  0.056  0.256  0.064  1.096  0.344  0.024  0.376
    [2401] -1.056  0.264 -0.056 -0.224  0.104 -0.544 -0.544 -0.824  0.336 -0.016
    [2411]  1.384 -1.184 -0.536  1.104 -0.184  0.376 -0.024 -0.304  0.944 -1.096
    [2421] -0.376  0.856  0.744  0.096  0.256  0.904  1.744  0.856  0.336  0.864
    [2431] -0.944  0.576  1.144 -0.784  0.904 -0.096  0.064  0.744  0.256  0.376
    [2441] -1.104 -0.904 -0.064 -0.264  0.384  0.696 -0.696  1.296  0.104 -1.064
    [2451] -0.224 -1.184 -0.016 -0.856  0.216 -0.344  0.104  0.384  0.544  0.376
    [2461] -0.104  0.064 -0.536 -0.696  0.024 -0.224  1.224 -0.624  0.704  0.544
    [2471]  0.784  0.304 -1.144 -0.304  0.464 -0.136 -0.224 -0.896  0.096 -0.896
    [2481] -0.104 -0.416 -0.496 -1.504  0.104 -0.336  0.136 -0.264 -0.864 -0.264
    [2491]  1.296  0.176 -0.944 -0.744  1.304  0.136  0.576 -0.544  0.144  0.896
    [2501] -0.496 -1.184 -0.896  0.704 -0.304  0.224  0.256 -0.056  0.536  0.376
    [2511] -0.224 -0.304  0.136  0.704 -1.304  0.056  0.176  0.864 -0.576 -0.544
    [2521] -1.136 -0.256  0.176 -0.496 -0.056 -1.136  0.904 -0.096 -0.904 -0.256
    [2531] -0.296 -0.136 -0.504  0.624  0.176 -0.744 -1.136 -0.096 -0.376  0.096
    [2541] -0.664 -0.776 -0.104 -0.384 -0.664  0.336  0.296 -0.696  0.744 -0.736
    [2551] -0.016 -0.944  0.936  0.176 -0.416 -0.824 -1.136 -0.624 -0.304 -0.784
    [2561] -0.104  0.616  1.296  1.664 -1.696 -0.744 -0.696  0.376 -1.376  0.664
    [2571]  0.136  0.336 -0.336  0.136  0.744 -0.064 -0.096 -1.104  0.944  1.224
    [2581] -1.384 -0.944  0.416  0.384 -0.104 -0.696 -0.496 -1.104  1.144  0.336
    [2591]  0.376  0.696  1.064  0.464 -0.264  0.216 -0.584 -0.024  0.544 -0.896
    [2601]  0.024 -0.544 -0.944 -0.584  0.296 -1.136 -1.376  0.864  0.264  0.024
    [2611] -0.584  0.856  0.064  0.224 -1.744  0.664 -0.064  1.296 -0.384  0.224
    [2621]  0.544  0.664 -0.944 -1.304  0.344 -0.216  0.336 -0.056 -0.504 -0.384
    [2631]  0.224  0.136  0.536  0.336 -0.024  0.496  0.384  0.736 -0.736 -0.144
    [2641]  1.104  0.056 -0.296 -0.224  0.736 -0.544  0.144 -0.864 -0.064  0.096
    [2651]  0.784 -0.256 -1.224  0.176 -0.264 -0.696 -0.576  0.744  0.096  0.376
    [2661]  0.184 -0.376 -0.304  0.224 -0.104  0.936 -0.296  0.776 -0.576 -0.664
    [2671]  1.664  0.104 -1.296  0.784 -0.584  0.904 -1.056 -1.056 -0.496 -1.344
    [2681]  0.696  0.304 -0.864 -0.576  0.104 -0.776  1.504  0.856 -0.416  0.744
    [2691] -0.216 -0.224  0.904 -0.696 -1.344  0.896 -0.864 -1.336 -0.696  0.144
    [2701] -0.144 -0.184 -0.944  0.144  0.584 -0.096  0.544  0.744 -0.336  0.224
    [2711] -0.536 -1.296  0.224  0.104 -1.504  1.376  0.056  0.536  0.264 -0.376
    [2721]  0.304  0.056 -1.056 -0.256 -0.096 -0.696  0.016 -0.144 -1.104 -0.056
    [2731]  1.504 -0.184 -0.544  0.104  0.104  0.104  0.616  0.224  0.416  0.256
    [2741] -0.304  0.864  0.136 -0.144 -0.096 -1.696  0.904 -0.104  0.744 -0.136
    [2751]  0.216 -0.576 -0.264  0.664 -1.704 -0.104 -0.056 -0.304  0.856 -0.624
    [2761] -0.944 -0.144  1.096  0.104 -0.216  1.664 -1.696  0.376  0.744  0.096
    [2771]  0.504 -0.304 -1.296 -0.336  0.304  0.176  0.576  0.016 -0.064 -0.384
    [2781]  0.104 -1.104 -0.424  0.736 -0.584  0.336 -0.904  1.344  0.944  0.944
    [2791]  0.016  0.544 -0.096  0.584  0.664  0.176 -0.384  1.144 -0.264 -0.064
    [2801] -1.136  0.904 -0.264 -1.304 -1.136 -1.376 -0.536 -1.104  0.464  0.584
    [2811] -0.136 -0.264 -1.056 -0.024  1.664  1.304 -0.056 -1.376  0.176  0.384
    [2821]  0.496 -0.544 -0.584 -0.504 -0.256  0.264 -0.056  0.416 -0.176 -0.144
    [2831]  0.536 -0.904 -0.216 -0.536  0.696  0.184  1.104  0.104  0.624 -0.296
    [2841] -0.376 -0.896  0.776 -0.384  0.664  0.304 -0.176 -0.576 -1.304  1.696
    [2851] -0.896 -1.136 -1.064 -0.904 -0.536  0.336 -0.824  0.176 -0.096  0.584
    [2861] -0.304  0.376  0.696 -1.184  0.904  0.304 -1.136  0.856 -0.264 -0.136
    [2871]  0.216 -0.544 -0.584 -0.256  1.296 -0.696  0.304 -0.224 -0.064 -1.096
    [2881] -0.704  0.696  0.544 -0.304  0.904  0.056 -0.904 -1.376  0.264  0.096
    [2891] -0.496 -0.664 -0.136 -1.096  0.856  0.856 -0.304  0.576  1.224 -1.144
    [2901] -1.144  0.544 -1.064  1.144  0.496  0.304 -0.576  0.944 -0.384 -0.856
    [2911] -0.176 -0.864  0.304  0.296  0.064 -0.744 -0.384 -1.144  0.944 -0.056
    [2921] -0.416  0.904  1.104 -0.256 -0.944  0.504 -0.304 -0.904 -0.336  0.936
    [2931]  0.504 -0.544  0.224 -0.056  1.336  0.744 -0.944  0.704  1.376 -0.696
    [2941]  1.744  0.736 -0.576  0.384  0.336  0.544 -0.864 -1.336  0.704  0.264
    [2951]  0.904 -0.696 -1.144 -0.216  0.264 -1.104 -0.304  0.496 -0.464 -0.336
    [2961]  0.536 -0.664 -1.056 -0.536  0.904 -1.664  0.504 -0.016  0.096  0.104
    [2971] -0.104  0.776  0.736 -0.056 -0.056  0.024  1.184 -1.376  0.056 -0.544
    [2981]  0.584  1.144 -0.024 -0.224  0.296  1.096  0.296 -0.536  0.096 -1.704
    [2991]  0.704  1.336 -0.664 -1.224  0.064  0.536 -0.464  0.904 -0.664 -1.184
    [3001] -0.296  0.904 -0.496 -0.896  1.504 -0.336 -0.056 -0.264 -0.864  0.904
    [3011] -0.384 -0.216 -0.024 -1.104 -0.424  0.904  0.744  0.544  0.696  0.224
    [3021]  0.744  0.136  0.176 -0.856  0.504 -0.576 -0.144 -1.344 -0.944 -0.616
    [3031] -0.496  0.064 -0.384  0.664 -0.704  0.136 -0.864 -0.856 -1.184  0.736
    [3041] -1.696  0.024 -0.496  0.304  0.256 -0.064  0.936  0.144 -1.104  0.256
    [3051]  0.104  1.664  0.736 -0.024 -0.744  0.584 -0.864 -1.136  0.216  0.216
    [3061] -1.224 -0.896 -0.904  1.056  0.504  0.536  0.064 -1.664 -0.216  1.696
    [3071]  1.056 -0.616  1.144  0.176  0.104 -0.744  0.384  0.864 -0.056 -0.664
    [3081]  0.824 -0.856  0.096  0.944  0.064  0.864 -0.336 -0.496 -0.664  1.304
    [3091]  0.336 -0.024 -0.136 -0.544 -0.864 -0.144 -0.536 -0.336  0.304 -1.744
    [3101]  0.384 -0.464 -0.736  1.136 -0.144  0.576  0.136 -1.336  0.224  1.336
    [3111] -1.696 -0.544 -1.136  0.376  0.824  0.024 -0.664 -1.304 -0.616  0.104
    [3121]  0.016 -0.344 -0.136 -0.064  0.136  0.024  0.776 -0.696 -0.224 -0.264
    [3131]  0.576 -0.696 -0.424  0.696 -0.536  0.224  0.776 -0.064 -0.584  0.296
    [3141] -0.216  0.296 -0.224  0.624 -0.544  1.184  0.184 -0.144  0.096  1.224
    [3151]  0.096 -0.584 -0.184 -0.424  0.056 -0.544  0.416  0.224 -0.336 -0.384
    [3161] -1.184  0.496  0.384  0.936  0.696 -1.136  1.224 -0.496 -0.864 -0.856
    [3171]  0.064 -0.336 -0.496  1.296 -0.064  0.536  0.384  0.696 -0.944  1.344
    [3181]  0.896  0.736 -0.696  0.224  0.584  0.144 -0.544 -0.176  0.304 -0.576
    [3191]  0.224  1.184 -0.544 -1.136  0.216  0.944 -0.696  0.024  0.064 -0.704
    [3201] -0.736  0.376  0.064  0.864 -0.296  1.104 -0.584 -0.056 -0.376  0.536
    [3211] -0.744  0.704 -0.304  0.544 -0.536 -1.144 -0.224 -0.136 -0.224 -0.144
    [3221] -0.056 -0.096 -0.336 -0.224 -1.136  0.704  0.584 -0.744 -0.384  1.104
    [3231] -0.144  1.104  0.616  0.064 -0.896  0.384 -1.096 -0.224  0.584  0.176
    [3241]  0.824 -1.056  0.496 -0.144 -0.136  0.104  0.376 -0.864  0.376  0.864
    [3251] -1.704  0.624  0.064 -0.256  0.904  0.096  0.824 -0.944  0.896  0.256
    [3261]  0.496  0.064 -0.056 -0.136 -0.144 -0.264 -0.376 -1.064  0.344 -0.216
    [3271] -0.584 -0.664 -0.016  1.104 -0.464 -1.336  1.104 -0.344 -0.496 -0.064
    [3281]  0.696  0.216 -1.144  0.144  0.304 -0.904 -0.144  0.056 -0.304  0.304
    [3291]  0.736 -0.384  0.704 -0.104  1.184 -0.384 -0.856 -0.504 -1.376  0.744
    [3301] -0.256  0.696  0.056 -1.304  0.304 -0.256 -0.104  0.664 -0.664 -0.176
    [3311]  0.616  0.864 -0.496 -0.144  0.664  0.904  0.944  0.384  0.464  0.776
    [3321] -1.744 -0.664  0.304  0.304  1.184 -1.696  0.304  0.264 -0.144  0.944
    [3331]  0.224  0.224  1.704 -0.144  0.096 -0.136 -0.304 -0.096 -0.144  0.136
    [3341]  1.384 -0.176 -0.864 -0.496 -0.896  0.864 -0.264  0.776 -0.144 -0.424
    [3351] -1.184  0.176 -0.376  0.736  0.056  0.136  0.184  0.944 -0.136 -0.056
    [3361] -1.104 -0.664  0.256  0.864  0.304 -1.064 -0.904  0.024 -0.336 -1.224
    [3371]  0.144  0.864  0.184  0.536 -1.704  0.576 -0.464 -0.016  0.224 -0.384
    [3381]  0.544 -0.384  0.104  0.256 -0.704 -0.416 -0.776 -0.776  0.696 -0.664
    [3391] -0.896  0.296  0.616 -0.664 -1.376 -0.264 -0.336 -0.216 -0.064  0.224
    [3401] -0.384  0.944  0.904  0.864  1.296 -1.504  0.064  0.304  0.544  0.296
    [3411] -0.864  0.216  1.304 -0.696  0.024 -1.144 -1.696  1.056 -1.056 -0.696
    [3421] -1.344 -0.256  0.264  0.104 -0.056  0.504 -0.944 -0.336 -0.944 -0.064
    [3431]  0.024 -0.944 -0.304  0.776  1.096  0.416  0.416  0.904  0.336  0.776
    [3441] -0.704  0.296  0.136 -0.424 -0.024  0.424 -0.216  0.304 -0.344  0.224
    [3451]  0.064  0.304  0.096  0.736 -1.064 -0.496 -0.016  0.744 -0.096  0.064
    [3461] -0.424 -0.344  0.096  0.304 -0.736 -0.664  0.776  1.224  0.736  0.256
    [3471]  0.704  0.256  0.616 -0.584 -1.064  1.144 -1.344 -0.416 -1.376 -0.576
    [3481]  0.336 -0.864  0.216 -1.696  0.464  0.944  0.576  0.416 -0.176  0.544
    [3491] -0.904 -1.336  0.256  0.336 -0.136 -0.744  0.336 -1.064  0.336  0.584
    [3501]  0.264  0.936  0.576  0.144 -0.016 -0.224 -0.624  1.056  1.696  0.536
    [3511]  0.024  0.704 -0.296  0.536  0.264 -0.496 -0.544  0.784  0.216 -0.936
    [3521]  0.544 -1.336  0.504  0.344  0.744  0.864  0.824  0.424 -0.376 -0.304
    [3531] -0.056  0.064 -0.904  0.504  0.696  1.296 -1.296 -0.344 -0.056  0.064
    [3541]  0.544  1.136  0.336  0.424  0.704 -0.336  0.136 -1.664 -0.744  1.296
    [3551] -0.536 -0.224  0.384 -0.384 -0.256 -1.664 -0.536  1.384  1.336  0.504
    [3561]  0.904  1.704 -0.064 -0.544 -0.504  0.136 -0.064 -0.136  0.384  0.464
    [3571]  0.064 -0.696  0.024  0.064  1.144  0.096  0.304 -0.616 -0.744 -0.856
    [3581]  0.864  0.224  1.136 -0.296  0.264 -0.424  0.624  0.944 -0.896 -0.056
    [3591]  0.584  0.896 -0.376 -0.096  0.304  0.104  0.144  0.424 -0.616  0.776
    [3601] -0.904  0.784 -0.744  0.496  0.056  0.584  0.864 -0.464 -0.536 -0.584
    [3611] -0.216 -1.056 -0.624 -0.416 -0.296 -0.544  1.224 -0.416  0.224  0.904
    [3621]  1.664 -0.576  0.584  0.416 -0.064  0.256  0.256 -0.384  0.264  0.904
    [3631]  0.096 -0.784 -0.544 -0.664  0.064 -0.776 -0.304  0.624 -0.584 -0.504
    [3641] -1.744  0.544 -0.176  0.224 -0.576 -0.416  0.144 -0.584 -0.224 -1.344
    [3651]  0.016  1.096 -0.136  0.264 -1.096 -0.104 -0.496 -0.096 -1.184  0.664
    [3661] -0.336  1.144 -0.256 -1.144 -0.176  0.424  0.056  0.376 -0.616 -0.296
    [3671] -1.184  0.024 -0.424  0.864 -0.416  0.624  0.304 -0.896 -0.856 -0.584
    [3681]  0.496 -1.104  0.904  0.104  1.744 -0.384 -0.024  1.384 -0.864 -0.864
    [3691] -0.624  1.096  0.064 -0.664  1.104  0.536  1.104  0.864 -0.696 -0.264
    [3701]  0.944  1.744  1.376 -0.744 -0.224 -0.304  0.256  0.176  0.736  0.536
    [3711] -1.304  0.224  0.856 -0.696 -0.144  0.104  0.904 -0.696  0.616  1.344
    [3721]  0.064  0.224 -0.224 -0.024 -0.376  0.696  0.136 -0.704  0.216  0.584
    [3731] -1.504  0.744 -0.176  0.304 -0.184 -0.336 -0.376 -0.504  0.584  0.376
    [3741] -1.144  0.296  0.824 -0.184  0.064  0.616  1.136  0.056  0.904  1.704
    [3751]  0.576  1.224 -0.304  1.664  0.424  0.496  0.576 -0.064  0.496 -0.904
    [3761] -0.696  1.704 -0.856  0.224  0.384  0.584 -0.136 -0.904  1.184 -0.304
    [3771] -0.096  0.904 -0.696 -0.336  1.064 -0.216 -0.504  0.624  1.376 -0.256
    [3781] -1.336  0.904 -0.336 -0.216  0.696  0.096  0.904  0.536  0.736 -0.176
    [3791]  0.424 -1.096 -0.624 -0.544 -0.016 -0.864  0.296 -0.136  1.056  0.536
    [3801]  0.144 -0.696  0.944 -0.536 -0.096 -1.696  0.504 -0.104  0.704 -0.056
    [3811]  0.264 -0.704  0.864 -0.336 -0.384 -0.024  1.504  0.664 -0.424  0.416
    [3821] -0.384  1.144 -0.384  0.856  1.136 -0.576  0.336  0.304  0.696 -0.736
    [3831] -0.424 -1.104  0.896  0.904  0.304  0.336  1.304 -0.296 -0.904  0.056
    [3841] -1.744  1.136 -0.024  0.056  0.104  0.536  0.056 -1.224  0.736 -0.536
    [3851] -0.704  1.184 -0.384  0.224  0.336 -0.376 -0.704 -0.224  1.304  1.104
    [3861]  1.296 -0.536 -0.744  0.304  0.824 -1.104  0.736  1.136 -0.424 -1.344
    [3871] -0.584 -0.544  0.904 -0.536  0.176  0.304 -0.224  0.176  0.104  0.144
    [3881]  0.256  0.296  0.864 -0.944  0.584  1.336 -0.304 -0.584  0.336  0.304
    [3891] -0.296 -0.704  0.296  1.296 -1.296 -0.336  0.496 -0.584  0.936  0.144
    [3901]  0.696  0.224  0.264  1.376  0.136  0.504 -0.544 -0.416 -0.544 -0.056
    [3911]  0.776  1.336 -0.584  0.296  0.496 -0.944 -0.496 -1.664 -0.504  0.376
    [3921] -1.056  0.584 -1.376  0.296  0.056 -0.264 -0.744  0.544  0.744  0.624
    [3931]  0.704  0.064  0.576  0.056 -0.504  0.896  0.096  1.696  0.536  0.776
    [3941] -0.184 -1.696  0.104 -0.384  0.624 -0.944  0.664  0.216  0.304  1.136
    [3951]  0.336  1.696 -0.664 -1.704  0.024  0.136 -0.216 -0.096 -1.144  0.224
    [3961]  1.104  1.296  0.504 -0.704 -0.904 -0.376  0.096 -0.536 -0.256 -0.336
    [3971]  0.904 -1.056  0.744 -0.136  1.344 -0.744  0.584 -0.384 -0.144  0.264
    [3981] -0.696  0.136  0.264 -0.896 -1.144 -1.504 -0.744  0.136  1.336 -0.096
    [3991]  0.584 -0.376 -0.744  1.104  0.896  0.944 -0.216  1.744 -0.584 -0.784
    [4001]  1.504 -0.176 -0.296  0.216 -0.896  0.736  0.416  1.096  0.736 -0.136
    [4011]  0.224 -0.024  0.304 -0.776 -0.056 -0.856  0.304 -0.064  0.704 -0.664
    [4021] -0.776 -0.544  0.544 -1.304 -0.296  0.536 -0.704 -0.064  0.304 -1.224
    [4031]  0.704 -0.304  1.704 -0.216 -0.616 -0.224  0.304 -0.304  1.104 -0.904
    [4041] -0.304 -0.256 -0.696 -0.096 -1.144 -0.536 -0.264 -0.416  0.064 -1.296
    [4051] -0.416  0.056  0.864 -0.176 -0.136 -1.224 -0.736 -1.136  0.296 -0.416
    [4061] -0.216 -0.584  0.624 -0.944 -0.384 -0.544  1.336 -0.416  1.336 -0.104
    [4071]  1.144 -1.184  0.104  0.176  0.096  0.904 -1.136 -1.184  0.504 -0.024
    [4081] -0.624  0.856  0.624 -0.904  0.536 -1.704  0.704  0.384 -0.936  0.136
    [4091]  0.496  0.856 -1.704 -0.304 -0.504 -0.584 -0.584 -1.344 -0.496 -0.776
    [4101] -0.384  0.696 -0.576 -0.824  0.224  0.536  1.224  0.824 -0.584  0.144
    [4111] -1.376 -0.064 -0.416 -0.176  0.096 -0.336  0.504 -0.704  0.544  0.584
    [4121] -0.216  0.584  1.696  0.176  1.704 -1.664  1.096  0.064  0.384  1.376
    [4131]  1.336  1.384 -0.496 -1.664  0.736 -1.064 -0.944  0.664 -0.696 -0.504
    [4141]  0.664  1.056  0.216  0.384 -0.176 -0.336  0.664 -0.584 -0.056 -1.056
    [4151]  0.024  0.896  0.256 -0.064 -0.176  0.864  0.304 -0.344 -0.464  0.296
    [4161]  0.664 -0.136 -1.704 -0.296 -0.944 -0.256  0.184  0.176 -0.824 -0.776
    [4171]  0.104  0.304 -0.064  0.696  0.504 -0.496  0.744  0.024 -0.504 -0.336
    [4181]  0.944 -0.856 -0.944  0.064 -0.224  0.256  0.496 -0.104  0.376 -0.696
    [4191] -0.224  0.576 -0.224 -0.864  0.744  0.296  0.176 -0.256  0.256  0.736
    [4201] -1.696 -1.184  1.136 -0.224  0.136 -0.696  0.096  0.024  0.056 -1.504
    [4211]  0.696 -0.384 -0.624  0.944  0.784 -0.704  1.384 -1.296  0.536 -0.856
    [4221] -0.256  1.224  0.304 -0.416 -0.784 -0.504 -0.584  0.744  0.136  1.104
    [4231] -0.584 -0.384  0.336 -0.536 -0.496 -0.176 -0.536 -0.944  0.584  0.224
    [4241]  1.104  0.304  0.336 -1.504 -0.336  0.776 -1.224 -0.224  0.376  0.104
    [4251]  0.136 -0.056 -0.664 -0.104  0.256  0.184 -0.424 -0.264 -0.096 -0.544
    [4261]  0.576 -0.416 -1.384  1.744  0.264  0.024 -0.584  0.896 -0.744 -0.504
    [4271] -0.536 -0.056  0.336 -0.336 -1.504 -0.304 -0.384  0.896 -1.144  0.024
    [4281]  0.664 -1.504 -0.664  1.184  0.104  0.896 -0.904 -1.104  0.904 -1.184
    [4291] -0.024  0.104 -0.176 -0.336  0.424  0.104  0.064  0.536  0.856 -1.336
    [4301] -0.864  0.264  0.264  0.704 -0.136  0.104 -0.856  0.264 -0.544 -0.384
    [4311] -0.776 -0.384  0.384  0.504  0.544 -0.344 -0.384  0.104 -1.104  0.064
    [4321]  1.376  0.776  0.224  0.304  0.544 -0.664 -0.464  0.664 -0.296  0.504
    [4331]  0.744 -1.504  0.096 -1.184 -0.424  0.144  0.856  0.496  0.496  0.304
    [4341]  0.104  0.776  0.464 -0.264 -0.664  0.424  1.336  0.664 -1.376  0.336
    [4351] -0.944 -0.944  0.296 -0.776  0.384 -0.064  0.696  1.704  0.904  1.136
    [4361]  0.536  0.336  0.504 -0.224 -1.224 -0.144  0.344 -0.576  0.696 -0.256
    [4371]  0.224  0.736  0.704  0.896 -0.064  0.304  0.176 -0.056  0.056  0.736
    [4381] -1.664 -1.136 -0.016  0.904  0.696  0.896 -1.704  0.136  0.744  0.664
    [4391] -1.304  0.544  0.744 -0.264  1.096  0.416 -0.696  0.056  0.904 -0.296
    [4401]  0.024  1.064  0.664  1.744 -0.704  0.584 -1.344 -0.064 -0.544  0.584
    [4411]  0.384 -0.696 -0.064  0.264  0.944  1.144  0.496  0.384  0.416  1.144
    [4421]  0.296 -1.344 -0.496  0.256  0.584 -0.224  0.384 -0.624  0.184 -0.224
    [4431]  0.256 -0.704  0.304 -1.304 -0.944  0.704 -0.424 -0.704 -0.744  0.384
    [4441]  1.056  0.296 -1.344 -0.224 -0.664 -0.736  1.304 -0.544  0.936  0.384
    [4451]  0.056  1.104  0.296 -0.304 -0.216  0.544 -1.296  0.104 -1.184 -1.504
    [4461]  0.176 -0.824  0.896 -1.504 -1.304  0.864 -0.056  0.896 -0.016  0.064
    [4471] -0.144  0.904 -0.024 -0.216 -0.944 -0.136  0.904 -1.296  1.056  0.144
    [4481] -1.096  1.384  0.296  0.056  0.576 -0.776 -0.016  1.384 -0.776  0.856
    [4491] -0.704  0.304 -0.136  0.864 -0.864 -0.136 -0.136 -0.136 -0.744  0.664
    [4501] -0.664  0.096  0.744 -0.056 -0.264  0.056 -1.384 -0.216  0.784 -1.336
    [4511]  0.856  1.136  0.736  0.904 -0.664 -0.864 -0.144  0.224  0.336  0.744
    [4521] -0.896 -0.424  0.376  0.864 -0.056  1.376  0.496  0.704  1.744  1.104
    [4531] -0.416 -0.304  1.144  0.696  0.384 -0.544  0.664  0.536 -0.944 -1.144
    [4541]  0.216  0.696 -0.304  0.904  0.464 -0.056  0.216 -0.936 -0.744  0.776
    [4551]  1.056 -0.744 -0.024  0.544  0.744  0.304 -0.264 -0.624  1.336  1.744
    [4561]  0.016 -1.384 -0.056 -0.384 -1.136  0.576 -0.104 -0.384 -0.024 -0.104
    [4571] -0.464 -1.144 -0.144 -1.504 -0.424 -0.064  0.224 -1.744 -0.296  1.504
    [4581] -0.104 -0.856  0.256 -0.224  0.216  0.904  0.336 -0.024  0.936  0.256
    [4591]  0.576 -0.744  0.504 -0.136 -1.304 -0.384 -0.504 -0.504 -0.744 -0.024
    [4601]  0.624  0.776 -0.736  0.056 -0.536  0.696  1.096  0.496  0.024  0.824
    [4611]  0.464 -0.576 -0.056 -0.584 -1.504  0.304 -0.064  1.744  0.096  0.776
    [4621]  0.504 -0.096  0.544  0.376 -0.144  0.256  0.064 -0.144  0.224  1.144
    [4631]  0.536  1.696  0.216 -0.544 -1.704  0.144 -0.696 -0.064 -0.336 -0.336
    [4641]  1.296  0.016 -1.296  0.944 -0.504 -0.024  1.184  0.304 -0.944  0.536
    [4651]  1.744  0.736  0.864 -0.304 -0.536 -0.904  0.584  0.336 -0.776 -0.336
    [4661] -0.896  0.016 -1.304  0.376  0.664 -1.336 -0.064  0.944  1.344  0.696
    [4671]  0.256 -0.536 -0.704  1.344  0.336  0.344 -0.264 -0.864 -0.896 -0.744
    [4681]  0.296  0.944  0.216  0.744  1.104  0.536 -0.784  0.696  0.904 -0.464
    [4691] -0.584 -0.696  0.704 -0.216  0.384 -0.224  0.856 -0.176  1.296 -0.184
    [4701]  1.096 -0.496  0.344 -0.696  1.056  0.776  0.304 -1.696  0.296 -0.336
    [4711] -0.384 -0.616 -0.576 -0.224 -0.104  0.224  1.344  0.704  0.416 -1.144
    [4721] -1.104  0.296  1.104 -0.496  1.344 -0.616  0.464  0.704  0.384 -1.144
    [4731] -1.184 -0.736  0.536  1.136  1.144  0.056 -0.056 -0.224  0.776  0.296
    [4741] -0.344 -0.056 -0.544 -0.104  1.136 -0.536  0.304 -0.296  0.896  0.224
    [4751] -0.144  0.856  0.256  0.336  0.464  0.696  0.736  0.144  0.744 -0.304
    [4761]  0.384  0.424  1.376  0.664 -1.184  0.504 -0.864 -0.624 -0.576  0.064
    [4771] -0.224 -0.416 -0.224 -1.696 -0.824  0.544  0.016 -0.584  1.696  0.136
    [4781]  0.224  0.384 -0.536  0.336  0.584 -0.464 -0.864  0.736  0.296  0.304
    [4791]  0.704 -1.104 -0.064  0.504 -0.336 -0.296  0.184  0.024 -0.176 -0.224
    [4801]  0.064  0.304 -0.696  1.744  0.136 -0.104 -0.176 -0.744  0.096  0.144
    [4811] -0.184 -0.744  0.136 -0.184  1.096  0.776 -0.576 -0.904  0.224  0.704
    [4821]  0.216  1.296 -0.104  0.256 -1.104  0.144  0.064  0.544  0.416  0.384
    [4831]  0.176  0.296  0.896  0.336  0.296 -0.056  0.544 -0.024 -0.416  0.384
    [4841]  0.216  0.416 -0.064 -0.136  1.344 -0.256  0.264 -1.136  1.144  0.104
    [4851]  0.056  0.904  0.864  1.096 -0.376  0.864  0.744  0.744  0.576  0.616
    [4861]  0.096 -0.224  0.624 -0.784 -0.336  0.216 -0.904  1.136 -0.864 -0.256
    [4871]  0.296 -0.416  0.576 -0.104  0.904  0.896 -0.896  0.904  1.144 -1.224
    [4881] -0.464 -0.224 -0.064 -0.056  0.416  0.176  0.144 -0.544  1.376  0.856
    [4891] -0.336 -0.056 -0.224  0.104 -0.296  0.256 -0.664 -1.224 -0.264  0.896
    [4901] -0.696 -0.496 -0.856 -0.464 -0.376  0.944  0.424  0.944 -0.664  1.064
    [4911]  1.224 -0.104 -0.424 -0.376  0.576  0.904 -0.544  0.896 -0.416  0.664
    [4921]  0.584 -1.504 -0.784  0.176  0.024  0.056  0.624  0.704 -0.616 -1.296
    [4931]  0.376  1.504  0.904  0.064 -0.576  0.096 -0.096  0.056  0.536 -0.584
    [4941]  0.136  0.776  1.136 -0.904  0.224  0.176  1.104  0.136 -1.136 -0.064
    [4951]  0.344  0.056 -0.776  0.576 -1.144 -0.176 -0.896 -0.296  0.944 -0.416
    [4961]  0.016  0.224  1.384 -0.184 -0.504  0.544  0.696 -0.224  0.696 -0.696
    [4971] -0.664 -0.104  0.104 -0.424  1.096  1.344 -0.936 -0.584 -0.536 -1.096
    [4981]  1.704  0.776 -0.144  0.144  0.696  0.664  0.096  0.856  0.216 -0.824
    [4991]  1.504  0.144 -0.384  0.344 -1.376  0.184 -0.064 -0.136  0.384  0.224

## Estimate Dist under H0 {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
p_H0 <- data.frame(stat = H_0) |>
  ggplot(aes(x = stat)) +
  geom_histogram() +
  #geom_vline(xintercept = c(left_threshold, right_threshold), col = "tomato") +
  theme_bw()
p_H0
```

<figure>

</figure>

## Find Reject Region

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
left_threshold <- quantile(H_0, .025)
right_threshold <- quantile(H_0, .975)
```

## Estimate Dist under H0 {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
p_H0 +
  geom_vline(xintercept = c(left_threshold, right_threshold), col = "tomato")
```

<figure>

</figure>

---

[← Power {#power .title}](01-power-power-title.md) · [Up: contents](index.md) · [An Alternative Hypothesis →](03-an-alternative-hypothesis.md)
