---
title: An Alternative Hypothesis
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/10-power-mbi/slides.html
source_file: sources/berkeley-stat158/spring-2026/10-power-mbi/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# An Alternative Hypothesis

**Source:** [`10-power-mbi/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/10-power-mbi/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## An Alternative Hypothesis

Consider a constant shift of 1 for all units.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
tau <- 1
```

## From data to schedule

<style>#wjsynwckji table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#wjsynwckji thead, #wjsynwckji tbody, #wjsynwckji tfoot, #wjsynwckji tr, #wjsynwckji td, #wjsynwckji th {
  border-style: none;
}

#wjsynwckji p {
  margin: 0;
  padding: 0;
}

#wjsynwckji .gt_table {
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

#wjsynwckji .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#wjsynwckji .gt_title {
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

#wjsynwckji .gt_subtitle {
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

#wjsynwckji .gt_heading {
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

#wjsynwckji .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#wjsynwckji .gt_col_headings {
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

#wjsynwckji .gt_col_heading {
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

#wjsynwckji .gt_column_spanner_outer {
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

#wjsynwckji .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#wjsynwckji .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#wjsynwckji .gt_column_spanner {
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

#wjsynwckji .gt_spanner_row {
  border-bottom-style: hidden;
}

#wjsynwckji .gt_group_heading {
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

#wjsynwckji .gt_empty_group_heading {
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

#wjsynwckji .gt_from_md > :first-child {
  margin-top: 0;
}

#wjsynwckji .gt_from_md > :last-child {
  margin-bottom: 0;
}

#wjsynwckji .gt_row {
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

#wjsynwckji .gt_stub {
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

#wjsynwckji .gt_stub_row_group {
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

#wjsynwckji .gt_row_group_first td {
  border-top-width: 2px;
}

#wjsynwckji .gt_row_group_first th {
  border-top-width: 2px;
}

#wjsynwckji .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#wjsynwckji .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#wjsynwckji .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#wjsynwckji .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#wjsynwckji .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#wjsynwckji .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#wjsynwckji .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#wjsynwckji .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#wjsynwckji .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#wjsynwckji .gt_footnotes {
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

#wjsynwckji .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#wjsynwckji .gt_sourcenotes {
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

#wjsynwckji .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#wjsynwckji .gt_left {
  text-align: left;
}

#wjsynwckji .gt_center {
  text-align: center;
}

#wjsynwckji .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#wjsynwckji .gt_font_normal {
  font-weight: normal;
}

#wjsynwckji .gt_font_bold {
  font-weight: bold;
}

#wjsynwckji .gt_font_italic {
  font-style: italic;
}

#wjsynwckji .gt_super {
  font-size: 65%;
}

#wjsynwckji .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#wjsynwckji .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#wjsynwckji .gt_indent_1 {
  text-indent: 5px;
}

#wjsynwckji .gt_indent_2 {
  text-indent: 10px;
}

#wjsynwckji .gt_indent_3 {
  text-indent: 15px;
}

#wjsynwckji .gt_indent_4 {
  text-indent: 20px;
}

#wjsynwckji .gt_indent_5 {
  text-indent: 25px;
}

#wjsynwckji .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#wjsynwckji div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

<style>#ynsqwvtbeb table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#ynsqwvtbeb thead, #ynsqwvtbeb tbody, #ynsqwvtbeb tfoot, #ynsqwvtbeb tr, #ynsqwvtbeb td, #ynsqwvtbeb th {
  border-style: none;
}

#ynsqwvtbeb p {
  margin: 0;
  padding: 0;
}

#ynsqwvtbeb .gt_table {
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

#ynsqwvtbeb .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}

#ynsqwvtbeb .gt_title {
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

#ynsqwvtbeb .gt_subtitle {
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

#ynsqwvtbeb .gt_heading {
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

#ynsqwvtbeb .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ynsqwvtbeb .gt_col_headings {
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

#ynsqwvtbeb .gt_col_heading {
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

#ynsqwvtbeb .gt_column_spanner_outer {
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

#ynsqwvtbeb .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#ynsqwvtbeb .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#ynsqwvtbeb .gt_column_spanner {
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

#ynsqwvtbeb .gt_spanner_row {
  border-bottom-style: hidden;
}

#ynsqwvtbeb .gt_group_heading {
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

#ynsqwvtbeb .gt_empty_group_heading {
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

#ynsqwvtbeb .gt_from_md > :first-child {
  margin-top: 0;
}

#ynsqwvtbeb .gt_from_md > :last-child {
  margin-bottom: 0;
}

#ynsqwvtbeb .gt_row {
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

#ynsqwvtbeb .gt_stub {
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

#ynsqwvtbeb .gt_stub_row_group {
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

#ynsqwvtbeb .gt_row_group_first td {
  border-top-width: 2px;
}

#ynsqwvtbeb .gt_row_group_first th {
  border-top-width: 2px;
}

#ynsqwvtbeb .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ynsqwvtbeb .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#ynsqwvtbeb .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#ynsqwvtbeb .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ynsqwvtbeb .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#ynsqwvtbeb .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#ynsqwvtbeb .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}

#ynsqwvtbeb .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#ynsqwvtbeb .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#ynsqwvtbeb .gt_footnotes {
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

#ynsqwvtbeb .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ynsqwvtbeb .gt_sourcenotes {
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

#ynsqwvtbeb .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#ynsqwvtbeb .gt_left {
  text-align: left;
}

#ynsqwvtbeb .gt_center {
  text-align: center;
}

#ynsqwvtbeb .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#ynsqwvtbeb .gt_font_normal {
  font-weight: normal;
}

#ynsqwvtbeb .gt_font_bold {
  font-weight: bold;
}

#ynsqwvtbeb .gt_font_italic {
  font-style: italic;
}

#ynsqwvtbeb .gt_super {
  font-size: 65%;
}

#ynsqwvtbeb .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}

#ynsqwvtbeb .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#ynsqwvtbeb .gt_indent_1 {
  text-indent: 5px;
}

#ynsqwvtbeb .gt_indent_2 {
  text-indent: 10px;
}

#ynsqwvtbeb .gt_indent_3 {
  text-indent: 15px;
}

#ynsqwvtbeb .gt_indent_4 {
  text-indent: 20px;
}

#ynsqwvtbeb .gt_indent_5 {
  text-indent: 25px;
}

#ynsqwvtbeb .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}

#ynsqwvtbeb div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
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

       [1]  1.344  0.904  1.544 -0.104  0.224 -0.184  0.736  0.704  0.304  1.176
      [11]  1.536  1.544  0.304  0.056  2.184  1.304  0.696  2.096  1.096  1.744
      [21]  0.256  1.784  1.496  1.056  1.184  1.384  0.304  0.864  0.976  0.504
      [31]  0.056  1.704  0.536  0.696  0.776  1.064  0.896  1.216  0.024  0.424
      [41]  0.616  1.456  0.896  0.856  1.736  1.344  0.536  0.336  1.536  0.536
      [51]  0.496  1.496  0.024  1.176  0.336  0.776  1.096  0.816 -0.136  0.664
      [61]  1.216  1.544  0.856  1.496 -0.184  1.424  0.624  1.464  0.784  0.944
      [71]  0.704  0.096  1.176  1.184  0.976  1.064  1.504  0.056  0.064  0.944
      [81]  0.856  0.504  1.576  1.064  1.896  0.696  1.056  0.424  1.504  0.904
      [91]  0.936  1.256  1.496  0.936 -0.144  0.584  1.744  0.016  1.096  1.064
     [101]  0.736  0.864  0.704  0.304  0.224  1.056  1.696  1.496  1.264  0.904
     [111]  0.016  0.696  1.096  0.536  0.496  1.056  0.296  1.296  1.264  1.376
     [121]  0.736  0.536 -0.096  1.104  1.736  0.104  1.896  1.376  0.296  0.224
     [131]  0.576  0.496  1.264  1.336  1.136  0.304  1.104  0.944  1.296  1.104
     [141]  2.104  1.016  0.304  0.904  1.584  0.904  0.256  1.344  1.184  0.864
     [151]  1.296  1.656  1.696  1.056  1.464  0.064  0.544  0.904  0.296  1.904
     [161]  0.224  0.536  0.736  1.096  1.304  0.704  0.944  0.984  1.376  1.056
     [171]  1.136  0.776  0.864  0.936  1.496  0.736  0.744  1.104  1.176  1.784
     [181]  0.944  0.816  1.264  0.976  1.336  0.816  1.104  1.344  0.624  1.256
     [191]  0.656  0.416  0.904  1.024  1.056  0.256  0.736  1.344  1.224  1.064
     [201]  1.256  1.984  0.256  0.896  0.464  1.664  1.024  1.704  0.024  2.104
     [211] -0.144  0.816  1.464  1.024  0.736  1.944  0.384  1.624  0.624  0.304
     [221]  1.464  1.296  1.024  0.776  0.984  0.936  1.496  0.504  1.736  1.144
     [231]  1.944  1.304  0.504  0.504  0.736  0.776  1.096  1.464  1.296  0.904
     [241]  1.584  0.264  0.216  1.536  1.984  0.864  1.424  1.216  0.216  1.984
     [251]  2.144  1.776  0.064  0.704  1.464  0.976  0.504  0.416  1.744  0.736
     [261]  0.984  0.824  0.504  0.936  0.664  0.016  1.656  2.176  0.704  1.256
     [271]  0.496  0.896  0.936  0.496  0.424  0.344  0.896  0.264  0.024  0.856
     [281]  1.496  0.504  1.424 -0.136  1.104  1.576  0.504  0.656  1.496  1.504
     [291]  0.064  0.856  0.864  1.056  1.496  1.536  0.624  1.344  0.944  1.096
     [301]  1.584  1.176  1.664  0.816  1.944  1.896  0.704  0.616  1.264  1.776
     [311]  0.304  1.376  0.496  0.704  1.296  0.776  1.464  1.136  0.336  0.696
     [321]  0.416  1.344  0.016  0.904  0.536  1.536  1.776  0.904  1.544  1.384
     [331]  1.264 -0.136  0.696  0.424  1.696  1.496  1.536  1.616  0.896  0.704
     [341]  0.984  1.416  0.296  0.464  0.656  1.536  0.296  1.424  1.016  1.264
     [351]  0.856  1.504  1.184  0.216  0.776  1.736  1.624  0.776  1.904  1.096
     [361]  0.944  0.904  1.016  0.264  0.576  0.504  0.504  0.224  0.944  1.224
     [371]  0.056  1.176  1.256  0.536  1.376  2.184  0.256  0.696  1.344  0.544
     [381]  1.104  1.136  2.176  1.304  0.816  2.144  1.056  0.224  1.216  1.224
     [391]  1.536  1.064  2.144  1.976  0.064  0.896  2.136  1.016  2.136  1.656
     [401]  1.064  1.096  0.864  1.344  0.696  0.456  0.544  0.264  0.664  0.984
     [411]  0.856 -0.176  1.024  0.936  1.496  1.536  0.064  1.776  0.664  1.016
     [421]  0.936 -0.176  1.576  0.696  0.496  1.216  0.256  1.264  1.944  0.336
     [431]  1.024  1.416  0.816  1.704  1.464  0.896  0.944  1.576  1.144  0.944
     [441]  0.664  0.056  1.776  0.584  0.936  1.744  1.584  2.136  1.184  0.344
     [451]  1.584  1.536  0.824  1.536  1.224  0.864  1.696  1.216  1.064  1.224
     [461]  0.256  1.464  0.584  0.856  0.816  0.384  1.744  1.256  2.104  1.344
     [471]  0.664  0.664  0.304  0.936  1.104  0.576  1.304 -0.096  0.984  0.576
     [481]  1.536  1.504  0.696  1.656  1.056  1.336  1.616  1.024  1.536  1.104
     [491] -0.184  0.816  0.784  0.096  0.776  1.656  1.376  1.136  0.056  1.496
     [501]  1.616  1.944  0.904  1.064  0.064  0.936  1.376  1.016  1.504  1.056
     [511]  0.464  1.344  1.264  1.736  0.224  0.336  1.104  0.096  0.624  0.936
     [521]  0.624  1.096  0.256  0.864  1.104  1.416  1.104  1.704  0.736  1.504
     [531]  0.544  0.296  0.704  0.056  1.496  0.664  0.664  0.304  0.744  0.776
     [541]  0.544  1.584  1.104  1.104  0.904  0.304  1.064  0.264  1.104  1.944
     [551]  0.336  0.936  1.104  1.424  0.304  0.824  0.944  0.624  0.864  1.504
     [561]  1.056  0.296  1.416  0.256 -0.184  0.896  1.456  1.376  0.504  1.176
     [571]  0.256  1.336  1.976  0.296  0.704  1.064  1.536  1.344 -0.184  1.016
     [581]  1.344  0.064  0.736  0.584  0.336  0.304  0.256  1.496  1.536  1.064
     [591]  1.224  1.144  1.024  1.584  0.864  1.336  1.336  2.184  0.544  0.576
     [601]  1.296  1.704  1.704  1.144  1.664  1.296  1.136 -0.184  0.864  1.264
     [611]  1.736  0.904 -0.184  1.176  1.776  0.536  1.056  0.544  1.096  1.264
     [621]  1.104 -0.176  1.184  1.216  1.496  1.984  1.496  1.224  1.184  0.904
     [631]  1.624  1.064  0.936  1.776  1.584  0.784  0.576  0.896  1.784  0.264
     [641]  0.304  1.096  1.216  0.336  1.976  0.736  1.424  0.336  1.336  1.336
     [651]  0.864  1.416  1.104  0.264  1.944  1.504  0.056  0.264  1.776  1.016
     [661]  0.104  1.504  0.016  1.104  0.864  0.576  1.336  0.656  2.136  0.944
     [671]  0.496  0.504  0.824  0.896  0.784  1.256  1.464  1.096  0.224  0.696
     [681]  0.096  1.584  0.904  1.496  0.496  2.136  0.104  1.504  1.464  0.344
     [691]  1.584  1.384 -0.096  0.944  2.104  0.576  1.344  1.736  0.776  1.464
     [701]  1.344  0.984  1.104  0.256  1.096  1.136  0.304  0.736  0.664  0.736
     [711]  0.456  1.384  0.896  0.976  0.976  1.064  0.704  0.744  1.984  0.656
     [721]  0.816  0.416  0.984  0.576  1.296  1.496  1.296  1.736  1.024  0.696
     [731]  0.296  0.984  0.744  0.256  1.744  1.424  1.664  0.624  1.744  1.416
     [741]  1.184  1.176  1.064  1.504  0.936  0.696 -0.176  0.896  0.696  0.064
     [751]  0.464  1.704  0.536  1.704  1.064  0.496  0.664  0.744  0.736  2.176
     [761]  0.304  1.536  0.296  0.784  0.576  0.624  1.464  1.064 -0.096  1.144
     [771]  0.984  0.504  1.976  0.256  0.896  1.704  0.784  0.496  0.776  0.056
     [781]  0.584  1.016  0.944  0.096  0.536  1.176  1.064  2.136  1.224  1.344
     [791]  1.064  0.696  1.496 -0.184  1.016  0.936  0.016  1.624 -0.176  0.736
     [801]  0.256  0.296  1.464  1.176  0.344  1.496  1.056  1.344  1.416  2.184
     [811]  0.944  1.584  0.456  1.264 -0.184  0.824  0.696  1.664  0.744  0.344
     [821]  1.096  1.576  0.904  1.504  1.904  1.536  1.744  1.384  1.784  1.584
     [831]  1.344  0.776  1.504  1.744  0.744  0.984  0.696  0.384  0.216  0.576
     [841]  1.424  1.096  1.296  0.704  1.304  0.696  0.896  1.096  0.904  1.984
     [851]  0.336  0.776  0.896  0.776  1.264  0.736  1.064  1.064  0.464  1.496
     [861] -0.096  1.176  1.416  0.736  1.184  0.256  1.024  1.464  0.664  1.704
     [871]  1.296  0.224  0.376  2.144  0.624  0.744  0.504  1.416  1.616  0.856
     [881]  0.936  1.024  0.416  0.496  0.824  1.296  0.504  1.224  0.936  1.064
     [891]  0.336  1.464  1.256  0.496  0.856  1.584  1.024  2.184 -0.104  0.736
     [901]  0.096  0.696  0.896  1.176  2.136  1.024  0.384  0.496  1.264  0.704
     [911]  0.344  0.736  1.176  1.264  0.784  0.544  0.464  0.704  1.536  2.096
     [921]  0.896  0.896  1.424  0.744  1.096  1.344  0.664  1.224  0.064  0.936
     [931]  1.464  1.016  1.304  0.736  0.624  1.296  1.104  1.704  1.336  1.776
     [941]  0.856  1.296  0.904  0.744  1.096  0.256  1.464  1.744  1.944  0.624
     [951]  0.744  0.944  0.864  0.024  0.736  1.704  0.744  1.216  1.064  0.464
     [961]  0.656  1.496  0.024  0.496  1.064  1.224  1.296  1.224  1.224  1.176
     [971]  1.016  0.624  0.616  1.376  0.096  1.344  0.824  1.464  0.744  0.864
     [981]  1.344  2.144  1.064  1.696 -0.176  0.736  1.536  0.504  1.144  0.824
     [991]  0.456  1.176  1.664  1.144  0.656 -0.136  1.104  0.496  0.056  0.664
    [1001]  0.056  0.416  0.464  0.904  1.216  1.376  0.824  1.144  1.696  1.176
    [1011] -0.104  0.936  1.576  0.856  1.344  0.504  0.784  0.656  0.824  1.736
    [1021]  1.224  0.704  1.296  0.984  0.656  0.104  1.304  1.984  1.984  0.456
    [1031]  0.904  0.856  1.344  1.064  0.576  0.704  0.064  1.944  1.104  0.776
    [1041]  0.056  0.776  1.376  0.824  1.104  1.104  1.376  0.944  0.496  0.496
    [1051]  1.104  1.336  0.024  1.264  0.976  0.824  0.736  0.984  0.904  0.664
    [1061]  1.296  0.536  0.464  1.344  0.656  1.736  1.176  0.384  0.864  0.984
    [1071] -0.136  0.544  1.944  0.536  0.936  1.056  0.064  0.496  0.056  0.904
    [1081]  1.344  1.344  1.144  1.096  1.064  0.784  1.576  0.064  1.936  1.136
    [1091]  0.024  1.376  1.264  0.224  1.504  0.904  1.704 -0.176  0.496  2.104
    [1101]  1.176  1.096  0.664  0.824  0.904  0.744  1.944  0.544  1.256  0.304
    [1111]  1.784  0.696  0.656  0.336  0.224  1.024  0.784  0.464 -0.104  0.736
    [1121]  1.584  1.664  0.896  1.464  0.536  1.376  0.224  1.056  0.976  1.624
    [1131]  0.936  1.456  1.416  2.104  1.784  0.704  0.976  0.016  0.864  0.944
    [1141]  0.256  0.816  1.896  0.696  2.104  0.256  1.536  0.824  0.736  0.696
    [1151]  0.896  1.664  1.104  1.976  1.104  0.736  0.864  1.576  0.616  0.464
    [1161]  1.064  1.104  1.384  1.096  1.096  1.224  0.744  0.864  0.744  1.056
    [1171]  1.456  0.704  1.344  2.136  0.976  0.424  0.464  0.976  1.216  0.096
    [1181]  0.936  0.704  1.664  1.536  1.736  1.584  0.056  0.976  1.064  1.376
    [1191]  1.696  0.576  1.504  1.776  1.056  0.856  1.296  0.304  0.896  1.336
    [1201]  0.336  1.176  0.576  1.744  0.704  0.296  0.936  0.696  0.904  0.656
    [1211]  0.816  1.936  1.904  1.904  1.984  1.344  1.544  1.056  1.144  0.944
    [1221]  1.136  1.696  1.216  1.056  1.704  0.864  1.176  1.584  0.504  1.776
    [1231]  1.096  1.656  1.496  1.024  1.664  1.744  1.744  0.816  1.304  1.344
    [1241]  1.136  1.704  1.584  1.136  1.744  1.096  0.544  0.496  1.544  1.416
    [1251]  0.296  0.656  1.216  1.304  1.344  0.624  1.656  1.056  0.656  0.704
    [1261]  0.664  1.216  0.456  0.496  0.944  1.416  1.896  0.536  0.264  1.584
    [1271]  1.096  1.464  1.744  1.424  1.576  0.736  1.536  1.176  1.136  1.104
    [1281]  0.776  1.224  0.736 -0.176  1.144  0.936  0.424  0.776  0.904  0.696
    [1291]  0.896  1.424  1.696  1.096  1.056  0.256  1.024  0.456  1.296  1.136
    [1301]  0.256  0.736  1.024  0.624  1.656  0.736  0.016  0.896  1.576  1.624
    [1311]  0.696  1.576  1.136  0.216  1.256  1.136  0.936  0.904  1.024  2.096
    [1321]  1.976  1.064  0.864  1.376  0.896  1.024  0.656  1.536  0.976  0.624
    [1331]  0.736  1.104  1.744  1.016  0.736  0.704  1.144  1.544 -0.176  0.704
    [1341]  0.976  0.056  0.856  0.624  0.504  0.944  1.096  0.536  1.504  0.976
    [1351]  1.416  1.296  1.336  1.576  0.336  1.424  1.376  0.784  1.984  1.904
    [1361]  1.696  0.896  0.704  1.584  0.424  0.464  1.344  0.496 -0.096  0.536
    [1371]  0.224  0.264  0.896  1.104  1.504  1.584  1.264  0.776  0.024  1.704
    [1381]  0.664  0.304  1.984  1.344  0.936  0.896  0.904  0.816  1.344  0.456
    [1391]  0.456  0.656  1.216  0.704  1.944  0.304  0.624  1.736  1.416  0.384
    [1401]  0.624  0.856  0.064  1.304  1.504  0.544  0.504  0.824  0.536  1.416
    [1411]  1.304  1.056  1.656  0.536  0.904  0.224  1.424  0.544  0.744  1.064
    [1421]  1.224  1.024 -0.144  2.096  1.096  0.904  0.736  0.656  1.336  1.136
    [1431]  0.256  0.304  1.384 -0.136  0.984  1.736  1.464  2.176  1.136  1.304
    [1441]  1.376  0.936  0.904  0.704  1.464  1.576  1.496  0.344  1.544  0.504
    [1451]  1.664  0.896  1.224  0.744  1.096  0.576  1.704  0.856  0.656  0.784
    [1461]  1.464  1.416  0.536 -0.176  0.624  1.896  1.744  0.896  1.336  0.456
    [1471]  0.416  0.944  0.696  1.944  0.344  0.936  0.696  0.264  0.976  1.456
    [1481]  0.536  1.144  1.904  1.304  1.016  0.416  0.656  1.504 -0.136  1.496
    [1491]  1.376  0.824  0.624  0.944  0.704  0.864  0.736  0.896  1.056  1.536
    [1501]  1.776  1.296  1.936  0.104  1.296  1.664  1.736  0.416  0.416  0.264
    [1511]  0.736  1.336  1.744  1.304  1.344  1.096  1.976  0.936  1.296  1.696
    [1521]  1.536  1.344  1.264  0.016  1.264  1.256  1.584  0.624  1.056  0.416
    [1531]  0.976  1.104  1.424  1.664  1.256  1.536  2.184  0.856  1.056  0.856
    [1541]  0.256  2.144  0.736  0.056  0.544  0.736  1.704  0.464  0.736  0.256
    [1551]  1.496  1.496  0.576  1.504  1.496  0.024  1.544  1.176  1.416  0.544
    [1561]  1.664  1.264  1.344  1.976  1.944  0.856  0.776  0.304  1.736  1.584
    [1571]  1.184  0.224  0.576 -0.096  0.944 -0.184  1.696  0.824  0.224  0.896
    [1581]  0.696  0.504  0.976  0.696  0.504  1.136  1.136  0.664  1.744  0.936
    [1591]  0.216  1.464  1.704  1.144  1.176  1.744  1.016  0.984  0.944 -0.104
    [1601]  0.744  1.536  0.696  0.336  0.976  0.624  1.736  0.736  0.544  0.504
    [1611]  0.264  0.656  0.296  0.616  1.384  0.904  0.336  0.824  1.136  0.344
    [1621]  1.264  1.416  0.384  1.104  0.584  1.696  0.984  1.696  0.024  1.384
    [1631]  0.696  0.936  0.024  0.904  0.744  0.776  0.896  0.256  1.224  0.904
    [1641]  0.224 -0.144  0.864  0.736  1.264  1.064  1.336  0.744  1.376  0.856
    [1651]  1.264  1.256  0.304  0.416  0.496  0.984  1.784  1.576  1.336  1.184
    [1661]  0.256  1.136  0.456  1.624  1.576  0.216  0.744  1.224  0.224  1.304
    [1671]  2.176  1.704  2.176  0.056  0.936  1.496  0.776  1.464  2.176  0.416
    [1681]  0.656  0.744  0.616  1.016  0.464  0.304  1.016  1.264  0.744  1.496
    [1691]  1.184  0.216  1.456  1.216  1.176  1.504  1.576  0.496  0.696  1.344
    [1701]  2.104  1.656  0.424  1.496  1.096  0.856  1.696  1.096  1.176  0.664
    [1711]  0.936  1.944  0.016  0.896  1.944  1.224  1.504  1.304  1.264  1.504
    [1721]  1.776  0.896  1.304  0.736  0.736  1.224  1.296  0.936  2.144  1.976
    [1731]  1.984  1.016  1.616  1.336  2.144  1.304  0.064  0.896  0.384  0.944
    [1741]  0.744  1.096  1.024  0.936  1.536  1.504  1.056  1.296  2.176  1.136
    [1751]  1.136  1.056  0.296  0.744  0.896  2.144  1.056  1.784  1.256  0.256
    [1761]  0.744  0.816  0.296  0.304  1.024  0.416  1.624  0.584  2.184  0.976
    [1771]  0.544  0.704  1.944  0.944  0.024  1.304  0.104  0.624  0.296  1.936
    [1781]  1.416  1.496  1.064  1.184  1.664  0.824  1.536  0.936  1.056  1.184
    [1791]  0.816  1.976  0.624  1.344  0.456  1.984  0.496  1.336  1.104  1.464
    [1801]  1.344  2.144  0.696  1.344  1.096  1.016  1.984  0.656  0.416  0.856
    [1811]  0.264  0.296  1.016  0.104  1.104  1.456  0.856  0.704  0.464  1.304
    [1821]  0.424  1.504  1.104  0.984 -0.144  1.536  1.104  0.744  0.824  1.336
    [1831]  1.984  1.704  1.104  0.696  0.224  0.904  1.384  0.976  0.624  0.824
    [1841]  0.744  0.944  1.176  0.896  0.776  1.256  0.624  0.096 -0.136  1.576
    [1851]  1.496  1.656  1.104  0.304  0.984  0.256 -0.176  0.336  1.136  0.784
    [1861]  0.656  1.536  0.264  0.464  1.056  1.744 -0.144  0.624  0.616  0.936
    [1871]  1.024  0.264  0.496  0.904  2.144 -0.136  1.904  0.024  1.264  0.456
    [1881]  1.576  1.944  0.864  0.864  1.104  1.464  1.264  1.064  0.584  0.496
    [1891]  1.016  1.144  0.944  0.904  1.216  1.304  1.296  1.936  0.624  1.216
    [1901]  0.744  1.376  0.624  1.176  0.464  1.176  0.784  1.736  0.304  0.904
    [1911]  0.304  2.104  0.824  1.344  1.504  0.976  1.104  1.576  1.256  0.864
    [1921]  1.936  1.296  0.904  0.824  0.496  0.624  0.296  1.776  2.096  0.536
    [1931]  0.704  1.104  0.336  0.936  0.304  0.904  0.056  1.056  1.664  0.464
    [1941]  1.384 -0.104  0.984  0.264  0.856  1.176  1.224  0.896  0.624  1.576
    [1951]  1.144  0.944  0.656  1.016  1.496  1.056  0.864  1.096  1.936  0.376
    [1961]  1.496  1.536  1.616  0.504  1.536  0.064  0.904  0.856  0.504  1.664
    [1971]  1.176  0.896  1.936  1.344  1.024  1.344  1.136  1.504  0.776  0.736
    [1981]  0.576  0.776  1.376  1.056  0.096  1.536  1.704  1.896  1.216  0.864
    [1991]  1.056  0.056  0.976  0.904  1.096  1.056 -0.144  1.736  2.136  2.184
    [2001]  0.336  0.856  1.264  0.904  0.936  0.104  0.096  0.304  1.064  0.024
    [2011]  0.904  0.704  1.544  1.464  0.864  1.304  1.064  0.384  1.504  1.416
    [2021]  1.096  0.944  0.904  0.264  1.096  0.424  1.224  0.296  0.576  1.136
    [2031]  0.576  0.464  2.184  0.576  0.784  1.024  1.784  0.456  0.256  1.064
    [2041]  0.904  0.776  0.736  0.864  0.456 -0.096  0.296  1.016  1.944  0.656
    [2051]  0.424 -0.184  0.744  0.056  0.504  0.496  1.344  0.536  1.016  0.536
    [2061]  0.216  0.944  0.864  0.216  0.936  0.816  0.376  1.296  1.064  0.544
    [2071]  0.856  0.224  1.264  1.304  0.896  1.376  0.936  1.416  0.696  1.576
    [2081]  1.536  0.776  1.576  1.136  0.264  0.904  0.864  1.296  0.664  1.064
    [2091]  1.704  0.704  0.624  0.656  1.744  0.264  1.536  1.704  1.896  1.256
    [2101]  1.624  0.984  1.664  0.336  1.544  0.736  0.104  0.464  1.104  0.056
    [2111]  0.864  1.896  0.264  1.504  1.264  1.264  0.976  0.816  0.536  0.656
    [2121]  0.776  0.896  1.264  1.224  0.536  0.704  0.824 -0.136  1.176  1.176
    [2131]  0.584  0.584  1.024  1.096  0.904  0.016  0.216  1.664  2.136  1.096
    [2141]  0.784  0.584  0.264  0.464  0.864  1.496  1.176  0.336  1.136  0.664
    [2151]  1.496  0.544  0.296  1.936  1.376 -0.184  1.384  0.776  1.256  1.464
    [2161]  2.096  0.936 -0.184  1.616 -0.104  1.664  0.224  1.224  1.536  0.056
    [2171]  1.936  1.176  1.096  0.256  0.904  0.576  1.176  0.936  1.336  0.264
    [2181]  1.496  0.216  0.704  0.416  0.384  1.056  1.456  1.104  0.776 -0.176
    [2191]  0.536  1.704  0.296  1.176  0.344  1.656  1.224  0.824  0.904  1.576
    [2201]  0.536  0.656  1.264  0.464  1.144  1.496  2.136  1.504  1.224  1.584
    [2211]  1.944  1.016  0.704  0.064  0.216  1.016  0.896  0.776  0.696  0.696
    [2221]  0.696  1.064  1.464  1.336  0.504  1.664  1.696  0.736  0.304  0.656
    [2231]  1.496  0.656  1.584  0.904  1.776  0.704  1.104  1.504  0.904  1.264
    [2241]  1.064  0.416  0.216  2.136  1.064  0.224  1.456  0.696  1.536  1.504
    [2251]  1.776  1.096  1.256  1.216  1.176  1.136  1.104  1.544  1.104  1.944
    [2261]  1.264  1.136  0.264  0.896 -0.104  0.296  0.776  1.224  1.536  0.976
    [2271]  0.456  0.936  1.344  1.016  1.944  1.136  1.416  0.864  1.224  1.224
    [2281]  1.584  1.664  0.496  0.936  1.376  1.056  1.904  0.544  0.536  0.464
    [2291]  1.144  0.424  0.056  1.176  0.976  1.664  0.256  0.736  0.096  0.496
    [2301]  0.856  1.096  0.824  0.616  0.896  1.456  0.864  0.896  0.904  0.896
    [2311]  0.656  0.464  1.264  1.016  1.944  1.344  0.784  1.304  0.656  0.944
    [2321]  0.424  0.256  1.184  0.864  0.504  1.304  1.376  0.696  0.384  1.536
    [2331]  1.304  1.536  0.064  0.296  1.416  1.304  1.464  0.984  0.656  0.064
    [2341]  1.176  1.504 -0.096  0.464  0.504  0.256  0.224  0.856  1.576  1.064
    [2351]  0.504  1.224  0.296  1.896 -0.184  1.136  1.704  1.584  1.544  0.704
    [2361]  0.496  0.464  1.224  1.296 -0.096  0.864  1.984  0.976  0.736  0.416
    [2371]  0.304  0.336  1.504  1.536  0.416  1.144  1.224  0.744  1.224  1.064
    [2381]  1.136  1.736  0.464  0.824  0.856  0.856  0.104  0.936  0.296  0.616
    [2391]  0.664  1.264  1.176  0.864  0.576  1.264 -0.104  1.944  0.784  1.704
    [2401]  0.664  0.584  1.184  1.056  1.144  0.624  0.064  0.096  0.024  0.776
    [2411]  0.376  1.304  1.024  0.624  0.864  0.536  1.224  1.616  0.464  1.096
    [2421]  0.344  0.416  0.696  0.496  1.056  0.856  0.816  0.016  0.936  0.744
    [2431]  0.456  1.256  0.496  1.224  1.136  0.496  0.584  1.304 -0.184  1.184
    [2441]  1.184  1.304  1.144  1.904  0.856  1.456  1.544  1.776  0.464  1.136
    [2451]  1.776  0.936  0.944  2.136 -0.104  1.024  0.984  0.704  0.904  0.944
    [2461]  0.536  0.744  0.944  1.096  1.496  1.024  0.944  1.296  1.656  1.144
    [2471]  1.496  1.264  0.216  1.224  0.896  1.976  0.744  1.536  1.256  2.184
    [2481]  0.216  1.344  0.896  2.176  1.416  0.216  0.824  1.904  0.864  1.656
    [2491]  1.096  1.584  0.256  0.904  1.264  1.304  0.584  1.224  1.536  0.936
    [2501]  0.896 -0.176  1.696  1.504  1.056  1.496  0.064  1.176  1.104  1.496
    [2511]  1.776  1.896  0.296  0.416  0.896  0.224  1.256  1.144  0.416  1.344
    [2521]  2.136  0.056  1.136  0.984  1.096  1.344  1.416  0.256  1.776  0.416
    [2531]  1.064  0.976  1.176  0.464  0.664  0.904  0.736  0.656  1.696  1.056
    [2541]  0.536  1.096  0.224  1.536  1.136  1.104  0.704  1.696  0.016  0.024
    [2551]  0.984  0.784  0.024  1.304  0.856  0.744  1.616  0.664  0.976  1.424
    [2561]  0.456  1.096  0.064  1.376  0.304  0.576  0.984  1.744  0.776  0.936
    [2571]  1.184  1.344  1.104  0.536  0.744  1.776  0.696  1.056  0.496  1.216
    [2581]  1.144  0.104  0.704  1.664  1.424  1.104  0.096  0.064  1.736  1.504
    [2591]  0.624  0.944  1.264  1.544  0.056  1.896  1.096  0.424  0.464  0.304
    [2601]  0.936  2.096  1.776  0.016  0.264  0.496  1.016  0.856  1.704  0.504
    [2611]  1.304  0.664  1.104  0.864  1.104  0.224 -0.184  0.904  1.344  1.176
    [2621]  1.264  0.736  1.096  1.504  1.704  0.904  0.824  0.624  0.816  1.504
    [2631]  0.024  2.184  0.864  0.496  1.704  1.664  0.824  0.696  0.736  2.176
    [2641]  0.656  1.056  1.336  0.504  1.344  0.744  0.784  1.064  0.264  0.296
    [2651]  0.744  1.744  0.536  2.176  1.696  0.984  0.824  0.824 -0.144  0.944
    [2661]  1.504  1.264  0.856  1.584  1.304  1.304  0.744  1.304  0.616  1.096
    [2671]  1.064  0.856 -0.176  1.176  1.256  0.424  1.576  1.504  2.144 -0.136
    [2681]  0.896  0.584  0.256  1.376  1.344  1.264  0.024  0.056  0.424  0.504
    [2691]  0.864  1.424  1.704  1.064  0.336  1.464  1.584  1.536  0.736 -0.136
    [2701]  1.184  1.024  0.864  1.624  2.144  1.664  1.376  0.304  0.696  0.864
    [2711]  1.976  1.376  1.064  1.504  0.824  0.616  0.736  0.736  0.656  0.784
    [2721]  1.336  0.704  0.904  0.736  0.856  1.536  1.264  0.704  1.544  1.904
    [2731]  1.296  0.304  0.544  1.224  1.504  0.504  1.176  1.616  1.536  0.936
    [2741]  1.096  0.744  0.336  1.376  1.504  0.944  1.136  1.024  0.696  1.736
    [2751]  1.536  0.336  1.416  1.504  1.296  1.184  0.904  1.344  1.616  0.416
    [2761]  0.976  1.464  1.344  1.536  0.536  0.744  1.576  0.416  1.104  0.744
    [2771]  1.184  0.016  0.264  0.776  1.496  0.816  0.936  1.544  0.696  2.176
    [2781]  0.904  0.944  1.696  1.664  0.936  1.296  1.064  0.696  1.096  1.384
    [2791]  0.936 -0.144  0.504  0.576  1.704  1.376  0.056  1.224  1.056  0.824
    [2801]  0.856  2.144  1.056  1.056  0.264  0.664  1.256  2.176  0.264  0.296
    [2811]  1.136  0.936  0.936  0.864  1.016  0.936  1.336  1.016  1.344  2.184
    [2821]  0.664  0.496  0.904  0.824  1.896  0.576  0.656  0.264  1.104  0.896
    [2831]  0.456  1.936  0.264  0.656  1.736  1.344  0.976  1.544  1.384  1.464
    [2841]  1.704  1.664  1.496  1.224  1.104  1.024  1.624  0.016  0.336  0.584
    [2851]  0.056  1.064  0.424  1.264  1.944  0.664  0.744  1.144  0.544  1.456
    [2861]  1.896  1.944  0.576  1.504  1.096  1.496  0.704  1.104  0.624  1.096
    [2871]  0.216  2.136  0.504  0.064 -0.096  1.344  0.304  0.224  1.904  0.544
    [2881]  0.984  1.344  0.944  1.336  0.464  0.304  0.496  0.464  1.656  0.624
    [2891]  0.344  0.424  1.296  1.344  2.144  1.576  0.424  0.296  1.424  0.264
    [2901] -0.136  1.744  1.144  1.304  1.056  0.536  1.544  0.064  1.256  1.696
    [2911]  1.376  1.296  1.144  0.544  0.904  0.224  1.536  1.544  1.704  0.336
    [2921]  1.096  1.056  0.384  1.184  1.304  1.304  1.056  1.456  0.104  0.944
    [2931]  0.256  0.376  0.464  1.944  0.856  2.144  0.504  1.744  2.176  0.256
    [2941]  1.144  1.536  0.304  1.584  0.976  1.304  1.384  2.136  1.264  1.064
    [2951]  0.936  0.944  0.336  0.936  1.696  0.896  0.416  1.504  1.264  0.504
    [2961]  0.024  1.576  1.064  1.096  1.336  0.464  0.704 -0.096  1.304  1.016
    [2971]  1.904  1.216  0.704  2.184  0.776  1.504  0.504  1.384  1.304  0.976
    [2981]  1.664  1.176  0.664  1.216  1.696  0.896  0.896  0.656  0.056  0.936
    [2991]  0.496  1.336  0.296  0.896  0.224  0.864  0.744  0.584  1.376  1.696
    [3001]  1.224  0.904  0.336  0.656 -0.096  1.264  1.344  0.656  0.896  0.504
    [3011]  1.056  1.256  0.456  0.536  0.496  2.136  0.304  1.096  2.096  0.896
    [3021]  1.544  0.744  1.176  1.256  0.944  1.184  0.776  1.344  0.424  0.264
    [3031]  1.104  0.384  1.536  1.264  0.576  0.536  1.056  0.616  0.864  0.304
    [3041]  1.304  0.864  0.624  1.904  0.696  0.536  1.664  2.144  1.096  0.904
    [3051]  1.096  1.064  1.536  1.064  0.744  0.504  0.224  1.616  1.776  0.936
    [3061]  1.336  1.224  1.464  1.536  1.136  1.776  0.576  0.504  0.424  0.936
    [3071]  1.696  0.984  1.104  1.544  0.896  0.776  0.464  0.056  0.624  1.504
    [3081]  1.264  1.976  1.176  0.536  1.144  0.304  1.056  1.224  1.784  1.776
    [3091]  0.704  1.064  0.816  1.536  1.344  0.656  1.176  1.296  1.104 -0.176
    [3101]  1.704  1.496 -0.104  1.216  0.784  0.424  1.184 -0.104  0.896  0.504
    [3111]  0.784  0.936  0.464  1.136  1.536  1.136  1.416  0.624  0.984  0.944
    [3121]  1.256  0.896  0.024  2.104  1.104  1.536  0.424  0.776  0.736  1.336
    [3131]  0.936  0.904  0.536  1.056  0.376  0.776  0.584  1.504  0.016  0.776
    [3141]  1.176  1.136  1.064  0.936  0.856  0.984  1.376  0.624  0.776  0.024
    [3151]  1.096  1.024  1.424  0.016  1.664  2.184  0.496  0.264  1.696  0.296
    [3161]  0.496  0.096  1.136  1.216  1.024  0.296  1.616  0.936  0.776  0.784
    [3171]  1.296  0.384  1.224  1.336  1.464  1.184  1.136  0.704  0.656  0.704
    [3181]  1.016  0.984  1.776  1.736  0.576  0.816  0.904  0.944  0.656  1.256
    [3191]  0.224  0.744  1.176  1.416  0.336  0.696  0.496  1.024  1.264  1.344
    [3201]  0.776  0.224  1.056  1.536  0.504  0.704  1.936  0.656  1.336  1.936
    [3211]  0.704  0.504  0.296  1.664  1.136  1.736  1.536  0.896  1.136  0.296
    [3221]  1.584  1.096  0.496  1.504  0.864  1.016  2.104  0.944  1.736  0.696
    [3231]  1.304  1.584  0.984  1.624  0.464  1.136  1.104  0.664  1.024  0.504
    [3241]  1.304  1.064  1.464  0.984  0.536  1.104  0.864  1.104  0.904  1.056
    [3251]  1.096  1.224  0.864  1.696  0.544  0.304  1.784  1.416  0.824  1.104
    [3261]  0.536  2.176  0.416  1.064 -0.096  2.104  0.336  1.584  1.264  1.696
    [3271]  0.864  1.216  0.904  0.256  1.736  2.144  1.376  1.616  1.296  1.064
    [3281]  0.696  1.704  0.944  1.944  0.944  1.904  1.264  1.344  0.624  0.376
    [3291]  1.576  1.056  0.056  1.536  1.056  0.984  0.744  0.776  0.424  0.776
    [3301]  1.136  0.504  1.504  1.096  0.616  0.024  1.464  1.696  0.736  0.984
    [3311]  0.984  1.224  1.464  1.984  1.776  0.864  1.416  0.736  0.456  0.936
    [3321]  1.936  0.464  0.464  0.936  1.104  0.256  1.344  1.016  1.264  1.616
    [3331]  0.864 -0.184  1.664  1.584  1.544  0.504  0.824  1.544  1.584  1.024
    [3341]  0.696  0.224  0.016  1.304  0.224  0.056  1.176  1.776  1.344  0.576
    [3351]  0.904  0.824  1.104  1.304  0.296  0.696  1.144  2.184  1.256  0.536
    [3361]  1.544  0.304  0.416  1.344  0.304  0.944  0.584  0.936  1.104  0.456
    [3371]  1.616  0.904  0.496  1.064  0.976  0.464  1.504  1.576  0.264  0.456
    [3381]  0.816  0.864  0.776  1.144  1.144  1.016  0.976  0.904  0.784  1.624
    [3391]  1.136  0.736  1.264  2.176  0.056  2.144  1.464  1.496  1.304  1.944
    [3401]  1.416  0.976  1.696  0.104  0.976  0.056  0.496  0.904  0.056  0.976
    [3411]  1.024  1.064  1.344  0.224  1.056  0.824  0.824  0.936  1.576  1.464
    [3421]  1.744  0.616  0.864  0.576  2.184  0.064  0.544  0.704  1.464  0.944
    [3431]  0.424  1.264  1.304  0.656  0.216  1.696  0.344  0.696  1.984  2.144
    [3441]  0.904  1.264  0.816  0.936  1.616  0.536  0.736  1.496  0.544  0.064
    [3451]  1.576  1.376  0.984  1.296  2.104  0.536  0.656  0.104  1.696  1.896
    [3461]  1.264  0.256  1.296  0.496  0.464  1.336  0.896 -0.184  1.504  0.624
    [3471]  1.304  1.456  0.936  1.256  0.904  0.856  1.624  1.096  1.296  0.904
    [3481]  1.744  1.144  0.496  0.536  0.976  0.744  0.936  1.384  0.856  1.656
    [3491]  1.736  1.144  2.176  1.536  2.136  1.136  1.264  1.184  0.976  0.296
    [3501]  1.056  0.296  0.664  1.944  0.104  0.896  2.176  0.944  0.904  0.696
    [3511]  2.096  1.904  0.944  2.176  1.304  0.384  1.776  1.096  0.344  1.064
    [3521]  1.304  1.344  1.504  0.224  1.176  1.424  1.136  1.064  0.944  0.496
    [3531]  0.856  1.256  1.096  0.656  0.304  1.744  0.256  1.176  1.176  0.496
    [3541]  0.696  0.656  0.576  1.376  0.896  0.816  1.344  0.864  0.464  1.744
    [3551]  0.336  0.416  0.536  1.216  0.856  0.456  1.424  0.664  1.336  1.176
    [3561]  1.344  0.424  0.296  0.456  1.096  0.784  1.296  0.336  1.944  1.096
    [3571]  0.536  0.816  0.264  1.016  0.264  0.416  0.304  1.504  1.336  1.296
    [3581]  1.344  0.496  1.256  1.776  0.664  0.256  0.696  0.696  1.504  1.704
    [3591]  1.064  0.464  1.256  0.656  1.096  0.576  0.584 -0.144 -0.096  1.736
    [3601]  0.664  0.336  0.296  1.744  1.136  1.104  1.344  0.704  1.496  1.336
    [3611]  1.344  1.464  0.736  1.176  0.504  1.056  0.856  0.576  0.416  1.264
    [3621]  0.584  1.344  0.904  0.464  0.256  1.376  1.704  0.744  1.216  0.736
    [3631]  0.824  1.296  1.376  0.464  1.736  1.224  1.184  0.584  0.864  0.864
    [3641]  1.304  1.096  1.424  0.104  1.504  1.056  0.696  1.744  1.096  1.504
    [3651]  1.296  0.504  1.904  1.104  1.184  1.464  0.696  0.384  0.504  1.344
    [3661]  0.056  0.264  1.504  0.376  1.104  0.664  0.704  2.096  1.616  1.496
    [3671]  0.936  1.136  0.624  0.456  1.096  1.304  1.464  1.216  0.776  1.296
    [3681]  0.376  1.296  1.056  0.976  0.304  1.624  1.344  1.624  0.584  0.736
    [3691]  0.936  1.464  1.264  1.104  1.776  0.584  1.096  0.784  1.776  1.704
    [3701]  1.504  0.896  0.656  1.624  1.024  0.944  1.376  1.184  1.416  0.784
    [3711]  1.264  0.344  1.504  1.376  0.944  0.784  0.984  0.824  2.176  1.184
    [3721]  0.896  1.304  0.416  0.016  0.776  1.456  1.064  0.856  0.496  1.056
    [3731]  1.944  0.416  0.896  0.496  0.504  1.544  1.024  1.024  1.696  0.536
    [3741]  0.736  1.496  1.576  0.304  0.376  1.064  0.544  0.936 -0.096  0.736
    [3751]  0.656  1.776  1.464  1.376  1.296  1.416  0.984  1.696  1.464  0.296
    [3761]  0.864  1.264  0.336  1.144  1.536  1.136  1.376  1.024  0.856  0.696
    [3771]  0.944  1.064  0.584  1.104  0.816  1.096  0.264  0.304  2.136  0.256
    [3781]  1.344  0.496  1.064  1.104  1.224  1.216  0.704  1.024  0.704  0.856
    [3791]  0.944  1.376  0.536  1.304  0.064 -0.184  1.104  0.464  0.776  0.664
    [3801]  1.664  1.504  0.776 -0.184  1.224  0.096  1.184  0.784  0.856  0.456
    [3811]  0.696  1.224  1.344  1.104  1.504  0.504  1.016  1.416  0.584  1.624
    [3821]  0.744  0.776  1.624  0.376  1.024  0.944  0.776  0.824  0.896  1.064
    [3831]  1.696  0.496  0.984  0.696  0.616  0.896  1.024  1.696  1.536  0.784
    [3841]  1.304  0.296  0.664  2.144  0.416  1.264  0.736  1.976  0.864  0.704
    [3851]  0.936  0.376  0.456  0.984  0.896  1.016  1.104  0.944  0.576  1.216
    [3861]  0.416  1.384  0.584  1.744  0.024  0.416  1.656  1.064  1.304  0.856
    [3871]  1.304  0.936  0.536  0.464  0.344  0.944 -0.136  0.944  1.304  1.296
    [3881]  2.184  1.936  0.416  1.696  1.176  1.304  1.904  1.064  0.944  2.184
    [3891]  1.304  1.376  0.656  1.504  0.104  1.264  0.696  0.536  1.096  0.544
    [3901]  0.464  0.784  0.504  0.936  0.984  0.456  0.784  0.296  1.456  0.304
    [3911]  1.016  0.736  1.504  1.936  1.024  0.536  0.744  0.696  0.304  0.296
    [3921]  0.416  0.544  0.944  0.024  0.384  1.256  0.656  1.784  0.216  0.936
    [3931]  0.424  1.424  0.504  1.664  1.584  0.424  0.544  0.256  1.176  1.344
    [3941]  0.536  0.896 -0.104  1.544  0.824  0.256  0.864  0.864  2.136  1.704
    [3951]  0.624  0.776  0.656  1.096  0.896  0.744  1.176  1.504  0.984  1.936
    [3961]  1.104  1.504  0.984  1.696  0.224  1.336  0.296  1.504  0.336  1.416
    [3971]  1.736  1.336  0.504  1.584  1.536  1.944  2.096  1.064  1.504  1.304
    [3981]  1.136  1.144  0.064  1.664  2.184  1.504  1.096  0.256  0.664  1.656
    [3991]  0.464  1.064  0.976  1.696  1.664  0.336  0.936  0.576  1.496  1.496
    [4001]  1.576  1.704  1.304  1.104  0.896  0.504  1.576  1.104  0.744  1.664
    [4011]  0.496  0.784  0.744  1.336  0.984  1.064 -0.176  1.584  1.504  1.216
    [4021]  0.856  0.536  0.056 -0.144  1.664  1.464  1.016  0.536  0.296  1.304
    [4031]  1.296  0.224  0.304  1.504  1.464  1.376  0.424  0.824  1.576  0.744
    [4041]  0.264  0.336  0.296  0.944  1.896  1.776  1.104  0.856  1.504  0.896
    [4051]  1.264  1.256  1.416  0.736  1.296  0.264  1.104  1.264  0.736  1.904
    [4061]  1.416  0.936  1.664  0.064  1.296  1.296  0.824  0.656  1.536  1.296
    [4071]  1.736  1.104  1.056  1.184  0.656  1.904  0.864  0.424  1.776  1.016
    [4081]  1.624  0.056  1.296  1.096  1.776  1.064  1.064  1.264  1.304  2.184
    [4091]  0.424  1.344  1.536  0.384  1.504  1.504  0.496  1.504  0.304  0.936
    [4101]  0.944  1.216  1.176  1.176  0.704  0.664  0.256  1.976  2.176  1.296
    [4111]  1.136  0.904  0.744  1.304  0.936  1.376  0.944  1.096  0.784  0.464
    [4121]  0.936  1.144  1.424  0.896  0.544  2.104  1.264  0.656  1.984  2.136
    [4131]  1.704  1.576  1.216  0.256  1.696  0.256  0.496  0.024  1.984  0.704
    [4141]  1.504  0.904  1.264  1.256  0.904  0.336  0.984  1.224  0.096  1.496
    [4151]  1.104  1.504  1.056  0.416  1.056  1.256  0.696  1.944  1.784  0.664
    [4161]  1.056  1.064  1.096  1.456  0.424  1.536  1.936  1.504  2.136  2.136
    [4171]  1.304  0.504  1.104  1.056  1.016  1.616  0.736  0.936  1.776  0.536
    [4181]  0.824  0.256  1.064  1.776  1.136  1.984  1.104  1.464  0.744  0.696
    [4191]  0.464  0.584  1.136  1.776  1.264  0.736  1.256  0.264  0.016  0.664
    [4201]  1.664  0.624  0.304  1.584  0.864  0.696  1.056  0.664  1.296  0.336
    [4211]  0.024  0.736  1.536  1.296  0.856  0.296  1.944  1.544  1.056  0.496
    [4221]  1.704  1.504  0.544  1.696 -0.096  0.496  0.976  0.544 -0.144  0.536
    [4231]  0.624  0.936  1.224  1.176  0.216  0.496  1.304  0.696  0.224  1.416
    [4241]  1.736  1.176  0.496  1.776  1.536  0.944  1.424  1.664  0.456  0.304
    [4251]  1.264  0.864  0.704  1.096  1.496  0.504  0.224  2.176  0.784  1.656
    [4261]  0.256  0.096  0.376  0.616  1.096  0.464  1.136  0.784  0.704  2.104
    [4271]  1.616  0.704  1.376  2.176  1.096  1.104  1.736  1.584  1.944  0.696
    [4281]  1.144  1.704  1.096  1.104 -0.104  1.224  1.504  0.896  1.256  1.536
    [4291]  0.824  0.616  0.456  1.344  1.536  0.336  1.584  0.624  0.656  0.736
    [4301]  1.584  1.104  0.656  1.344  1.704  0.544  1.304  1.424  0.584  1.184
    [4311]  0.456  1.096  0.496  1.056  1.096  0.856  1.736  1.744  0.224  1.784
    [4321]  1.504  1.744  0.904  0.736  0.736  1.216  1.344  1.256  1.976  0.104
    [4331] -0.176  0.456  0.904  1.104  1.504  1.016  1.776  0.736  0.936  1.256
    [4341]  1.104  1.344  1.544  1.056  1.464  0.904  1.136  1.264  1.304  0.576
    [4351]  0.256  0.576 -0.104  0.464  0.824  0.656  1.304  0.816  1.136  1.224
    [4361]  1.144  2.136  1.736  1.384  0.736  1.376  1.336  0.464  0.304  1.736
    [4371]  0.896  1.096  1.104 -0.144  0.576  0.584  0.064  1.256  1.056  0.984
    [4381]  0.344  1.456  0.664  1.104  0.576  1.264  1.656  0.024  1.464  0.984
    [4391]  0.704  0.696  1.496  0.504  0.016  0.816  1.216  0.984  0.984  0.656
    [4401]  1.544  0.856  0.704  1.336  0.296  1.256  0.496  0.264  1.376  1.616
    [4411]  0.624  0.224  1.256  0.224  0.384  1.176  1.376  0.904  1.336  0.704
    [4421]  1.344  0.936  0.944  1.136  0.304  0.624  0.576  0.624  1.376 -0.096
    [4431]  0.896  0.104  0.904  0.256  0.904  1.576  0.984  0.936  2.136  0.976
    [4441]  0.984  0.016  0.936  0.464  1.176  0.696  0.664 -0.184  0.736  0.936
    [4451]  0.656  1.624  0.384  0.464  1.224  1.056  1.696  0.864  0.656  0.016
    [4461]  1.384  0.344  0.824  1.104  0.696  0.336  0.784  1.136  1.776  0.936
    [4471]  1.136  1.784  1.136  1.224  0.744  0.664  1.096  1.504  1.096  1.696
    [4481]  1.344 -0.136  0.696  1.664  1.304  0.824  1.336  0.384  1.784  1.264
    [4491]  1.456  1.984  0.064  1.104  0.856  0.624  1.784  1.424  2.176  1.104
    [4501]  0.584  1.384  0.256  0.816  0.664  0.256  1.064  0.904  1.296  1.984
    [4511]  0.504  1.416  1.456  1.056  1.104  0.824  1.024  1.544  0.856  1.584
    [4521]  0.416  0.856  1.216  0.936  1.376  0.064  0.656  0.344  1.224  0.304
    [4531]  1.304  1.616  0.944  1.216  1.976  1.496  1.696  0.304  1.256  0.856
    [4541]  1.296  1.144  1.176  2.096 -0.184  1.696  1.024  0.576  0.896  1.296
    [4551]  0.936  0.816  0.976  0.576  0.064  1.504  1.344  0.704  1.104  1.024
    [4561]  0.656  0.664  1.896  0.896  0.496  1.464  1.976  1.416  0.944  2.104
    [4571]  0.496  1.504  0.824  0.224  0.264  1.376  0.736  0.776  0.416  0.744
    [4581]  0.024  1.256  1.344  0.776  1.936  2.096  1.296  2.104  0.264  1.376
    [4591]  1.296  1.704  1.464  1.744  0.736  1.296  1.296  1.464  1.704  1.616
    [4601]  0.904  0.504  1.096  0.664  1.184  1.256  0.944  1.016  1.176  0.864
    [4611]  0.456  0.896  1.376  0.944  1.664  0.424  0.816  1.064  0.336  1.224
    [4621] -0.096  0.216  1.616  0.216  0.536  1.936  1.096  0.376  0.296  0.704
    [4631]  1.936  0.016  1.304  1.016  1.504  1.456  1.064  0.104  0.496  1.136
    [4641]  1.176  0.976  0.976  1.504  0.456  1.184  1.304  1.136  0.456  0.656
    [4651]  1.416  1.256  0.464  1.016  0.736  2.176  1.264  0.784  0.304  1.144
    [4661]  0.624  0.904  1.544  0.616  0.664  0.784  1.096  0.744  0.976  1.304
    [4671]  0.944  1.944  0.056  1.696 -0.144 -0.136  1.496  1.336  1.736  0.744
    [4681]  1.304  1.544  1.984  0.536  0.536 -0.096  1.096  1.696  1.544  0.624
    [4691]  1.304  0.936  0.816  0.456  0.216  0.904  1.264 -0.144  1.016  1.336
    [4701]  1.424  0.304  0.664  1.504  0.576  1.736  1.096  1.976 -0.096  1.464
    [4711]  0.656  0.736  0.504  1.304  1.416  0.864  0.424  0.056  1.296  1.624
    [4721]  1.696  0.896  0.424  1.456  0.496  1.184  1.136  0.624  0.896  0.656
    [4731]  0.304  1.184  1.336  0.904  0.496  0.664  0.616  0.624  0.016  0.064
    [4741]  0.904  1.224  0.696  2.176  1.656  1.336  0.256  0.736  0.896  0.504
    [4751]  1.096  1.704  1.064  1.096  1.576  0.496  0.896  0.664  1.024  1.136
    [4761]  1.296  0.336  0.584  0.864  0.416  1.256  1.056  0.824  1.056  0.736
    [4771]  0.776  0.736  1.096  0.744  0.816  1.376  0.704  1.096  1.456  0.256
    [4781]  0.416  1.544  0.664  0.264  1.056  0.296  1.064  1.144 -0.176  2.184
    [4791]  1.224  0.824  0.704  1.016  1.016  1.296  0.896  1.064  0.736  0.816
    [4801]  1.104  2.176  0.376  0.504  1.136  1.216  1.256  0.696  1.224  0.256
    [4811]  0.256  0.296  1.704  0.416  0.744  0.904  1.064  0.984  1.064  1.776
    [4821]  1.176  0.336  1.064  1.304  1.376  0.536  1.296  2.184  0.896  0.824
    [4831]  0.504  0.856  1.064  0.704  0.696  1.696  1.504  0.344  0.464  0.864
    [4841]  0.856  1.936  0.896  1.376  0.656  1.896  0.336  1.256  0.544  1.336
    [4851]  1.744  2.176  0.424  1.584  0.896  1.344  1.304  0.296  1.224  1.736
    [4861]  0.864  0.736  1.544  1.096  0.456  0.056  1.104  1.176 -0.176  1.176
    [4871]  1.544  1.256  1.224  1.784  1.664  1.056  0.784  2.184  0.776  0.936
    [4881]  0.904  0.664  1.904  0.696  1.176  0.264  0.376  0.224  0.664  1.216
    [4891]  1.336  0.256  1.296  0.264  1.104  1.696  0.616  0.624  1.264  0.584
    [4901]  1.544  0.664  0.656  1.176  1.304  1.424  1.136  1.224  0.984  1.464
    [4911]  0.744  1.056  1.096  1.376  1.504  0.296  0.056  1.504  1.424  0.984
    [4921]  0.896  1.496  1.064  0.744  1.504  0.616  0.584  1.104  1.424  0.936
    [4931]  1.496  1.424  1.784  1.576  1.576  0.736  0.944  2.144  1.744  2.104
    [4941]  0.584  1.544  0.384  0.456  1.744  0.776  0.896  0.704  1.544  0.864
    [4951]  1.136  0.256  1.176  0.936  1.504  1.376  1.496  1.264  0.904  0.744
    [4961]  0.664  0.664  1.144  0.424  0.856  1.264  0.816  0.664  1.104  0.904
    [4971]  0.776  1.544  1.016  1.216  1.064  1.704  1.696  1.224  1.464  1.904
    [4981]  1.776  1.256  1.024  1.064  0.296  0.936  0.456  0.504  1.496  0.704
    [4991]  0.864  0.056  1.536  0.064  0.744  0.464  0.856  1.296  1.744  0.064

## Estimate Dist under HA {data-id="quarto-animate-title"}

---

[← The Null Hypothesis](02-the-null-hypothesis.md) · [Up: contents](index.md) · [Power →](04-power.md)
