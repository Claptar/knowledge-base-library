---
title: An Alternative Hypothesis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/09-power-3/slides.html
source_file: sources/berkeley-stat158/spring-2026/09-power-3/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# An Alternative Hypothesis

**Source:** [`09-power-3/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/09-power-3/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## An Alternative Hypothesis

Consider a constant shift of 1 for all units.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
tau <- 1
```

## From data to schedule

<style>#zckrickoks table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#zckrickoks thead, #zckrickoks tbody, #zckrickoks tfoot, #zckrickoks tr, #zckrickoks td, #zckrickoks th {
  border-style: none;
}

#zckrickoks p {
  margin: 0;
  padding: 0;
}

#zckrickoks .gt_table {
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

#zckrickoks .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#zckrickoks .gt_title {
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

#zckrickoks .gt_subtitle {
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

#zckrickoks .gt_heading {
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

#zckrickoks .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#zckrickoks .gt_col_headings {
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

#zckrickoks .gt_col_heading {
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

#zckrickoks .gt_column_spanner_outer {
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

#zckrickoks .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#zckrickoks .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#zckrickoks .gt_column_spanner {
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

#zckrickoks .gt_spanner_row {
  border-bottom-style: hidden;
}

#zckrickoks .gt_group_heading {
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

#zckrickoks .gt_empty_group_heading {
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

#zckrickoks .gt_from_md > :first-child {
  margin-top: 0;
}

#zckrickoks .gt_from_md > :last-child {
  margin-bottom: 0;
}

#zckrickoks .gt_row {
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

#zckrickoks .gt_stub {
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

#zckrickoks .gt_stub_row_group {
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

#zckrickoks .gt_row_group_first td {
  border-top-width: 2px;
}

#zckrickoks .gt_row_group_first th {
  border-top-width: 2px;
}

#zckrickoks .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#zckrickoks .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#zckrickoks .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#zckrickoks .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#zckrickoks .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#zckrickoks .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#zckrickoks .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#zckrickoks .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#zckrickoks .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#zckrickoks .gt_footnotes {
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

#zckrickoks .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#zckrickoks .gt_sourcenotes {
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

#zckrickoks .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#zckrickoks .gt_left {
  text-align: left;
}

#zckrickoks .gt_center {
  text-align: center;
}

#zckrickoks .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#zckrickoks .gt_font_normal {
  font-weight: normal;
}

#zckrickoks .gt_font_bold {
  font-weight: bold;
}

#zckrickoks .gt_font_italic {
  font-style: italic;
}

#zckrickoks .gt_super {
  font-size: 65%;
}

#zckrickoks .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#zckrickoks .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#zckrickoks .gt_indent_1 {
  text-indent: 5px;
}

#zckrickoks .gt_indent_2 {
  text-indent: 10px;
}

#zckrickoks .gt_indent_3 {
  text-indent: 15px;
}

#zckrickoks .gt_indent_4 {
  text-indent: 20px;
}

#zckrickoks .gt_indent_5 {
  text-indent: 25px;
}

#zckrickoks .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#zckrickoks div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

<style>#gpuvpnsvzs table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#gpuvpnsvzs thead, #gpuvpnsvzs tbody, #gpuvpnsvzs tfoot, #gpuvpnsvzs tr, #gpuvpnsvzs td, #gpuvpnsvzs th {
  border-style: none;
}

#gpuvpnsvzs p {
  margin: 0;
  padding: 0;
}

#gpuvpnsvzs .gt_table {
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

#gpuvpnsvzs .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#gpuvpnsvzs .gt_title {
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

#gpuvpnsvzs .gt_subtitle {
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

#gpuvpnsvzs .gt_heading {
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

#gpuvpnsvzs .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#gpuvpnsvzs .gt_col_headings {
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

#gpuvpnsvzs .gt_col_heading {
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

#gpuvpnsvzs .gt_column_spanner_outer {
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

#gpuvpnsvzs .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#gpuvpnsvzs .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#gpuvpnsvzs .gt_column_spanner {
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

#gpuvpnsvzs .gt_spanner_row {
  border-bottom-style: hidden;
}

#gpuvpnsvzs .gt_group_heading {
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

#gpuvpnsvzs .gt_empty_group_heading {
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

#gpuvpnsvzs .gt_from_md > :first-child {
  margin-top: 0;
}

#gpuvpnsvzs .gt_from_md > :last-child {
  margin-bottom: 0;
}

#gpuvpnsvzs .gt_row {
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

#gpuvpnsvzs .gt_stub {
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

#gpuvpnsvzs .gt_stub_row_group {
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

#gpuvpnsvzs .gt_row_group_first td {
  border-top-width: 2px;
}

#gpuvpnsvzs .gt_row_group_first th {
  border-top-width: 2px;
}

#gpuvpnsvzs .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#gpuvpnsvzs .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#gpuvpnsvzs .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#gpuvpnsvzs .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#gpuvpnsvzs .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#gpuvpnsvzs .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#gpuvpnsvzs .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#gpuvpnsvzs .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#gpuvpnsvzs .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#gpuvpnsvzs .gt_footnotes {
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

#gpuvpnsvzs .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#gpuvpnsvzs .gt_sourcenotes {
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

#gpuvpnsvzs .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#gpuvpnsvzs .gt_left {
  text-align: left;
}

#gpuvpnsvzs .gt_center {
  text-align: center;
}

#gpuvpnsvzs .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#gpuvpnsvzs .gt_font_normal {
  font-weight: normal;
}

#gpuvpnsvzs .gt_font_bold {
  font-weight: bold;
}

#gpuvpnsvzs .gt_font_italic {
  font-style: italic;
}

#gpuvpnsvzs .gt_super {
  font-size: 65%;
}

#gpuvpnsvzs .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#gpuvpnsvzs .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#gpuvpnsvzs .gt_indent_1 {
  text-indent: 5px;
}

#gpuvpnsvzs .gt_indent_2 {
  text-indent: 10px;
}

#gpuvpnsvzs .gt_indent_3 {
  text-indent: 15px;
}

#gpuvpnsvzs .gt_indent_4 {
  text-indent: 20px;
}

#gpuvpnsvzs .gt_indent_5 {
  text-indent: 25px;
}

#gpuvpnsvzs .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#gpuvpnsvzs div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

       [1]  0.496  1.576  1.144  0.496  2.104  0.856  1.744  1.024  1.384  1.584
      [11]  1.504  0.896  2.176  0.984  0.864  0.304  0.624  1.336  1.704  1.536
      [21]  1.504  1.504  1.104  0.544  1.104  1.976  0.504  0.096 -0.176  1.776
      [31]  0.816  1.744  0.896  0.776  0.656  1.296  1.736  0.864  0.656  0.936
      [41]  0.416  1.496  1.296  1.616  0.904  2.096  1.944  0.624  0.304  0.976
      [51]  1.304  1.064  0.944  1.976  0.736  1.264  0.744  1.704  2.176  1.184
      [61]  1.376  2.144  0.904  1.744  1.696  0.704  0.296  1.416  0.704  1.784
      [71]  0.856  0.496  0.864  0.936  0.864  0.416  0.704  1.704  1.096  1.984
      [81]  1.104  0.664  0.896  1.536  0.656  0.536  0.256  1.096  1.224  0.336
      [91]  0.704  0.696  0.296  1.704  0.464  0.864  0.096  1.616  1.296  1.224
     [101]  0.944  1.104  1.704  0.616  1.456  0.496  0.936  0.936  1.144  0.304
     [111]  0.256  0.904  0.976  1.256  1.784  0.824  1.136  0.984  0.456  1.264
     [121]  1.016  1.576  0.984  0.296  1.064  1.624  0.696  0.936  1.304  1.416
     [131]  1.504  1.584  1.136  0.904  1.096  0.624  0.664  0.264  1.336  1.536
     [141]  0.016  0.576  0.984  1.096  0.944  1.544  0.624  0.704  0.744  1.416
     [151]  0.064  1.104  1.336  0.976  1.344  1.056  1.024  0.056  0.984  0.096
     [161]  1.736  0.656  0.296  0.704  0.696  1.696  0.976  0.344  0.496  1.336
     [171]  1.136  1.496  0.944  0.576  1.656  1.344  1.976  1.496  1.024  1.584
     [181]  0.464  1.304  1.776  1.344  1.096  1.896  2.096  0.096  1.496  1.016
     [191]  0.704  0.776  2.144  0.304  1.904  1.576  1.336  1.696  0.544  1.704
     [201]  0.264  0.056  0.744  0.024  0.064  1.064  0.544  0.616  1.056  1.056
     [211]  1.504  1.576  1.496  1.464  0.344  1.584  1.416  0.744  0.224  0.736
     [221]  0.936  0.696  0.896  1.024  0.936  2.144  1.576  0.016  1.704  0.936
     [231]  0.904  0.624  1.744  1.256  1.976  0.784  1.344  0.704  0.864  0.224
     [241]  1.056  1.704  1.304  0.624  0.504  0.936  1.736  1.096  0.464  1.056
     [251]  0.296  0.704  1.184  1.376  1.216  0.504  1.064  0.696  1.184  1.376
     [261]  1.344  0.496  0.624  1.224  0.016  0.856  1.136  0.904  1.056 -0.184
     [271]  1.584  0.936  1.144  1.976  1.104  1.464  0.624  1.736  0.904  2.184
     [281]  0.744  0.736  1.376  0.464  0.464  1.176  1.696  0.824  1.504 -0.096
     [291]  1.504  1.456  1.464  0.904  1.224  1.784  0.456  0.256  1.976  1.344
     [301]  1.176 -0.136  0.016  0.904  1.704  1.536  1.296  1.424  1.776  0.104
     [311]  1.464  0.904  0.264  1.976  0.464  1.096  1.136  0.904  0.336  0.744
     [321]  0.576  1.536  1.264  0.944  2.144  1.056  1.424  1.064  0.984  0.704
     [331]  1.024  1.976  1.104  0.904  1.376  1.496  0.656  0.704  1.296  1.704
     [341]  1.224  0.736  0.064 -0.136  1.216  1.016 -0.176  0.456  0.216  1.064
     [351] -0.096  0.744  1.296  0.856  1.696  0.296  0.704  0.416  0.984  1.296
     [361]  0.496  0.944  1.416  0.544  0.736  1.936  1.576  0.416  0.496  0.256
     [371]  0.464  0.736  1.496  1.176  0.936  1.136  1.344  0.904  0.656  0.824
     [381]  1.776  1.096 -0.136  0.864  0.744  0.936 -0.136  0.104  0.544  0.656
     [391]  0.584  0.416  1.576  0.664  1.056  0.696  1.144  1.784  0.504  1.416
     [401]  0.944  1.936  1.584  1.664  0.256  0.664  0.696  1.096  1.464  0.304
     [411] -0.144  1.376  1.496  0.256  1.304  0.864  1.136  0.896  1.664  0.744
     [421]  1.256  1.224  0.944  1.944  1.944  0.896  0.896  1.216  1.344  1.224
     [431]  0.856  1.536  0.984  1.096  0.056  1.136  1.696  0.824  0.776  0.864
     [441]  0.944  1.544  2.104  0.704  1.344  0.744  0.024  0.984  1.464  0.936
     [451]  1.136  0.664  1.256  0.904  1.336  1.104  0.864  0.256  1.136  0.784
     [461]  1.296  0.936  1.104  1.056  1.264  1.296  0.584  1.736  1.696  0.584
     [471]  0.896  0.856  0.936  0.064  1.216  1.744 -0.144  1.296  0.336  1.064
     [481]  0.896 -0.176  1.016  1.064  0.904  1.744  0.816  0.656  0.496  0.576
     [491]  0.776  1.104  0.896  0.624  1.256  1.216  0.056  1.104  1.664  0.616
     [501]  1.304  1.304  1.664  1.304  0.744  0.864  0.824  1.744  0.744  1.104
     [511]  0.424  1.144  1.376  1.944  0.736  1.296  0.336  0.304  1.264  0.224
     [521]  1.704  1.296  1.344  0.984 -0.184  1.496  1.104  0.896  1.776  0.936
     [531]  1.176  0.336  0.936  1.296  1.296  0.736  0.864  1.304  1.376  1.344
     [541]  1.216  1.064  0.216  1.776  0.064  0.936  1.984  1.256  0.624  1.504
     [551]  1.296  1.256  1.224  1.936  2.184  0.504  0.824  0.464  0.304  1.496
     [561]  1.304  0.624  1.056  1.496  0.936  0.936  1.216  0.736  1.464  1.936
     [571] -0.144  0.784  1.016  2.176  0.936  0.704  1.744  0.744  0.424  0.704
     [581]  0.904  1.464  0.744  1.096  0.416  0.856  0.824  0.816  2.136  0.224
     [591]  1.264  2.144  0.656  1.336  0.416  0.496  1.536  1.904  0.736  1.504
     [601]  1.456  0.304  1.096  0.504  0.256  0.664 -0.096  1.264  1.496 -0.096
     [611]  0.736  0.224  1.896  0.304  0.944  0.544  1.536  0.904  1.104  1.056
     [621]  0.896  0.984  1.304  0.896  2.136  0.776  1.096  1.256  0.384  1.064
     [631]  0.496  1.936  1.264  0.936  0.704  0.696  1.496  1.136  1.336  1.104
     [641]  1.704  1.736  0.784  1.104 -0.176  1.536  1.144  0.464  1.944  1.616
     [651]  1.784  0.256  1.424  0.064  1.016  0.496  1.584  1.536  0.976  0.664
     [661]  1.736  1.536  0.744  1.296  0.424  1.536  0.544  1.056  1.376  0.816
     [671]  1.096  1.224  0.856  1.376  0.656  1.176  0.536  0.736  0.104  1.656
     [681]  0.896  0.696  1.336  1.144  0.856  2.184  0.864  0.936  1.224  1.504
     [691]  0.696  0.536  1.256  1.096  1.384  0.864  0.544  1.264  1.304  0.704
     [701]  0.656  1.456  0.264  0.896  1.744  1.584  0.584  0.824  1.296  0.624
     [711]  1.184  1.096  0.544  1.944  1.624  0.424 -0.096  0.984  0.224  1.376
     [721] -0.184  0.656  1.536 -0.104  0.064  1.104  1.776  0.336  0.816  1.664
     [731]  1.896  1.464  1.664  0.624  0.656  0.696  1.224 -0.176  1.344  0.896
     [741]  1.584  1.776  1.184  1.424  0.616  0.544  0.736  1.736  1.304  1.016
     [751] -0.176  0.864  1.144  0.664  1.184  0.664  0.664  0.984  1.296  0.656
     [761]  2.096  0.256  0.696  0.904  1.504  1.904  0.664  0.696  0.496  1.896
     [771] -0.136  0.464  0.904  0.416  0.896  0.456  1.104  1.096  1.064  1.584
     [781]  0.304  0.904  1.904  1.576  0.376  0.816  0.976  1.344  0.224  2.096
     [791]  0.624  0.296  1.576  1.336  0.496  0.744  0.456  1.264  1.376  1.296
     [801]  0.936  1.024  1.416  0.456  1.416  1.056  1.984  0.776  0.856  0.904
     [811]  1.096  0.664  0.344  1.264  0.256  1.056  1.096  0.576  1.776  1.744
     [821]  1.064  1.016  0.824  0.904  1.264  0.904  1.656  0.616  1.064  1.064
     [831]  0.856  0.984  0.696  1.504  1.416  0.824  1.304  1.584  1.056  2.096
     [841]  0.896  1.344  0.056  0.496  0.304  1.496  1.744  0.704  0.664  0.824
     [851]  1.264  1.536  1.576  1.496  0.584  0.496  2.184  0.696  0.896  0.464
     [861]  1.416  1.224  2.136  0.416  0.664  2.104  1.904  0.856  0.464  0.936
     [871]  1.104  0.344  1.304  0.224  0.424  1.064  0.496  0.696  1.256  0.304
     [881]  1.624  0.736  1.936  0.256  0.784  0.776  1.936  1.496  0.224  0.304
     [891]  0.824  0.016  0.416  1.584  0.936  1.784  0.856  0.304  0.576  1.944
     [901]  1.344  0.784  0.824  1.056  1.296  0.896  2.176  0.496  0.064  0.864
     [911]  1.504  0.024  0.776  0.424  2.176  1.384  1.576  1.744  0.736  1.736
     [921]  0.104  1.784  0.896  0.256  1.184 -0.104  0.584  1.264  0.936  1.456
     [931]  2.144  1.976  0.424  0.624  1.144  0.704  0.024  1.304  1.296  0.864
     [941]  1.456  0.736  0.264  1.304  1.016  0.656  1.496  0.904  1.704  0.096
     [951]  0.096  1.696  1.144  1.056  1.376  0.936  1.104  0.944  1.384  0.576
     [961]  0.256  1.544  0.416  1.464  1.776  1.336  0.064  0.264  1.136  1.136
     [971]  2.136  0.544  1.136  0.736  0.544  0.856  0.056  1.464  0.496  0.016
     [981] -0.104  0.936  0.816  1.704  1.136  1.536  1.376  1.216  1.736  0.456
     [991]  0.504  0.624  0.336  1.744 -0.104  0.896  0.784  0.584  0.504  1.776
    [1001]  1.736  0.904  0.304  0.496  0.296  1.104  1.656  1.504  0.976  1.744
    [1011] -0.184  0.984  0.664  0.696  0.496  0.464  0.496  2.176  0.824  1.696
    [1021]  1.224  1.776  0.896  0.824  0.944  0.976  1.416  0.904  1.296  0.296
    [1031]  0.624  0.944  0.944  0.816  0.856  1.936  0.296  0.816 -0.096  0.504
    [1041]  1.696  1.104  0.496  1.424  0.104  0.056  1.464  1.336  0.296  0.864
    [1051]  0.536  0.416  1.096  0.896  0.656  1.936  1.576  1.096  0.464  0.864
    [1061]  1.936  1.424  0.744  1.336  1.704  1.944  1.056  0.464  1.224  0.416
    [1071]  0.936  0.944  0.296  0.296  1.616  2.096  0.344  0.304  1.096  1.736
    [1081]  0.936  1.504  0.976  1.096  0.704 -0.184  1.064  1.496  0.744  1.184
    [1091]  0.816  0.096  0.296  0.296  0.904  1.136  0.904  0.584  0.704  1.496
    [1101]  1.064  0.896  0.304  1.744  1.904  1.576  0.904  0.416  0.496  2.144
    [1111]  0.456  1.456  0.776  1.064  1.224  0.896  0.656  1.224 -0.176  1.024
    [1121]  1.144  0.704  1.664  1.056  1.184  1.616  1.304  0.296  0.864  0.936
    [1131] -0.104  1.096  1.704  1.336  1.104  1.584  1.536 -0.144  0.704  0.424
    [1141]  1.064  1.544  1.744  0.336  0.384  1.256  1.744  0.496  1.056  1.064
    [1151]  1.904  0.984  0.616  1.464  0.456  1.664  0.536  0.824  0.504  1.336
    [1161]  1.784  1.304  1.744  0.304  0.696  2.184  0.696  2.144  0.336  0.536
    [1171]  1.496  1.064  0.496  0.864  1.304  1.656  0.936  1.944  0.464  0.304
    [1181]  0.944  0.424  1.776  0.264  0.816  2.096  1.384  1.296  0.536  0.544
    [1191]  1.384  0.504  0.656  1.096  1.224  1.536  1.064  0.984  1.296  1.096
    [1201]  0.504  0.304  1.464  0.816  1.176  1.376  1.064  1.304  0.536  1.216
    [1211]  1.704  0.416  0.256  1.464  0.944  1.456  1.064  1.536  0.816  1.696
    [1221]  0.264  0.504  1.024  1.696  0.416  0.304  1.056  0.896  0.976  1.584
    [1231]  0.744  1.504  1.184  0.936  1.984  1.624  0.096 -0.144  0.936  1.256
    [1241]  1.704  0.656  0.704  1.096  1.136  1.536  0.024  1.296  0.896  1.096
    [1251]  1.376  1.104  1.184  0.064  0.536  0.736  0.696 -0.104  0.424  1.064
    [1261]  1.576  1.344  0.984  0.784  0.056  0.864  1.616  1.104  1.704  0.296
    [1271]  0.664  1.744  1.384  0.696  0.544  0.944  0.304  1.224  1.976  0.776
    [1281]  1.576  0.624  0.856  2.096  1.344  0.744  0.776  1.136  0.496  1.744
    [1291]  0.504  1.104  0.304  0.296  1.744  1.264  1.496  1.696  2.096  1.016
    [1301]  0.896  0.896  0.984  1.304  0.944  0.744  1.776  0.776  0.664  1.104
    [1311]  1.296  1.184  1.464  0.656  0.264  1.096  1.256  1.616  1.064  1.344
    [1321]  0.056  1.744  0.456  0.024  0.744  1.176  1.096  0.416  1.776  1.224
    [1331]  0.496  1.264  1.616  1.936  1.216  0.936  0.104  1.696  1.184 -0.096
    [1341]  1.264  1.344  1.024  1.264 -0.184  1.136  1.176  1.264  1.464  0.096
    [1351]  0.096  0.376  1.376  1.136  0.664  0.656  1.096  1.184  1.496  0.056
    [1361] -0.104  1.176  0.304  1.176  1.064  1.744  0.856  0.296  0.944  1.104
    [1371]  0.656  1.744  0.776  0.704  1.656  0.744  0.624  1.544  0.896  0.056
    [1381]  1.336  0.224  1.696  0.944  0.496  2.144  0.816  1.504  0.664  0.224
    [1391]  0.656  1.224  0.904  1.656  2.104  1.216  1.304  0.776  2.104  2.136
    [1401]  1.376  1.176  0.264  1.344  0.696  1.224  1.344  0.064  1.336  1.504
    [1411]  1.096  0.736  1.584  0.856  1.984  1.424  0.936  0.864  0.376  1.304
    [1421]  1.536  1.264  0.696  1.504  1.176  0.464  1.496  0.216  0.584  0.936
    [1431]  1.064  1.976  0.704  1.216  0.504  0.656  1.536  0.744  1.536  1.064
    [1441]  0.416  0.096  0.664  1.696  1.064  0.856  1.296  1.736  0.264  1.344
    [1451]  1.256  0.936  0.424  1.496  2.176  0.896  0.224  0.536  1.744  0.944
    [1461]  0.936  1.656  0.424  1.336  0.424  1.496  0.536  1.784  1.096 -0.176
    [1471]  1.344  0.704  2.136  1.744  0.456  1.296  1.944  1.536  1.656  0.536
    [1481]  1.304  1.144  1.656  0.704  1.104  1.744  0.984  1.384  0.744  0.936
    [1491]  0.536  1.344  1.064  1.056  0.944  0.296  1.576  0.824  1.976  1.096
    [1501]  0.904  1.504  0.896  1.576  1.104  0.864  1.104  1.904  0.576  1.064
    [1511]  0.224 -0.184  0.056  1.616  1.984 -0.184  1.744  2.104  1.056  0.584
    [1521]  1.344  0.264  1.144  1.024  1.096  0.464  1.776  1.176  0.864  1.296
    [1531]  1.944  0.464  0.536  1.184  1.656  1.376  0.656  1.424  1.504  1.536
    [1541]  1.304  1.424  0.496  0.624 -0.144  1.136  1.584  0.296  1.424  0.896
    [1551]  1.536  1.224  0.864 -0.144  1.704  1.736  1.504  0.256  0.056  1.776
    [1561]  1.344  1.544  0.456  1.696  1.056  1.024  0.256  0.104  1.416  0.456
    [1571]  0.296  1.576  0.496  0.904  0.264  0.936  0.616  1.064  0.864  1.016
    [1581]  1.264  1.104  1.344  0.344 -0.184  1.016  0.016  1.224  0.896  1.304
    [1591]  1.176  0.704  1.576  1.424  0.936  0.536  0.416  1.264  1.304 -0.136
    [1601]  1.424  0.464  0.496  1.136  0.096  0.336  0.704  0.256  0.704  0.856
    [1611]  0.736  1.224  1.016  1.696  0.296  1.464  1.104  1.304  0.936  0.496
    [1621]  1.296  1.096  0.864  1.224  0.536  0.624  0.944  0.256  1.944  1.296
    [1631]  0.336  1.056  1.024  0.056  1.304  1.064  1.464  1.624  0.784  0.416
    [1641]  1.544  1.184  0.496  1.296  2.144  1.336  1.104  1.056  0.256  1.144
    [1651]  0.944  0.616  0.096  1.024  0.304  0.336  2.176  0.296  1.064  1.896
    [1661]  0.656  1.704  0.256  0.296  0.664  0.536  1.496  0.464  1.136  0.304
    [1671]  1.016  1.904  0.496  1.504  1.496  1.944  0.584  1.456  1.536  0.304
    [1681]  1.704  1.064  1.904  0.504  1.104  2.176  1.296  1.536  0.024  0.416
    [1691]  0.904  1.184  1.536  0.664  1.184  0.096  0.304  0.656  1.144  1.696
    [1701]  1.104  0.744  2.176  0.776  0.984  1.104  1.504  1.136  0.776  1.744
    [1711]  0.896  1.704  1.256  0.736  0.776  1.096  1.016  0.776  0.584  2.176
    [1721]  0.536  0.896  1.064  1.216  1.144  1.544  1.744  0.776  1.016  1.016
    [1731]  1.104  1.656  1.064  1.184  1.336  0.896  0.536  1.344  1.704  1.576
    [1741]  0.776  0.744  0.256  1.536  0.656  1.744  0.896  1.064  0.904  0.064
    [1751]  0.504  0.424  0.776  0.224  1.744  0.984  0.776  0.736  1.504  0.576
    [1761]  1.296  0.256  0.984  1.904 -0.144  1.496  0.824  0.464  1.744  0.576
    [1771]  0.096  1.536  0.656  1.224  0.776  1.256  0.736  2.136  1.136  0.064
    [1781]  0.944  0.904  1.064  1.784  0.424  0.304  0.376  0.816  0.416  1.224
    [1791]  1.696  1.464  1.016  0.584  0.776  2.144  0.744  0.384  0.904  1.176
    [1801]  1.976  0.424  1.896  0.696  0.736  0.664  1.704  0.216  1.216  1.936
    [1811]  1.304  1.216  2.144  1.296  0.504  0.696  1.264  1.416  1.304  0.936
    [1821]  0.336  1.376  1.296  1.464  1.376  0.984  0.856  0.456  1.256  1.224
    [1831]  1.224  0.856  1.104  0.864  1.256  0.744  1.584  0.496 -0.104  1.176
    [1841]  0.704  0.264  1.224  1.296  1.064  1.296  1.576  0.336  0.704  0.736
    [1851]  0.816  0.824  0.064  0.784  0.096  1.344  1.064  0.384  0.464  0.896
    [1861]  1.576  1.536  2.176  2.144  1.736  1.496  0.984  0.584  1.424 -0.144
    [1871]  0.936  1.424  1.344  1.096  1.264  0.656  0.744  1.936  0.816 -0.184
    [1881]  1.536  1.776  0.984  0.464  0.624  0.424  0.464  0.016  0.496  0.064
    [1891]  1.224  0.424  1.024  2.184  1.624 -0.184  1.096  1.296  0.696  0.504
    [1901]  1.376  0.896  1.064  1.136  2.176  1.416  1.376  1.144  1.304  1.496
    [1911]  0.504  1.064  0.496  0.664  0.816  1.304  1.136  0.064  1.184  0.464
    [1921]  0.584  0.896  1.376  0.624  0.936  0.424  0.496  0.904  1.376  0.064
    [1931]  1.296  0.864  1.344  1.016  0.784  1.056  0.496  0.664  1.296  1.176
    [1941]  1.424  0.064  1.016  1.056  1.504  0.864  0.576  0.904  0.504  0.584
    [1951] -0.096  0.904  1.464  1.416  0.944 -0.176  0.464  0.864  1.344  1.616
    [1961]  0.904  0.776  0.696  1.504  0.296  1.776  0.024  0.536  0.784  1.224
    [1971]  1.416  0.256  0.904  1.096  1.176  0.784  0.936  1.024  0.536  0.416
    [1981]  0.536  0.576  1.704  0.464  0.944  1.776  0.664  1.144  0.456  1.656
    [1991]  2.184  1.744  0.104  0.544  1.224  0.576  0.704  1.704  0.216  0.904
    [2001]  1.344  1.064  1.584  1.104  0.824  1.504  1.104  1.936  0.656  1.944
    [2011]  1.704  0.864  0.056  0.664  0.696  0.264  0.496  0.056  0.024  0.736
    [2021]  0.616  1.144  1.496  1.624  1.264  1.104  0.224  0.464  0.424  0.424
    [2031]  1.464  0.616  0.856  1.024  1.176  0.344  1.184  1.176  1.344  1.256
    [2041]  1.384  1.944  1.056  1.184  2.176  2.184  1.016  0.256  0.056  0.984
    [2051]  1.136  0.904  1.376  1.424  0.576  0.704  1.376  0.096  1.296  0.904
    [2061]  1.064  1.536  1.576  0.736  1.344  1.456  1.104  1.104  1.184  0.936
    [2071]  0.336  0.224  0.024  1.184  0.264  0.056  2.136  0.536  1.064  1.464
    [2081]  0.824  0.944  1.064  1.064  1.704  1.464  0.264  1.264  0.256  0.784
    [2091]  0.744  1.424  0.544  0.536  1.464  1.336  0.864  1.136  1.176  1.096
    [2101]  1.664  0.944  0.856  1.024  0.376  0.904  0.544  0.304  0.536  1.104
    [2111]  1.464  0.096  0.536  0.296  0.104  1.064  0.096  1.256  0.504  0.696
    [2121]  0.856  1.056  0.976  1.056  0.416  1.744  0.856  0.784  0.424  1.936
    [2131]  0.984  0.224  1.536  1.776  1.944  0.904  1.976  1.336  0.504  1.064
    [2141]  1.736  0.304  1.464  1.936  0.496  1.304  1.696  1.024  1.576  0.936
    [2151]  0.416  0.656  1.464  1.744  1.696  0.256  0.904  0.464  0.824 -0.104
    [2161]  0.096  1.064  0.824  1.624 -0.096  1.304  1.456  0.736  0.256  0.864
    [2171]  1.096  1.304  1.656  1.776  0.904  1.376  2.144  0.744  1.136  1.576
    [2181]  1.224  0.936  0.584  1.616  1.296  1.016  0.896  1.224  1.936  0.944
    [2191]  1.616  1.304  0.464  0.936 -0.184  1.064  1.016  1.656  0.256  0.496
    [2201]  1.536  1.136  0.256  1.944  0.056  0.856  0.696  0.856  1.376  0.296
    [2211]  1.064  0.264  0.376  1.064  0.984  0.864  1.104  0.584  1.216  0.496
    [2221]  0.064  1.496  1.144  0.624  1.664  0.304  1.296  1.224  1.224  1.136
    [2231]  0.896  1.056 -0.184  1.336  0.984  1.056  1.936  0.664  1.104  0.536
    [2241]  1.264  0.664  1.936  1.376  0.896  1.936  0.664  1.216  1.064  1.136
    [2251]  0.896  1.304  1.304  1.944  1.144  1.344  0.464  0.736  1.424  1.576
    [2261]  0.256  0.896  0.584  0.784  0.384  0.904  1.536  0.496  0.264  0.056
    [2271]  1.104  1.576  0.736  0.624  0.944  0.984  1.376  0.936  1.216  1.936
    [2281]  1.536  0.944  0.736  0.864  2.176  0.544  1.344  0.704  1.184  0.864
    [2291]  0.576  1.464  0.864  0.544  0.744  0.064 -0.144  1.496 -0.184  1.096
    [2301]  1.216  0.216  1.776  1.264  0.976  1.104  1.896  1.736  1.984  0.624
    [2311]  0.464  0.656  2.136  0.584  0.536  1.344  0.624  1.344  1.944  1.256
    [2321]  0.936  1.136  1.336  1.696  0.896  1.064  1.256  1.496  0.936  1.664
    [2331]  0.544  1.344  0.576  0.296  1.944  0.864  1.464  0.784  1.224  1.096
    [2341]  1.064  1.064  0.064  0.736  1.496  1.544  1.224  0.296  0.896  1.104
    [2351]  1.296  0.416  1.744 -0.136  1.056  0.384  0.064  0.976  0.904  0.384
    [2361]  1.104  0.504  0.624  0.224 -0.144  1.304  1.984  0.016  1.376  0.776
    [2371]  1.096  1.936  0.296  0.736  1.136  1.144  0.904  0.544  0.016  1.296
    [2381]  1.064  1.616  0.904  0.336  1.576  0.064  1.584  1.144  0.336  0.744
    [2391]  1.704  0.856  0.336  0.736  1.136  0.296  0.784  0.456  1.104  0.936
    [2401]  1.056  0.664  1.224  1.744  1.776  1.304  0.584  1.136  1.136  0.576
    [2411]  0.504  0.904  0.936  0.336  1.664  1.696  1.584  0.216  1.624  1.416
    [2421]  0.904  0.664  1.136  0.944  1.136  0.264  1.536  1.224  0.016  0.976
    [2431]  0.704  0.456  0.256  1.584  0.464  0.304  1.976  1.936  1.096  0.304
    [2441]  1.544  0.296  1.136  1.144  0.936  0.704 -0.136  0.344  1.496  0.944
    [2451]  1.344 -0.136  0.856  0.536  0.904  0.656  1.936  0.424  0.264  0.536
    [2461]  0.616  0.424  1.016  0.776  0.656  0.624  1.704  0.704  1.304  0.664
    [2471]  0.704  1.064  0.496  1.024  1.456  0.936  1.904 -0.136 -0.176  1.664
    [2481]  1.136  1.064  0.696 -0.176  1.016  0.616  1.304  0.296  1.376  0.704
    [2491]  0.936  0.696  0.824  1.096  0.416  1.744  0.736  0.496  0.824  1.056
    [2501]  1.104  0.984  0.296  1.616  1.424  0.264  1.584  1.584  0.336  0.904
    [2511]  0.576  1.664  0.664  1.576  1.704  1.064  1.576  1.376  0.664  0.776
    [2521]  1.736  1.936  0.864  1.256  1.384  0.904  1.496  1.936  1.496  0.656
    [2531]  1.224  0.656  0.936  2.096  1.096  0.576  0.856  1.304  1.704  1.504
    [2541]  1.504  0.976  0.856  1.144  0.504  0.864  1.304  0.544  0.976  1.264
    [2551]  0.696  1.664  1.216  0.224  1.776  0.096  1.064  0.224  0.496  2.144
    [2561]  0.896  1.424  1.296  0.504  0.504  1.016  1.344  1.744  1.184  1.464
    [2571]  1.576  1.096  0.664  1.896  2.104  1.496  0.656  0.664  1.496  1.464
    [2581]  1.784  1.264  2.184  0.336  1.344  0.504  1.264  1.136  1.784  1.224
    [2591]  0.856  1.704  2.176  1.944  0.536  1.264  1.296  0.776  1.224  1.624
    [2601]  1.576  1.096  1.384  1.424  1.784  1.264  0.936  1.496  1.144  1.304
    [2611]  1.704  2.144  0.736  0.736  1.264  0.896 -0.184  0.936  0.976  1.144
    [2621]  1.264  1.344  1.024 -0.184  0.344  0.824  0.464  0.744  0.336  0.776
    [2631]  1.024  1.224  1.416  0.544  1.496  1.624  0.744  0.664  0.816  0.416
    [2641]  1.664  1.056  1.456  1.704  0.424  1.904  1.944  0.216  0.464  0.736
    [2651]  0.064  2.184  0.864  1.496  0.256  0.936  0.904  0.704  0.936  0.904
    [2661]  2.104  0.296  1.096  1.504  1.576  1.136  0.864  0.904  0.704  1.976
    [2671]  0.536  0.984  2.184  0.496  1.536  1.224  0.696  1.176  0.696  0.536
    [2681]  0.504  0.624  1.336  1.144  1.536  0.896  0.496  0.016  1.264  1.264
    [2691]  2.096  1.696  0.736  1.496  0.856  1.464  1.464  1.104  1.424  0.936
    [2701]  1.144  0.776  0.304  1.376  0.696  1.664  0.696  0.584  0.496  1.536
    [2711]  1.136  1.944  1.344  0.256  1.176  1.296  0.656  1.736  1.016  0.056
    [2721] -0.104  1.264  1.256  0.616  0.216  0.784  1.096  1.064  1.376  0.944
    [2731]  0.304  1.224  0.544  0.864  0.736  0.416  0.936  1.696  0.624  0.536
    [2741]  1.904  0.624  0.576  0.856  0.224  0.896  1.456  0.504  1.176  0.936
    [2751]  0.816  1.736 -0.096  0.056  1.056  1.584  1.544  1.224 -0.144  1.216
    [2761]  0.704  0.656  1.096  1.944  1.056  1.584  1.736  0.696  1.056  0.856
    [2771]  1.224  0.504  0.984  1.696  1.064  0.896  0.664  1.536  1.176  1.144
    [2781]  1.416 -0.144 -0.136  1.064  0.704  1.344  0.856  1.744  0.064  0.456
    [2791]  1.104  0.464  1.496  1.336  0.656  0.896  1.336  1.104  1.344  0.856
    [2801]  1.096  1.656  1.304  1.064  1.064  0.304  0.304  1.176  0.856  0.856
    [2811]  0.056  0.784  0.576  0.496  0.696  0.864  1.096  0.864  0.504  0.424
    [2821]  1.024 -0.136  1.096  1.504  1.296  0.696  0.704  0.856  2.096  0.664
    [2831]  1.224  0.744  1.016  1.064  1.944  0.376  0.944  0.696  0.536  1.504
    [2841]  0.696  1.536  0.656  0.584  1.064  0.704  1.664  0.976  0.424  0.704
    [2851]  2.184  0.976  1.344  0.896  1.504  0.336  1.464  1.064  1.416  1.744
    [2861]  1.144  1.016  0.784  0.984  0.904  0.496  0.296  0.624  0.544 -0.184
    [2871]  1.184 -0.184  0.864  1.696  0.896  0.224  1.064  1.104  1.576  0.856
    [2881]  1.096  1.536  1.296  0.584  0.984  1.464  1.624  1.344  0.424  1.136
    [2891]  0.696  1.024  0.904  1.064  1.024  1.176 -0.184  0.256  0.576  1.104
    [2901]  0.704  1.176  0.944  0.896  1.344  1.024  0.344  1.504  1.704  0.496
    [2911]  1.264  1.456  0.704  0.864 -0.104  1.024  1.984  1.504  0.976  0.896
    [2921]  1.904  1.504  1.456  0.736  0.704  1.536  0.984  1.144  1.184  0.376
    [2931]  1.496  1.264  0.424  1.616  1.464  1.984  1.576  1.536  1.096 -0.144
    [2941]  1.096  0.624  0.504  1.176  1.464  1.144  0.944  0.544  0.776  0.824
    [2951]  0.224  1.736  0.904  1.944  1.336  1.584  1.344  0.784  1.536  1.304
    [2961]  0.536  1.104  0.464  1.024  0.456  1.576  1.424  1.304  1.264  0.856
    [2971]  1.056  1.064  1.224  1.104  0.256  1.296  0.696  1.304  1.576 -0.104
    [2981]  0.624  1.536  0.936  1.024  0.984 -0.104 -0.136  1.064  0.464  0.864
    [2991]  1.144  0.296  0.496  0.704  0.296  0.984  1.504  0.104  0.776  0.464
    [3001]  1.304  0.536  1.056  1.176  1.344  0.336  0.464  0.584  0.464  1.904
    [3011]  0.464  1.376  1.064  1.536  1.376  1.456  0.984  0.624  1.376  1.696
    [3021]  1.776  2.184  0.704  1.016  0.736  0.824  0.664  1.424  1.424  1.144
    [3031]  0.296  0.896  1.016  2.144  1.064  1.336  0.496  1.104  0.256  0.976
    [3041]  0.584  0.416  0.464  0.736  1.264  0.896  1.624  1.744  1.104  1.744
    [3051]  0.216  1.176  1.184  0.656  1.176  0.224  0.024  0.056  0.496  0.544
    [3061]  1.264  0.744  0.656  1.344  0.104  1.504  1.696  0.336  0.576  0.736
    [3071]  0.576  0.336  0.264  0.104  1.584  0.896  0.464  1.696  0.656  0.776
    [3081]  0.256  0.976  1.504  0.056  1.344  0.736  0.264  0.224  0.736  1.536
    [3091]  1.296  0.904  1.096  0.256  1.344  1.144  0.744  0.744  2.184  1.744
    [3101]  1.264  1.936  0.704  1.744  0.816  0.344  1.784  1.256  0.784  1.376
    [3111]  0.896  0.984  1.744  0.936  0.224  1.096  0.064  1.136  1.456  0.864
    [3121]  0.616  2.096  0.016  0.304  1.536  1.064  1.416  0.984  0.584  1.344
    [3131]  0.504  0.096  1.584  1.096  1.296  1.256  0.496  0.616  0.624  1.096
    [3141]  0.576  0.904  0.264  0.384 -0.176  0.656  0.744  2.136  0.496  0.864
    [3151]  1.096  0.696  1.584  0.816  1.464  1.344  0.616  1.704  1.544 -0.144
    [3161]  0.224  0.744  0.744  1.176  1.376  1.264  1.344  1.944  0.304  0.936
    [3171]  0.016  1.664  1.496  0.696  0.864  1.336  1.664  0.656  1.176  1.704
    [3181]  2.104  0.536  0.416  1.536  0.736  1.184  1.224  0.504  0.776  0.656
    [3191]  0.416  1.304  2.104  0.696  1.096  0.696  1.624  1.336  0.744  0.736
    [3201]  1.216  0.696  0.656  1.536  0.856  1.136  0.784  0.704  1.944  1.144
    [3211]  1.784  1.296 -0.176  0.304  1.176  1.536  0.464  0.696  1.464  0.744
    [3221]  0.536  0.736  0.936  0.936  0.896  1.104  0.696  1.776  0.864  0.864
    [3231]  1.224  1.504  1.704  1.304  1.176  0.584  1.656  1.056  0.296  1.496
    [3241]  1.056  0.584  0.064  0.744  1.536  0.056  0.064  0.856  1.696  0.656
    [3251]  1.256  1.504  0.824  1.104  0.856  0.584  1.504  1.296  0.976  0.464
    [3261]  1.744  1.024  1.536  1.376  1.664  0.584  1.616  1.264  1.536  0.344
    [3271]  0.056  1.304  0.704  1.056  1.664  1.904  1.384  1.016  0.896  0.696
    [3281]  1.136  0.296  2.104  0.504  1.256  1.256  0.944  0.096  0.744  1.296
    [3291]  0.904  1.256  0.296  0.296  1.144  1.544 -0.136  0.224  1.224  1.296
    [3301]  0.296  0.216  0.936  0.456  1.264  1.256  0.576  1.376  1.536  0.936
    [3311]  1.544  1.096  0.696  0.056  1.984  0.576  1.304  1.936  1.664  1.056
    [3321]  0.464  1.256  1.464  1.176  1.464  1.424  0.696  1.696  1.136  1.536
    [3331]  0.784  1.264  0.816  1.536  0.504  0.736  0.264  0.896  0.464  0.296
    [3341]  1.096  0.576  0.696  1.656  2.136  1.544  1.456  0.896  1.136  1.224
    [3351]  1.984  1.704  0.896  1.424  0.216  1.776  1.024  0.776  1.344  1.096
    [3361]  0.944  0.936  1.584  1.304  0.736  1.744  1.224  0.624  1.304  0.696
    [3371]  1.296  1.616  0.784  0.264  1.096  0.696  0.064  1.136  1.464  0.304
    [3381]  1.096  1.024  0.704  1.976  1.704  1.056  0.256  1.776  1.744  1.184
    [3391]  0.896  0.384  0.264  0.064  0.024  1.376  1.136  1.136  1.184  1.376
    [3401]  0.704  1.944  0.944  0.096  0.336  0.096  1.416  1.584  0.504  1.704
    [3411]  1.256  0.536  1.944  0.104  1.504  0.496  1.016  1.936  1.184  2.184
    [3421]  0.224  1.096  0.944  0.464  1.536  1.016  1.064  1.696  0.856  0.704
    [3431]  1.144  0.856  0.416  1.296  1.064  1.056  1.536  0.936  0.664  1.224
    [3441]  0.656  1.424  0.616  0.704  1.456  1.984  1.024  1.544  1.224  1.736
    [3451]  0.936  0.496  0.976  1.664  1.136  0.264  0.944  0.616  1.456  1.016
    [3461]  0.464  1.504  1.296  0.824  1.576  1.944  1.104  0.304  1.256  0.856
    [3471]  0.696  0.696  1.016  1.064  0.656 -0.176  1.216  0.224  1.264  1.056
    [3481]  1.504  1.704  1.576  0.744  0.016  0.656  1.344  1.264  1.696  1.416
    [3491]  0.376  1.896  1.344  1.184  1.496  0.544  1.104  1.544  1.064  0.696
    [3501]  0.776  0.904  0.536  1.504  1.456  1.296  1.416 -0.104  0.896  1.664
    [3511]  1.736  0.664  0.744  1.296  0.656 -0.136  1.736  1.224 -0.096  0.536
    [3521]  1.544  1.936  1.736  1.184  2.144  1.224  0.424  1.144  1.424  1.064
    [3531]  1.904  0.784  1.136  1.464  0.464  2.104  1.064  0.416  2.144  0.704
    [3541]  1.224  1.304  0.696  0.496  1.696  1.784  0.376  0.656  1.376  1.096
    [3551]  0.784  1.056  1.104  1.264  1.944  1.456  1.944  0.656  1.096  0.904
    [3561]  0.936  1.576  1.064  1.216  0.656  1.736  1.896  0.536  0.896  1.664
    [3571]  0.016  0.784  1.264 -0.144  1.304  1.296  2.136  0.336  0.256  1.064
    [3581]  1.136  0.704  1.344  0.264 -0.176  1.184  1.224  1.704  0.496  1.224
    [3591]  1.296  1.176  1.344  1.224  0.496  1.376  1.104  1.456  1.176  1.944
    [3601]  1.224  0.936  1.216  0.056  1.384  0.256  1.184  0.664  1.536  0.416
    [3611]  0.896  1.456  0.744  0.496  1.736 -0.144  1.296  0.584  1.984  1.464
    [3621]  0.664  0.696  1.184  1.136  1.944  0.824  0.736  0.624  1.096  1.664
    [3631]  0.776  1.104  1.176  1.344  0.496  1.376  0.464  0.776  0.784  0.896
    [3641]  0.904  0.816  2.144  1.296  1.976  1.464  1.224  1.424  1.744  1.664
    [3651]  0.064  0.864  1.696  1.376  0.376  0.656  0.696  1.424  1.104  1.464
    [3661]  1.264  1.136  0.264  1.416  0.256  0.504  0.984  1.944  1.216  1.536
    [3671]  0.736  1.144  1.936  1.504  0.024  0.736 -0.096  0.664  0.744  0.064
    [3681]  0.216  1.784  0.904  0.464 -0.184  0.696  0.744  1.016  0.856  0.376
    [3691]  0.544  1.224  0.744  0.536  1.264  1.056  1.744  0.624  1.736  1.384
    [3701]  1.576 -0.176  0.224  0.944  0.064  0.304  0.984  1.056  0.624  1.344
    [3711]  1.344  0.904  0.944  1.736  1.336  0.344  1.144  1.704  1.744  0.904
    [3721]  0.856 -0.176  1.216  0.984  1.336  1.056  0.896  1.056  0.784  0.704
    [3731]  0.376 -0.144  1.536  1.184  0.936 -0.096  0.656  0.664  0.256 -0.184
    [3741]  1.136  1.504  1.384  0.896  0.984  1.496  0.064  1.264  1.096  0.336
    [3751]  1.104  0.504  0.904  1.264  1.496  1.504  0.464  1.336  0.904  1.256
    [3761]  1.736  0.296  0.864  1.056  0.576  0.296  1.416  0.504  1.256  0.584
    [3771]  1.096  1.136  0.304  0.504  0.624  0.696  1.776  1.424  1.104  0.664
    [3781]  0.064  1.616  0.544 -0.144  0.936  1.136  1.376  1.064  0.296  1.016
    [3791]  0.936 -0.176  0.656  1.064  0.384  0.424  0.704  1.744  0.704  1.336
    [3801]  1.776  1.616  0.984  1.536  0.864  0.976  1.736  0.504  1.376  1.336
    [3811]  0.864  1.024  1.096  0.976  0.704  1.184  0.224  1.264  0.656  1.064
    [3821]  2.104 -0.176  0.584  1.544  0.976  1.304  1.104  0.016  0.256  1.416
    [3831]  1.584  1.176  1.184  0.224  1.264  1.416  0.304  0.696  0.216  0.416
    [3841]  1.016  1.544  0.064 -0.096  1.224  1.496 -0.184  1.744  0.224  1.936
    [3851]  0.896  0.984  1.456  0.736  1.664  0.656  1.136  0.544  0.664  1.096
    [3861]  0.696  2.136  0.896  1.144  0.584  1.456  0.464  1.136 -0.104  0.064
    [3871]  1.464  0.896  0.664  1.064  0.736  0.904  0.544  1.064  0.864  0.464
    [3881]  0.896  0.744  1.144  1.176  1.344  0.496  0.984  1.456  0.064  1.504
    [3891]  1.704  1.344  1.464  1.536  1.704  0.944  1.064 -0.096  1.544  0.496
    [3901]  1.376  0.496  1.344  0.744  0.576  0.656  1.104  0.344  1.104 -0.144
    [3911]  0.504  1.496  0.856  1.576  0.376  1.256 -0.144  0.896  1.096  1.064
    [3921]  0.736  0.424  1.096  1.936  1.784  0.376  0.984  0.896  0.256  1.344
    [3931]  0.496  0.384  1.096  0.696  0.696  1.696  1.696  0.304  1.056  1.136
    [3941]  0.664 -0.176  0.416  1.496  1.664  0.776  0.936  0.736  0.864  0.904
    [3951]  0.696  0.904  0.696  1.056  1.144  1.424  1.496  1.336  0.336  0.616
    [3961]  1.336  1.144  0.864  1.936  0.984  1.016  0.224  1.304  1.504  1.584
    [3971]  1.144  0.656  0.256  1.344  0.776  1.904  0.424  1.104  1.536  0.824
    [3981]  0.864  1.584  0.696  1.776  0.856  0.736 -0.144  1.256  1.264  0.464
    [3991]  1.696  0.744  0.936  0.624  0.416  1.344  0.536  0.944  0.344  0.296
    [4001]  0.736  1.376  1.104  1.336  1.104  0.464  0.016  1.384  1.056  1.136
    [4011]  0.656  1.056  1.064  1.424  0.624  0.864  0.304  1.504  1.304  1.696
    [4021]  1.464  0.984  0.984  1.344  2.104  1.376  0.984  1.136  0.624  1.024
    [4031]  1.264  1.264  1.064  0.984  1.296  0.504  1.984  0.976 -0.176  0.496
    [4041]  0.336  1.744  0.896  2.176  1.776  1.584  0.784  1.104  0.336  1.064
    [4051]  0.216  0.624  1.704 -0.144  0.744  0.336  1.104  0.776  0.944  0.264
    [4061]  2.104  0.504  0.664  0.504  0.344  2.176  1.096  1.464  0.856  0.424
    [4071]  0.584  0.896  1.096  0.736  1.184  0.936  1.336  0.784  1.376  1.536
    [4081]  1.384  0.904  1.136  0.296  1.216  1.344  1.184  0.696  1.544  0.736
    [4091]  1.776 -0.176  0.664  1.696 -0.144  0.864  0.296  0.496  0.256  1.176
    [4101]  1.744 -0.176  2.136  0.064  0.336  1.056  1.704  1.976  1.096  1.744
    [4111]  0.744  0.536  0.504  2.096  0.336  0.784  1.776  1.496 -0.096  1.176
    [4121]  1.096  1.464  0.704  1.264  0.664  0.696  1.296  0.096  0.896  1.184
    [4131]  1.624  0.456  0.864  1.184  0.464  0.416  1.696  0.864  0.344  2.136
    [4141]  1.736  1.504  1.064  1.544  0.736  1.416  1.376  0.944  0.216  0.256
    [4151]  1.416  1.616  0.824 -0.136  2.096  0.536  0.976  1.264  0.264  1.336
    [4161]  0.616  1.464  0.616  1.536  0.416  1.984  1.336  0.704  1.216  1.376
    [4171]  0.816  0.624  1.976  0.816  1.016  0.304  1.024  0.544  0.936  1.664
    [4181]  1.136  1.256  1.936  1.176  0.696  1.224  1.104  0.536  2.096  1.696
    [4191]  0.704  0.496  0.856  1.744  1.264  0.856  1.664  1.704  1.176  0.504
    [4201]  1.096  1.936  1.504  1.056  1.696  0.936  1.704  0.496  0.304  0.096
    [4211]  1.984  1.136  1.704  0.464  1.744  0.504  1.064  0.744 -0.104  1.376
    [4221]  1.744  1.064  1.464  1.624  1.496  1.416  1.064  0.824  0.464  0.624
    [4231]  1.536  0.096  1.136  1.464  1.296  1.096  0.104  0.896  0.936  1.376
    [4241]  1.736  1.304  1.664  1.504  0.904  1.144  0.416  0.464  0.896  1.296
    [4251]  0.536  1.344  1.624  0.704  1.176  0.056  1.256  0.744  1.224  0.416
    [4261]  1.544  1.776  1.304  0.744  0.496  0.536  1.696  1.016  1.056  0.936
    [4271]  0.984  0.776  1.376  0.744  1.384  0.504  0.624  0.216  1.656  0.336
    [4281]  1.176  0.224  0.016  0.576  1.344  0.536  2.144  0.896  0.496  1.744
    [4291]  0.576  0.256  0.536  0.544  1.224  0.856  0.496  1.504  0.576  0.736
    [4301]  1.296  1.224  1.904  0.504  1.664 -0.104  0.856  1.424  1.016 -0.104
    [4311]  0.464  0.936  0.904  0.896  1.456 -0.144  0.944  0.416  0.296  0.696
    [4321]  0.344  0.216  1.656  0.736  1.736  1.464  1.136  0.016  1.704  1.496
    [4331]  0.664  0.944  1.576  0.944  0.696  1.504  0.616  1.216  0.904  0.864
    [4341]  0.624  1.464  1.216 -0.144  0.744  1.704  1.344  1.504  0.304  2.184
    [4351]  1.264  1.664  0.096  1.744  0.744  1.344  1.456  1.464  1.664  0.056
    [4361]  0.856  0.896  0.704 -0.096  0.584  1.704  0.024  1.496  1.104  1.104
    [4371]  1.304  0.656  1.544  1.496  1.704  1.016 -0.096  0.344  1.376  0.936
    [4381]  0.464  1.296  0.056  1.144  0.464  1.144  0.696  1.064 -0.136  2.096
    [4391]  0.336  1.416  1.904  1.984  1.656  1.416  0.216  0.704  1.296  1.744
    [4401]  0.936  1.264  0.384  0.816  1.664  1.376  0.944  0.944  0.584  0.816
    [4411] -0.096  0.584  0.224  0.616  0.256  0.384  0.904  1.344  0.976  0.776
    [4421]  1.456  0.464  0.304  1.976  1.576  0.664  0.496  0.256  0.584  0.096
    [4431]  1.224  1.144  0.256  1.096  0.704  0.536  0.944  1.704  1.936  1.416
    [4441]  0.944  0.536  1.616  0.536  0.416  2.144  0.744  1.456  1.544  1.504
    [4451]  1.144  1.536  0.016  1.376  1.144  1.936  0.904  0.064  1.464  0.104
    [4461]  2.144  1.896  1.576  2.144  1.704  1.064  1.464  1.176  0.584  2.104
    [4471]  0.736  1.536  0.704  1.744  0.224  1.056  1.224  0.536  0.296  1.064
    [4481]  0.976  0.856  1.624  1.304  1.304  1.136 -0.136  1.704 -0.144  1.096
    [4491]  0.776  1.536  0.896  0.296  1.304  0.744  1.064  0.944  0.416  1.584
    [4501]  1.336  2.176  0.464  0.624  1.624  1.584  1.616  1.624  1.264  0.656
    [4511]  1.064  1.624  0.744  1.384  0.656  1.704  0.264  0.656  0.224  1.256
    [4521]  1.024  0.936  1.496  1.064  0.496 -0.144  0.576  0.424  1.056  1.136
    [4531]  0.024  2.184  1.264  0.056  1.064  0.504  1.264  1.424  0.536  1.024
    [4541]  0.784  0.496  0.504  1.384  1.496  0.736  1.696  0.544  0.896  0.496
    [4551]  0.624  0.704  1.184  1.984  0.824  0.944  1.064  1.296  1.376  1.496
    [4561]  0.704  0.824  0.064  1.504  0.624  1.496  0.496  1.624  1.696  0.456
    [4571]  0.736  0.744  0.784  1.776  0.736  1.984  0.976  0.864  1.216  1.536
    [4581]  1.744  0.384 -0.144  0.424  0.504  1.296  1.176  0.456  0.416  0.536
    [4591]  1.376  1.456  0.496  0.936  0.704  0.984  1.496  0.944  1.304  0.216
    [4601]  0.336  0.304  0.464  0.264  1.736  1.376  1.656  0.296  1.096  0.984
    [4611]  1.344  0.776  0.856  1.264  1.944  0.016  0.576 -0.104  1.904  0.304
    [4621]  0.696  1.216  1.984  1.096  1.016  1.104  1.296  1.344  1.576  1.544
    [4631]  2.096  0.424  1.336  0.544  0.816  0.696  1.784  0.384  0.936  1.936
    [4641]  0.984  0.936  0.944  1.424  1.304  0.464 -0.144  1.536  1.464  0.336
    [4651]  0.544  1.576  1.696  1.536  1.936  1.224  2.136  0.656  0.464  1.056
    [4661]  0.736  1.664  2.176  0.856  1.504  0.904  0.576  1.616  0.744  1.224
    [4671]  0.864  1.496  1.336  2.104  0.936  1.496  1.384  0.424  1.256  1.016
    [4681]  1.424  0.744  0.664  1.104  1.464  1.296  1.416  1.104  0.896  1.456
    [4691]  0.104  0.776  1.504  0.664  0.536  1.224  1.104  1.456  0.576  0.496
    [4701]  1.464  0.056  1.136  0.664  1.224  0.416  1.304  1.096  1.216  1.504
    [4711]  0.504  1.664  0.896  0.656  0.856  0.416  1.464  1.376  0.304  0.296
    [4721]  0.904 -0.144  1.496  0.424  1.664  1.056  0.936  1.056  0.384  1.704
    [4731]  0.264  1.296  1.536  0.896  1.264  0.824  0.104  0.984  0.344  2.144
    [4741]  1.504  1.576 -0.104  1.464  0.304  0.504  1.344  0.296  0.536  1.304
    [4751]  0.296  1.504  1.256  0.696 -0.184  1.176  0.424  1.344  0.704  0.664
    [4761]  1.496  1.696  0.736  0.104  0.344  1.936  1.696  0.904  0.576  0.944
    [4771]  0.904 -0.104  0.704 -0.144  0.576  0.896  0.976  0.624  0.056  1.336
    [4781]  0.656  0.784  1.224  0.896  1.016  2.176  1.704  1.056  0.816  1.536
    [4791]  1.296  0.664  1.936  0.584  1.064  1.024  0.936  0.776  1.064  1.024
    [4801]  1.336  0.784  0.904 -0.136  1.536 -0.136  1.056  1.536  0.904  1.984
    [4811]  1.136  1.944  0.824  1.344  1.336  0.784  2.136  1.304  1.224  1.224
    [4821]  0.464 -0.176  1.416  0.656  0.464  0.216 -0.136  1.024  0.256  1.376
    [4831]  0.696  0.744  1.216  0.256  0.304  0.584  1.224  0.864  0.064  1.424
    [4841]  1.304  1.504  0.784  1.256  0.776  1.184  2.176  2.176  1.224  0.816
    [4851]  0.224  0.496  0.536  0.376  1.264  1.216  1.904  0.984  0.864  0.696
    [4861]  0.064  0.496  1.296 -0.104  0.216  0.336  0.904  0.496  0.504  0.904
    [4871]  1.224  1.696  0.064  1.256  0.824  1.256  1.224  0.424  1.296  0.416
    [4881]  0.744  1.096  1.336  1.656  2.176  1.456  0.896  1.056  1.024  0.456
    [4891]  0.936  0.464  1.736  0.456  1.936  0.584  0.744  0.504  1.136  0.656
    [4901]  1.016  1.784  0.496  0.536  1.536  1.016  0.936  0.304  1.384  1.704
    [4911]  1.304  0.496  1.016  2.104  1.624  1.456  0.496  0.896  0.816  1.104
    [4921]  1.104 -0.104  0.976  0.424  0.104  0.776  1.976  0.504  1.304  0.624
    [4931]  0.944  0.744  0.456  1.296  0.056  0.824  1.104  1.304  0.936  0.296
    [4941]  0.416  1.104  0.264  0.736  2.184  1.176  0.656  2.136  0.536  0.904
    [4951]  0.504  0.824 -0.136  2.136  0.824  0.224  1.504  0.736  1.496  1.264
    [4961]  1.136  1.184  1.344  0.296  1.224  1.936  1.016  1.096  0.256  0.064
    [4971]  0.224  1.096  1.304  0.336  1.256  0.016  1.736  1.144  1.104 -0.144
    [4981]  1.376  0.456  1.624  1.104  1.056  1.136  1.776  1.264  0.736  0.776
    [4991]  0.936  1.376  0.944  0.256  0.944  1.536  1.576  1.056 -0.096  1.264

## Estimate Dist under HA {data-id="quarto-animate-title"}

---

[← The Null Hypothesis](02-the-null-hypothesis.md) · [Up: contents](index.md) · [Power →](04-power.md)
