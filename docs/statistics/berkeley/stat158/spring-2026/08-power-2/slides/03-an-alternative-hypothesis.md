---
title: An Alternative Hypothesis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/08-power-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# An Alternative Hypothesis

**Source:** [`08-power-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/08-power-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## An Alternative Hypothesis

Consider a constant shift of 1 for all units.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
tau <- 1
```

## From data to schedule

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
my_obs_sched <- my_data |>
  mutate(Y_0 = ifelse(d_i == 0, y_i, NA),
         Y_1 = ifelse(d_i == 1, y_i, NA)) |>
  select(i, Y_0, Y_1)

my_obs_sched |>
  gt() |>
  tab_header(title = "My Observed Schedule")
```

<style>#cidcfyxnya table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#cidcfyxnya thead, #cidcfyxnya tbody, #cidcfyxnya tfoot, #cidcfyxnya tr, #cidcfyxnya td, #cidcfyxnya th {
  border-style: none;
}

#cidcfyxnya p {
  margin: 0;
  padding: 0;
}

#cidcfyxnya .gt_table {
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

#cidcfyxnya .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#cidcfyxnya .gt_title {
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

#cidcfyxnya .gt_subtitle {
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

#cidcfyxnya .gt_heading {
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

#cidcfyxnya .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#cidcfyxnya .gt_col_headings {
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

#cidcfyxnya .gt_col_heading {
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

#cidcfyxnya .gt_column_spanner_outer {
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

#cidcfyxnya .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#cidcfyxnya .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#cidcfyxnya .gt_column_spanner {
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

#cidcfyxnya .gt_spanner_row {
  border-bottom-style: hidden;
}

#cidcfyxnya .gt_group_heading {
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

#cidcfyxnya .gt_empty_group_heading {
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

#cidcfyxnya .gt_from_md > :first-child {
  margin-top: 0;
}

#cidcfyxnya .gt_from_md > :last-child {
  margin-bottom: 0;
}

#cidcfyxnya .gt_row {
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

#cidcfyxnya .gt_stub {
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

#cidcfyxnya .gt_stub_row_group {
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

#cidcfyxnya .gt_row_group_first td {
  border-top-width: 2px;
}

#cidcfyxnya .gt_row_group_first th {
  border-top-width: 2px;
}

#cidcfyxnya .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#cidcfyxnya .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#cidcfyxnya .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#cidcfyxnya .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#cidcfyxnya .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#cidcfyxnya .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#cidcfyxnya .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#cidcfyxnya .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#cidcfyxnya .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#cidcfyxnya .gt_footnotes {
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

#cidcfyxnya .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#cidcfyxnya .gt_sourcenotes {
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

#cidcfyxnya .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#cidcfyxnya .gt_left {
  text-align: left;
}

#cidcfyxnya .gt_center {
  text-align: center;
}

#cidcfyxnya .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#cidcfyxnya .gt_font_normal {
  font-weight: normal;
}

#cidcfyxnya .gt_font_bold {
  font-weight: bold;
}

#cidcfyxnya .gt_font_italic {
  font-style: italic;
}

#cidcfyxnya .gt_super {
  font-size: 65%;
}

#cidcfyxnya .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#cidcfyxnya .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#cidcfyxnya .gt_indent_1 {
  text-indent: 5px;
}

#cidcfyxnya .gt_indent_2 {
  text-indent: 10px;
}

#cidcfyxnya .gt_indent_3 {
  text-indent: 15px;
}

#cidcfyxnya .gt_indent_4 {
  text-indent: 20px;
}

#cidcfyxnya .gt_indent_5 {
  text-indent: 25px;
}

#cidcfyxnya .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#cidcfyxnya div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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
my_alt_sched <- my_obs_sched |>
  mutate(Y_0 = ifelse(is.na(Y_0), Y_1 - tau, Y_0),
         Y_1 = ifelse(is.na(Y_1), Y_0 + tau, Y_1))

my_alt_sched |>
  gt() |>
  tab_header(title = "My Alt Schedule")
```

<style>#cgolyaqyym table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#cgolyaqyym thead, #cgolyaqyym tbody, #cgolyaqyym tfoot, #cgolyaqyym tr, #cgolyaqyym td, #cgolyaqyym th {
  border-style: none;
}

#cgolyaqyym p {
  margin: 0;
  padding: 0;
}

#cgolyaqyym .gt_table {
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

#cgolyaqyym .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#cgolyaqyym .gt_title {
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

#cgolyaqyym .gt_subtitle {
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

#cgolyaqyym .gt_heading {
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

#cgolyaqyym .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#cgolyaqyym .gt_col_headings {
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

#cgolyaqyym .gt_col_heading {
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

#cgolyaqyym .gt_column_spanner_outer {
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

#cgolyaqyym .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#cgolyaqyym .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#cgolyaqyym .gt_column_spanner {
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

#cgolyaqyym .gt_spanner_row {
  border-bottom-style: hidden;
}

#cgolyaqyym .gt_group_heading {
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

#cgolyaqyym .gt_empty_group_heading {
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

#cgolyaqyym .gt_from_md > :first-child {
  margin-top: 0;
}

#cgolyaqyym .gt_from_md > :last-child {
  margin-bottom: 0;
}

#cgolyaqyym .gt_row {
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

#cgolyaqyym .gt_stub {
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

#cgolyaqyym .gt_stub_row_group {
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

#cgolyaqyym .gt_row_group_first td {
  border-top-width: 2px;
}

#cgolyaqyym .gt_row_group_first th {
  border-top-width: 2px;
}

#cgolyaqyym .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#cgolyaqyym .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#cgolyaqyym .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#cgolyaqyym .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#cgolyaqyym .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#cgolyaqyym .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#cgolyaqyym .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#cgolyaqyym .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#cgolyaqyym .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#cgolyaqyym .gt_footnotes {
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

#cgolyaqyym .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#cgolyaqyym .gt_sourcenotes {
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

#cgolyaqyym .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#cgolyaqyym .gt_left {
  text-align: left;
}

#cgolyaqyym .gt_center {
  text-align: center;
}

#cgolyaqyym .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#cgolyaqyym .gt_font_normal {
  font-weight: normal;
}

#cgolyaqyym .gt_font_bold {
  font-weight: bold;
}

#cgolyaqyym .gt_font_italic {
  font-style: italic;
}

#cgolyaqyym .gt_super {
  font-size: 65%;
}

#cgolyaqyym .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#cgolyaqyym .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#cgolyaqyym .gt_indent_1 {
  text-indent: 5px;
}

#cgolyaqyym .gt_indent_2 {
  text-indent: 10px;
}

#cgolyaqyym .gt_indent_3 {
  text-indent: 15px;
}

#cgolyaqyym .gt_indent_4 {
  text-indent: 20px;
}

#cgolyaqyym .gt_indent_5 {
  text-indent: 25px;
}

#cgolyaqyym .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#cgolyaqyym div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>

<table class="gt_table caption-top" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading header">
<th colspan="3" class="gt_heading gt_title gt_font_normal gt_bottom_border">My Alt Schedule</th>
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
<td class="gt_row gt_right" headers="Y_0">-0.10</td>
<td class="gt_row gt_right" headers="Y_1">0.90</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">2</td>
<td class="gt_row gt_right" headers="Y_0">-0.50</td>
<td class="gt_row gt_right" headers="Y_1">0.50</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">3</td>
<td class="gt_row gt_right" headers="Y_0">1.20</td>
<td class="gt_row gt_right" headers="Y_1">2.20</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">4</td>
<td class="gt_row gt_right" headers="Y_0">-1.40</td>
<td class="gt_row gt_right" headers="Y_1">-0.40</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">5</td>
<td class="gt_row gt_right" headers="Y_0">0.10</td>
<td class="gt_row gt_right" headers="Y_1">1.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">6</td>
<td class="gt_row gt_right" headers="Y_0">-1.00</td>
<td class="gt_row gt_right" headers="Y_1">0.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">7</td>
<td class="gt_row gt_right" headers="Y_0">1.10</td>
<td class="gt_row gt_right" headers="Y_1">2.10</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">8</td>
<td class="gt_row gt_right" headers="Y_0">0.00</td>
<td class="gt_row gt_right" headers="Y_1">1.00</td>
</tr>
<tr class="odd">
<td class="gt_row gt_right" headers="i">9</td>
<td class="gt_row gt_right" headers="Y_0">0.02</td>
<td class="gt_row gt_right" headers="Y_1">1.02</td>
</tr>
<tr class="even">
<td class="gt_row gt_right" headers="i">10</td>
<td class="gt_row gt_right" headers="Y_0">0.50</td>
<td class="gt_row gt_right" headers="Y_1">1.50</td>
</tr>
</tbody>
</table>

## Estimate Dist under HA {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
H_A <- rand_stats(schedule = my_alt_sched, d_i = my_data$d_i, reps = 5000)
H_A
```

       [1]  0.056  1.416  1.664  0.584 -0.136  0.856  1.616  0.624  1.624  1.016
      [11]  1.296  0.616  1.104  0.304  0.256  0.744  1.096  0.096  0.424 -0.096
      [21]  0.264  1.504  1.896  1.704  1.224  0.936  1.056  1.096  1.184  1.184
      [31] -0.176  0.576  0.256  1.016  0.704  0.936  0.456  0.864  1.464  0.816
      [41]  0.656  0.624  0.904  2.104  1.704  0.696  1.456  1.456  0.344  1.704
      [51]  1.696  1.744 -0.104  1.376  0.696  2.136  0.216  0.896  0.264  1.304
      [61]  0.984  0.296  0.416  1.176  1.976  0.824  1.576  0.896  1.736  1.504
      [71]  1.264  1.944  1.504  0.024  1.104  0.896  1.544  1.656  0.304  1.144
      [81]  0.536  0.056  1.376 -0.096  0.944  1.016  1.624  0.864  1.344  1.496
      [91]  0.496  1.296  1.216  0.864  0.896  1.064  0.296  1.016  2.184  0.944
     [101]  1.056  1.264  1.464  0.696  0.656  1.304  1.176  0.944  1.304  0.824
     [111] -0.136  1.504  1.096  0.336  0.736  0.016  1.976  0.664  0.504  1.784
     [121] -0.096  0.296  1.664  0.896  0.304  0.464  1.344  0.984  0.536  0.056
     [131]  1.136  1.344  0.456  0.944  0.704  1.136  1.424  0.936  0.536  0.464
     [141]  0.656  1.024  0.656  1.344  0.744  0.536  1.776  1.136  0.384  1.096
     [151]  1.584  1.776  0.256  1.264  1.016  0.904  1.144  1.704  1.136  0.656
     [161]  1.256  0.296  0.864  1.376  1.224  0.624  1.096  0.856  1.504  0.864
     [171]  0.216  1.656  1.576  1.344  0.584  1.536  0.536  0.816  1.176  0.984
     [181]  0.344  1.944  0.664  1.136  2.176  0.936  0.584  1.664  0.904  1.176
     [191]  0.376  0.256  1.456  0.544  0.384  1.264  1.184  1.504  1.944  1.144
     [201]  0.456  0.296  0.264  0.496  0.704  0.904  1.144  2.104  1.104  1.264
     [211]  0.504  0.904  1.016  0.504  0.936  0.264  1.216  1.704  0.904  0.864
     [221]  0.744  1.104  0.056  0.056  0.584  0.664  1.696  1.504  1.936  0.696
     [231]  0.776  1.176  0.264  1.336  0.296  1.544  0.976  0.304  1.416  0.064
     [241]  2.096  1.304  0.656  0.944  1.536  0.696  1.296  1.096  1.264  0.896
     [251]  0.856  0.464  1.616  1.176 -0.096  1.536  0.256  0.744  0.936  1.544
     [261]  1.064  1.384  1.104  1.136  0.496  0.776  1.256  1.296  0.976  2.104
     [271]  0.816  0.904  1.736  0.096  0.664  1.344  1.104  0.056  0.944  0.464
     [281]  1.936  1.616  1.344  0.856  0.504  0.704  0.296  1.136  1.696  1.016
     [291]  1.696  1.504  0.944  0.696  0.344  0.816  1.944  0.344  1.216  1.296
     [301]  1.016  0.344  0.704  1.744  0.424  0.744  1.424  0.776  0.656  1.776
     [311]  1.304 -0.096  1.664  0.824  0.424  0.776  1.624  1.136  1.744  1.424
     [321]  1.536  0.536  1.256  0.536  1.696  0.496  0.056  0.456  1.144  1.696
     [331]  1.264  0.416  0.304  0.624  1.096  0.304  0.584  0.856  1.136  1.296
     [341]  1.536  1.064  0.424  1.696  1.144  0.936  0.704  0.736  1.064  1.224
     [351]  1.264  0.736  1.096  0.824  1.936  1.056  1.696  1.464  0.056  1.584
     [361]  0.736  0.944  0.536  1.104  1.224  1.096  1.384  0.296  2.136  0.544
     [371]  1.776  1.104  0.656  0.424  1.704  1.144  1.616  0.304  1.296  1.984
     [381]  1.496  0.496  0.616  0.224  0.696  1.944  0.304  1.344  0.704  1.176
     [391]  1.736  2.176  1.536  0.656  1.376  0.976  1.504  0.936  2.096  0.576
     [401]  1.736  0.464  0.496  1.896  0.456  1.216  0.824  0.536  0.504  1.064
     [411]  0.776  1.584  0.856  1.096  0.304  0.256  1.104  0.536  1.416  1.976
     [421]  0.776  1.384  0.024  1.304  0.616  0.376  0.896  1.264  1.264  0.336
     [431]  1.456  1.336  1.424  1.096  0.864  0.864  0.456  0.904  0.216  0.056
     [441]  1.304  1.744  1.944  1.704  1.496  0.344 -0.144  1.496  1.016  1.104
     [451]  0.936  0.744  0.624  0.656  1.776  0.864  1.224  1.416  1.096  2.184
     [461]  0.696  1.896  1.416  0.856  1.504  0.976  0.984  1.024  1.344  0.896
     [471]  0.656  0.416  1.424  1.136  0.096  1.736  0.936  0.104  1.104  0.736
     [481]  0.464  0.544  0.384  1.064  0.704  0.864  1.096  0.696  1.064  0.936
     [491]  0.416  1.424  0.864  0.864  1.536  1.064  1.136  1.064  0.664  1.264
     [501]  0.664  1.696  0.936  1.416  0.704  1.224  0.616  0.976  1.064  1.456
     [511]  0.056  1.336  1.584  0.704  1.344  0.944  1.456  0.736  1.504  1.104
     [521]  1.496  0.896  0.784 -0.144  0.896  0.736  0.896  1.664  0.904  1.936
     [531]  0.264  2.136  0.656  1.544 -0.176  1.064  0.064  0.904  1.576  0.664
     [541]  1.544  1.136  0.776  1.264  0.424  0.944  1.336  2.176  1.464  1.344
     [551]  1.704  0.624 -0.176  1.704  0.856  0.896  1.624  0.824  1.976  0.336
     [561]  0.336  0.504  2.184  1.136  1.224  1.304  1.056  1.376  1.376  2.144
     [571]  0.496  0.576  1.096  1.464  1.136  0.544  1.464  1.944  2.104  1.456
     [581]  0.016  1.256  0.864  2.176  1.584  1.344  0.824  1.056  0.656  0.904
     [591]  1.216  1.784  1.704  1.024  1.016  1.736  0.696  0.984  0.944  1.944
     [601]  1.016  1.896  2.176  1.184  1.536  1.336  0.496  0.456  0.856  0.496
     [611]  1.616  1.344  0.904  1.304  0.824  0.864  0.416  1.056  1.464  0.744
     [621]  0.664  1.064  1.216  1.136  0.464  0.864  1.536  1.096  2.104  1.144
     [631]  1.104  0.864  1.064  1.784  1.024  0.296  0.224  1.104  0.264  0.304
     [641]  0.304  1.464  1.096  1.016  0.584  1.704  0.816  1.416  0.624  0.496
     [651]  0.904  0.256  1.936  0.504  1.104  0.064 -0.104  0.704  0.704  0.856
     [661]  1.096  1.536  0.704  1.104  1.736  1.704  0.856  0.064  1.536  1.224
     [671]  0.664  0.896  1.656  0.736  0.376  1.376  1.664  0.056  1.656  1.184
     [681]  1.096  0.496  1.576  0.904  0.304  1.464  1.296  1.504  1.184  0.576
     [691]  1.544  0.776  0.056  1.296  1.104  0.456  1.064  0.496  1.256  2.096
     [701]  0.744  0.704  1.016  1.616  1.296  2.136  0.536  1.216  1.144  1.096
     [711]  1.216  0.736  0.936  0.496  0.496  0.664  1.304  1.736  0.624  0.664
     [721]  1.784  0.776  0.504  0.504  1.416  0.896  0.736  1.096  1.584  1.104
     [731]  1.304  1.416  1.936  1.224  0.776  0.944  0.584  0.224  1.264  1.936
     [741]  1.576  1.496  1.536  1.336  1.456  0.744  1.016  0.464  0.936  0.824
     [751]  0.984  1.896  1.136  1.136  0.824 -0.136  1.456  0.216  0.944  1.016
     [761]  1.096  0.936  0.416  0.744  1.536  0.336  1.296  0.464  0.736  1.256
     [771]  1.984  1.944  1.496  0.704  1.016  0.656  0.464  0.456  0.696  0.064
     [781]  1.536 -0.096  0.784  0.664  1.216  1.136  0.784  1.696  1.696  0.496
     [791]  0.416  1.296  0.936  1.744  0.504  0.064  0.304  0.576  0.504  1.384
     [801]  1.216  1.216  0.984  0.424  0.896  0.864  1.664  0.584  0.736  1.096
     [811]  0.776  0.584  0.536  0.864  1.056  1.216  0.664  1.016  0.224  1.096
     [821]  1.544  0.776  0.216  0.496  0.936  0.904  0.016  1.416  0.776  0.936
     [831]  0.304  1.544  0.336  1.464  0.824  1.576  0.744  1.584  0.656  0.464
     [841]  1.936  0.544  0.824  2.176  1.744  0.736  0.584  0.576  0.736  0.504
     [851]  1.184  1.664  1.424  1.016  1.104  0.336  1.136  1.184  0.504  1.504
     [861]  1.304  0.824  1.536  1.336  0.944  0.784  1.296  0.376  0.736  1.744
     [871]  0.624  1.536  0.344  1.016  0.304  1.456  0.904  1.696  1.216  1.776
     [881]  1.064  0.896  1.904  1.704 -0.144  0.936  0.896  1.176  1.104  1.056
     [891]  1.264  0.744  1.296  1.264  1.536  1.176  0.416  1.536  1.104  0.896
     [901]  2.104 -0.176  0.664  1.096  1.096  1.064  1.096  1.264  0.904  0.536
     [911] -0.104  0.504  0.456  0.064  0.816  0.744  1.776  0.464  0.904  1.016
     [921]  1.664  1.184  0.816  1.544  0.624  0.496  1.416  0.576  0.776  0.864
     [931]  0.464  1.144  0.696  2.136  1.096  1.504  1.576  1.376  1.584  1.104
     [941]  0.784  0.696  1.376  1.416  1.416  1.336  0.056  0.584  0.896  1.336
     [951]  1.456  1.504 -0.096  0.904 -0.104  0.656  1.144  0.776  0.904  1.264
     [961]  1.136  0.264  1.736  0.224  1.136  1.504  1.224  0.936  1.096  0.744
     [971]  0.424  0.464  1.696  1.584  0.936  0.304  0.584  1.536  0.936  1.176
     [981]  0.704  0.704  1.216  1.424  0.696  1.264  0.696  0.584  0.016  1.104
     [991]  1.256  0.256  1.464  0.744  0.864  1.104  2.144  0.784  1.304  1.224
    [1001]  2.096  1.064  1.256  0.896  0.656  1.104  2.136  0.664  1.736  0.024
    [1011]  1.384  1.944  0.896  0.896  0.696  1.136  1.576  1.104  1.664  1.344
    [1021]  0.944  2.136  0.816  1.096 -0.144  0.944  1.624  1.104  1.664  0.096
    [1031]  1.704  1.064  0.696  1.064  0.296  1.896  2.144  1.024  2.144  1.376
    [1041]  0.584  0.896  0.936  1.576  2.096  0.904  0.264  1.376  0.936  1.416
    [1051]  1.704  1.096  2.184  0.536  1.336  0.736  1.416  1.184  1.464  0.256
    [1061]  0.584  0.216  0.736  1.464  0.896  1.424  1.704  0.824  0.416  0.704
    [1071]  1.544  0.256  1.264  1.256  1.456  1.344  0.584  1.544  0.224  0.256
    [1081]  1.376  1.576  0.936  1.384  0.696  0.664  0.824  0.536  0.864  0.424
    [1091]  0.544  0.936  0.016  1.136  0.864  0.656  1.096  0.104 -0.176  1.184
    [1101]  1.024  0.424  1.784  1.184  1.016  2.184  0.736  0.896  0.944  1.536
    [1111]  0.224  0.904  0.296  1.544  0.704  0.696  1.704  0.656  1.504  0.576
    [1121]  0.416  0.776  1.056  0.624  0.744  0.936  1.336  1.696  0.896  1.336
    [1131]  0.304  0.656  0.824  0.024  1.256 -0.184  0.104  1.264  1.664  0.256
    [1141]  1.744  0.464  0.864  0.464  1.136  0.784  1.536  1.464  1.064  1.624
    [1151]  1.384  1.504  1.256  1.496  1.104  1.536  0.536  1.104  1.776 -0.096
    [1161]  1.736  1.016  1.104  1.264  0.304  1.296  1.664  1.984  1.224  0.664
    [1171]  1.576  0.264  1.104  1.136  1.144  0.656  0.936  1.336 -0.144 -0.136
    [1181]  1.224  1.344  0.744  0.864  0.864  1.016  0.344  0.376  1.904  1.424
    [1191]  0.896  0.424  0.504  0.984  0.736  0.336  0.736  1.704  0.296  0.536
    [1201]  0.544  0.984  1.096  2.176  1.296  0.944  1.416  0.736  1.184  0.064
    [1211]  1.336  1.216  1.944  0.864 -0.144  1.536  0.704  1.736  0.264  1.696
    [1221]  1.304  0.296  0.744  1.096  0.704  1.104  0.656  0.944  1.576  0.504
    [1231]  0.256  0.664  1.696  1.016  1.184  1.304  0.816  0.464  1.304  1.536
    [1241]  1.696  0.696  1.696  1.344  0.696  1.344 -0.104  0.816  0.736  0.696
    [1251]  0.864  1.536  1.376  0.336  0.464  0.536  0.496 -0.136  1.064  1.176
    [1261]  0.824  1.624  0.584  0.536  1.104  1.296  1.944  0.856  1.944  0.776
    [1271]  0.936  1.576  1.104  0.784  1.416  0.264  0.224  0.616  0.296  0.496
    [1281]  0.376  1.336  0.696  1.024  1.504  0.696  1.296  1.776  1.464  1.736
    [1291]  0.936  0.456  1.064  0.976  0.744  1.664  0.696  1.064 -0.184  1.376
    [1301]  0.104  0.904  1.584  1.096  1.344  1.136  0.496  0.976  0.656  0.496
    [1311]  1.896  1.464  0.504  0.224  1.064  0.504  1.104  0.344  0.736  0.416
    [1321]  0.816  0.456  0.896  0.504  1.296  1.376  0.216  0.536  1.536  0.096
    [1331]  0.496  1.296  1.384  0.856  0.664  1.384  1.144  1.336  0.864  1.664
    [1341]  2.176  0.976  0.504  0.976  0.264  1.224  0.496  0.544  1.704  0.656
    [1351]  0.704  1.696  1.704  1.744  0.896  1.056  1.304  0.704  0.944  1.336
    [1361]  2.184  0.424  1.664  0.296  0.544  0.256  1.176 -0.136  1.704  0.544
    [1371]  0.704  0.624  1.536  1.184  0.624  1.936  0.936  1.136  1.144  0.424
    [1381]  0.336  0.824  0.496  1.936  0.424  0.416  2.104  1.576  1.664  0.704
    [1391]  0.064  1.784  1.064  0.944  0.696  0.736  0.776  0.896  1.304  1.144
    [1401]  1.376  0.744  1.424  1.136  0.504  1.536  1.784  0.744  0.696  1.224
    [1411]  1.976  1.504  1.264  1.296  0.296  1.384  1.464  0.256  1.344  0.544
    [1421]  0.496  1.536  1.104  1.256  1.376  0.296  0.544  1.736  1.024  0.736
    [1431]  1.664  1.504  0.904  0.624  0.864  0.024  1.704  0.504  1.144  1.776
    [1441]  1.304  1.704  1.336  0.904  0.496  0.784  1.576  1.064  1.664  1.696
    [1451]  0.584  0.664  0.944  1.544  1.784  1.144  0.944  0.376  1.136  1.896
    [1461]  1.616  1.984  0.936  0.904  1.264  0.624  0.096  1.144  1.944  0.224
    [1471]  1.344  0.816  0.256  1.296  1.536 -0.136  0.304  1.504  0.704  1.904
    [1481]  1.336  0.096  0.816  1.464  1.264  1.784  1.376  1.144  0.536  1.264
    [1491]  1.384  1.064  1.096  1.424  0.896  1.536  0.416  0.944  2.176  0.256
    [1501]  1.096  1.064  0.584  1.264  0.744  1.784  0.936  0.904  1.896  0.984
    [1511]  0.904 -0.096  1.064  1.664  0.656  0.744  1.296  1.704  1.336  0.536
    [1521]  1.304  0.576  1.016  0.496  1.384  0.584  0.856  1.456  0.256  0.056
    [1531]  0.376  0.896  0.936  1.544  0.984  0.576  1.064  1.296  0.784  1.464
    [1541]  1.736  1.024  0.296  1.704  0.984  0.336  1.096  0.896  1.176  1.696
    [1551]  0.384  1.344  0.056  0.856  1.784  1.936  0.816  0.616  1.144  0.736
    [1561]  0.896  1.256  0.384  0.464  1.264  1.344  0.536  0.736  0.416  1.544
    [1571]  1.296  1.056  0.344  1.024  0.736  1.536  0.776  0.696  1.136  1.384
    [1581]  0.936  1.704  1.264  1.024  0.664  0.736  0.456  1.296  0.504  0.504
    [1591]  1.424  1.264  1.304  1.896  0.384  1.944  0.064  0.224  0.904  1.616
    [1601]  0.904  0.416  1.096  1.056  0.256  0.984  0.064  1.104  0.256  0.904
    [1611]  0.744  1.704  1.224  1.944  1.584  1.496  0.656  0.064  1.136  1.424
    [1621]  0.696  1.456  0.784  0.104  0.224  0.504  1.536  0.784  1.416  0.544
    [1631]  1.376  0.536  0.096  1.176  0.256  1.736  0.264  1.656  1.464  1.264
    [1641]  1.264  1.304  0.784  1.144  0.824  1.744  1.136  0.784  1.704  0.056
    [1651]  1.496  0.264  0.744  0.656  1.176  1.936  0.624  0.864  0.296  0.624
    [1661]  0.616  1.696  0.824  1.224  0.864  1.504  1.296  1.136  1.144  0.704
    [1671]  1.456  1.416  1.456  0.536  0.776  0.864  1.584  1.584 -0.104  1.536
    [1681]  0.536  1.096  1.216  0.416  2.096  0.904  0.384  1.016  1.744  0.504
    [1691]  0.496  1.296  1.056  1.336  0.776  0.944  0.464  1.056  1.704  0.904
    [1701]  0.584  1.136  0.344  1.224  0.896  1.536  0.024  1.224  1.064  1.096
    [1711]  0.104  0.824  0.864  1.416  0.536  1.264  0.904  0.064  0.656  1.504
    [1721]  1.224  0.944  1.064  0.936  0.064  0.544  0.984  0.896  0.696  1.184
    [1731]  1.984  0.984  0.904  0.944  0.504  1.904  1.656  1.064  1.464  0.104
    [1741]  1.104  1.936  0.784  0.696  1.096  0.496  0.464  0.296  1.304  1.584
    [1751]  0.784  0.896  0.456 -0.184  0.904  0.896  1.704  0.544  1.504  1.744
    [1761]  1.176 -0.184  1.104  1.064  1.184  1.464  1.224  1.224  0.296  1.376
    [1771]  0.616  0.016  1.616  1.616  1.456  0.856  1.624  1.456  1.696  1.496
    [1781]  1.544  2.176  1.136  0.304  0.864  0.256  0.944  1.184  1.224  0.704
    [1791]  0.944  1.264  1.216  1.944  0.544 -0.104  0.824  0.456  0.296  1.096
    [1801]  1.064  0.656  0.376  1.296  1.536  1.736  0.104  0.656  1.704  1.576
    [1811] -0.096  0.984  1.224  1.056  0.744  1.584  1.704  0.504  1.096  0.856
    [1821]  0.784  1.464  0.704  1.104  1.456  1.064  1.504  1.736  0.904  1.304
    [1831]  0.936  1.296  0.736  1.056  1.264  0.056  1.104  0.856  1.216  0.784
    [1841]  0.984  0.896  1.696  1.936  0.784  1.744  2.136  1.976  1.256  1.424
    [1851]  1.216  0.336  0.624  0.664  1.144  1.376  1.416  0.504 -0.176  0.664
    [1861]  1.464  0.336  1.744  1.024  0.856  1.744  1.064  1.304  0.936  0.576
    [1871]  0.504  1.144  0.664  1.096  0.944  0.736  1.016  0.504  0.304  0.904
    [1881]  1.584  0.696  1.064  0.376  1.696  0.704  1.776  0.936  0.896  1.256
    [1891]  0.416  1.216  0.264  0.896  1.664 -0.176  1.656  1.696  1.176  1.936
    [1901]  1.136  1.104  1.696  0.464  1.104  0.784 -0.184  0.424  0.384  2.184
    [1911]  1.464  0.936  1.304  0.776  1.104  1.584  0.496  2.104  0.776  2.176
    [1921]  0.584  1.264  0.496  1.336  1.256  0.304  0.496  0.904  1.344  1.424
    [1931]  0.424  0.824  1.144  2.104  1.296  0.824  1.456  1.504  1.304  1.296
    [1941]  1.424  1.424  0.736  0.304  2.136  1.744  1.224  1.384  0.904  1.424
    [1951]  0.496  0.256  0.736  0.336  0.464  0.664  1.936  1.456  1.304  1.936
    [1961]  0.784  1.464  1.216  0.864  1.296  1.344  0.976  0.824  0.656  0.296
    [1971]  0.904  1.136  0.536  0.864  0.776  0.024  0.984  1.056  1.416  0.464
    [1981]  1.344  0.936  0.856  1.424  1.504  1.984  0.744  2.136  1.944  1.904
    [1991]  1.696  0.736  1.064  1.464  1.064  1.576  0.664  1.304  0.936  1.464
    [2001]  1.064  1.256  0.696  1.264  0.624  0.616  1.424  0.384  0.984  0.504
    [2011]  0.856  1.504  1.256  1.744  1.104  0.664  1.504  1.304  1.064  1.096
    [2021]  1.136  1.344  1.176  1.096  0.536  1.984  0.944  1.296  0.464  0.384
    [2031]  1.304  0.856  2.144  1.744  0.664  0.256  1.096  0.864  1.256  1.304
    [2041]  0.256  0.896  0.784  0.544 -0.184  0.416  1.096 -0.096  0.504  1.504
    [2051]  0.896  0.944  1.784  0.904  1.576  0.264  1.504  1.424  0.344  1.776
    [2061]  1.896  1.696  1.536  1.184  1.184  0.704  1.496  1.696  1.264  0.536
    [2071]  1.704  1.464  1.344  1.296  0.616  0.904  0.256  1.976  1.344  1.096
    [2081]  2.176  0.944  0.376  2.144  0.696  0.776  0.216  1.704  1.176  0.624
    [2091]  0.784  1.136  1.336  1.776  1.744  0.504  0.584  1.536  0.336  0.504
    [2101]  0.736  1.224  0.984  1.144  0.064  0.376  0.024  1.504  0.096  1.416
    [2111]  0.496  1.096 -0.144  2.144  0.064  0.896  1.696  0.904  0.704  1.376
    [2121]  0.816  1.296  1.664  1.424  0.424  0.944  0.296 -0.096  0.656  1.064
    [2131]  1.416  1.264  1.264  1.704  1.344  1.104  2.184  1.304  1.064  1.744
    [2141]  1.096  0.624  1.264  1.096  1.536  1.336  0.624  1.264  1.624  0.936
    [2151]  0.736  0.496  0.736  0.976  1.136  2.176  0.304  0.464  1.016  1.056
    [2161]  1.496  1.696  0.056  0.936  0.864  1.304  1.264  0.424  0.624  1.496
    [2171]  1.224  2.104  1.416  0.776  1.296  0.576  1.184  1.344  1.264  1.264
    [2181]  1.784  0.864  1.344  1.544  1.536  0.696  1.176  0.344  0.936  0.304
    [2191]  0.416  1.296  1.096  0.256  1.496  0.464  0.976  0.736 -0.136  1.696
    [2201]  1.936  0.464  1.304  1.624  0.984  1.456  0.936  0.896  1.504  0.224
    [2211]  1.504  0.984  0.936  2.104  1.224  0.576  0.504  0.816  1.256  1.144
    [2221]  1.136  0.936  0.984  0.744  1.184  1.184  1.536  1.576  0.904  0.896
    [2231]  0.056  0.744  1.176  0.304 -0.184  0.816  1.256  1.296  0.464  1.096
    [2241]  1.744  1.616  1.704  1.704  1.344  1.376  0.704  0.896  0.304  1.696
    [2251]  0.784  1.464  0.264  0.624  1.336  1.376  0.024  1.344  2.136  1.544
    [2261]  0.904  1.264  0.576  0.296  0.256  1.144  0.544  0.744  0.776  1.096
    [2271]  0.656  0.776  0.656  0.736  1.376  1.936  0.936  2.104  1.296  0.384
    [2281] -0.104  2.104  1.376  1.096  1.936  0.744  0.064  0.664  0.624  1.056
    [2291]  1.016  0.336  0.576  1.536  1.584  1.216  1.344  1.936  0.504  0.656
    [2301]  1.104  0.544  1.976  1.104  0.864  1.664  1.264  1.096  0.624 -0.144
    [2311]  0.856  0.896  0.496  0.064  0.256  1.296  0.264  0.744  0.896  0.904
    [2321]  0.824  1.016  0.224  1.544  1.144  0.256  0.536  1.544  0.456  1.264
    [2331]  1.256  0.656  1.184  1.024  1.696  1.736  0.496  0.584  0.504  1.544
    [2341]  1.496  0.936  1.096  1.056  0.624  1.064  1.144  0.824  0.624  1.416
    [2351]  1.536  0.736  0.264  1.744  1.224  1.976  1.344  0.656  0.264  0.656
    [2361]  0.736  0.696  1.456  1.136  2.104  1.664  0.896  1.376  1.304  1.224
    [2371]  1.224  1.936  1.064  1.416  1.064  0.024  0.656  1.304  0.224  0.904
    [2381]  0.296  1.304  1.696  0.896  1.064  1.776  0.704  0.744  0.856  0.904
    [2391]  0.336  0.256  0.456  0.296  2.184  0.784  1.736  0.856  1.984  0.584
    [2401]  0.304  0.896  1.144  1.376  1.144  0.104  1.184  0.976  1.016  1.096
    [2411]  1.104  0.496  1.104  0.056  1.136  0.896  1.624  0.424  0.664  1.344
    [2421]  1.376  1.064  1.616 -0.176  0.984  1.256  1.496  1.496  0.984  1.096
    [2431]  0.496  0.464  1.536  0.696  1.776  1.536  1.376  0.624  1.976  1.576
    [2441]  0.944  1.184  1.784  0.424  0.624  1.424  1.256  1.544  1.616  1.496
    [2451]  1.344  1.344  1.904  0.504  0.296  0.504  1.776  0.016  0.336  1.464
    [2461]  1.224  0.456  0.544  1.184  1.576  1.656  1.136  0.256  0.576  2.184
    [2471] -0.184 -0.184  1.104  1.416  1.776  1.376  1.224  1.536  1.496  0.296
    [2481]  0.736  1.264  1.784  1.464  0.456  0.896  0.736  1.336  0.896  1.056
    [2491]  0.264  1.336  1.504  0.424  1.336  0.896  1.536  0.296  0.864  0.856
    [2501]  0.896  1.456  2.096  1.064  0.904  0.624  1.504  1.264  1.904  0.856
    [2511]  0.224  1.576  1.144  1.744  0.704  0.464  1.696  1.024  0.856  0.624
    [2521]  0.856  0.976  1.104  0.496  1.664  0.264  1.776  0.104  1.304  1.296
    [2531]  1.344  1.104  0.296  0.864  1.096  1.544  0.704  0.584  1.104  0.056
    [2541]  2.096  0.464  0.784  0.424  0.904  1.136  0.664  0.624  1.576  1.136
    [2551]  0.696  1.296  0.664  1.176  1.336  0.304  0.216  1.336  0.696  0.896
    [2561]  1.984  0.464  1.936  1.376  1.536  0.904  1.144  1.176  0.256  2.184
    [2571]  0.464  0.976  1.136  1.096  0.904  1.424  1.056  0.456  0.296  1.136
    [2581]  0.504  1.456  1.296  1.296  1.016  0.224  1.064  1.136  1.304  1.456
    [2591]  0.816  1.064  1.616  0.704  0.856  1.416  0.624  1.344  2.136  1.104
    [2601]  0.456  1.224  1.344  1.696  0.856  0.296  0.504  1.104  0.096  0.216
    [2611]  1.016  1.136  0.824  0.416  0.336  0.464  0.624  1.536  0.264  1.064
    [2621]  1.496  0.824  1.744  1.096  1.536  1.696 -0.176  1.264  1.136  0.296
    [2631]  0.816  1.096  0.904  1.896  1.304  0.896  0.856  0.536  1.144  0.856
    [2641] -0.104  1.776  1.584  0.936  0.576  0.616  0.896  1.264  1.096  0.776
    [2651]  0.704  1.136  0.304  1.296  0.624  1.904  2.184  0.304  0.856  0.504
    [2661]  1.696  0.496  1.736  0.336  0.224  1.536  0.736  1.184  0.736  1.464
    [2671]  0.976  1.744  0.064  0.864  1.096  0.736  1.096  0.664  1.784  1.024
    [2681]  0.704  1.136  1.536  1.296  0.824  1.144  1.696  1.344  1.136  0.376
    [2691]  1.616  1.504  1.376  0.536  0.256  0.904  0.904  0.864  1.304  0.696
    [2701]  1.664  0.536  2.096  1.296  1.736  0.896  0.936  1.304  0.784  1.064
    [2711]  1.064  0.824  1.704  1.616  1.624  1.416  1.776  1.056  1.544  0.824
    [2721]  1.024  0.944  0.504  0.336  1.616  0.344  1.336  1.984  1.136  1.456
    [2731]  0.856  0.984  0.424  1.264  1.296  1.264  1.376  1.264  0.744  1.424
    [2741]  1.936  1.144  0.696  0.256  0.704  1.296  0.704  1.744  1.224  1.464
    [2751]  0.056  1.296  0.984  1.496  1.136  1.624  1.464  0.536  1.544  0.056
    [2761]  1.224  1.136  1.176  1.016  1.104  0.296  0.424  1.936 -0.104  0.984
    [2771]  0.024  1.296  0.896  1.984  1.264  1.016  0.696  1.224  0.904  1.944
    [2781]  1.344  1.304  1.264  1.464  1.384  0.016  0.416  0.704  1.016  1.696
    [2791]  0.336  1.744  0.296  0.864  0.584  0.856  0.464  1.704  1.544  0.936
    [2801]  0.224  0.304  1.064  1.344  0.304  0.816  0.904  1.424  0.504  0.336
    [2811]  0.256  1.696  0.776  1.736  0.024  0.904  0.896  0.584  1.016  1.136
    [2821]  0.656  1.536  1.576  0.896  0.584  0.256  1.296  1.736  0.104  0.904
    [2831]  0.816  1.696  1.344  1.376  0.776  1.416  1.496  0.536  1.504  0.336
    [2841]  0.936  0.864 -0.176  1.256  1.216  1.536  1.216  1.344  1.776  1.144
    [2851]  1.176  0.976  0.656  0.624  1.704  0.456  1.184  1.464  0.024  0.904
    [2861]  1.184 -0.144  1.176  0.576  1.944 -0.184  1.704  0.696 -0.136  1.904
    [2871]  0.336  0.896  1.944  1.024  0.416  1.344  0.856  1.056  1.016  1.944
    [2881]  1.976  0.816  1.424  0.864  1.376  1.256  1.264  0.696  1.344  1.336
    [2891]  0.624  0.904  0.664  0.864  0.824  1.424  1.464  0.864 -0.104  0.896
    [2901]  1.416  0.504  0.696  1.216  0.696  1.536  1.256  1.024  0.464  0.544
    [2911]  0.824  1.936  1.584  0.784  1.464  0.256  0.224  1.584  1.624  1.104
    [2921]  0.896  1.024  1.464  1.536  1.376  1.696  1.576  1.624  0.984  0.944
    [2931]  0.824  1.936  1.096  0.736  0.544  0.376  0.936  1.176  0.896  0.456
    [2941]  1.344  1.176  0.896  0.056  0.296  0.296  0.424  1.536  1.504  0.056
    [2951]  1.656  0.864  1.216  0.536  1.144  1.304  0.624  1.744  1.504  1.224
    [2961]  0.896  0.824  0.296  1.704  0.304  0.784  1.304  1.616  0.496  1.744
    [2971]  1.704  1.704  1.536  1.136  1.176  0.936  1.296  1.336  0.656  0.296
    [2981]  0.456  0.896  1.584  0.704  0.936  1.464  0.776  1.304  2.136  1.096
    [2991]  1.336  1.544  1.224  1.136  0.776  1.384  1.296  1.496  1.104  0.664
    [3001] -0.184  1.904  1.576  0.464  0.904  2.096  0.304  0.336  0.536  0.696
    [3011]  1.736  1.584  1.544  0.896  0.664  0.104  1.544  0.656  1.536  0.816
    [3021]  1.064  0.896  1.024  0.744  0.464  2.184  0.896  0.616  1.904  1.744
    [3031] -0.136  1.616  0.616  0.496  1.416  0.504  1.336  0.976  0.496  0.416
    [3041]  0.056  1.136  0.936  0.624  1.896  0.056  1.504  1.104  0.704  1.656
    [3051]  0.736  1.584  1.184  1.224  0.624  0.256  1.584  1.696  1.904  0.016
    [3061]  0.856  0.736  0.856  0.664  0.456  0.744  0.656  1.936  0.576  1.456
    [3071] -0.136  1.136  1.744  1.136  0.584  0.496  1.136  0.264  1.696  0.776
    [3081]  1.016  0.216  0.016  1.064  0.744  1.304  1.416  1.544  1.496 -0.136
    [3091]  0.984  1.064  0.744  1.944  1.016  0.864  0.744  1.744  1.176  0.464
    [3101]  0.936  1.104  0.896  0.496  1.576  1.424  0.216  1.176  0.656  1.104
    [3111]  1.016  1.336  1.056  0.456  0.944  1.776  1.056  1.296  0.584  1.136
    [3121]  0.464  0.584  0.504  1.704  0.936  0.584  0.936  1.096  1.536  1.456
    [3131]  1.016  1.744  0.704  1.064  1.656  0.736  1.056  1.576  1.296  0.744
    [3141]  1.296  1.944  1.384  1.544  1.144 -0.184  0.576  1.176  0.784  1.344
    [3151]  1.256  1.104  0.944  0.896  0.496  1.136  1.696  1.456  0.864  1.264
    [3161]  1.184  0.616  1.016  1.744  0.464  1.456  1.696  1.936  1.464  0.256
    [3171]  0.816  1.224  0.696  1.256  0.624  1.064  1.664  0.736  1.584  1.176
    [3181]  0.496  0.896  0.944  1.464  0.424  0.904  1.496  1.344  1.664  0.544
    [3191]  0.584  1.264  1.224  2.104  1.136  1.624  1.144  0.496  1.136  0.896
    [3201]  1.224  0.984  1.056  1.984 -0.176  1.024  1.216  1.696  1.296  0.384
    [3211]  1.784  1.496  1.664  1.696  1.296  1.664  0.784  1.344  0.704  1.496
    [3221]  0.816  1.296  1.504  1.344  1.776  0.536  0.024  0.704  1.376  1.176
    [3231]  0.736  1.064  0.944  1.296  0.256  1.536  0.736  1.064  0.864  0.424
    [3241]  0.504  1.296  1.136  1.184  1.096  1.056  2.184  1.656  1.104  1.016
    [3251]  1.264  0.776  1.616  1.496  0.496  1.656  1.184  1.144  0.416  0.856
    [3261]  0.656  1.184  0.904  1.064  0.944  1.464  0.256  1.016  1.304  0.944
    [3271]  1.104  1.064  1.944  0.856  1.504  1.376 -0.176  0.304  1.464  0.624
    [3281]  0.936  2.144  0.504  0.664  1.936  0.336 -0.104  0.264  1.456  0.344
    [3291]  1.296  0.824  1.344  0.464  1.584  0.584  1.664  0.744  0.976  1.744
    [3301]  2.136  2.184  0.744  1.376  1.536  0.704  1.544  1.304  1.624  0.584
    [3311]  0.344  0.656  1.936  0.936  1.776  0.824  0.936  0.704  0.936  1.176
    [3321]  0.936  0.464  2.144  1.296 -0.136  0.944  1.936  1.736  0.656  1.576
    [3331]  1.264  1.256  2.104  0.496  0.064 -0.136  0.696  1.376  1.144  1.104
    [3341]  1.024  0.416  0.496  0.656  1.336  0.416  1.176  0.976  0.504  1.536
    [3351]  2.136  0.864  0.616  0.944  0.976  1.264  0.104  1.096  0.864  1.256
    [3361]  2.176  0.704  1.424  1.016  1.136  1.784  1.456  0.784  0.824  0.544
    [3371]  0.784  0.496  1.104  1.456  0.864  0.936  0.976  1.744  0.064  1.256
    [3381] -0.136  0.896  0.496  1.584  0.256 -0.144  1.976  2.096  1.304  1.544
    [3391]  1.936  1.304  0.536  0.824  0.656  1.264  0.496  1.616  0.536  1.656
    [3401]  0.776  0.656  0.864  0.696  1.536  0.984  2.096  1.056  1.616  0.976
    [3411]  2.104  1.104  1.264  0.464  0.864  1.536  0.576  1.696  0.696  1.584
    [3421]  1.944  1.024  0.704  0.744  1.136  0.776  1.216  1.224  1.256  0.944
    [3431]  1.104  1.944  1.056  1.296  1.104  1.144  0.256  1.104  0.856  1.176
    [3441]  0.936  1.336  1.064  0.464  1.336  1.144 -0.136  0.824  1.104  0.216
    [3451]  1.144  1.504  1.624  0.704  1.504  0.504  1.216  0.336  0.296  1.344
    [3461]  1.296  1.144  1.256  0.864  1.696  0.704  1.096  0.464  0.064  0.304
    [3471]  1.304  1.024  0.696  0.896  0.824  0.496  1.224  0.304  0.464  1.536
    [3481]  0.496  0.464  0.376  1.504  0.656  0.976  0.464  1.096  0.056  0.904
    [3491]  1.376  0.904 -0.136  1.384  0.624  0.696  0.856  1.064  1.664  1.696
    [3501]  0.296  1.216  1.064  1.376  1.496  0.904  1.696  1.184  0.664  0.216
    [3511]  0.096  0.216  0.456  1.376  0.064  0.904  2.184  0.656  0.056  0.504
    [3521]  1.056  1.096  1.704  1.376  1.544  1.584  0.816  0.856  0.744  0.856
    [3531]  0.944  1.064  0.624  0.696  1.064  1.536  0.984  0.696  1.544  0.576
    [3541]  0.824  1.176  1.216  1.304  1.504  1.536  1.704  0.504  0.704  1.136
    [3551]  0.616  1.576  1.976  1.424  1.264  0.896  0.576  1.064  0.704 -0.104
    [3561]  1.536  0.776  0.696  0.936  1.696  0.064  1.184  1.504  2.096 -0.176
    [3571]  1.064  1.936  1.296  1.144 -0.176  1.256  1.536  0.704  0.896  1.504
    [3581]  0.984  1.504  1.096  0.416  1.536  0.096  0.824  1.304  0.744  0.896
    [3591]  0.504 -0.176  0.024  0.496  1.184  0.936  0.496  0.904  1.336  1.944
    [3601]  0.336  0.464  0.304  0.904  0.424  0.416  1.496  0.496  0.984  0.624
    [3611]  0.784  0.376  1.264  0.064  1.304  1.464  1.144  1.216  0.736  0.504
    [3621]  1.064  0.616  1.456  0.544  1.704  0.424  0.896  1.216  1.256  1.936
    [3631]  0.696  0.656  1.224  1.064  0.456  0.304  1.504  0.056  0.864  0.944
    [3641]  0.856  1.096  0.744  0.056  1.736  0.256  1.504  1.064  0.824  0.704
    [3651]  0.824  0.296  1.504  0.664  2.176  0.296  0.736  0.536  0.464  0.216
    [3661]  1.944  0.464  0.536  0.896  1.296  0.856  0.744  0.984  0.256  1.016
    [3671]  1.064 -0.144  1.096  1.304  1.176  1.576  1.136  0.576  0.616 -0.184
    [3681]  0.904  1.656  0.944  0.496  1.096  1.176  0.904  1.776  0.544  1.984
    [3691]  0.304  1.344  0.064  0.904  1.264  0.824  0.936  1.344  0.384  0.096
    [3701]  1.416  0.544  1.256  1.176  0.464  0.224  1.696  1.984  1.656  1.216
    [3711]  0.784  0.944  0.336  0.896  1.376  1.296  0.936  0.784  1.296  1.704
    [3721]  0.864  0.984  0.704  0.696  0.456  0.624  1.216 -0.144  0.696  0.544
    [3731]  1.024  0.936  1.136  0.536 -0.104  0.704  0.656  1.544  1.064  0.264
    [3741]  0.464  0.696  0.776  1.496  1.376  1.264  0.304  1.056  1.344  1.304
    [3751]  1.584  1.056  1.064  1.056  0.856  1.296  0.464  0.656  0.664  1.296
    [3761]  1.264  0.984  2.184  1.256  1.624  1.224  1.056  1.656  1.536  0.624
    [3771]  1.264  1.056  0.264  0.904  1.136  1.016  1.456  1.456  0.776  1.344
    [3781]  1.104  0.656  2.176  1.776  1.056  1.096  0.264  0.576  0.264  0.096
    [3791]  1.304  1.496  1.376  0.496  0.536  2.136  0.744  1.344  0.736  1.304
    [3801]  0.864  1.504  0.744  1.024  0.864  1.784  0.304  1.464  1.224  0.024
    [3811]  0.304  0.816  0.904  1.056  0.296  1.104  0.496  1.216  1.136 -0.184
    [3821]  0.624  0.504 -0.176  1.056  0.696  1.504  1.096  0.984  0.864  1.256
    [3831]  0.504  0.664  1.096  0.696  0.736  1.424  0.704  1.144  1.376  0.344
    [3841]  1.296  1.696  0.344  0.256  1.624  0.576  0.424 -0.104  0.256  1.384
    [3851]  1.056  0.904  1.696  0.504  0.624  1.064 -0.176  1.496  0.064  0.504
    [3861]  1.336  0.504  1.216  1.224  1.696  0.256 -0.104  0.456  0.736  0.784
    [3871]  1.376  1.536  0.656  1.344  2.096  2.144  0.504  0.776  1.016  0.904
    [3881]  0.696  1.264  1.744  1.496  0.256  0.496  1.136  0.824  1.344  1.736
    [3891]  0.304  0.264  1.376  1.104  0.904  0.856  0.024  1.536  0.736  0.576
    [3901]  0.224  1.936  0.776  0.064  1.096  0.496  1.736  1.264  0.736  1.136
    [3911]  1.504  0.544  1.096 -0.136  0.096  2.104  1.296  1.216  0.264  0.736
    [3921]  1.504  1.224  0.944  1.136  0.944  0.816  1.216  1.536  1.504  1.064
    [3931]  1.136  1.504  1.696  1.216  0.576  2.096  0.736  0.256 -0.184  0.256
    [3941]  0.576 -0.144  0.296  0.664  0.424  1.384  0.976  0.056  1.104  0.984
    [3951]  1.376 -0.144  0.016  1.176  0.056  1.536  0.664  0.856  1.264  0.544
    [3961] -0.184  1.456  0.896  1.576  1.096  1.736  1.416  1.136  1.024  1.144
    [3971]  0.256  1.944  0.456  0.936  1.056  0.936  0.344  1.656 -0.096  1.216
    [3981]  1.136  1.104  0.256  0.736  2.184  1.696  1.216  0.984  1.536  0.744
    [3991]  1.744  1.936  1.376 -0.184  0.536  1.136  0.304  1.096  0.736  0.936
    [4001]  1.104  0.496  0.336  0.536  0.464  0.736  0.904  1.536  1.216  1.264
    [4011]  0.736  0.464 -0.144  1.984  1.744  1.544  0.896  0.584  1.256  1.336
    [4021]  1.344  1.216  1.136  1.096  1.576  1.744  1.496  1.464  1.696  1.464
    [4031]  0.584  1.216  0.544  1.104  0.544  1.304 -0.096  1.224  1.416  1.384
    [4041]  1.144  0.816  1.136  0.496  1.056  0.224  1.224 -0.096  1.016  1.216
    [4051]  1.464  0.896  0.424  1.536  1.496  1.584  1.936  0.344  0.504  0.864
    [4061]  2.096  0.496  1.104  1.144  0.736  1.456  1.224  0.704  1.104  0.664
    [4071]  0.984  0.824  1.744  1.304  0.896  1.656  1.416  1.696  1.736  1.704
    [4081]  0.824  0.736  1.776  1.176 -0.104  0.016  1.344  0.944  0.496  0.456
    [4091]  1.056  1.344  1.416  1.536  0.896  0.016  0.416  0.824  0.696  1.064
    [4101]  0.696  1.504  0.304  0.624  0.944  1.504  1.336  0.864  0.496  0.816
    [4111]  0.784  1.296  1.424  0.944  0.936  1.696  1.384  1.016  1.776  1.136
    [4121]  1.256  1.496  0.536  0.776  0.896  1.144  1.336  0.896  1.424  1.064
    [4131]  0.424  2.104  0.736  0.704  0.504  1.064  1.496  1.696  1.104  1.504
    [4141]  1.224  1.536  2.136  2.104  0.736  1.104  0.464  1.016  1.704  1.696
    [4151]  1.304  0.736  1.024  1.096  0.616  0.304  1.184  1.456  0.504  0.704
    [4161]  0.584  0.344  1.344  1.496  1.664  0.576  0.464  1.264  0.784  1.336
    [4171]  0.336 -0.104  1.424  0.624  1.776  1.104  0.944  0.904 -0.176  0.496
    [4181]  0.456  1.936  0.864  0.864  1.136  0.224  1.744  0.816  0.256  1.424
    [4191]  1.056  1.416  1.016  1.504  1.576  0.896  1.536  1.576  0.056  1.256
    [4201]  1.496  1.464  0.944  1.296  1.304  1.184  0.496  0.984  0.776  1.736
    [4211]  0.656  0.624  1.256  0.776  1.304  0.736  0.656  1.704  1.576  0.536
    [4221]  1.896  0.584  0.784  0.856  1.736  0.224  0.624  0.736  0.984  1.624
    [4231]  0.296  1.264  0.344  1.024  1.256  1.216  1.456  1.344  0.744  1.256
    [4241]  0.736  1.744  0.464  0.744  0.936  0.936  0.704  1.456  1.064  0.656
    [4251]  1.784  0.976  0.536  0.944 -0.176  0.784  0.016  1.064  0.304  0.824
    [4261]  1.264  0.464  0.584  0.704  1.256  0.824  0.736  1.056  1.104  1.096
    [4271]  0.496  0.304  0.624  0.664  1.264  0.024  1.936  1.664  1.776  1.184
    [4281]  1.304  0.504  0.536  0.256  0.584  0.464  0.704  1.264  0.656  1.216
    [4291]  1.264  0.296  0.096  0.624  1.256  0.976  1.744  1.496  1.624  0.984
    [4301]  0.816  0.824  1.424  2.104  1.904  1.736  0.936  0.544  0.936  1.944
    [4311]  0.536  0.576  0.984  0.864  1.136  1.184  0.656  1.016  0.696  1.064
    [4321]  1.096  1.296  1.176  0.904  1.704  1.336  1.304  1.496  0.464  1.656
    [4331]  1.104  1.184  1.376  0.224  1.936  1.136  1.296  0.304  1.104  0.936
    [4341]  1.224  0.736  0.456  1.464  1.304 -0.176  0.736  0.304  0.224  0.544
    [4351]  0.904  0.016  0.904  0.984  0.536  0.936  0.944  0.904  0.024  1.104
    [4361]  0.544  1.616  0.704  1.176 -0.144  0.664  0.816  1.256  0.024 -0.136
    [4371]  1.176  1.704 -0.136  1.224  1.176  1.224  0.896  1.984  0.344  1.064
    [4381]  1.536  1.136  1.104  0.864  1.184  0.944  0.336  0.944  1.056  1.424
    [4391]  1.664  1.896  0.064  1.704  0.824  0.736  0.296  1.576  1.736  1.056
    [4401]  1.016  0.824  0.464  1.464  0.496 -0.096  0.056 -0.136  0.704  1.056
    [4411]  0.664  1.216  0.224  0.376  0.736  0.896  0.744  1.064  1.296  0.704
    [4421]  0.336  1.256  1.016  0.016  1.224  0.736  0.944  1.176  0.896 -0.104
    [4431]  0.464  1.216  1.264  1.936  1.344  0.696  1.696  0.696  0.456  1.136
    [4441]  1.696  1.216  1.104  0.416  0.944  1.064  0.304  0.496  0.424  1.544
    [4451]  1.744  1.256  1.136  1.904  0.984  0.976  0.776  0.936  1.584  0.736
    [4461]  2.104  0.776  0.016  1.024 -0.176  0.264  1.304  1.464  0.536  0.984
    [4471]  1.064  1.056  0.656  1.936  0.504  0.896  1.576  1.776  1.064  1.944
    [4481]  1.736  0.464  0.736  0.464  1.104  1.176  0.744  0.544  0.816  1.024
    [4491]  0.576  0.624 -0.184  1.784  1.136  0.936  1.336  2.184  1.376  0.704
    [4501]  1.744  1.496  1.264  1.344  1.136  1.496  0.296  0.736  0.296  1.056
    [4511]  1.144  1.056  0.736  0.704  0.736  0.896  0.696  1.936  0.256  1.536
    [4521]  1.376  1.096  0.336  0.656  0.376  1.624  0.984  0.984  1.224  0.464
    [4531]  1.256  1.696  0.296  1.376  1.104  1.664  1.136  1.104  1.056  1.744
    [4541]  0.456  0.856  0.064  1.184  1.464  0.416  1.264  0.896  1.416  1.984
    [4551]  0.976  1.696  1.904  0.224  1.256  0.856  1.256  0.736  1.216  1.424
    [4561]  1.216  0.744  1.944  1.376  0.624  1.016  1.096  1.704  1.704  1.096
    [4571]  1.184  1.056  0.064  0.736  0.256  1.704  1.256  1.376  1.384  0.256
    [4581]  1.096  1.096  0.864  1.496  0.496  0.736  0.984  1.064  0.736  0.864
    [4591]  0.496  1.416  0.736  1.096  1.536  0.504  1.096  1.176  0.664  0.376
    [4601]  0.504  0.056  0.464  0.704  1.344  1.336  0.656  0.896  0.776  1.416
    [4611]  0.864  1.704  2.104  0.376  0.624  1.576  0.936  0.624  0.304  1.296
    [4621]  0.824  1.176  1.336  0.536  0.456  1.744  1.024  0.296  1.264  1.296
    [4631]  1.336  1.104 -0.104  1.136  1.336  1.656  0.896  0.024  0.536  0.776
    [4641]  0.424  1.744  0.296  1.944  1.064  1.104  0.704  0.216 -0.144  0.536
    [4651]  1.776  2.176  1.344  1.104  0.296  1.264  1.104  0.984  1.944  1.376
    [4661]  2.096  0.824  1.296  1.376  1.416  1.056  0.856  2.144  1.264  0.304
    [4671]  1.104  0.536  0.904  1.336  0.416  1.144  0.856  0.896  0.336 -0.104
    [4681]  0.464  0.664  1.504  1.696  2.136  0.536  0.544  1.064  1.104  1.064
    [4691]  1.496  0.544  1.264  1.216  0.616  1.536  0.944  0.216  1.696  1.976
    [4701]  1.264  1.264  1.016  0.736  0.944  0.904  1.376  0.936  0.096  0.904
    [4711]  0.264  1.704  0.064  1.504  0.376  1.296  1.704  0.904  1.144  1.384
    [4721]  0.824  0.696  0.744  0.336  1.696  0.696  0.896  0.936  0.656  0.304
    [4731]  0.696  0.896  0.496  1.776  0.744  0.976  1.384  1.704  0.424  0.896
    [4741]  1.744  1.224  1.376  0.264  0.824  1.176  0.616  1.304  0.664  1.336
    [4751]  1.176  0.264  0.544  1.536  1.664  1.536  2.136  1.744  1.304  1.424
    [4761]  1.744  1.496  1.136  1.296  0.744  1.936  1.136  1.304  0.736  0.904
    [4771]  1.016  1.944  1.024  1.264  0.784  1.936  1.416  0.296  0.896  0.256
    [4781]  1.936  1.144  1.416  0.984  0.776  2.096  1.616  1.024  2.104  0.504
    [4791]  0.704  1.216  0.064  1.336  0.744  0.544  0.944  2.176  0.856  0.896
    [4801]  1.104  0.864  1.296  0.416  1.336  1.416  1.504  0.864  0.944  0.816
    [4811]  1.144  0.536  1.464  0.624  0.456  1.216  0.584  0.904  0.824  1.664
    [4821]  0.416  0.904  0.936  0.456  1.056  1.296  1.744  1.176  1.976  0.864
    [4831]  1.304  1.264  0.904  0.056  0.864  1.584  0.624  1.224  0.264  1.544
    [4841]  1.656  0.744  1.216  0.496  1.376  0.544  1.216  2.104  1.664  0.936
    [4851] -0.144  0.336  0.944  1.016  1.344  1.096  1.504  0.664  0.496  0.064
    [4861]  1.424  0.976  0.216  0.544  1.264  0.656  1.744  0.464  0.424  0.896
    [4871]  0.744  0.536  0.656  1.584  1.344  1.184  1.664  0.656  0.744  1.504
    [4881]  0.056  0.016  1.936  0.496  0.944  0.784  1.256  1.176  0.864  0.224
    [4891]  0.496  0.896  0.696  0.016  0.016  0.656  1.064  0.624  1.576  0.944
    [4901]  1.976  1.016  0.464  0.576  0.984  1.944  1.536  0.336  0.936  1.064
    [4911]  0.856  0.424  1.064  0.624  1.696  1.256  0.856  1.376  1.224  0.824
    [4921]  0.624  1.264  0.856  1.064  0.296  0.304  1.736  1.184  1.616  0.536
    [4931]  1.016  1.264  1.064  1.704  0.736  2.176  1.504  0.056  1.144  1.544
    [4941]  1.344  1.504  1.584  1.376  1.944  0.464  1.744  0.464  1.176  1.104
    [4951]  1.096  0.016  0.824  0.744  0.896  1.096  1.024  1.736  0.224  0.864
    [4961]  0.536  0.704  1.224  1.016  0.064  1.984  1.776  1.984  1.096  1.544
    [4971]  0.264  0.576  0.664  1.544  0.016 -0.096  1.256  0.744  0.824  1.384
    [4981]  1.416  1.696  0.656  1.024  1.536  0.296  0.784  1.376  1.184  0.456
    [4991]  1.504  2.176  1.064  0.864  0.744  1.464  0.576  0.624  1.104  0.816

## Estimate Dist under HA {data-id="quarto-animate-title"}

``` {.sourceCode .numberSource .r .number-lines .code-with-copy data-id="quarto-animate-code"}
p_HA <- data.frame(stat = H_A) |>
  ggplot(aes(x = stat)) +
  geom_histogram() +
  theme_bw()
p_HA
```

<figure>

</figure>

---

[← The Null Hypothesis](02-the-null-hypothesis.md) · [Up: contents](index.md) · [Power {#power-1} →](04-power-power-1.md)
